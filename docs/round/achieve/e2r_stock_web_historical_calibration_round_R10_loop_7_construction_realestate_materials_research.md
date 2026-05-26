# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata

```text
research_session = historical_calibration_after_stock_web_ohlc_breakthrough
round = R10
loop = 5
sector = 건설·부동산·건자재
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough
live_candidate_mode = false
current_stock_discovery_allowed = false
stock_agent_repo_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
output_format = one_standalone_markdown_file
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

이번 MD는 현재 추천/스캔이 아니라 과거 trigger-level calibration이다. `stock_agent` 레포는 열지 않았고, 가격 소스인 `Songdaiki/stock-web`만 price atlas로 사용했다.

## 1. Round Scope

R10은 건설·부동산·건자재 라운드다. 이번 loop는 성공형 한샘, 이벤트 프리미엄형 현대건설, 품질/안전 4C형 GS건설·HDC현대산업개발을 섞었다. 핵심 질문은 세 가지다.

1. 리모델링/건자재 수요처럼 실적이 뒤따르는 경우 Stage2를 너무 늦게 잡는가.
2. NEOM 같은 대형 정책/프로젝트 narrative에서 가격만 먼저 뜬 Green은 false-positive가 되는가.
3. 건설 품질·안전 사고는 4C를 비용 확정 이후가 아니라 사고 발생 시점부터 watch해야 하는가.

## 2. Stock-Web OHLC Input / Price Source Validation

|field|value|
|---|---|
|source|Songdaiki/stock-web|
|source_url|https://github.com/Songdaiki/stock-web|
|source_basis|FinanceData/marcap transformed into assistant-readable symbol-year CSV shards|
|price_basis|tradable_raw|
|price_adjustment_status|raw_unadjusted_marcap|
|min_date|1995-05-02|
|max_date|2026-02-20|
|tradable_row_count|14354401|
|raw_row_count|15214118|
|symbol_count|5414|
|active_like_symbol_count|2868|
|inactive_or_delisted_like_symbol_count|2546|
|calibration_shard_root|atlas/ohlcv_tradable_by_symbol_year|
|raw_shard_root|atlas/ohlcv_raw_by_symbol_year|

Schema mapping used: `d,o,h,l,c,v,a,mc,s,m = date,open,high,low,close,volume,amount,market_cap,shares,market`.

## 3. Historical Eligibility Gate

All selected trigger rows used stock-web tradable shards and had at least 180 forward tradable days available before manifest max date. 30D/90D/180D MFE and MAE were calculated from high/low after entry close. 1Y/2Y values are included where the observed stock-web window allowed it; market and sector relative return fields are marked `unavailable` because this round did not add external index shards.

## 4. Canonical Archetypes Tested

|archetype|mechanism|case|
|---|---|---|
|INTERIOR_REMODELING_STAY_HOME_EPS_RERATING|consumer time-at-home demand → remodeling/order mix → OP revision → rerating|한샘|
|MEGA_PROJECT_NEOM_POLICY_EVENT_PREMIUM|policy/project narrative → relative strength → contract/margin gate missing → event premium fade|현대건설|
|CONSTRUCTION_QUALITY_SAFETY_THESIS_BREAK|quality accident → legal/regulatory/cost risk → brand/trust damage → 4C|GS건설|
|BRAND_TRUST_CONSTRUCTION_ACCIDENT_THESIS_BREAK|fatal construction accident → license/sanction/rebuild risk → thesis break|HDC현대산업개발|

## 5. Case Selection Summary

|case_id|symbol|company|case_type|archetype|best_trigger|
|---|---|---|---|---|---|
|R10L5_CASE01_HANSEM_COVID_REMODELING|009240|한샘|structural_success|INTERIOR_REMODELING_STAY_HOME_EPS_RERATING|R10L5_C01_T1_STAGE2_EARLY_REMODELING_DEMAND|
|R10L5_CASE02_HYUNDAI_CONSTRUCTION_NEOM_EVENT|000720|현대건설|event_premium_failed_rerating|MEGA_PROJECT_NEOM_POLICY_EVENT_PREMIUM|R10L5_C02_T1_STAGE2_NEOM_AWARENESS|
|R10L5_CASE03_GS_CONSTRUCTION_QUALITY_4C|006360|GS건설|hard_4c_thesis_break|CONSTRUCTION_QUALITY_SAFETY_THESIS_BREAK|R10L5_C03_T1_STAGE2_QUALITY_INCIDENT|
|R10L5_CASE04_HDC_QUALITY_4C|294870|HDC현대산업개발|hard_4c_thesis_break|BRAND_TRUST_CONSTRUCTION_ACCIDENT_THESIS_BREAK|R10L5_C04_T1_HWAJEONG_COLLAPSE_4C|

## 6. Evidence Source Map

|case|evidence anchors|source notes|
|---|---|---|
|한샘|2020 stay-home remodeling demand, furniture/interior demand, relative strength; 2021 control-premium event|Hanssem company profile and public Korea press/analyst coverage; stock-web 009240 rows|
|현대건설|2022 Saudi/NEOM expectation, Crown Prince visit/theme flow, missing hard contract/margin bridge|public Korea press/analyst coverage; stock-web 000720 rows|
|GS건설|2023 Geomdan parking-garage collapse, investigation flow, full reconstruction/cost recognition|public Korea press/MOLIT investigation flow; stock-web 006360 rows|
|HDC현대산업개발|2022 Gwangju Hwajeong I-Park collapse, government investigation, sanction risk|Gwangju Hwajeong I-Park public incident references; stock-web 294870 rows|

## 7. Price Data Source Map

|symbol|company|profile_path|tradable shard examples|corporate action window status|
|---|---|---|---|---|
|009240|한샘|atlas/symbol_profiles/009/009240.json|atlas/ohlcv_tradable_by_symbol_year/009/009240/2020.csv; 2021.csv|clean; profile has no corporate-action candidates in tested window|
|000720|현대건설|atlas/symbol_profiles/000/000720.json|atlas/ohlcv_tradable_by_symbol_year/000/000720/2022.csv; 2023.csv|old corporate-action candidates only; no tested-window contamination|
|006360|GS건설|atlas/symbol_profiles/006/006360.json|atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv|old 2014 candidate only; no tested-window contamination|
|294870|HDC현대산업개발|atlas/symbol_profiles/294/294870.json|atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv|2020 candidate only; no tested-window contamination|

## 8. Case-by-Case Trigger Grid

|trigger_id|case_id|type|date|entry|price|MFE90|MAE90|MFE180|MAE180|outcome|usable|dedupe|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R10L5_C01_T1_STAGE2_EARLY_REMODELING_DEMAND|R10L5_CASE01_HANSEM_COVID_REMODELING|Stage2|2020-04-07|2020-04-07|59800|106.5|-0.5|106.5|-0.5|excellent_entry|True|True|
|R10L5_C01_T2_STAGE2_ACTIONABLE_Q1_DEMAND|R10L5_CASE01_HANSEM_COVID_REMODELING|Stage2-Actionable|2020-05-13|2020-05-13|86000|43.6|-3.7|50.0|-3.7|excellent_entry|True|True|
|R10L5_C01_T3_STAGE3_YELLOW_RS_EARNINGS|R10L5_CASE01_HANSEM_COVID_REMODELING|Stage3-Yellow|2020-06-02|2020-06-02|95000|30.0|-15.7|35.8|-15.7|good_entry|True|True|
|R10L5_C01_T4_STAGE3_GREEN_CONFIRMED_RERATING|R10L5_CASE01_HANSEM_COVID_REMODELING|Stage3-Green|2020-07-09|2020-07-09|111000|11.3|-10.0|16.2|-10.0|late_entry|True|True|
|R10L5_C01_T5_4B_CONTROL_PREMIUM_BLOWOFF|R10L5_CASE01_HANSEM_COVID_REMODELING|4B|2021-07-14|2021-07-14|146500|1.7|-43.0|1.7|-43.0|event_premium|True|False|
|R10L5_C02_T1_STAGE2_NEOM_AWARENESS|R10L5_CASE02_HYUNDAI_CONSTRUCTION_NEOM_EVENT|Stage2|2022-11-01|2022-11-01|37250|19.3|-12.6|19.3|-12.6|event_premium|True|True|
|R10L5_C02_T2_STAGE2_ACTIONABLE_POLICY_RS|R10L5_CASE02_HYUNDAI_CONSTRUCTION_NEOM_EVENT|Stage2-Actionable|2022-11-09|2022-11-09|40750|9.2|-20.1|9.2|-20.1|good_entry|True|True|
|R10L5_C02_T4_STAGE3_GREEN_TOO_LATE_NEOM|R10L5_CASE02_HYUNDAI_CONSTRUCTION_NEOM_EVENT|Stage3-Green|2022-11-14|2022-11-14|43550|2.1|-25.3|2.1|-25.3|late_entry|True|True|
|R10L5_C02_T5_4B_PRICE_ONLY_EVENT_PEAK|R10L5_CASE02_HYUNDAI_CONSTRUCTION_NEOM_EVENT|4B|2022-11-14|2022-11-14|43550|2.1|-25.3|2.1|-25.3|event_premium|True|False|
|R10L5_C03_T1_STAGE2_QUALITY_INCIDENT|R10L5_CASE03_GS_CONSTRUCTION_QUALITY_4C|Stage2|2023-04-29|2023-05-02|20500|8.0|-33.2|8.0|-38.2|thesis_break|True|True|
|R10L5_C03_T5_4B_QUALITY_OVERHANG_COST_WATCH|R10L5_CASE03_GS_CONSTRUCTION_QUALITY_4C|4B|2023-06-29|2023-06-29|18600|3.1|-31.9|-0.0|-31.9|thesis_break|True|False|
|R10L5_C03_T6_4C_FULL_RECONSTRUCTION_COST|R10L5_CASE03_GS_CONSTRUCTION_QUALITY_4C|4C|2023-07-05|2023-07-06|14520|3.9|-12.9|19.8|-12.9|hard_4c_late|True|False|
|R10L5_C04_T1_HWAJEONG_COLLAPSE_4C|R10L5_CASE04_HDC_QUALITY_4C|4C|2022-01-11|2022-01-12|20850|8.9|-36.9|8.9|-49.2|hard_4c_success|True|False|
|R10L5_C04_T5_INVESTIGATION_QUALITY_RISK|R10L5_CASE04_HDC_QUALITY_4C|4B|2022-03-14|2022-03-14|16400|7.0|-29.3|7.0|-35.4|hard_4c_late|True|False|
|R10L5_C04_T6_ADMIN_SANCTION_4C_CONFIRM|R10L5_CASE04_HDC_QUALITY_4C|4C|2022-03-29|2022-03-29|15250|6.6|-30.2|6.6|-30.2|hard_4c_late|True|False|

## 9. Trigger-Level OHLC Backtest Tables

### Entry / risk comparison

|trigger_id|type|entry|price|MFE90|MAE90|MFE180|MAE180|outcome|
|---|---|---|---|---|---|---|---|---|
|R10L5_C01_T1_STAGE2_EARLY_REMODELING_DEMAND|Stage2|2020-04-07|59800|106.5|-0.5|106.5|-0.5|excellent_entry|
|R10L5_C01_T2_STAGE2_ACTIONABLE_Q1_DEMAND|Stage2-Actionable|2020-05-13|86000|43.6|-3.7|50.0|-3.7|excellent_entry|
|R10L5_C01_T3_STAGE3_YELLOW_RS_EARNINGS|Stage3-Yellow|2020-06-02|95000|30.0|-15.7|35.8|-15.7|good_entry|
|R10L5_C01_T4_STAGE3_GREEN_CONFIRMED_RERATING|Stage3-Green|2020-07-09|111000|11.3|-10.0|16.2|-10.0|late_entry|
|R10L5_C01_T5_4B_CONTROL_PREMIUM_BLOWOFF|4B|2021-07-14|146500|1.7|-43.0|1.7|-43.0|event_premium|
|R10L5_C02_T1_STAGE2_NEOM_AWARENESS|Stage2|2022-11-01|37250|19.3|-12.6|19.3|-12.6|event_premium|
|R10L5_C02_T2_STAGE2_ACTIONABLE_POLICY_RS|Stage2-Actionable|2022-11-09|40750|9.2|-20.1|9.2|-20.1|good_entry|
|R10L5_C02_T4_STAGE3_GREEN_TOO_LATE_NEOM|Stage3-Green|2022-11-14|43550|2.1|-25.3|2.1|-25.3|late_entry|
|R10L5_C02_T5_4B_PRICE_ONLY_EVENT_PEAK|4B|2022-11-14|43550|2.1|-25.3|2.1|-25.3|event_premium|
|R10L5_C03_T1_STAGE2_QUALITY_INCIDENT|Stage2|2023-05-02|20500|8.0|-33.2|8.0|-38.2|thesis_break|
|R10L5_C03_T5_4B_QUALITY_OVERHANG_COST_WATCH|4B|2023-06-29|18600|3.1|-31.9|-0.0|-31.9|thesis_break|
|R10L5_C03_T6_4C_FULL_RECONSTRUCTION_COST|4C|2023-07-06|14520|3.9|-12.9|19.8|-12.9|hard_4c_late|
|R10L5_C04_T1_HWAJEONG_COLLAPSE_4C|4C|2022-01-12|20850|8.9|-36.9|8.9|-49.2|hard_4c_success|
|R10L5_C04_T5_INVESTIGATION_QUALITY_RISK|4B|2022-03-14|16400|7.0|-29.3|7.0|-35.4|hard_4c_late|
|R10L5_C04_T6_ADMIN_SANCTION_4C_CONFIRM|4C|2022-03-29|15250|6.6|-30.2|6.6|-30.2|hard_4c_late|

### Key observations

- 한샘은 Stage2가 Green보다 훨씬 좋다. 2020-04-07 entry는 MFE90 106.5 / MAE90 -0.5였고, 2020-07-09 Green은 MFE90 11.3 / MAE90 -10.0으로 upside 대부분을 놓쳤다.
- 현대건설 NEOM 테마는 Stage2 watch로는 쓸 수 있으나 Green까지 올리면 peak 부근 진입이 된다. 2022-11-14 Green 후보는 MFE90 2.1 / MAE90 -25.3이었다.
- GS건설과 HDC현대산업개발은 비용 확정이나 행정제재 이전에 사고 발생 자체가 4C-watch여야 했다. GS 초기 incident row는 이후 MAE90 -33.2, HDC 붕괴 row는 MAE180 -49.2를 만들었다.

## 10. 1D Price Path Summaries


### R10L5_CASE01 한샘 — best Stage2 after 2020-04-07 close 59,800
|step|date|close_return_pct|high_to_date_return_pct|low_to_date_return_pct|
|---|---|---:|---:|---:|
|D+1|2020-04-08|2.8|8.7|2.0|
|D+2|2020-04-09|4.5|8.7|0.8|
|D+5|2020-04-16|3.5|8.7|-0.5|
|D+10|2020-04-23|19.1|20.4|-0.5|
|D+20|2020-05-08|26.6|26.8|-0.5|
|D+30|2020-05-22|41.5|52.3|-0.5|
|D+60|2020-07-03|60.0|62.0|-0.5|
|D+90|2020-08-20|79.8|106.5|-0.5|
|D+180|2021-01-06|83.1|106.5|-0.5|
|D+252|2021-04-08|109.9|115.7|-0.5|
|D+504|2022-04-12|not_listed_in_table|149.2|-0.5|

### R10L5_CASE02 현대건설 — best Stage2 after 2022-11-01 close 37,250
|step|date|close_return_pct|high_to_date_return_pct|low_to_date_return_pct|
|---|---|---:|---:|---:|
|D+1|2022-11-02|-0.5|3.2|-1.6|
|D+3|2022-11-04|2.6|3.5|-1.6|
|D+5|2022-11-08|2.6|8.2|-1.6|
|D+10|2022-11-15|14.2|19.3|-1.6|
|D+20|2022-11-29|9.0|19.3|-1.6|
|D+30|2022-12-13|-1.9|19.3|-2.0|
|D+60|2023-02-01|1.9|19.3|-12.6|
|D+90|2023-03-15|-0.4|19.3|-12.6|
|D+180|2023-07-31|0.4|19.3|-12.6|

### R10L5_CASE03 GS건설 — quality incident after 2023-05-02 close 20,500
|step|date|close_return_pct|high_to_date_return_pct|low_to_date_return_pct|
|---|---|---:|---:|---:|
|D+1|2023-05-03|-2.0|4.4|-3.4|
|D+5|2023-05-10|2.4|6.8|-3.4|
|D+10|2023-05-17|0.5|7.8|-3.4|
|D+20|2023-05-31|1.2|8.0|-3.4|
|D+30|2023-06-15|2.7|8.0|-2.4|
|D+60|2023-07-31|-28.7|8.0|-33.2|
|D+90|2023-09-11|-28.5|8.0|-33.2|
|D+180|2023-12-28|-26.7|8.0|-38.2|

### R10L5_CASE04 HDC현대산업개발 — hard 4C after 2022-01-12 close 20,850
|step|date|close_return_pct|high_to_date_return_pct|low_to_date_return_pct|
|---|---|---:|---:|---:|
|D+1|2022-01-13|-1.2|8.9|-6.7|
|D+2|2022-01-14|-9.6|8.9|-10.3|
|D+5|2022-01-19|-23.7|8.9|-25.7|
|D+10|2022-01-26|-30.9|8.9|-35.3|
|D+20|2022-02-15|-25.9|8.9|-35.3|
|D+30|2022-02-28|-23.0|8.9|-35.3|
|D+60|2022-04-13|-28.3|8.9|-36.9|
|D+90|2022-05-27|-34.3|8.9|-36.9|
|D+180|2022-09-27|not_listed_in_table|8.9|-49.2|


## 11. Case Trigger Comparison

|case|best actual trigger|baseline likely trigger|after profile trigger|verdict|
|---|---|---|---|---|
|한샘|Stage2 2020-04-07|Stage3-Green 2020-07-09|Stage2 2020-04-07|baseline Green gate too late|
|현대건설|Stage2 watch 2022-11-01|Stage3-Green 2022-11-14|Stage2 watch only|event premium, do not Green without contract/margin bridge|
|GS건설|incident 4C-watch 2023-05-02|hard 4C after full reconstruction 2023-07-06|incident 4C-watch 2023-05-02|early quality-risk watch needed|
|HDC현대산업개발|hard 4C 2022-01-12|hard 4C if safety gate exists|hard 4C 2022-01-12|legal/safety thesis break should be immediate|

## 12. Stage2 → Stage4 Audit

한샘은 Stage2 trigger의 MFE가 크고 MAE가 얕았다. 이것은 `old_gate_problem = Stage3_gate_too_late`에 해당한다. Stage2가 좋았던 이유는 단순 theme이 아니라 stay-home demand, 리모델링 수요, 상대강도, 실적 추정 개선이 같은 방향으로 겹쳤기 때문이다.

현대건설은 Stage2에서는 단기 event MFE가 있었지만, 계약/수주/마진 bridge가 없었다. 따라서 Stage2-Actionable은 가능해도 Stage3-Green으로 올리면 false-positive_score에 가까워진다.

GS건설과 HDC현대산업개발은 Stage2 entry가 아니라 4C-risk audit이다. 건설 품질/안전 사고는 실적수치가 나오기 전에도 수주/분양/브랜드 신뢰를 훼손하므로, legal/regulatory risk component가 즉시 켜져야 한다.

## 13. Stage3 Yellow / Green Lateness Audit

|case|Stage2 entry|Green entry|peak after Stage2|green_lateness_ratio|verdict|
|---|---:|---:|---:|---:|---|
|한샘|59,800|111,000|149,000|0.378|Green 다소 늦음. Stage2-Actionable 승격 필요|
|현대건설|37,250|43,550|44,450|0.875|Green이 upside 대부분을 놓침|
|GS건설|not_applicable|not_applicable|22,150|not_applicable|4C/risk case|
|HDC현대산업개발|not_applicable|not_applicable|22,700|not_applicable|4C/risk case|

## 14. 4B Timing Audit

4B는 가격만으로 확정하지 않고 local/full-window proximity를 분리했다.

|trigger|local proximity|full-window proximity|non-price evidence|verdict|
|---|---:|---:|---|---|
|한샘 2021-07-14 control-premium blowoff|1.00|1.00|control premium, valuation blowoff, positioning|good_full_window_4B_timing|
|현대건설 2022-11-14 NEOM event peak|1.00|1.00|price_only/event premium|price_only_local_4B_watch_not_full_exit|
|GS건설 2023-06-29 quality overhang|0.45|0.45|investigation/cost watch|quality_4B_watch_before_cost_confirmation|
|HDC 2022-03-14 investigation risk|0.34|0.34|legal/regulatory risk after 4C|late_quality_4B_after_4C|

핵심은 현대건설이다. peak proximity만 보면 4B timing은 좋지만, 비가격 증거가 없으면 full 4B가 아니라 event-premium watch다. 반대로 한샘은 control premium과 valuation/positioning이 붙어 full-window 4B로 보는 것이 맞다.

## 15. 4C Protection Audit

|case|4C trigger|MAE after trigger|protection label|interpretation|
|---|---|---:|---|---|
|HDC현대산업개발|2022-01-12|MAE180 -49.2|hard_4c_success|사고 당일/다음 거래일에 4C를 켜야 이후 drawdown을 피할 수 있었다|
|GS건설|2023-05-02|MAE90 -33.2|thesis_break_watch_only|사고 발생 때 4C-watch 필요. 2023-07-06 hard 4C는 늦었다|
|한샘|2021-07-14 이후|MAE90 -43.0|thesis_break_watch_only|4B control-premium peak 뒤 thesis weakening 감지|
|현대건설|none|not_applicable|hard_4c_not_confirmed|event premium fade이지 hard 4C는 아니다|

## 16. Baseline Score Simulation

Baseline current proxy는 Green confirmation을 너무 늦게 요구하고, 건설 품질 사고는 비용/제재 확인 후에야 hard하게 잡는 형태로 가정했다. 이 가정은 production score를 뜻하지 않는다.

```jsonl
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L5_CASE01_HANSEM_COVID_REMODELING", "trigger_id": "R10L5_C01_T1_STAGE2_EARLY_REMODELING_DEMAND", "symbol": "009240", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 0}, "weighted_score_before": 13, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 4, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 0}, "weighted_score_after": 17, "stage_label_after": "Stage2", "changed_components": ["relative_strength_score", "revision_score"], "component_delta_explanation": "after profile boosts early RS/revision for proven Stage2 entries and boosts legal/thesis-break risk for construction quality events; no production score changed.", "selected_by_profile": true, "MFE_90D_pct": 106.5, "MAE_90D_pct": -0.5, "score_return_alignment_label": "score_low_return_high_missed_structural"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L5_CASE01_HANSEM_COVID_REMODELING", "trigger_id": "R10L5_C01_T4_STAGE3_GREEN_CONFIRMED_RERATING", "symbol": "009240", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 0}, "weighted_score_before": 13, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 0}, "weighted_score_after": 13, "stage_label_after": "Stage2", "changed_components": [], "component_delta_explanation": "after profile boosts early RS/revision for proven Stage2 entries and boosts legal/thesis-break risk for construction quality events; no production score changed.", "selected_by_profile": false, "MFE_90D_pct": 11.3, "MAE_90D_pct": -10.0, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L5_CASE02_HYUNDAI_CONSTRUCTION_NEOM_EVENT", "trigger_id": "R10L5_C02_T4_STAGE3_GREEN_TOO_LATE_NEOM", "symbol": "000720", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 0}, "weighted_score_before": 15, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 0}, "weighted_score_after": 15, "stage_label_after": "Stage2", "changed_components": [], "component_delta_explanation": "after profile boosts early RS/revision for proven Stage2 entries and boosts legal/thesis-break risk for construction quality events; no production score changed.", "selected_by_profile": false, "MFE_90D_pct": 2.1, "MAE_90D_pct": -25.3, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L5_CASE03_GS_CONSTRUCTION_QUALITY_4C", "trigger_id": "R10L5_C03_T5_4B_QUALITY_OVERHANG_COST_WATCH", "symbol": "006360", "trigger_type": "4B", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 8, "thesis_break_score": 5}, "weighted_score_before": 22, "stage_label_before": "4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 8, "thesis_break_score": 7}, "weighted_score_after": 26, "stage_label_after": "4B-watch", "changed_components": ["legal_or_contract_risk_score", "thesis_break_score"], "component_delta_explanation": "after profile boosts early RS/revision for proven Stage2 entries and boosts legal/thesis-break risk for construction quality events; no production score changed.", "selected_by_profile": false, "MFE_90D_pct": 3.1, "MAE_90D_pct": -31.9, "score_return_alignment_label": "score_mid_return_low_watch_only"}
```

## 17. Shadow Profile Optimization Loop

|profile_id|case_count|selected_trigger_count|selected_representative_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|hit_rate_MFE90_gt_20pct|bad_entry_rate_MAE90_lt_minus_15pct|false_positive_rate|missed_structural_count|late_green_count|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|
|baseline_current_proxy|4|4|2|6.7|-17.6|0.0|0.5|0.2|1|2|reference|
|r10_stage2_actionable_quality_guard|4|4|3|44.6|-15.4|0.3|0.3|0.0|0|0|best mixed entry/risk profile|
|stage3_yellow_entry_relaxed|4|4|3|15.7|-23.0|0.3|1.0|0.0|0|0|Allow Yellow when one evidence gate is missing but RS and revision/customer evidence are strong.|
|green_confirmation_timing_relaxed|4|4|3|20.3|-19.0|0.3|0.7|0.0|0|0|Shift Green threshold earlier but still require non-price evidence; rejects pure NEOM price chase.|
|four_b_peak_timing_tuned|4|4|0|3.5|-32.4|0.0|1.0|0.0|0|0|Split price-only local 4B from non-price 4B; keep Hansem full-window 4B, Hyundai price-only watch.|
|four_c_thesis_break_earlier|4|4|1|8.0|-33.2|0.0|1.0|0.0|0|0|Quality/safety/legal accidents trigger 4C watch at incident date, not only after cost or sanction confirmation.|

Best profile for this R10 loop: `r10_stage2_actionable_quality_guard`.

## 18. Before / After Backtest Comparison

|case|best_actual_trigger|baseline_selected_trigger|after_selected_trigger|baseline_MFE90|after_MFE90|baseline_MAE90|after_MAE90|reason|
|---|---|---|---|---:|---:|---:|---:|---|
|한샘|Stage2 2020-04-07|Green 2020-07-09|Stage2 2020-04-07|11.3|106.5|-10.0|-0.5|early demand/revision + RS should be promoted|
|현대건설|Stage2 watch 2022-11-01|Green 2022-11-14|Stage2 watch only|2.1|19.3|-25.3|-12.6|price-only event premium should not Green|
|GS건설|4C-watch 2023-05-02|hard 4C 2023-07-06|4C-watch 2023-05-02|3.9|8.0|-12.9|-33.2|watch should start at incident; hard 4C later|
|HDC현대산업개발|hard 4C 2022-01-12|hard 4C if quality gate exists|hard 4C 2022-01-12|8.9|8.9|-36.9|-36.9|quality accident is immediate thesis break|

## 19. Score-Return Alignment Matrix

|alignment_label|trigger_count|avg_weighted_score_before|avg_weighted_score_after|avg_MFE_90D_pct|avg_MAE_90D_pct|verdict|
|---|---:|---:|---:|---:|---:|---|
|score_low_return_high_missed_structural|1|25|29|106.5|-0.5|한샘 early Stage2는 missed structural|
|score_mid_return_high_promote_candidate|2|25|27|14.6|-10.3|Stage2 watch는 가능하나 evidence guard 필요|
|score_high_return_low_false_positive|2|34|34|2.1|-25.3|NEOM Green / price-only 4B는 false-positive risk|
|score_mid_return_low_watch_only|10|24|28|7.1|-24.4|risk/watch labels dominate; not entry aggregate|

## 20. Weight Sensitivity Table

row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_early_revision_plus_RS,0,3,+3,Hansem Stage2 produced MFE90 106.5 with MAE90 -0.5; Green had only MFE90 11.3 with deeper MAE.,"For structural interior/remodeling, early Stage2 improved 90D upside capture by about +95pp versus Green while avoiding added drawdown.",R10L5_C01_T1_STAGE2_EARLY_REMODELING_DEMAND|R10L5_C01_T4_STAGE3_GREEN_CONFIRMED_RERATING,2,shadow-only; production unchanged
shadow_weight,price_only_megaproject_event_cap,0,-2,-2,Hyundai Construction NEOM Green near local peak had MFE90 2.1 and MAE90 -25.3.,Rejects converting price-only policy/event premium into full Green without contract/backlog/margin bridge.,R10L5_C02_T4_STAGE3_GREEN_TOO_LATE_NEOM|R10L5_C02_T5_4B_PRICE_ONLY_EVENT_PEAK,2,shadow-only; production unchanged
shadow_weight,construction_quality_incident_4c_watch,0,3,+3,GS and HDC quality/safety incidents preceded deep MAE drawdowns when treated early.,Moves quality accident from late confirmation to 4C-watch immediately; HDC avoided a further observed MAE180 near -49.2 from incident entry.,R10L5_C03_T1_STAGE2_QUALITY_INCIDENT|R10L5_C04_T1_HWAJEONG_COLLAPSE_4C,2,shadow-only; production unchanged
shadow_weight,non_price_4b_required_for_full_exit,0,2,+2,Hansem had control premium/valuation/positioning 4B near full-window peak; Hyundai had price-only event premium.,Splitting local price-only from full 4B reduces premature exit on event themes while retaining true blowoff/overhang detection.,R10L5_C01_T5_4B_CONTROL_PREMIUM_BLOWOFF|R10L5_C02_T5_4B_PRICE_ONLY_EVENT_PEAK,2,shadow-only; production unchanged
shadow_weight,legal_regulatory_thesis_break_hard_gate,0,2,+2,GS/HDC safety and legal-regulatory evidence directly broke construction-quality thesis.,Improves drawdown-protection tagging; does not convert narrative-only risk into weight change without OHLC window.,R10L5_C03_T6_4C_FULL_RECONSTRUCTION_COST|R10L5_C04_T6_ADMIN_SANCTION_4C_CONFIRM,2,shadow-only; production unchanged

## 21. Optimization Decision Log

```jsonl
{"row_type": "optimization_decision", "decision_id": "R10L5_DEC01", "hypothesis": "Early demand/revision + RS should promote Stage2 to Actionable in interior/materials recovery cases.", "tested_trigger_ids": ["R10L5_C01_T1_STAGE2_EARLY_REMODELING_DEMAND", "R10L5_C01_T4_STAGE3_GREEN_CONFIRMED_RERATING"], "baseline_profile": "baseline_current_proxy", "selected_profile": "r10_stage2_actionable_quality_guard", "backtest_result_summary": "Hansem early Stage2 MFE90 106.5 / MAE90 -0.5 versus Green MFE90 11.3 / MAE90 -10.0.", "accepted_or_rejected": "accepted", "delta_magnitude": "+3", "why_not_larger_delta": "Only one clean structural-success interior case in this R10 loop.", "risks": "May over-promote one-off COVID demand without revision evidence.", "next_validation_needed": "Find non-COVID remodeling/materials counterexample."}
{"row_type": "optimization_decision", "decision_id": "R10L5_DEC02", "hypothesis": "Price-only mega-project event premium should not become full Green without contract/backlog/margin bridge.", "tested_trigger_ids": ["R10L5_C02_T1_STAGE2_NEOM_AWARENESS", "R10L5_C02_T4_STAGE3_GREEN_TOO_LATE_NEOM"], "baseline_profile": "baseline_current_proxy", "selected_profile": "r10_stage2_actionable_quality_guard", "backtest_result_summary": "Hyundai Stage2 had MFE90 19.3 / MAE90 -12.6, while Green near peak had MFE90 2.1 / MAE90 -25.3.", "accepted_or_rejected": "accepted", "delta_magnitude": "-2", "why_not_larger_delta": "The Stage2 event itself had positive MFE; reject only Green promotion, not watchlist awareness.", "risks": "Real contract announcements could justify promotion in other cases.", "next_validation_needed": "Test Saudi/NEOM actual-contract winners separately."}
{"row_type": "optimization_decision", "decision_id": "R10L5_DEC03", "hypothesis": "Construction quality/safety event with legal/regulatory consequence should trigger immediate 4C-watch.", "tested_trigger_ids": ["R10L5_C03_T1_STAGE2_QUALITY_INCIDENT", "R10L5_C04_T1_HWAJEONG_COLLAPSE_4C"], "baseline_profile": "baseline_current_proxy", "selected_profile": "four_c_thesis_break_earlier", "backtest_result_summary": "GS initial incident led to MAE90 -33.2; HDC incident led to MAE180 -49.2. Later confirmation rows were too late for full protection.", "accepted_or_rejected": "accepted", "delta_magnitude": "+3", "why_not_larger_delta": "Small sample of two quality accidents; keep as watch/hard-gate pair, not generic construction-risk penalty.", "risks": "False breaks from minor accidents or non-material project issues.", "next_validation_needed": "Compare with minor non-fatal site accidents that did not impair stock path."}
```

## 22. Overfitting / Robustness Check

- Usable trigger count = 15.
- Representative entry trigger count = 8.
- The strongest positive delta is +3, not +5, because this round has one clean structural-success case for early Stage2 promotion and two quality-accident 4C cases.
- Counterexample: 현대건설 NEOM event shows why early Stage2/RS cannot become full Green without contract/backlog/margin bridge.
- Counterexample: GS건설 2023-07 hard 4C was late and later recovered partly; therefore quality-incident hard gate should be a watch→confirm pair, not unconditional permanent reject.

## 23. Cross-case Aggregate Metrics

### Trigger type aggregate

row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,below_entry_90D_rate,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,4B,4,0,3.5,2.6,-32.4,-30.6,2.7,-33.9,1.0,not_applicable,overlay_only,overlay_only,representative rows only; duplicate same-entry labels excluded
aggregate_metric,4C,3,0,6.5,6.6,-26.7,-30.2,11.8,-30.8,1.0,not_applicable,not_applicable,not_applicable,representative rows only; duplicate same-entry labels excluded
aggregate_metric,Stage2,3,3,44.6,19.3,-15.4,-12.6,44.6,-17.1,0.67,not_applicable,not_applicable,not_applicable,representative rows only; duplicate same-entry labels excluded
aggregate_metric,Stage2-Actionable,2,2,26.4,26.4,-11.9,-11.9,29.6,-11.9,1.0,not_applicable,not_applicable,not_applicable,representative rows only; duplicate same-entry labels excluded
aggregate_metric,Stage3-Green,2,2,6.7,6.7,-17.6,-17.6,9.2,-17.6,1.0,not_applicable,not_applicable,not_applicable,representative rows only; duplicate same-entry labels excluded
aggregate_metric,Stage3-Yellow,1,1,30.0,30.0,-15.7,-15.7,35.8,-15.7,1.0,not_applicable,not_applicable,not_applicable,representative rows only; duplicate same-entry labels excluded

### Profile aggregate

row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,4,4,2,6.7,6.7,-17.6,-17.6,9.2,-17.6,0.0,0.5,0.25,1,2,0.64,split_overlay,split_overlay,reference
profile_comparison,r10_stage2_actionable_quality_guard,4,4,3,44.6,19.3,-15.4,-12.6,44.6,-17.1,0.33,0.33,0.0,0,0,0.34,split_overlay,split_overlay,best mixed entry/risk profile
profile_comparison,stage3_yellow_entry_relaxed,4,4,3,15.7,9.2,-23.0,-20.1,17.7,-24.7,0.33,1.0,0.0,0,0,0.34,split_overlay,split_overlay,Allow Yellow when one evidence gate is missing but RS and revision/customer evidence are strong.
profile_comparison,green_confirmation_timing_relaxed,4,4,3,20.3,9.2,-19.0,-20.1,22.4,-20.7,0.33,0.67,0.0,0,0,0.34,split_overlay,split_overlay,Shift Green threshold earlier but still require non-price evidence; rejects pure NEOM price chase.
profile_comparison,four_b_peak_timing_tuned,4,4,0,3.5,2.6,-32.4,-30.6,2.7,-33.9,0.0,1.0,0.0,0,0,0.34,split_overlay,split_overlay,"Split price-only local 4B from non-price 4B; keep Hansem full-window 4B, Hyundai price-only watch."
profile_comparison,four_c_thesis_break_earlier,4,4,1,8.0,8.0,-33.2,-33.2,8.0,-38.2,0.0,1.0,0.0,0,0,0.34,split_overlay,split_overlay,"Quality/safety/legal accidents trigger 4C watch at incident date, not only after cost or sanction confirmation."

## 24. Score-Price Alignment Verdict

R10 validates three shadow-only changes. First, early evidence plus relative strength in interior/remodeling should become Stage2-Actionable earlier than Green. Second, price-only mega-project themes should stay Stage2 watch until contract/backlog/margin bridge closes. Third, construction quality/safety incidents should immediately activate 4C-watch, with hard 4C confirmation when legal/regulatory/cost evidence arrives.

## 25. Validation Scope / Non-Validation Scope

### this_round_validates

- Stage2-Actionable early demand/revision + relative strength in interior/remodeling.
- Price-only mega-project/event premium rejection as full Stage3-Green.
- Non-price 4B distinction: control premium/valuation blowoff vs price-only local peak.
- Construction quality/safety incident as immediate 4C-watch.
- Hard 4C confirmation on legal/regulatory/cost evidence.

### this_round_does_not_validate

- Broad Green relaxation across all construction contractors.
- PF financing risk gate for builders without a quality/safety event.
- Adjusted-price corporate-action revalidation.
- Market/sector relative return calibration.

No shadow delta is proposed for unvalidated gates.

## 26. Shadow Weight Calibration

row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_early_revision_plus_RS,0,3,+3,Hansem Stage2 produced MFE90 106.5 with MAE90 -0.5; Green had only MFE90 11.3 with deeper MAE.,"For structural interior/remodeling, early Stage2 improved 90D upside capture by about +95pp versus Green while avoiding added drawdown.",R10L5_C01_T1_STAGE2_EARLY_REMODELING_DEMAND|R10L5_C01_T4_STAGE3_GREEN_CONFIRMED_RERATING,2,shadow-only; production unchanged
shadow_weight,price_only_megaproject_event_cap,0,-2,-2,Hyundai Construction NEOM Green near local peak had MFE90 2.1 and MAE90 -25.3.,Rejects converting price-only policy/event premium into full Green without contract/backlog/margin bridge.,R10L5_C02_T4_STAGE3_GREEN_TOO_LATE_NEOM|R10L5_C02_T5_4B_PRICE_ONLY_EVENT_PEAK,2,shadow-only; production unchanged
shadow_weight,construction_quality_incident_4c_watch,0,3,+3,GS and HDC quality/safety incidents preceded deep MAE drawdowns when treated early.,Moves quality accident from late confirmation to 4C-watch immediately; HDC avoided a further observed MAE180 near -49.2 from incident entry.,R10L5_C03_T1_STAGE2_QUALITY_INCIDENT|R10L5_C04_T1_HWAJEONG_COLLAPSE_4C,2,shadow-only; production unchanged
shadow_weight,non_price_4b_required_for_full_exit,0,2,+2,Hansem had control premium/valuation/positioning 4B near full-window peak; Hyundai had price-only event premium.,Splitting local price-only from full 4B reduces premature exit on event themes while retaining true blowoff/overhang detection.,R10L5_C01_T5_4B_CONTROL_PREMIUM_BLOWOFF|R10L5_C02_T5_4B_PRICE_ONLY_EVENT_PEAK,2,shadow-only; production unchanged
shadow_weight,legal_regulatory_thesis_break_hard_gate,0,2,+2,GS/HDC safety and legal-regulatory evidence directly broke construction-quality thesis.,Improves drawdown-protection tagging; does not convert narrative-only risk into weight change without OHLC window.,R10L5_C03_T6_4C_FULL_RECONSTRUCTION_COST|R10L5_C04_T6_ADMIN_SANCTION_4C_CONFIRM,2,shadow-only; production unchanged

## 27. Machine-Readable Rows

### 27.1 Price source validation row JSONL

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 27.2 Case rows JSONL

```jsonl
{"row_type": "case", "case_id": "R10L5_CASE01_HANSEM_COVID_REMODELING", "symbol": "009240", "company_name": "한샘", "round": "R10", "loop": "5", "sector": "건설·부동산·건자재", "case_type": "structural_success", "primary_archetype": "INTERIOR_REMODELING_STAY_HOME_EPS_RERATING", "best_trigger": "R10L5_C01_T1_STAGE2_EARLY_REMODELING_DEMAND", "calibration_usable": true, "historical_window_status": "504D_available_or_manifest_observed", "score_price_alignment": "mixed_alignment_relevant_for_shadow_calibration", "price_source": "Songdaiki/stock-web", "notes": "집콕/리모델링 수요와 실적 추정 상향이 가격보다 늦게 닫히며, Stage2가 Green보다 훨씬 유리했던 성공형 케이스."}
{"row_type": "case", "case_id": "R10L5_CASE02_HYUNDAI_CONSTRUCTION_NEOM_EVENT", "symbol": "000720", "company_name": "현대건설", "round": "R10", "loop": "5", "sector": "건설·부동산·건자재", "case_type": "event_premium_failed_rerating", "primary_archetype": "MEGA_PROJECT_NEOM_POLICY_EVENT_PREMIUM", "best_trigger": "R10L5_C02_T1_STAGE2_NEOM_AWARENESS", "calibration_usable": true, "historical_window_status": "504D_available_or_manifest_observed", "score_price_alignment": "mixed_alignment_relevant_for_shadow_calibration", "price_source": "Songdaiki/stock-web", "notes": "NEOM/사우디 이벤트 프리미엄은 단기 MFE는 만들었지만 OP/FCF 확정으로 이어지기 전 Green을 주면 늦고 취약했다."}
{"row_type": "case", "case_id": "R10L5_CASE03_GS_CONSTRUCTION_QUALITY_4C", "symbol": "006360", "company_name": "GS건설", "round": "R10", "loop": "5", "sector": "건설·부동산·건자재", "case_type": "hard_4c_thesis_break", "primary_archetype": "CONSTRUCTION_QUALITY_SAFETY_THESIS_BREAK", "best_trigger": "R10L5_C03_T1_STAGE2_QUALITY_INCIDENT", "calibration_usable": true, "historical_window_status": "504D_available_or_manifest_observed", "score_price_alignment": "mixed_alignment_relevant_for_shadow_calibration", "price_source": "Songdaiki/stock-web", "notes": "인천 검단 지하주차장 붕괴 이후 재시공/비용 인식까지 quality-risk가 4C로 진화한 케이스."}
{"row_type": "case", "case_id": "R10L5_CASE04_HDC_QUALITY_4C", "symbol": "294870", "company_name": "HDC현대산업개발", "round": "R10", "loop": "5", "sector": "건설·부동산·건자재", "case_type": "hard_4c_thesis_break", "primary_archetype": "BRAND_TRUST_CONSTRUCTION_ACCIDENT_THESIS_BREAK", "best_trigger": "R10L5_C04_T1_HWAJEONG_COLLAPSE_4C", "calibration_usable": true, "historical_window_status": "504D_available_or_manifest_observed", "score_price_alignment": "mixed_alignment_relevant_for_shadow_calibration", "price_source": "Songdaiki/stock-web", "notes": "광주 화정 아이파크 붕괴는 브랜드 신뢰와 수주/분양 thesis가 동시에 깨진 hard 4C 사례."}
```

### 27.3 Trigger rows JSONL

```jsonl
{"row_type": "trigger", "trigger_id": "R10L5_C01_T1_STAGE2_EARLY_REMODELING_DEMAND", "case_id": "R10L5_CASE01_HANSEM_COVID_REMODELING", "symbol": "009240", "company_name": "한샘", "round": "R10", "loop": "5", "sector": "건설·부동산·건자재", "primary_archetype": "INTERIOR_REMODELING_STAY_HOME_EPS_RERATING", "trigger_type": "Stage2", "trigger_date": "2020-04-07", "evidence_available_at_that_date": "코로나 이후 주거시간 증가, 가구/리모델링 수요 회복, 1Q 이후 실적 개선 기대가 공개 뉴스·리포트에 반영되기 시작한 구간.", "evidence_source": "Hanssem public company profile; Korea press/analyst coverage on 2020 home-interior demand; stock-web rows 2020-04-07 onward", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009240/2020.csv", "profile_path": "atlas/symbol_profiles/009/009240.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-04-07", "entry_price": 59800, "MFE_30D_pct": 52.3, "MFE_90D_pct": 106.5, "MFE_180D_pct": 106.5, "MFE_1Y_pct": 115.7, "MFE_2Y_pct": 149.2, "MAE_30D_pct": -0.5, "MAE_90D_pct": -0.5, "MAE_180D_pct": -0.5, "MAE_1Y_pct": -0.5, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2021-07-14", "peak_price": 149000, "drawdown_after_peak_pct": -44.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.378, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "excellent_entry", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R10L5_C01_EG1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R10L5_C01_T2_STAGE2_ACTIONABLE_Q1_DEMAND", "case_id": "R10L5_CASE01_HANSEM_COVID_REMODELING", "symbol": "009240", "company_name": "한샘", "round": "R10", "loop": "5", "sector": "건설·부동산·건자재", "primary_archetype": "INTERIOR_REMODELING_STAY_HOME_EPS_RERATING", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-05-13", "evidence_available_at_that_date": "상반기 리모델링/가구 수요와 주가 상대강도가 동시에 확인된 후보.", "evidence_source": "stock-web rows 2020-05-13 onward; Hanssem industry/news coverage", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009240/2020.csv", "profile_path": "atlas/symbol_profiles/009/009240.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-05-13", "entry_price": 86000, "MFE_30D_pct": 43.6, "MFE_90D_pct": 43.6, "MFE_180D_pct": 50.0, "MFE_1Y_pct": 73.3, "MFE_2Y_pct": 73.3, "MAE_30D_pct": -3.7, "MAE_90D_pct": -3.7, "MAE_180D_pct": -3.7, "MAE_1Y_pct": -3.7, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-14", "peak_price": 149000, "drawdown_after_peak_pct": -44.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.282, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "excellent_entry", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R10L5_C01_EG2", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R10L5_C01_T3_STAGE3_YELLOW_RS_EARNINGS", "case_id": "R10L5_CASE01_HANSEM_COVID_REMODELING", "symbol": "009240", "company_name": "한샘", "round": "R10", "loop": "5", "sector": "건설·부동산·건자재", "primary_archetype": "INTERIOR_REMODELING_STAY_HOME_EPS_RERATING", "trigger_type": "Stage3-Yellow", "trigger_date": "2020-06-02", "evidence_available_at_that_date": "실적 기대와 가격 상대강도는 강해졌으나 margin/backlog 정량 gate는 완전히 닫히기 전.", "evidence_source": "stock-web rows 2020-06-02 onward; company/analyst reporting", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009240/2020.csv", "profile_path": "atlas/symbol_profiles/009/009240.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-06-02", "entry_price": 95000, "MFE_30D_pct": 30.0, "MFE_90D_pct": 30.0, "MFE_180D_pct": 35.8, "MFE_1Y_pct": 56.8, "MFE_2Y_pct": 56.8, "MAE_30D_pct": -15.7, "MAE_90D_pct": -15.7, "MAE_180D_pct": -15.7, "MAE_1Y_pct": -15.7, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-14", "peak_price": 149000, "drawdown_after_peak_pct": -44.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.184, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_entry", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R10L5_C01_EG3", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R10L5_C01_T4_STAGE3_GREEN_CONFIRMED_RERATING", "case_id": "R10L5_CASE01_HANSEM_COVID_REMODELING", "symbol": "009240", "company_name": "한샘", "round": "R10", "loop": "5", "sector": "건설·부동산·건자재", "primary_archetype": "INTERIOR_REMODELING_STAY_HOME_EPS_RERATING", "trigger_type": "Stage3-Green", "trigger_date": "2020-07-09", "evidence_available_at_that_date": "강한 가격 상대강도와 실적 기대가 같이 닫힌 본 진입 후보이나 Stage2 대비 이미 상당한 상승을 소모.", "evidence_source": "stock-web rows 2020-07-09 onward; 2020 2Q improvement coverage", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009240/2020.csv", "profile_path": "atlas/symbol_profiles/009/009240.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-07-09", "entry_price": 111000, "MFE_30D_pct": 11.3, "MFE_90D_pct": 11.3, "MFE_180D_pct": 16.2, "MFE_1Y_pct": 34.2, "MFE_2Y_pct": 34.2, "MAE_30D_pct": -10.0, "MAE_90D_pct": -10.0, "MAE_180D_pct": -10.0, "MAE_1Y_pct": -10.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-14", "peak_price": 149000, "drawdown_after_peak_pct": -44.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.378, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_entry", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R10L5_C01_EG4", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R10L5_C01_T5_4B_CONTROL_PREMIUM_BLOWOFF", "case_id": "R10L5_CASE01_HANSEM_COVID_REMODELING", "symbol": "009240", "company_name": "한샘", "round": "R10", "loop": "5", "sector": "건설·부동산·건자재", "primary_archetype": "INTERIOR_REMODELING_STAY_HOME_EPS_RERATING", "trigger_type": "4B", "trigger_date": "2021-07-14", "evidence_available_at_that_date": "경영권/인수 프리미엄과 peak-proximity가 겹친 구간. Stage3 thesis 취소가 아니라 4B-watch overlay.", "evidence_source": "Hanssem control-premium/acquisition news coverage; stock-web rows 2021-07-14 onward", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009240/2021.csv", "profile_path": "atlas/symbol_profiles/009/009240.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-07-14", "entry_price": 146500, "MFE_30D_pct": 1.7, "MFE_90D_pct": 1.7, "MFE_180D_pct": 1.7, "MFE_1Y_pct": 1.7, "MFE_2Y_pct": 1.7, "MAE_30D_pct": -20.5, "MAE_90D_pct": -43.0, "MAE_180D_pct": -43.0, "MAE_1Y_pct": -43.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-14", "peak_price": 149000, "drawdown_after_peak_pct": -44.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": "control_premium_or_event_premium|valuation_blowoff|positioning_overheat", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_premium", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R10L5_C01_EG5", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "trigger_id": "R10L5_C02_T1_STAGE2_NEOM_AWARENESS", "case_id": "R10L5_CASE02_HYUNDAI_CONSTRUCTION_NEOM_EVENT", "symbol": "000720", "company_name": "현대건설", "round": "R10", "loop": "5", "sector": "건설·부동산·건자재", "primary_archetype": "MEGA_PROJECT_NEOM_POLICY_EVENT_PREMIUM", "trigger_type": "Stage2", "trigger_date": "2022-11-01", "evidence_available_at_that_date": "사우디/NEOM 기대와 해외수주 narrative가 가격에 반영되기 시작했으나 수주·마진 bridge는 미확정.", "evidence_source": "Korea press on Saudi/NEOM construction expectations; stock-web rows 2022-11-01 onward", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000720/2022.csv", "profile_path": "atlas/symbol_profiles/000/000720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-11-01", "entry_price": 37250, "MFE_30D_pct": 19.3, "MFE_90D_pct": 19.3, "MFE_180D_pct": 19.3, "MFE_1Y_pct": 19.3, "MFE_2Y_pct": 19.3, "MAE_30D_pct": -4.8, "MAE_90D_pct": -12.6, "MAE_180D_pct": -12.6, "MAE_1Y_pct": -12.6, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": true, "peak_date": "2022-11-14", "peak_price": 44450, "drawdown_after_peak_pct": -27.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.833, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "event_premium", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R10L5_C02_EG1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R10L5_C02_T2_STAGE2_ACTIONABLE_POLICY_RS", "case_id": "R10L5_CASE02_HYUNDAI_CONSTRUCTION_NEOM_EVENT", "symbol": "000720", "company_name": "현대건설", "round": "R10", "loop": "5", "sector": "건설·부동산·건자재", "primary_archetype": "MEGA_PROJECT_NEOM_POLICY_EVENT_PREMIUM", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-11-09", "evidence_available_at_that_date": "NEOM/사우디 방한 기대와 상대강도 결합. 아직 계약·OP bridge 미확정이라 Actionable 이하.", "evidence_source": "stock-web rows 2022-11-09 onward; public news on Saudi Crown Prince/NEOM theme", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000720/2022.csv", "profile_path": "atlas/symbol_profiles/000/000720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-11-09", "entry_price": 40750, "MFE_30D_pct": 9.2, "MFE_90D_pct": 9.2, "MFE_180D_pct": 9.2, "MFE_1Y_pct": 9.2, "MFE_2Y_pct": 9.2, "MAE_30D_pct": -10.6, "MAE_90D_pct": -20.1, "MAE_180D_pct": -20.1, "MAE_1Y_pct": -20.1, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-11-14", "peak_price": 44450, "drawdown_after_peak_pct": -27.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.833, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_entry", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R10L5_C02_EG2", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R10L5_C02_T4_STAGE3_GREEN_TOO_LATE_NEOM", "case_id": "R10L5_CASE02_HYUNDAI_CONSTRUCTION_NEOM_EVENT", "symbol": "000720", "company_name": "현대건설", "round": "R10", "loop": "5", "sector": "건설·부동산·건자재", "primary_archetype": "MEGA_PROJECT_NEOM_POLICY_EVENT_PREMIUM", "trigger_type": "Stage3-Green", "trigger_date": "2022-11-14", "evidence_available_at_that_date": "가격과 narrative는 강했으나 수주/마진/FCF gate가 부족한 상태에서 Green을 주면 peak 부근 진입.", "evidence_source": "stock-web rows 2022-11-14 onward; NEOM-event coverage", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000720/2022.csv", "profile_path": "atlas/symbol_profiles/000/000720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-11-14", "entry_price": 43550, "MFE_30D_pct": 2.1, "MFE_90D_pct": 2.1, "MFE_180D_pct": 2.1, "MFE_1Y_pct": 2.1, "MFE_2Y_pct": 2.1, "MAE_30D_pct": -16.3, "MAE_90D_pct": -25.3, "MAE_180D_pct": -25.3, "MAE_1Y_pct": -25.3, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-11-14", "peak_price": 44450, "drawdown_after_peak_pct": -27.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.833, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_entry", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R10L5_C02_EG3", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R10L5_C02_T5_4B_PRICE_ONLY_EVENT_PEAK", "case_id": "R10L5_CASE02_HYUNDAI_CONSTRUCTION_NEOM_EVENT", "symbol": "000720", "company_name": "현대건설", "round": "R10", "loop": "5", "sector": "건설·부동산·건자재", "primary_archetype": "MEGA_PROJECT_NEOM_POLICY_EVENT_PREMIUM", "trigger_type": "4B", "trigger_date": "2022-11-14", "evidence_available_at_that_date": "가격-only local blowoff. 비가격 4B evidence는 약하므로 full 4B가 아니라 event-premium watch.", "evidence_source": "stock-web rows 2022-11-14 onward; public NEOM theme flow", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000720/2022.csv", "profile_path": "atlas/symbol_profiles/000/000720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-11-14", "entry_price": 43550, "MFE_30D_pct": 2.1, "MFE_90D_pct": 2.1, "MFE_180D_pct": 2.1, "MFE_1Y_pct": 2.1, "MFE_2Y_pct": 2.1, "MAE_30D_pct": -16.3, "MAE_90D_pct": -25.3, "MAE_180D_pct": -25.3, "MAE_1Y_pct": -25.3, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-11-14", "peak_price": 44450, "drawdown_after_peak_pct": -27.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_watch_not_full_exit", "four_b_evidence_type": "price_only|positioning_overheat", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "event_premium", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R10L5_C02_EG3", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "trigger_id": "R10L5_C03_T1_STAGE2_QUALITY_INCIDENT", "case_id": "R10L5_CASE03_GS_CONSTRUCTION_QUALITY_4C", "symbol": "006360", "company_name": "GS건설", "round": "R10", "loop": "5", "sector": "건설·부동산·건자재", "primary_archetype": "CONSTRUCTION_QUALITY_SAFETY_THESIS_BREAK", "trigger_type": "Stage2", "trigger_date": "2023-04-29", "evidence_available_at_that_date": "검단 아파트 지하주차장 붕괴 이후 quality/safety risk가 공개적으로 발생. 주말 발생으로 다음 거래일 종가 진입.", "evidence_source": "Korea public news/MOLIT investigation flow; stock-web rows 2023-05-02 onward", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv", "profile_path": "atlas/symbol_profiles/006/006360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-05-02", "entry_price": 20500, "MFE_30D_pct": 8.0, "MFE_90D_pct": 8.0, "MFE_180D_pct": 8.0, "MFE_1Y_pct": 12.0, "MFE_2Y_pct": 12.0, "MAE_30D_pct": -2.4, "MAE_90D_pct": -33.2, "MAE_180D_pct": -38.2, "MAE_1Y_pct": -38.2, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-05-24", "peak_price": 22150, "drawdown_after_peak_pct": -42.8, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "thesis_break", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R10L5_C03_EG1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R10L5_C03_T5_4B_QUALITY_OVERHANG_COST_WATCH", "case_id": "R10L5_CASE03_GS_CONSTRUCTION_QUALITY_4C", "symbol": "006360", "company_name": "GS건설", "round": "R10", "loop": "5", "sector": "건설·부동산·건자재", "primary_archetype": "CONSTRUCTION_QUALITY_SAFETY_THESIS_BREAK", "trigger_type": "4B", "trigger_date": "2023-06-29", "evidence_available_at_that_date": "사고조사/품질 리스크가 비용 인식 가능성으로 번지는 watch.", "evidence_source": "stock-web rows 2023-06-29 onward; public investigation/cost coverage", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv", "profile_path": "atlas/symbol_profiles/006/006360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-29", "entry_price": 18600, "MFE_30D_pct": 3.1, "MFE_90D_pct": 3.1, "MFE_180D_pct": -0.0, "MFE_1Y_pct": 23.4, "MFE_2Y_pct": 23.4, "MAE_30D_pct": -26.3, "MAE_90D_pct": -31.9, "MAE_180D_pct": -31.9, "MAE_1Y_pct": -31.9, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-20", "peak_price": 22950, "drawdown_after_peak_pct": "not_observed_after_manifest_max", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.45, "four_b_full_window_peak_proximity": 0.45, "four_b_timing_verdict": "quality_4B_watch_before_cost_confirmation", "four_b_evidence_type": "legal_or_regulatory_block|margin_or_backlog_slowdown", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "thesis_break", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R10L5_C03_EG2", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "trigger_id": "R10L5_C03_T6_4C_FULL_RECONSTRUCTION_COST", "case_id": "R10L5_CASE03_GS_CONSTRUCTION_QUALITY_4C", "symbol": "006360", "company_name": "GS건설", "round": "R10", "loop": "5", "sector": "건설·부동산·건자재", "primary_archetype": "CONSTRUCTION_QUALITY_SAFETY_THESIS_BREAK", "trigger_type": "4C", "trigger_date": "2023-07-05", "evidence_available_at_that_date": "검단 단지 전면 재시공/비용 인식이 공개되며 thesis break가 하드하게 닫힘.", "evidence_source": "public Korea press/company disclosure flow; stock-web rows 2023-07-06 onward", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv", "profile_path": "atlas/symbol_profiles/006/006360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-06", "entry_price": 14520, "MFE_30D_pct": 5.6, "MFE_90D_pct": 3.9, "MFE_180D_pct": 19.8, "MFE_1Y_pct": 58.1, "MFE_2Y_pct": 58.1, "MAE_30D_pct": -7.7, "MAE_90D_pct": -12.9, "MAE_180D_pct": -12.9, "MAE_1Y_pct": -12.9, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-20", "peak_price": 22950, "drawdown_after_peak_pct": "not_observed_after_manifest_max", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "legal_or_regulatory_block|margin_or_backlog_slowdown", "four_c_protection_label": "hard_4c_late_but_valid", "trigger_outcome_label": "hard_4c_late", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R10L5_C03_EG3", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only"}
{"row_type": "trigger", "trigger_id": "R10L5_C04_T1_HWAJEONG_COLLAPSE_4C", "case_id": "R10L5_CASE04_HDC_QUALITY_4C", "symbol": "294870", "company_name": "HDC현대산업개발", "round": "R10", "loop": "5", "sector": "건설·부동산·건자재", "primary_archetype": "BRAND_TRUST_CONSTRUCTION_ACCIDENT_THESIS_BREAK", "trigger_type": "4C", "trigger_date": "2022-01-11", "evidence_available_at_that_date": "광주 화정 아이파크 외벽 붕괴. 장마감 후 발생 성격이므로 다음 거래일 종가 기준.", "evidence_source": "Gwangju Hwajeong I-Park exterior wall collapse source; stock-web rows 2022-01-12 onward", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv", "profile_path": "atlas/symbol_profiles/294/294870.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-01-12", "entry_price": 20850, "MFE_30D_pct": 8.9, "MFE_90D_pct": 8.9, "MFE_180D_pct": 8.9, "MFE_1Y_pct": 8.9, "MFE_2Y_pct": 15.3, "MAE_30D_pct": -35.3, "MAE_90D_pct": -36.9, "MAE_180D_pct": -49.2, "MAE_1Y_pct": -49.2, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-01-12", "peak_price": 22700, "drawdown_after_peak_pct": -52.4, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "legal_or_regulatory_block|accounting_trust_risk", "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "hard_4c_success", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R10L5_C04_EG1", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only"}
{"row_type": "trigger", "trigger_id": "R10L5_C04_T5_INVESTIGATION_QUALITY_RISK", "case_id": "R10L5_CASE04_HDC_QUALITY_4C", "symbol": "294870", "company_name": "HDC현대산업개발", "round": "R10", "loop": "5", "sector": "건설·부동산·건자재", "primary_archetype": "BRAND_TRUST_CONSTRUCTION_ACCIDENT_THESIS_BREAK", "trigger_type": "4B", "trigger_date": "2022-03-14", "evidence_available_at_that_date": "정부 사고조사 결과/부실시공 논리 공개. 이미 4C 뒤지만 quality-risk overlay로 재확인.", "evidence_source": "Gwangju investigation public reporting; stock-web rows 2022-03-14 onward", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv", "profile_path": "atlas/symbol_profiles/294/294870.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-03-14", "entry_price": 16400, "MFE_30D_pct": 7.0, "MFE_90D_pct": 7.0, "MFE_180D_pct": 7.0, "MFE_1Y_pct": 7.0, "MFE_2Y_pct": 46.6, "MAE_30D_pct": -10.1, "MAE_90D_pct": -29.3, "MAE_180D_pct": -35.4, "MAE_1Y_pct": -35.4, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-20", "peak_price": 24050, "drawdown_after_peak_pct": -52.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.34, "four_b_full_window_peak_proximity": 0.34, "four_b_timing_verdict": "late_quality_4B_after_4C", "four_b_evidence_type": "legal_or_regulatory_block|margin_or_backlog_slowdown", "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "hard_4c_late", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R10L5_C04_EG2", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "trigger_id": "R10L5_C04_T6_ADMIN_SANCTION_4C_CONFIRM", "case_id": "R10L5_CASE04_HDC_QUALITY_4C", "symbol": "294870", "company_name": "HDC현대산업개발", "round": "R10", "loop": "5", "sector": "건설·부동산·건자재", "primary_archetype": "BRAND_TRUST_CONSTRUCTION_ACCIDENT_THESIS_BREAK", "trigger_type": "4C", "trigger_date": "2022-03-29", "evidence_available_at_that_date": "영업정지/행정제재 관련 보도와 공시성 리스크가 4C를 재확인.", "evidence_source": "public Korea administrative sanction reporting; stock-web rows 2022-03-29 onward", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv", "profile_path": "atlas/symbol_profiles/294/294870.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-03-29", "entry_price": 15250, "MFE_30D_pct": 6.6, "MFE_90D_pct": 6.6, "MFE_180D_pct": 6.6, "MFE_1Y_pct": 6.6, "MFE_2Y_pct": 57.7, "MAE_30D_pct": -13.8, "MAE_90D_pct": -30.2, "MAE_180D_pct": -30.2, "MAE_1Y_pct": -30.2, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-20", "peak_price": 24050, "drawdown_after_peak_pct": -52.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "legal_or_regulatory_block", "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "hard_4c_late", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D", "same_entry_group_id": "R10L5_C04_EG3", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only"}
```

### 27.4 Score simulation rows JSONL

```jsonl
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L5_CASE01_HANSEM_COVID_REMODELING", "trigger_id": "R10L5_C01_T1_STAGE2_EARLY_REMODELING_DEMAND", "symbol": "009240", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 0}, "weighted_score_before": 13, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 4, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 0}, "weighted_score_after": 17, "stage_label_after": "Stage2", "changed_components": ["relative_strength_score", "revision_score"], "component_delta_explanation": "after profile boosts early RS/revision for proven Stage2 entries and boosts legal/thesis-break risk for construction quality events; no production score changed.", "selected_by_profile": true, "MFE_90D_pct": 106.5, "MAE_90D_pct": -0.5, "score_return_alignment_label": "score_low_return_high_missed_structural"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L5_CASE01_HANSEM_COVID_REMODELING", "trigger_id": "R10L5_C01_T2_STAGE2_ACTIONABLE_Q1_DEMAND", "symbol": "009240", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 0}, "weighted_score_before": 13, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 0}, "weighted_score_after": 13, "stage_label_after": "Stage2", "changed_components": [], "component_delta_explanation": "after profile boosts early RS/revision for proven Stage2 entries and boosts legal/thesis-break risk for construction quality events; no production score changed.", "selected_by_profile": false, "MFE_90D_pct": 43.6, "MAE_90D_pct": -3.7, "score_return_alignment_label": "score_low_return_high_missed_structural"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L5_CASE01_HANSEM_COVID_REMODELING", "trigger_id": "R10L5_C01_T3_STAGE3_YELLOW_RS_EARNINGS", "symbol": "009240", "trigger_type": "Stage3-Yellow", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 0}, "weighted_score_before": 13, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 0}, "weighted_score_after": 13, "stage_label_after": "Stage2", "changed_components": [], "component_delta_explanation": "after profile boosts early RS/revision for proven Stage2 entries and boosts legal/thesis-break risk for construction quality events; no production score changed.", "selected_by_profile": false, "MFE_90D_pct": 30.0, "MAE_90D_pct": -15.7, "score_return_alignment_label": "score_low_return_high_missed_structural"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L5_CASE01_HANSEM_COVID_REMODELING", "trigger_id": "R10L5_C01_T4_STAGE3_GREEN_CONFIRMED_RERATING", "symbol": "009240", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 0}, "weighted_score_before": 13, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 0}, "weighted_score_after": 13, "stage_label_after": "Stage2", "changed_components": [], "component_delta_explanation": "after profile boosts early RS/revision for proven Stage2 entries and boosts legal/thesis-break risk for construction quality events; no production score changed.", "selected_by_profile": false, "MFE_90D_pct": 11.3, "MAE_90D_pct": -10.0, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L5_CASE01_HANSEM_COVID_REMODELING", "trigger_id": "R10L5_C01_T5_4B_CONTROL_PREMIUM_BLOWOFF", "symbol": "009240", "trigger_type": "4B", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 8, "thesis_break_score": 5}, "weighted_score_before": 22, "stage_label_before": "4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 8, "thesis_break_score": 7}, "weighted_score_after": 26, "stage_label_after": "4B-watch", "changed_components": ["legal_or_contract_risk_score", "thesis_break_score"], "component_delta_explanation": "after profile boosts early RS/revision for proven Stage2 entries and boosts legal/thesis-break risk for construction quality events; no production score changed.", "selected_by_profile": false, "MFE_90D_pct": 1.7, "MAE_90D_pct": -43.0, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L5_CASE02_HYUNDAI_CONSTRUCTION_NEOM_EVENT", "trigger_id": "R10L5_C02_T1_STAGE2_NEOM_AWARENESS", "symbol": "000720", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 0}, "weighted_score_before": 18, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 4, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 0}, "weighted_score_after": 22, "stage_label_after": "Stage2-Actionable", "changed_components": ["relative_strength_score", "revision_score"], "component_delta_explanation": "after profile boosts early RS/revision for proven Stage2 entries and boosts legal/thesis-break risk for construction quality events; no production score changed.", "selected_by_profile": true, "MFE_90D_pct": 19.3, "MAE_90D_pct": -12.6, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L5_CASE02_HYUNDAI_CONSTRUCTION_NEOM_EVENT", "trigger_id": "R10L5_C02_T2_STAGE2_ACTIONABLE_POLICY_RS", "symbol": "000720", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 0}, "weighted_score_before": 10, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 0}, "weighted_score_after": 10, "stage_label_after": "Stage2", "changed_components": [], "component_delta_explanation": "after profile boosts early RS/revision for proven Stage2 entries and boosts legal/thesis-break risk for construction quality events; no production score changed.", "selected_by_profile": false, "MFE_90D_pct": 9.2, "MAE_90D_pct": -20.1, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L5_CASE02_HYUNDAI_CONSTRUCTION_NEOM_EVENT", "trigger_id": "R10L5_C02_T4_STAGE3_GREEN_TOO_LATE_NEOM", "symbol": "000720", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 0}, "weighted_score_before": 15, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 0}, "weighted_score_after": 15, "stage_label_after": "Stage2", "changed_components": [], "component_delta_explanation": "after profile boosts early RS/revision for proven Stage2 entries and boosts legal/thesis-break risk for construction quality events; no production score changed.", "selected_by_profile": false, "MFE_90D_pct": 2.1, "MAE_90D_pct": -25.3, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L5_CASE02_HYUNDAI_CONSTRUCTION_NEOM_EVENT", "trigger_id": "R10L5_C02_T5_4B_PRICE_ONLY_EVENT_PEAK", "symbol": "000720", "trigger_type": "4B", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 8, "thesis_break_score": 5}, "weighted_score_before": 22, "stage_label_before": "4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 8, "thesis_break_score": 7}, "weighted_score_after": 26, "stage_label_after": "4B-watch", "changed_components": ["legal_or_contract_risk_score", "thesis_break_score"], "component_delta_explanation": "after profile boosts early RS/revision for proven Stage2 entries and boosts legal/thesis-break risk for construction quality events; no production score changed.", "selected_by_profile": false, "MFE_90D_pct": 2.1, "MAE_90D_pct": -25.3, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L5_CASE03_GS_CONSTRUCTION_QUALITY_4C", "trigger_id": "R10L5_C03_T1_STAGE2_QUALITY_INCIDENT", "symbol": "006360", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 0}, "weighted_score_before": 10, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 0}, "weighted_score_after": 10, "stage_label_after": "Stage2", "changed_components": [], "component_delta_explanation": "after profile boosts early RS/revision for proven Stage2 entries and boosts legal/thesis-break risk for construction quality events; no production score changed.", "selected_by_profile": true, "MFE_90D_pct": 8.0, "MAE_90D_pct": -33.2, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L5_CASE03_GS_CONSTRUCTION_QUALITY_4C", "trigger_id": "R10L5_C03_T5_4B_QUALITY_OVERHANG_COST_WATCH", "symbol": "006360", "trigger_type": "4B", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 8, "thesis_break_score": 5}, "weighted_score_before": 22, "stage_label_before": "4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 8, "thesis_break_score": 7}, "weighted_score_after": 26, "stage_label_after": "4B-watch", "changed_components": ["legal_or_contract_risk_score", "thesis_break_score"], "component_delta_explanation": "after profile boosts early RS/revision for proven Stage2 entries and boosts legal/thesis-break risk for construction quality events; no production score changed.", "selected_by_profile": false, "MFE_90D_pct": 3.1, "MAE_90D_pct": -31.9, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L5_CASE03_GS_CONSTRUCTION_QUALITY_4C", "trigger_id": "R10L5_C03_T6_4C_FULL_RECONSTRUCTION_COST", "symbol": "006360", "trigger_type": "4C", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 9}, "weighted_score_before": 19, "stage_label_before": "4C", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 11}, "weighted_score_after": 23, "stage_label_after": "4C", "changed_components": ["legal_or_contract_risk_score", "thesis_break_score"], "component_delta_explanation": "after profile boosts early RS/revision for proven Stage2 entries and boosts legal/thesis-break risk for construction quality events; no production score changed.", "selected_by_profile": false, "MFE_90D_pct": 3.9, "MAE_90D_pct": -12.9, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L5_CASE04_HDC_QUALITY_4C", "trigger_id": "R10L5_C04_T1_HWAJEONG_COLLAPSE_4C", "symbol": "294870", "trigger_type": "4C", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 9}, "weighted_score_before": 19, "stage_label_before": "4C", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 11}, "weighted_score_after": 23, "stage_label_after": "4C", "changed_components": ["legal_or_contract_risk_score", "thesis_break_score"], "component_delta_explanation": "after profile boosts early RS/revision for proven Stage2 entries and boosts legal/thesis-break risk for construction quality events; no production score changed.", "selected_by_profile": true, "MFE_90D_pct": 8.9, "MAE_90D_pct": -36.9, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L5_CASE04_HDC_QUALITY_4C", "trigger_id": "R10L5_C04_T5_INVESTIGATION_QUALITY_RISK", "symbol": "294870", "trigger_type": "4B", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 8, "thesis_break_score": 5}, "weighted_score_before": 22, "stage_label_before": "4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 8, "thesis_break_score": 7}, "weighted_score_after": 26, "stage_label_after": "4B-watch", "changed_components": ["legal_or_contract_risk_score", "thesis_break_score"], "component_delta_explanation": "after profile boosts early RS/revision for proven Stage2 entries and boosts legal/thesis-break risk for construction quality events; no production score changed.", "selected_by_profile": false, "MFE_90D_pct": 7.0, "MAE_90D_pct": -29.3, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R10L5_CASE04_HDC_QUALITY_4C", "trigger_id": "R10L5_C04_T6_ADMIN_SANCTION_4C_CONFIRM", "symbol": "294870", "trigger_type": "4C", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 9}, "weighted_score_before": 19, "stage_label_before": "4C", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 0, "order_intake_quality_score": 0, "positioning_overheat_score": 1, "thesis_break_score": 11}, "weighted_score_after": 23, "stage_label_after": "4C", "changed_components": ["legal_or_contract_risk_score", "thesis_break_score"], "component_delta_explanation": "after profile boosts early RS/revision for proven Stage2 entries and boosts legal/thesis-break risk for construction quality events; no production score changed.", "selected_by_profile": false, "MFE_90D_pct": 6.6, "MAE_90D_pct": -30.2, "score_return_alignment_label": "score_mid_return_low_watch_only"}
```

### 27.5 Profile comparison rows CSV

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,4,4,2,6.7,6.7,-17.6,-17.6,9.2,-17.6,0.0,0.5,0.25,1,2,0.64,split_overlay,split_overlay,reference
profile_comparison,r10_stage2_actionable_quality_guard,4,4,3,44.6,19.3,-15.4,-12.6,44.6,-17.1,0.33,0.33,0.0,0,0,0.34,split_overlay,split_overlay,best mixed entry/risk profile
profile_comparison,stage3_yellow_entry_relaxed,4,4,3,15.7,9.2,-23.0,-20.1,17.7,-24.7,0.33,1.0,0.0,0,0,0.34,split_overlay,split_overlay,Allow Yellow when one evidence gate is missing but RS and revision/customer evidence are strong.
profile_comparison,green_confirmation_timing_relaxed,4,4,3,20.3,9.2,-19.0,-20.1,22.4,-20.7,0.33,0.67,0.0,0,0,0.34,split_overlay,split_overlay,Shift Green threshold earlier but still require non-price evidence; rejects pure NEOM price chase.
profile_comparison,four_b_peak_timing_tuned,4,4,0,3.5,2.6,-32.4,-30.6,2.7,-33.9,0.0,1.0,0.0,0,0,0.34,split_overlay,split_overlay,"Split price-only local 4B from non-price 4B; keep Hansem full-window 4B, Hyundai price-only watch."
profile_comparison,four_c_thesis_break_earlier,4,4,1,8.0,8.0,-33.2,-33.2,8.0,-38.2,0.0,1.0,0.0,0,0,0.34,split_overlay,split_overlay,"Quality/safety/legal accidents trigger 4C watch at incident date, not only after cost or sanction confirmation."
```

### 27.6 Shadow weight CSV

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_early_revision_plus_RS,0,3,+3,Hansem Stage2 produced MFE90 106.5 with MAE90 -0.5; Green had only MFE90 11.3 with deeper MAE.,"For structural interior/remodeling, early Stage2 improved 90D upside capture by about +95pp versus Green while avoiding added drawdown.",R10L5_C01_T1_STAGE2_EARLY_REMODELING_DEMAND|R10L5_C01_T4_STAGE3_GREEN_CONFIRMED_RERATING,2,shadow-only; production unchanged
shadow_weight,price_only_megaproject_event_cap,0,-2,-2,Hyundai Construction NEOM Green near local peak had MFE90 2.1 and MAE90 -25.3.,Rejects converting price-only policy/event premium into full Green without contract/backlog/margin bridge.,R10L5_C02_T4_STAGE3_GREEN_TOO_LATE_NEOM|R10L5_C02_T5_4B_PRICE_ONLY_EVENT_PEAK,2,shadow-only; production unchanged
shadow_weight,construction_quality_incident_4c_watch,0,3,+3,GS and HDC quality/safety incidents preceded deep MAE drawdowns when treated early.,Moves quality accident from late confirmation to 4C-watch immediately; HDC avoided a further observed MAE180 near -49.2 from incident entry.,R10L5_C03_T1_STAGE2_QUALITY_INCIDENT|R10L5_C04_T1_HWAJEONG_COLLAPSE_4C,2,shadow-only; production unchanged
shadow_weight,non_price_4b_required_for_full_exit,0,2,+2,Hansem had control premium/valuation/positioning 4B near full-window peak; Hyundai had price-only event premium.,Splitting local price-only from full 4B reduces premature exit on event themes while retaining true blowoff/overhang detection.,R10L5_C01_T5_4B_CONTROL_PREMIUM_BLOWOFF|R10L5_C02_T5_4B_PRICE_ONLY_EVENT_PEAK,2,shadow-only; production unchanged
shadow_weight,legal_regulatory_thesis_break_hard_gate,0,2,+2,GS/HDC safety and legal-regulatory evidence directly broke construction-quality thesis.,Improves drawdown-protection tagging; does not convert narrative-only risk into weight change without OHLC window.,R10L5_C03_T6_4C_FULL_RECONSTRUCTION_COST|R10L5_C04_T6_ADMIN_SANCTION_4C_CONFIRM,2,shadow-only; production unchanged
```

### 27.7 Optimization decision rows JSONL

```jsonl
{"row_type": "optimization_decision", "decision_id": "R10L5_DEC01", "hypothesis": "Early demand/revision + RS should promote Stage2 to Actionable in interior/materials recovery cases.", "tested_trigger_ids": ["R10L5_C01_T1_STAGE2_EARLY_REMODELING_DEMAND", "R10L5_C01_T4_STAGE3_GREEN_CONFIRMED_RERATING"], "baseline_profile": "baseline_current_proxy", "selected_profile": "r10_stage2_actionable_quality_guard", "backtest_result_summary": "Hansem early Stage2 MFE90 106.5 / MAE90 -0.5 versus Green MFE90 11.3 / MAE90 -10.0.", "accepted_or_rejected": "accepted", "delta_magnitude": "+3", "why_not_larger_delta": "Only one clean structural-success interior case in this R10 loop.", "risks": "May over-promote one-off COVID demand without revision evidence.", "next_validation_needed": "Find non-COVID remodeling/materials counterexample."}
{"row_type": "optimization_decision", "decision_id": "R10L5_DEC02", "hypothesis": "Price-only mega-project event premium should not become full Green without contract/backlog/margin bridge.", "tested_trigger_ids": ["R10L5_C02_T1_STAGE2_NEOM_AWARENESS", "R10L5_C02_T4_STAGE3_GREEN_TOO_LATE_NEOM"], "baseline_profile": "baseline_current_proxy", "selected_profile": "r10_stage2_actionable_quality_guard", "backtest_result_summary": "Hyundai Stage2 had MFE90 19.3 / MAE90 -12.6, while Green near peak had MFE90 2.1 / MAE90 -25.3.", "accepted_or_rejected": "accepted", "delta_magnitude": "-2", "why_not_larger_delta": "The Stage2 event itself had positive MFE; reject only Green promotion, not watchlist awareness.", "risks": "Real contract announcements could justify promotion in other cases.", "next_validation_needed": "Test Saudi/NEOM actual-contract winners separately."}
{"row_type": "optimization_decision", "decision_id": "R10L5_DEC03", "hypothesis": "Construction quality/safety event with legal/regulatory consequence should trigger immediate 4C-watch.", "tested_trigger_ids": ["R10L5_C03_T1_STAGE2_QUALITY_INCIDENT", "R10L5_C04_T1_HWAJEONG_COLLAPSE_4C"], "baseline_profile": "baseline_current_proxy", "selected_profile": "four_c_thesis_break_earlier", "backtest_result_summary": "GS initial incident led to MAE90 -33.2; HDC incident led to MAE180 -49.2. Later confirmation rows were too late for full protection.", "accepted_or_rejected": "accepted", "delta_magnitude": "+3", "why_not_larger_delta": "Small sample of two quality accidents; keep as watch/hard-gate pair, not generic construction-risk penalty.", "risks": "False breaks from minor accidents or non-material project issues.", "next_validation_needed": "Compare with minor non-fatal site accidents that did not impair stock path."}
```

### 27.8 Narrative-only rows JSONL

```jsonl
{"row_type":"narrative_only","case_id":"R10L5_NARRATIVE_ONLY_PF_RISK","symbol":"universe","reason":"PF/부동산 금융 리스크는 이번 loop에서 OHLC-anchored hard trigger로 충분히 닫지 못했으므로 weight calibration에 사용하지 않는다.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

### 27.9 Aggregate metric rows CSV

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,below_entry_90D_rate,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,4B,4,0,3.5,2.6,-32.4,-30.6,2.7,-33.9,1.0,not_applicable,overlay_only,overlay_only,representative rows only; duplicate same-entry labels excluded
aggregate_metric,4C,3,0,6.5,6.6,-26.7,-30.2,11.8,-30.8,1.0,not_applicable,not_applicable,not_applicable,representative rows only; duplicate same-entry labels excluded
aggregate_metric,Stage2,3,3,44.6,19.3,-15.4,-12.6,44.6,-17.1,0.67,not_applicable,not_applicable,not_applicable,representative rows only; duplicate same-entry labels excluded
aggregate_metric,Stage2-Actionable,2,2,26.4,26.4,-11.9,-11.9,29.6,-11.9,1.0,not_applicable,not_applicable,not_applicable,representative rows only; duplicate same-entry labels excluded
aggregate_metric,Stage3-Green,2,2,6.7,6.7,-17.6,-17.6,9.2,-17.6,1.0,not_applicable,not_applicable,not_applicable,representative rows only; duplicate same-entry labels excluded
aggregate_metric,Stage3-Yellow,1,1,30.0,30.0,-15.7,-15.7,35.8,-15.7,1.0,not_applicable,not_applicable,not_applicable,representative rows only; duplicate same-entry labels excluded
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
current_round = R10
current_loop = 5
next_round = R11
next_sector = 정책·지정학·재난·이벤트
best_shadow_profile = r10_stage2_actionable_quality_guard
production_scoring_changed = false
```

## 30. Source Notes

- Stock-Web manifest/schema/profile/tradable-row paths are from `Songdaiki/stock-web` using price basis `tradable_raw` and `raw_unadjusted_marcap`.
- Stock-web manifest max date used for forward-window gating: 2026-02-20.
- Price rows referenced include:
  - `atlas/ohlcv_tradable_by_symbol_year/009/009240/2020.csv`, `2021.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/000/000720/2022.csv`, `2023.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv`
- Public evidence references used for narrative anchoring include Hanssem company profile, public Korea press/analyst coverage on home-interior demand, public NEOM/Saudi construction-theme coverage, public GS Geomdan collapse/reconstruction coverage, and the Gwangju Hwajeong I-Park collapse reference.
- This MD is not investment advice and contains no current/live candidate recommendation.
