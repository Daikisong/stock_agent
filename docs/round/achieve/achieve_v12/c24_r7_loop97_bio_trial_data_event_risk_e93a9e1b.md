# E2R Stock-Web v12 Residual Research — R7 loop 97 / L7 / C24

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R7
selected_loop: 97
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: PLATFORM_LICENSE_TRIAL_DATA_RERATING_TARGETED_ONCOLOGY_VS_BINARY_FAILURE_AND_OPTIONALITY_HIGH_MAE
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - trial_data_to_partner_revenue_bridge_test
  - binary_trial_regulatory_failure_guardrail
  - platform_license_positive_delta
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

C24는 “임상 데이터”, “긍정적 결과”, “학회 발표”, “FDA 기대”, “파트너링/라이선스”라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 trial-data/event가 실제 partner validation, regulatory path, milestone, royalty/revenue bridge, cash runway, dilution risk, and binary-failure guard로 연결되는지다.

```text
bio trial data / platform license / clinical event headline
  → data quality / endpoint durability / partner validation
  → regulatory path / milestone / royalty or commercialization bridge
  → cash runway / dilution / binary failure risk
  → stock-web 1D OHLC forward path
```

임상 데이터는 어두운 실험실에서 켜지는 신호등과 같다. 초록불처럼 보여도, 실제 길이 열리려면 endpoint, 규제기관, 파트너 검증, 현금화 다리를 모두 건너야 한다. C24는 “데이터가 나왔다”와 “위험조정 가치가 현금화된다”를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["196170","028300","039200","140410"],"profile_paths":["atlas/symbol_profiles/196/196170.json","atlas/symbol_profiles/028/028300.json","atlas/symbol_profiles/039/039200.json","atlas/symbol_profiles/140/140410.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv","atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","atlas/ohlcv_tradable_by_symbol_year/039/039200/2024.csv","atlas/ohlcv_tradable_by_symbol_year/140/140410/2024.csv"],"validation_scope":"2024 trigger-level forward path; 196170 caveats end 2021, 028300 caveats end 2021, 039200 caveat is 2022, 140410 caveats are 2022. Selected 2024 local windows avoid active corporate-action contamination."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C24 at 27 rows, 3 rows short of the 30-row minimum stability zone.
- Existing registry shows C24 parsed through `R7 loop 96`.
- This output uses `R7 loop 97`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- Prior C24 loop 96 touched targeted oncology / platform license data / gene therapy event risk. This file compresses platform-license positive delta, binary failure, targeted oncology rerating, and trial optionality high-MAE guard.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C24-R7L97-01 | 196170 | 알테오젠 | 2024-02-23 | 2024-02-23 | 131200 | 402000 | 119000 | 206.40% | -9.30% | Platform/license validation path worked explosively, but needs partner/milestone/royalty bridge. |
| C24-R7L97-02 | 028300 | HLB | 2024-05-16 | 2024-05-16 | 95800 | 106900 | 45150 | 11.59% | -52.87% | Binary regulatory/trial event failure; approval expectation must be hard-guarded. |
| C24-R7L97-03 | 039200 | 오스코텍 | 2024-03-12 | 2024-03-12 | 28900 | 45850 | 25100 | 58.65% | -13.15% | Targeted oncology data/partner validation rerating worked but had event-volatility drawdown. |
| C24-R7L97-04 | 140410 | 메지온 | 2024-02-26 | 2024-02-26 | 40050 | 50200 | 27000 | 25.34% | -32.58% | Trial optionality made MFE, but high-MAE and endpoint/regulatory uncertainty block Green. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C24-R7L97-01","round":"R7","loop":"97","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"PLATFORM_LICENSE_VALIDATION_DATA_RERATING_PARTNER_ROYALTY_BRIDGE","symbol":"196170","name":"알테오젠","trigger_type":"platform_license_validation_data_rerating_partner_royalty_bridge","trigger_date":"2024-02-23","entry_date":"2024-02-23","entry_price":131200,"peak_price":402000,"peak_date":"2024-10-22","trough_price":119000,"trough_date":"2024-02-23","mfe_pct":206.40,"mae_pct":-9.30,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_partner_milestone_royalty_URLs","residual_flag":"platform_license_validation_extreme_positive_but_requires_partner_milestone_royalty_cash_bridge","dedupe_key":"C24_BIO_TRIAL_DATA_EVENT_RISK|196170|platform_license_validation_data_rerating_partner_royalty_bridge|2024-02-23"}
{"row_type":"trigger","case_id":"C24-R7L97-02","round":"R7","loop":"97","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BINARY_TRIAL_REGULATORY_EVENT_FAILURE_HARD_4C","symbol":"028300","name":"HLB","trigger_type":"binary_trial_regulatory_event_failure_hard_4c","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":95800,"peak_price":106900,"peak_date":"2024-05-16","trough_price":45150,"trough_date":"2024-05-21","mfe_pct":11.59,"mae_pct":-52.87,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_4C_or_binary_event_block","residual_flag":"binary_trial_regulatory_failure_price_strength_collapsed_without_approval_data_bridge","dedupe_key":"C24_BIO_TRIAL_DATA_EVENT_RISK|028300|binary_trial_regulatory_event_failure_hard_4c|2024-05-16"}
{"row_type":"trigger","case_id":"C24-R7L97-03","round":"R7","loop":"97","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"TARGETED_ONCOLOGY_DATA_PARTNER_VALIDATION_RERATING_WITH_EVENT_VOLATILITY","symbol":"039200","name":"오스코텍","trigger_type":"targeted_oncology_data_partner_validation_rerating_with_event_volatility","trigger_date":"2024-03-12","entry_date":"2024-03-12","entry_price":28900,"peak_price":45850,"peak_date":"2024-08-21","trough_price":25100,"trough_date":"2024-04-08","mfe_pct":58.65,"mae_pct":-13.15,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_data_partner_URLs","residual_flag":"targeted_oncology_data_rerating_positive_but_event_volatility_and_endpoint_bridge_required","dedupe_key":"C24_BIO_TRIAL_DATA_EVENT_RISK|039200|targeted_oncology_data_partner_validation_rerating_with_event_volatility|2024-03-12"}
{"row_type":"trigger","case_id":"C24-R7L97-04","round":"R7","loop":"97","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"TRIAL_OPTIONALITY_HIGH_MAE_ENDPOINT_REGULATORY_GUARD","symbol":"140410","name":"메지온","trigger_type":"trial_optionality_high_mae_endpoint_regulatory_guard","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":40050,"peak_price":50200,"peak_date":"2024-03-06","trough_price":27000,"trough_date":"2024-09-30","mfe_pct":25.34,"mae_pct":-32.58,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_high_MAE_guardrail","residual_flag":"trial_optionality_MFE_but_endpoint_regulatory_uncertainty_and_high_MAE_block_Green","dedupe_key":"C24_BIO_TRIAL_DATA_EVENT_RISK|140410|trial_optionality_high_mae_endpoint_regulatory_guard|2024-02-26"}
```

## 6. Score-return alignment

### 6.1 Platform/license positive delta

`196170` is the constructive C24 row. The price path shows that platform validation and licensing-style evidence can create enormous repricing. But even here, production Green should require exact partner, milestone, royalty, exclusivity, regulatory path and cash bridge.

### 6.2 Binary failure block

`028300` is the hard guardrail. The price path had pre-event strength and same-day MFE, but the forward path collapsed almost immediately. C24 should hard-block binary trial/regulatory failures and not let prior price strength override the event result.

### 6.3 Targeted oncology and trial optionality need guardrails

`039200` is a positive but volatile targeted-oncology data rerating path. `140410` shows the option-like family: MFE exists, but later drawdown is too large to promote without endpoint durability, regulatory clarity, and dilution/cash runway proof.

## 7. Raw component score simulation

| symbol | data/platform quality | partner/regulatory bridge | milestone/royalty/revenue | cash runway/dilution guard | price confirmation | event-risk guard | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 196170 | 24 | 20 | 18 | 12 | 25 | -4 | 95 | Stage3-Yellow/Green candidate |
| 028300 | 15 | 0 | 0 | 2 | 2 | -25 | -6 | Hard 4C / binary event block |
| 039200 | 21 | 15 | 10 | 8 | 16 | -6 | 64 | Stage3-Yellow candidate |
| 140410 | 16 | 7 | 3 | 5 | 8 | -15 | 24 | Stage2/Yellow high-MAE guard |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c24_trial_data_requires_endpoint_partner_regulatory_cash_bridge","scope":"C24_BIO_TRIAL_DATA_EVENT_RISK","candidate_action":"stage2_required_bridge","rule":"Do not promote trial-data/platform-event labels above Stage2 unless endpoint quality, durability, partner validation, regulatory path, milestone/royalty/revenue bridge, cash runway, and dilution risk are visible.","supporting_cases":["028300","140410"],"counterbalanced_by":["196170","039200"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c24_platform_license_positive_delta","scope":"C24_BIO_TRIAL_DATA_EVENT_RISK","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"Platform/license validation rows can receive strong Stage3-Yellow/Green candidate treatment when partner validation, milestone/royalty economics, and cash bridge are URL-verified.","supporting_cases":["196170"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c24_binary_failure_hard_event_block","scope":"C24_BIO_TRIAL_DATA_EVENT_RISK","candidate_action":"hard_4c_or_event_block","rule":"Binary trial/regulatory failures must override prior price strength; severe MAE after event failure should be hard-blocked from Green.","supporting_cases":["028300"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c24_trial_optionality_high_MAE_guard","scope":"C24_BIO_TRIAL_DATA_EVENT_RISK","candidate_action":"stage2_to_yellow_with_high_MAE_guardrail","rule":"Trial optionality rows with MFE but high later MAE should remain Stage2/Yellow until endpoint durability, regulatory clarity, and cash-runway evidence repairs the row.","supporting_cases":["140410"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c24_targeted_oncology_data_yellow_delta","scope":"C24_BIO_TRIAL_DATA_EVENT_RISK","candidate_action":"stage3_yellow_candidate_delta","rule":"Targeted oncology data rows can receive Yellow treatment when data quality and partner/regulatory bridge are visible, but event volatility blocks automatic Green.","supporting_cases":["039200"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","round":"R7","loop":"97","positive_rows":2,"counterexample_rows":2,"new_symbol_count":4,"primary_residual":"C24 should separate platform/license validation and targeted-oncology data rerating from binary trial/regulatory failure and high-MAE optionality without endpoint, regulatory or cash bridge.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_to_green_candidate_delta","hard_4c_or_event_block","stage2_to_yellow_with_high_MAE_guardrail","stage3_yellow_candidate_delta"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","sample_count":4,"avg_mfe_pct":75.50,"avg_mae_pct":-26.98,"median_mfe_pct":42.00,"median_mae_pct":-22.87,"interpretation":"C24 has extreme upside in validated platform/data rows, but binary failure and high-MAE optionality require hard event-risk blocking and non-price bridge verification."}
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
- Ingest this C24 R7 loop 97 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c24_trial_data_requires_endpoint_partner_regulatory_cash_bridge -> stage2_required_bridge
  2. c24_platform_license_positive_delta -> stage3_yellow_to_green_candidate_delta
  3. c24_binary_failure_hard_event_block -> hard_4c_or_event_block
  4. c24_trial_optionality_high_MAE_guard -> stage2_to_yellow_with_high_MAE_guardrail
  5. c24_targeted_oncology_data_yellow_delta -> stage3_yellow_candidate_delta

Expected behavior:
- Trial-data/platform-event vocabulary alone should not create Green.
- Endpoint quality, durability, partner validation, regulatory path, milestone/royalty/revenue bridge, cash runway and dilution risk can justify Stage3-Yellow/Green.
- Binary event failures and high-MAE optionality should be blocked or capped until exact non-price evidence repairs the row.
```
