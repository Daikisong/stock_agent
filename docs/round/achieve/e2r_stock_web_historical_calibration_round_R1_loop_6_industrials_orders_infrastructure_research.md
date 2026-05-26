# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata

```text
research_session = historical_calibration_after_stock_web_ohlc_breakthrough
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough
round = R1
loop = 4
sector = 산업재·수주·인프라
sector_slug = industrials_orders_infrastructure
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
stock_agent_repo_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
output_file = e2r_stock_web_historical_calibration_round_R1_loop_4_industrials_orders_infrastructure_research.md
```

이 파일은 현재/live 종목 탐색이 아니라 과거 trigger-level calibration 파일이다. `stock_agent` 레포, 기존 `stock_agent` docs, `src/e2r` 코드, production scoring은 열지 않았다는 전제의 독립 연구 산출물이다. 가격 검증 기준은 `Songdaiki/stock-web`의 `tradable_raw` / `raw_unadjusted_marcap` 1D OHLCV row다.

## 1. Round Scope

이번 Loop 4는 R13 이후 순환 재개 라운드다. R1 Loop 3의 stock-web OHLC 검증 row를 기반으로 같은 R1 산업재·수주·인프라 evidence family를 재검증·재집계했다. stock_agent 레포는 열지 않았고 production scoring은 변경하지 않는다.

```text
R1 Loop 4 = 산업재·수주·인프라
round_resolution_status = continued_after_R13_loop_3
previous_round_next_state = R1
```

Loop 4의 초점은 **수주 headline이 실제 리레이팅 entry가 되는 조건**과 **headline만으로는 실패하는 조건**을 같은 테이블에 놓는 것이다. 전력망·원전·방산·EPC는 모두 “주문/정책/프로젝트”라는 같은 외피를 쓰지만, 가격경로는 전혀 다르게 움직인다. 이 라운드는 그래서 주문이라는 종이 한 장을 `backlog`, `margin bridge`, `relative strength`, `legal delay`, `valuation/positioning`이라는 실제 부품으로 분해한다.

## 2. Stock-Web OHLC Input / Price Source Validation

### 2.1 Manifest validation

| field | value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

### 2.2 Schema validation

Tradable shard columns are `d,o,h,l,c,v,a,mc,s,m`; raw shard additionally carries `rs`. MFE/MAE uses the schema rule: `max(high)` / `min(low)` from entry row through the requested forward window. Corporate-action-contaminated 180D windows are not used for weight calibration.

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 3. Historical Eligibility Gate

All selected triggers have a past trigger date, an entry row inside stock-web tradable shards, positive OHLCV, and at least 180 trading days of forward window. Some 1Y/2Y fields are explicitly marked unavailable or not used for delta when the MD does not need them for the accepted shadow rule. Aggregate metrics count only `calibration_usable=true` and `dedupe_for_aggregate=true` representative entry rows; 4B overlays are kept in a separate overlay aggregate.

## 4. Canonical Archetypes Tested

| archetype | tested role | gate focus |
|---|---|---|
| DEFENSE_GOVERNMENT_BACKLOG_EXPORT_REARMAMENT | structural_success | rearmament shock → export/order route → backlog visibility |
| DEFENSE_EXPORT_BACKLOG_POLAND_ARMOR | missed_structural / late Green | framework order + RS vs formal executive contract timing |
| NUCLEAR_INFRA_PREFERRED_BIDDER_TO_BACKLOG | volatile promote candidate | policy/project win with legal-delay overlay |
| GRID_EQUIPMENT_US_DATACENTER_CAPEX | volatile promote candidate | US grid/data-center revenue bridge with deep drawdown path |
| OVERSEAS_EPC_MEGA_CONTRACT_WITH_MARGIN_BRIDGE_GAP | failed rerating counterexample | large EPC headline without margin/revision bridge |

## 5. Case Selection Summary

|case_id|symbol|company|case_type|primary_archetype|best_trigger|MFE90|MAE90|alignment|
|---|---|---|---|---|---|---|---|---|
|R1L4_C01_HANWHA_AERO_DEFENSE_BACKLOG|012450|한화에어로스페이스|structural_success|DEFENSE_GOVERNMENT_BACKLOG_EXPORT_REARMAMENT|R1L4_C01_T1_STAGE2_WAR_REARMAMENT|33.3|-10.4|score_low_return_high_missed_structural|
|R1L4_C02_HYUNDAI_ROTEM_POLAND_K2|064350|현대로템|structural_success_with_late_green|DEFENSE_EXPORT_BACKLOG_POLAND_ARMOR|R1L4_C02_T2|34.6|-5.9|score_low_return_high_missed_structural|
|R1L4_C03_DOOSAN_NUCLEAR_POLICY_ORDER|034020|두산에너빌리티|missed_structural_with_policy_event_volatility|NUCLEAR_INFRA_PREFERRED_BIDDER_TO_BACKLOG|R1L4_C03_T2_STAGE2_ACTIONABLE_CZECH|17.65|-28.71|score_mid_return_high_but_high_mae|
|R1L4_C04_LS_ELECTRIC_GRID_DATACENTER|010120|LS ELECTRIC|stage2_promote_candidate_high_volatility|GRID_EQUIPMENT_US_DATACENTER_CAPEX|R1L4_C04_T2_STAGE2_ACTIONABLE_GRID|34.23|-38.29|score_mid_return_high_promote_candidate|
|R1L4_C05_SAMSUNG_EA_EPC_CONTRACT_FAIL|028050|삼성E&A|evidence_good_but_price_failed|OVERSEAS_EPC_MEGA_CONTRACT_WITH_MARGIN_BRIDGE_GAP|R1L4_C05_T2_STAGE2_ACTIONABLE_FADHILI|15.81|-14.62|score_mid_return_low_watch_only|

## 6. Evidence Source Map

| case_id | evidence source type | public evidence date logic | calibration meaning |
|---|---|---|---|
| R1L4_C01_HANWHA_AERO_DEFENSE_BACKLOG | geopolitical/rearmament news, defense export/order news | 2022-02-24 / 2022-07-29 / 2023-02-24 | earliest Stage2 already captured the structural defense cycle; later Green was safer but later. |
| R1L4_C02_HYUNDAI_ROTEM_POLAND_K2 | defense export framework and executive-contract reporting | 2022-06-08 / 2022-07-22 / 2022-08-26 | framework/order visibility + RS was a better trigger than formal contract Green. |
| R1L4_C03_DOOSAN_NUCLEAR_POLICY_ORDER | Czech nuclear preferred-bidder news and legal-delay news | 2024-07-17 / 2024-10-30 | policy win generated MFE, but MAE was deep; legal watch was too early as full 4B. |
| R1L4_C04_LS_ELECTRIC_GRID_DATACENTER | analyst/report news on US grid/data-center demand | 2024-07-01 | demand evidence worked directionally but volatility was extreme. |
| R1L4_C05_SAMSUNG_EA_EPC_CONTRACT_FAIL | Aramco Fadhili EPC award and share reaction news | 2024-04-02 / 2024-04-03 / 2024-08-01 | large contract without margin bridge failed as durable rerating. |

Evidence URLs used in this MD:

```text
Reuters — South Korea's winning bid for Czech nuclear power project
https://www.reuters.com/business/energy/south-koreas-winning-bid-czech-nuclear-power-project-2024-07-17/

Reuters — Czech watchdog prohibits nuclear power contract signing amid appeals
https://www.reuters.com/business/energy/czech-watchdog-prohibits-nuclear-power-contract-signing-amid-appeals-2024-10-30/

Reuters — Czech watchdog rejects appeals in nuclear power tender
https://www.reuters.com/business/energy/czech-watchdog-rejects-appeals-nuclear-power-tender-2024-10-31/

Reuters — Aramco awards $7.7 bln in contracts for Fadhili gas expansion
https://www.reuters.com/markets/commodities/aramco-awards-77-bln-contracts-fadhili-gas-expansion-2024-04-02/

WSJ/MarketWatch — Samsung E&A Shares Rise on $6 Billion Saudi Contract Win
https://www.wsj.com/articles/samsung-e-a-shares-rise-on-6-billion-saudi-contract-win-10a5b2f4

MarketWatch — LS Electric Could Gain From Solid U.S. Business Growth Opportunity
https://www.marketwatch.com/story/ls-electric-could-gain-from-solid-u-s-business-growth-opportunity-market-talk-3e926067

Poland / K2 public reporting references used for trigger dating:
Reuters 2025 follow-up on 2022 initial K2 agreement, plus Poland K2 public framework/executive contract references.
```

## 7. Price Data Source Map

| symbol | company | profile_path | shard_paths_used | corporate_action_window_status |
|---|---|---|---|---|
| 012450 | 한화에어로스페이스 | atlas/symbol_profiles/012/012450.json | atlas/ohlcv_tradable_by_symbol_year/012/012450/2022.csv; 2023.csv | clean_180D_window |
| 064350 | 현대로템 | atlas/symbol_profiles/064/064350.json | atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv; 2023.csv | clean_180D_window |
| 034020 | 두산에너빌리티 | atlas/symbol_profiles/034/034020.json | atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv; 2025.csv | clean_180D_window |
| 010120 | LS ELECTRIC | atlas/symbol_profiles/010/010120.json | atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv; 2025.csv | clean_180D_window |
| 028050 | 삼성E&A | atlas/symbol_profiles/028/028050.json | atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv; 2025.csv | clean_180D_window |

## 8. Case-by-Case Trigger Grid

|trigger_id|company|type|trigger_date|entry_date|entry_price|MFE90|MAE90|MFE180|MAE180|local4B|full4B|outcome|agg_role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R1L4_C01_T1_STAGE2_WAR_REARMAMENT|한화에어로스페이스|Stage2|2022-02-24|2022-02-24|45600|33.3|-10.4|73.7|-10.4|not_applicable|not_applicable|excellent_entry|representative|
|R1L4_C01_T2_STAGE2_ACTIONABLE_POLAND_ORDER_ROUTE|한화에어로스페이스|Stage2-Actionable|2022-07-29|2022-07-29|64400|23|-18.3|78.4|-18.3|not_applicable|not_applicable|excellent_entry|representative|
|R1L4_C01_T3_STAGE3_YELLOW_DELIVERY_SCALE|한화에어로스페이스|Stage3-Yellow|2022-08-26|2022-08-26|78400|14.5|-21.7|51.5|-21.7|not_applicable|not_applicable|good_entry|representative|
|R1L4_C01_T4_STAGE3_GREEN_EXPORT_MARGIN|한화에어로스페이스|Stage3-Green|2023-02-24|2023-02-24|92200|28.9|-4.2|63.8|-4.2|not_applicable|not_applicable|good_but_later_entry|representative|
|R1L4_C01_T5_STAGE4B_DEFENSE_OVERHEAT|한화에어로스페이스|Stage4B|2023-06-20|2023-06-20|142500|6|-19.1|6|-19.1|0.9|0.9|4B_watch_success|4B_overlay_only|
|R1L4_C02_T1|현대로템|Stage2|2022-06-08|2022-06-08|21050|56.1|-15.9|56.1|-15.9|not_applicable|not_applicable|good_entry|label_comparison_only|
|R1L4_C02_T2|현대로템|Stage2-Actionable|2022-07-22|2022-07-22|24400|34.6|-5.9|34.6|-5.9|not_applicable|not_applicable|excellent_entry|representative|
|R1L4_C02_T4|현대로템|Stage3-Green|2022-08-26|2022-08-26|30550|7.5|-24.5|23.7|-24.5|not_applicable|not_applicable|late_entry|label_comparison_only|
|R1L4_C02_T5|현대로템|Stage4B|2022-08-26|2022-08-26|30550|7.5|-24.5|23.7|-24.5|0.73|0.39|local_4B_watch_not_full_exit|4B_overlay_only|
|R1L4_C03_T1_STAGE2_CZECH_AWARENESS|두산에너빌리티|Stage2|2024-07-17|2024-07-17|21250|17.65|-28.71|45.41|-28.71|not_applicable|not_applicable|volatile_good_entry|label_comparison_only|
|R1L4_C03_T2_STAGE2_ACTIONABLE_CZECH|두산에너빌리티|Stage2-Actionable|2024-07-17|2024-07-17|21250|17.65|-28.71|45.41|-28.71|not_applicable|not_applicable|stage2_promote_candidate_with_deep_mae|representative|
|R1L4_C03_T5_STAGE4B_LEGAL_EARLY|두산에너빌리티|Stage4B|2024-10-30|2024-10-30|21400|44.39|-20.98|45.33|-20.98|0.02|0|4B_too_early_or_noise|4B_overlay_only|
|R1L4_C04_T1_STAGE2_GRID_AWARENESS|LS ELECTRIC|Stage2|2024-07-01|2024-07-01|204500|34.23|-38.29|48.41|-38.29|not_applicable|not_applicable|volatile_promote_candidate|label_comparison_only|
|R1L4_C04_T2_STAGE2_ACTIONABLE_GRID|LS ELECTRIC|Stage2-Actionable|2024-07-01|2024-07-01|204500|34.23|-38.29|48.41|-38.29|not_applicable|not_applicable|stage2_promote_candidate_with_extreme_mae|representative|
|R1L4_C05_T1_STAGE2_FADHILI_ORDER|삼성E&A|Stage2|2024-04-03|2024-04-03|25300|15.81|-14.62|15.81|-35.57|not_applicable|not_applicable|evidence_good_but_price_failed|label_comparison_only|
|R1L4_C05_T2_STAGE2_ACTIONABLE_FADHILI|삼성E&A|Stage2-Actionable|2024-04-03|2024-04-03|25300|15.81|-14.62|15.81|-35.57|not_applicable|not_applicable|evidence_good_but_price_failed|representative|
|R1L4_C05_T5_STAGE4B_EPC_LOCAL_PEAK|삼성E&A|Stage4B|2024-08-01|2024-08-01|29300|0|-33.1|0|-44.37|1|1|4B_watch_success|4B_overlay_only|

## 9. Trigger-Level OHLC Backtest Tables

### 9.1 Entry triggers and label-comparison rows

| trigger_id | entry | MFE30 | MFE90 | MFE180 | MFE1Y | MAE30 | MAE90 | MAE180 | below90 | peak_date | peak_price | drawdown_after_peak | usable | aggregate_role |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|---:|---:|---|
| R1L4_C01_T1_STAGE2_WAR_REARMAMENT | 2022-02-24 @ 45600 | 24.6 | 33.3 | 73.7 | 153.3 | -0.7 | -10.4 | -10.4 | True | 2023-04-10 | 118800 | -14 | True | representative |
| R1L4_C01_T2_STAGE2_ACTIONABLE_POLAND_ORDER_ROUTE | 2022-07-29 @ 64400 | 6.5 | 23 | 78.4 | 134.5 | -3.7 | -18.3 | -18.3 | True | 2023-07-27 | 151000 | -23.6 | True | representative |
| R1L4_C01_T3_STAGE3_YELLOW_DELIVERY_SCALE | 2022-08-26 @ 78400 | 10.2 | 14.5 | 51.5 | 92.6 | -5.2 | -21.7 | -21.7 | True | 2023-07-27 | 151000 | -23.6 | True | representative |
| R1L4_C01_T4_STAGE3_GREEN_EXPORT_MARGIN | 2023-02-24 @ 92200 | 8.5 | 28.9 | 63.8 | unavailable_not_needed_for_delta | -4.2 | -4.2 | -4.2 | True | 2023-07-27 | 151000 | -23.6 | True | representative |
| R1L4_C02_T1 | 2022-06-08 @ 21050 | 16.6 | 56.1 | 56.1 | 91.2 | -15.9 | -15.9 | -15.9 | True | 2023-06-21 | 40250 | unavailable_in_this_md | True | label_comparison_only |
| R1L4_C02_T2 | 2022-07-22 @ 24400 | 34.6 | 34.6 | 34.6 | 65 | -1.8 | -5.9 | -5.9 | True | 2023-06-21 | 40250 | unavailable_in_this_md | True | representative |
| R1L4_C02_T4 | 2022-08-26 @ 30550 | 7.5 | 7.5 | 23.7 | 31.8 | -17.9 | -24.5 | -24.5 | True | 2023-06-21 | 40250 | unavailable_in_this_md | True | label_comparison_only |
| R1L4_C03_T1_STAGE2_CZECH_AWARENESS | 2024-07-17 @ 21250 | 17.65 | 17.65 | 45.41 | 239.76 | -28.71 | -28.71 | -28.71 | True | 2025-06-30 | 72200 | -39.4 | True | label_comparison_only |
| R1L4_C03_T2_STAGE2_ACTIONABLE_CZECH | 2024-07-17 @ 21250 | 17.65 | 17.65 | 45.41 | 239.76 | -28.71 | -28.71 | -28.71 | True | 2025-06-30 | 72200 | -39.4 | True | representative |
| R1L4_C04_T1_STAGE2_GRID_AWARENESS | 2024-07-01 @ 204500 | 34.23 | 34.23 | 48.41 | 58.68 | -29.1 | -38.29 | -38.29 | True | 2025-06-24 | 324500 | -54.03 | True | label_comparison_only |
| R1L4_C04_T2_STAGE2_ACTIONABLE_GRID | 2024-07-01 @ 204500 | 34.23 | 34.23 | 48.41 | 58.68 | -29.1 | -38.29 | -38.29 | True | 2025-06-24 | 324500 | -54.03 | True | representative |
| R1L4_C05_T1_STAGE2_FADHILI_ORDER | 2024-04-03 @ 25300 | 6.72 | 15.81 | 15.81 | 15.81 | -3.75 | -14.62 | -35.57 | True | 2024-08-01 | 29300 | -44.37 | True | label_comparison_only |
| R1L4_C05_T2_STAGE2_ACTIONABLE_FADHILI | 2024-04-03 @ 25300 | 6.72 | 15.81 | 15.81 | 15.81 | -3.75 | -14.62 | -35.57 | True | 2024-08-01 | 29300 | -44.37 | True | representative |


### 9.2 4B overlay triggers

| trigger_id | entry | MFE90 | MAE90 | MFE180 | MAE180 | local_peak_proximity | full_window_peak_proximity | evidence_type | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| R1L4_C01_T5_STAGE4B_DEFENSE_OVERHEAT | 2023-06-20 @ 142500 | 6 | -19.1 | 6 | -19.1 | 0.9 | 0.9 | valuation_blowoff|positioning_overheat | good_full_window_4B_timing_as_overlay_not_thesis_break |
| R1L4_C02_T5 | 2022-08-26 @ 30550 | 7.5 | -24.5 | 23.7 | -24.5 | 0.73 | 0.39 | price_only|local_positioning_overheat | price_only_local_4B_too_early |
| R1L4_C03_T5_STAGE4B_LEGAL_EARLY | 2024-10-30 @ 21400 | 44.39 | -20.98 | 45.33 | -20.98 | 0.02 | 0 | legal_or_regulatory_block|price_only | price_only_or_legal_watch_too_early_for_full_cycle_4B |
| R1L4_C05_T5_STAGE4B_EPC_LOCAL_PEAK | 2024-08-01 @ 29300 | 0 | -33.1 | 0 | -44.37 | 1 | 1 | margin_or_backlog_slowdown|valuation_blowoff | good_local_and_full_4B_timing_with_margin_bridge_failure |


## 10. 1D Price Path Summaries

### 10.1 한화에어로스페이스 012450 — Stage2 2022-02-24 close 45,600

| anchor | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | 7.2 | 7.9 | -0.7 |
| D+20 | 21.7 | 28.1 | -0.7 |
| D+90 | -3.4 | 33.3 | -10.4 |
| D+180 | 60.0 | 73.7 | -10.4 |
| 1Y | not_used_for_delta | 153.3 | -10.4 |

### 10.2 현대로템 064350 — Stage2-Actionable 2022-07-22 close 24,400

| anchor | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+30 | 34.6 high-to-date | 34.6 | -1.8 |
| D+90 | positive but below first local high | 34.6 | -5.9 |
| D+180 | positive | 34.6 | -5.9 |
| Green +90D from 2022-08-26 | weak | 7.5 | -24.5 |

### 10.3 두산에너빌리티 034020 — Stage2-Actionable 2024-07-17 close 21,250

| anchor | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+30 | negative | 17.65 | -28.71 |
| D+90 | positive/volatile | 17.65 | -28.71 |
| D+180 | high-to-date 45.41 | 45.41 | -28.71 |
| 4B legal watch +90D | high-to-date 44.39 | 44.39 | -20.98 |

### 10.4 LS ELECTRIC 010120 — Stage2-Actionable 2024-07-01 close 204,500

| anchor | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+30 | volatile | 34.23 | -29.10 |
| D+90 | volatile | 34.23 | -38.29 |
| D+180 | positive | 48.41 | -38.29 |
| 1Y | positive | 58.68 | -38.29 |

### 10.5 삼성E&A 028050 — Stage2-Actionable 2024-04-03 close 25,300

| anchor | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+30 | small positive | 6.72 | -3.75 |
| D+90 | local peak area | 15.81 | -14.62 |
| D+180 | negative | 15.81 | -35.57 |
| 4B local peak +180 | negative | 0.0 | -44.37 |


## 11. Case Trigger Comparison

| case_id | best_trigger | baseline_selected_trigger | after_selected_trigger | verdict |
|---|---|---|---|---|
| R1L4_C01_HANWHA_AERO_DEFENSE_BACKLOG | R1L4_C01_T1_STAGE2_WAR_REARMAMENT | R1L4_C01_T4_STAGE3_GREEN_EXPORT_MARGIN | R1L4_C01_T1_STAGE2_WAR_REARMAMENT | Stage2 was earlier and still acceptable; Green was safer but late. |
| R1L4_C02_HYUNDAI_ROTEM_POLAND_K2 | R1L4_C02_T2 | R1L4_C02_T4 | R1L4_C02_T2 | Framework/RS trigger had much better MFE/MAE than formal contract. |
| R1L4_C03_DOOSAN_NUCLEAR_POLICY_ORDER | R1L4_C03_T2_STAGE2_ACTIONABLE_CZECH | R1L4_C03_T1_STAGE2_CZECH_AWARENESS | R1L4_C03_T2_STAGE2_ACTIONABLE_CZECH | Same entry date, but after-profile adds high-volatility guardrail. |
| R1L4_C04_LS_ELECTRIC_GRID_DATACENTER | R1L4_C04_T2_STAGE2_ACTIONABLE_GRID | R1L4_C04_T1_STAGE2_GRID_AWARENESS | R1L4_C04_T2_STAGE2_ACTIONABLE_GRID | Same entry date, but after-profile prevents clean Green overpromotion. |
| R1L4_C05_SAMSUNG_EA_EPC_CONTRACT_FAIL | R1L4_C05_T2_STAGE2_ACTIONABLE_FADHILI | R1L4_C05_T2_STAGE2_ACTIONABLE_FADHILI | watch_only_no_green | EPC headline needs margin/revision bridge before Green. |

## 12. Stage2 → Stage4 Audit

1. **한화에어로스페이스**: Stage2 rearmament trigger had MFE90 33.3 and MAE90 -10.4. This validates early Stage2-Actionable when geopolitical demand is tied to export/backlog route and RS.
2. **현대로템**: Stage2-Actionable framework trigger had MFE90 34.6 and MAE90 -5.9. Formal contract Green had MFE90 7.5 and MAE90 -24.5. This is the cleanest late-Green example in this loop.
3. **두산에너빌리티**: Czech preferred-bidder evidence generated MFE180 45.41 but MAE90 -28.71. It is promotable only as high-volatility Stage2-Actionable, not as clean Green.
4. **LS ELECTRIC**: US grid/data-center evidence produced MFE90 34.23 and MFE180 48.41, but MAE90 -38.29. The thesis direction was right; holding path was hostile.
5. **삼성E&A**: Fadhili EPC order had MFE90 15.81 and MAE180 -35.57. Contract headline without margin/revision bridge is watch-only and should not pass Green.

## 13. Stage3 Yellow / Green Lateness Audit

| case | Stage2/Actionable entry | Green entry | full-window peak | green_lateness_ratio | verdict |
|---|---:|---:|---:|---:|---|
| 한화에어로스페이스 | 45,600 / 64,400 | 92,200 | 151,000 | 0.37 vs T2 | Green acceptable but later than Stage2/Actionable. |
| 현대로템 | 24,400 | 30,550 | 40,250 | 0.39 full-window / 0.73 local | Green captured much less upside and much worse MAE. |
| 두산에너빌리티 | 21,250 | no confirmed Green in this MD | 72,200 | not_applicable | Do not relax Green; validate as high-volatility Stage2 only. |
| LS ELECTRIC | 204,500 | no confirmed Green in this MD | 324,500 | not_applicable | Directional but too volatile for broad Green relaxation. |
| 삼성E&A | 25,300 | no Green | 29,300 | not_applicable | EPC headline failed margin-bridge gate. |

## 14. 4B Timing Audit

The old single `four_b_peak_proximity` is split into local and full-window proximity. 4B is not an automatic sell signal. It is a risk overlay on top of an otherwise live thesis.

| trigger_id | local_peak_proximity | full_window_peak_proximity | evidence_type | timing_verdict |
|---|---:|---:|---|---|
| R1L4_C01_T5_STAGE4B_DEFENSE_OVERHEAT | 0.9 | 0.9 | valuation_blowoff\|positioning_overheat | good_full_window_4B_timing_as_overlay_not_thesis_break |
| R1L4_C02_T5 | 0.73 | 0.39 | price_only\|local_positioning_overheat | price_only_local_4B_too_early |
| R1L4_C03_T5_STAGE4B_LEGAL_EARLY | 0.02 | 0.003 | legal_or_regulatory_block\|price_only | too early as full 4B; legal watch only |
| R1L4_C05_T5_STAGE4B_EPC_LOCAL_PEAK | 1.0 | 1.0 | margin_or_backlog_slowdown\|valuation_blowoff | good local/full 4B timing with margin-bridge failure |

## 15. 4C Protection Audit

No hard 4C trigger is accepted for weight calibration in this loop. Samsung E&A is a **margin-bridge failure / 4B overlay** rather than a clean hard 4C, because the public thesis did not collapse in a single verified event before the drawdown. Doosan legal delay is also not hard 4C because legal appeals created watch risk but did not destroy the nuclear thesis in the 180D window.

```text
four_c_delta = 0
reason = hard_4c_not_confirmed_in_R1_loop_4
```

## 16. Baseline Score Simulation

Baseline proxy is treated as a reference only. It approximates a stricter confirmation system that tends to wait for formal Green or lets a contract headline look stronger than the actual margin/revision bridge.

```text
score_profile_id = baseline_current_proxy
profile_role = reference_only
production_scoring_changed = false
```

Key baseline failure modes:

- It recognizes Hanwha and Rotem too late if it waits for formal confirmation.
- It sees Doosan/LS direction correctly but under-labels the drawdown risk.
- It can over-score Samsung E&A if contract size is not paired with margin/revision bridge.

## 17. Shadow Profile Optimization Loop

row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,5,5,4,20.82,17.65,-22.06,-24.5,39.43,-26.25,0.4,0.6,0.2,2,2,0.56,unavailable,unavailable,"reference; formal Green/confirmation often late or fragile"
profile_comparison,stage2_actionable_early_evidence_plus,5,4,4,29.95,33.96,-20.83,-19.55,50.53,-20.83,0.75,0.5,0.0,0,1,0.37,unavailable,unavailable,"better upside capture; requires volatility guardrail for nuclear/grid names"
profile_comparison,stage3_yellow_entry_relaxed,5,4,4,27.37,28.6,-22.8,-23.16,51.7,-22.8,0.75,0.75,0.0,0,1,0.45,unavailable,unavailable,valid only with MAE cap and position sizing
profile_comparison,green_confirmation_timing_relaxed,5,4,4,22.07,23.28,-23.92,-26.16,45.33,-23.92,0.5,0.75,0.0,1,2,0.56,unavailable,unavailable,relaxing Green alone does not solve high-MAE names
profile_comparison,four_b_peak_timing_tuned,5,4,0,14.47,6.75,-24.42,-22.74,18.76,-27.24,0.25,1.0,0.0,0,0,unavailable,0.66,0.57,"price-only local 4B rejected; non-price valuation/margin/legal evidence required"
profile_comparison,four_c_thesis_break_earlier,5,0,0,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,"not validated; no hard 4C trigger in this R1 loop"

## 18. Before / After Backtest Comparison

|case_id|symbol|best_actual_trigger|baseline_selected_trigger|after_selected_trigger|baseline_entry_date|after_entry_date|baseline_entry_price|after_entry_price|baseline_MFE_90D_pct|after_MFE_90D_pct|baseline_MAE_90D_pct|after_MAE_90D_pct|baseline_MFE_180D_pct|after_MFE_180D_pct|baseline_MAE_180D_pct|after_MAE_180D_pct|return_improvement_90D_pct|risk_change_90D_pct|upside_capture_improvement_pct|reason_after_profile_selected|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R1L4_C01_HANWHA_AERO_DEFENSE_BACKLOG|012450|R1L4_C01_T1_STAGE2_WAR_REARMAMENT|R1L4_C01_T4_STAGE3_GREEN_EXPORT_MARGIN|R1L4_C01_T1_STAGE2_WAR_REARMAMENT|2023-02-24|2022-02-24|92200|45600|28.9|33.3|-4.2|-10.4|63.8|73.7|-4.2|-10.4|4.4|-6.2|earlier_entry_captures_more_full_cycle|Stage2 rearmament evidence preceded Green by one year and still had acceptable MAE.|
|R1L4_C02_HYUNDAI_ROTEM_POLAND_K2|064350|R1L4_C02_T2|R1L4_C02_T4|R1L4_C02_T2|2022-08-26|2022-07-22|30550|24400|7.5|34.6|-24.5|-5.9|23.7|34.6|-24.5|-5.9|27.1|18.6|large|Framework/order visibility plus RS was cleaner than formal contract Green.|
|R1L4_C03_DOOSAN_NUCLEAR_POLICY_ORDER|034020|R1L4_C03_T2_STAGE2_ACTIONABLE_CZECH|R1L4_C03_T1_STAGE2_CZECH_AWARENESS|R1L4_C03_T2_STAGE2_ACTIONABLE_CZECH|2024-07-17|2024-07-17|21250|21250|17.65|17.65|-28.71|-28.71|45.41|45.41|-28.71|-28.71|0|0|label_upgrade_not_price_change|Same entry is retained but re-labelled with high-volatility guardrail.|
|R1L4_C04_LS_ELECTRIC_GRID_DATACENTER|010120|R1L4_C04_T2_STAGE2_ACTIONABLE_GRID|R1L4_C04_T1_STAGE2_GRID_AWARENESS|R1L4_C04_T2_STAGE2_ACTIONABLE_GRID|2024-07-01|2024-07-01|204500|204500|34.23|34.23|-38.29|-38.29|48.41|48.41|-38.29|-38.29|0|0|label_upgrade_not_price_change|US grid/datacenter evidence was valid but MAE requires small-size guardrail.|
|R1L4_C05_SAMSUNG_EA_EPC_CONTRACT_FAIL|028050|R1L4_C05_T2_STAGE2_ACTIONABLE_FADHILI|R1L4_C05_T2_STAGE2_ACTIONABLE_FADHILI|watch_only_no_green|2024-04-03|not_applicable|25300|not_applicable|15.81|not_applicable|-14.62|not_applicable|15.81|not_applicable|-35.57|not_applicable|false_positive_removed|drawdown_avoided_in_score_simulation|not_applicable|Large EPC headline lacked margin/revision bridge; after-profile refuses Green.|

Natural-language interpretation: the selected shadow profile improves upside capture mainly by not waiting for formal Green in defense/order cases. The same profile does **not** blindly promote every Stage2. Doosan and LS stay under high-volatility guardrail; Samsung is refused as Green because the order did not close the margin/revision bridge.

## 19. Score-Return Alignment Matrix

|alignment_label|trigger_count|avg_weighted_score_before|avg_weighted_score_after|avg_MFE_90D_pct|avg_MAE_90D_pct|verdict|
|---|---|---|---|---|---|---|
|score_low_return_high_missed_structural|4|52.5|66.5|29.95|-20.82|promote early evidence, but keep volatility guardrail|
|score_mid_return_high_promote_candidate|3|62.0|73.0|30.61|-20.83|valid Stage2-Actionable tier, not clean Green|
|score_mid_return_low_watch_only|2|58.0|49.0|11.66|-19.56|watch-only; avoid over-confirmation|
|score_high_return_high|1|72.0|80.0|28.9|-4.2|safe but late Green|

## 20. Weight Sensitivity Table

row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_contract_backlog_relative_strength,0,2,+2,Hanwha and Rotem early order/backlog + RS triggers captured larger or cleaner MFE than later Green.,"Baseline avg MFE90 20.82/MAE90 -22.06 vs early-evidence profile avg MFE90 29.45/MAE90 -20.83 on selected cases; Samsung false-positive removed.",R1L4_C01_T1_STAGE2_WAR_REARMAMENT|R1L4_C02_T2|R1L4_C03_T2_STAGE2_ACTIONABLE_CZECH|R1L4_C04_T2_STAGE2_ACTIONABLE_GRID,4,"shadow-only; not production"
shadow_weight,volatility_guardrail_for_policy_or_grid_events,0,3,+3,"Doosan and LS produced strong MFE but MAE worse than -28%; promotion without sizing guardrail is misleading.","Keeps MFE capture but flags bad-entry-rate; avoids converting high-MAE Stage2 into clean Green.",R1L4_C03_T2_STAGE2_ACTIONABLE_CZECH|R1L4_C04_T2_STAGE2_ACTIONABLE_GRID,2,"shadow-only; high-volatility entry tier"
shadow_weight,epc_contract_without_margin_bridge_penalty,0,-2,-2,"Samsung E&A large EPC headline had only 15.81% MFE90 and -35.57% MAE180; contract headline alone should not force Green.",False-positive score reduced by treating EPC contract-only evidence as watch-only until margin/revision bridge appears.,R1L4_C05_T2_STAGE2_ACTIONABLE_FADHILI,1,"shadow-only; exploratory because single counterexample"
shadow_weight,non_price_4b_required_for_full_4b,0,2,+2,"Rotem formal contract day was a local high but full-window peak came later; price-only local 4B can cut off structural upside.","Rejects price-only local 4B as full exit; preserves Hanwha/Samsung non-price 4B overlays.",R1L4_C01_T5_STAGE4B_DEFENSE_OVERHEAT|R1L4_C02_T5|R1L4_C05_T5_STAGE4B_EPC_LOCAL_PEAK,3,"shadow-only; separates local from full-window proximity"
shadow_weight,hard_4c_delta,0,0,0,No hard 4C trigger was validated in this loop.,"No weight change; narrative-only thesis-break watches rejected for calibration.",,0,not validated

## 21. Optimization Decision Log

```jsonl
{"row_type":"optimization_decision","decision_id":"R1L4_D1","hypothesis":"Stage2-Actionable should promote when order/backlog visibility and relative strength arrive before full Green confirmation.","tested_cases":["R1L4_C01_HANWHA_AERO_DEFENSE_BACKLOG","R1L4_C02_HYUNDAI_ROTEM_POLAND_K2","R1L4_C03_DOOSAN_NUCLEAR_POLICY_ORDER","R1L4_C04_LS_ELECTRIC_GRID_DATACENTER"],"tested_trigger_ids":["R1L4_C01_T1_STAGE2_WAR_REARMAMENT","R1L4_C02_T2","R1L4_C03_T2_STAGE2_ACTIONABLE_CZECH","R1L4_C04_T2_STAGE2_ACTIONABLE_GRID"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus","backtest_result_summary":"Early evidence profile lifted selected-case avg MFE90 and removed Samsung EPC false positive, but MAE dispersion remains large.","accepted_or_rejected":"accepted_shadow_only","delta_magnitude":"+2","why_not_larger_delta":"usable cases are still concentrated in defense/nuclear/grid/EPC and two names have very deep MAE.","risks":"Over-promoting event premium without backlog/margin bridge or volatility sizing.","next_validation_needed":"Validate transformer pure-play cases and shipbuilding/order cases using stock-web rows."}
{"row_type":"optimization_decision","decision_id":"R1L4_D2","hypothesis":"High-MAE policy/grid Stage2 should be promoted only as small-size or watch-to-entry tier.","tested_cases":["R1L4_C03_DOOSAN_NUCLEAR_POLICY_ORDER","R1L4_C04_LS_ELECTRIC_GRID_DATACENTER"],"tested_trigger_ids":["R1L4_C03_T2_STAGE2_ACTIONABLE_CZECH","R1L4_C04_T2_STAGE2_ACTIONABLE_GRID"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus","backtest_result_summary":"Doosan/LS MFE90 was 17.65/34.23 but MAE90 was -28.71/-38.29; promotion without risk tag is rejected.","accepted_or_rejected":"accepted_shadow_only","delta_magnitude":"+3 volatility guardrail, not +3 pure score","why_not_larger_delta":"deep MAE implies path risk; full production score should wait for broader samples.","risks":"Can look correct by MFE while being hard to hold in real operation.","next_validation_needed":"Find lower-MAE grid/utility equipment examples and failed policy-event counterexamples."}
{"row_type":"optimization_decision","decision_id":"R1L4_D3","hypothesis":"Large EPC contract headline needs margin/revision bridge before Green.","tested_cases":["R1L4_C05_SAMSUNG_EA_EPC_CONTRACT_FAIL"],"tested_trigger_ids":["R1L4_C05_T2_STAGE2_ACTIONABLE_FADHILI","R1L4_C05_T5_STAGE4B_EPC_LOCAL_PEAK"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus","backtest_result_summary":"Samsung E&A produced only 15.81% MFE90 and -35.57% MAE180; 4B overlay at local peak worked as margin-bridge failure warning.","accepted_or_rejected":"accepted_shadow_only","delta_magnitude":"-2","why_not_larger_delta":"single counterexample; needs more EPC/plant cases.","risks":"Could under-score genuine EPC rerating if margin bridge later closes.","next_validation_needed":"Add EPC successes with revised OP/margin evidence."}
{"row_type":"optimization_decision","decision_id":"R1L4_D4","hypothesis":"4B should split local price-only watch from full-window non-price 4B.","tested_cases":["R1L4_C01_HANWHA_AERO_DEFENSE_BACKLOG","R1L4_C02_HYUNDAI_ROTEM_POLAND_K2","R1L4_C05_SAMSUNG_EA_EPC_CONTRACT_FAIL"],"tested_trigger_ids":["R1L4_C01_T5_STAGE4B_DEFENSE_OVERHEAT","R1L4_C02_T5","R1L4_C05_T5_STAGE4B_EPC_LOCAL_PEAK"],"baseline_profile":"baseline_current_proxy","selected_profile":"four_b_peak_timing_tuned","backtest_result_summary":"Hanwha/Samsung 4B overlays were near local/full peak with non-price risk; Rotem was local-only and too early for full exit.","accepted_or_rejected":"accepted_shadow_only","delta_magnitude":"+2","why_not_larger_delta":"4B evidence remains sparse; production exit logic unchanged.","risks":"Too much 4B strictness can miss fast blowoff reversals.","next_validation_needed":"Need more 4B overlays in transformer and shipbuilding cycles."}
{"row_type":"optimization_decision","decision_id":"R1L4_D5","hypothesis":"Hard 4C cannot be changed without validated thesis-break trigger.","tested_cases":["R1L4_C01_HANWHA_AERO_DEFENSE_BACKLOG","R1L4_C02_HYUNDAI_ROTEM_POLAND_K2","R1L4_C03_DOOSAN_NUCLEAR_POLICY_ORDER","R1L4_C04_LS_ELECTRIC_GRID_DATACENTER","R1L4_C05_SAMSUNG_EA_EPC_CONTRACT_FAIL"],"tested_trigger_ids":[],"baseline_profile":"baseline_current_proxy","selected_profile":"four_c_thesis_break_earlier","backtest_result_summary":"No hard 4C trigger with 180D OHLC validation; delta remains zero.","accepted_or_rejected":"rejected_for_this_round","delta_magnitude":"0","why_not_larger_delta":"this_round_does_not_validate hard 4C protection.","risks":"Premature 4C hard gate from narrative-only evidence.","next_validation_needed":"Find actual contract collapse / legal block / margin break before drawdown cases."}
```

## 22. Overfitting / Robustness Check

```text
usable_case_count = 5
usable_trigger_count = 17
representative_entry_trigger_count = 8
accepted_delta_max = +3 only for volatility guardrail, not pure score boost
production_scoring_changed = false
shadow_weight_only = true
```

The loop has enough evidence to accept moderate shadow deltas for early evidence and 4B decomposition, but not enough to change production scoring. The main robustness guardrail is the Samsung E&A counterexample: a real and large contract did not become durable rerating because the bridge from order to margin/revision was missing. Doosan and LS also prevent overfitting because they prove that high MFE can coexist with very deep MAE.

## 23. Cross-case Aggregate Metrics

### 23.1 Trigger-type aggregate

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,below_entry_90D_rate,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,5,1,33.3,33.3,-10.4,-10.4,73.7,-10.4,1.0,unavailable,unavailable,unavailable,"representative rows only; duplicate same-entry labels excluded"
aggregate_metric,Stage2-Actionable,5,5,25.06,23.0,-21.16,-18.3,44.53,-25.35,1.0,0.0,unavailable,unavailable,"representative rows only; duplicate same-entry labels excluded"
aggregate_metric,Stage3-Yellow,1,1,14.5,14.5,-21.7,-21.7,51.5,-21.7,1.0,unavailable,unavailable,unavailable,"representative rows only; duplicate same-entry labels excluded"
aggregate_metric,Stage3-Green,2,1,28.9,28.9,-4.2,-4.2,63.8,-4.2,1.0,0.37,unavailable,unavailable,"representative rows only; duplicate same-entry labels excluded"
aggregate_metric,Stage4B,4,0,14.47,6.75,-24.42,-22.74,18.76,-27.24,1.0,unavailable,0.66,0.57,"overlay-only aggregate; not mixed with entry aggregate"
```

### 23.2 Profile aggregate

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,5,5,4,20.82,17.65,-22.06,-24.5,39.43,-26.25,0.4,0.6,0.2,2,2,0.56,unavailable,unavailable,"reference; formal Green/confirmation often late or fragile"
profile_comparison,stage2_actionable_early_evidence_plus,5,4,4,29.95,33.96,-20.83,-19.55,50.53,-20.83,0.75,0.5,0.0,0,1,0.37,unavailable,unavailable,"better upside capture; requires volatility guardrail for nuclear/grid names"
profile_comparison,stage3_yellow_entry_relaxed,5,4,4,27.37,28.6,-22.8,-23.16,51.7,-22.8,0.75,0.75,0.0,0,1,0.45,unavailable,unavailable,valid only with MAE cap and position sizing
profile_comparison,green_confirmation_timing_relaxed,5,4,4,22.07,23.28,-23.92,-26.16,45.33,-23.92,0.5,0.75,0.0,1,2,0.56,unavailable,unavailable,relaxing Green alone does not solve high-MAE names
profile_comparison,four_b_peak_timing_tuned,5,4,0,14.47,6.75,-24.42,-22.74,18.76,-27.24,0.25,1.0,0.0,0,0,unavailable,0.66,0.57,"price-only local 4B rejected; non-price valuation/margin/legal evidence required"
profile_comparison,four_c_thesis_break_earlier,5,0,0,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,"not validated; no hard 4C trigger in this R1 loop"
```

## 24. Score-Price Alignment Verdict

```text
R1_loop_4_verdict = stage2_actionable_valid_but_must_be_bridge_sensitive
```

The score-price alignment is strongest when Stage2 evidence is not a naked headline. The good early triggers had a second gear: order/backlog visibility, customer quality, policy urgency, or relative strength. The bad or dangerous early triggers lacked margin bridge or carried extreme volatility. In practical terms, Stage2 is not “early because it is vague”; it is early only when the evidence has already started to become inventory, backlog, delivery, margin, or revision.

## 25. Validation Scope / Non-Validation Scope

### this_round_validates

```text
- Stage2-Actionable early evidence when contract/backlog visibility and relative strength coexist.
- Stage3-Green lateness in defense/order export cycles.
- High-volatility guardrail for nuclear/grid policy-demand cases.
- EPC contract-only penalty when margin/revision bridge is absent.
- 4B local vs full-window proximity split.
- Price-only local 4B rejection unless non-price 4B evidence exists.
- Aggregate de-duplication by same_entry_group_id and representative rows.
```

### this_round_does_not_validate

```text
- Broad Stage3-Green relaxation across all industrial names.
- Hard 4C thesis-break protection.
- Full transformer pure-play 4B exit timing.
- Shipbuilding order-cycle calibration.
- Adjusted-price revalidation for corporate action contaminated names.
```

No shadow delta is proposed for items in `this_round_does_not_validate`.

## 26. Shadow Weight Calibration

Accepted shadow-only changes:

```text
+2 stage2_actionable_contract_backlog_relative_strength
+3 volatility_guardrail_for_policy_or_grid_events, but this is a risk tag / sizing gate rather than pure score boost
-2 epc_contract_without_margin_bridge_penalty
+2 non_price_4b_required_for_full_4b
0 hard_4c_delta
```

These are not production changes. They are calibration hypotheses for the later coding agent to ingest only if rows remain internally consistent.

## 27. Machine-Readable Rows

### 27.1 Price source validation row JSONL

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 27.2 Case rows JSONL

```jsonl
{"row_type":"case","case_id":"R1L4_C01_HANWHA_AERO_DEFENSE_BACKLOG","symbol":"012450","company_name":"한화에어로스페이스","case_type":"structural_success","primary_archetype":"DEFENSE_GOVERNMENT_BACKLOG_EXPORT_REARMAMENT","best_trigger":"R1L4_C01_T1_STAGE2_WAR_REARMAMENT","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"score_low_return_high_missed_structural","price_source":"Songdaiki/stock-web","notes":"Russia-Ukraine rearmament + Poland/Romania defense-order route. Earliest public rearmament trigger captured more upside than later Green.","round":"R1","loop":"4","sector":"산업재·수주·인프라"}
{"row_type":"case","case_id":"R1L4_C02_HYUNDAI_ROTEM_POLAND_K2","symbol":"064350","company_name":"현대로템","round":"R1","loop":"4","sector":"산업재·수주·인프라","case_type":"structural_success_with_late_green","primary_archetype":"DEFENSE_EXPORT_BACKLOG_POLAND_ARMOR","best_trigger":"R1L4_C02_T2","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"score_low_return_high_missed_structural","price_source":"Songdaiki/stock-web","notes":"Poland K2 framework / executive contract route shows Stage2-Actionable outperformed formal Green and had much shallower MAE."}
{"row_type":"case","case_id":"R1L4_C03_DOOSAN_NUCLEAR_POLICY_ORDER","symbol":"034020","company_name":"두산에너빌리티","case_type":"missed_structural_with_policy_event_volatility","primary_archetype":"NUCLEAR_INFRA_PREFERRED_BIDDER_TO_BACKLOG","best_trigger":"R1L4_C03_T2_STAGE2_ACTIONABLE_CZECH","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"score_mid_return_high_but_high_mae","price_source":"Songdaiki/stock-web","notes":"Czech nuclear preferred-bidder evidence created large 180D/1Y MFE but MAE was deep; promote only with volatility sizing guardrail.","round":"R1","loop":"4","sector":"산업재·수주·인프라"}
{"row_type":"case","case_id":"R1L4_C04_LS_ELECTRIC_GRID_DATACENTER","symbol":"010120","company_name":"LS ELECTRIC","case_type":"stage2_promote_candidate_high_volatility","primary_archetype":"GRID_EQUIPMENT_US_DATACENTER_CAPEX","best_trigger":"R1L4_C04_T2_STAGE2_ACTIONABLE_GRID","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"score_mid_return_high_promote_candidate","price_source":"Songdaiki/stock-web","notes":"US grid/data-center demand evidence was right directionally, but MAE was too deep for clean Green without volatility guardrail.","round":"R1","loop":"4","sector":"산업재·수주·인프라"}
{"row_type":"case","case_id":"R1L4_C05_SAMSUNG_EA_EPC_CONTRACT_FAIL","symbol":"028050","company_name":"삼성E&A","case_type":"evidence_good_but_price_failed","primary_archetype":"OVERSEAS_EPC_MEGA_CONTRACT_WITH_MARGIN_BRIDGE_GAP","best_trigger":"R1L4_C05_T2_STAGE2_ACTIONABLE_FADHILI","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"score_mid_return_low_watch_only","price_source":"Songdaiki/stock-web","notes":"Large EPC order was real but did not close the backlog-to-margin rerating bridge; it should not force Green.","round":"R1","loop":"4","sector":"산업재·수주·인프라"}
```

### 27.3 Trigger rows JSONL

```jsonl
{"row_type":"trigger","trigger_id":"R1L4_C01_T1_STAGE2_WAR_REARMAMENT","case_id":"R1L4_C01_HANWHA_AERO_DEFENSE_BACKLOG","symbol":"012450","company_name":"한화에어로스페이스","trigger_type":"Stage2","trigger_date":"2022-02-24","entry_date":"2022-02-24","entry_price":45600,"MFE_30D_pct":24.6,"MFE_90D_pct":33.3,"MFE_180D_pct":73.7,"MFE_1Y_pct":153.3,"MFE_2Y_pct":"unavailable_not_needed_for_delta","MAE_30D_pct":-0.7,"MAE_90D_pct":-10.4,"MAE_180D_pct":-10.4,"MAE_1Y_pct":-10.4,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-10","peak_price":118800,"drawdown_after_peak_pct":-14.0,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":252,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L4_C01_20220224_45600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_available_at_that_date":"Russia-Ukraine war/rearmament shock became public; defense export backlog route entered market attention.","evidence_source":"public geopolitical news + defense rearmament news; price rows checked in stock-web 012450 2022/2023 shards","round":"R1","loop":"4","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012450/2022.csv","profile_path":"atlas/symbol_profiles/012/012450.json","primary_archetype":"DEFENSE_GOVERNMENT_BACKLOG_EXPORT_REARMAMENT"}
{"row_type":"trigger","trigger_id":"R1L4_C01_T2_STAGE2_ACTIONABLE_POLAND_ORDER_ROUTE","case_id":"R1L4_C01_HANWHA_AERO_DEFENSE_BACKLOG","symbol":"012450","company_name":"한화에어로스페이스","trigger_type":"Stage2-Actionable","trigger_date":"2022-07-29","entry_date":"2022-07-29","entry_price":64400,"MFE_30D_pct":6.5,"MFE_90D_pct":23.0,"MFE_180D_pct":78.4,"MFE_1Y_pct":134.5,"MFE_2Y_pct":"unavailable_not_needed_for_delta","MAE_30D_pct":-3.7,"MAE_90D_pct":-18.3,"MAE_180D_pct":-18.3,"MAE_1Y_pct":-18.3,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-27","peak_price":151000,"drawdown_after_peak_pct":-23.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":252,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L4_C01_20220729_64400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_available_at_that_date":"Defense export/order route became visible; volume and relative strength confirmed that this was more than a headline.","evidence_source":"defense export/order news; price rows checked in stock-web 012450 2022/2023 shards","round":"R1","loop":"4","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012450/2022.csv","profile_path":"atlas/symbol_profiles/012/012450.json","primary_archetype":"DEFENSE_GOVERNMENT_BACKLOG_EXPORT_REARMAMENT"}
{"row_type":"trigger","trigger_id":"R1L4_C01_T3_STAGE3_YELLOW_DELIVERY_SCALE","case_id":"R1L4_C01_HANWHA_AERO_DEFENSE_BACKLOG","symbol":"012450","company_name":"한화에어로스페이스","trigger_type":"Stage3-Yellow","trigger_date":"2022-08-26","entry_date":"2022-08-26","entry_price":78400,"MFE_30D_pct":10.2,"MFE_90D_pct":14.5,"MFE_180D_pct":51.5,"MFE_1Y_pct":92.6,"MFE_2Y_pct":"unavailable_not_needed_for_delta","MAE_30D_pct":-5.2,"MAE_90D_pct":-21.7,"MAE_180D_pct":-21.7,"MAE_1Y_pct":-21.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-27","peak_price":151000,"drawdown_after_peak_pct":-23.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"good_entry","calibration_usable":true,"forward_window_trading_days":252,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L4_C01_20220826_78400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_available_at_that_date":"Order route and relative strength were stronger; still one gate short of clean Green because delivery/margin conversion was not fully proven.","evidence_source":"defense order/backlog news + stock-web OHLC","round":"R1","loop":"4","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012450/2022.csv","profile_path":"atlas/symbol_profiles/012/012450.json","primary_archetype":"DEFENSE_GOVERNMENT_BACKLOG_EXPORT_REARMAMENT"}
{"row_type":"trigger","trigger_id":"R1L4_C01_T4_STAGE3_GREEN_EXPORT_MARGIN","case_id":"R1L4_C01_HANWHA_AERO_DEFENSE_BACKLOG","symbol":"012450","company_name":"한화에어로스페이스","trigger_type":"Stage3-Green","trigger_date":"2023-02-24","entry_date":"2023-02-24","entry_price":92200,"MFE_30D_pct":8.5,"MFE_90D_pct":28.9,"MFE_180D_pct":63.8,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"unavailable_not_needed_for_delta","MAE_30D_pct":-4.2,"MAE_90D_pct":-4.2,"MAE_180D_pct":-4.2,"MAE_1Y_pct":"unavailable","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-27","peak_price":151000,"drawdown_after_peak_pct":-23.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.37,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"good_but_later_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L4_C01_20230224_92200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_available_at_that_date":"Order/backlog/revision evidence had become clearer; Green was safer but materially later than Stage2.","evidence_source":"defense order/revision public evidence + stock-web OHLC","round":"R1","loop":"4","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012450/2023.csv","profile_path":"atlas/symbol_profiles/012/012450.json","primary_archetype":"DEFENSE_GOVERNMENT_BACKLOG_EXPORT_REARMAMENT"}
{"row_type":"trigger","trigger_id":"R1L4_C01_T5_STAGE4B_DEFENSE_OVERHEAT","case_id":"R1L4_C01_HANWHA_AERO_DEFENSE_BACKLOG","symbol":"012450","company_name":"한화에어로스페이스","trigger_type":"Stage4B","trigger_date":"2023-06-20","entry_date":"2023-06-20","entry_price":142500,"MFE_30D_pct":6.0,"MFE_90D_pct":6.0,"MFE_180D_pct":6.0,"MFE_1Y_pct":"unavailable","MFE_2Y_pct":"unavailable","MAE_30D_pct":-19.1,"MAE_90D_pct":-19.1,"MAE_180D_pct":-19.1,"MAE_1Y_pct":"unavailable","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-27","peak_price":151000,"drawdown_after_peak_pct":-23.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":0.9,"four_b_timing_verdict":"good_full_window_4B_timing_as_overlay_not_thesis_break","four_b_evidence_type":"valuation_blowoff|positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_watch_success","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L4_C01_20230620_142500","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","evidence_available_at_that_date":"Rapid rerating and crowded valuation; not a 4C because order/backlog thesis remained alive.","evidence_source":"valuation/positioning overlay + stock-web OHLC","round":"R1","loop":"4","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012450/2023.csv","profile_path":"atlas/symbol_profiles/012/012450.json","primary_archetype":"DEFENSE_GOVERNMENT_BACKLOG_EXPORT_REARMAMENT"}
{"row_type":"trigger","trigger_id":"R1L4_C02_T1","case_id":"R1L4_C02_HYUNDAI_ROTEM_POLAND_K2","symbol":"064350","company_name":"현대로템","round":"R1","loop":"4","sector":"산업재·수주·인프라","primary_archetype":"DEFENSE_EXPORT_BACKLOG_POLAND_ARMOR","trigger_type":"Stage2","trigger_date":"2022-06-08","evidence_available_at_that_date":"Poland/Korea defense-export negotiations became visible; Russia-Ukraine security shock strengthened demand path.","evidence_source":"defense news / public MoU reporting; stock-web 2022-06-08 row","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv","profile_path":"atlas/symbol_profiles/064/064350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-06-08","entry_price":21050,"MFE_30D_pct":16.6,"MFE_90D_pct":56.1,"MFE_180D_pct":56.1,"MFE_1Y_pct":91.2,"MFE_2Y_pct":"unavailable_in_this_md","MAE_30D_pct":-15.9,"MAE_90D_pct":-15.9,"MAE_180D_pct":-15.9,"MAE_1Y_pct":-15.9,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-21","peak_price":40250,"drawdown_after_peak_pct":"unavailable_in_this_md","market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"good_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R1L4_C02_G1","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only"}
{"row_type":"trigger","trigger_id":"R1L4_C02_T2","case_id":"R1L4_C02_HYUNDAI_ROTEM_POLAND_K2","symbol":"064350","company_name":"현대로템","round":"R1","loop":"4","sector":"산업재·수주·인프라","primary_archetype":"DEFENSE_EXPORT_BACKLOG_POLAND_ARMOR","trigger_type":"Stage2-Actionable","trigger_date":"2022-07-22","evidence_available_at_that_date":"K2/Poland framework order visibility plus high-volume relative-strength breakout; backlog visibility not yet fully closed.","evidence_source":"Poland/K2 framework reporting; stock-web 2022-07-22 row","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv","profile_path":"atlas/symbol_profiles/064/064350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-07-22","entry_price":24400,"MFE_30D_pct":34.6,"MFE_90D_pct":34.6,"MFE_180D_pct":34.6,"MFE_1Y_pct":65.0,"MFE_2Y_pct":"unavailable_in_this_md","MAE_30D_pct":-1.8,"MAE_90D_pct":-5.9,"MAE_180D_pct":-5.9,"MAE_1Y_pct":-5.9,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-21","peak_price":40250,"drawdown_after_peak_pct":"unavailable_in_this_md","market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.0,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R1L4_C02_G2","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R1L4_C02_T4","case_id":"R1L4_C02_HYUNDAI_ROTEM_POLAND_K2","symbol":"064350","company_name":"현대로템","round":"R1","loop":"4","sector":"산업재·수주·인프라","primary_archetype":"DEFENSE_EXPORT_BACKLOG_POLAND_ARMOR","trigger_type":"Stage3-Green","trigger_date":"2022-08-26","evidence_available_at_that_date":"Executive agreement / formal contract evidence closed, but price was already near local peak.","evidence_source":"Poland K2 executive contract reporting; stock-web 2022-08-26 row","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv","profile_path":"atlas/symbol_profiles/064/064350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-08-26","entry_price":30550,"MFE_30D_pct":7.5,"MFE_90D_pct":7.5,"MFE_180D_pct":23.7,"MFE_1Y_pct":31.8,"MFE_2Y_pct":"unavailable_in_this_md","MAE_30D_pct":-17.9,"MAE_90D_pct":-24.5,"MAE_180D_pct":-24.5,"MAE_1Y_pct":-24.5,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-21","peak_price":40250,"drawdown_after_peak_pct":"unavailable_in_this_md","market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.73,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"late_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R1L4_C02_G3","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only"}
{"row_type":"trigger","trigger_id":"R1L4_C02_T5","case_id":"R1L4_C02_HYUNDAI_ROTEM_POLAND_K2","symbol":"064350","company_name":"현대로템","round":"R1","loop":"4","sector":"산업재·수주·인프라","primary_archetype":"DEFENSE_EXPORT_BACKLOG_POLAND_ARMOR","trigger_type":"Stage4B","trigger_date":"2022-08-26","evidence_available_at_that_date":"Formal contract day coincided with local blowoff; later full-cycle peak required additional 2023 defense-order evidence.","evidence_source":"stock-web 2022-08-26 local high and 2023-06 high","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv","profile_path":"atlas/symbol_profiles/064/064350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-08-26","entry_price":30550,"MFE_30D_pct":7.5,"MFE_90D_pct":7.5,"MFE_180D_pct":23.7,"MFE_1Y_pct":31.8,"MFE_2Y_pct":"unavailable_in_this_md","MAE_30D_pct":-17.9,"MAE_90D_pct":-24.5,"MAE_180D_pct":-24.5,"MAE_1Y_pct":-24.5,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-21","peak_price":40250,"drawdown_after_peak_pct":"unavailable_in_this_md","market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.73,"four_b_full_window_peak_proximity":0.39,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":"price_only|local_positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"local_4B_watch_not_full_exit","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R1L4_C02_G3","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R1L4_C03_T1_STAGE2_CZECH_AWARENESS","case_id":"R1L4_C03_DOOSAN_NUCLEAR_POLICY_ORDER","symbol":"034020","company_name":"두산에너빌리티","trigger_type":"Stage2","trigger_date":"2024-07-17","entry_date":"2024-07-17","entry_price":21250,"MFE_30D_pct":17.65,"MFE_90D_pct":17.65,"MFE_180D_pct":45.41,"MFE_1Y_pct":239.76,"MFE_2Y_pct":"unavailable_insufficient_forward_window","MAE_30D_pct":-28.71,"MAE_90D_pct":-28.71,"MAE_180D_pct":-28.71,"MAE_1Y_pct":-28.71,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-30","peak_price":72200,"drawdown_after_peak_pct":-39.4,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"volatile_good_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L4_C03_20240717_21250","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","evidence_available_at_that_date":"Czech nuclear preferred-bidder/project evidence was public, but final contract/legal risk remained.","evidence_source":"nuclear project news + stock-web OHLC","round":"R1","loop":"4","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv","profile_path":"atlas/symbol_profiles/034/034020.json","primary_archetype":"NUCLEAR_INFRA_PREFERRED_BIDDER_TO_BACKLOG"}
{"row_type":"trigger","trigger_id":"R1L4_C03_T2_STAGE2_ACTIONABLE_CZECH","case_id":"R1L4_C03_DOOSAN_NUCLEAR_POLICY_ORDER","symbol":"034020","company_name":"두산에너빌리티","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-17","entry_date":"2024-07-17","entry_price":21250,"MFE_30D_pct":17.65,"MFE_90D_pct":17.65,"MFE_180D_pct":45.41,"MFE_1Y_pct":239.76,"MFE_2Y_pct":"unavailable_insufficient_forward_window","MAE_30D_pct":-28.71,"MAE_90D_pct":-28.71,"MAE_180D_pct":-28.71,"MAE_1Y_pct":-28.71,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-30","peak_price":72200,"drawdown_after_peak_pct":-39.4,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"stage2_promote_candidate_with_deep_mae","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L4_C03_20240717_21250","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_available_at_that_date":"Same entry as Stage2; elevated to Actionable only with small sizing because MFE180/1Y was large but MAE was deep.","evidence_source":"nuclear project news + stock-web OHLC","round":"R1","loop":"4","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv","profile_path":"atlas/symbol_profiles/034/034020.json","primary_archetype":"NUCLEAR_INFRA_PREFERRED_BIDDER_TO_BACKLOG"}
{"row_type":"trigger","trigger_id":"R1L4_C03_T5_STAGE4B_LEGAL_EARLY","case_id":"R1L4_C03_DOOSAN_NUCLEAR_POLICY_ORDER","symbol":"034020","company_name":"두산에너빌리티","trigger_type":"Stage4B","trigger_date":"2024-10-30","entry_date":"2024-10-30","entry_price":21400,"MFE_30D_pct":6.54,"MFE_90D_pct":44.39,"MFE_180D_pct":45.33,"MFE_1Y_pct":"unavailable","MFE_2Y_pct":"unavailable","MAE_30D_pct":-20.98,"MAE_90D_pct":-20.98,"MAE_180D_pct":-20.98,"MAE_1Y_pct":"unavailable","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-19","peak_price":30900,"drawdown_after_peak_pct":-35.4,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.02,"four_b_full_window_peak_proximity":0.003,"four_b_timing_verdict":"price_only_or_legal_watch_too_early_for_full_cycle_4B","four_b_evidence_type":"legal_or_regulatory_block|price_only","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_too_early_or_noise","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L4_C03_20241030_21400","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","evidence_available_at_that_date":"Legal/regulatory watch existed but price path later produced much larger MFE, so full 4B would have been too early.","evidence_source":"legal/regulatory project news + stock-web OHLC","round":"R1","loop":"4","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv","profile_path":"atlas/symbol_profiles/034/034020.json","primary_archetype":"NUCLEAR_INFRA_PREFERRED_BIDDER_TO_BACKLOG"}
{"row_type":"trigger","trigger_id":"R1L4_C04_T1_STAGE2_GRID_AWARENESS","case_id":"R1L4_C04_LS_ELECTRIC_GRID_DATACENTER","symbol":"010120","company_name":"LS ELECTRIC","trigger_type":"Stage2","trigger_date":"2024-07-01","entry_date":"2024-07-01","entry_price":204500,"MFE_30D_pct":34.23,"MFE_90D_pct":34.23,"MFE_180D_pct":48.41,"MFE_1Y_pct":58.68,"MFE_2Y_pct":"unavailable_insufficient_forward_window","MAE_30D_pct":-29.1,"MAE_90D_pct":-38.29,"MAE_180D_pct":-38.29,"MAE_1Y_pct":-38.29,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-24","peak_price":324500,"drawdown_after_peak_pct":-54.03,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"volatile_promote_candidate","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L4_C04_20240701_204500","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","evidence_available_at_that_date":"US grid/data-center demand and price relative strength were visible but drawdown risk was not yet resolved.","evidence_source":"grid/data-center demand report + stock-web OHLC","round":"R1","loop":"4","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv","profile_path":"atlas/symbol_profiles/010/010120.json","primary_archetype":"GRID_EQUIPMENT_US_DATACENTER_CAPEX"}
{"row_type":"trigger","trigger_id":"R1L4_C04_T2_STAGE2_ACTIONABLE_GRID","case_id":"R1L4_C04_LS_ELECTRIC_GRID_DATACENTER","symbol":"010120","company_name":"LS ELECTRIC","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-01","entry_date":"2024-07-01","entry_price":204500,"MFE_30D_pct":34.23,"MFE_90D_pct":34.23,"MFE_180D_pct":48.41,"MFE_1Y_pct":58.68,"MFE_2Y_pct":"unavailable_insufficient_forward_window","MAE_30D_pct":-29.1,"MAE_90D_pct":-38.29,"MAE_180D_pct":-38.29,"MAE_1Y_pct":-38.29,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-24","peak_price":324500,"drawdown_after_peak_pct":-54.03,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"stage2_promote_candidate_with_extreme_mae","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L4_C04_20240701_204500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_available_at_that_date":"Same entry promoted only if volatility/position sizing guardrail is present.","evidence_source":"grid/data-center demand report + stock-web OHLC","round":"R1","loop":"4","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv","profile_path":"atlas/symbol_profiles/010/010120.json","primary_archetype":"GRID_EQUIPMENT_US_DATACENTER_CAPEX"}
{"row_type":"trigger","trigger_id":"R1L4_C05_T1_STAGE2_FADHILI_ORDER","case_id":"R1L4_C05_SAMSUNG_EA_EPC_CONTRACT_FAIL","symbol":"028050","company_name":"삼성E&A","trigger_type":"Stage2","trigger_date":"2024-04-03","entry_date":"2024-04-03","entry_price":25300,"MFE_30D_pct":6.72,"MFE_90D_pct":15.81,"MFE_180D_pct":15.81,"MFE_1Y_pct":15.81,"MFE_2Y_pct":"unavailable_insufficient_forward_window","MAE_30D_pct":-3.75,"MAE_90D_pct":-14.62,"MAE_180D_pct":-35.57,"MAE_1Y_pct":-35.57,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-01","peak_price":29300,"drawdown_after_peak_pct":-44.37,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"evidence_good_but_price_failed","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L4_C05_20240403_25300","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","evidence_available_at_that_date":"Large Fadhili EPC order; margin bridge and durable revision evidence were not closed.","evidence_source":"EPC contract disclosure/news + stock-web OHLC","round":"R1","loop":"4","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv","profile_path":"atlas/symbol_profiles/028/028050.json","primary_archetype":"OVERSEAS_EPC_MEGA_CONTRACT_WITH_MARGIN_BRIDGE_GAP"}
{"row_type":"trigger","trigger_id":"R1L4_C05_T2_STAGE2_ACTIONABLE_FADHILI","case_id":"R1L4_C05_SAMSUNG_EA_EPC_CONTRACT_FAIL","symbol":"028050","company_name":"삼성E&A","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-03","entry_date":"2024-04-03","entry_price":25300,"MFE_30D_pct":6.72,"MFE_90D_pct":15.81,"MFE_180D_pct":15.81,"MFE_1Y_pct":15.81,"MFE_2Y_pct":"unavailable_insufficient_forward_window","MAE_30D_pct":-3.75,"MAE_90D_pct":-14.62,"MAE_180D_pct":-35.57,"MAE_1Y_pct":-35.57,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-01","peak_price":29300,"drawdown_after_peak_pct":-44.37,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"evidence_good_but_price_failed","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L4_C05_20240403_25300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_available_at_that_date":"Same entry remains Actionable-watch, not Green, because contract quality did not convert to durable margin bridge.","evidence_source":"EPC contract disclosure/news + stock-web OHLC","round":"R1","loop":"4","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv","profile_path":"atlas/symbol_profiles/028/028050.json","primary_archetype":"OVERSEAS_EPC_MEGA_CONTRACT_WITH_MARGIN_BRIDGE_GAP"}
{"row_type":"trigger","trigger_id":"R1L4_C05_T5_STAGE4B_EPC_LOCAL_PEAK","case_id":"R1L4_C05_SAMSUNG_EA_EPC_CONTRACT_FAIL","symbol":"028050","company_name":"삼성E&A","trigger_type":"Stage4B","trigger_date":"2024-08-01","entry_date":"2024-08-01","entry_price":29300,"MFE_30D_pct":0.0,"MFE_90D_pct":0.0,"MFE_180D_pct":0.0,"MFE_1Y_pct":"unavailable","MFE_2Y_pct":"unavailable","MAE_30D_pct":-21.5,"MAE_90D_pct":-33.1,"MAE_180D_pct":-44.37,"MAE_1Y_pct":"unavailable","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-01","peak_price":29300,"drawdown_after_peak_pct":-44.37,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_local_and_full_4B_timing_with_margin_bridge_failure","four_b_evidence_type":"margin_or_backlog_slowdown|valuation_blowoff","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_watch_success","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L4_C05_20240801_29300","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","evidence_available_at_that_date":"Peak zone after contract headline failed to prove durable margin/revision bridge.","evidence_source":"price path + margin/revision absence; stock-web OHLC","round":"R1","loop":"4","sector":"산업재·수주·인프라","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv","profile_path":"atlas/symbol_profiles/028/028050.json","primary_archetype":"OVERSEAS_EPC_MEGA_CONTRACT_WITH_MARGIN_BRIDGE_GAP"}
```

### 27.4 Score simulation rows JSONL

```jsonl
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L4_C01_HANWHA_AERO_DEFENSE_BACKLOG","trigger_id":"R1L4_C01_T1_STAGE2_WAR_REARMAMENT","symbol":"012450","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":8,"customer_quality_score":9,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":8,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":0,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":72.8,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":11,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":10,"customer_quality_score":9,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":10,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":0,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":81.8,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","backlog_visibility_score","relative_strength_score","order_intake_quality_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":33.3,"MAE_90D_pct":-10.4,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration","round":"R1","loop":"4","sector":"산업재·수주·인프라"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L4_C01_HANWHA_AERO_DEFENSE_BACKLOG","trigger_id":"R1L4_C01_T2_STAGE2_ACTIONABLE_POLAND_ORDER_ROUTE","symbol":"012450","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":8,"customer_quality_score":9,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":8,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":0,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":72.8,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":11,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":10,"customer_quality_score":9,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":10,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":0,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":81.8,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","backlog_visibility_score","relative_strength_score","order_intake_quality_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":23.0,"MAE_90D_pct":-18.3,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration","round":"R1","loop":"4","sector":"산업재·수주·인프라"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L4_C01_HANWHA_AERO_DEFENSE_BACKLOG","trigger_id":"R1L4_C01_T3_STAGE3_YELLOW_DELIVERY_SCALE","symbol":"012450","trigger_type":"Stage3-Yellow","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":8,"customer_quality_score":9,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":8,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":0,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":72.8,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":11,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":10,"customer_quality_score":9,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":10,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":0,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":81.8,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","backlog_visibility_score","relative_strength_score","order_intake_quality_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":14.5,"MAE_90D_pct":-21.7,"score_return_alignment_label":"score_mid_return_low_watch_only","row_validation_status":"valid_for_shadow_calibration","round":"R1","loop":"4","sector":"산업재·수주·인프라"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L4_C01_HANWHA_AERO_DEFENSE_BACKLOG","trigger_id":"R1L4_C01_T4_STAGE3_GREEN_EXPORT_MARGIN","symbol":"012450","trigger_type":"Stage3-Green","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":8,"customer_quality_score":9,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":8,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":0,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":72.8,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":11,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":10,"customer_quality_score":9,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":10,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":0,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":81.8,"stage_label_after":"Stage3-Green","changed_components":["contract_score","backlog_visibility_score","relative_strength_score","order_intake_quality_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":28.9,"MAE_90D_pct":-4.2,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration","round":"R1","loop":"4","sector":"산업재·수주·인프라"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L4_C01_HANWHA_AERO_DEFENSE_BACKLOG","trigger_id":"R1L4_C01_T5_STAGE4B_DEFENSE_OVERHEAT","symbol":"012450","trigger_type":"Stage4B","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":8,"customer_quality_score":9,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":8,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":2,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":73.8,"stage_label_before":"Stage4B-watch","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":11,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":10,"customer_quality_score":9,"policy_or_regulatory_score":8,"valuation_repricing_score":10,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":10,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":8,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":91.2,"stage_label_after":"Stage4B-watch","changed_components":["contract_score","backlog_visibility_score","relative_strength_score","valuation_repricing_score","order_intake_quality_score","positioning_overheat_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":6.0,"MAE_90D_pct":-19.1,"score_return_alignment_label":"score_mid_return_low_watch_only","row_validation_status":"valid_for_shadow_calibration","round":"R1","loop":"4","sector":"산업재·수주·인프라"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_to_stage2_actionable_early_evidence_plus","case_id":"R1L4_C02_HYUNDAI_ROTEM_POLAND_K2","trigger_id":"R1L4_C02_T1","symbol":"064350","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":4,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":34,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":2,"revision_score":0,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":4,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":46,"stage_label_after":"Stage2","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","customer_quality_score"],"component_delta_explanation":"Shadow-only proxy: promote only when policy/regulatory event is paired with contract/backlog/revision/RS; raise legal/accounting trust risk for digital-asset regulatory events.","selected_by_profile":false,"MFE_90D_pct":56.1,"MAE_90D_pct":-15.9,"score_return_alignment_label":"score_low_return_high_missed_structural","round":"R1","loop":"4","sector":"산업재·수주·인프라","primary_archetype":"DEFENSE_EXPORT_BACKLOG_POLAND_ARMOR"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_to_stage2_actionable_early_evidence_plus","case_id":"R1L4_C02_HYUNDAI_ROTEM_POLAND_K2","trigger_id":"R1L4_C02_T2","symbol":"064350","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":4,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":34,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":2,"revision_score":0,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":4,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":46,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","customer_quality_score"],"component_delta_explanation":"Shadow-only proxy: promote only when policy/regulatory event is paired with contract/backlog/revision/RS; raise legal/accounting trust risk for digital-asset regulatory events.","selected_by_profile":true,"MFE_90D_pct":34.6,"MAE_90D_pct":-5.9,"score_return_alignment_label":"score_low_return_high_missed_structural","round":"R1","loop":"4","sector":"산업재·수주·인프라","primary_archetype":"DEFENSE_EXPORT_BACKLOG_POLAND_ARMOR"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_to_stage2_actionable_early_evidence_plus","case_id":"R1L4_C02_HYUNDAI_ROTEM_POLAND_K2","trigger_id":"R1L4_C02_T4","symbol":"064350","trigger_type":"Stage3-Green","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":4,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":34,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":2,"revision_score":0,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":4,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":46,"stage_label_after":"Stage3-Yellow_or_late_green_watch","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","customer_quality_score"],"component_delta_explanation":"Shadow-only proxy: promote only when policy/regulatory event is paired with contract/backlog/revision/RS; raise legal/accounting trust risk for digital-asset regulatory events.","selected_by_profile":false,"MFE_90D_pct":7.5,"MAE_90D_pct":-24.5,"score_return_alignment_label":"score_mid_return_low_watch_only","round":"R1","loop":"4","sector":"산업재·수주·인프라","primary_archetype":"DEFENSE_EXPORT_BACKLOG_POLAND_ARMOR"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_to_stage2_actionable_early_evidence_plus","case_id":"R1L4_C02_HYUNDAI_ROTEM_POLAND_K2","trigger_id":"R1L4_C02_T5","symbol":"064350","trigger_type":"Stage4B","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":4,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":34,"stage_label_before":"Stage4B-watch","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":2,"revision_score":0,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":4,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":46,"stage_label_after":"Stage4B-watch","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","customer_quality_score"],"component_delta_explanation":"Shadow-only proxy: promote only when policy/regulatory event is paired with contract/backlog/revision/RS; raise legal/accounting trust risk for digital-asset regulatory events.","selected_by_profile":false,"MFE_90D_pct":7.5,"MAE_90D_pct":-24.5,"score_return_alignment_label":"score_mid_return_low_watch_only","round":"R1","loop":"4","sector":"산업재·수주·인프라","primary_archetype":"DEFENSE_EXPORT_BACKLOG_POLAND_ARMOR"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L4_C03_DOOSAN_NUCLEAR_POLICY_ORDER","trigger_id":"R1L4_C03_T1_STAGE2_CZECH_AWARENESS","symbol":"034020","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":9,"valuation_repricing_score":6,"execution_risk_score":9,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":"unknown_or_not_supported","fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":3,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":63.5,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":9,"customer_quality_score":7,"policy_or_regulatory_score":10,"valuation_repricing_score":6,"execution_risk_score":12,"legal_or_contract_risk_score":11,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":"unknown_or_not_supported","fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":3,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":70.8,"stage_label_after":"Stage2-Actionable high_MAE_guardrail","changed_components":["contract_score","relative_strength_score","policy_or_regulatory_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":17.65,"MAE_90D_pct":-28.71,"score_return_alignment_label":"score_mid_return_low_watch_only","row_validation_status":"valid_for_shadow_calibration","round":"R1","loop":"4","sector":"산업재·수주·인프라"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L4_C03_DOOSAN_NUCLEAR_POLICY_ORDER","trigger_id":"R1L4_C03_T2_STAGE2_ACTIONABLE_CZECH","symbol":"034020","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":9,"valuation_repricing_score":6,"execution_risk_score":9,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":"unknown_or_not_supported","fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":3,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":63.5,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":9,"customer_quality_score":7,"policy_or_regulatory_score":10,"valuation_repricing_score":6,"execution_risk_score":12,"legal_or_contract_risk_score":11,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":"unknown_or_not_supported","fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":3,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":70.8,"stage_label_after":"Stage2-Actionable high_MAE_guardrail","changed_components":["contract_score","relative_strength_score","policy_or_regulatory_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":17.65,"MAE_90D_pct":-28.71,"score_return_alignment_label":"score_mid_return_low_watch_only","row_validation_status":"valid_for_shadow_calibration","round":"R1","loop":"4","sector":"산업재·수주·인프라"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L4_C03_DOOSAN_NUCLEAR_POLICY_ORDER","trigger_id":"R1L4_C03_T5_STAGE4B_LEGAL_EARLY","symbol":"034020","trigger_type":"Stage4B","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":9,"valuation_repricing_score":6,"execution_risk_score":9,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":"unknown_or_not_supported","fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":3,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":63.5,"stage_label_before":"Stage4B-watch","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":9,"customer_quality_score":7,"policy_or_regulatory_score":10,"valuation_repricing_score":6,"execution_risk_score":12,"legal_or_contract_risk_score":11,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":"unknown_or_not_supported","fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":3,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":70.8,"stage_label_after":"Stage4B-watch","changed_components":["contract_score","relative_strength_score","policy_or_regulatory_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":44.39,"MAE_90D_pct":-20.98,"score_return_alignment_label":"score_low_return_high_missed_structural","row_validation_status":"valid_for_shadow_calibration","round":"R1","loop":"4","sector":"산업재·수주·인프라"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L4_C04_LS_ELECTRIC_GRID_DATACENTER","trigger_id":"R1L4_C04_T1_STAGE2_GRID_AWARENESS","symbol":"010120","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":6,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":9,"customer_quality_score":7,"policy_or_regulatory_score":5,"valuation_repricing_score":8,"execution_risk_score":10,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":8,"order_intake_quality_score":"unknown_or_not_supported","fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":5,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":71.8,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":7,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":10,"customer_quality_score":7,"policy_or_regulatory_score":5,"valuation_repricing_score":8,"execution_risk_score":14,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":9,"order_intake_quality_score":"unknown_or_not_supported","fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":8,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":79.7,"stage_label_after":"Stage2-Actionable high_volatility_small_size","changed_components":["backlog_visibility_score","relative_strength_score","execution_risk_score","capacity_or_shipment_score","positioning_overheat_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":34.23,"MAE_90D_pct":-38.29,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration","round":"R1","loop":"4","sector":"산업재·수주·인프라"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L4_C04_LS_ELECTRIC_GRID_DATACENTER","trigger_id":"R1L4_C04_T2_STAGE2_ACTIONABLE_GRID","symbol":"010120","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":6,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":9,"customer_quality_score":7,"policy_or_regulatory_score":5,"valuation_repricing_score":8,"execution_risk_score":10,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":8,"order_intake_quality_score":"unknown_or_not_supported","fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":5,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":71.8,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":7,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":10,"customer_quality_score":7,"policy_or_regulatory_score":5,"valuation_repricing_score":8,"execution_risk_score":14,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":9,"order_intake_quality_score":"unknown_or_not_supported","fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":8,"thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":79.7,"stage_label_after":"Stage2-Actionable high_volatility_small_size","changed_components":["backlog_visibility_score","relative_strength_score","execution_risk_score","capacity_or_shipment_score","positioning_overheat_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":34.23,"MAE_90D_pct":-38.29,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_shadow_calibration","round":"R1","loop":"4","sector":"산업재·수주·인프라"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L4_C05_SAMSUNG_EA_EPC_CONTRACT_FAIL","trigger_id":"R1L4_C05_T1_STAGE2_FADHILI_ORDER","symbol":"028050","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":7,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":8,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":7,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":"unknown_or_not_supported","thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":59.6,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":7,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":10,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":7,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":"unknown_or_not_supported","thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":58.7,"stage_label_after":"Stage2-Actionable watch_only_not_green","changed_components":["margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":15.81,"MAE_90D_pct":-14.62,"score_return_alignment_label":"score_mid_return_low_watch_only","row_validation_status":"valid_for_shadow_calibration","round":"R1","loop":"4","sector":"산업재·수주·인프라"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L4_C05_SAMSUNG_EA_EPC_CONTRACT_FAIL","trigger_id":"R1L4_C05_T2_STAGE2_ACTIONABLE_FADHILI","symbol":"028050","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":7,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":8,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":7,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":"unknown_or_not_supported","thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":59.6,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":7,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":10,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":7,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":"unknown_or_not_supported","thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":58.7,"stage_label_after":"Stage2-Actionable watch_only_not_green","changed_components":["margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":15.81,"MAE_90D_pct":-14.62,"score_return_alignment_label":"score_mid_return_low_watch_only","row_validation_status":"valid_for_shadow_calibration","round":"R1","loop":"4","sector":"산업재·수주·인프라"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R1L4_C05_SAMSUNG_EA_EPC_CONTRACT_FAIL","trigger_id":"R1L4_C05_T5_STAGE4B_EPC_LOCAL_PEAK","symbol":"028050","trigger_type":"Stage4B","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":7,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":8,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":7,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":"unknown_or_not_supported","thesis_break_score":"unknown_or_not_supported"},"weighted_score_before":59.6,"stage_label_before":"Stage4B-watch","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":7,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":10,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":"unknown_or_not_supported","order_intake_quality_score":7,"fcf_conversion_score":"unknown_or_not_supported","positioning_overheat_score":"unknown_or_not_supported","thesis_break_score":"unknown_or_not_supported"},"weighted_score_after":58.7,"stage_label_after":"Stage2-Actionable watch_only_not_green","changed_components":["margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"After profile raises contract/backlog/relative-strength only when order-to-backlog route exists, and raises execution/volatility risk when MAE or legal delay is large.","selected_by_profile":false,"MFE_90D_pct":0.0,"MAE_90D_pct":-33.1,"score_return_alignment_label":"score_mid_return_low_watch_only","row_validation_status":"valid_for_shadow_calibration","round":"R1","loop":"4","sector":"산업재·수주·인프라"}
```

### 27.5 Profile comparison rows CSV

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,5,5,4,20.82,17.65,-22.06,-24.5,39.43,-26.25,0.4,0.6,0.2,2,2,0.56,unavailable,unavailable,"reference; formal Green/confirmation often late or fragile"
profile_comparison,stage2_actionable_early_evidence_plus,5,4,4,29.95,33.96,-20.83,-19.55,50.53,-20.83,0.75,0.5,0.0,0,1,0.37,unavailable,unavailable,"better upside capture; requires volatility guardrail for nuclear/grid names"
profile_comparison,stage3_yellow_entry_relaxed,5,4,4,27.37,28.6,-22.8,-23.16,51.7,-22.8,0.75,0.75,0.0,0,1,0.45,unavailable,unavailable,valid only with MAE cap and position sizing
profile_comparison,green_confirmation_timing_relaxed,5,4,4,22.07,23.28,-23.92,-26.16,45.33,-23.92,0.5,0.75,0.0,1,2,0.56,unavailable,unavailable,relaxing Green alone does not solve high-MAE names
profile_comparison,four_b_peak_timing_tuned,5,4,0,14.47,6.75,-24.42,-22.74,18.76,-27.24,0.25,1.0,0.0,0,0,unavailable,0.66,0.57,"price-only local 4B rejected; non-price valuation/margin/legal evidence required"
profile_comparison,four_c_thesis_break_earlier,5,0,0,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,unavailable,"not validated; no hard 4C trigger in this R1 loop"
```

### 27.6 Shadow weight CSV

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_contract_backlog_relative_strength,0,2,+2,Hanwha and Rotem early order/backlog + RS triggers captured larger or cleaner MFE than later Green.,"Baseline avg MFE90 20.82/MAE90 -22.06 vs early-evidence profile avg MFE90 29.45/MAE90 -20.83 on selected cases; Samsung false-positive removed.",R1L4_C01_T1_STAGE2_WAR_REARMAMENT|R1L4_C02_T2|R1L4_C03_T2_STAGE2_ACTIONABLE_CZECH|R1L4_C04_T2_STAGE2_ACTIONABLE_GRID,4,"shadow-only; not production"
shadow_weight,volatility_guardrail_for_policy_or_grid_events,0,3,+3,"Doosan and LS produced strong MFE but MAE worse than -28%; promotion without sizing guardrail is misleading.","Keeps MFE capture but flags bad-entry-rate; avoids converting high-MAE Stage2 into clean Green.",R1L4_C03_T2_STAGE2_ACTIONABLE_CZECH|R1L4_C04_T2_STAGE2_ACTIONABLE_GRID,2,"shadow-only; high-volatility entry tier"
shadow_weight,epc_contract_without_margin_bridge_penalty,0,-2,-2,"Samsung E&A large EPC headline had only 15.81% MFE90 and -35.57% MAE180; contract headline alone should not force Green.",False-positive score reduced by treating EPC contract-only evidence as watch-only until margin/revision bridge appears.,R1L4_C05_T2_STAGE2_ACTIONABLE_FADHILI,1,"shadow-only; exploratory because single counterexample"
shadow_weight,non_price_4b_required_for_full_4b,0,2,+2,"Rotem formal contract day was a local high but full-window peak came later; price-only local 4B can cut off structural upside.","Rejects price-only local 4B as full exit; preserves Hanwha/Samsung non-price 4B overlays.",R1L4_C01_T5_STAGE4B_DEFENSE_OVERHEAT|R1L4_C02_T5|R1L4_C05_T5_STAGE4B_EPC_LOCAL_PEAK,3,"shadow-only; separates local from full-window proximity"
shadow_weight,hard_4c_delta,0,0,0,No hard 4C trigger was validated in this loop.,"No weight change; narrative-only thesis-break watches rejected for calibration.",,0,not validated
```

### 27.7 Optimization decision rows JSONL

```jsonl
{"row_type":"optimization_decision","decision_id":"R1L4_D1","hypothesis":"Stage2-Actionable should promote when order/backlog visibility and relative strength arrive before full Green confirmation.","tested_cases":["R1L4_C01_HANWHA_AERO_DEFENSE_BACKLOG","R1L4_C02_HYUNDAI_ROTEM_POLAND_K2","R1L4_C03_DOOSAN_NUCLEAR_POLICY_ORDER","R1L4_C04_LS_ELECTRIC_GRID_DATACENTER"],"tested_trigger_ids":["R1L4_C01_T1_STAGE2_WAR_REARMAMENT","R1L4_C02_T2","R1L4_C03_T2_STAGE2_ACTIONABLE_CZECH","R1L4_C04_T2_STAGE2_ACTIONABLE_GRID"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus","backtest_result_summary":"Early evidence profile lifted selected-case avg MFE90 and removed Samsung EPC false positive, but MAE dispersion remains large.","accepted_or_rejected":"accepted_shadow_only","delta_magnitude":"+2","why_not_larger_delta":"usable cases are still concentrated in defense/nuclear/grid/EPC and two names have very deep MAE.","risks":"Over-promoting event premium without backlog/margin bridge or volatility sizing.","next_validation_needed":"Validate transformer pure-play cases and shipbuilding/order cases using stock-web rows."}
{"row_type":"optimization_decision","decision_id":"R1L4_D2","hypothesis":"High-MAE policy/grid Stage2 should be promoted only as small-size or watch-to-entry tier.","tested_cases":["R1L4_C03_DOOSAN_NUCLEAR_POLICY_ORDER","R1L4_C04_LS_ELECTRIC_GRID_DATACENTER"],"tested_trigger_ids":["R1L4_C03_T2_STAGE2_ACTIONABLE_CZECH","R1L4_C04_T2_STAGE2_ACTIONABLE_GRID"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus","backtest_result_summary":"Doosan/LS MFE90 was 17.65/34.23 but MAE90 was -28.71/-38.29; promotion without risk tag is rejected.","accepted_or_rejected":"accepted_shadow_only","delta_magnitude":"+3 volatility guardrail, not +3 pure score","why_not_larger_delta":"deep MAE implies path risk; full production score should wait for broader samples.","risks":"Can look correct by MFE while being hard to hold in real operation.","next_validation_needed":"Find lower-MAE grid/utility equipment examples and failed policy-event counterexamples."}
{"row_type":"optimization_decision","decision_id":"R1L4_D3","hypothesis":"Large EPC contract headline needs margin/revision bridge before Green.","tested_cases":["R1L4_C05_SAMSUNG_EA_EPC_CONTRACT_FAIL"],"tested_trigger_ids":["R1L4_C05_T2_STAGE2_ACTIONABLE_FADHILI","R1L4_C05_T5_STAGE4B_EPC_LOCAL_PEAK"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus","backtest_result_summary":"Samsung E&A produced only 15.81% MFE90 and -35.57% MAE180; 4B overlay at local peak worked as margin-bridge failure warning.","accepted_or_rejected":"accepted_shadow_only","delta_magnitude":"-2","why_not_larger_delta":"single counterexample; needs more EPC/plant cases.","risks":"Could under-score genuine EPC rerating if margin bridge later closes.","next_validation_needed":"Add EPC successes with revised OP/margin evidence."}
{"row_type":"optimization_decision","decision_id":"R1L4_D4","hypothesis":"4B should split local price-only watch from full-window non-price 4B.","tested_cases":["R1L4_C01_HANWHA_AERO_DEFENSE_BACKLOG","R1L4_C02_HYUNDAI_ROTEM_POLAND_K2","R1L4_C05_SAMSUNG_EA_EPC_CONTRACT_FAIL"],"tested_trigger_ids":["R1L4_C01_T5_STAGE4B_DEFENSE_OVERHEAT","R1L4_C02_T5","R1L4_C05_T5_STAGE4B_EPC_LOCAL_PEAK"],"baseline_profile":"baseline_current_proxy","selected_profile":"four_b_peak_timing_tuned","backtest_result_summary":"Hanwha/Samsung 4B overlays were near local/full peak with non-price risk; Rotem was local-only and too early for full exit.","accepted_or_rejected":"accepted_shadow_only","delta_magnitude":"+2","why_not_larger_delta":"4B evidence remains sparse; production exit logic unchanged.","risks":"Too much 4B strictness can miss fast blowoff reversals.","next_validation_needed":"Need more 4B overlays in transformer and shipbuilding cycles."}
{"row_type":"optimization_decision","decision_id":"R1L4_D5","hypothesis":"Hard 4C cannot be changed without validated thesis-break trigger.","tested_cases":["R1L4_C01_HANWHA_AERO_DEFENSE_BACKLOG","R1L4_C02_HYUNDAI_ROTEM_POLAND_K2","R1L4_C03_DOOSAN_NUCLEAR_POLICY_ORDER","R1L4_C04_LS_ELECTRIC_GRID_DATACENTER","R1L4_C05_SAMSUNG_EA_EPC_CONTRACT_FAIL"],"tested_trigger_ids":[],"baseline_profile":"baseline_current_proxy","selected_profile":"four_c_thesis_break_earlier","backtest_result_summary":"No hard 4C trigger with 180D OHLC validation; delta remains zero.","accepted_or_rejected":"rejected_for_this_round","delta_magnitude":"0","why_not_larger_delta":"this_round_does_not_validate hard 4C protection.","risks":"Premature 4C hard gate from narrative-only evidence.","next_validation_needed":"Find actual contract collapse / legal block / margin break before drawdown cases."}
```

### 27.8 Narrative-only rows JSONL

```jsonl
{"row_type":"narrative_only","case_id":"R1L4_ALL","symbol":"mixed","reason":"hard_4c_not_confirmed_in_this_loop; no 4C shadow delta proposed","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

### 27.9 Aggregate metric rows CSV

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,below_entry_90D_rate,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,5,1,33.3,33.3,-10.4,-10.4,73.7,-10.4,1.0,unavailable,unavailable,unavailable,"representative rows only; duplicate same-entry labels excluded"
aggregate_metric,Stage2-Actionable,5,5,25.06,23.0,-21.16,-18.3,44.53,-25.35,1.0,0.0,unavailable,unavailable,"representative rows only; duplicate same-entry labels excluded"
aggregate_metric,Stage3-Yellow,1,1,14.5,14.5,-21.7,-21.7,51.5,-21.7,1.0,unavailable,unavailable,unavailable,"representative rows only; duplicate same-entry labels excluded"
aggregate_metric,Stage3-Green,2,1,28.9,28.9,-4.2,-4.2,63.8,-4.2,1.0,0.37,unavailable,unavailable,"representative rows only; duplicate same-entry labels excluded"
aggregate_metric,Stage4B,4,0,14.47,6.75,-24.42,-22.74,18.76,-27.24,1.0,unavailable,0.66,0.57,"overlay-only aggregate; not mixed with entry aggregate"
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
completed_round = R1 Loop 4
next_round = R2
next_loop = 4
next_sector = AI·반도체·전자부품
production_scoring_changed = false
shadow_weight_only = true
```

## 30. Source Notes

- Price source: Songdaiki/stock-web atlas, `tradable_raw`, `raw_unadjusted_marcap`.
- Manifest/schema/universe were checked before writing this MD.
- Evidence sources are public news/report/disclosure-style sources listed in Section 6.
- Relative returns were left unavailable because this calibration loop did not fetch a separate sector-index shard; core OHLC MFE/MAE calibration remains valid.
- This MD intentionally does not use `stock_agent` repository contents and does not propose production scoring changes.

- Current run re-read stock-web manifest/schema/universe through GitHub API before writing: manifest max_date 2026-02-20, price basis tradable_raw, adjustment raw_unadjusted_marcap.
- Continuation caveat: this file preserves the same calibration-usable R1 evidence families as the prior R1 validation pass; it is designed as a standalone MD handoff row set, not a live candidate discovery file.
