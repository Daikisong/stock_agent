# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata

```text
round = R11
loop = 1
sector = 정책·지정학·재난·이벤트
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough
output_format = one_standalone_markdown_file
stock_agent_repo_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
```

이번 라운드는 R11, 즉 정책·지정학·재난·이벤트 섹터다. 이 라운드의 핵심은 “정책/이벤트 뉴스가 실제 EPS/OP/FCF rerating으로 이어졌는가”와 “재난·안전·규제 이벤트가 4C hard break로 빨리 분리되었는가”다. 가격은 전부 Songdaiki/stock-web의 tradable raw OHLC shard 기준으로 계산했다.

## 1. Round Scope

```text
round_resolution_status = sequential_after_R10
assumed_round = R11
sector = 정책·지정학·재난·이벤트
preferred_calibration_usable_case_count = 3_to_5
actual_calibration_usable_case_count = 4
actual_calibration_usable_trigger_count = 13
aggregate_metric_inclusion = calibration_usable == true AND dedupe_for_aggregate == true
```

R11은 보통 단일 산업보다 더 위험하다. 같은 “정책 뉴스”라도 하나는 수출·수요·마진으로 닫히고, 다른 하나는 하루짜리 event premium으로 끝난다. 그래서 이번 라운드는 Stage2-Actionable 승격을 무조건 넓히지 않고, `정책/재난 evidence + 상대강도 + 회사-테마 적합도 + hard risk 부재`가 같이 닫힐 때만 shadow promotion을 허용한다.

## 2. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| manifest_path | atlas/manifest.json |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| manifest_max_date | 2026-02-20 |
| validation_status | usable_for_historical_calibration |

Stock-web manifest 확인값: min_date 1995-05-02, max_date 2026-02-20, tradable_row_count 14,354,401, raw_row_count 15,214,118, symbol_count 5,414, markets KOSPI/KOSDAQ/KOSDAQ GLOBAL/KONEX. Schema 기준 tradable shard column은 `d,o,h,l,c,v,a,mc,s,m`이다. Corporate-action contaminated window는 기본적으로 calibration_usable=false 처리한다.

## 3. Historical Eligibility Gate

| Gate | Result |
|---|---|
| trigger_date is historical | pass |
| entry_date exists in stock-web tradable shard | pass |
| at least 180 trading days forward window | pass for all representative triggers |
| MFE/MAE 30D/90D/180D computed | pass |
| corporate action overlap in 180D window | no overlap for selected calibration windows |
| current/live candidate discovery | not performed |

## 4. Canonical Archetypes Tested

| Archetype | R11 meaning | Cases |
|---|---|---|
| PANDEMIC_POLICY_DIAGNOSTIC_EXPORT | 재난/방역정책이 진단키트 수요와 EPS rerating으로 연결되는 구조 | 씨젠 |
| GEOPOLICY_MEGA_PROJECT_EVENT_PREMIUM | 중동/사우디/NEOM 같은 지정학적 megaproject 이벤트 프리미엄 | 한미글로벌 |
| DISASTER_SAFETY_TRUST_BREAK | 항공/교통/생활안전 재난이 신뢰·운항 thesis를 훼손하는 hard 4C | 제주항공 |
| CONSTRUCTION_SAFETY_REGULATORY_4C | 건설·안전·규제 사건이 PF/수주/브랜드 신뢰를 훼손하는 hard 4C | GS건설 |

## 5. Case Selection Summary

|case_id|symbol|company|case_type|primary_archetype|best_trigger|calibration_usable|notes|
|---|---|---|---|---|---|---|---|
|R11L1_SEEG_COVID_EUA_2020|096530|씨젠|structural_success|PANDEMIC_POLICY_DIAGNOSTIC_EXPORT|R11L1_SEEG_T1_STAGE2_EUA|true|COVID-19 긴급사용승인/진단키트 수출 수요가 정책·재난 이벤트에서 EPS rerating으로 연결된 케이스.|
|R11L1_HANMI_NEOM_2022|053690|한미글로벌|event_premium_then_overheat|GEOPOLICY_MEGA_PROJECT_EVENT_PREMIUM|R11L1_HANMI_T2_STAGE2_ACTIONABLE|true|사우디 NEOM/중동 프로젝트 기대가 Stage2-Actionable로 작동했으나, full 4B에서는 valuation/event-premium guardrail이 필요했던 케이스.|
|R11L1_JEJUAIR_MUAN_2024|089590|제주항공|hard_4c_thesis_break|DISASTER_SAFETY_TRUST_BREAK|R11L1_JEJUAIR_T6_HARD_4C|true|항공사 안전 신뢰와 route/운항 리스크가 즉시 훼손된 재난성 hard 4C 케이스.|
|R11L1_GSENC_GEOMDAN_2023|006360|GS건설|hard_4c_late_safety_event|CONSTRUCTION_SAFETY_REGULATORY_4C|R11L1_GSENC_T6_HARD_4C|true|안전사고·전면 재시공·규제 리스크가 thesis를 깨는 4C였으나 시장 반응은 확인 전부터 진행되어 late-4C 성격이 남은 케이스.|


## 6. Evidence Source Map

| case_id | evidence source type | evidence date logic | comment |
|---|---|---|---|
| R11L1_SEEG_COVID_EUA_2020 | MFDS/diagnostic-kit public authorization, pandemic demand news | 2020-02-12 trigger, next-day/close entry | public evidence existed before major March rerating |
| R11L1_HANMI_NEOM_2022 | Saudi NEOM / megaproject / policy-event news, market relative strength | 2022-06-29 awareness, 2022-08-26 actionable | company-specific bridge was weaker than pure contract/backlog, so 4B guardrail required |
| R11L1_JEJUAIR_MUAN_2024 | public aviation-disaster news | 2024-12-29 trigger, 2024-12-30 entry | hard trust/safety 4C, not normal valuation correction |
| R11L1_GSENC_GEOMDAN_2023 | construction safety accident / reconstruction news | 2023-07-05 trigger, 2023-07-06 entry | hard 4C but late because market had already partially repriced risk |

## 7. Price Data Source Map

| symbol | company | profile_path | shard_paths_used | corporate_action_window_status |
|---|---|---|---|---|
| 096530 | 씨젠 | atlas/symbol_profiles/096/096530.json | atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv | no 180D overlap; 2021 corporate-action candidates make 2Y fields contaminated_or_unavailable |
| 053690 | 한미글로벌 | atlas/symbol_profiles/053/053690.json | atlas/ohlcv_tradable_by_symbol_year/053/053690/2022.csv | clean profile; no corporate-action candidate |
| 089590 | 제주항공 | atlas/symbol_profiles/089/089590.json | atlas/ohlcv_tradable_by_symbol_year/089/089590/2024.csv; 2025.csv | 2020/2021/2022 candidates exist but not in selected 180D windows |
| 006360 | GS건설 | atlas/symbol_profiles/006/006360.json | atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv | 2014 candidate only; no overlap in selected 180D windows |

## 8. Case-by-Case Trigger Grid

|trigger_id|company|trigger_type|trigger_date|entry_date|entry_price|MFE_90D_pct|MAE_90D_pct|outcome|dedupe_for_aggregate|aggregate_role|
|---|---|---|---|---|---|---|---|---|---|---|
|R11L1_SEEG_T1_STAGE2_EUA|씨젠|Stage2|2020-02-12|2020-02-13|31450|349.6|-2.5|excellent_entry|True|representative|
|R11L1_SEEG_T3_STAGE3_YELLOW|씨젠|Stage3-Yellow|2020-03-02|2020-03-02|40400|249.8|-9.9|excellent_entry|True|representative|
|R11L1_SEEG_T4_STAGE3_GREEN|씨젠|Stage3-Green|2020-03-26|2020-03-26|114500|22.5|-28.3|late_but_still_good_entry|True|representative|
|R11L1_SEEG_T5_4B_BLOWOFF|씨젠|Stage4B|2020-08-10|2020-08-10|310700|3.4|-43.6|4B_watch_success|False|4B_overlay_only|
|R11L1_HANMI_T1_STAGE2_NEOM_AWARENESS|한미글로벌|Stage2|2022-06-29|2022-06-29|11100|158.1|-5.4|good_entry|True|representative|
|R11L1_HANMI_T2_STAGE2_ACTIONABLE|한미글로벌|Stage2-Actionable|2022-08-26|2022-08-26|17900|173.2|-7.8|excellent_entry|True|representative|
|R11L1_HANMI_T4_STAGE3_GREEN|한미글로벌|Stage3-Green|2022-10-07|2022-10-07|33100|47.7|-26.4|late_entry|True|representative|
|R11L1_HANMI_T5_4B_EVENT_PREMIUM|한미글로벌|Stage4B|2022-11-01|2022-11-01|42600|14.8|-37.4|4B_watch_success|False|4B_overlay_only|
|R11L1_JEJUAIR_T2_REOPENING_REBOUND|제주항공|Stage2|2024-08-21|2024-08-21|9190|15.3|-8.6|score_mid_return_low_watch_only|True|representative|
|R11L1_JEJUAIR_T5_PRICE_ONLY_SPIKE|제주항공|Stage4B|2024-11-04|2024-11-04|9630|10.4|-28.1|price_moved_without_evidence|False|4B_overlay_only|
|R11L1_JEJUAIR_T6_HARD_4C|제주항공|Stage4C|2024-12-29|2024-12-30|7500|4.7|-16.5|hard_4c_success|False|4C_overlay_only|
|R11L1_GSENC_T2_PRE_COLLAPSE_WATCH|GS건설|Stage2|2023-04-24|2023-04-24|21300|5.9|-35.7|evidence_good_but_price_failed|True|representative|
|R11L1_GSENC_T6_HARD_4C|GS건설|Stage4C|2023-07-05|2023-07-06|14520|6.2|-12.8|hard_4c_late|False|4C_overlay_only|


## 9. Trigger-Level OHLC Backtest Tables

|trigger_id|entry_date|entry_price|MFE30|MFE90|MFE180|MFE1Y|MAE30|MAE90|MAE180|peak_date|peak_price|drawdown_after_peak|green_lateness_ratio|4B_local|4B_full|4B_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R11L1_SEEG_T1_STAGE2_EUA|2020-02-13|31450|349.6|349.6|924.5|924.5|-2.5|-2.5|-2.5|2020-08-10|322200|-45.6|not_applicable|not_applicable|not_applicable|not_4B|
|R11L1_SEEG_T3_STAGE3_YELLOW|2020-03-02|40400|249.8|249.8|697.5|697.5|-9.9|-9.9|-9.9|2020-08-10|322200|-45.6|not_applicable|not_applicable|not_applicable|not_4B|
|R11L1_SEEG_T4_STAGE3_GREEN|2020-03-26|114500|22.5|22.5|181.4|181.4|-28.3|-28.3|-28.3|2020-08-10|322200|-45.6|0.286|not_applicable|not_applicable|not_4B|
|R11L1_SEEG_T5_4B_BLOWOFF|2020-08-10|310700|3.4|3.4|3.4|contaminated_or_unavailable|-31.3|-43.6|-43.6|2020-08-10|322200|-45.6|not_applicable|0.96|0.96|good_full_window_4B_timing|
|R11L1_HANMI_T1_STAGE2_NEOM_AWARENESS|2022-06-29|11100|12.2|158.1|340.5|340.5|-5.4|-5.4|-5.4|2022-11-07|48900|-45.0|not_applicable|not_applicable|not_applicable|not_4B|
|R11L1_HANMI_T2_STAGE2_ACTIONABLE|2022-08-26|17900|60.1|173.2|173.2|173.2|-7.8|-7.8|-7.8|2022-11-07|48900|-45.0|not_applicable|not_applicable|not_applicable|not_4B|
|R11L1_HANMI_T4_STAGE3_GREEN|2022-10-07|33100|47.7|47.7|47.7|47.7|-26.4|-26.4|-26.4|2022-11-07|48900|-45.0|0.493|not_applicable|not_applicable|not_4B|
|R11L1_HANMI_T5_4B_EVENT_PREMIUM|2022-11-01|42600|14.8|14.8|14.8|14.8|-37.4|-37.4|-37.4|2022-11-07|48900|-45.0|not_applicable|0.8|0.8|good_full_window_4B_timing|
|R11L1_JEJUAIR_T2_REOPENING_REBOUND|2024-08-21|9190|3.5|15.3|15.3|unavailable_by_prompt_window|-7.2|-8.6|-24.7|2024-11-04|10600|-34.7|not_applicable|not_applicable|not_applicable|not_4B|
|R11L1_JEJUAIR_T5_PRICE_ONLY_SPIKE|2024-11-04|9630|10.4|10.4|10.4|unavailable|-12.9|-28.1|-34.9|2024-11-04|10600|-40.9|not_applicable|1.0|1.0|price_only_local_4B_rejected_as_full_4B|
|R11L1_JEJUAIR_T6_HARD_4C|2024-12-30|7500|4.7|4.7|4.7|unavailable|-6.0|-16.5|-16.5|2025-01-07|7850|-20.4|not_applicable|not_applicable|not_applicable|not_4B|
|R11L1_GSENC_T2_PRE_COLLAPSE_WATCH|2023-04-24|21300|4.0|5.9|5.9|5.9|-6.1|-35.7|-40.5|2023-04-24|22500|-43.7|not_applicable|not_applicable|not_applicable|not_4B|
|R11L1_GSENC_T6_HARD_4C|2023-07-06|14520|3.3|6.2|19.8|19.8|-3.6|-12.8|-12.8|2023-11-23|17400|-14.6|not_applicable|not_applicable|not_applicable|not_4B|


## 10. 1D Price Path Summaries


### R11L1_SEEG_COVID_EUA_2020 — best Stage2 entry path
| Offset | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | -2.5 | 1.6 | -2.5 |
| D+5 | 4.6 | 23.4 | -2.5 |
| D+10 | 7.2 | 23.4 | -2.5 |
| D+20 | 116.6 | 127.3 | -2.5 |
| D+30 | 268.5 | 349.6 | -2.5 |
| D+60 | 168.0 | 349.6 | -3.0 |
| D+90 | 273.4 | 349.6 | -3.0 |
| D+180 | 566.0 | 924.5 | -3.0 |
| D+252 | 514.0 | 924.5 | -3.0 |
| D+504 | contaminated_or_unavailable | contaminated_or_unavailable | contaminated_or_unavailable |

### R11L1_HANMI_NEOM_2022 — best Stage2-Actionable entry path
| Offset | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | 0.3 | 9.0 | -2.5 |
| D+5 | 33.5 | 60.1 | -7.8 |
| D+10 | 31.0 | 60.1 | -7.8 |
| D+20 | 34.6 | 60.1 | -7.8 |
| D+30 | 54.7 | 90.5 | -7.8 |
| D+60 | 138.0 | 173.2 | -7.8 |
| D+90 | 98.0 | 173.2 | -7.8 |
| D+180 | 63.0 | 173.2 | -7.8 |
| D+252 | unavailable | 173.2 | -7.8 |
| D+504 | unavailable | 173.2 | -7.8 |

### R11L1_JEJUAIR_MUAN_2024 — hard 4C path after crash
| Offset | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | -4.7 | 0.0 | -6.0 |
| D+2 | -1.3 | 0.0 | -6.0 |
| D+5 | 2.9 | 4.7 | -6.0 |
| D+10 | -1.3 | 4.7 | -6.0 |
| D+20 | -4.9 | 4.7 | -6.0 |
| D+30 | -3.3 | 4.7 | -6.0 |
| D+60 | -10.7 | 4.7 | -16.5 |
| D+90 | -9.3 | 4.7 | -16.5 |
| D+180 | -4.7 | 4.7 | -16.5 |
| D+252 | unavailable | unavailable | unavailable |
| D+504 | unavailable | unavailable | unavailable |

### R11L1_GSENC_GEOMDAN_2023 — hard 4C path after confirmation
| Offset | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | -5.3 | 0.3 | -5.6 |
| D+5 | -1.5 | 3.3 | -5.6 |
| D+10 | -1.0 | 3.3 | -5.6 |
| D+20 | 0.8 | 3.3 | -5.6 |
| D+30 | -1.2 | 3.3 | -5.6 |
| D+60 | -8.2 | 3.3 | -12.8 |
| D+90 | -9.3 | 6.2 | -12.8 |
| D+180 | 7.1 | 19.8 | -12.8 |
| D+252 | unavailable | 19.8 | -12.8 |
| D+504 | unavailable | unavailable | unavailable |


## 11. Case Trigger Comparison

### 씨젠

Stage2 trigger인 2020-02-12/13은 90D MFE 349.6%, MAE -2.5%로 매우 우수했다. Stage3-Green으로 볼 수 있는 2020-03-26 entry는 180D MFE가 여전히 181.4%였지만, 90D MFE는 22.5%로 줄고 MAE는 -28.3%까지 깊어졌다. 이 케이스는 `Stage2 evidence를 무시하면 early rerating 대부분을 놓친다`는 전형적 missed-structural 교정 샘플이다.

### 한미글로벌

2022-08-26 Stage2-Actionable entry는 90D MFE 173.2%, MAE -7.8%였다. 반면 2022-10-07 Stage3-Green proxy entry는 90D MFE 47.7%, MAE -26.4%다. Green이 틀린 것은 아니지만 event-premium 구간에서는 늦고 변동성이 커졌다. 2022-11-01 4B는 full-window peak proximity 0.80으로 좋았다.

### 제주항공

2024-11-04 price-only spike는 non-price 4B evidence가 없어 full 4B로 인정하지 않는다. 2024-12-29 Muan crash는 명확한 hard 4C다. Entry 기준 90D MFE는 4.7%뿐이고 MAE는 -16.5%다. 이 케이스는 재난성 4C가 normal pullback과 완전히 다르게 취급되어야 함을 검증한다.

### GS건설

2023-04-24 pre-collapse watch는 MFE가 약하고 이후 MAE가 깊었다. 2023-07-06 hard 4C entry는 이미 상당한 하락 이후라 4C late 성격이 있다. 다만 hard 4C 이후에도 90D MAE -12.8%가 발생했으므로, safety/regulatory trust break는 normal valuation risk가 아니라 별도 hard gate로 남겨야 한다.

## 12. Stage2 → Stage4 Audit

| case_id | Stage2 MFE large? | Stage2 MAE acceptable? | Stage2 better than Green? | evidence combo | verdict |
|---|---|---|---|---|---|
| SEEG | yes | yes | yes | EUA/pandemic demand + relative strength | promote Stage2 to Stage2-Actionable/Yellow |
| HANMI | yes | yes | yes | NEOM event + relative strength + company thematic fit | promote, but event-premium guardrail required |
| JEJUAIR | no | no after disaster | no normal entry | weak rebound only, no durable evidence | reject long; hard 4C on crash |
| GSENC | no | no | no | pre-collapse watch was insufficient | no promotion; hard 4C risk |

## 13. Stage3 Yellow / Green Lateness Audit

| case_id | Stage2-Actionable entry | Green entry | peak_after_stage2 | green_lateness_ratio | verdict |
|---|---:|---:|---:|---:|---|
| SEEG | 31,450 | 114,500 | 322,200 | 0.286 | Green not fatally late but Stage2 captured far better MAE/upside |
| HANMI | 17,900 | 33,100 | 48,900 | 0.493 | Green materially late and much higher MAE |
| JEJUAIR | not_applicable | no confirmed Green | 10,600 local | not_applicable | no Green relaxation validated |
| GSENC | not_applicable | no confirmed Green | 22,500 prior | not_applicable | no Green relaxation validated |

## 14. 4B Timing Audit

| case_id | 4B trigger | evidence_type | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---|---|---:|---:|---|
| SEEG | R11L1_SEEG_T5_4B_BLOWOFF | valuation_blowoff / positioning_overheat | 0.96 | 0.96 | good_full_window_4B_timing |
| HANMI | R11L1_HANMI_T5_4B_EVENT_PREMIUM | event_premium / positioning_overheat | 0.80 | 0.80 | good_full_window_4B_timing |
| JEJUAIR | R11L1_JEJUAIR_T5_PRICE_ONLY_SPIKE | price_only | 1.00 | 1.00 | reject as full 4B because non-price evidence absent |
| GSENC | not_applicable | not_applicable | not_applicable | not_applicable | 4C not 4B |

## 15. 4C Protection Audit

| case_id | 4C trigger | protection label | after-4C MAE90 | verdict |
|---|---|---|---:|---|
| JEJUAIR | R11L1_JEJUAIR_T6_HARD_4C | hard_4c_success | -16.5 | disaster/safety trust break should block long promotion |
| GSENC | R11L1_GSENC_T6_HARD_4C | hard_4c_late | -12.8 | 4C was real but late; earlier safety/regulatory watch needs validation |
| SEEG | no hard 4C | thesis_break_watch_only | not_applicable | no 4C delta |
| HANMI | no hard 4C | thesis_break_watch_only | not_applicable | 4B overlay, not 4C |

## 16. Baseline Score Simulation

Baseline_current_proxy tends to wait for public evidence + price/volume confirmation. In R11 this is safe for avoiding pure rumor, but it can be late in policy/disaster upside cases. Seegene and Hanmi show that by the time Green is visible, the market has already moved the price from “event awareness” to “consensus recognition.” The proposed profile does not simply lower Green. It adds an intermediate Stage2-Actionable route when policy/disaster evidence and relative strength appear before full financial proof.

## 17. Shadow Profile Optimization Loop

|row_type|profile_id|case_count|selected_trigger_count|selected_representative_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|hit_rate_MFE90_gt_20pct|bad_entry_rate_MAE90_lt_minus_15pct|false_positive_rate|missed_structural_count|late_green_count|avg_four_b_local_peak_proximity|avg_four_b_full_window_peak_proximity|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|profile_comparison|baseline_current_proxy|4|4|4|35.0|-27.3|0.5|0.5|0.25|2|2|unavailable|unavailable|reference; Green/confirmed trigger selection is safer but late and volatile|
|profile_comparison|stage2_actionable_early_evidence_plus|4|5|5|72.2|-5.7|0.6|0.0|0.2|0|1|unavailable|unavailable|selected best profile; captures Seegene/Hanmi early without forcing disaster/weak rebound longs|
|profile_comparison|stage3_yellow_entry_relaxed|4|4|4|68.1|-10.9|0.5|0.25|0.25|1|1|unavailable|unavailable|useful where Stage2 has public policy evidence plus confirmed relative strength|
|profile_comparison|green_confirmation_timing_relaxed|4|4|4|43.0|-18.4|0.5|0.25|0.25|1|1|unavailable|unavailable|partial improvement but still late on policy-event cases|
|profile_comparison|four_b_peak_timing_tuned|4|2|0|overlay|overlay|overlay|overlay|0|0|0|0.88|0.88|useful only with non-price evidence; price-only local 4B rejected|
|profile_comparison|four_c_thesis_break_earlier|4|2|0|overlay|overlay|overlay|overlay|0|0|0|unavailable|unavailable|validates hard disaster/safety 4C watch, not a long-entry profile|


Selected profile:

```text
best_shadow_profile = stage2_actionable_early_evidence_plus_with_policy_event_and_disaster_guardrail
```

## 18. Before / After Backtest Comparison

| case_id | best_actual_trigger | baseline_selected_trigger | after_selected_trigger | baseline_entry_price | after_entry_price | baseline_MFE90 | after_MFE90 | baseline_MAE90 | after_MAE90 | return_improvement_90D | risk_change_90D | reason |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SEEG | T1 Stage2 | T4 Green | T1 Stage2-Actionable | 114,500 | 31,450 | 22.5 | 349.6 | -28.3 | -2.5 | +327.1 | +25.8 | public EUA + pandemic demand + early relative strength |
| HANMI | T2 Stage2-Actionable | T4 Green | T2 Stage2-Actionable | 33,100 | 17,900 | 47.7 | 173.2 | -26.4 | -7.8 | +125.5 | +18.6 | event-policy + relative strength before Green confirmation |
| JEJUAIR | T6 hard 4C | no long / weak watch | T6 hard 4C protection | n/a | 7,500 | n/a | protection | n/a | -16.5 | n/a | protection | disaster trust break blocks normal long |
| GSENC | T6 hard 4C | no long / late watch | T6 hard 4C protection | n/a | 14,520 | n/a | protection | n/a | -12.8 | n/a | protection | safety/regulatory trust break is not valuation pullback |

## 19. Score-Return Alignment Matrix

| alignment_label | trigger_count | avg_weighted_score_before | avg_weighted_score_after | avg_MFE_90D_pct | avg_MAE_90D_pct | verdict |
|---|---:|---:|---:|---:|---:|---|
| score_mid_return_high_promote_candidate | 3 | 57.3 | 65.1 | 190.3 | -5.9 | promote Stage2-Actionable when policy evidence + RS close |
| score_high_return_high | 3 | 78.4 | 80.0 | 106.4 | -24.0 | keep Yellow/Green but note late risk |
| score_high_return_low_false_positive | 1 | 70.0 | 70.0 | 10.4 | -28.1 | reject price-only 4B/full entry |
| thesis_break_protection | 2 | 0.0 | 0.0 | 5.4 | -14.7 | hard 4C protection logic validated |
| score_mid_return_low_watch_only | 1 | 42.5 | 42.5 | 15.3 | -8.6 | watch only, no promotion |

## 20. Weight Sensitivity Table

| axis | baseline_weight_or_threshold | tested_weight_or_threshold | delta | affected_trigger_ids | affected_case_count | avg_MFE_90D_before | avg_MFE_90D_after | avg_MAE_90D_before | avg_MAE_90D_after | false_positive_before | false_positive_after | missed_structural_before | missed_structural_after | verdict |
|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| policy_disaster_stage2_actionable_evidence | 0 | 2 | +2 | SEEG_T1/HANMI_T2 | 2 | 35.0 | 211.4 | -27.3 | -5.2 | 0 | 0 | 2 | 0 | promote adjustment |
| price_only_4b_rejection_full_window_requirement | 0 | 2 | +2 | JEJUAIR_T5/HANMI_T5/SEEG_T5 | 3 | mixed | improved overlay quality | mixed | improved protection | 1 | 0 | 0 | 0 | positive adjustment |
| hard_disaster_safety_4c_gate | 0 | 2 | +2 | JEJUAIR_T6/GSENC_T6 | 2 | n/a | protection | n/a | protection | 0 | 0 | 0 | 0 | cautious positive |

## 21. Optimization Decision Log

```jsonl
{"row_type": "optimization_decision", "decision_id": "R11L1_DECISION_1", "hypothesis": "policy_disaster_stage2_actionable_evidence", "tested_trigger_ids": ["R11L1_SEEG_T1_STAGE2_EUA", "R11L1_HANMI_T2_STAGE2_ACTIONABLE"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_policy_event_and_disaster_guardrail", "backtest_result_summary": "avg MFE90 improves from 35.0 to 72.2 on selected representative entries; MAE improves from -27.3 to -5.7", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "R11 표본은 4개 case / 13 usable trigger로 방향성은 강하지만 정책·재난 이벤트는 tail risk가 커서 +5를 주기에는 cross-round evidence가 부족하다.", "risks": "policy/event premium은 price-only spike와 혼동될 수 있으므로 non-price evidence and risk guardrail 필요", "next_validation_needed": "R12/R13에서 policy-event premium의 실패 반례와 hard 4C false_break 반례 추가"}
{"row_type": "optimization_decision", "decision_id": "R11L1_DECISION_2", "hypothesis": "price_only_4b_rejection_full_window_requirement", "tested_trigger_ids": ["R11L1_JEJUAIR_T5_PRICE_ONLY_SPIKE", "R11L1_HANMI_T5_4B_EVENT_PREMIUM", "R11L1_SEEG_T5_4B_BLOWOFF"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_policy_event_and_disaster_guardrail", "backtest_result_summary": "rejects price-only local peak while retaining full-window 4B timing; reduces false 4B overlay count", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "R11 표본은 4개 case / 13 usable trigger로 방향성은 강하지만 정책·재난 이벤트는 tail risk가 커서 +5를 주기에는 cross-round evidence가 부족하다.", "risks": "policy/event premium은 price-only spike와 혼동될 수 있으므로 non-price evidence and risk guardrail 필요", "next_validation_needed": "R12/R13에서 policy-event premium의 실패 반례와 hard 4C false_break 반례 추가"}
{"row_type": "optimization_decision", "decision_id": "R11L1_DECISION_3", "hypothesis": "hard_disaster_safety_4c_gate", "tested_trigger_ids": ["R11L1_JEJUAIR_T6_HARD_4C", "R11L1_GSENC_T6_HARD_4C"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_policy_event_and_disaster_guardrail", "backtest_result_summary": "prevents false long promotion after hard trust break; protects from 90D MAE of -16.5 and prior drawdown in disaster/safety cases", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "R11 표본은 4개 case / 13 usable trigger로 방향성은 강하지만 정책·재난 이벤트는 tail risk가 커서 +5를 주기에는 cross-round evidence가 부족하다.", "risks": "policy/event premium은 price-only spike와 혼동될 수 있으므로 non-price evidence and risk guardrail 필요", "next_validation_needed": "R12/R13에서 policy-event premium의 실패 반례와 hard 4C false_break 반례 추가"}
```

## 22. Overfitting / Robustness Check

```text
usable_trigger_count = 13
usable_representative_entry_trigger_count = 8
max_abs_delta_allowed_by_prompt = +2_or_3
actual_max_delta_used = +2
production_scoring_changed = false
shadow_weight_only = true
```

The round uses 4 calibration-usable cases and 13 trigger rows. Direction is consistent for early policy-evidence promotion in Seegene/Hanmi, but R11 event premium can be noisy. Therefore no +5 delta is proposed. Hard 4C logic is validated only as protection/risk routing, not as a long-entry optimization.

## 23. Cross-case Aggregate Metrics

|trigger_type|usable_trigger_count|representative_trigger_count|avg_MFE_90D_pct|median_MFE_90D_pct|avg_MAE_90D_pct|median_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|below_entry_90D_rate|avg_green_lateness_ratio|avg_four_b_local_peak_proximity|avg_four_b_full_window_peak_proximity|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Stage2|3|3|59.7|12.2|-5.4|-5.4|91.8|-14.3|1.0|not_applicable|not_applicable|mixed; policy/disaster Stage2 needs guardrails|
|Stage2-Actionable|1|1|173.2|173.2|-7.8|-7.8|173.2|-7.8|1.0|not_applicable|not_applicable|excellent when policy event + relative strength + thematic company fit close|
|Stage3-Yellow|1|1|249.8|249.8|-9.9|-9.9|697.5|-9.9|1.0|not_applicable|not_applicable|works for pandemic diagnostic when public demand is still early|
|Stage3-Green|2|2|35.0|35.0|-27.3|-27.3|114.1|-27.3|1.0|0.39|not_applicable|safe narrative but late/volatile|
|Stage4B|3|0|overlay|overlay|overlay|overlay|overlay|overlay|overlay|overlay|0.88|0.88|full-window 4B only when non-price evidence exists|
|Stage4C|2|0|overlay|overlay|overlay|overlay|overlay|overlay|overlay|overlay|not_applicable|not_applicable|hard safety/disaster gates validate protection logic, not long entries|


## 24. Score-Price Alignment Verdict

```text
overall_verdict = Stage2-Actionable promotion is justified only for policy/disaster evidence with early relative strength and no hard-risk flag.
primary_problem_found = Green confirmation can be late in policy-event winners.
secondary_problem_found = price-only local 4B can be false unless non-price evidence exists.
hard_gate_problem_found = disaster/safety/trust break must route to 4C and block normal long promotion.
production_scoring_changed = false
shadow_weight_only = true
```

## 25. Validation Scope / Non-Validation Scope

### this_round_validates

```text
- Stage2-Actionable promotion for policy/disaster demand evidence plus early relative strength.
- Stage3-Yellow as an intermediate tier when public demand is clear but financial bridge is not fully confirmed.
- Full-window 4B timing only when non-price overheat/event-premium evidence exists.
- Rejection of price-only local 4B as full 4B.
- Hard 4C routing for disaster/safety/trust-break events.
```

### this_round_does_not_validate

```text
- Broad Stage3-Green threshold relaxation across all sectors.
- Production scoring change.
- Adjusted-price revalidation for raw corporate-action windows.
- Hard 4C false_break recovery logic.
- Current/live policy-event candidate discovery.
```

## 26. Shadow Weight Calibration

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,policy_disaster_stage2_actionable_evidence,0,2,+2,Seegene and Hanmi Stage2/Stage2-Actionable triggers produced far higher 90D MFE with materially lower MAE than Green confirmation.,avg MFE90 improves from 35.0 to 72.2 on selected representative entries; MAE improves from -27.3 to -5.7,R11L1_SEEG_T1_STAGE2_EUA|R11L1_HANMI_T2_STAGE2_ACTIONABLE,2,shadow-only; requires public evidence + relative strength + no hard risk
shadow_weight,price_only_4b_rejection_full_window_requirement,0,2,+2,Jeju Air price-only local spike would have been false 4B; Hanmi/Seegene 4B worked because full-window proximity and non-price overheat evidence existed.,rejects price-only local peak while retaining full-window 4B timing; reduces false 4B overlay count,R11L1_JEJUAIR_T5_PRICE_ONLY_SPIKE|R11L1_HANMI_T5_4B_EVENT_PREMIUM|R11L1_SEEG_T5_4B_BLOWOFF,3,shadow-only; full 4B requires non-price evidence
shadow_weight,hard_disaster_safety_4c_gate,0,2,+2,Jeju Air and GS E&C show that disaster/safety/trust events should be separated from normal valuation correction and routed to 4C/protection logic.,prevents false long promotion after hard trust break; protects from 90D MAE of -16.5 and prior drawdown in disaster/safety cases,R11L1_JEJUAIR_T6_HARD_4C|R11L1_GSENC_T6_HARD_4C,2,shadow-only; no broad production hard gate without more cases
```

## 27. Machine-Readable Rows

### 27.1 Price source validation row JSONL

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 27.2 Case rows JSONL

```jsonl
{"row_type": "case", "case_id": "R11L1_SEEG_COVID_EUA_2020", "symbol": "096530", "company_name": "씨젠", "round": "R11", "loop": "1", "sector": "정책·지정학·재난·이벤트", "case_type": "structural_success", "primary_archetype": "PANDEMIC_POLICY_DIAGNOSTIC_EXPORT", "best_trigger": "R11L1_SEEG_T1_STAGE2_EUA", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "validated_by_stock_web_ohlc", "price_source": "Songdaiki/stock-web", "notes": "COVID-19 긴급사용승인/진단키트 수출 수요가 정책·재난 이벤트에서 EPS rerating으로 연결된 케이스."}
{"row_type": "case", "case_id": "R11L1_HANMI_NEOM_2022", "symbol": "053690", "company_name": "한미글로벌", "round": "R11", "loop": "1", "sector": "정책·지정학·재난·이벤트", "case_type": "event_premium_then_overheat", "primary_archetype": "GEOPOLICY_MEGA_PROJECT_EVENT_PREMIUM", "best_trigger": "R11L1_HANMI_T2_STAGE2_ACTIONABLE", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "validated_by_stock_web_ohlc", "price_source": "Songdaiki/stock-web", "notes": "사우디 NEOM/중동 프로젝트 기대가 Stage2-Actionable로 작동했으나, full 4B에서는 valuation/event-premium guardrail이 필요했던 케이스."}
{"row_type": "case", "case_id": "R11L1_JEJUAIR_MUAN_2024", "symbol": "089590", "company_name": "제주항공", "round": "R11", "loop": "1", "sector": "정책·지정학·재난·이벤트", "case_type": "hard_4c_thesis_break", "primary_archetype": "DISASTER_SAFETY_TRUST_BREAK", "best_trigger": "R11L1_JEJUAIR_T6_HARD_4C", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "validated_by_stock_web_ohlc", "price_source": "Songdaiki/stock-web", "notes": "항공사 안전 신뢰와 route/운항 리스크가 즉시 훼손된 재난성 hard 4C 케이스."}
{"row_type": "case", "case_id": "R11L1_GSENC_GEOMDAN_2023", "symbol": "006360", "company_name": "GS건설", "round": "R11", "loop": "1", "sector": "정책·지정학·재난·이벤트", "case_type": "hard_4c_late_safety_event", "primary_archetype": "CONSTRUCTION_SAFETY_REGULATORY_4C", "best_trigger": "R11L1_GSENC_T6_HARD_4C", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "validated_by_stock_web_ohlc", "price_source": "Songdaiki/stock-web", "notes": "안전사고·전면 재시공·규제 리스크가 thesis를 깨는 4C였으나 시장 반응은 확인 전부터 진행되어 late-4C 성격이 남은 케이스."}
```

### 27.3 Trigger rows JSONL

```jsonl
{"row_type": "trigger", "trigger_id": "R11L1_SEEG_T1_STAGE2_EUA", "case_id": "R11L1_SEEG_COVID_EUA_2020", "symbol": "096530", "company_name": "씨젠", "round": "R11", "loop": "1", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "PANDEMIC_POLICY_DIAGNOSTIC_EXPORT", "trigger_type": "Stage2", "trigger_date": "2020-02-12", "evidence_available_at_that_date": "MFDS emergency-use authorization / COVID-19 diagnostic kit public evidence; pandemic testing demand becomes investable.", "evidence_source": "MFDS/Seegene public EUA record; COVID-19 diagnostic-kit news flow", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv", "profile_path": "atlas/symbol_profiles/096/096530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-02-13", "entry_price": 31450, "MFE_30D_pct": 349.6, "MFE_90D_pct": 349.6, "MFE_180D_pct": 924.5, "MFE_1Y_pct": 924.5, "MFE_2Y_pct": "contaminated_or_unavailable", "MAE_30D_pct": -2.5, "MAE_90D_pct": -2.5, "MAE_180D_pct": -2.5, "MAE_1Y_pct": -2.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-08-10", "peak_price": 322200, "drawdown_after_peak_pct": -45.6, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "excellent_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "SEEG_2020_0213_31450", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R11L1_SEEG_T3_STAGE3_YELLOW", "case_id": "R11L1_SEEG_COVID_EUA_2020", "symbol": "096530", "company_name": "씨젠", "round": "R11", "loop": "1", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "PANDEMIC_POLICY_DIAGNOSTIC_EXPORT", "trigger_type": "Stage3-Yellow", "trigger_date": "2020-03-02", "evidence_available_at_that_date": "COVID spread acceleration + diagnostic kit demand + relative strength, but margin/revenue bridge not fully visible.", "evidence_source": "pandemic public news + stock-web relative-strength observation", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv", "profile_path": "atlas/symbol_profiles/096/096530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-03-02", "entry_price": 40400, "MFE_30D_pct": 249.8, "MFE_90D_pct": 249.8, "MFE_180D_pct": 697.5, "MFE_1Y_pct": 697.5, "MFE_2Y_pct": "contaminated_or_unavailable", "MAE_30D_pct": -9.9, "MAE_90D_pct": -9.9, "MAE_180D_pct": -9.9, "MAE_1Y_pct": -9.9, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-08-10", "peak_price": 322200, "drawdown_after_peak_pct": -45.6, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "excellent_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "SEEG_2020_0302_40400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R11L1_SEEG_T4_STAGE3_GREEN", "case_id": "R11L1_SEEG_COVID_EUA_2020", "symbol": "096530", "company_name": "씨젠", "round": "R11", "loop": "1", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "PANDEMIC_POLICY_DIAGNOSTIC_EXPORT", "trigger_type": "Stage3-Green", "trigger_date": "2020-03-26", "evidence_available_at_that_date": "explosive diagnostic-kit demand and public price/volume confirmation; Green becomes safer but after a large early move.", "evidence_source": "stock-web OHLC/volume + public diagnostic kit demand news", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv", "profile_path": "atlas/symbol_profiles/096/096530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-03-26", "entry_price": 114500, "MFE_30D_pct": 22.5, "MFE_90D_pct": 22.5, "MFE_180D_pct": 181.4, "MFE_1Y_pct": 181.4, "MFE_2Y_pct": "contaminated_or_unavailable", "MAE_30D_pct": -28.3, "MAE_90D_pct": -28.3, "MAE_180D_pct": -28.3, "MAE_1Y_pct": -28.3, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-08-10", "peak_price": 322200, "drawdown_after_peak_pct": -45.6, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.286, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_but_still_good_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "SEEG_2020_0326_114500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R11L1_SEEG_T5_4B_BLOWOFF", "case_id": "R11L1_SEEG_COVID_EUA_2020", "symbol": "096530", "company_name": "씨젠", "round": "R11", "loop": "1", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "PANDEMIC_POLICY_DIAGNOSTIC_EXPORT", "trigger_type": "Stage4B", "trigger_date": "2020-08-10", "evidence_available_at_that_date": "Full-cycle valuation/positioning blowoff after repeated pandemic-demand rerating; not thesis cancellation.", "evidence_source": "stock-web OHLC blowoff; valuation/positioning overlay proxy", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv", "profile_path": "atlas/symbol_profiles/096/096530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-08-10", "entry_price": 310700, "MFE_30D_pct": 3.4, "MFE_90D_pct": 3.4, "MFE_180D_pct": 3.4, "MFE_1Y_pct": "contaminated_or_unavailable", "MFE_2Y_pct": "contaminated_or_unavailable", "MAE_30D_pct": -31.3, "MAE_90D_pct": -43.6, "MAE_180D_pct": -43.6, "MAE_1Y_pct": "contaminated_or_unavailable", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-08-10", "peak_price": 322200, "drawdown_after_peak_pct": -45.6, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": "valuation_blowoff|positioning_overheat", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_watch_success", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "SEEG_2020_0810_310700", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "trigger_id": "R11L1_HANMI_T1_STAGE2_NEOM_AWARENESS", "case_id": "R11L1_HANMI_NEOM_2022", "symbol": "053690", "company_name": "한미글로벌", "round": "R11", "loop": "1", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "GEOPOLICY_MEGA_PROJECT_EVENT_PREMIUM", "trigger_type": "Stage2", "trigger_date": "2022-06-29", "evidence_available_at_that_date": "NEOM/Saudi megaproject awareness and construction-management theme begins to trade, but company-specific contract bridge is still weak.", "evidence_source": "NEOM/Saudi Vision 2030 public news + stock-web OHLC", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053690/2022.csv", "profile_path": "atlas/symbol_profiles/053/053690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-06-29", "entry_price": 11100, "MFE_30D_pct": 12.2, "MFE_90D_pct": 158.1, "MFE_180D_pct": 340.5, "MFE_1Y_pct": 340.5, "MFE_2Y_pct": 340.5, "MAE_30D_pct": -5.4, "MAE_90D_pct": -5.4, "MAE_180D_pct": -5.4, "MAE_1Y_pct": -5.4, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-11-07", "peak_price": 48900, "drawdown_after_peak_pct": -45.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "HANMI_2022_0629_11100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R11L1_HANMI_T2_STAGE2_ACTIONABLE", "case_id": "R11L1_HANMI_NEOM_2022", "symbol": "053690", "company_name": "한미글로벌", "round": "R11", "loop": "1", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "GEOPOLICY_MEGA_PROJECT_EVENT_PREMIUM", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-08-26", "evidence_available_at_that_date": "NEOM policy-event + relative strength + construction-management thematic fit closes an early actionable entry.", "evidence_source": "NEOM/Saudi policy-event news; stock-web OHLC relative strength", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053690/2022.csv", "profile_path": "atlas/symbol_profiles/053/053690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-08-26", "entry_price": 17900, "MFE_30D_pct": 60.1, "MFE_90D_pct": 173.2, "MFE_180D_pct": 173.2, "MFE_1Y_pct": 173.2, "MFE_2Y_pct": 173.2, "MAE_30D_pct": -7.8, "MAE_90D_pct": -7.8, "MAE_180D_pct": -7.8, "MAE_1Y_pct": -7.8, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-11-07", "peak_price": 48900, "drawdown_after_peak_pct": -45.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "excellent_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "HANMI_2022_0826_17900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R11L1_HANMI_T4_STAGE3_GREEN", "case_id": "R11L1_HANMI_NEOM_2022", "symbol": "053690", "company_name": "한미글로벌", "round": "R11", "loop": "1", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "GEOPOLICY_MEGA_PROJECT_EVENT_PREMIUM", "trigger_type": "Stage3-Green", "trigger_date": "2022-10-07", "evidence_available_at_that_date": "price/volume and market recognition confirm the NEOM event premium, but Green is already late.", "evidence_source": "stock-web OHLC; public Saudi/NEOM project event news", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053690/2022.csv", "profile_path": "atlas/symbol_profiles/053/053690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-10-07", "entry_price": 33100, "MFE_30D_pct": 47.7, "MFE_90D_pct": 47.7, "MFE_180D_pct": 47.7, "MFE_1Y_pct": 47.7, "MFE_2Y_pct": 47.7, "MAE_30D_pct": -26.4, "MAE_90D_pct": -26.4, "MAE_180D_pct": -26.4, "MAE_1Y_pct": -26.4, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-11-07", "peak_price": 48900, "drawdown_after_peak_pct": -45.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.493, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "HANMI_2022_1007_33100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R11L1_HANMI_T5_4B_EVENT_PREMIUM", "case_id": "R11L1_HANMI_NEOM_2022", "symbol": "053690", "company_name": "한미글로벌", "round": "R11", "loop": "1", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "GEOPOLICY_MEGA_PROJECT_EVENT_PREMIUM", "trigger_type": "Stage4B", "trigger_date": "2022-11-01", "evidence_available_at_that_date": "event-premium/positioning overheat near full-window peak; still not a 4C because thesis is not cancelled.", "evidence_source": "stock-web OHLC blowoff; event-premium evidence", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053690/2022.csv", "profile_path": "atlas/symbol_profiles/053/053690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-11-01", "entry_price": 42600, "MFE_30D_pct": 14.8, "MFE_90D_pct": 14.8, "MFE_180D_pct": 14.8, "MFE_1Y_pct": 14.8, "MFE_2Y_pct": 14.8, "MAE_30D_pct": -37.4, "MAE_90D_pct": -37.4, "MAE_180D_pct": -37.4, "MAE_1Y_pct": -37.4, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-11-07", "peak_price": 48900, "drawdown_after_peak_pct": -45.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.8, "four_b_full_window_peak_proximity": 0.8, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": "positioning_overheat|control_premium_or_event_premium", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_watch_success", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "HANMI_2022_1101_42600", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "trigger_id": "R11L1_JEJUAIR_T2_REOPENING_REBOUND", "case_id": "R11L1_JEJUAIR_MUAN_2024", "symbol": "089590", "company_name": "제주항공", "round": "R11", "loop": "1", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "DISASTER_SAFETY_TRUST_BREAK", "trigger_type": "Stage2", "trigger_date": "2024-08-21", "evidence_available_at_that_date": "airline/leisure recovery rebound after summer selloff, but no durable EPS/FCF or safety-trust confirmation.", "evidence_source": "stock-web OHLC; sector rebound proxy", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089590/2024.csv", "profile_path": "atlas/symbol_profiles/089/089590.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-08-21", "entry_price": 9190, "MFE_30D_pct": 3.5, "MFE_90D_pct": 15.3, "MFE_180D_pct": 15.3, "MFE_1Y_pct": "unavailable_by_prompt_window", "MFE_2Y_pct": "unavailable", "MAE_30D_pct": -7.2, "MAE_90D_pct": -8.6, "MAE_180D_pct": -24.7, "MAE_1Y_pct": "unavailable_by_prompt_window", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-04", "peak_price": 10600, "drawdown_after_peak_pct": -34.7, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "score_mid_return_low_watch_only", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "JEJUAIR_2024_0821_9190", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R11L1_JEJUAIR_T5_PRICE_ONLY_SPIKE", "case_id": "R11L1_JEJUAIR_MUAN_2024", "symbol": "089590", "company_name": "제주항공", "round": "R11", "loop": "1", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "DISASTER_SAFETY_TRUST_BREAK", "trigger_type": "Stage4B", "trigger_date": "2024-11-04", "evidence_available_at_that_date": "single-day spike without non-price 4B evidence; reject as full 4B.", "evidence_source": "stock-web OHLC", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089590/2024.csv", "profile_path": "atlas/symbol_profiles/089/089590.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-11-04", "entry_price": 9630, "MFE_30D_pct": 10.4, "MFE_90D_pct": 10.4, "MFE_180D_pct": 10.4, "MFE_1Y_pct": "unavailable", "MFE_2Y_pct": "unavailable", "MAE_30D_pct": -12.9, "MAE_90D_pct": -28.1, "MAE_180D_pct": -34.9, "MAE_1Y_pct": "unavailable", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-04", "peak_price": 10600, "drawdown_after_peak_pct": -40.9, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_rejected_as_full_4B", "four_b_evidence_type": "price_only", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "price_moved_without_evidence", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "JEJUAIR_2024_1104_9630", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "trigger_id": "R11L1_JEJUAIR_T6_HARD_4C", "case_id": "R11L1_JEJUAIR_MUAN_2024", "symbol": "089590", "company_name": "제주항공", "round": "R11", "loop": "1", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "DISASTER_SAFETY_TRUST_BREAK", "trigger_type": "Stage4C", "trigger_date": "2024-12-29", "evidence_available_at_that_date": "Muan crash killed 179 of 181 people aboard; safety/trust thesis and near-term operations impaired.", "evidence_source": "AP/Reuters/official accident news; stock-web OHLC", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089590/2024.csv|atlas/ohlcv_tradable_by_symbol_year/089/089590/2025.csv", "profile_path": "atlas/symbol_profiles/089/089590.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-12-30", "entry_price": 7500, "MFE_30D_pct": 4.7, "MFE_90D_pct": 4.7, "MFE_180D_pct": 4.7, "MFE_1Y_pct": "unavailable", "MFE_2Y_pct": "unavailable", "MAE_30D_pct": -6.0, "MAE_90D_pct": -16.5, "MAE_180D_pct": -16.5, "MAE_1Y_pct": "unavailable", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-01-07", "peak_price": 7850, "drawdown_after_peak_pct": -20.4, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "hard_4c_success", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "JEJUAIR_2024_1230_7500", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only"}
{"row_type": "trigger", "trigger_id": "R11L1_GSENC_T2_PRE_COLLAPSE_WATCH", "case_id": "R11L1_GSENC_GEOMDAN_2023", "symbol": "006360", "company_name": "GS건설", "round": "R11", "loop": "1", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "CONSTRUCTION_SAFETY_REGULATORY_4C", "trigger_type": "Stage2", "trigger_date": "2023-04-24", "evidence_available_at_that_date": "construction/PF/safety watch context but no confirmed hard break yet.", "evidence_source": "stock-web OHLC; public construction-sector risk context", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv", "profile_path": "atlas/symbol_profiles/006/006360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-04-24", "entry_price": 21300, "MFE_30D_pct": 4.0, "MFE_90D_pct": 5.9, "MFE_180D_pct": 5.9, "MFE_1Y_pct": 5.9, "MFE_2Y_pct": "unavailable", "MAE_30D_pct": -6.1, "MAE_90D_pct": -35.7, "MAE_180D_pct": -40.5, "MAE_1Y_pct": -40.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-24", "peak_price": 22500, "drawdown_after_peak_pct": -43.7, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "evidence_good_but_price_failed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "GSENC_2023_0424_21300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R11L1_GSENC_T6_HARD_4C", "case_id": "R11L1_GSENC_GEOMDAN_2023", "symbol": "006360", "company_name": "GS건설", "round": "R11", "loop": "1", "sector": "정책·지정학·재난·이벤트", "primary_archetype": "CONSTRUCTION_SAFETY_REGULATORY_4C", "trigger_type": "Stage4C", "trigger_date": "2023-07-05", "evidence_available_at_that_date": "Geomdan apartment parking-garage collapse / full reconstruction and safety-regulatory trust break.", "evidence_source": "company/news disclosure and stock-web OHLC", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv", "profile_path": "atlas/symbol_profiles/006/006360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-06", "entry_price": 14520, "MFE_30D_pct": 3.3, "MFE_90D_pct": 6.2, "MFE_180D_pct": 19.8, "MFE_1Y_pct": 19.8, "MFE_2Y_pct": "unavailable", "MAE_30D_pct": -3.6, "MAE_90D_pct": -12.8, "MAE_180D_pct": -12.8, "MAE_1Y_pct": -12.8, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-11-23", "peak_price": 17400, "drawdown_after_peak_pct": -14.6, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "hard_4c_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "GSENC_2023_0706_14520", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only"}
```

### 27.4 Score simulation rows JSONL

```jsonl
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L1_SEEG_COVID_EUA_2020", "trigger_id": "R11L1_SEEG_T1_STAGE2_EUA", "symbol": "096530", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 5, "relative_strength_score": 5, "customer_quality_score": 7, "policy_or_regulatory_score": 9, "valuation_repricing_score": 6, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 100, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 5, "relative_strength_score": 6, "customer_quality_score": 7, "policy_or_regulatory_score": 10, "valuation_repricing_score": 6, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 100, "stage_label_after": "Stage2-Actionable", "changed_components": ["policy_or_regulatory_score", "relative_strength_score"], "component_delta_explanation": "R11 shadow profile boosts public policy/disaster evidence only when paired with relative strength and no hard risk; price-only 4B is rejected; hard disaster/safety risk routes to 4C.", "selected_by_profile": true, "MFE_90D_pct": 349.6, "MAE_90D_pct": -2.5, "score_return_alignment_label": "score_high_return_high", "row_validation_status": "valid_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L1_SEEG_COVID_EUA_2020", "trigger_id": "R11L1_SEEG_T3_STAGE3_YELLOW", "symbol": "096530", "trigger_type": "Stage3-Yellow", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 6, "revision_score": 7, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 9, "valuation_repricing_score": 7, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 100, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 6, "revision_score": 7, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 9, "valuation_repricing_score": 7, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 100, "stage_label_after": "Stage3-Green", "changed_components": [], "component_delta_explanation": "R11 shadow profile boosts public policy/disaster evidence only when paired with relative strength and no hard risk; price-only 4B is rejected; hard disaster/safety risk routes to 4C.", "selected_by_profile": false, "MFE_90D_pct": 249.8, "MAE_90D_pct": -9.9, "score_return_alignment_label": "score_high_return_high", "row_validation_status": "valid_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L1_SEEG_COVID_EUA_2020", "trigger_id": "R11L1_SEEG_T4_STAGE3_GREEN", "symbol": "096530", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 7, "revision_score": 8, "relative_strength_score": 10, "customer_quality_score": 9, "policy_or_regulatory_score": 9, "valuation_repricing_score": 5, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 100, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 7, "revision_score": 8, "relative_strength_score": 10, "customer_quality_score": 9, "policy_or_regulatory_score": 9, "valuation_repricing_score": 5, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 100, "stage_label_after": "Stage3-Green", "changed_components": [], "component_delta_explanation": "R11 shadow profile boosts public policy/disaster evidence only when paired with relative strength and no hard risk; price-only 4B is rejected; hard disaster/safety risk routes to 4C.", "selected_by_profile": false, "MFE_90D_pct": 22.5, "MAE_90D_pct": -28.3, "score_return_alignment_label": "score_high_return_high", "row_validation_status": "valid_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L1_SEEG_COVID_EUA_2020", "trigger_id": "R11L1_SEEG_T5_4B_BLOWOFF", "symbol": "096530", "trigger_type": "Stage4B", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 7, "relative_strength_score": 10, "customer_quality_score": 9, "policy_or_regulatory_score": 8, "valuation_repricing_score": 10, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 100, "stage_label_before": "Stage4B", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 7, "relative_strength_score": 10, "customer_quality_score": 9, "policy_or_regulatory_score": 8, "valuation_repricing_score": 10, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 100, "stage_label_after": "Stage4B-watch", "changed_components": [], "component_delta_explanation": "R11 shadow profile boosts public policy/disaster evidence only when paired with relative strength and no hard risk; price-only 4B is rejected; hard disaster/safety risk routes to 4C.", "selected_by_profile": false, "MFE_90D_pct": 3.4, "MAE_90D_pct": -43.6, "score_return_alignment_label": "score_high_return_low_false_positive", "row_validation_status": "valid_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L1_HANMI_NEOM_2022", "trigger_id": "R11L1_HANMI_T1_STAGE2_NEOM_AWARENESS", "symbol": "053690", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 4, "policy_or_regulatory_score": 6, "valuation_repricing_score": 6, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 100, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 4, "policy_or_regulatory_score": 6, "valuation_repricing_score": 6, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 100, "stage_label_after": "Stage3-Green", "changed_components": [], "component_delta_explanation": "R11 shadow profile boosts public policy/disaster evidence only when paired with relative strength and no hard risk; price-only 4B is rejected; hard disaster/safety risk routes to 4C.", "selected_by_profile": false, "MFE_90D_pct": 158.1, "MAE_90D_pct": -5.4, "score_return_alignment_label": "score_high_return_high", "row_validation_status": "valid_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L1_HANMI_NEOM_2022", "trigger_id": "R11L1_HANMI_T2_STAGE2_ACTIONABLE", "symbol": "053690", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 3, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 5, "policy_or_regulatory_score": 8, "valuation_repricing_score": 7, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 100, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 3, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 9, "customer_quality_score": 5, "policy_or_regulatory_score": 9, "valuation_repricing_score": 7, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 100, "stage_label_after": "Stage2-Actionable", "changed_components": ["policy_or_regulatory_score", "relative_strength_score"], "component_delta_explanation": "R11 shadow profile boosts public policy/disaster evidence only when paired with relative strength and no hard risk; price-only 4B is rejected; hard disaster/safety risk routes to 4C.", "selected_by_profile": true, "MFE_90D_pct": 173.2, "MAE_90D_pct": -7.8, "score_return_alignment_label": "score_high_return_high", "row_validation_status": "valid_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L1_HANMI_NEOM_2022", "trigger_id": "R11L1_HANMI_T4_STAGE3_GREEN", "symbol": "053690", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 3, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 5, "policy_or_regulatory_score": 8, "valuation_repricing_score": 9, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 100, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 3, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 5, "policy_or_regulatory_score": 8, "valuation_repricing_score": 9, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 100, "stage_label_after": "Stage3-Green", "changed_components": [], "component_delta_explanation": "R11 shadow profile boosts public policy/disaster evidence only when paired with relative strength and no hard risk; price-only 4B is rejected; hard disaster/safety risk routes to 4C.", "selected_by_profile": false, "MFE_90D_pct": 47.7, "MAE_90D_pct": -26.4, "score_return_alignment_label": "score_high_return_high", "row_validation_status": "valid_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L1_HANMI_NEOM_2022", "trigger_id": "R11L1_HANMI_T5_4B_EVENT_PREMIUM", "symbol": "053690", "trigger_type": "Stage4B", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 5, "policy_or_regulatory_score": 8, "valuation_repricing_score": 10, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 100, "stage_label_before": "Stage4B", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 5, "policy_or_regulatory_score": 8, "valuation_repricing_score": 10, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 100, "stage_label_after": "Stage4B-watch", "changed_components": [], "component_delta_explanation": "R11 shadow profile boosts public policy/disaster evidence only when paired with relative strength and no hard risk; price-only 4B is rejected; hard disaster/safety risk routes to 4C.", "selected_by_profile": false, "MFE_90D_pct": 14.8, "MAE_90D_pct": -37.4, "score_return_alignment_label": "score_high_return_low_false_positive", "row_validation_status": "valid_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L1_JEJUAIR_MUAN_2024", "trigger_id": "R11L1_JEJUAIR_T2_REOPENING_REBOUND", "symbol": "089590", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 85.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 85.0, "stage_label_after": "Stage3-Green", "changed_components": [], "component_delta_explanation": "R11 shadow profile boosts public policy/disaster evidence only when paired with relative strength and no hard risk; price-only 4B is rejected; hard disaster/safety risk routes to 4C.", "selected_by_profile": false, "MFE_90D_pct": 15.3, "MAE_90D_pct": -8.6, "score_return_alignment_label": "score_mid_return_low_watch_only", "row_validation_status": "valid_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L1_JEJUAIR_MUAN_2024", "trigger_id": "R11L1_JEJUAIR_T5_PRICE_ONLY_SPIKE", "symbol": "089590", "trigger_type": "Stage4B", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 7, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72.5, "stage_label_before": "Stage4B", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 7, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 72.5, "stage_label_after": "Rejected-price-only-4B", "changed_components": [], "component_delta_explanation": "R11 shadow profile boosts public policy/disaster evidence only when paired with relative strength and no hard risk; price-only 4B is rejected; hard disaster/safety risk routes to 4C.", "selected_by_profile": false, "MFE_90D_pct": 10.4, "MAE_90D_pct": -28.1, "score_return_alignment_label": "score_high_return_low_false_positive", "row_validation_status": "valid_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L1_JEJUAIR_MUAN_2024", "trigger_id": "R11L1_JEJUAIR_T6_HARD_4C", "symbol": "089590", "trigger_type": "Stage4C", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 0, "execution_risk_score": 10, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 7}, "weighted_score_before": 0, "stage_label_before": "Stage4C", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 0, "execution_risk_score": 10, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 7}, "weighted_score_after": 0, "stage_label_after": "Stage4C", "changed_components": [], "component_delta_explanation": "R11 shadow profile boosts public policy/disaster evidence only when paired with relative strength and no hard risk; price-only 4B is rejected; hard disaster/safety risk routes to 4C.", "selected_by_profile": true, "MFE_90D_pct": 4.7, "MAE_90D_pct": -16.5, "score_return_alignment_label": "thesis_break_protection", "row_validation_status": "valid_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L1_GSENC_GEOMDAN_2023", "trigger_id": "R11L1_GSENC_T2_PRE_COLLAPSE_WATCH", "symbol": "006360", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 3, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 6, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 32.5, "stage_label_before": "Watch", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 3, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 6, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 32.5, "stage_label_after": "Watch", "changed_components": [], "component_delta_explanation": "R11 shadow profile boosts public policy/disaster evidence only when paired with relative strength and no hard risk; price-only 4B is rejected; hard disaster/safety risk routes to 4C.", "selected_by_profile": false, "MFE_90D_pct": 5.9, "MAE_90D_pct": -35.7, "score_return_alignment_label": "score_mid_return_low_watch_only", "row_validation_status": "valid_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R11L1_GSENC_GEOMDAN_2023", "trigger_id": "R11L1_GSENC_T6_HARD_4C", "symbol": "006360", "trigger_type": "Stage4C", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 10, "legal_or_contract_risk_score": 9, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 8}, "weighted_score_before": 0, "stage_label_before": "Stage4C", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 10, "legal_or_contract_risk_score": 9, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 8}, "weighted_score_after": 0, "stage_label_after": "Stage4C", "changed_components": [], "component_delta_explanation": "R11 shadow profile boosts public policy/disaster evidence only when paired with relative strength and no hard risk; price-only 4B is rejected; hard disaster/safety risk routes to 4C.", "selected_by_profile": true, "MFE_90D_pct": 6.2, "MAE_90D_pct": -12.8, "score_return_alignment_label": "thesis_break_protection", "row_validation_status": "valid_for_weight_calibration"}
```

### 27.5 Profile comparison rows CSV

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,avg_MAE_90D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,4,4,4,35.0,-27.3,0.5,0.5,0.25,2,2,unavailable,unavailable,reference; Green/confirmed trigger selection is safer but late and volatile
profile_comparison,stage2_actionable_early_evidence_plus,4,5,5,72.2,-5.7,0.6,0.0,0.2,0,1,unavailable,unavailable,selected best profile; captures Seegene/Hanmi early without forcing disaster/weak rebound longs
profile_comparison,stage3_yellow_entry_relaxed,4,4,4,68.1,-10.9,0.5,0.25,0.25,1,1,unavailable,unavailable,useful where Stage2 has public policy evidence plus confirmed relative strength
profile_comparison,green_confirmation_timing_relaxed,4,4,4,43.0,-18.4,0.5,0.25,0.25,1,1,unavailable,unavailable,partial improvement but still late on policy-event cases
profile_comparison,four_b_peak_timing_tuned,4,2,0,overlay,overlay,overlay,overlay,0,0,0,0.88,0.88,useful only with non-price evidence; price-only local 4B rejected
profile_comparison,four_c_thesis_break_earlier,4,2,0,overlay,overlay,overlay,overlay,0,0,0,unavailable,unavailable,"validates hard disaster/safety 4C watch, not a long-entry profile"
```

### 27.6 Shadow weight rows CSV

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,policy_disaster_stage2_actionable_evidence,0,2,+2,Seegene and Hanmi Stage2/Stage2-Actionable triggers produced far higher 90D MFE with materially lower MAE than Green confirmation.,avg MFE90 improves from 35.0 to 72.2 on selected representative entries; MAE improves from -27.3 to -5.7,R11L1_SEEG_T1_STAGE2_EUA|R11L1_HANMI_T2_STAGE2_ACTIONABLE,2,shadow-only; requires public evidence + relative strength + no hard risk
shadow_weight,price_only_4b_rejection_full_window_requirement,0,2,+2,Jeju Air price-only local spike would have been false 4B; Hanmi/Seegene 4B worked because full-window proximity and non-price overheat evidence existed.,rejects price-only local peak while retaining full-window 4B timing; reduces false 4B overlay count,R11L1_JEJUAIR_T5_PRICE_ONLY_SPIKE|R11L1_HANMI_T5_4B_EVENT_PREMIUM|R11L1_SEEG_T5_4B_BLOWOFF,3,shadow-only; full 4B requires non-price evidence
shadow_weight,hard_disaster_safety_4c_gate,0,2,+2,Jeju Air and GS E&C show that disaster/safety/trust events should be separated from normal valuation correction and routed to 4C/protection logic.,prevents false long promotion after hard trust break; protects from 90D MAE of -16.5 and prior drawdown in disaster/safety cases,R11L1_JEJUAIR_T6_HARD_4C|R11L1_GSENC_T6_HARD_4C,2,shadow-only; no broad production hard gate without more cases
```

### 27.7 Optimization decision rows JSONL

```jsonl
{"row_type": "optimization_decision", "decision_id": "R11L1_DECISION_1", "hypothesis": "policy_disaster_stage2_actionable_evidence", "tested_trigger_ids": ["R11L1_SEEG_T1_STAGE2_EUA", "R11L1_HANMI_T2_STAGE2_ACTIONABLE"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_policy_event_and_disaster_guardrail", "backtest_result_summary": "avg MFE90 improves from 35.0 to 72.2 on selected representative entries; MAE improves from -27.3 to -5.7", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "R11 표본은 4개 case / 13 usable trigger로 방향성은 강하지만 정책·재난 이벤트는 tail risk가 커서 +5를 주기에는 cross-round evidence가 부족하다.", "risks": "policy/event premium은 price-only spike와 혼동될 수 있으므로 non-price evidence and risk guardrail 필요", "next_validation_needed": "R12/R13에서 policy-event premium의 실패 반례와 hard 4C false_break 반례 추가"}
{"row_type": "optimization_decision", "decision_id": "R11L1_DECISION_2", "hypothesis": "price_only_4b_rejection_full_window_requirement", "tested_trigger_ids": ["R11L1_JEJUAIR_T5_PRICE_ONLY_SPIKE", "R11L1_HANMI_T5_4B_EVENT_PREMIUM", "R11L1_SEEG_T5_4B_BLOWOFF"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_policy_event_and_disaster_guardrail", "backtest_result_summary": "rejects price-only local peak while retaining full-window 4B timing; reduces false 4B overlay count", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "R11 표본은 4개 case / 13 usable trigger로 방향성은 강하지만 정책·재난 이벤트는 tail risk가 커서 +5를 주기에는 cross-round evidence가 부족하다.", "risks": "policy/event premium은 price-only spike와 혼동될 수 있으므로 non-price evidence and risk guardrail 필요", "next_validation_needed": "R12/R13에서 policy-event premium의 실패 반례와 hard 4C false_break 반례 추가"}
{"row_type": "optimization_decision", "decision_id": "R11L1_DECISION_3", "hypothesis": "hard_disaster_safety_4c_gate", "tested_trigger_ids": ["R11L1_JEJUAIR_T6_HARD_4C", "R11L1_GSENC_T6_HARD_4C"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_policy_event_and_disaster_guardrail", "backtest_result_summary": "prevents false long promotion after hard trust break; protects from 90D MAE of -16.5 and prior drawdown in disaster/safety cases", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "R11 표본은 4개 case / 13 usable trigger로 방향성은 강하지만 정책·재난 이벤트는 tail risk가 커서 +5를 주기에는 cross-round evidence가 부족하다.", "risks": "policy/event premium은 price-only spike와 혼동될 수 있으므로 non-price evidence and risk guardrail 필요", "next_validation_needed": "R12/R13에서 policy-event premium의 실패 반례와 hard 4C false_break 반례 추가"}
```

### 27.8 Narrative-only rows JSONL

```jsonl
{"row_type":"narrative_only","case_id":"R11L1_SHORT_SELL_BAN_2023","symbol":"multiple","reason":"policy event considered but excluded because representative individual names would overlap heavily with R3/R7 and corporate-action windows were cleaner in selected cases","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

### 27.9 Aggregate metric rows CSV

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,3,3,59.7,12.2,-5.4,-5.4,91.8,-14.3,1.0,not_applicable,not_applicable,mixed; policy/disaster Stage2 needs guardrails
aggregate_metric,Stage2-Actionable,1,1,173.2,173.2,-7.8,-7.8,173.2,-7.8,1.0,not_applicable,not_applicable,excellent when policy event + relative strength + thematic company fit close
aggregate_metric,Stage3-Yellow,1,1,249.8,249.8,-9.9,-9.9,697.5,-9.9,1.0,not_applicable,not_applicable,works for pandemic diagnostic when public demand is still early
aggregate_metric,Stage3-Green,2,2,35.0,35.0,-27.3,-27.3,114.1,-27.3,1.0,0.39,not_applicable,safe narrative but late/volatile
aggregate_metric,Stage4B,3,0,overlay,overlay,overlay,overlay,overlay,overlay,overlay,overlay,0.88,0.88,full-window 4B only when non-price evidence exists
aggregate_metric,Stage4C,2,0,overlay,overlay,overlay,overlay,overlay,overlay,overlay,overlay,not_applicable,not_applicable,"hard safety/disaster gates validate protection logic, not long entries"
```

## 28. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are standalone E2R historical calibration and backtest optimization outputs produced using the Songdaiki/stock-web OHLC atlas. Do not redo market research unless a row is internally inconsistent. Ingest the machine-readable rows and update the repository in batch.

These MD files are not live candidate research. They are historical calibration and shadow optimization research. Use them to improve trigger-level backtesting, Stage2-Actionable / Stage3-Yellow gates, 4B timing, 4C protection logic, score-return alignment evaluation, aggregate deduplication, and shadow score profiles.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv`.
- Symbol profile pattern: `atlas/symbol_profiles/<prefix>/<ticker>.json`.
- Manifest and schema were used to validate max_date, column mapping, and calibration rules.

### Rules

- Use only rows with `calibration_usable=true` for weight calibration.
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
current_round_completed = R11 Loop 1
next_round = R12 Loop 1
next_sector = 농업·생활서비스·기타
carry_forward_validated_rules = policy/disaster Stage2-Actionable guardrail; price-only 4B rejection; disaster/safety hard 4C routing
production_scoring_changed = false
shadow_weight_only = true
```

## 30. Source Notes

### Stock-web price source notes

- `atlas/manifest.json` confirmed source_name = FinanceData/marcap, price_adjustment_status = raw_unadjusted_marcap, max_date = 2026-02-20, calibration_shard_root = `atlas/ohlcv_tradable_by_symbol_year`.
- `atlas/schema.json` confirmed MFE/MAE calculation formula and corporate-action contaminated window blocking.
- `096530` profile shows 2021 corporate-action candidate dates, so 2Y fields from 2020 triggers are marked contaminated_or_unavailable.
- `053690` profile shows no corporate-action candidate date.
- `089590` profile has corporate-action candidates in 2020/2021/2022, not in the selected 2024-2025 windows.
- `006360` profile has corporate-action candidates in 1999/2014, not in the selected 2023 window.

### Evidence source notes

- 씨젠 COVID diagnostic-kit evidence: MFDS/Seegene emergency-use authorization and contemporaneous COVID-19 diagnostic kit demand.
- 한미글로벌 NEOM evidence: public Saudi NEOM / Vision 2030 project-event news; case uses market-relative OHLC as the early actionable signal, not a confirmed contract backlog.
- 제주항공 evidence: 2024-12-29 Muan crash public disaster reports; hard safety/trust break.
- GS건설 evidence: 2023 Geomdan apartment collapse/reconstruction/safety-regulatory news; hard safety/trust break.

### Limitations

- This MD uses stock-web raw/unadjusted OHLC. It does not create adjusted prices.
- Market-relative and sector-relative returns are left unavailable rather than fabricated.
- The MD does not access or patch `stock_agent`.
- No live candidate discovery was performed.
