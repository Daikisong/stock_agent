# E2R Stock-Web v12 Residual Research — R7 loop 98 / L7 / C25

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R7
selected_loop: 98
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_DEVICE_INSTALLED_BASE_CONSUMABLE_EXPORT_MARGIN_BRIDGE_VS_DENTAL_CGM_DIGITAL_DENTAL_EXPORT_REIMBURSEMENT_FALSE_STAGE2
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - reimbursement_export_guardrail
  - installed_base_consumable_margin_bridge_test
  - dental_export_channel_false_stage2_guard
  - CGM_reimbursement_event_cap_guard
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

C25는 “의료기기 수출”, “해외 인허가”, “보험/reimbursement”, “소모품 반복 매출”, “미용기기/치과/진단기기”라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 장비가 실제 설치 기반으로 쌓이고, consumable/reorder/reimbursement/channel access가 반복 매출과 margin/FCF/revision으로 내려오는지다.

```text
medical device export / reimbursement headline
  → installed base / channel access / reimbursement status
  → consumable reorder / utilization / distributor sell-through
  → gross margin / OPM / FCF / EPS revision bridge
  → stock-web 1D OHLC forward path
```

의료기기는 병원에 들어간 장비가 끝이 아니다. 진짜 돈은 장비가 계속 쓰이고, 소모품·시술·보험 정산이 반복될 때 흐른다. C25는 “장비가 팔렸다”와 “장비가 반복 매출을 만든다”를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["214150","145720","099190","043150","228670"],"profile_paths":["atlas/symbol_profiles/214/214150.json","atlas/symbol_profiles/145/145720.json","atlas/symbol_profiles/099/099190.json","atlas/symbol_profiles/043/043150.json","atlas/symbol_profiles/228/228670.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/214/214150/2024.csv","atlas/ohlcv_tradable_by_symbol_year/145/145720/2024.csv","atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv","atlas/ohlcv_tradable_by_symbol_year/043/043150/2024.csv","atlas/ohlcv_tradable_by_symbol_year/228/228670/2024.csv"],"validation_scope":"2024 trigger-level forward path; 214150 caveat is 2017, 145720 has zero corporate-action candidates, 099190 caveats are 2015/2023, 043150 caveat is 2010, 228670 caveats are 2021; all are outside selected 2024 local windows."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 1 lists C25 at 33 rows, 17 rows short of the 50-row practical calibration zone.
- Existing registry shows C25 parsed through `R7 loop 97`.
- This output uses `R7 loop 98`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- Prior C25 rows already touched broad aesthetic/body-composition/dental labels. This file compresses an installed-base/consumable positive anchor with dental implant, CGM/reimbursement, dental imaging, and digital dental export false-Stage2 paths.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C25-R7L98-01 | 214150 | 클래시스 | 2024-03-14 | 2024-03-14 | 34450 | 62900 | 33100 | 82.58% | -3.92% | Aesthetic installed-base/consumable export path worked strongly with controlled MAE. |
| C25-R7L98-02 | 145720 | 덴티움 | 2024-02-29 | 2024-02-29 | 144200 | 148500 | 68200 | 2.98% | -52.70% | Dental implant export/channel label failed without reorder and reimbursement/cash bridge. |
| C25-R7L98-03 | 099190 | 아이센스 | 2024-01-10 | 2024-01-10 | 29500 | 30400 | 14520 | 3.05% | -50.78% | CGM/reimbursement optionality became high-MAE false Stage2 when conversion proof lagged. |
| C25-R7L98-04 | 043150 | 바텍 | 2024-01-02 | 2024-01-02 | 33300 | 33750 | 22550 | 1.35% | -32.28% | Dental imaging export label produced tiny MFE and persistent MAE. |
| C25-R7L98-05 | 228670 | 레이 | 2024-03-12 | 2024-03-12 | 16870 | 17680 | 7600 | 4.80% | -54.95% | Digital dental device/export label decayed without channel utilization and margin bridge. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C25-R7L98-01","round":"R7","loop":"98","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_INSTALLED_BASE_CONSUMABLE_EXPORT_MARGIN_BRIDGE","symbol":"214150","name":"클래시스","trigger_type":"aesthetic_device_installed_base_consumable_export_margin_bridge","trigger_date":"2024-03-14","entry_date":"2024-03-14","entry_price":34450,"peak_price":62900,"peak_date":"2024-10-21","trough_price":33100,"trough_date":"2024-03-15","mfe_pct":82.58,"mae_pct":-3.92,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_installed_base_consumable_URLs","residual_flag":"strong_positive_but_requires_installed_base_consumable_OPM_URLs_before_production_Green","dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|214150|aesthetic_device_installed_base_consumable_export_margin_bridge|2024-03-14"}
{"row_type":"trigger","case_id":"C25-R7L98-02","round":"R7","loop":"98","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_IMPLANT_EXPORT_CHANNEL_REORDER_REIMBURSEMENT_FALSE_STAGE2","symbol":"145720","name":"덴티움","trigger_type":"dental_implant_export_channel_reorder_reimbursement_false_stage2","trigger_date":"2024-02-29","entry_date":"2024-02-29","entry_price":144200,"peak_price":148500,"peak_date":"2024-03-06","trough_price":68200,"trough_date":"2024-11-01","mfe_pct":2.98,"mae_pct":-52.70,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_local_4B_watch","residual_flag":"dental_export_label_failed_without_channel_reorder_reimbursement_margin_bridge","dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|145720|dental_implant_export_channel_reorder_reimbursement_false_stage2|2024-02-29"}
{"row_type":"trigger","case_id":"C25-R7L98-03","round":"R7","loop":"98","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"CGM_REIMBURSEMENT_OPTIONALITY_HIGH_MAE_FALSE_STAGE2","symbol":"099190","name":"아이센스","trigger_type":"cgm_reimbursement_optionality_high_mae_false_stage2","trigger_date":"2024-01-10","entry_date":"2024-01-10","entry_price":29500,"peak_price":30400,"peak_date":"2024-01-12","trough_price":14520,"trough_date":"2024-09-09","mfe_pct":3.05,"mae_pct":-50.78,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Event-cap_or_4C_watch_until_reimbursement_revenue_bridge","residual_flag":"CGM_reimbursement_label_without_revenue_margin_conversion_became_high_MAE","dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|099190|cgm_reimbursement_optionality_high_mae_false_stage2|2024-01-10"}
{"row_type":"trigger","case_id":"C25-R7L98-04","round":"R7","loop":"98","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_IMAGING_EXPORT_WEAK_MFE_HIGH_MAE","symbol":"043150","name":"바텍","trigger_type":"dental_imaging_export_weak_mfe_high_mae","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":33300,"peak_price":33750,"peak_date":"2024-01-02","trough_price":22550,"trough_date":"2024-11-01","mfe_pct":1.35,"mae_pct":-32.28,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"dental_imaging_export_label_needs_reorder_margin_reimbursement_bridge","dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|043150|dental_imaging_export_weak_mfe_high_mae|2024-01-02"}
{"row_type":"trigger","case_id":"C25-R7L98-05","round":"R7","loop":"98","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DIGITAL_DENTAL_DEVICE_EXPORT_CHANNEL_DECAY_HIGH_MAE","symbol":"228670","name":"레이","trigger_type":"digital_dental_device_export_channel_decay_high_mae","trigger_date":"2024-03-12","entry_date":"2024-03-12","entry_price":16870,"peak_price":17680,"peak_date":"2024-03-19","trough_price":7600,"trough_date":"2024-09-10","mfe_pct":4.80,"mae_pct":-54.95,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_4C_watch","residual_flag":"digital_dental_device_export_label_failed_without_utilization_channel_margin_bridge","dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|228670|digital_dental_device_export_channel_decay_high_mae|2024-03-12"}
```

## 6. Score-return alignment

### 6.1 Installed-base / consumable winner

`214150` is the constructive C25 row. The forward path shows how a medical aesthetic device can be scored differently when the market sees installed base, recurring procedure demand, consumable/reorder economics, and OPM expansion. It can be a Stage3-Yellow/Green candidate after exact URL verification.

### 6.2 Dental export false-stage family

`145720`, `043150`, and `228670` show the dangerous side of C25. Dental implant, dental imaging, and digital dental exports are all plausible medical-device stories, but the price paths show that export vocabulary alone is not enough. Without channel sell-through, reorder, reimbursement/access, and margin proof, these rows become severe high-MAE false Stage2 paths.

### 6.3 CGM / reimbursement event-cap

`099190` is a reimbursement optionality warning. CGM or wearable glucose monitoring vocabulary can sound like recurring medical-device revenue, but if reimbursement and real revenue conversion lag, the row should remain event-cap or 4C watch rather than persistent Yellow.

## 7. Raw component score simulation

| symbol | device/export evidence | installed base / utilization | consumable/reorder | reimbursement/channel access | margin/FCF bridge | price confirmation | MAE guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 214150 | 23 | 22 | 20 | 13 | 18 | 23 | -2 | 87 | Stage3-Yellow/Green candidate |
| 145720 | 16 | 6 | 5 | 4 | 4 | 1 | -24 | 12 | Hard counterexample/local 4B |
| 099190 | 17 | 6 | 4 | 7 | 3 | 2 | -23 | 16 | Event-cap / 4C watch |
| 043150 | 14 | 5 | 4 | 4 | 3 | 1 | -15 | 16 | Stage2/local 4B |
| 228670 | 13 | 4 | 3 | 3 | 2 | 2 | -25 | 2 | Hard counterexample / 4C watch |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c25_device_export_requires_installed_base_reorder_reimbursement_margin_bridge","scope":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","candidate_action":"stage2_required_bridge","rule":"Do not promote medical-device export/reimbursement labels above Stage2 unless installed base, utilization, consumable reorder, channel access, reimbursement, gross margin, OPM, FCF, or EPS revision bridge is visible.","supporting_cases":["145720","099190","043150","228670"],"counterbalanced_by":["214150"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c25_aesthetic_installed_base_positive_delta","scope":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"Medical aesthetic device names with verified installed base, repeat procedure demand, consumable/reorder economics, and OPM bridge can receive stronger Stage3-Yellow/Green candidate treatment.","supporting_cases":["214150"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c25_dental_export_false_stage2_guard","scope":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","candidate_action":"local_4b_watch_guard","rule":"Dental implant, imaging, or digital dental export labels with tiny MFE and severe MAE should remain local 4B or hard counterexample until reorder/channel/margin evidence repairs the thesis.","supporting_cases":["145720","043150","228670"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c25_reimbursement_optionality_event_cap_guard","scope":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","candidate_action":"event_cap_or_4c_watch","rule":"CGM/reimbursement optionality should not be scored as recurring device revenue unless reimbursement, adoption, and revenue conversion are verified; severe MAE triggers event-cap or 4C watch.","supporting_cases":["099190"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","round":"R7","loop":"98","positive_rows":1,"counterexample_rows":4,"new_symbol_count":5,"primary_residual":"C25 should separate installed-base/consumable medical-device winners from dental export, CGM reimbursement, and digital dental labels that fail without reorder, utilization, reimbursement, and margin bridge.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_to_green_candidate_delta","local_4b_watch_guard","event_cap_or_4c_watch"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","sample_count":5,"avg_mfe_pct":18.95,"avg_mae_pct":-38.93,"median_mfe_pct":3.05,"median_mae_pct":-50.78,"interpretation":"C25 upside is concentrated in verified installed-base/consumable models; export/reimbursement vocabulary without repeat revenue conversion creates severe high-MAE false Stage2 paths."}
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
  - selected local windows avoid active corporate-action contamination
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
  1. c25_device_export_requires_installed_base_reorder_reimbursement_margin_bridge -> stage2_required_bridge
  2. c25_aesthetic_installed_base_positive_delta -> stage3_yellow_to_green_candidate_delta
  3. c25_dental_export_false_stage2_guard -> local_4b_watch_guard
  4. c25_reimbursement_optionality_event_cap_guard -> event_cap_or_4c_watch

Expected behavior:
- Medical-device export/reimbursement vocabulary alone should not create Green.
- Installed base, utilization, consumable reorder, channel access, reimbursement, gross margin, OPM, FCF, or EPS revision can justify Stage3-Yellow.
- Dental export and CGM/reimbursement labels should be capped when MFE is tiny and MAE is severe.
```
