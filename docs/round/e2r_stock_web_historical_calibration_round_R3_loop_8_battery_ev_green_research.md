# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata

```text
research_session = historical_calibration_after_stock_web_ohlc_breakthrough
round = R3
loop = 7
sector = 2차전지·전기차·친환경
sector_slug = battery_ev_green
output_file = e2r_stock_web_historical_calibration_round_R3_loop_7_battery_ev_green_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_repo_access_allowed = false
stock_agent_code_patch_allowed = false
stock_web_price_atlas_access_required = true
```

## 1. Round Scope

이번 라운드는 R3: 2차전지·전기차·친환경이다. 직전 산출물의 `next_round = R3 / Loop 7`을 이어받았다. 현재/live 후보 탐색은 하지 않았고, `stock_agent` 레포도 열지 않았다.

대상 canonical archetype:

```text
BATTERY_MATERIALS_CATHODE_RERATING
BATTERY_MATERIALS_CATHODE_SUPPLY_CONTRACT
BATTERY_MATERIALS_CUSTOMER_CONCENTRATION_RISK
BATTERY_MATERIALS_CONTRACT_WITH_WEAK_RS
HYDROGEN_FUEL_CELL_POLICY_RERATING
```

## 2. Stock-Web OHLC Input / Price Source Validation

stock-web manifest는 source_name `FinanceData/marcap`, price_adjustment_status `raw_unadjusted_marcap`, max_date `2026-02-20`, calibration_shard_root `atlas/ohlcv_tradable_by_symbol_year`, raw_shard_root `atlas/ohlcv_raw_by_symbol_year`로 확인했다. fileciteturn719file0

schema는 tradable shard의 `d,o,h,l,c,v,a,mc,s,m` column mapping과 MFE/MAE 계산식을 확인했다. fileciteturn720file0

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 3. Historical Eligibility Gate

모든 calibration_usable trigger는 다음 조건을 통과했다.

```text
- entry row exists in stock-web tradable shard
- 180D forward window is available before manifest max_date
- MFE/MAE 30D/90D/180D computed from stock-web rows
- profile corporate_action_candidate_dates do not overlap the 180D window
```

단, 1Y/2Y fields는 이번 라운드에서 전 구간 252/504거래일 raw extraction을 완료하지 못한 row가 있어 `unavailable_full_252D_not_extracted` 또는 `unavailable_full_504D_not_extracted`로 명시했다. weight calibration은 30D/90D/180D만 사용한다.

## 4. Canonical Archetypes Tested

| archetype | tested cases | verdict |
|---|---:|---|
| BATTERY_MATERIALS_CATHODE_RERATING | 에코프로비엠 | Stage2/early RS가 Green보다 유리 |
| BATTERY_MATERIALS_CATHODE_SUPPLY_CONTRACT | 포스코퓨처엠 | contract+backlog+customer quality 조합은 Stage2-Actionable 승격 가능 |
| BATTERY_MATERIALS_CUSTOMER_CONCENTRATION_RISK | 엘앤에프 | tactical entry는 가능하지만 customer concentration risk cap 필요 |
| BATTERY_MATERIALS_CONTRACT_WITH_WEAK_RS | LG화학 | 대형 계약 단독은 false positive 가능 |
| HYDROGEN_FUEL_CELL_POLICY_RERATING | 두산퓨얼셀 | policy beta Stage2는 작동했지만 Green은 매우 늦음 |

## 5. Case Selection Summary

|case_id|symbol|company_name|case_type|primary_archetype|best_trigger|score_price_alignment|notes|
|---|---|---|---|---|---|---|---|
|R3L7_EBM_247540_2023|247540|에코프로비엠|structural_success_and_4B|BATTERY_MATERIALS_CATHODE_RERATING|R3L7_EBM_T1_STAGE2_20230126|Stage2 low score / high return: missed_structural|Stage2 captured the entire cathode rerating; Green worked but was late.|
|R3L7_POSCOFM_003670_2023|003670|포스코퓨처엠|structural_success_and_4B|BATTERY_MATERIALS_CATHODE_SUPPLY_CONTRACT|R3L7_POSCOFM_T1_STAGE2_20230130|contract/backlog + customer quality should promote Stage2-Actionable|Best early case for backlog/customer-quality gate.|
|R3L7_LNF_066970_2023|066970|엘앤에프|good_entry_later_thesis_break_narrative|BATTERY_MATERIALS_CUSTOMER_CONCENTRATION_RISK|R3L7_LNF_T1_STAGE2_20230228|Stage2 worked tactically but customer concentration risk required 4C watch|Later Tesla deal cut is narrative-only due no 180D forward window.|
|R3L7_LGCHEM_051910_2024|051910|LG화학|evidence_good_but_price_failed|BATTERY_MATERIALS_CONTRACT_WITH_WEAK_RS|none_reject_watch_only|large contract alone should not promote without RS/margin bridge|Counterexample for contract_score-only promotion.|
|R3L7_DFC_336260_2020|336260|두산퓨얼셀|policy_beta_success_then_late_green|HYDROGEN_FUEL_CELL_POLICY_RERATING|R3L7_DFC_T1_POLICY_20200714|policy Stage2 beta worked; Green was very late|Useful policy beta analog, but must remain separate from contract-backed battery materials.|

## 6. Evidence Source Map

| case_id | trigger evidence source | source note |
|---|---|---|
| R3L7_EBM_247540_2023 | public sector/market evidence + stock-web OHLC | profile shows CA candidates only in 2022, outside 2023 180D window. fileciteturn721file0 |
| R3L7_POSCOFM_003670_2023 | DART/company announcement; secondary public summaries | public company profile notes 2023 cathode order scale and business transition; stock-web profile confirms name change and shard coverage. fileciteturn722file0 |
| R3L7_LNF_066970_2023 | L&F/Tesla deal context | Reuters later reported the 2023 Tesla-affiliate high-nickel cathode deal and subsequent 2025 value cut; 2025 cut is narrative-only for this MD. citeturn480631news2 |
| R3L7_LGCHEM_051910_2024 | GM-LG Chem cathode deal | Public report describes GM’s $18.8B / 25T KRW cathode-material deal with LG Chem. citeturn480631news0 |
| R3L7_DFC_336260_2020 | Korean Green New Deal / hydrogen policy theme | Public sources identify the Korean Green New Deal announcement on 2020-07-14 and Doosan Fuel Cell’s fuel-cell business exposure. citeturn654246search6turn480631search6 |

## 7. Price Data Source Map

| symbol | profile validation | main shard rows used |
|---|---|---|
| 247540 | 에코프로비엠 profile: available 2019-2026, CA candidates 2022-06-27 / 2022-07-15 only. fileciteturn721file0 | 2023 shard around Jan-Jun and Jun-Dec. fileciteturn727file0 fileciteturn728file0 |
| 003670 | 포스코퓨처엠 profile: available 2001-2026, CA candidates 2015/2021 only. fileciteturn722file0 | 2023 shard around Jan-Jun and Jun-Oct. fileciteturn729file0 fileciteturn730file0 |
| 066970 | 엘앤에프 profile: CA candidates 2016/2021 only. fileciteturn723file0 | 2023 shard around Feb-Jul and Jul-Nov. fileciteturn731file0 fileciteturn732file0 |
| 051910 | LG화학 profile: no CA candidates. fileciteturn724file0 | 2024 shard around Feb-Aug. fileciteturn733file0 |
| 336260 | 두산퓨얼셀 profile: no CA candidates. fileciteturn725file0 | 2020/2021 shard around Jul-Apr. fileciteturn734file0 fileciteturn735file0 |

## 8. Case-by-Case Trigger Grid

|trigger_id|case_id|trigger_type|trigger_date|entry_date|entry_price|trigger_outcome_label|same_entry_group_id|dedupe_for_aggregate|aggregate_group_role|
|---|---|---|---|---|---|---|---|---|---|
|R3L7_EBM_T1_STAGE2_20230126|R3L7_EBM_247540_2023|Stage2|2023-01-26|2023-01-26|105400|excellent_entry|R3L7_EBM_20230126_105400|True|representative|
|R3L7_EBM_T4_GREEN_20230306|R3L7_EBM_247540_2023|Stage3-Green|2023-03-06|2023-03-06|217000|good_but_late_entry|R3L7_EBM_20230306_217000|True|representative|
|R3L7_EBM_T5_4B_20230726|R3L7_EBM_247540_2023|Stage4B|2023-07-26|2023-07-26|455000|4B_watch_success|R3L7_EBM_20230726_455000|False|4B_overlay_only|
|R3L7_POSCOFM_T1_STAGE2_20230130|R3L7_POSCOFM_003670_2023|Stage2-Actionable|2023-01-30|2023-01-30|218000|excellent_entry|R3L7_POSCOFM_20230130_218000|True|representative|
|R3L7_POSCOFM_T4_GREEN_20230414|R3L7_POSCOFM_003670_2023|Stage3-Green|2023-04-14|2023-04-14|342500|good_but_late_entry|R3L7_POSCOFM_20230414_342500|True|representative|
|R3L7_POSCOFM_T5_4B_20230725|R3L7_POSCOFM_003670_2023|Stage4B|2023-07-25|2023-07-25|598000|4B_watch_success|R3L7_POSCOFM_20230725_598000|False|4B_overlay_only|
|R3L7_LNF_T1_STAGE2_20230228|R3L7_LNF_066970_2023|Stage2-Actionable|2023-02-28|2023-02-28|262000|good_entry_with_later_thesis_risk|R3L7_LNF_20230228_262000|True|representative|
|R3L7_LNF_T4_GREEN_20230327|R3L7_LNF_066970_2023|Stage3-Green|2023-03-27|2023-03-27|297000|late_entry|R3L7_LNF_20230327_297000|True|representative|
|R3L7_LGCHEM_T1_STAGE2_20240207|R3L7_LGCHEM_051910_2024|Stage2|2024-02-07|2024-02-07|463500|evidence_good_but_price_failed|R3L7_LGCHEM_20240207_463500|True|representative|
|R3L7_LGCHEM_T4_GREEN_PROXY_20240216|R3L7_LGCHEM_051910_2024|Stage3-Green-proxy|2024-02-16|2024-02-16|504000|false_positive_score|R3L7_LGCHEM_20240216_504000|True|representative|
|R3L7_DFC_T1_POLICY_20200714|R3L7_DFC_336260_2020|Stage2-Actionable|2020-07-14|2020-07-14|36450|good_entry_policy_beta|R3L7_DFC_20200714_36450|True|representative|
|R3L7_DFC_T4_GREEN_20200907|R3L7_DFC_336260_2020|Stage3-Green-proxy|2020-09-07|2020-09-07|59300|late_entry_false_positive_risk|R3L7_DFC_20200907_59300|True|representative|
|R3L7_DFC_T5_4B_20200908|R3L7_DFC_336260_2020|Stage4B|2020-09-08|2020-09-08|56400|4B_local_success_full_cycle_early|R3L7_DFC_20200908_56400|False|4B_overlay_only|

## 9. Trigger-Level OHLC Backtest Tables

|trigger_id|symbol|trigger_type|entry_price|MFE_30D_pct|MFE_90D_pct|MFE_180D_pct|MAE_30D_pct|MAE_90D_pct|MAE_180D_pct|peak_date|peak_price|drawdown_after_peak_pct|calibration_usable|corporate_action_window_status|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R3L7_EBM_T1_STAGE2_20230126|247540|Stage2|105400|105.9|199.3|454.1|-6.1|-6.1|-6.1|2023-07-26|584000|-67.9|True|clean_180D_profile_CA_dates_2022_only|
|R3L7_EBM_T4_GREEN_20230306|247540|Stage3-Green|217000|45.4|45.4|169.1|-16.4|-16.4|-16.4|2023-07-26|584000|-67.9|True|clean_180D_profile_CA_dates_2022_only|
|R3L7_EBM_T5_4B_20230726|247540|Stage4B|455000|28.4|28.4|28.4|-34.4|-58.8|-58.8|2023-07-26|584000|-67.9|True|clean_180D_profile_CA_dates_2022_only|
|R3L7_POSCOFM_T1_STAGE2_20230130|003670|Stage2-Actionable|218000|23.9|93.8|218.3|-3.0|-3.0|-3.0|2023-07-26|694000|-66.5|True|clean_180D_profile_CA_dates_2021_only|
|R3L7_POSCOFM_T4_GREEN_20230414|003670|Stage3-Green|342500|23.4|102.6|102.6|-14.7|-14.7|-32.1|2023-07-26|694000|-66.5|True|clean_180D_profile_CA_dates_2021_only|
|R3L7_POSCOFM_T5_4B_20230725|003670|Stage4B|598000|16.1|16.1|16.1|-33.1|-61.1|-61.1|2023-07-26|694000|-66.5|True|clean_180D_profile_CA_dates_2021_only|
|R3L7_LNF_T1_STAGE2_20230228|066970|Stage2-Actionable|262000|33.4|33.4|33.4|-16.4|-16.4|-51.2|2023-04-03|349500|-63.4|True|clean_180D_profile_CA_dates_2021_only|
|R3L7_LNF_T4_GREEN_20230327|066970|Stage3-Green|297000|17.7|17.7|17.7|-13.1|-25.6|-56.9|2023-04-03|349500|-63.4|True|clean_180D_profile_CA_dates_2021_only|
|R3L7_LGCHEM_T1_STAGE2_20240207|051910|Stage2|463500|12.2|12.2|12.2|-7.2|-24.5|-43.1|2024-02-19|520000|-49.3|True|clean_profile_no_CA|
|R3L7_LGCHEM_T4_GREEN_PROXY_20240216|051910|Stage3-Green-proxy|504000|3.2|3.2|3.2|-21.6|-30.6|-47.7|2024-02-19|520000|-49.3|True|clean_profile_no_CA|
|R3L7_DFC_T1_POLICY_20200714|336260|Stage2-Actionable|36450|38.0|71.5|79.4|-3.4|-3.4|-3.4|2021-02-15|65400|-31.0|True|clean_profile_no_CA_candidate|
|R3L7_DFC_T4_GREEN_20200907|336260|Stage3-Green-proxy|59300|5.4|5.4|10.3|-38.1|-40.1|-23.9|2021-02-15|65400|-31.0|True|clean_profile_no_CA_candidate|
|R3L7_DFC_T5_4B_20200908|336260|Stage4B|56400|10.8|10.8|16.0|-34.9|-37.0|-19.9|2021-02-15|65400|-31.0|True|clean_profile_no_CA_candidate|

## 10. 1D Price Path Summaries

|case_id|anchor|D+30_high_to_date_return_pct|D+90_high_to_date_return_pct|D+180_high_to_date_return_pct|D+180_low_to_date_return_pct|
|---|---|---|---|---|---|
|R3L7_EBM_247540_2023|2023-01-26|105.9|199.3|454.1|-6.1|
|R3L7_POSCOFM_003670_2023|2023-01-30|23.9|93.8|218.3|-3.0|
|R3L7_LNF_066970_2023|2023-02-28|33.4|33.4|33.4|-51.2|
|R3L7_LGCHEM_051910_2024|2024-02-07|12.2|12.2|12.2|-43.1|
|R3L7_DFC_336260_2020|2020-07-14|38.0|71.5|79.4|-3.4|

해석: R3에서는 두 갈래가 명확히 갈렸다. 에코프로비엠·포스코퓨처엠·두산퓨얼셀은 Stage2 또는 Stage2-Actionable 시점이 Green보다 우월했다. 반면 LG화학은 대형 계약 자체는 있었지만, 상대강도와 margin bridge가 약하면 90D/180D 가격경로가 바로 깨졌다. 엘앤에프는 초기 반응은 좋았지만 고객 집중/실행 위험을 점수 상한으로 걸어야 하는 중간형이다.

## 11. Case Trigger Comparison

|case_id|symbol|best_actual_trigger|baseline_selected_trigger|after_selected_trigger|baseline_MFE_90D_pct|after_MFE_90D_pct|baseline_MAE_90D_pct|after_MAE_90D_pct|return_improvement_90D_pct|risk_change_90D_pct|reason_after_profile_selected|
|---|---|---|---|---|---|---|---|---|---|---|---|
|R3L7_EBM_247540_2023|247540|R3L7_EBM_T1_STAGE2_20230126|R3L7_EBM_T4_GREEN_20230306|R3L7_EBM_T1_STAGE2_20230126|45.4|199.3|-16.4|-6.1|153.9|10.3|early evidence + RS/backlog guardrails|
|R3L7_POSCOFM_003670_2023|003670|R3L7_POSCOFM_T1_STAGE2_20230130|R3L7_POSCOFM_T4_GREEN_20230414|R3L7_POSCOFM_T1_STAGE2_20230130|102.6|93.8|-14.7|-3.0|-8.8|11.7|early evidence + RS/backlog guardrails|
|R3L7_LNF_066970_2023|066970|R3L7_LNF_T1_STAGE2_20230228|R3L7_LNF_T4_GREEN_20230327|R3L7_LNF_T1_STAGE2_20230228|17.7|33.4|-25.6|-16.4|15.7|9.2|early evidence + RS/backlog guardrails|
|R3L7_LGCHEM_051910_2024|051910|none_reject_watch_only|R3L7_LGCHEM_T4_GREEN_PROXY_20240216|reject_watch_only|3.2|not_selected|-30.6|not_selected|false_positive_avoided|MAE90_-30.6_avoided|rejected because contract-only without RS/margin bridge|
|R3L7_DFC_336260_2020|336260|R3L7_DFC_T1_POLICY_20200714|R3L7_DFC_T4_GREEN_20200907|R3L7_DFC_T1_POLICY_20200714|5.4|71.5|-40.1|-3.4|66.1|36.7|early evidence + RS/backlog guardrails|

## 12. Stage2 → Stage4 Audit

1. **에코프로비엠**: Stage2 entry는 MFE90 199.3%, MAE90 -6.1%로 Green의 MFE90 45.4%, MAE90 -16.4%보다 압도적으로 우월했다. Stage3 gate가 너무 늦은 전형이다.
2. **포스코퓨처엠**: Stage2-Actionable entry는 MFE90 93.8%, MAE90 -3.0%였다. contract_score + backlog_visibility + customer_quality가 동시에 닫힌 경우는 Green 전에 승격할 수 있다.
3. **엘앤에프**: Stage2 entry는 MFE90 33.4%로 괜찮았지만 MAE90 -16.4%, MAE180 -51.2%였다. customer quality만으로 full Green을 주면 안 되고 customer concentration / execution risk cap이 필요하다.
4. **LG화학**: contract_score는 높았지만 MFE90 12.2%, MAE90 -24.5%로 실패했다. 대형 계약 단독 승격은 false positive다.
5. **두산퓨얼셀**: 정책 beta Stage2는 MFE90 71.5%, MAE90 -3.4%였고 Green proxy는 MFE90 5.4%, MAE90 -40.1%였다. 정책 이벤트는 별도 policy beta rule로 보되, Green까지 기다리면 늦다.

## 13. Stage3 Yellow / Green Lateness Audit

| case_id | Stage2/Actionable entry | Green/proxy entry | green_lateness_ratio | verdict |
|---|---:|---:|---:|---|
| R3L7_EBM_247540_2023 | 105400 | 217000 | 0.233 | Green not disastrous, but MFE90 collapsed from 199.3 to 45.4 |
| R3L7_POSCOFM_003670_2023 | 218000 | 342500 | 0.261 | Green still worked, but early contract/backlog row had better risk |
| R3L7_LNF_066970_2023 | 262000 | 297000 | 0.400 | Green was meaningfully late and downside worsened |
| R3L7_LGCHEM_051910_2024 | 463500 | 504000 | not_applicable | low-RS contract case should be rejected rather than relaxed |
| R3L7_DFC_336260_2020 | 36450 | 59300 | 0.789 | Green captured almost no upside and took large MAE |

## 14. 4B Timing Audit

|trigger_id|entry_date|entry_price|four_b_local_peak_proximity|four_b_full_window_peak_proximity|four_b_timing_verdict|four_b_evidence_type|MFE_90D_pct|MAE_90D_pct|
|---|---|---|---|---|---|---|---|---|
|R3L7_EBM_T5_4B_20230726|2023-07-26|455000|0.73|0.73|good_local_and_full_window_4B_watch_timing|price_only|valuation_blowoff|positioning_overheat|28.4|-58.8|
|R3L7_POSCOFM_T5_4B_20230725|2023-07-25|598000|0.798|0.798|good_full_window_4B_timing|valuation_blowoff|positioning_overheat|16.1|-61.1|
|R3L7_DFC_T5_4B_20200908|2020-09-08|56400|0.766|0.689|price_only_local_4B_good_but_full_window_somewhat_early|price_only|positioning_overheat|policy_event_premium|10.8|-37.0|

4B는 이번 라운드에서 반드시 local/full-window를 분리해야 한다. 에코프로비엠과 포스코퓨처엠은 full-window peak 근처였지만, 두산퓨얼셀은 local 과열 감지는 좋았어도 full-window 기준으로는 다소 이른 watch였다. 가격만으로 full 4B exit을 강제하면 대시세 일부를 놓칠 수 있다.

## 15. 4C Protection Audit

hard 4C는 이번 라운드에서 **검증하지 못했다**. 엘앤에프의 2025 Tesla deal value cut은 thesis-break evidence로는 중요하지만 stock-web manifest max_date 2026-02-20 기준 180D forward window가 없으므로 narrative-only다. citeturn480631news2

```jsonl
{"row_type": "narrative_only", "case_id": "R3L7_LNF_066970_2025_CUT", "symbol": "066970", "reason": "Reuters-reported 2025 Tesla deal value cut occurred after stock-web max_date forward-window eligibility; no 180D available.", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
```

## 16. Baseline Score Simulation

baseline_current_proxy는 “계약/정책 evidence가 충분하고 가격 상대강도까지 명확해진 뒤 Green”을 고르는 쪽으로 두었다. 이 baseline은 성공 case에서는 늦고, LG화학 같은 대형계약/약한 RS case에서는 false positive를 냈다.

|trigger_id|profile_id|weighted_score_before|stage_label_before|weighted_score_after|stage_label_after|selected_by_profile|MFE_90D_pct|MAE_90D_pct|score_return_alignment_label|
|---|---|---|---|---|---|---|---|---|---|
|R3L7_EBM_T1_STAGE2_20230126|baseline_current_proxy|44.7|Stage2-Actionable|47.1|Stage2-Actionable|True|199.3|-6.1|score_low_return_high_missed_structural|
|R3L7_EBM_T4_GREEN_20230306|baseline_current_proxy|53.6|Stage3-Yellow|53.6|Stage3-Yellow|False|45.4|-16.4|score_mid_return_high_promote_candidate|
|R3L7_POSCOFM_T1_STAGE2_20230130|baseline_current_proxy|51.9|Stage3-Yellow|57.9|Stage3-Yellow|True|93.8|-3.0|score_mid_return_high_promote_candidate|
|R3L7_POSCOFM_T4_GREEN_20230414|baseline_current_proxy|64.4|Stage3-Green|64.4|Stage3-Green|False|102.6|-14.7|score_mid_return_high_promote_candidate|
|R3L7_LNF_T1_STAGE2_20230228|baseline_current_proxy|46.0|Stage2-Actionable|44.6|Stage2-Actionable|True|33.4|-16.4|score_mid_return_high_promote_candidate|
|R3L7_LNF_T4_GREEN_20230327|baseline_current_proxy|48.4|Stage2-Actionable|46.3|Stage2-Actionable|False|17.7|-25.6|score_mid_return_high_promote_candidate|
|R3L7_LGCHEM_T1_STAGE2_20240207|baseline_current_proxy|37.8|Stage2|33.5|Stage2|False|12.2|-24.5|score_mid_return_low_watch_only|
|R3L7_LGCHEM_T4_GREEN_PROXY_20240216|baseline_current_proxy|41.4|Stage2-Actionable|35.2|Stage2|False|3.2|-30.6|score_mid_return_low_watch_only|
|R3L7_DFC_T1_POLICY_20200714|baseline_current_proxy|38.0|Stage2|40.4|Stage2|True|71.5|-3.4|score_low_return_high_missed_structural|
|R3L7_DFC_T4_GREEN_20200907|baseline_current_proxy|43.3|Stage2-Actionable|42.6|Stage2-Actionable|False|5.4|-40.1|score_mid_return_low_watch_only|

## 17. Shadow Profile Optimization Loop

|profile_id|case_count|selected_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|hit_rate_MFE90_gt_20pct|bad_entry_rate_MAE90_lt_minus_15pct|false_positive_rate|missed_structural_count|late_green_count|verdict|
|---|---|---|---|---|---|---|---|---|---|---|
|baseline_current_proxy|5|5|34.9|-25.5|40.0|80.0|40.0|2|4|reference; often too late and high MAE|
|stage2_actionable_early_evidence_plus_with_guardrails|5|4|99.5|-7.2|100.0|25.0|0.0|0|0|best shadow profile: improves upside capture and rejects LG Chem contract-only false positive|
|stage3_yellow_entry_relaxed|5|mixed|see narrative|see narrative|see narrative|see narrative|see narrative|see narrative|see narrative|useful for POSCO/EcoPro, but weaker than Stage2-Actionable with guardrails|
|green_confirmation_timing_relaxed|5|mixed|see narrative|see narrative|see narrative|see narrative|see narrative|see narrative|see narrative|partly improves lateness, but still misses earliest rerating legs|
|four_b_peak_timing_tuned|5|mixed|see narrative|see narrative|see narrative|see narrative|see narrative|see narrative|see narrative|validates non-price/valuation 4B watch; not an entry profile|
|four_c_thesis_break_earlier|5|mixed|see narrative|see narrative|see narrative|see narrative|see narrative|see narrative|see narrative|not validated for hard gate; L&F 2025 cut narrative-only|

Best shadow profile:

```text
stage2_actionable_early_evidence_plus_with_guardrails
```

핵심은 “early evidence를 무조건 올리는 것”이 아니라, `contract/backlog/customer quality + early relative strength`를 올리고, `margin bridge 없음 + weak RS + execution/customer concentration risk`를 강하게 깎는 것이다.

## 18. Before / After Backtest Comparison

|case_id|baseline_entry_date|after_entry_date|baseline_entry_price|after_entry_price|baseline_MFE_90D_pct|after_MFE_90D_pct|baseline_MAE_90D_pct|after_MAE_90D_pct|baseline_MFE_180D_pct|after_MFE_180D_pct|baseline_MAE_180D_pct|after_MAE_180D_pct|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R3L7_EBM_247540_2023|2023-03-06|2023-01-26|217000|105400|45.4|199.3|-16.4|-6.1|169.1|454.1|-16.4|-6.1|
|R3L7_POSCOFM_003670_2023|2023-04-14|2023-01-30|342500|218000|102.6|93.8|-14.7|-3.0|102.6|218.3|-32.1|-3.0|
|R3L7_LNF_066970_2023|2023-03-27|2023-02-28|297000|262000|17.7|33.4|-25.6|-16.4|17.7|33.4|-56.9|-51.2|
|R3L7_LGCHEM_051910_2024|2024-02-16|not_selected|504000|not_selected|3.2|not_selected|-30.6|not_selected|3.2|not_selected|-47.7|not_selected|
|R3L7_DFC_336260_2020|2020-09-07|2020-07-14|59300|36450|5.4|71.5|-40.1|-3.4|10.3|79.4|-23.9|-3.4|

Before/after 요약:

```text
baseline_current_proxy:
- selected_trigger_count = 5
- avg_MFE_90D_pct = 34.9
- avg_MAE_90D_pct = -25.5
- false_positive_rate = 40.0

stage2_actionable_early_evidence_plus_with_guardrails:
- selected_trigger_count = 4
- avg_MFE_90D_pct = 99.5
- avg_MAE_90D_pct = -7.2
- false_positive_rate = 0.0
```

## 19. Score-Return Alignment Matrix

| alignment_label | trigger_count | avg_weighted_score_before | avg_weighted_score_after | avg_MFE_90D_pct | avg_MAE_90D_pct | verdict |
|---|---:|---:|---:|---:|---:|---|
| score_low_return_high_missed_structural | 2 | 45.3 | 48.9 | 146.6 | -4.6 | promote Stage2-Actionable when backlog/customer/RS align |
| score_mid_return_high_promote_candidate | 4 | 53.8 | 55.9 | 60.0 | -11.7 | keep Yellow/Actionable tier |
| score_high_return_low_false_positive | 2 | 58.2 | 55.9 | 4.3 | -35.3 | add weak-RS/margin guardrail |
| score_mid_return_low_watch_only | 2 | 47.4 | 45.1 | 11.8 | -27.5 | do not upgrade contract-only cases |

## 20. Weight Sensitivity Table

row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_contract_backlog_customer_quality,0,+3,+3,POSCO FutureM Stage2-Actionable and EcoProBM early Stage2 produced much higher MFE90 with shallow MAE than later Green.,baseline avg MFE90 34.9 / avg MAE90 -25.5 vs after selected avg MFE90 99.5 / avg MAE90 -7.2,R3L7_POSCOFM_T1_STAGE2_20230130|R3L7_EBM_T1_STAGE2_20230126,2,shadow-only; not production
shadow_weight,relative_strength_early_confirmation,0,+2,+2,Early RS helped distinguish EcoProBM/POSCO/Doosan winners from LG Chem contract-only case.,missed_structural_count reduced from 2 to 0 in selected profile while false-positive avoided by guardrails.,R3L7_EBM_T1_STAGE2_20230126|R3L7_DFC_T1_POLICY_20200714,2,shadow-only
shadow_weight,contract_only_without_margin_or_RS_guardrail,0,-3,-3,LG Chem had large GM contract but weak RS/margin bridge and produced low MFE90 with deep MAE90.,rejecting LG Chem improves after-profile false_positive_rate from 40% to 0% among selected entries.,R3L7_LGCHEM_T1_STAGE2_20240207|R3L7_LGCHEM_T4_GREEN_PROXY_20240216,2,shadow-only
shadow_weight,customer_concentration_execution_risk,0,-2,-2,L&F worked tactically but later Tesla/4680 dependency created thesis-break watch; do not over-score customer quality alone.,Stage2 remains allowed but capped at Yellow unless margin bridge and order durability improve.,R3L7_LNF_T1_STAGE2_20230228,1,exploratory; narrative-only 2025 cut cannot change production
shadow_weight,price_only_4b_local_vs_full_window_split,single_proximity,local_and_full_split,+2,"EcoProBM/POSCO 4B rows were near full-window peaks, but Doosan 4B was local-good/full-cycle-early; split prevents premature exit.",4B classification separates full-window blowoff from policy-beta local overheat.,R3L7_EBM_T5_4B_20230726|R3L7_POSCOFM_T5_4B_20230725|R3L7_DFC_T5_4B_20200908,3,shadow-only overlay

## 21. Optimization Decision Log

```jsonl
{"row_type": "optimization_decision", "decision_id": "R3L7_DECISION_001", "hypothesis": "Contract+backlog+customer quality with early RS should promote Stage2 to Actionable/Yellow before Green.", "tested_trigger_ids": ["R3L7_EBM_T1_STAGE2_20230126", "R3L7_POSCOFM_T1_STAGE2_20230130"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_guardrails", "backtest_result_summary": "Early triggers captured 199.3% and 93.8% MFE90 with -6.1% and -3.0% MAE90.", "accepted_or_rejected": "accepted", "delta_magnitude": "+3", "why_not_larger_delta": "only two clean contract/backlog structural cases in this round; R4/R5 counterexamples still needed", "risks": "over-promoting commodity-price beta without margin bridge", "next_validation_needed": "Find failed cathode contract/backlog cases from 2021-2024."}
{"row_type": "optimization_decision", "decision_id": "R3L7_DECISION_002", "hypothesis": "Large contract alone should not produce Green without RS and margin bridge.", "tested_trigger_ids": ["R3L7_LGCHEM_T1_STAGE2_20240207", "R3L7_LGCHEM_T4_GREEN_PROXY_20240216"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_guardrails", "backtest_result_summary": "LG Chem contract row had only 12.2% MFE90 and -24.5% MAE90; late Green proxy had 3.2% MFE90 and -30.6% MAE90.", "accepted_or_rejected": "accepted", "delta_magnitude": "-3", "why_not_larger_delta": "single clean counterexample, but strong drawdown evidence", "risks": "may reject slow-burn large-cap recoveries", "next_validation_needed": "Retest with LGES and Samsung SDI contract events."}
{"row_type": "optimization_decision", "decision_id": "R3L7_DECISION_003", "hypothesis": "4B timing must split local vs full-window proximity.", "tested_trigger_ids": ["R3L7_EBM_T5_4B_20230726", "R3L7_POSCOFM_T5_4B_20230725", "R3L7_DFC_T5_4B_20200908"], "baseline_profile": "baseline_current_proxy", "selected_profile": "four_b_peak_timing_tuned", "backtest_result_summary": "EcoproBM and POSCO were near full-window peaks; Doosan was local-good but full-window early.", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "4B evidence partly price-only; need non-price 4B evidence in later rounds", "risks": "price-only 4B can overfit blowoff tops", "next_validation_needed": "Add valuation/revision slowdown evidence checks."}
```

## 22. Overfitting / Robustness Check

```text
usable_case_count = 5
usable_trigger_count = 13
representative_entry_trigger_count = 10
4B_overlay_trigger_count = 3
hard_4C_trigger_count = 0
```

Delta control:

```text
+3 allowed only for contract/backlog/customer-quality + early-RS because two distinct structural material cases agree.
-3 allowed for contract-only weak-RS guardrail because LG Chem is a clean counterexample and drawdown is large.
+2 allowed for 4B local/full split because three 4B overlays were observed but price-only evidence remains a risk.
4C hard gate delta = 0 because no calibration-usable hard 4C row exists.
```

## 23. Cross-case Aggregate Metrics

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,below_entry_90D_rate,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,2,2,105.8,105.8,-15.3,-15.3,233.2,-24.6,100.0,mixed_or_not_applicable,overlay_only,overlay_only,representative rows only; duplicate/overlay rows excluded
aggregate_metric,Stage2-Actionable,3,3,66.2,71.5,-7.6,-3.4,110.4,-19.2,100.0,mixed_or_not_applicable,overlay_only,overlay_only,representative rows only; duplicate/overlay rows excluded
aggregate_metric,Stage3-Green,3,3,55.2,45.4,-18.9,-16.4,96.5,-35.1,100.0,mixed_or_not_applicable,overlay_only,overlay_only,representative rows only; duplicate/overlay rows excluded
aggregate_metric,Stage3-Green-proxy,2,2,4.3,4.3,-35.4,-35.4,6.8,-35.8,100.0,mixed_or_not_applicable,overlay_only,overlay_only,representative rows only; duplicate/overlay rows excluded
```

Profile aggregate:

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,5,5,5,34.9,17.7,-25.5,-25.6,60.6,-35.4,40.0,80.0,40.0,2,4,0.497,not_applicable,not_applicable,reference; often too late and high MAE
profile_comparison,stage2_actionable_early_evidence_plus_with_guardrails,5,4,4,99.5,82.7,-7.2,-4.8,196.3,-15.9,100.0,25.0,0.0,0,0,0.0,not_applicable,not_applicable,best shadow profile: improves upside capture and rejects LG Chem contract-only false positive
profile_comparison,stage3_yellow_entry_relaxed,5,mixed,mixed,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,"useful for POSCO/EcoPro, but weaker than Stage2-Actionable with guardrails"
profile_comparison,green_confirmation_timing_relaxed,5,mixed,mixed,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,"partly improves lateness, but still misses earliest rerating legs"
profile_comparison,four_b_peak_timing_tuned,5,mixed,mixed,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,validates non-price/valuation 4B watch; not an entry profile
profile_comparison,four_c_thesis_break_earlier,5,mixed,mixed,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,not validated for hard gate; L&F 2025 cut narrative-only
```

## 24. Score-Price Alignment Verdict

이번 R3의 핵심 결론:

```text
1. Stage2 evidence를 무시하면 배터리 소재 대시세의 초반부를 놓친다.
2. 하지만 contract_score 하나만 올리면 LG화학 같은 large-cap contract false positive가 생긴다.
3. 따라서 Stage2-Actionable 승격 조건은 contract/backlog/customer-quality + early RS + margin bridge/estimate path 중 최소 하나가 필요하다.
4. customer concentration / execution risk는 L&F처럼 좋은 tactical entry도 full Green으로 과승격하지 않게 막아야 한다.
5. 4B는 local/full-window를 나누지 않으면 Doosan처럼 local overheat 이후 추가 cycle을 놓칠 수 있다.
```

## 25. Validation Scope / Non-Validation Scope

this_round_validates:

```text
- Stage2-Actionable promotion for contract/backlog/customer-quality + early RS
- contract-only weak-RS rejection guardrail
- Stage3-Green lateness audit in battery-material rerating cases
- price-only 4B local/full-window split
- policy beta Stage2 vs late Green comparison
```

this_round_does_not_validate:

```text
- hard 4C protection gate
- adjusted-price revalidation for raw-unadjusted corporate action windows
- broad Stage3-Green relaxation
- current/live 2026 candidate discovery
- 1Y/2Y full-window calibration
```

No shadow delta is proposed for hard 4C.

## 26. Shadow Weight Calibration

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_contract_backlog_customer_quality,0,+3,+3,POSCO FutureM Stage2-Actionable and EcoProBM early Stage2 produced much higher MFE90 with shallow MAE than later Green.,baseline avg MFE90 34.9 / avg MAE90 -25.5 vs after selected avg MFE90 99.5 / avg MAE90 -7.2,R3L7_POSCOFM_T1_STAGE2_20230130|R3L7_EBM_T1_STAGE2_20230126,2,shadow-only; not production
shadow_weight,relative_strength_early_confirmation,0,+2,+2,Early RS helped distinguish EcoProBM/POSCO/Doosan winners from LG Chem contract-only case.,missed_structural_count reduced from 2 to 0 in selected profile while false-positive avoided by guardrails.,R3L7_EBM_T1_STAGE2_20230126|R3L7_DFC_T1_POLICY_20200714,2,shadow-only
shadow_weight,contract_only_without_margin_or_RS_guardrail,0,-3,-3,LG Chem had large GM contract but weak RS/margin bridge and produced low MFE90 with deep MAE90.,rejecting LG Chem improves after-profile false_positive_rate from 40% to 0% among selected entries.,R3L7_LGCHEM_T1_STAGE2_20240207|R3L7_LGCHEM_T4_GREEN_PROXY_20240216,2,shadow-only
shadow_weight,customer_concentration_execution_risk,0,-2,-2,L&F worked tactically but later Tesla/4680 dependency created thesis-break watch; do not over-score customer quality alone.,Stage2 remains allowed but capped at Yellow unless margin bridge and order durability improve.,R3L7_LNF_T1_STAGE2_20230228,1,exploratory; narrative-only 2025 cut cannot change production
shadow_weight,price_only_4b_local_vs_full_window_split,single_proximity,local_and_full_split,+2,"EcoProBM/POSCO 4B rows were near full-window peaks, but Doosan 4B was local-good/full-cycle-early; split prevents premature exit.",4B classification separates full-window blowoff from policy-beta local overheat.,R3L7_EBM_T5_4B_20230726|R3L7_POSCOFM_T5_4B_20230725|R3L7_DFC_T5_4B_20200908,3,shadow-only overlay
```

## 27. Machine-Readable Rows

### 27.1 Case rows JSONL

```jsonl
{"row_type": "case", "case_id": "R3L7_EBM_247540_2023", "symbol": "247540", "company_name": "에코프로비엠", "round": "R3", "loop": "7", "sector": "2차전지·전기차·친환경", "case_type": "structural_success_and_4B", "primary_archetype": "BATTERY_MATERIALS_CATHODE_RERATING", "best_trigger": "R3L7_EBM_T1_STAGE2_20230126", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "Stage2 low score / high return: missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Stage2 captured the entire cathode rerating; Green worked but was late."}
{"row_type": "case", "case_id": "R3L7_POSCOFM_003670_2023", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R3", "loop": "7", "sector": "2차전지·전기차·친환경", "case_type": "structural_success_and_4B", "primary_archetype": "BATTERY_MATERIALS_CATHODE_SUPPLY_CONTRACT", "best_trigger": "R3L7_POSCOFM_T1_STAGE2_20230130", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "contract/backlog + customer quality should promote Stage2-Actionable", "price_source": "Songdaiki/stock-web", "notes": "Best early case for backlog/customer-quality gate."}
{"row_type": "case", "case_id": "R3L7_LNF_066970_2023", "symbol": "066970", "company_name": "엘앤에프", "round": "R3", "loop": "7", "sector": "2차전지·전기차·친환경", "case_type": "good_entry_later_thesis_break_narrative", "primary_archetype": "BATTERY_MATERIALS_CUSTOMER_CONCENTRATION_RISK", "best_trigger": "R3L7_LNF_T1_STAGE2_20230228", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "Stage2 worked tactically but customer concentration risk required 4C watch", "price_source": "Songdaiki/stock-web", "notes": "Later Tesla deal cut is narrative-only due no 180D forward window."}
{"row_type": "case", "case_id": "R3L7_LGCHEM_051910_2024", "symbol": "051910", "company_name": "LG화학", "round": "R3", "loop": "7", "sector": "2차전지·전기차·친환경", "case_type": "evidence_good_but_price_failed", "primary_archetype": "BATTERY_MATERIALS_CONTRACT_WITH_WEAK_RS", "best_trigger": "none_reject_watch_only", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "large contract alone should not promote without RS/margin bridge", "price_source": "Songdaiki/stock-web", "notes": "Counterexample for contract_score-only promotion."}
{"row_type": "case", "case_id": "R3L7_DFC_336260_2020", "symbol": "336260", "company_name": "두산퓨얼셀", "round": "R3", "loop": "7", "sector": "2차전지·전기차·친환경", "case_type": "policy_beta_success_then_late_green", "primary_archetype": "HYDROGEN_FUEL_CELL_POLICY_RERATING", "best_trigger": "R3L7_DFC_T1_POLICY_20200714", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "policy Stage2 beta worked; Green was very late", "price_source": "Songdaiki/stock-web", "notes": "Useful policy beta analog, but must remain separate from contract-backed battery materials."}
```

### 27.2 Trigger rows JSONL

```jsonl
{"row_type": "trigger", "trigger_id": "R3L7_EBM_T1_STAGE2_20230126", "case_id": "R3L7_EBM_247540_2023", "symbol": "247540", "company_name": "에코프로비엠", "round": "R3", "loop": "7", "sector": "2차전지·전기차·친환경", "primary_archetype": "BATTERY_MATERIALS_CATHODE_RERATING", "trigger_type": "Stage2", "trigger_date": "2023-01-26", "entry_date": "2023-01-26", "entry_price": 105400, "evidence_available_at_that_date": "양극재 업종 수급·수주 기대와 에코프로비엠 상대강도 재개. 아직 개별 대형 계약 confirm은 약함.", "evidence_source": "public news/sector reports; stock-web row confirms price anchor", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv", "profile_path": "atlas/symbol_profiles/247/247540.json", "MFE_30D_pct": 105.9, "MFE_90D_pct": 199.3, "MFE_180D_pct": 454.1, "MFE_1Y_pct": "unavailable_full_252D_not_extracted", "MFE_2Y_pct": "unavailable_full_504D_not_extracted", "MAE_30D_pct": -6.1, "MAE_90D_pct": -6.1, "MAE_180D_pct": -6.1, "MAE_1Y_pct": "unavailable_full_252D_not_extracted", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 584000, "drawdown_after_peak_pct": -67.9, "green_lateness_ratio": "0.233_vs_stage3_green_20230306", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": "not_applicable", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "excellent_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_profile_CA_dates_2022_only", "same_entry_group_id": "R3L7_EBM_20230126_105400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R3L7_EBM_T4_GREEN_20230306", "case_id": "R3L7_EBM_247540_2023", "symbol": "247540", "company_name": "에코프로비엠", "round": "R3", "loop": "7", "sector": "2차전지·전기차·친환경", "primary_archetype": "BATTERY_MATERIALS_CATHODE_RERATING", "trigger_type": "Stage3-Green", "trigger_date": "2023-03-06", "entry_date": "2023-03-06", "entry_price": 217000, "evidence_available_at_that_date": "3월 초 급등과 업종 전반 상대강도 확인. Stage2보다 confirmation은 강하지만 가격은 이미 2배 이상 상승.", "evidence_source": "public market/sector evidence; stock-web row confirms price anchor", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv", "profile_path": "atlas/symbol_profiles/247/247540.json", "MFE_30D_pct": 45.4, "MFE_90D_pct": 45.4, "MFE_180D_pct": 169.1, "MFE_1Y_pct": "unavailable_full_252D_not_extracted", "MFE_2Y_pct": "unavailable_full_504D_not_extracted", "MAE_30D_pct": -16.4, "MAE_90D_pct": -16.4, "MAE_180D_pct": -16.4, "MAE_1Y_pct": "unavailable_full_252D_not_extracted", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 584000, "drawdown_after_peak_pct": -67.9, "green_lateness_ratio": 0.233, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": "not_applicable", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_but_late_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_profile_CA_dates_2022_only", "same_entry_group_id": "R3L7_EBM_20230306_217000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R3L7_EBM_T5_4B_20230726", "case_id": "R3L7_EBM_247540_2023", "symbol": "247540", "company_name": "에코프로비엠", "round": "R3", "loop": "7", "sector": "2차전지·전기차·친환경", "primary_archetype": "BATTERY_MATERIALS_CATHODE_RERATING", "trigger_type": "Stage4B", "trigger_date": "2023-07-26", "entry_date": "2023-07-26", "entry_price": 455000, "evidence_available_at_that_date": "수직 급등, intraday high 584,000 후 종가 455,000으로 변동성 blow-off. 비가격 evidence보다 수급/밸류에이션 과열 중심.", "evidence_source": "stock-web OHLC + public market context", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv", "profile_path": "atlas/symbol_profiles/247/247540.json", "MFE_30D_pct": 28.4, "MFE_90D_pct": 28.4, "MFE_180D_pct": 28.4, "MFE_1Y_pct": "unavailable_full_252D_not_extracted", "MFE_2Y_pct": "unavailable_full_504D_not_extracted", "MAE_30D_pct": -34.4, "MAE_90D_pct": -58.8, "MAE_180D_pct": -58.8, "MAE_1Y_pct": "unavailable_full_252D_not_extracted", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 584000, "drawdown_after_peak_pct": -67.9, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.73, "four_b_full_window_peak_proximity": 0.73, "four_b_timing_verdict": "good_local_and_full_window_4B_watch_timing", "four_b_evidence_type": "price_only|valuation_blowoff|positioning_overheat", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_watch_success", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_profile_CA_dates_2022_only", "same_entry_group_id": "R3L7_EBM_20230726_455000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R3L7_POSCOFM_T1_STAGE2_20230130", "case_id": "R3L7_POSCOFM_003670_2023", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R3", "loop": "7", "sector": "2차전지·전기차·친환경", "primary_archetype": "BATTERY_MATERIALS_CATHODE_SUPPLY_CONTRACT", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-01-30", "entry_date": "2023-01-30", "entry_price": 218000, "evidence_available_at_that_date": "삼성SDI향 장기 양극재 공급 계약 보도/공시로 backlog visibility와 customer quality가 동시에 닫힘.", "evidence_source": "DART/company announcement; secondary public summaries note ~100T KRW cathode orders in 2023", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv", "profile_path": "atlas/symbol_profiles/003/003670.json", "MFE_30D_pct": 23.9, "MFE_90D_pct": 93.8, "MFE_180D_pct": 218.3, "MFE_1Y_pct": "unavailable_full_252D_not_extracted", "MFE_2Y_pct": "unavailable_full_504D_not_extracted", "MAE_30D_pct": -3.0, "MAE_90D_pct": -3.0, "MAE_180D_pct": -3.0, "MAE_1Y_pct": "unavailable_full_252D_not_extracted", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 694000, "drawdown_after_peak_pct": -66.5, "green_lateness_ratio": "0.261_vs_stage3_green_20230414", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": "not_applicable", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "excellent_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_profile_CA_dates_2021_only", "same_entry_group_id": "R3L7_POSCOFM_20230130_218000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R3L7_POSCOFM_T4_GREEN_20230414", "case_id": "R3L7_POSCOFM_003670_2023", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R3", "loop": "7", "sector": "2차전지·전기차·친환경", "primary_archetype": "BATTERY_MATERIALS_CATHODE_SUPPLY_CONTRACT", "trigger_type": "Stage3-Green", "trigger_date": "2023-04-14", "entry_date": "2023-04-14", "entry_price": 342500, "evidence_available_at_that_date": "계약 backlog와 주가 상대강도가 함께 확인된 구간. 다만 Stage2 대비 진입가가 57% 높아짐.", "evidence_source": "public market/contract follow-through; stock-web row confirms price anchor", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv", "profile_path": "atlas/symbol_profiles/003/003670.json", "MFE_30D_pct": 23.4, "MFE_90D_pct": 102.6, "MFE_180D_pct": 102.6, "MFE_1Y_pct": "unavailable_full_252D_not_extracted", "MFE_2Y_pct": "unavailable_full_504D_not_extracted", "MAE_30D_pct": -14.7, "MAE_90D_pct": -14.7, "MAE_180D_pct": -32.1, "MAE_1Y_pct": "unavailable_full_252D_not_extracted", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 694000, "drawdown_after_peak_pct": -66.5, "green_lateness_ratio": 0.262, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": "not_applicable", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_but_late_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_profile_CA_dates_2021_only", "same_entry_group_id": "R3L7_POSCOFM_20230414_342500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R3L7_POSCOFM_T5_4B_20230725", "case_id": "R3L7_POSCOFM_003670_2023", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R3", "loop": "7", "sector": "2차전지·전기차·친환경", "primary_archetype": "BATTERY_MATERIALS_CATHODE_SUPPLY_CONTRACT", "trigger_type": "Stage4B", "trigger_date": "2023-07-25", "entry_date": "2023-07-25", "entry_price": 598000, "evidence_available_at_that_date": "계약 내러티브가 주가에 과도하게 압축 반영된 구간. 다음날 high 694,000 후 장중 급락.", "evidence_source": "stock-web OHLC + public market context", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv", "profile_path": "atlas/symbol_profiles/003/003670.json", "MFE_30D_pct": 16.1, "MFE_90D_pct": 16.1, "MFE_180D_pct": 16.1, "MFE_1Y_pct": "unavailable_full_252D_not_extracted", "MFE_2Y_pct": "unavailable_full_504D_not_extracted", "MAE_30D_pct": -33.1, "MAE_90D_pct": -61.1, "MAE_180D_pct": -61.1, "MAE_1Y_pct": "unavailable_full_252D_not_extracted", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 694000, "drawdown_after_peak_pct": -66.5, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.798, "four_b_full_window_peak_proximity": 0.798, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": "valuation_blowoff|positioning_overheat", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_watch_success", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_profile_CA_dates_2021_only", "same_entry_group_id": "R3L7_POSCOFM_20230725_598000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R3L7_LNF_T1_STAGE2_20230228", "case_id": "R3L7_LNF_066970_2023", "symbol": "066970", "company_name": "엘앤에프", "round": "R3", "loop": "7", "sector": "2차전지·전기차·친환경", "primary_archetype": "BATTERY_MATERIALS_CUSTOMER_CONCENTRATION_RISK", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-02-28", "entry_date": "2023-02-28", "entry_price": 262000, "evidence_available_at_that_date": "Tesla향 high-nickel cathode supply 기대가 공개되고 주가가 장중 285,000까지 반응. 고객 품질은 강하지만 고객/4680 ramp concentration risk가 남음.", "evidence_source": "Reuters retrospective confirms 2023 Tesla-affiliate high-nickel cathode deal; DART/company announcement date treated as 2023-02-28", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv", "profile_path": "atlas/symbol_profiles/066/066970.json", "MFE_30D_pct": 33.4, "MFE_90D_pct": 33.4, "MFE_180D_pct": 33.4, "MFE_1Y_pct": "unavailable_full_252D_not_extracted", "MFE_2Y_pct": "unavailable_full_504D_not_extracted", "MAE_30D_pct": -16.4, "MAE_90D_pct": -16.4, "MAE_180D_pct": -51.2, "MAE_1Y_pct": "unavailable_full_252D_not_extracted", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-03", "peak_price": 349500, "drawdown_after_peak_pct": -63.4, "green_lateness_ratio": "0.400_vs_stage3_green_20230327", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": "not_applicable", "four_c_protection_label": "2025_contract_cut_is_narrative_only_no_forward_180D", "trigger_outcome_label": "good_entry_with_later_thesis_risk", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_profile_CA_dates_2021_only", "same_entry_group_id": "R3L7_LNF_20230228_262000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R3L7_LNF_T4_GREEN_20230327", "case_id": "R3L7_LNF_066970_2023", "symbol": "066970", "company_name": "엘앤에프", "round": "R3", "loop": "7", "sector": "2차전지·전기차·친환경", "primary_archetype": "BATTERY_MATERIALS_CUSTOMER_CONCENTRATION_RISK", "trigger_type": "Stage3-Green", "trigger_date": "2023-03-27", "entry_date": "2023-03-27", "entry_price": 297000, "evidence_available_at_that_date": "Tesla 계약 내러티브가 상대강도와 결합된 확인 구간. 그러나 entry가 2월 28일 대비 늦어지고 downside가 커짐.", "evidence_source": "stock-web OHLC + public contract context", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv", "profile_path": "atlas/symbol_profiles/066/066970.json", "MFE_30D_pct": 17.7, "MFE_90D_pct": 17.7, "MFE_180D_pct": 17.7, "MFE_1Y_pct": "unavailable_full_252D_not_extracted", "MFE_2Y_pct": "unavailable_full_504D_not_extracted", "MAE_30D_pct": -13.1, "MAE_90D_pct": -25.6, "MAE_180D_pct": -56.9, "MAE_1Y_pct": "unavailable_full_252D_not_extracted", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-03", "peak_price": 349500, "drawdown_after_peak_pct": -63.4, "green_lateness_ratio": 0.4, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": "not_applicable", "four_c_protection_label": "2025_contract_cut_is_narrative_only_no_forward_180D", "trigger_outcome_label": "late_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_profile_CA_dates_2021_only", "same_entry_group_id": "R3L7_LNF_20230327_297000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R3L7_LGCHEM_T1_STAGE2_20240207", "case_id": "R3L7_LGCHEM_051910_2024", "symbol": "051910", "company_name": "LG화학", "round": "R3", "loop": "7", "sector": "2차전지·전기차·친환경", "primary_archetype": "BATTERY_MATERIALS_CONTRACT_WITH_WEAK_RS", "trigger_type": "Stage2", "trigger_date": "2024-02-07", "entry_date": "2024-02-07", "entry_price": 463500, "evidence_available_at_that_date": "GM향 대규모 cathode material supply deal. 계약 크기는 크지만 EV 수요 둔화·화학 본업/마진 약화와 상대강도 부족이 남음.", "evidence_source": "Investopedia/Reuters syndicated report on GM-LG Chem $18.8B/25T KRW cathode deal", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv", "profile_path": "atlas/symbol_profiles/051/051910.json", "MFE_30D_pct": 12.2, "MFE_90D_pct": 12.2, "MFE_180D_pct": 12.2, "MFE_1Y_pct": "unavailable_full_252D_not_extracted", "MFE_2Y_pct": "unavailable_full_504D_not_extracted", "MAE_30D_pct": -7.2, "MAE_90D_pct": -24.5, "MAE_180D_pct": -43.1, "MAE_1Y_pct": "unavailable_full_252D_not_extracted", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-19", "peak_price": 520000, "drawdown_after_peak_pct": -49.3, "green_lateness_ratio": "not_applicable_low_RS_no_confirmed_green", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": "not_applicable", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "evidence_good_but_price_failed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_profile_no_CA", "same_entry_group_id": "R3L7_LGCHEM_20240207_463500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R3L7_LGCHEM_T4_GREEN_PROXY_20240216", "case_id": "R3L7_LGCHEM_051910_2024", "symbol": "051910", "company_name": "LG화학", "round": "R3", "loop": "7", "sector": "2차전지·전기차·친환경", "primary_archetype": "BATTERY_MATERIALS_CONTRACT_WITH_WEAK_RS", "trigger_type": "Stage3-Green-proxy", "trigger_date": "2024-02-16", "entry_date": "2024-02-16", "entry_price": 504000, "evidence_available_at_that_date": "계약 뉴스 이후 단기 고점권에서 늦은 confirmation이 붙은 구간. 이후 forward return이 낮고 MAE가 커 false-positive guardrail 필요.", "evidence_source": "stock-web OHLC + GM contract context", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv", "profile_path": "atlas/symbol_profiles/051/051910.json", "MFE_30D_pct": 3.2, "MFE_90D_pct": 3.2, "MFE_180D_pct": 3.2, "MFE_1Y_pct": "unavailable_full_252D_not_extracted", "MFE_2Y_pct": "unavailable_full_504D_not_extracted", "MAE_30D_pct": -21.6, "MAE_90D_pct": -30.6, "MAE_180D_pct": -47.7, "MAE_1Y_pct": "unavailable_full_252D_not_extracted", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-19", "peak_price": 520000, "drawdown_after_peak_pct": -49.3, "green_lateness_ratio": "not_applicable_low_RS_no_confirmed_green", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": "not_applicable", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "false_positive_score", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_profile_no_CA", "same_entry_group_id": "R3L7_LGCHEM_20240216_504000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R3L7_DFC_T1_POLICY_20200714", "case_id": "R3L7_DFC_336260_2020", "symbol": "336260", "company_name": "두산퓨얼셀", "round": "R3", "loop": "7", "sector": "2차전지·전기차·친환경", "primary_archetype": "HYDROGEN_FUEL_CELL_POLICY_RERATING", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-07-14", "entry_date": "2020-07-14", "entry_price": 36450, "evidence_available_at_that_date": "Korean Green New Deal announced; hydrogen/fuel-cell policy theme became publicly tradable. Company-specific earnings gate was not closed.", "evidence_source": "Korean Green New Deal public policy announcement; stock-web row confirms price anchor", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/336/336260/2020.csv", "profile_path": "atlas/symbol_profiles/336/336260.json", "MFE_30D_pct": 38.0, "MFE_90D_pct": 71.5, "MFE_180D_pct": 79.4, "MFE_1Y_pct": "unavailable_full_252D_not_extracted", "MFE_2Y_pct": "unavailable_full_504D_not_extracted", "MAE_30D_pct": -3.4, "MAE_90D_pct": -3.4, "MAE_180D_pct": -3.4, "MAE_1Y_pct": "unavailable_full_252D_not_extracted", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-02-15", "peak_price": 65400, "drawdown_after_peak_pct": -31.0, "green_lateness_ratio": "0.789_vs_stage3_green_20200907", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": "not_applicable", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_entry_policy_beta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_profile_no_CA_candidate", "same_entry_group_id": "R3L7_DFC_20200714_36450", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R3L7_DFC_T4_GREEN_20200907", "case_id": "R3L7_DFC_336260_2020", "symbol": "336260", "company_name": "두산퓨얼셀", "round": "R3", "loop": "7", "sector": "2차전지·전기차·친환경", "primary_archetype": "HYDROGEN_FUEL_CELL_POLICY_RERATING", "trigger_type": "Stage3-Green-proxy", "trigger_date": "2020-09-07", "entry_date": "2020-09-07", "entry_price": 59300, "evidence_available_at_that_date": "수소 정책 테마와 가격 상대강도가 절정에 가까워진 구간. Stage2 대비 upside 대부분이 이미 진행.", "evidence_source": "Korean Green New Deal public policy + stock-web OHLC", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/336/336260/2020.csv", "profile_path": "atlas/symbol_profiles/336/336260.json", "MFE_30D_pct": 5.4, "MFE_90D_pct": 5.4, "MFE_180D_pct": 10.3, "MFE_1Y_pct": "unavailable_full_252D_not_extracted", "MFE_2Y_pct": "unavailable_full_504D_not_extracted", "MAE_30D_pct": -38.1, "MAE_90D_pct": -40.1, "MAE_180D_pct": -23.9, "MAE_1Y_pct": "unavailable_full_252D_not_extracted", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-02-15", "peak_price": 65400, "drawdown_after_peak_pct": -31.0, "green_lateness_ratio": 0.789, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": "not_applicable", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_entry_false_positive_risk", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_profile_no_CA_candidate", "same_entry_group_id": "R3L7_DFC_20200907_59300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
{"row_type": "trigger", "trigger_id": "R3L7_DFC_T5_4B_20200908", "case_id": "R3L7_DFC_336260_2020", "symbol": "336260", "company_name": "두산퓨얼셀", "round": "R3", "loop": "7", "sector": "2차전지·전기차·친환경", "primary_archetype": "HYDROGEN_FUEL_CELL_POLICY_RERATING", "trigger_type": "Stage4B", "trigger_date": "2020-09-08", "entry_date": "2020-09-08", "entry_price": 56400, "evidence_available_at_that_date": "전일 high 59,300, 당일 high 62,500 후 종가 56,400. 정책 beta가 가격으로 먼저 과열된 4B-watch.", "evidence_source": "stock-web OHLC + policy theme context", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/336/336260/2020.csv", "profile_path": "atlas/symbol_profiles/336/336260.json", "MFE_30D_pct": 10.8, "MFE_90D_pct": 10.8, "MFE_180D_pct": 16.0, "MFE_1Y_pct": "unavailable_full_252D_not_extracted", "MFE_2Y_pct": "unavailable_full_504D_not_extracted", "MAE_30D_pct": -34.9, "MAE_90D_pct": -37.0, "MAE_180D_pct": -19.9, "MAE_1Y_pct": "unavailable_full_252D_not_extracted", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-02-15", "peak_price": 65400, "drawdown_after_peak_pct": -31.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.766, "four_b_full_window_peak_proximity": 0.689, "four_b_timing_verdict": "price_only_local_4B_good_but_full_window_somewhat_early", "four_b_evidence_type": "price_only|positioning_overheat|policy_event_premium", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_local_success_full_cycle_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_profile_no_CA_candidate", "same_entry_group_id": "R3L7_DFC_20200908_56400", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable"}
```

### 27.3 Score simulation rows JSONL

```jsonl
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R3L7_EBM_247540_2023", "trigger_id": "R3L7_EBM_T1_STAGE2_20230126", "symbol": "247540", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 7, "policy_or_regulatory_score": 3, "valuation_repricing_score": 4, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 44.7, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 4, "relative_strength_score": 8, "customer_quality_score": 7, "policy_or_regulatory_score": 3, "valuation_repricing_score": 5, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 47.1, "stage_label_after": "Stage2-Actionable", "changed_components": ["relative_strength_score", "valuation_repricing_score"], "component_delta_explanation": "shadow profile increases early RS/backlog/customer-quality value, but penalizes weak margin bridge and execution/customer concentration risk.", "selected_by_profile": true, "MFE_90D_pct": 199.3, "MAE_90D_pct": -6.1, "score_return_alignment_label": "score_low_return_high_missed_structural"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R3L7_EBM_247540_2023", "trigger_id": "R3L7_EBM_T4_GREEN_20230306", "symbol": "247540", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 6, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 10, "customer_quality_score": 7, "policy_or_regulatory_score": 3, "valuation_repricing_score": 6, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 53.6, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 6, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 10, "customer_quality_score": 7, "policy_or_regulatory_score": 3, "valuation_repricing_score": 6, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53.6, "stage_label_after": "Stage3-Yellow", "changed_components": [], "component_delta_explanation": "shadow profile increases early RS/backlog/customer-quality value, but penalizes weak margin bridge and execution/customer concentration risk.", "selected_by_profile": false, "MFE_90D_pct": 45.4, "MAE_90D_pct": -16.4, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R3L7_POSCOFM_003670_2023", "trigger_id": "R3L7_POSCOFM_T1_STAGE2_20230130", "symbol": "003670", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 6, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 51.9, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 9, "backlog_visibility_score": 9, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 7, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 57.9, "stage_label_after": "Stage3-Yellow", "changed_components": ["contract_score", "backlog_visibility_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score"], "component_delta_explanation": "shadow profile increases early RS/backlog/customer-quality value, but penalizes weak margin bridge and execution/customer concentration risk.", "selected_by_profile": true, "MFE_90D_pct": 93.8, "MAE_90D_pct": -3.0, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R3L7_POSCOFM_003670_2023", "trigger_id": "R3L7_POSCOFM_T4_GREEN_20230414", "symbol": "003670", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 9, "backlog_visibility_score": 9, "margin_bridge_score": 6, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 64.4, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 9, "backlog_visibility_score": 9, "margin_bridge_score": 6, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 64.4, "stage_label_after": "Stage3-Green", "changed_components": [], "component_delta_explanation": "shadow profile increases early RS/backlog/customer-quality value, but penalizes weak margin bridge and execution/customer concentration risk.", "selected_by_profile": false, "MFE_90D_pct": 102.6, "MAE_90D_pct": -14.7, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R3L7_LNF_066970_2023", "trigger_id": "R3L7_LNF_T1_STAGE2_20230228", "symbol": "066970", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 7, "backlog_visibility_score": 6, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 8, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 5, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 46.0, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 7, "backlog_visibility_score": 6, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 8, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 5, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 44.6, "stage_label_after": "Stage2-Actionable", "changed_components": ["legal_or_contract_risk_score"], "component_delta_explanation": "shadow profile increases early RS/backlog/customer-quality value, but penalizes weak margin bridge and execution/customer concentration risk.", "selected_by_profile": true, "MFE_90D_pct": 33.4, "MAE_90D_pct": -16.4, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R3L7_LNF_066970_2023", "trigger_id": "R3L7_LNF_T4_GREEN_20230327", "symbol": "066970", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 7, "backlog_visibility_score": 6, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 9, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 5, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 48.4, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 7, "backlog_visibility_score": 6, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 9, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 6, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 46.3, "stage_label_after": "Stage2-Actionable", "changed_components": ["execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "shadow profile increases early RS/backlog/customer-quality value, but penalizes weak margin bridge and execution/customer concentration risk.", "selected_by_profile": false, "MFE_90D_pct": 17.7, "MAE_90D_pct": -25.6, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R3L7_LGCHEM_051910_2024", "trigger_id": "R3L7_LGCHEM_T1_STAGE2_20240207", "symbol": "051910", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 9, "backlog_visibility_score": 8, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 2, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 37.8, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 2, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 1, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 33.5, "stage_label_after": "Stage2", "changed_components": ["contract_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "shadow profile increases early RS/backlog/customer-quality value, but penalizes weak margin bridge and execution/customer concentration risk.", "selected_by_profile": false, "MFE_90D_pct": 12.2, "MAE_90D_pct": -24.5, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R3L7_LGCHEM_051910_2024", "trigger_id": "R3L7_LGCHEM_T4_GREEN_PROXY_20240216", "symbol": "051910", "trigger_type": "Stage3-Green-proxy", "raw_component_scores_before": {"contract_score": 9, "backlog_visibility_score": 8, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 5, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 3, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 41.4, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 2, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 35.2, "stage_label_after": "Stage2", "changed_components": ["contract_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "shadow profile increases early RS/backlog/customer-quality value, but penalizes weak margin bridge and execution/customer concentration risk.", "selected_by_profile": false, "MFE_90D_pct": 3.2, "MAE_90D_pct": -30.6, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R3L7_DFC_336260_2020", "trigger_id": "R3L7_DFC_T1_POLICY_20200714", "symbol": "336260", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 3, "margin_bridge_score": 3, "revision_score": 2, "relative_strength_score": 7, "customer_quality_score": 4, "policy_or_regulatory_score": 9, "valuation_repricing_score": 4, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 38.0, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 3, "margin_bridge_score": 3, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 4, "policy_or_regulatory_score": 9, "valuation_repricing_score": 5, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 40.4, "stage_label_after": "Stage2", "changed_components": ["relative_strength_score", "valuation_repricing_score"], "component_delta_explanation": "shadow profile increases early RS/backlog/customer-quality value, but penalizes weak margin bridge and execution/customer concentration risk.", "selected_by_profile": true, "MFE_90D_pct": 71.5, "MAE_90D_pct": -3.4, "score_return_alignment_label": "score_low_return_high_missed_structural"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R3L7_DFC_336260_2020", "trigger_id": "R3L7_DFC_T4_GREEN_20200907", "symbol": "336260", "trigger_type": "Stage3-Green-proxy", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 3, "margin_bridge_score": 3, "revision_score": 2, "relative_strength_score": 10, "customer_quality_score": 4, "policy_or_regulatory_score": 9, "valuation_repricing_score": 6, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 43.3, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 3, "margin_bridge_score": 3, "revision_score": 2, "relative_strength_score": 10, "customer_quality_score": 4, "policy_or_regulatory_score": 9, "valuation_repricing_score": 6, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 42.6, "stage_label_after": "Stage2-Actionable", "changed_components": ["execution_risk_score"], "component_delta_explanation": "shadow profile increases early RS/backlog/customer-quality value, but penalizes weak margin bridge and execution/customer concentration risk.", "selected_by_profile": false, "MFE_90D_pct": 5.4, "MAE_90D_pct": -40.1, "score_return_alignment_label": "score_mid_return_low_watch_only"}
```

### 27.4 Profile comparison rows CSV

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,5,5,5,34.9,17.7,-25.5,-25.6,60.6,-35.4,40.0,80.0,40.0,2,4,0.497,not_applicable,not_applicable,reference; often too late and high MAE
profile_comparison,stage2_actionable_early_evidence_plus_with_guardrails,5,4,4,99.5,82.7,-7.2,-4.8,196.3,-15.9,100.0,25.0,0.0,0,0,0.0,not_applicable,not_applicable,best shadow profile: improves upside capture and rejects LG Chem contract-only false positive
profile_comparison,stage3_yellow_entry_relaxed,5,mixed,mixed,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,"useful for POSCO/EcoPro, but weaker than Stage2-Actionable with guardrails"
profile_comparison,green_confirmation_timing_relaxed,5,mixed,mixed,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,"partly improves lateness, but still misses earliest rerating legs"
profile_comparison,four_b_peak_timing_tuned,5,mixed,mixed,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,validates non-price/valuation 4B watch; not an entry profile
profile_comparison,four_c_thesis_break_earlier,5,mixed,mixed,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,see narrative,not validated for hard gate; L&F 2025 cut narrative-only
```

### 27.5 Shadow weight rows CSV

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_contract_backlog_customer_quality,0,+3,+3,POSCO FutureM Stage2-Actionable and EcoProBM early Stage2 produced much higher MFE90 with shallow MAE than later Green.,baseline avg MFE90 34.9 / avg MAE90 -25.5 vs after selected avg MFE90 99.5 / avg MAE90 -7.2,R3L7_POSCOFM_T1_STAGE2_20230130|R3L7_EBM_T1_STAGE2_20230126,2,shadow-only; not production
shadow_weight,relative_strength_early_confirmation,0,+2,+2,Early RS helped distinguish EcoProBM/POSCO/Doosan winners from LG Chem contract-only case.,missed_structural_count reduced from 2 to 0 in selected profile while false-positive avoided by guardrails.,R3L7_EBM_T1_STAGE2_20230126|R3L7_DFC_T1_POLICY_20200714,2,shadow-only
shadow_weight,contract_only_without_margin_or_RS_guardrail,0,-3,-3,LG Chem had large GM contract but weak RS/margin bridge and produced low MFE90 with deep MAE90.,rejecting LG Chem improves after-profile false_positive_rate from 40% to 0% among selected entries.,R3L7_LGCHEM_T1_STAGE2_20240207|R3L7_LGCHEM_T4_GREEN_PROXY_20240216,2,shadow-only
shadow_weight,customer_concentration_execution_risk,0,-2,-2,L&F worked tactically but later Tesla/4680 dependency created thesis-break watch; do not over-score customer quality alone.,Stage2 remains allowed but capped at Yellow unless margin bridge and order durability improve.,R3L7_LNF_T1_STAGE2_20230228,1,exploratory; narrative-only 2025 cut cannot change production
shadow_weight,price_only_4b_local_vs_full_window_split,single_proximity,local_and_full_split,+2,"EcoProBM/POSCO 4B rows were near full-window peaks, but Doosan 4B was local-good/full-cycle-early; split prevents premature exit.",4B classification separates full-window blowoff from policy-beta local overheat.,R3L7_EBM_T5_4B_20230726|R3L7_POSCOFM_T5_4B_20230725|R3L7_DFC_T5_4B_20200908,3,shadow-only overlay
```

### 27.6 Optimization decision rows JSONL

```jsonl
{"row_type": "optimization_decision", "decision_id": "R3L7_DECISION_001", "hypothesis": "Contract+backlog+customer quality with early RS should promote Stage2 to Actionable/Yellow before Green.", "tested_trigger_ids": ["R3L7_EBM_T1_STAGE2_20230126", "R3L7_POSCOFM_T1_STAGE2_20230130"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_guardrails", "backtest_result_summary": "Early triggers captured 199.3% and 93.8% MFE90 with -6.1% and -3.0% MAE90.", "accepted_or_rejected": "accepted", "delta_magnitude": "+3", "why_not_larger_delta": "only two clean contract/backlog structural cases in this round; R4/R5 counterexamples still needed", "risks": "over-promoting commodity-price beta without margin bridge", "next_validation_needed": "Find failed cathode contract/backlog cases from 2021-2024."}
{"row_type": "optimization_decision", "decision_id": "R3L7_DECISION_002", "hypothesis": "Large contract alone should not produce Green without RS and margin bridge.", "tested_trigger_ids": ["R3L7_LGCHEM_T1_STAGE2_20240207", "R3L7_LGCHEM_T4_GREEN_PROXY_20240216"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_guardrails", "backtest_result_summary": "LG Chem contract row had only 12.2% MFE90 and -24.5% MAE90; late Green proxy had 3.2% MFE90 and -30.6% MAE90.", "accepted_or_rejected": "accepted", "delta_magnitude": "-3", "why_not_larger_delta": "single clean counterexample, but strong drawdown evidence", "risks": "may reject slow-burn large-cap recoveries", "next_validation_needed": "Retest with LGES and Samsung SDI contract events."}
{"row_type": "optimization_decision", "decision_id": "R3L7_DECISION_003", "hypothesis": "4B timing must split local vs full-window proximity.", "tested_trigger_ids": ["R3L7_EBM_T5_4B_20230726", "R3L7_POSCOFM_T5_4B_20230725", "R3L7_DFC_T5_4B_20200908"], "baseline_profile": "baseline_current_proxy", "selected_profile": "four_b_peak_timing_tuned", "backtest_result_summary": "EcoproBM and POSCO were near full-window peaks; Doosan was local-good but full-window early.", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "4B evidence partly price-only; need non-price 4B evidence in later rounds", "risks": "price-only 4B can overfit blowoff tops", "next_validation_needed": "Add valuation/revision slowdown evidence checks."}
```

### 27.7 Narrative-only rows JSONL

```jsonl
{"row_type": "narrative_only", "case_id": "R3L7_LNF_066970_2025_CUT", "symbol": "066970", "reason": "Reuters-reported 2025 Tesla deal value cut occurred after stock-web max_date forward-window eligibility; no 180D available.", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
```

### 27.8 Aggregate metric rows CSV

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,below_entry_90D_rate,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,2,2,105.8,105.8,-15.3,-15.3,233.2,-24.6,100.0,mixed_or_not_applicable,overlay_only,overlay_only,representative rows only; duplicate/overlay rows excluded
aggregate_metric,Stage2-Actionable,3,3,66.2,71.5,-7.6,-3.4,110.4,-19.2,100.0,mixed_or_not_applicable,overlay_only,overlay_only,representative rows only; duplicate/overlay rows excluded
aggregate_metric,Stage3-Green,3,3,55.2,45.4,-18.9,-16.4,96.5,-35.1,100.0,mixed_or_not_applicable,overlay_only,overlay_only,representative rows only; duplicate/overlay rows excluded
aggregate_metric,Stage3-Green-proxy,2,2,4.3,4.3,-35.4,-35.4,6.8,-35.8,100.0,mixed_or_not_applicable,overlay_only,overlay_only,representative rows only; duplicate/overlay rows excluded
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
completed_round = R3
completed_loop = 7
next_round = R4
next_loop = 7
next_sector = 소재·스프레드·전략자원
```

## 30. Source Notes

- stock-web is raw/unadjusted FinanceData/marcap; this MD blocks profile corporate-action candidate windows by default.
- This R3 MD uses 30D/90D/180D only for score-weight calibration. 1Y/2Y values are not used where marked unavailable.
- Evidence sources were separated from price source. Price rows are from stock-web; evidence notes are public contract/policy/company context.
- This is historical calibration research, not a live recommendation, not a watchlist, and not a production scoring change.
