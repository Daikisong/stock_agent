# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata

```text
research_session = historical_calibration_after_stock_web_ohlc_breakthrough
round = R12
loop = 3
sector = 농업·생활서비스·기타
output_file = e2r_stock_web_historical_calibration_round_R12_loop_3_agriculture_life_services_other_research.md
stock_agent_repo_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
current_stock_discovery_allowed = false
```

이번 파일은 현재 종목 추천이나 live 후보 스캔이 아니다. 직전 산출물의 `next_round=R12`를 이어 받아, 농업·사료·식량가격 이벤트 계열에서 과거 trigger-level backtest만 수행했다.

## 1. Round Scope

- round: R12 = 농업·생활서비스·기타
- loop: 3
- tested archetype cluster: feed / grain / food-supply shock
- calibration-usable cases: 3
- calibration-usable trigger rows: 12
- score profile candidates: 6
- selected shadow profile: `r12_stage2_feed_policy_shock_guarded`

이번 R12는 식량·사료 shock의 “빨리 붙는 event premium”을 검증했다. 결과적으로 Green 확인은 일부 사례에서 너무 늦었고, Stage2-Actionable은 실제 가격경로에서 더 좋은 기대값을 보였다. 단, 이 라운드는 농업 외 생활서비스 전반을 검증하지 못했다.

## 2. Stock-Web OHLC Input / Price Source Validation

Stock-web manifest는 `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `max_date=2026-02-20`, `tradable_row_count=14,354,401`, `raw_row_count=15,214,118`, `symbol_count=5,414`, `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`를 기록한다. fileciteturn585file0

Schema 기준으로 tradable shard의 column은 `d,o,h,l,c,v,a,mc,s,m`이며, `MFE_N_pct=(max high from entry_date through N tradable rows / entry_price - 1) * 100`, `MAE_N_pct=(min low from entry_date through N tradable rows / entry_price - 1) * 100`다. fileciteturn586file0 Universe 파일은 code, latest name, first/last date, trading_day_count, markets, latest close, status, profile path 구조를 사용한다. fileciteturn587file0

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 3. Historical Eligibility Gate

All selected trigger rows satisfy:

```text
entry_date in stock-web tradable shard = true
forward 180D available by manifest max_date = true
OHLCV present = true
MFE/MAE 30D/90D/180D computed = true
corporate-action-contaminated 180D window = false
```

Profile checks:

| symbol | company | profile | corporate_action_candidate_dates | status |
| --- | --- | --- | --- | --- |
| 005860 | 한일사료 | atlas/symbol_profiles/005/005860.json | 1997-01-30|1997-02-13|1999-07-14|1999-10-11|2000-01-10|2016-12-22 | 2022 window clean |
| 218150 | 미래생명자원 | atlas/symbol_profiles/218/218150.json | 2017-12-28 | 2022 window clean |
| 027710 | 팜스토리 | atlas/symbol_profiles/027/027710.json | 1999-10-25|2000-05-26|2000-06-09|2005-10-25|2011-01-21|2019-12-13 | 2022 window clean |

한일사료 profile은 2022년 shard와 2023~2026년 shard가 존재하며, 2016-12-22 이후 corporate-action candidate가 없다. fileciteturn588file0 미래생명자원 profile의 corporate-action candidate는 2017-12-28로 이번 2022 window 밖이다. fileciteturn589file0 팜스토리 profile의 마지막 corporate-action candidate는 2019-12-13으로 이번 2022 window 밖이다. fileciteturn593file0

## 4. Canonical Archetypes Tested

```text
FEED_GRAIN_SUPPLY_SHOCK
FEED_ADDITIVE_GRAIN_SUPPLY_SHOCK
FOOD_FEED_CHAIN_GRAIN_SHOCK
EVENT_PREMIUM_OVERHEAT_4B
```

Public evidence context: Russia’s full-scale invasion of Ukraine began on 2022-02-24, and the event created an immediately observable global grain/food-supply shock. citeturn661643search8 FAO reported that March 2022 global food prices reached a record high, driven materially by the Russian invasion and disruptions to Ukrainian/Russian agricultural exports. citeturn661643news3 Russia and Ukraine were major wheat/sunflower oil suppliers, and the conflict threatened grain and food commodity markets. citeturn661643search10

## 5. Case Selection Summary

| case_id | symbol | company_name | case_type | primary_archetype | best_trigger | calibration_usable | score_price_alignment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R12L3_C01_005860_FEED_GRAIN_SHOCK | 005860 | 한일사료 | structural_success_with_event_premium | FEED_GRAIN_SUPPLY_SHOCK | R12L3_C01_T2 | True | stage2_actionable_outperformed_late_confirmation |
| R12L3_C02_218150_FEED_ADDITIVE_GRAIN_SHOCK | 218150 | 미래생명자원 | stage2_promote_candidate_but_fast_overheat | FEED_ADDITIVE_GRAIN_SUPPLY_SHOCK | R12L3_C02_T2 | True | stage2_actionable_ok_green_late_4B_needed |
| R12L3_C03_027710_FEED_FOOD_CHAIN_SHOCK | 027710 | 팜스토리 | cyclical_success_then_overheat_drawdown | FOOD_FEED_CHAIN_GRAIN_SHOCK | R12L3_C03_T2 | True | stage2_actionable_outperformed_late_confirmation |

## 6. Evidence Source Map

| evidence_id | date | type | used_for | note |
| --- | --- | --- | --- | --- |
| EVID_R12_GLOBAL_20220224 | 2022-02-24 | global_news | Stage2 | Russia-Ukraine invasion; public food/grain supply shock |
| EVID_R12_FAO_202204 | 2022-04-08 | FAO/news | Stage2-Actionable/Stage3 | Food Price Index all-time high in March 2022, war-driven |
| EVID_R12_PRICE_RS | 2022-03~04 | stock-web OHLC relative strength | Stage2-Actionable/Green | price-volume expansion after public macro evidence |
| EVID_R12_4B_PRICE | 2022-04~05 | price-only 4B | 4B overlay | blowoff / local peak proximity; not full 4B without non-price evidence |

## 7. Price Data Source Map

| symbol | years_used | profile | price_shard | source_rows |
| --- | --- | --- | --- | --- |
| 005860 | 2022, 2023 spot-check | atlas/symbol_profiles/005/005860.json | atlas/ohlcv_tradable_by_symbol_year/005/005860/2022.csv | 2022-02-24, 2022-03-21, 2022-04-15, 2022-04-25, 2022-12-29 |
| 218150 | 2022 | atlas/symbol_profiles/218/218150.json | atlas/ohlcv_tradable_by_symbol_year/218/218150/2022.csv | 2022-02-24, 2022-03-02, 2022-03-22, 2022-04-19, 2022-12-29 |
| 027710 | 2022 | atlas/symbol_profiles/027/027710.json | atlas/ohlcv_tradable_by_symbol_year/027/027710/2022.csv | 2022-02-24, 2022-04-15, 2022-04-25, 2022-04-27, 2022-12-29 |

Price anchors: 한일사료 2022-02-24 close 2,555, 2022-03-21 close 2,795, 2022-04-25 high 15,850, 2022-12-29 low 4,170 are in the stock-web 2022 shard. fileciteturn594file0 fileciteturn595file0 미래생명자원 2022-02-24 close 8,090, 2022-03-02 close 8,820, 2022-04-19 high 12,900, and 2022-12-29 low 3,800 are in the stock-web 2022 shard. fileciteturn597file0 fileciteturn598file0 팜스토리 2022-02-24 close 3,040, 2022-04-15 close 2,950, 2022-04-27 high 6,330, and 2022-12-29 low 1,630 are in the stock-web 2022 shard. fileciteturn599file0 fileciteturn600file0

## 8. Case-by-Case Trigger Grid

| case_id | trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R12L3_C01_005860_FEED_GRAIN_SHOCK | R12L3_C01_T1 | 005860 | Stage2 | 2022-02-24 | 2022-02-24 | 2555 | Russia-Ukraine invasion day; global grain/feed supply shock became public and directly mar... |
| R12L3_C01_005860_FEED_GRAIN_SHOCK | R12L3_C01_T2 | 005860 | Stage2-Actionable | 2022-03-21 | 2022-03-21 | 2795 | grain/feed shock persisted; stock-web row shows volume expansion and first sustained break... |
| R12L3_C01_005860_FEED_GRAIN_SHOCK | R12L3_C01_T3 | 005860 | Stage3-Green | 2022-04-15 | 2022-04-15 | 4680 | public food-price narrative + repeated relative-strength closure; Green confirmation after... |
| R12L3_C01_005860_FEED_GRAIN_SHOCK | R12L3_C01_T4 | 005860 | Stage4B | 2022-04-25 | 2022-04-25 | 13350 | blowoff day after sequential limit-up style expansion; price-only overheat overlay near lo... |
| R12L3_C02_218150_FEED_ADDITIVE_GRAIN_SHOCK | R12L3_C02_T1 | 218150 | Stage2 | 2022-02-24 | 2022-02-24 | 8090 | Russia-Ukraine full invasion day; feed additive / animal nutrition proxy captured food-sec... |
| R12L3_C02_218150_FEED_ADDITIVE_GRAIN_SHOCK | R12L3_C02_T2 | 218150 | Stage2-Actionable | 2022-03-02 | 2022-03-02 | 8820 | post-invasion continuation gap plus relative-strength confirmation after reset from 2022-0... |
| R12L3_C02_218150_FEED_ADDITIVE_GRAIN_SHOCK | R12L3_C02_T3 | 218150 | Stage3-Green | 2022-03-22 | 2022-03-22 | 11750 | second breakout and public feed/food-security narrative fully priced; Green captures confi... |
| R12L3_C02_218150_FEED_ADDITIVE_GRAIN_SHOCK | R12L3_C02_T4 | 218150 | Stage4B | 2022-04-19 | 2022-04-19 | 11550 | local/full cycle peak day; price-only overheat after repeated public food-security narrati... |
| R12L3_C03_027710_FEED_FOOD_CHAIN_SHOCK | R12L3_C03_T1 | 027710 | Stage2 | 2022-02-24 | 2022-02-24 | 3040 | global grain/feed shock; feed-food chain proxy participates but first leg is less explosiv... |
| R12L3_C03_027710_FEED_FOOD_CHAIN_SHOCK | R12L3_C03_T2 | 027710 | Stage2-Actionable | 2022-04-15 | 2022-04-15 | 2950 | second wave relative-strength close after FAO record food-price confirmation; still before... |
| R12L3_C03_027710_FEED_FOOD_CHAIN_SHOCK | R12L3_C03_T3 | 027710 | Stage3-Yellow | 2022-04-25 | 2022-04-25 | 4095 | food-chain proxy finally reaches high-volume breakout; evidence sufficient for Yellow, but... |
| R12L3_C03_027710_FEED_FOOD_CHAIN_SHOCK | R12L3_C03_T4 | 027710 | Stage4B | 2022-04-27 | 2022-04-27 | 4335 | intraday high made full-window peak but close had already fallen; 4B is late if triggered ... |

## 9. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | trigger_outcome_label | dedupe_for_aggregate | aggregate_group_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R12L3_C01_T1 | 005860 | Stage2 | 2022-02-24 | 2555 | 85.5 | 520.4 | 520.4 | -18.6 | -18.6 | -18.6 | 2022-04-25 | 15850 | -73.7 | missed_structural | True | representative |
| R12L3_C01_T2 | 005860 | Stage2-Actionable | 2022-03-21 | 2795 | 467.1 | 467.1 | 467.1 | -20.6 | -20.6 | -20.6 | 2022-04-25 | 15850 | -73.7 | excellent_entry | True | representative |
| R12L3_C01_T3 | 005860 | Stage3-Green | 2022-04-15 | 4680 | 238.7 | 238.7 | 238.7 | -19.9 | -19.9 | -19.9 | 2022-04-25 | 15850 | -73.7 | good_but_later_than_actionable | True | representative |
| R12L3_C01_T4 | 005860 | Stage4B | 2022-04-25 | 13350 | 18.7 | 18.7 | 18.7 | -45.1 | -60.2 | -68.8 | 2022-04-25 | 15850 | -73.7 | 4B_watch_success | False | 4B_overlay_only |
| R12L3_C02_T1 | 218150 | Stage2 | 2022-02-24 | 8090 | 53.3 | 59.5 | 59.5 | -16.8 | -14.7 | -42.6 | 2022-04-19 | 12900 | -70.5 | good_entry | True | representative |
| R12L3_C02_T2 | 218150 | Stage2-Actionable | 2022-03-02 | 8820 | 40.6 | 46.3 | 46.3 | -15.9 | -21.8 | -47.3 | 2022-04-19 | 12900 | -70.5 | good_entry | True | representative |
| R12L3_C02_T3 | 218150 | Stage3-Green | 2022-03-22 | 11750 | 9.8 | 9.8 | 9.8 | -14.5 | -41.3 | -60.5 | 2022-04-19 | 12900 | -70.5 | late_entry | True | representative |
| R12L3_C02_T4 | 218150 | Stage4B | 2022-04-19 | 11550 | 11.7 | 11.7 | 11.7 | -35.5 | -40.3 | -59.8 | 2022-04-19 | 12900 | -70.5 | 4B_watch_success | False | 4B_overlay_only |
| R12L3_C03_T1 | 027710 | Stage2 | 2022-02-24 | 3040 | 15.1 | 75.0 | 75.0 | -20.9 | -20.9 | -38.5 | 2022-04-27 | 6330 | -74.2 | stage2_promote_candidate | True | representative |
| R12L3_C03_T2 | 027710 | Stage2-Actionable | 2022-04-15 | 2950 | 114.6 | 114.6 | 114.6 | -7.3 | -18.8 | -36.6 | 2022-04-27 | 6330 | -74.2 | excellent_entry | True | representative |
| R12L3_C03_T3 | 027710 | Stage3-Yellow | 2022-04-25 | 4095 | 54.6 | 54.6 | 54.6 | -15.4 | -41.5 | -54.3 | 2022-04-27 | 6330 | -74.2 | good_but_late_yellow | True | representative |
| R12L3_C03_T4 | 027710 | Stage4B | 2022-04-27 | 4335 | 46.0 | 46.0 | 46.0 | -20.1 | -44.8 | -56.9 | 2022-04-27 | 6330 | -74.2 | 4B_watch_late | False | 4B_overlay_only |

## 10. 1D Price Path Summaries

### 005860 한일사료 — best Stage2-Actionable trigger R12L3_C01_T2

```text
entry = 2022-03-21 close 2,795
D+1  2022-03-22 close 3,630 / high-to-date 3,630 / low-to-date 2,220
D+2  2022-03-23 close 3,995 / high-to-date 4,680 / low-to-date 2,220
D+5  2022-03-28 close 4,110 / high-to-date 4,740 / low-to-date 2,220
D+20 approx 2022-04-19 close 7,900 / high-to-date 7,900 / low-to-date 2,220
D+30 approx 2022-05-02 close 9,330 / high-to-date 15,850 / low-to-date 2,220
D+60 approx 2022-06-20 close 9,870 / high-to-date 15,850 / low-to-date 2,220
D+90 approx 2022-07-29 close 5,470 / high-to-date 15,850 / low-to-date 2,220
D+180 approx 2022-12-29 close 4,210 / high-to-date 15,850 / low-to-date 2,220
```

### 218150 미래생명자원 — best Stage2-Actionable trigger R12L3_C02_T2

```text
entry = 2022-03-02 close 8,820
D+1  2022-03-03 close 9,390 / high-to-date 10,450 / low-to-date 7,420
D+5  2022-03-08 close 8,520 / high-to-date 10,450 / low-to-date 7,420
D+10 approx 2022-03-16 close 7,990 / high-to-date 10,450 / low-to-date 7,420
D+20 approx 2022-03-31 close 10,200 / high-to-date 12,400 / low-to-date 7,420
D+30 approx 2022-04-14 close 10,950 / high-to-date 12,900 / low-to-date 7,420
D+60 approx 2022-05-31 close 8,160 / high-to-date 12,900 / low-to-date 7,300
D+90 approx 2022-07-12 close 6,050 / high-to-date 12,900 / low-to-date 5,930
D+180 approx 2022-12-29 close 3,850 / high-to-date 12,900 / low-to-date 3,800
```

### 027710 팜스토리 — best Stage2-Actionable trigger R12L3_C03_T2

```text
entry = 2022-04-15 close 2,950
D+1  2022-04-18 close 3,010 / high-to-date 3,220 / low-to-date 2,765
D+2  2022-04-19 close 3,240 / high-to-date 3,415 / low-to-date 2,765
D+5  2022-04-22 close 3,150 / high-to-date 3,415 / low-to-date 2,765
D+10 approx 2022-05-02 close 4,620 / high-to-date 6,330 / low-to-date 2,765
D+20 approx 2022-05-17 close 4,045 / high-to-date 6,330 / low-to-date 2,765
D+30 approx 2022-05-31 close 4,005 / high-to-date 6,330 / low-to-date 2,735
D+60 approx 2022-07-14 close 2,655 / high-to-date 6,330 / low-to-date 2,635
D+90 approx 2022-08-31 close 2,500 / high-to-date 6,330 / low-to-date 2,395
D+180 approx 2022-12-29 close 1,640 / high-to-date 6,330 / low-to-date 1,630
```

## 11. Case Trigger Comparison

| case_id | symbol | best_actual_trigger | baseline_selected_trigger | after_selected_trigger | baseline_entry_date | after_entry_date | baseline_MFE_90D_pct | after_MFE_90D_pct | baseline_MAE_90D_pct | after_MAE_90D_pct | return_improvement_90D_pct | risk_change_90D_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R12L3_C01_005860_FEED_GRAIN_SHOCK | 005860 | R12L3_C01_T2 | R12L3_C01_T3 | R12L3_C01_T2 | 2022-04-15 | 2022-03-21 | 238.7 | 467.1 | -19.9 | -20.6 | 228.4 | -0.7 |
| R12L3_C02_218150_FEED_ADDITIVE_GRAIN_SHOCK | 218150 | R12L3_C02_T2 | R12L3_C02_T3 | R12L3_C02_T2 | 2022-03-22 | 2022-03-02 | 9.8 | 46.3 | -41.3 | -21.8 | 36.5 | 19.5 |
| R12L3_C03_027710_FEED_FOOD_CHAIN_SHOCK | 027710 | R12L3_C03_T2 | R12L3_C03_T3 | R12L3_C03_T2 | 2022-04-25 | 2022-04-15 | 54.6 | 114.6 | -41.5 | -18.8 | 60.0 | 22.7 |

Interpretation: the selected shadow profile moves the machine from “confirmation after the train has left the station” to “boarding while the macro shock and price-volume evidence are already visible.” It is not just earlier; it is earlier with the same public evidence available to the market.

## 12. Stage2 → Stage4 Audit

- 한일사료: Stage2-Actionable after 2022-03-21 produced MFE90 467.1 with MAE90 -20.6. Green at 2022-04-15 still worked, but it surrendered 228.4 percentage points of MFE90 versus Actionable.
- 미래생명자원: Stage2-Actionable at 2022-03-02 produced MFE90 46.3; Green at 2022-03-22 produced only 9.8 and quickly became late-event exposure.
- 팜스토리: Stage2 on 2022-02-24 was only a promote candidate. The better entry was the second-wave Actionable trigger on 2022-04-15, before the final 2022-04-27 peak.

R12 rule: public food-supply shock alone is not enough. It becomes Stage2-Actionable only when paired with stock-web relative-strength expansion and no immediate 4B overheat.

## 13. Stage3 Yellow / Green Lateness Audit

| case | actionable_entry | green_entry | green_or_yellow_entry | peak | green_lateness_ratio | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| 한일사료 | 2795 | 4680 |  | 15850 | 0.144 | Green not catastrophic, but Actionable much better |
| 미래생명자원 | 8820 | 11750 |  | 12900 | 0.718 | Green captured upside too late |
| 팜스토리 | 2950 |  | 4095 | 6330 | 0.339 | Yellow usable but not as strong as Actionable |

## 14. 4B Timing Audit

| case | 4B_trigger | entry | stage2_actionable_entry | peak | local_proximity | full_proximity | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 한일사료 | 2022-04-25 | 13350 | 2795 | 15850 | 0.809 | 0.809 | good timing but price-only |
| 미래생명자원 | 2022-04-19 | 11550 | 8820 | 12900 | 0.669 | 0.669 | borderline good watch |
| 팜스토리 | 2022-04-27 | 4335 | 2950 | 6330 | 0.41 | 0.41 | close-based 4B was late after intraday peak |

R12 4B conclusion: price-only 4B is valid as a watch overlay, not a full hard exit. A full 4B should require non-price evidence such as valuation blowoff + revision slowdown, dilution/CB, lockup/overhang, or clear margin/backlog deterioration.

## 15. 4C Protection Audit

Hard 4C is not validated in this round. The observed declines were mostly event-premium fade after food-shock blowoff. No distinct public thesis-break evidence was validated before the drawdowns. Therefore:

```text
four_c_hard_gate_delta = 0
four_c_protection_label = hard_4c_not_confirmed
```

## 16. Baseline Score Simulation

Baseline current proxy behavior:

```text
baseline_current_proxy:
- tends to wait for repeated relative strength and public narrative closure
- selects Stage3-Green or late Yellow in these event-premium shocks
- misses the best Stage2-Actionable entries
```

| case_id | trigger_id | symbol | trigger_type | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | score_return_alignment_label |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R12L3_C01_005860_FEED_GRAIN_SHOCK | R12L3_C01_T1 | 005860 | Stage2 | 26 | Stage2 | 31 | Stage2 | 520.4 | -18.6 | score_low_return_high_missed_structural |
| R12L3_C01_005860_FEED_GRAIN_SHOCK | R12L3_C01_T2 | 005860 | Stage2-Actionable | 44 | Stage3-Yellow | 52 | Stage3-Yellow | 467.1 | -20.6 | score_high_return_high |
| R12L3_C01_005860_FEED_GRAIN_SHOCK | R12L3_C01_T3 | 005860 | Stage3-Green | 56 | Stage3-Green | 64 | Stage3-Yellow | 238.7 | -19.9 | score_high_return_high |
| R12L3_C01_005860_FEED_GRAIN_SHOCK | R12L3_C01_T4 | 005860 | Stage4B | 62 | Stage3+4B-watch | 68 | Stage3+4B-watch | 18.7 | -60.2 | score_high_return_low_false_positive |
| R12L3_C02_218150_FEED_ADDITIVE_GRAIN_SHOCK | R12L3_C02_T1 | 218150 | Stage2 | 34 | Stage2-Actionable | 40 | Stage2-Actionable | 59.5 | -14.7 | score_low_return_high_missed_structural |
| R12L3_C02_218150_FEED_ADDITIVE_GRAIN_SHOCK | R12L3_C02_T2 | 218150 | Stage2-Actionable | 46 | Stage3-Yellow | 53 | Stage3-Yellow | 46.3 | -21.8 | score_high_return_high |
| R12L3_C02_218150_FEED_ADDITIVE_GRAIN_SHOCK | R12L3_C02_T3 | 218150 | Stage3-Green | 58 | Stage3-Green | 66 | Stage3-Yellow | 9.8 | -41.3 | score_high_return_low_false_positive |
| R12L3_C02_218150_FEED_ADDITIVE_GRAIN_SHOCK | R12L3_C02_T4 | 218150 | Stage4B | 58 | Stage3+4B-watch | 64 | Stage3+4B-watch | 11.7 | -40.3 | score_high_return_low_false_positive |
| R12L3_C03_027710_FEED_FOOD_CHAIN_SHOCK | R12L3_C03_T1 | 027710 | Stage2 | 28 | Stage2 | 34 | Stage2 | 75.0 | -20.9 | score_low_return_high_missed_structural |
| R12L3_C03_027710_FEED_FOOD_CHAIN_SHOCK | R12L3_C03_T2 | 027710 | Stage2-Actionable | 44 | Stage3-Yellow | 52 | Stage3-Yellow | 114.6 | -18.8 | score_high_return_high |
| R12L3_C03_027710_FEED_FOOD_CHAIN_SHOCK | R12L3_C03_T3 | 027710 | Stage3-Yellow | 52 | Stage3-Green | 60 | Stage3-Yellow | 54.6 | -41.5 | score_high_return_high |
| R12L3_C03_027710_FEED_FOOD_CHAIN_SHOCK | R12L3_C03_T4 | 027710 | Stage4B | 56 | Stage3+4B-watch | 62 | Stage3+4B-watch | 46.0 | -44.8 | score_high_return_high |

## 17. Shadow Profile Optimization Loop

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,3,3,3,101.0,54.6,-34.2,-41.3,101.0,-44.9,1.0,1.0,0.33,2,2,0.4,not_mixed_with_entry_profiles,not_mixed_with_entry_profiles,reference; catches confirmation but loses early upside and tolerates late entries
profile_comparison,r12_stage2_feed_policy_shock_guarded,3,3,3,209.3,114.6,-20.4,-20.6,209.3,-34.8,1.0,1.0,0.0,0,0,not_selected_as_green,overlay_only,overlay_only,best shadow profile; earlier entry improves average MFE90 while reducing average MAE90 severity
profile_comparison,stage3_yellow_entry_relaxed,3,3,3,189.3,54.6,-28.0,-21.8,189.3,-40.7,1.0,1.0,0.0,1,1,0.34,overlay_only,overlay_only,usable but less clean than Stage2-Actionable because 미래생명자원 Green-like trigger is already late
profile_comparison,green_confirmation_timing_relaxed,3,3,3,101.0,54.6,-34.2,-41.3,101.0,-44.9,0.67,1.0,0.33,2,2,0.4,overlay_only,overlay_only,reject broad Green relaxation; fixes little and still accepts late event premium
profile_comparison,four_b_peak_timing_tuned,3,3,0,25.5,18.7,-48.4,-44.8,25.5,-61.8,0.33,1.0,0.0,0,0,overlay,0.6,0.6,4B overlay should be watch-only unless non-price 4B evidence exists; price-only works best near 0.7~1.0
profile_comparison,four_c_thesis_break_earlier,3,0,0,not_validated,not_validated,not_validated,not_validated,not_validated,not_validated,not_validated,not_validated,not_validated,not_validated,not_validated,not_validated,not_validated,not_validated,hard 4C not validated in this round; no 4C hard-gate delta
```

Best profile: `r12_stage2_feed_policy_shock_guarded`.

Mechanism: macro shock is like a floodgate. The first drip is news; the usable signal is when water pressure appears in the price-volume tape. But if the water is already spraying everywhere, that is not entry confirmation anymore—it is 4B watch.

## 18. Before / After Backtest Comparison

The selected profile improved average MFE90 from 101.0% to 209.3% and improved average MAE90 from -34.2% to -20.4%. The improvement is concentrated in one large missed structural event (한일사료), but all three cases favored earlier Actionable selection over late Green/Yellow confirmation.

| case_id | symbol | baseline_entry_price | after_entry_price | baseline_MFE_180D_pct | after_MFE_180D_pct | baseline_MAE_180D_pct | after_MAE_180D_pct | reason_after_profile_selected |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R12L3_C01_005860_FEED_GRAIN_SHOCK | 005860 | 4680 | 2795 | 238.7 | 467.1 | -19.9 | -20.6 | early policy/feed shock plus relative strength beat late confirmation |
| R12L3_C02_218150_FEED_ADDITIVE_GRAIN_SHOCK | 218150 | 11750 | 8820 | 9.8 | 46.3 | -60.5 | -47.3 | early policy/feed shock plus relative strength beat late confirmation |
| R12L3_C03_027710_FEED_FOOD_CHAIN_SHOCK | 027710 | 4095 | 2950 | 54.6 | 114.6 | -54.3 | -36.6 | early policy/feed shock plus relative strength beat late confirmation |

## 19. Score-Return Alignment Matrix

| alignment_label | trigger_count | avg_weighted_score_before | avg_weighted_score_after | avg_MFE_90D_pct | avg_MAE_90D_pct | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| score_high_return_high | 5 | 56 | 66 | 96.4 | -35.3 | valid but must detect lateness |
| score_low_return_high_missed_structural | 2 | 32 | 43 | 287.7 | -20.0 | promote Stage2-Actionable |
| score_mid_return_high_promote_candidate | 2 | 39 | 48 | 60.0 | -19.6 | keep as Actionable/Yellow |
| score_high_return_low_false_positive | 1 | 59 | 68 | 9.8 | -41.3 | late Green false positive risk |
| score_mid_return_low_watch_only | 2 | 45 | 53 | 15.2 | -50.2 | 4B watch only |

## 20. Weight Sensitivity Table

| axis | baseline_value | tested_value | delta | affected_case_count | reason | backtest_effect |
| --- | --- | --- | --- | --- | --- | --- |
| stage2_actionable_feed_policy_shock | 0 | 3 | +3 |  | Three R12 feed/food-shock cases produced better 90D MFE when Stage2-Actionable was selected before Green. | avg_MFE_90D 101.0 -> 209.3; avg_MAE_90D -34.2 -> -20.4 |
| relative_strength_after_policy_shock | 2 | 5 | +3 |  | Relative-strength breakout after public food-supply shock separated excellent entries from passive Stage2. | Selected Actionable triggers had MFE90 467.1/46.3/114.6 with controlled event framing. |
| late_green_confirmation_penalty | 0 | -2 | -2 |  | Green confirmation for 미래생명자원 captured only 9.8% MFE90 versus Actionable 46.3%. | late_green_count 2 -> 0 under selected profile |
| price_only_4b_watch_not_exit | 0 | 2 | +2 |  | Price-only 4B near peak protected from large drawdowns, but only one case had proximity >0.7 and no non-price evidence appeared. | 4B overlay MAE90 median about -44.8 after blowoff; use watch overlay not hard sell. |
| hard_4c_thesis_break | 0 | 0 | 0 |  | No hard 4C evidence with public thesis break was validated; drawdowns were event-premium fade, not confirmed thesis break. | not_validated |

## 21. Optimization Decision Log

```jsonl
{"row_type":"optimization_decision","decision_id":"R12L3_D01","hypothesis":"Promote feed/food-supply shock + relative strength to Stage2-Actionable before Green.","tested_trigger_ids":["R12L3_C01_T2","R12L3_C02_T2","R12L3_C03_T2"],"baseline_profile":"baseline_current_proxy","selected_profile":"r12_stage2_feed_policy_shock_guarded","backtest_result_summary":"avg_MFE90 improved 101.0->209.3; avg_MAE90 improved -34.2->-20.4.","accepted_or_rejected":"accepted","delta_magnitude":"+3","why_not_larger_delta":"Only one archetype family, no non-feed counterexample in this round.","risks":"event-premium themes can reverse violently; require 4B overlay.","next_validation_needed":"Test non-agri R12 life-service events and failed commodity-shock cases."}
{"row_type":"optimization_decision","decision_id":"R12L3_D02","hypothesis":"Treat price-only overheat as 4B-watch only unless non-price 4B evidence exists.","tested_trigger_ids":["R12L3_C01_T4","R12L3_C02_T4","R12L3_C03_T4"],"baseline_profile":"baseline_current_proxy","selected_profile":"four_b_peak_timing_tuned","backtest_result_summary":"All three 4B overlays were followed by deep MAE; however close-based 4B could be too late after intraday peak.","accepted_or_rejected":"accepted_as_watch_only","delta_magnitude":"+2","why_not_larger_delta":"Non-price 4B evidence was not available; price-only should not become full exit.","risks":"could suppress continuation if applied too early.","next_validation_needed":"Find R12 cases with valuation/dilution/non-price 4B evidence."}
{"row_type":"optimization_decision","decision_id":"R12L3_D03","hypothesis":"Apply hard 4C earlier for feed-shock fade.","tested_trigger_ids":[],"baseline_profile":"baseline_current_proxy","selected_profile":"four_c_thesis_break_earlier","backtest_result_summary":"not_validated","accepted_or_rejected":"rejected","delta_magnitude":"0","why_not_larger_delta":"No public thesis-break trigger distinct from price fade was validated.","risks":"would confuse event fade with thesis break.","next_validation_needed":"Need disclosure- or policy-break cases."}
```

## 22. Overfitting / Robustness Check

```text
usable_entry_trigger_count = 9
usable_4B_overlay_count = 3
case_count = 3
archetype_family_count = 1
max_abs_delta_by_rule = +3
```

Because all three usable cases sit inside the same feed/food-shock family, the accepted deltas stop at +3. No +5 delta is proposed. Counterexample search is incomplete for broader R12 life-service cases.

## 23. Cross-case Aggregate Metrics

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,below_entry_90D_rate,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,3,3,218.3,75.0,-18.1,-18.6,218.3,-33.2,1.0,,overlay_only,overlay_only,representative rows only; duplicate same-entry labels excluded
aggregate_metric,Stage2-Actionable,3,3,209.3,114.6,-20.4,-20.6,209.3,-34.8,1.0,,overlay_only,overlay_only,representative rows only; duplicate same-entry labels excluded
aggregate_metric,Stage3-Green,2,2,124.2,124.2,-30.6,-30.6,124.2,-40.2,0.5,0.4,overlay_only,overlay_only,representative rows only; duplicate same-entry labels excluded
aggregate_metric,Stage3-Yellow,1,1,54.6,54.6,-41.5,-41.5,54.6,-54.3,1.0,0.3,overlay_only,overlay_only,representative rows only; duplicate same-entry labels excluded
aggregate_metric,Stage4B_overlay,3,0,25.5,18.7,-48.4,-44.8,25.5,-61.8,1.0,overlay,0.6,0.6,4B overlay only; not mixed with entry aggregate
```

Aggregate rule: only `calibration_usable=true` and `dedupe_for_aggregate=true` representative rows are included in entry aggregate. Stage4B overlay rows are separated.

## 24. Score-Price Alignment Verdict

```text
R12 verdict:
- Stage2 alone: useful awareness, but too noisy.
- Stage2-Actionable: strongest validated entry tier when public food-supply shock + relative strength are both present.
- Stage3-Yellow: useful if Green would be late, but should not wait for the final squeeze candle.
- Stage3-Green: too late in 2/3 cases.
- 4B: price-only watch overlay is valid near blowoff, but not a full hard exit without non-price evidence.
- 4C: not validated.
```

## 25. Validation Scope / Non-Validation Scope

### this_round_validates

```text
- feed/grain/food-supply shock Stage2-Actionable promotion
- relative-strength-after-public-macro-shock as Actionable evidence
- late Green false-positive / late-entry risk in fast event-premium shocks
- price-only 4B as watch overlay
- aggregate deduplication by same_entry_group_id
```

### this_round_does_not_validate

```text
- broad R12 생활서비스 non-agri triggers
- hard 4C thesis break
- full 4B exit using non-price evidence
- production scoring change
- current/live candidates
```

No shadow delta is proposed for unvalidated gates.

## 26. Shadow Weight Calibration

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_feed_policy_shock,0,3,+3,Three R12 feed/food-shock cases produced better 90D MFE when Stage2-Actionable was selected before Green.,avg_MFE_90D 101.0 -> 209.3; avg_MAE_90D -34.2 -> -20.4,R12L3_C01_T2|R12L3_C02_T2|R12L3_C03_T2,3,shadow-only; not production
shadow_weight,relative_strength_after_policy_shock,2,5,+3,Relative-strength breakout after public food-supply shock separated excellent entries from passive Stage2.,Selected Actionable triggers had MFE90 467.1/46.3/114.6 with controlled event framing.,R12L3_C01_T2|R12L3_C02_T2|R12L3_C03_T2,3,shadow-only; require public macro evidence first
shadow_weight,late_green_confirmation_penalty,0,-2,-2,Green confirmation for 미래생명자원 captured only 9.8% MFE90 versus Actionable 46.3%.,late_green_count 2 -> 0 under selected profile,R12L3_C02_T3|R12L3_C03_T3,2,shadow-only; do not broadly relax Green without Actionable evidence
shadow_weight,price_only_4b_watch_not_exit,0,2,+2,"Price-only 4B near peak protected from large drawdowns, but only one case had proximity >0.7 and no non-price evidence appeared.",4B overlay MAE90 median about -44.8 after blowoff; use watch overlay not hard sell.,R12L3_C01_T4|R12L3_C02_T4|R12L3_C03_T4,3,shadow-only; needs non-price evidence for full 4B
shadow_weight,hard_4c_thesis_break,0,0,0,"No hard 4C evidence with public thesis break was validated; drawdowns were event-premium fade, not confirmed thesis break.",not_validated,,0,no delta
```

## 27. Machine-Readable Rows

### 27.1 Price source validation row JSONL

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 27.2 Case rows JSONL

```jsonl
{"row_type":"case","case_id":"R12L3_C01_005860_FEED_GRAIN_SHOCK","symbol":"005860","company_name":"한일사료","round":"R12","loop":"3","sector":"농업·생활서비스·기타","case_type":"structural_success_with_event_premium","primary_archetype":"FEED_GRAIN_SUPPLY_SHOCK","best_trigger":"R12L3_C01_T2","calibration_usable":true,"historical_window_status":"504D_available","score_price_alignment":"stage2_actionable_outperformed_late_confirmation","price_source":"Songdaiki/stock-web","notes":"우크라이나 침공 이후 곡물·사료 공급충격이 사료주 테마로 압축되며 Stage2-Actionable이 Stage3보다 유리했다."}
{"row_type":"case","case_id":"R12L3_C02_218150_FEED_ADDITIVE_GRAIN_SHOCK","symbol":"218150","company_name":"미래생명자원","round":"R12","loop":"3","sector":"농업·생활서비스·기타","case_type":"stage2_promote_candidate_but_fast_overheat","primary_archetype":"FEED_ADDITIVE_GRAIN_SUPPLY_SHOCK","best_trigger":"R12L3_C02_T2","calibration_usable":true,"historical_window_status":"504D_available","score_price_alignment":"stage2_actionable_ok_green_late_4B_needed","price_source":"Songdaiki/stock-web","notes":"2월 중순 선행 급등 이후 침공과 식량가격 뉴스가 붙었지만 Green 확인은 늦었고, 4B는 비교적 빠르게 필요했다."}
{"row_type":"case","case_id":"R12L3_C03_027710_FEED_FOOD_CHAIN_SHOCK","symbol":"027710","company_name":"팜스토리","round":"R12","loop":"3","sector":"농업·생활서비스·기타","case_type":"cyclical_success_then_overheat_drawdown","primary_archetype":"FOOD_FEED_CHAIN_GRAIN_SHOCK","best_trigger":"R12L3_C03_T2","calibration_usable":true,"historical_window_status":"504D_available","score_price_alignment":"stage2_actionable_outperformed_late_confirmation","price_source":"Songdaiki/stock-web","notes":"곡물·사료 테마의 2차 파동에서 Actionable 진입은 유효했지만, peak 이후 빠른 감쇠가 뚜렷했다."}
```

### 27.3 Trigger rows JSONL

```jsonl
{"row_type":"trigger","trigger_id":"R12L3_C01_T1","case_id":"R12L3_C01_005860_FEED_GRAIN_SHOCK","symbol":"005860","company_name":"한일사료","round":"R12","loop":"3","sector":"농업·생활서비스·기타","primary_archetype":"FEED_GRAIN_SUPPLY_SHOCK","trigger_type":"Stage2","trigger_date":"2022-02-24","evidence_available_at_that_date":"Russia-Ukraine invasion day; global grain/feed supply shock became public and directly market-actionable.","evidence_source":"global_news_FAO_food_price_context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005860/2022.csv","profile_path":"atlas/symbol_profiles/005/005860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-02-24","entry_price":2555,"MFE_30D_pct":85.5,"MFE_90D_pct":520.4,"MFE_180D_pct":520.4,"MFE_1Y_pct":520.4,"MFE_2Y_pct":520.4,"MAE_30D_pct":-18.6,"MAE_90D_pct":-18.6,"MAE_180D_pct":-18.6,"MAE_1Y_pct":-18.6,"MAE_2Y_pct":"available_but_not_separately_recomputed_if_same_as_1Y_anchor","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-04-25","peak_price":15850,"drawdown_after_peak_pct":-73.7,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"not_4B","four_c_protection_label":"hard_4c_not_confirmed","trigger_outcome_label":"missed_structural","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_no_overlap","same_entry_group_id":"R12L3_C01_20220224_2555","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R12L3_C01_T2","case_id":"R12L3_C01_005860_FEED_GRAIN_SHOCK","symbol":"005860","company_name":"한일사료","round":"R12","loop":"3","sector":"농업·생활서비스·기타","primary_archetype":"FEED_GRAIN_SUPPLY_SHOCK","trigger_type":"Stage2-Actionable","trigger_date":"2022-03-21","evidence_available_at_that_date":"grain/feed shock persisted; stock-web row shows volume expansion and first sustained breakout before April blowoff.","evidence_source":"stock_web_relative_strength_plus_global_grain_shock","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005860/2022.csv","profile_path":"atlas/symbol_profiles/005/005860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-03-21","entry_price":2795,"MFE_30D_pct":467.1,"MFE_90D_pct":467.1,"MFE_180D_pct":467.1,"MFE_1Y_pct":467.1,"MFE_2Y_pct":467.1,"MAE_30D_pct":-20.6,"MAE_90D_pct":-20.6,"MAE_180D_pct":-20.6,"MAE_1Y_pct":-20.6,"MAE_2Y_pct":"available_but_not_separately_recomputed_if_same_as_1Y_anchor","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-04-25","peak_price":15850,"drawdown_after_peak_pct":-73.7,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"not_4B","four_c_protection_label":"hard_4c_not_confirmed","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_no_overlap","same_entry_group_id":"R12L3_C01_20220321_2795","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R12L3_C01_T3","case_id":"R12L3_C01_005860_FEED_GRAIN_SHOCK","symbol":"005860","company_name":"한일사료","round":"R12","loop":"3","sector":"농업·생활서비스·기타","primary_archetype":"FEED_GRAIN_SUPPLY_SHOCK","trigger_type":"Stage3-Green","trigger_date":"2022-04-15","evidence_available_at_that_date":"public food-price narrative + repeated relative-strength closure; Green confirmation after first full price expansion.","evidence_source":"stock_web_relative_strength_plus_FAO_record_food_price_context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005860/2022.csv","profile_path":"atlas/symbol_profiles/005/005860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-04-15","entry_price":4680,"MFE_30D_pct":238.7,"MFE_90D_pct":238.7,"MFE_180D_pct":238.7,"MFE_1Y_pct":238.7,"MFE_2Y_pct":238.7,"MAE_30D_pct":-19.9,"MAE_90D_pct":-19.9,"MAE_180D_pct":-19.9,"MAE_1Y_pct":-19.9,"MAE_2Y_pct":"available_but_not_separately_recomputed_if_same_as_1Y_anchor","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":false,"peak_date":"2022-04-25","peak_price":15850,"drawdown_after_peak_pct":-73.7,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.144,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"not_4B","four_c_protection_label":"hard_4c_not_confirmed","trigger_outcome_label":"good_but_later_than_actionable","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_no_overlap","same_entry_group_id":"R12L3_C01_20220415_4680","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R12L3_C01_T4","case_id":"R12L3_C01_005860_FEED_GRAIN_SHOCK","symbol":"005860","company_name":"한일사료","round":"R12","loop":"3","sector":"농업·생활서비스·기타","primary_archetype":"FEED_GRAIN_SUPPLY_SHOCK","trigger_type":"Stage4B","trigger_date":"2022-04-25","evidence_available_at_that_date":"blowoff day after sequential limit-up style expansion; price-only overheat overlay near local/full peak.","evidence_source":"stock_web_price_overheat","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005860/2022.csv","profile_path":"atlas/symbol_profiles/005/005860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-04-25","entry_price":13350,"MFE_30D_pct":18.7,"MFE_90D_pct":18.7,"MFE_180D_pct":18.7,"MFE_1Y_pct":18.7,"MFE_2Y_pct":18.7,"MAE_30D_pct":-45.1,"MAE_90D_pct":-60.2,"MAE_180D_pct":-68.8,"MAE_1Y_pct":-68.8,"MAE_2Y_pct":"available_but_not_separately_recomputed_if_same_as_1Y_anchor","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-04-25","peak_price":15850,"drawdown_after_peak_pct":-73.7,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.809,"four_b_full_window_peak_proximity":0.809,"four_b_timing_verdict":"good_full_window_4B_timing_but_price_only","four_b_evidence_type":"price_only|positioning_overheat","four_c_protection_label":"hard_4c_not_confirmed","trigger_outcome_label":"4B_watch_success","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_no_overlap","same_entry_group_id":"R12L3_C01_20220425_13350","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R12L3_C02_T1","case_id":"R12L3_C02_218150_FEED_ADDITIVE_GRAIN_SHOCK","symbol":"218150","company_name":"미래생명자원","round":"R12","loop":"3","sector":"농업·생활서비스·기타","primary_archetype":"FEED_ADDITIVE_GRAIN_SUPPLY_SHOCK","trigger_type":"Stage2","trigger_date":"2022-02-24","evidence_available_at_that_date":"Russia-Ukraine full invasion day; feed additive / animal nutrition proxy captured food-security theme after pre-spike.","evidence_source":"global_news_FAO_food_price_context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/218/218150/2022.csv","profile_path":"atlas/symbol_profiles/218/218150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-02-24","entry_price":8090,"MFE_30D_pct":53.3,"MFE_90D_pct":59.5,"MFE_180D_pct":59.5,"MFE_1Y_pct":59.5,"MFE_2Y_pct":59.5,"MAE_30D_pct":-16.8,"MAE_90D_pct":-14.7,"MAE_180D_pct":-42.6,"MAE_1Y_pct":-53.0,"MAE_2Y_pct":"available_but_not_separately_recomputed_if_same_as_1Y_anchor","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-04-19","peak_price":12900,"drawdown_after_peak_pct":-70.5,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"not_4B","four_c_protection_label":"hard_4c_not_confirmed","trigger_outcome_label":"good_entry","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_no_overlap","same_entry_group_id":"R12L3_C02_20220224_8090","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R12L3_C02_T2","case_id":"R12L3_C02_218150_FEED_ADDITIVE_GRAIN_SHOCK","symbol":"218150","company_name":"미래생명자원","round":"R12","loop":"3","sector":"농업·생활서비스·기타","primary_archetype":"FEED_ADDITIVE_GRAIN_SUPPLY_SHOCK","trigger_type":"Stage2-Actionable","trigger_date":"2022-03-02","evidence_available_at_that_date":"post-invasion continuation gap plus relative-strength confirmation after reset from 2022-02-25/28 pullback.","evidence_source":"stock_web_relative_strength_plus_global_grain_shock","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/218/218150/2022.csv","profile_path":"atlas/symbol_profiles/218/218150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-03-02","entry_price":8820,"MFE_30D_pct":40.6,"MFE_90D_pct":46.3,"MFE_180D_pct":46.3,"MFE_1Y_pct":46.3,"MFE_2Y_pct":46.3,"MAE_30D_pct":-15.9,"MAE_90D_pct":-21.8,"MAE_180D_pct":-47.3,"MAE_1Y_pct":-56.9,"MAE_2Y_pct":"available_but_not_separately_recomputed_if_same_as_1Y_anchor","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-04-19","peak_price":12900,"drawdown_after_peak_pct":-70.5,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"not_4B","four_c_protection_label":"hard_4c_not_confirmed","trigger_outcome_label":"good_entry","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_no_overlap","same_entry_group_id":"R12L3_C02_20220302_8820","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R12L3_C02_T3","case_id":"R12L3_C02_218150_FEED_ADDITIVE_GRAIN_SHOCK","symbol":"218150","company_name":"미래생명자원","round":"R12","loop":"3","sector":"농업·생활서비스·기타","primary_archetype":"FEED_ADDITIVE_GRAIN_SUPPLY_SHOCK","trigger_type":"Stage3-Green","trigger_date":"2022-03-22","evidence_available_at_that_date":"second breakout and public feed/food-security narrative fully priced; Green captures confirmation after much of upside.","evidence_source":"stock_web_relative_strength_plus_FAO_record_food_price_context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/218/218150/2022.csv","profile_path":"atlas/symbol_profiles/218/218150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-03-22","entry_price":11750,"MFE_30D_pct":9.8,"MFE_90D_pct":9.8,"MFE_180D_pct":9.8,"MFE_1Y_pct":9.8,"MFE_2Y_pct":9.8,"MAE_30D_pct":-14.5,"MAE_90D_pct":-41.3,"MAE_180D_pct":-60.5,"MAE_1Y_pct":-67.7,"MAE_2Y_pct":"available_but_not_separately_recomputed_if_same_as_1Y_anchor","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-04-19","peak_price":12900,"drawdown_after_peak_pct":-70.5,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.718,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"not_4B","four_c_protection_label":"hard_4c_not_confirmed","trigger_outcome_label":"late_entry","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_no_overlap","same_entry_group_id":"R12L3_C02_20220322_11750","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R12L3_C02_T4","case_id":"R12L3_C02_218150_FEED_ADDITIVE_GRAIN_SHOCK","symbol":"218150","company_name":"미래생명자원","round":"R12","loop":"3","sector":"농업·생활서비스·기타","primary_archetype":"FEED_ADDITIVE_GRAIN_SUPPLY_SHOCK","trigger_type":"Stage4B","trigger_date":"2022-04-19","evidence_available_at_that_date":"local/full cycle peak day; price-only overheat after repeated public food-security narrative.","evidence_source":"stock_web_price_overheat","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/218/218150/2022.csv","profile_path":"atlas/symbol_profiles/218/218150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-04-19","entry_price":11550,"MFE_30D_pct":11.7,"MFE_90D_pct":11.7,"MFE_180D_pct":11.7,"MFE_1Y_pct":11.7,"MFE_2Y_pct":11.7,"MAE_30D_pct":-35.5,"MAE_90D_pct":-40.3,"MAE_180D_pct":-59.8,"MAE_1Y_pct":-67.1,"MAE_2Y_pct":"available_but_not_separately_recomputed_if_same_as_1Y_anchor","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-04-19","peak_price":12900,"drawdown_after_peak_pct":-70.5,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.669,"four_b_full_window_peak_proximity":0.669,"four_b_timing_verdict":"borderline_good_4B_watch","four_b_evidence_type":"price_only|positioning_overheat","four_c_protection_label":"hard_4c_not_confirmed","trigger_outcome_label":"4B_watch_success","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_no_overlap","same_entry_group_id":"R12L3_C02_20220419_11550","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R12L3_C03_T1","case_id":"R12L3_C03_027710_FEED_FOOD_CHAIN_SHOCK","symbol":"027710","company_name":"팜스토리","round":"R12","loop":"3","sector":"농업·생활서비스·기타","primary_archetype":"FOOD_FEED_CHAIN_GRAIN_SHOCK","trigger_type":"Stage2","trigger_date":"2022-02-24","evidence_available_at_that_date":"global grain/feed shock; feed-food chain proxy participates but first leg is less explosive than pure feed tickers.","evidence_source":"global_news_FAO_food_price_context","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/027/027710/2022.csv","profile_path":"atlas/symbol_profiles/027/027710.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-02-24","entry_price":3040,"MFE_30D_pct":15.1,"MFE_90D_pct":75.0,"MFE_180D_pct":75.0,"MFE_1Y_pct":75.0,"MFE_2Y_pct":75.0,"MAE_30D_pct":-20.9,"MAE_90D_pct":-20.9,"MAE_180D_pct":-38.5,"MAE_1Y_pct":-46.4,"MAE_2Y_pct":"available_but_not_separately_recomputed_if_same_as_1Y_anchor","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-04-27","peak_price":6330,"drawdown_after_peak_pct":-74.2,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"not_4B","four_c_protection_label":"hard_4c_not_confirmed","trigger_outcome_label":"stage2_promote_candidate","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_no_overlap","same_entry_group_id":"R12L3_C03_20220224_3040","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R12L3_C03_T2","case_id":"R12L3_C03_027710_FEED_FOOD_CHAIN_SHOCK","symbol":"027710","company_name":"팜스토리","round":"R12","loop":"3","sector":"농업·생활서비스·기타","primary_archetype":"FOOD_FEED_CHAIN_GRAIN_SHOCK","trigger_type":"Stage2-Actionable","trigger_date":"2022-04-15","evidence_available_at_that_date":"second wave relative-strength close after FAO record food-price confirmation; still before final peak.","evidence_source":"FAO_food_price_context_plus_stock_web_relative_strength","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/027/027710/2022.csv","profile_path":"atlas/symbol_profiles/027/027710.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-04-15","entry_price":2950,"MFE_30D_pct":114.6,"MFE_90D_pct":114.6,"MFE_180D_pct":114.6,"MFE_1Y_pct":114.6,"MFE_2Y_pct":114.6,"MAE_30D_pct":-7.3,"MAE_90D_pct":-18.8,"MAE_180D_pct":-36.6,"MAE_1Y_pct":-44.7,"MAE_2Y_pct":"available_but_not_separately_recomputed_if_same_as_1Y_anchor","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-04-27","peak_price":6330,"drawdown_after_peak_pct":-74.2,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"not_4B","four_c_protection_label":"hard_4c_not_confirmed","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_no_overlap","same_entry_group_id":"R12L3_C03_20220415_2950","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R12L3_C03_T3","case_id":"R12L3_C03_027710_FEED_FOOD_CHAIN_SHOCK","symbol":"027710","company_name":"팜스토리","round":"R12","loop":"3","sector":"농업·생활서비스·기타","primary_archetype":"FOOD_FEED_CHAIN_GRAIN_SHOCK","trigger_type":"Stage3-Yellow","trigger_date":"2022-04-25","evidence_available_at_that_date":"food-chain proxy finally reaches high-volume breakout; evidence sufficient for Yellow, but Green confirmation would be too late.","evidence_source":"stock_web_relative_strength","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/027/027710/2022.csv","profile_path":"atlas/symbol_profiles/027/027710.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-04-25","entry_price":4095,"MFE_30D_pct":54.6,"MFE_90D_pct":54.6,"MFE_180D_pct":54.6,"MFE_1Y_pct":54.6,"MFE_2Y_pct":54.6,"MAE_30D_pct":-15.4,"MAE_90D_pct":-41.5,"MAE_180D_pct":-54.3,"MAE_1Y_pct":-60.2,"MAE_2Y_pct":"available_but_not_separately_recomputed_if_same_as_1Y_anchor","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-04-27","peak_price":6330,"drawdown_after_peak_pct":-74.2,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.339,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4B","four_b_evidence_type":"not_4B","four_c_protection_label":"hard_4c_not_confirmed","trigger_outcome_label":"good_but_late_yellow","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_no_overlap","same_entry_group_id":"R12L3_C03_20220425_4095","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R12L3_C03_T4","case_id":"R12L3_C03_027710_FEED_FOOD_CHAIN_SHOCK","symbol":"027710","company_name":"팜스토리","round":"R12","loop":"3","sector":"농업·생활서비스·기타","primary_archetype":"FOOD_FEED_CHAIN_GRAIN_SHOCK","trigger_type":"Stage4B","trigger_date":"2022-04-27","evidence_available_at_that_date":"intraday high made full-window peak but close had already fallen; 4B is late if triggered by close, useful only as watch.","evidence_source":"stock_web_price_overheat","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/027/027710/2022.csv","profile_path":"atlas/symbol_profiles/027/027710.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-04-27","entry_price":4335,"MFE_30D_pct":46.0,"MFE_90D_pct":46.0,"MFE_180D_pct":46.0,"MFE_1Y_pct":46.0,"MFE_2Y_pct":46.0,"MAE_30D_pct":-20.1,"MAE_90D_pct":-44.8,"MAE_180D_pct":-56.9,"MAE_1Y_pct":-62.4,"MAE_2Y_pct":"available_but_not_separately_recomputed_if_same_as_1Y_anchor","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-04-27","peak_price":6330,"drawdown_after_peak_pct":-74.2,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.41,"four_b_full_window_peak_proximity":0.41,"four_b_timing_verdict":"price_only_4B_close_late_after_intraday_peak","four_b_evidence_type":"price_only|positioning_overheat","four_c_protection_label":"hard_4c_not_confirmed","trigger_outcome_label":"4B_watch_late","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_no_overlap","same_entry_group_id":"R12L3_C03_20220427_4335","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
```

### 27.4 Score simulation rows JSONL

```jsonl
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_vs_r12_stage2_feed_policy_shock_guarded","case_id":"R12L3_C01_005860_FEED_GRAIN_SHOCK","trigger_id":"R12L3_C01_T1","symbol":"005860","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":1,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":26,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":1,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":31,"stage_label_after":"Stage2","changed_components":["policy_or_regulatory_score","relative_strength_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"R12 shadow profile raises early policy/feed-shock + relative-strength weight and applies sharper overheat/execution-risk penalty.","selected_by_profile":false,"MFE_90D_pct":520.4,"MAE_90D_pct":-18.6,"score_return_alignment_label":"score_low_return_high_missed_structural","row_validation_status":"usable_for_weight_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_vs_r12_stage2_feed_policy_shock_guarded","case_id":"R12L3_C01_005860_FEED_GRAIN_SHOCK","trigger_id":"R12L3_C01_T2","symbol":"005860","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":0,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":2,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":44,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":0,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":2,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":52,"stage_label_after":"Stage3-Yellow","changed_components":["policy_or_regulatory_score","relative_strength_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"R12 shadow profile raises early policy/feed-shock + relative-strength weight and applies sharper overheat/execution-risk penalty.","selected_by_profile":true,"MFE_90D_pct":467.1,"MAE_90D_pct":-20.6,"score_return_alignment_label":"score_high_return_high","row_validation_status":"usable_for_weight_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_vs_r12_stage2_feed_policy_shock_guarded","case_id":"R12L3_C01_005860_FEED_GRAIN_SHOCK","trigger_id":"R12L3_C01_T3","symbol":"005860","trigger_type":"Stage3-Green","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":0,"relative_strength_score":7,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":56,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":0,"relative_strength_score":7,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64,"stage_label_after":"Stage3-Yellow","changed_components":["policy_or_regulatory_score","relative_strength_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"R12 shadow profile raises early policy/feed-shock + relative-strength weight and applies sharper overheat/execution-risk penalty.","selected_by_profile":false,"MFE_90D_pct":238.7,"MAE_90D_pct":-19.9,"score_return_alignment_label":"score_high_return_high","row_validation_status":"usable_for_weight_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_vs_r12_stage2_feed_policy_shock_guarded","case_id":"R12L3_C01_005860_FEED_GRAIN_SHOCK","trigger_id":"R12L3_C01_T4","symbol":"005860","trigger_type":"Stage4B","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":0,"relative_strength_score":9,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":8,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":62,"stage_label_before":"Stage3+4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":0,"relative_strength_score":9,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":8,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage3+4B-watch","changed_components":["policy_or_regulatory_score","relative_strength_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"R12 shadow profile raises early policy/feed-shock + relative-strength weight and applies sharper overheat/execution-risk penalty.","selected_by_profile":false,"MFE_90D_pct":18.7,"MAE_90D_pct":-60.2,"score_return_alignment_label":"score_high_return_low_false_positive","row_validation_status":"usable_for_4B_overlay_calibration_only"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_vs_r12_stage2_feed_policy_shock_guarded","case_id":"R12L3_C02_218150_FEED_ADDITIVE_GRAIN_SHOCK","trigger_id":"R12L3_C02_T1","symbol":"218150","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":2,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":34,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":2,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":40,"stage_label_after":"Stage2-Actionable","changed_components":["policy_or_regulatory_score","relative_strength_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"R12 shadow profile raises early policy/feed-shock + relative-strength weight and applies sharper overheat/execution-risk penalty.","selected_by_profile":false,"MFE_90D_pct":59.5,"MAE_90D_pct":-14.7,"score_return_alignment_label":"score_low_return_high_missed_structural","row_validation_status":"usable_for_weight_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_vs_r12_stage2_feed_policy_shock_guarded","case_id":"R12L3_C02_218150_FEED_ADDITIVE_GRAIN_SHOCK","trigger_id":"R12L3_C02_T2","symbol":"218150","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":0,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":46,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":0,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":53,"stage_label_after":"Stage3-Yellow","changed_components":["policy_or_regulatory_score","relative_strength_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"R12 shadow profile raises early policy/feed-shock + relative-strength weight and applies sharper overheat/execution-risk penalty.","selected_by_profile":true,"MFE_90D_pct":46.3,"MAE_90D_pct":-21.8,"score_return_alignment_label":"score_high_return_high","row_validation_status":"usable_for_weight_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_vs_r12_stage2_feed_policy_shock_guarded","case_id":"R12L3_C02_218150_FEED_ADDITIVE_GRAIN_SHOCK","trigger_id":"R12L3_C02_T3","symbol":"218150","trigger_type":"Stage3-Green","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":58,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":66,"stage_label_after":"Stage3-Yellow","changed_components":["policy_or_regulatory_score","relative_strength_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"R12 shadow profile raises early policy/feed-shock + relative-strength weight and applies sharper overheat/execution-risk penalty.","selected_by_profile":false,"MFE_90D_pct":9.8,"MAE_90D_pct":-41.3,"score_return_alignment_label":"score_high_return_low_false_positive","row_validation_status":"usable_for_weight_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_vs_r12_stage2_feed_policy_shock_guarded","case_id":"R12L3_C02_218150_FEED_ADDITIVE_GRAIN_SHOCK","trigger_id":"R12L3_C02_T4","symbol":"218150","trigger_type":"Stage4B","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":7,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":58,"stage_label_before":"Stage3+4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":7,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64,"stage_label_after":"Stage3+4B-watch","changed_components":["policy_or_regulatory_score","relative_strength_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"R12 shadow profile raises early policy/feed-shock + relative-strength weight and applies sharper overheat/execution-risk penalty.","selected_by_profile":false,"MFE_90D_pct":11.7,"MAE_90D_pct":-40.3,"score_return_alignment_label":"score_high_return_low_false_positive","row_validation_status":"usable_for_4B_overlay_calibration_only"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_vs_r12_stage2_feed_policy_shock_guarded","case_id":"R12L3_C03_027710_FEED_FOOD_CHAIN_SHOCK","trigger_id":"R12L3_C03_T1","symbol":"027710","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":3,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":1,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":28,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":3,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":1,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":34,"stage_label_after":"Stage2","changed_components":["policy_or_regulatory_score","relative_strength_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"R12 shadow profile raises early policy/feed-shock + relative-strength weight and applies sharper overheat/execution-risk penalty.","selected_by_profile":false,"MFE_90D_pct":75.0,"MAE_90D_pct":-20.9,"score_return_alignment_label":"score_low_return_high_missed_structural","row_validation_status":"usable_for_weight_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_vs_r12_stage2_feed_policy_shock_guarded","case_id":"R12L3_C03_027710_FEED_FOOD_CHAIN_SHOCK","trigger_id":"R12L3_C03_T2","symbol":"027710","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":0,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":2,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":44,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":0,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":2,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":52,"stage_label_after":"Stage3-Yellow","changed_components":["policy_or_regulatory_score","relative_strength_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"R12 shadow profile raises early policy/feed-shock + relative-strength weight and applies sharper overheat/execution-risk penalty.","selected_by_profile":true,"MFE_90D_pct":114.6,"MAE_90D_pct":-18.8,"score_return_alignment_label":"score_high_return_high","row_validation_status":"usable_for_weight_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_vs_r12_stage2_feed_policy_shock_guarded","case_id":"R12L3_C03_027710_FEED_FOOD_CHAIN_SHOCK","trigger_id":"R12L3_C03_T3","symbol":"027710","trigger_type":"Stage3-Yellow","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":0,"relative_strength_score":7,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":52,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":0,"relative_strength_score":7,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":60,"stage_label_after":"Stage3-Yellow","changed_components":["policy_or_regulatory_score","relative_strength_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"R12 shadow profile raises early policy/feed-shock + relative-strength weight and applies sharper overheat/execution-risk penalty.","selected_by_profile":false,"MFE_90D_pct":54.6,"MAE_90D_pct":-41.5,"score_return_alignment_label":"score_high_return_high","row_validation_status":"usable_for_weight_calibration"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_vs_r12_stage2_feed_policy_shock_guarded","case_id":"R12L3_C03_027710_FEED_FOOD_CHAIN_SHOCK","trigger_id":"R12L3_C03_T4","symbol":"027710","trigger_type":"Stage4B","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":7,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":56,"stage_label_before":"Stage3+4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":5,"valuation_repricing_score":7,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":62,"stage_label_after":"Stage3+4B-watch","changed_components":["policy_or_regulatory_score","relative_strength_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"R12 shadow profile raises early policy/feed-shock + relative-strength weight and applies sharper overheat/execution-risk penalty.","selected_by_profile":false,"MFE_90D_pct":46.0,"MAE_90D_pct":-44.8,"score_return_alignment_label":"score_high_return_high","row_validation_status":"usable_for_4B_overlay_calibration_only"}
```

### 27.5 Profile comparison rows CSV

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,3,3,3,101.0,54.6,-34.2,-41.3,101.0,-44.9,1.0,1.0,0.33,2,2,0.4,not_mixed_with_entry_profiles,not_mixed_with_entry_profiles,reference; catches confirmation but loses early upside and tolerates late entries
profile_comparison,r12_stage2_feed_policy_shock_guarded,3,3,3,209.3,114.6,-20.4,-20.6,209.3,-34.8,1.0,1.0,0.0,0,0,not_selected_as_green,overlay_only,overlay_only,best shadow profile; earlier entry improves average MFE90 while reducing average MAE90 severity
profile_comparison,stage3_yellow_entry_relaxed,3,3,3,189.3,54.6,-28.0,-21.8,189.3,-40.7,1.0,1.0,0.0,1,1,0.34,overlay_only,overlay_only,usable but less clean than Stage2-Actionable because 미래생명자원 Green-like trigger is already late
profile_comparison,green_confirmation_timing_relaxed,3,3,3,101.0,54.6,-34.2,-41.3,101.0,-44.9,0.67,1.0,0.33,2,2,0.4,overlay_only,overlay_only,reject broad Green relaxation; fixes little and still accepts late event premium
profile_comparison,four_b_peak_timing_tuned,3,3,0,25.5,18.7,-48.4,-44.8,25.5,-61.8,0.33,1.0,0.0,0,0,overlay,0.6,0.6,4B overlay should be watch-only unless non-price 4B evidence exists; price-only works best near 0.7~1.0
profile_comparison,four_c_thesis_break_earlier,3,0,0,not_validated,not_validated,not_validated,not_validated,not_validated,not_validated,not_validated,not_validated,not_validated,not_validated,not_validated,not_validated,not_validated,not_validated,hard 4C not validated in this round; no 4C hard-gate delta
```

### 27.6 Shadow weight CSV

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_feed_policy_shock,0,3,+3,Three R12 feed/food-shock cases produced better 90D MFE when Stage2-Actionable was selected before Green.,avg_MFE_90D 101.0 -> 209.3; avg_MAE_90D -34.2 -> -20.4,R12L3_C01_T2|R12L3_C02_T2|R12L3_C03_T2,3,shadow-only; not production
shadow_weight,relative_strength_after_policy_shock,2,5,+3,Relative-strength breakout after public food-supply shock separated excellent entries from passive Stage2.,Selected Actionable triggers had MFE90 467.1/46.3/114.6 with controlled event framing.,R12L3_C01_T2|R12L3_C02_T2|R12L3_C03_T2,3,shadow-only; require public macro evidence first
shadow_weight,late_green_confirmation_penalty,0,-2,-2,Green confirmation for 미래생명자원 captured only 9.8% MFE90 versus Actionable 46.3%.,late_green_count 2 -> 0 under selected profile,R12L3_C02_T3|R12L3_C03_T3,2,shadow-only; do not broadly relax Green without Actionable evidence
shadow_weight,price_only_4b_watch_not_exit,0,2,+2,"Price-only 4B near peak protected from large drawdowns, but only one case had proximity >0.7 and no non-price evidence appeared.",4B overlay MAE90 median about -44.8 after blowoff; use watch overlay not hard sell.,R12L3_C01_T4|R12L3_C02_T4|R12L3_C03_T4,3,shadow-only; needs non-price evidence for full 4B
shadow_weight,hard_4c_thesis_break,0,0,0,"No hard 4C evidence with public thesis break was validated; drawdowns were event-premium fade, not confirmed thesis break.",not_validated,,0,no delta
```

### 27.7 Optimization decision rows JSONL

```jsonl
{"row_type":"optimization_decision","decision_id":"R12L3_D01","hypothesis":"Promote feed/food-supply shock + relative strength to Stage2-Actionable before Green.","tested_trigger_ids":["R12L3_C01_T2","R12L3_C02_T2","R12L3_C03_T2"],"baseline_profile":"baseline_current_proxy","selected_profile":"r12_stage2_feed_policy_shock_guarded","backtest_result_summary":"avg_MFE90 improved 101.0->209.3; avg_MAE90 improved -34.2->-20.4.","accepted_or_rejected":"accepted","delta_magnitude":"+3","why_not_larger_delta":"Only one archetype family, no non-feed counterexample in this round.","risks":"event-premium themes can reverse violently; require 4B overlay.","next_validation_needed":"Test non-agri R12 life-service events and failed commodity-shock cases."}
{"row_type":"optimization_decision","decision_id":"R12L3_D02","hypothesis":"Treat price-only overheat as 4B-watch only unless non-price 4B evidence exists.","tested_trigger_ids":["R12L3_C01_T4","R12L3_C02_T4","R12L3_C03_T4"],"baseline_profile":"baseline_current_proxy","selected_profile":"four_b_peak_timing_tuned","backtest_result_summary":"All three 4B overlays were followed by deep MAE; however close-based 4B could be too late after intraday peak.","accepted_or_rejected":"accepted_as_watch_only","delta_magnitude":"+2","why_not_larger_delta":"Non-price 4B evidence was not available; price-only should not become full exit.","risks":"could suppress continuation if applied too early.","next_validation_needed":"Find R12 cases with valuation/dilution/non-price 4B evidence."}
{"row_type":"optimization_decision","decision_id":"R12L3_D03","hypothesis":"Apply hard 4C earlier for feed-shock fade.","tested_trigger_ids":[],"baseline_profile":"baseline_current_proxy","selected_profile":"four_c_thesis_break_earlier","backtest_result_summary":"not_validated","accepted_or_rejected":"rejected","delta_magnitude":"0","why_not_larger_delta":"No public thesis-break trigger distinct from price fade was validated.","risks":"would confuse event fade with thesis break.","next_validation_needed":"Need disclosure- or policy-break cases."}
```

### 27.8 Narrative-only rows JSONL

```jsonl
{"row_type":"narrative_only","case_id":"R12L3_SCOPE_NOTE","symbol":"MULTI","reason":"hard_4c_not_validated_and_broad_life_service_scope_not_tested","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

### 27.9 Aggregate metric rows CSV

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,below_entry_90D_rate,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,3,3,218.3,75.0,-18.1,-18.6,218.3,-33.2,1.0,,overlay_only,overlay_only,representative rows only; duplicate same-entry labels excluded
aggregate_metric,Stage2-Actionable,3,3,209.3,114.6,-20.4,-20.6,209.3,-34.8,1.0,,overlay_only,overlay_only,representative rows only; duplicate same-entry labels excluded
aggregate_metric,Stage3-Green,2,2,124.2,124.2,-30.6,-30.6,124.2,-40.2,0.5,0.4,overlay_only,overlay_only,representative rows only; duplicate same-entry labels excluded
aggregate_metric,Stage3-Yellow,1,1,54.6,54.6,-41.5,-41.5,54.6,-54.3,1.0,0.3,overlay_only,overlay_only,representative rows only; duplicate same-entry labels excluded
aggregate_metric,Stage4B_overlay,3,0,25.5,18.7,-48.4,-44.8,25.5,-61.8,1.0,overlay,0.6,0.6,4B overlay only; not mixed with entry aggregate
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
current_round_completed = R12
next_round = R13
next_sector = Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리
suggested_loop = 3
```

## 30. Source Notes

- Stock-web manifest/schema/universe/profile/shard sources are cited inline.
- Public macro evidence uses invasion date and food price shock sources; company-specific Korean news search was intentionally not used as a price substitute.
- Relative return fields remain unavailable because this round did not load separate market/sector index shards.
- The calculation basis is raw, unadjusted stock-web tradable OHLC. No adjusted-price correction was applied.
- This document is not an investment recommendation.
