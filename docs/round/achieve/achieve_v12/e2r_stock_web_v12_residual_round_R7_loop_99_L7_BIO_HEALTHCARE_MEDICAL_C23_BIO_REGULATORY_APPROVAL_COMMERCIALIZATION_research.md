# E2R Stock-Web v12 Residual Research — R7 loop 99 / L7 / C23

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R7
selected_loop: 99
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: CNS_DRUG_BIOSIMILAR_GI_DRUG_APPROVAL_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE_VS_BINARY_REGULATORY_FAILURE_AND_LABEL_SPIKE
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - approval_to_revenue_bridge_test
  - launch_reimbursement_channel_guardrail
  - binary_regulatory_failure_guardrail
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

이번 파일은 `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION` 전용 residual research다.

C23은 “승인”, “허가”, “품목허가”, “FDA/EMA”, “상업화”라는 단어만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 승인 이벤트가 실제 launch timing, reimbursement, channel access, prescription/order conversion, gross-to-net, OPM/FCF로 이어지는지다.

```text
regulatory approval / commercialization headline
  → launch timing / reimbursement / channel access
  → prescription or customer order conversion
  → revenue / gross-to-net / margin / FCF bridge
  → stock-web 1D OHLC forward path
```

승인은 병원 문이 열리는 장면이다. 하지만 매출은 환자가 실제로 처방받고, 보험·채널·가격을 통과해 계산서가 찍힐 때 생긴다. C23은 “문이 열렸다”와 “매출이 들어왔다”를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["326030","000250","195940","028300"],"profile_paths":["atlas/symbol_profiles/326/326030.json","atlas/symbol_profiles/000/000250.json","atlas/symbol_profiles/195/195940.json","atlas/symbol_profiles/028/028300.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/326/326030/2024.csv","atlas/ohlcv_tradable_by_symbol_year/000/000250/2024.csv","atlas/ohlcv_tradable_by_symbol_year/195/195940/2024.csv","atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv"],"validation_scope":"2024 trigger-level forward path; selected local windows avoid active corporate-action caveat windows. 326030, 195940 have zero corporate-action candidates; 000250 has only an old 2002 caveat; 028300 local May 2024 row is used only as binary regulatory failure counterexample."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C23 at 29 rows, 1 row short of the 30-row minimum stability zone.
- Existing registry shows C23 parsed through `R7 loop 98`.
- This output uses `R7 loop 99`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file separates CNS commercial revenue, biosimilar/ophthalmology partner commercialization, GI-drug launch/reimbursement, and binary regulatory failure.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C23-R7L99-01 | 326030 | SK바이오팜 | 2024-08-08 | 2024-08-08 | 89800 | 130000 | 82800 | 44.77% | -7.80% | CNS drug commercialization/revenue bridge path worked; strongest large-cap commercial execution candidate. |
| C23-R7L99-02 | 000250 | 삼천당제약 | 2024-03-25 | 2024-03-25 | 111100 | 230000 | 98900 | 107.02% | -10.98% | Biosimilar/ophthalmology commercialization optionality produced explosive MFE, but launch/reimbursement bridge still required. |
| C23-R7L99-03 | 195940 | HK이노엔 | 2024-08-28 | 2024-08-28 | 44100 | 52000 | 43700 | 17.91% | -0.91% | GI drug commercialization/reimbursement path had controlled MAE and moderate MFE. |
| C23-R7L99-04 | 028300 | HLB | 2024-05-16 | 2024-05-16 | 95800 | 106900 | 45150 | 11.59% | -52.87% | Binary regulatory event failure shows approval expectation must not be scored as commercialization. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C23-R7L99-01","round":"R7","loop":"99","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"CNS_DRUG_COMMERCIAL_REVENUE_MARGIN_BRIDGE","symbol":"326030","name":"SK바이오팜","trigger_type":"cns_drug_commercial_revenue_margin_bridge","trigger_date":"2024-08-08","entry_date":"2024-08-08","entry_price":89800,"peak_price":130000,"peak_date":"2024-10-16","trough_price":82800,"trough_date":"2024-08-08","mfe_pct":44.77,"mae_pct":-7.80,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_exact_revenue_margin_URLs","residual_flag":"positive_commercial_execution_path_but_requires_prescription_revenue_margin_bridge","dedupe_key":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|326030|cns_drug_commercial_revenue_margin_bridge|2024-08-08"}
{"row_type":"trigger","case_id":"C23-R7L99-02","round":"R7","loop":"99","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"OPHTHALMOLOGY_BIOSIMILAR_PARTNER_APPROVAL_COMMERCIALIZATION_OPTIONALITY","symbol":"000250","name":"삼천당제약","trigger_type":"ophthalmology_biosimilar_partner_approval_commercialization_optionality","trigger_date":"2024-03-25","entry_date":"2024-03-25","entry_price":111100,"peak_price":230000,"peak_date":"2024-07-10","trough_price":98900,"trough_date":"2024-04-05","mfe_pct":107.02,"mae_pct":-10.98,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_with_high_volatility_guardrail","residual_flag":"explosive_MFE_but_launch_reimbursement_channel_revenue_bridge_required_before_Green","dedupe_key":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|000250|ophthalmology_biosimilar_partner_approval_commercialization_optionality|2024-03-25"}
{"row_type":"trigger","case_id":"C23-R7L99-03","round":"R7","loop":"99","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"GI_DRUG_COMMERCIALIZATION_REIMBURSEMENT_CHANNEL_BRIDGE","symbol":"195940","name":"HK이노엔","trigger_type":"gi_drug_commercialization_reimbursement_channel_bridge","trigger_date":"2024-08-28","entry_date":"2024-08-28","entry_price":44100,"peak_price":52000,"peak_date":"2024-10-07","trough_price":43700,"trough_date":"2024-09-05","mfe_pct":17.91,"mae_pct":-0.91,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_channel_revenue_URLs","residual_flag":"controlled_MAE_commercialization_path_but_exact_reimbursement_channel_URLs_required","dedupe_key":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|195940|gi_drug_commercialization_reimbursement_channel_bridge|2024-08-28"}
{"row_type":"trigger","case_id":"C23-R7L99-04","round":"R7","loop":"99","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BINARY_REGULATORY_APPROVAL_EXPECTATION_FAILURE_NOT_COMMERCIALIZATION","symbol":"028300","name":"HLB","trigger_type":"binary_regulatory_approval_expectation_failure_not_commercialization","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":95800,"peak_price":106900,"peak_date":"2024-05-16","trough_price":45150,"trough_date":"2024-05-21","mfe_pct":11.59,"mae_pct":-52.87,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_4C_or_binary_event_block","residual_flag":"approval_expectation_price_strength_failed_before_commercialization_bridge","dedupe_key":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|028300|binary_regulatory_approval_expectation_failure_not_commercialization|2024-05-16"}
```

## 6. Score-return alignment

### 6.1 Commercial execution winner family

`326030` and `195940` are the cleanest C23 mechanisms in this sample. The market rewarded already-opened commercial paths where revenue and channel execution can be monitored. These rows support Stage3-Yellow treatment when prescription/order conversion, reimbursement, and OPM/FCF are verified.

### 6.2 Approval/partner optionality with high volatility

`000250` shows the explosive positive family. It can generate very large MFE, but the same row demonstrates why C23 should not stop at the approval/partner headline. Commercial launch, reimbursement, supply, pricing, and revenue conversion still need exact evidence before production Green.

### 6.3 Binary regulatory failure

`028300` is the hard guardrail. It had pre-event price strength and same-day MFE, but the forward path collapsed before any commercialization bridge existed. C23 should treat this as approval-expectation failure, not approval-to-commercialization success.

## 7. Raw component score simulation

| symbol | regulatory/commercial evidence | launch/channel bridge | revenue/margin bridge | price confirmation | event-risk guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 326030 | 21 | 18 | 18 | 22 | -4 | 75 | Stage3-Yellow/Green candidate |
| 000250 | 22 | 14 | 10 | 25 | -7 | 64 | Stage3-Yellow with volatility guard |
| 195940 | 19 | 17 | 14 | 15 | -1 | 64 | Stage3-Yellow candidate |
| 028300 | 15 | 2 | 0 | 4 | -24 | -3 | Hard 4C / binary event block |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c23_approval_requires_launch_reimbursement_revenue_bridge","scope":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","candidate_action":"stage2_required_bridge","rule":"Do not promote approval/regulatory/commercialization labels above Stage2 unless launch timing, reimbursement, channel access, prescription/order conversion, revenue, margin, FCF, or EPS revision bridge is visible.","supporting_cases":["028300"],"counterbalanced_by":["326030","000250","195940"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c23_commercial_revenue_positive_delta","scope":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"Names with verified commercial sales, prescription/order conversion, and OPM/FCF bridge can receive stronger Stage3-Yellow/Green candidate treatment.","supporting_cases":["326030","195940"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c23_biosimilar_optional_high_volatility_guard","scope":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","candidate_action":"stage3_yellow_with_volatility_guard","rule":"Biosimilar/partner approval optionality can be Stage3-Yellow when MFE is strong, but production Green requires launch, reimbursement, channel, and revenue confirmation.","supporting_cases":["000250"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c23_binary_approval_expectation_failure_guard","scope":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","candidate_action":"hard_4c_watch","rule":"Pre-event approval expectation price strength must not override binary regulatory failure; if commercialization bridge never opens and MAE dominates, mark hard 4C or event-risk block.","supporting_cases":["028300"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","round":"R7","loop":"99","positive_rows":3,"counterexample_rows":1,"new_symbol_count":4,"primary_residual":"C23 should separate true commercialization revenue bridge from approval/partner optionality and binary regulatory expectation failure.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_to_green_candidate_delta","stage3_yellow_with_volatility_guard","hard_4c_watch"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","sample_count":4,"avg_mfe_pct":45.32,"avg_mae_pct":-18.14,"median_mfe_pct":31.34,"median_mae_pct":-9.39,"interpretation":"C23 has strong upside when commercialization and revenue conversion are real, but binary approval expectation failures require hard event-risk blocking."}
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
- Ingest this C23 R7 loop 99 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c23_approval_requires_launch_reimbursement_revenue_bridge -> stage2_required_bridge
  2. c23_commercial_revenue_positive_delta -> stage3_yellow_to_green_candidate_delta
  3. c23_biosimilar_optional_high_volatility_guard -> stage3_yellow_with_volatility_guard
  4. c23_binary_approval_expectation_failure_guard -> hard_4c_watch

Expected behavior:
- Approval/regulatory vocabulary alone should not create Green.
- Launch timing, reimbursement, channel access, prescription/order conversion, revenue, margin, FCF, or EPS revision can justify Stage3-Yellow/Green.
- Binary approval-expectation failures should be hard-blocked before they contaminate commercialization-success rows.
```
