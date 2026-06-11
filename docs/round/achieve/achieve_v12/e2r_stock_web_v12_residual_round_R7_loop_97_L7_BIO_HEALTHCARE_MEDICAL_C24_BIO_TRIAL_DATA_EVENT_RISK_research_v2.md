# E2R Stock-Web v12 Residual Research — R7 loop 97 / L7 / C24

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R7
selected_loop: 97
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: BIO_PLATFORM_ADC_AND_ONCOLOGY_TRIAL_DATA_DURABILITY_BRIDGE_VS_CLINICAL_EVENT_CRASH_HARD_4C
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - 4C_thesis_break_watch
  - clinical_event_durability_guardrail
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

이번 파일은 `C24_BIO_TRIAL_DATA_EVENT_RISK` 전용 residual research다.

C24는 “임상”, “데이터”, “파이프라인”, “AACR/ASCO/학회”, “FDA 이벤트” 같은 단어만으로 Stage3-Green을 주는 bucket이 아니다. 이 archetype의 핵심은 임상 이벤트가 실제 데이터 질, 파트너 optionality, 후속 개발 가능성, 규제/상업화 경로로 이어지는지다.

```text
clinical data / pipeline event / trial catalyst
  → data durability / endpoint quality / safety profile
  → partner optionality / next-stage trial / regulatory path
  → funding runway / commercialization probability
  → stock-web 1D OHLC forward path
```

임상 이벤트는 병원 복도 끝의 신호등과 같다. 초록불처럼 보여도 실제로 건널 수 있으려면 데이터가 튼튼하고, 안전성·환자군·파트너·규제 경로가 모두 이어져야 한다. C24는 “불이 켜졌다”와 “길을 건넜다”를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["196170","141080","028300","298380"],"profile_paths":["atlas/symbol_profiles/196/196170.json","atlas/symbol_profiles/141/141080.json","atlas/symbol_profiles/028/028300.json","atlas/symbol_profiles/298/298380.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv","atlas/ohlcv_tradable_by_symbol_year/141/141080/2024.csv","atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","atlas/ohlcv_tradable_by_symbol_year/298/298380/2024.csv"],"validation_scope":"2024 trigger-level forward path; 298380 has no corporate-action candidates; 196170/141080/028300 historical caveats are outside or flagged away from the selected 2024 local windows except 141080 has a 2024-04-23 profile caveat, so pre-caveat February/March rows are used for that case."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C24 at 27 rows, 3 rows short of the 30-row minimum stability zone.
- Existing registry shows C24 parsed through `R7 loop 96`.
- This output uses `R7 loop 97`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file separates durable platform/ADC data rerating from single binary clinical-event crash risk.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C24-R7L97-01 | 196170 | 알테오젠 | 2024-02-22 | 2024-02-22 | 105000 | 225500 | 85000 | 114.76% | -19.05% | Bio-platform event rerating worked, but early volatility requires staging and partner/data durability proof. |
| C24-R7L97-02 | 141080 | 리가켐바이오 | 2024-02-22 | 2024-02-22 | 56100 | 84000 | 53000 | 49.73% | -5.53% | ADC/pipeline data + partner optionality path with relatively contained MAE. |
| C24-R7L97-03 | 298380 | 에이비엘바이오 | 2024-02-22 | 2024-02-22 | 21250 | 30500 | 20650 | 43.53% | -2.82% | Bispecific/platform pipeline rerating candidate; price asymmetry constructive pending exact data/partner URLs. |
| C24-R7L97-04 | 028300 | HLB | 2024-05-16 | 2024-05-16 | 95800 | 106900 | 45150 | 11.59% | -52.87% | Binary clinical/regulatory event risk crash; hard 4C watch / thesis-break counterexample. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C24-R7L97-01","round":"R7","loop":"97","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_PLATFORM_TRIAL_DATA_PARTNER_RERATING_HIGH_MAE_GUARD","symbol":"196170","name":"알테오젠","trigger_type":"bio_platform_trial_data_partner_rerating_high_mae_guard","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":105000,"peak_price":225500,"peak_date":"2024-03-18","trough_price":85000,"trough_date":"2024-02-22","mfe_pct":114.76,"mae_pct":-19.05,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_with_sizing_guard","residual_flag":"platform_rerating_positive_but_requires_exact_partner_data_durability_URLs","dedupe_key":"C24_BIO_TRIAL_DATA_EVENT_RISK|196170|bio_platform_trial_data_partner_rerating_high_mae_guard|2024-02-22"}
{"row_type":"trigger","case_id":"C24-R7L97-02","round":"R7","loop":"97","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"ADC_PIPELINE_DATA_PARTNER_OPTIONALITY_POSITIVE","symbol":"141080","name":"리가켐바이오","trigger_type":"adc_pipeline_data_partner_optionality_positive","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":56100,"peak_price":84000,"peak_date":"2024-03-11","trough_price":53000,"trough_date":"2024-02-22","mfe_pct":49.73,"mae_pct":-5.53,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_data_partner_URLs","residual_flag":"ADC_pipeline_data_positive_with_contained_MAE_pre_corporate_action_candidate_window","dedupe_key":"C24_BIO_TRIAL_DATA_EVENT_RISK|141080|adc_pipeline_data_partner_optionality_positive|2024-02-22"}
{"row_type":"trigger","case_id":"C24-R7L97-03","round":"R7","loop":"97","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BISPECIFIC_PLATFORM_PIPELINE_DATA_RERATING","symbol":"298380","name":"에이비엘바이오","trigger_type":"bispecific_platform_pipeline_data_rerating","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":21250,"peak_price":30500,"peak_date":"2024-03-13","trough_price":20650,"trough_date":"2024-02-22","mfe_pct":43.53,"mae_pct":-2.82,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_exact_trial_partner_URLs","residual_flag":"constructive_platform_pipeline_event_path_with_low_MAE","dedupe_key":"C24_BIO_TRIAL_DATA_EVENT_RISK|298380|bispecific_platform_pipeline_data_rerating|2024-02-22"}
{"row_type":"trigger","case_id":"C24-R7L97-04","round":"R7","loop":"97","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BINARY_CLINICAL_REGULATORY_EVENT_CRASH_HARD_4C","symbol":"028300","name":"HLB","trigger_type":"binary_clinical_regulatory_event_crash_hard_4c","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":95800,"peak_price":106900,"peak_date":"2024-05-16","trough_price":45150,"trough_date":"2024-05-21","mfe_pct":11.59,"mae_pct":-52.87,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_4C_watch_or_binary_event_risk_block","residual_flag":"binary_event_crash_after_pre_event_price_strength","dedupe_key":"C24_BIO_TRIAL_DATA_EVENT_RISK|028300|binary_clinical_regulatory_event_crash_hard_4c|2024-05-16"}
```

## 6. Score-return alignment

### 6.1 Durable platform rerating family

`196170`, `141080`, and `298380` show the constructive side of C24. The market rewarded platform optionality and pipeline data narratives when the event did not remain a one-day headline. However, even the strongest case should not become production Green without exact non-price evidence: data durability, endpoint relevance, safety, partner economics, and next-stage trial/regulatory path.

### 6.2 Binary event crash family

`028300` is the hard guardrail. The pre-event candle had upside, but the forward path collapsed immediately after the binary event. That is exactly the C24 risk: price can be strong right before the event while the thesis is one regulatory/clinical decision away from hard 4C.

### 6.3 Mechanism

C24 should behave like a clinical gatekeeper. Stage2 can recognize catalyst optionality, Yellow can recognize durable data plus partner path, but Green should require more than excitement: endpoint quality, safety, partner validation, funding runway, and a credible regulatory or commercial path.

## 7. Raw component score simulation

| symbol | data/platform evidence | partner/next-stage bridge | regulatory/commercial path | price confirmation | event-risk guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 196170 | 23 | 21 | 17 | 25 | -8 | 78 | Stage3-Yellow/Green candidate with sizing guard |
| 141080 | 22 | 18 | 14 | 20 | -3 | 71 | Stage3-Yellow candidate |
| 298380 | 19 | 15 | 12 | 18 | -2 | 62 | Stage3-Yellow candidate |
| 028300 | 16 | 6 | 3 | 4 | -24 | 5 | Hard 4C / binary event block |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c24_trial_event_requires_data_durability_partner_path","scope":"C24_BIO_TRIAL_DATA_EVENT_RISK","candidate_action":"stage2_required_bridge","rule":"Do not promote clinical/pipeline event labels above Stage2 unless data durability, endpoint quality, safety, partner validation, next-stage trial, funding runway, or regulatory path is visible.","supporting_cases":["028300"],"counterbalanced_by":["196170","141080","298380"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c24_platform_data_positive_delta","scope":"C24_BIO_TRIAL_DATA_EVENT_RISK","candidate_action":"stage3_yellow_candidate_delta","rule":"Bio-platform or ADC/bispecific names with durable data plus partner optionality can receive Stage3-Yellow treatment, but production Green requires exact URL-verified evidence and binary risk control.","supporting_cases":["196170","141080","298380"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c24_binary_event_crash_4c_guard","scope":"C24_BIO_TRIAL_DATA_EVENT_RISK","candidate_action":"hard_4c_watch","rule":"Pre-event price strength must not override binary clinical/regulatory risk; if the forward path shows immediate low-MFE/high-MAE collapse after a binary event, mark hard 4C or event-risk block.","supporting_cases":["028300"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","round":"R7","loop":"97","positive_rows":3,"counterexample_rows":1,"new_symbol_count":4,"primary_residual":"C24 needs sharper separation between durable platform/pipeline data rerating and binary clinical/regulatory event crash risk.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_candidate_delta","hard_4c_watch"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","sample_count":4,"avg_mfe_pct":54.90,"avg_mae_pct":-20.07,"median_mfe_pct":46.63,"median_mae_pct":-12.29,"interpretation":"C24 can generate large upside when platform data and partner optionality are durable, but binary event crashes require a hard 4C guard despite pre-event price strength."}
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
  - historical corporate-action caveats, where present, are outside selected local 2024 windows or explicitly avoided
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research session.

Goal:
- Ingest this C24 R7 loop 97 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c24_trial_event_requires_data_durability_partner_path -> stage2_required_bridge
  2. c24_platform_data_positive_delta -> stage3_yellow_candidate_delta
  3. c24_binary_event_crash_4c_guard -> hard_4c_watch

Expected behavior:
- Clinical/pipeline vocabulary alone should not create Green.
- Durable data, endpoint quality, safety, partner validation, next-stage trial, funding runway, and regulatory path can justify Stage3-Yellow.
- Pre-event price strength must not override binary event crash risk.
```
