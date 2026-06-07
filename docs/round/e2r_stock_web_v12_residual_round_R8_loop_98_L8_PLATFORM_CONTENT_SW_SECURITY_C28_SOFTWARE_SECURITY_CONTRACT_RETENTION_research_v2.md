# E2R Stock-Web v12 Residual Research — R8 loop 98 / L8 / C28

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R8
selected_loop: 98
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: ERP_OFFICE_SECURITY_LICENSE_CONTRACT_RETENTION_MARGIN_BRIDGE_VS_AI_SOFTWARE_SECURITY_THEME_HIGH_MAE_FALSE_STAGE2
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - contract_retention_guardrail
  - recurring_revenue_margin_bridge_test
  - theme_beta_false_stage2_guard
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

이번 파일은 `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION` 전용 residual research다.

C28은 “AI 소프트웨어”, “보안”, “ERP”, “오피스”, “클라우드”, “망분리/제로트러스트” 같은 단어만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 소프트웨어/보안 제품이 실제 계약 유지율, 갱신, 좌석 수 확장, 유지보수 매출, ARR/recurring revenue, OPM/revision으로 이어지는지다.

```text
software / security / ERP / office AI headline
  → contract renewal / retention / seat expansion
  → recurring maintenance / ARR / cloud conversion
  → margin / OPM / EPS revision bridge
  → stock-web 1D OHLC forward path
```

소프트웨어 계약은 임대료와 같다. 첫 계약은 열쇠를 건네는 장면이고, retention은 매달 월세가 밀리지 않고 들어오는 장면이다. C28은 “문을 열었다”와 “월세가 반복된다”를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["012510","030520","053800","263860"],"profile_paths":["atlas/symbol_profiles/012/012510.json","atlas/symbol_profiles/030/030520.json","atlas/symbol_profiles/053/053800.json","atlas/symbol_profiles/263/263860.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv","atlas/ohlcv_tradable_by_symbol_year/030/030520/2024.csv","atlas/ohlcv_tradable_by_symbol_year/053/053800/2024.csv","atlas/ohlcv_tradable_by_symbol_year/263/263860/2024.csv"],"validation_scope":"2024 trigger-level forward path; profile corporate-action caveats for selected names are old historical caveats outside the selected 2024 trigger windows."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C28 at 27 rows, 3 rows short of the 30-row minimum stability zone.
- Existing registry shows C28 parsed through `R8 loop 97`.
- This output uses `R8 loop 98`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file separates ERP/cloud recurring software from AI office theme, endpoint/security theme, and NAC/EDR retention weakness.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C28-R8L98-01 | 012510 | 더존비즈온 | 2024-04-04 | 2024-04-04 | 53300 | 78300 | 44900 | 46.90% | -15.76% | ERP/cloud/AI software rerating worked, but retention and OPM bridge are needed before Green. |
| C28-R8L98-02 | 030520 | 한글과컴퓨터 | 2024-01-10 | 2024-01-10 | 24750 | 38450 | 15100 | 55.35% | -38.99% | AI office/document software theme had huge MFE but later severe drawdown; high-MAE guardrail. |
| C28-R8L98-03 | 053800 | 안랩 | 2024-04-11 | 2024-04-11 | 64800 | 75600 | 50700 | 16.67% | -21.76% | Cybersecurity theme spike was tradable but decayed without recurring contract/margin proof. |
| C28-R8L98-04 | 263860 | 지니언스 | 2024-01-22 | 2024-01-22 | 14750 | 16000 | 8310 | 8.47% | -43.66% | NAC/EDR security label failed badly; retention and ARR bridge absent. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C28-R8L98-01","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ERP_CLOUD_AI_SOFTWARE_CONTRACT_RETENTION_OPM_BRIDGE","symbol":"012510","name":"더존비즈온","trigger_type":"erp_cloud_ai_software_contract_retention_opm_bridge","trigger_date":"2024-04-04","entry_date":"2024-04-04","entry_price":53300,"peak_price":78300,"peak_date":"2024-07-08","trough_price":44900,"trough_date":"2024-10-10","mfe_pct":46.90,"mae_pct":-15.76,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_retention_OPM_URLs","residual_flag":"positive_ERP_cloud_software_rerating_but_retention_margin_bridge_required","dedupe_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|012510|erp_cloud_ai_software_contract_retention_opm_bridge|2024-04-04"}
{"row_type":"trigger","case_id":"C28-R8L98-02","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AI_OFFICE_DOCUMENT_SOFTWARE_THEME_HIGH_MAE_GUARD","symbol":"030520","name":"한글과컴퓨터","trigger_type":"ai_office_document_software_theme_high_mae_guard","trigger_date":"2024-01-10","entry_date":"2024-01-10","entry_price":24750,"peak_price":38450,"peak_date":"2024-01-22","trough_price":15100,"trough_date":"2024-08-05","mfe_pct":55.35,"mae_pct":-38.99,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_high_MAE_guardrail","residual_flag":"AI_office_label_made_large_MFE_but_failed_retention_margin_durability","dedupe_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|030520|ai_office_document_software_theme_high_mae_guard|2024-01-10"}
{"row_type":"trigger","case_id":"C28-R8L98-03","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"CYBERSECURITY_THEME_SPIKE_WITHOUT_RECURRING_RETENTION_BRIDGE","symbol":"053800","name":"안랩","trigger_type":"cybersecurity_theme_spike_without_recurring_retention_bridge","trigger_date":"2024-04-11","entry_date":"2024-04-11","entry_price":64800,"peak_price":75600,"peak_date":"2024-04-12","trough_price":50700,"trough_date":"2024-09-23","mfe_pct":16.67,"mae_pct":-21.76,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"security_label_event_spike_decayed_without_contract_retention_margin_bridge","dedupe_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|053800|cybersecurity_theme_spike_without_recurring_retention_bridge|2024-04-11"}
{"row_type":"trigger","case_id":"C28-R8L98-04","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"NAC_EDR_SECURITY_RETENTION_WEAKNESS_HIGH_MAE_FALSE_STAGE2","symbol":"263860","name":"지니언스","trigger_type":"nac_edr_security_retention_weakness_high_mae_false_stage2","trigger_date":"2024-01-22","entry_date":"2024-01-22","entry_price":14750,"peak_price":16000,"peak_date":"2024-01-29","trough_price":8310,"trough_date":"2024-07-19","mfe_pct":8.47,"mae_pct":-43.66,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_4C_watch","residual_flag":"security_contract_label_failed_without_ARR_retention_margin_bridge","dedupe_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|263860|nac_edr_security_retention_weakness_high_mae_false_stage2|2024-01-22"}
```

## 6. Score-return alignment

### 6.1 ERP/cloud software positive but bridge-dependent

`012510` is the constructive C28 row. The stock repriced materially after the April trigger, but later drawdown still shows why C28 should ask for retention, recurring revenue, OPM, and EPS revision evidence. This is Stage3-Yellow candidate, not automatic Green.

### 6.2 AI office theme high-MAE path

`030520` is the dangerous middle family. The AI office/document software theme created large MFE, but the later trough was much deeper than a normal contract-retention drawdown. This argues for a late confirmation rule: without seat expansion, retention, and margin durability, the model should not treat AI software vocabulary as C28 Green.

### 6.3 Cybersecurity label false positives

`053800` and `263860` show the security-label trap. A security headline can create a tradeable spike, but if contract renewal, ARR, maintenance, and margin bridge are not visible, the path becomes local 4B watch or hard counterexample.

## 7. Raw component score simulation

| symbol | contract/retention evidence | recurring revenue/ARR | margin/revision bridge | price confirmation | MAE/logic guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 012510 | 18 | 16 | 14 | 21 | -7 | 62 | Stage3-Yellow candidate |
| 030520 | 14 | 8 | 6 | 24 | -16 | 36 | Stage2/Yellow high-MAE guard |
| 053800 | 12 | 7 | 6 | 8 | -10 | 23 | Stage2/local 4B watch |
| 263860 | 10 | 5 | 3 | 3 | -18 | 3 | Hard counterexample / 4C watch |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c28_software_security_requires_retention_arr_margin_bridge","scope":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","candidate_action":"stage2_required_bridge","rule":"Do not promote software/security/ERP/office-AI labels above Stage2 unless contract renewal, retention, seat expansion, recurring maintenance, ARR, cloud conversion, OPM, cash conversion, or EPS revision bridge is visible.","supporting_cases":["030520","053800","263860"],"counterbalanced_by":["012510"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c28_erp_cloud_positive_delta","scope":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","candidate_action":"stage3_yellow_candidate_delta","rule":"ERP/cloud software names with verified recurring contract retention plus OPM/revision bridge can receive Stage3-Yellow treatment; Green requires drawdown containment and URL-verified evidence.","supporting_cases":["012510"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c28_ai_office_theme_high_mae_guard","scope":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","candidate_action":"local_4b_watch_guard","rule":"AI office/document software theme spikes should be capped at Yellow/local 4B when later MAE is severe and no seat-retention or margin durability bridge is verified.","supporting_cases":["030520"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c28_security_label_false_stage2_guard","scope":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","candidate_action":"hard_4c_watch","rule":"Security labels with small or temporary MFE and severe MAE should become hard counterexamples when ARR/retention and renewal evidence is absent.","supporting_cases":["053800","263860"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","round":"R8","loop":"98","positive_rows":1,"counterexample_rows":3,"new_symbol_count":4,"primary_residual":"C28 needs sharper separation between recurring contract-retention software and AI/security theme spikes without ARR, renewal, seat expansion, or margin durability.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_candidate_delta","local_4b_watch_guard","hard_4c_watch"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","sample_count":4,"avg_mfe_pct":31.85,"avg_mae_pct":-30.04,"median_mfe_pct":31.79,"median_mae_pct":-30.38,"interpretation":"C28 software/security labels can produce large MFE, but asymmetry turns poor when recurring retention and margin bridge are absent."}
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
  - selected profile corporate-action caveats are historical and outside local 2024 trigger windows
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
  1. c28_software_security_requires_retention_arr_margin_bridge -> stage2_required_bridge
  2. c28_erp_cloud_positive_delta -> stage3_yellow_candidate_delta
  3. c28_ai_office_theme_high_mae_guard -> local_4b_watch_guard
  4. c28_security_label_false_stage2_guard -> hard_4c_watch

Expected behavior:
- Software/security/ERP/office-AI vocabulary alone should not create Green.
- Contract renewal, retention, seat expansion, recurring maintenance, ARR, cloud conversion, OPM, cash conversion, or EPS revision can justify Stage3-Yellow.
- AI/security theme spikes should be capped or marked hard counterexample when MAE dominates and retention evidence is absent.
```
