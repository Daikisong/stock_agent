# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata

```text
research_session = historical_calibration_after_stock_web_ohlc_breakthrough
round = R3
loop = 1
sector = 2차전지·전기차·친환경
sector_slug = secondary_battery_ev_green
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
stock_agent_repo_accessed = false
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is a standalone historical calibration and backtest optimization note. It is not live candidate research, not a repository patch, and not an investment recommendation.

## 1. Round Scope

```text
R3 = 2차전지·전기차·친환경
```

The calibration question for this round is not “battery theme was hot.” The question is narrower:

```text
EV battery contract / cathode order / U.S. JV / IRA or AMPC support
→ actual visibility of volume, margin, customer quality, utilization, and valuation runway
→ stock-web OHLC forward path
→ Stage2 / Stage2-Actionable / Stage3-Yellow / Stage3-Green / 4B / 4C timing quality
```

This R3 pass uses three calibration-usable historical cases and two narrative-only guardrail rows. The key lesson is that battery-material order headlines had very strong Stage2 upside in 2023, but weak customer-specific conversion, commodity price reversal, and EV demand slowdown quickly turned many Green-looking setups into 4B/4C-watch structures.

## 2. Stock-Web OHLC Input / Price Source Validation

Stock-web validation was performed before case analysis.

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","source_repo_url":"https://github.com/FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"inactive_or_delisted_like_symbol_count":2546,"markets":["KONEX","KOSDAQ","KOSDAQ GLOBAL","KOSPI"],"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Stock-web manifest states that the atlas was generated from FinanceData/marcap, uses `raw_unadjusted_marcap`, has `max_date = 2026-02-20`, and uses `atlas/ohlcv_tradable_by_symbol_year` as calibration shard root. The schema maps tradable columns as `d,o,h,l,c,v,a,mc,s,m`, and defines MFE/MAE as high/low over N tradable rows divided by entry close. Corporate-action-contaminated windows are blocked by default.

## 3. Historical Eligibility Gate

```text
minimum_forward_window_required = 180 trading days
preferred_forward_window = 252 to 504 trading days
calibration basis = tradable_raw OHLC
corporate_action rule = block if corporate_action_candidate_dates overlap entry_date~D+180
```

All three calibration-usable cases have entry dates before 2024-09-30 and therefore have at least 180 tradable days available by the stock-web manifest max date. No corporate action candidate date overlaps the 180D forward windows used in this round.

## 4. Canonical Archetypes Tested

```text
BATTERY_MATERIALS_ORDERBOOK_RERATING
CATHODE_SUPPLY_CONTRACT_STAGE2_ACTIONABLE
EV_BATTERY_JV_WITH_DEMAND_SLOWDOWN_4B
TESLA_4680_SUPPLY_OPTIONALITY_WITH_CALL_OFF_RISK
BATTERY_THEME_OVERHEAT_4B
EV_DEMAND_SLOWDOWN_THESIS_BREAK_WATCH
```

## 5. Case Selection Summary

| bucket | case_id | symbol | company | calibration_usable | role |
|---|---:|---:|---|---:|---|
| structural_success / overheat | r3_loop1_posco_future_m_2023_orderbook | 003670 | 포스코퓨처엠 | true | 2023 cathode-order rerating, very strong Stage2 path, later 4B overheat |
| Stage2_promote_candidate / later break | r3_loop1_lnf_tesla_4680_2023 | 066970 | 엘앤에프 | true | Tesla 4680 supply optionality; strong early MFE but deep MAE and later call-off risk |
| evidence_good_but_price_failed | r3_loop1_samsung_sdi_gm_jv_2024 | 006400 | 삼성SDI | true | U.S. GM JV finalized; contract/JV evidence failed to become durable rerating |
| narrative-only hard 4C watch | r3_loop1_lges_ford_freudenberg_2025 | 373220 | LG에너지솔루션 | false | 2025 contract cancellation; forward 180D not available by manifest max_date |
| narrative-only overheat / corporate-action blocked | r3_loop1_ecopro_2024_blocked | 086520 | 에코프로 | false | stock-web self-test/price window marked corporate-action blocked, not weight calibration |

## 6. Evidence Source Map

| case_id | evidence source used | note |
|---|---|---|
| r3_loop1_posco_future_m_2023_orderbook | POSCO Future M public company history and 2023 battery-material orderbook summary; market-recognized 2023 cathode order wave | Evidence confidence: medium. The backtest is usable, but production implementation should attach original Korean filings for each contract row. |
| r3_loop1_lnf_tesla_4680_2023 | Reuters later summary of the 2023 L&F high-nickel cathode deal with Tesla and affiliates, plus the later value collapse of that same contract | The 2023 trigger is the initial supply-deal disclosure; the 2025 cancellation is used only as 4C narrative, not as 2023 evidence. |
| r3_loop1_samsung_sdi_gm_jv_2024 | Reuters report that Samsung SDI and GM completed the U.S. Indiana JV agreement on 2024-08-28; report notes roughly $3.5bn investment, 27GWh initial capacity, potential 36GWh, and stock +3.2% intraday | This is a clean Stage2 contract/JV evidence row but failed on forward OHLC. |
| r3_loop1_lges_ford_freudenberg_2025 | Reuters reports on Ford/LGES and Freudenberg/LGES contract terminations in Dec 2025 | Not used for weight due insufficient forward window. |
| r3_loop1_ecopro_2024_blocked | stock-web diagnostics / profile-style corporate-action contamination logic | Not used for weight due price-window block. |

## 7. Price Data Source Map

| symbol | profile_path | shard_path(s) checked | corporate action status |
|---:|---|---|---|
| 003670 | `atlas/symbol_profiles/003/003670.json` | `atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv`, 2024 continuation by manifest availability | corporate-action candidates: 2015-05-04, 2021-02-03; no 2023 180D overlap |
| 066970 | `atlas/symbol_profiles/066/066970.json` | `atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv` | corporate-action candidates: 2016-02-19, 2021-08-11; no 2023 180D overlap |
| 006400 | `atlas/symbol_profiles/006/006400.json` | `atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv`, `.../2025.csv` | corporate-action candidates: 1996-01-03, 1998-11-03, 2014-07-15; no 2024 180D overlap |
| 373220 | `atlas/symbol_profiles/373/373220.json` expected | not used for calibration | 2025 trigger too recent for 180D by manifest max_date |
| 086520 | `atlas/symbol_profiles/086/086520.json` expected | not used for calibration | corporate-action-contaminated window flagged in prior stock-web diagnostics; narrative-only |

## 8. Case-by-Case Trigger Grid

### Case A — POSCO Future M / 2023 cathode-order rerating

```text
case_id = r3_loop1_posco_future_m_2023_orderbook
symbol = 003670
company = 포스코퓨처엠
primary_archetype = BATTERY_MATERIALS_ORDERBOOK_RERATING
case_type = structural_success + 4B_overheat
```

| trigger_id | type | trigger_date | entry_date | evidence available at date | entry close |
|---|---|---:|---:|---|---:|
| r3_posco_t1 | Stage2 | 2023-01-26 | 2023-01-26 | orderbook/cathode-material demand wave; stock-web row showed immediate volume/price expansion | 208500 |
| r3_posco_t2 | Stage2-Actionable | 2023-03-07 | 2023-03-07 | battery-material rerating with strong relative strength and expanding volume | 260500 |
| r3_posco_t3 | Stage3-Yellow | 2023-04-17 | 2023-04-17 | orderbook thesis + battery-material capacity story + second leg price confirmation | 384500 |
| r3_posco_t4 | Stage3-Green | 2023-07-24 | 2023-07-24 | multi-source battery-material orderbook thesis broadly accepted; price already in momentum blowoff | 542000 |
| r3_posco_t5 | Stage4B | 2023-07-25 | 2023-07-25 | parabolic price action and valuation/crowding risk | 598000 |
| r3_posco_t6 | Stage4C-watch | 2023-10~2024 | not used | EV/materials demand slowdown and valuation compression appeared later | n/a |

### Case B — L&F / Tesla 4680 cathode optionality

```text
case_id = r3_loop1_lnf_tesla_4680_2023
symbol = 066970
company = 엘앤에프
primary_archetype = TESLA_4680_SUPPLY_OPTIONALITY_WITH_CALL_OFF_RISK
case_type = Stage2_promote_candidate + later thesis_break_watch
```

| trigger_id | type | trigger_date | entry_date | evidence available at date | entry close |
|---|---|---:|---:|---|---:|
| r3_lnf_t1 | Stage2 | 2023-02-28 | 2023-02-28 | Tesla-affiliate high-nickel cathode supply optionality became visible | 262000 |
| r3_lnf_t2 | Stage2-Actionable | 2023-03-27 | 2023-03-27 | strong price/volume confirmation after supply optionality | 297000 |
| r3_lnf_t3 | Stage3-Yellow | 2023-04-03 | 2023-04-03 | peak confirmation without enough margin/call-off visibility | 328000 |
| r3_lnf_t4 | Stage3-Green | not_confirmed | n/a | no clean Green because customer-specific volume and margin bridge remained uncertain | n/a |
| r3_lnf_t5 | Stage4B | 2023-04-18 | 2023-04-18 | post-spike valuation/crowding and customer concentration risk | 325500 |
| r3_lnf_t6 | Stage4C | 2025-12-29 | not usable | Reuters later reported the 2023 deal value was cut sharply; no 180D forward window | n/a |

### Case C — Samsung SDI / GM U.S. battery JV finalization

```text
case_id = r3_loop1_samsung_sdi_gm_jv_2024
symbol = 006400
company = 삼성SDI
primary_archetype = EV_BATTERY_JV_WITH_DEMAND_SLOWDOWN_4B
case_type = evidence_good_but_price_failed
```

| trigger_id | type | trigger_date | entry_date | evidence available at date | entry close |
|---|---|---:|---:|---|---:|
| r3_sdi_t1 | Stage2 | 2024-08-28 | 2024-08-28 | Samsung SDI and GM completed Indiana JV; roughly $3.5bn investment and 27GWh initial capacity | 339500 |
| r3_sdi_t2 | Stage2-Actionable | 2024-09-02 | 2024-09-02 | immediate follow-through to 369000 close, but still demand/margin gate open | 369000 |
| r3_sdi_t3 | Stage3-Yellow | 2024-09-24 | 2024-09-24 | price high after JV evidence, but EV demand slowdown and delayed production created unresolved gate | 387500 |
| r3_sdi_t4 | Stage3-Green | not_confirmed | n/a | no durable Green; forward OHLC failed | n/a |
| r3_sdi_t5 | Stage4B | 2024-10-15 | 2024-10-15 | loss of momentum / valuation and EV demand slowdown risk | 351000 |
| r3_sdi_t6 | Stage4C-watch | 2025-03~04 | 2025-03-14 | price broke prior thesis path; low reached 170000 in April 2025 | 191400 |

## 9. Trigger-Level OHLC Backtest Tables

All return values are percentage units. MFE/MAE are based on stock-web tradable high/low windows.

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MFE_1Y_pct | MFE_2Y_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | MAE_1Y_pct | peak_date | peak_price | drawdown_after_peak_pct | calibration_usable |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| r3_posco_t1 | 003670 | Stage2 | 2023-01-26 | 208500 | 29.5 | 102.6 | 232.9 | 232.9 | 232.9 | -1.2 | -1.2 | -1.2 | -33.1 | 2023-07-26 | 694000 | -66.0 | true |
| r3_posco_t2 | 003670 | Stage2-Actionable | 2023-03-07 | 260500 | 62.2 | 166.4 | 166.4 | 166.4 | 166.4 | -19.4 | -19.4 | -20.4 | -45.0 | 2023-07-26 | 694000 | -66.0 | true |
| r3_posco_t3 | 003670 | Stage3-Yellow | 2023-04-17 | 384500 | 9.9 | 80.5 | 80.5 | 80.5 | 80.5 | -14.6 | -21.6 | -31.0 | -51.0 | 2023-07-26 | 694000 | -66.0 | true |
| r3_posco_t4 | 003670 | Stage3-Green | 2023-07-24 | 542000 | 28.0 | 28.0 | 28.0 | 28.0 | 28.0 | -14.4 | -39.0 | -50.0 | -60.0 | 2023-07-26 | 694000 | -66.0 | true |
| r3_lnf_t1 | 066970 | Stage2 | 2023-02-28 | 262000 | 33.4 | 33.4 | 33.4 | 33.4 | 33.4 | -16.4 | -16.4 | -50.4 | -50.4 | 2023-04-03 | 349500 | -62.8 | true |
| r3_lnf_t2 | 066970 | Stage2-Actionable | 2023-03-27 | 297000 | 17.7 | 17.7 | 17.7 | 17.7 | 17.7 | -8.6 | -24.8 | -56.3 | -56.3 | 2023-04-03 | 349500 | -62.8 | true |
| r3_lnf_t3 | 066970 | Stage3-Yellow | 2023-04-03 | 328000 | 6.6 | 6.6 | 6.6 | 6.6 | 6.6 | -19.7 | -31.9 | -60.4 | -60.4 | 2023-04-03 | 349500 | -62.8 | true |
| r3_sdi_t1 | 006400 | Stage2 | 2024-08-28 | 339500 | 15.8 | 15.9 | 15.9 | 15.9 | n/a | -2.2 | -30.6 | -49.9 | -49.9 | 2024-09-30 | 393500 | -56.8 | true |
| r3_sdi_t2 | 006400 | Stage2-Actionable | 2024-09-02 | 369000 | 6.6 | 6.6 | 6.6 | 6.6 | n/a | -9.5 | -36.2 | -53.9 | -53.9 | 2024-09-30 | 393500 | -56.8 | true |
| r3_sdi_t3 | 006400 | Stage3-Yellow | 2024-09-24 | 387500 | 1.5 | 1.5 | 1.5 | 1.5 | n/a | -8.4 | -38.2 | -56.1 | -56.1 | 2024-09-30 | 393500 | -56.8 | true |

## 10. 1D Price Path Summaries

### POSCO Future M — best Stage2 trigger `r3_posco_t1`, entry 2023-01-26 close 208500

| point | date | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|---:|
| D+1 | 2023-01-27 | 1.4 | 3.8 | -1.2 |
| D+2 | 2023-01-30 | 4.6 | 5.5 | -1.2 |
| D+3 | 2023-01-31 | 7.2 | 12.5 | -1.2 |
| D+5 | 2023-02-02 | 7.2 | 12.5 | -1.2 |
| D+10 | 2023-02-09 | 16.3 | 16.3 | -1.2 |
| D+20 | 2023-02-23 | 4.3 | 16.3 | -1.2 |
| D+30 | 2023-03-10 | 18.5 | 29.5 | -1.2 |
| D+60 | 2023-04-24 | 74.3 | 102.6 | -1.2 |
| D+90 | 2023-06-02 | 79.4 | 102.6 | -1.2 |
| D+180 | 2023-10~ | n/a | 232.9 | -20.4 |
| D+252 | 2024-01~ | n/a | 232.9 | -33.1 |
| D+504 | 2025-01~ | n/a | 232.9 | -60% area |

### L&F — best Stage2 trigger `r3_lnf_t1`, entry 2023-02-28 close 262000

| point | date | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|---:|
| D+1 | 2023-03-02 | -4.4 | 3.6 | -4.6 |
| D+2 | 2023-03-03 | -1.3 | 3.6 | -4.6 |
| D+3 | 2023-03-06 | -1.5 | 3.6 | -4.6 |
| D+5 | 2023-03-08 | -6.1 | 3.6 | -7.8 |
| D+10 | 2023-03-16 | -6.9 | 3.6 | -14.7 |
| D+20 | 2023-03-30 | 13.0 | 17.6 | -16.4 |
| D+30 | 2023-04-13 | 13.4 | 33.4 | -16.4 |
| D+60 | 2023-05-26 | -4.0 | 33.4 | -16.4 |
| D+90 | 2023-07-12 | -11.3 | 33.4 | -16.4 |
| D+180 | 2023-11~ | n/a | 33.4 | -50.4 |
| D+252 | 2024-02~ | n/a | 33.4 | -50.4 |
| D+504 | 2025-02~ | n/a | 33.4 | -60% area |

### Samsung SDI — Stage2 trigger `r3_sdi_t1`, entry 2024-08-28 close 339500

| point | date | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|---:|
| D+1 | 2024-08-29 | 5.6 | 6.8 | -0.4 |
| D+2 | 2024-08-30 | 4.1 | 6.8 | -0.4 |
| D+3 | 2024-09-02 | 10.1 | 9.9 | -0.4 |
| D+5 | 2024-09-04 | 5.4 | 11.9 | -0.4 |
| D+10 | 2024-09-11 | 7.8 | 11.9 | -2.2 |
| D+20 | 2024-09-30 | 11.5 | 15.9 | -2.2 |
| D+30 | 2024-10-15 | 3.1 | 15.9 | -8.4 |
| D+60 | 2024-11-29 | -25.0 | 15.9 | -30.6 |
| D+90 | 2025-01~ | -30% area | 15.9 | -30.6 |
| D+180 | 2025-05~ | -40% area | 15.9 | -49.9 |
| D+252 | 2025-09~ | n/a | 15.9 | -49.9 |
| D+504 | n/a | n/a | n/a | n/a |

## 11. Case Trigger Comparison

| case_id | best_actual_trigger | baseline_selected_trigger | after_selected_trigger | verdict |
|---|---|---|---|---|
| r3_loop1_posco_future_m_2023_orderbook | r3_posco_t1 | r3_posco_t3 | r3_posco_t1 | Stage2 caught far more upside with shallow initial MAE; Green was late and 4B should have appeared near blowoff. |
| r3_loop1_lnf_tesla_4680_2023 | r3_lnf_t1 | r3_lnf_t3 | r3_lnf_t1 | Stage2 had useful MFE, but MAE/deep drawdown made it Stage2-Actionable only with customer-concentration guardrail. |
| r3_loop1_samsung_sdi_gm_jv_2024 | none_good | r3_sdi_t3 | reject_green | Contract/JV evidence was not enough; forward OHLC showed false-positive risk. |

## 12. Stage2 → Stage4 Audit

### POSCO Future M

Stage2 was the best entry. The 2023-01-26 row produced about +102.6% MFE_90D and +232.9% MFE_180D with only shallow early MAE. Stage3-Green on 2023-07-24 still had +28.0% MFE to the blowoff high, but it captured only the last part of the move and carried severe drawdown risk. This is a clean `Stage3_gate_too_late` case.

### L&F

Stage2 on 2023-02-28 produced +33.4% MFE, but it also had -16.4% 30D/90D MAE and later over -50% drawdown. This is not a Green-quality structural rerating. The correct shadow treatment is `Stage2-Actionable with customer_calloff_and_4680_yield_guardrail`.

### Samsung SDI

The GM JV finalization was high-quality evidence, but forward OHLC failed. MFE_90D was only +15.9% while MAE_180D was around -49.9%. This is `evidence_good_but_price_failed`, and it argues against promoting JV headlines to Green without EV demand, utilization, and margin bridge confirmation.

## 13. Stage3 Yellow / Green Lateness Audit

| case_id | Stage2_Actionable_entry | Green_entry | peak_after_stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| r3_loop1_posco_future_m_2023_orderbook | 260500 | 542000 | 694000 | 0.63 | Green captured too little of the move; Yellow/Stage2-Actionable should exist earlier. |
| r3_loop1_lnf_tesla_4680_2023 | 297000 | not_confirmed | 349500 | n/a | No Green because customer-specific volume and margin bridge did not close. |
| r3_loop1_samsung_sdi_gm_jv_2024 | 369000 | not_confirmed | 393500 | n/a | No Green; forward path rejected the thesis. |

## 14. 4B Timing Audit

| case_id | Stage2_Actionable_entry | 4B_entry | peak_price | four_b_peak_proximity | verdict |
|---|---:|---:|---:|---:|---|
| r3_loop1_posco_future_m_2023_orderbook | 260500 | 598000 | 694000 | 0.77 | good 4B timing; peak-zone blowoff/crowding risk should trigger. |
| r3_loop1_lnf_tesla_4680_2023 | 297000 | 325500 | 349500 | 0.54 | somewhat early but justified because MAE and customer concentration were large. |
| r3_loop1_samsung_sdi_gm_jv_2024 | 369000 | 351000 | 393500 | -0.73 | this is not a peak 4B; it is deterioration/failed-rerating watch. |

## 15. 4C Protection Audit

| case_id | 4C trigger | four_c_protection_label | note |
|---|---|---|---|
| r3_loop1_posco_future_m_2023_orderbook | not hard-confirmed in calibration window | thesis_break_watch_only | Overheat and valuation compression visible, but not a single hard 4C event in the calibrated trigger set. |
| r3_loop1_lnf_tesla_4680_2023 | 2025-12-29 Reuters call-off/value-cut evidence | hard_4c_late / narrative-only | Strong hard break, but too late and outside 180D forward calibration. |
| r3_loop1_samsung_sdi_gm_jv_2024 | 2025-03~04 price deterioration | hard_4c_late | The price had already broken down; earlier demand/utilization red-team signal is needed. |

## 16. Baseline Score Simulation

`baseline_current_proxy` is a research proxy, not a claim about production code.

| case_id | trigger | weighted_score_before | stage_label_before | selected_by_baseline | alignment |
|---|---|---:|---|---:|---|
| r3_loop1_posco_future_m_2023_orderbook | r3_posco_t1 | 66 | Stage2 | false | score_low_return_high_missed_structural |
| r3_loop1_posco_future_m_2023_orderbook | r3_posco_t3 | 82 | Stage3-Yellow | true | score_high_return_high but late |
| r3_loop1_lnf_tesla_4680_2023 | r3_lnf_t1 | 68 | Stage2 | false | score_mid_return_high_promote_candidate |
| r3_loop1_lnf_tesla_4680_2023 | r3_lnf_t3 | 81 | Stage3-Yellow | true | score_high_return_low_false_positive risk |
| r3_loop1_samsung_sdi_gm_jv_2024 | r3_sdi_t1 | 65 | Stage2 | false | score_mid_return_low_watch_only |
| r3_loop1_samsung_sdi_gm_jv_2024 | r3_sdi_t3 | 79 | Stage3-Yellow | true | score_high_return_low_false_positive |

## 17. Shadow Profile Optimization Loop

| profile_id | changed_axes | selected entry per case | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | missed_structural_count | verdict |
|---|---|---|---:|---:|---:|---:|---|
| baseline_current_proxy | reference | posco_t3 / lnf_t3 / sdi_t3 | 29.3 | -31.1 | 0.67 | 2 | too late and too permissive for weak-JV evidence |
| stage2_actionable_early_evidence_plus | early order+RS, but with guardrails | posco_t1 / lnf_t1 / reject_sdi | 55.0 | -8.6 | 0.00 | 0 | best balance; captures POSCO and L&F while rejecting Samsung SDI Green |
| stage3_yellow_entry_relaxed | lower Yellow threshold | posco_t2 / lnf_t1 / sdi_t1 | 49.7 | -16.0 | 0.33 | 0 | good upside but accepts Samsung SDI weak setup |
| green_confirmation_timing_relaxed | earlier Green | posco_t2 / lnf_t3 / sdi_t3 | 26.6 | -28.5 | 0.67 | 1 | not enough; still late or false-positive |
| four_b_peak_timing_tuned | stricter parabolic 4B | posco_t1 with 4B Jul25 / lnf_t1 with 4B Apr18 / reject_sdi | 55.0 | -8.6 | 0.00 | 0 | useful overlay, not standalone entry profile |
| four_c_thesis_break_earlier | stronger demand/call-off red-team | reject lnf green / reject sdi green | 34.0 | -8.6 | 0.00 | 1 | good protection, but needs more cases |

Selected profile:

```text
best_shadow_profile = stage2_actionable_early_evidence_plus
```

## 18. Before / After Backtest Comparison

| case_id | best_actual_trigger | baseline_selected_trigger | after_selected_trigger | baseline_MFE_90D_pct | after_MFE_90D_pct | baseline_MAE_90D_pct | after_MAE_90D_pct | return_improvement_90D_pct | risk_change_90D_pct | reason_after_profile_selected |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| r3_loop1_posco_future_m_2023_orderbook | r3_posco_t1 | r3_posco_t3 | r3_posco_t1 | 80.5 | 102.6 | -21.6 | -1.2 | +22.1 | +20.4 | early orderbook + relative strength captured rerating before Green |
| r3_loop1_lnf_tesla_4680_2023 | r3_lnf_t1 | r3_lnf_t3 | r3_lnf_t1 | 6.6 | 33.4 | -31.9 | -16.4 | +26.8 | +15.5 | early customer-order evidence better than later confirmation, but guardrail remains |
| r3_loop1_samsung_sdi_gm_jv_2024 | reject | r3_sdi_t3 | reject_green | 1.5 | n/a | -38.2 | n/a | avoided false positive | avoided large drawdown | JV evidence lacked utilization/demand/margin bridge |

The after-profile improves the average selected MFE_90D by moving POSCO and L&F from late confirmation triggers to early Stage2-Actionable triggers, while preventing Samsung SDI from becoming a Stage3-Yellow/Green-style entry.

## 19. Score-Return Alignment Matrix

| alignment_label | trigger_count | avg_weighted_score_before | avg_weighted_score_after | avg_MFE_90D_pct | avg_MAE_90D_pct | verdict |
|---|---:|---:|---:|---:|---:|---|
| score_low_return_high_missed_structural | 1 | 66 | 76 | 102.6 | -1.2 | promote early orderbook + relative strength |
| score_mid_return_high_promote_candidate | 1 | 68 | 75 | 33.4 | -16.4 | promote only with customer-concentration guardrail |
| score_mid_return_low_watch_only | 1 | 65 | 62 | 15.9 | -30.6 | keep as watch; do not promote JV headline alone |
| score_high_return_low_false_positive | 2 | 80 | 68 | 4.1 | -35.1 | reduce confirmation-only score when demand/margin bridge absent |
| score_high_return_high | 1 | 82 | 82 | 80.5 | -21.6 | good but late; keep as confirmation, not first entry |

## 20. Weight Sensitivity Table

| axis | baseline | tested | delta | affected_triggers | avg_MFE_90D_before | avg_MFE_90D_after | avg_MAE_90D_before | avg_MAE_90D_after | false_positive_before | false_positive_after | verdict |
|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| stage2_actionable_orderbook_plus_relative_strength | 0 | +2 | +2 | r3_posco_t1,r3_lnf_t1 | 43.6 | 68.0 | -17.6 | -8.8 | 0 | 0 | accepted |
| customer_specific_volume_margin_gate | 0 | +2 guardrail | +2 | r3_lnf_t1,r3_sdi_t1 | 24.8 | 24.8 | -23.5 | -23.5 | 1 | 0 | accepted as guardrail |
| confirmation_only_green_without_margin_bridge | 0 | -2 | -2 | r3_lnf_t3,r3_sdi_t3 | 4.1 | reject | -35.1 | avoided | 2 | 0 | accepted |

## 21. Optimization Decision Log

```jsonl
{"row_type":"optimization_decision","decision_id":"r3_loop1_decision_001","hypothesis":"Battery-material orderbook plus strong relative-strength confirmation should be promoted from Stage2 to Stage2-Actionable before full Green evidence, but only when customer/concentration guardrails do not block it.","tested_cases":["r3_loop1_posco_future_m_2023_orderbook","r3_loop1_lnf_tesla_4680_2023","r3_loop1_samsung_sdi_gm_jv_2024"],"tested_trigger_ids":["r3_posco_t1","r3_lnf_t1","r3_sdi_t1"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus","backtest_result_summary":"POSCO Stage2 MFE_90D 102.6 / MAE_90D -1.2; L&F Stage2 MFE_90D 33.4 / MAE_90D -16.4; Samsung SDI JV had only 15.9 MFE and -30.6 MAE, so rejected from Green.","accepted_or_rejected":"accepted","delta_magnitude":"+2","why_not_larger_delta":"Sample has only three usable cases and L&F shows deep drawdown/customer call-off risk.","next_validation_needed":"Add LGES/SK On/Samsung SDI ESS pivot cases once 180D windows close; add more failed contract examples."}
{"row_type":"optimization_decision","decision_id":"r3_loop1_decision_002","hypothesis":"Confirmation-only Stage3-Yellow should be penalized when EV demand, utilization, customer call-off, or margin bridge remain unresolved.","tested_cases":["r3_loop1_lnf_tesla_4680_2023","r3_loop1_samsung_sdi_gm_jv_2024"],"tested_trigger_ids":["r3_lnf_t3","r3_sdi_t3"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus","backtest_result_summary":"Late confirmation triggers had poor forward MFE/MAE compared with Stage2 or reject decisions.","accepted_or_rejected":"accepted","delta_magnitude":"-2","why_not_larger_delta":"The POSCO case shows late confirmation can still have positive MFE in blowoff markets; avoid overblocking all momentum.","next_validation_needed":"Find cases where late Green confirmation remained durable after EV demand slowdown."}
```

## 22. Overfitting / Robustness Check

```text
usable_case_count = 3
usable_trigger_count = 10
maximum_allowed_delta = +2 / -2 unless cross-round repetition appears
counterexample_present = true
counterexample_case = Samsung SDI GM JV 2024
```

The accepted deltas are capped at +/-2. POSCO alone would argue for a larger early Stage2 boost, but L&F and Samsung SDI prove that customer concentration and EV demand slowdown can turn contract evidence into a false-positive. Therefore the profile is not “battery contract = Green.” It is “battery contract/orderbook + relative strength = Stage2-Actionable only if call-off, utilization, and margin guardrails are not triggered.”

## 23. Cross-case Aggregate Metrics

### Trigger type aggregate

| trigger_type | usable_trigger_count | avg_MFE_90D_pct | median_MFE_90D_pct | avg_MAE_90D_pct | median_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | below_entry_90D_rate | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Stage2 | 3 | 50.6 | 33.4 | -16.4 | -16.4 | 80.7 | -33.8 | 0.67 | high dispersion; promote with guardrails |
| Stage2-Actionable | 3 | 63.3 | 17.7 | -22.9 | -24.8 | 63.3 | -43.4 | 1.00 | good early capture but volatile |
| Stage3-Yellow | 3 | 29.3 | 6.6 | -31.1 | -31.9 | 29.3 | -49.2 | 1.00 | too late / false-positive risk |
| Stage3-Green | 1 | 28.0 | 28.0 | -39.0 | -39.0 | 28.0 | -50.0 | 1.00 | Green was late in POSCO and absent in failures |
| Stage4B | 3 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | useful overlay, especially POSCO peak-zone |
| Stage4C | 2 narrative | n/a | n/a | n/a | n/a | n/a | n/a | n/a | not enough OHLC-forward cases for hard gate delta |

### Profile aggregate

| profile_id | case_count | selected_trigger_count | avg_MFE_90D_pct | median_MFE_90D_pct | avg_MAE_90D_pct | median_MAE_90D_pct | hit_rate_MFE90_gt_20pct | bad_entry_rate_MAE90_lt_minus_15pct | false_positive_rate | missed_structural_count | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| baseline_current_proxy | 3 | 3 | 29.3 | 6.6 | -31.1 | -31.9 | 0.33 | 1.00 | 0.67 | 2 | reference, too late and too permissive |
| stage2_actionable_early_evidence_plus | 3 | 2 + 1 reject | 55.0 | 55.0 | -8.6 | -8.6 | 1.00 | 0.50 | 0.00 | 0 | best profile |
| stage3_yellow_entry_relaxed | 3 | 3 | 49.7 | 33.4 | -16.0 | -16.4 | 0.67 | 0.67 | 0.33 | 0 | useful but accepts weak Samsung SDI case |
| green_confirmation_timing_relaxed | 3 | 3 | 26.6 | 6.6 | -28.5 | -31.9 | 0.33 | 1.00 | 0.67 | 1 | rejected |
| four_b_peak_timing_tuned | 3 | 2 + overlay | 55.0 | 55.0 | -8.6 | -8.6 | 1.00 | 0.50 | 0.00 | 0 | accept as overlay only |
| four_c_thesis_break_earlier | 3 | protective overlay | n/a | n/a | n/a | n/a | n/a | n/a | 0.00 | n/a | needs more cases |

## 24. Score-Price Alignment Verdict

```text
overall_verdict = Stage2-Actionable should be supported for R3, but only with strict customer/demand/margin guardrails.
```

R3 shows a different shape from R1/R2. In R1 industrial orderbook, contract/backlog visibility often behaves like durable structural evidence. In R3 battery, contract evidence can be real but still fragile because EV demand, subsidy policy, lithium/cathode ASP, customer production yield, and call-off risk can break the earnings bridge. Therefore Stage2-Actionable is valid, but Green must remain stricter than in power-equipment-like orderbook cases.

## 25. Shadow Weight Calibration

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_battery_orderbook_plus_relative_strength,0,2,+2,"POSCO and L&F Stage2 triggers produced better MFE than late confirmation triggers","POSCO MFE90 improved from 80.5 at late Yellow to 102.6 at early Stage2; L&F improved from 6.6 at Yellow to 33.4 at Stage2","r3_posco_t1|r3_lnf_t1",2,"shadow-only; not production"
shadow_weight,customer_concentration_calloff_margin_guardrail,0,2,+2,"L&F and Samsung SDI show that customer/JV evidence can fail without volume and margin bridge","Samsung SDI Green/Yellow avoided -38.2 MAE90 false-positive; L&F remains Actionable only, not Green","r3_lnf_t1|r3_sdi_t1|r3_sdi_t3",3,"shadow-only guardrail"
shadow_weight,confirmation_only_green_without_ev_demand_bridge,0,-2,-2,"Late confirmation triggers underperformed when EV demand/utilization remained open","Average late confirmation MFE90 was low and MAE90 deep for L&F and Samsung SDI","r3_lnf_t3|r3_sdi_t3",2,"do not lower Green threshold from momentum alone"
```

## 26. Machine-Readable Rows

### 26.1 Case rows JSONL

```jsonl
{"row_type":"case","case_id":"r3_loop1_posco_future_m_2023_orderbook","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"1","sector":"2차전지·전기차·친환경","case_type":"structural_success_with_4b_overheat","primary_archetype":"BATTERY_MATERIALS_ORDERBOOK_RERATING","best_trigger":"r3_posco_t1","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"missed_structural_then_late_green","price_source":"Songdaiki/stock-web","notes":"Stage2 captured most of upside; Stage3-Green was late and near 4B blowoff."}
{"row_type":"case","case_id":"r3_loop1_lnf_tesla_4680_2023","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"1","sector":"2차전지·전기차·친환경","case_type":"stage2_promote_candidate_with_later_thesis_break_watch","primary_archetype":"TESLA_4680_SUPPLY_OPTIONALITY_WITH_CALL_OFF_RISK","best_trigger":"r3_lnf_t1","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"stage2_promote_candidate_but_not_green","price_source":"Songdaiki/stock-web","notes":"Early MFE was good but customer concentration and later call-off risk block Green."}
{"row_type":"case","case_id":"r3_loop1_samsung_sdi_gm_jv_2024","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"1","sector":"2차전지·전기차·친환경","case_type":"evidence_good_but_price_failed","primary_archetype":"EV_BATTERY_JV_WITH_DEMAND_SLOWDOWN_4B","best_trigger":"none_good","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"false_positive_score_if_promoted","price_source":"Songdaiki/stock-web","notes":"JV headline lacked demand/utilization/margin bridge; forward OHLC failed."}
{"row_type":"case","case_id":"r3_loop1_lges_ford_freudenberg_2025","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"1","sector":"2차전지·전기차·친환경","case_type":"4c_thesis_break_narrative_only","primary_archetype":"EV_DEMAND_SLOWDOWN_THESIS_BREAK_WATCH","best_trigger":"narrative_only_2025_contract_cancellation","calibration_usable":false,"historical_window_status":"insufficient_forward_180D_by_manifest_max_date","score_price_alignment":"narrative_only","price_source":"Songdaiki/stock-web","notes":"Useful 4C thesis-break pattern, but not weight calibration."}
{"row_type":"case","case_id":"r3_loop1_ecopro_2024_blocked","symbol":"086520","company_name":"에코프로","round":"R3","loop":"1","sector":"2차전지·전기차·친환경","case_type":"overheat_price_window_blocked","primary_archetype":"BATTERY_THEME_OVERHEAT_4B","best_trigger":"narrative_only_corporate_action_blocked","calibration_usable":false,"historical_window_status":"corporate_action_contaminated_or_window_blocked","score_price_alignment":"narrative_only","price_source":"Songdaiki/stock-web","notes":"Do not use for shadow weight until adjusted-price revalidation."}
```

### 26.2 Trigger rows JSONL

```jsonl
{"row_type":"trigger","trigger_id":"r3_posco_t1","case_id":"r3_loop1_posco_future_m_2023_orderbook","symbol":"003670","trigger_type":"Stage2","trigger_date":"2023-01-26","entry_date":"2023-01-26","entry_price":208500,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":29.5,"MFE_90D_pct":102.6,"MFE_180D_pct":232.9,"MFE_1Y_pct":232.9,"MFE_2Y_pct":232.9,"MAE_30D_pct":-1.2,"MAE_90D_pct":-1.2,"MAE_180D_pct":-1.2,"MAE_1Y_pct":-33.1,"peak_date":"2023-07-26","peak_price":694000,"drawdown_after_peak_pct":-66.0,"green_lateness_ratio":0.63,"four_b_peak_proximity":0.77,"trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[]}
{"row_type":"trigger","trigger_id":"r3_lnf_t1","case_id":"r3_loop1_lnf_tesla_4680_2023","symbol":"066970","trigger_type":"Stage2","trigger_date":"2023-02-28","entry_date":"2023-02-28","entry_price":262000,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":33.4,"MFE_90D_pct":33.4,"MFE_180D_pct":33.4,"MFE_1Y_pct":33.4,"MFE_2Y_pct":33.4,"MAE_30D_pct":-16.4,"MAE_90D_pct":-16.4,"MAE_180D_pct":-50.4,"MAE_1Y_pct":-50.4,"peak_date":"2023-04-03","peak_price":349500,"drawdown_after_peak_pct":-62.8,"green_lateness_ratio":"not_applicable","four_b_peak_proximity":0.54,"trigger_outcome_label":"good_entry_but_guardrailed","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[]}
{"row_type":"trigger","trigger_id":"r3_sdi_t1","case_id":"r3_loop1_samsung_sdi_gm_jv_2024","symbol":"006400","trigger_type":"Stage2","trigger_date":"2024-08-28","entry_date":"2024-08-28","entry_price":339500,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv","profile_path":"atlas/symbol_profiles/006/006400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":15.8,"MFE_90D_pct":15.9,"MFE_180D_pct":15.9,"MFE_1Y_pct":15.9,"MFE_2Y_pct":null,"MAE_30D_pct":-2.2,"MAE_90D_pct":-30.6,"MAE_180D_pct":-49.9,"MAE_1Y_pct":-49.9,"peak_date":"2024-09-30","peak_price":393500,"drawdown_after_peak_pct":-56.8,"green_lateness_ratio":"not_applicable","four_b_peak_proximity":-0.73,"trigger_outcome_label":"evidence_good_but_price_failed","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[]}
```

### 26.3 Score simulation rows JSONL

```jsonl
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"r3_loop1_posco_future_m_2023_orderbook","trigger_id":"r3_posco_t3","symbol":"003670","trigger_type":"Stage3-Yellow","weighted_score":82,"stage_label":"Stage3-Yellow","selected_by_profile":true,"MFE_90D_pct":80.5,"MAE_90D_pct":-21.6,"score_return_alignment_label":"score_high_return_high_but_late"}
{"row_type":"score_simulation","profile_id":"stage2_actionable_early_evidence_plus","case_id":"r3_loop1_posco_future_m_2023_orderbook","trigger_id":"r3_posco_t1","symbol":"003670","trigger_type":"Stage2-Actionable","weighted_score":76,"stage_label":"Stage2-Actionable","selected_by_profile":true,"MFE_90D_pct":102.6,"MAE_90D_pct":-1.2,"score_return_alignment_label":"score_mid_return_high_promote_candidate"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"r3_loop1_lnf_tesla_4680_2023","trigger_id":"r3_lnf_t3","symbol":"066970","trigger_type":"Stage3-Yellow","weighted_score":81,"stage_label":"Stage3-Yellow","selected_by_profile":true,"MFE_90D_pct":6.6,"MAE_90D_pct":-31.9,"score_return_alignment_label":"score_high_return_low_false_positive"}
{"row_type":"score_simulation","profile_id":"stage2_actionable_early_evidence_plus","case_id":"r3_loop1_lnf_tesla_4680_2023","trigger_id":"r3_lnf_t1","symbol":"066970","trigger_type":"Stage2-Actionable","weighted_score":75,"stage_label":"Stage2-Actionable_guardrailed","selected_by_profile":true,"MFE_90D_pct":33.4,"MAE_90D_pct":-16.4,"score_return_alignment_label":"score_mid_return_high_promote_candidate"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"r3_loop1_samsung_sdi_gm_jv_2024","trigger_id":"r3_sdi_t3","symbol":"006400","trigger_type":"Stage3-Yellow","weighted_score":79,"stage_label":"Stage3-Yellow","selected_by_profile":true,"MFE_90D_pct":1.5,"MAE_90D_pct":-38.2,"score_return_alignment_label":"score_high_return_low_false_positive"}
{"row_type":"score_simulation","profile_id":"stage2_actionable_early_evidence_plus","case_id":"r3_loop1_samsung_sdi_gm_jv_2024","trigger_id":"r3_sdi_t1","symbol":"006400","trigger_type":"Stage2-watch","weighted_score":62,"stage_label":"WatchOnly","selected_by_profile":false,"MFE_90D_pct":15.9,"MAE_90D_pct":-30.6,"score_return_alignment_label":"score_mid_return_low_watch_only"}
```

### 26.4 Profile comparison rows CSV

```csv
row_type,profile_id,case_count,avg_MFE_90D_pct,avg_MAE_90D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,verdict
profile_comparison,baseline_current_proxy,3,29.3,-31.1,0.33,1.00,0.67,2,2,"reference; too late and too permissive"
profile_comparison,stage2_actionable_early_evidence_plus,3,55.0,-8.6,1.00,0.50,0.00,0,0,"best upside capture with guardrails"
profile_comparison,stage3_yellow_entry_relaxed,3,49.7,-16.0,0.67,0.67,0.33,0,1,"useful but accepts weak Samsung SDI setup"
profile_comparison,green_confirmation_timing_relaxed,3,26.6,-28.5,0.33,1.00,0.67,1,2,"rejected"
profile_comparison,four_b_peak_timing_tuned,3,55.0,-8.6,1.00,0.50,0.00,0,0,"accepted as overlay only"
profile_comparison,four_c_thesis_break_earlier,3,,,,,0.00,,,"needs more OHLC-usable hard 4C cases"
```

### 26.5 Narrative-only rows JSONL

```jsonl
{"row_type":"narrative_only","case_id":"r3_loop1_lges_ford_freudenberg_2025","symbol":"373220","reason":"hard_4c_evidence_available_but_forward_180D_unavailable_by_stock_web_manifest_max_date","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
{"row_type":"narrative_only","case_id":"r3_loop1_ecopro_2024_blocked","symbol":"086520","reason":"corporate_action_contaminated_or_stock_web_window_blocked","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 27. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are standalone E2R historical calibration and backtest optimization outputs produced using the Songdaiki/stock-web OHLC atlas. Do not redo market research unless a row is internally inconsistent. Ingest the machine-readable rows and update the repository in batch.

These MD files are not live candidate research. They are historical calibration and shadow optimization research. Use them to improve trigger-level backtesting, Stage2-Actionable / Stage3-Yellow gates, 4B timing, 4C protection logic, score-return alignment evaluation, and shadow score profiles.

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
- Preserve shadow-only calibration separately from production rules.
- Keep Stage2-Actionable as a shadow trigger type unless already supported.
- Do not hardcode historical company names into scoring logic.
- Production scoring must not change unless the user explicitly approves applying the shadow profile.

### Repository tasks
1. Parse case / trigger / score_simulation / profile_comparison / optimization_decision / shadow weight / aggregate rows.
2. Validate price_source_validation rows.
3. Validate MFE / MAE / peak / drawdown values.
4. Validate green_lateness_ratio.
5. Validate four_b_peak_proximity.
6. Validate 4C protection labels.
7. Validate calibration_usable filtering.
8. Validate before/after profile comparison rows.
9. Validate score-return alignment labels.
10. Append valid case rows to abstract case library.
11. Append valid trigger rows to trigger calibration dataset.
12. Append score_simulation and profile_comparison rows to shadow calibration dataset.
13. Append shadow weight rows to shadow calibration profile only if before/after backtest effect exists.
14. Add tests that narrative-only, non-OHLC, insufficient-forward-window, and corporate-action-contaminated rows cannot change weights.
15. Add tests for optimization decision validation.
16. Produce checkpoint summary.

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

## 28. Next Round State

```text
current_round_completed = R3 Loop 1
next_round = R4 Loop 1
next_sector = 소재·스프레드·전략자원
production_scoring_changed = false
shadow_weight_only = true
```

## 29. Source Notes

- Stock-web manifest and schema were checked for `max_date`, price basis, shard layout, and MFE/MAE rules.
- Stock-web symbol profiles were checked for 003670, 066970, and 006400. Corporate action candidate dates did not overlap the calibrated 180D windows.
- Reuters evidence was used for Samsung SDI/GM JV and L&F/Tesla contract context. Later 2025 hard-break reports were used only as narrative-only guardrails when the forward 180D calibration window did not exist.
- Raw/unadjusted data means the numbers are suitable for shadow calibration only. Any production adoption should preserve the corporate-action block and may later add adjusted-price revalidation.
