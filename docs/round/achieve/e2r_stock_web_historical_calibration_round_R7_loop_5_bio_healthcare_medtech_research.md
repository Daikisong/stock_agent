# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata

```text
round = R7
loop = 3
sector = 바이오·헬스케어·의료기기
sector_slug = bio_healthcare_medtech
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough
live_candidate_mode = false
current_stock_discovery_allowed = false
stock_agent_repo_access_allowed = false
stock_agent_code_patch_allowed = false
repo_path_output_allowed = false
production_scoring_changed = false
shadow_weight_only = true
output_format = one_standalone_markdown_file
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
prompt_version = v11
round_resolution_status = continued_from_prior_next_round
assumed_round = R7
assumption_note = "직전 산출물의 next_round가 R7 Loop 3였으므로 R7 Loop 3로 진행했다. stock_agent 레포나 기존 구현 파일은 열지 않았다."
```

This file is a standalone historical calibration / backtest optimization output. It is not a live candidate scan, not a stock recommendation, and not a repository patch. The only repository accessed for this research run is `Songdaiki/stock-web` as a historical OHLC price atlas.

## 1. Round Scope

R7 Loop 3 retests the 바이오·헬스케어·의료기기 loop after the earlier CDMO / platform licensing / FDA binary / diagnostic demand-shock cases. The new emphasis is a medtech consumables-and-export route, represented by Classys, because the earlier R7 loops validated biotech and diagnostic volatility but left medical-device operating leverage under-tested.

The main calibration question is not “which company was good,” but which public evidence bundle deserved earlier Stage2-Actionable / Stage3-Yellow treatment and which bundle needed hard binary-risk or 4B overlay.

## 2. Stock-Web OHLC Input / Price Source Validation

| item | path | observed value |
|---|---|---|
| manifest | `atlas/manifest.json` | `source_name=FinanceData/marcap`; `max_date=2026-02-20`; `tradable_row_count=14354401`; `raw_row_count=15214118`; markets `KONEX`, `KOSDAQ`, `KOSDAQ GLOBAL`, `KOSPI` |
| schema | `atlas/schema.json` | tradable columns `d,o,h,l,c,v,a,mc,s,m`; raw columns add `rs`; MFE/MAE formulas confirmed |
| calibration shard root | `atlas/ohlcv_tradable_by_symbol_year` | tradable raw OHLCV, zero-volume/invalid rows excluded |
| raw shard root | `atlas/ohlcv_raw_by_symbol_year` | raw reference rows only, not used for score calibration |
| universe | `atlas/universe/all_symbols.csv` | symbol/profile map used only for path normalization |

Price-source validation row:

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 3. Historical Eligibility Gate

| gate | result |
|---|---|
| trigger dates are historical | pass |
| entry dates exist in tradable shards | pass for all calibration rows |
| at least 180 forward trading days | pass for all representative rows; some 4B overlay 1Y/2Y fields are unavailable because they occur near/after 2024 peaks |
| OHLCV present | pass |
| MFE/MAE 30D/90D/180D calculated | pass |
| corporate-action contamination | clean for selected 180D windows; Classys has a 2017 SPAC/name-change corporate-action candidate, outside all selected 2023~2024 windows |
| raw/unadjusted caveat | retained; no adjusted-price inference made |

## 4. Canonical Archetypes Tested

| archetype | sub-archetype | validation status | mechanism |
|---|---|---|---|
| CDMO_BACKLOG_CAPACITY_VISIBILITY | global customer + capacity + contract/backlog | validated | public order/backlog and utilization evidence can justify Stage2-Actionable before Green |
| PLATFORM_TECH_LICENSING_OPTIONALITY | enzyme/platform licensing optionality | validated with sizing guardrail | early platform news can produce very high MFE, but MAE/volatility requires cap |
| REGULATORY_BINARY_APPROVAL_RISK | FDA binary event premium | validated as Green blocker | price strength before final regulatory outcome must not become structural Green |
| DIAGNOSTIC_DEMAND_SHOCK_EPS_RERATING | emergency-use demand shock | validated as exceptional Stage2 route | public authorization/demand evidence can precede reported EPS and still rerate sharply |
| MEDTECH_CONSUMABLE_EXPORT_OPERATING_LEVERAGE | installed base + consumables + overseas expansion | newly validated in Loop 3 | recurring consumables + export expansion can be Stage2-Actionable before the obvious Green spike |

## 5. Case Selection Summary

| case_id | symbol | company | case_type | primary_archetype | best_trigger | calibration_usable |
|---|---|---|---|---|---|---|
| R7L3_C1_SBIO_CDMO_BACKLOG | 207940 | 삼성바이오로직스 | structural_success | CDMO_BACKLOG_CAPACITY_VISIBILITY | R7L3_C1_T2_STAGE2_ACTIONABLE | true |
| R7L3_C2_ALTEOGEN_PLATFORM | 196170 | 알테오젠 | stage2_promote_candidate_and_4b_watch | PLATFORM_TECH_LICENSING_OPTIONALITY | R7L3_C2_T2_STAGE2_ACTIONABLE | true |
| R7L3_C3_HLB_BINARY | 028300 | HLB | failed_rerating_4c_thesis_break | REGULATORY_BINARY_APPROVAL_RISK | R7L3_C3_T1_STAGE2_EVENT_PREMIUM | true |
| R7L3_C4_SEEG_DIAGNOSTIC | 096530 | 씨젠 | diagnostic_structural_success_then_4b | DIAGNOSTIC_DEMAND_SHOCK_EPS_RERATING | R7L3_C4_T1_STAGE2_EUA_DEMAND | true |
| R7L3_C5_CLASSYS_MEDTECH | 214150 | 클래시스 | medtech_stage2_promote_candidate | MEDTECH_CONSUMABLE_EXPORT_OPERATING_LEVERAGE | R7L3_C5_T1_STAGE2_ACTIONABLE | true |

## 6. Evidence Source Map

| case | trigger evidence used | evidence confidence | evidence caveat |
|---|---|---|---|
| 삼성바이오로직스 | CDMO contract/backlog/capacity/customer-quality evidence and 2024 earnings momentum | medium | exact individual contract disclosure timestamps should be rechecked by coding-agent ingestion before production conversion |
| 알테오젠 | ALT-B4 / Keytruda SC optionality and platform licensing news around 2024 | medium | very high volatility; licensing optionality is not the same as FCF visibility |
| HLB | FDA approval expectation, price premium, and May 2024 CRL / non-approval shock | high for 4C, medium for pre-CRL expectation | binary regulatory risk caps Stage3-Green even when price is strong |
| 씨젠 | Korean COVID-19 test authorization and global diagnostic-kit demand shock in early 2020 | high | demand shock is real, but normalization requires 4B overlay |
| 클래시스 | 2023~2024 medical-device export/installed-base/consumables operating leverage; public earnings momentum | medium | exact report timestamps need batch revalidation; price path itself is clean and usable |

## 7. Price Data Source Map

| symbol | company | profile_path | shard paths used | corporate-action window status |
|---|---|---|---|---|
| 207940 | 삼성바이오로직스 | `atlas/symbol_profiles/207/207940.json` | `atlas/ohlcv_tradable_by_symbol_year/207/207940/2024.csv`, `2025.csv` | selected 180D windows clean; later 2Y unavailable/blocked |
| 196170 | 알테오젠 | `atlas/symbol_profiles/196/196170.json` | `atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv` | selected 180D window clean |
| 028300 | HLB | `atlas/symbol_profiles/028/028300.json` | `atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv`, `2025.csv` | selected 180D window clean |
| 096530 | 씨젠 | `atlas/symbol_profiles/096/096530.json` | `atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv` | 2020 180D window clean; later 2Y contaminated/unavailable |
| 214150 | 클래시스 | `atlas/symbol_profiles/214/214150.json` | `atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv`, `2024.csv` | 2017 SPAC/name-change candidate outside selected 2023~2024 calibration windows |

## 8. Case-by-Case Trigger Grid

| trigger_id | company | trigger_type | trigger_date | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | outcome | dedupe_for_aggregate | aggregate_group_role |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---:|---|---|---|
| R7L3_C1_T1_STAGE2 | 삼성바이오로직스 | Stage2 | 2024-01-22 | 2024-01-22 | 793000 | 11.0 | -3.2 | 26.7 | -9.1 | 2025-02-14 | 1209000 | good_entry | true | representative |
| R7L3_C1_T2_STAGE2_ACTIONABLE | 삼성바이오로직스 | Stage2-Actionable | 2024-07-02 | 2024-07-02 | 810000 | 37.4 | -3.2 | 49.3 | -3.2 | 2025-02-14 | 1209000 | excellent_entry | true | representative |
| R7L3_C1_T4_STAGE3_GREEN | 삼성바이오로직스 | Stage3-Green | 2024-07-26 | 2024-07-26 | 915000 | 21.6 | -8.1 | 32.1 | -8.1 | 2025-02-14 | 1209000 | late_but_valid_entry | true | representative |
| R7L3_C1_T5_4B_WATCH | 삼성바이오로직스 | 4B-watch | 2025-02-14 | 2025-02-14 | 1180000 | 0.8 | -16.9 | 0.8 | -17.7 | 2025-02-14 | 1209000 | 4b_watch_near_peak | false | 4B_overlay_only |
| R7L3_C2_T2_STAGE2_ACTIONABLE | 알테오젠 | Stage2-Actionable | 2024-02-22 | 2024-02-23 | 131200 | 121.8 | -9.1 | 247.2 | -9.1 | 2024-11-11 | 455500 | excellent_entry | true | representative |
| R7L3_C2_T3_STAGE3_YELLOW | 알테오젠 | Stage3-Yellow | 2024-03-05 | 2024-03-05 | 192200 | 51.4 | -18.8 | 137.0 | -18.8 | 2024-11-11 | 455500 | good_entry_high_volatility | true | representative |
| R7L3_C2_T4_STAGE3_GREEN | 알테오젠 | Stage3-Green | 2024-06-07 | 2024-06-07 | 269000 | 35.1 | -10.6 | 69.3 | -10.6 | 2024-11-11 | 455500 | late_entry | true | representative |
| R7L3_C2_T5_4B_WATCH | 알테오젠 | 4B-watch | 2024-11-11 | 2024-11-11 | 445500 | 2.2 | -38.7 | 2.2 | -38.7 | 2024-11-11 | 455500 | price_only_near_peak_watch | false | 4B_overlay_only |
| R7L3_C3_T1_STAGE2_EVENT_PREMIUM | HLB | Stage2 | 2024-01-26 | 2024-01-26 | 65200 | 97.9 | -3.4 | 97.9 | -27.9 | 2024-03-26 | 129000 | event_premium_binary_success_before_4c | true | representative |
| R7L3_C3_T3_STAGE3_YELLOW | HLB | Stage3-Yellow | 2024-03-21 | 2024-03-21 | 112700 | 14.5 | -58.3 | 14.5 | -58.3 | 2024-03-26 | 129000 | false_positive_score | true | representative |
| R7L3_C3_T5_4B_WATCH | HLB | 4B-watch | 2024-03-26 | 2024-03-26 | 120800 | 6.8 | -61.1 | 6.8 | -61.1 | 2024-03-26 | 129000 | 4b_watch_near_peak | false | 4B_overlay_only |
| R7L3_C3_T6_4C_TBREAK | HLB | 4C-thesis-break | 2024-05-17 | 2024-05-17 | 67100 | 46.2 | -29.9 | 46.2 | -29.9 | 2024-07-08 | 98100 | hard_4c_late_but_still_protective | false | 4C_overlay_only |
| R7L3_C4_T1_STAGE2_EUA_DEMAND | 씨젠 | Stage2 | 2020-02-12 | 2020-02-13 | 31450 | 349.6 | -2.5 | 924.5 | -2.5 | 2020-08-10 | 322200 | excellent_entry | true | representative |
| R7L3_C4_T3_STAGE3_YELLOW | 씨젠 | Stage3-Yellow | 2020-03-02 | 2020-03-02 | 40400 | 249.8 | -9.9 | 697.5 | -9.9 | 2020-08-10 | 322200 | excellent_entry | true | representative |
| R7L3_C4_T4_STAGE3_GREEN | 씨젠 | Stage3-Green | 2020-03-26 | 2020-03-26 | 114500 | 22.5 | -28.3 | 181.4 | -28.3 | 2020-08-10 | 322200 | late_but_still_good_entry | true | representative |
| R7L3_C4_T5_4B_BLOWOFF | 씨젠 | 4B-watch | 2020-08-10 | 2020-08-10 | 310700 | 3.4 | -43.6 | 3.4 | -43.6 | 2020-08-10 | 322200 | 4B_watch_success | false | 4B_overlay_only |
| R7L3_C5_T1_STAGE2_ACTIONABLE | 클래시스 | Stage2-Actionable | 2023-05-17 | 2023-05-17 | 26400 | 59.1 | -8.0 | 63.1 | -8.0 | 2024-10-21 | 62900 | excellent_medtech_entry | true | representative |
| R7L3_C5_T3_STAGE3_YELLOW | 클래시스 | Stage3-Yellow | 2023-08-21 | 2023-08-21 | 37500 | 14.8 | -16.5 | 32.8 | -22.9 | 2024-10-21 | 62900 | acceptable_but_volatile_yellow | true | representative |
| R7L3_C5_T4_STAGE3_GREEN | 클래시스 | Stage3-Green | 2024-05-09 | 2024-05-09 | 48500 | 19.4 | -15.4 | 29.7 | -17.5 | 2024-10-21 | 62900 | late_entry | true | representative |
| R7L3_C5_T5_4B_WATCH | 클래시스 | 4B-watch | 2024-10-21 | 2024-10-21 | 61900 | 1.6 | -35.4 | 1.6 | -35.4 | 2024-10-21 | 62900 | 4b_watch_near_peak | false | 4B_overlay_only |

## 9. Trigger-Level OHLC Backtest Tables

All return values are percentage units. Relative-return fields are marked `unavailable` because this calibration run did not import index/ETF shards; that does not block core trigger-level OHLC validation.

| trigger_id | price_shard_path | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MFE_1Y | MFE_2Y | MAE_30D | MAE_90D | MAE_180D | MAE_1Y | below_30D | below_90D | peak_date | peak_price | dd_after_peak | green_lateness_ratio | 4B_local | 4B_full | 4B_verdict |
|---|---|---|---:|---:|---:|---:|---|---|---:|---:|---:|---|---|---|---|---:|---:|---|---|---|---|
| R7L3_C1_T1_STAGE2 | `atlas/ohlcv_tradable_by_symbol_year/207/207940/2024.csv` | 2024-01-22 | 793000 | 10.7 | 11.0 | 26.7 | 52.5 | unavailable | -3.2 | -3.2 | -9.1 | -9.1 | true | true | 2025-02-14 | 1209000 | -17.7 | not_applicable | not_applicable | not_applicable | not_4B |
| R7L3_C1_T2_STAGE2_ACTIONABLE | `atlas/ohlcv_tradable_by_symbol_year/207/207940/2024.csv` | 2024-07-02 | 810000 | 21.7 | 37.4 | 49.3 | 49.3 | unavailable | -3.2 | -3.2 | -3.2 | -17.7 | true | true | 2025-02-14 | 1209000 | -17.7 | not_applicable | not_applicable | not_applicable | not_4B |
| R7L3_C1_T4_STAGE3_GREEN | `atlas/ohlcv_tradable_by_symbol_year/207/207940/2024.csv` | 2024-07-26 | 915000 | 9.8 | 21.6 | 32.1 | 32.1 | unavailable | -8.1 | -8.1 | -8.1 | -17.7 | true | true | 2025-02-14 | 1209000 | -17.7 | 0.37 | not_applicable | not_applicable | not_4B |
| R7L3_C1_T5_4B_WATCH | `atlas/ohlcv_tradable_by_symbol_year/207/207940/2025.csv` | 2025-02-14 | 1180000 | 0.8 | 0.8 | 0.8 | unavailable | unavailable | -16.9 | -16.9 | -17.7 | unavailable | true | true | 2025-02-14 | 1209000 | -17.7 | not_applicable | 0.96 | 0.96 | good_full_window_4B_timing |
| R7L3_C2_T2_STAGE2_ACTIONABLE | `atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv` | 2024-02-23 | 131200 | 71.9 | 121.8 | 247.2 | 247.2 | unavailable | -9.1 | -9.1 | -9.1 | -38.7 | true | true | 2024-11-11 | 455500 | -38.7 | not_applicable | not_applicable | not_applicable | not_4B |
| R7L3_C2_T3_STAGE3_YELLOW | `atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv` | 2024-03-05 | 192200 | 17.3 | 51.4 | 137.0 | 137.0 | unavailable | -18.8 | -18.8 | -18.8 | -38.7 | true | true | 2024-11-11 | 455500 | -38.7 | not_applicable | not_applicable | not_applicable | not_4B |
| R7L3_C2_T4_STAGE3_GREEN | `atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv` | 2024-06-07 | 269000 | 13.9 | 35.1 | 69.3 | 69.3 | unavailable | -10.6 | -10.6 | -10.6 | -38.7 | true | true | 2024-11-11 | 455500 | -38.7 | 0.52 | not_applicable | not_applicable | not_4B |
| R7L3_C2_T5_4B_WATCH | `atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv` | 2024-11-11 | 445500 | 2.2 | 2.2 | 2.2 | unavailable | unavailable | -38.7 | -38.7 | -38.7 | unavailable | true | true | 2024-11-11 | 455500 | -38.7 | not_applicable | 0.97 | 0.97 | price_only_near_peak_watch_not_full_4B |
| R7L3_C3_T1_STAGE2_EVENT_PREMIUM | `atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv` | 2024-01-26 | 65200 | 27.3 | 97.9 | 97.9 | 97.9 | unavailable | -3.4 | -3.4 | -27.9 | -29.9 | true | true | 2024-03-26 | 129000 | -61.1 | not_applicable | not_applicable | not_applicable | not_4B |
| R7L3_C3_T3_STAGE3_YELLOW | `atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv` | 2024-03-21 | 112700 | 14.5 | 14.5 | 14.5 | 14.5 | unavailable | -58.3 | -58.3 | -58.3 | -61.1 | true | true | 2024-03-26 | 129000 | -61.1 | not_applicable | not_applicable | not_applicable | not_4B |
| R7L3_C3_T5_4B_WATCH | `atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv` | 2024-03-26 | 120800 | 6.8 | 6.8 | 6.8 | unavailable | unavailable | -61.1 | -61.1 | -61.1 | unavailable | true | true | 2024-03-26 | 129000 | -61.1 | not_applicable | 0.94 | 0.94 | good_peak_proximity_but_price_only_not_full_4B |
| R7L3_C3_T6_4C_TBREAK | `atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv` | 2024-05-17 | 67100 | 10.0 | 46.2 | 46.2 | unavailable | unavailable | -29.9 | -29.9 | -29.9 | unavailable | true | true | 2024-07-08 | 98100 | -29.9 | not_applicable | not_applicable | not_applicable | not_4B |
| R7L3_C4_T1_STAGE2_EUA_DEMAND | `atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv` | 2020-02-13 | 31450 | 349.6 | 349.6 | 924.5 | 924.5 | contaminated_or_unavailable | -2.5 | -2.5 | -2.5 | -3.0 | true | true | 2020-08-10 | 322200 | -45.6 | not_applicable | not_applicable | not_applicable | not_4B |
| R7L3_C4_T3_STAGE3_YELLOW | `atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv` | 2020-03-02 | 40400 | 249.8 | 249.8 | 697.5 | 697.5 | contaminated_or_unavailable | -9.9 | -9.9 | -9.9 | -43.6 | true | true | 2020-08-10 | 322200 | -45.6 | not_applicable | not_applicable | not_applicable | not_4B |
| R7L3_C4_T4_STAGE3_GREEN | `atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv` | 2020-03-26 | 114500 | 22.5 | 22.5 | 181.4 | 181.4 | contaminated_or_unavailable | -28.3 | -28.3 | -28.3 | -43.6 | true | true | 2020-08-10 | 322200 | -45.6 | 0.286 | not_applicable | not_applicable | not_4B |
| R7L3_C4_T5_4B_BLOWOFF | `atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv` | 2020-08-10 | 310700 | 3.4 | 3.4 | 3.4 | contaminated_or_unavailable | contaminated_or_unavailable | -31.3 | -43.6 | -43.6 | contaminated_or_unavailable | true | true | 2020-08-10 | 322200 | -45.6 | not_applicable | 0.96 | 0.96 | good_full_window_4B_timing |
| R7L3_C5_T1_STAGE2_ACTIONABLE | `atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv` | 2023-05-17 | 26400 | 34.3 | 59.1 | 63.1 | 63.1 | unavailable | -8.0 | -8.0 | -8.0 | -8.0 | true | true | 2024-10-21 | 62900 | -36.4 | not_applicable | not_applicable | not_applicable | not_4B |
| R7L3_C5_T3_STAGE3_YELLOW | `atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv` | 2023-08-21 | 37500 | 12.0 | 14.8 | 32.8 | 67.7 | unavailable | -16.5 | -16.5 | -22.9 | -22.9 | true | true | 2024-10-21 | 62900 | -36.4 | not_applicable | not_applicable | not_applicable | not_4B |
| R7L3_C5_T4_STAGE3_GREEN | `atlas/ohlcv_tradable_by_symbol_year/214/214150/2024.csv` | 2024-05-09 | 48500 | 17.3 | 19.4 | 29.7 | 29.7 | unavailable | -5.9 | -15.4 | -17.5 | -17.5 | true | true | 2024-10-21 | 62900 | -36.4 | 0.605 | not_applicable | not_applicable | not_4B |
| R7L3_C5_T5_4B_WATCH | `atlas/ohlcv_tradable_by_symbol_year/214/214150/2024.csv` | 2024-10-21 | 61900 | 1.6 | 1.6 | 1.6 | unavailable | unavailable | -35.4 | -35.4 | -35.4 | unavailable | true | true | 2024-10-21 | 62900 | -36.4 | not_applicable | 0.973 | 0.973 | good_full_window_4B_timing |

## 10. 1D Price Path Summaries

### 삼성바이오로직스 best actionable trigger: 2024-07-02 close 810,000

| point | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | 0.0 | 1.0 | -2.2 |
| D+5 | -2.2 | 3.1 | -3.2 |
| D+10 | 1.9 | 4.3 | -3.2 |
| D+20 | 15.8 | 18.5 | -3.2 |
| D+30 | 18.5 | 21.7 | -3.2 |
| D+60 | 19.1 | 31.1 | -3.2 |
| D+90 | 30.7 | 37.4 | -3.2 |
| D+180 | 45.7 | 49.3 | -3.2 |
| D+252 | 26.9 | 49.3 | -3.2 |
| D+504 | unavailable | unavailable | unavailable |

### 알테오젠 best actionable trigger: 2024-02-23 close 131,200

| point | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | 19.4 | 23.2 | 4.1 |
| D+5 | 25.4 | 33.8 | -9.1 |
| D+10 | 46.5 | 51.0 | -9.1 |
| D+20 | 56.1 | 71.9 | -9.1 |
| D+30 | 30.3 | 71.9 | -9.1 |
| D+60 | 44.8 | 84.8 | -9.1 |
| D+90 | 104.6 | 121.8 | -9.1 |
| D+180 | 239.6 | 247.2 | -9.1 |
| D+252 | 126.5 | 247.2 | -9.1 |
| D+504 | unavailable | unavailable | unavailable |

### HLB binary event trigger: 2024-01-26 close 65,200

| point | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | -3.2 | 11.3 | -8.0 |
| D+5 | 7.4 | 12.0 | -8.0 |
| D+10 | 16.1 | 27.3 | -3.4 |
| D+20 | 25.0 | 27.3 | -3.4 |
| D+30 | 58.6 | 64.1 | -3.4 |
| D+60 | 53.4 | 97.9 | -3.4 |
| D+90 | -27.9 | 97.9 | -27.9 |
| D+180 | 12.6 | 97.9 | -29.9 |
| D+252 | 12.6 | 97.9 | -29.9 |

### 씨젠 Stage2 diagnostic trigger: 2020-02-13 close 31,450

| point | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
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

### 클래시스 medtech Stage2-Actionable trigger: 2023-05-17 close 26,400

| point | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | 0.0 | 0.8 | -3.0 |
| D+2 | -0.2 | 1.7 | -3.0 |
| D+3 | -2.3 | 1.7 | -3.8 |
| D+5 | -3.0 | 1.7 | -8.0 |
| D+10 | 3.0 | 4.7 | -8.0 |
| D+20 | 21.4 | 25.4 | -8.0 |
| D+30 | 20.8 | 34.3 | -8.0 |
| D+60 | 17.4 | 34.3 | -8.0 |
| D+90 | 34.7 | 59.1 | -8.0 |
| D+180 | 43.0 | 63.1 | -8.0 |
| D+252 | 45.3 | 63.1 | -8.0 |
| D+504 | unavailable | unavailable | unavailable |

### 클래시스 Stage3-Green trigger: 2024-05-09 close 48,500

| point | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|
| D+1 | -2.1 | 2.1 | -3.1 |
| D+5 | 2.1 | 4.7 | -3.1 |
| D+10 | 0.6 | 7.8 | -3.1 |
| D+20 | -2.1 | 7.8 | -5.9 |
| D+30 | 13.4 | 17.3 | -5.9 |
| D+60 | 1.0 | 17.3 | -15.4 |
| D+90 | 13.0 | 19.4 | -15.4 |
| D+180 | -8.6 | 29.7 | -17.5 |
| D+252 | unavailable | unavailable | unavailable |

## 11. Case Trigger Comparison

| case | best actual trigger | late / risky trigger | comparison verdict |
|---|---|---|---|
| 삼성바이오로직스 | Stage2-Actionable 2024-07-02 | Green 2024-07-26 | Green valid but gave up 15.8 pp MFE90 and added MAE |
| 알테오젠 | Stage2-Actionable 2024-02-23 | Green 2024-06-07 | Green still profitable but missed a large part of the option-value rerating |
| HLB | Stage2 event-premium 2024-01-26 | Yellow 2024-03-21 | price strength was not structural; late Yellow had MAE90 -58.3 and must be capped |
| 씨젠 | Stage2 EUA/demand 2020-02-13 | Green 2020-03-26 | Green caught some move but Stage2 captured the explosive rerating with shallow MAE |
| 클래시스 | Stage2-Actionable 2023-05-17 | Green 2024-05-09 | medtech export/consumable operating leverage was visible before the obvious Green spike |

## 12. Stage2 → Stage4 Audit

| case | Stage2 MFE large? | Stage2 MAE acceptable? | Stage2 better than Green? | evidence bundle | verdict |
|---|---|---|---|---|---|
| 삼성바이오로직스 | yes | yes | yes | CDMO contract/backlog + capacity + customer quality | promote de-risked Stage2-Actionable |
| 알테오젠 | yes | borderline but acceptable | yes | platform licensing optionality + strong RS + high-quality customer signal | promote with volatility sizing guardrail |
| HLB | yes | early yes, later no | not clean | FDA approval probability + price event premium | keep below Green until regulatory outcome closes |
| 씨젠 | yes | yes | yes | public authorization + global test demand + RS | exceptional demand-shock Stage2 route |
| 클래시스 | yes | yes | yes | installed-base / consumables / exports / operating leverage | promote medtech consumable Stage2-Actionable |

Stage2/Stage2-Actionable worked best when the early evidence had operating leverage or demand visibility. It failed as a Green signal when the evidence was a binary approval probability rather than a closed de-risking event.

## 13. Stage3 Yellow / Green Lateness Audit

| case | Stage2/Actionable entry | Green entry | peak after Stage2/Actionable | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| 삼성바이오로직스 | 810000 | 915000 | 1209000 | 0.37 | Green somewhat late |
| 알테오젠 | 131200 | 269000 | 455500 | 0.52 | Green materially late |
| HLB | 65200 | 112700 | 129000 | not_applicable | binary risk blocks broad Green relaxation |
| 씨젠 | 31450 | 114500 | 322200 | 0.286 | Green not catastrophic, but Stage2 captured most upside |
| 클래시스 | 26400 | 48500 | 62900 | 0.605 | Green missed most of the medtech operating-leverage rerating |

The loop validates a differentiated rule: relax Stage2/Yellow only when the early signal is backed by demand/contract/installed-base evidence, not when it is a binary regulatory probability.

## 14. 4B Timing Audit

| case | 4B trigger | local proximity | full-window proximity | evidence type | verdict |
|---|---|---:|---:|---|---|
| 삼성바이오로직스 | 2025-02-14 | 0.96 | 0.96 | valuation_blowoff, positioning_overheat | good full-window watch, not 4C |
| 알테오젠 | 2024-11-11 | 0.97 | 0.97 | price_only, positioning_overheat | near peak; full 4B requires non-price evidence |
| HLB | 2024-03-26 | 0.94 | 0.94 | price_only, regulatory_binary_risk | good peak watch; binary-risk cap is primary |
| 씨젠 | 2020-08-10 | 0.96 | 0.96 | valuation_blowoff, positioning_overheat, revision_slowdown | good full-window 4B timing |
| 클래시스 | 2024-10-21 | 0.973 | 0.973 | valuation_blowoff, positioning_overheat, growth_normalization_watch | good full-window 4B-watch, not thesis break |

Loop 3 reinforces the split between price-only 4B watch and full 4B. Price-only near-peak signals should trigger monitoring, but full 4B needs at least one non-price risk: valuation blowoff, revision slowdown, lockup/overhang, legal/regulatory delay, or margin/backlog slowdown.

## 15. 4C Protection Audit

HLB is the only hard 4C row in this loop. The 2024-05-17 4C event came after the March peak, so it is not an ideal early 4C. It is still useful as a binary-risk calibration row: the prior Stage3-Yellow candidate had MAE90 -58.3, proving that unresolved regulatory binary risk must cap Green.

No broad hard-4C delta is proposed for the whole R7 loop because only one hard 4C row is available.

## 16. Baseline Score Simulation

Baseline proxy waits for Green-like confirmation and therefore tends to select later entries:

| case | baseline selected | after selected | baseline MFE90 | after MFE90 | baseline MAE90 | after MAE90 | why after wins |
|---|---|---|---:|---:|---:|---:|---|
| 삼성바이오로직스 | R7L3_C1_T4_STAGE3_GREEN | R7L3_C1_T2_STAGE2_ACTIONABLE | 21.6 | 37.4 | -8.1 | -3.2 | de-risked CDMO evidence was visible earlier |
| 알테오젠 | R7L3_C2_T4_STAGE3_GREEN | R7L3_C2_T2_STAGE2_ACTIONABLE | 35.1 | 121.8 | -10.6 | -9.1 | platform optionality was rewarded before Green |
| HLB | R7L3_C3_T3_STAGE3_YELLOW | R7L3_C3_T1_STAGE2_EVENT_PREMIUM | 14.5 | 97.9 | -58.3 | -3.4 | after profile treats it as event premium, not structural Green |
| 씨젠 | R7L3_C4_T4_STAGE3_GREEN | R7L3_C4_T1_STAGE2_EUA_DEMAND | 22.5 | 349.6 | -28.3 | -2.5 | public demand shock preceded EPS confirmation |
| 클래시스 | R7L3_C5_T4_STAGE3_GREEN | R7L3_C5_T1_STAGE2_ACTIONABLE | 19.4 | 59.1 | -15.4 | -8.0 | medtech export/consumable leverage was visible before the later spike |

## 17. Shadow Profile Optimization Loop

| profile_id | profile_hypothesis | selected_representative_trigger_count | avg_MFE_90D_pct | median_MFE_90D_pct | avg_MAE_90D_pct | median_MAE_90D_pct | below_entry_90D_rate | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| baseline_current_proxy | waits for Green-like confirmation | 5 | 26.6 | 21.6 | -23.8 | -15.4 | 1.0 | 0.2 | 4 | 4 | 0.437 | 0.958 | 0.958 | reference; too late and misses Stage2/Yellow upside |
| stage2_actionable_early_evidence_plus | promotes de-risked Stage2 evidence | 5 | 133.6 | 97.9 | -5.2 | -3.4 | 1.0 | 0.0 | 0 | 0 | 0.437 | 0.958 | 0.958 | best upside/risk, but must cap binary risk |
| stage3_yellow_entry_relaxed | promotes Yellow with one gate missing | 5 | 81.4 | 51.4 | -21.3 | -16.5 | 1.0 | 0.2 | 1 | 1 | 0.437 | 0.958 | 0.958 | useful but worse than Stage2-actionable because HLB/Seegene/medtech move earlier |
| green_confirmation_timing_relaxed | brings Green threshold slightly forward | 5 | 58.4 | 35.1 | -19.0 | -15.4 | 1.0 | 0.2 | 1 | 1 | 0.437 | 0.958 | 0.958 | better than baseline only if binary risk is penalized |
| four_b_peak_timing_tuned | 4B watch overlay near full-window peak | 5 | 2.9 | 2.2 | -38.0 | -38.7 | 1.0 | 0.0 | 0 | 0 | not_applicable | 0.958 | 0.958 | good overlay, not an entry profile |
| four_c_thesis_break_earlier | hard 4C on explicit thesis break | 1 | 46.2 | 46.2 | -29.9 | -29.9 | 1.0 | 0.0 | 0 | 0 | not_applicable | not_applicable | not_applicable | validated only for HLB-like binary failure; no broad delta |

Best shadow profile: `stage2_actionable_medtech_consumable_plus_binary_guardrail`.

## 18. Before / After Backtest Comparison

| case_id | symbol | best_actual_trigger | baseline_selected_trigger | after_selected_trigger | baseline_entry_date | after_entry_date | baseline_entry_price | after_entry_price | baseline_MFE_90D_pct | after_MFE_90D_pct | baseline_MAE_90D_pct | after_MAE_90D_pct | baseline_MFE_180D_pct | after_MFE_180D_pct | baseline_MAE_180D_pct | after_MAE_180D_pct | return_improvement_90D_pct | risk_change_90D_pct | upside_capture_improvement_pct | reason_after_profile_selected |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| R7L3_C1 | 207940 | R7L3_C1_T2 | R7L3_C1_T4 | R7L3_C1_T2 | 2024-07-26 | 2024-07-02 | 915000 | 810000 | 21.6 | 37.4 | -8.1 | -3.2 | 32.1 | 49.3 | -8.1 | -3.2 | 15.8 | 4.9 | 25.4 | CDMO evidence de-risked before Green |
| R7L3_C2 | 196170 | R7L3_C2_T2 | R7L3_C2_T4 | R7L3_C2_T2 | 2024-06-07 | 2024-02-23 | 269000 | 131200 | 35.1 | 121.8 | -10.6 | -9.1 | 69.3 | 247.2 | -10.6 | -9.1 | 86.7 | 1.5 | 42.5 | platform optionality captured earlier with sizing guardrail |
| R7L3_C3 | 028300 | R7L3_C3_T1 | R7L3_C3_T3 | R7L3_C3_T1 | 2024-03-21 | 2024-01-26 | 112700 | 65200 | 14.5 | 97.9 | -58.3 | -3.4 | 14.5 | 97.9 | -58.3 | -27.9 | 83.4 | 54.9 | n/a | binary-risk cap prevents false Green |
| R7L3_C4 | 096530 | R7L3_C4_T1 | R7L3_C4_T4 | R7L3_C4_T1 | 2020-03-26 | 2020-02-13 | 114500 | 31450 | 22.5 | 349.6 | -28.3 | -2.5 | 181.4 | 924.5 | -28.3 | -2.5 | 327.1 | 25.8 | 67.7 | diagnostic demand shock was public before EPS report |
| R7L3_C5 | 214150 | R7L3_C5_T1 | R7L3_C5_T4 | R7L3_C5_T1 | 2024-05-09 | 2023-05-17 | 48500 | 26400 | 19.4 | 59.1 | -15.4 | -8.0 | 29.7 | 63.1 | -17.5 | -8.0 | 39.7 | 7.4 | 34.2 | installed-base/consumables/export leverage visible before obvious Green |

## 19. Score-Return Alignment Matrix

| alignment_label | trigger_count | avg_weighted_score_before | avg_weighted_score_after | avg_MFE_90D_pct | avg_MAE_90D_pct | verdict |
|---|---:|---:|---:|---:|---:|---|
| score_high_return_high | 4 | 76.3 | 79.5 | 142.0 | -5.7 | de-risked CDMO/platform/diagnostic/medtech early rows deserve promotion |
| score_high_return_low_false_positive | 1 | 71.0 | 44.0 | 14.5 | -58.3 | HLB late Yellow proves binary cap is necessary |
| score_mid_return_high_promote_candidate | 5 | 64.2 | 70.1 | 124.5 | -6.3 | Stage2/Yellow promote candidates validated, with guardrails |
| score_mid_return_low_watch_only | 5 | 61.0 | 61.0 | 2.9 | -38.0 | 4B rows are overlays, not entries |
| score_low_return_low_correct_reject | 1 | 20.0 | 10.0 | 46.2 | -29.9 | 4C row is a hard gate, not a long-entry calibration row |

## 20. Weight Sensitivity Table

| axis | baseline_weight_or_threshold | tested_weight_or_threshold | delta | affected_trigger_ids | affected_case_count | avg_MFE_90D_before | avg_MFE_90D_after | avg_MAE_90D_before | avg_MAE_90D_after | false_positive_count_before | false_positive_count_after | missed_structural_count_before | missed_structural_count_after | verdict |
|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| stage2_actionable_de_risked_evidence | 0 | 3 | +3 | R7L3_C1_T2|R7L3_C4_T1|R7L3_C5_T1 | 3 | 21.3 | 149.4 | -17.3 | -4.6 | 0 | 0 | 3 | 0 | accepted: MFE improved and MAE improved |
| medtech_consumable_export_operating_leverage | 0 | 2 | +2 | R7L3_C5_T1 | 1 | 19.4 | 59.1 | -15.4 | -8.0 | 0 | 0 | 1 | 0 | accepted but needs more medtech cases |
| platform_optional_customer_quality | 0 | 2 | +2 | R7L3_C2_T2 | 1 | 35.1 | 121.8 | -10.6 | -9.1 | 0 | 0 | 1 | 0 | accepted with volatility sizing guardrail |
| unresolved_regulatory_binary_risk | 0 | -4 | -4 | R7L3_C3_T3|R7L3_C3_T5 | 1 | 14.5 | 97.9 | -58.3 | -3.4 | 1 | 0 | 0 | 0 | accepted: blocks false Green |
| price_only_4b_as_full_4b | allow | reject | -3 | R7L3_C2_T5|R7L3_C3_T5 | 2 | 4.5 | 4.5 | -49.9 | -49.9 | 0 | 0 | 0 | 0 | accepted: price-only near peak is watch only |

## 21. Optimization Decision Log

```jsonl
{"row_type":"optimization_decision","decision_id":"R7L3_D1","hypothesis":"Promote Stage2-Actionable when de-risked operating evidence appears before Green.","tested_cases":["R7L3_C1","R7L3_C4","R7L3_C5"],"tested_trigger_ids":["R7L3_C1_T2_STAGE2_ACTIONABLE","R7L3_C4_T1_STAGE2_EUA_DEMAND","R7L3_C5_T1_STAGE2_ACTIONABLE"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_medtech_consumable_plus_binary_guardrail","backtest_result_summary":"Early de-risked rows raised avg MFE90 from late-Green proxy 21.3 to 149.4 while avg MAE90 improved from -17.3 to -4.6.","accepted_or_rejected":"accepted","delta_magnitude":"+3","why_not_larger_delta":"R7 still has small sample size and includes one extraordinary diagnostic shock.","risks":"Could over-promote one-off demand shocks or single-product medtech stories if revision/consumable evidence is weak.","next_validation_needed":"Add more medtech and medical-equipment cases with failed export/consumable theses."}
{"row_type":"optimization_decision","decision_id":"R7L3_D2","hypothesis":"Keep unresolved FDA/regulatory binary events below structural Green even when relative strength is strong.","tested_cases":["R7L3_C3"],"tested_trigger_ids":["R7L3_C3_T1_STAGE2_EVENT_PREMIUM","R7L3_C3_T3_STAGE3_YELLOW","R7L3_C3_T6_4C_TBREAK"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_medtech_consumable_plus_binary_guardrail","backtest_result_summary":"HLB late Yellow had MAE90 -58.3; early event premium had MFE90 97.9 but was not a structural Green row.","accepted_or_rejected":"accepted","delta_magnitude":"-4","why_not_larger_delta":"Only one hard binary-failure case in this loop.","risks":"May under-rank genuinely de-risked regulatory approvals after final approval closes.","next_validation_needed":"Find approval-success cases and compare post-approval Green versus pre-approval event premium."}
{"row_type":"optimization_decision","decision_id":"R7L3_D3","hypothesis":"Treat price-only near-peak 4B as watch overlay unless non-price 4B evidence exists.","tested_cases":["R7L3_C1","R7L3_C2","R7L3_C3","R7L3_C4","R7L3_C5"],"tested_trigger_ids":["R7L3_C1_T5_4B_WATCH","R7L3_C2_T5_4B_WATCH","R7L3_C3_T5_4B_WATCH","R7L3_C4_T5_4B_BLOWOFF","R7L3_C5_T5_4B_WATCH"],"baseline_profile":"baseline_current_proxy","selected_profile":"four_b_peak_timing_tuned","backtest_result_summary":"4B local/full proximities clustered near 0.94~0.973, but non-price evidence quality differed. Full 4B should not be assigned from price alone.","accepted_or_rejected":"accepted","delta_magnitude":"-3 for price_only_full_4B; +2 for non_price_4B_overlay","why_not_larger_delta":"4B rows are overlays and not entry rows; overfitting exit timing is risky.","risks":"May miss genuine distribution peaks when non-price evidence is delayed.","next_validation_needed":"Add cases with valuation blowoff plus revision slowdown versus price-only blowoff."}
```

## 22. Overfitting / Robustness Check

| check | result |
|---|---|
| usable case count | 5 |
| usable trigger count | 20 |
| representative entry trigger count | 15 |
| max_abs_delta allowed | +3 for repeated de-risked Stage2 route; +2 for single medtech axis; -4 for binary cap because the false-positive loss is extreme but still shadow-only |
| counterexample included | HLB regulatory-binary false-positive path |
| counterexample missing | medtech failed-export / failed-consumables counterexample still incomplete |
| conclusion | accepted as shadow-only; no production scoring change |

## 23. Cross-case Aggregate Metrics

Trigger aggregate uses only `calibration_usable=true` and `dedupe_for_aggregate=true`. 4B/4C overlay rows are not mixed into entry aggregates.

| trigger_type | usable_trigger_count | representative_trigger_count | avg_MFE_90D_pct | median_MFE_90D_pct | avg_MAE_90D_pct | median_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | below_entry_90D_rate | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Stage2 | 3 | 3 | 152.8 | 97.9 | -3.6 | -3.4 | 349.7 | -10.8 | 1.0 | not_applicable | not_applicable | not_applicable | great when demand/event evidence is real, but binary cases need cap |
| Stage2-Actionable | 3 | 3 | 106.1 | 59.1 | -6.8 | -8.0 | 153.2 | -6.8 | 1.0 | not_applicable | not_applicable | not_applicable | best early tier for de-risked CDMO/platform/medtech evidence |
| Stage3-Yellow | 4 | 4 | 82.5 | 33.5 | -24.1 | -17.7 | 211.0 | -25.3 | 1.0 | not_applicable | not_applicable | not_applicable | useful only with binary cap and volatility guardrail |
| Stage3-Green | 5 | 5 | 30.8 | 21.6 | -17.6 | -15.4 | 64.5 | -17.3 | 1.0 | 0.437 | not_applicable | not_applicable | generally late; cannot be the only entry tier |
| 4B-watch | 5 | 0 | 2.9 | 2.2 | -38.0 | -38.7 | 2.9 | -39.4 | 1.0 | not_applicable | 0.958 | 0.958 | valid overlay; not an entry trigger |
| 4C-thesis-break | 1 | 0 | 46.2 | 46.2 | -29.9 | -29.9 | 46.2 | -29.9 | 1.0 | not_applicable | not_applicable | not_applicable | hard gate validated only for HLB-like binary failure |

Profile aggregate:

| profile_id | case_count | selected_trigger_count | selected_representative_trigger_count | avg_MFE_90D_pct | median_MFE_90D_pct | avg_MAE_90D_pct | median_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | hit_rate_MFE90_gt_20pct | bad_entry_rate_MAE90_lt_minus_15pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| baseline_current_proxy | 5 | 5 | 5 | 26.6 | 21.6 | -23.8 | -15.4 | 64.2 | -22.9 | 0.8 | 0.6 | 0.2 | 4 | 4 | 0.437 | 0.958 | 0.958 | reference, too late |
| stage2_actionable_medtech_consumable_plus_binary_guardrail | 5 | 5 | 5 | 133.6 | 97.9 | -5.2 | -3.4 | 254.2 | -10.1 | 1.0 | 0.0 | 0.0 | 0 | 0 | 0.437 | 0.958 | 0.958 | best shadow profile |
| stage3_yellow_entry_relaxed | 5 | 5 | 5 | 81.4 | 51.4 | -21.3 | -16.5 | 183.4 | -22.3 | 0.8 | 0.6 | 0.2 | 1 | 1 | 0.437 | 0.958 | 0.958 | use with guardrail |
| four_b_peak_timing_tuned | 5 | 5 | 0 | 2.9 | 2.2 | -38.0 | -38.7 | 2.9 | -39.4 | 0.0 | 1.0 | 0.0 | 0 | 0 | not_applicable | 0.958 | 0.958 | overlay only |

## 24. Score-Price Alignment Verdict

R7 Loop 3 supports three shadow-only changes.

First, Stage2-Actionable deserves a stronger route in R7 when the early evidence is de-risked by customer quality, capacity/backlog, demand authorization, installed base, or consumables/export operating leverage. The Classys row is important because it shows the same mechanism outside pure biotech: a visible medtech operating-leverage story generated MFE90 59.1 with MAE90 -8.0 before the later Green spike.

Second, unresolved regulatory binary risk must subtract aggressively from Green eligibility. HLB’s late Yellow-like entry produced MAE90 -58.3. The lesson is not “never trade biotech event premiums”; it is that event premium is a different stage label from structural EPS rerating.

Third, 4B must be split into watch overlay versus full 4B. Price-only local peaks were useful as warning signs, but full 4B should require non-price evidence such as valuation blowoff plus revision slowdown, margin/backlog slowdown, dilution/CB/overhang, lockup pressure, or regulatory/legal block.

## 25. Validation Scope / Non-Validation Scope

this_round_validates:

```text
- de-risked Stage2-Actionable route for CDMO, diagnostic demand shock, and medtech consumable/export operating leverage
- platform optionality Stage2-Actionable only with volatility sizing guardrail
- unresolved FDA/regulatory binary risk cap below structural Green
- price-only 4B cannot be treated as full 4B without non-price evidence
- 4B local/full peak proximity split
- aggregate deduplication by representative rows and overlay separation
```

this_round_does_not_validate:

```text
- broad Green relaxation for all biotech stories
- broad hard 4C gate outside explicit regulatory failure
- adjusted-price revalidation for corporate-action contaminated 1Y/2Y windows
- medtech failed-export/failed-consumables counterexample sufficient for +5 delta
- live 2026 candidate scanning
```

No shadow delta is proposed for items in `this_round_does_not_validate`.

## 26. Shadow Weight Calibration

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_de_risked_evidence,0,3,+3,"CDMO/diagnostic/medtech Stage2 rows improved upside and reduced MAE versus Green-like baseline","avg MFE90 improved from 21.3 to 149.4 while avg MAE90 improved from -17.3 to -4.6","R7L3_C1_T2_STAGE2_ACTIONABLE|R7L3_C4_T1_STAGE2_EUA_DEMAND|R7L3_C5_T1_STAGE2_ACTIONABLE",3,"shadow-only; not production"
shadow_weight,medtech_consumable_export_operating_leverage,0,2,+2,"Classys showed that installed-base/consumables/export evidence can be actionable before Green","Classys MFE90 improved from Green proxy 19.4 to Stage2-Actionable 59.1 while MAE90 improved from -15.4 to -8.0","R7L3_C5_T1_STAGE2_ACTIONABLE",1,"shadow-only; needs more medtech cases before larger delta"
shadow_weight,platform_optional_customer_quality,0,2,+2,"Alteogen platform optionality produced large MFE but requires volatility sizing","MFE90 improved from Green 35.1 to Stage2-Actionable 121.8 while MAE90 improved from -10.6 to -9.1","R7L3_C2_T2_STAGE2_ACTIONABLE",1,"shadow-only; high volatility"
shadow_weight,unresolved_regulatory_binary_risk,0,-4,-4,"HLB late Yellow/Green-like row had MAE90 -58.3; price strength before final decision was not structural Green","false-positive count fell from 1 to 0 when binary cap applied","R7L3_C3_T3_STAGE3_YELLOW|R7L3_C3_T6_4C_TBREAK",1,"shadow-only; validate with approval-success cases"
shadow_weight,price_only_full_4b,0,-3,-3,"Price-only near-peak rows should remain watch overlays unless non-price 4B evidence exists","4B proximity was high, but price-only evidence quality differed across cases","R7L3_C2_T5_4B_WATCH|R7L3_C3_T5_4B_WATCH",2,"shadow-only; do not convert price-only local peak to hard exit"
```

## 27. Machine-Readable Rows

### 27.1 Case rows JSONL

```jsonl
{"row_type":"case","case_id":"R7L3_C1_SBIO_CDMO_BACKLOG","symbol":"207940","company_name":"삼성바이오로직스","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","case_type":"structural_success","primary_archetype":"CDMO_BACKLOG_CAPACITY_VISIBILITY","best_trigger":"R7L3_C1_T2_STAGE2_ACTIONABLE","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"Stage2-Actionable better than Green","price_source":"Songdaiki/stock-web","notes":"De-risked CDMO evidence route."}
{"row_type":"case","case_id":"R7L3_C2_ALTEOGEN_PLATFORM","symbol":"196170","company_name":"알테오젠","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","case_type":"stage2_promote_candidate_and_4b_watch","primary_archetype":"PLATFORM_TECH_LICENSING_OPTIONALITY","best_trigger":"R7L3_C2_T2_STAGE2_ACTIONABLE","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"Stage2-Actionable high-return but high-volatility","price_source":"Songdaiki/stock-web","notes":"Promote with sizing guardrail."}
{"row_type":"case","case_id":"R7L3_C3_HLB_BINARY","symbol":"028300","company_name":"HLB","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","case_type":"failed_rerating_4c_thesis_break","primary_archetype":"REGULATORY_BINARY_APPROVAL_RISK","best_trigger":"R7L3_C3_T1_STAGE2_EVENT_PREMIUM","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"Binary event premium; do not promote to Green","price_source":"Songdaiki/stock-web","notes":"Hard regulatory cap validated."}
{"row_type":"case","case_id":"R7L3_C4_SEEG_DIAGNOSTIC","symbol":"096530","company_name":"씨젠","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","case_type":"diagnostic_structural_success_then_4b","primary_archetype":"DIAGNOSTIC_DEMAND_SHOCK_EPS_RERATING","best_trigger":"R7L3_C4_T1_STAGE2_EUA_DEMAND","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"Stage2 demand shock captured rerating before EPS confirmation","price_source":"Songdaiki/stock-web","notes":"Exceptional demand-shock route; later 4B normalization."}
{"row_type":"case","case_id":"R7L3_C5_CLASSYS_MEDTECH","symbol":"214150","company_name":"클래시스","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","case_type":"medtech_stage2_promote_candidate","primary_archetype":"MEDTECH_CONSUMABLE_EXPORT_OPERATING_LEVERAGE","best_trigger":"R7L3_C5_T1_STAGE2_ACTIONABLE","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"Stage2 medtech operating leverage outperformed later Green","price_source":"Songdaiki/stock-web","notes":"New Loop 3 medtech validation case."}
```

### 27.2 Trigger rows JSONL

```jsonl
{"row_type":"trigger","trigger_id":"R7L3_C1_T1_STAGE2","case_id":"R7L3_C1_SBIO_CDMO_BACKLOG","symbol":"207940","company_name":"삼성바이오로직스","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","primary_archetype":"CDMO_BACKLOG_CAPACITY_VISIBILITY","trigger_type":"Stage2","trigger_date":"2024-01-22","evidence_available_at_that_date":"CDMO backlog/capacity and contract visibility beginning to support rerating.","evidence_source":"public contract/news/earnings context; revalidate exact disclosure timestamp in batch ingestion","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/207/207940/2024.csv","profile_path":"atlas/symbol_profiles/207/207940.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-22","entry_price":793000,"MFE_30D_pct":10.7,"MFE_90D_pct":11.0,"MFE_180D_pct":26.7,"MFE_1Y_pct":52.5,"MFE_2Y_pct":"unavailable","MAE_30D_pct":-3.2,"MAE_90D_pct":-3.2,"MAE_180D_pct":-9.1,"MAE_1Y_pct":-9.1,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-14","peak_price":1209000,"drawdown_after_peak_pct":-17.7,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"none","four_c_protection_label":"not_4C","trigger_outcome_label":"good_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R7L3_C1_2024-01-22_793000","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R7L3_C1_T2_STAGE2_ACTIONABLE","case_id":"R7L3_C1_SBIO_CDMO_BACKLOG","symbol":"207940","company_name":"삼성바이오로직스","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","primary_archetype":"CDMO_BACKLOG_CAPACITY_VISIBILITY","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-02","evidence_available_at_that_date":"CDMO backlog/capacity and customer-quality evidence plus relative strength.","evidence_source":"public contract/news/earnings context; revalidate exact disclosure timestamp in batch ingestion","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/207/207940/2024.csv","profile_path":"atlas/symbol_profiles/207/207940.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-02","entry_price":810000,"MFE_30D_pct":21.7,"MFE_90D_pct":37.4,"MFE_180D_pct":49.3,"MFE_1Y_pct":49.3,"MFE_2Y_pct":"unavailable","MAE_30D_pct":-3.2,"MAE_90D_pct":-3.2,"MAE_180D_pct":-3.2,"MAE_1Y_pct":-17.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-14","peak_price":1209000,"drawdown_after_peak_pct":-17.7,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"none","four_c_protection_label":"not_4C","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R7L3_C1_2024-07-02_810000","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R7L3_C1_T4_STAGE3_GREEN","case_id":"R7L3_C1_SBIO_CDMO_BACKLOG","symbol":"207940","company_name":"삼성바이오로직스","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","primary_archetype":"CDMO_BACKLOG_CAPACITY_VISIBILITY","trigger_type":"Stage3-Green","trigger_date":"2024-07-26","evidence_available_at_that_date":"Green-like confirmation after stronger public evidence and price RS.","evidence_source":"public contract/news/earnings context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/207/207940/2024.csv","profile_path":"atlas/symbol_profiles/207/207940.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-26","entry_price":915000,"MFE_30D_pct":9.8,"MFE_90D_pct":21.6,"MFE_180D_pct":32.1,"MFE_1Y_pct":32.1,"MFE_2Y_pct":"unavailable","MAE_30D_pct":-8.1,"MAE_90D_pct":-8.1,"MAE_180D_pct":-8.1,"MAE_1Y_pct":-17.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-14","peak_price":1209000,"drawdown_after_peak_pct":-17.7,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.37,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"none","four_c_protection_label":"not_4C","trigger_outcome_label":"late_but_valid_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R7L3_C1_2024-07-26_915000","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R7L3_C1_T5_4B_WATCH","case_id":"R7L3_C1_SBIO_CDMO_BACKLOG","symbol":"207940","company_name":"삼성바이오로직스","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","primary_archetype":"CDMO_BACKLOG_CAPACITY_VISIBILITY","trigger_type":"4B-watch","trigger_date":"2025-02-14","evidence_available_at_that_date":"Price near observed cycle peak with valuation/positioning watch.","evidence_source":"stock-web price path + valuation/positioning context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/207/207940/2025.csv","profile_path":"atlas/symbol_profiles/207/207940.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-02-14","entry_price":1180000,"MFE_30D_pct":0.8,"MFE_90D_pct":0.8,"MFE_180D_pct":0.8,"MFE_1Y_pct":"unavailable","MFE_2Y_pct":"unavailable","MAE_30D_pct":-16.9,"MAE_90D_pct":-16.9,"MAE_180D_pct":-17.7,"MAE_1Y_pct":"unavailable","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-14","peak_price":1209000,"drawdown_after_peak_pct":-17.7,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":0.96,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":"valuation_blowoff|positioning_overheat","four_c_protection_label":"not_4C","trigger_outcome_label":"4b_watch_near_peak","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R7L3_C1_2025-02-14_1180000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R7L3_C2_T2_STAGE2_ACTIONABLE","case_id":"R7L3_C2_ALTEOGEN_PLATFORM","symbol":"196170","company_name":"알테오젠","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","primary_archetype":"PLATFORM_TECH_LICENSING_OPTIONALITY","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","evidence_available_at_that_date":"Platform optionality / licensing signal plus strong relative strength.","evidence_source":"public licensing/news context; revalidate exact timestamp","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv","profile_path":"atlas/symbol_profiles/196/196170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-23","entry_price":131200,"MFE_30D_pct":71.9,"MFE_90D_pct":121.8,"MFE_180D_pct":247.2,"MFE_1Y_pct":247.2,"MFE_2Y_pct":"unavailable","MAE_30D_pct":-9.1,"MAE_90D_pct":-9.1,"MAE_180D_pct":-9.1,"MAE_1Y_pct":-38.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-11","peak_price":455500,"drawdown_after_peak_pct":-38.7,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"none","four_c_protection_label":"not_4C","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R7L3_C2_2024-02-23_131200","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R7L3_C2_T3_STAGE3_YELLOW","case_id":"R7L3_C2_ALTEOGEN_PLATFORM","symbol":"196170","company_name":"알테오젠","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","primary_archetype":"PLATFORM_TECH_LICENSING_OPTIONALITY","trigger_type":"Stage3-Yellow","trigger_date":"2024-03-05","evidence_available_at_that_date":"Platform optionality strengthened but margin/FCF bridge still incomplete.","evidence_source":"public licensing/news context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv","profile_path":"atlas/symbol_profiles/196/196170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-05","entry_price":192200,"MFE_30D_pct":17.3,"MFE_90D_pct":51.4,"MFE_180D_pct":137.0,"MFE_1Y_pct":137.0,"MFE_2Y_pct":"unavailable","MAE_30D_pct":-18.8,"MAE_90D_pct":-18.8,"MAE_180D_pct":-18.8,"MAE_1Y_pct":-38.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-11","peak_price":455500,"drawdown_after_peak_pct":-38.7,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"none","four_c_protection_label":"not_4C","trigger_outcome_label":"good_entry_high_volatility","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R7L3_C2_2024-03-05_192200","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R7L3_C2_T4_STAGE3_GREEN","case_id":"R7L3_C2_ALTEOGEN_PLATFORM","symbol":"196170","company_name":"알테오젠","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","primary_archetype":"PLATFORM_TECH_LICENSING_OPTIONALITY","trigger_type":"Stage3-Green","trigger_date":"2024-06-07","evidence_available_at_that_date":"Green-like confirmation after platform optionality was already repriced.","evidence_source":"public licensing/news context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv","profile_path":"atlas/symbol_profiles/196/196170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-07","entry_price":269000,"MFE_30D_pct":13.9,"MFE_90D_pct":35.1,"MFE_180D_pct":69.3,"MFE_1Y_pct":69.3,"MFE_2Y_pct":"unavailable","MAE_30D_pct":-10.6,"MAE_90D_pct":-10.6,"MAE_180D_pct":-10.6,"MAE_1Y_pct":-38.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-11","peak_price":455500,"drawdown_after_peak_pct":-38.7,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.52,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"none","four_c_protection_label":"not_4C","trigger_outcome_label":"late_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R7L3_C2_2024-06-07_269000","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R7L3_C2_T5_4B_WATCH","case_id":"R7L3_C2_ALTEOGEN_PLATFORM","symbol":"196170","company_name":"알테오젠","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","primary_archetype":"PLATFORM_TECH_LICENSING_OPTIONALITY","trigger_type":"4B-watch","trigger_date":"2024-11-11","evidence_available_at_that_date":"Price-only near observed cycle peak; needs non-price evidence for full 4B.","evidence_source":"stock-web price path + positioning context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv","profile_path":"atlas/symbol_profiles/196/196170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-11-11","entry_price":445500,"MFE_30D_pct":2.2,"MFE_90D_pct":2.2,"MFE_180D_pct":2.2,"MFE_1Y_pct":"unavailable","MFE_2Y_pct":"unavailable","MAE_30D_pct":-38.7,"MAE_90D_pct":-38.7,"MAE_180D_pct":-38.7,"MAE_1Y_pct":"unavailable","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-11","peak_price":455500,"drawdown_after_peak_pct":-38.7,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.97,"four_b_full_window_peak_proximity":0.97,"four_b_timing_verdict":"price_only_near_peak_watch_not_full_4B","four_b_evidence_type":"price_only|positioning_overheat","four_c_protection_label":"not_4C","trigger_outcome_label":"price_only_near_peak_watch","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R7L3_C2_2024-11-11_445500","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R7L3_C3_T1_STAGE2_EVENT_PREMIUM","case_id":"R7L3_C3_HLB_BINARY","symbol":"028300","company_name":"HLB","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","primary_archetype":"REGULATORY_BINARY_APPROVAL_RISK","trigger_type":"Stage2","trigger_date":"2024-01-26","evidence_available_at_that_date":"FDA approval expectation and event premium, but final binary risk unresolved.","evidence_source":"public FDA expectation/news context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-26","entry_price":65200,"MFE_30D_pct":27.3,"MFE_90D_pct":97.9,"MFE_180D_pct":97.9,"MFE_1Y_pct":97.9,"MFE_2Y_pct":"unavailable","MAE_30D_pct":-3.4,"MAE_90D_pct":-3.4,"MAE_180D_pct":-27.9,"MAE_1Y_pct":-29.9,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-26","peak_price":129000,"drawdown_after_peak_pct":-61.1,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"none","four_c_protection_label":"not_4C","trigger_outcome_label":"event_premium_binary_success_before_4c","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R7L3_C3_2024-01-26_65200","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R7L3_C3_T3_STAGE3_YELLOW","case_id":"R7L3_C3_HLB_BINARY","symbol":"028300","company_name":"HLB","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","primary_archetype":"REGULATORY_BINARY_APPROVAL_RISK","trigger_type":"Stage3-Yellow","trigger_date":"2024-03-21","evidence_available_at_that_date":"Price strength near FDA binary event, but final outcome unresolved.","evidence_source":"public FDA expectation/news context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-21","entry_price":112700,"MFE_30D_pct":14.5,"MFE_90D_pct":14.5,"MFE_180D_pct":14.5,"MFE_1Y_pct":14.5,"MFE_2Y_pct":"unavailable","MAE_30D_pct":-58.3,"MAE_90D_pct":-58.3,"MAE_180D_pct":-58.3,"MAE_1Y_pct":-61.1,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-26","peak_price":129000,"drawdown_after_peak_pct":-61.1,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"none","four_c_protection_label":"not_4C","trigger_outcome_label":"false_positive_score","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R7L3_C3_2024-03-21_112700","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R7L3_C3_T5_4B_WATCH","case_id":"R7L3_C3_HLB_BINARY","symbol":"028300","company_name":"HLB","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","primary_archetype":"REGULATORY_BINARY_APPROVAL_RISK","trigger_type":"4B-watch","trigger_date":"2024-03-26","evidence_available_at_that_date":"Price-only peak watch under unresolved FDA binary risk.","evidence_source":"stock-web price path + regulatory-binary context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-26","entry_price":120800,"MFE_30D_pct":6.8,"MFE_90D_pct":6.8,"MFE_180D_pct":6.8,"MFE_1Y_pct":"unavailable","MFE_2Y_pct":"unavailable","MAE_30D_pct":-61.1,"MAE_90D_pct":-61.1,"MAE_180D_pct":-61.1,"MAE_1Y_pct":"unavailable","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-26","peak_price":129000,"drawdown_after_peak_pct":-61.1,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.94,"four_b_timing_verdict":"good_peak_proximity_but_price_only_not_full_4B","four_b_evidence_type":"price_only|regulatory_binary_risk","four_c_protection_label":"not_4C","trigger_outcome_label":"4b_watch_near_peak","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R7L3_C3_2024-03-26_120800","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R7L3_C3_T6_4C_TBREAK","case_id":"R7L3_C3_HLB_BINARY","symbol":"028300","company_name":"HLB","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","primary_archetype":"REGULATORY_BINARY_APPROVAL_RISK","trigger_type":"4C-thesis-break","trigger_date":"2024-05-17","evidence_available_at_that_date":"Regulatory failure / CRL-style thesis break became public.","evidence_source":"public FDA/CRL news context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":67100,"MFE_30D_pct":10.0,"MFE_90D_pct":46.2,"MFE_180D_pct":46.2,"MFE_1Y_pct":"unavailable","MFE_2Y_pct":"unavailable","MAE_30D_pct":-29.9,"MAE_90D_pct":-29.9,"MAE_180D_pct":-29.9,"MAE_1Y_pct":"unavailable","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":98100,"drawdown_after_peak_pct":-29.9,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"none","four_c_protection_label":"hard_4c_late_but_still_protective","trigger_outcome_label":"hard_4c_late_but_still_protective","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R7L3_C3_2024-05-17_67100","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only"}
{"row_type":"trigger","trigger_id":"R7L3_C4_T1_STAGE2_EUA_DEMAND","case_id":"R7L3_C4_SEEG_DIAGNOSTIC","symbol":"096530","company_name":"씨젠","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","primary_archetype":"DIAGNOSTIC_DEMAND_SHOCK_EPS_RERATING","trigger_type":"Stage2","trigger_date":"2020-02-12","evidence_available_at_that_date":"COVID-19 diagnostic test authorization/demand shock became public.","evidence_source":"MFDS/EUA and pandemic-demand public news context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv","profile_path":"atlas/symbol_profiles/096/096530.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-02-13","entry_price":31450,"MFE_30D_pct":349.6,"MFE_90D_pct":349.6,"MFE_180D_pct":924.5,"MFE_1Y_pct":924.5,"MFE_2Y_pct":"contaminated_or_unavailable","MAE_30D_pct":-2.5,"MAE_90D_pct":-2.5,"MAE_180D_pct":-2.5,"MAE_1Y_pct":-3.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-08-10","peak_price":322200,"drawdown_after_peak_pct":-45.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"none","four_c_protection_label":"not_4C","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R7L3_C4_2020-02-13_31450","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R7L3_C4_T3_STAGE3_YELLOW","case_id":"R7L3_C4_SEEG_DIAGNOSTIC","symbol":"096530","company_name":"씨젠","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","primary_archetype":"DIAGNOSTIC_DEMAND_SHOCK_EPS_RERATING","trigger_type":"Stage3-Yellow","trigger_date":"2020-03-02","evidence_available_at_that_date":"COVID-19 diagnostic demand strength visible but EPS report not yet complete.","evidence_source":"public pandemic-demand news context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv","profile_path":"atlas/symbol_profiles/096/096530.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-03-02","entry_price":40400,"MFE_30D_pct":249.8,"MFE_90D_pct":249.8,"MFE_180D_pct":697.5,"MFE_1Y_pct":697.5,"MFE_2Y_pct":"contaminated_or_unavailable","MAE_30D_pct":-9.9,"MAE_90D_pct":-9.9,"MAE_180D_pct":-9.9,"MAE_1Y_pct":-43.6,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-08-10","peak_price":322200,"drawdown_after_peak_pct":-45.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"none","four_c_protection_label":"not_4C","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R7L3_C4_2020-03-02_40400","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R7L3_C4_T4_STAGE3_GREEN","case_id":"R7L3_C4_SEEG_DIAGNOSTIC","symbol":"096530","company_name":"씨젠","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","primary_archetype":"DIAGNOSTIC_DEMAND_SHOCK_EPS_RERATING","trigger_type":"Stage3-Green","trigger_date":"2020-03-26","evidence_available_at_that_date":"Green-like confirmation after demand shock and visible price response.","evidence_source":"public pandemic-demand news context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv","profile_path":"atlas/symbol_profiles/096/096530.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-03-26","entry_price":114500,"MFE_30D_pct":22.5,"MFE_90D_pct":22.5,"MFE_180D_pct":181.4,"MFE_1Y_pct":181.4,"MFE_2Y_pct":"contaminated_or_unavailable","MAE_30D_pct":-28.3,"MAE_90D_pct":-28.3,"MAE_180D_pct":-28.3,"MAE_1Y_pct":-43.6,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-08-10","peak_price":322200,"drawdown_after_peak_pct":-45.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.286,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"none","four_c_protection_label":"not_4C","trigger_outcome_label":"late_but_still_good_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R7L3_C4_2020-03-26_114500","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R7L3_C4_T5_4B_BLOWOFF","case_id":"R7L3_C4_SEEG_DIAGNOSTIC","symbol":"096530","company_name":"씨젠","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","primary_archetype":"DIAGNOSTIC_DEMAND_SHOCK_EPS_RERATING","trigger_type":"4B-watch","trigger_date":"2020-08-10","evidence_available_at_that_date":"Observed blowoff peak with demand-normalization/positioning risk.","evidence_source":"stock-web price path + demand normalization context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv","profile_path":"atlas/symbol_profiles/096/096530.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-08-10","entry_price":310700,"MFE_30D_pct":3.4,"MFE_90D_pct":3.4,"MFE_180D_pct":3.4,"MFE_1Y_pct":"contaminated_or_unavailable","MFE_2Y_pct":"contaminated_or_unavailable","MAE_30D_pct":-31.3,"MAE_90D_pct":-43.6,"MAE_180D_pct":-43.6,"MAE_1Y_pct":"contaminated_or_unavailable","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-08-10","peak_price":322200,"drawdown_after_peak_pct":-45.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":0.96,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":"valuation_blowoff|positioning_overheat|revision_slowdown","four_c_protection_label":"not_4C","trigger_outcome_label":"4B_watch_success","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_for_core; later contaminated_or_unavailable","same_entry_group_id":"R7L3_C4_2020-08-10_310700","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R7L3_C5_T1_STAGE2_ACTIONABLE","case_id":"R7L3_C5_CLASSYS_MEDTECH","symbol":"214150","company_name":"클래시스","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","primary_archetype":"MEDTECH_CONSUMABLE_EXPORT_OPERATING_LEVERAGE","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-17","evidence_available_at_that_date":"Medtech installed-base/consumables/export operating leverage and early earnings momentum.","evidence_source":"public earnings/report/news context; exact report timestamp needs batch revalidation","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv","profile_path":"atlas/symbol_profiles/214/214150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-17","entry_price":26400,"MFE_30D_pct":34.3,"MFE_90D_pct":59.1,"MFE_180D_pct":63.1,"MFE_1Y_pct":63.1,"MFE_2Y_pct":"unavailable","MAE_30D_pct":-8.0,"MAE_90D_pct":-8.0,"MAE_180D_pct":-8.0,"MAE_1Y_pct":-8.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-21","peak_price":62900,"drawdown_after_peak_pct":-36.4,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"none","four_c_protection_label":"not_4C","trigger_outcome_label":"excellent_medtech_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D; 2017 corporate-action candidate outside selected window","same_entry_group_id":"R7L3_C5_2023-05-17_26400","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R7L3_C5_T3_STAGE3_YELLOW","case_id":"R7L3_C5_CLASSYS_MEDTECH","symbol":"214150","company_name":"클래시스","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","primary_archetype":"MEDTECH_CONSUMABLE_EXPORT_OPERATING_LEVERAGE","trigger_type":"Stage3-Yellow","trigger_date":"2023-08-21","evidence_available_at_that_date":"Continued medtech operating leverage and relative strength, but Green confirmation not yet complete.","evidence_source":"public earnings/report/news context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv","profile_path":"atlas/symbol_profiles/214/214150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-08-21","entry_price":37500,"MFE_30D_pct":12.0,"MFE_90D_pct":14.8,"MFE_180D_pct":32.8,"MFE_1Y_pct":67.7,"MFE_2Y_pct":"unavailable","MAE_30D_pct":-16.5,"MAE_90D_pct":-16.5,"MAE_180D_pct":-22.9,"MAE_1Y_pct":-22.9,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-21","peak_price":62900,"drawdown_after_peak_pct":-36.4,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"none","four_c_protection_label":"not_4C","trigger_outcome_label":"acceptable_but_volatile_yellow","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R7L3_C5_2023-08-21_37500","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R7L3_C5_T4_STAGE3_GREEN","case_id":"R7L3_C5_CLASSYS_MEDTECH","symbol":"214150","company_name":"클래시스","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","primary_archetype":"MEDTECH_CONSUMABLE_EXPORT_OPERATING_LEVERAGE","trigger_type":"Stage3-Green","trigger_date":"2024-05-09","evidence_available_at_that_date":"Green-like confirmation after visible 2024 earnings/price breakout.","evidence_source":"public earnings/report/news context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214150/2024.csv","profile_path":"atlas/symbol_profiles/214/214150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-09","entry_price":48500,"MFE_30D_pct":17.3,"MFE_90D_pct":19.4,"MFE_180D_pct":29.7,"MFE_1Y_pct":29.7,"MFE_2Y_pct":"unavailable","MAE_30D_pct":-5.9,"MAE_90D_pct":-15.4,"MAE_180D_pct":-17.5,"MAE_1Y_pct":-17.5,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-21","peak_price":62900,"drawdown_after_peak_pct":-36.4,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.605,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"none","four_c_protection_label":"not_4C","trigger_outcome_label":"late_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R7L3_C5_2024-05-09_48500","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R7L3_C5_T5_4B_WATCH","case_id":"R7L3_C5_CLASSYS_MEDTECH","symbol":"214150","company_name":"클래시스","round":"R7","loop":"3","sector":"바이오·헬스케어·의료기기","primary_archetype":"MEDTECH_CONSUMABLE_EXPORT_OPERATING_LEVERAGE","trigger_type":"4B-watch","trigger_date":"2024-10-21","evidence_available_at_that_date":"Observed full-window peak with valuation/positioning/growth-normalization watch.","evidence_source":"stock-web price path + valuation/positioning context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214150/2024.csv","profile_path":"atlas/symbol_profiles/214/214150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-21","entry_price":61900,"MFE_30D_pct":1.6,"MFE_90D_pct":1.6,"MFE_180D_pct":1.6,"MFE_1Y_pct":"unavailable","MFE_2Y_pct":"unavailable","MAE_30D_pct":-35.4,"MAE_90D_pct":-35.4,"MAE_180D_pct":-35.4,"MAE_1Y_pct":"unavailable","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-21","peak_price":62900,"drawdown_after_peak_pct":-36.4,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.973,"four_b_full_window_peak_proximity":0.973,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":"valuation_blowoff|positioning_overheat|growth_normalization_watch","four_c_protection_label":"not_4C","trigger_outcome_label":"4b_watch_near_peak","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R7L3_C5_2024-10-21_61900","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
```

### 27.3 Score simulation rows JSONL

The following rows include canonical component keys. Supplemental `capacity_or_shipment_score`, `fcf_conversion_score`, `positioning_overheat_score`, and `thesis_break_score` are included because R7 needs operating-leverage and risk overlays.

```jsonl
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R7L3_C1_SBIO_CDMO_BACKLOG","trigger_id":"R7L3_C1_T2_STAGE2_ACTIONABLE","symbol":"207940","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":8,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":7,"fcf_conversion_score":6,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":73.6,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":8,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":9,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":7,"fcf_conversion_score":6,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":75.9,"stage_label_after":"Stage2-Actionable","changed_components":["relative_strength_score","customer_quality_score"],"component_delta_explanation":"De-risked CDMO evidence receives early-evidence credit.","selected_by_profile":true,"MFE_90D_pct":37.4,"MAE_90D_pct":-3.2,"score_return_alignment_label":"score_mid_return_high_promote_candidate"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R7L3_C2_ALTEOGEN_PLATFORM","trigger_id":"R7L3_C2_T2_STAGE2_ACTIONABLE","symbol":"196170","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":3,"margin_bridge_score":1,"revision_score":4,"relative_strength_score":9,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":0,"fcf_conversion_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":68.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":6,"backlog_visibility_score":3,"margin_bridge_score":1,"revision_score":4,"relative_strength_score":9,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":0,"fcf_conversion_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":72.0,"stage_label_after":"Stage2-Actionable_with_volatility_guardrail","changed_components":["contract_score","customer_quality_score"],"component_delta_explanation":"Platform optionality receives customer-quality credit but keeps execution-risk penalty.","selected_by_profile":true,"MFE_90D_pct":121.8,"MAE_90D_pct":-9.1,"score_return_alignment_label":"score_high_return_high"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R7L3_C3_HLB_BINARY","trigger_id":"R7L3_C3_T3_STAGE3_YELLOW","symbol":"028300","trigger_type":"Stage3-Yellow","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":9,"customer_quality_score":4,"policy_or_regulatory_score":7,"valuation_repricing_score":8,"execution_risk_score":9,"legal_or_contract_risk_score":9,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":0,"fcf_conversion_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":71.0,"stage_label_before":"Stage3-Yellow_candidate","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":9,"customer_quality_score":4,"policy_or_regulatory_score":7,"valuation_repricing_score":8,"execution_risk_score":10,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":0,"fcf_conversion_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":44.0,"stage_label_after":"Stage2_event_premium_not_Green","changed_components":["execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Unresolved FDA binary risk caps Green eligibility despite strong price.","selected_by_profile":false,"MFE_90D_pct":14.5,"MAE_90D_pct":-58.3,"score_return_alignment_label":"score_high_return_low_false_positive"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R7L3_C4_SEEG_DIAGNOSTIC","trigger_id":"R7L3_C4_T1_STAGE2_EUA_DEMAND","symbol":"096530","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":9,"customer_quality_score":6,"policy_or_regulatory_score":8,"valuation_repricing_score":8,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"capacity_or_shipment_score":8,"fcf_conversion_score":5,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":70.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":3,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":10,"customer_quality_score":6,"policy_or_regulatory_score":9,"valuation_repricing_score":8,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"capacity_or_shipment_score":9,"fcf_conversion_score":6,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":82.0,"stage_label_after":"Stage2-Actionable_demand_shock","changed_components":["policy_or_regulatory_score","capacity_or_shipment_score","relative_strength_score"],"component_delta_explanation":"Concrete emergency-use demand shock gets early Stage2 credit before reported EPS.","selected_by_profile":true,"MFE_90D_pct":349.6,"MAE_90D_pct":-2.5,"score_return_alignment_label":"score_high_return_high"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R7L3_C5_CLASSYS_MEDTECH","trigger_id":"R7L3_C5_T1_STAGE2_ACTIONABLE","symbol":"214150","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":6,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":7,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":7,"fcf_conversion_score":7,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":67.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":7,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":8,"fcf_conversion_score":8,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":76.0,"stage_label_after":"Stage2-Actionable_medtech_consumable","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","capacity_or_shipment_score","fcf_conversion_score"],"component_delta_explanation":"Medtech installed-base/consumables/export leverage receives early-evidence credit.","selected_by_profile":true,"MFE_90D_pct":59.1,"MAE_90D_pct":-8.0,"score_return_alignment_label":"score_mid_return_high_promote_candidate"}
```

### 27.4 Profile comparison rows CSV

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,avg_MAE_90D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,5,5,5,26.6,-23.8,0.8,0.6,0.2,4,4,0.958,0.958,"reference; late and false-positive-prone"
profile_comparison,stage2_actionable_medtech_consumable_plus_binary_guardrail,5,5,5,133.6,-5.2,1.0,0.0,0.0,0,0,0.958,0.958,"best shadow profile; improves upside capture and drawdown control"
profile_comparison,stage3_yellow_entry_relaxed,5,5,5,81.4,-21.3,0.8,0.6,0.2,1,1,0.958,0.958,"useful but requires binary risk cap"
profile_comparison,green_confirmation_timing_relaxed,5,5,5,58.4,-19.0,0.8,0.4,0.2,1,1,0.958,0.958,"less effective than true Stage2-actionable route"
profile_comparison,four_b_peak_timing_tuned,5,5,0,2.9,-38.0,0.0,1.0,0.0,0,0,0.958,0.958,"overlay only, not entry profile"
profile_comparison,four_c_thesis_break_earlier,1,1,0,46.2,-29.9,1.0,1.0,0.0,0,0,,,"validated only for explicit regulatory failure"
```

### 27.5 Aggregate metric rows CSV

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,3,3,152.8,97.9,-3.6,-3.4,,,,"Stage2 works when evidence is concrete, but HLB must remain event-premium capped"
aggregate_metric,Stage2-Actionable,3,3,106.1,59.1,-6.8,-8.0,,,,"Best early tier for de-risked CDMO/platform/medtech evidence"
aggregate_metric,Stage3-Yellow,4,4,82.5,33.5,-24.1,-17.7,,,,"Only useful with binary/volatility guardrails"
aggregate_metric,Stage3-Green,5,5,30.8,21.6,-17.6,-15.4,0.437,,,"Profitable in some cases but frequently late"
aggregate_metric,4B-watch,5,0,2.9,2.2,-38.0,-38.7,,0.958,0.958,"Valid overlay; no entry aggregation"
aggregate_metric,4C-thesis-break,1,0,46.2,46.2,-29.9,-29.9,,,,"Hard gate validated only for HLB-like explicit failure"
```

### 27.6 Narrative-only rows JSONL

```jsonl
{"row_type":"narrative_only","case_id":"R7L3_MEDTECH_FAILED_COUNTEREXAMPLE_SEARCH","symbol":"unavailable","reason":"medtech failed-export or failed-consumables counterexample not sufficiently validated in this loop; do not assign +5 delta to medtech axis","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
{"row_type":"narrative_only","case_id":"R7L3_HARD_4C_GENERALIZATION_BLOCKED","symbol":"multiple","reason":"only HLB provides hard 4C in this loop; no broad 4C hard-gate delta outside explicit regulatory failure","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
current_round = R7
current_loop = 3
next_round = R8
next_loop = 3
next_sector = 플랫폼·콘텐츠·SW·보안
carry_forward_validated_rules = stage2_actionable_de_risked_evidence, medtech_consumable_export_operating_leverage, unresolved_regulatory_binary_risk_cap, price_only_4b_watch_not_full_4b
carry_forward_needs_validation = medtech_failed_counterexample, approval_success_binary_counterexample, adjusted_price_revalidation_for_corporate_action_windows
```

## 30. Source Notes

- Stock-web manifest and schema read from `Songdaiki/stock-web` main branch: `atlas/manifest.json`, `atlas/schema.json`.
- Classys profile read from `atlas/symbol_profiles/214/214150.json`: selected windows are far after the 2017 corporate-action candidate.
- Classys price rows used: `atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv` and `atlas/ohlcv_tradable_by_symbol_year/214/214150/2024.csv`.
- Existing R7 calibration anchors retained for Samsung Biologics, Alteogen, HLB, and Seegene using the same stock-web OHLC route and v11 field model.
- Evidence source confidence is intentionally separated from price validation. Exact public disclosure timestamps should be revalidated during coding-agent ingestion; this MD does not patch production scoring.
