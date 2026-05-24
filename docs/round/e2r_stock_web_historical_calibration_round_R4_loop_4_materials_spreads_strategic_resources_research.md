# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata

- research_session: historical_calibration_after_stock_web_ohlc_breakthrough
- round: R4
- loop: 2
- sector: 소재·스프레드·전략자원
- output_format: one_standalone_markdown_file
- stock_agent_repo_access_allowed: false
- stock_agent_code_patch_allowed: false
- production_scoring_changed: false
- shadow_weight_only: true
- generated_file: `e2r_stock_web_historical_calibration_round_R4_loop_2_materials_spreads_strategic_resources_research.md`

## 1. Round Scope

이번 라운드는 R4 Loop 2다. R4 Loop 1의 대표 소재 case를 반복해 늘리는 것보다, **spread / margin bridge / strategic-resource event premium**의 차이를 분리하는 데 초점을 맞췄다. 목적은 Stage2-Actionable 조기 승격이 유효한 소재 case와, 가격만 먼저 오른 strategic resource event를 E2R structural rerating으로 오인하는 case를 동시에 검증하는 것이다.

## 2. Stock-Web OHLC Input / Price Source Validation

|field|value|
|---|---|
|source|Songdaiki/stock-web|
|manifest_max_date|2026-02-20|
|price_basis|tradable_raw|
|price_adjustment_status|raw_unadjusted_marcap|
|calibration_shard_root|atlas/ohlcv_tradable_by_symbol_year|
|raw_shard_root|atlas/ohlcv_raw_by_symbol_year|
|schema_columns|d,o,h,l,c,v,a,mc,s,m|
|validation_status|usable_for_historical_calibration|

Manifest에서 확인한 max_date는 2026-02-20이며, 모든 forward-window 판단은 이 날짜 기준이다. 가격 row는 raw/unadjusted marcap basis이므로 corporate-action candidate window는 기본적으로 block한다. 이번 테스트 window는 각 profile의 오래된 corporate-action candidate 날짜와 겹치지 않는다.

## 3. Historical Eligibility Gate

|rule|status|
|---|---|
|entry row exists|passed for all usable triggers|
|forward 180 trading days|passed for all usable triggers|
|MFE/MAE 30/90/180D computed|passed|
|corporate-action contaminated 180D window|none in tested windows|
|latest/live candidate included|false|

## 4. Canonical Archetypes Tested

|canonical archetype|mechanism|why R4|
|---|---|---|
|SPREAD_MARGIN_RERATING|원재료/제품 spread가 개선되고 OP revision이 따라붙는 구조|소재 cycle에서 Green confirmation이 늦는지 검증|
|LATEX_SPREAD_EPS_EXPLOSION|제품 가격/수요가 EPS를 급격히 바꾸는 구조|Stage2-Actionable 조기 승격 후보|
|PETROCHEMICAL_SPREAD_MEAN_REVERSION|spread 반등은 크지만 지속성이 낮은 cycle|false_positive_score 및 Green guardrail|
|STRATEGIC_RESOURCE_EVENT_PREMIUM|희토류/전략자원 event premium|price-only event와 structural rerating 분리|

## 5. Case Selection Summary

|case_id|symbol|company|case_type|archetype|best_trigger|note|
|---|---|---|---|---|---|---|
|R4L2-C1-HYOSUNG_TNC_SPANDEX_2020|298020|효성티앤씨|structural_success|SPREAD_MARGIN_RERATING|R4L2-C1-T2|Stage2-Actionable spread+RS+margin bridge가 Green보다 훨씬 좋은 entry.|
|R4L2-C2-KUMHO_PETRO_NB_LATEX_2020|011780|금호석유화학|structural_success|LATEX_SPREAD_EPS_EXPLOSION|R4L2-C2-T2|NB latex spread 초기 evidence가 Green보다 우월.|
|R4L2-C3-KPIC_ETHYLENE_SPREAD_2021|006650|대한유화|cyclical_success_then_false_positive|PETROCHEMICAL_SPREAD_MEAN_REVERSION|R4L2-C3-T2|Stage2는 수익을 줬지만 Green은 peak 부근 false positive. cycle guardrail 필요.|
|R4L2-C4-UNION_MATERIAL_RARE_EARTH_2023|047400|유니온머티리얼|event_premium_overheat|STRATEGIC_RESOURCE_EVENT_PREMIUM|none_for_weight|MFE는 크지만 price-only event. weight 승격 근거로 사용 금지.|

## 6. Evidence Source Map

가격은 stock-web이고, trigger label은 당시 공개됐다고 볼 수 있는 공시/뉴스/리포트/실적자료를 research proxy로 해석했다. 원자료 URL을 live 탐색하거나 현재 후보 스캔하지 않았으며, stock_agent repo도 열지 않았다.

|case|evidence channels used|price source|
|---|---|---|
|효성티앤씨|스판덱스 spread, 업황/실적 preview, IR/리포트 proxy|stock-web 298020 2020/2021 OHLC|
|금호석유화학|NB latex 수요, 합성고무/페놀 spread, 실적 preview proxy|stock-web 011780 2020/2021 OHLC|
|대한유화|ethylene/PE/PP spread, valuation, cycle reversal watch|stock-web 006650 2021 OHLC|
|유니온머티리얼|희토류/전략자원 event headlines, price/volume only evidence|stock-web 047400 2023 OHLC|

## 7. Price Data Source Map

|item|path|note|
|---|---|---|
|manifest/schema|atlas/manifest.json / atlas/schema.json|max_date=2026-02-20, raw_unadjusted_marcap, tradable_raw calibration shards|
|효성티앤씨|atlas/symbol_profiles/298/298020.json; atlas/ohlcv_tradable_by_symbol_year/298/298020/2020.csv; /2021.csv|No corporate-action candidate in tested window; entry rows observed around 2020-09-15 and 2021-02-01.|
|금호석유화학|atlas/symbol_profiles/011/011780.json; atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv; /2021.csv|Profile has old 2001 corporate-action caveat; tested 2020-2021 window is clean for 180D calibration.|
|대한유화|atlas/symbol_profiles/006/006650.json; atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv|Profile has old 2010 corporate-action caveat; tested 2021 window is clean for 180D calibration.|
|유니온머티리얼|atlas/symbol_profiles/047/047400.json; atlas/ohlcv_tradable_by_symbol_year/047/047400/2023.csv|Profile has old 2011 corporate-action caveat; tested 2023 window is clean for 180D calibration.|

## 8. Case-by-Case Trigger Grid

|trigger_id|case_id|symbol|company|type|trigger_date|entry_date|entry_price|MFE30|MFE90|MFE180|MAE90|peak_date|peak_price|DD_after_peak|green_late|4B_local|4B_full|outcome|usable|same_entry_group|dedupe|role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R4L2-C1-T1|R4L2-C1-HYOSUNG_TNC_SPANDEX_2020|298020|효성티앤씨|Stage2|2020-09-15|2020-09-15|120,000|30.4|177.1|562.5|-7.5|2021-07-16|963,000|-60.5|not_applicable|not_applicable|not_applicable|missed_structural|true|R4L2-C1-G1-20200915-120000|false|label_comparison_only|
|R4L2-C1-T2|R4L2-C1-HYOSUNG_TNC_SPANDEX_2020|298020|효성티앤씨|Stage2-Actionable|2020-09-15|2020-09-15|120,000|30.4|177.1|562.5|-7.5|2021-07-16|963,000|-60.5|not_applicable|not_applicable|not_applicable|excellent_entry|true|R4L2-C1-G1-20200915-120000|true|representative|
|R4L2-C1-T3|R4L2-C1-HYOSUNG_TNC_SPANDEX_2020|298020|효성티앤씨|Stage3-Yellow|2021-01-15|2021-01-15|250,000|101.2|224.0|285.2|-4.0|2021-07-16|963,000|-60.5|not_applicable|not_applicable|not_applicable|good_entry|true|R4L2-C1-G2-20210115-250000|true|representative|
|R4L2-C1-T4|R4L2-C1-HYOSUNG_TNC_SPANDEX_2020|298020|효성티앤씨|Stage3-Green|2021-02-01|2021-02-01|389,000|29.3|108.2|147.6|-12.9|2021-07-16|963,000|-60.5|0.3|not_applicable|not_applicable|late_entry|true|R4L2-C1-G3-20210201-389000|true|representative|
|R4L2-C1-T5|R4L2-C1-HYOSUNG_TNC_SPANDEX_2020|298020|효성티앤씨|Stage4B|2021-07-16|2021-07-16|881,000|9.4|9.4|9.4|-32.0|2021-07-16|963,000|-60.5|not_applicable|0.9|0.9|overheat|true|R4L2-C1-G4-20210716-881000|false|4B_overlay_only|
|R4L2-C2-T1|R4L2-C2-KUMHO_PETRO_NB_LATEX_2020|011780|금호석유화학|Stage2|2020-09-28|2020-09-28|106,000|43.4|176.9|181.6|-3.8|2021-05-06|298,500|-35.0|not_applicable|not_applicable|not_applicable|missed_structural|true|R4L2-C2-G1-20200928-106000|false|label_comparison_only|
|R4L2-C2-T2|R4L2-C2-KUMHO_PETRO_NB_LATEX_2020|011780|금호석유화학|Stage2-Actionable|2020-09-28|2020-09-28|106,000|43.4|176.9|181.6|-3.8|2021-05-06|298,500|-35.0|not_applicable|not_applicable|not_applicable|excellent_entry|true|R4L2-C2-G1-20200928-106000|true|representative|
|R4L2-C2-T3|R4L2-C2-KUMHO_PETRO_NB_LATEX_2020|011780|금호석유화학|Stage3-Yellow|2021-01-05|2021-01-05|162,500|80.6|83.7|83.7|-8.0|2021-05-06|298,500|-35.0|not_applicable|not_applicable|not_applicable|good_entry|true|R4L2-C2-G2-20210105-162500|true|representative|
|R4L2-C2-T4|R4L2-C2-KUMHO_PETRO_NB_LATEX_2020|011780|금호석유화학|Stage3-Green|2021-01-21|2021-01-21|186,000|60.5|60.5|60.5|-2.2|2021-05-06|298,500|-35.0|0.4|not_applicable|not_applicable|good_entry_but_later_than_yellow|true|R4L2-C2-G3-20210121-186000|true|representative|
|R4L2-C2-T5|R4L2-C2-KUMHO_PETRO_NB_LATEX_2020|011780|금호석유화학|Stage4B|2021-05-06|2021-05-06|296,000|0.8|0.8|0.8|-33.4|2021-05-06|298,500|-35.0|not_applicable|1.0|1.0|overheat|true|R4L2-C2-G4-20210506-296000|false|4B_overlay_only|
|R4L2-C3-T1|R4L2-C3-KPIC_ETHYLENE_SPREAD_2021|006650|대한유화|Stage2|2021-01-06|2021-01-06|277,000|46.4|46.4|46.4|-21.1|2021-02-17|405,500|-49.0|not_applicable|not_applicable|not_applicable|cyclical_success|true|R4L2-C3-G1-20210106-277000|false|label_comparison_only|
|R4L2-C3-T2|R4L2-C3-KPIC_ETHYLENE_SPREAD_2021|006650|대한유화|Stage2-Actionable|2021-01-06|2021-01-06|277,000|46.4|46.4|46.4|-21.1|2021-02-17|405,500|-49.0|not_applicable|not_applicable|not_applicable|good_entry_but_cyclical|true|R4L2-C3-G1-20210106-277000|true|representative|
|R4L2-C3-T3|R4L2-C3-KPIC_ETHYLENE_SPREAD_2021|006650|대한유화|Stage3-Yellow|2021-02-10|2021-02-10|373,500|8.6|8.6|8.6|-28.4|2021-02-17|405,500|-49.0|not_applicable|not_applicable|not_applicable|late_entry|true|R4L2-C3-G2-20210210-373500|true|representative|
|R4L2-C3-T4|R4L2-C3-KPIC_ETHYLENE_SPREAD_2021|006650|대한유화|Stage3-Green|2021-02-16|2021-02-16|393,500|3.0|3.0|3.0|-32.0|2021-02-17|405,500|-49.0|0.8|not_applicable|not_applicable|false_positive_score|true|R4L2-C3-G3-20210216-393500|true|representative|
|R4L2-C3-T6|R4L2-C3-KPIC_ETHYLENE_SPREAD_2021|006650|대한유화|Stage4C|2021-04-05|2021-04-05|305,000|14.8|14.8|14.8|-28.4|2021-04-27|372,500|-41.3|not_applicable|not_applicable|not_applicable|thesis_break|true|R4L2-C3-G4-20210405-305000|false|4C_overlay_only|
|R4L2-C4-T0|R4L2-C4-UNION_MATERIAL_RARE_EARTH_2023|047400|유니온머티리얼|earliest_awareness|2023-02-06|2023-02-06|2,845|20.0|177.3|177.3|-8.4|2023-05-04|7,890|-58.0|not_applicable|not_applicable|not_applicable|price_moved_without_evidence|true|R4L2-C4-G1-20230206-2845|true|representative|
|R4L2-C4-T1|R4L2-C4-UNION_MATERIAL_RARE_EARTH_2023|047400|유니온머티리얼|Stage2|2023-04-06|2023-04-06|3,725|111.8|111.8|111.8|-19.5|2023-05-04|7,890|-58.0|not_applicable|not_applicable|not_applicable|event_premium|true|R4L2-C4-G2-20230406-3725|false|label_comparison_only|
|R4L2-C4-T2|R4L2-C4-UNION_MATERIAL_RARE_EARTH_2023|047400|유니온머티리얼|Stage2-Actionable|2023-04-06|2023-04-06|3,725|111.8|111.8|111.8|-19.5|2023-05-04|7,890|-58.0|not_applicable|not_applicable|not_applicable|score_mid_return_high_promote_candidate_but_rejected_by_evidence|true|R4L2-C4-G2-20230406-3725|true|representative|
|R4L2-C4-T5|R4L2-C4-UNION_MATERIAL_RARE_EARTH_2023|047400|유니온머티리얼|Stage4B|2023-05-04|2023-05-04|6,570|20.1|20.1|20.1|-49.5|2023-05-04|7,890|-58.0|not_applicable|0.7|0.7|overheat|true|R4L2-C4-G3-20230504-6570|false|4B_overlay_only|
|R4L2-C4-T6|R4L2-C4-UNION_MATERIAL_RARE_EARTH_2023|047400|유니온머티리얼|Stage4C|2023-05-12|2023-05-12|4,990|8.6|8.6|8.6|-33.6|2023-05-26|5,430|-38.9|not_applicable|not_applicable|not_applicable|thesis_break|true|R4L2-C4-G4-20230512-4990|false|4C_overlay_only|

## 9. Trigger-Level OHLC Backtest Tables


### R4L2-C1-HYOSUNG_TNC_SPANDEX_2020

|trigger_id|case_id|symbol|company|type|trigger_date|entry_date|entry_price|MFE30|MFE90|MFE180|MAE90|peak_date|peak_price|DD_after_peak|green_late|4B_local|4B_full|outcome|usable|same_entry_group|dedupe|role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R4L2-C1-T1|R4L2-C1-HYOSUNG_TNC_SPANDEX_2020|298020|효성티앤씨|Stage2|2020-09-15|2020-09-15|120,000|30.4|177.1|562.5|-7.5|2021-07-16|963,000|-60.5|not_applicable|not_applicable|not_applicable|missed_structural|true|R4L2-C1-G1-20200915-120000|false|label_comparison_only|
|R4L2-C1-T2|R4L2-C1-HYOSUNG_TNC_SPANDEX_2020|298020|효성티앤씨|Stage2-Actionable|2020-09-15|2020-09-15|120,000|30.4|177.1|562.5|-7.5|2021-07-16|963,000|-60.5|not_applicable|not_applicable|not_applicable|excellent_entry|true|R4L2-C1-G1-20200915-120000|true|representative|
|R4L2-C1-T3|R4L2-C1-HYOSUNG_TNC_SPANDEX_2020|298020|효성티앤씨|Stage3-Yellow|2021-01-15|2021-01-15|250,000|101.2|224.0|285.2|-4.0|2021-07-16|963,000|-60.5|not_applicable|not_applicable|not_applicable|good_entry|true|R4L2-C1-G2-20210115-250000|true|representative|
|R4L2-C1-T4|R4L2-C1-HYOSUNG_TNC_SPANDEX_2020|298020|효성티앤씨|Stage3-Green|2021-02-01|2021-02-01|389,000|29.3|108.2|147.6|-12.9|2021-07-16|963,000|-60.5|0.3|not_applicable|not_applicable|late_entry|true|R4L2-C1-G3-20210201-389000|true|representative|
|R4L2-C1-T5|R4L2-C1-HYOSUNG_TNC_SPANDEX_2020|298020|효성티앤씨|Stage4B|2021-07-16|2021-07-16|881,000|9.4|9.4|9.4|-32.0|2021-07-16|963,000|-60.5|not_applicable|0.9|0.9|overheat|true|R4L2-C1-G4-20210716-881000|false|4B_overlay_only|


### R4L2-C2-KUMHO_PETRO_NB_LATEX_2020

|trigger_id|case_id|symbol|company|type|trigger_date|entry_date|entry_price|MFE30|MFE90|MFE180|MAE90|peak_date|peak_price|DD_after_peak|green_late|4B_local|4B_full|outcome|usable|same_entry_group|dedupe|role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R4L2-C2-T1|R4L2-C2-KUMHO_PETRO_NB_LATEX_2020|011780|금호석유화학|Stage2|2020-09-28|2020-09-28|106,000|43.4|176.9|181.6|-3.8|2021-05-06|298,500|-35.0|not_applicable|not_applicable|not_applicable|missed_structural|true|R4L2-C2-G1-20200928-106000|false|label_comparison_only|
|R4L2-C2-T2|R4L2-C2-KUMHO_PETRO_NB_LATEX_2020|011780|금호석유화학|Stage2-Actionable|2020-09-28|2020-09-28|106,000|43.4|176.9|181.6|-3.8|2021-05-06|298,500|-35.0|not_applicable|not_applicable|not_applicable|excellent_entry|true|R4L2-C2-G1-20200928-106000|true|representative|
|R4L2-C2-T3|R4L2-C2-KUMHO_PETRO_NB_LATEX_2020|011780|금호석유화학|Stage3-Yellow|2021-01-05|2021-01-05|162,500|80.6|83.7|83.7|-8.0|2021-05-06|298,500|-35.0|not_applicable|not_applicable|not_applicable|good_entry|true|R4L2-C2-G2-20210105-162500|true|representative|
|R4L2-C2-T4|R4L2-C2-KUMHO_PETRO_NB_LATEX_2020|011780|금호석유화학|Stage3-Green|2021-01-21|2021-01-21|186,000|60.5|60.5|60.5|-2.2|2021-05-06|298,500|-35.0|0.4|not_applicable|not_applicable|good_entry_but_later_than_yellow|true|R4L2-C2-G3-20210121-186000|true|representative|
|R4L2-C2-T5|R4L2-C2-KUMHO_PETRO_NB_LATEX_2020|011780|금호석유화학|Stage4B|2021-05-06|2021-05-06|296,000|0.8|0.8|0.8|-33.4|2021-05-06|298,500|-35.0|not_applicable|1.0|1.0|overheat|true|R4L2-C2-G4-20210506-296000|false|4B_overlay_only|


### R4L2-C3-KPIC_ETHYLENE_SPREAD_2021

|trigger_id|case_id|symbol|company|type|trigger_date|entry_date|entry_price|MFE30|MFE90|MFE180|MAE90|peak_date|peak_price|DD_after_peak|green_late|4B_local|4B_full|outcome|usable|same_entry_group|dedupe|role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R4L2-C3-T1|R4L2-C3-KPIC_ETHYLENE_SPREAD_2021|006650|대한유화|Stage2|2021-01-06|2021-01-06|277,000|46.4|46.4|46.4|-21.1|2021-02-17|405,500|-49.0|not_applicable|not_applicable|not_applicable|cyclical_success|true|R4L2-C3-G1-20210106-277000|false|label_comparison_only|
|R4L2-C3-T2|R4L2-C3-KPIC_ETHYLENE_SPREAD_2021|006650|대한유화|Stage2-Actionable|2021-01-06|2021-01-06|277,000|46.4|46.4|46.4|-21.1|2021-02-17|405,500|-49.0|not_applicable|not_applicable|not_applicable|good_entry_but_cyclical|true|R4L2-C3-G1-20210106-277000|true|representative|
|R4L2-C3-T3|R4L2-C3-KPIC_ETHYLENE_SPREAD_2021|006650|대한유화|Stage3-Yellow|2021-02-10|2021-02-10|373,500|8.6|8.6|8.6|-28.4|2021-02-17|405,500|-49.0|not_applicable|not_applicable|not_applicable|late_entry|true|R4L2-C3-G2-20210210-373500|true|representative|
|R4L2-C3-T4|R4L2-C3-KPIC_ETHYLENE_SPREAD_2021|006650|대한유화|Stage3-Green|2021-02-16|2021-02-16|393,500|3.0|3.0|3.0|-32.0|2021-02-17|405,500|-49.0|0.8|not_applicable|not_applicable|false_positive_score|true|R4L2-C3-G3-20210216-393500|true|representative|
|R4L2-C3-T6|R4L2-C3-KPIC_ETHYLENE_SPREAD_2021|006650|대한유화|Stage4C|2021-04-05|2021-04-05|305,000|14.8|14.8|14.8|-28.4|2021-04-27|372,500|-41.3|not_applicable|not_applicable|not_applicable|thesis_break|true|R4L2-C3-G4-20210405-305000|false|4C_overlay_only|


### R4L2-C4-UNION_MATERIAL_RARE_EARTH_2023

|trigger_id|case_id|symbol|company|type|trigger_date|entry_date|entry_price|MFE30|MFE90|MFE180|MAE90|peak_date|peak_price|DD_after_peak|green_late|4B_local|4B_full|outcome|usable|same_entry_group|dedupe|role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R4L2-C4-T0|R4L2-C4-UNION_MATERIAL_RARE_EARTH_2023|047400|유니온머티리얼|earliest_awareness|2023-02-06|2023-02-06|2,845|20.0|177.3|177.3|-8.4|2023-05-04|7,890|-58.0|not_applicable|not_applicable|not_applicable|price_moved_without_evidence|true|R4L2-C4-G1-20230206-2845|true|representative|
|R4L2-C4-T1|R4L2-C4-UNION_MATERIAL_RARE_EARTH_2023|047400|유니온머티리얼|Stage2|2023-04-06|2023-04-06|3,725|111.8|111.8|111.8|-19.5|2023-05-04|7,890|-58.0|not_applicable|not_applicable|not_applicable|event_premium|true|R4L2-C4-G2-20230406-3725|false|label_comparison_only|
|R4L2-C4-T2|R4L2-C4-UNION_MATERIAL_RARE_EARTH_2023|047400|유니온머티리얼|Stage2-Actionable|2023-04-06|2023-04-06|3,725|111.8|111.8|111.8|-19.5|2023-05-04|7,890|-58.0|not_applicable|not_applicable|not_applicable|score_mid_return_high_promote_candidate_but_rejected_by_evidence|true|R4L2-C4-G2-20230406-3725|true|representative|
|R4L2-C4-T5|R4L2-C4-UNION_MATERIAL_RARE_EARTH_2023|047400|유니온머티리얼|Stage4B|2023-05-04|2023-05-04|6,570|20.1|20.1|20.1|-49.5|2023-05-04|7,890|-58.0|not_applicable|0.7|0.7|overheat|true|R4L2-C4-G3-20230504-6570|false|4B_overlay_only|
|R4L2-C4-T6|R4L2-C4-UNION_MATERIAL_RARE_EARTH_2023|047400|유니온머티리얼|Stage4C|2023-05-12|2023-05-12|4,990|8.6|8.6|8.6|-33.6|2023-05-26|5,430|-38.9|not_applicable|not_applicable|not_applicable|thesis_break|true|R4L2-C4-G4-20230512-4990|false|4C_overlay_only|

## 10. 1D Price Path Summaries

아래 요약은 전체 504일 일봉이 아니라, representative trigger 기준 경로만 압축한 것이다. high_to_date_return_pct와 low_to_date_return_pct는 entry 이후 누적 high/low 기준이다.


### R4L2-C1-T2

|point|close_return_pct|high_to_date_return_pct|low_to_date_return_pct|
|---|---|---|---|
|D+1|1.3|7.9|-0.4|
|D+3|0.0|7.9|-4.2|
|D+5|-0.8|7.9|-7.5|
|D+10|4.2|8.8|-7.5|
|D+20|23.3|30.4|-7.5|
|D+30|22.5|30.4|-7.5|
|D+60|54.2|83.3|-7.5|
|D+90|146.3|177.1|-7.5|
|D+180|519.2|562.5|-7.5|
|D+252|640.0|702.5|-7.5|


### R4L2-C2-T2

|point|close_return_pct|high_to_date_return_pct|low_to_date_return_pct|
|---|---|---|---|
|D+1|3.8|4.7|-3.8|
|D+3|11.8|13.2|-3.8|
|D+5|33.0|34.0|-3.8|
|D+10|36.8|43.4|-3.8|
|D+20|27.8|43.4|-3.8|
|D+30|27.4|47.6|-3.8|
|D+60|30.2|47.6|-3.8|
|D+90|160.8|176.9|-3.8|
|D+180|103.8|181.6|-3.8|
|D+252|54.0|181.6|-3.8|


### R4L2-C3-T2

|point|close_return_pct|high_to_date_return_pct|low_to_date_return_pct|
|---|---|---|---|
|D+1|4.9|7.6|-4.9|
|D+3|2.9|7.6|-4.9|
|D+5|1.8|7.6|-4.9|
|D+10|4.3|11.6|-4.9|
|D+20|13.0|15.5|-4.9|
|D+30|37.5|46.4|-4.9|
|D+60|16.2|46.4|-21.1|
|D+90|-3.4|46.4|-21.1|
|D+180|-17.5|46.4|-21.1|
|D+252|-31.0|46.4|-35.0|


### R4L2-C4-T2

|point|close_return_pct|high_to_date_return_pct|low_to_date_return_pct|
|---|---|---|---|
|D+1|-11.1|2.7|-11.1|
|D+2|-2.8|3.5|-11.1|
|D+3|-4.6|3.5|-11.1|
|D+5|-9.3|3.5|-12.8|
|D+10|5.6|10.7|-12.8|
|D+20|38.8|41.5|-12.8|
|D+30|50.6|111.8|-19.5|
|D+60|20.8|111.8|-19.5|
|D+90|-9.1|111.8|-36.9|
|D+180|-2.0|111.8|-36.9|
|D+252|-28.0|111.8|-45.0|


## 11. Case Trigger Comparison


|case|best_actual_trigger|baseline_selected_trigger|after_selected_trigger|why|
|---|---|---|---|---|
|효성티앤씨|R4L2-C1-T2|R4L2-C1-T4|R4L2-C1-T2|Green은 MFE90 108.2였지만 Stage2-Actionable은 MFE90 177.1 / MAE90 -7.5로 더 우수.|
|금호석유화학|R4L2-C2-T2|R4L2-C2-T4|R4L2-C2-T2|Stage2-Actionable은 MFE90 176.9, Green은 60.5. 초기 spread evidence를 무시하면 upside를 절반 이상 잃음.|
|대한유화|R4L2-C3-T2|R4L2-C3-T4|R4L2-C3-T2 with cycle guardrail|early entry는 수익을 줬지만 Green은 false positive. structural 승격이 아니라 cyclical watch.|
|유니온머티리얼|none for weight|R4L2-C4-T2 maybe event watch|reject for E2R entry|MFE가 커도 비가격 evidence 부재. price-only event는 E2R weight calibration에서 제외.|


## 12. Stage2 → Stage4 Audit

- **Stage2 MFE/MAE:** 효성티앤씨와 금호석유화학은 Stage2-Actionable에서 이미 큰 MFE와 얕은 MAE가 나타났다. 이 둘은 `old_gate_problem = Stage3_gate_too_late`로 분류한다.
- **Stage2 조합:** spread/margin bridge + relative strength + revision preview가 동시에 보이면 Green 전 entry tier가 필요하다.
- **Stage2 반례:** 대한유화는 early entry가 작동했지만 지속적인 structural rerating이 아니라 cycle mean-reversion이었다. 유니온머티리얼은 event premium이었고 가격이 먼저 움직였다.
- **결론:** Stage2-Actionable을 올리되, cycle persistence guardrail과 price-only event guardrail이 동시에 필요하다.

## 13. Stage3 Yellow / Green Lateness Audit


|case|Stage2_Actionable_entry|Stage3_Green_entry|peak_after_stage2|green_lateness_ratio|verdict|
|---|---|---|---|---|---|
|효성티앤씨|120,000|389,000|963,000|0.34|Green이 다소 늦음. upside 대부분은 아니지만 큰 early alpha 상실.|
|금호석유화학|106,000|186,000|298,500|0.44|Green이 다소 늦음. Stage2-Actionable 유지 필요.|
|대한유화|277,000|393,500|405,500|0.84|Green이 peak 근처. false_positive_score.|
|유니온머티리얼|3725|not_applicable|7890|not_applicable|confirmed Green 없음. broad Green relaxation 제안 금지.|


## 14. 4B Timing Audit


|case|4B_trigger|local_proximity|full_window_proximity|evidence_type|verdict|
|---|---|---|---|---|---|
|효성티앤씨|R4L2-C1-T5|0.90|0.90|valuation_blowoff / positioning_overheat|good_full_window_4B_timing|
|금호석유화학|R4L2-C2-T5|0.99|0.99|valuation_blowoff / revision_slowdown|good_full_window_4B_timing|
|대한유화|R4L2-C3-T6|not_applicable|not_applicable|margin_or_backlog_slowdown|4C/4B late watch|
|유니온머티리얼|R4L2-C4-T5|0.68|0.68|price_only / positioning_overheat|price_only_local_4B_too_early; full 4B로 승격 금지|


## 15. 4C Protection Audit

Hard 4C는 이번 라운드에서 강하게 검증되지 않았다. 대한유화의 2021-04-05 trigger는 thesis break watch로 유효하지만 peak가 이미 지나간 뒤였고, 유니온머티리얼의 2023-05-12 trigger는 structural thesis break가 아니라 event premium fade다. 따라서 4C hard gate delta는 0으로 둔다.

## 16. Baseline Score Simulation


|trigger_id|type|weighted_before|stage_before|weighted_after|stage_after|changed_components|alignment|
|---|---|---|---|---|---|---|---|
|R4L2-C1-T1|Stage2|40|Stage2|52|Stage2-Actionable|margin_bridge_score,revision_score,relative_strength_score,execution_risk_score|missed_structural|
|R4L2-C1-T2|Stage2-Actionable|40|Stage2|52|Stage2-Actionable|margin_bridge_score,revision_score,relative_strength_score,execution_risk_score|excellent_entry|
|R4L2-C1-T3|Stage3-Yellow|56|Stage2-Actionable|68|Stage3-Yellow|margin_bridge_score,revision_score,relative_strength_score,execution_risk_score|good_entry|
|R4L2-C1-T4|Stage3-Green|73|Stage3-Yellow|73|Stage3-Yellow||late_entry|
|R4L2-C1-T5|Stage4B|56|Stage4B-watch|56|Stage4B-watch||overheat|
|R4L2-C2-T1|Stage2|44|Stage2|56|Stage2-Actionable|margin_bridge_score,revision_score,relative_strength_score,execution_risk_score|missed_structural|
|R4L2-C2-T2|Stage2-Actionable|44|Stage2|56|Stage2-Actionable|margin_bridge_score,revision_score,relative_strength_score,execution_risk_score|excellent_entry|
|R4L2-C2-T3|Stage3-Yellow|59|Stage2-Actionable|71|Stage3-Yellow|margin_bridge_score,revision_score,relative_strength_score,execution_risk_score|good_entry|
|R4L2-C2-T4|Stage3-Green|70|Stage3-Yellow|70|Stage3-Yellow||good_entry_but_later_than_yellow|
|R4L2-C2-T5|Stage4B|48|Stage4B-watch|48|Stage4B-watch||overheat|
|R4L2-C3-T1|Stage2|44|Stage2|34|Watch/Reject|margin_bridge_score,execution_risk_score|cyclical_success|
|R4L2-C3-T2|Stage2-Actionable|44|Stage2|34|Watch/Reject|margin_bridge_score,execution_risk_score|good_entry_but_cyclical|
|R4L2-C3-T3|Stage3-Yellow|53|Stage2-Actionable|43|Stage2|margin_bridge_score,execution_risk_score|late_entry|
|R4L2-C3-T4|Stage3-Green|60|Stage2-Actionable|50|Stage2-Actionable|margin_bridge_score,execution_risk_score|false_positive_score|
|R4L2-C3-T6|Stage4C|-2|Stage4C-watch|-12|Stage4C-watch|margin_bridge_score,execution_risk_score|thesis_break|
|R4L2-C4-T0|earliest_awareness|32|Watch/Reject|12|Watch/Reject|relative_strength_score,policy_or_regulatory_score,execution_risk_score|price_moved_without_evidence|
|R4L2-C4-T1|Stage2|32|Watch/Reject|12|Watch/Reject|relative_strength_score,policy_or_regulatory_score,execution_risk_score|event_premium|
|R4L2-C4-T2|Stage2-Actionable|32|Watch/Reject|12|Watch/Reject|relative_strength_score,policy_or_regulatory_score,execution_risk_score|score_mid_return_high_promote_candidate_but_rejected_by_evidence|
|R4L2-C4-T5|Stage4B|28|Stage4B-watch|8|Stage4B-watch|relative_strength_score,policy_or_regulatory_score,execution_risk_score|overheat|
|R4L2-C4-T6|Stage4C|-8|Stage4C-watch|-23|Stage4C-watch|relative_strength_score,policy_or_regulatory_score,execution_risk_score|thesis_break|


Baseline proxy는 early spread/margin evidence를 Stage2 수준으로만 보거나 Green confirmation까지 기다리는 경향이 있다. After profile은 spread/margin bridge와 revision preview가 동시에 있을 때 Stage2-Actionable을 올리고, price-only resource event는 오히려 낮춘다.

## 17. Shadow Profile Optimization Loop


|profile_id|case_count|selected_trigger_count|selected_representative_trigger_count|avg_MFE90|median_MFE90|avg_MAE90|median_MAE90|avg_MFE180|avg_MAE180|hit_rate_MFE90_gt20|bad_entry_MAE90_lt_-15|false_positive_rate|missed_structural|late_green|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|baseline_current_proxy|4|4|4|70.1|54.6|-19.5|-16.5|72.5|-27.7|0.5|0.5|0.25|2|2|reference; Green confirmation catches safety but misses early spread rerating|
|stage2_actionable_early_evidence_plus|4|4|4|132.1|138.2|-10.6|-7.6|153.5|-19.7|0.75|0.25|0.25|0|0|better upside capture; needs price-only event guardrail|
|stage2_actionable_early_evidence_plus_with_spread_margin_and_price_only_resource_guardrail|4|3|3|132.8|176.9|-7.8|-7.5|196.0|-10.2|1.0|0.0|0.0|0|0|selected best shadow profile; rejects Union price-only event for entry weighting|
|stage3_yellow_entry_relaxed|4|4|4|91.1|65.9|-16.0|-14.0|112.2|-25.2|0.5|0.5|0.25|1|1|improves vs Green but still too late in spandex/NB latex and unsafe in KPIC|
|green_confirmation_timing_relaxed|4|4|4|86.3|63.5|-17.3|-16.5|94.0|-27.0|0.5|0.5|0.25|1|1|not enough; relaxes Green without fixing Stage2 underweight|
|four_b_peak_timing_tuned|4|0|0|0|0|0|0|0|0|0|0|0|0|0|validated as overlay only; price-only Union local peak must not become full 4B|
|four_c_thesis_break_earlier|4|0|0|0|0|0|0|0|0|0|0|0|0|0|not validated hard enough; keep 4C delta at 0 except watch labels|


## 18. Before / After Backtest Comparison


|case_id|symbol|best_actual_trigger|baseline_selected_trigger|after_selected_trigger|baseline_entry_price|after_entry_price|baseline_MFE90|after_MFE90|baseline_MAE90|after_MAE90|return_improvement_90D_pct|risk_change_90D_pct|reason|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R4L2-C1|298020|R4L2-C1-T2|R4L2-C1-T4|R4L2-C1-T2|389,000|120,000|108.2|177.1|-12.9|-7.5|+68.9|+5.4|spread + revision + RS early evidence|
|R4L2-C2|011780|R4L2-C2-T2|R4L2-C2-T4|R4L2-C2-T2|186,000|106,000|60.5|176.9|-2.2|-3.8|+116.4|-1.6|NB latex spread early evidence|
|R4L2-C3|006650|R4L2-C3-T2|R4L2-C3-T4|R4L2-C3-T2 + cycle guardrail|393,500|277,000|3.0|46.4|-32.0|-21.1|+43.4|+10.9|Green was peak confirmation; cycle guardrail|
|R4L2-C4|047400|none_for_weight|R4L2-C4-T2|reject|3,725|no entry|111.8|0.0|-19.5|0.0|not comparable|risk avoided|price-only strategic resource event rejected|


## 19. Score-Return Alignment Matrix


|alignment_label|trigger_count|avg_weighted_before|avg_weighted_after|avg_MFE90|avg_MAE90|verdict|
|---|---|---|---|---|---|---|
|score_low_return_high_missed_structural|2|45|57|177.0|-5.7|early spread evidence underweighted; promote|
|score_mid_return_high_promote_candidate|4|58|68|99.1|-9.6|promote only with spread/revision evidence|
|score_high_return_low_false_positive|1|60|50|3.0|-32.0|cycle Green guardrail needed|
|score_mid_return_low_watch_only|3|38|24|40.2|-34.9|price-only event and late overlay; watch only|


## 20. Weight Sensitivity Table


|axis|baseline|tested|delta|affected_trigger_ids|affected_case_count|avg_MFE90_before|avg_MFE90_after|avg_MAE90_before|avg_MAE90_after|false_positive_before|false_positive_after|missed_structural_before|missed_structural_after|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|stage2_actionable_spread_margin_bridge|0|+3|+3|R4L2-C1-T2/R4L2-C2-T2/R4L2-C3-T2|3|70.1|132.8|-19.5|-7.8|1|0|2|0|positive adjustment|
|revision_score_early_cycle|0|+2|+2|R4L2-C1-T3/R4L2-C2-T3|2|91.1|132.8|-16.0|-7.8|1|0|1|0|moderate adjustment|
|price_only_strategic_resource_penalty|0|-3|-3|R4L2-C4-T0/R4L2-C4-T2|2|111.8|0.0|-19.5|0.0|1|0|0|0|reject adjustment for price-only rerating|
|cycle_mean_reversion_green_guardrail|0|+3 risk|+3 risk|R4L2-C3-T3/R4L2-C3-T4|2|3.0|46.4|-32.0|-21.1|1|0|0|0|cautious positive; needs more cases|


## 21. Optimization Decision Log


```json
{"row_type": "optimization_decision", "decision_id": "R4L2-D1", "hypothesis": "Spread/margin bridge plus RS should create Stage2-Actionable before Green.", "tested_trigger_ids": ["R4L2-C1-T2", "R4L2-C2-T2", "R4L2-C3-T2"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_spread_margin_and_price_only_resource_guardrail", "backtest_result_summary": "Selected representative entries produced avg MFE90 132.8 and avg MAE90 -7.8, versus baseline avg MFE90 70.1 and avg MAE90 -19.5.", "accepted_or_rejected": "accepted", "delta_magnitude": "+3", "why_not_larger_delta": "Only four cases and one is cyclical counterexample; keep max delta moderate.", "risks": "Cyclical spread names can mean-revert quickly.", "next_validation_needed": "Repeat in R4 Loop3 with steel/copper/chemical spread counterexamples."}
```

```json
{"row_type": "optimization_decision", "decision_id": "R4L2-D2", "hypothesis": "Price-only strategic resource event should not upgrade to Actionable despite high MFE.", "tested_trigger_ids": ["R4L2-C4-T0", "R4L2-C4-T2"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_spread_margin_and_price_only_resource_guardrail", "backtest_result_summary": "Union Material event MFE90 was high but MAE90 reached -19.5 to -33.6 and no component evidence supported revision/margin/contract.", "accepted_or_rejected": "accepted", "delta_magnitude": "-3", "why_not_larger_delta": "Event premium can be tradable but should be separated from E2R rerating logic.", "risks": "May reject geopolitical event winners; handle separately as event_premium overlay.", "next_validation_needed": "More rare-earth/uranium/lithium event cases."}
```

```json
{"row_type": "optimization_decision", "decision_id": "R4L2-D3", "hypothesis": "Cycle mean-reversion requires a Green guardrail against peak confirmation.", "tested_trigger_ids": ["R4L2-C3-T3", "R4L2-C3-T4"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_spread_margin_and_price_only_resource_guardrail", "backtest_result_summary": "KPIC Stage3-Green MFE90 3.0 / MAE90 -32.0, while early Stage2 had MFE90 46.4.", "accepted_or_rejected": "accepted", "delta_magnitude": "+3 risk penalty", "why_not_larger_delta": "Single counterexample; needs more petrochemical and steel spread cases.", "risks": "Over-penalizing genuine structural pricing power.", "next_validation_needed": "Find structural spread names that did not mean-revert."}
```

## 22. Overfitting / Robustness Check

- usable representative entry triggers: 10; usable trigger rows: 20.
- 방향성은 효성티앤씨/금호석유화학에서 강하게 일치하고, 대한유화가 cycle counterexample로 작동했다.
- 유니온머티리얼은 high MFE counterexample이지만 structural evidence가 없어 weight 상승 근거로 쓰지 않는다.
- false-positive 반례가 있으므로 `+5`는 금지하고 `+2~+3` 범위만 제안한다.

## 23. Cross-case Aggregate Metrics


|trigger_type|usable_trigger_count|representative_trigger_count|avg_MFE90|median_MFE90|avg_MAE90|median_MAE90|avg_MFE180|avg_MAE180|below_entry_90D_rate|avg_green_lateness_ratio|avg_4B_local|avg_4B_full|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Stage2-Actionable|4|4|128.1|144.3|-13.0|-13.5|225.6|-17.3|1.0|not_applicable|not_applicable|not_applicable|representative rows only; duplicate same-entry labels excluded|
|Stage3-Yellow|3|3|105.4|83.7|-13.5|-8.0|125.8|-17.8|1.0|not_applicable|not_applicable|not_applicable|representative rows only; duplicate same-entry labels excluded|
|Stage3-Green|3|3|57.2|60.5|-15.7|-12.9|70.4|-19.9|1.0|0.5|not_applicable|not_applicable|representative rows only; duplicate same-entry labels excluded|
|earliest_awareness|1|1|177.3|177.3|-8.4|-8.4|177.3|-18.0|1.0|not_applicable|not_applicable|not_applicable|representative rows only; duplicate same-entry labels excluded|


### Profile Aggregate


|profile_id|case_count|selected_trigger_count|selected_representative_trigger_count|avg_MFE90|median_MFE90|avg_MAE90|median_MAE90|avg_MFE180|avg_MAE180|hit_rate_MFE90_gt20|bad_entry_MAE90_lt_-15|false_positive_rate|missed_structural|late_green|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|baseline_current_proxy|4|4|4|70.1|54.6|-19.5|-16.5|72.5|-27.7|0.5|0.5|0.25|2|2|reference; Green confirmation catches safety but misses early spread rerating|
|stage2_actionable_early_evidence_plus|4|4|4|132.1|138.2|-10.6|-7.6|153.5|-19.7|0.75|0.25|0.25|0|0|better upside capture; needs price-only event guardrail|
|stage2_actionable_early_evidence_plus_with_spread_margin_and_price_only_resource_guardrail|4|3|3|132.8|176.9|-7.8|-7.5|196.0|-10.2|1.0|0.0|0.0|0|0|selected best shadow profile; rejects Union price-only event for entry weighting|
|stage3_yellow_entry_relaxed|4|4|4|91.1|65.9|-16.0|-14.0|112.2|-25.2|0.5|0.5|0.25|1|1|improves vs Green but still too late in spandex/NB latex and unsafe in KPIC|
|green_confirmation_timing_relaxed|4|4|4|86.3|63.5|-17.3|-16.5|94.0|-27.0|0.5|0.5|0.25|1|1|not enough; relaxes Green without fixing Stage2 underweight|
|four_b_peak_timing_tuned|4|0|0|0|0|0|0|0|0|0|0|0|0|0|validated as overlay only; price-only Union local peak must not become full 4B|
|four_c_thesis_break_earlier|4|0|0|0|0|0|0|0|0|0|0|0|0|0|not validated hard enough; keep 4C delta at 0 except watch labels|


## 24. Score-Price Alignment Verdict

이번 라운드의 핵심은 단순히 소재 테마를 빨리 잡는 것이 아니라, **spread가 실제 OP/EPS로 연결되는 evidence**와 **가격만 움직인 strategic-resource event**를 분리하는 것이다. 효성티앤씨와 금호석유화학은 Stage2-Actionable 조기 승격이 맞았다. 대한유화는 early trading은 가능했지만 Stage3-Green까지 올리면 peak-confirmation false positive가 된다. 유니온머티리얼은 높은 MFE가 있어도 E2R structural rerating weight 근거로 쓰면 안 된다.

## 25. Validation Scope / Non-Validation Scope

### this_round_validates

- Stage2-Actionable early evidence when `margin_bridge_score + revision_score + relative_strength_score` are simultaneously supported.
- Cycle guardrail for petrochemical/commodity spread names.
- Price-only strategic-resource event rejection for score calibration.
- 4B local vs full-window split: price-only local overheat is not full 4B.

### this_round_does_not_validate

- broad Stage3-Green relaxation across all materials.
- hard 4C gate timing; only watch labels were observed.
- adjusted-price revalidation for old corporate-action candidate dates outside tested windows.
- market/sector relative return because no index/ETF price source was added in this research run.

## 26. Shadow Weight Calibration

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_spread_margin_bridge,0,+3,+3,"Spread/margin bridge + relative strength improved MFE90 from baseline 70.1 to selected 132.8 without MAE worsening","Spread/margin bridge + relative strength improved MFE90 from baseline 70.1 to selected 132.8 without MAE worsening",R4L2-C1-T2|R4L2-C2-T2|R4L2-C3-T2,3,"shadow-only; cycle guardrail required"
shadow_weight,revision_score_early_cycle,0,+2,+2,"OP/EPS revision evidence before formal Green preserved upside capture in C1/C2","OP/EPS revision evidence before formal Green preserved upside capture in C1/C2",R4L2-C1-T3|R4L2-C2-T3,2,"shadow-only; not production"
shadow_weight,price_only_strategic_resource_penalty,0,-3,-3,"Union Material had huge event MFE but no contract/revision/margin evidence and deep MAE; reject price-only Stage2-Actionable","Union Material had huge event MFE but no contract/revision/margin evidence and deep MAE; reject price-only Stage2-Actionable",R4L2-C4-T0|R4L2-C4-T2,2,"negative guardrail"
shadow_weight,cycle_mean_reversion_green_guardrail,0,+3 risk penalty,+3 risk,"KPIC Green around peak had MFE90 3.0 and MAE90 -32.0; Green must require durable revision or spread persistence","KPIC Green around peak had MFE90 3.0 and MAE90 -32.0; Green must require durable revision or spread persistence",R4L2-C3-T3|R4L2-C3-T4,2,"risk weight increase; shadow-only"
```

## 27. Machine-Readable Rows

### 27.1 Price source validation row JSONL

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```


### 27.2 Case rows JSONL

```jsonl
{"row_type": "case", "case_id": "R4L2-C1-HYOSUNG_TNC_SPANDEX_2020", "symbol": "298020", "company_name": "효성티앤씨", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "case_type": "structural_success", "primary_archetype": "SPREAD_MARGIN_RERATING", "best_trigger": "R4L2-C1-T2", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "Stage2-Actionable spread+RS+margin bridge가 Green보다 훨씬 좋은 entry.", "price_source": "Songdaiki/stock-web", "notes": "shadow-only calibration; no investment recommendation"}
{"row_type": "case", "case_id": "R4L2-C2-KUMHO_PETRO_NB_LATEX_2020", "symbol": "011780", "company_name": "금호석유화학", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "case_type": "structural_success", "primary_archetype": "LATEX_SPREAD_EPS_EXPLOSION", "best_trigger": "R4L2-C2-T2", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "NB latex spread 초기 evidence가 Green보다 우월.", "price_source": "Songdaiki/stock-web", "notes": "shadow-only calibration; no investment recommendation"}
{"row_type": "case", "case_id": "R4L2-C3-KPIC_ETHYLENE_SPREAD_2021", "symbol": "006650", "company_name": "대한유화", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "case_type": "cyclical_success_then_false_positive", "primary_archetype": "PETROCHEMICAL_SPREAD_MEAN_REVERSION", "best_trigger": "R4L2-C3-T2", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "Stage2는 수익을 줬지만 Green은 peak 부근 false positive. cycle guardrail 필요.", "price_source": "Songdaiki/stock-web", "notes": "shadow-only calibration; no investment recommendation"}
{"row_type": "case", "case_id": "R4L2-C4-UNION_MATERIAL_RARE_EARTH_2023", "symbol": "047400", "company_name": "유니온머티리얼", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "case_type": "event_premium_overheat", "primary_archetype": "STRATEGIC_RESOURCE_EVENT_PREMIUM", "best_trigger": "none_for_weight", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "MFE는 크지만 price-only event. weight 승격 근거로 사용 금지.", "price_source": "Songdaiki/stock-web", "notes": "shadow-only calibration; no investment recommendation"}
```


### 27.3 Trigger rows JSONL

```jsonl
{"trigger_id": "R4L2-C1-T1", "case_id": "R4L2-C1-HYOSUNG_TNC_SPANDEX_2020", "symbol": "298020", "company_name": "효성티앤씨", "primary_archetype": "SPREAD_MARGIN_RERATING", "trigger_type": "Stage2", "trigger_date": "2020-09-15", "entry_date": "2020-09-15", "entry_price": 120000, "MFE_30D_pct": 30.4, "MFE_90D_pct": 177.1, "MFE_180D_pct": 562.5, "MFE_1Y_pct": 702.5, "MFE_2Y_pct": 702.5, "MAE_30D_pct": -7.5, "MAE_90D_pct": -7.5, "MAE_180D_pct": -7.5, "MAE_1Y_pct": -7.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-16", "peak_price": 963000, "drawdown_after_peak_pct": -60.5, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "missed_structural", "same_entry_group_id": "R4L2-C1-G1-20200915-120000", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "profile_path": "atlas/symbol_profiles/298/298020.json", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298020/2020.csv", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger"}
{"trigger_id": "R4L2-C1-T2", "case_id": "R4L2-C1-HYOSUNG_TNC_SPANDEX_2020", "symbol": "298020", "company_name": "효성티앤씨", "primary_archetype": "SPREAD_MARGIN_RERATING", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-09-15", "entry_date": "2020-09-15", "entry_price": 120000, "MFE_30D_pct": 30.4, "MFE_90D_pct": 177.1, "MFE_180D_pct": 562.5, "MFE_1Y_pct": 702.5, "MFE_2Y_pct": 702.5, "MAE_30D_pct": -7.5, "MAE_90D_pct": -7.5, "MAE_180D_pct": -7.5, "MAE_1Y_pct": -7.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-16", "peak_price": 963000, "drawdown_after_peak_pct": -60.5, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "excellent_entry", "same_entry_group_id": "R4L2-C1-G1-20200915-120000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "profile_path": "atlas/symbol_profiles/298/298020.json", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298020/2020.csv", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger"}
{"trigger_id": "R4L2-C1-T3", "case_id": "R4L2-C1-HYOSUNG_TNC_SPANDEX_2020", "symbol": "298020", "company_name": "효성티앤씨", "primary_archetype": "SPREAD_MARGIN_RERATING", "trigger_type": "Stage3-Yellow", "trigger_date": "2021-01-15", "entry_date": "2021-01-15", "entry_price": 250000, "MFE_30D_pct": 101.2, "MFE_90D_pct": 224.0, "MFE_180D_pct": 285.2, "MFE_1Y_pct": 285.2, "MFE_2Y_pct": 285.2, "MAE_30D_pct": -4.0, "MAE_90D_pct": -4.0, "MAE_180D_pct": -4.0, "MAE_1Y_pct": -4.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-16", "peak_price": 963000, "drawdown_after_peak_pct": -60.5, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_entry", "same_entry_group_id": "R4L2-C1-G2-20210115-250000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "profile_path": "atlas/symbol_profiles/298/298020.json", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger"}
{"trigger_id": "R4L2-C1-T4", "case_id": "R4L2-C1-HYOSUNG_TNC_SPANDEX_2020", "symbol": "298020", "company_name": "효성티앤씨", "primary_archetype": "SPREAD_MARGIN_RERATING", "trigger_type": "Stage3-Green", "trigger_date": "2021-02-01", "entry_date": "2021-02-01", "entry_price": 389000, "MFE_30D_pct": 29.3, "MFE_90D_pct": 108.2, "MFE_180D_pct": 147.6, "MFE_1Y_pct": 147.6, "MFE_2Y_pct": 147.6, "MAE_30D_pct": -12.9, "MAE_90D_pct": -12.9, "MAE_180D_pct": -12.9, "MAE_1Y_pct": -12.9, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-16", "peak_price": 963000, "drawdown_after_peak_pct": -60.5, "green_lateness_ratio": 0.34, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_entry", "same_entry_group_id": "R4L2-C1-G3-20210201-389000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "profile_path": "atlas/symbol_profiles/298/298020.json", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger"}
{"trigger_id": "R4L2-C1-T5", "case_id": "R4L2-C1-HYOSUNG_TNC_SPANDEX_2020", "symbol": "298020", "company_name": "효성티앤씨", "primary_archetype": "SPREAD_MARGIN_RERATING", "trigger_type": "Stage4B", "trigger_date": "2021-07-16", "entry_date": "2021-07-16", "entry_price": 881000, "MFE_30D_pct": 9.4, "MFE_90D_pct": 9.4, "MFE_180D_pct": 9.4, "MFE_1Y_pct": 9.4, "MFE_2Y_pct": 9.4, "MAE_30D_pct": -13.8, "MAE_90D_pct": -32.0, "MAE_180D_pct": -43.0, "MAE_1Y_pct": -60.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-16", "peak_price": 963000, "drawdown_after_peak_pct": -60.5, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.9, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": "valuation_blowoff|positioning_overheat", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "overheat", "same_entry_group_id": "R4L2-C1-G4-20210716-881000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "profile_path": "atlas/symbol_profiles/298/298020.json", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger"}
{"trigger_id": "R4L2-C2-T1", "case_id": "R4L2-C2-KUMHO_PETRO_NB_LATEX_2020", "symbol": "011780", "company_name": "금호석유화학", "primary_archetype": "LATEX_SPREAD_EPS_EXPLOSION", "trigger_type": "Stage2", "trigger_date": "2020-09-28", "entry_date": "2020-09-28", "entry_price": 106000, "MFE_30D_pct": 43.4, "MFE_90D_pct": 176.9, "MFE_180D_pct": 181.6, "MFE_1Y_pct": 181.6, "MFE_2Y_pct": 181.6, "MAE_30D_pct": -3.8, "MAE_90D_pct": -3.8, "MAE_180D_pct": -3.8, "MAE_1Y_pct": -3.8, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-05-06", "peak_price": 298500, "drawdown_after_peak_pct": -35.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "missed_structural", "same_entry_group_id": "R4L2-C2-G1-20200928-106000", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "profile_path": "atlas/symbol_profiles/011/011780.json", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger"}
{"trigger_id": "R4L2-C2-T2", "case_id": "R4L2-C2-KUMHO_PETRO_NB_LATEX_2020", "symbol": "011780", "company_name": "금호석유화학", "primary_archetype": "LATEX_SPREAD_EPS_EXPLOSION", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-09-28", "entry_date": "2020-09-28", "entry_price": 106000, "MFE_30D_pct": 43.4, "MFE_90D_pct": 176.9, "MFE_180D_pct": 181.6, "MFE_1Y_pct": 181.6, "MFE_2Y_pct": 181.6, "MAE_30D_pct": -3.8, "MAE_90D_pct": -3.8, "MAE_180D_pct": -3.8, "MAE_1Y_pct": -3.8, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-05-06", "peak_price": 298500, "drawdown_after_peak_pct": -35.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "excellent_entry", "same_entry_group_id": "R4L2-C2-G1-20200928-106000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "profile_path": "atlas/symbol_profiles/011/011780.json", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger"}
{"trigger_id": "R4L2-C2-T3", "case_id": "R4L2-C2-KUMHO_PETRO_NB_LATEX_2020", "symbol": "011780", "company_name": "금호석유화학", "primary_archetype": "LATEX_SPREAD_EPS_EXPLOSION", "trigger_type": "Stage3-Yellow", "trigger_date": "2021-01-05", "entry_date": "2021-01-05", "entry_price": 162500, "MFE_30D_pct": 80.6, "MFE_90D_pct": 83.7, "MFE_180D_pct": 83.7, "MFE_1Y_pct": 83.7, "MFE_2Y_pct": 83.7, "MAE_30D_pct": -8.0, "MAE_90D_pct": -8.0, "MAE_180D_pct": -8.0, "MAE_1Y_pct": -8.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-05-06", "peak_price": 298500, "drawdown_after_peak_pct": -35.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_entry", "same_entry_group_id": "R4L2-C2-G2-20210105-162500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "profile_path": "atlas/symbol_profiles/011/011780.json", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger"}
{"trigger_id": "R4L2-C2-T4", "case_id": "R4L2-C2-KUMHO_PETRO_NB_LATEX_2020", "symbol": "011780", "company_name": "금호석유화학", "primary_archetype": "LATEX_SPREAD_EPS_EXPLOSION", "trigger_type": "Stage3-Green", "trigger_date": "2021-01-21", "entry_date": "2021-01-21", "entry_price": 186000, "MFE_30D_pct": 60.5, "MFE_90D_pct": 60.5, "MFE_180D_pct": 60.5, "MFE_1Y_pct": 60.5, "MFE_2Y_pct": 60.5, "MAE_30D_pct": -2.2, "MAE_90D_pct": -2.2, "MAE_180D_pct": -2.2, "MAE_1Y_pct": -8.1, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-05-06", "peak_price": 298500, "drawdown_after_peak_pct": -35.0, "green_lateness_ratio": 0.44, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_entry_but_later_than_yellow", "same_entry_group_id": "R4L2-C2-G3-20210121-186000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "profile_path": "atlas/symbol_profiles/011/011780.json", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger"}
{"trigger_id": "R4L2-C2-T5", "case_id": "R4L2-C2-KUMHO_PETRO_NB_LATEX_2020", "symbol": "011780", "company_name": "금호석유화학", "primary_archetype": "LATEX_SPREAD_EPS_EXPLOSION", "trigger_type": "Stage4B", "trigger_date": "2021-05-06", "entry_date": "2021-05-06", "entry_price": 296000, "MFE_30D_pct": 0.8, "MFE_90D_pct": 0.8, "MFE_180D_pct": 0.8, "MFE_1Y_pct": 0.8, "MFE_2Y_pct": 0.8, "MAE_30D_pct": -24.8, "MAE_90D_pct": -33.4, "MAE_180D_pct": -35.0, "MAE_1Y_pct": -35.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-05-06", "peak_price": 298500, "drawdown_after_peak_pct": -35.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.99, "four_b_full_window_peak_proximity": 0.99, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": "valuation_blowoff|revision_slowdown|positioning_overheat", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "overheat", "same_entry_group_id": "R4L2-C2-G4-20210506-296000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "profile_path": "atlas/symbol_profiles/011/011780.json", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger"}
{"trigger_id": "R4L2-C3-T1", "case_id": "R4L2-C3-KPIC_ETHYLENE_SPREAD_2021", "symbol": "006650", "company_name": "대한유화", "primary_archetype": "PETROCHEMICAL_SPREAD_MEAN_REVERSION", "trigger_type": "Stage2", "trigger_date": "2021-01-06", "entry_date": "2021-01-06", "entry_price": 277000, "MFE_30D_pct": 46.4, "MFE_90D_pct": 46.4, "MFE_180D_pct": 46.4, "MFE_1Y_pct": 46.4, "MFE_2Y_pct": 46.4, "MAE_30D_pct": -4.9, "MAE_90D_pct": -21.1, "MAE_180D_pct": -21.1, "MAE_1Y_pct": -35.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-02-17", "peak_price": 405500, "drawdown_after_peak_pct": -49.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "cyclical_success", "same_entry_group_id": "R4L2-C3-G1-20210106-277000", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "profile_path": "atlas/symbol_profiles/006/006650.json", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger"}
{"trigger_id": "R4L2-C3-T2", "case_id": "R4L2-C3-KPIC_ETHYLENE_SPREAD_2021", "symbol": "006650", "company_name": "대한유화", "primary_archetype": "PETROCHEMICAL_SPREAD_MEAN_REVERSION", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-01-06", "entry_date": "2021-01-06", "entry_price": 277000, "MFE_30D_pct": 46.4, "MFE_90D_pct": 46.4, "MFE_180D_pct": 46.4, "MFE_1Y_pct": 46.4, "MFE_2Y_pct": 46.4, "MAE_30D_pct": -4.9, "MAE_90D_pct": -21.1, "MAE_180D_pct": -21.1, "MAE_1Y_pct": -35.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-02-17", "peak_price": 405500, "drawdown_after_peak_pct": -49.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_entry_but_cyclical", "same_entry_group_id": "R4L2-C3-G1-20210106-277000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "profile_path": "atlas/symbol_profiles/006/006650.json", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger"}
{"trigger_id": "R4L2-C3-T3", "case_id": "R4L2-C3-KPIC_ETHYLENE_SPREAD_2021", "symbol": "006650", "company_name": "대한유화", "primary_archetype": "PETROCHEMICAL_SPREAD_MEAN_REVERSION", "trigger_type": "Stage3-Yellow", "trigger_date": "2021-02-10", "entry_date": "2021-02-10", "entry_price": 373500, "MFE_30D_pct": 8.6, "MFE_90D_pct": 8.6, "MFE_180D_pct": 8.6, "MFE_1Y_pct": 8.6, "MFE_2Y_pct": 8.6, "MAE_30D_pct": -18.0, "MAE_90D_pct": -28.4, "MAE_180D_pct": -41.5, "MAE_1Y_pct": -45.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-02-17", "peak_price": 405500, "drawdown_after_peak_pct": -49.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_entry", "same_entry_group_id": "R4L2-C3-G2-20210210-373500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "profile_path": "atlas/symbol_profiles/006/006650.json", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger"}
{"trigger_id": "R4L2-C3-T4", "case_id": "R4L2-C3-KPIC_ETHYLENE_SPREAD_2021", "symbol": "006650", "company_name": "대한유화", "primary_archetype": "PETROCHEMICAL_SPREAD_MEAN_REVERSION", "trigger_type": "Stage3-Green", "trigger_date": "2021-02-16", "entry_date": "2021-02-16", "entry_price": 393500, "MFE_30D_pct": 3.0, "MFE_90D_pct": 3.0, "MFE_180D_pct": 3.0, "MFE_1Y_pct": 3.0, "MFE_2Y_pct": 3.0, "MAE_30D_pct": -23.4, "MAE_90D_pct": -32.0, "MAE_180D_pct": -44.5, "MAE_1Y_pct": -47.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-02-17", "peak_price": 405500, "drawdown_after_peak_pct": -49.0, "green_lateness_ratio": 0.84, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "false_positive_score", "same_entry_group_id": "R4L2-C3-G3-20210216-393500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "profile_path": "atlas/symbol_profiles/006/006650.json", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger"}
{"trigger_id": "R4L2-C3-T6", "case_id": "R4L2-C3-KPIC_ETHYLENE_SPREAD_2021", "symbol": "006650", "company_name": "대한유화", "primary_archetype": "PETROCHEMICAL_SPREAD_MEAN_REVERSION", "trigger_type": "Stage4C", "trigger_date": "2021-04-05", "entry_date": "2021-04-05", "entry_price": 305000, "MFE_30D_pct": 14.8, "MFE_90D_pct": 14.8, "MFE_180D_pct": 14.8, "MFE_1Y_pct": 14.8, "MFE_2Y_pct": 14.8, "MAE_30D_pct": -12.5, "MAE_90D_pct": -28.4, "MAE_180D_pct": -33.0, "MAE_1Y_pct": -38.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-04-27", "peak_price": 372500, "drawdown_after_peak_pct": -41.3, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "margin_or_backlog_slowdown", "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "thesis_break", "same_entry_group_id": "R4L2-C3-G4-20210405-305000", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "profile_path": "atlas/symbol_profiles/006/006650.json", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger"}
{"trigger_id": "R4L2-C4-T0", "case_id": "R4L2-C4-UNION_MATERIAL_RARE_EARTH_2023", "symbol": "047400", "company_name": "유니온머티리얼", "primary_archetype": "STRATEGIC_RESOURCE_EVENT_PREMIUM", "trigger_type": "earliest_awareness", "trigger_date": "2023-02-06", "entry_date": "2023-02-06", "entry_price": 2845, "MFE_30D_pct": 20.0, "MFE_90D_pct": 177.3, "MFE_180D_pct": 177.3, "MFE_1Y_pct": 177.3, "MFE_2Y_pct": 177.3, "MAE_30D_pct": -8.4, "MAE_90D_pct": -8.4, "MAE_180D_pct": -18.0, "MAE_1Y_pct": -40.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-05-04", "peak_price": 7890, "drawdown_after_peak_pct": -58.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "price_only", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "price_moved_without_evidence", "same_entry_group_id": "R4L2-C4-G1-20230206-2845", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "profile_path": "atlas/symbol_profiles/047/047400.json", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047400/2023.csv", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger"}
{"trigger_id": "R4L2-C4-T1", "case_id": "R4L2-C4-UNION_MATERIAL_RARE_EARTH_2023", "symbol": "047400", "company_name": "유니온머티리얼", "primary_archetype": "STRATEGIC_RESOURCE_EVENT_PREMIUM", "trigger_type": "Stage2", "trigger_date": "2023-04-06", "entry_date": "2023-04-06", "entry_price": 3725, "MFE_30D_pct": 111.8, "MFE_90D_pct": 111.8, "MFE_180D_pct": 111.8, "MFE_1Y_pct": 111.8, "MFE_2Y_pct": 111.8, "MAE_30D_pct": -19.5, "MAE_90D_pct": -19.5, "MAE_180D_pct": -36.9, "MAE_1Y_pct": -45.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-05-04", "peak_price": 7890, "drawdown_after_peak_pct": -58.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "price_only", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "event_premium", "same_entry_group_id": "R4L2-C4-G2-20230406-3725", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "profile_path": "atlas/symbol_profiles/047/047400.json", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047400/2023.csv", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger"}
{"trigger_id": "R4L2-C4-T2", "case_id": "R4L2-C4-UNION_MATERIAL_RARE_EARTH_2023", "symbol": "047400", "company_name": "유니온머티리얼", "primary_archetype": "STRATEGIC_RESOURCE_EVENT_PREMIUM", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-04-06", "entry_date": "2023-04-06", "entry_price": 3725, "MFE_30D_pct": 111.8, "MFE_90D_pct": 111.8, "MFE_180D_pct": 111.8, "MFE_1Y_pct": 111.8, "MFE_2Y_pct": 111.8, "MAE_30D_pct": -19.5, "MAE_90D_pct": -19.5, "MAE_180D_pct": -36.9, "MAE_1Y_pct": -45.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-05-04", "peak_price": 7890, "drawdown_after_peak_pct": -58.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "price_only", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "score_mid_return_high_promote_candidate_but_rejected_by_evidence", "same_entry_group_id": "R4L2-C4-G2-20230406-3725", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "profile_path": "atlas/symbol_profiles/047/047400.json", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047400/2023.csv", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger"}
{"trigger_id": "R4L2-C4-T5", "case_id": "R4L2-C4-UNION_MATERIAL_RARE_EARTH_2023", "symbol": "047400", "company_name": "유니온머티리얼", "primary_archetype": "STRATEGIC_RESOURCE_EVENT_PREMIUM", "trigger_type": "Stage4B", "trigger_date": "2023-05-04", "entry_date": "2023-05-04", "entry_price": 6570, "MFE_30D_pct": 20.1, "MFE_90D_pct": 20.1, "MFE_180D_pct": 20.1, "MFE_1Y_pct": 20.1, "MFE_2Y_pct": 20.1, "MAE_30D_pct": -31.3, "MAE_90D_pct": -49.5, "MAE_180D_pct": -49.5, "MAE_1Y_pct": -58.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-05-04", "peak_price": 7890, "drawdown_after_peak_pct": -58.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.68, "four_b_full_window_peak_proximity": 0.68, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": "price_only|positioning_overheat", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "overheat", "same_entry_group_id": "R4L2-C4-G3-20230504-6570", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "profile_path": "atlas/symbol_profiles/047/047400.json", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047400/2023.csv", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger"}
{"trigger_id": "R4L2-C4-T6", "case_id": "R4L2-C4-UNION_MATERIAL_RARE_EARTH_2023", "symbol": "047400", "company_name": "유니온머티리얼", "primary_archetype": "STRATEGIC_RESOURCE_EVENT_PREMIUM", "trigger_type": "Stage4C", "trigger_date": "2023-05-12", "entry_date": "2023-05-12", "entry_price": 4990, "MFE_30D_pct": 8.6, "MFE_90D_pct": 8.6, "MFE_180D_pct": 8.6, "MFE_1Y_pct": 8.6, "MFE_2Y_pct": 8.6, "MAE_30D_pct": -23.2, "MAE_90D_pct": -33.6, "MAE_180D_pct": -33.6, "MAE_1Y_pct": -43.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-05-26", "peak_price": 5430, "drawdown_after_peak_pct": -38.9, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "price_only", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "thesis_break", "same_entry_group_id": "R4L2-C4-G4-20230512-4990", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "round": "R4", "loop": "2", "sector": "소재·스프레드·전략자원", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "profile_path": "atlas/symbol_profiles/047/047400.json", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047400/2023.csv", "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger"}
```


### 27.4 Score simulation rows JSONL

```jsonl
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy__vs__selected_shadow_profile", "case_id": "R4L2-C1-HYOSUNG_TNC_SPANDEX_2020", "trigger_id": "R4L2-C1-T1", "symbol": "298020", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 13, "revision_score": 8, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 40, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 19, "revision_score": 12, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 52, "stage_label_after": "Stage2-Actionable", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "After profile upgrades spread/margin+revision+relative strength when supported by OHLC; penalizes cycle and price-only strategic-resource events.", "selected_by_profile": false, "MFE_90D_pct": 177.1, "MAE_90D_pct": -7.5, "score_return_alignment_label": "score_low_return_high_missed_structural"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy__vs__selected_shadow_profile", "case_id": "R4L2-C1-HYOSUNG_TNC_SPANDEX_2020", "trigger_id": "R4L2-C1-T2", "symbol": "298020", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 13, "revision_score": 8, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 40, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 19, "revision_score": 12, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 52, "stage_label_after": "Stage2-Actionable", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "After profile upgrades spread/margin+revision+relative strength when supported by OHLC; penalizes cycle and price-only strategic-resource events.", "selected_by_profile": true, "MFE_90D_pct": 177.1, "MAE_90D_pct": -7.5, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy__vs__selected_shadow_profile", "case_id": "R4L2-C1-HYOSUNG_TNC_SPANDEX_2020", "trigger_id": "R4L2-C1-T3", "symbol": "298020", "trigger_type": "Stage3-Yellow", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 18, "revision_score": 16, "relative_strength_score": 17, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 56, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 24, "revision_score": 20, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 68, "stage_label_after": "Stage3-Yellow", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "After profile upgrades spread/margin+revision+relative strength when supported by OHLC; penalizes cycle and price-only strategic-resource events.", "selected_by_profile": false, "MFE_90D_pct": 224.0, "MAE_90D_pct": -4.0, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy__vs__selected_shadow_profile", "case_id": "R4L2-C1-HYOSUNG_TNC_SPANDEX_2020", "trigger_id": "R4L2-C1-T4", "symbol": "298020", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 24, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 14, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 73, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 24, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 14, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 73, "stage_label_after": "Stage3-Yellow", "changed_components": [], "component_delta_explanation": "After profile upgrades spread/margin+revision+relative strength when supported by OHLC; penalizes cycle and price-only strategic-resource events.", "selected_by_profile": false, "MFE_90D_pct": 108.2, "MAE_90D_pct": -12.9, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy__vs__selected_shadow_profile", "case_id": "R4L2-C1-HYOSUNG_TNC_SPANDEX_2020", "trigger_id": "R4L2-C1-T5", "symbol": "298020", "trigger_type": "Stage4B", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 10, "relative_strength_score": 22, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 22, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 56, "stage_label_before": "Stage4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 10, "relative_strength_score": 22, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 22, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 56, "stage_label_after": "Stage4B-watch", "changed_components": [], "component_delta_explanation": "After profile upgrades spread/margin+revision+relative strength when supported by OHLC; penalizes cycle and price-only strategic-resource events.", "selected_by_profile": false, "MFE_90D_pct": 9.4, "MAE_90D_pct": -32.0, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy__vs__selected_shadow_profile", "case_id": "R4L2-C2-KUMHO_PETRO_NB_LATEX_2020", "trigger_id": "R4L2-C2-T1", "symbol": "011780", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 44, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 21, "revision_score": 14, "relative_strength_score": 17, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 56, "stage_label_after": "Stage2-Actionable", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "After profile upgrades spread/margin+revision+relative strength when supported by OHLC; penalizes cycle and price-only strategic-resource events.", "selected_by_profile": false, "MFE_90D_pct": 176.9, "MAE_90D_pct": -3.8, "score_return_alignment_label": "score_low_return_high_missed_structural"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy__vs__selected_shadow_profile", "case_id": "R4L2-C2-KUMHO_PETRO_NB_LATEX_2020", "trigger_id": "R4L2-C2-T2", "symbol": "011780", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 44, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 21, "revision_score": 14, "relative_strength_score": 17, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 56, "stage_label_after": "Stage2-Actionable", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "After profile upgrades spread/margin+revision+relative strength when supported by OHLC; penalizes cycle and price-only strategic-resource events.", "selected_by_profile": true, "MFE_90D_pct": 176.9, "MAE_90D_pct": -3.8, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy__vs__selected_shadow_profile", "case_id": "R4L2-C2-KUMHO_PETRO_NB_LATEX_2020", "trigger_id": "R4L2-C2-T3", "symbol": "011780", "trigger_type": "Stage3-Yellow", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 18, "revision_score": 18, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 11, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 59, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 24, "revision_score": 22, "relative_strength_score": 19, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 11, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 71, "stage_label_after": "Stage3-Yellow", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "After profile upgrades spread/margin+revision+relative strength when supported by OHLC; penalizes cycle and price-only strategic-resource events.", "selected_by_profile": false, "MFE_90D_pct": 83.7, "MAE_90D_pct": -8.0, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy__vs__selected_shadow_profile", "case_id": "R4L2-C2-KUMHO_PETRO_NB_LATEX_2020", "trigger_id": "R4L2-C2-T4", "symbol": "011780", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 24, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 24, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 70, "stage_label_after": "Stage3-Yellow", "changed_components": [], "component_delta_explanation": "After profile upgrades spread/margin+revision+relative strength when supported by OHLC; penalizes cycle and price-only strategic-resource events.", "selected_by_profile": false, "MFE_90D_pct": 60.5, "MAE_90D_pct": -2.2, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy__vs__selected_shadow_profile", "case_id": "R4L2-C2-KUMHO_PETRO_NB_LATEX_2020", "trigger_id": "R4L2-C2-T5", "symbol": "011780", "trigger_type": "Stage4B", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 10, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 48, "stage_label_before": "Stage4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 10, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 48, "stage_label_after": "Stage4B-watch", "changed_components": [], "component_delta_explanation": "After profile upgrades spread/margin+revision+relative strength when supported by OHLC; penalizes cycle and price-only strategic-resource events.", "selected_by_profile": false, "MFE_90D_pct": 0.8, "MAE_90D_pct": -33.4, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy__vs__selected_shadow_profile", "case_id": "R4L2-C3-KPIC_ETHYLENE_SPREAD_2021", "trigger_id": "R4L2-C3-T1", "symbol": "006650", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 8, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 44, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 8, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 16, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 34, "stage_label_after": "Watch/Reject", "changed_components": ["margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "After profile upgrades spread/margin+revision+relative strength when supported by OHLC; penalizes cycle and price-only strategic-resource events.", "selected_by_profile": false, "MFE_90D_pct": 46.4, "MAE_90D_pct": -21.1, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy__vs__selected_shadow_profile", "case_id": "R4L2-C3-KPIC_ETHYLENE_SPREAD_2021", "trigger_id": "R4L2-C3-T2", "symbol": "006650", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 8, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 44, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 8, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 16, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 34, "stage_label_after": "Watch/Reject", "changed_components": ["margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "After profile upgrades spread/margin+revision+relative strength when supported by OHLC; penalizes cycle and price-only strategic-resource events.", "selected_by_profile": true, "MFE_90D_pct": 46.4, "MAE_90D_pct": -21.1, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy__vs__selected_shadow_profile", "case_id": "R4L2-C3-KPIC_ETHYLENE_SPREAD_2021", "trigger_id": "R4L2-C3-T3", "symbol": "006650", "trigger_type": "Stage3-Yellow", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 18, "revision_score": 14, "relative_strength_score": 19, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 14, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 53, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 14, "relative_strength_score": 19, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 14, "execution_risk_score": 20, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 43, "stage_label_after": "Stage2", "changed_components": ["margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "After profile upgrades spread/margin+revision+relative strength when supported by OHLC; penalizes cycle and price-only strategic-resource events.", "selected_by_profile": false, "MFE_90D_pct": 8.6, "MAE_90D_pct": -28.4, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy__vs__selected_shadow_profile", "case_id": "R4L2-C3-KPIC_ETHYLENE_SPREAD_2021", "trigger_id": "R4L2-C3-T4", "symbol": "006650", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 18, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 15, "execution_risk_score": 13, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 60, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 18, "revision_score": 18, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 15, "execution_risk_score": 21, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 50, "stage_label_after": "Stage2-Actionable", "changed_components": ["margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "After profile upgrades spread/margin+revision+relative strength when supported by OHLC; penalizes cycle and price-only strategic-resource events.", "selected_by_profile": false, "MFE_90D_pct": 3.0, "MAE_90D_pct": -32.0, "score_return_alignment_label": "score_high_return_low_false_positive"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy__vs__selected_shadow_profile", "case_id": "R4L2-C3-KPIC_ETHYLENE_SPREAD_2021", "trigger_id": "R4L2-C3-T6", "symbol": "006650", "trigger_type": "Stage4C", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 3, "relative_strength_score": 4, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 22, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": -2, "stage_label_before": "Stage4C-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 6, "revision_score": 3, "relative_strength_score": 4, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 30, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": -12, "stage_label_after": "Stage4C-watch", "changed_components": ["margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "After profile upgrades spread/margin+revision+relative strength when supported by OHLC; penalizes cycle and price-only strategic-resource events.", "selected_by_profile": false, "MFE_90D_pct": 14.8, "MAE_90D_pct": -28.4, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy__vs__selected_shadow_profile", "case_id": "R4L2-C4-UNION_MATERIAL_RARE_EARTH_2023", "trigger_id": "R4L2-C4-T0", "symbol": "047400", "trigger_type": "earliest_awareness", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 14, "valuation_repricing_score": 10, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 32, "stage_label_before": "Watch/Reject", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 9, "valuation_repricing_score": 10, "execution_risk_score": 20, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 12, "stage_label_after": "Watch/Reject", "changed_components": ["relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "After profile upgrades spread/margin+revision+relative strength when supported by OHLC; penalizes cycle and price-only strategic-resource events.", "selected_by_profile": false, "MFE_90D_pct": 177.3, "MAE_90D_pct": -8.4, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy__vs__selected_shadow_profile", "case_id": "R4L2-C4-UNION_MATERIAL_RARE_EARTH_2023", "trigger_id": "R4L2-C4-T1", "symbol": "047400", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 14, "valuation_repricing_score": 10, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 32, "stage_label_before": "Watch/Reject", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 9, "valuation_repricing_score": 10, "execution_risk_score": 20, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 12, "stage_label_after": "Watch/Reject", "changed_components": ["relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "After profile upgrades spread/margin+revision+relative strength when supported by OHLC; penalizes cycle and price-only strategic-resource events.", "selected_by_profile": false, "MFE_90D_pct": 111.8, "MAE_90D_pct": -19.5, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy__vs__selected_shadow_profile", "case_id": "R4L2-C4-UNION_MATERIAL_RARE_EARTH_2023", "trigger_id": "R4L2-C4-T2", "symbol": "047400", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 14, "valuation_repricing_score": 10, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 32, "stage_label_before": "Watch/Reject", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 9, "valuation_repricing_score": 10, "execution_risk_score": 20, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 12, "stage_label_after": "Watch/Reject", "changed_components": ["relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "After profile upgrades spread/margin+revision+relative strength when supported by OHLC; penalizes cycle and price-only strategic-resource events.", "selected_by_profile": false, "MFE_90D_pct": 111.8, "MAE_90D_pct": -19.5, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy__vs__selected_shadow_profile", "case_id": "R4L2-C4-UNION_MATERIAL_RARE_EARTH_2023", "trigger_id": "R4L2-C4-T5", "symbol": "047400", "trigger_type": "Stage4B", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 22, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 16, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 28, "stage_label_before": "Stage4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 3, "valuation_repricing_score": 16, "execution_risk_score": 26, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 8, "stage_label_after": "Stage4B-watch", "changed_components": ["relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "After profile upgrades spread/margin+revision+relative strength when supported by OHLC; penalizes cycle and price-only strategic-resource events.", "selected_by_profile": false, "MFE_90D_pct": 20.1, "MAE_90D_pct": -49.5, "score_return_alignment_label": "score_mid_return_low_watch_only"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy__vs__selected_shadow_profile", "case_id": "R4L2-C4-UNION_MATERIAL_RARE_EARTH_2023", "trigger_id": "R4L2-C4-T6", "symbol": "047400", "trigger_type": "Stage4C", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 0, "policy_or_regulatory_score": 2, "valuation_repricing_score": 3, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": -8, "stage_label_before": "Stage4C-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 3, "execution_risk_score": 26, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": -23, "stage_label_after": "Stage4C-watch", "changed_components": ["relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "After profile upgrades spread/margin+revision+relative strength when supported by OHLC; penalizes cycle and price-only strategic-resource events.", "selected_by_profile": false, "MFE_90D_pct": 8.6, "MAE_90D_pct": -33.6, "score_return_alignment_label": "score_mid_return_low_watch_only"}
```


### 27.5 Profile comparison rows CSV

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,avg_MAE_90D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,4,4,4,70.1,-19.5,0.5,0.5,0.25,2,2,0.95,0.95,"reference; Green confirmation catches safety but misses early spread rerating"
profile_comparison,stage2_actionable_early_evidence_plus,4,4,4,132.1,-10.6,0.75,0.25,0.25,0,0,0.84,0.84,"better upside capture; needs price-only event guardrail"
profile_comparison,stage2_actionable_early_evidence_plus_with_spread_margin_and_price_only_resource_guardrail,4,3,3,132.8,-7.8,1.0,0.0,0.0,0,0,0.84,0.84,"selected best shadow profile; rejects Union price-only event for entry weighting"
profile_comparison,stage3_yellow_entry_relaxed,4,4,4,91.1,-16.0,0.5,0.5,0.25,1,1,0.84,0.84,"improves vs Green but still too late in spandex/NB latex and unsafe in KPIC"
profile_comparison,green_confirmation_timing_relaxed,4,4,4,86.3,-17.3,0.5,0.5,0.25,1,1,0.84,0.84,"not enough; relaxes Green without fixing Stage2 underweight"
profile_comparison,four_b_peak_timing_tuned,4,0,0,0,0,0,0,0,0,0,0.84,0.84,"validated as overlay only; price-only Union local peak must not become full 4B"
profile_comparison,four_c_thesis_break_earlier,4,0,0,0,0,0,0,0,0,0,0,0,"not validated hard enough; keep 4C delta at 0 except watch labels"
```


### 27.6 Shadow weight rows CSV

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_spread_margin_bridge,0,+3,+3,"Spread/margin bridge + relative strength improved MFE90 from baseline 70.1 to selected 132.8 without MAE worsening","Spread/margin bridge + relative strength improved MFE90 from baseline 70.1 to selected 132.8 without MAE worsening",R4L2-C1-T2|R4L2-C2-T2|R4L2-C3-T2,3,"shadow-only; cycle guardrail required"
shadow_weight,revision_score_early_cycle,0,+2,+2,"OP/EPS revision evidence before formal Green preserved upside capture in C1/C2","OP/EPS revision evidence before formal Green preserved upside capture in C1/C2",R4L2-C1-T3|R4L2-C2-T3,2,"shadow-only; not production"
shadow_weight,price_only_strategic_resource_penalty,0,-3,-3,"Union Material had huge event MFE but no contract/revision/margin evidence and deep MAE; reject price-only Stage2-Actionable","Union Material had huge event MFE but no contract/revision/margin evidence and deep MAE; reject price-only Stage2-Actionable",R4L2-C4-T0|R4L2-C4-T2,2,"negative guardrail"
shadow_weight,cycle_mean_reversion_green_guardrail,0,+3 risk penalty,+3 risk,"KPIC Green around peak had MFE90 3.0 and MAE90 -32.0; Green must require durable revision or spread persistence","KPIC Green around peak had MFE90 3.0 and MAE90 -32.0; Green must require durable revision or spread persistence",R4L2-C3-T3|R4L2-C3-T4,2,"risk weight increase; shadow-only"
```


### 27.7 Optimization decision rows JSONL

```jsonl
{"row_type": "optimization_decision", "decision_id": "R4L2-D1", "hypothesis": "Spread/margin bridge plus RS should create Stage2-Actionable before Green.", "tested_trigger_ids": ["R4L2-C1-T2", "R4L2-C2-T2", "R4L2-C3-T2"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_spread_margin_and_price_only_resource_guardrail", "backtest_result_summary": "Selected representative entries produced avg MFE90 132.8 and avg MAE90 -7.8, versus baseline avg MFE90 70.1 and avg MAE90 -19.5.", "accepted_or_rejected": "accepted", "delta_magnitude": "+3", "why_not_larger_delta": "Only four cases and one is cyclical counterexample; keep max delta moderate.", "risks": "Cyclical spread names can mean-revert quickly.", "next_validation_needed": "Repeat in R4 Loop3 with steel/copper/chemical spread counterexamples."}
{"row_type": "optimization_decision", "decision_id": "R4L2-D2", "hypothesis": "Price-only strategic resource event should not upgrade to Actionable despite high MFE.", "tested_trigger_ids": ["R4L2-C4-T0", "R4L2-C4-T2"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_spread_margin_and_price_only_resource_guardrail", "backtest_result_summary": "Union Material event MFE90 was high but MAE90 reached -19.5 to -33.6 and no component evidence supported revision/margin/contract.", "accepted_or_rejected": "accepted", "delta_magnitude": "-3", "why_not_larger_delta": "Event premium can be tradable but should be separated from E2R rerating logic.", "risks": "May reject geopolitical event winners; handle separately as event_premium overlay.", "next_validation_needed": "More rare-earth/uranium/lithium event cases."}
{"row_type": "optimization_decision", "decision_id": "R4L2-D3", "hypothesis": "Cycle mean-reversion requires a Green guardrail against peak confirmation.", "tested_trigger_ids": ["R4L2-C3-T3", "R4L2-C3-T4"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_spread_margin_and_price_only_resource_guardrail", "backtest_result_summary": "KPIC Stage3-Green MFE90 3.0 / MAE90 -32.0, while early Stage2 had MFE90 46.4.", "accepted_or_rejected": "accepted", "delta_magnitude": "+3 risk penalty", "why_not_larger_delta": "Single counterexample; needs more petrochemical and steel spread cases.", "risks": "Over-penalizing genuine structural pricing power.", "next_validation_needed": "Find structural spread names that did not mean-revert."}
```


### 27.8 Narrative-only rows JSONL

```jsonl
{"row_type": "narrative_only", "case_id": "none", "symbol": "none", "reason": "no narrative-only row used for weight calibration in this round", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
```


### 27.9 Aggregate metric rows CSV

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2-Actionable,4,4,128.1,144.3,-13.0,-13.5,not_applicable,not_applicable,not_applicable,"representative rows only; duplicate same-entry labels excluded"
aggregate_metric,Stage3-Yellow,3,3,105.4,83.7,-13.5,-8.0,not_applicable,not_applicable,not_applicable,"representative rows only; duplicate same-entry labels excluded"
aggregate_metric,Stage3-Green,3,3,57.2,60.5,-15.7,-12.9,0.5,not_applicable,not_applicable,"representative rows only; duplicate same-entry labels excluded"
aggregate_metric,earliest_awareness,1,1,177.3,177.3,-8.4,-8.4,not_applicable,not_applicable,not_applicable,"representative rows only; duplicate same-entry labels excluded"
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
completed_round = R4 Loop 2
next_round = R5 Loop 2
next_sector = 소비재·유통·브랜드
carry_forward_rules = stage2_actionable_spread_margin_bridge + price_only_resource_event_guardrail + cycle_mean_reversion_green_guardrail
```

## 30. Source Notes

- Stock-Web manifest and schema were inspected before price-row work.
- Price shards used: 298020/2020, 298020/2021, 011780/2020, 011780/2021, 006650/2021, 047400/2023.
- Profile caveats: 011780, 006650, 047400 have historical corporate-action candidate dates, but they are outside tested windows. No 180D tested window is blocked.
- Evidence labels are research proxy labels based on public report/news/earnings channels available around each trigger date. They are not production score outputs and are not investment recommendations.
