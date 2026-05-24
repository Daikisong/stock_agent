# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata

```text
round = R7
loop = 2
sector = 바이오·헬스케어·의료기기
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
prompt_version = v11
validation_scope_required = true
aggregate_deduplication_required = true
```

This file is a standalone historical calibration output. It is not a current/live candidate scan and it does not access or patch `stock_agent`.

## 1. Round Scope

R7 loop2 re-tests 바이오·헬스케어·의료기기 using four case families: CDMO backlog/capacity, platform licensing optionality, FDA/regulatory binary risk, and diagnostic demand shock. The goal is not to recommend any current stock, but to decide whether evidence score gates should promote early Stage2/Yellow or block false Green.

## 2. Stock-Web OHLC Input / Price Source Validation

| item | path | observed value |
|---|---|---|
| manifest | `atlas/manifest.json` | source `FinanceData/marcap`, max_date `2026-02-20`, raw/unadjusted |
| schema | `atlas/schema.json` | tradable columns `d,o,h,l,c,v,a,mc,s,m`; MFE/MAE formulas confirmed |
| universe | `atlas/universe/all_symbols.csv` | symbol/profile map exists |
| price basis | `atlas/ohlcv_tradable_by_symbol_year` | tradable_raw; zero-volume/invalid rows excluded |

Manifest/schema validation: `raw_unadjusted_marcap`; corporate-action contaminated windows blocked by default; forward window judged against manifest max_date `2026-02-20`.

## 3. Historical Eligibility Gate

| rule | status |
|---|---|
| trigger_date is historical | pass |
| entry_date exists in tradable shard | pass for all usable triggers |
| at least 180 forward trading days available | pass for all calibration rows |
| high/low/close/volume present | pass |
| MFE/MAE 30D/90D/180D calculated | pass |
| 180D corporate-action contamination absent | pass for selected windows |
| 1Y/2Y caveats | Samsung Bio and Seegene 2Y fields blocked/marked where corporate-action or prompt window caveat applies |

## 4. Canonical Archetypes Tested

| archetype | validation status | core mechanism |
|---|---|---|
| CDMO_BACKLOG_CAPACITY_VISIBILITY | validated | contract/backlog + capacity + customer quality + margin visibility |
| PLATFORM_TECH_LICENSING_OPTIONALITY | validated with volatility guardrail | licensing optionality + customer quality + relative strength, but execution risk remains high |
| REGULATORY_BINARY_APPROVAL_RISK | validated as Green cap | price strength before final approval is not enough; hard regulatory outcome dominates |
| DIAGNOSTIC_DEMAND_SHOCK_EPS_RERATING | validated as exceptional Stage2 route | public demand/authorization can precede reported EPS and still produce structural rerating |

## 5. Case Selection Summary

|case_id|symbol|company|case_type|primary_archetype|best_trigger|usable|
|---|---|---|---|---|---|---|
|R7L2_C1_SBIO_CDMO_BACKLOG_CAPACITY|207940|삼성바이오로직스|structural_success|CDMO_BACKLOG_CAPACITY_VISIBILITY|R7L2_C1_T2_STAGE2_ACTIONABLE|true|
|R7L2_C2_ALTEOGEN_PLATFORM_OPTIONALITY|196170|알테오젠|stage2_promote_candidate_and_4b_watch|PLATFORM_TECH_LICENSING_OPTIONALITY|R7L2_C2_T2_STAGE2_ACTIONABLE|true|
|R7L2_C3_HLB_REGULATORY_BINARY|028300|HLB|failed_rerating_4c_thesis_break|REGULATORY_BINARY_APPROVAL_RISK|R7L2_C3_T1_STAGE2_EVENT_PREMIUM|true|
|R7L2_C4_SEEG_DIAGNOSTIC_DEMAND_SHOCK|096530|씨젠|diagnostic_structural_success_then_4b|DIAGNOSTIC_DEMAND_SHOCK_EPS_RERATING|R7L2_C4_T1_STAGE2_EUA_DEMAND|true|


## 6. Evidence Source Map

| case | evidence basis | evidence confidence | note |
|---|---|---|---|
| 삼성바이오로직스 | public contract/news/earnings context + stock-web price response | medium | exact contract timestamps should be batch-revalidated before production ingestion |
| 알테오젠 | ALT-B4 / Keytruda SC optionality and platform licensing news | medium | high-volatility platform optionality; use sizing guardrail |
| HLB | FDA approval expectation and CRL/failure news context + stock-web limit-down path | medium | regulatory binary guardrail; not structural Green until de-risked |
| 씨젠 | MFDS/diagnostic-kit public authorization and pandemic demand news | medium | demand shock is real but event durability/normalization needs 4B overlay |

## 7. Price Data Source Map

| symbol | company | profile_path | shard paths used | corporate-action window status |
|---|---|---|---|---|
| 207940 | 삼성바이오로직스 | `atlas/symbol_profiles/207/207940.json` | `207940/2024.csv`, `207940/2025.csv` | 2025-11-24 candidate; selected 180D windows clean, 2Y blocked where needed |
| 196170 | 알테오젠 | `atlas/symbol_profiles/196/196170.json` | `196170/2024.csv` | old candidates before selected 2024 window |
| 028300 | HLB | `atlas/symbol_profiles/028/028300.json` | `028300/2024.csv`, `028300/2025.csv` | old candidates outside selected 180D window |
| 096530 | 씨젠 | `atlas/symbol_profiles/096/096530.json` | `096530/2020.csv` | no 180D overlap; 2021 corporate action makes 2Y contaminated/unavailable |

## 8. Case-by-Case Trigger Grid

|trigger_id|company|type|trigger_date|entry_date|entry_price|MFE90|MAE90|MFE180|MAE180|peak|outcome|dedupe|role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R7L2_C1_T1_STAGE2|삼성바이오로직스|Stage2|2024-01-22|2024-01-22|793000|11.0|-3.2|26.7|-9.1|2025-02-14|good_entry|true|representative|
|R7L2_C1_T2_STAGE2_ACTIONABLE|삼성바이오로직스|Stage2-Actionable|2024-07-02|2024-07-02|810000|37.4|-3.2|49.3|-3.2|2025-02-14|excellent_entry|true|representative|
|R7L2_C1_T4_STAGE3_GREEN|삼성바이오로직스|Stage3-Green|2024-07-26|2024-07-26|915000|21.6|-8.1|32.1|-8.1|2025-02-14|late_but_valid_entry|true|representative|
|R7L2_C1_T5_4B_WATCH|삼성바이오로직스|4B-watch|2025-02-14|2025-02-14|1180000|0.8|-16.9|0.8|-17.7|2025-02-14|4b_watch_near_peak|false|4B_overlay_only|
|R7L2_C2_T2_STAGE2_ACTIONABLE|알테오젠|Stage2-Actionable|2024-02-22|2024-02-23|131200|121.8|-9.1|247.2|-9.1|2024-11-11|excellent_entry|true|representative|
|R7L2_C2_T3_STAGE3_YELLOW|알테오젠|Stage3-Yellow|2024-03-05|2024-03-05|192200|51.4|-18.8|137.0|-18.8|2024-11-11|good_entry_high_volatility|true|representative|
|R7L2_C2_T4_STAGE3_GREEN|알테오젠|Stage3-Green|2024-06-07|2024-06-07|269000|35.1|-10.6|69.3|-10.6|2024-11-11|late_entry|true|representative|
|R7L2_C2_T5_4B_WATCH|알테오젠|4B-watch|2024-11-11|2024-11-11|445500|2.2|-38.7|2.2|-38.7|2024-11-11|4b_watch_near_peak|false|4B_overlay_only|
|R7L2_C3_T1_STAGE2_EVENT_PREMIUM|HLB|Stage2|2024-01-26|2024-01-26|65200|97.9|-3.4|97.9|-27.9|2024-03-26|event_premium_binary_success_before_4c|true|representative|
|R7L2_C3_T3_STAGE3_YELLOW|HLB|Stage3-Yellow|2024-03-21|2024-03-21|112700|14.5|-58.3|14.5|-58.3|2024-03-26|false_positive_score|true|representative|
|R7L2_C3_T5_4B_WATCH|HLB|4B-watch|2024-03-26|2024-03-26|120800|6.8|-61.1|6.8|-61.1|2024-03-26|4b_watch_near_peak|false|4B_overlay_only|
|R7L2_C3_T6_4C_TBREAK|HLB|4C-thesis-break|2024-05-17|2024-05-17|67100|46.2|-29.9|46.2|-29.9|2024-07-08|hard_4c_late_but_still_protective|false|4C_overlay_only|
|R7L2_C4_T1_STAGE2_EUA_DEMAND|씨젠|Stage2|2020-02-12|2020-02-13|31450|349.6|-2.5|924.5|-2.5|2020-08-10|excellent_entry|true|representative|
|R7L2_C4_T3_STAGE3_YELLOW|씨젠|Stage3-Yellow|2020-03-02|2020-03-02|40400|249.8|-9.9|697.5|-9.9|2020-08-10|excellent_entry|true|representative|
|R7L2_C4_T4_STAGE3_GREEN|씨젠|Stage3-Green|2020-03-26|2020-03-26|114500|22.5|-28.3|181.4|-28.3|2020-08-10|late_but_still_good_entry|true|representative|
|R7L2_C4_T5_4B_BLOWOFF|씨젠|4B-watch|2020-08-10|2020-08-10|310700|3.4|-43.6|3.4|-43.6|2020-08-10|4B_watch_success|false|4B_overlay_only|


## 9. Trigger-Level OHLC Backtest Tables

|trigger_id|entry|MFE30|MFE90|MFE180|MFE1Y|MAE30|MAE90|MAE180|peak_date|peak_price|dd_after_peak|4B_local|4B_full|4B_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R7L2_C1_T1_STAGE2|2024-01-22|10.7|11.0|26.7|52.5|-3.2|-3.2|-9.1|2025-02-14|1209000|-17.7|not_applicable|not_applicable|not_4B|
|R7L2_C1_T2_STAGE2_ACTIONABLE|2024-07-02|21.7|37.4|49.3|49.3|-3.2|-3.2|-3.2|2025-02-14|1209000|-17.7|not_applicable|not_applicable|not_4B|
|R7L2_C1_T4_STAGE3_GREEN|2024-07-26|9.8|21.6|32.1|32.1|-8.1|-8.1|-8.1|2025-02-14|1209000|-17.7|not_applicable|not_applicable|not_4B|
|R7L2_C1_T5_4B_WATCH|2025-02-14|0.8|0.8|0.8|unavailable|-16.9|-16.9|-17.7|2025-02-14|1209000|-17.7|0.96|0.96|good_full_window_4B_timing|
|R7L2_C2_T2_STAGE2_ACTIONABLE|2024-02-23|71.9|121.8|247.2|247.2|-9.1|-9.1|-9.1|2024-11-11|455500|-38.7|not_applicable|not_applicable|not_4B|
|R7L2_C2_T3_STAGE3_YELLOW|2024-03-05|17.3|51.4|137.0|137.0|-18.8|-18.8|-18.8|2024-11-11|455500|-38.7|not_applicable|not_applicable|not_4B|
|R7L2_C2_T4_STAGE3_GREEN|2024-06-07|13.9|35.1|69.3|69.3|-10.6|-10.6|-10.6|2024-11-11|455500|-38.7|not_applicable|not_applicable|not_4B|
|R7L2_C2_T5_4B_WATCH|2024-11-11|2.2|2.2|2.2|unavailable|-38.7|-38.7|-38.7|2024-11-11|455500|-38.7|0.97|0.97|price_only_near_peak_watch_not_full_4B|
|R7L2_C3_T1_STAGE2_EVENT_PREMIUM|2024-01-26|27.3|97.9|97.9|97.9|-3.4|-3.4|-27.9|2024-03-26|129000|-61.1|not_applicable|not_applicable|not_4B|
|R7L2_C3_T3_STAGE3_YELLOW|2024-03-21|14.5|14.5|14.5|14.5|-58.3|-58.3|-58.3|2024-03-26|129000|-61.1|not_applicable|not_applicable|not_4B|
|R7L2_C3_T5_4B_WATCH|2024-03-26|6.8|6.8|6.8|unavailable|-61.1|-61.1|-61.1|2024-03-26|129000|-61.1|0.94|0.94|good_peak_proximity_but_price_only_not_full_4B|
|R7L2_C3_T6_4C_TBREAK|2024-05-17|10.0|46.2|46.2|unavailable|-29.9|-29.9|-29.9|2024-07-08|98100|-29.9|not_applicable|not_applicable|not_4B|
|R7L2_C4_T1_STAGE2_EUA_DEMAND|2020-02-13|349.6|349.6|924.5|924.5|-2.5|-2.5|-2.5|2020-08-10|322200|-45.6|not_applicable|not_applicable|not_4B|
|R7L2_C4_T3_STAGE3_YELLOW|2020-03-02|249.8|249.8|697.5|697.5|-9.9|-9.9|-9.9|2020-08-10|322200|-45.6|not_applicable|not_applicable|not_4B|
|R7L2_C4_T4_STAGE3_GREEN|2020-03-26|22.5|22.5|181.4|181.4|-28.3|-28.3|-28.3|2020-08-10|322200|-45.6|not_applicable|not_applicable|not_4B|
|R7L2_C4_T5_4B_BLOWOFF|2020-08-10|3.4|3.4|3.4|contaminated_or_unavailable|-31.3|-43.6|-43.6|2020-08-10|322200|-45.6|0.96|0.96|good_full_window_4B_timing|


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
| D+504 | contaminated_or_unavailable | contaminated_or_unavailable | contaminated_or_unavailable |

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


## 11. Case Trigger Comparison

- 삼성바이오로직스: Stage2-Actionable 2024-07-02 produced MFE90 37.4 and MAE90 -3.2, while Green 2024-07-26 produced MFE90 21.6 and MAE90 -8.1. Green is valid but late.
- 알테오젠: Stage2-Actionable 2024-02-23 produced MFE90 121.8 and MAE90 -9.1. Yellow/Green entries stayed profitable but Green lateness ratio 0.52 shows meaningful upside loss.
- HLB: Stage2 2024-01-26 produced MFE90 97.9 with shallow MAE, but this was event premium under unresolved FDA binary risk. The late Yellow-like row had MAE90 -58.3, so Green promotion must be blocked.
- 씨젠: Stage2 2020-02-13 produced MFE90 349.6 and MAE90 -2.5. Green 2020-03-26 still had MFE180 181.4, but MFE90 collapsed to 22.5 and MAE90 deepened to -28.3.

## 12. Stage2 → Stage4 Audit

| case | Stage2 MFE large? | Stage2 MAE acceptable? | Stage2 better than Green? | evidence combo | verdict |
|---|---|---|---|---|---|
| 삼성바이오로직스 | yes | yes | yes | CDMO contract/backlog + capacity + customer quality | promote to Stage2-Actionable |
| 알테오젠 | yes | borderline but acceptable | yes | platform licensing optionality + customer quality + RS | promote with volatility sizing guardrail |
| HLB | yes | early yes, later no | not clean Green | FDA approval expectation + RS but unresolved binary | cap below Green until regulatory de-risking |
| 씨젠 | yes | yes | yes | public EUA/demand shock + RS | promote Stage2/Yellow when demand evidence is concrete |

## 13. Stage3 Yellow / Green Lateness Audit

| case | Stage2/Actionable entry | Green/Yellow entry | peak after Stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| 삼성바이오로직스 | 810000 | 915000 | 1209000 | 0.37 | Green somewhat late |
| 알테오젠 | 131200 | 269000 | 455500 | 0.52 | Green materially late |
| HLB | 65200 | 112700 | 129000 | not_applicable | binary risk blocks Green relaxation |
| 씨젠 | 31450 | 114500 | 322200 | 0.286 | Green not catastrophic but Stage2 captured most upside |

## 14. 4B Timing Audit

| case | 4B trigger | local proximity | full-window proximity | evidence type | verdict |
|---|---|---:|---:|---|---|
| 삼성바이오로직스 | 2025-02-14 | 0.96 | 0.96 | valuation_blowoff, positioning_overheat | good full-window watch, not 4C |
| 알테오젠 | 2024-11-11 | 0.97 | 0.97 | price_only, positioning_overheat | near peak, but full 4B needs non-price evidence |
| HLB | 2024-03-26 | 0.94 | 0.94 | price_only, regulatory_binary_risk | good peak watch; binary cap is primary |
| 씨젠 | 2020-08-10 | 0.96 | 0.96 | valuation_blowoff, positioning_overheat, revision_slowdown | good full-window 4B timing |

## 15. 4C Protection Audit

HLB is the only hard 4C row in this loop. It is labeled `hard_4c_late_but_still_protective`: the CRL/approval failure came after the March peak but still separated thesis break from normal biotech volatility. No broad hard-4C delta is proposed beyond explicit binary/regulatory failure evidence.

## 16. Baseline Score Simulation

Baseline proxy tends to wait for Green-like confirmation. That is acceptable for CDMO safety, but late for platform/diagnostic upside and dangerous for unresolved FDA binary setups. The best shadow profile is not a simple Green relaxation. It adds an early de-risked Stage2 route and a hard binary-risk cap.

## 17. Shadow Profile Optimization Loop

|profile_id|selected_representative_trigger_count|avg_MFE90|avg_MAE90|hit_rate_MFE90_gt20|bad_entry_rate_MAE90_lt_-15|false_positive_rate|missed_structural|late_green|
|---|---|---|---|---|---|---|---|---|
|baseline_current_proxy|4|23.4|-26.3|0.75|0.5|0.25|3|3|
|stage2_actionable_early_evidence_plus_with_binary_and_event_guardrail|4|151.7|-4.5|1.0|0.0|0.0|0|0|
|stage3_yellow_entry_relaxed|4|84.3|-23.8|0.75|0.5|0.25|0|1|
|green_confirmation_timing_relaxed|4|88.3|-22.6|0.75|0.5|0.25|0|0|
|four_b_peak_timing_tuned|4|3.3|-40.1|0.0|1.0|0.0|0|0|
|four_c_thesis_break_earlier|1|46.2|-29.9|1.0|1.0|0.0|0|0|
|binary_regulatory_and_event_premium_guardrail|3|169.6|-4.9|1.0|0.0|0.0|0|0|


Best profile: `stage2_actionable_early_evidence_plus_with_binary_and_event_guardrail`.

## 18. Before / After Backtest Comparison

|case_id|symbol|best_actual_trigger|baseline_selected_trigger|after_selected_trigger|baseline_entry|after_entry|baseline_price|after_price|baseline_MFE90|after_MFE90|baseline_MAE90|after_MAE90|baseline_MFE180|after_MFE180|baseline_MAE180|after_MAE180|return_improve90|risk_change90|reason|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R7L2_C1_SBIO_CDMO_BACKLOG_CAPACITY|207940|R7L2_C1_T2_STAGE2_ACTIONABLE|R7L2_C1_T4_STAGE3_GREEN|R7L2_C1_T2_STAGE2_ACTIONABLE|2024-07-26|2024-07-02|915000|810000|21.6|37.4|-8.1|-3.2|32.1|49.3|-8.1|-3.2|15.8|4.9|early evidence captures more upside; binary/event guardrail controls false Green|
|R7L2_C2_ALTEOGEN_PLATFORM_OPTIONALITY|196170|R7L2_C2_T2_STAGE2_ACTIONABLE|R7L2_C2_T4_STAGE3_GREEN|R7L2_C2_T2_STAGE2_ACTIONABLE|2024-06-07|2024-02-23|269000|131200|35.1|121.8|-10.6|-9.1|69.3|247.2|-10.6|-9.1|86.7|1.5|early evidence captures more upside; binary/event guardrail controls false Green|
|R7L2_C3_HLB_REGULATORY_BINARY|028300|R7L2_C3_T1_STAGE2_EVENT_PREMIUM|R7L2_C3_T3_STAGE3_YELLOW|R7L2_C3_T1_STAGE2_EVENT_PREMIUM|2024-03-21|2024-01-26|112700|65200|14.5|97.9|-58.3|-3.4|14.5|97.9|-58.3|-27.9|83.4|54.9|early evidence captures more upside; binary/event guardrail controls false Green|
|R7L2_C4_SEEG_DIAGNOSTIC_DEMAND_SHOCK|096530|R7L2_C4_T1_STAGE2_EUA_DEMAND|R7L2_C4_T4_STAGE3_GREEN|R7L2_C4_T1_STAGE2_EUA_DEMAND|2020-03-26|2020-02-13|114500|31450|22.5|349.6|-28.3|-2.5|181.4|924.5|-28.3|-2.5|327.1|25.8|early evidence captures more upside; binary/event guardrail controls false Green|


Natural-language verdict: the after-profile changes the gate from “wait for all Green confirmation” to “allow early Stage2-Actionable only when evidence is de-risked or demand is concrete; block unresolved binary events from becoming Green.” This increases upside capture while reducing deep MAE from false Green rows.

## 19. Score-Return Alignment Matrix

| alignment_label | trigger_count | avg_weighted_score_before | avg_weighted_score_after | avg_MFE90 | avg_MAE90 | verdict |
|---|---:|---:|---:|---:|---:|---|
| score_high_return_high | 7 | 39.5 | 42.1 | 144.7 | -7.9 | early de-risked evidence generally aligned |
| score_low_return_high_missed_structural | 2 | 25.4 | 32.8 | 205.3 | -2.8 | Stage2 evidence should not be ignored |
| score_high_return_low_false_positive | 1 | 11.3 | 8.6 | 14.5 | -58.3 | HLB-style binary risk must cap Green |
| score_mid_return_low_watch_only | 4 | 9.1 | 8.4 | 3.3 | -40.1 | 4B overlay, not entry aggregate |
| score_mid_return_high_promote_candidate | 2 | 34.2 | 35.8 | 69.3 | -14.9 | keep Yellow/sizing guardrail |

## 20. Weight Sensitivity Table

| axis | baseline | tested | delta | affected_trigger_ids | affected_case_count | avg_MFE90_before | avg_MFE90_after | avg_MAE90_before | avg_MAE90_after | false_positive_before | false_positive_after | missed_structural_before | missed_structural_after | verdict |
|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| de_risked_stage2_actionable_evidence | 0 | 2 | +2 | SBIO_T2, ALTEO_T2 | 2 | 28.3 | 79.7 | -8.8 | -6.6 | 0 | 0 | 2 | 0 | promote adjustment |
| diagnostic_demand_shock_stage2_evidence | 0 | 2 | +2 | SEEG_T1, SEEG_T4 | 1 | 22.5 | 349.6 | -28.3 | -2.5 | 0 | 0 | 1 | 0 | promote with demand-proof guardrail |
| binary_regulatory_risk_cap | 0 | 3 | +3 | HLB_T1, HLB_T3, HLB_T6 | 1 | 14.5 | 97.9 | -58.3 | -3.4 | 1 | 0 | 0 | 0 | positive risk adjustment |
| price_only_4b_reject_as_full_4b | 0 | 2 | +2 | ALTEO_T5, HLB_T5, SEEG_T5 | 3 | 4.1 | overlay_only | -47.9 | overlay_only | 0 | 0 | 0 | 0 | keep local/full 4B split |

## 21. Optimization Decision Log

```jsonl
{"row_type": "optimization_decision", "decision_id": "R7L2_D1", "hypothesis": "Promote Stage2-Actionable when de-risked CDMO/platform/diagnostic evidence plus relative strength appear before Green.", "tested_trigger_ids": ["R7L2_C1_T2_STAGE2_ACTIONABLE", "R7L2_C2_T2_STAGE2_ACTIONABLE", "R7L2_C4_T1_STAGE2_EUA_DEMAND"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_binary_and_event_guardrail", "backtest_result_summary": "After profile improves avg selected MFE90 from 23.4 to 151.9 and avg MAE90 from -26.4 to -4.6 on the four case set.", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "R7 still mixes structural CDMO/platform, diagnostic shock, and binary approval risk; cross-round validation needed.", "risks": "May over-credit one-off demand shocks if no sustained revenue/margin bridge is present.", "next_validation_needed": "Find medtech/diagnostic demand-shock counterexamples and approval success/failure pairs."}
{"row_type": "optimization_decision", "decision_id": "R7L2_D2", "hypothesis": "Unresolved FDA/binary regulatory expectation must cap Green even when MFE before decision is high.", "tested_trigger_ids": ["R7L2_C3_T1_STAGE2_EVENT_PREMIUM", "R7L2_C3_T3_STAGE3_YELLOW", "R7L2_C3_T6_4C_TBREAK"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_binary_and_event_guardrail", "backtest_result_summary": "HLB late Yellow proxy produced MAE90 -58.3; hard 4C was late but still separates thesis break from normal volatility.", "accepted_or_rejected": "accepted", "delta_magnitude": "+3", "why_not_larger_delta": "Single hard binary failure in this loop; do not generalize to all biotech.", "risks": "May under-credit genuine approvals before final decision.", "next_validation_needed": "Validate with approval-success rows and false-break 4C rows."}
```

## 22. Overfitting / Robustness Check

- `usable_trigger_count = 16` and `representative_entry_trigger_count = 11`.
- The +2 early-evidence delta is allowed because the direction repeats across CDMO, platform optionality, and diagnostic demand shock.
- The +3 binary-risk cap is allowed only as a risk penalty because HLB shows a deep false-positive pattern. It is not a general short/exit rule.
- The 4B delta is overlay-only: price-only peak proximity can create good local timing but cannot be treated as full thesis break.
- Counterexamples seen: HLB binary false positive; Alteogen high-volatility platform risk; price-only 4B rows without non-price evidence.

## 23. Cross-case Aggregate Metrics

|trigger_type|usable_trigger_count|representative_trigger_count|avg_MFE90|median_MFE90|avg_MAE90|median_MAE90|avg_MFE180|avg_MAE180|verdict|
|---|---|---|---|---|---|---|---|---|---|
|Stage2|3|3|152.8|97.9|-3.0|-3.2|349.7|-13.2|entry aggregate; overlay excluded|
|Stage2-Actionable|2|2|79.6|79.6|-6.2|-6.2|148.2|-6.2|entry aggregate; overlay excluded|
|Stage3-Green|3|3|26.4|22.5|-15.7|-10.6|94.3|-15.7|entry aggregate; overlay excluded|
|Stage3-Yellow|3|3|105.2|51.4|-29.0|-18.8|283.0|-29.0|entry aggregate; overlay excluded|


Overlay aggregate:

| overlay_type | usable_trigger_count | avg_MFE90 | avg_MAE90 | avg_local_peak_proximity | avg_full_peak_proximity | verdict |
|---|---:|---:|---:|---:|---:|---|
| 4B-watch | 4 | 3.3 | -40.1 | 0.96 | 0.96 | near-peak timing works, but full 4B requires non-price evidence |
| 4C-thesis-break | 1 | 46.2 | -29.9 | unavailable | unavailable | validated only for explicit CRL/regulatory failure |

## 24. Score-Price Alignment Verdict

R7 loop2 supports a two-key model. The first key opens early entry only when evidence is concrete: backlog/capacity, named platform optionality, or authorized diagnostic demand. The second key blocks false Green: unresolved regulatory binary risk cannot be promoted just because price and news are strong. In practice, the agent should behave like a triage desk: fast-track the cases whose revenue bridge is already forming, quarantine binary approval trades until the decisive evidence arrives, and put price-only blowoffs into overlay rather than thesis-break buckets.

## 25. Validation Scope / Non-Validation Scope

```text
this_round_validates:
- Stage2-Actionable early evidence for de-risked CDMO/platform triggers.
- Diagnostic demand-shock Stage2 promotion when public demand/authorization evidence is concrete.
- Binary regulatory risk cap for unresolved FDA/approval setups.
- Price-only 4B rejection as full 4B without non-price evidence.
- Local vs full-window 4B split.
```

```text
this_round_does_not_validate:
- Broad Stage3-Green threshold relaxation across all biotech.
- Hard 4C timing for non-regulatory clinical failures outside HLB-style CRL.
- Post-approval commercial execution failures.
- Adjusted-price treatment for corporate-action-contaminated 2Y windows.
```

## 26. Shadow Weight Calibration

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,de_risked_stage2_actionable_evidence,0,2,+2,"Samsung Bio/Alteogen de-risked early evidence outperformed later Green entries","baseline avg MFE90 23.4 / MAE90 -26.4 improves to after-profile avg MFE90 151.9 / MAE90 -4.6","R7L2_C1_T2_STAGE2_ACTIONABLE|R7L2_C2_T2_STAGE2_ACTIONABLE",2,"shadow-only; not production"
shadow_weight,diagnostic_demand_shock_stage2_evidence,0,2,+2,"Seegene shows public diagnostic demand evidence can precede reported EPS and still be the best entry","Stage2 MFE90 349.6 and MAE90 -2.5 vs Green MFE90 22.5 and MAE90 -28.3","R7L2_C4_T1_STAGE2_EUA_DEMAND|R7L2_C4_T4_STAGE3_GREEN",2,"requires real demand authorization/export signal; not generic pandemic rumor"
shadow_weight,binary_regulatory_risk_cap,0,3,+3,"HLB shows high RS plus approval expectation can become false positive without final regulatory de-risking","HLB Yellow-like entry had MFE90 14.5 and MAE90 -58.3; after profile blocks full Green","R7L2_C3_T1_STAGE2_EVENT_PREMIUM|R7L2_C3_T3_STAGE3_YELLOW|R7L2_C3_T6_4C_TBREAK",3,"shadow-only; FDA/approval binary only"
shadow_weight,price_only_4b_reject_as_full_4b,0,2,+2,"Alteogen/HLB price-only peaks were useful watch overlays but require non-price evidence for full 4B","4B overlay rows show avg MFE90 3.3 and avg MAE90 -40.1; non-price evidence separates full 4B from watch-only","R7L2_C2_T5_4B_WATCH|R7L2_C3_T5_4B_WATCH|R7L2_C4_T5_4B_BLOWOFF",3,"shadow-only overlay logic"
```

## 27. Machine-Readable Rows

### 27.1 Price source validation row JSONL

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 27.2 Case rows JSONL

```jsonl
{"row_type": "case", "case_id": "R7L2_C1_SBIO_CDMO_BACKLOG_CAPACITY", "symbol": "207940", "company_name": "삼성바이오로직스", "round": "R7", "loop": "2", "sector": "바이오·헬스케어·의료기기", "case_type": "structural_success", "primary_archetype": "CDMO_BACKLOG_CAPACITY_VISIBILITY", "best_trigger": "R7L2_C1_T2_STAGE2_ACTIONABLE", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "validated_by_stock_web_ohlc", "price_source": "Songdaiki/stock-web", "notes": "CDMO backlog/capacity/customer-quality evidence가 Green 확인 전부터 주가 re-rating으로 연결된 케이스."}
{"row_type": "case", "case_id": "R7L2_C2_ALTEOGEN_PLATFORM_OPTIONALITY", "symbol": "196170", "company_name": "알테오젠", "round": "R7", "loop": "2", "sector": "바이오·헬스케어·의료기기", "case_type": "stage2_promote_candidate_and_4b_watch", "primary_archetype": "PLATFORM_TECH_LICENSING_OPTIONALITY", "best_trigger": "R7L2_C2_T2_STAGE2_ACTIONABLE", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "validated_by_stock_web_ohlc", "price_source": "Songdaiki/stock-web", "notes": "ALT-B4/SC 제형 플랫폼 optionality가 Stage2-Actionable 구간에서 이미 re-rating을 만든 케이스. 단, 고변동성 sizing guardrail 필요."}
{"row_type": "case", "case_id": "R7L2_C3_HLB_REGULATORY_BINARY", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "2", "sector": "바이오·헬스케어·의료기기", "case_type": "failed_rerating_4c_thesis_break", "primary_archetype": "REGULATORY_BINARY_APPROVAL_RISK", "best_trigger": "R7L2_C3_T1_STAGE2_EVENT_PREMIUM", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "validated_by_stock_web_ohlc", "price_source": "Songdaiki/stock-web", "notes": "승인 기대감으로 MFE가 컸지만 최종 CRL 전에는 구조적 Green으로 승격하면 안 되는 binary-risk 케이스."}
{"row_type": "case", "case_id": "R7L2_C4_SEEG_DIAGNOSTIC_DEMAND_SHOCK", "symbol": "096530", "company_name": "씨젠", "round": "R7", "loop": "2", "sector": "바이오·헬스케어·의료기기", "case_type": "diagnostic_structural_success_then_4b", "primary_archetype": "DIAGNOSTIC_DEMAND_SHOCK_EPS_RERATING", "best_trigger": "R7L2_C4_T1_STAGE2_EUA_DEMAND", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "validated_by_stock_web_ohlc", "price_source": "Songdaiki/stock-web", "notes": "COVID 진단키트 긴급사용/수출 수요가 EPS re-rating으로 직결된 진단/헬스케어 demand-shock 케이스."}
```

### 27.3 Trigger rows JSONL

```jsonl
{"row_type": "trigger", "trigger_id": "R7L2_C1_T1_STAGE2", "case_id": "R7L2_C1_SBIO_CDMO_BACKLOG_CAPACITY", "symbol": "207940", "company_name": "삼성바이오로직스", "round": "R7", "loop": "2", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "CDMO_BACKLOG_CAPACITY_VISIBILITY", "trigger_type": "Stage2", "trigger_date": "2024-01-22", "evidence_available_at_that_date": "2024년 초 CDMO 수주/가동률/실적 가시성의 초기 evidence. 아직 capacity/backlog bridge가 완전히 닫히기 전이라 Stage2.", "evidence_source": "public contract/news/earnings context; stock-web OHLC", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/207/207940/2024.csv", "profile_path": "atlas/symbol_profiles/207/207940.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-22", "entry_price": 793000, "MFE_30D_pct": 10.7, "MFE_90D_pct": 11.0, "MFE_180D_pct": 26.7, "MFE_1Y_pct": 52.5, "MFE_2Y_pct": "contaminated_or_unavailable", "MAE_30D_pct": -3.2, "MAE_90D_pct": -3.2, "MAE_180D_pct": -9.1, "MAE_1Y_pct": -9.1, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-14", "peak_price": 1209000, "drawdown_after_peak_pct": -17.7, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "SBIO_2024_0122_793000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R7L2_C1_T2_STAGE2_ACTIONABLE", "case_id": "R7L2_C1_SBIO_CDMO_BACKLOG_CAPACITY", "symbol": "207940", "company_name": "삼성바이오로직스", "round": "R7", "loop": "2", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "CDMO_BACKLOG_CAPACITY_VISIBILITY", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-02", "evidence_available_at_that_date": "수주/backlog + capacity visibility + 상대강도 조합. Green 전이지만 과거 OHLC상 가장 좋은 entry.", "evidence_source": "public contract/news/earnings context; stock-web OHLC", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/207/207940/2024.csv", "profile_path": "atlas/symbol_profiles/207/207940.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-02", "entry_price": 810000, "MFE_30D_pct": 21.7, "MFE_90D_pct": 37.4, "MFE_180D_pct": 49.3, "MFE_1Y_pct": 49.3, "MFE_2Y_pct": "contaminated_or_unavailable", "MAE_30D_pct": -3.2, "MAE_90D_pct": -3.2, "MAE_180D_pct": -3.2, "MAE_1Y_pct": -3.2, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-14", "peak_price": 1209000, "drawdown_after_peak_pct": -17.7, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "excellent_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "SBIO_2024_0702_810000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R7L2_C1_T4_STAGE3_GREEN", "case_id": "R7L2_C1_SBIO_CDMO_BACKLOG_CAPACITY", "symbol": "207940", "company_name": "삼성바이오로직스", "round": "R7", "loop": "2", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "CDMO_BACKLOG_CAPACITY_VISIBILITY", "trigger_type": "Stage3-Green", "trigger_date": "2024-07-26", "evidence_available_at_that_date": "공개 evidence 2~3개와 가격 상대강도가 닫히는 Green proxy. 안전하지만 Stage2-Actionable보다 늦다.", "evidence_source": "public contract/news/earnings context; stock-web OHLC", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/207/207940/2024.csv", "profile_path": "atlas/symbol_profiles/207/207940.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-26", "entry_price": 915000, "MFE_30D_pct": 9.8, "MFE_90D_pct": 21.6, "MFE_180D_pct": 32.1, "MFE_1Y_pct": 32.1, "MFE_2Y_pct": "contaminated_or_unavailable", "MAE_30D_pct": -8.1, "MAE_90D_pct": -8.1, "MAE_180D_pct": -8.1, "MAE_1Y_pct": -8.1, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-14", "peak_price": 1209000, "drawdown_after_peak_pct": -17.7, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.37, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_but_valid_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "SBIO_2024_0726_915000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R7L2_C1_T5_4B_WATCH", "case_id": "R7L2_C1_SBIO_CDMO_BACKLOG_CAPACITY", "symbol": "207940", "company_name": "삼성바이오로직스", "round": "R7", "loop": "2", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "CDMO_BACKLOG_CAPACITY_VISIBILITY", "trigger_type": "4B-watch", "trigger_date": "2025-02-14", "evidence_available_at_that_date": "peak 근처 valuation/positioning watch. thesis break가 아니라 Stage3 + 4B-watch overlay.", "evidence_source": "stock-web OHLC + valuation/positioning context", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/207/207940/2025.csv", "profile_path": "atlas/symbol_profiles/207/207940.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-02-14", "entry_price": 1180000, "MFE_30D_pct": 0.8, "MFE_90D_pct": 0.8, "MFE_180D_pct": 0.8, "MFE_1Y_pct": "unavailable", "MFE_2Y_pct": "unavailable", "MAE_30D_pct": -16.9, "MAE_90D_pct": -16.9, "MAE_180D_pct": -17.7, "MAE_1Y_pct": "unavailable", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-14", "peak_price": 1209000, "drawdown_after_peak_pct": -17.7, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": "valuation_blowoff|positioning_overheat", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4b_watch_near_peak", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "SBIO_2025_0214_1180000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "trigger_id": "R7L2_C2_T2_STAGE2_ACTIONABLE", "case_id": "R7L2_C2_ALTEOGEN_PLATFORM_OPTIONALITY", "symbol": "196170", "company_name": "알테오젠", "round": "R7", "loop": "2", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "PLATFORM_TECH_LICENSING_OPTIONALITY", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "evidence_available_at_that_date": "ALT-B4/SC platform optionality + customer quality + 상대강도. 아직 full Green은 아니나 entry 기대값이 가장 컸다.", "evidence_source": "public licensing/platform news; stock-web OHLC", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv", "profile_path": "atlas/symbol_profiles/196/196170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-23", "entry_price": 131200, "MFE_30D_pct": 71.9, "MFE_90D_pct": 121.8, "MFE_180D_pct": 247.2, "MFE_1Y_pct": 247.2, "MFE_2Y_pct": "unavailable", "MAE_30D_pct": -9.1, "MAE_90D_pct": -9.1, "MAE_180D_pct": -9.1, "MAE_1Y_pct": -9.1, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-11", "peak_price": 455500, "drawdown_after_peak_pct": -38.7, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "excellent_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "ALTEO_2024_0223_131200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R7L2_C2_T3_STAGE3_YELLOW", "case_id": "R7L2_C2_ALTEOGEN_PLATFORM_OPTIONALITY", "symbol": "196170", "company_name": "알테오젠", "round": "R7", "loop": "2", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "PLATFORM_TECH_LICENSING_OPTIONALITY", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-03-05", "evidence_available_at_that_date": "플랫폼 optionality가 더 넓게 알려졌지만 margin/revenue bridge는 미완. Yellow로 sizing 제한 필요.", "evidence_source": "public licensing/platform news; stock-web OHLC", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv", "profile_path": "atlas/symbol_profiles/196/196170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-05", "entry_price": 192200, "MFE_30D_pct": 17.3, "MFE_90D_pct": 51.4, "MFE_180D_pct": 137.0, "MFE_1Y_pct": 137.0, "MFE_2Y_pct": "unavailable", "MAE_30D_pct": -18.8, "MAE_90D_pct": -18.8, "MAE_180D_pct": -18.8, "MAE_1Y_pct": -18.8, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-11", "peak_price": 455500, "drawdown_after_peak_pct": -38.7, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_entry_high_volatility", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "ALTEO_2024_0305_192200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R7L2_C2_T4_STAGE3_GREEN", "case_id": "R7L2_C2_ALTEOGEN_PLATFORM_OPTIONALITY", "symbol": "196170", "company_name": "알테오젠", "round": "R7", "loop": "2", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "PLATFORM_TECH_LICENSING_OPTIONALITY", "trigger_type": "Stage3-Green", "trigger_date": "2024-06-07", "evidence_available_at_that_date": "공개 evidence와 상대강도는 더 명확하지만 Stage2-Actionable 대비 upside 상당 부분을 사용한 뒤다.", "evidence_source": "public licensing/platform news; stock-web OHLC", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv", "profile_path": "atlas/symbol_profiles/196/196170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-07", "entry_price": 269000, "MFE_30D_pct": 13.9, "MFE_90D_pct": 35.1, "MFE_180D_pct": 69.3, "MFE_1Y_pct": 69.3, "MFE_2Y_pct": "unavailable", "MAE_30D_pct": -10.6, "MAE_90D_pct": -10.6, "MAE_180D_pct": -10.6, "MAE_1Y_pct": -10.6, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-11", "peak_price": 455500, "drawdown_after_peak_pct": -38.7, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.52, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "ALTEO_2024_0607_269000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R7L2_C2_T5_4B_WATCH", "case_id": "R7L2_C2_ALTEOGEN_PLATFORM_OPTIONALITY", "symbol": "196170", "company_name": "알테오젠", "round": "R7", "loop": "2", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "PLATFORM_TECH_LICENSING_OPTIONALITY", "trigger_type": "4B-watch", "trigger_date": "2024-11-11", "evidence_available_at_that_date": "가격상 peak proximity는 좋지만 non-price 4B evidence가 부족하여 full 4B가 아니라 watch overlay.", "evidence_source": "stock-web OHLC + positioning context", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv", "profile_path": "atlas/symbol_profiles/196/196170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-11-11", "entry_price": 445500, "MFE_30D_pct": 2.2, "MFE_90D_pct": 2.2, "MFE_180D_pct": 2.2, "MFE_1Y_pct": "unavailable", "MFE_2Y_pct": "unavailable", "MAE_30D_pct": -38.7, "MAE_90D_pct": -38.7, "MAE_180D_pct": -38.7, "MAE_1Y_pct": "unavailable", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-11", "peak_price": 455500, "drawdown_after_peak_pct": -38.7, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "price_only_near_peak_watch_not_full_4B", "four_b_evidence_type": "price_only|positioning_overheat", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4b_watch_near_peak", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "ALTEO_2024_1111_445500", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "trigger_id": "R7L2_C3_T1_STAGE2_EVENT_PREMIUM", "case_id": "R7L2_C3_HLB_REGULATORY_BINARY", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "2", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "REGULATORY_BINARY_APPROVAL_RISK", "trigger_type": "Stage2", "trigger_date": "2024-01-26", "evidence_available_at_that_date": "FDA 승인 기대감과 상대강도. MFE는 컸지만 최종 승인 전이라 structural Green이 아니라 event-premium/binary-risk stage.", "evidence_source": "public FDA expectation/news; stock-web OHLC", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-26", "entry_price": 65200, "MFE_30D_pct": 27.3, "MFE_90D_pct": 97.9, "MFE_180D_pct": 97.9, "MFE_1Y_pct": 97.9, "MFE_2Y_pct": "unavailable", "MAE_30D_pct": -3.4, "MAE_90D_pct": -3.4, "MAE_180D_pct": -27.9, "MAE_1Y_pct": -29.9, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-26", "peak_price": 129000, "drawdown_after_peak_pct": -61.1, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "event_premium_binary_success_before_4c", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "HLB_2024_0126_65200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R7L2_C3_T3_STAGE3_YELLOW", "case_id": "R7L2_C3_HLB_REGULATORY_BINARY", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "2", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "REGULATORY_BINARY_APPROVAL_RISK", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-03-21", "evidence_available_at_that_date": "승인 기대와 가격 강세가 강하지만 최종 regulatory de-risking이 닫히지 않은 상태. Green으로 올리면 false positive.", "evidence_source": "public FDA expectation/news; stock-web OHLC", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-21", "entry_price": 112700, "MFE_30D_pct": 14.5, "MFE_90D_pct": 14.5, "MFE_180D_pct": 14.5, "MFE_1Y_pct": 14.5, "MFE_2Y_pct": "unavailable", "MAE_30D_pct": -58.3, "MAE_90D_pct": -58.3, "MAE_180D_pct": -58.3, "MAE_1Y_pct": -58.3, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-26", "peak_price": 129000, "drawdown_after_peak_pct": -61.1, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "false_positive_score", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "HLB_2024_0321_112700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R7L2_C3_T5_4B_WATCH", "case_id": "R7L2_C3_HLB_REGULATORY_BINARY", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "2", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "REGULATORY_BINARY_APPROVAL_RISK", "trigger_type": "4B-watch", "trigger_date": "2024-03-26", "evidence_available_at_that_date": "peak 근처 가격 과열과 binary risk. 가격상 4B-watch는 맞지만 non-price full 4B보다는 binary-risk cap이 핵심.", "evidence_source": "public FDA expectation/news; stock-web OHLC", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-26", "entry_price": 120800, "MFE_30D_pct": 6.8, "MFE_90D_pct": 6.8, "MFE_180D_pct": 6.8, "MFE_1Y_pct": "unavailable", "MFE_2Y_pct": "unavailable", "MAE_30D_pct": -61.1, "MAE_90D_pct": -61.1, "MAE_180D_pct": -61.1, "MAE_1Y_pct": "unavailable", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-26", "peak_price": 129000, "drawdown_after_peak_pct": -61.1, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "good_peak_proximity_but_price_only_not_full_4B", "four_b_evidence_type": "price_only|regulatory_binary_risk", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4b_watch_near_peak", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "HLB_2024_0326_120800", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "trigger_id": "R7L2_C3_T6_4C_TBREAK", "case_id": "R7L2_C3_HLB_REGULATORY_BINARY", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "2", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "REGULATORY_BINARY_APPROVAL_RISK", "trigger_type": "4C-thesis-break", "trigger_date": "2024-05-17", "evidence_available_at_that_date": "FDA CRL/approval failure로 thesis가 깨진 hard 4C. 늦었지만 추가 drawdown 보호 기능은 있음.", "evidence_source": "public CRL/failure news; stock-web OHLC", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-17", "entry_price": 67100, "MFE_30D_pct": 10.0, "MFE_90D_pct": 46.2, "MFE_180D_pct": 46.2, "MFE_1Y_pct": "unavailable", "MFE_2Y_pct": "unavailable", "MAE_30D_pct": -29.9, "MAE_90D_pct": -29.9, "MAE_180D_pct": -29.9, "MAE_1Y_pct": "unavailable", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-08", "peak_price": 98100, "drawdown_after_peak_pct": -29.9, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "hard_4c_late_but_still_protective", "trigger_outcome_label": "hard_4c_late_but_still_protective", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "HLB_2024_0517_67100", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only"}
{"row_type": "trigger", "trigger_id": "R7L2_C4_T1_STAGE2_EUA_DEMAND", "case_id": "R7L2_C4_SEEG_DIAGNOSTIC_DEMAND_SHOCK", "symbol": "096530", "company_name": "씨젠", "round": "R7", "loop": "2", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "DIAGNOSTIC_DEMAND_SHOCK_EPS_RERATING", "trigger_type": "Stage2", "trigger_date": "2020-02-12", "evidence_available_at_that_date": "COVID-19 진단키트 긴급사용/수요 shock. 초기 Stage2지만 EPS rerating으로 직결되는 수요 evidence.", "evidence_source": "MFDS/diagnostic-kit public authorization and pandemic news; stock-web OHLC", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv", "profile_path": "atlas/symbol_profiles/096/096530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-02-13", "entry_price": 31450, "MFE_30D_pct": 349.6, "MFE_90D_pct": 349.6, "MFE_180D_pct": 924.5, "MFE_1Y_pct": 924.5, "MFE_2Y_pct": "contaminated_or_unavailable", "MAE_30D_pct": -2.5, "MAE_90D_pct": -2.5, "MAE_180D_pct": -2.5, "MAE_1Y_pct": -2.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-08-10", "peak_price": 322200, "drawdown_after_peak_pct": -45.6, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "excellent_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "SEEG_2020_0213_31450", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R7L2_C4_T3_STAGE3_YELLOW", "case_id": "R7L2_C4_SEEG_DIAGNOSTIC_DEMAND_SHOCK", "symbol": "096530", "company_name": "씨젠", "round": "R7", "loop": "2", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "DIAGNOSTIC_DEMAND_SHOCK_EPS_RERATING", "trigger_type": "Stage3-Yellow", "trigger_date": "2020-03-02", "evidence_available_at_that_date": "COVID 확산과 진단 수요의 가시화. 아직 실적 숫자는 뒤따르지만 수요 bridge가 강해 Yellow 진입 가능.", "evidence_source": "pandemic public news and diagnostic demand; stock-web OHLC", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv", "profile_path": "atlas/symbol_profiles/096/096530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-03-02", "entry_price": 40400, "MFE_30D_pct": 249.8, "MFE_90D_pct": 249.8, "MFE_180D_pct": 697.5, "MFE_1Y_pct": 697.5, "MFE_2Y_pct": "contaminated_or_unavailable", "MAE_30D_pct": -9.9, "MAE_90D_pct": -9.9, "MAE_180D_pct": -9.9, "MAE_1Y_pct": -9.9, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-08-10", "peak_price": 322200, "drawdown_after_peak_pct": -45.6, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "excellent_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "SEEG_2020_0302_40400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R7L2_C4_T4_STAGE3_GREEN", "case_id": "R7L2_C4_SEEG_DIAGNOSTIC_DEMAND_SHOCK", "symbol": "096530", "company_name": "씨젠", "round": "R7", "loop": "2", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "DIAGNOSTIC_DEMAND_SHOCK_EPS_RERATING", "trigger_type": "Stage3-Green", "trigger_date": "2020-03-26", "evidence_available_at_that_date": "진단 수요/가격 상대강도가 이미 시장에 넓게 확인된 Green. 여전히 180D MFE는 크지만 90D 기대값은 Stage2보다 훨씬 낮다.", "evidence_source": "pandemic public news and stock-web OHLC", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv", "profile_path": "atlas/symbol_profiles/096/096530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-03-26", "entry_price": 114500, "MFE_30D_pct": 22.5, "MFE_90D_pct": 22.5, "MFE_180D_pct": 181.4, "MFE_1Y_pct": 181.4, "MFE_2Y_pct": "contaminated_or_unavailable", "MAE_30D_pct": -28.3, "MAE_90D_pct": -28.3, "MAE_180D_pct": -28.3, "MAE_1Y_pct": -28.3, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-08-10", "peak_price": 322200, "drawdown_after_peak_pct": -45.6, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.286, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_but_still_good_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "SEEG_2020_0326_114500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R7L2_C4_T5_4B_BLOWOFF", "case_id": "R7L2_C4_SEEG_DIAGNOSTIC_DEMAND_SHOCK", "symbol": "096530", "company_name": "씨젠", "round": "R7", "loop": "2", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "DIAGNOSTIC_DEMAND_SHOCK_EPS_RERATING", "trigger_type": "4B-watch", "trigger_date": "2020-08-10", "evidence_available_at_that_date": "diagnostic demand peak/valuation blowoff/positioning 과열. full-window peak 근처 4B-watch가 잘 작동.", "evidence_source": "pandemic demand normalization context; stock-web OHLC", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096530/2020.csv", "profile_path": "atlas/symbol_profiles/096/096530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-08-10", "entry_price": 310700, "MFE_30D_pct": 3.4, "MFE_90D_pct": 3.4, "MFE_180D_pct": 3.4, "MFE_1Y_pct": "contaminated_or_unavailable", "MFE_2Y_pct": "contaminated_or_unavailable", "MAE_30D_pct": -31.3, "MAE_90D_pct": -43.6, "MAE_180D_pct": -43.6, "MAE_1Y_pct": "contaminated_or_unavailable", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-08-10", "peak_price": 322200, "drawdown_after_peak_pct": -45.6, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": "valuation_blowoff|positioning_overheat|revision_slowdown", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_watch_success", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_or_no_overlap", "same_entry_group_id": "SEEG_2020_0810_310700", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only"}
```

### 27.4 Score simulation rows JSONL

```jsonl
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L2_C1_SBIO_CDMO_BACKLOG_CAPACITY", "trigger_id": "R7L2_C1_T1_STAGE2", "symbol": "207940", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 6, "revision_score": 4, "relative_strength_score": 4, "customer_quality_score": 8, "policy_or_regulatory_score": 2, "valuation_repricing_score": 5, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 8, "fcf_conversion_score": 6, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 59.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 6, "revision_score": 4, "relative_strength_score": 5, "customer_quality_score": 9, "policy_or_regulatory_score": 2, "valuation_repricing_score": 5, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 8, "fcf_conversion_score": 6, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 61.0, "stage_label_after": "Stage3-Green", "changed_components": ["relative_strength_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "positioning_overheat_score"], "component_delta_explanation": "R7 loop2 shadow profile credits de-risked CDMO/platform/diagnostic Stage2 evidence, caps unresolved FDA binary risk, and rejects price-only 4B as full 4B.", "selected_by_profile": false, "MFE_90D_pct": 11.0, "MAE_90D_pct": -3.2, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L2_C1_SBIO_CDMO_BACKLOG_CAPACITY", "trigger_id": "R7L2_C1_T2_STAGE2_ACTIONABLE", "symbol": "207940", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 6, "revision_score": 6, "relative_strength_score": 7, "customer_quality_score": 8, "policy_or_regulatory_score": 2, "valuation_repricing_score": 5, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 8, "fcf_conversion_score": 6, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 64.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 6, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 9, "policy_or_regulatory_score": 2, "valuation_repricing_score": 5, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 8, "fcf_conversion_score": 6, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 66.0, "stage_label_after": "Stage3-Green", "changed_components": ["relative_strength_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "positioning_overheat_score"], "component_delta_explanation": "R7 loop2 shadow profile credits de-risked CDMO/platform/diagnostic Stage2 evidence, caps unresolved FDA binary risk, and rejects price-only 4B as full 4B.", "selected_by_profile": true, "MFE_90D_pct": 37.4, "MAE_90D_pct": -3.2, "score_return_alignment_label": "score_high_return_high"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L2_C1_SBIO_CDMO_BACKLOG_CAPACITY", "trigger_id": "R7L2_C1_T4_STAGE3_GREEN", "symbol": "207940", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 6, "revision_score": 7, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 2, "valuation_repricing_score": 5, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 8, "fcf_conversion_score": 6, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 66.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 6, "revision_score": 7, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 2, "valuation_repricing_score": 5, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 8, "fcf_conversion_score": 6, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 66.0, "stage_label_after": "Stage3-Green", "changed_components": ["relative_strength_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "positioning_overheat_score"], "component_delta_explanation": "R7 loop2 shadow profile credits de-risked CDMO/platform/diagnostic Stage2 evidence, caps unresolved FDA binary risk, and rejects price-only 4B as full 4B.", "selected_by_profile": false, "MFE_90D_pct": 21.6, "MAE_90D_pct": -8.1, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L2_C1_SBIO_CDMO_BACKLOG_CAPACITY", "trigger_id": "R7L2_C1_T5_4B_WATCH", "symbol": "207940", "trigger_type": "4B-watch", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 6, "revision_score": 6, "relative_strength_score": 7, "customer_quality_score": 8, "policy_or_regulatory_score": 2, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 8, "fcf_conversion_score": 6, "positioning_overheat_score": 8, "thesis_break_score": 0}, "weighted_score_before": 63.4, "stage_label_before": "Stage3+4B-watch", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 6, "revision_score": 6, "relative_strength_score": 7, "customer_quality_score": 8, "policy_or_regulatory_score": 2, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 8, "fcf_conversion_score": 6, "positioning_overheat_score": 8, "thesis_break_score": 0}, "weighted_score_after": 63.4, "stage_label_after": "Stage3+4B-watch", "changed_components": ["relative_strength_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "positioning_overheat_score"], "component_delta_explanation": "R7 loop2 shadow profile credits de-risked CDMO/platform/diagnostic Stage2 evidence, caps unresolved FDA binary risk, and rejects price-only 4B as full 4B.", "selected_by_profile": false, "MFE_90D_pct": 0.8, "MAE_90D_pct": -16.9, "score_return_alignment_label": "score_high_return_low_false_positive"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L2_C2_ALTEOGEN_PLATFORM_OPTIONALITY", "trigger_id": "R7L2_C2_T2_STAGE2_ACTIONABLE", "symbol": "196170", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 6, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 4, "relative_strength_score": 9, "customer_quality_score": 8, "policy_or_regulatory_score": 3, "valuation_repricing_score": 7, "execution_risk_score": 5, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 36.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 9, "policy_or_regulatory_score": 3, "valuation_repricing_score": 7, "execution_risk_score": 5, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 38.0, "stage_label_after": "Stage3-Yellow", "changed_components": ["relative_strength_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "positioning_overheat_score"], "component_delta_explanation": "R7 loop2 shadow profile credits de-risked CDMO/platform/diagnostic Stage2 evidence, caps unresolved FDA binary risk, and rejects price-only 4B as full 4B.", "selected_by_profile": true, "MFE_90D_pct": 121.8, "MAE_90D_pct": -9.1, "score_return_alignment_label": "score_high_return_high"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L2_C2_ALTEOGEN_PLATFORM_OPTIONALITY", "trigger_id": "R7L2_C2_T3_STAGE3_YELLOW", "symbol": "196170", "trigger_type": "Stage3-Yellow", "raw_component_scores_before": {"contract_score": 6, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 5, "relative_strength_score": 9, "customer_quality_score": 8, "policy_or_regulatory_score": 3, "valuation_repricing_score": 7, "execution_risk_score": 5, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 37.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 5, "relative_strength_score": 10, "customer_quality_score": 9, "policy_or_regulatory_score": 3, "valuation_repricing_score": 7, "execution_risk_score": 5, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 39.0, "stage_label_after": "Stage3-Yellow", "changed_components": ["relative_strength_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "positioning_overheat_score"], "component_delta_explanation": "R7 loop2 shadow profile credits de-risked CDMO/platform/diagnostic Stage2 evidence, caps unresolved FDA binary risk, and rejects price-only 4B as full 4B.", "selected_by_profile": false, "MFE_90D_pct": 51.4, "MAE_90D_pct": -18.8, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L2_C2_ALTEOGEN_PLATFORM_OPTIONALITY", "trigger_id": "R7L2_C2_T4_STAGE3_GREEN", "symbol": "196170", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 6, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 5, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 3, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 37.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 5, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 3, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 37.0, "stage_label_after": "Stage3-Yellow", "changed_components": ["relative_strength_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "positioning_overheat_score"], "component_delta_explanation": "R7 loop2 shadow profile credits de-risked CDMO/platform/diagnostic Stage2 evidence, caps unresolved FDA binary risk, and rejects price-only 4B as full 4B.", "selected_by_profile": false, "MFE_90D_pct": 35.1, "MAE_90D_pct": -10.6, "score_return_alignment_label": "score_high_return_high"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L2_C2_ALTEOGEN_PLATFORM_OPTIONALITY", "trigger_id": "R7L2_C2_T5_4B_WATCH", "symbol": "196170", "trigger_type": "4B-watch", "raw_component_scores_before": {"contract_score": 6, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 5, "relative_strength_score": 9, "customer_quality_score": 8, "policy_or_regulatory_score": 3, "valuation_repricing_score": 7, "execution_risk_score": 7, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 8, "thesis_break_score": 0}, "weighted_score_before": 31.9, "stage_label_before": "Stage3+4B-watch", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 5, "relative_strength_score": 9, "customer_quality_score": 8, "policy_or_regulatory_score": 3, "valuation_repricing_score": 7, "execution_risk_score": 7, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 7, "thesis_break_score": 0}, "weighted_score_after": 32.4, "stage_label_after": "Stage3+4B-watch", "changed_components": ["relative_strength_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "positioning_overheat_score"], "component_delta_explanation": "R7 loop2 shadow profile credits de-risked CDMO/platform/diagnostic Stage2 evidence, caps unresolved FDA binary risk, and rejects price-only 4B as full 4B.", "selected_by_profile": false, "MFE_90D_pct": 2.2, "MAE_90D_pct": -38.7, "score_return_alignment_label": "score_high_return_low_false_positive"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L2_C3_HLB_REGULATORY_BINARY", "trigger_id": "R7L2_C3_T1_STAGE2_EVENT_PREMIUM", "symbol": "028300", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 9, "customer_quality_score": 4, "policy_or_regulatory_score": 7, "valuation_repricing_score": 8, "execution_risk_score": 9, "legal_or_contract_risk_score": 9, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 17.5, "stage_label_before": "Stage2-BinaryRiskCap", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 9, "customer_quality_score": 4, "policy_or_regulatory_score": 7, "valuation_repricing_score": 8, "execution_risk_score": 10, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 16.0, "stage_label_after": "Stage2-BinaryRiskCap", "changed_components": ["relative_strength_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "positioning_overheat_score"], "component_delta_explanation": "R7 loop2 shadow profile credits de-risked CDMO/platform/diagnostic Stage2 evidence, caps unresolved FDA binary risk, and rejects price-only 4B as full 4B.", "selected_by_profile": true, "MFE_90D_pct": 97.9, "MAE_90D_pct": -3.4, "score_return_alignment_label": "score_low_return_high_missed_structural"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L2_C3_HLB_REGULATORY_BINARY", "trigger_id": "R7L2_C3_T3_STAGE3_YELLOW", "symbol": "028300", "trigger_type": "Stage3-Yellow", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 9, "customer_quality_score": 4, "policy_or_regulatory_score": 7, "valuation_repricing_score": 8, "execution_risk_score": 9, "legal_or_contract_risk_score": 9, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 17.5, "stage_label_before": "Stage2-BinaryRiskCap", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 9, "customer_quality_score": 4, "policy_or_regulatory_score": 7, "valuation_repricing_score": 8, "execution_risk_score": 10, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 16.0, "stage_label_after": "Stage2-BinaryRiskCap", "changed_components": ["relative_strength_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "positioning_overheat_score"], "component_delta_explanation": "R7 loop2 shadow profile credits de-risked CDMO/platform/diagnostic Stage2 evidence, caps unresolved FDA binary risk, and rejects price-only 4B as full 4B.", "selected_by_profile": false, "MFE_90D_pct": 14.5, "MAE_90D_pct": -58.3, "score_return_alignment_label": "score_high_return_low_false_positive"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L2_C3_HLB_REGULATORY_BINARY", "trigger_id": "R7L2_C3_T5_4B_WATCH", "symbol": "028300", "trigger_type": "4B-watch", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 9, "customer_quality_score": 4, "policy_or_regulatory_score": 7, "valuation_repricing_score": 8, "execution_risk_score": 9, "legal_or_contract_risk_score": 9, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 8, "thesis_break_score": 0}, "weighted_score_before": 13.9, "stage_label_before": "Stage3+4B-watch", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 9, "customer_quality_score": 4, "policy_or_regulatory_score": 7, "valuation_repricing_score": 8, "execution_risk_score": 10, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 7, "thesis_break_score": 0}, "weighted_score_after": 12.9, "stage_label_after": "Stage3+4B-watch", "changed_components": ["relative_strength_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "positioning_overheat_score"], "component_delta_explanation": "R7 loop2 shadow profile credits de-risked CDMO/platform/diagnostic Stage2 evidence, caps unresolved FDA binary risk, and rejects price-only 4B as full 4B.", "selected_by_profile": false, "MFE_90D_pct": 6.8, "MAE_90D_pct": -61.1, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L2_C3_HLB_REGULATORY_BINARY", "trigger_id": "R7L2_C3_T6_4C_TBREAK", "symbol": "028300", "trigger_type": "4C-thesis-break", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 9, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 10, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 10}, "weighted_score_before": 0.0, "stage_label_before": "Stage4C", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 9, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 10, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 10}, "weighted_score_after": 0.0, "stage_label_after": "Stage4C", "changed_components": ["relative_strength_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "positioning_overheat_score"], "component_delta_explanation": "R7 loop2 shadow profile credits de-risked CDMO/platform/diagnostic Stage2 evidence, caps unresolved FDA binary risk, and rejects price-only 4B as full 4B.", "selected_by_profile": true, "MFE_90D_pct": 46.2, "MAE_90D_pct": -29.9, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L2_C4_SEEG_DIAGNOSTIC_DEMAND_SHOCK", "trigger_id": "R7L2_C4_T1_STAGE2_EUA_DEMAND", "symbol": "096530", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 4, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 9, "customer_quality_score": 5, "policy_or_regulatory_score": 8, "valuation_repricing_score": 7, "execution_risk_score": 4, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 8, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 57.2, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 4, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 10, "customer_quality_score": 6, "policy_or_regulatory_score": 9, "valuation_repricing_score": 7, "execution_risk_score": 4, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 8, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 60.2, "stage_label_after": "Stage3-Green", "changed_components": ["relative_strength_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "positioning_overheat_score"], "component_delta_explanation": "R7 loop2 shadow profile credits de-risked CDMO/platform/diagnostic Stage2 evidence, caps unresolved FDA binary risk, and rejects price-only 4B as full 4B.", "selected_by_profile": true, "MFE_90D_pct": 349.6, "MAE_90D_pct": -2.5, "score_return_alignment_label": "score_high_return_high"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L2_C4_SEEG_DIAGNOSTIC_DEMAND_SHOCK", "trigger_id": "R7L2_C4_T3_STAGE3_YELLOW", "symbol": "096530", "trigger_type": "Stage3-Yellow", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 4, "margin_bridge_score": 7, "revision_score": 8, "relative_strength_score": 9, "customer_quality_score": 5, "policy_or_regulatory_score": 8, "valuation_repricing_score": 7, "execution_risk_score": 4, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 8, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 62.2, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 4, "margin_bridge_score": 7, "revision_score": 8, "relative_strength_score": 10, "customer_quality_score": 6, "policy_or_regulatory_score": 9, "valuation_repricing_score": 7, "execution_risk_score": 4, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 8, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 65.2, "stage_label_after": "Stage3-Green", "changed_components": ["relative_strength_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "positioning_overheat_score"], "component_delta_explanation": "R7 loop2 shadow profile credits de-risked CDMO/platform/diagnostic Stage2 evidence, caps unresolved FDA binary risk, and rejects price-only 4B as full 4B.", "selected_by_profile": false, "MFE_90D_pct": 249.8, "MAE_90D_pct": -9.9, "score_return_alignment_label": "score_high_return_high"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L2_C4_SEEG_DIAGNOSTIC_DEMAND_SHOCK", "trigger_id": "R7L2_C4_T4_STAGE3_GREEN", "symbol": "096530", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 4, "margin_bridge_score": 7, "revision_score": 8, "relative_strength_score": 9, "customer_quality_score": 5, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": 4, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 8, "positioning_overheat_score": 3, "thesis_break_score": 0}, "weighted_score_before": 61.9, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 4, "margin_bridge_score": 7, "revision_score": 8, "relative_strength_score": 9, "customer_quality_score": 5, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": 4, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 8, "positioning_overheat_score": 3, "thesis_break_score": 0}, "weighted_score_after": 61.9, "stage_label_after": "Stage3-Green", "changed_components": ["relative_strength_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "positioning_overheat_score"], "component_delta_explanation": "R7 loop2 shadow profile credits de-risked CDMO/platform/diagnostic Stage2 evidence, caps unresolved FDA binary risk, and rejects price-only 4B as full 4B.", "selected_by_profile": false, "MFE_90D_pct": 22.5, "MAE_90D_pct": -28.3, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R7L2_C4_SEEG_DIAGNOSTIC_DEMAND_SHOCK", "trigger_id": "R7L2_C4_T5_4B_BLOWOFF", "symbol": "096530", "trigger_type": "4B-watch", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 4, "margin_bridge_score": 7, "revision_score": 4, "relative_strength_score": 9, "customer_quality_score": 5, "policy_or_regulatory_score": 8, "valuation_repricing_score": 9, "execution_risk_score": 4, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 8, "positioning_overheat_score": 10, "thesis_break_score": 0}, "weighted_score_before": 55.8, "stage_label_before": "Stage3+4B-watch", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 4, "margin_bridge_score": 7, "revision_score": 4, "relative_strength_score": 9, "customer_quality_score": 5, "policy_or_regulatory_score": 8, "valuation_repricing_score": 9, "execution_risk_score": 4, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 7, "fcf_conversion_score": 8, "positioning_overheat_score": 10, "thesis_break_score": 0}, "weighted_score_after": 55.8, "stage_label_after": "Stage3+4B-watch", "changed_components": ["relative_strength_score", "customer_quality_score", "execution_risk_score", "legal_or_contract_risk_score", "positioning_overheat_score"], "component_delta_explanation": "R7 loop2 shadow profile credits de-risked CDMO/platform/diagnostic Stage2 evidence, caps unresolved FDA binary risk, and rejects price-only 4B as full 4B.", "selected_by_profile": false, "MFE_90D_pct": 3.4, "MAE_90D_pct": -43.6, "score_return_alignment_label": "score_high_return_low_false_positive"}
```

### 27.5 Profile comparison rows CSV

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,avg_MAE_90D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,4,4,4,23.4,-26.3,0.75,0.5,0.25,3,3,unavailable,unavailable,"reference"
profile_comparison,stage2_actionable_early_evidence_plus_with_binary_and_event_guardrail,4,4,4,151.7,-4.5,1.0,0.0,0.0,0,0,unavailable,unavailable,"best: improves upside capture with acceptable MAE"
profile_comparison,stage3_yellow_entry_relaxed,4,4,4,84.3,-23.8,0.75,0.5,0.25,0,1,unavailable,unavailable,"shadow test only"
profile_comparison,green_confirmation_timing_relaxed,4,4,4,88.3,-22.6,0.75,0.5,0.25,0,0,unavailable,unavailable,"shadow test only"
profile_comparison,four_b_peak_timing_tuned,4,4,4,3.3,-40.1,0.0,1.0,0.0,0,0,unavailable,unavailable,"shadow test only"
profile_comparison,four_c_thesis_break_earlier,4,1,1,46.2,-29.9,1.0,1.0,0.0,0,0,unavailable,unavailable,"shadow test only"
profile_comparison,binary_regulatory_and_event_premium_guardrail,4,4,3,169.6,-4.9,1.0,0.0,0.0,0,0,unavailable,unavailable,"shadow test only"
```

### 27.6 Shadow weight CSV

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,de_risked_stage2_actionable_evidence,0,2,+2,"Samsung Bio/Alteogen de-risked early evidence outperformed later Green entries","baseline avg MFE90 23.4 / MAE90 -26.4 improves to after-profile avg MFE90 151.9 / MAE90 -4.6","R7L2_C1_T2_STAGE2_ACTIONABLE|R7L2_C2_T2_STAGE2_ACTIONABLE",2,"shadow-only; not production"
shadow_weight,diagnostic_demand_shock_stage2_evidence,0,2,+2,"Seegene shows public diagnostic demand evidence can precede reported EPS and still be the best entry","Stage2 MFE90 349.6 and MAE90 -2.5 vs Green MFE90 22.5 and MAE90 -28.3","R7L2_C4_T1_STAGE2_EUA_DEMAND|R7L2_C4_T4_STAGE3_GREEN",2,"requires real demand authorization/export signal; not generic pandemic rumor"
shadow_weight,binary_regulatory_risk_cap,0,3,+3,"HLB shows high RS plus approval expectation can become false positive without final regulatory de-risking","HLB Yellow-like entry had MFE90 14.5 and MAE90 -58.3; after profile blocks full Green","R7L2_C3_T1_STAGE2_EVENT_PREMIUM|R7L2_C3_T3_STAGE3_YELLOW|R7L2_C3_T6_4C_TBREAK",3,"shadow-only; FDA/approval binary only"
shadow_weight,price_only_4b_reject_as_full_4b,0,2,+2,"Alteogen/HLB price-only peaks were useful watch overlays but require non-price evidence for full 4B","4B overlay rows show avg MFE90 3.3 and avg MAE90 -40.1; non-price evidence separates full 4B from watch-only","R7L2_C2_T5_4B_WATCH|R7L2_C3_T5_4B_WATCH|R7L2_C4_T5_4B_BLOWOFF",3,"shadow-only overlay logic"
```

### 27.7 Optimization decision rows JSONL

```jsonl
{"row_type": "optimization_decision", "decision_id": "R7L2_D1", "hypothesis": "Promote Stage2-Actionable when de-risked CDMO/platform/diagnostic evidence plus relative strength appear before Green.", "tested_trigger_ids": ["R7L2_C1_T2_STAGE2_ACTIONABLE", "R7L2_C2_T2_STAGE2_ACTIONABLE", "R7L2_C4_T1_STAGE2_EUA_DEMAND"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_binary_and_event_guardrail", "backtest_result_summary": "After profile improves avg selected MFE90 from 23.4 to 151.9 and avg MAE90 from -26.4 to -4.6 on the four case set.", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "R7 still mixes structural CDMO/platform, diagnostic shock, and binary approval risk; cross-round validation needed.", "risks": "May over-credit one-off demand shocks if no sustained revenue/margin bridge is present.", "next_validation_needed": "Find medtech/diagnostic demand-shock counterexamples and approval success/failure pairs."}
{"row_type": "optimization_decision", "decision_id": "R7L2_D2", "hypothesis": "Unresolved FDA/binary regulatory expectation must cap Green even when MFE before decision is high.", "tested_trigger_ids": ["R7L2_C3_T1_STAGE2_EVENT_PREMIUM", "R7L2_C3_T3_STAGE3_YELLOW", "R7L2_C3_T6_4C_TBREAK"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_binary_and_event_guardrail", "backtest_result_summary": "HLB late Yellow proxy produced MAE90 -58.3; hard 4C was late but still separates thesis break from normal volatility.", "accepted_or_rejected": "accepted", "delta_magnitude": "+3", "why_not_larger_delta": "Single hard binary failure in this loop; do not generalize to all biotech.", "risks": "May under-credit genuine approvals before final decision.", "next_validation_needed": "Validate with approval-success rows and false-break 4C rows."}
```

### 27.8 Narrative-only rows JSONL

```jsonl
{"row_type":"narrative_only","case_id":"R7L2_NONE","symbol":"none","reason":"no narrative-only rows used for weight calibration in this file","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

### 27.9 Aggregate metric rows CSV

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,3,3,152.8,97.9,-3.0,-3.2,unavailable,unavailable,unavailable,"representative rows only; duplicate same-entry labels excluded"
aggregate_metric,Stage2-Actionable,2,2,79.6,79.6,-6.2,-6.2,unavailable,unavailable,unavailable,"representative rows only; duplicate same-entry labels excluded"
aggregate_metric,Stage3-Green,3,3,26.4,22.5,-15.7,-10.6,unavailable,unavailable,unavailable,"representative rows only; duplicate same-entry labels excluded"
aggregate_metric,Stage3-Yellow,3,3,105.2,51.4,-29.0,-18.8,unavailable,unavailable,unavailable,"representative rows only; duplicate same-entry labels excluded"
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
completed_round = R7
completed_loop = 2
next_round = R8
next_loop = 2
next_sector = 플랫폼·콘텐츠·SW·보안
carry_forward_questions:
- 플랫폼/콘텐츠/SW에서도 Stage2 evidence가 Green보다 나은지 검증한다.
- price-only 4B와 non-price full 4B를 계속 분리한다.
- hard 4C는 명시적 thesis break evidence 없이는 부여하지 않는다.
```

## 30. Source Notes

- Price source: Songdaiki/stock-web, `atlas/manifest.json`, `atlas/schema.json`, and symbol profiles for 207940, 196170, 028300, 096530.
- Price basis: raw/unadjusted `tradable_raw`. No adjusted-price inference was used.
- Evidence source labels are research notes and must be batch-revalidated against official DART/MFDS/company disclosures before production ingestion.
- This document is not investment advice and contains no current/live candidate recommendation.
