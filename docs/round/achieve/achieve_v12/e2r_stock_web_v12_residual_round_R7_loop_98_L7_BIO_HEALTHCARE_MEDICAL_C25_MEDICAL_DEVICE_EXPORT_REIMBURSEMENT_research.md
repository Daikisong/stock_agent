# E2R Stock-Web v12 Residual Research — R7 loop 98 / L7 / C25

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R7
selected_loop: 98
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_INSTALLED_BASE_CONSUMABLE_MARGIN_BRIDGE_VS_DEVICE_LABEL_HIGH_MAE_FALSE_STAGE2
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - reimbursement_export_guardrail
  - installed_base_consumable_margin_bridge_test
  - high_MAE_guardrail
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT` 전용 residual research다.

C25는 “의료기기”, “수출”, “FDA/CE/인허가”, “reimbursement”라는 단어를 곧바로 Stage3-Green으로 올리는 bucket이 아니다. 의료기기는 약보다 덜 binary해 보이지만, 실제 투자 경로는 설치 기반·소모품·보험수가·의사 채택·채널 재주문이 연결될 때만 반복 수익 구조가 된다.

```text
medical device / export / reimbursement headline
  → installed base / clinician adoption / distributor depth
  → consumable reorder / reimbursement coverage / procedure volume
  → gross margin / OPM / EPS revision bridge
  → stock-web 1D OHLC forward path
```

기계 한 대를 판 것은 문을 연 것이다. 소모품·시술량·reimbursement가 반복되는 순간부터 병원 복도에 불이 계속 켜진다. C25는 이 “한 번 판 기계”와 “반복 매출 엔진”을 분리해야 한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["214150","290650","099190","145720","228670"],"profile_paths":["atlas/symbol_profiles/214/214150.json","atlas/symbol_profiles/290/290650.json","atlas/symbol_profiles/099/099190.json","atlas/symbol_profiles/145/145720.json","atlas/symbol_profiles/228/228670.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/214/214150/2024.csv","atlas/ohlcv_tradable_by_symbol_year/290/290650/2024.csv","atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv","atlas/ohlcv_tradable_by_symbol_year/145/145720/2024.csv","atlas/ohlcv_tradable_by_symbol_year/228/228670/2024.csv"],"validation_scope":"2024 trigger-level forward path; historical corporate-action profile caveats outside local 2024 windows are treated as profile caveats, not local row rejection."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 1 lists C25 at 33 rows and asks for medical-device export, reimbursement, and recurring consumable revenue expansion.
- Existing registry shows C25 latest parsed file at `R7 loop 97`.
- This output uses `R7 loop 98`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file emphasizes installed-base/consumable margin bridges versus reimbursement/channel label false positives.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C25-R7L98-01 | 214150 | 클래시스 | 2024-06-12 | 2024-06-12 | 53800 | 62900 | 41050 | 16.91% | -23.70% | Aesthetic device installed-base/consumable ramp had MFE, but deep MAE blocks automatic Green. |
| C25-R7L98-02 | 290650 | 엘앤씨바이오 | 2024-06-12 | 2024-06-12 | 21650 | 25800 | 16480 | 19.17% | -23.88% | Tissue/implant optionality produced MFE, but reimbursement/procedure bridge was not enough for Green. |
| C25-R7L98-03 | 099190 | 아이센스 | 2024-06-05 | 2024-06-05 | 19560 | 22850 | 14520 | 16.82% | -25.77% | CGM/diabetes device label produced tradeable spike but high-MAE false Stage2 risk. |
| C25-R7L98-04 | 145720 | 덴티움 | 2024-05-10 | 2024-05-10 | 120300 | 125500 | 57500 | 4.32% | -52.20% | Dental implant export/reimbursement vocabulary failed badly without channel/revision bridge. |
| C25-R7L98-05 | 228670 | 레이 | 2024-06-10 | 2024-06-10 | 11120 | 13800 | 7600 | 24.10% | -31.65% | Digital dentistry/X-ray optionality had MFE, but later drawdown says device label alone is not enough. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C25-R7L98-01","round":"R7","loop":"98","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_INSTALLED_BASE_CONSUMABLE_RAMP_HIGH_MAE","symbol":"214150","name":"클래시스","trigger_type":"aesthetic_device_installed_base_consumable_ramp_second_leg","trigger_date":"2024-06-12","entry_date":"2024-06-12","entry_price":53800,"peak_price":62900,"peak_date":"2024-10-21","trough_price":41050,"trough_date":"2024-08-05","mfe_pct":16.91,"mae_pct":-23.70,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_with_high_MAE_guardrail","residual_flag":"positive_device_installed_base_path_but_consumable_margin_bridge_required_before_Green","dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|214150|aesthetic_device_installed_base_consumable_ramp_second_leg|2024-06-12"}
{"row_type":"trigger","case_id":"C25-R7L98-02","round":"R7","loop":"98","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"TISSUE_IMPLANT_PROCEDURE_REIMBURSEMENT_OPTIONALITY_HIGH_MAE","symbol":"290650","name":"엘앤씨바이오","trigger_type":"tissue_implant_procedure_reimbursement_optionality","trigger_date":"2024-06-12","entry_date":"2024-06-12","entry_price":21650,"peak_price":25800,"peak_date":"2024-07-05","trough_price":16480,"trough_date":"2024-08-05","mfe_pct":19.17,"mae_pct":-23.88,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_high_MAE_guardrail","residual_flag":"procedure_volume_and_reimbursement_bridge_required","dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|290650|tissue_implant_procedure_reimbursement_optionality|2024-06-12"}
{"row_type":"trigger","case_id":"C25-R7L98-03","round":"R7","loop":"98","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"CGM_DIABETES_DEVICE_REIMBURSEMENT_LABEL_HIGH_MAE_FALSE_STAGE2","symbol":"099190","name":"아이센스","trigger_type":"cgm_diabetes_device_reimbursement_label_high_mae","trigger_date":"2024-06-05","entry_date":"2024-06-05","entry_price":19560,"peak_price":22850,"peak_date":"2024-07-10","trough_price":14520,"trough_date":"2024-09-09","mfe_pct":16.82,"mae_pct":-25.77,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"counterexample_device_label_without_reimbursement_adoption_margin_bridge","dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|099190|cgm_diabetes_device_reimbursement_label_high_mae|2024-06-05"}
{"row_type":"trigger","case_id":"C25-R7L98-04","round":"R7","loop":"98","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_IMPLANT_EXPORT_REIMBURSEMENT_CHANNEL_BREAK_COUNTEREXAMPLE","symbol":"145720","name":"덴티움","trigger_type":"dental_implant_export_reimbursement_channel_break","trigger_date":"2024-05-10","entry_date":"2024-05-10","entry_price":120300,"peak_price":125500,"peak_date":"2024-05-14","trough_price":57500,"trough_date":"2024-11-12","mfe_pct":4.32,"mae_pct":-52.20,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_4C_watch","residual_flag":"dental_implant_export_label_failed_without_channel_revision_bridge","dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|145720|dental_implant_export_reimbursement_channel_break|2024-05-10"}
{"row_type":"trigger","case_id":"C25-R7L98-05","round":"R7","loop":"98","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DIGITAL_DENTISTRY_XRAY_DEVICE_OPTIONALITY_HIGH_MAE","symbol":"228670","name":"레이","trigger_type":"digital_dentistry_xray_device_optionality_high_mae","trigger_date":"2024-06-10","entry_date":"2024-06-10","entry_price":11120,"peak_price":13800,"peak_date":"2024-07-04","trough_price":7600,"trough_date":"2024-09-10","mfe_pct":24.10,"mae_pct":-31.65,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_event_cap_with_high_MAE_guardrail","residual_flag":"device_optionality_spike_decayed_without_channel_reimbursement_bridge","dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|228670|digital_dentistry_xray_device_optionality_high_mae|2024-06-10"}
```

## 6. Score-return alignment

### 6.1 Installed-base positive path with drawdown risk

`214150` is the constructive case, but not clean enough for automatic Green. The device installed-base/consumable story produced MFE, yet the stock still went through a deep August drawdown. This suggests the model should treat aesthetic-device export as Stage3-Yellow candidate only when consumable repeat revenue and margin bridge are visible.

### 6.2 Procedure/reimbursement optionality with weak durability

`290650` and `099190` show the middle failure family. They can generate short MFE when the market recognizes medical device/procedure or diabetes-device optionality, but reimbursement coverage, procedure volume, and margin/revision bridge must be proven. Otherwise they behave like high-MAE Stage2 false positives.

### 6.3 Dental device counterexample family

`145720` and `228670` are the stronger counterexamples. Dental implant/digital dentistry labels can look like export/reimbursement devices, but if channel demand and EPS revision break, the forward path becomes dominated by MAE. `145720` especially argues for hard 4C watch when channel/revision breaks after the device label has already been priced.

## 7. Raw component score simulation

| symbol | export/reimbursement evidence | installed-base/consumable bridge | procedure/channel depth | margin/revision bridge | price confirmation | MAE guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 214150 | 21 | 19 | 16 | 13 | 15 | -10 | 74 | Stage3-Yellow candidate |
| 290650 | 17 | 10 | 12 | 7 | 13 | -10 | 49 | Stage2/Yellow with guardrail |
| 099190 | 16 | 11 | 9 | 6 | 10 | -11 | 41 | Stage2/local 4B watch |
| 145720 | 16 | 7 | 5 | 2 | 2 | -20 | 12 | Hard counterexample / 4C watch |
| 228670 | 15 | 8 | 8 | 4 | 12 | -14 | 33 | Event-cap / high-MAE false Stage2 |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c25_device_export_requires_installed_base_consumable_reimbursement_bridge","scope":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","candidate_action":"stage2_required_bridge","rule":"Do not promote medical-device export or reimbursement labels above Stage2 unless installed base, clinician adoption, reimbursement coverage, procedure volume, consumable reorder, margin, or EPS revision bridge is visible.","supporting_cases":["099190","145720","228670"],"counterbalanced_by":["214150","290650"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c25_high_mae_device_label_guardrail","scope":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","candidate_action":"local_4b_watch_guard","rule":"If device-label MFE is paired with deep MAE and no verified reimbursement/consumable bridge, cap at local 4B watch or event-cap.","supporting_cases":["290650","099190","228670"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c25_channel_revision_break_hard_counterexample","scope":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","candidate_action":"hard_4c_watch","rule":"If dental/medical-device export vocabulary is followed by channel demand or EPS revision break and MAE dominates MFE, mark as hard counterexample / 4C watch rather than Stage2 persistence.","supporting_cases":["145720"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c25_installed_base_consumable_positive_delta","scope":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","candidate_action":"stage3_yellow_candidate_delta","rule":"Installed-base device names with recurring consumable revenue and verified margin bridge can receive stronger Stage3-Yellow treatment; Green requires drawdown containment and URL-verified non-price evidence.","supporting_cases":["214150"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","round":"R7","loop":"98","positive_rows":2,"counterexample_rows":3,"new_symbol_count":5,"primary_residual":"C25 needs sharper separation between medical-device export/reimbursement labels and actual installed-base, consumable, procedure-volume, margin/revision bridges.","candidate_patch_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_watch","stage3_yellow_candidate_delta"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","sample_count":5,"avg_mfe_pct":16.26,"avg_mae_pct":-31.44,"median_mfe_pct":16.91,"median_mae_pct":-25.77,"interpretation":"C25 device labels can create MFE, but drawdown is severe unless recurring consumable/reimbursement/channel margin bridge is real."}
```

## 10. Validation flags

```text
usable_for_ledger: true
usable_for_production_patch: false
reason_not_promotion_ready:
  - source_proxy_only=true
  - evidence_url_pending=true
  - non-price exact URLs must be verified before applying weight deltas
  - local 2024 OHLC rows were checked from stock-web tradable shards
  - corporate-action profile caveats, where present, are outside the local 2024 trigger windows used here
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research session.

Goal:
- Ingest this C25 R7 loop 98 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c25_device_export_requires_installed_base_consumable_reimbursement_bridge -> stage2_required_bridge
  2. c25_high_mae_device_label_guardrail -> local_4b_watch_guard
  3. c25_channel_revision_break_hard_counterexample -> hard_4c_watch
  4. c25_installed_base_consumable_positive_delta -> stage3_yellow_candidate_delta

Expected behavior:
- Medical-device export/reimbursement vocabulary alone should not create Green.
- Installed base, clinician adoption, procedure volume, reimbursement coverage, consumable reorder, margin, or EPS revision can justify Stage3-Yellow.
- Dental/device labels followed by channel/revision break should become hard counterexample / 4C watch.
- High-MAE device optionality should be capped at event-cap/local 4B watch until non-price bridge is verified.
```
