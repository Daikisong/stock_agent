# E2R Stock-Web V12 Residual Research — R7 loop 98 / C24_BIO_TRIAL_DATA_EVENT_RISK

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R7
selected_loop: 98
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: mixed_C24_trial_data_event_risk_quality_holdout
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 / quality holdout / C24 rows 69 / trial-data 4B-4C timing validation
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: "2026-02-20"
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection rationale

C24는 정적 No-Repeat Index 기준으로 이미 50 rows를 넘긴 Priority 2 구역이지만, 이번 세션에서 Priority 0/1 축을 여러 차례 보강한 뒤 남은 품질 문제는 **trial-data event의 4B/4C 타이밍**이다. C24는 정보 신뢰도가 점수 대부분을 차지하는 archetype이므로, 같은 임상 이벤트라도 mature randomized endpoint success, DMC futility, ODAC/CRL, small-N early data를 한 덩어리로 처리하면 Stage3와 Stage4가 동시에 오염된다.

이번 pass는 새 positive 채굴보다 **endpoint maturity / signal source / regulatory reason / portfolio diversification / price-path MAE**를 이용해 C24의 hard 4C와 local 4B를 분리하는 quality holdout이다.

## 2. Stock-Web validation scope

```yaml
manifest_url: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
schema_url: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
profile_root: atlas/symbol_profiles
entry_price_rule: entry_date close from tradable shard
MFE_rule: max high from entry row through N tradable rows versus entry_price
MAE_rule: min low from entry row through N tradable rows versus entry_price
forward_windows: [30D, 90D, 180D]
corporate_action_screen: entry_date_to_180D
calibration_usable_rows: 7
```

Screened-out candidates:

```yaml
screened_out_corporate_action_contaminated_candidates:
  - symbol: "140410"
    name: 메지온
    rejected_candidate: "2022-03-22 유데나필 FDA CRL / appeal-boundary candidate"
    reason: corporate_action_candidate within proposed 180D window
  - symbol: "235980"
    name: 메드팩토
    rejected_candidate: "2023-10-23 백토서팁 trial-data / rights-issue contamination candidate"
    reason: corporate_action_candidate within proposed 180D window
  - symbol: "084990"
    name: 헬릭스미스
    rejected_candidate: "2019-09-24 VM202 phase3 miss original date"
    reason: 2020 stock split/rights adjustment candidate within 180D window; replaced by clean 2024-01-04 trigger
```

## 3. Evidence source matrix

| symbol | trigger_family | source | source_url |
|---|---|---|---|
| 000100 | LASER301_MARIPOSA_positive_PFS_bridge | KHIDI/Yakup — 오스코텍, 렉라자 1차 치료제 허가 시 로열티 기대 | https://www.khidi.or.kr/board/view?linkId=48887771&menuId=MENU01816 |
| 039200 | MARIPOSA_royalty_milestone_trial_data_bridge | 팜이데일리 — 오스코텍, 렉라자/MARIPOSA 및 royalty 기대 | https://pharm.edaily.co.kr/news/read?newsId=02013926638822664 |
| 215600 | PexaVec_PHOCUS_DMC_futility_stop | BioSpectator — SillaJen Pexa-Vec PHOCUS early termination | https://www.biospectator.com/news/view/8206 |
| 084990 | VM202_DPN_phase3_2_failure_overkill_buffer | 팜이데일리 — 헬릭스미스 엔젠시스 임상 실패 | https://pharm.edaily.co.kr/news/read?newsId=01456326638754440 |
| 128940 | Poziotinib_ODAC_benefit_risk_negative_portfolio_buffer | 연합뉴스 — FDA 자문위 포지오티닙 신속승인 비권고 | https://www.yna.co.kr/view/AKR20220923024600017 |
| 028300 | Rivoceranib_Camrelizumab_CRL_nonclinical_BIMO_GMP_boundary | Elevar — Rivoceranib+Camrelizumab NDA resubmission and CRL context | https://elevartx.com/2024/09/23/elevar-therapeutics-resubmits-new-drug-application/ |
| 310210 | VRN11_AACR_early_1a_smallN_interpretation_risk | 팜이데일리 — 보로노이 VRN11 AACR early clinical data and price reaction | https://pharm.edaily.co.kr/news/read?newsId=02164806642141368 |

## 4. Case table — actual Stock-Web 1D OHLC path

| symbol | name | trigger_type | trigger_date | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date_180D | drawdown_after_peak_180D_pct | role |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| 000100 | 유한양행 | Stage3-Yellow | 2023-10-23 | 2023-10-23 | 62000 | 3.5484 | -11.4516 | 15.4839 | -11.4516 | 59.0323 | -11.4516 | 2024-07-15 | -3.6511 | positive |
| 039200 | 오스코텍 | Stage3-Yellow | 2023-10-23 | 2023-10-23 | 21850 | 2.0595 | -16.2471 | 13.0435 | -17.6201 | 104.1190 | -17.6201 | 2024-07-10 | -7.7354 | positive |
| 215600 | 신라젠 | Stage4C | 2019-08-02 | 2019-08-02 | 31200 | 0.0000 | -71.1538 | 0.0000 | -74.9359 | 0.0000 | -74.9359 | 2019-08-02 | -74.9359 | counterexample |
| 084990 | 헬릭스미스 | Stage4B | 2024-01-04 | 2024-01-04 | 3935 | 89.0724 | -17.4079 | 89.0724 | -17.4079 | 89.0724 | -17.4079 | 2024-02-06 | -56.1156 | counterexample |
| 128940 | 한미약품 | Stage4B | 2022-09-23 | 2022-09-23 | 237000 | 10.1266 | -5.6962 | 29.9578 | -5.6962 | 43.2489 | -5.6962 | 2023-04-14 | -14.4330 | counterexample |
| 028300 | HLB | Stage4B | 2024-05-17 | 2024-05-17 | 67100 | 9.9851 | -32.7124 | 46.1997 | -32.7124 | 46.1997 | -32.7124 | 2024-07-08 | -40.0612 | counterexample |
| 310210 | 보로노이 | Stage4B | 2025-04-30 | 2025-04-30 | 95600 | 19.3515 | -6.0669 | 60.7741 | -6.0669 | 167.2594 | -6.0669 | 2025-12-03 | -32.0548 | positive_with_4B_watch |

## 5. Interpretation

### 5.1 Positive path: mature endpoint success plus commercial bridge

`000100 유한양행` and `039200 오스코텍` show that C24 should not blindly penalize all clinical-event names. The key was not merely “good clinical data”; it was **mature phase-3 signal + regulatory/commercial/royalty bridge**. The 180D MFE opened to `59.0323%` and `104.1190%`, while 180D MAE stayed materially shallower than the hard-failure cases.

### 5.2 Hard 4C path: asset-level futility with no residual MFE

`215600 신라젠` is the clean hard 4C anchor. DMC futility and lack of survival benefit were asset-level thesis breaks, and the Stock-Web path recorded `0.0000%` 180D MFE versus `-74.9359%` 180D MAE. This is the archetypal C24 case where `hard_4c_thesis_break_routes_to_4c` should be strict.

### 5.3 Overkill buffer: negative regulatory or endpoint event is not always full-company 4C

`084990 헬릭스미스`, `128940 한미약품`, and `028300 HLB` show that hard 4C can overfire. Endpoint failure, ODAC negativity, or CRL are severe, but the routing must distinguish:

```text
asset-level futility / no efficacy = hard 4C
single-asset negative event inside diversified pharma = Stage4B or portfolio-buffer watch
CRL from GMP/BIMO/nonclinical inspection gap = Stage4B unless clinical efficacy/safety thesis is broken
```

HLB in particular had a deep MAE path but also a large 90D/180D MFE, implying that “CRL” alone is not granular enough as a hard 4C trigger.

### 5.4 Early-data watch: small-N signal can be positive but still 4B

`310210 보로노이` had early 1a data interpretation risk, yet 180D MFE expanded to `167.2594%`. The correct calibration is not Stage3-Green, but also not hard 4C. It is a **Stage4B watch with milestone-progression gate**.

## 6. Raw component score / return alignment

C24 runtime proxy weight assumption:

```yaml
weights:
  eps_fcf_explosion: 5
  earnings_visibility: 15
  bottleneck_pricing: 5
  market_mispricing: 10
  valuation_rerating: 5
  capital_allocation: 5
  information_confidence: 55
```

| symbol | name | score_total_current_proxy | expected_stage_v12 | current_profile_error_type | MFE_180D_pct | MAE_180D_pct |
|---|---:|---:|---|---|---:|---:|
| 000100 | 유한양행 | 78.5000 | Stage3-Yellow | underweights_mature_phase3_commercial_bridge_if_treated_as_event_only | 59.0323 | -11.4516 |
| 039200 | 오스코텍 | 76.0500 | Stage3-Yellow | event_risk_profile_misses_royalty_bridge_positive | 104.1190 | -17.6201 |
| 215600 | 신라젠 | 5.2500 | Stage4C | must_route_asset_level_futility_to_hard_4C_immediately | 0.0000 | -74.9359 |
| 084990 | 헬릭스미스 | 39.3500 | Stage4B | hard_4C_overkill_after_known_failure_when_relief_or_optionality_rally_occurs | 89.0724 | -17.4079 |
| 128940 | 한미약품 | 52.3000 | Stage4B | single_asset_regulatory_failure_should_not_hard_4C_diversified_pharma | 43.2489 | -5.6962 |
| 028300 | HLB | 44.5000 | Stage4B | CRL_reason_split_needed_clinical_failure_vs_nonclinical_inspection | 46.1997 | -32.7124 |
| 310210 | 보로노이 | 58.8500 | Stage4B | early_smallN_data_should_not_be_hard_4C_but_needs_4B_local_risk_overlay | 167.2594 | -6.0669 |

## 7. Machine-readable trigger rows JSONL

```jsonl
{"case_id":"C24_000100_2023_10_23_LASER_MARIPOSA_positive_PFS_bridge","symbol":"000100","name":"유한양행","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_mature_phase3_positive_PFS_to_regulatory_commercial_bridge","trigger_type":"Stage3-Yellow","trigger_family":"LASER301_MARIPOSA_positive_PFS_bridge","trigger_date":"2023-10-23","entry_date":"2023-10-23","entry_price":62000,"MFE_30D_pct":3.5484,"MAE_30D_pct":-11.4516,"MFE_90D_pct":15.4839,"MAE_90D_pct":-11.4516,"MFE_180D_pct":59.0323,"MAE_180D_pct":-11.4516,"peak_date_180D":"2024-07-15","peak_price_180D":98600,"drawdown_after_peak_180D_pct":-3.6511,"case_role":"positive","expected_stage_v12":"Stage3-Yellow","calibration_usable":true,"current_profile_error_type":"underweights_mature_phase3_commercial_bridge_if_treated_as_event_only","evidence_summary":"레이저티닙/렉라자 계열은 무작위 3상 PFS 신호와 1차치료/상업화 bridge가 붙어 C24 안에서도 단순 이벤트가 아니라 Stage3-Yellow 후보로 압축 가능했다.","source_url":"https://www.khidi.or.kr/board/view?linkId=48887771&menuId=MENU01816","source_title":"KHIDI/Yakup — 오스코텍, 렉라자 1차 치료제 허가 시 로열티 기대","score_components":{"eps_fcf_explosion":60,"earnings_visibility":80,"bottleneck_pricing":50,"market_mispricing":65,"valuation_rerating":55,"capital_allocation":45,"information_confidence":90},"score_total_current_proxy":78.5,"stock_web_manifest_max_date":"2026-02-20","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","corporate_action_contaminated_180D_window":false,"insufficient_forward_window":false,"source_proxy_only":false,"evidence_url_pending":false}
{"case_id":"C24_039200_2023_10_23_MARIPOSA_royalty_milestone_trial_data_bridge","symbol":"039200","name":"오스코텍","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_mature_phase3_positive_royalty_milestone_bridge","trigger_type":"Stage3-Yellow","trigger_family":"MARIPOSA_royalty_milestone_trial_data_bridge","trigger_date":"2023-10-23","entry_date":"2023-10-23","entry_price":21850,"MFE_30D_pct":2.0595,"MAE_30D_pct":-16.2471,"MFE_90D_pct":13.0435,"MAE_90D_pct":-17.6201,"MFE_180D_pct":104.119,"MAE_180D_pct":-17.6201,"peak_date_180D":"2024-07-10","peak_price_180D":44600,"drawdown_after_peak_180D_pct":-7.7354,"case_role":"positive","expected_stage_v12":"Stage3-Yellow","calibration_usable":true,"current_profile_error_type":"event_risk_profile_misses_royalty_bridge_positive","evidence_summary":"오스코텍은 직접 판매 회사가 아니라 royalty/milestone bridge가 핵심이므로, 같은 trial-data positive라도 상업화 현금흐름 가시성을 별도 축으로 봐야 했다.","source_url":"https://pharm.edaily.co.kr/news/read?newsId=02013926638822664","source_title":"팜이데일리 — 오스코텍, 렉라자/MARIPOSA 및 royalty 기대","score_components":{"eps_fcf_explosion":50,"earnings_visibility":78,"bottleneck_pricing":48,"market_mispricing":68,"valuation_rerating":50,"capital_allocation":35,"information_confidence":88},"score_total_current_proxy":76.05,"stock_web_manifest_max_date":"2026-02-20","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","corporate_action_contaminated_180D_window":false,"insufficient_forward_window":false,"source_proxy_only":false,"evidence_url_pending":false}
{"case_id":"C24_215600_2019_08_02_PexaVec_PHOCUS_DMC_futility_stop","symbol":"215600","name":"신라젠","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_asset_level_DMC_futility_hard_4C","trigger_type":"Stage4C","trigger_family":"PexaVec_PHOCUS_DMC_futility_stop","trigger_date":"2019-08-02","entry_date":"2019-08-02","entry_price":31200,"MFE_30D_pct":0.0,"MAE_30D_pct":-71.1538,"MFE_90D_pct":0.0,"MAE_90D_pct":-74.9359,"MFE_180D_pct":0.0,"MAE_180D_pct":-74.9359,"peak_date_180D":"2019-08-02","peak_price_180D":31200,"drawdown_after_peak_180D_pct":-74.9359,"case_role":"counterexample","expected_stage_v12":"Stage4C","calibration_usable":true,"current_profile_error_type":"must_route_asset_level_futility_to_hard_4C_immediately","evidence_summary":"DMC futility와 생존기간 개선 실패는 C24에서 hard thesis break다. 이후 가격경로도 MFE가 열리지 않고 MAE만 깊어졌다.","source_url":"https://www.biospectator.com/news/view/8206","source_title":"BioSpectator — SillaJen Pexa-Vec PHOCUS early termination","score_components":{"eps_fcf_explosion":0,"earnings_visibility":0,"bottleneck_pricing":0,"market_mispricing":20,"valuation_rerating":5,"capital_allocation":5,"information_confidence":5},"score_total_current_proxy":5.25,"stock_web_manifest_max_date":"2026-02-20","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","corporate_action_contaminated_180D_window":false,"insufficient_forward_window":false,"source_proxy_only":false,"evidence_url_pending":false}
{"case_id":"C24_084990_2024_01_04_VM202_DPN_phase3_failure_overkill_buffer","symbol":"084990","name":"헬릭스미스","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_endpoint_failure_but_price_overkill_buffer","trigger_type":"Stage4B","trigger_family":"VM202_DPN_phase3_2_failure_overkill_buffer","trigger_date":"2024-01-04","entry_date":"2024-01-04","entry_price":3935,"MFE_30D_pct":89.0724,"MAE_30D_pct":-17.4079,"MFE_90D_pct":89.0724,"MAE_90D_pct":-17.4079,"MFE_180D_pct":89.0724,"MAE_180D_pct":-17.4079,"peak_date_180D":"2024-02-06","peak_price_180D":7440,"drawdown_after_peak_180D_pct":-56.1156,"case_role":"counterexample","expected_stage_v12":"Stage4B","calibration_usable":true,"current_profile_error_type":"hard_4C_overkill_after_known_failure_when_relief_or_optionality_rally_occurs","evidence_summary":"반복된 엔젠시스 임상 실패는 thesis damage지만, 2024년 entry 시점 가격경로는 relief/optional value로 MFE가 크게 열렸다. hard 4C 대신 Stage4B + local watch가 더 맞았다.","source_url":"https://pharm.edaily.co.kr/news/read?newsId=01456326638754440","source_title":"팜이데일리 — 헬릭스미스 엔젠시스 임상 실패","score_components":{"eps_fcf_explosion":10,"earnings_visibility":10,"bottleneck_pricing":0,"market_mispricing":60,"valuation_rerating":35,"capital_allocation":20,"information_confidence":52},"score_total_current_proxy":39.35,"stock_web_manifest_max_date":"2026-02-20","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","corporate_action_contaminated_180D_window":false,"insufficient_forward_window":false,"source_proxy_only":false,"evidence_url_pending":false}
{"case_id":"C24_128940_2022_09_23_Poziotinib_ODAC_negative_portfolio_buffer","symbol":"128940","name":"한미약품","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_single_asset_negative_ODAC_diversified_pipeline_buffer","trigger_type":"Stage4B","trigger_family":"Poziotinib_ODAC_benefit_risk_negative_portfolio_buffer","trigger_date":"2022-09-23","entry_date":"2022-09-23","entry_price":237000,"MFE_30D_pct":10.1266,"MAE_30D_pct":-5.6962,"MFE_90D_pct":29.9578,"MAE_90D_pct":-5.6962,"MFE_180D_pct":43.2489,"MAE_180D_pct":-5.6962,"peak_date_180D":"2023-04-14","peak_price_180D":339500,"drawdown_after_peak_180D_pct":-14.433,"case_role":"counterexample","expected_stage_v12":"Stage4B","calibration_usable":true,"current_profile_error_type":"single_asset_regulatory_failure_should_not_hard_4C_diversified_pharma","evidence_summary":"포지오티닙 ODAC 비권고는 부정적 trial/regulatory event지만, 다품목·다파이프라인 제약사는 hard 4C로 전체 thesis를 닫으면 과잉 방어가 된다.","source_url":"https://www.yna.co.kr/view/AKR20220923024600017","source_title":"연합뉴스 — FDA 자문위 포지오티닙 신속승인 비권고","score_components":{"eps_fcf_explosion":40,"earnings_visibility":45,"bottleneck_pricing":25,"market_mispricing":55,"valuation_rerating":38,"capital_allocation":60,"information_confidence":58},"score_total_current_proxy":52.3,"stock_web_manifest_max_date":"2026-02-20","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","corporate_action_contaminated_180D_window":false,"insufficient_forward_window":false,"source_proxy_only":false,"evidence_url_pending":false}
{"case_id":"C24_028300_2024_05_17_Rivoceranib_Camrelizumab_CRL_nonclinical_boundary","symbol":"028300","name":"HLB","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_CRL_nonclinical_GMP_BIMO_boundary","trigger_type":"Stage4B","trigger_family":"Rivoceranib_Camrelizumab_CRL_nonclinical_BIMO_GMP_boundary","trigger_date":"2024-05-17","entry_date":"2024-05-17","entry_price":67100,"MFE_30D_pct":9.9851,"MAE_30D_pct":-32.7124,"MFE_90D_pct":46.1997,"MAE_90D_pct":-32.7124,"MFE_180D_pct":46.1997,"MAE_180D_pct":-32.7124,"peak_date_180D":"2024-07-08","peak_price_180D":98100,"drawdown_after_peak_180D_pct":-40.0612,"case_role":"counterexample","expected_stage_v12":"Stage4B","calibration_usable":true,"current_profile_error_type":"CRL_reason_split_needed_clinical_failure_vs_nonclinical_inspection","evidence_summary":"CRL은 강한 4B/4C 이벤트지만, clinical efficacy/safety thesis break인지 GMP/BIMO/inspection gap인지 분리해야 한다. HLB는 high-MAE였지만 90D MFE도 크게 열려 hard 4C 단정은 과했다.","source_url":"https://elevartx.com/2024/09/23/elevar-therapeutics-resubmits-new-drug-application/","source_title":"Elevar — Rivoceranib+Camrelizumab NDA resubmission and CRL context","score_components":{"eps_fcf_explosion":10,"earnings_visibility":20,"bottleneck_pricing":10,"market_mispricing":55,"valuation_rerating":20,"capital_allocation":20,"information_confidence":60},"score_total_current_proxy":44.5,"stock_web_manifest_max_date":"2026-02-20","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","corporate_action_contaminated_180D_window":false,"insufficient_forward_window":false,"source_proxy_only":false,"evidence_url_pending":false}
{"case_id":"C24_310210_2025_04_30_VRN11_AACR_early_1a_smallN_interpretation_risk","symbol":"310210","name":"보로노이","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_early_phase_smallN_signal_interpretation_risk","trigger_type":"Stage4B","trigger_family":"VRN11_AACR_early_1a_smallN_interpretation_risk","trigger_date":"2025-04-30","entry_date":"2025-04-30","entry_price":95600,"MFE_30D_pct":19.3515,"MAE_30D_pct":-6.0669,"MFE_90D_pct":60.7741,"MAE_90D_pct":-6.0669,"MFE_180D_pct":167.2594,"MAE_180D_pct":-6.0669,"peak_date_180D":"2025-12-03","peak_price_180D":255500,"drawdown_after_peak_180D_pct":-32.0548,"case_role":"positive_with_4B_watch","expected_stage_v12":"Stage4B","calibration_usable":true,"current_profile_error_type":"early_smallN_data_should_not_be_hard_4C_but_needs_4B_local_risk_overlay","evidence_summary":"소수 환자 early data는 해석 리스크가 크다. 다만 가격경로는 큰 MFE를 열었기 때문에 hard 4C가 아니라 Stage4B watch + milestone progression gate가 맞았다.","source_url":"https://pharm.edaily.co.kr/news/read?newsId=02164806642141368","source_title":"팜이데일리 — 보로노이 VRN11 AACR early clinical data and price reaction","score_components":{"eps_fcf_explosion":25,"earnings_visibility":35,"bottleneck_pricing":45,"market_mispricing":70,"valuation_rerating":35,"capital_allocation":35,"information_confidence":72},"score_total_current_proxy":58.85,"stock_web_manifest_max_date":"2026-02-20","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","corporate_action_contaminated_180D_window":false,"insufficient_forward_window":false,"source_proxy_only":false,"evidence_url_pending":false}
```

## 8. Machine-readable score simulation JSONL

```jsonl
{"case_id":"C24_000100_2023_10_23_LASER_MARIPOSA_positive_PFS_bridge","symbol":"000100","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","score_weight_profile":"C24_BIO_TRIAL_DATA_EVENT_RISK_runtime_proxy","weights":{"eps_fcf_explosion":5,"earnings_visibility":15,"bottleneck_pricing":5,"market_mispricing":10,"valuation_rerating":5,"capital_allocation":5,"information_confidence":55},"score_components":{"eps_fcf_explosion":60,"earnings_visibility":80,"bottleneck_pricing":50,"market_mispricing":65,"valuation_rerating":55,"capital_allocation":45,"information_confidence":90},"score_total_current_proxy":78.5,"expected_stage_v12":"Stage3-Yellow","return_alignment":{"MFE_180D_pct":59.0323,"MAE_180D_pct":-11.4516,"drawdown_after_peak_180D_pct":-3.6511}}
{"case_id":"C24_039200_2023_10_23_MARIPOSA_royalty_milestone_trial_data_bridge","symbol":"039200","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","score_weight_profile":"C24_BIO_TRIAL_DATA_EVENT_RISK_runtime_proxy","weights":{"eps_fcf_explosion":5,"earnings_visibility":15,"bottleneck_pricing":5,"market_mispricing":10,"valuation_rerating":5,"capital_allocation":5,"information_confidence":55},"score_components":{"eps_fcf_explosion":50,"earnings_visibility":78,"bottleneck_pricing":48,"market_mispricing":68,"valuation_rerating":50,"capital_allocation":35,"information_confidence":88},"score_total_current_proxy":76.05,"expected_stage_v12":"Stage3-Yellow","return_alignment":{"MFE_180D_pct":104.119,"MAE_180D_pct":-17.6201,"drawdown_after_peak_180D_pct":-7.7354}}
{"case_id":"C24_215600_2019_08_02_PexaVec_PHOCUS_DMC_futility_stop","symbol":"215600","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","score_weight_profile":"C24_BIO_TRIAL_DATA_EVENT_RISK_runtime_proxy","weights":{"eps_fcf_explosion":5,"earnings_visibility":15,"bottleneck_pricing":5,"market_mispricing":10,"valuation_rerating":5,"capital_allocation":5,"information_confidence":55},"score_components":{"eps_fcf_explosion":0,"earnings_visibility":0,"bottleneck_pricing":0,"market_mispricing":20,"valuation_rerating":5,"capital_allocation":5,"information_confidence":5},"score_total_current_proxy":5.25,"expected_stage_v12":"Stage4C","return_alignment":{"MFE_180D_pct":0.0,"MAE_180D_pct":-74.9359,"drawdown_after_peak_180D_pct":-74.9359}}
{"case_id":"C24_084990_2024_01_04_VM202_DPN_phase3_failure_overkill_buffer","symbol":"084990","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","score_weight_profile":"C24_BIO_TRIAL_DATA_EVENT_RISK_runtime_proxy","weights":{"eps_fcf_explosion":5,"earnings_visibility":15,"bottleneck_pricing":5,"market_mispricing":10,"valuation_rerating":5,"capital_allocation":5,"information_confidence":55},"score_components":{"eps_fcf_explosion":10,"earnings_visibility":10,"bottleneck_pricing":0,"market_mispricing":60,"valuation_rerating":35,"capital_allocation":20,"information_confidence":52},"score_total_current_proxy":39.35,"expected_stage_v12":"Stage4B","return_alignment":{"MFE_180D_pct":89.0724,"MAE_180D_pct":-17.4079,"drawdown_after_peak_180D_pct":-56.1156}}
{"case_id":"C24_128940_2022_09_23_Poziotinib_ODAC_negative_portfolio_buffer","symbol":"128940","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","score_weight_profile":"C24_BIO_TRIAL_DATA_EVENT_RISK_runtime_proxy","weights":{"eps_fcf_explosion":5,"earnings_visibility":15,"bottleneck_pricing":5,"market_mispricing":10,"valuation_rerating":5,"capital_allocation":5,"information_confidence":55},"score_components":{"eps_fcf_explosion":40,"earnings_visibility":45,"bottleneck_pricing":25,"market_mispricing":55,"valuation_rerating":38,"capital_allocation":60,"information_confidence":58},"score_total_current_proxy":52.3,"expected_stage_v12":"Stage4B","return_alignment":{"MFE_180D_pct":43.2489,"MAE_180D_pct":-5.6962,"drawdown_after_peak_180D_pct":-14.433}}
{"case_id":"C24_028300_2024_05_17_Rivoceranib_Camrelizumab_CRL_nonclinical_boundary","symbol":"028300","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","score_weight_profile":"C24_BIO_TRIAL_DATA_EVENT_RISK_runtime_proxy","weights":{"eps_fcf_explosion":5,"earnings_visibility":15,"bottleneck_pricing":5,"market_mispricing":10,"valuation_rerating":5,"capital_allocation":5,"information_confidence":55},"score_components":{"eps_fcf_explosion":10,"earnings_visibility":20,"bottleneck_pricing":10,"market_mispricing":55,"valuation_rerating":20,"capital_allocation":20,"information_confidence":60},"score_total_current_proxy":44.5,"expected_stage_v12":"Stage4B","return_alignment":{"MFE_180D_pct":46.1997,"MAE_180D_pct":-32.7124,"drawdown_after_peak_180D_pct":-40.0612}}
{"case_id":"C24_310210_2025_04_30_VRN11_AACR_early_1a_smallN_interpretation_risk","symbol":"310210","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","score_weight_profile":"C24_BIO_TRIAL_DATA_EVENT_RISK_runtime_proxy","weights":{"eps_fcf_explosion":5,"earnings_visibility":15,"bottleneck_pricing":5,"market_mispricing":10,"valuation_rerating":5,"capital_allocation":5,"information_confidence":55},"score_components":{"eps_fcf_explosion":25,"earnings_visibility":35,"bottleneck_pricing":45,"market_mispricing":70,"valuation_rerating":35,"capital_allocation":35,"information_confidence":72},"score_total_current_proxy":58.85,"expected_stage_v12":"Stage4B","return_alignment":{"MFE_180D_pct":167.2594,"MAE_180D_pct":-6.0669,"drawdown_after_peak_180D_pct":-32.0548}}
```

## 9. Aggregate row

```json
{
  "aggregate_id": "R7_loop_98_C24_trial_data_event_risk_quality_holdout",
  "selected_round": "R7",
  "selected_loop": 98,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK",
  "calibration_usable_rows": 7,
  "representative_rows": 7,
  "positive_case_count": 3,
  "counterexample_count": 4,
  "stage4B_case_count": 4,
  "stage4C_case_count": 1,
  "current_profile_error_count": 5,
  "avg_MFE_90D_pct": 36.3616,
  "avg_MAE_90D_pct": -23.6987,
  "avg_MFE_180D_pct": 72.7045,
  "avg_MAE_180D_pct": -23.6987,
  "do_not_propose_new_weight_delta": false
}
```

## 10. Shadow rule candidate

```text
C24_TRIAL_DATA_EVENT_RISK_SPLIT_ENDPOINT_CONFIRMED_HARD_4C_VS_EARLY_DATA_OR_PORTFOLIO_BUFFER_4B
```

Rule sketch:

```yaml
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
new_axis_proposed: C24_TRIAL_DATA_EVENT_RISK_REQUIRES_ENDPOINT_MATURITY_AND_SIGNAL_SOURCE_SPLIT_WITH_HARD_4C_OVERKILL_BUFFER
hard_4c_required_when:
  - DMC futility recommendation
  - randomized endpoint miss with no credible residual registration path
  - clinical efficacy/safety thesis break, not just filing inspection delay
stage4b_required_when:
  - ODAC / CRL / regulatory delay is asset-specific or nonclinical and company has portfolio buffer
  - early small-N data is ambiguous or market interpretation is unstable
  - MFE opens but peak-to-trough drawdown exceeds local 4B guard
stage3_yellow_allowed_when:
  - mature phase-3 endpoint success
  - regulatory filing/approval path exists
  - commercialization, royalty, milestone, or reimbursement bridge is visible
existing_axis_strengthened:
  - hard_4c_thesis_break_routes_to_4c when confirmed futility or endpoint failure is asset-level
  - full_4b_requires_non_price_evidence
  - local_4b_watch_guard
existing_axis_weakened:
  - hard_4c_thesis_break_routes_to_4c for nonclinical/GMP/BIMO CRL, early-data interpretation, or diversified-pipeline single-asset events
```

## 11. Residual contribution summary

```yaml
loop_contribution_label: canonical_archetype_rule_candidate
new_independent_case_count: 7
reused_symbol_from_index_top_covered_count: 3
reused_case_count: 0
same_archetype_new_trigger_family_count: 7
same_archetype_new_symbol_count: 4
positive_case_count: 3
counterexample_count: 4
4B_case_count: 4
4C_case_count: 1
current_profile_error_count: 5
diversity_score_summary: "7 trigger families / mature-positive 2 / hard-4C 1 / hard-4C-overkill buffers 3 / early-data positive-with-4B 1"
auto_selected_coverage_gap: "C24 static 69 rows; quality holdout selected only because C24 trial-event 4B/4C split remains high-impact"
sector_specific_rule_candidate: L7_C24_TRIAL_EVENT_ENDPOINT_MATURITY_AND_REGULATORY_REASON_SPLIT
canonical_archetype_rule_candidate: C24_TRIAL_DATA_EVENT_RISK_SPLIT_ENDPOINT_CONFIRMED_HARD_4C_VS_EARLY_DATA_OR_PORTFOLIO_BUFFER_4B
```

## 12. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
jsonl_trigger_row_count: 7
calibration_usable_rows: 7
representative_rows: 7
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
screened_out_corporate_action_contaminated_candidates:
  - 140410_MEZZION_2022_FDA_CRL_window
  - 235980_MEDPACTO_2023_trial_data_window
  - 084990_HELIXMITH_2019_VM202_original_window
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 13. Deferred Coding Agent Handoff Prompt

```text
You are the deferred coding agent for stock_agent. Do not execute this during the research session.

Input MD:
e2r_stock_web_v12_residual_round_R7_loop_98_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md

Task:
1. Parse the JSONL trigger rows and score_simulation rows.
2. Validate that every calibration_usable row has entry_date, entry_price, MFE_30D_pct, MAE_30D_pct, MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, MAE_180D_pct.
3. Confirm no corporate-action contamination in the entry_date~180D windows using stock-web symbol profiles.
4. Do not mutate production scoring directly.
5. Add this file to batch calibration intake only if the filename, metadata, and canonical IDs match.
6. Candidate shadow rule to evaluate:
   C24_TRIAL_DATA_EVENT_RISK_SPLIT_ENDPOINT_CONFIRMED_HARD_4C_VS_EARLY_DATA_OR_PORTFOLIO_BUFFER_4B
7. Evaluate whether C24 hard_4c_thesis_break_routes_to_4c needs a reason-code split:
   - confirmed futility / endpoint miss = hard 4C
   - small-N early data / nonclinical CRL / diversified pharma single-asset event = Stage4B unless price/evidence confirms thesis break
8. Produce a proposed patch only in a separate implementation session.
```

## 14. Next recommended archetypes

```yaml
next_recommended_archetypes:
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only
  - C24_BIO_TRIAL_DATA_EVENT_RISK_holdout_only_if_new_endpoint_or_regulatory_reason_code
  - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_quality_holdout
```
