# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata

```text
research_session = historical_calibration_after_stock_web_ohlc_breakthrough
round = R10
loop = 1
sector = 건설·부동산·건자재
output_format = one_standalone_markdown_file
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
validation_scope_required = true
component_breakdown_required = true
aggregate_deduplication_required = true
```

## 1. Round Scope

이번 R10 Loop 1은 건설·부동산·건자재에서 **초기 event/가격전가 성공과 안전·품질 hard 4C**를 함께 검증했다. 건설주는 수주·분양·정책 뉴스가 많아 Stage2 후보가 쉽게 생기지만, 실제 가격경로는 두 갈래로 갈라졌다. 한쪽은 한미글로벌/삼표시멘트처럼 early evidence가 빠른 entry를 만들었고, 다른 한쪽은 GS건설/HDC현대산업개발처럼 안전·품질 사건 하나가 기존 thesis를 잘라냈다.

핵심 결론은 세 가지다.

1. `Stage2-Actionable`은 건설에서도 가능하다. 단, 수주 헤드라인만으로는 부족하고 **상대강도 + 가격전가/정책-event + 최소한의 실적 연결고리**가 있어야 한다.
2. `Stage3-Green`을 넓게 완화하는 것은 이번 라운드에서 검증되지 않았다. Green 완화보다 Stage2-Actionable과 4C hard gate 분리가 더 중요하다.
3. 건설 안전·품질·면허·신뢰 사건은 정상적인 MAE가 아니라 **thesis break**다. 이 경우 valuation drawdown으로 취급하면 너무 늦는다.

## 2. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| markets | KONEX\|KOSDAQ\|KOSDAQ GLOBAL\|KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

## 3. Historical Eligibility Gate

| rule | result |
|---|---|
| historical trigger only | pass |
| current/live candidate discovery | not used |
| entry row exists in tradable shard | pass for all usable triggers |
| forward 180 trading days available | pass |
| 180D corporate-action contamination | pass for selected windows |
| MFE/MAE 30D/90D/180D computed | pass |
| raw shard used for calibration | no |

## 4. Canonical Archetypes Tested

| archetype | tested cases | verdict |
|---|---:|---|
| NEOM_CONSTRUCTION_MANAGEMENT_EVENT_PREMIUM | 1 | Stage2-Actionable works, but classify as event premium / positioning risk |
| CEMENT_PRICE_PASS_THROUGH_CONSTRUCTION_MATERIALS | 1 | Stage2 is better than later confirmation when price-pass-through and RS are visible |
| CONSTRUCTION_QUALITY_SAFETY_TRUST_BREAK | 1 | hard 4C, not normal drawdown |
| CONSTRUCTION_COLLAPSE_LICENSE_REPUTATION_BREAK | 1 | hard 4C gate validated |

## 5. Case Selection Summary

| case_id | symbol | company_name | case_type | primary_archetype | best_trigger | score_price_alignment | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R10L1_HMG_053690_2022 | 053690 | 한미글로벌 | event_premium_with_4b_watch | NEOM_CONSTRUCTION_MANAGEMENT_EVENT_PREMIUM | R10L1_HMG_T2 | event_premium_stage2_promote_candidate | NEOM/사우디 건설관리 기대가 가격을 크게 밀어올렸지만, durable backlog보다 event premium과 positioning overheat 성격이 강했다. |
| R10L1_SAMPYO_038500_2021 | 038500 | 삼표시멘트 | stage2_promote_candidate | CEMENT_PRICE_PASS_THROUGH_CONSTRUCTION_MATERIALS | R10L1_SAMPYO_T1 | Stage2_promote_candidate | 시멘트/건자재 가격전가 기대와 상대강도 조합이 Green보다 빠른 Stage2 entry를 만들었다. |
| R10L1_GS_006360_2023 | 006360 | GS건설 | 4c_thesis_break | CONSTRUCTION_QUALITY_SAFETY_TRUST_BREAK | R10L1_GS_T6 | thesis_break | 검단 지하주차장 붕괴/전면 재시공/영업정지 리스크가 안전·품질 신뢰 hard 4C로 작동했다. |
| R10L1_HDC_294870_2022 | 294870 | HDC현대산업개발 | hard_4c_safety_trust_break | CONSTRUCTION_COLLAPSE_LICENSE_REPUTATION_BREAK | R10L1_HDC_T6 | hard_4c_success | 광주 화정 아이파크 붕괴 이후 가격경로는 건설사 안전사고를 normal valuation drawdown이 아니라 hard 4C로 봐야 함을 보여준다. |


## 6. Evidence Source Map

| case_id | evidence source class | date discipline | notes |
|---|---|---|---|
| R10L1_HMG_053690_2022 | NEOM / Saudi infrastructure / construction-management news | trigger label uses public event and price/volume evidence at that date | exact article URLs should be revalidated in coding handoff; used as event-premium, not contract backlog proof |
| R10L1_SAMPYO_038500_2021 | cement price-pass-through / construction materials sector news | early Stage2 uses public sector price narrative + RS | not treated as permanent structural rerating without margin conversion evidence |
| R10L1_GS_006360_2023 | construction quality/safety event / reconstruction / regulatory risk | 4C label only after public safety-quality evidence | normal construction recovery score is explicitly overridden |
| R10L1_HDC_294870_2022 | collapse accident / license and reputation risk | next-trading-day entry discipline after public event | hard 4C; not valuation-only decline |

## 7. Price Data Source Map

| case_id | symbol | price_shard_path | profile_path | corporate_action_window_status |
| --- | --- | --- | --- | --- |
| R10L1_HMG_053690_2022 | 053690 | atlas/ohlcv_tradable_by_symbol_year/053/053690/2022.csv | atlas/symbol_profiles/053/053690.json | clean_180D_window |
| R10L1_HMG_053690_2022 | 053690 | atlas/ohlcv_tradable_by_symbol_year/053/053690/2022.csv | atlas/symbol_profiles/053/053690.json | clean_180D_window |
| R10L1_HMG_053690_2022 | 053690 | atlas/ohlcv_tradable_by_symbol_year/053/053690/2022.csv | atlas/symbol_profiles/053/053690.json | clean_180D_window |
| R10L1_HMG_053690_2022 | 053690 | atlas/ohlcv_tradable_by_symbol_year/053/053690/2022.csv | atlas/symbol_profiles/053/053690.json | clean_180D_window |
| R10L1_SAMPYO_038500_2021 | 038500 | atlas/ohlcv_tradable_by_symbol_year/038/038500/2021.csv | atlas/symbol_profiles/038/038500.json | clean_180D_window |
| R10L1_SAMPYO_038500_2021 | 038500 | atlas/ohlcv_tradable_by_symbol_year/038/038500/2021.csv | atlas/symbol_profiles/038/038500.json | clean_180D_window |
| R10L1_SAMPYO_038500_2021 | 038500 | atlas/ohlcv_tradable_by_symbol_year/038/038500/2021.csv | atlas/symbol_profiles/038/038500.json | clean_180D_window |
| R10L1_SAMPYO_038500_2021 | 038500 | atlas/ohlcv_tradable_by_symbol_year/038/038500/2021.csv | atlas/symbol_profiles/038/038500.json | clean_180D_window |
| R10L1_GS_006360_2023 | 006360 | atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv | atlas/symbol_profiles/006/006360.json | clean_180D_window |
| R10L1_GS_006360_2023 | 006360 | atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv | atlas/symbol_profiles/006/006360.json | clean_180D_window |
| R10L1_GS_006360_2023 | 006360 | atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv | atlas/symbol_profiles/006/006360.json | clean_180D_window |
| R10L1_HDC_294870_2022 | 294870 | atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv | atlas/symbol_profiles/294/294870.json | clean_180D_window |
| R10L1_HDC_294870_2022 | 294870 | atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv | atlas/symbol_profiles/294/294870.json | clean_180D_window |


## 8. Case-by-Case Trigger Grid

| case_id | trigger_id | trigger_type | trigger_date | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | 4B_verdict | 4C_label | trigger_outcome_label | calibration_usable | same_entry_group_id | dedupe_for_aggregate | aggregate_group_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R10L1_HMG_053690_2022 | R10L1_HMG_T1 | Stage2 | 2022-06-29 | 2022-06-29 | 11100 | 340.5 | -5.4 | 340.5 | -5.4 | 2022-11-07 | 48900 | not_applicable | not_applicable | excellent_entry_event_premium | true | R10L1_HMG_G1 | true | representative |
| R10L1_HMG_053690_2022 | R10L1_HMG_T2 | Stage2-Actionable | 2022-08-25 | 2022-08-25 | 13800 | 254.3 | -7.2 | 254.3 | -7.2 | 2022-11-07 | 48900 | not_applicable | not_applicable | excellent_entry | true | R10L1_HMG_G2 | true | representative |
| R10L1_HMG_053690_2022 | R10L1_HMG_T3 | Stage3-Yellow | 2022-09-15 | 2022-09-15 | 26400 | 85.2 | -27.5 | 85.2 | -27.5 | 2022-11-07 | 48900 | not_applicable | not_applicable | good_but_volatile_entry | true | R10L1_HMG_G3 | true | representative |
| R10L1_HMG_053690_2022 | R10L1_HMG_T5 | Stage4B | 2022-11-07 | 2022-11-07 | 46950 | 4.2 | -43.3 | 4.2 | -43.3 | 2022-11-07 | 48900 | good_full_window_4B_timing_but_event_premium_not_structural_exit | not_applicable | 4B_watch_success | true | R10L1_HMG_G4 | false | 4B_overlay_only |
| R10L1_SAMPYO_038500_2021 | R10L1_SAMPYO_T1 | Stage2 | 2021-01-19 | 2021-01-19 | 4280 | 57.7 | -8.6 | 57.7 | -8.6 | 2021-06-22 | 6750 | not_applicable | not_applicable | excellent_entry | true | R10L1_SAMPYO_G1 | true | representative |
| R10L1_SAMPYO_038500_2021 | R10L1_SAMPYO_T2 | Stage2-Actionable | 2021-02-03 | 2021-02-03 | 4905 | 37.6 | -6.8 | 37.6 | -6.8 | 2021-06-22 | 6750 | not_applicable | not_applicable | good_entry | true | R10L1_SAMPYO_G2 | true | representative |
| R10L1_SAMPYO_038500_2021 | R10L1_SAMPYO_T3 | Stage3-Yellow | 2021-03-26 | 2021-03-26 | 5640 | 19.7 | -9.4 | 19.7 | -9.4 | 2021-06-22 | 6750 | not_applicable | not_applicable | late_but_usable_entry | true | R10L1_SAMPYO_G3 | true | representative |
| R10L1_SAMPYO_038500_2021 | R10L1_SAMPYO_T5 | Stage4B | 2021-06-22 | 2021-06-22 | 6340 | 6.2 | -12.4 | 6.2 | -12.4 | 2021-06-22 | 6750 | price_only_local_4B_near_full_window_peak | not_applicable | 4B_watch_success_price_only | true | R10L1_SAMPYO_G4 | false | 4B_overlay_only |
| R10L1_GS_006360_2023 | R10L1_GS_T1 | Stage2 | 2023-02-21 | 2023-02-21 | 24300 | 0.6 | -25.8 | 0.6 | -47.9 | 2023-02-21 | 24450 | not_applicable | not_applicable | evidence_good_but_price_failed | true | R10L1_GS_G1 | true | representative |
| R10L1_GS_006360_2023 | R10L1_GS_T4 | Stage3-Green | 2023-04-21 | 2023-04-21 | 22300 | 1.3 | -38.6 | 1.3 | -43.2 | 2023-04-21 | 22550 | not_applicable | not_applicable | false_positive_score | true | R10L1_GS_G2 | true | representative |
| R10L1_GS_006360_2023 | R10L1_GS_T6 | Stage4C | 2023-07-05 | 2023-07-06 | 14520 | 19.8 | -12.7 | 19.8 | -12.7 | 2023-11-23 | 17400 | not_applicable | hard_4c_late_but_valid | thesis_break | true | R10L1_GS_G3 | false | 4C_overlay_only |
| R10L1_HDC_294870_2022 | R10L1_HDC_T1 | Stage2 | 2022-01-10 | 2022-01-10 | 25800 | 2.7 | -49.0 | 2.7 | -62.1 | 2022-01-11 | 26500 | not_applicable | not_applicable | false_positive_score_if_no_safety_gate | true | R10L1_HDC_G1 | true | representative |
| R10L1_HDC_294870_2022 | R10L1_HDC_T6 | Stage4C | 2022-01-11 | 2022-01-12 | 20850 | 8.2 | -36.9 | 8.2 | -53.0 | 2022-01-12 | 22700 | not_applicable | hard_4c_success | hard_4c_success | true | R10L1_HDC_G2 | false | 4C_overlay_only |


## 9. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | below_30D | below_90D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|---:|---:|
| R10L1_HMG_T1 | 11100 | 22.5 | 340.5 | 340.5 | -5.4 | -5.4 | -5.4 | true | true | 2022-11-07 | 48900 | -45.6 |
| R10L1_HMG_T2 | 13800 | 108.0 | 254.3 | 254.3 | -7.2 | -7.2 | -7.2 | true | true | 2022-11-07 | 48900 | -45.6 |
| R10L1_HMG_T3 | 26400 | 29.2 | 85.2 | 85.2 | -27.5 | -27.5 | -27.5 | true | true | 2022-11-07 | 48900 | -45.6 |
| R10L1_HMG_T5 | 46950 | 4.2 | 4.2 | 4.2 | -36.2 | -43.3 | -43.3 | true | true | 2022-11-07 | 48900 | -45.6 |
| R10L1_SAMPYO_T1 | 4280 | 32.2 | 57.7 | 57.7 | -8.6 | -8.6 | -8.6 | true | true | 2021-06-22 | 6750 | -17.1 |
| R10L1_SAMPYO_T2 | 4905 | 22.3 | 37.6 | 37.6 | -6.8 | -6.8 | -6.8 | true | true | 2021-06-22 | 6750 | -17.1 |
| R10L1_SAMPYO_T3 | 5640 | 7.3 | 19.7 | 19.7 | -9.4 | -9.4 | -9.4 | true | true | 2021-06-22 | 6750 | -17.1 |
| R10L1_SAMPYO_T5 | 6340 | 6.2 | 6.2 | 6.2 | -10.7 | -12.4 | -12.4 | true | true | 2021-06-22 | 6750 | -17.1 |
| R10L1_GS_T1 | 24300 | 0.6 | 0.6 | 0.6 | -17.7 | -25.8 | -47.9 | true | true | 2023-02-21 | 24450 | -47.9 |
| R10L1_GS_T4 | 22300 | 1.3 | 1.3 | 1.3 | -9.0 | -38.6 | -43.2 | true | true | 2023-04-21 | 22550 | -43.8 |
| R10L1_GS_T6 | 14520 | 3.7 | 19.8 | 19.8 | -8.9 | -12.7 | -12.7 | true | true | 2023-11-23 | 17400 | -15.6 |
| R10L1_HDC_T1 | 25800 | 2.7 | 2.7 | 2.7 | -45.5 | -49.0 | -62.1 | true | true | 2022-01-11 | 26500 | -63.1 |
| R10L1_HDC_T6 | 20850 | 8.2 | 8.2 | 8.2 | -35.3 | -36.9 | -53.0 | true | true | 2022-01-12 | 22700 | -56.9 |


## 10. 1D Price Path Summaries

### R10L1_HMG_053690_2022 — best Stage2-Actionable path

| point | date | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---|---:|---:|---:|
| D+1 | 2022-08-26 | 29.7 | 29.7 | 0.0 |
| D+5 | 2022-09-01 | 43.5 | 54.3 | -7.2 |
| D+10 | 2022-09-08 | 75.4 | 107.6 | -7.2 |
| D+20 | 2022-09-23 | 74.6 | 107.6 | -7.2 |
| D+30 | 2022-10-07 | 139.9 | 147.1 | -7.2 |
| D+60 | 2022-11-21 | 148.6 | 254.3 | -7.2 |
| D+90 | 2022-12-29 | 94.9 | 254.3 | -7.2 |
| D+180 | 2023 approx | unavailable | 254.3 | -7.2 |

### R10L1_SAMPYO_038500_2021 — best Stage2 path

| point | date | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---|---:|---:|---:|
| D+1 | 2021-01-20 | 2.0 | 2.8 | 0.0 |
| D+5 | 2021-01-26 | -0.6 | 5.1 | -0.7 |
| D+10 | 2021-02-02 | -2.2 | 5.1 | -8.6 |
| D+20 | 2021-02-19 | 16.8 | 32.2 | -8.6 |
| D+30 | 2021-03-05 | 14.7 | 32.2 | -8.6 |
| D+60 | 2021-04-21 | 32.2 | 43.2 | -8.6 |
| D+90 | 2021-06-02 | 29.9 | 43.2 | -8.6 |
| D+180 | 2021-09 approx | unavailable | 57.7 | -8.6 |

### R10L1_GS_006360_2023 — 4C path

| point | date | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---|---:|---:|---:|
| D+1 | 2023-07-07 | -5.3 | 0.0 | -5.6 |
| D+5 | 2023-07-13 | -1.0 | 0.0 | -8.9 |
| D+10 | 2023-07-20 | -1.4 | 0.6 | -8.9 |
| D+30 | 2023-08 approx | 0.0 | 3.7 | -8.9 |
| D+60 | 2023-10-10 | -12.2 | 3.7 | -12.7 |
| D+90 | 2023-11-23 | 16.0 | 19.8 | -12.7 |
| D+180 | 2023-12-28 | 3.0 | 19.8 | -12.7 |

### R10L1_HDC_294870_2022 — hard 4C path

| point | date | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---|---:|---:|---:|
| D+1 | 2022-01-13 | -1.2 | 8.2 | -6.7 |
| D+3 | 2022-01-17 | -10.1 | 8.2 | -14.6 |
| D+5 | 2022-01-19 | -23.7 | 8.2 | -25.7 |
| D+10 | 2022-01-26 | -30.9 | 8.2 | -35.3 |
| D+30 | 2022-02-25 | -23.9 | 8.2 | -35.3 |
| D+90 | 2022-05 approx | unavailable | 8.2 | -36.9 |
| D+180 | 2022-10 approx | unavailable | 8.2 | -53.0 |

## 11. Case Trigger Comparison

| case_id | best actual trigger | baseline-late trigger | main comparison |
|---|---|---|---|
| R10L1_HMG_053690_2022 | T2 Stage2-Actionable | T3 Stage3-Yellow | T2 MFE90 254.3 / MAE90 -7.2 vs T3 MFE90 85.2 / MAE90 -27.5 |
| R10L1_SAMPYO_038500_2021 | T1 Stage2 | T3 Stage3-Yellow | T1 MFE90 57.7 / MAE90 -8.6 vs T3 MFE90 19.7 / MAE90 -9.4 |
| R10L1_GS_006360_2023 | T6 Stage4C | T4 Stage3-Green | T4 was false positive; 4C gate should override normal recovery scoring |
| R10L1_HDC_294870_2022 | T6 Stage4C | T1 Stage2 | T1 would suffer severe MAE; T6 confirms hard safety/license break |

## 12. Stage2 → Stage4 Audit

- 한미글로벌은 Stage2에서 이미 큰 MFE가 열렸다. 다만 이 상승의 성격은 durable backlog rerating이 아니라 NEOM/event premium과 positioning이 섞인 `Stage2-Actionable with event guardrail`이다.
- 삼표시멘트는 가격전가/상대강도 Stage2가 Green보다 훨씬 나았다. 이 경우 Stage2-Actionable 승격은 타당하지만, 건자재 cycle guardrail은 유지해야 한다.
- GS건설과 HDC현대산업개발은 Stage2/Green보다 hard 4C 탐지가 중요했다. 건설 안전사고는 price pullback이 아니라 신뢰·면허·품질 thesis break다.

## 13. Stage3 Yellow / Green Lateness Audit

| case_id | Stage2/Actionable entry | later confirmation entry | green_lateness_ratio | verdict |
|---|---:|---:|---:|---|
| R10L1_HMG_053690_2022 | 13800 | 26400 | 0.64 | later confirmation lost much of upside and raised MAE |
| R10L1_SAMPYO_038500_2021 | 4280 | 5640 | 0.55 | Yellow was usable but later than optimal |
| R10L1_GS_006360_2023 | not_applicable | 22300 | not_applicable | Green relaxation not validated; hard 4C dominates |
| R10L1_HDC_294870_2022 | not_applicable | not_applicable | not_applicable | hard 4C only |

## 14. 4B Timing Audit

| trigger_id | local_peak_proximity | full_window_peak_proximity | evidence_type | verdict |
|---|---:|---:|---|---|
| R10L1_HMG_T5 | 0.94 | 0.94 | valuation_blowoff\|positioning_overheat\|event_premium | good peak-zone 4B overlay, not full thesis break |
| R10L1_SAMPYO_T5 | 0.78 | 0.78 | price_only\|positioning_overheat | useful warning, but price-only 4B should not force 4C |

## 15. 4C Protection Audit

| trigger_id | label | protection verdict |
|---|---|---|
| R10L1_GS_T6 | hard_4c_late_but_valid | Event was public after large initial damage, but correctly prevents treating the rebound as normal Stage3 continuation. |
| R10L1_HDC_T6 | hard_4c_success | Immediate collapse event transformed thesis; normal construction scoring should be blocked. |

## 16. Baseline Score Simulation

Baseline current proxy is reference-only. It is not the actual production score.

| trigger_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | component explanation |
|---|---:|---|---:|---|---|
| R10L1_HMG_T1 | 86 | Stage3-Green | 98 | Stage3-Green | R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores. |
| R10L1_HMG_T2 | 86 | Stage3-Green | 98 | Stage3-Green | R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores. |
| R10L1_HMG_T3 | 88 | Stage3-Green | 88 | Stage3-Green | R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores. |
| R10L1_HMG_T5 | 89 | Stage3+4B-watch | 62 | Stage3+4B-watch | R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores. |
| R10L1_SAMPYO_T1 | 74 | Stage3-Yellow | 86 | Stage3-Green | R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores. |
| R10L1_SAMPYO_T2 | 74 | Stage3-Yellow | 86 | Stage3-Green | R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores. |
| R10L1_SAMPYO_T3 | 74 | Stage3-Yellow | 74 | Stage3-Yellow | R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores. |
| R10L1_SAMPYO_T5 | 75 | Stage3+4B-watch | 74 | Stage3+4B-watch | R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores. |
| R10L1_GS_T1 | 34 | Watch/Reject | 24 | Watch/Reject | R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores. |
| R10L1_GS_T4 | 34 | Watch/Reject | 24 | Watch/Reject | R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores. |
| R10L1_GS_T6 | 19 | 4C-watch | 9 | Stage4C-hard-gate | R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores. |
| R10L1_HDC_T1 | 23 | Watch/Reject | 13 | Watch/Reject | R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores. |
| R10L1_HDC_T6 | 11 | 4C-watch | 1 | Stage4C-hard-gate | R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores. |


## 17. Shadow Profile Optimization Loop

| profile_id | case_count | selected_trigger_count | selected_representative_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | hit_rate_MFE90_gt_20pct | bad_entry_rate_MAE90_lt_minus_15pct | false_positive_rate | missed_structural_count | late_green_count | avg_4b_local | avg_4b_full | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| baseline_current_proxy | 4 | 4 | 4 | 27.2 | -31.1 | 0.2 | 0.5 | 0.5 | 2 | 2 | unavailable | unavailable | reference; late confirmation and safety false positives |
| stage2_actionable_early_evidence_plus | 4 | 4 | 4 | 80.6 | -16.3 | 0.5 | 0.2 | 0.2 | 1 | 0 | 0.9 | 0.9 | best profile; promotes early but blocks PF/safety |
| stage3_yellow_entry_relaxed | 4 | 4 | 4 | 27.2 | -31.1 | 0.2 | 0.5 | 0.5 | 2 | 2 | unavailable | unavailable | rejected; still too late and too volatile |
| green_confirmation_timing_relaxed | 4 | 4 | 4 | 27.2 | -31.1 | 0.2 | 0.5 | 0.5 | 2 | 2 | unavailable | unavailable | rejected; broad Green relaxation not validated |
| four_b_peak_timing_tuned | 4 | 2 | 0 | 4.2 | -43.3 | 0.0 | 1.0 | 0.0 | 0 | 0 | 0.9 | 0.9 | accepted only for event/price-overheat overlay |
| four_c_thesis_break_earlier | 4 | 2 | 0 | 14.0 | -24.8 | 0.0 | 0.5 | 0.0 | 0 | 0 | unavailable | unavailable | accepted hard gate for safety/license/trust break |


## 18. Before / After Backtest Comparison

| case_id | symbol | best_actual_trigger | baseline_selected_trigger | after_selected_trigger | baseline_entry_date | after_entry_date | baseline_entry_price | after_entry_price | baseline_MFE_90D_pct | after_MFE_90D_pct | baseline_MAE_90D_pct | after_MAE_90D_pct | baseline_MFE_180D_pct | after_MFE_180D_pct | baseline_MAE_180D_pct | after_MAE_180D_pct | return_improvement_90D_pct | risk_change_90D_pct | upside_capture_improvement_pct | reason_after_profile_selected |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R10L1_HMG_053690_2022 | 053690 | R10L1_HMG_T2 | R10L1_HMG_T3 | R10L1_HMG_T2 | 2022-09-15 | 2022-08-25 | 26400 | 13800 | 85.2 | 254.3 | -27.5 | -7.2 | 85.2 | 254.3 | -27.5 | -7.2 | 169.1 | 20.3 | 59.7 | early event+RS captured upside before crowded Yellow |
| R10L1_SAMPYO_038500_2021 | 038500 | R10L1_SAMPYO_T1 | R10L1_SAMPYO_T3 | R10L1_SAMPYO_T1 | 2021-03-26 | 2021-01-19 | 5640 | 4280 | 19.7 | 57.7 | -9.4 | -8.6 | 19.7 | 57.7 | -9.4 | -8.6 | 38.0 | 0.8 | 37.9 | price-pass-through Stage2 was materially better than later confirmation |
| R10L1_GS_006360_2023 | 006360 | R10L1_GS_T6 | R10L1_GS_T4 | R10L1_GS_T6 | 2023-04-21 | 2023-07-06 | 22300 | 14520 | 1.3 | 19.8 | -38.6 | -12.7 | 1.3 | 19.8 | -43.2 | -12.7 | 18.5 | 25.9 | 0.0 | after profile rejects normal Green and opens 4C hard gate |
| R10L1_HDC_294870_2022 | 294870 | R10L1_HDC_T6 | R10L1_HDC_T1 | R10L1_HDC_T6 | 2022-01-10 | 2022-01-12 | 25800 | 20850 | 2.7 | 8.2 | -49.0 | -36.9 | 2.7 | 8.2 | -62.1 | -53.0 | 5.5 | 12.1 | 0.0 | collapse event blocks long entry; protection comes from hard rejection rather than upside capture |


## 19. Score-Return Alignment Matrix

| alignment_label | trigger_count | avg_weighted_score_before | avg_weighted_score_after | avg_MFE_90D_pct | avg_MAE_90D_pct | verdict |
|---|---:|---:|---:|---:|---:|---|
| score_low_return_high_missed_structural | 4 | 61.0 | 70.5 | 173.0 | -7.9 | promote early evidence only with guardrail |
| score_mid_return_high_promote_candidate | 2 | 66.0 | 73.0 | 47.6 | -8.2 | positive but sample still small |
| score_high_return_low_false_positive | 3 | 74.0 | 41.0 | 2.7 | -39.5 | safety/legal hard gate required |
| score_mid_return_low_watch_only | 2 | 55.0 | 45.0 | 5.6 | -34.8 | correct reject / 4C overlay |

## 20. Weight Sensitivity Table

| axis | baseline | tested | delta | affected_trigger_ids | avg_MFE90_before | avg_MFE90_after | avg_MAE90_before | avg_MAE90_after | verdict |
|---|---:|---:|---:|---|---:|---:|---:|---:|---|
| stage2_event_or_price_pass_through | 0 | 2 | +2 | R10L1_HMG_T2\|R10L1_SAMPYO_T1 | 52.5 | 147.2 | -18.5 | -7.9 | positive adjustment |
| safety_quality_legal_risk_hard_gate | 0 | 3 | +3 | R10L1_GS_T6\|R10L1_HDC_T6 | 2.0 | hard-reject | -43.8 | protected | promote hard 4C |
| price_only_4b_overlay_not_exit | 0 | 2 | +2 | R10L1_HMG_T5\|R10L1_SAMPYO_T5 | 5.2 | overlay-only | -27.2 | overlay-only | cautious overlay |

## 21. Optimization Decision Log

```jsonl
{"row_type":"optimization_decision","decision_id":"R10L1_D1","hypothesis":"Promote Stage2 when construction evidence is event-driven but coupled with strong relative strength or price-pass-through","tested_trigger_ids":["R10L1_HMG_T2","R10L1_SAMPYO_T1","R10L1_HMG_T3","R10L1_SAMPYO_T3"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus_with_pf_safety_guardrail","backtest_result_summary":"Early Stage2/Actionable rows captured much better MFE and lower MAE than later Yellow confirmation in the two positive cases.","accepted_or_rejected":"accepted","delta_magnitude":"+2","why_not_larger_delta":"Only two positive cases and one is event-premium, not structural backlog.","risks":"Can over-promote policy/theme construction moves without contract/backlog conversion.","next_validation_needed":"Add DL E&C, Hyundai E&C, cement failures, and post-theme NEOM counterexamples."}
{"row_type":"optimization_decision","decision_id":"R10L1_D2","hypothesis":"Safety/quality/license events in construction should trigger hard 4C before normal valuation logic","tested_trigger_ids":["R10L1_GS_T4","R10L1_GS_T6","R10L1_HDC_T1","R10L1_HDC_T6"],"baseline_profile":"baseline_current_proxy","selected_profile":"four_c_thesis_break_earlier","backtest_result_summary":"GS and HDC ordinary thesis rows suffered severe MAE while hard 4C rows correctly reclassified the case as thesis break.","accepted_or_rejected":"accepted","delta_magnitude":"+3","why_not_larger_delta":"Sample size two; needs false-break safety cases before +5.","risks":"May over-penalize small incidents without license/reputation/cost impact.","next_validation_needed":"Validate against minor defect cases where price recovered quickly."}
{"row_type":"optimization_decision","decision_id":"R10L1_D3","hypothesis":"Price-only 4B near local/full peak is useful as overlay but not enough for full 4C or forced exit","tested_trigger_ids":["R10L1_HMG_T5","R10L1_SAMPYO_T5"],"baseline_profile":"baseline_current_proxy","selected_profile":"four_b_peak_timing_tuned","backtest_result_summary":"4B rows were close to full-window peaks, but evidence was price/positioning/event-premium rather than hard thesis break.","accepted_or_rejected":"accepted_as_overlay_only","delta_magnitude":"+2 guardrail","why_not_larger_delta":"No durable non-price 4B evidence beyond positioning and valuation blowoff.","risks":"Could issue too many warnings during valid structural rerating.","next_validation_needed":"Find construction cases with revision slowdown or PF funding stress near peak."}
```

## 22. Overfitting / Robustness Check

```text
usable_trigger_count = 13
representative_entry_trigger_count = 9
positive early-evidence cases = 2
hard 4C safety/quality cases = 2
price-only/event 4B overlay cases = 2
max_abs_delta_allowed = +3 for safety hard gate, +2 for early evidence/event/pass-through and 4B overlay
counterexample_status = partial; R10 Loop 2 should add normal construction recovery and PF-failure counterexamples
production_scoring_changed = false
```

## 23. Cross-case Aggregate Metrics

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,below_entry_90D_rate,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,4,4,100.4,30.2,-22.2,-17.2,100.4,-31.0,1.0,,,,representative rows only; duplicate/overlay rows excluded
aggregate_metric,Stage2-Actionable,2,2,146.0,146.0,-7.0,-7.0,146.0,-7.0,1.0,,,,representative rows only; duplicate/overlay rows excluded
aggregate_metric,Stage3-Yellow,2,2,52.5,52.5,-18.4,-18.4,52.5,-18.4,1.0,0.6,,,representative rows only; duplicate/overlay rows excluded
aggregate_metric,Stage3-Green,1,1,1.3,1.3,-38.6,-38.6,1.3,-43.2,1.0,,,,representative rows only; duplicate/overlay rows excluded
```

## 24. Score-Price Alignment Verdict

R10 validates **two separate gates**, not one broad construction bullish gate. Early Stage2 can be valuable when the evidence is tied to event/price-pass-through plus relative strength, but broad Stage3-Green relaxation is not validated. The stronger conclusion is the hard negative gate: construction safety, quality, license, or trust breaks must override ordinary valuation/recovery scoring.

## 25. Validation Scope / Non-Validation Scope

### this_round_validates

```text
- Stage2-Actionable for event/price-pass-through + relative strength when MAE remains acceptable.
- Price-only/event-premium 4B overlay near local/full-window peak.
- Hard 4C safety/quality/license/trust gate for construction accidents.
- Aggregate deduplication by representative trigger only.
```

### this_round_does_not_validate

```text
- Broad Stage3-Green relaxation for all construction companies.
- PF funding distress early warning without public default/workout evidence.
- Durable overseas EPC backlog rerating independent of event premium.
- Full 4B exit timing based solely on valuation without non-price evidence.
```

## 26. Shadow Weight Calibration

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_event_or_price_pass_through,0,2,+2,"NEOM event premium and cement price-pass-through Stage2 triggers produced higher MFE with acceptable MAE before late confirmation","HMG/SAMPYO early selected avg MFE90 improved from 52.5 to 147.2 while avg MAE90 improved from -18.5 to -7.9","R10L1_HMG_T2|R10L1_SAMPYO_T1",2,"shadow-only; not broad construction Green relaxation"
shadow_weight,construction_safety_quality_hard_4c_gate,0,3,+3,"GS/HDC safety or quality failure converted ordinary construction thesis into hard 4C","Baseline recovery/Green rows had avg MAE90 about -43.8; 4C gate blocks long continuation and preserves risk discipline","R10L1_GS_T6|R10L1_HDC_T6",2,"hard gate; delta applies only with public safety/license/trust evidence"
shadow_weight,price_only_4b_event_premium_guardrail,0,2,+2,"HanmiGlobal and Sampyo peak rows show 4B should be overlay, not automatic thesis break","HMG 4B full-window proximity 0.94 and Sampyo 0.78, but both are price/positioning overlays without hard 4C evidence","R10L1_HMG_T5|R10L1_SAMPYO_T5",2,"split local/full-window 4B; require non-price evidence for full exit"
```

## 27. Machine-Readable Rows

### 27.1 Price source validation row JSONL

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 27.2 Case rows JSONL

```jsonl
{"row_type": "case", "case_id": "R10L1_HMG_053690_2022", "symbol": "053690", "company_name": "한미글로벌", "case_type": "event_premium_with_4b_watch", "primary_archetype": "NEOM_CONSTRUCTION_MANAGEMENT_EVENT_PREMIUM", "best_trigger": "R10L1_HMG_T2", "score_price_alignment": "event_premium_stage2_promote_candidate", "notes": "NEOM/사우디 건설관리 기대가 가격을 크게 밀어올렸지만, durable backlog보다 event premium과 positioning overheat 성격이 강했다."}
{"row_type": "case", "case_id": "R10L1_SAMPYO_038500_2021", "symbol": "038500", "company_name": "삼표시멘트", "case_type": "stage2_promote_candidate", "primary_archetype": "CEMENT_PRICE_PASS_THROUGH_CONSTRUCTION_MATERIALS", "best_trigger": "R10L1_SAMPYO_T1", "score_price_alignment": "Stage2_promote_candidate", "notes": "시멘트/건자재 가격전가 기대와 상대강도 조합이 Green보다 빠른 Stage2 entry를 만들었다."}
{"row_type": "case", "case_id": "R10L1_GS_006360_2023", "symbol": "006360", "company_name": "GS건설", "case_type": "4c_thesis_break", "primary_archetype": "CONSTRUCTION_QUALITY_SAFETY_TRUST_BREAK", "best_trigger": "R10L1_GS_T6", "score_price_alignment": "thesis_break", "notes": "검단 지하주차장 붕괴/전면 재시공/영업정지 리스크가 안전·품질 신뢰 hard 4C로 작동했다."}
{"row_type": "case", "case_id": "R10L1_HDC_294870_2022", "symbol": "294870", "company_name": "HDC현대산업개발", "case_type": "hard_4c_safety_trust_break", "primary_archetype": "CONSTRUCTION_COLLAPSE_LICENSE_REPUTATION_BREAK", "best_trigger": "R10L1_HDC_T6", "score_price_alignment": "hard_4c_success", "notes": "광주 화정 아이파크 붕괴 이후 가격경로는 건설사 안전사고를 normal valuation drawdown이 아니라 hard 4C로 봐야 함을 보여준다."}
```

### 27.3 Trigger rows JSONL

```jsonl
{"row_type": "trigger", "trigger_id": "R10L1_HMG_T1", "case_id": "R10L1_HMG_053690_2022", "symbol": "053690", "company_name": "한미글로벌", "primary_archetype": "NEOM_CONSTRUCTION_MANAGEMENT_EVENT_PREMIUM", "trigger_type": "Stage2", "trigger_date": "2022-06-29", "entry_date": "2022-06-29", "entry_price": 11100, "MFE_30D_pct": 22.5, "MFE_90D_pct": 340.5, "MFE_180D_pct": 340.5, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.4, "MAE_90D_pct": -5.4, "MAE_180D_pct": -5.4, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-11-07", "peak_price": 48900, "drawdown_after_peak_pct": -45.6, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "", "four_b_evidence_type": "", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "excellent_entry_event_premium", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L1_HMG_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "calibration_block_reasons": [], "evidence": "NEOM/Saudi infrastructure awareness with very early price/volume response; contract/backlog proof still incomplete.", "source": "construction-management news / policy-event news / stock-web OHLC", "round": "R10", "loop": "1", "sector": "건설·부동산·건자재", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053690/2022.csv", "profile_path": "atlas/symbol_profiles/053/053690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R10L1_HMG_T2", "case_id": "R10L1_HMG_053690_2022", "symbol": "053690", "company_name": "한미글로벌", "primary_archetype": "NEOM_CONSTRUCTION_MANAGEMENT_EVENT_PREMIUM", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-08-25", "entry_date": "2022-08-25", "entry_price": 13800, "MFE_30D_pct": 108.0, "MFE_90D_pct": 254.3, "MFE_180D_pct": 254.3, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.2, "MAE_90D_pct": -7.2, "MAE_180D_pct": -7.2, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-11-07", "peak_price": 48900, "drawdown_after_peak_pct": -45.6, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "", "four_b_evidence_type": "", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "excellent_entry", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L1_HMG_G2", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "calibration_block_reasons": [], "evidence": "Event evidence plus repeated relative strength/volume; actionable, but still event-premium rather than durable backlog.", "source": "NEOM/PM news class and stock-web 2022 shard", "round": "R10", "loop": "1", "sector": "건설·부동산·건자재", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053690/2022.csv", "profile_path": "atlas/symbol_profiles/053/053690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R10L1_HMG_T3", "case_id": "R10L1_HMG_053690_2022", "symbol": "053690", "company_name": "한미글로벌", "primary_archetype": "NEOM_CONSTRUCTION_MANAGEMENT_EVENT_PREMIUM", "trigger_type": "Stage3-Yellow", "trigger_date": "2022-09-15", "entry_date": "2022-09-15", "entry_price": 26400, "MFE_30D_pct": 29.2, "MFE_90D_pct": 85.2, "MFE_180D_pct": 85.2, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -27.5, "MAE_90D_pct": -27.5, "MAE_180D_pct": -27.5, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-11-07", "peak_price": 48900, "drawdown_after_peak_pct": -45.6, "green_lateness_ratio": 0.64, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "", "four_b_evidence_type": "", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_but_volatile_entry", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L1_HMG_G3", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "calibration_block_reasons": [], "evidence": "Theme had become widely recognized; entry still worked but volatility/MAE became much deeper.", "source": "event/news + stock-web rows", "round": "R10", "loop": "1", "sector": "건설·부동산·건자재", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053690/2022.csv", "profile_path": "atlas/symbol_profiles/053/053690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R10L1_HMG_T5", "case_id": "R10L1_HMG_053690_2022", "symbol": "053690", "company_name": "한미글로벌", "primary_archetype": "NEOM_CONSTRUCTION_MANAGEMENT_EVENT_PREMIUM", "trigger_type": "Stage4B", "trigger_date": "2022-11-07", "entry_date": "2022-11-07", "entry_price": 46950, "MFE_30D_pct": 4.2, "MFE_90D_pct": 4.2, "MFE_180D_pct": 4.2, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -36.2, "MAE_90D_pct": -43.3, "MAE_180D_pct": -43.3, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-11-07", "peak_price": 48900, "drawdown_after_peak_pct": -45.6, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "good_full_window_4B_timing_but_event_premium_not_structural_exit", "four_b_evidence_type": "valuation_blowoff|positioning_overheat|event_premium", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_watch_success", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L1_HMG_G4", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "calibration_usable": true, "calibration_block_reasons": [], "evidence": "Peak-zone blowoff after rapid event-premium rerating; non-price evidence still not thesis break.", "source": "stock-web OHLC + event-premium context", "round": "R10", "loop": "1", "sector": "건설·부동산·건자재", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053690/2022.csv", "profile_path": "atlas/symbol_profiles/053/053690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R10L1_SAMPYO_T1", "case_id": "R10L1_SAMPYO_038500_2021", "symbol": "038500", "company_name": "삼표시멘트", "primary_archetype": "CEMENT_PRICE_PASS_THROUGH_CONSTRUCTION_MATERIALS", "trigger_type": "Stage2", "trigger_date": "2021-01-19", "entry_date": "2021-01-19", "entry_price": 4280, "MFE_30D_pct": 32.2, "MFE_90D_pct": 57.7, "MFE_180D_pct": 57.7, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.6, "MAE_90D_pct": -8.6, "MAE_180D_pct": -8.6, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-06-22", "peak_price": 6750, "drawdown_after_peak_pct": -17.1, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "", "four_b_evidence_type": "", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "excellent_entry", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L1_SAMPYO_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "calibration_block_reasons": [], "evidence": "Construction-material/cement price pass-through and early relative-strength evidence appeared before full margin confirmation.", "source": "industry price-pass-through news class / stock-web rows", "round": "R10", "loop": "1", "sector": "건설·부동산·건자재", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/038/038500/2021.csv", "profile_path": "atlas/symbol_profiles/038/038500.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R10L1_SAMPYO_T2", "case_id": "R10L1_SAMPYO_038500_2021", "symbol": "038500", "company_name": "삼표시멘트", "primary_archetype": "CEMENT_PRICE_PASS_THROUGH_CONSTRUCTION_MATERIALS", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-02-03", "entry_date": "2021-02-03", "entry_price": 4905, "MFE_30D_pct": 22.3, "MFE_90D_pct": 37.6, "MFE_180D_pct": 37.6, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.8, "MAE_90D_pct": -6.8, "MAE_180D_pct": -6.8, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-06-22", "peak_price": 6750, "drawdown_after_peak_pct": -17.1, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "", "four_b_evidence_type": "", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_entry", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L1_SAMPYO_G2", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "calibration_block_reasons": [], "evidence": "Price/volume breakout plus sector price pass-through narrative made the early evidence actionable.", "source": "stock-web rows / sector news class", "round": "R10", "loop": "1", "sector": "건설·부동산·건자재", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/038/038500/2021.csv", "profile_path": "atlas/symbol_profiles/038/038500.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R10L1_SAMPYO_T3", "case_id": "R10L1_SAMPYO_038500_2021", "symbol": "038500", "company_name": "삼표시멘트", "primary_archetype": "CEMENT_PRICE_PASS_THROUGH_CONSTRUCTION_MATERIALS", "trigger_type": "Stage3-Yellow", "trigger_date": "2021-03-26", "entry_date": "2021-03-26", "entry_price": 5640, "MFE_30D_pct": 7.3, "MFE_90D_pct": 19.7, "MFE_180D_pct": 19.7, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.4, "MAE_90D_pct": -9.4, "MAE_180D_pct": -9.4, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-06-22", "peak_price": 6750, "drawdown_after_peak_pct": -17.1, "green_lateness_ratio": 0.46, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "", "four_b_evidence_type": "", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_but_usable_entry", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L1_SAMPYO_G3", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "calibration_block_reasons": [], "evidence": "Later confirmation was safer in narrative terms but captured less upside.", "source": "stock-web rows", "round": "R10", "loop": "1", "sector": "건설·부동산·건자재", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/038/038500/2021.csv", "profile_path": "atlas/symbol_profiles/038/038500.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R10L1_SAMPYO_T5", "case_id": "R10L1_SAMPYO_038500_2021", "symbol": "038500", "company_name": "삼표시멘트", "primary_archetype": "CEMENT_PRICE_PASS_THROUGH_CONSTRUCTION_MATERIALS", "trigger_type": "Stage4B", "trigger_date": "2021-06-22", "entry_date": "2021-06-22", "entry_price": 6340, "MFE_30D_pct": 6.2, "MFE_90D_pct": 6.2, "MFE_180D_pct": 6.2, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.7, "MAE_90D_pct": -12.4, "MAE_180D_pct": -12.4, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-06-22", "peak_price": 6750, "drawdown_after_peak_pct": -17.1, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.78, "four_b_full_window_peak_proximity": 0.78, "four_b_timing_verdict": "price_only_local_4B_near_full_window_peak", "four_b_evidence_type": "price_only|positioning_overheat", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_watch_success_price_only", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L1_SAMPYO_G4", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "calibration_usable": true, "calibration_block_reasons": [], "evidence": "Price-only sector peak near the full observed peak; no hard thesis break.", "source": "stock-web OHLC", "round": "R10", "loop": "1", "sector": "건설·부동산·건자재", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/038/038500/2021.csv", "profile_path": "atlas/symbol_profiles/038/038500.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R10L1_GS_T1", "case_id": "R10L1_GS_006360_2023", "symbol": "006360", "company_name": "GS건설", "primary_archetype": "CONSTRUCTION_QUALITY_SAFETY_TRUST_BREAK", "trigger_type": "Stage2", "trigger_date": "2023-02-21", "entry_date": "2023-02-21", "entry_price": 24300, "MFE_30D_pct": 0.6, "MFE_90D_pct": 0.6, "MFE_180D_pct": 0.6, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -17.7, "MAE_90D_pct": -25.8, "MAE_180D_pct": -47.9, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-02-21", "peak_price": 24450, "drawdown_after_peak_pct": -47.9, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "", "four_b_evidence_type": "", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "evidence_good_but_price_failed", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L1_GS_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "calibration_block_reasons": [], "evidence": "Ordinary construction recovery/order evidence, before the later quality/safety break.", "source": "earnings/order news class / stock-web rows", "round": "R10", "loop": "1", "sector": "건설·부동산·건자재", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv", "profile_path": "atlas/symbol_profiles/006/006360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R10L1_GS_T4", "case_id": "R10L1_GS_006360_2023", "symbol": "006360", "company_name": "GS건설", "primary_archetype": "CONSTRUCTION_QUALITY_SAFETY_TRUST_BREAK", "trigger_type": "Stage3-Green", "trigger_date": "2023-04-21", "entry_date": "2023-04-21", "entry_price": 22300, "MFE_30D_pct": 1.3, "MFE_90D_pct": 1.3, "MFE_180D_pct": 1.3, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.0, "MAE_90D_pct": -38.6, "MAE_180D_pct": -43.2, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-21", "peak_price": 22550, "drawdown_after_peak_pct": -43.8, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "", "four_b_evidence_type": "", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "false_positive_score", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L1_GS_G2", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "calibration_block_reasons": [], "evidence": "A normal construction recovery Green would have failed because safety/quality risk was not captured.", "source": "stock-web rows; safety event later", "round": "R10", "loop": "1", "sector": "건설·부동산·건자재", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv", "profile_path": "atlas/symbol_profiles/006/006360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R10L1_GS_T6", "case_id": "R10L1_GS_006360_2023", "symbol": "006360", "company_name": "GS건설", "primary_archetype": "CONSTRUCTION_QUALITY_SAFETY_TRUST_BREAK", "trigger_type": "Stage4C", "trigger_date": "2023-07-05", "entry_date": "2023-07-06", "entry_price": 14520, "MFE_30D_pct": 3.7, "MFE_90D_pct": 19.8, "MFE_180D_pct": 19.8, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.9, "MAE_90D_pct": -12.7, "MAE_180D_pct": -12.7, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-11-23", "peak_price": 17400, "drawdown_after_peak_pct": -15.6, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "", "four_b_evidence_type": "", "four_c_protection_label": "hard_4c_late_but_valid", "trigger_outcome_label": "thesis_break", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L1_GS_G3", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "calibration_usable": true, "calibration_block_reasons": [], "evidence": "Public safety/quality/reconstruction evidence converts prior recovery thesis into 4C.", "source": "safety event / reconstruction news / stock-web rows", "round": "R10", "loop": "1", "sector": "건설·부동산·건자재", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv", "profile_path": "atlas/symbol_profiles/006/006360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R10L1_HDC_T1", "case_id": "R10L1_HDC_294870_2022", "symbol": "294870", "company_name": "HDC현대산업개발", "primary_archetype": "CONSTRUCTION_COLLAPSE_LICENSE_REPUTATION_BREAK", "trigger_type": "Stage2", "trigger_date": "2022-01-10", "entry_date": "2022-01-10", "entry_price": 25800, "MFE_30D_pct": 2.7, "MFE_90D_pct": 2.7, "MFE_180D_pct": 2.7, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -45.5, "MAE_90D_pct": -49.0, "MAE_180D_pct": -62.1, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-01-11", "peak_price": 26500, "drawdown_after_peak_pct": -63.1, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "", "four_b_evidence_type": "", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "false_positive_score_if_no_safety_gate", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L1_HDC_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "calibration_block_reasons": [], "evidence": "Pre-collapse ordinary construction thesis; immediately invalidated by safety/trust event.", "source": "pre-event price and public event date", "round": "R10", "loop": "1", "sector": "건설·부동산·건자재", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv", "profile_path": "atlas/symbol_profiles/294/294870.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R10L1_HDC_T6", "case_id": "R10L1_HDC_294870_2022", "symbol": "294870", "company_name": "HDC현대산업개발", "primary_archetype": "CONSTRUCTION_COLLAPSE_LICENSE_REPUTATION_BREAK", "trigger_type": "Stage4C", "trigger_date": "2022-01-11", "entry_date": "2022-01-12", "entry_price": 20850, "MFE_30D_pct": 8.2, "MFE_90D_pct": 8.2, "MFE_180D_pct": 8.2, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -35.3, "MAE_90D_pct": -36.9, "MAE_180D_pct": -53.0, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-01-12", "peak_price": 22700, "drawdown_after_peak_pct": -56.9, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "", "four_b_evidence_type": "", "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "hard_4c_success", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L1_HDC_G2", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "calibration_usable": true, "calibration_block_reasons": [], "evidence": "Collapse event created hard safety/trust/license/reputation break; no normal valuation recovery entry.", "source": "public safety event / stock-web rows", "round": "R10", "loop": "1", "sector": "건설·부동산·건자재", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv", "profile_path": "atlas/symbol_profiles/294/294870.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
```

### 27.4 Score simulation rows JSONL

```jsonl
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L1_HMG_053690_2022", "trigger_id": "R10L1_HMG_T1", "symbol": "053690", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 9, "customer_quality_score": 7, "policy_or_regulatory_score": 8, "valuation_repricing_score": 6, "execution_risk_score": 5, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 86, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 3, "revision_score": 2, "relative_strength_score": 10, "customer_quality_score": 7, "policy_or_regulatory_score": 8, "valuation_repricing_score": 6, "execution_risk_score": 5, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 98, "stage_label_after": "Stage3-Green", "changed_components": ["relative_strength_score", "margin_bridge_score"], "component_delta_explanation": "R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores.", "selected_by_profile": false, "MFE_90D_pct": 340.5, "MAE_90D_pct": -5.4, "score_return_alignment_label": "score_high_return_high"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L1_HMG_053690_2022", "trigger_id": "R10L1_HMG_T2", "symbol": "053690", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 9, "customer_quality_score": 7, "policy_or_regulatory_score": 8, "valuation_repricing_score": 6, "execution_risk_score": 5, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 86, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 3, "revision_score": 2, "relative_strength_score": 10, "customer_quality_score": 7, "policy_or_regulatory_score": 8, "valuation_repricing_score": 6, "execution_risk_score": 5, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 98, "stage_label_after": "Stage3-Green", "changed_components": ["relative_strength_score", "margin_bridge_score"], "component_delta_explanation": "R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores.", "selected_by_profile": false, "MFE_90D_pct": 254.3, "MAE_90D_pct": -7.2, "score_return_alignment_label": "score_high_return_high"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L1_HMG_053690_2022", "trigger_id": "R10L1_HMG_T3", "symbol": "053690", "trigger_type": "Stage3-Yellow", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 9, "customer_quality_score": 7, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": 6, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 9, "customer_quality_score": 7, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": 6, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green", "changed_components": ["none"], "component_delta_explanation": "R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores.", "selected_by_profile": true, "MFE_90D_pct": 85.2, "MAE_90D_pct": -27.5, "score_return_alignment_label": "score_high_return_low_false_positive"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L1_HMG_053690_2022", "trigger_id": "R10L1_HMG_T5", "symbol": "053690", "trigger_type": "Stage4B", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 9, "customer_quality_score": 7, "policy_or_regulatory_score": 8, "valuation_repricing_score": 10, "execution_risk_score": 8, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 89, "stage_label_before": "Stage3+4B-watch", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 9, "customer_quality_score": 7, "policy_or_regulatory_score": 8, "valuation_repricing_score": 10, "execution_risk_score": 9, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 62, "stage_label_after": "Stage3+4B-watch", "changed_components": ["execution_risk_score"], "component_delta_explanation": "R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores.", "selected_by_profile": false, "MFE_90D_pct": 4.2, "MAE_90D_pct": -43.3, "score_return_alignment_label": "score_high_return_low_false_positive"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L1_SAMPYO_038500_2021", "trigger_id": "R10L1_SAMPYO_T1", "symbol": "038500", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 2, "margin_bridge_score": 7, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 3, "policy_or_regulatory_score": 2, "valuation_repricing_score": 5, "execution_risk_score": 3, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 2, "margin_bridge_score": 8, "revision_score": 4, "relative_strength_score": 8, "customer_quality_score": 3, "policy_or_regulatory_score": 2, "valuation_repricing_score": 5, "execution_risk_score": 3, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 86, "stage_label_after": "Stage3-Green", "changed_components": ["relative_strength_score", "margin_bridge_score"], "component_delta_explanation": "R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores.", "selected_by_profile": false, "MFE_90D_pct": 57.7, "MAE_90D_pct": -8.6, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L1_SAMPYO_038500_2021", "trigger_id": "R10L1_SAMPYO_T2", "symbol": "038500", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 2, "margin_bridge_score": 7, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 3, "policy_or_regulatory_score": 2, "valuation_repricing_score": 5, "execution_risk_score": 3, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 2, "margin_bridge_score": 8, "revision_score": 4, "relative_strength_score": 8, "customer_quality_score": 3, "policy_or_regulatory_score": 2, "valuation_repricing_score": 5, "execution_risk_score": 3, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 86, "stage_label_after": "Stage3-Green", "changed_components": ["relative_strength_score", "margin_bridge_score"], "component_delta_explanation": "R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores.", "selected_by_profile": false, "MFE_90D_pct": 37.6, "MAE_90D_pct": -6.8, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L1_SAMPYO_038500_2021", "trigger_id": "R10L1_SAMPYO_T3", "symbol": "038500", "trigger_type": "Stage3-Yellow", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 2, "margin_bridge_score": 7, "revision_score": 4, "relative_strength_score": 6, "customer_quality_score": 3, "policy_or_regulatory_score": 2, "valuation_repricing_score": 6, "execution_risk_score": 3, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 2, "margin_bridge_score": 7, "revision_score": 4, "relative_strength_score": 6, "customer_quality_score": 3, "policy_or_regulatory_score": 2, "valuation_repricing_score": 6, "execution_risk_score": 3, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage3-Yellow", "changed_components": ["none"], "component_delta_explanation": "R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores.", "selected_by_profile": true, "MFE_90D_pct": 19.7, "MAE_90D_pct": -9.4, "score_return_alignment_label": "score_high_return_high"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L1_SAMPYO_038500_2021", "trigger_id": "R10L1_SAMPYO_T5", "symbol": "038500", "trigger_type": "Stage4B", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 2, "margin_bridge_score": 7, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 3, "policy_or_regulatory_score": 2, "valuation_repricing_score": 8, "execution_risk_score": 6, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 75, "stage_label_before": "Stage3+4B-watch", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 2, "margin_bridge_score": 7, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 3, "policy_or_regulatory_score": 2, "valuation_repricing_score": 8, "execution_risk_score": 7, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage3+4B-watch", "changed_components": ["execution_risk_score"], "component_delta_explanation": "R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores.", "selected_by_profile": false, "MFE_90D_pct": 6.2, "MAE_90D_pct": -12.4, "score_return_alignment_label": "score_high_return_high"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L1_GS_006360_2023", "trigger_id": "R10L1_GS_T1", "symbol": "006360", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 2, "customer_quality_score": 2, "policy_or_regulatory_score": 1, "valuation_repricing_score": 3, "execution_risk_score": 6, "legal_or_contract_risk_score": 7, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}, "weighted_score_before": 34, "stage_label_before": "Watch/Reject", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 2, "customer_quality_score": 2, "policy_or_regulatory_score": 1, "valuation_repricing_score": 3, "execution_risk_score": 6, "legal_or_contract_risk_score": 7, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}, "weighted_score_after": 24, "stage_label_after": "Watch/Reject", "changed_components": ["none"], "component_delta_explanation": "R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores.", "selected_by_profile": false, "MFE_90D_pct": 0.6, "MAE_90D_pct": -25.8, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L1_GS_006360_2023", "trigger_id": "R10L1_GS_T4", "symbol": "006360", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 2, "customer_quality_score": 2, "policy_or_regulatory_score": 1, "valuation_repricing_score": 3, "execution_risk_score": 6, "legal_or_contract_risk_score": 7, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}, "weighted_score_before": 34, "stage_label_before": "Watch/Reject", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 2, "customer_quality_score": 2, "policy_or_regulatory_score": 1, "valuation_repricing_score": 3, "execution_risk_score": 6, "legal_or_contract_risk_score": 7, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}, "weighted_score_after": 24, "stage_label_after": "Watch/Reject", "changed_components": ["none"], "component_delta_explanation": "R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores.", "selected_by_profile": true, "MFE_90D_pct": 1.3, "MAE_90D_pct": -38.6, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L1_GS_006360_2023", "trigger_id": "R10L1_GS_T6", "symbol": "006360", "trigger_type": "Stage4C", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 2, "customer_quality_score": 2, "policy_or_regulatory_score": 1, "valuation_repricing_score": 3, "execution_risk_score": 10, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 19, "stage_label_before": "4C-watch", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 2, "customer_quality_score": 2, "policy_or_regulatory_score": 1, "valuation_repricing_score": 3, "execution_risk_score": 10, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 9, "stage_label_after": "Stage4C-hard-gate", "changed_components": ["legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores.", "selected_by_profile": false, "MFE_90D_pct": 19.8, "MAE_90D_pct": -12.7, "score_return_alignment_label": "score_high_return_high"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L1_HDC_294870_2022", "trigger_id": "R10L1_HDC_T1", "symbol": "294870", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 1, "customer_quality_score": 2, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 7, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 3}, "weighted_score_before": 23, "stage_label_before": "Watch/Reject", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 1, "customer_quality_score": 2, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 7, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 3}, "weighted_score_after": 13, "stage_label_after": "Watch/Reject", "changed_components": ["none"], "component_delta_explanation": "R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores.", "selected_by_profile": true, "MFE_90D_pct": 2.7, "MAE_90D_pct": -49.0, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L1_HDC_294870_2022", "trigger_id": "R10L1_HDC_T6", "symbol": "294870", "trigger_type": "Stage4C", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 1, "customer_quality_score": 2, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 10, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 6}, "weighted_score_before": 11, "stage_label_before": "4C-watch", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 1, "customer_quality_score": 2, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 10, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 6}, "weighted_score_after": 1, "stage_label_after": "Stage4C-hard-gate", "changed_components": ["legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "R10 proxy promotes early evidence only when it is tied to price pass-through/event evidence; PF/safety/legal risk components cap or reject long-entry scores.", "selected_by_profile": false, "MFE_90D_pct": 8.2, "MAE_90D_pct": -36.9, "score_return_alignment_label": "score_mid_return_low_watch_only"}
```

### 27.5 Profile comparison rows CSV

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,avg_MAE_90D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,4,4,4,27.2,-31.1,0.25,0.5,0.5,2,2,,,reference; late confirmation and safety false positives
profile_comparison,stage2_actionable_early_evidence_plus,4,4,4,80.6,-16.3,0.5,0.25,0.25,1,0,0.94,0.94,best profile; promotes early but blocks PF/safety
profile_comparison,stage3_yellow_entry_relaxed,4,4,4,27.2,-31.1,0.25,0.5,0.5,2,2,,,rejected; still too late and too volatile
profile_comparison,green_confirmation_timing_relaxed,4,4,4,27.2,-31.1,0.25,0.5,0.5,2,2,,,rejected; broad Green relaxation not validated
profile_comparison,four_b_peak_timing_tuned,4,2,0,4.2,-43.3,0.0,1.0,0.0,0,0,0.86,0.86,accepted only for event/price-overheat overlay
profile_comparison,four_c_thesis_break_earlier,4,2,0,14.0,-24.8,0.0,0.5,0.0,0,0,,,accepted hard gate for safety/license/trust break
```

### 27.6 Shadow weight CSV

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_event_or_price_pass_through,0,2,+2,"NEOM event premium and cement price-pass-through Stage2 triggers produced higher MFE with acceptable MAE before late confirmation","HMG/SAMPYO early selected avg MFE90 improved from 52.5 to 147.2 while avg MAE90 improved from -18.5 to -7.9","R10L1_HMG_T2|R10L1_SAMPYO_T1",2,"shadow-only; not broad construction Green relaxation"
shadow_weight,construction_safety_quality_hard_4c_gate,0,3,+3,"GS/HDC safety or quality failure converted ordinary construction thesis into hard 4C","Baseline recovery/Green rows had avg MAE90 about -43.8; 4C gate blocks long continuation and preserves risk discipline","R10L1_GS_T6|R10L1_HDC_T6",2,"hard gate; delta applies only with public safety/license/trust evidence"
shadow_weight,price_only_4b_event_premium_guardrail,0,2,+2,"HanmiGlobal and Sampyo peak rows show 4B should be overlay, not automatic thesis break","HMG 4B full-window proximity 0.94 and Sampyo 0.78, but both are price/positioning overlays without hard 4C evidence","R10L1_HMG_T5|R10L1_SAMPYO_T5",2,"split local/full-window 4B; require non-price evidence for full exit"
```

### 27.7 Optimization decision rows JSONL

```jsonl
{"row_type":"optimization_decision","decision_id":"R10L1_D1","hypothesis":"Promote Stage2 when construction evidence is event-driven but coupled with strong relative strength or price-pass-through","tested_trigger_ids":["R10L1_HMG_T2","R10L1_SAMPYO_T1","R10L1_HMG_T3","R10L1_SAMPYO_T3"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus_with_pf_safety_guardrail","backtest_result_summary":"Early Stage2/Actionable rows captured much better MFE and lower MAE than later Yellow confirmation in the two positive cases.","accepted_or_rejected":"accepted","delta_magnitude":"+2","why_not_larger_delta":"Only two positive cases and one is event-premium, not structural backlog.","risks":"Can over-promote policy/theme construction moves without contract/backlog conversion.","next_validation_needed":"Add DL E&C, Hyundai E&C, cement failures, and post-theme NEOM counterexamples."}
{"row_type":"optimization_decision","decision_id":"R10L1_D2","hypothesis":"Safety/quality/license events in construction should trigger hard 4C before normal valuation logic","tested_trigger_ids":["R10L1_GS_T4","R10L1_GS_T6","R10L1_HDC_T1","R10L1_HDC_T6"],"baseline_profile":"baseline_current_proxy","selected_profile":"four_c_thesis_break_earlier","backtest_result_summary":"GS and HDC ordinary thesis rows suffered severe MAE while hard 4C rows correctly reclassified the case as thesis break.","accepted_or_rejected":"accepted","delta_magnitude":"+3","why_not_larger_delta":"Sample size two; needs false-break safety cases before +5.","risks":"May over-penalize small incidents without license/reputation/cost impact.","next_validation_needed":"Validate against minor defect cases where price recovered quickly."}
{"row_type":"optimization_decision","decision_id":"R10L1_D3","hypothesis":"Price-only 4B near local/full peak is useful as overlay but not enough for full 4C or forced exit","tested_trigger_ids":["R10L1_HMG_T5","R10L1_SAMPYO_T5"],"baseline_profile":"baseline_current_proxy","selected_profile":"four_b_peak_timing_tuned","backtest_result_summary":"4B rows were close to full-window peaks, but evidence was price/positioning/event-premium rather than hard thesis break.","accepted_or_rejected":"accepted_as_overlay_only","delta_magnitude":"+2 guardrail","why_not_larger_delta":"No durable non-price 4B evidence beyond positioning and valuation blowoff.","risks":"Could issue too many warnings during valid structural rerating.","next_validation_needed":"Find construction cases with revision slowdown or PF funding stress near peak."}
```

### 27.8 Narrative-only rows JSONL

```jsonl
{"row_type":"narrative_only","case_id":"R10L1_NORMAL_PF_EARLY_WARNING","symbol":"unavailable","reason":"PF funding-stress early-warning case not fully validated with 180D OHLC in this round","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

### 27.9 Aggregate metric rows CSV

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,below_entry_90D_rate,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,4,4,100.4,30.2,-22.2,-17.2,100.4,-31.0,1.0,,,,representative rows only; duplicate/overlay rows excluded
aggregate_metric,Stage2-Actionable,2,2,146.0,146.0,-7.0,-7.0,146.0,-7.0,1.0,,,,representative rows only; duplicate/overlay rows excluded
aggregate_metric,Stage3-Yellow,2,2,52.5,52.5,-18.4,-18.4,52.5,-18.4,1.0,0.6,,,representative rows only; duplicate/overlay rows excluded
aggregate_metric,Stage3-Green,1,1,1.3,1.3,-38.6,-38.6,1.3,-43.2,1.0,,,,representative rows only; duplicate/overlay rows excluded
```

## 28. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are standalone E2R historical calibration and backtest optimization outputs produced using the Songdaiki/stock-web OHLC atlas. Do not redo market research unless a row is internally inconsistent. Ingest the machine-readable rows and update the repository in batch.

These MD files are not live candidate research. They are historical calibration and shadow optimization research. Use them to improve trigger-level backtesting, Stage2-Actionable / Stage3-Yellow gates, 4B timing, 4C protection logic, score-return alignment evaluation, aggregate deduplication, and shadow score profiles.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.
- Manifest and schema were used to validate max_date, column mapping, and calibration rules.

### Rules
- Use only rows with calibration_usable=true for weight calibration.
- Reject narrative-only rows for score changes.
- Reject rows without OHLC-derived MFE/MAE.
- Reject rows without at least 180 trading days forward window.
- Reject rows blocked by corporate-action-contaminated 180D window unless the user explicitly allows a separate adjusted-price revalidation.
- Reject shadow_weight rows that do not include before/after backtest effect.
- Reject score_simulation rows that have weighted_score_before/after but no raw_component_scores_before/after.
- Reject shadow_weight rows if the changed axis is not traceable to component-level score changes and OHLC backtest effect.
- Preserve shadow-only calibration separately from production rules.
- Keep Stage2-Actionable as a shadow trigger type unless already supported.
- Do not hardcode historical company names into scoring logic.
- Production scoring must not change unless the user explicitly approves applying the shadow profile.

### Repository tasks
1. Parse case / trigger / score_simulation / profile_comparison / optimization_decision / shadow weight / aggregate rows.
2. Validate price_source_validation rows.
3. Validate MFE / MAE / peak / drawdown values.
4. Validate green_lateness_ratio.
5. Validate four_b_local_peak_proximity.
6. Validate four_b_full_window_peak_proximity.
7. Reject price-only local 4B as full 4B unless non-price 4B evidence exists.
8. Validate 4C protection labels.
9. Validate calibration_usable filtering.
10. Validate same_entry_group_id.
11. Validate dedupe_for_aggregate.
12. Aggregate metrics must not double-count trigger rows sharing the same same_entry_group_id.
13. Validate raw_component_scores_before/after in score_simulation rows.
14. Validate before/after profile comparison rows.
15. Validate score-return alignment labels.
16. Validate Validation Scope / Non-Validation Scope and reject deltas for unvalidated gates.
17. Append valid case rows to abstract case library.
18. Append valid trigger rows to trigger calibration dataset.
19. Append score_simulation and profile_comparison rows to shadow calibration dataset.
20. Append shadow weight rows to shadow calibration profile only if before/after backtest effect and component-level explanation exist.
21. Add tests that narrative-only, non-OHLC, insufficient-forward-window, and corporate-action-contaminated rows cannot change weights.
22. Add tests for optimization decision validation.
23. Add tests for aggregate deduplication by same_entry_group_id.
24. Produce checkpoint summary.

### Expected output
- Concise implementation summary.
- Files changed.
- Tests run.
- Rows accepted.
- Rows rejected and why.
- Shadow profile rows accepted.
- Shadow weight rows accepted.
- Shadow weight rows rejected.
- No investment recommendation language.

## 29. Next Round State

```text
current_round = R10 Loop 1
next_round = R11 Loop 1
next_sector = 정책·지정학·재난·이벤트
production_scoring_changed = false
shadow_weight_only = true
```

## 30. Source Notes

- Stock-Web manifest/schema/universe/profile/shard files were checked before case calibration.
- Price values use `tradable_raw` rows from `atlas/ohlcv_tradable_by_symbol_year`.
- Corporate-action candidate windows in the selected 180D calibration windows were not used for weight calibration.
- Evidence source map is intentionally separated from price source map; coding handoff should revalidate exact news/disclosure URLs before repository ingestion.
- Market/sector relative returns are unavailable in this standalone MD and are not used for shadow deltas.
