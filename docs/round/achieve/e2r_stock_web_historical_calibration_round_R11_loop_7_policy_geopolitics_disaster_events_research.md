# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata

| field | value |
| --- | --- |
| research_session | historical_calibration_after_stock_web_ohlc_breakthrough |
| round | R11 |
| loop | 6 |
| sector | 정책·지정학·재난·이벤트 |
| output_mode | one_standalone_markdown_file |
| stock_agent_repo_accessed | false |
| production_scoring_changed | false |
| shadow_weight_only | true |
| price_source | Songdaiki/stock-web |
| stock_web_manifest_max_date | 2026-02-20 |
| generated_artifact | e2r_stock_web_historical_calibration_round_R11_loop_6_policy_geopolitics_disaster_events_research.md |
| calibration_usable_case_count | 5 |
| calibration_usable_trigger_count | 17 |
| score_profile_test_count | 6 |
| shadow_weight_delta_count | 5 |
| best_shadow_profile | r11_stage2_event_policy_early_guard |

## 1. Round Scope

R11 loop 6은 정책·지정학·재난·이벤트 라운드다. 이 파일은 loop 5에서 이미 stock-web OHLC 검증이 끝난 방산 수출, 경영권 프리미엄, 정책 법안, 가격-only blowoff trigger set을 유지하되, v11 요구사항인 same_entry_group_id/dedupe, raw component score breakdown, 4B local/full-window split, Validation Scope/Non-Validation Scope, shadow-only handoff reject 규칙을 더 닫는 historical calibration pass다. 핵심은 “최종 확인까지 기다린 Green이 안전했는가, 아니면 시장이 이미 Stage2에서 리레이팅 엔진을 켰는가”를 stock-web 1D OHLC로 검증하는 것이다.

이번 라운드는 방산 수출, 경영권 프리미엄, 정책 법안, 가격-only blowoff라는 네 개의 이벤트 축을 비교한다. 이벤트주는 공장 설비가 아니라 뉴스 플로우가 시동키다. 그래서 같은 MFE라도 공개 evidence가 있는 상승과 증거 없는 가격-only 상승을 분리해야 한다.

## 2. Stock-Web OHLC Input / Price Source Validation

stock-web manifest 기준은 `FinanceData/marcap`, `tradable_raw`, `raw_unadjusted_marcap`이다. Manifest max_date는 `2026-02-20`, calibration shard root는 `atlas/ohlcv_tradable_by_symbol_year`다. Schema의 tradable shard 컬럼은 `d/o/h/l/c/v/a/mc/s/m`이며, 본 파일의 MFE/MAE는 모두 entry_date 종가 대비 stock-web high/low로 계산된 percentage unit이다. Current-session price-source validation fields used in this artifact: `source_name=FinanceData/marcap`, `source_repo_url=https://github.com/FinanceData/marcap`, `min_date=1995-05-02`, `max_date=2026-02-20`, `tradable_row_count=14,354,401`, `raw_row_count=15,214,118`, `symbol_count=5,414`, `active_like_symbol_count=2,868`, `inactive_or_delisted_like_symbol_count=2,546`, `markets=KONEX/KOSDAQ/KOSDAQ GLOBAL/KOSPI`, `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`, `raw_shard_root=atlas/ohlcv_raw_by_symbol_year`, `schema_path=atlas/schema.json`, `universe_path=atlas/universe/all_symbols.csv`.

Source paths used:

- manifest: `atlas/manifest.json`
- schema: `atlas/schema.json`
- universe: `atlas/universe/all_symbols.csv`
- OHLC shards: listed per trigger in section 27 JSONL rows
- symbol profiles: listed per trigger in section 27 JSONL rows

## 3. Historical Eligibility Gate

| condition | status |
| --- | --- |
| trigger_date is historical | pass |
| entry_date exists in stock-web tradable shard | pass for all calibration rows |
| >=180 forward tradable days available | pass for all usable trigger rows |
| corporate-action contamination in 180D window | none in selected 2022~2023 windows |
| price basis | tradable_raw / raw_unadjusted_marcap |
| relative return availability | unavailable; core calibration retained |

## 4. Canonical Archetypes Tested

| archetype | case ids | mechanism |
| --- | --- | --- |
| GEOPOLITICAL_DEFENSE_EXPORT_POLICY | R11L6_C01 / R11L6_C02 | 전쟁·안보 수요가 방산 수출 framework→executive contract→실적 기대 경로로 바뀌는 구조 |
| CONTROL_PREMIUM_GOVERNANCE_EVENT | R11L6_C03 | 경영권 경쟁이 명시적 tender price로 event-premium cap을 만들고, 종료 뉴스가 thesis break가 되는 구조 |
| PRICE_ONLY_MANIPULATION_OR_FORCED_LIQUIDATION | R11L6_C04 | 증거 없는 장기 가격상승이 4B price-only watch로는 유용하지만 positive score 학습에는 위험한 구조 |
| IRA_RENEWABLE_POLICY_RERATING | R11L6_C05 | 정책 법안 경로가 final signing 이전에 rerating을 먼저 시작하는 구조 |

## 5. Case Selection Summary

| case_id | symbol | company | case_type | best_trigger | summary |
| --- | --- | --- | --- | --- | --- |
| R11L6_C01 | 012450 | 한화에어로스페이스 | structural_success | R11L6_C01_T1 | Defense export framework caught rerating earlier than executive contract Green. |
| R11L6_C02 | 064350 | 현대로템 | Stage2_promote_candidate | R11L6_C02_T1 | K2/Poland framework trigger outperformed later momentum confirmation. |
| R11L6_C03 | 041510 | 에스엠 | event_premium_success_then_4B_4C | R11L6_C03_T1 | Control-premium Stage2 worked; tender cap became 4B, not fresh entry. |
| R11L6_C04 | 004690 | 삼천리 | price_moved_without_evidence_4C_late | R11L6_C04_T0 | Extreme OHLC blowoff without accepted public evidence; useful as price-only rejection. |
| R11L6_C05 | 112610 | 씨에스윈드 | policy_rerating_success | R11L6_C05_T1 | IRA path trigger beat final law-signing confirmation. |

## 6. Evidence Source Map

Evidence source and price source are intentionally separated.

- Defense export cases use the 2022 Korea–Poland defense package framework / executive-contract path for K9, K2, and related systems. The calibration question is whether July framework evidence was enough before August executive contracts.
- SM uses public governance/tender-offer evidence: Kakao strategic stake, HYBE stake/tender, Kakao 150,000-won tender cap, and HYBE majority-control withdrawal.
- CS Wind uses the US Inflation Reduction Act policy path. The July policy-path trigger is compared with the August 16, 2022 law-signing confirmation.
- Samchully is deliberately not accepted as an evidence-backed Stage2/Stage3 case. It is used as a price-only blowoff / forced-liquidation / 4C-late guardrail.

## 7. Price Data Source Map

| symbol | company | OHLC shards used | profile path | corporate-action status |
| --- | --- | --- | --- | --- |
| 012450 | 한화에어로스페이스 | atlas/ohlcv_tradable_by_symbol_year/012/012450/2022.csv; 2023.csv; 2024.csv | atlas/symbol_profiles/012/012450.json | selected windows clean_180D |
| 064350 | 현대로템 | atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv; 2023.csv; 2024.csv | atlas/symbol_profiles/064/064350.json | selected windows clean_180D |
| 041510 | 에스엠 | atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv | atlas/symbol_profiles/041/041510.json | selected windows clean_180D |
| 004690 | 삼천리 | atlas/ohlcv_tradable_by_symbol_year/004/004690/2022.csv; 2023.csv | atlas/symbol_profiles/004/004690.json | selected windows clean_180D |
| 112610 | 씨에스윈드 | atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv; 2023.csv | atlas/symbol_profiles/112/112610.json | selected windows clean_180D |

## 8. Case-by-Case Trigger Grid

| case | trigger_id | type | trigger_date | entry_date | entry_price | evidence | outcome |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R11L6_C01 | R11L6_C01_T1 | Stage2 | 2022-07-27 | 2022-07-27 | 52200 | Poland/Korea defense framework agreement for K9/K2/FA-50 family; public defense-export policy shock. | excellent_entry |
| R11L6_C01 | R11L6_C01_T2 | Stage2-Actionable | 2022-07-27 | 2022-07-27 | 52200 | Same framework event, upgraded because defense-export size + immediate relative strength closed the early-evidence gate. | excellent_entry |
| R11L6_C01 | R11L6_C01_T4 | Stage3-Green | 2022-08-26 | 2022-08-26 | 78400 | First executive K9 contract; contract confirmation closed, but entry came after substantial rerating and before a deep v | late_entry |
| R11L6_C01 | R11L6_C01_T5 | 4B | 2023-06-20 | 2023-06-20 | 142500 | Defense-export rerating blowoff/positioning watch after full cycle extension. | 4B_watch_success |
| R11L6_C02 | R11L6_C02_T1 | Stage2 | 2022-07-22 | 2022-07-22 | 24400 | K2 tank / Poland framework signal enters public tape; material geopolitical defense-export demand but contract details s | good_entry |
| R11L6_C02 | R11L6_C02_T2 | Stage2-Actionable | 2022-08-24 | 2022-08-24 | 31400 | Post-framework momentum break; not enough incremental non-price evidence versus the July framework. | late_event_premium |
| R11L6_C02 | R11L6_C02_T5 | 4B | 2023-06-20 | 2023-06-20 | 39350 | Local/full-window price proximity after defense rerating; watch overlay, not thesis cancellation. | 4B_watch_success |
| R11L6_C03 | R11L6_C03_T1 | Stage2 | 2023-02-07 | 2023-02-07 | 90100 | Kakao strategic stake / SM governance battle becomes public event premium; not yet final control auction. | excellent_event_entry |
| R11L6_C03 | R11L6_C03_T3 | Stage3-Yellow | 2023-02-10 | 2023-02-10 | 114700 | HYBE 14.8% stake/tender offer increases control-premium probability, but overhang and bid ceiling risk also rise. | event_premium_good_but_risky |
| R11L6_C03 | R11L6_C03_T5 | 4B | 2023-03-07 | 2023-03-07 | 149700 | Kakao 150,000-won tender offer establishes explicit event-premium cap; strong 4B overlay rather than fresh entry. | 4B_watch_success |
| R11L6_C03 | R11L6_C03_T6 | 4C | 2023-03-13 | 2023-03-13 | 113100 | HYBE abandons majority-control pursuit; control-premium thesis breaks after peak but before full low. | thesis_break |
| R11L6_C04 | R11L6_C04_T0 | Price-only no-evidence run | 2022-05-13 | 2022-05-13 | 133000 | No evidence-backed EPS/OP/policy trigger found in this pass; OHLC shows long low-liquidity rerating before 2023 crash. | price_moved_without_evidence |
| R11L6_C04 | R11L6_C04_T5 | 4B | 2023-02-28 | 2023-02-28 | 513000 | Peak-proximity price-only 4B. No non-price 4B evidence available at the date; should not be treated as full evidence-bas | price_only_4B_watch |
| R11L6_C04 | R11L6_C04_T6 | 4C | 2023-04-24 | 2023-04-24 | 348500 | Visible forced-liquidation/crash trigger; hard 4C appears after peak and after first large limit-down. | thesis_break_late |
| R11L6_C05 | R11L6_C05_T1 | Stage2 | 2022-07-28 | 2022-07-28 | 52800 | US climate bill / IRA path re-enters public policy tape; wind tower domestic-content and clean-energy tax-credit optiona | excellent_policy_entry |
| R11L6_C05 | R11L6_C05_T2 | Stage2-Actionable | 2022-08-16 | 2022-08-16 | 65100 | IRA signed into law. Confirmation improves policy durability but loses much of the first rerating leg. | good_but_later_policy_confirmation |
| R11L6_C05 | R11L6_C05_T5 | 4B | 2023-06-21 | 2023-06-21 | 87200 | Policy rerating high after repeated momentum; 4B watch for policy-benefit saturation and revision fatigue. | 4B_watch_success |

## 9. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MFE90 | MFE180 | MFE1Y | MFE2Y | MAE30 | MAE90 | MAE180 | peak_date | peak_price | drawdown_after_peak | 4B local/full | dedupe | aggregate_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R11L6_C01_T1 | 2022-07-27 @ 52200 | 66.28 | 66.28 | 130.08 | 189.27 | 532.18 | -4.02 | -4.02 | -4.02 | 2024-07-30 | 330000 | -33.0 | None/None | True | representative |
| R11L6_C01_T2 | 2022-07-27 @ 52200 | 66.28 | 66.28 | 130.08 | 189.27 | 532.18 | -4.02 | -4.02 | -4.02 | 2024-07-30 | 330000 | -33.0 | None/None | False | label_comparison_only |
| R11L6_C01_T4 | 2022-08-26 @ 78400 | 10.71 | 10.71 | 53.19 | 92.6 | 320.92 | -32.91 | -32.91 | -32.91 | 2024-07-30 | 330000 | -33.0 | None/None | True | representative |
| R11L6_C01_T5 | 2023-06-20 @ 142500 | 5.96 | 5.96 | 131.58 | 131.58 | unavailable_forward_504_not_recomputed | -19.02 | -19.02 | -19.02 | 2024-07-30 | 330000 | -33.0 | 0.91/0.91 | False | 4B_overlay_only |
| R11L6_C02_T1 | 2022-07-22 @ 24400 | 34.63 | 34.63 | 54.92 | 64.96 | 110.25 | -14.75 | -14.75 | -14.75 | 2024-07-31 | 51300 | -22.0 | None/None | True | representative |
| R11L6_C02_T2 | 2022-08-24 @ 31400 | 4.62 | 4.62 | 20.38 | 28.18 | 63.38 | -22.29 | -26.59 | -26.59 | 2024-07-31 | 51300 | -22.0 | None/None | True | representative |
| R11L6_C02_T5 | 2023-06-20 @ 39350 | 2.29 | 2.29 | 30.37 | 30.37 | unavailable_forward_504_not_recomputed | -18.17 | -22.62 | -35.32 | 2024-07-31 | 51300 | -22.0 | 0.94/0.94 | False | 4B_overlay_only |
| R11L6_C03_T1 | 2023-02-07 @ 90100 | 78.91 | 78.91 | 78.91 | 78.91 | 78.91 | -4.88 | -4.88 | -4.88 | 2023-03-08 | 161200 | -45.66 | None/None | True | representative |
| R11L6_C03_T3 | 2023-02-10 @ 114700 | 40.54 | 40.54 | 40.54 | 40.54 | 40.54 | -21.1 | -23.63 | -23.63 | 2023-03-08 | 161200 | -45.66 | None/None | True | representative |
| R11L6_C03_T5 | 2023-03-07 @ 149700 | 7.68 | 7.68 | 7.68 | 7.68 | 7.68 | -41.48 | -41.48 | -41.48 | 2023-03-08 | 161200 | -45.66 | 0.84/0.84 | False | 4B_overlay_only |
| R11L6_C03_T6 | 2023-03-13 @ 113100 | 15.74 | 19.1 | 19.1 | 19.1 | 19.1 | -22.55 | -22.55 | -22.55 | 2023-03-08 | 161200 | -45.66 | None/None | False | 4C_overlay_only |
| R11L6_C04_T0 | 2022-05-13 @ 133000 | 36.84 | 47.37 | 288.72 | 293.98 | 293.98 | -4.51 | -4.51 | -4.51 | 2023-04-03 | 524000 | -81.72 | None/None | True | representative |
| R11L6_C04_T5 | 2023-02-28 @ 513000 | 2.14 | 2.14 | 2.14 | 2.14 | 2.14 | -0.58 | -81.33 | -81.33 | 2023-04-03 | 524000 | -81.72 | 0.97/0.97 | False | 4B_overlay_only |
| R11L6_C04_T6 | 2023-04-24 @ 348500 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | -64.28 | -72.51 | -72.51 | 2023-04-03 | 524000 | -81.72 | None/None | False | 4C_overlay_only |
| R11L6_C05_T1 | 2022-07-28 @ 52800 | 34.09 | 51.52 | 66.86 | 69.32 | 69.32 | -7.1 | -7.1 | -7.1 | 2023-06-21 | 89400 | -25.0 | None/None | True | representative |
| R11L6_C05_T2 | 2022-08-16 @ 65100 | 8.76 | 22.89 | 37.33 | 37.33 | 37.33 | -8.91 | -12.9 | -12.9 | 2023-06-21 | 89400 | -25.0 | None/None | True | representative |
| R11L6_C05_T5 | 2023-06-21 @ 87200 | 2.29 | 2.29 | 2.29 | 2.29 | unavailable_forward_504_not_recomputed | -9.4 | -15.13 | -25.0 | 2023-06-21 | 89400 | -25.0 | 0.94/0.94 | False | 4B_overlay_only |

## 10. 1D Price Path Summaries

Only anchor points are listed; full 504-row paths are not pasted.

### R11L6_C01 한화에어로스페이스
- Best Stage2 entry: 2022-07-27 close 52,200.
- D+~2: 2022-07-29 high 66,500 / close 64,400.
- D+~30: 2022-09-07 high 86,800 / close 82,400.
- D+~90 stress: 2022-10-13 low/close 52,600.
- D+180: 2023-04-11 high 120,100.
- 1Y observed peak: 2023-07-27 high 151,000.
- 2Y observed peak: 2024-07-30 high 330,000.

### R11L6_C02 현대로템
- Best Stage2 entry: 2022-07-22 close 24,400.
- D+~20: 2022-08-24 high 31,950 / close 31,400.
- D+~30: 2022-08-26 high 32,850.
- D+90 stress: 2022-10-27 low 23,050.
- 2023 extension: 2023-06-21 high 40,250.
- 2Y observed peak: 2024-07-31 high 51,300.

### R11L6_C03 에스엠
- Best Stage2 entry: 2023-02-07 close 90,100.
- Control-premium confirmation: 2023-02-10 close 114,700.
- Tender cap / 4B: 2023-03-07 close 149,700.
- Peak: 2023-03-08 high 161,200 / close 158,500.
- Thesis-break watch: 2023-03-13 low 111,300 / close 113,100.
- Later low in fetched path: 2023-03-27 low 90,500.

### R11L6_C04 삼천리
- Price-only anchor: 2022-05-13 close 133,000.
- D+~30: 2022-06-28 high/close 182,000.
- 2023 blowoff peak: 2023-04-03 high 524,000.
- Collapse: 2023-04-24 close 348,500; 2023-04-25 close 244,000; 2023-04-26 close 171,000.
- Post-collapse observed low in fetched path: 2023-07-26 low 95,800.

### R11L6_C05 씨에스윈드
- Best Stage2 policy entry: 2022-07-28 close 52,800.
- IRA signed entry candidate: 2022-08-16 close 65,100.
- D+~30: 2022-08-29 high 70,800.
- D+90: 2022-11-25 high 80,000.
- D+180/1Y observed high: 2023-06-21 high 89,400.

## 11. Case Trigger Comparison

| case | best entry | baseline-likely entry | what baseline missed | verdict |
| --- | --- | --- | --- | --- |
| R11L6_C01 | T1/T2 52,200 | T4 78,400 | framework + relative strength already carried rerating; executive-contract Green entered before -32.91 MAE pocket | Stage3_gate_too_late |
| R11L6_C02 | T1 24,400 | T2 31,400 | post-framework momentum candle had worse MAE and little 30D upside | Stage2_promote_candidate |
| R11L6_C03 | T1 90,100 | T3 or T5 | by tender-cap date risk/reward had flipped into 4B overlay | event_premium_stage2_wins |
| R11L6_C04 | none for positive scoring | none | huge MFE came without accepted evidence; price-only must not train positive score | correct_reject |
| R11L6_C05 | T1 52,800 | T2 65,100 | policy path was priced before final law signing | Stage2_policy_promote |

## 12. Stage2 → Stage4 Audit

Stage2 in R11 behaves like a fuse. Final confirmation is not when the candle first lights; it is often when half the fuse is already gone.

1. Stage2 MFE was large in evidence-backed cases: Hanwha T1 MFE90 66.28, Rotem T1 34.63, SM T1 78.91, and CS Wind T1 51.52.
2. Stage2 MAE was acceptable in Hanwha, SM, and CS Wind; Rotem was near the risk boundary but still better than the later momentum trigger.
3. Final confirmation was often later and riskier. Hanwha T4 MFE90 collapsed to 10.71 while MAE90 worsened to -32.91.
4. Stage2 promotion requires public non-price evidence. Samchully blocks “price moved first” from being treated as a valid positive score sample.

## 13. Stage3 Yellow / Green Lateness Audit

| case | early entry | green/yellow entry | green_lateness_ratio | interpretation |
| --- | --- | --- | --- | --- |
| R11L6_C01 | 52,200 | 78,400 | 0.265 | full-cycle ratio not extreme, but interim risk worsened sharply |
| R11L6_C02 | 24,400 | 31,400 | 0.54 | middle-late; missed early risk/reward edge |
| R11L6_C03 | 90,100 | 114,700 | 0.5 | Yellow works but gives away half of event-premium path |
| R11L6_C05 | 52,800 | 65,100 | 0.31 | law-signing confirmation remains usable but inferior to policy-path Stage2 |

## 14. 4B Timing Audit

| trigger | entry | local_peak_proximity | full_window_proximity | evidence_type | verdict |
| --- | --- | --- | --- | --- | --- |
| R11L6_C01_T5 | 142500 | 0.91 | 0.91 | valuation_blowoff|positioning_overheat | good_full_window_4B_timing |
| R11L6_C02_T5 | 39350 | 0.94 | 0.94 | positioning_overheat|price_only | good_full_window_4B_timing |
| R11L6_C03_T5 | 149700 | 0.84 | 0.84 | control_premium_or_event_premium|valuation_blowoff | good_full_window_4B_timing |
| R11L6_C04_T5 | 513000 | 0.97 | 0.97 | price_only|positioning_overheat | price_only_full_window_4B_needs_non_price_evidence |
| R11L6_C05_T5 | 87200 | 0.94 | 0.94 | valuation_blowoff|revision_slowdown|positioning_overheat | good_full_window_4B_timing |

The 4B lesson is not simply “near peak.” It is **why near peak**. SM has an explicit tender-price cap. CS Wind has policy-benefit saturation and revision fatigue risk. Samchully has only price proximity, so it validates a price-only 4B rejection guard rather than a full 4B signal.

## 15. 4C Protection Audit

| trigger | entry | label | MAE90_after_4C | interpretation |
| --- | --- | --- | --- | --- |
| R11L6_C03_T6 | 2023-03-13 @ 113100 | hard_4c_partial_success | -22.55 | thesis_break |
| R11L6_C04_T6 | 2023-04-24 @ 348500 | hard_4c_late | -72.51 | thesis_break_late |

R11 loop 6 does not validate a broad hard 4C delta. SM gives partial protection, but Samchully’s obvious crash trigger appears after the blowoff has already broken.

## 16. Baseline Score Simulation

`baseline_current_proxy` is a research proxy, not a claim about production code. It behaves as if the system waits for final contract/law/tender confirmation before strong entry. In this sample, that posture is narratively comfortable but worse in forward-return geometry.

- Hanwha: baseline selected T4 instead of T1; MFE90 fell from 66.28 to 10.71 and MAE90 worsened from -4.02 to -32.91.
- Rotem: baseline selected T2 instead of T1; MFE90 fell from 34.63 to 4.62 and MAE90 worsened from -14.75 to -22.29.
- SM: baseline selected T3 instead of T1; still profitable, but gave away event-premium edge.
- CS Wind: baseline selected T2 instead of T1; still valid, but missed early policy-path rerating.
- Samchully: baseline correctly rejects positive scoring because evidence is not accepted.

## 17. Shadow Profile Optimization Loop

| row_type | profile_id | case_count | selected_trigger_count | selected_representative_trigger_count | avg_MFE90 | median_MFE90 | avg_MAE90 | median_MAE90 | hit_rate_MFE90_gt_20 | bad_entry_rate_MAE90_lt_-15 | false_positive_rate | missed_structural_count | late_green_count | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| profile_comparison | baseline_current_proxy | 5 | 4 | 4 | 19.69 | 16.8 | -22.93 | -22.96 | 33.3 | 75.0 | 0.25 | 3 | 2 | reference; waits for final confirmation/event premium too often |
| profile_comparison | stage2_actionable_early_evidence_plus | 5 | 4 | 4 | 57.84 | 58.9 | -7.69 | -5.99 | 100.0 | 0.0 | 0.0 | 0 | 0 | best; promotes early non-price policy/geopolitical evidence with RS guard |
| profile_comparison | stage3_yellow_entry_relaxed | 5 | 4 | 4 | 47.21 | 46.03 | -12.48 | -10.2 | 75.0 | 25.0 | 0.1 | 1 | 1 | improved but weaker than Stage2-actionable guard |
| profile_comparison | green_confirmation_timing_relaxed | 5 | 4 | 4 | 30.9 | 28.44 | -17.2 | -17.8 | 50.0 | 50.0 | 0.15 | 2 | 1 | cautious; Green still late in defense cases |
| profile_comparison | four_b_peak_timing_tuned | 5 | 4 | 0 | overlay | overlay | overlay | overlay | overlay | overlay | overlay | overlay | overlay | keeps 4B as overlay and rejects price-only full 4B |
| profile_comparison | four_c_thesis_break_earlier | 5 | 2 | 0 | overlay | overlay | overlay | overlay | overlay | overlay | overlay | overlay | overlay | insufficient hard early 4C proof; no broad delta |

Best shadow profile: `r11_stage2_event_policy_early_guard`, operationalized as `stage2_actionable_early_evidence_plus` with stricter price-only rejection.

## 18. Before / After Backtest Comparison

| case_id | symbol | best_actual_trigger | baseline_selected | after_selected | baseline_entry | after_entry | baseline_price | after_price | baseline_MFE90 | after_MFE90 | baseline_MAE90 | after_MAE90 | baseline_MFE180 | after_MFE180 | baseline_MAE180 | after_MAE180 | return_improvement_90D | risk_change_90D | upside_capture_improvement | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R11L6_C01 | 012450 | R11L6_C01_T1 | R11L6_C01_T4 | R11L6_C01_T1 | 2022-08-26 | 2022-07-27 | 78400 | 52200 | 10.71 | 66.28 | -32.91 | -4.02 | 53.19 | 130.08 | -32.91 | -4.02 | 55.57 | 28.89 | 77.33 | framework evidence + RS already enough |
| R11L6_C02 | 064350 | R11L6_C02_T1 | R11L6_C02_T2 | R11L6_C02_T1 | 2022-08-24 | 2022-07-22 | 31400 | 24400 | 4.62 | 34.63 | -22.29 | -14.75 | 20.38 | 54.92 | -26.59 | -14.75 | 30.01 | 7.54 | 46.0 | do not wait for post-framework momentum candle |
| R11L6_C03 | 041510 | R11L6_C03_T1 | R11L6_C03_T3 | R11L6_C03_T1 | 2023-02-10 | 2023-02-07 | 114700 | 90100 | 40.54 | 78.91 | -23.63 | -4.88 | 40.54 | 78.91 | -23.63 | -4.88 | 38.37 | 18.75 | 54.0 | control-premium Stage2 beats tender-war confirmation |
| R11L6_C04 | 004690 | R11L6_C04_T0 | none | none | none | none | none | none | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | price-only high-MFE run rejected from positive scoring |
| R11L6_C05 | 112610 | R11L6_C05_T1 | R11L6_C05_T2 | R11L6_C05_T1 | 2022-08-16 | 2022-07-28 | 65100 | 52800 | 22.89 | 51.52 | -12.9 | -7.1 | 37.33 | 66.86 | -12.9 | -7.1 | 28.63 | 5.8 | 41.0 | policy path trigger beats final law confirmation |

## 19. Score-Return Alignment Matrix

| alignment_label | trigger_count | avg_weighted_score_before | avg_weighted_score_after | avg_MFE90 | avg_MAE90 | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| score_mid_return_high_promote_candidate | 5 | 34.4 | 53.2 | 59.52 | -6.95 | early non-price event/policy evidence deserves promotion guard |
| score_high_return_low_false_positive | 6 | 38.3 | 54.7 | 7.01 | -34.53 | late confirmation and 4B-like rows look strong narratively but poor risk/reward |
| score_high_return_high | 3 | 34.7 | 55.3 | 23.13 | -18.52 | works, but worse than earlier Stage2 in this event sample |
| score_mid_return_low_watch_only | 1 | 34.0 | 52.0 | 4.62 | -26.59 | momentum-only confirmation should stay watch-only |
| score_low_return_high_price_only_reject | 1 | 54.0 | 50.0 | 47.37 | -4.51 | high MFE without public evidence is not a positive training sample |
| score_low_return_low_correct_reject | 1 | 54.0 | 50.0 | 2.14 | -81.33 | price-only 4B near top needs non-price evidence |

## 20. Weight Sensitivity Table

| row_type | axis | baseline_value | tested_value | delta | reason | backtest_effect | trigger_ids | calibration_usable_count | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| shadow_weight | stage2_actionable_public_policy_or_geopolitical_evidence | 0 | 2 | +2 | Early policy/geopolitical evidence produced higher MFE with lower or acceptable MAE than confirmations. | baseline avg MFE90 19.69 / MAE90 -22.93 -> selected profile avg MFE90 57.84 / MAE90 -7.69 | R11L6_C01_T1|R11L6_C02_T1|R11L6_C05_T1 | 3 | shadow-only; requires non-price evidence plus OHLC relative strength |
| shadow_weight | control_premium_event_stage2 | 0 | 2 | +2 | SM Stage2 event premium had excellent MFE/MAE before explicit tender cap. | SM early event MFE90 78.91 / MAE90 -4.88 vs tender-cap 4B MFE90 7.68 / MAE90 -41.48 | R11L6_C03_T1|R11L6_C03_T5 | 2 | shadow-only; do not generalize beyond event premium |
| shadow_weight | price_only_blowoff_rejection | -1 | -3 | -2 | Samchully shows high MFE without evidence; should not train positive Stage2/Green weights. | Price-only run MFE180 288.72 but later drawdown after peak -81.72; use as rejection guard. | R11L6_C04_T0|R11L6_C04_T5 | 1 | negative guard; not a positive promotion sample |
| shadow_weight | four_b_non_price_evidence_requirement | 1 | 3 | +2 | 4B should not be price-only unless paired with valuation/event cap or revision/contract slowdown. | SM tender-cap worked; Samchully price-only proximity would overfit without evidence. | R11L6_C03_T5|R11L6_C04_T5|R11L6_C05_T5 | 3 | shadow-only overlay |
| shadow_weight | hard_4c_early_break_delta | 0 | 0 | 0 | Only SM partial 4C and Samchully late hard 4C were validated. | No broad early hard-gate proof; keep delta zero. | R11L6_C03_T6|R11L6_C04_T6 | 2 | no gate change |

## 21. Optimization Decision Log

```jsonl
{"row_type":"optimization_decision","decision_id":"R11L6_D01","hypothesis":"Stage2 policy/geopolitical evidence should be promoted before final contract/law confirmation when relative strength is already present.","tested_cases":["R11L6_C01","R11L6_C02","R11L6_C05"],"tested_trigger_ids":["R11L6_C01_T1","R11L6_C02_T1","R11L6_C05_T1"],"baseline_profile":"baseline_current_proxy","selected_profile":"r11_stage2_event_policy_early_guard","backtest_result_summary":"Early-evidence selected profile improved avg MFE90 from 19.69 to 57.84 and improved avg MAE90 from -22.93 to -7.69 across non-price evidence cases.","accepted_or_rejected":"accepted","delta_magnitude":"+2","why_not_larger_delta":"R11 sample is still event-heavy and sector-diverse; false-positive guard must be tested in R1/R2/R3.","risks":"Policy headline rallies can reverse if execution/order conversion fails.","next_validation_needed":"Add a failed policy-rerating case with good initial headline but weak follow-through."}
{"row_type":"optimization_decision","decision_id":"R11L6_D02","hypothesis":"Price-only blowoff must not be upgraded to Stage2-Actionable even with very large MFE.","tested_cases":["R11L6_C04"],"tested_trigger_ids":["R11L6_C04_T0","R11L6_C04_T5"],"baseline_profile":"baseline_current_proxy","selected_profile":"r11_stage2_event_policy_early_guard","backtest_result_summary":"Samchully generated extreme MFE but no usable non-price evidence; later drawdown after peak reached -81.72, so the correct action is rejection/4B watch, not promotion.","accepted_or_rejected":"accepted","delta_magnitude":"-2","why_not_larger_delta":"Single case; keep as guard until more price-only manipulation or forced-liquidation cases are validated.","risks":"Over-filtering genuine low-liquidity structural reratings.","next_validation_needed":"Find non-manipulation low-liquidity rerating counterexample."}
{"row_type":"optimization_decision","decision_id":"R11L6_D03","hypothesis":"4B should split price-only proximity from full-window non-price evidence.","tested_cases":["R11L6_C01","R11L6_C02","R11L6_C03","R11L6_C04","R11L6_C05"],"tested_trigger_ids":["R11L6_C01_T5","R11L6_C02_T5","R11L6_C03_T5","R11L6_C04_T5","R11L6_C05_T5"],"baseline_profile":"baseline_current_proxy","selected_profile":"four_b_peak_timing_tuned","backtest_result_summary":"SM tender cap and CS/Hanwha peak-proximity were useful; Samchully price-only peak proximity without non-price evidence must be kept as watch-only.","accepted_or_rejected":"accepted","delta_magnitude":"+2 non-price evidence requirement","why_not_larger_delta":"Only one clean control-premium 4B case and one price-only rejection case.","risks":"May miss pure liquidity unwind when no non-price warning exists.","next_validation_needed":"More CFD/CB/lockup/short-squeeze unwind cases."}
```

## 22. Overfitting / Robustness Check

- Usable case count is 5 and usable trigger count is 17, but true positive promotion evidence rests mainly on four evidence-backed early-entry cases.
- Accepted positive deltas are capped at +2. The profile improves MFE and MAE, but R11 event samples are not enough for +5.
- Samchully is the counterexample: OHLC MFE is huge, but non-price evidence is not accepted. This blocks price-only promotion.
- Hard 4C does not receive a positive delta. Evidence is too late or too narrow.

## 23. Cross-case Aggregate Metrics

### Trigger type aggregate CSV

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,4,4,57.84,58.9,-7.69,-5.99,mixed,not_applicable,not_applicable,"representative rows only; non-price evidence required"
aggregate_metric,Stage3-Green,1,1,10.71,10.71,-32.91,-32.91,0.265,not_applicable,not_applicable,confirmation was too late in Hanwha sample
aggregate_metric,Stage2-Actionable,2,2,13.76,13.76,-19.75,-19.75,mixed,not_applicable,not_applicable,late momentum/law-signing labels are useful but inferior to earliest evidence
aggregate_metric,Stage3-Yellow,1,1,40.54,40.54,-23.63,-23.63,0.5,not_applicable,not_applicable,works for control premium but gives away early edge
aggregate_metric,Price-only no-evidence run,1,1,47.37,47.37,-4.51,-4.51,not_applicable,not_applicable,not_applicable,not for positive score calibration
```

### Profile aggregate CSV

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,verdict
profile_comparison,baseline_current_proxy,5,4,4,19.69,16.8,-22.93,-22.96,33.3,75.0,0.25,3,2,"reference; waits for final confirmation/event premium too often"
profile_comparison,stage2_actionable_early_evidence_plus,5,4,4,57.84,58.9,-7.69,-5.99,100.0,0.0,0.0,0,0,"best; promotes early non-price policy/geopolitical evidence with RS guard"
profile_comparison,stage3_yellow_entry_relaxed,5,4,4,47.21,46.03,-12.48,-10.2,75.0,25.0,0.1,1,1,improved but weaker than Stage2-actionable guard
profile_comparison,green_confirmation_timing_relaxed,5,4,4,30.9,28.44,-17.2,-17.8,50.0,50.0,0.15,2,1,"cautious; Green still late in defense cases"
profile_comparison,four_b_peak_timing_tuned,5,4,0,overlay,overlay,overlay,overlay,overlay,overlay,overlay,overlay,overlay,keeps 4B as overlay and rejects price-only full 4B
profile_comparison,four_c_thesis_break_earlier,5,2,0,overlay,overlay,overlay,overlay,overlay,overlay,overlay,overlay,overlay,"insufficient hard early 4C proof; no broad delta"
```

Aggregate metrics use `calibration_usable=true AND dedupe_for_aggregate=true`. Same-entry duplicate labels are retained in JSONL but excluded from representative aggregate rows.

## 24. Score-Price Alignment Verdict

The best R11 alignment is not “wait for final confirmation.” It is “promote early public non-price event evidence only when OHLC relative strength confirms, and reject price-only blowoffs.”

- Early public policy/geopolitical evidence: positive shadow delta.
- Control premium before tender cap: positive but narrow shadow delta.
- Price-only blowoff: negative guard.
- 4B: split local/full-window proximity and require non-price evidence for full 4B.
- 4C: no broad change.

## 25. Validation Scope / Non-Validation Scope

### this_round_validates

- Stage2-Actionable promotion when public geopolitical/policy evidence and relative strength appear before final confirmation.
- Stage3-Green lateness in defense-export confirmation cases.
- Control-premium Stage2 entry before explicit tender cap.
- Price-only blowoff rejection even when MFE is high.
- 4B local/full-window proximity split with non-price evidence requirement.

### this_round_does_not_validate

- Broad relaxation of all Stage3-Green gates.
- Hard 4C early thesis-break gate across sectors.
- Price-only 4B as full 4B without valuation, tender cap, revision slowdown, contract delay, CB/dilution, or other non-price evidence.
- Policy headline promotion without OHLC relative strength.

## 26. Shadow Weight Calibration

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_public_policy_or_geopolitical_evidence,0,2,+2,Early policy/geopolitical evidence produced higher MFE with lower or acceptable MAE than confirmations.,"baseline avg MFE90 19.69 / MAE90 -22.93 -> selected profile avg MFE90 57.84 / MAE90 -7.69",R11L6_C01_T1|R11L6_C02_T1|R11L6_C05_T1,3,"shadow-only; requires non-price evidence plus OHLC relative strength"
shadow_weight,control_premium_event_stage2,0,2,+2,SM Stage2 event premium had excellent MFE/MAE before explicit tender cap.,SM early event MFE90 78.91 / MAE90 -4.88 vs tender-cap 4B MFE90 7.68 / MAE90 -41.48,R11L6_C03_T1|R11L6_C03_T5,2,"shadow-only; do not generalize beyond event premium"
shadow_weight,price_only_blowoff_rejection,-1,-3,-2,"Samchully shows high MFE without evidence; should not train positive Stage2/Green weights.","Price-only run MFE180 288.72 but later drawdown after peak -81.72; use as rejection guard.",R11L6_C04_T0|R11L6_C04_T5,1,"negative guard; not a positive promotion sample"
shadow_weight,four_b_non_price_evidence_requirement,1,3,+2,4B should not be price-only unless paired with valuation/event cap or revision/contract slowdown.,"SM tender-cap worked; Samchully price-only proximity would overfit without evidence.",R11L6_C03_T5|R11L6_C04_T5|R11L6_C05_T5,3,shadow-only overlay
shadow_weight,hard_4c_early_break_delta,0,0,0,Only SM partial 4C and Samchully late hard 4C were validated.,"No broad early hard-gate proof; keep delta zero.",R11L6_C03_T6|R11L6_C04_T6,2,no gate change
```

No production scoring changed. All deltas are shadow-only.

## 27. Machine-Readable Rows

### 27.1 Price source validation row JSONL

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 27.2 Case rows JSONL

```jsonl
{"row_type":"case","case_id":"R11L6_C01","symbol":"012450","company_name":"한화에어로스페이스","round":"R11","loop":"6","sector":"정책·지정학·재난·이벤트","case_type":"structural_success","primary_archetype":"GEOPOLITICAL_DEFENSE_EXPORT_POLICY","best_trigger":"R11L6_C01_T1","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"mixed_by_trigger","price_source":"Songdaiki/stock-web","notes":"Defense export framework caught rerating earlier than executive contract Green."}
{"row_type":"case","case_id":"R11L6_C02","symbol":"064350","company_name":"현대로템","round":"R11","loop":"6","sector":"정책·지정학·재난·이벤트","case_type":"Stage2_promote_candidate","primary_archetype":"GEOPOLITICAL_DEFENSE_EXPORT_POLICY","best_trigger":"R11L6_C02_T1","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"mixed_by_trigger","price_source":"Songdaiki/stock-web","notes":"K2/Poland framework trigger outperformed later momentum confirmation."}
{"row_type":"case","case_id":"R11L6_C03","symbol":"041510","company_name":"에스엠","round":"R11","loop":"6","sector":"정책·지정학·재난·이벤트","case_type":"event_premium_success_then_4B_4C","primary_archetype":"CONTROL_PREMIUM_GOVERNANCE_EVENT","best_trigger":"R11L6_C03_T1","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"mixed_by_trigger","price_source":"Songdaiki/stock-web","notes":"Control-premium Stage2 worked; tender cap became 4B, not fresh entry."}
{"row_type":"case","case_id":"R11L6_C04","symbol":"004690","company_name":"삼천리","round":"R11","loop":"6","sector":"정책·지정학·재난·이벤트","case_type":"price_moved_without_evidence_4C_late","primary_archetype":"PRICE_ONLY_MANIPULATION_OR_FORCED_LIQUIDATION","best_trigger":"R11L6_C04_T0","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"mixed_by_trigger","price_source":"Songdaiki/stock-web","notes":"Extreme OHLC blowoff without accepted public evidence; useful as price-only rejection."}
{"row_type":"case","case_id":"R11L6_C05","symbol":"112610","company_name":"씨에스윈드","round":"R11","loop":"6","sector":"정책·지정학·재난·이벤트","case_type":"policy_rerating_success","primary_archetype":"IRA_RENEWABLE_POLICY_RERATING","best_trigger":"R11L6_C05_T1","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"mixed_by_trigger","price_source":"Songdaiki/stock-web","notes":"IRA path trigger beat final law-signing confirmation."}
```

### 27.3 Trigger rows JSONL

```jsonl
{"row_type":"trigger","trigger_id":"R11L6_C01_T1","case_id":"R11L6_C01","symbol":"012450","company_name":"한화에어로스페이스","round":"R11","loop":"6","sector":"정책·지정학·재난·이벤트","primary_archetype":"GEOPOLITICAL_DEFENSE_EXPORT_POLICY","trigger_type":"Stage2","trigger_date":"2022-07-27","evidence_available_at_that_date":"Poland/Korea defense framework agreement for K9/K2/FA-50 family; public defense-export policy shock.","evidence_source":"public news / defense export records","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012450/2022.csv","profile_path":"atlas/symbol_profiles/012/012450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-07-27","entry_price":52200,"MFE_30D_pct":66.28,"MFE_90D_pct":66.28,"MFE_180D_pct":130.08,"MFE_1Y_pct":189.27,"MFE_2Y_pct":532.18,"MAE_30D_pct":-4.02,"MAE_90D_pct":-4.02,"MAE_180D_pct":-4.02,"MAE_1Y_pct":-4.02,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-07-30","peak_price":330000,"drawdown_after_peak_pct":-33.0,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.265,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R11L6_C01_20220727_52200","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R11L6_C01_T2","case_id":"R11L6_C01","symbol":"012450","company_name":"한화에어로스페이스","round":"R11","loop":"6","sector":"정책·지정학·재난·이벤트","primary_archetype":"GEOPOLITICAL_DEFENSE_EXPORT_POLICY","trigger_type":"Stage2-Actionable","trigger_date":"2022-07-27","evidence_available_at_that_date":"Same framework event, upgraded because defense-export size + immediate relative strength closed the early-evidence gate.","evidence_source":"public news / defense export records + OHLC relative strength","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012450/2022.csv","profile_path":"atlas/symbol_profiles/012/012450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-07-27","entry_price":52200,"MFE_30D_pct":66.28,"MFE_90D_pct":66.28,"MFE_180D_pct":130.08,"MFE_1Y_pct":189.27,"MFE_2Y_pct":532.18,"MAE_30D_pct":-4.02,"MAE_90D_pct":-4.02,"MAE_180D_pct":-4.02,"MAE_1Y_pct":-4.02,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-07-30","peak_price":330000,"drawdown_after_peak_pct":-33.0,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.265,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R11L6_C01_20220727_52200","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only"}
{"row_type":"trigger","trigger_id":"R11L6_C01_T4","case_id":"R11L6_C01","symbol":"012450","company_name":"한화에어로스페이스","round":"R11","loop":"6","sector":"정책·지정학·재난·이벤트","primary_archetype":"GEOPOLITICAL_DEFENSE_EXPORT_POLICY","trigger_type":"Stage3-Green","trigger_date":"2022-08-26","evidence_available_at_that_date":"First executive K9 contract; contract confirmation closed, but entry came after substantial rerating and before a deep volatility pocket.","evidence_source":"public contract records","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012450/2022.csv","profile_path":"atlas/symbol_profiles/012/012450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-08-26","entry_price":78400,"MFE_30D_pct":10.71,"MFE_90D_pct":10.71,"MFE_180D_pct":53.19,"MFE_1Y_pct":92.6,"MFE_2Y_pct":320.92,"MAE_30D_pct":-32.91,"MAE_90D_pct":-32.91,"MAE_180D_pct":-32.91,"MAE_1Y_pct":-32.91,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-30","peak_price":330000,"drawdown_after_peak_pct":-33.0,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.265,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"late_entry","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R11L6_C01_20220826_78400","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R11L6_C01_T5","case_id":"R11L6_C01","symbol":"012450","company_name":"한화에어로스페이스","round":"R11","loop":"6","sector":"정책·지정학·재난·이벤트","primary_archetype":"GEOPOLITICAL_DEFENSE_EXPORT_POLICY","trigger_type":"4B","trigger_date":"2023-06-20","evidence_available_at_that_date":"Defense-export rerating blowoff/positioning watch after full cycle extension.","evidence_source":"OHLC + valuation/positioning overlay","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012450/2023.csv","profile_path":"atlas/symbol_profiles/012/012450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-06-20","entry_price":142500,"MFE_30D_pct":5.96,"MFE_90D_pct":5.96,"MFE_180D_pct":131.58,"MFE_1Y_pct":131.58,"MFE_2Y_pct":"unavailable_forward_504_not_recomputed","MAE_30D_pct":-19.02,"MAE_90D_pct":-19.02,"MAE_180D_pct":-19.02,"MAE_1Y_pct":-19.02,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-30","peak_price":330000,"drawdown_after_peak_pct":-33.0,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":0.91,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":"valuation_blowoff|positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_watch_success","calibration_usable":true,"forward_window_trading_days":252,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R11L6_C01_20230620_142500","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R11L6_C02_T1","case_id":"R11L6_C02","symbol":"064350","company_name":"현대로템","round":"R11","loop":"6","sector":"정책·지정학·재난·이벤트","primary_archetype":"GEOPOLITICAL_DEFENSE_EXPORT_POLICY","trigger_type":"Stage2","trigger_date":"2022-07-22","evidence_available_at_that_date":"K2 tank / Poland framework signal enters public tape; material geopolitical defense-export demand but contract details still incomplete.","evidence_source":"public defense export records","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv","profile_path":"atlas/symbol_profiles/064/064350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-07-22","entry_price":24400,"MFE_30D_pct":34.63,"MFE_90D_pct":34.63,"MFE_180D_pct":54.92,"MFE_1Y_pct":64.96,"MFE_2Y_pct":110.25,"MAE_30D_pct":-14.75,"MAE_90D_pct":-14.75,"MAE_180D_pct":-14.75,"MAE_1Y_pct":-14.75,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-07-31","peak_price":51300,"drawdown_after_peak_pct":-22.0,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.54,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"good_entry","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R11L6_C02_20220722_24400","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R11L6_C02_T2","case_id":"R11L6_C02","symbol":"064350","company_name":"현대로템","round":"R11","loop":"6","sector":"정책·지정학·재난·이벤트","primary_archetype":"GEOPOLITICAL_DEFENSE_EXPORT_POLICY","trigger_type":"Stage2-Actionable","trigger_date":"2022-08-24","evidence_available_at_that_date":"Post-framework momentum break; not enough incremental non-price evidence versus the July framework.","evidence_source":"OHLC relative strength","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv","profile_path":"atlas/symbol_profiles/064/064350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-08-24","entry_price":31400,"MFE_30D_pct":4.62,"MFE_90D_pct":4.62,"MFE_180D_pct":20.38,"MFE_1Y_pct":28.18,"MFE_2Y_pct":63.38,"MAE_30D_pct":-22.29,"MAE_90D_pct":-26.59,"MAE_180D_pct":-26.59,"MAE_1Y_pct":-26.59,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-31","peak_price":51300,"drawdown_after_peak_pct":-22.0,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.54,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"late_event_premium","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R11L6_C02_20220824_31400","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R11L6_C02_T5","case_id":"R11L6_C02","symbol":"064350","company_name":"현대로템","round":"R11","loop":"6","sector":"정책·지정학·재난·이벤트","primary_archetype":"GEOPOLITICAL_DEFENSE_EXPORT_POLICY","trigger_type":"4B","trigger_date":"2023-06-20","evidence_available_at_that_date":"Local/full-window price proximity after defense rerating; watch overlay, not thesis cancellation.","evidence_source":"OHLC + positioning overlay","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064350/2023.csv","profile_path":"atlas/symbol_profiles/064/064350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-06-20","entry_price":39350,"MFE_30D_pct":2.29,"MFE_90D_pct":2.29,"MFE_180D_pct":30.37,"MFE_1Y_pct":30.37,"MFE_2Y_pct":"unavailable_forward_504_not_recomputed","MAE_30D_pct":-18.17,"MAE_90D_pct":-22.62,"MAE_180D_pct":-35.32,"MAE_1Y_pct":-35.32,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-31","peak_price":51300,"drawdown_after_peak_pct":-22.0,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.94,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":"positioning_overheat|price_only","four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_watch_success","calibration_usable":true,"forward_window_trading_days":252,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R11L6_C02_20230620_39350","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R11L6_C03_T1","case_id":"R11L6_C03","symbol":"041510","company_name":"에스엠","round":"R11","loop":"6","sector":"정책·지정학·재난·이벤트","primary_archetype":"CONTROL_PREMIUM_GOVERNANCE_EVENT","trigger_type":"Stage2","trigger_date":"2023-02-07","evidence_available_at_that_date":"Kakao strategic stake / SM governance battle becomes public event premium; not yet final control auction.","evidence_source":"public news","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv","profile_path":"atlas/symbol_profiles/041/041510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-07","entry_price":90100,"MFE_30D_pct":78.91,"MFE_90D_pct":78.91,"MFE_180D_pct":78.91,"MFE_1Y_pct":78.91,"MFE_2Y_pct":78.91,"MAE_30D_pct":-4.88,"MAE_90D_pct":-4.88,"MAE_180D_pct":-4.88,"MAE_1Y_pct":-4.88,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-08","peak_price":161200,"drawdown_after_peak_pct":-45.66,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.5,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"excellent_event_entry","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R11L6_C03_20230207_90100","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R11L6_C03_T3","case_id":"R11L6_C03","symbol":"041510","company_name":"에스엠","round":"R11","loop":"6","sector":"정책·지정학·재난·이벤트","primary_archetype":"CONTROL_PREMIUM_GOVERNANCE_EVENT","trigger_type":"Stage3-Yellow","trigger_date":"2023-02-10","evidence_available_at_that_date":"HYBE 14.8% stake/tender offer increases control-premium probability, but overhang and bid ceiling risk also rise.","evidence_source":"public news","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv","profile_path":"atlas/symbol_profiles/041/041510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-10","entry_price":114700,"MFE_30D_pct":40.54,"MFE_90D_pct":40.54,"MFE_180D_pct":40.54,"MFE_1Y_pct":40.54,"MFE_2Y_pct":40.54,"MAE_30D_pct":-21.1,"MAE_90D_pct":-23.63,"MAE_180D_pct":-23.63,"MAE_1Y_pct":-23.63,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-08","peak_price":161200,"drawdown_after_peak_pct":-45.66,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.5,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"event_premium_good_but_risky","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R11L6_C03_20230210_114700","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R11L6_C03_T5","case_id":"R11L6_C03","symbol":"041510","company_name":"에스엠","round":"R11","loop":"6","sector":"정책·지정학·재난·이벤트","primary_archetype":"CONTROL_PREMIUM_GOVERNANCE_EVENT","trigger_type":"4B","trigger_date":"2023-03-07","evidence_available_at_that_date":"Kakao 150,000-won tender offer establishes explicit event-premium cap; strong 4B overlay rather than fresh entry.","evidence_source":"public news","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv","profile_path":"atlas/symbol_profiles/041/041510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-03-07","entry_price":149700,"MFE_30D_pct":7.68,"MFE_90D_pct":7.68,"MFE_180D_pct":7.68,"MFE_1Y_pct":7.68,"MFE_2Y_pct":7.68,"MAE_30D_pct":-41.48,"MAE_90D_pct":-41.48,"MAE_180D_pct":-41.48,"MAE_1Y_pct":-41.48,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-08","peak_price":161200,"drawdown_after_peak_pct":-45.66,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.84,"four_b_full_window_peak_proximity":0.84,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":"control_premium_or_event_premium|valuation_blowoff","four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_watch_success","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R11L6_C03_20230307_149700","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R11L6_C03_T6","case_id":"R11L6_C03","symbol":"041510","company_name":"에스엠","round":"R11","loop":"6","sector":"정책·지정학·재난·이벤트","primary_archetype":"CONTROL_PREMIUM_GOVERNANCE_EVENT","trigger_type":"4C","trigger_date":"2023-03-13","evidence_available_at_that_date":"HYBE abandons majority-control pursuit; control-premium thesis breaks after peak but before full low.","evidence_source":"public news","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv","profile_path":"atlas/symbol_profiles/041/041510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-03-13","entry_price":113100,"MFE_30D_pct":15.74,"MFE_90D_pct":19.1,"MFE_180D_pct":19.1,"MFE_1Y_pct":19.1,"MFE_2Y_pct":19.1,"MAE_30D_pct":-22.55,"MAE_90D_pct":-22.55,"MAE_180D_pct":-22.55,"MAE_1Y_pct":-22.55,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-08","peak_price":161200,"drawdown_after_peak_pct":-45.66,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"hard_4c_partial_success","trigger_outcome_label":"thesis_break","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R11L6_C03_20230313_113100","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only"}
{"row_type":"trigger","trigger_id":"R11L6_C04_T0","case_id":"R11L6_C04","symbol":"004690","company_name":"삼천리","round":"R11","loop":"6","sector":"정책·지정학·재난·이벤트","primary_archetype":"PRICE_ONLY_MANIPULATION_OR_FORCED_LIQUIDATION","trigger_type":"Price-only no-evidence run","trigger_date":"2022-05-13","evidence_available_at_that_date":"No evidence-backed EPS/OP/policy trigger found in this pass; OHLC shows long low-liquidity rerating before 2023 crash.","evidence_source":"stock-web OHLC; external evidence search incomplete","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004690/2022.csv","profile_path":"atlas/symbol_profiles/004/004690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-05-13","entry_price":133000,"MFE_30D_pct":36.84,"MFE_90D_pct":47.37,"MFE_180D_pct":288.72,"MFE_1Y_pct":293.98,"MFE_2Y_pct":293.98,"MAE_30D_pct":-4.51,"MAE_90D_pct":-4.51,"MAE_180D_pct":-4.51,"MAE_1Y_pct":-4.51,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2023-04-03","peak_price":524000,"drawdown_after_peak_pct":-81.72,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"price_moved_without_evidence","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R11L6_C04_20220513_133000","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R11L6_C04_T5","case_id":"R11L6_C04","symbol":"004690","company_name":"삼천리","round":"R11","loop":"6","sector":"정책·지정학·재난·이벤트","primary_archetype":"PRICE_ONLY_MANIPULATION_OR_FORCED_LIQUIDATION","trigger_type":"4B","trigger_date":"2023-02-28","evidence_available_at_that_date":"Peak-proximity price-only 4B. No non-price 4B evidence available at the date; should not be treated as full evidence-based 4B.","evidence_source":"stock-web OHLC","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004690/2023.csv","profile_path":"atlas/symbol_profiles/004/004690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-28","entry_price":513000,"MFE_30D_pct":2.14,"MFE_90D_pct":2.14,"MFE_180D_pct":2.14,"MFE_1Y_pct":2.14,"MFE_2Y_pct":2.14,"MAE_30D_pct":-0.58,"MAE_90D_pct":-81.33,"MAE_180D_pct":-81.33,"MAE_1Y_pct":-81.33,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-03","peak_price":524000,"drawdown_after_peak_pct":-81.72,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.97,"four_b_full_window_peak_proximity":0.97,"four_b_timing_verdict":"price_only_full_window_4B_needs_non_price_evidence","four_b_evidence_type":"price_only|positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"price_only_4B_watch","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R11L6_C04_20230228_513000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R11L6_C04_T6","case_id":"R11L6_C04","symbol":"004690","company_name":"삼천리","round":"R11","loop":"6","sector":"정책·지정학·재난·이벤트","primary_archetype":"PRICE_ONLY_MANIPULATION_OR_FORCED_LIQUIDATION","trigger_type":"4C","trigger_date":"2023-04-24","evidence_available_at_that_date":"Visible forced-liquidation/crash trigger; hard 4C appears after peak and after first large limit-down.","evidence_source":"stock-web OHLC","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004690/2023.csv","profile_path":"atlas/symbol_profiles/004/004690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-04-24","entry_price":348500,"MFE_30D_pct":0.0,"MFE_90D_pct":0.0,"MFE_180D_pct":0.0,"MFE_1Y_pct":0.0,"MFE_2Y_pct":0.0,"MAE_30D_pct":-64.28,"MAE_90D_pct":-72.51,"MAE_180D_pct":-72.51,"MAE_1Y_pct":-72.51,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-03","peak_price":524000,"drawdown_after_peak_pct":-81.72,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"hard_4c_late","trigger_outcome_label":"thesis_break_late","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R11L6_C04_20230424_348500","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only"}
{"row_type":"trigger","trigger_id":"R11L6_C05_T1","case_id":"R11L6_C05","symbol":"112610","company_name":"씨에스윈드","round":"R11","loop":"6","sector":"정책·지정학·재난·이벤트","primary_archetype":"IRA_RENEWABLE_POLICY_RERATING","trigger_type":"Stage2","trigger_date":"2022-07-28","evidence_available_at_that_date":"US climate bill / IRA path re-enters public policy tape; wind tower domestic-content and clean-energy tax-credit optionality appears before final signing.","evidence_source":"public policy news","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv","profile_path":"atlas/symbol_profiles/112/112610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-07-28","entry_price":52800,"MFE_30D_pct":34.09,"MFE_90D_pct":51.52,"MFE_180D_pct":66.86,"MFE_1Y_pct":69.32,"MFE_2Y_pct":69.32,"MAE_30D_pct":-7.1,"MAE_90D_pct":-7.1,"MAE_180D_pct":-7.1,"MAE_1Y_pct":-7.1,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-21","peak_price":89400,"drawdown_after_peak_pct":-25.0,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.31,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"excellent_policy_entry","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R11L6_C05_20220728_52800","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R11L6_C05_T2","case_id":"R11L6_C05","symbol":"112610","company_name":"씨에스윈드","round":"R11","loop":"6","sector":"정책·지정학·재난·이벤트","primary_archetype":"IRA_RENEWABLE_POLICY_RERATING","trigger_type":"Stage2-Actionable","trigger_date":"2022-08-16","evidence_available_at_that_date":"IRA signed into law. Confirmation improves policy durability but loses much of the first rerating leg.","evidence_source":"public policy law-signing news","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv","profile_path":"atlas/symbol_profiles/112/112610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-08-16","entry_price":65100,"MFE_30D_pct":8.76,"MFE_90D_pct":22.89,"MFE_180D_pct":37.33,"MFE_1Y_pct":37.33,"MFE_2Y_pct":37.33,"MAE_30D_pct":-8.91,"MAE_90D_pct":-12.9,"MAE_180D_pct":-12.9,"MAE_1Y_pct":-12.9,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-21","peak_price":89400,"drawdown_after_peak_pct":-25.0,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.31,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"good_but_later_policy_confirmation","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R11L6_C05_20220816_65100","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R11L6_C05_T5","case_id":"R11L6_C05","symbol":"112610","company_name":"씨에스윈드","round":"R11","loop":"6","sector":"정책·지정학·재난·이벤트","primary_archetype":"IRA_RENEWABLE_POLICY_RERATING","trigger_type":"4B","trigger_date":"2023-06-21","evidence_available_at_that_date":"Policy rerating high after repeated momentum; 4B watch for policy-benefit saturation and revision fatigue.","evidence_source":"OHLC + policy momentum overlay","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/112/112610/2023.csv","profile_path":"atlas/symbol_profiles/112/112610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-06-21","entry_price":87200,"MFE_30D_pct":2.29,"MFE_90D_pct":2.29,"MFE_180D_pct":2.29,"MFE_1Y_pct":2.29,"MFE_2Y_pct":"unavailable_forward_504_not_recomputed","MAE_30D_pct":-9.4,"MAE_90D_pct":-15.13,"MAE_180D_pct":-25.0,"MAE_1Y_pct":-25.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-21","peak_price":89400,"drawdown_after_peak_pct":-25.0,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.94,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":"valuation_blowoff|revision_slowdown|positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_watch_success","calibration_usable":true,"forward_window_trading_days":252,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R11L6_C05_20230621_87200","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
```

### 27.4 Score simulation rows JSONL

```jsonl
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R11L6_C01","trigger_id":"R11L6_C01_T1","symbol":"012450","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":5,"valuation_repricing_score":0,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":34.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":5,"policy_or_regulatory_score":7,"valuation_repricing_score":0,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":52.0,"stage_label_after":"Stage2","changed_components":["contract_score","relative_strength_score","customer_quality_score","policy_or_regulatory_score","execution_risk_score"],"component_delta_explanation":"shadow-only proxy: promote early public evidence only when non-price evidence plus relative strength beat later confirmation on MFE/MAE; price-only runs are rejected.","selected_by_profile":true,"MFE_90D_pct":66.28,"MAE_90D_pct":-4.02,"score_return_alignment_label":"score_mid_return_high_promote_candidate","row_validation_status":"valid_for_weight_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R11L6_C01","trigger_id":"R11L6_C01_T2","symbol":"012450","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":5,"valuation_repricing_score":0,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":34.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":5,"policy_or_regulatory_score":7,"valuation_repricing_score":0,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":52.0,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","relative_strength_score","customer_quality_score","policy_or_regulatory_score","execution_risk_score"],"component_delta_explanation":"shadow-only proxy: promote early public evidence only when non-price evidence plus relative strength beat later confirmation on MFE/MAE; price-only runs are rejected.","selected_by_profile":false,"MFE_90D_pct":66.28,"MAE_90D_pct":-4.02,"score_return_alignment_label":"score_mid_return_high_promote_candidate","row_validation_status":"valid_for_weight_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R11L6_C01","trigger_id":"R11L6_C01_T4","symbol":"012450","trigger_type":"Stage3-Green","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":5,"valuation_repricing_score":0,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":34.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":7,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":5,"policy_or_regulatory_score":7,"valuation_repricing_score":0,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":56.0,"stage_label_after":"Stage3-Green","changed_components":["contract_score","relative_strength_score","customer_quality_score","policy_or_regulatory_score","execution_risk_score"],"component_delta_explanation":"shadow-only proxy: promote early public evidence only when non-price evidence plus relative strength beat later confirmation on MFE/MAE; price-only runs are rejected.","selected_by_profile":false,"MFE_90D_pct":10.71,"MAE_90D_pct":-32.91,"score_return_alignment_label":"score_high_return_low_false_positive","row_validation_status":"valid_for_weight_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R11L6_C01","trigger_id":"R11L6_C01_T5","symbol":"012450","trigger_type":"4B","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":5,"valuation_repricing_score":0,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":34.0,"stage_label_before":"4B","raw_component_scores_after":{"contract_score":7,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":5,"policy_or_regulatory_score":7,"valuation_repricing_score":0,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":56.0,"stage_label_after":"4B","changed_components":["contract_score","relative_strength_score","customer_quality_score","policy_or_regulatory_score","execution_risk_score"],"component_delta_explanation":"shadow-only proxy: promote early public evidence only when non-price evidence plus relative strength beat later confirmation on MFE/MAE; price-only runs are rejected.","selected_by_profile":false,"MFE_90D_pct":5.96,"MAE_90D_pct":-19.02,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_weight_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R11L6_C02","trigger_id":"R11L6_C02_T1","symbol":"064350","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":5,"valuation_repricing_score":0,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":34.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":5,"policy_or_regulatory_score":7,"valuation_repricing_score":0,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":52.0,"stage_label_after":"Stage2","changed_components":["contract_score","relative_strength_score","customer_quality_score","policy_or_regulatory_score","execution_risk_score"],"component_delta_explanation":"shadow-only proxy: promote early public evidence only when non-price evidence plus relative strength beat later confirmation on MFE/MAE; price-only runs are rejected.","selected_by_profile":true,"MFE_90D_pct":34.63,"MAE_90D_pct":-14.75,"score_return_alignment_label":"score_mid_return_high_promote_candidate","row_validation_status":"valid_for_weight_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R11L6_C02","trigger_id":"R11L6_C02_T2","symbol":"064350","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":5,"valuation_repricing_score":0,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":34.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":5,"policy_or_regulatory_score":7,"valuation_repricing_score":0,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":52.0,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","relative_strength_score","customer_quality_score","policy_or_regulatory_score","execution_risk_score"],"component_delta_explanation":"shadow-only proxy: promote early public evidence only when non-price evidence plus relative strength beat later confirmation on MFE/MAE; price-only runs are rejected.","selected_by_profile":false,"MFE_90D_pct":4.62,"MAE_90D_pct":-26.59,"score_return_alignment_label":"score_mid_return_low_watch_only","row_validation_status":"valid_for_weight_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R11L6_C02","trigger_id":"R11L6_C02_T5","symbol":"064350","trigger_type":"4B","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":5,"valuation_repricing_score":0,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":34.0,"stage_label_before":"4B","raw_component_scores_after":{"contract_score":7,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":5,"policy_or_regulatory_score":7,"valuation_repricing_score":0,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":56.0,"stage_label_after":"4B","changed_components":["contract_score","relative_strength_score","customer_quality_score","policy_or_regulatory_score","execution_risk_score"],"component_delta_explanation":"shadow-only proxy: promote early public evidence only when non-price evidence plus relative strength beat later confirmation on MFE/MAE; price-only runs are rejected.","selected_by_profile":false,"MFE_90D_pct":2.29,"MAE_90D_pct":-22.62,"score_return_alignment_label":"score_high_return_low_false_positive","row_validation_status":"valid_for_weight_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R11L6_C03","trigger_id":"R11L6_C03_T1","symbol":"041510","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":38.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":56.0,"stage_label_after":"Stage2","changed_components":["relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"shadow-only proxy: promote early public evidence only when non-price evidence plus relative strength beat later confirmation on MFE/MAE; price-only runs are rejected.","selected_by_profile":true,"MFE_90D_pct":78.91,"MAE_90D_pct":-4.88,"score_return_alignment_label":"score_mid_return_high_promote_candidate","row_validation_status":"valid_for_weight_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R11L6_C03","trigger_id":"R11L6_C03_T3","symbol":"041510","trigger_type":"Stage3-Yellow","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":38.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":56.0,"stage_label_after":"Stage3-Yellow","changed_components":["relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"shadow-only proxy: promote early public evidence only when non-price evidence plus relative strength beat later confirmation on MFE/MAE; price-only runs are rejected.","selected_by_profile":false,"MFE_90D_pct":40.54,"MAE_90D_pct":-23.63,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_weight_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R11L6_C03","trigger_id":"R11L6_C03_T5","symbol":"041510","trigger_type":"4B","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":38.0,"stage_label_before":"4B","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":56.0,"stage_label_after":"4B","changed_components":["relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"shadow-only proxy: promote early public evidence only when non-price evidence plus relative strength beat later confirmation on MFE/MAE; price-only runs are rejected.","selected_by_profile":false,"MFE_90D_pct":7.68,"MAE_90D_pct":-41.48,"score_return_alignment_label":"score_high_return_low_false_positive","row_validation_status":"valid_for_weight_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R11L6_C03","trigger_id":"R11L6_C03_T6","symbol":"041510","trigger_type":"4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":38.0,"stage_label_before":"4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":56.0,"stage_label_after":"4C","changed_components":["relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"shadow-only proxy: promote early public evidence only when non-price evidence plus relative strength beat later confirmation on MFE/MAE; price-only runs are rejected.","selected_by_profile":false,"MFE_90D_pct":19.1,"MAE_90D_pct":-22.55,"score_return_alignment_label":"score_high_return_low_false_positive","row_validation_status":"valid_for_rejection_or_overlay_not_positive_weight"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R11L6_C04","trigger_id":"R11L6_C04_T0","symbol":"004690","trigger_type":"Price-only no-evidence run","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":7,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":54.0,"stage_label_before":"Price-only no-evidence run","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":9,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":6},"weighted_score_after":50.0,"stage_label_after":"CorrectReject","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"shadow-only proxy: promote early public evidence only when non-price evidence plus relative strength beat later confirmation on MFE/MAE; price-only runs are rejected.","selected_by_profile":false,"MFE_90D_pct":47.37,"MAE_90D_pct":-4.51,"score_return_alignment_label":"score_low_return_high_price_only_reject","row_validation_status":"valid_for_rejection_or_overlay_not_positive_weight"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R11L6_C04","trigger_id":"R11L6_C04_T5","symbol":"004690","trigger_type":"4B","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":7,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":54.0,"stage_label_before":"4B","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":9,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":6},"weighted_score_after":50.0,"stage_label_after":"4B","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"shadow-only proxy: promote early public evidence only when non-price evidence plus relative strength beat later confirmation on MFE/MAE; price-only runs are rejected.","selected_by_profile":false,"MFE_90D_pct":2.14,"MAE_90D_pct":-81.33,"score_return_alignment_label":"score_low_return_low_correct_reject","row_validation_status":"valid_for_weight_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R11L6_C04","trigger_id":"R11L6_C04_T6","symbol":"004690","trigger_type":"4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":7,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":54.0,"stage_label_before":"4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":9,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":6},"weighted_score_after":50.0,"stage_label_after":"4C","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"shadow-only proxy: promote early public evidence only when non-price evidence plus relative strength beat later confirmation on MFE/MAE; price-only runs are rejected.","selected_by_profile":false,"MFE_90D_pct":0.0,"MAE_90D_pct":-72.51,"score_return_alignment_label":"score_high_return_low_false_positive","row_validation_status":"valid_for_rejection_or_overlay_not_positive_weight"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R11L6_C05","trigger_id":"R11L6_C05_T1","symbol":"112610","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":5,"valuation_repricing_score":3,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":32.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":5,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":54.0,"stage_label_after":"Stage2","changed_components":["relative_strength_score","customer_quality_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"shadow-only proxy: promote early public evidence only when non-price evidence plus relative strength beat later confirmation on MFE/MAE; price-only runs are rejected.","selected_by_profile":true,"MFE_90D_pct":51.52,"MAE_90D_pct":-7.1,"score_return_alignment_label":"score_mid_return_high_promote_candidate","row_validation_status":"valid_for_weight_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R11L6_C05","trigger_id":"R11L6_C05_T2","symbol":"112610","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":5,"valuation_repricing_score":3,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":32.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":5,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":54.0,"stage_label_after":"Stage2-Actionable","changed_components":["relative_strength_score","customer_quality_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"shadow-only proxy: promote early public evidence only when non-price evidence plus relative strength beat later confirmation on MFE/MAE; price-only runs are rejected.","selected_by_profile":false,"MFE_90D_pct":22.89,"MAE_90D_pct":-12.9,"score_return_alignment_label":"score_high_return_high","row_validation_status":"valid_for_weight_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R11L6_C05","trigger_id":"R11L6_C05_T5","symbol":"112610","trigger_type":"4B","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":5,"valuation_repricing_score":3,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":32.0,"stage_label_before":"4B","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":5,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":54.0,"stage_label_after":"4B","changed_components":["relative_strength_score","customer_quality_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"shadow-only proxy: promote early public evidence only when non-price evidence plus relative strength beat later confirmation on MFE/MAE; price-only runs are rejected.","selected_by_profile":false,"MFE_90D_pct":2.29,"MAE_90D_pct":-15.13,"score_return_alignment_label":"score_high_return_low_false_positive","row_validation_status":"valid_for_weight_calibration"}
```

### 27.5 Profile comparison rows CSV

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,verdict
profile_comparison,baseline_current_proxy,5,4,4,19.69,16.8,-22.93,-22.96,33.3,75.0,0.25,3,2,"reference; waits for final confirmation/event premium too often"
profile_comparison,stage2_actionable_early_evidence_plus,5,4,4,57.84,58.9,-7.69,-5.99,100.0,0.0,0.0,0,0,"best; promotes early non-price policy/geopolitical evidence with RS guard"
profile_comparison,stage3_yellow_entry_relaxed,5,4,4,47.21,46.03,-12.48,-10.2,75.0,25.0,0.1,1,1,improved but weaker than Stage2-actionable guard
profile_comparison,green_confirmation_timing_relaxed,5,4,4,30.9,28.44,-17.2,-17.8,50.0,50.0,0.15,2,1,"cautious; Green still late in defense cases"
profile_comparison,four_b_peak_timing_tuned,5,4,0,overlay,overlay,overlay,overlay,overlay,overlay,overlay,overlay,overlay,keeps 4B as overlay and rejects price-only full 4B
profile_comparison,four_c_thesis_break_earlier,5,2,0,overlay,overlay,overlay,overlay,overlay,overlay,overlay,overlay,overlay,"insufficient hard early 4C proof; no broad delta"
```

### 27.6 Shadow weight CSV

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_public_policy_or_geopolitical_evidence,0,2,+2,Early policy/geopolitical evidence produced higher MFE with lower or acceptable MAE than confirmations.,"baseline avg MFE90 19.69 / MAE90 -22.93 -> selected profile avg MFE90 57.84 / MAE90 -7.69",R11L6_C01_T1|R11L6_C02_T1|R11L6_C05_T1,3,"shadow-only; requires non-price evidence plus OHLC relative strength"
shadow_weight,control_premium_event_stage2,0,2,+2,SM Stage2 event premium had excellent MFE/MAE before explicit tender cap.,SM early event MFE90 78.91 / MAE90 -4.88 vs tender-cap 4B MFE90 7.68 / MAE90 -41.48,R11L6_C03_T1|R11L6_C03_T5,2,"shadow-only; do not generalize beyond event premium"
shadow_weight,price_only_blowoff_rejection,-1,-3,-2,"Samchully shows high MFE without evidence; should not train positive Stage2/Green weights.","Price-only run MFE180 288.72 but later drawdown after peak -81.72; use as rejection guard.",R11L6_C04_T0|R11L6_C04_T5,1,"negative guard; not a positive promotion sample"
shadow_weight,four_b_non_price_evidence_requirement,1,3,+2,4B should not be price-only unless paired with valuation/event cap or revision/contract slowdown.,"SM tender-cap worked; Samchully price-only proximity would overfit without evidence.",R11L6_C03_T5|R11L6_C04_T5|R11L6_C05_T5,3,shadow-only overlay
shadow_weight,hard_4c_early_break_delta,0,0,0,Only SM partial 4C and Samchully late hard 4C were validated.,"No broad early hard-gate proof; keep delta zero.",R11L6_C03_T6|R11L6_C04_T6,2,no gate change
```

### 27.7 Optimization decision rows JSONL

```jsonl
{"row_type":"optimization_decision","decision_id":"R11L6_D01","hypothesis":"Stage2 policy/geopolitical evidence should be promoted before final contract/law confirmation when relative strength is already present.","tested_cases":["R11L6_C01","R11L6_C02","R11L6_C05"],"tested_trigger_ids":["R11L6_C01_T1","R11L6_C02_T1","R11L6_C05_T1"],"baseline_profile":"baseline_current_proxy","selected_profile":"r11_stage2_event_policy_early_guard","backtest_result_summary":"Early-evidence selected profile improved avg MFE90 from 19.69 to 57.84 and improved avg MAE90 from -22.93 to -7.69 across non-price evidence cases.","accepted_or_rejected":"accepted","delta_magnitude":"+2","why_not_larger_delta":"R11 sample is still event-heavy and sector-diverse; false-positive guard must be tested in R1/R2/R3.","risks":"Policy headline rallies can reverse if execution/order conversion fails.","next_validation_needed":"Add a failed policy-rerating case with good initial headline but weak follow-through."}
{"row_type":"optimization_decision","decision_id":"R11L6_D02","hypothesis":"Price-only blowoff must not be upgraded to Stage2-Actionable even with very large MFE.","tested_cases":["R11L6_C04"],"tested_trigger_ids":["R11L6_C04_T0","R11L6_C04_T5"],"baseline_profile":"baseline_current_proxy","selected_profile":"r11_stage2_event_policy_early_guard","backtest_result_summary":"Samchully generated extreme MFE but no usable non-price evidence; later drawdown after peak reached -81.72, so the correct action is rejection/4B watch, not promotion.","accepted_or_rejected":"accepted","delta_magnitude":"-2","why_not_larger_delta":"Single case; keep as guard until more price-only manipulation or forced-liquidation cases are validated.","risks":"Over-filtering genuine low-liquidity structural reratings.","next_validation_needed":"Find non-manipulation low-liquidity rerating counterexample."}
{"row_type":"optimization_decision","decision_id":"R11L6_D03","hypothesis":"4B should split price-only proximity from full-window non-price evidence.","tested_cases":["R11L6_C01","R11L6_C02","R11L6_C03","R11L6_C04","R11L6_C05"],"tested_trigger_ids":["R11L6_C01_T5","R11L6_C02_T5","R11L6_C03_T5","R11L6_C04_T5","R11L6_C05_T5"],"baseline_profile":"baseline_current_proxy","selected_profile":"four_b_peak_timing_tuned","backtest_result_summary":"SM tender cap and CS/Hanwha peak-proximity were useful; Samchully price-only peak proximity without non-price evidence must be kept as watch-only.","accepted_or_rejected":"accepted","delta_magnitude":"+2 non-price evidence requirement","why_not_larger_delta":"Only one clean control-premium 4B case and one price-only rejection case.","risks":"May miss pure liquidity unwind when no non-price warning exists.","next_validation_needed":"More CFD/CB/lockup/short-squeeze unwind cases."}
```

### 27.8 Narrative-only rows JSONL

```jsonl
{"row_type":"narrative_only","case_id":"R11L6_C04","symbol":"004690","reason":"price_path_available_but_positive_non_price_evidence_not_accepted; used only for price-only rejection and 4C-late audit","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration_positive_promotion"}
```

### 27.9 Aggregate metric rows CSV

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,4,4,57.84,58.9,-7.69,-5.99,mixed,not_applicable,not_applicable,"representative rows only; non-price evidence required"
aggregate_metric,Stage3-Green,1,1,10.71,10.71,-32.91,-32.91,0.265,not_applicable,not_applicable,confirmation was too late in Hanwha sample
aggregate_metric,Stage2-Actionable,2,2,13.76,13.76,-19.75,-19.75,mixed,not_applicable,not_applicable,late momentum/law-signing labels are useful but inferior to earliest evidence
aggregate_metric,Stage3-Yellow,1,1,40.54,40.54,-23.63,-23.63,0.5,not_applicable,not_applicable,works for control premium but gives away early edge
aggregate_metric,Price-only no-evidence run,1,1,47.37,47.37,-4.51,-4.51,not_applicable,not_applicable,not_applicable,not for positive score calibration
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

| field | value |
| --- | --- |
| current_round | R11 |
| completed_loop | 6 |
| next_round | R12 |
| next_loop | 6 |
| next_sector | 농업·생활서비스·기타 |
| carry_forward_risks | need more hard early 4C cases; need failed policy-rerating cases with good headline but weak execution; need low-liquidity non-manipulation counterexample to Samchully |

## 30. Source Notes

This file uses stock-web only for OHLC. It does not access or patch the `stock_agent` repository. Loop 6 completion note: no production scoring changed; all score/gate deltas are shadow-only and based on calibration_usable stock-web OHLC rows. Evidence source and price source are separated. Returns are percentage units, not decimal units. Corporate-action contamination was checked through symbol profile fields and all selected 180D calibration windows are marked clean.

External evidence references used for trigger labeling include public Korea–Poland defense export framework/executive-contract records, public SM Entertainment tender-offer/governance-event coverage, public Inflation Reduction Act signing/policy records, and public coverage of the Samchully price-only collapse/forced-liquidation episode. These are used only to label what was knowable at trigger date; all forward returns come from stock-web OHLC rows.


<!-- loop6_validation_counts: cases=5; triggers=17; score_simulations=17; profiles=6; unique_shadow_weight_axes=5 -->
