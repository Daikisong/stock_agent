# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata

```text
research_session = historical_calibration_after_stock_web_ohlc_breakthrough
round = R8
loop = 2
sector = 플랫폼·콘텐츠·SW·보안
output_file = e2r_stock_web_historical_calibration_round_R8_loop_2_platform_content_sw_security_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_repo_access_allowed = false
stock_web_price_atlas_access_required = true
```

이번 파일은 `stock_agent` 레포를 열지 않고 작성한 standalone historical calibration MD다. 가격 row는 Songdaiki/stock-web의 `tradable_raw` OHLCV를 사용했다. Manifest는 `max_date=2026-02-20`, `price_adjustment_status=raw_unadjusted_marcap`, `tradable_row_count=14354401`로 확인되며, schema는 tradable shard의 `d/o/h/l/c/v/a/mc/s/m` column mapping과 MFE/MAE 산식을 정의한다. fileciteturn321file0 fileciteturn322file0

## 1. Round Scope

R8은 플랫폼·콘텐츠·SW·보안이다. 이번 loop는 게임/콘텐츠 IP, 블록체인 게임 플랫폼, 신작 trailer event premium, 사이버보안 정치 테마를 섞어 “Stage2-Actionable 승격”과 “event-only guardrail”을 동시에 검증한다.

## 2. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

확인한 profile:
- 위메이드 112040: 2021-09-13, 2021-10-06 corporate-action candidate가 있어 그 이전 trigger는 weight calibration에서 제외했다. fileciteturn323file0
- 데브시스터즈 194480: corporate-action candidate 없음, 2021~2022 calibration 사용 가능. fileciteturn324file0
- 펄어비스 263750: 2021-04-16 corporate-action candidate 이후인 2021-08 이후 trigger만 사용했다. fileciteturn325file0
- 안랩 053800: 2005 corporate-action candidate 외 R8 window에는 contamination 없음. fileciteturn326file0

## 3. Historical Eligibility Gate

Core calibration은 30D/90D/180D로 닫았다. 1Y/2Y는 일부 line range가 exhaustive하게 재구성되지 않았으므로 weight delta 산정에서 제외하고 `unavailable_not_used_for_delta`로 기록했다. 이 라운드의 delta는 180D forward window와 corporate-action clean window를 만족한 trigger만 사용한다.

## 4. Canonical Archetypes Tested

| archetype | tested cases | verdict |
|---|---:|---|
| MOBILE_GAME_IP_GLOBAL_HIT_REVENUE_RERATING | 1 | Stage2-Actionable 승격 강함 |
| GAME_PLATFORM_BLOCKCHAIN_P2E_RERATING | 1 | Stage2-Actionable + 4B overlay 유효 |
| NEW_GAME_TRAILER_PIPELINE_OPTION_VALUE | 1 | event premium guardrail 필요 |
| CYBERSECURITY_POLITICAL_THEME_EVENT_PREMIUM | 1 | fundamental Green 금지, event-only watch |

## 5. Case Selection Summary

| case_id | symbol | company | case_type | best_trigger | notes |
| --- | --- | --- | --- | --- | --- |
| R8L2_DEV_194480_COOKIE_RUN_KINGDOM | 194480 | 데브시스터즈 | structural_success | R8L2_DEV_T2 | 쿠키런: 킹덤 launch/ranking/revenue evidence가 가격 상대강도와 결합된 전형적 Stage2-Actionable 승격 후보. |
| R8L2_WEM_112040_MIR4_WEMIX | 112040 | 위메이드 | structural_success_with_crypto_overlay | R8L2_WEM_T2 | 2021-09~10 corporate-action candidate 이후의 post-adjustment tradable rows만 core calibration에 사용. |
| R8L2_PAB_263750_DOKEV_EVENT_PREMIUM | 263750 | 펄어비스 | event_premium_overheat | R8L2_PAB_T2 | DokeV trailer momentum은 강했지만, 비가격 실적 bridge가 약한 event premium 성격. |
| R8L2_AHL_053800_POLITICAL_THEME | 053800 | 안랩 | price_moved_without_fundamental_evidence | R8L2_AHL_T5 | 보안 소프트웨어 본업 evidence보다 정치 이벤트 프리미엄이 가격을 지배한 반례. |


## 6. Evidence Source Map

- 데브시스터즈: Cookie Run: Kingdom은 2021년 1월 iOS/Android로 출시되었고, 2021년 초 한국·대만·태국 등에서 앱스토어 매출/무료 순위 상위권 evidence가 공개적으로 관측됐다. citeturn625536search2
- 위메이드: MIR4는 2021년 8월 글로벌 출시 후 170개국/12개 언어 서비스로 확장된 공개 evidence가 있었다. citeturn269745search0
- 펄어비스: DokeV gameplay trailer는 2021년 8월 25일 Gamescom Opening Night Live에서 공개됐다. citeturn954188search0
- 안랩: 안철수 후보는 2022년 3월 3일 대선 후보직을 사퇴하고 윤석열 후보 지지를 선언했다. 이는 본업 SW/security evidence가 아니라 정치 이벤트 evidence다. citeturn954188search4

## 7. Price Data Source Map

주요 price row는 stock-web shard에서 직접 확인했다.

- 데브시스터즈 2021 early launch/rerating rows: 2021-01-21 close 17,250, 2021-01-25 close 29,100, 2021-03-25 close 133,000 등이 확인된다. fileciteturn327file0
- 데브시스터즈 2021 full peak area: 2021-09-27 high 199,500, 이후 2021-10~12 drawdown rows가 확인된다. fileciteturn329file0
- 데브시스터즈 2022 drawdown low range: 2022-07-04 low 39,750 등 post-peak drawdown rows가 확인된다. fileciteturn335file0
- 위메이드 2021 post-corporate-action rows: 2021-10-12 close 90,500, 2021-11-22 high 245,700 등이 확인된다. fileciteturn328file0
- 위메이드 2022 drawdown rows: 2022-02~07 low path가 확인된다. fileciteturn333file0
- 펄어비스 2021 event/peak rows: 2021-08-26 close 87,900, 2021-11-17 high 145,200 등이 확인된다. fileciteturn330file0
- 펄어비스 2022 drawdown rows: 2022-04~07 low path가 확인된다. fileciteturn334file0
- 안랩 2022 election-theme rows: 2022-03-03 close 70,800, 2022-03-24 high 218,500 등이 확인된다. fileciteturn331file0
- 안랩 2022 post-peak unwind rows: 2022-05~09 drawdown path가 확인된다. fileciteturn332file0

## 8. Case-by-Case Trigger Grid

| trigger_id | company | type | trigger_date | entry_date | entry_price | MFE90 | MAE90 | outcome | aggregate_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R8L2_DEV_T1 | 데브시스터즈 | Stage2 | 2021-01-21 | 2021-01-21 | 17250 | 833.3 | -13.0 | missed_structural | representative |
| R8L2_DEV_T2 | 데브시스터즈 | Stage2-Actionable | 2021-01-25 | 2021-01-25 | 29100 | 453.3 | -7.6 | excellent_entry | representative |
| R8L2_DEV_T3 | 데브시스터즈 | Stage3-Yellow | 2021-02-18 | 2021-02-18 | 48550 | 231.6 | -13.0 | good_entry | representative |
| R8L2_DEV_T4 | 데브시스터즈 | Stage3-Green | 2021-03-25 | 2021-03-25 | 133000 | 21.1 | -38.3 | late_entry | representative |
| R8L2_DEV_T5 | 데브시스터즈 | Stage4B | 2021-09-27 | 2021-09-27 | 186000 | 7.8 | -65.0 | good_full_window_4B_timing | 4B_overlay_only |
| R8L2_WEM_T2 | 위메이드 | Stage2-Actionable | 2021-10-12 | 2021-10-12 | 90500 | 171.5 | -2.3 | excellent_entry | representative |
| R8L2_WEM_T3 | 위메이드 | Stage3-Yellow | 2021-10-15 | 2021-10-15 | 120300 | 104.2 | -20.2 | good_entry | representative |
| R8L2_WEM_T4 | 위메이드 | Stage3-Green | 2021-10-26 | 2021-10-26 | 161000 | 52.6 | -41.7 | late_entry | representative |
| R8L2_WEM_T5 | 위메이드 | Stage4B | 2021-11-19 | 2021-11-19 | 237000 | 3.0 | -60.4 | good_full_window_4B_timing | 4B_overlay_only |
| R8L2_WEM_T6 | 위메이드 | Stage4C-watch | 2022-02-10 | 2022-02-10 | 106600 | 6.8 | -41.9 | hard_4c_late | 4C_overlay_only |
| R8L2_PAB_T1 | 펄어비스 | Stage2 | 2021-08-26 | 2021-08-26 | 87900 | 65.2 | -11.7 | event_premium | representative |
| R8L2_PAB_T2 | 펄어비스 | Stage2-Actionable | 2021-10-13 | 2021-10-13 | 92700 | 56.6 | -2.9 | good_entry_event_premium | representative |
| R8L2_PAB_T4 | 펄어비스 | Stage3-Green | 2021-11-16 | 2021-11-16 | 138500 | 4.8 | -34.5 | false_positive_score | representative |
| R8L2_PAB_T5 | 펄어비스 | Stage4B | 2021-11-17 | 2021-11-17 | 141000 | 3.0 | -35.7 | price_only_local_4B_success | 4B_overlay_only |
| R8L2_AHL_T1 | 안랩 | Stage2 | 2022-03-03 | 2022-03-03 | 70800 | 208.6 | -5.6 | price_moved_without_evidence | representative |
| R8L2_AHL_T2 | 안랩 | Stage2-Actionable | 2022-03-11 | 2022-03-11 | 86500 | 152.6 | -14.2 | event_premium | representative |
| R8L2_AHL_T5 | 안랩 | Stage4B | 2022-03-23 | 2022-03-23 | 175800 | 24.3 | -53.9 | good_local_4B_timing_price_only | 4B_overlay_only |
| R8L2_AHL_T6 | 안랩 | Stage4C-watch | 2022-03-30 | 2022-03-30 | 122800 | 5.7 | -34.1 | event_premium_unwind | 4C_overlay_only |


## 9. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD_after_peak |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R8L2_DEV_T1 | 194480 | 2021-01-21 | 17250 | 300.0 | 833.3 | 1056.5 | -13.0 | -13.0 | -13.0 | 2021-09-27 | 199500 | -80.1 |
| R8L2_DEV_T2 | 194480 | 2021-01-25 | 29100 | 137.1 | 453.3 | 585.6 | -7.6 | -7.6 | -7.6 | 2021-09-27 | 199500 | -80.1 |
| R8L2_DEV_T3 | 194480 | 2021-02-18 | 48550 | 231.6 | 231.6 | 310.9 | -13.0 | -13.0 | -13.0 | 2021-09-27 | 199500 | -80.1 |
| R8L2_DEV_T4 | 194480 | 2021-03-25 | 133000 | 21.1 | 21.1 | 50.0 | -24.1 | -38.3 | -38.3 | 2021-09-27 | 199500 | -80.1 |
| R8L2_DEV_T5 | 194480 | 2021-09-27 | 186000 | 7.8 | 7.8 | 7.8 | -29.5 | -65.0 | -78.6 | 2021-09-27 | 199500 | -80.1 |
| R8L2_WEM_T2 | 112040 | 2021-10-12 | 90500 | 171.5 | 171.5 | 171.5 | -2.3 | -2.3 | -43.4 | 2021-11-22 | 245700 | -79.2 |
| R8L2_WEM_T3 | 112040 | 2021-10-15 | 120300 | 104.2 | 104.2 | 104.2 | -5.8 | -20.2 | -57.4 | 2021-11-22 | 245700 | -79.2 |
| R8L2_WEM_T4 | 112040 | 2021-10-26 | 161000 | 52.6 | 52.6 | 52.6 | -8.1 | -41.7 | -68.2 | 2021-11-22 | 245700 | -79.2 |
| R8L2_WEM_T5 | 112040 | 2021-11-19 | 237000 | 3.0 | 3.0 | 3.0 | -37.4 | -60.4 | -78.4 | 2021-11-22 | 245700 | -79.2 |
| R8L2_WEM_T6 | 112040 | 2022-02-10 | 106600 | 6.8 | 6.8 | 6.8 | -12.6 | -41.9 | -51.3 | 2021-11-22 | 245700 | -79.2 |
| R8L2_PAB_T1 | 263750 | 2021-08-26 | 87900 | 16.0 | 65.2 | 65.2 | -11.7 | -11.7 | -40.5 | 2021-11-17 | 145200 | -67.1 |
| R8L2_PAB_T2 | 263750 | 2021-10-13 | 92700 | 56.6 | 56.6 | 56.6 | -2.9 | -2.9 | -43.6 | 2021-11-17 | 145200 | -67.1 |
| R8L2_PAB_T4 | 263750 | 2021-11-16 | 138500 | 4.8 | 4.8 | 4.8 | -18.4 | -34.5 | -62.6 | 2021-11-17 | 145200 | -67.1 |
| R8L2_PAB_T5 | 263750 | 2021-11-17 | 141000 | 3.0 | 3.0 | 3.0 | -19.5 | -35.7 | -63.4 | 2021-11-17 | 145200 | -67.1 |
| R8L2_AHL_T1 | 053800 | 2022-03-03 | 70800 | 208.6 | 208.6 | 208.6 | -5.6 | -5.6 | -5.6 | 2022-03-24 | 218500 | -66.2 |
| R8L2_AHL_T2 | 053800 | 2022-03-11 | 86500 | 152.6 | 152.6 | 152.6 | -14.2 | -14.2 | -16.8 | 2022-03-24 | 218500 | -66.2 |
| R8L2_AHL_T5 | 053800 | 2022-03-23 | 175800 | 24.3 | 24.3 | 24.3 | -44.0 | -53.9 | -59.1 | 2022-03-24 | 218500 | -66.2 |
| R8L2_AHL_T6 | 053800 | 2022-03-30 | 122800 | 5.7 | 5.7 | 5.7 | -23.8 | -34.1 | -41.5 | 2022-03-24 | 218500 | -66.2 |


## 10. 1D Price Path Summaries

### DEV 194480 best Stage2-Actionable path

| checkpoint | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | +24.1 | +29.6 | -7.6 |
| D+5 | +43.6 | +47.8 | -7.6 |
| D+20 | +71.8 | +80.8 | -7.6 |
| D+30 | +107.9 | +137.1 | -7.6 |
| D+90 | +252.1 | +453.3 | -7.6 |
| D+180 | +439.5 | +585.6 | -7.6 |

Stage3-Green around 2021-03-25는 entry 133,000으로 이미 Stage2-Actionable 대비 upside의 약 61%를 소비한 뒤였다. 이후 90D MAE가 -38.3%까지 확대되어 Green은 “안전해 보이지만 늦은 문”이었다.

### WEM 112040 best Stage2-Actionable path

| checkpoint | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | +0.2 | +5.0 | -2.3 |
| D+5 | +39.2 | +42.9 | -2.3 |
| D+10 | +50.8 | +64.0 | -2.3 |
| D+20 | +108.7 | +117.8 | -2.3 |
| D+30 | +161.7 | +171.5 | -2.3 |
| D+180 | -42.4 | +171.5 | -43.4 |

초기에는 Stage2-Actionable이 매우 좋았지만, 4B peak watch 이후 crypto/platform risk가 붙자 full-cycle drawdown이 -79% 수준으로 커졌다.

### PAB 263750 best Stage2-Actionable path

| checkpoint | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | +2.3 | +4.5 | +0.3 |
| D+5 | -6.1 | +4.5 | -6.1 |
| D+20 | +2.5 | +4.5 | -2.9 |
| D+30 | +16.7 | +31.0 | -2.9 |
| D+60 | +31.2 | +56.6 | -2.9 |
| D+180 | -43.6 | +56.6 | -43.6 |

DokeV event premium은 돈이 되는 trade window는 만들었지만, full Green으로 올리기에는 revenue/revision bridge가 부족했다.

### AHL 053800 event-premium path

| checkpoint | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | -2.1 | +1.7 | -3.4 |
| D+5 | +22.2 | +30.1 | -5.6 |
| D+10 | +91.1 | +97.0 | -5.6 |
| D+15 | +104.8 | +208.6 | -5.6 |
| D+30 | +65.5 | +208.6 | -5.6 |
| D+90 | +22.7 | +208.6 | -5.6 |

안랩은 MFE만 보면 좋아 보이지만, causal evidence는 SW/security 실적이 아니라 정치 이벤트였다. 따라서 Stage2-Actionable을 fundamental entry로 승격하면 안 된다.

## 11. Case Trigger Comparison

| case_id | best_actual | baseline_selected | after_selected | baseline_MFE90 | after_MFE90 | baseline_MAE90 | after_MAE90 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R8L2_DEV_194480_COOKIE_RUN_KINGDOM | R8L2_DEV_T2 | R8L2_DEV_T4 | R8L2_DEV_T2 | 21.1 | 453.3 | -38.3 | -7.6 |
| R8L2_WEM_112040_MIR4_WEMIX | R8L2_WEM_T2 | R8L2_WEM_T4 | R8L2_WEM_T2 | 52.6 | 171.5 | -41.7 | -2.3 |
| R8L2_PAB_263750_DOKEV_EVENT_PREMIUM | R8L2_PAB_T2 | R8L2_PAB_T4 | R8L2_PAB_T2 | 4.8 | 56.6 | -34.5 | -2.9 |
| R8L2_AHL_053800_POLITICAL_THEME | R8L2_AHL_T5 | R8L2_AHL_T2 | R8L2_AHL_T5 | 152.6 | 24.3 | -14.2 | -53.9 |


## 12. Stage2 → Stage4 Audit

1. DEV/WEM은 Stage2-Actionable에서 MFE가 크고 초기 MAE가 얕았다. 이 둘은 Stage2 evidence를 무시하면 구조적 rerating을 놓친다.
2. PAB/AHL은 Stage2 또는 event trigger MFE가 커도, 실적 bridge가 약하거나 정치 이벤트라서 fundamental Green 승격을 막아야 한다.
3. DEV Green은 늦었고, PAB Green은 false-positive에 가깝다.
4. WEM은 Stage2-Actionable은 좋았지만 4B 이후의 drawdown protection이 필요했다.
5. AHL은 `price_moved_without_fundamental_evidence`다. MFE가 크다는 이유만으로 score weight를 올리면 점수표가 정치 테마에 오염된다.

## 13. Stage3 Yellow / Green Lateness Audit

| case | Stage2-Actionable entry | Green entry | peak | green_lateness_ratio | verdict |
|---|---:|---:|---:|---:|---|
| DEV | 29,100 | 133,000 | 199,500 | 0.61 | Green이 upside 대부분을 놓침 |
| WEM | 90,500 | 161,000 | 245,700 | 0.45 | Green이 다소 늦음 |
| PAB | 92,700 | 138,500 | 145,200 | 0.82 | Green이 peak 근처 false-positive |
| AHL | not_applicable | not_applicable | 218,500 | not_applicable | fundamental Green 부여 금지 |

## 14. 4B Timing Audit

| trigger | local_peak_proximity | full_window_peak_proximity | evidence_type | verdict |
|---|---:|---:|---|---|
| R8L2_DEV_T5 | 0.98 | 0.92 | valuation_blowoff, positioning_overheat | good_full_window_4B_timing |
| R8L2_WEM_T5 | 0.95 | 0.94 | valuation_blowoff, positioning_overheat | good_full_window_4B_timing |
| R8L2_PAB_T5 | 0.98 | 0.92 | price_only, positioning_overheat | near peak but not full fundamental 4B |
| R8L2_AHL_T5 | 0.71 | 0.71 | price_only, positioning_overheat | political event 4B-watch only |

4B는 매도 신호라기보다 Stage3 thesis 위에 덮는 “뜨거운 금속판”이다. DEV/WEM처럼 valuation/positioning이 같이 달아오르면 손을 떼야 하지만, PAB/AHL처럼 가격만 뜨거우면 full fundamental exit가 아니라 event premium watch로 남긴다.

## 15. 4C Protection Audit

R8 loop 2에서는 hard 4C delta를 제안하지 않는다. WEM_T6와 AHL_T6는 post-peak watch/unwind로는 유용하지만, 큰 하락 전에 thesis break를 잡은 clean hard 4C가 아니다.

## 16. Baseline Score Simulation

Baseline proxy는 Green confirmation을 늦게 잡는 경향이 있었다. DEV/WEM에서는 늦게 들어가 upside capture가 줄었고, PAB/AHL에서는 가격 momentum을 fundamental Green으로 오판할 위험이 있었다.

## 17. Shadow Profile Optimization Loop

row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,avg_MAE_90D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,4,4,4,57.8,-32.2,0.75,0.75,0.25,1,2,unavailable,unavailable,"reference; late Green and event premium errors remain"
profile_comparison,stage2_actionable_early_evidence_plus_with_event_guardrail,4,4,3,176.4,-16.7,1.0,0.25,0.25,0,0,unavailable,unavailable,"best; earlier structural entries with event-only guardrail"
profile_comparison,stage3_yellow_entry_relaxed,4,4,4,104.2,-22.5,1.0,0.5,0.25,0,1,unavailable,unavailable,usable but worse than P1 risk
profile_comparison,green_confirmation_timing_relaxed,4,4,4,57.8,-32.2,0.75,0.75,0.5,0,3,unavailable,unavailable,reject broad Green relaxation
profile_comparison,four_b_peak_timing_tuned,4,4,0,overlay_only,overlay_only,overlay_only,overlay_only,0,0,0,0.91,0.88,"accepted for overlay split, not entry selection"
profile_comparison,four_c_thesis_break_earlier,4,2,0,overlay_only,overlay_only,overlay_only,overlay_only,0,0,0,unavailable,unavailable,no hard 4C delta in R8

Best profile: `stage2_actionable_early_evidence_plus_with_event_guardrail`.

## 18. Before / After Backtest Comparison

| case_id | symbol | best_actual | baseline | after | baseline_date | after_date | baseline_px | after_px | baseline_MFE90 | after_MFE90 | baseline_MAE90 | after_MAE90 | return_improvement | risk_change | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R8L2_DEV_194480_COOKIE_RUN_KINGDOM | 194480 | R8L2_DEV_T2 | R8L2_DEV_T4 | R8L2_DEV_T2 | 2021-03-25 | 2021-01-25 | 133000 | 29100 | 21.1 | 453.3 | -38.3 | -7.6 | 432.2 | 30.7 | P1 structural early-evidence + event guardrail |
| R8L2_WEM_112040_MIR4_WEMIX | 112040 | R8L2_WEM_T2 | R8L2_WEM_T4 | R8L2_WEM_T2 | 2021-10-26 | 2021-10-12 | 161000 | 90500 | 52.6 | 171.5 | -41.7 | -2.3 | 118.9 | 39.4 | P1 structural early-evidence + event guardrail |
| R8L2_PAB_263750_DOKEV_EVENT_PREMIUM | 263750 | R8L2_PAB_T2 | R8L2_PAB_T4 | R8L2_PAB_T2 | 2021-11-16 | 2021-10-13 | 138500 | 92700 | 4.8 | 56.6 | -34.5 | -2.9 | 51.8 | 31.6 | P1 structural early-evidence + event guardrail |
| R8L2_AHL_053800_POLITICAL_THEME | 053800 | R8L2_AHL_T5 | R8L2_AHL_T2 | R8L2_AHL_T5 | 2022-03-11 | 2022-03-23 | 86500 | 175800 | 152.6 | 24.3 | -14.2 | -53.9 | -128.3 | -39.7 | P1 structural early-evidence + event guardrail |


해석: after profile은 DEV/WEM에서 entry를 앞당기고, PAB/AHL에서는 event-only premium을 Green으로 올리지 않는다. 평균 MFE90은 baseline 대비 개선되지만, 핵심은 단순히 수익률을 키운 것이 아니라 “구조적 evidence와 event premium을 분리”한 것이다.

## 19. Score-Return Alignment Matrix

| alignment_label | trigger_count | avg_score_before | avg_score_after | avg_MFE90 | avg_MAE90 | verdict |
|---|---:|---:|---:|---:|---:|---|
| score_low_return_high_missed_structural | 1 | 47 | 61 | 833.3 | -13.0 | DEV_T1 승격 후보 |
| score_mid_return_high_promote_candidate | 5 | 60.8 | 70.8 | 157.0 | -12.6 | structural early evidence 승격 |
| score_high_return_low_false_positive | 1 | 74 | 65 | 4.8 | -34.5 | PAB Green 감점 필요 |
| score_mid_return_low_watch_only | 3 | 56.3 | 46.0 | 132.3 | -17.9 | event-only watch |
| score_high_return_high | 6 | 73.2 | 77.0 | 69.5 | -40.9 | 4B overlay 포함 |

## 20. Weight Sensitivity Table

row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
"shadow_weight","stage2_actionable_early_evidence_with_real_customer_or_revision",0,2,"+2","DEV/WEM early Stage2-Actionable rows produced very high MFE90 with acceptable initial MAE","baseline avg_MFE90 83.7 / avg_MAE90 -28.2 vs selected P1 avg_MFE90 146.5 / avg_MAE90 -20.5","R8L2_DEV_T2|R8L2_WEM_T2","2","shadow-only; event-only guardrail required"
"shadow_weight","event_premium_guardrail",0,3,"+3","PAB/AHL show price-only event premium can generate large MFE but lacks durable EPS/OP bridge and creates false Green risk","broad Green relaxation creates avg_MAE90 -28.0 and 3 late/false Green errors","R8L2_PAB_T4|R8L2_AHL_T1|R8L2_AHL_T2","3","shadow-only; do not reject watch, reject Green promotion"
"shadow_weight","green_confirmation_without_revision_bridge",0,-2,"-2","Green confirmation near obvious price highs missed upside or created false positive in DEV/PAB","DEV Green MFE90 21.1 vs DEV Stage2-Actionable 453.3; PAB Green MFE90 4.8 with MAE90 -34.5","R8L2_DEV_T4|R8L2_PAB_T4","2","shadow-only; not broad Green relaxation"
"shadow_weight","four_b_non_price_evidence_requirement",0,2,"+2","local/full peak proximity works, but price-only 4B should remain overlay-watch unless valuation/revision/positioning evidence is present","DEV/WEM 4B proximity 0.92/0.94 aligns with drawdown; PAB/AHL price-only 4B needs not become fundamental exit","R8L2_DEV_T5|R8L2_WEM_T5|R8L2_PAB_T5|R8L2_AHL_T5","4","shadow-only"

## 21. Optimization Decision Log

```jsonl
{"row_type":"optimization_decision","decision_id":"R8L2_DECISION_01","hypothesis":"R8 structural game hits can be caught before Green via Stage2-Actionable if launch/ranking/customer evidence and relative strength coexist.","tested_trigger_ids":["R8L2_DEV_T2","R8L2_WEM_T2"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus_with_event_guardrail","backtest_result_summary":"Stage2-Actionable entries materially improved MFE90 versus Green while MAE90 stayed acceptable in structural hit cases.","accepted_or_rejected":"accepted","delta_magnitude":"+2","why_not_larger_delta":"R8 also contains event-only and political-theme counterexamples.","risks":"over-promoting trailer/political price movement without revenue bridge","next_validation_needed":"R8 next loop should add platform/SaaS cases with reported ARR or operating-profit bridge."}
{"row_type":"optimization_decision","decision_id":"R8L2_DECISION_02","hypothesis":"Price-only event premium should not become Stage3-Green even when MFE is large.","tested_trigger_ids":["R8L2_PAB_T4","R8L2_AHL_T1","R8L2_AHL_T2"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus_with_event_guardrail","backtest_result_summary":"AHL produced huge MFE but was political premium; PAB Green near peak had low MFE and large MAE.","accepted_or_rejected":"accepted","delta_magnitude":"+3","why_not_larger_delta":"event premium can still be profitable as a watch/trade tier; do not hard reject all event moves.","risks":"may under-score legitimate content IP option value before reported numbers.","next_validation_needed":"separate game pipeline option value from political event premium."}
{"row_type":"optimization_decision","decision_id":"R8L2_DECISION_03","hypothesis":"Hard 4C protection is not validated in R8 loop 2.","tested_trigger_ids":["R8L2_WEM_T6","R8L2_AHL_T6"],"baseline_profile":"baseline_current_proxy","selected_profile":"four_c_thesis_break_earlier","backtest_result_summary":"Observed 4C-watch rows are late or event-premium unwind, not clean hard thesis-break examples.","accepted_or_rejected":"rejected_for_delta","delta_magnitude":"0","why_not_larger_delta":"no validated hard 4C trigger.","risks":"forcing 4C delta from event-premium unwind would overfit.","next_validation_needed":"find SaaS/accounting/security breach or platform regulation cases with true thesis break."}
```

## 22. Overfitting / Robustness Check

- Usable trigger count: 18
- Representative entry trigger count: 12
- Direction consistency: DEV/WEM은 Stage2-Actionable 승격 방향이 일관된다.
- Counterexample: PAB/AHL은 event-only momentum이 높은 MFE를 만들 수 있지만, fundamental Green 승격에는 실패한다.
- Delta cap: +2~+3 범위만 허용. hard 4C delta는 0.

## 23. Cross-case Aggregate Metrics

| trigger_type | usable_trigger_count | representative_trigger_count | avg_MFE90 | median_MFE90 | avg_MAE90 | median_MAE90 | avg_MFE180 | avg_MAE180 | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Stage2 | 3 | 3 | 369.0 | 208.6 | -10.1 | -11.7 | 443.4 | -19.7 | representative rows only |
| Stage2-Actionable | 4 | 4 | 208.5 | 162.1 | -6.8 | -5.2 | 241.6 | -27.9 | representative rows only |
| Stage3-Yellow | 2 | 2 | 167.9 | 167.9 | -16.6 | -16.6 | 207.5 | -35.2 | representative rows only |
| Stage3-Green | 3 | 3 | 26.2 | 21.1 | -38.2 | -38.3 | 35.8 | -56.4 | representative rows only |


## 24. Score-Price Alignment Verdict

```text
selected_shadow_profile = stage2_actionable_early_evidence_plus_with_event_guardrail
score_price_alignment = mixed_but_actionable
main_positive = Stage2-Actionable for real game hit / platform traction evidence
main_negative = event-only or political premium must not become fundamental Green
4B_verdict = split local/full peak proximity and require non-price evidence for full 4B
4C_verdict = not validated for hard gate in this loop
```

## 25. Validation Scope / Non-Validation Scope

### this_round_validates

- Stage2-Actionable early evidence for real game hit / platform traction with relative strength.
- Event-only/political premium guardrail.
- Stage3-Green lateness / false-positive risk.
- 4B local vs full-window proximity split.
- Price-only 4B watch rejection as full fundamental 4B unless non-price evidence exists.

### this_round_does_not_validate

- Broad Stage3-Green relaxation.
- Hard 4C protection.
- SaaS/ARR-specific R8 rules.
- Cybersecurity contract/order-driven rerating.
- Long-horizon 1Y/2Y adjusted-price calibration.

## 26. Shadow Weight Calibration

Recommended shadow-only changes:

1. `stage2_actionable_early_evidence_with_real_customer_or_revision`: +2
2. `event_premium_guardrail`: +3
3. `green_confirmation_without_revision_bridge`: -2
4. `four_b_non_price_evidence_requirement`: +2
5. `hard_4c_gate_delta`: 0

No production scoring is changed.

## 27. Machine-Readable Rows

### 27.1 Price source validation row JSONL

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 27.2 Case rows JSONL

```jsonl
{"row_type":"case","case_id":"R8L2_DEV_194480_COOKIE_RUN_KINGDOM","symbol":"194480","company_name":"데브시스터즈","case_type":"structural_success","primary_archetype":"MOBILE_GAME_IP_GLOBAL_HIT_REVENUE_RERATING","best_trigger":"R8L2_DEV_T2","notes":"쿠키런: 킹덤 launch/ranking/revenue evidence가 가격 상대강도와 결합된 전형적 Stage2-Actionable 승격 후보.","round":"R8","loop":"2","sector":"플랫폼·콘텐츠·SW·보안","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"mixed; early evidence worked for structural game hits, but event-only/political premium needs guardrail","price_source":"Songdaiki/stock-web"}
{"row_type":"case","case_id":"R8L2_WEM_112040_MIR4_WEMIX","symbol":"112040","company_name":"위메이드","case_type":"structural_success_with_crypto_overlay","primary_archetype":"GAME_PLATFORM_BLOCKCHAIN_P2E_RERATING","best_trigger":"R8L2_WEM_T2","notes":"2021-09~10 corporate-action candidate 이후의 post-adjustment tradable rows만 core calibration에 사용.","round":"R8","loop":"2","sector":"플랫폼·콘텐츠·SW·보안","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"mixed; early evidence worked for structural game hits, but event-only/political premium needs guardrail","price_source":"Songdaiki/stock-web"}
{"row_type":"case","case_id":"R8L2_PAB_263750_DOKEV_EVENT_PREMIUM","symbol":"263750","company_name":"펄어비스","case_type":"event_premium_overheat","primary_archetype":"NEW_GAME_TRAILER_PIPELINE_OPTION_VALUE","best_trigger":"R8L2_PAB_T2","notes":"DokeV trailer momentum은 강했지만, 비가격 실적 bridge가 약한 event premium 성격.","round":"R8","loop":"2","sector":"플랫폼·콘텐츠·SW·보안","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"mixed; early evidence worked for structural game hits, but event-only/political premium needs guardrail","price_source":"Songdaiki/stock-web"}
{"row_type":"case","case_id":"R8L2_AHL_053800_POLITICAL_THEME","symbol":"053800","company_name":"안랩","case_type":"price_moved_without_fundamental_evidence","primary_archetype":"CYBERSECURITY_POLITICAL_THEME_EVENT_PREMIUM","best_trigger":"R8L2_AHL_T5","notes":"보안 소프트웨어 본업 evidence보다 정치 이벤트 프리미엄이 가격을 지배한 반례.","round":"R8","loop":"2","sector":"플랫폼·콘텐츠·SW·보안","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"mixed; early evidence worked for structural game hits, but event-only/political premium needs guardrail","price_source":"Songdaiki/stock-web"}
```

### 27.3 Trigger rows JSONL

```jsonl
{"row_type":"trigger","trigger_id":"R8L2_DEV_T1","case_id":"R8L2_DEV_194480_COOKIE_RUN_KINGDOM","symbol":"194480","company_name":"데브시스터즈","round":"R8","loop":"2","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"MOBILE_GAME_IP_GLOBAL_HIT_REVENUE_RERATING","trigger_type":"Stage2","trigger_date":"2021-01-21","evidence_available_at_that_date":"Cookie Run: Kingdom released/ranking evidence visible; early market reaction.","evidence_source":"public game launch/ranking/news; see Source Notes","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv","profile_path":"atlas/symbol_profiles/194/194480.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-01-21","entry_price":17250,"MFE_30D_pct":300.0,"MFE_90D_pct":833.3,"MFE_180D_pct":1056.5,"MFE_1Y_pct":"unavailable_not_used_for_delta","MFE_2Y_pct":"unavailable_not_used_for_delta","MAE_30D_pct":-13.0,"MAE_90D_pct":-13.0,"MAE_180D_pct":-13.0,"MAE_1Y_pct":"unavailable_not_used_for_delta","below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2021-09-27","peak_price":199500,"drawdown_after_peak_pct":-80.1,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_or_entry_after_candidate","same_entry_group_id":"R8L2_DEV_194480_COOKIE_RUN_KINGDOM::2021-01-21::17250","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L2_DEV_T2","case_id":"R8L2_DEV_194480_COOKIE_RUN_KINGDOM","symbol":"194480","company_name":"데브시스터즈","round":"R8","loop":"2","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"MOBILE_GAME_IP_GLOBAL_HIT_REVENUE_RERATING","trigger_type":"Stage2-Actionable","trigger_date":"2021-01-25","evidence_available_at_that_date":"Launch traction plus limit-up style relative strength; early evidence became tradeable signal.","evidence_source":"stock-web OHLC + public game launch/ranking/news","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv","profile_path":"atlas/symbol_profiles/194/194480.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-01-25","entry_price":29100,"MFE_30D_pct":137.1,"MFE_90D_pct":453.3,"MFE_180D_pct":585.6,"MFE_1Y_pct":"unavailable_not_used_for_delta","MFE_2Y_pct":"unavailable_not_used_for_delta","MAE_30D_pct":-7.6,"MAE_90D_pct":-7.6,"MAE_180D_pct":-7.6,"MAE_1Y_pct":"unavailable_not_used_for_delta","below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2021-09-27","peak_price":199500,"drawdown_after_peak_pct":-80.1,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.61,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_or_entry_after_candidate","same_entry_group_id":"R8L2_DEV_194480_COOKIE_RUN_KINGDOM::2021-01-25::29100","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L2_DEV_T3","case_id":"R8L2_DEV_194480_COOKIE_RUN_KINGDOM","symbol":"194480","company_name":"데브시스터즈","round":"R8","loop":"2","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"MOBILE_GAME_IP_GLOBAL_HIT_REVENUE_RERATING","trigger_type":"Stage3-Yellow","trigger_date":"2021-02-18","evidence_available_at_that_date":"Repeated overseas/app ranking evidence; still before full reported earnings bridge.","evidence_source":"public ranking/news + stock-web OHLC","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv","profile_path":"atlas/symbol_profiles/194/194480.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-02-18","entry_price":48550,"MFE_30D_pct":231.6,"MFE_90D_pct":231.6,"MFE_180D_pct":310.9,"MFE_1Y_pct":"unavailable_not_used_for_delta","MFE_2Y_pct":"unavailable_not_used_for_delta","MAE_30D_pct":-13.0,"MAE_90D_pct":-13.0,"MAE_180D_pct":-13.0,"MAE_1Y_pct":"unavailable_not_used_for_delta","below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2021-09-27","peak_price":199500,"drawdown_after_peak_pct":-80.1,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.61,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"good_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_or_entry_after_candidate","same_entry_group_id":"R8L2_DEV_194480_COOKIE_RUN_KINGDOM::2021-02-18::48550","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L2_DEV_T4","case_id":"R8L2_DEV_194480_COOKIE_RUN_KINGDOM","symbol":"194480","company_name":"데브시스터즈","round":"R8","loop":"2","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"MOBILE_GAME_IP_GLOBAL_HIT_REVENUE_RERATING","trigger_type":"Stage3-Green","trigger_date":"2021-03-25","evidence_available_at_that_date":"Reported/visible hit evidence had become obvious; Green confirmation arrived after major rerating.","evidence_source":"public ranking/visible hit evidence + stock-web OHLC","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv","profile_path":"atlas/symbol_profiles/194/194480.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-03-25","entry_price":133000,"MFE_30D_pct":21.1,"MFE_90D_pct":21.1,"MFE_180D_pct":50.0,"MFE_1Y_pct":"unavailable_not_used_for_delta","MFE_2Y_pct":"unavailable_not_used_for_delta","MAE_30D_pct":-24.1,"MAE_90D_pct":-38.3,"MAE_180D_pct":-38.3,"MAE_1Y_pct":"unavailable_not_used_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-09-27","peak_price":199500,"drawdown_after_peak_pct":-80.1,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.61,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"late_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_or_entry_after_candidate","same_entry_group_id":"R8L2_DEV_194480_COOKIE_RUN_KINGDOM::2021-03-25::133000","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L2_DEV_T5","case_id":"R8L2_DEV_194480_COOKIE_RUN_KINGDOM","symbol":"194480","company_name":"데브시스터즈","round":"R8","loop":"2","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"MOBILE_GAME_IP_GLOBAL_HIT_REVENUE_RERATING","trigger_type":"Stage4B","trigger_date":"2021-09-27","evidence_available_at_that_date":"Full-cycle blowoff/valuation-positioning overlay near high.","evidence_source":"stock-web OHLC + price/valuation overlay","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv","profile_path":"atlas/symbol_profiles/194/194480.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-09-27","entry_price":186000,"MFE_30D_pct":7.8,"MFE_90D_pct":7.8,"MFE_180D_pct":7.8,"MFE_1Y_pct":"unavailable_not_used_for_delta","MFE_2Y_pct":"unavailable_not_used_for_delta","MAE_30D_pct":-29.5,"MAE_90D_pct":-65.0,"MAE_180D_pct":-78.6,"MAE_1Y_pct":"unavailable_not_used_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-09-27","peak_price":199500,"drawdown_after_peak_pct":-80.1,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":0.92,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":"valuation_blowoff|positioning_overheat","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"good_full_window_4B_timing","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_or_entry_after_candidate","same_entry_group_id":"R8L2_DEV_194480_COOKIE_RUN_KINGDOM::2021-09-27::186000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R8L2_WEM_T2","case_id":"R8L2_WEM_112040_MIR4_WEMIX","symbol":"112040","company_name":"위메이드","round":"R8","loop":"2","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"GAME_PLATFORM_BLOCKCHAIN_P2E_RERATING","trigger_type":"Stage2-Actionable","trigger_date":"2021-10-12","evidence_available_at_that_date":"Post-corporate-action tradable row; MIR4/WEMIX traction plus relative strength.","evidence_source":"MIR4 global/WEMIX public evidence + stock-web OHLC","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/112/112040/2021.csv","profile_path":"atlas/symbol_profiles/112/112040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-10-12","entry_price":90500,"MFE_30D_pct":171.5,"MFE_90D_pct":171.5,"MFE_180D_pct":171.5,"MFE_1Y_pct":"unavailable_not_used_for_delta","MFE_2Y_pct":"unavailable_not_used_for_delta","MAE_30D_pct":-2.3,"MAE_90D_pct":-2.3,"MAE_180D_pct":-43.4,"MAE_1Y_pct":"unavailable_not_used_for_delta","below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2021-11-22","peak_price":245700,"drawdown_after_peak_pct":-79.2,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.45,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_or_entry_after_candidate","same_entry_group_id":"R8L2_WEM_112040_MIR4_WEMIX::2021-10-12::90500","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L2_WEM_T3","case_id":"R8L2_WEM_112040_MIR4_WEMIX","symbol":"112040","company_name":"위메이드","round":"R8","loop":"2","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"GAME_PLATFORM_BLOCKCHAIN_P2E_RERATING","trigger_type":"Stage3-Yellow","trigger_date":"2021-10-15","evidence_available_at_that_date":"MIR4/WEMIX traction no longer just awareness; still before full blowoff.","evidence_source":"public MIR4/WEMIX evidence + stock-web OHLC","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/112/112040/2021.csv","profile_path":"atlas/symbol_profiles/112/112040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-10-15","entry_price":120300,"MFE_30D_pct":104.2,"MFE_90D_pct":104.2,"MFE_180D_pct":104.2,"MFE_1Y_pct":"unavailable_not_used_for_delta","MFE_2Y_pct":"unavailable_not_used_for_delta","MAE_30D_pct":-5.8,"MAE_90D_pct":-20.2,"MAE_180D_pct":-57.4,"MAE_1Y_pct":"unavailable_not_used_for_delta","below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2021-11-22","peak_price":245700,"drawdown_after_peak_pct":-79.2,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.45,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"good_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_or_entry_after_candidate","same_entry_group_id":"R8L2_WEM_112040_MIR4_WEMIX::2021-10-15::120300","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L2_WEM_T4","case_id":"R8L2_WEM_112040_MIR4_WEMIX","symbol":"112040","company_name":"위메이드","round":"R8","loop":"2","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"GAME_PLATFORM_BLOCKCHAIN_P2E_RERATING","trigger_type":"Stage3-Green","trigger_date":"2021-10-26","evidence_available_at_that_date":"Full momentum confirmation, but entry captures less remaining upside.","evidence_source":"public MIR4/WEMIX evidence + stock-web OHLC","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/112/112040/2021.csv","profile_path":"atlas/symbol_profiles/112/112040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-10-26","entry_price":161000,"MFE_30D_pct":52.6,"MFE_90D_pct":52.6,"MFE_180D_pct":52.6,"MFE_1Y_pct":"unavailable_not_used_for_delta","MFE_2Y_pct":"unavailable_not_used_for_delta","MAE_30D_pct":-8.1,"MAE_90D_pct":-41.7,"MAE_180D_pct":-68.2,"MAE_1Y_pct":"unavailable_not_used_for_delta","below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2021-11-22","peak_price":245700,"drawdown_after_peak_pct":-79.2,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.45,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"late_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_or_entry_after_candidate","same_entry_group_id":"R8L2_WEM_112040_MIR4_WEMIX::2021-10-26::161000","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L2_WEM_T5","case_id":"R8L2_WEM_112040_MIR4_WEMIX","symbol":"112040","company_name":"위메이드","round":"R8","loop":"2","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"GAME_PLATFORM_BLOCKCHAIN_P2E_RERATING","trigger_type":"Stage4B","trigger_date":"2021-11-19","evidence_available_at_that_date":"Blowoff/positioning/valuation overlay near full-cycle high.","evidence_source":"stock-web OHLC + valuation/positioning overlay","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/112/112040/2021.csv","profile_path":"atlas/symbol_profiles/112/112040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-11-19","entry_price":237000,"MFE_30D_pct":3.0,"MFE_90D_pct":3.0,"MFE_180D_pct":3.0,"MFE_1Y_pct":"unavailable_not_used_for_delta","MFE_2Y_pct":"unavailable_not_used_for_delta","MAE_30D_pct":-37.4,"MAE_90D_pct":-60.4,"MAE_180D_pct":-78.4,"MAE_1Y_pct":"unavailable_not_used_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-22","peak_price":245700,"drawdown_after_peak_pct":-79.2,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":0.94,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":"valuation_blowoff|positioning_overheat","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"good_full_window_4B_timing","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_or_entry_after_candidate","same_entry_group_id":"R8L2_WEM_112040_MIR4_WEMIX::2021-11-19::237000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R8L2_WEM_T6","case_id":"R8L2_WEM_112040_MIR4_WEMIX","symbol":"112040","company_name":"위메이드","round":"R8","loop":"2","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"GAME_PLATFORM_BLOCKCHAIN_P2E_RERATING","trigger_type":"Stage4C-watch","trigger_date":"2022-02-10","evidence_available_at_that_date":"Post-peak breakdown; crypto/game platform thesis risk had become price-visible.","evidence_source":"stock-web OHLC + public crypto/platform risk context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/112/112040/2022.csv","profile_path":"atlas/symbol_profiles/112/112040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-02-10","entry_price":106600,"MFE_30D_pct":6.8,"MFE_90D_pct":6.8,"MFE_180D_pct":6.8,"MFE_1Y_pct":"unavailable_not_used_for_delta","MFE_2Y_pct":"unavailable_not_used_for_delta","MAE_30D_pct":-12.6,"MAE_90D_pct":-41.9,"MAE_180D_pct":-51.3,"MAE_1Y_pct":"unavailable_not_used_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-22","peak_price":245700,"drawdown_after_peak_pct":-79.2,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"hard_4c_late","trigger_outcome_label":"hard_4c_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_or_entry_after_candidate","same_entry_group_id":"R8L2_WEM_112040_MIR4_WEMIX::2022-02-10::106600","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only"}
{"row_type":"trigger","trigger_id":"R8L2_PAB_T1","case_id":"R8L2_PAB_263750_DOKEV_EVENT_PREMIUM","symbol":"263750","company_name":"펄어비스","round":"R8","loop":"2","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"NEW_GAME_TRAILER_PIPELINE_OPTION_VALUE","trigger_type":"Stage2","trigger_date":"2021-08-26","evidence_available_at_that_date":"DokeV Gamescom trailer event; strong price reaction but weak immediate EPS bridge.","evidence_source":"DokeV Gamescom trailer + stock-web OHLC","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv","profile_path":"atlas/symbol_profiles/263/263750.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-08-26","entry_price":87900,"MFE_30D_pct":16.0,"MFE_90D_pct":65.2,"MFE_180D_pct":65.2,"MFE_1Y_pct":"unavailable_not_used_for_delta","MFE_2Y_pct":"unavailable_not_used_for_delta","MAE_30D_pct":-11.7,"MAE_90D_pct":-11.7,"MAE_180D_pct":-40.5,"MAE_1Y_pct":"unavailable_not_used_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":145200,"drawdown_after_peak_pct":-67.1,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.82,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"event_premium","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_or_entry_after_candidate","same_entry_group_id":"R8L2_PAB_263750_DOKEV_EVENT_PREMIUM::2021-08-26::87900","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L2_PAB_T2","case_id":"R8L2_PAB_263750_DOKEV_EVENT_PREMIUM","symbol":"263750","company_name":"펄어비스","round":"R8","loop":"2","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"NEW_GAME_TRAILER_PIPELINE_OPTION_VALUE","trigger_type":"Stage2-Actionable","trigger_date":"2021-10-13","evidence_available_at_that_date":"Trailer option value plus renewed momentum; still not full Green without earnings bridge.","evidence_source":"stock-web OHLC + DokeV public event","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv","profile_path":"atlas/symbol_profiles/263/263750.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-10-13","entry_price":92700,"MFE_30D_pct":56.6,"MFE_90D_pct":56.6,"MFE_180D_pct":56.6,"MFE_1Y_pct":"unavailable_not_used_for_delta","MFE_2Y_pct":"unavailable_not_used_for_delta","MAE_30D_pct":-2.9,"MAE_90D_pct":-2.9,"MAE_180D_pct":-43.6,"MAE_1Y_pct":"unavailable_not_used_for_delta","below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":145200,"drawdown_after_peak_pct":-67.1,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.82,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"good_entry_event_premium","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_or_entry_after_candidate","same_entry_group_id":"R8L2_PAB_263750_DOKEV_EVENT_PREMIUM::2021-10-13::92700","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L2_PAB_T4","case_id":"R8L2_PAB_263750_DOKEV_EVENT_PREMIUM","symbol":"263750","company_name":"펄어비스","round":"R8","loop":"2","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"NEW_GAME_TRAILER_PIPELINE_OPTION_VALUE","trigger_type":"Stage3-Green","trigger_date":"2021-11-16","evidence_available_at_that_date":"Price confirmation arrived near local/full peak; no immediate margin bridge.","evidence_source":"stock-web OHLC + public event context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv","profile_path":"atlas/symbol_profiles/263/263750.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-11-16","entry_price":138500,"MFE_30D_pct":4.8,"MFE_90D_pct":4.8,"MFE_180D_pct":4.8,"MFE_1Y_pct":"unavailable_not_used_for_delta","MFE_2Y_pct":"unavailable_not_used_for_delta","MAE_30D_pct":-18.4,"MAE_90D_pct":-34.5,"MAE_180D_pct":-62.6,"MAE_1Y_pct":"unavailable_not_used_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":145200,"drawdown_after_peak_pct":-67.1,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.82,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"false_positive_score","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_or_entry_after_candidate","same_entry_group_id":"R8L2_PAB_263750_DOKEV_EVENT_PREMIUM::2021-11-16::138500","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L2_PAB_T5","case_id":"R8L2_PAB_263750_DOKEV_EVENT_PREMIUM","symbol":"263750","company_name":"펄어비스","round":"R8","loop":"2","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"NEW_GAME_TRAILER_PIPELINE_OPTION_VALUE","trigger_type":"Stage4B","trigger_date":"2021-11-17","evidence_available_at_that_date":"Price-only/local blowoff near observed full-window peak.","evidence_source":"stock-web OHLC","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv","profile_path":"atlas/symbol_profiles/263/263750.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-11-17","entry_price":141000,"MFE_30D_pct":3.0,"MFE_90D_pct":3.0,"MFE_180D_pct":3.0,"MFE_1Y_pct":"unavailable_not_used_for_delta","MFE_2Y_pct":"unavailable_not_used_for_delta","MAE_30D_pct":-19.5,"MAE_90D_pct":-35.7,"MAE_180D_pct":-63.4,"MAE_1Y_pct":"unavailable_not_used_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":145200,"drawdown_after_peak_pct":-67.1,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":0.92,"four_b_timing_verdict":"price_only_local_4B_near_full_peak_but_non_price_evidence_weak","four_b_evidence_type":"price_only|positioning_overheat","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"price_only_local_4B_success","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_or_entry_after_candidate","same_entry_group_id":"R8L2_PAB_263750_DOKEV_EVENT_PREMIUM::2021-11-17::141000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R8L2_AHL_T1","case_id":"R8L2_AHL_053800_POLITICAL_THEME","symbol":"053800","company_name":"안랩","round":"R8","loop":"2","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"CYBERSECURITY_POLITICAL_THEME_EVENT_PREMIUM","trigger_type":"Stage2","trigger_date":"2022-03-03","evidence_available_at_that_date":"Ahn withdrew and endorsed Yoon; price reaction tied to political theme, not software EPS bridge.","evidence_source":"public election event + stock-web OHLC","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv","profile_path":"atlas/symbol_profiles/053/053800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-03-03","entry_price":70800,"MFE_30D_pct":208.6,"MFE_90D_pct":208.6,"MFE_180D_pct":208.6,"MFE_1Y_pct":"unavailable_not_used_for_delta","MFE_2Y_pct":"unavailable_not_used_for_delta","MAE_30D_pct":-5.6,"MAE_90D_pct":-5.6,"MAE_180D_pct":-5.6,"MAE_1Y_pct":"unavailable_not_used_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":false,"peak_date":"2022-03-24","peak_price":218500,"drawdown_after_peak_pct":-66.2,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"price_moved_without_evidence","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_or_entry_after_candidate","same_entry_group_id":"R8L2_AHL_053800_POLITICAL_THEME::2022-03-03::70800","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L2_AHL_T2","case_id":"R8L2_AHL_053800_POLITICAL_THEME","symbol":"053800","company_name":"안랩","round":"R8","loop":"2","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"CYBERSECURITY_POLITICAL_THEME_EVENT_PREMIUM","trigger_type":"Stage2-Actionable","trigger_date":"2022-03-11","evidence_available_at_that_date":"Political theme momentum accelerated after election; not backed by cybersecurity contract/revision evidence.","evidence_source":"public election event + stock-web OHLC","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv","profile_path":"atlas/symbol_profiles/053/053800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-03-11","entry_price":86500,"MFE_30D_pct":152.6,"MFE_90D_pct":152.6,"MFE_180D_pct":152.6,"MFE_1Y_pct":"unavailable_not_used_for_delta","MFE_2Y_pct":"unavailable_not_used_for_delta","MAE_30D_pct":-14.2,"MAE_90D_pct":-14.2,"MAE_180D_pct":-16.8,"MAE_1Y_pct":"unavailable_not_used_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-03-24","peak_price":218500,"drawdown_after_peak_pct":-66.2,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"event_premium","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_or_entry_after_candidate","same_entry_group_id":"R8L2_AHL_053800_POLITICAL_THEME::2022-03-11::86500","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L2_AHL_T5","case_id":"R8L2_AHL_053800_POLITICAL_THEME","symbol":"053800","company_name":"안랩","round":"R8","loop":"2","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"CYBERSECURITY_POLITICAL_THEME_EVENT_PREMIUM","trigger_type":"Stage4B","trigger_date":"2022-03-23","evidence_available_at_that_date":"Price-only/political-theme blowoff immediately before highest intraday spike.","evidence_source":"stock-web OHLC + election event context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv","profile_path":"atlas/symbol_profiles/053/053800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-03-23","entry_price":175800,"MFE_30D_pct":24.3,"MFE_90D_pct":24.3,"MFE_180D_pct":24.3,"MFE_1Y_pct":"unavailable_not_used_for_delta","MFE_2Y_pct":"unavailable_not_used_for_delta","MAE_30D_pct":-44.0,"MAE_90D_pct":-53.9,"MAE_180D_pct":-59.1,"MAE_1Y_pct":"unavailable_not_used_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-03-24","peak_price":218500,"drawdown_after_peak_pct":-66.2,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.71,"four_b_full_window_peak_proximity":0.71,"four_b_timing_verdict":"price_only_local_4B_near_full_peak_but_not_fundamental","four_b_evidence_type":"price_only|positioning_overheat","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"good_local_4B_timing_price_only","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_or_entry_after_candidate","same_entry_group_id":"R8L2_AHL_053800_POLITICAL_THEME::2022-03-23::175800","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R8L2_AHL_T6","case_id":"R8L2_AHL_053800_POLITICAL_THEME","symbol":"053800","company_name":"안랩","round":"R8","loop":"2","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"CYBERSECURITY_POLITICAL_THEME_EVENT_PREMIUM","trigger_type":"Stage4C-watch","trigger_date":"2022-03-30","evidence_available_at_that_date":"Event premium unwind after blowoff; no software thesis break needed because no software thesis was validated.","evidence_source":"stock-web OHLC","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv","profile_path":"atlas/symbol_profiles/053/053800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-03-30","entry_price":122800,"MFE_30D_pct":5.7,"MFE_90D_pct":5.7,"MFE_180D_pct":5.7,"MFE_1Y_pct":"unavailable_not_used_for_delta","MFE_2Y_pct":"unavailable_not_used_for_delta","MAE_30D_pct":-23.8,"MAE_90D_pct":-34.1,"MAE_180D_pct":-41.5,"MAE_1Y_pct":"unavailable_not_used_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-03-24","peak_price":218500,"drawdown_after_peak_pct":-66.2,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"false_fundamental_4c_not_applicable","trigger_outcome_label":"event_premium_unwind","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_or_entry_after_candidate","same_entry_group_id":"R8L2_AHL_053800_POLITICAL_THEME::2022-03-30::122800","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only"}
```

### 27.4 Score simulation rows JSONL

```jsonl
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R8L2_DEV_194480_COOKIE_RUN_KINGDOM","trigger_id":"R8L2_DEV_T1","symbol":"194480","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":10,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":47,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":3,"relative_strength_score":16,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage2-Actionable","changed_components":["relative_strength_score","customer_quality_score","revision_score"],"component_delta_explanation":"changed components are traceable to public evidence and OHLC-derived return/risk outcome; unknown components remain zero/not used.","selected_by_profile":false,"MFE_90D_pct":833.3,"MAE_90D_pct":-13.0,"score_return_alignment_label":"score_low_return_high_missed_structural","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R8L2_DEV_194480_COOKIE_RUN_KINGDOM","trigger_id":"R8L2_DEV_T2","symbol":"194480","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":14,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":58,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":4,"relative_strength_score":18,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable","changed_components":["relative_strength_score","customer_quality_score","revision_score","valuation_repricing_score"],"component_delta_explanation":"changed components are traceable to public evidence and OHLC-derived return/risk outcome; unknown components remain zero/not used.","selected_by_profile":true,"MFE_90D_pct":453.3,"MAE_90D_pct":-7.6,"score_return_alignment_label":"score_mid_return_high_promote_candidate","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R8L2_DEV_194480_COOKIE_RUN_KINGDOM","trigger_id":"R8L2_DEV_T3","symbol":"194480","trigger_type":"Stage3-Yellow","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":3,"relative_strength_score":15,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":63,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":17,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage3-Yellow","changed_components":["revision_score","relative_strength_score"],"component_delta_explanation":"changed components are traceable to public evidence and OHLC-derived return/risk outcome; unknown components remain zero/not used.","selected_by_profile":false,"MFE_90D_pct":231.6,"MAE_90D_pct":-13.0,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R8L2_DEV_194480_COOKIE_RUN_KINGDOM","trigger_id":"R8L2_DEV_T4","symbol":"194480","trigger_type":"Stage3-Green","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":7,"relative_strength_score":18,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":7,"relative_strength_score":18,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":76,"stage_label_after":"Stage3-Green","changed_components":[],"component_delta_explanation":"changed components are traceable to public evidence and OHLC-derived return/risk outcome; unknown components remain zero/not used.","selected_by_profile":false,"MFE_90D_pct":21.1,"MAE_90D_pct":-38.3,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R8L2_DEV_194480_COOKIE_RUN_KINGDOM","trigger_id":"R8L2_DEV_T5","symbol":"194480","trigger_type":"Stage4B","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage3-Green+4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":16,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82,"stage_label_after":"Stage3-Green+4B-watch","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"changed components are traceable to public evidence and OHLC-derived return/risk outcome; unknown components remain zero/not used.","selected_by_profile":false,"MFE_90D_pct":7.8,"MAE_90D_pct":-65.0,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R8L2_WEM_112040_MIR4_WEMIX","trigger_id":"R8L2_WEM_T2","symbol":"112040","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":14,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":60,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":18,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":74,"stage_label_after":"Stage2-Actionable","changed_components":["relative_strength_score","customer_quality_score","valuation_repricing_score"],"component_delta_explanation":"changed components are traceable to public evidence and OHLC-derived return/risk outcome; unknown components remain zero/not used.","selected_by_profile":true,"MFE_90D_pct":171.5,"MAE_90D_pct":-2.3,"score_return_alignment_label":"score_mid_return_high_promote_candidate","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R8L2_WEM_112040_MIR4_WEMIX","trigger_id":"R8L2_WEM_T3","symbol":"112040","trigger_type":"Stage3-Yellow","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":16,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":17,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score"],"component_delta_explanation":"changed components are traceable to public evidence and OHLC-derived return/risk outcome; unknown components remain zero/not used.","selected_by_profile":false,"MFE_90D_pct":104.2,"MAE_90D_pct":-20.2,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R8L2_WEM_112040_MIR4_WEMIX","trigger_id":"R8L2_WEM_T4","symbol":"112040","trigger_type":"Stage3-Green","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":18,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":79,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":18,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":79,"stage_label_after":"Stage3-Green","changed_components":[],"component_delta_explanation":"changed components are traceable to public evidence and OHLC-derived return/risk outcome; unknown components remain zero/not used.","selected_by_profile":false,"MFE_90D_pct":52.6,"MAE_90D_pct":-41.7,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R8L2_WEM_112040_MIR4_WEMIX","trigger_id":"R8L2_WEM_T5","symbol":"112040","trigger_type":"Stage4B","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":11,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Green+4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":16,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":13,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Green+4B-watch","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"changed components are traceable to public evidence and OHLC-derived return/risk outcome; unknown components remain zero/not used.","selected_by_profile":false,"MFE_90D_pct":3.0,"MAE_90D_pct":-60.4,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R8L2_WEM_112040_MIR4_WEMIX","trigger_id":"R8L2_WEM_T6","symbol":"112040","trigger_type":"Stage4C-watch","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":7,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":63,"stage_label_before":"4C-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":10,"legal_or_contract_risk_score":7,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":69,"stage_label_after":"4C-watch","changed_components":["execution_risk_score","legal_or_contract_risk_score","valuation_repricing_score"],"component_delta_explanation":"changed components are traceable to public evidence and OHLC-derived return/risk outcome; unknown components remain zero/not used.","selected_by_profile":false,"MFE_90D_pct":6.8,"MAE_90D_pct":-41.9,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R8L2_PAB_263750_DOKEV_EVENT_PREMIUM","trigger_id":"R8L2_PAB_T1","symbol":"263750","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":15,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":58,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":14,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":55,"stage_label_after":"Stage2-watch","changed_components":["execution_risk_score","customer_quality_score"],"component_delta_explanation":"changed components are traceable to public evidence and OHLC-derived return/risk outcome; unknown components remain zero/not used.","selected_by_profile":false,"MFE_90D_pct":65.2,"MAE_90D_pct":-11.7,"score_return_alignment_label":"score_mid_return_low_watch_only","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R8L2_PAB_263750_DOKEV_EVENT_PREMIUM","trigger_id":"R8L2_PAB_T2","symbol":"263750","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":16,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":16,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":62,"stage_label_after":"Stage2-Actionable-watch","changed_components":["execution_risk_score"],"component_delta_explanation":"changed components are traceable to public evidence and OHLC-derived return/risk outcome; unknown components remain zero/not used.","selected_by_profile":true,"MFE_90D_pct":56.6,"MAE_90D_pct":-2.9,"score_return_alignment_label":"score_mid_return_high_promote_candidate","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R8L2_PAB_263750_DOKEV_EVENT_PREMIUM","trigger_id":"R8L2_PAB_T4","symbol":"263750","trigger_type":"Stage3-Green","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":18,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":16,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":65,"stage_label_after":"Stage3-Yellow/4B-watch","changed_components":["execution_risk_score","relative_strength_score","customer_quality_score"],"component_delta_explanation":"changed components are traceable to public evidence and OHLC-derived return/risk outcome; unknown components remain zero/not used.","selected_by_profile":false,"MFE_90D_pct":4.8,"MAE_90D_pct":-34.5,"score_return_alignment_label":"score_high_return_low_false_positive","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R8L2_PAB_263750_DOKEV_EVENT_PREMIUM","trigger_id":"R8L2_PAB_T5","symbol":"263750","trigger_type":"Stage4B","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage3-Green+4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":15,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":75,"stage_label_after":"Stage3-Green+4B-watch","changed_components":["execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"changed components are traceable to public evidence and OHLC-derived return/risk outcome; unknown components remain zero/not used.","selected_by_profile":false,"MFE_90D_pct":3.0,"MAE_90D_pct":-35.7,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R8L2_AHL_053800_POLITICAL_THEME","trigger_id":"R8L2_AHL_T1","symbol":"053800","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":13,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":49,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":10,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":38,"stage_label_after":"event_premium_watch_only","changed_components":["relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"changed components are traceable to public evidence and OHLC-derived return/risk outcome; unknown components remain zero/not used.","selected_by_profile":false,"MFE_90D_pct":208.6,"MAE_90D_pct":-5.6,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R8L2_AHL_053800_POLITICAL_THEME","trigger_id":"R8L2_AHL_T2","symbol":"053800","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":17,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":57,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":11,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":41,"stage_label_after":"event_premium_watch_only","changed_components":["relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"changed components are traceable to public evidence and OHLC-derived return/risk outcome; unknown components remain zero/not used.","selected_by_profile":false,"MFE_90D_pct":152.6,"MAE_90D_pct":-14.2,"score_return_alignment_label":"score_mid_return_high_promote_candidate","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R8L2_AHL_053800_POLITICAL_THEME","trigger_id":"R8L2_AHL_T5","symbol":"053800","trigger_type":"Stage4B","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage3-Green+4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":13,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":60,"stage_label_after":"event_premium_4B-watch","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"changed components are traceable to public evidence and OHLC-derived return/risk outcome; unknown components remain zero/not used.","selected_by_profile":true,"MFE_90D_pct":24.3,"MAE_90D_pct":-53.9,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R8L2_AHL_053800_POLITICAL_THEME","trigger_id":"R8L2_AHL_T6","symbol":"053800","trigger_type":"Stage4C-watch","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":52,"stage_label_before":"4C-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":48,"stage_label_after":"event_premium_unwind_watch","changed_components":["execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"changed components are traceable to public evidence and OHLC-derived return/risk outcome; unknown components remain zero/not used.","selected_by_profile":false,"MFE_90D_pct":5.7,"MAE_90D_pct":-34.1,"score_return_alignment_label":"score_mid_return_low_watch_only","row_validation_status":"valid_for_shadow_calibration"}
```

### 27.5 Profile comparison rows CSV

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,avg_MAE_90D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,4,4,4,57.8,-32.2,0.75,0.75,0.25,1,2,unavailable,unavailable,"reference; late Green and event premium errors remain"
profile_comparison,stage2_actionable_early_evidence_plus_with_event_guardrail,4,4,3,176.4,-16.7,1.0,0.25,0.25,0,0,unavailable,unavailable,"best; earlier structural entries with event-only guardrail"
profile_comparison,stage3_yellow_entry_relaxed,4,4,4,104.2,-22.5,1.0,0.5,0.25,0,1,unavailable,unavailable,usable but worse than P1 risk
profile_comparison,green_confirmation_timing_relaxed,4,4,4,57.8,-32.2,0.75,0.75,0.5,0,3,unavailable,unavailable,reject broad Green relaxation
profile_comparison,four_b_peak_timing_tuned,4,4,0,overlay_only,overlay_only,overlay_only,overlay_only,0,0,0,0.91,0.88,"accepted for overlay split, not entry selection"
profile_comparison,four_c_thesis_break_earlier,4,2,0,overlay_only,overlay_only,overlay_only,overlay_only,0,0,0,unavailable,unavailable,no hard 4C delta in R8
```

### 27.6 Shadow weight CSV

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
"shadow_weight","stage2_actionable_early_evidence_with_real_customer_or_revision",0,2,"+2","DEV/WEM early Stage2-Actionable rows produced very high MFE90 with acceptable initial MAE","baseline avg_MFE90 83.7 / avg_MAE90 -28.2 vs selected P1 avg_MFE90 146.5 / avg_MAE90 -20.5","R8L2_DEV_T2|R8L2_WEM_T2","2","shadow-only; event-only guardrail required"
"shadow_weight","event_premium_guardrail",0,3,"+3","PAB/AHL show price-only event premium can generate large MFE but lacks durable EPS/OP bridge and creates false Green risk","broad Green relaxation creates avg_MAE90 -28.0 and 3 late/false Green errors","R8L2_PAB_T4|R8L2_AHL_T1|R8L2_AHL_T2","3","shadow-only; do not reject watch, reject Green promotion"
"shadow_weight","green_confirmation_without_revision_bridge",0,-2,"-2","Green confirmation near obvious price highs missed upside or created false positive in DEV/PAB","DEV Green MFE90 21.1 vs DEV Stage2-Actionable 453.3; PAB Green MFE90 4.8 with MAE90 -34.5","R8L2_DEV_T4|R8L2_PAB_T4","2","shadow-only; not broad Green relaxation"
"shadow_weight","four_b_non_price_evidence_requirement",0,2,"+2","local/full peak proximity works, but price-only 4B should remain overlay-watch unless valuation/revision/positioning evidence is present","DEV/WEM 4B proximity 0.92/0.94 aligns with drawdown; PAB/AHL price-only 4B needs not become fundamental exit","R8L2_DEV_T5|R8L2_WEM_T5|R8L2_PAB_T5|R8L2_AHL_T5","4","shadow-only"
```

### 27.7 Optimization decision rows JSONL

```jsonl
{"row_type":"optimization_decision","decision_id":"R8L2_DECISION_01","hypothesis":"R8 structural game hits can be caught before Green via Stage2-Actionable if launch/ranking/customer evidence and relative strength coexist.","tested_trigger_ids":["R8L2_DEV_T2","R8L2_WEM_T2"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus_with_event_guardrail","backtest_result_summary":"Stage2-Actionable entries materially improved MFE90 versus Green while MAE90 stayed acceptable in structural hit cases.","accepted_or_rejected":"accepted","delta_magnitude":"+2","why_not_larger_delta":"R8 also contains event-only and political-theme counterexamples.","risks":"over-promoting trailer/political price movement without revenue bridge","next_validation_needed":"R8 next loop should add platform/SaaS cases with reported ARR or operating-profit bridge."}
{"row_type":"optimization_decision","decision_id":"R8L2_DECISION_02","hypothesis":"Price-only event premium should not become Stage3-Green even when MFE is large.","tested_trigger_ids":["R8L2_PAB_T4","R8L2_AHL_T1","R8L2_AHL_T2"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus_with_event_guardrail","backtest_result_summary":"AHL produced huge MFE but was political premium; PAB Green near peak had low MFE and large MAE.","accepted_or_rejected":"accepted","delta_magnitude":"+3","why_not_larger_delta":"event premium can still be profitable as a watch/trade tier; do not hard reject all event moves.","risks":"may under-score legitimate content IP option value before reported numbers.","next_validation_needed":"separate game pipeline option value from political event premium."}
{"row_type":"optimization_decision","decision_id":"R8L2_DECISION_03","hypothesis":"Hard 4C protection is not validated in R8 loop 2.","tested_trigger_ids":["R8L2_WEM_T6","R8L2_AHL_T6"],"baseline_profile":"baseline_current_proxy","selected_profile":"four_c_thesis_break_earlier","backtest_result_summary":"Observed 4C-watch rows are late or event-premium unwind, not clean hard thesis-break examples.","accepted_or_rejected":"rejected_for_delta","delta_magnitude":"0","why_not_larger_delta":"no validated hard 4C trigger.","risks":"forcing 4C delta from event-premium unwind would overfit.","next_validation_needed":"find SaaS/accounting/security breach or platform regulation cases with true thesis break."}
```

### 27.8 Narrative-only rows JSONL

```jsonl
{"row_type":"narrative_only","case_id":"R8L2_WEM_112040_MIR4_WEMIX","symbol":"112040","reason":"early 2021-08/09 MIR4 global trigger overlaps 2021-09-13 and 2021-10-06 corporate-action candidate window in stock-web profile; excluded from weight calibration","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

### 27.9 Aggregate metric rows CSV

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,verdict
aggregate_metric,Stage2,3,3,369.0,208.6,-10.1,-11.7,"representative rows only"
aggregate_metric,Stage2-Actionable,4,4,208.5,162.1,-6.8,-5.2,"representative rows only"
aggregate_metric,Stage3-Yellow,2,2,167.9,167.9,-16.6,-16.6,"representative rows only"
aggregate_metric,Stage3-Green,3,3,26.2,21.1,-38.2,-38.3,"representative rows only"
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
current_round = R8
current_loop = 2
next_round = R9
next_sector = 모빌리티·운송·레저
carry_forward_questions =
- R8 SaaS/ARR and cybersecurity contract-driven rerating cases need separate loop.
- hard 4C still unvalidated.
- event premium guardrail should be tested in entertainment/platform non-game cases.
```

## 30. Source Notes

Stock-web manifest/schema/profile/price rows are cited inline above. Evidence sources used in this round are public historical launch/event references and are separated from stock-web OHLC. No current/live candidate screening was performed.
