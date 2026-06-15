# E2R Stock-Web v12 Residual Research — R8 loop 98 / L8 / C28

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R8
selected_loop: 98
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: AI_OFFICE_SOFTWARE_LICENSE_RETENTION_CLOUD_HOSTING_SECURITY_CONTRACT_RECURRING_REVENUE_BRIDGE_VS_ENDPOINT_SECURITY_CERTIFICATE_THEME_SPIKE
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - contract_retention_guardrail
  - recurring_revenue_margin_bridge_test
  - AI_office_license_positive_with_volatility_guard
  - endpoint_security_low_MFE_guardrail
  - digital_certificate_theme_spike_false_stage2_guard
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION` 전용 residual research다.

C28은 “AI 소프트웨어”, “오피스 SW”, “보안”, “클라우드”, “인증/identity”, “SaaS”라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 테마가 실제 계약 유지율, seat expansion, renewal, ARR/maintenance revenue, gross retention, net retention, gross margin, OPM, FCF, EPS revision으로 내려오는지다.

```text
software / security / AI office / cloud contract headline
  → renewal / seat expansion / ARR or maintenance revenue
  → gross retention / net retention / churn / contract length
  → gross margin / OPM / FCF / EPS revision bridge
  → stock-web 1D OHLC forward path
```

소프트웨어 계약은 구독 냉장고와 같다. 처음 설치되는 순간보다 중요한 것은 매달 문이 열리고, 사용자가 늘고, 해지가 줄고, 마진이 남는지다. C28은 “프로그램이 있다”와 “반복 매출이 남는다”를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["030520","079940","053800","053300"],"profile_paths":["atlas/symbol_profiles/030/030520.json","atlas/symbol_profiles/079/079940.json","atlas/symbol_profiles/053/053800.json","atlas/symbol_profiles/053/053300.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/030/030520/2024.csv","atlas/ohlcv_tradable_by_symbol_year/079/079940/2024.csv","atlas/ohlcv_tradable_by_symbol_year/053/053800/2024.csv","atlas/ohlcv_tradable_by_symbol_year/053/053300/2024.csv"],"validation_scope":"2024 trigger-level forward path; 030520 caveats are historical 2005/2006, 079940 caveats are 2006-2008, 053800 caveats are historical and outside selected 2024 window, and 053300 caveat is 2021. Selected 2024 local windows avoid active corporate-action contamination."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C28 at 27 rows, 3 rows short of the 30-row minimum stability zone.
- Existing registry shows C28 parsed through `R8 loop 97`.
- This output uses `R8 loop 98`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- Prior C28 loop 97 already covered AI software license and endpoint security false Stage2. This file separates AI office software volatile positive, cloud/hosting recurring label failure, endpoint security low-MFE path, and digital-certificate identity theme spike false Stage2.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C28-R8L98-01 | 030520 | 한글과컴퓨터 | 2024-01-08 | 2024-01-08 | 19460 | 38450 | 15090 | 97.58% | -22.46% | AI office software/license rerating worked explosively, but volatility demands retention/ARR proof. |
| C28-R8L98-02 | 079940 | 가비아 | 2024-03-13 | 2024-03-13 | 21450 | 24350 | 12300 | 13.52% | -42.66% | Cloud/hosting recurring-revenue label spiked, then decayed without visible retention/margin bridge. |
| C28-R8L98-03 | 053800 | 안랩 | 2024-01-22 | 2024-01-22 | 72500 | 75800 | 51000 | 4.55% | -29.66% | Endpoint/security label had weak MFE and persistent MAE. |
| C28-R8L98-04 | 053300 | 한국정보인증 | 2024-01-22 | 2024-01-22 | 5330 | 6050 | 3600 | 13.51% | -32.46% | Digital certificate/identity theme spike failed without contract retention and OPM bridge. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C28-R8L98-01","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AI_OFFICE_SOFTWARE_LICENSE_RETENTION_ARR_BRIDGE_VOLATILE_POSITIVE","symbol":"030520","name":"한글과컴퓨터","trigger_type":"ai_office_software_license_retention_arr_bridge_volatile_positive","trigger_date":"2024-01-08","entry_date":"2024-01-08","entry_price":19460,"peak_price":38450,"peak_date":"2024-01-22","trough_price":15090,"trough_date":"2024-01-08","mfe_pct":97.58,"mae_pct":-22.46,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_license_retention_ARR_OPM_URLs","residual_flag":"AI_office_SW_repricing_positive_but_requires_license_retention_ARR_margin_bridge","dedupe_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|030520|ai_office_software_license_retention_arr_bridge_volatile_positive|2024-01-08"}
{"row_type":"trigger","case_id":"C28-R8L98-02","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"CLOUD_HOSTING_SECURITY_CONTRACT_RECURRING_REVENUE_LABEL_HIGH_MAE","symbol":"079940","name":"가비아","trigger_type":"cloud_hosting_security_contract_recurring_revenue_label_high_mae","trigger_date":"2024-03-13","entry_date":"2024-03-13","entry_price":21450,"peak_price":24350,"peak_date":"2024-03-14","trough_price":12300,"trough_date":"2024-08-05","mfe_pct":13.52,"mae_pct":-42.66,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"cloud_hosting_recurring_label_failed_without_retention_margin_revision_bridge","dedupe_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|079940|cloud_hosting_security_contract_recurring_revenue_label_high_mae|2024-03-13"}
{"row_type":"trigger","case_id":"C28-R8L98-03","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ENDPOINT_SECURITY_CONTRACT_RETENTION_LOW_MFE_FALSE_STAGE2","symbol":"053800","name":"안랩","trigger_type":"endpoint_security_contract_retention_low_mfe_false_stage2","trigger_date":"2024-01-22","entry_date":"2024-01-22","entry_price":72500,"peak_price":75800,"peak_date":"2024-01-29","trough_price":51000,"trough_date":"2024-09-20","mfe_pct":4.55,"mae_pct":-29.66,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"endpoint_security_label_low_MFE_without_renewal_retention_OPM_bridge","dedupe_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|053800|endpoint_security_contract_retention_low_mfe_false_stage2|2024-01-22"}
{"row_type":"trigger","case_id":"C28-R8L98-04","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"DIGITAL_CERTIFICATE_IDENTITY_THEME_SPIKE_FALSE_STAGE2","symbol":"053300","name":"한국정보인증","trigger_type":"digital_certificate_identity_theme_spike_false_stage2","trigger_date":"2024-01-22","entry_date":"2024-01-22","entry_price":5330,"peak_price":6050,"peak_date":"2024-01-22","trough_price":3600,"trough_date":"2024-08-05","mfe_pct":13.51,"mae_pct":-32.46,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"certificate_identity_spike_decayed_without_contract_retention_margin_bridge","dedupe_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|053300|digital_certificate_identity_theme_spike_false_stage2|2024-01-22"}
```

## 6. Score-return alignment

### 6.1 AI office SW can reprice, but C28 still needs retention

`030520` is the constructive row in this sample. The forward price path shows that AI office software and license optionality can create large MFE. But the same row has double-digit MAE, so the model should not hand out automatic Green without license conversion, paid-seat retention, ARR/maintenance revenue and OPM bridge.

### 6.2 Cloud/hosting and security labels are not enough

`079940` and `053800` are caution rows. Both have plausible recurring or contract-like vocabulary, yet the forward path did not confirm durable rerating. C28 needs gross retention, renewal rate, churn, contract length, gross margin and OPM evidence before promotion.

### 6.3 Certificate/identity theme spike false Stage2

`053300` is the small-cap theme-spike row. Digital certificate and identity vocabulary can spike quickly, but without contract retention and margin bridge, the later drawdown dominates. This is a local 4B or false Stage2 case.

## 7. Raw component score simulation

| symbol | SW/security specificity | retention/renewal evidence | ARR/maintenance bridge | OPM/FCF bridge | price confirmation | MAE/theme guard | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 030520 | 22 | 10 | 10 | 8 | 24 | -10 | 64 | Stage3-Yellow candidate with volatility guard |
| 079940 | 17 | 7 | 8 | 5 | 6 | -18 | 25 | Stage2/local 4B |
| 053800 | 18 | 8 | 6 | 5 | 2 | -13 | 26 | Stage2/local 4B |
| 053300 | 14 | 5 | 4 | 3 | 6 | -14 | 18 | Local 4B / false Stage2 |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c28_SW_security_requires_retention_ARR_OPM_bridge","scope":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","candidate_action":"stage2_required_bridge","rule":"Do not promote software/security/AI-office/cloud/identity labels above Stage2 unless renewal, paid-seat expansion, ARR, maintenance revenue, gross retention, net retention, churn, contract length, gross margin, OPM, FCF, or EPS revision bridge is visible.","supporting_cases":["079940","053800","053300"],"counterbalanced_by":["030520"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c28_AI_office_SW_positive_but_volatile_delta","scope":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","candidate_action":"stage3_yellow_candidate_with_volatility_guard","rule":"AI office software rows can receive Yellow treatment when price confirmation is strong, but Green requires URL-verified paid-license retention, ARR and margin evidence.","supporting_cases":["030520"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c28_endpoint_security_low_MFE_guard","scope":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","candidate_action":"local_4b_watch_guard","rule":"Endpoint/security rows with low MFE and meaningful MAE should remain local 4B unless renewal and margin evidence repairs the row.","supporting_cases":["053800"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c28_certificate_identity_theme_spike_false_stage2_guard","scope":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","candidate_action":"local_4b_or_false_stage2_guard","rule":"Digital certificate/identity theme spikes should not be promoted when contract retention and OPM bridge are absent and later MAE dominates.","supporting_cases":["053300"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c28_cloud_hosting_recurring_label_high_MAE_guard","scope":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","candidate_action":"stage2_or_local_4b_watch","rule":"Cloud/hosting recurring-revenue labels require retention and OPM evidence; high MAE blocks Green even when the business model sounds recurring.","supporting_cases":["079940"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","round":"R8","loop":"98","positive_rows":1,"counterexample_rows":3,"new_symbol_count":4,"primary_residual":"C28 should separate volatile AI office software repricing from cloud/security/certificate labels that fail without retention, ARR, maintenance revenue and OPM bridge.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_candidate_with_volatility_guard","local_4b_watch_guard","local_4b_or_false_stage2_guard","stage2_or_local_4b_watch"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","sample_count":4,"avg_mfe_pct":32.29,"avg_mae_pct":-31.81,"median_mfe_pct":13.52,"median_mae_pct":-31.06,"interpretation":"C28 can create sharp upside in AI office software, but most security/cloud/certificate labels need strict retention and OPM guardrails because recurring-revenue vocabulary alone produced poor asymmetry."}
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
- Ingest this C28 R8 loop 98 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c28_SW_security_requires_retention_ARR_OPM_bridge -> stage2_required_bridge
  2. c28_AI_office_SW_positive_but_volatile_delta -> stage3_yellow_candidate_with_volatility_guard
  3. c28_endpoint_security_low_MFE_guard -> local_4b_watch_guard
  4. c28_certificate_identity_theme_spike_false_stage2_guard -> local_4b_or_false_stage2_guard
  5. c28_cloud_hosting_recurring_label_high_MAE_guard -> stage2_or_local_4b_watch

Expected behavior:
- Software/security/AI-office/cloud/identity vocabulary alone should not create Green.
- Renewal, paid-seat expansion, ARR, maintenance revenue, gross retention, net retention, churn, contract length, OPM, FCF, or EPS revision can justify Stage3-Yellow.
- Endpoint security, certificate identity, and cloud-hosting labels with low MFE/high MAE should remain capped until non-price evidence repairs the row.
```
