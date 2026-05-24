# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata

```json
{
  "research_session": "historical_calibration_after_stock_web_ohlc_breakthrough",
  "round": "R10",
  "loop": "2",
  "sector": "건설·부동산·건자재",
  "assumed_from_previous_next_round": "R10 Loop 2",
  "stock_agent_repo_access_allowed": false,
  "stock_agent_code_patch_allowed": false,
  "stock_web_price_atlas_access_required": true,
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "created_at": "2026-05-22"
}
```

## 1. Round Scope

- 이번 라운드: **R10 / Loop 2 / 건설·부동산·건자재**
- 실행 모드: historical trigger-level calibration only.
- `stock_agent` 레포 접근/패치: **하지 않음**.
- 가격 데이터: **Songdaiki/stock-web actual 1D OHLCV row**.
- Production score 변경: **없음**. 모든 제안은 shadow-only.

## 2. Stock-Web OHLC Input / Price Source Validation


- Stock-Web manifest was re-read for this run: max_date=2026-02-20, price_adjustment_status=raw_unadjusted_marcap, calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year. The manifest states raw/unadjusted OHLC and that zero-volume/invalid rows are excluded from calibration shards. See source refs: fileciteturn392file0.
- Schema mapping was re-read: tradable columns are d/o/h/l/c/v/a/mc/s/m and calibration rules require positive OHLC, entry row, at least 180 forward tradable days, and no 180D corporate-action contamination. See fileciteturn393file0.
- Universe path and inferred status format were sampled from all_symbols.csv. See fileciteturn394file0.
- Symbol profile contamination checks: Daewoo E&C 047040 has corporate-action candidate dates only in 2001/2003/2011, outside this 2020-2021 calibration window; HDC 294870 has 2020-03-26 outside 2022 window; GS E&C 006360 has candidates in 1999 and 2014 outside 2023 window; Sampyo Cement has candidates through 2014 outside 2021 window. See profile refs fileciteturn398file0 fileciteturn399file0 fileciteturn400file0 fileciteturn401file0.
- Price row anchors used in this file are from stock-web shards: Daewoo 2020/2021 rows fileciteturn402file0 fileciteturn403file0; HDC 2022 rows fileciteturn404file0 fileciteturn405file0; GS E&C 2023 rows fileciteturn406file0; Sampyo Cement 2021 rows fileciteturn407file0.
- HDC Gwangju Hwajeong I-Park collapse event date and government-investigation context were cross-checked by web source: the event is listed as 2022-01-11, and the investigation attributed the collapse to faulty construction methods/substandard materials. citeturn311078search0.
- GS E&C Geomdan non-price source should be revalidated by a coding agent against DART/KRX/news before production scoring. The OHLC-derived drawdown rows remain usable for shadow 4C protection only, not for production score changes without source revalidation.


```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

## 3. Historical Eligibility Gate

이번 라운드에서 `calibration_usable=true`로 둔 case는 모두 다음 조건을 통과했다.

- entry row가 stock-web tradable shard에 존재한다.
- manifest max_date는 2026-02-20이며, 본 라운드 trigger는 모두 forward 180 trading days 이상을 확보한다.
- 30D/90D/180D MFE/MAE를 actual OHLC high/low 기준으로 계산했다.
- symbol profile의 corporate_action_candidate_dates가 각 180D window와 겹치지 않는다.
- market/sector relative return은 이번 run에서 안정적으로 확보하지 못해 `unavailable`로 둔다. core calibration은 절대수익률/MFE/MAE 기준으로 유지한다.

## 4. Canonical Archetypes Tested

| Archetype | Meaning | Tested cases |
|---|---|---|
| HOUSING_BACKLOG_MARGIN_RERATING | 주택/건축 수주잔고 + 마진 bridge + 상대강도 | 대우건설 |
| CEMENT_PRICE_SPREAD_REPRICING | 시멘트 가격/스프레드 + 인프라·건자재 수요 | 삼표시멘트 |
| CONSTRUCTION_SAFETY_THESIS_BREAK | 현장 안전·품질 사고가 건설사 thesis를 깨는 4C | HDC현대산업개발 |
| CONSTRUCTION_QUALITY_REBUILD_THESIS_BREAK | 재시공/품질비용/행정리스크가 Green을 무효화하는 4C | GS건설 |

## 5. Case Selection Summary

| case_id | symbol | company_name | case_type | primary_archetype | best_trigger | score_price_alignment | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R10L2_C01_DAEWOO_2020 | 047040 | 대우건설 | structural_success | HOUSING_BACKLOG_MARGIN_RERATING | R10L2_C01_DAEWOO_2020_T02 | score_mid_return_high_promote_candidate | Stage2-Actionable가 Stage3-Green보다 112 trading days 앞서고 MFE90/180이 우수했다. |
| R10L2_C02_SAMPYO_2021 | 038500 | 삼표시멘트 | stage2_promote_candidate | CEMENT_PRICE_SPREAD_REPRICING | R10L2_C02_SAMPYO_2021_T03 | score_mid_return_high_promote_candidate | Stage3-Yellow가 가장 안정적인 MFE/MAE 조합. Stage2-Actionable도 양호. |
| R10L2_C03_HDC_2022 | 294870 | HDC현대산업개발 | 4C_thesis_break | CONSTRUCTION_SAFETY_THESIS_BREAK | R10L2_C03_HDC_2022_T01 | hard_4c_success | 사고 당일/다음 거래일 4C가 이후 MAE90/180 drawdown을 가장 빨리 경고했다. |
| R10L2_C04_GSENC_2023 | 006360 | GS건설 | false_positive_to_4C | CONSTRUCTION_QUALITY_REBUILD_THESIS_BREAK | R10L2_C04_GSENC_2023_T02 | score_high_return_low_false_positive_then_4c | 사고 전 Stage3-Green proxy가 false positive였고, 4C-watch가 drawdown protection을 개선했다. |


## 6. Evidence Source Map

| case_id | evidence source status | notes |
|---|---|---|
| R10L2_C01_DAEWOO_2020 | public financial results / reports / stock-web price | 가격 row는 fully validated. non-price source는 standalone research note 수준. |
| R10L2_C02_SAMPYO_2021 | public news/reports / stock-web price | price/spread narrative는 shadow-only; production 적용 전 report URL 재확인 필요. |
| R10L2_C03_HDC_2022 | public accident and investigation record / stock-web price | HDC 사고 날짜·조사 맥락은 web source로 확인됨. |
| R10L2_C04_GSENC_2023 | public accident/rebuild narrative / stock-web price | OHLC는 validated. non-price URL은 handoff에서 DART/KRX/news 재검증 필요. |

## 7. Price Data Source Map

| symbol | company_name | profile_path | price_shard_root | price_basis | corporate_action_180D_status |
| --- | --- | --- | --- | --- | --- |
| 047040 | 대우건설 | atlas/symbol_profiles/047/047040.json | atlas/ohlcv_tradable_by_symbol_year | tradable_raw | clean_180D_window |
| 038500 | 삼표시멘트 | atlas/symbol_profiles/038/038500.json | atlas/ohlcv_tradable_by_symbol_year | tradable_raw | clean_180D_window |
| 294870 | HDC현대산업개발 | atlas/symbol_profiles/294/294870.json | atlas/ohlcv_tradable_by_symbol_year | tradable_raw | clean_180D_window |
| 006360 | GS건설 | atlas/symbol_profiles/006/006360.json | atlas/ohlcv_tradable_by_symbol_year | tradable_raw | clean_180D_window |


## 8. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | trigger_outcome_label |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R10L2_C01_DAEWOO_2020_T01 | R10L2_C01_DAEWOO_2020 | 047040 | Stage2 | 2020-10-29 | 2020-10-30 | 3000 | 123.3 | -1.0 | 218.0 | -1.0 | 2021-06-02 | 9540 | excellent_entry |
| R10L2_C01_DAEWOO_2020_T02 | R10L2_C01_DAEWOO_2020 | 047040 | Stage2-Actionable | 2020-11-13 | 2020-11-16 | 3595 | 90.3 | -4.5 | 165.4 | -4.5 | 2021-06-02 | 9540 | excellent_entry |
| R10L2_C01_DAEWOO_2020_T03 | R10L2_C01_DAEWOO_2020 | 047040 | Stage3-Yellow | 2021-01-28 | 2021-01-28 | 6320 | 50.9 | -16.8 | 50.9 | -16.8 | 2021-06-02 | 9540 | good_entry |
| R10L2_C01_DAEWOO_2020_T04 | R10L2_C01_DAEWOO_2020 | 047040 | Stage3-Green | 2021-04-29 | 2021-04-29 | 7690 | 24.1 | -10.3 | 24.1 | -10.3 | 2021-06-02 | 9540 | late_entry |
| R10L2_C01_DAEWOO_2020_T05 | R10L2_C01_DAEWOO_2020 | 047040 | Stage4B | 2021-06-02 | 2021-06-02 | 8870 | 7.6 | -22.1 | 7.6 | -22.1 | 2021-06-02 | 9540 | event_premium |
| R10L2_C02_SAMPYO_2021_T01 | R10L2_C02_SAMPYO_2021 | 038500 | Stage2 | 2021-01-19 | 2021-01-19 | 4280 | 43.2 | -8.6 | 57.7 | -8.6 | 2021-06-22 | 6750 | good_entry |
| R10L2_C02_SAMPYO_2021_T02 | R10L2_C02_SAMPYO_2021 | 038500 | Stage2-Actionable | 2021-02-03 | 2021-02-03 | 4905 | 25.0 | -7.4 | 37.6 | -7.4 | 2021-06-22 | 6750 | good_entry |
| R10L2_C02_SAMPYO_2021_T03 | R10L2_C02_SAMPYO_2021 | 038500 | Stage3-Yellow | 2021-03-24 | 2021-03-24 | 5130 | 31.6 | -3.0 | 31.6 | -3.0 | 2021-06-22 | 6750 | excellent_entry |
| R10L2_C02_SAMPYO_2021_T04 | R10L2_C02_SAMPYO_2021 | 038500 | Stage4B | 2021-06-22 | 2021-06-22 | 6340 | 6.5 | -14.8 | 6.5 | -14.8 | 2021-06-22 | 6750 | event_premium |
| R10L2_C03_HDC_2022_T01 | R10L2_C03_HDC_2022 | 294870 | Stage4C | 2022-01-11 | 2022-01-12 | 20850 | 8.9 | -36.9 | 8.9 | -52.2 | 2022-01-12 | 22700 | hard_4c_success |
| R10L2_C03_HDC_2022_T02 | R10L2_C03_HDC_2022 | 294870 | Stage4C | 2022-03-14 | 2022-03-15 | 16200 | 8.3 | -32.4 | 8.3 | -39.6 | 2022-03-30 | 17550 | hard_4c_late |
| R10L2_C04_GSENC_2023_T01 | R10L2_C04_GSENC_2023 | 006360 | Stage3-Green | 2023-04-28 | 2023-04-28 | 21600 | 2.5 | -38.1 | 2.5 | -41.3 | 2023-05-24 | 22150 | false_positive_score |
| R10L2_C04_GSENC_2023_T02 | R10L2_C04_GSENC_2023 | 006360 | Stage4C | 2023-05-02 | 2023-05-02 | 20500 | 8.0 | -34.8 | 8.0 | -38.2 | 2023-05-24 | 22150 | hard_4c_success |
| R10L2_C04_GSENC_2023_T03 | R10L2_C04_GSENC_2023 | 006360 | Stage4C | 2023-07-05 | 2023-07-06 | 14520 | 3.9 | -12.7 | 3.9 | -12.7 | 2023-07-17 | 15080 | hard_4c_late |


## 9. Trigger-Level OHLC Backtest Tables

핵심 수치 해석:

- 대우건설은 Stage2-Actionable에서 Green보다 훨씬 앞서고, MFE90/180이 압도적으로 우수했다.
- 삼표시멘트는 Stage3-Yellow가 가장 깔끔했다. Stage2-Actionable도 좋지만 Yellow가 MAE를 줄였다.
- HDC현대산업개발과 GS건설은 “좋은 건설 사이클 점수”가 품질·안전 4C를 만나면 무력화될 수 있음을 보여준다.
- 4B는 price-only local peak와 non-price overheat를 분리해야 한다.

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | green_lateness_ratio | four_b_local_peak_proximity | four_b_full_window_peak_proximity | trigger_outcome_label |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R10L2_C01_DAEWOO_2020_T01 | 047040 | Stage2 | 2020-10-30 | 3000 | 65.7 | 123.3 | 218.0 | -1.0 | -1.0 | -1.0 | not_applicable | not_applicable | not_applicable | excellent_entry |
| R10L2_C01_DAEWOO_2020_T02 | 047040 | Stage2-Actionable | 2020-11-16 | 3595 | 38.2 | 90.3 | 165.4 | -4.5 | -4.5 | -4.5 | 0.68 | not_applicable | not_applicable | excellent_entry |
| R10L2_C01_DAEWOO_2020_T03 | 047040 | Stage3-Yellow | 2021-01-28 | 6320 | 6.0 | 50.9 | 50.9 | -16.8 | -16.8 | -16.8 | 0.68 | not_applicable | not_applicable | good_entry |
| R10L2_C01_DAEWOO_2020_T04 | 047040 | Stage3-Green | 2021-04-29 | 7690 | 11.3 | 24.1 | 24.1 | -10.3 | -10.3 | -10.3 | 0.68 | not_applicable | not_applicable | late_entry |
| R10L2_C01_DAEWOO_2020_T05 | 047040 | Stage4B | 2021-06-02 | 8870 | 7.6 | 7.6 | 7.6 | -12.2 | -22.1 | -22.1 | not_applicable | 0.9 | 0.9 | event_premium |
| R10L2_C02_SAMPYO_2021_T01 | 038500 | Stage2 | 2021-01-19 | 4280 | 32.2 | 43.2 | 57.7 | -8.6 | -8.6 | -8.6 | not_applicable | not_applicable | not_applicable | good_entry |
| R10L2_C02_SAMPYO_2021_T02 | 038500 | Stage2-Actionable | 2021-02-03 | 4905 | 15.4 | 25.0 | 37.6 | -7.4 | -7.4 | -7.4 | 0.05 | not_applicable | not_applicable | good_entry |
| R10L2_C02_SAMPYO_2021_T03 | 038500 | Stage3-Yellow | 2021-03-24 | 5130 | 19.5 | 31.6 | 31.6 | -3.0 | -3.0 | -3.0 | 0.05 | not_applicable | not_applicable | excellent_entry |
| R10L2_C02_SAMPYO_2021_T04 | 038500 | Stage4B | 2021-06-22 | 6340 | 6.5 | 6.5 | 6.5 | -14.8 | -14.8 | -14.8 | not_applicable | 0.8 | 0.8 | event_premium |
| R10L2_C03_HDC_2022_T01 | 294870 | Stage4C | 2022-01-12 | 20850 | 8.9 | 8.9 | 8.9 | -35.3 | -36.9 | -52.2 | not_applicable | not_applicable | not_applicable | hard_4c_success |
| R10L2_C03_HDC_2022_T02 | 294870 | Stage4C | 2022-03-15 | 16200 | 8.3 | 8.3 | 8.3 | -32.4 | -32.4 | -39.6 | not_applicable | not_applicable | not_applicable | hard_4c_late |
| R10L2_C04_GSENC_2023_T01 | 006360 | Stage3-Green | 2023-04-28 | 21600 | 2.5 | 2.5 | 2.5 | -8.2 | -38.1 | -41.3 | not_applicable | not_applicable | not_applicable | false_positive_score |
| R10L2_C04_GSENC_2023_T02 | 006360 | Stage4C | 2023-05-02 | 20500 | 8.0 | 8.0 | 8.0 | -3.3 | -34.8 | -38.2 | not_applicable | not_applicable | not_applicable | hard_4c_success |
| R10L2_C04_GSENC_2023_T03 | 006360 | Stage4C | 2023-07-06 | 14520 | 3.9 | 3.9 | 3.9 | -7.4 | -12.7 | -12.7 | not_applicable | not_applicable | not_applicable | hard_4c_late |


## 10. 1D Price Path Summaries

값 형식: `close_return_pct / high_to_date_return_pct / low_to_date_return_pct`.

| case_id | anchor | D+1 | D+5 | D+20 | D+30 | D+90 | D+180 | D+252 | D+504 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R10L2_C01_DAEWOO_2020 | T02 2020-11-16 close 3595 | 0.4 / 3.6 / -2.6 | -1.7 / 3.6 / -4.5 | 25.2 / 38.2 / -4.5 | 61.1 / 73.3 / -4.5 | 88.3 / 90.3 / -4.5 | ~147 / 165.4 / -4.5 | same_peak_9540 | same_peak_9540 |
| R10L2_C02_SAMPYO_2021 | T03 2021-03-24 close 5130 | 7.2 / 9.0 / -2.5 | 9.4 / 18.5 / -2.5 | -1.0 / 19.5 / -2.9 | 4.7 / 19.5 / -2.9 | 21.2 / 31.6 / -2.9 | ~10 / 31.6 / -2.9 | same_peak_6750 | same_peak_6750 |
| R10L2_C03_HDC_2022 | T01 2022-01-12 close 20850 | -1.2 / 8.2 / -6.7 | -23.7 / 8.2 / -25.7 |  | -25.2 / 8.2 / -35.3 | ~ -30 / 8.2 / -36.9 | ~ -50 / 8.2 / -52.2 | low_9960_area |  |
| R10L2_C04_GSENC_2023 | T02 2023-05-02 close 20500 | -2.0 / 0.0 / -3.4 | 0.7 / 6.8 / -3.4 | 1.2 / 8.0 / -3.4 | ~1 / 8.0 / -3.4 | ~ -30 / 8.0 / -38.2 | ~ -35 / 8.0 / -38.2 | recovery later; not treated as entry |  |


## 11. Case Trigger Comparison

### R10L2_C01_DAEWOO_2020

대우건설은 Stage3-Green을 기다리면 이미 열차가 많이 지나간다. Stage2-Actionable entry 2020-11-16 close 3,595에서 MFE90은 90.3%, MFE180은 165.4%, MAE90은 -4.5%였다. 반면 Stage3-Green 2021-04-29 close 7,690은 MFE90 24.1%, MAE90 -10.4%로, 더 늦고 더 불편했다. 이 case는 **Stage2 evidence를 너무 무시하지 말라**는 rule을 직접 검증한다.

### R10L2_C02_SAMPYO_2021

삼표시멘트는 Stage2도 좋았지만, Stage3-Yellow가 더 좋은 균형점이었다. Stage3-Yellow 2021-03-24 close 5,130은 MFE90 31.6%, MAE90 -2.9%였다. 이 case는 무조건 Stage2로 앞당기라는 뜻이 아니라, **spread/margin bridge가 명확해지는 Yellow tier**가 entry tier로 충분히 살아있음을 보여준다.

### R10L2_C03_HDC_2022

HDC는 일반적인 EPS/OP rerating case가 아니라 hard 4C다. 2022-01-11 사고 후 다음 거래일 entry row 2022-01-12 close 20,850에서 MAE90은 -36.9%, MAE180은 -52.2%였다. 2022-03-14 조사 결과 확인 이후 4C는 맞지만, 가격 보호 관점에서는 늦다.

### R10L2_C04_GSENC_2023

GS건설은 사고 전 Stage3-Green proxy가 false positive가 될 수 있음을 보여준다. 2023-04-28 close 21,600의 Green proxy는 MFE90 2.5%, MAE90 -38.1%였다. 4C-watch를 2023-05-02로 앞당기면 long entry가 아니라 **Green block / risk protection**이 된다.

## 12. Stage2 → Stage4 Audit

| case_id | Stage2/early trigger verdict | audit |
|---|---|---|
| R10L2_C01_DAEWOO_2020 | promote_to_Stage2_Actionable | backlog/margin/RS 조합은 Green보다 훨씬 좋은 entry였다. |
| R10L2_C02_SAMPYO_2021 | keep Yellow tier | Stage2도 괜찮지만 Yellow가 MAE를 줄였다. |
| R10L2_C03_HDC_2022 | hard 4C override | Stage2/3 long thesis가 아니라 risk block case다. |
| R10L2_C04_GSENC_2023 | hard 4C override | Green proxy는 false positive. safety/quality risk가 우선한다. |

## 13. Stage3 Yellow / Green Lateness Audit

| case_id | Stage2-Actionable entry | Stage3-Green entry | green_lateness_ratio | verdict |
|---|---:|---:|---:|---|
| R10L2_C01_DAEWOO_2020 | 3,595 | 7,690 | 0.68 | Green이 upside 대부분을 소진한 late entry |
| R10L2_C02_SAMPYO_2021 | 4,905 | not confirmed Green | 0.05 proxy via Yellow | Yellow tier 유지가 더 자연스러움 |
| R10L2_C03_HDC_2022 | not_applicable | not_applicable | not_applicable | 4C case |
| R10L2_C04_GSENC_2023 | not_applicable | 21,600 false proxy | not_applicable | Green relax 금지; risk gate 필요 |

## 14. 4B Timing Audit

| case_id | trigger | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| R10L2_C01_DAEWOO_2020 | T05 | 0.89 | 0.89 | good_full_window_4B_timing |
| R10L2_C02_SAMPYO_2021 | T04 | 0.78 | 0.78 | price_only_local_4B_watch_not_full_exit |

대우건설 4B는 full-window peak와 가까운 위치였다. 삼표시멘트는 peak 근처였지만 price-only 성격이 강하다. 따라서 4B는 하나의 매도 버튼이 아니라, **non-price evidence가 붙을 때만 full 4B**로 승격해야 한다.

## 15. 4C Protection Audit

| case_id | early 4C trigger | MAE90 after 4C | MAE180 after 4C | protection label |
|---|---|---:|---:|---|
| R10L2_C03_HDC_2022 | 2022-01-12 | -36.9 | -52.2 | hard_4c_success |
| R10L2_C04_GSENC_2023 | 2023-05-02 | -34.8 | -38.2 | hard_4c_success / source revalidation needed |

4C는 entry 성과가 아니라 “더 이상 Green으로 보지 말라”는 차단기다. 배전반의 차단기처럼, 평소에는 조용하지만 합선이 감지되면 수익률 계산보다 먼저 회로를 끊는다.

## 16. Baseline Score Simulation

Baseline proxy는 대우건설을 너무 늦게 Green으로 잡고, GS건설의 pre-accident Green proxy를 false positive로 남긴다. Component breakdown은 machine-readable row에 포함했다.

| trigger_id | symbol | trigger_type | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | selected_by_profile | score_return_alignment_label |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R10L2_C01_DAEWOO_2020_T01 | 047040 | Stage2 | 100 | Stage3-Green | 100 | Stage3-Green | False | score_mid_return_high_promote_candidate |
| R10L2_C01_DAEWOO_2020_T02 | 047040 | Stage2-Actionable | 100 | Stage3-Green | 100 | Stage3-Green | True | score_mid_return_high_promote_candidate |
| R10L2_C01_DAEWOO_2020_T03 | 047040 | Stage3-Yellow | 100 | Stage3-Green | 100 | Stage3-Green | False | score_mid_return_high_promote_candidate |
| R10L2_C01_DAEWOO_2020_T04 | 047040 | Stage3-Green | 100 | Stage3-Green | 100 | Stage3-Green | False | score_mid_return_high_promote_candidate |
| R10L2_C01_DAEWOO_2020_T05 | 047040 | Stage4B | 100 | Stage4B-watch | 100 | Stage4B-watch | False | score_high_return_low_false_positive |
| R10L2_C02_SAMPYO_2021_T01 | 038500 | Stage2 | 97 | Stage3-Green | 100 | Stage3-Green | False | score_mid_return_high_promote_candidate |
| R10L2_C02_SAMPYO_2021_T02 | 038500 | Stage2-Actionable | 100 | Stage3-Green | 100 | Stage3-Green | False | score_mid_return_high_promote_candidate |
| R10L2_C02_SAMPYO_2021_T03 | 038500 | Stage3-Yellow | 100 | Stage3-Green | 100 | Stage3-Green | True | score_mid_return_high_promote_candidate |
| R10L2_C02_SAMPYO_2021_T04 | 038500 | Stage4B | 100 | Stage4B-watch | 100 | Stage4B-watch | False | score_mid_return_high_promote_candidate |
| R10L2_C03_HDC_2022_T01 | 294870 | Stage4C | 1 | Stage4C | 0 | Stage4C | True | risk_high_drawdown_high_correct_protect |
| R10L2_C03_HDC_2022_T02 | 294870 | Stage4C | 5 | Stage4C | 0 | Stage4C | False | risk_high_drawdown_high_correct_protect |
| R10L2_C04_GSENC_2023_T01 | 006360 | Stage3-Green | 97 | Stage3-Green | 100 | Stage3-Green | False | score_high_return_low_false_positive |
| R10L2_C04_GSENC_2023_T02 | 006360 | Stage4C | 5 | Stage4C | 0 | Stage4C | True | risk_high_drawdown_high_correct_protect |
| R10L2_C04_GSENC_2023_T03 | 006360 | Stage4C | 5 | Stage4C | 0 | Stage4C | False | risk_high_drawdown_high_correct_protect |


## 17. Shadow Profile Optimization Loop

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,4,4,4,16.5,12.0,-20.7,-21.2,16.5,-22.6,0.5,0.5,0.25,1,1,0.68,not_applicable,not_applicable,reference; late Green and pre-4C false positive remain visible
profile_comparison,stage2_actionable_early_evidence_plus,4,4,4,36.2,24.3,-19.8,-18.9,58.0,-25.0,0.5,0.5,0.0,0,0,0.4,not_applicable,not_applicable,best blended profile; early cyclic entries + hard 4C protection
profile_comparison,stage3_yellow_entry_relaxed,4,3,3,28.0,31.6,-20.3,-9.9,34.7,-23.3,0.67,0.33,0.0,1,0,0.4,not_applicable,not_applicable,"useful, but misses Daewoo's very early Stage2-Actionable"
profile_comparison,green_confirmation_timing_relaxed,4,4,4,22.4,16.5,-19.2,-16.0,23.5,-22.0,0.5,0.5,0.25,1,1,0.68,not_applicable,not_applicable,too broad; GS false positive remains
profile_comparison,four_b_peak_timing_tuned,2,2,0,overlay_only,overlay_only,overlay_only,overlay_only,overlay_only,overlay_only,overlay_only,overlay_only,0.0,0,0,not_applicable,0.82,0.82,"Daewoo good full-window 4B; Sampyo price-only 4B should stay watch, not full exit"
profile_comparison,four_c_thesis_break_earlier,2,2,2,8.4,8.4,-35.8,-35.8,8.4,-45.2,0.0,1.0,0.0,0,0,not_applicable,not_applicable,not_applicable,"for protection, not entry; hard safety/legal risk should override long entry"
```

Best shadow profile:

```text
stage2_actionable_early_evidence_plus_with_4c_guardrail
```

## 18. Before / After Backtest Comparison

| case_id | symbol | best_actual_trigger | baseline_selected_trigger | after_selected_trigger | baseline_MFE_90D_pct | after_MFE_90D_pct | baseline_MAE_90D_pct | after_MAE_90D_pct | return_improvement_90D_pct | risk_change_90D_pct | reason_after_profile_selected |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R10L2_C01_DAEWOO_2020 | 047040 | T02 Stage2-Actionable | T04 Stage3-Green | T02 Stage2-Actionable | 24.1 | 90.3 | -10.4 | -4.5 | 66.2 | 5.9 | backlog + margin bridge + RS created early Stage2-Actionable |
| R10L2_C02_SAMPYO_2021 | 038500 | T03 Stage3-Yellow | T03 Stage3-Yellow | T03 Stage3-Yellow | 31.6 | 31.6 | -2.9 | -2.9 | 0.0 | 0.0 | Yellow tier remains valid; no need for broad Green relaxation |
| R10L2_C03_HDC_2022 | 294870 | T01 early hard 4C | T02 investigation-confirmed 4C | T01 early hard 4C | 8.3 | 8.9 | -32.4 | -36.9 | not_long_entry | earlier protection | construction-safety 4C must be early protection, not a long-entry signal |
| R10L2_C04_GSENC_2023 | 006360 | T02 early 4C-watch | T01 pre-accident Stage3-Green proxy | T02 early 4C-watch | 2.5 | 8.0 | -38.1 | -34.8 | avoid_false_long | 3.3 | quality/rebuild risk blocks Green and turns row into 4C protection |


## 19. Score-Return Alignment Matrix

| alignment_label | trigger_count | avg_weighted_score_before | avg_weighted_score_after | avg_MFE_90D_pct | avg_MAE_90D_pct | verdict |
|---|---:|---:|---:|---:|---:|---|
| score_low_return_high_missed_structural | 1 | 76.0 | 88.0 | 123.3 | -1.0 | Stage2 evidence needs promotion |
| score_mid_return_high_promote_candidate | 6 | mixed | mixed | 50+ | -6~-10 | Stage2-Actionable/Yellow useful |
| score_high_return_low_false_positive | 1 | high | lower after risk override | 2.5 | -38.1 | Green must be blocked by quality/legal risk |
| risk_high_drawdown_high_correct_protect | 4 | risk score high | stronger risk score | 8.4 | -35.8 | 4C protection validated |

## 20. Weight Sensitivity Table

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_backlog_margin_rs_combo,0,2,+2,Daewoo Stage2-Actionable produced MFE90 90.3 and MFE180 165.4 with MAE90 -4.5 before Green.,baseline selected Green MFE90 24.1/MAE90 -10.4; after selected Stage2-Actionable MFE90 90.3/MAE90 -4.5.,R10L2_C01_DAEWOO_2020_T02,1,exploratory-to-moderate; needs additional housing-cycle counterexamples before production
shadow_weight,stage3_yellow_spread_margin_bridge,0,1,+1,"Sampyo Stage3-Yellow gave the best risk-adjusted cement-cycle entry: MFE90 31.6, MAE90 -2.9.",keeps Yellow tier for price/spread bridge cases instead of forcing delayed Green.,R10L2_C02_SAMPYO_2021_T03,1,exploratory; not enough cases for stronger delta
shadow_weight,construction_quality_execution_legal_4c_override,0,3,+3,HDC and GS safety/quality thesis-break rows produced deep MAE90/180; hard risk should override positive construction-cycle scores.,GS baseline Stage3-Green proxy had MFE90 2.5 and MAE90 -38.1; 4C-watch avoids treating this as a long entry. HDC early 4C captured -36.9 MAE90 risk.,R10L2_C03_HDC_2022_T01|R10L2_C04_GSENC_2023_T02,2,moderate/strong for shadow because two different large builders show same risk shape
shadow_weight,price_only_4b_reject_as_full_exit,1,0,-1,Sampyo 4B was near local peak but only price/positioning evidence; Daewoo 4B had clearer event/valuation overheat.,separating local price-only 4B from full 4B avoids prematurely killing cyclic winners without non-price risk.,R10L2_C01_DAEWOO_2020_T05|R10L2_C02_SAMPYO_2021_T04,2,exploratory; preserve as watch overlay
```

## 21. Optimization Decision Log

```jsonl
{"row_type":"optimization_decision","decision_id":"R10L2_DECISION_01","hypothesis":"Backlog/margin bridge plus relative strength should promote some construction-cycle Stage2 rows to Stage2-Actionable.","tested_cases":["R10L2_C01_DAEWOO_2020","R10L2_C02_SAMPYO_2021"],"tested_trigger_ids":["R10L2_C01_DAEWOO_2020_T02","R10L2_C02_SAMPYO_2021_T02","R10L2_C02_SAMPYO_2021_T03"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus","backtest_result_summary":"Daewoo T02 greatly outperformed Green; Sampyo Yellow had better risk-adjusted profile than forcing Green.","accepted_or_rejected":"accepted_shadow_only","reason":"missed_structural risk falls without adding observed false positive in this small R10 set.","proposed_shadow_rule":"promote Stage2 to Stage2-Actionable when backlog/margin bridge + RS close together.","delta_magnitude":"+2 for Daewoo-type axis, +1 for spread-margin Yellow","why_not_larger_delta":"R10 sample is four cases and only two cyclical success cases.","risks":"construction cycles are macro-sensitive; raw/unadjusted price basis can overstate if corporate actions occur outside observed windows.","next_validation_needed":"Find 2020-2022 failed housing backlog cases and 2021-2022 cement false positives."}
{"row_type":"optimization_decision","decision_id":"R10L2_DECISION_02","hypothesis":"Construction quality/safety thesis breaks need hard 4C override before earnings confirmation catches up.","tested_cases":["R10L2_C03_HDC_2022","R10L2_C04_GSENC_2023"],"tested_trigger_ids":["R10L2_C03_HDC_2022_T01","R10L2_C04_GSENC_2023_T02"],"baseline_profile":"baseline_current_proxy","selected_profile":"four_c_thesis_break_earlier","backtest_result_summary":"HDC early 4C was followed by MAE90 -36.9 and MAE180 -52.2; GS early 4C-watch was followed by MAE90 -34.8.","accepted_or_rejected":"accepted_shadow_only","reason":"same pattern repeats across two large builders: safety/legal quality risk precedes or overwhelms financial confirmation.","proposed_shadow_rule":"execution/legal/accounting trust risk >= threshold blocks Green and promotes 4C-watch/hard 4C.","delta_magnitude":"+3 risk override","why_not_larger_delta":"GS non-price source URL should be revalidated before production; HDC source was easier to verify.","risks":"not every accident is thesis-breaking; require named site, material cost/liability, administrative/legal risk, or rebuild/order risk.","next_validation_needed":"Add non-fatal but recoverable accident cases to reduce false 4C breaks."}
```

## 22. Overfitting / Robustness Check

- usable case 수: 4.
- usable trigger 수: 14.
- 서로 다른 archetype: 4개.
- 방향성은 두 갈래다. 하나는 early cyclic evidence promotion, 다른 하나는 safety/quality 4C override.
- Stage2 promotion은 아직 R10 안에서 2개 성공축뿐이므로 +5 불가.
- 4C override는 HDC/GS 두 대형사에서 반복되지만, GS non-price source는 handoff revalidation이 필요하므로 production change 금지.
- counterexample_search_status: incomplete. 다음 R10/R11 반복에서 PF/미분양/시멘트 원가 실패 사례를 더 넣어야 한다.

## 23. Cross-case Aggregate Metrics

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,below_entry_90D_rate,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,2,2,83.2,83.2,-4.8,-4.8,137.8,-4.8,1.0,not_applicable,not_applicable,not_applicable,representative rows only; 4B/4C overlay rows separated
aggregate_metric,Stage2-Actionable,2,2,57.6,57.6,-6.0,-6.0,101.5,-6.0,1.0,0.4,not_applicable,not_applicable,representative rows only; 4B/4C overlay rows separated
aggregate_metric,Stage3-Yellow,2,2,41.2,41.2,-9.9,-9.9,41.2,-9.9,1.0,0.4,not_applicable,not_applicable,representative rows only; 4B/4C overlay rows separated
aggregate_metric,Stage3-Green,2,2,13.3,13.3,-24.2,-24.2,13.3,-25.8,1.0,0.7,not_applicable,not_applicable,representative rows only; 4B/4C overlay rows separated
aggregate_metric,Stage4B,2,0,not_applicable,not_applicable,not_applicable,not_applicable,not_applicable,not_applicable,overlay_only,not_applicable,0.8,0.8,overlay only
aggregate_metric,Stage4C,4,2,8.4,8.4,-35.8,-35.8,8.4,-45.2,1.0,not_applicable,not_applicable,not_applicable,representative rows only; 4B/4C overlay rows separated
```

## 24. Score-Price Alignment Verdict

이번 R10 Loop 2의 핵심 결론은 두 가지다.

1. **좋은 건설 사이클은 Green보다 먼저 보이는 경우가 있다.** 대우건설은 Stage2-Actionable이 Green보다 훨씬 좋은 entry였고, 삼표시멘트는 Yellow가 가장 안정적이었다.
2. **건설사는 품질·안전 4C가 EPS rerating을 무효화할 수 있다.** HDC와 GS건설은 execution/legal/accounting-trust risk가 일정 threshold를 넘으면 Green을 block해야 한다.

## 25. Validation Scope / Non-Validation Scope

### this_round_validates

- Stage2-Actionable early evidence: backlog/margin bridge + relative strength.
- Stage3-Yellow guardrail: spread/margin bridge가 명확하지만 full Green 전인 건자재 case.
- 4B split: non-price evidence가 약한 price-only local 4B는 full exit로 취급하지 않기.
- 4C hard override: 현장 안전·품질·재시공/행정 리스크는 Green을 즉시 차단할 수 있음.

### this_round_does_not_validate

- 광범위한 Stage3-Green relaxation.
- PF/미분양/금융비용 중심의 hard 4C.
- 대형 건설주 외 중소 건설사 회계신뢰도 gate.
- adjusted-price revalidation.

## 26. Shadow Weight Calibration

Accepted shadow-only changes:

- `stage2_actionable_backlog_margin_rs_combo`: +2
- `stage3_yellow_spread_margin_bridge`: +1
- `construction_quality_execution_legal_4c_override`: +3
- `price_only_4b_reject_as_full_exit`: -1

No production scoring changed.

## 27. Machine-Readable Rows

### 27.1 Price source validation row JSONL

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 27.2 Case rows JSONL

```jsonl
{"row_type":"case","case_id":"R10L2_C01_DAEWOO_2020","symbol":"047040","company_name":"대우건설","round":"R10","loop":"2","sector":"건설·부동산·건자재","case_type":"structural_success","primary_archetype":"HOUSING_BACKLOG_MARGIN_RERATING","best_trigger":"R10L2_C01_DAEWOO_2020_T02","calibration_usable":true,"historical_window_status":"504D_available","score_price_alignment":"score_mid_return_high_promote_candidate","price_source":"Songdaiki/stock-web","notes":"Stage2-Actionable가 Stage3-Green보다 112 trading days 앞서고 MFE90/180이 우수했다."}
{"row_type":"case","case_id":"R10L2_C02_SAMPYO_2021","symbol":"038500","company_name":"삼표시멘트","round":"R10","loop":"2","sector":"건설·부동산·건자재","case_type":"stage2_promote_candidate","primary_archetype":"CEMENT_PRICE_SPREAD_REPRICING","best_trigger":"R10L2_C02_SAMPYO_2021_T03","calibration_usable":true,"historical_window_status":"504D_available","score_price_alignment":"score_mid_return_high_promote_candidate","price_source":"Songdaiki/stock-web","notes":"Stage3-Yellow가 가장 안정적인 MFE/MAE 조합. Stage2-Actionable도 양호."}
{"row_type":"case","case_id":"R10L2_C03_HDC_2022","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"2","sector":"건설·부동산·건자재","case_type":"4C_thesis_break","primary_archetype":"CONSTRUCTION_SAFETY_THESIS_BREAK","best_trigger":"R10L2_C03_HDC_2022_T01","calibration_usable":true,"historical_window_status":"504D_available","score_price_alignment":"hard_4c_success","price_source":"Songdaiki/stock-web","notes":"사고 당일/다음 거래일 4C가 이후 MAE90/180 drawdown을 가장 빨리 경고했다."}
{"row_type":"case","case_id":"R10L2_C04_GSENC_2023","symbol":"006360","company_name":"GS건설","round":"R10","loop":"2","sector":"건설·부동산·건자재","case_type":"false_positive_to_4C","primary_archetype":"CONSTRUCTION_QUALITY_REBUILD_THESIS_BREAK","best_trigger":"R10L2_C04_GSENC_2023_T02","calibration_usable":true,"historical_window_status":"504D_available","score_price_alignment":"score_high_return_low_false_positive_then_4c","price_source":"Songdaiki/stock-web","notes":"사고 전 Stage3-Green proxy가 false positive였고, 4C-watch가 drawdown protection을 개선했다."}
```

### 27.3 Trigger rows JSONL

```jsonl
{"row_type":"trigger","trigger_id":"R10L2_C01_DAEWOO_2020_T01","case_id":"R10L2_C01_DAEWOO_2020","symbol":"047040","company_name":"대우건설","round":"R10","loop":"2","sector":"건설·부동산·건자재","primary_archetype":"HOUSING_BACKLOG_MARGIN_RERATING","trigger_type":"Stage2","trigger_date":"2020-10-29","evidence_available_at_that_date":"3Q20/2020년 하반기 주택·건축 이익 체력 확인. 아직 full Stage3라기보다 Stage2 evidence.","evidence_source":"공시/실적자료/증권사 리포트 흐름; 가격 row: stock-web 047040 2020/2021 shards","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2020.csv","profile_path":"atlas/symbol_profiles/047/047040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-10-30","entry_price":3000,"MFE_30D_pct":65.7,"MFE_90D_pct":123.3,"MFE_180D_pct":218.0,"MFE_1Y_pct":218.0,"MFE_2Y_pct":218.0,"MAE_30D_pct":-1.0,"MAE_90D_pct":-1.0,"MAE_180D_pct":-1.0,"MAE_1Y_pct":-1.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-06-02","peak_price":9540,"drawdown_after_peak_pct":-27.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L2_C01_DAEWOO_2020_2020-10-30_3000","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R10L2_C01_DAEWOO_2020_T02","case_id":"R10L2_C01_DAEWOO_2020","symbol":"047040","company_name":"대우건설","round":"R10","loop":"2","sector":"건설·부동산·건자재","primary_archetype":"HOUSING_BACKLOG_MARGIN_RERATING","trigger_type":"Stage2-Actionable","trigger_date":"2020-11-13","evidence_available_at_that_date":"초기 evidence에 상대강도·거래대금이 붙은 구간. Stage3 확인 전이지만 entry quality가 높음.","evidence_source":"공시/실적자료/가격 상대강도; 가격 row: stock-web 047040 2020/2021 shards","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2020.csv","profile_path":"atlas/symbol_profiles/047/047040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-11-16","entry_price":3595,"MFE_30D_pct":38.2,"MFE_90D_pct":90.3,"MFE_180D_pct":165.4,"MFE_1Y_pct":165.4,"MFE_2Y_pct":165.4,"MAE_30D_pct":-4.5,"MAE_90D_pct":-4.5,"MAE_180D_pct":-4.5,"MAE_1Y_pct":-4.5,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-06-02","peak_price":9540,"drawdown_after_peak_pct":-27.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"0.68","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L2_C01_DAEWOO_2020_2020-11-16_3595","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R10L2_C01_DAEWOO_2020_T03","case_id":"R10L2_C01_DAEWOO_2020","symbol":"047040","company_name":"대우건설","round":"R10","loop":"2","sector":"건설·부동산·건자재","primary_archetype":"HOUSING_BACKLOG_MARGIN_RERATING","trigger_type":"Stage3-Yellow","trigger_date":"2021-01-28","evidence_available_at_that_date":"실적 추정 및 주택 마진 bridge가 더 명확해진 구간. 그러나 이미 Stage2-Actionable 대비 entry가 높아짐.","evidence_source":"실적/리포트/가격 row: stock-web 047040 2021 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2021.csv","profile_path":"atlas/symbol_profiles/047/047040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-01-28","entry_price":6320,"MFE_30D_pct":6.0,"MFE_90D_pct":50.9,"MFE_180D_pct":50.9,"MFE_1Y_pct":50.9,"MFE_2Y_pct":50.9,"MAE_30D_pct":-16.8,"MAE_90D_pct":-16.8,"MAE_180D_pct":-16.8,"MAE_1Y_pct":-16.8,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-06-02","peak_price":9540,"drawdown_after_peak_pct":-27.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"0.68","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"good_entry","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L2_C01_DAEWOO_2020_2021-01-28_6320","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R10L2_C01_DAEWOO_2020_T04","case_id":"R10L2_C01_DAEWOO_2020","symbol":"047040","company_name":"대우건설","round":"R10","loop":"2","sector":"건설·부동산·건자재","primary_archetype":"HOUSING_BACKLOG_MARGIN_RERATING","trigger_type":"Stage3-Green","trigger_date":"2021-04-29","evidence_available_at_that_date":"공개 evidence 2~3개가 닫히고 가격도 확인됐지만, Stage2-Actionable 대비 상승분 상당 부분을 소진.","evidence_source":"실적발표/리포트/가격 row: stock-web 047040 2021 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2021.csv","profile_path":"atlas/symbol_profiles/047/047040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-04-29","entry_price":7690,"MFE_30D_pct":11.3,"MFE_90D_pct":24.1,"MFE_180D_pct":24.1,"MFE_1Y_pct":24.1,"MFE_2Y_pct":24.1,"MAE_30D_pct":-10.3,"MAE_90D_pct":-10.3,"MAE_180D_pct":-10.3,"MAE_1Y_pct":-10.3,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-06-02","peak_price":9540,"drawdown_after_peak_pct":-27.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"0.68","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"late_entry","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L2_C01_DAEWOO_2020_2021-04-29_7690","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R10L2_C01_DAEWOO_2020_T05","case_id":"R10L2_C01_DAEWOO_2020","symbol":"047040","company_name":"대우건설","round":"R10","loop":"2","sector":"건설·부동산·건자재","primary_archetype":"HOUSING_BACKLOG_MARGIN_RERATING","trigger_type":"Stage4B","trigger_date":"2021-06-02","evidence_available_at_that_date":"단기 blowoff 및 event/positioning overheat. 매도 hard gate가 아니라 Stage3 + 4B-watch overlay.","evidence_source":"가격 row 및 이벤트 프리미엄 관찰; stock-web 047040 2021 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2021.csv","profile_path":"atlas/symbol_profiles/047/047040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-06-02","entry_price":8870,"MFE_30D_pct":7.6,"MFE_90D_pct":7.6,"MFE_180D_pct":7.6,"MFE_1Y_pct":7.6,"MFE_2Y_pct":7.6,"MAE_30D_pct":-12.2,"MAE_90D_pct":-22.1,"MAE_180D_pct":-22.1,"MAE_1Y_pct":-22.1,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-06-02","peak_price":9540,"drawdown_after_peak_pct":-27.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.89,"four_b_full_window_peak_proximity":0.89,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":"positioning_overheat|valuation_blowoff","four_c_protection_label":"not_applicable","trigger_outcome_label":"event_premium","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L2_C01_DAEWOO_2020_2021-06-02_8870","dedupe_for_aggregate":true,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R10L2_C02_SAMPYO_2021_T01","case_id":"R10L2_C02_SAMPYO_2021","symbol":"038500","company_name":"삼표시멘트","round":"R10","loop":"2","sector":"건설·부동산·건자재","primary_archetype":"CEMENT_PRICE_SPREAD_REPRICING","trigger_type":"Stage2","trigger_date":"2021-01-19","evidence_available_at_that_date":"시멘트 가격·원가 스프레드 및 인프라/건자재 수요 기대가 가격/거래대금에 반영되기 시작.","evidence_source":"뉴스/리포트/가격 row: stock-web 038500 2021 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/038/038500/2021.csv","profile_path":"atlas/symbol_profiles/038/038500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-01-19","entry_price":4280,"MFE_30D_pct":32.2,"MFE_90D_pct":43.2,"MFE_180D_pct":57.7,"MFE_1Y_pct":57.7,"MFE_2Y_pct":57.7,"MAE_30D_pct":-8.6,"MAE_90D_pct":-8.6,"MAE_180D_pct":-8.6,"MAE_1Y_pct":-8.6,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-06-22","peak_price":6750,"drawdown_after_peak_pct":-20.0,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"good_entry","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L2_C02_SAMPYO_2021_2021-01-19_4280","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R10L2_C02_SAMPYO_2021_T02","case_id":"R10L2_C02_SAMPYO_2021","symbol":"038500","company_name":"삼표시멘트","round":"R10","loop":"2","sector":"건설·부동산·건자재","primary_archetype":"CEMENT_PRICE_SPREAD_REPRICING","trigger_type":"Stage2-Actionable","trigger_date":"2021-02-03","evidence_available_at_that_date":"시멘트/건자재 repricing 내러티브에 거래대금과 두 번째 가격 레벨업이 붙은 구간.","evidence_source":"뉴스/리포트/가격 row: stock-web 038500 2021 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/038/038500/2021.csv","profile_path":"atlas/symbol_profiles/038/038500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-02-03","entry_price":4905,"MFE_30D_pct":15.4,"MFE_90D_pct":25.0,"MFE_180D_pct":37.6,"MFE_1Y_pct":37.6,"MFE_2Y_pct":37.6,"MAE_30D_pct":-7.4,"MAE_90D_pct":-7.4,"MAE_180D_pct":-7.4,"MAE_1Y_pct":-7.4,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-06-22","peak_price":6750,"drawdown_after_peak_pct":-20.0,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"0.05","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"good_entry","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L2_C02_SAMPYO_2021_2021-02-03_4905","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R10L2_C02_SAMPYO_2021_T03","case_id":"R10L2_C02_SAMPYO_2021","symbol":"038500","company_name":"삼표시멘트","round":"R10","loop":"2","sector":"건설·부동산·건자재","primary_archetype":"CEMENT_PRICE_SPREAD_REPRICING","trigger_type":"Stage3-Yellow","trigger_date":"2021-03-24","evidence_available_at_that_date":"가격 인상/스프레드 bridge가 더 명확해졌지만 full Green confirmation에는 업황 지속성 검증이 남음.","evidence_source":"뉴스/리포트/가격 row: stock-web 038500 2021 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/038/038500/2021.csv","profile_path":"atlas/symbol_profiles/038/038500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-03-24","entry_price":5130,"MFE_30D_pct":19.5,"MFE_90D_pct":31.6,"MFE_180D_pct":31.6,"MFE_1Y_pct":31.6,"MFE_2Y_pct":31.6,"MAE_30D_pct":-3.0,"MAE_90D_pct":-3.0,"MAE_180D_pct":-3.0,"MAE_1Y_pct":-3.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-06-22","peak_price":6750,"drawdown_after_peak_pct":-20.0,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"0.05","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L2_C02_SAMPYO_2021_2021-03-24_5130","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R10L2_C02_SAMPYO_2021_T04","case_id":"R10L2_C02_SAMPYO_2021","symbol":"038500","company_name":"삼표시멘트","round":"R10","loop":"2","sector":"건설·부동산·건자재","primary_archetype":"CEMENT_PRICE_SPREAD_REPRICING","trigger_type":"Stage4B","trigger_date":"2021-06-22","evidence_available_at_that_date":"단기 수급 과열/테마성 가격 blowoff. 비가격 4B evidence는 약해 full 4B보다는 watch.","evidence_source":"가격 row: stock-web 038500 2021 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/038/038500/2021.csv","profile_path":"atlas/symbol_profiles/038/038500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-06-22","entry_price":6340,"MFE_30D_pct":6.5,"MFE_90D_pct":6.5,"MFE_180D_pct":6.5,"MFE_1Y_pct":6.5,"MFE_2Y_pct":6.5,"MAE_30D_pct":-14.8,"MAE_90D_pct":-14.8,"MAE_180D_pct":-14.8,"MAE_1Y_pct":-14.8,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-06-22","peak_price":6750,"drawdown_after_peak_pct":-20.0,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.78,"four_b_full_window_peak_proximity":0.78,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_exit","four_b_evidence_type":"price_only|positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"event_premium","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L2_C02_SAMPYO_2021_2021-06-22_6340","dedupe_for_aggregate":true,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R10L2_C03_HDC_2022_T01","case_id":"R10L2_C03_HDC_2022","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"2","sector":"건설·부동산·건자재","primary_archetype":"CONSTRUCTION_SAFETY_THESIS_BREAK","trigger_type":"Stage4C","trigger_date":"2022-01-11","evidence_available_at_that_date":"광주 화정아이파크 외벽 붕괴 사고. 2022-01-11 15:46 KST 발생으로 장마감 후 성격이 강해 다음 거래일 종가 entry.","evidence_source":"공개 사고 보도/정부 조사; 가격 row: stock-web 294870 2022 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-01-12","entry_price":20850,"MFE_30D_pct":8.9,"MFE_90D_pct":8.9,"MFE_180D_pct":8.9,"MFE_1Y_pct":8.9,"MFE_2Y_pct":15.3,"MAE_30D_pct":-35.3,"MAE_90D_pct":-36.9,"MAE_180D_pct":-52.2,"MAE_1Y_pct":-52.2,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-01-12","peak_price":22700,"drawdown_after_peak_pct":-56.1,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4c_success","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L2_C03_HDC_2022_2022-01-12_20850","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R10L2_C03_HDC_2022_T02","case_id":"R10L2_C03_HDC_2022","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"2","sector":"건설·부동산·건자재","primary_archetype":"CONSTRUCTION_SAFETY_THESIS_BREAK","trigger_type":"Stage4C","trigger_date":"2022-03-14","evidence_available_at_that_date":"정부 조사 결과/부실시공 원인 확인. 사고 당일 대비 늦은 hard confirmation.","evidence_source":"정부 조사/보도; 가격 row: stock-web 294870 2022 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-03-15","entry_price":16200,"MFE_30D_pct":8.3,"MFE_90D_pct":8.3,"MFE_180D_pct":8.3,"MFE_1Y_pct":8.3,"MFE_2Y_pct":48.5,"MAE_30D_pct":-32.4,"MAE_90D_pct":-32.4,"MAE_180D_pct":-39.6,"MAE_1Y_pct":-39.6,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-03-30","peak_price":17550,"drawdown_after_peak_pct":-44.2,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"hard_4c_late","trigger_outcome_label":"hard_4c_late","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L2_C03_HDC_2022_2022-03-15_16200","dedupe_for_aggregate":true,"aggregate_group_role":"4C_overlay_only"}
{"row_type":"trigger","trigger_id":"R10L2_C04_GSENC_2023_T01","case_id":"R10L2_C04_GSENC_2023","symbol":"006360","company_name":"GS건설","round":"R10","loop":"2","sector":"건설·부동산·건자재","primary_archetype":"CONSTRUCTION_QUALITY_REBUILD_THESIS_BREAK","trigger_type":"Stage3-Green","trigger_date":"2023-04-28","evidence_available_at_that_date":"사고 전까지는 안정적 주택/건축 실적과 업황 회복 기대가 남아 있던 구간. 이후 품질 리스크로 false positive화.","evidence_source":"실적/리포트/가격 row: stock-web 006360 2023 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-04-28","entry_price":21600,"MFE_30D_pct":2.5,"MFE_90D_pct":2.5,"MFE_180D_pct":2.5,"MFE_1Y_pct":2.5,"MFE_2Y_pct":6.2,"MAE_30D_pct":-8.2,"MAE_90D_pct":-38.1,"MAE_180D_pct":-41.3,"MAE_1Y_pct":-41.3,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-24","peak_price":22150,"drawdown_after_peak_pct":-42.8,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"false_positive_score","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L2_C04_GSENC_2023_2023-04-28_21600","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R10L2_C04_GSENC_2023_T02","case_id":"R10L2_C04_GSENC_2023","symbol":"006360","company_name":"GS건설","round":"R10","loop":"2","sector":"건설·부동산·건자재","primary_archetype":"CONSTRUCTION_QUALITY_REBUILD_THESIS_BREAK","trigger_type":"Stage4C","trigger_date":"2023-05-02","evidence_available_at_that_date":"인천 검단 현장 붕괴/품질 리스크가 공개적으로 반영되기 시작한 초기 4C-watch.","evidence_source":"공개 보도/가격 row: stock-web 006360 2023 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-02","entry_price":20500,"MFE_30D_pct":8.0,"MFE_90D_pct":8.0,"MFE_180D_pct":8.0,"MFE_1Y_pct":12.0,"MFE_2Y_pct":12.0,"MAE_30D_pct":-3.3,"MAE_90D_pct":-34.8,"MAE_180D_pct":-38.2,"MAE_1Y_pct":-38.2,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-24","peak_price":22150,"drawdown_after_peak_pct":-42.8,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4c_success","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L2_C04_GSENC_2023_2023-05-02_20500","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R10L2_C04_GSENC_2023_T03","case_id":"R10L2_C04_GSENC_2023","symbol":"006360","company_name":"GS건설","round":"R10","loop":"2","sector":"건설·부동산·건자재","primary_archetype":"CONSTRUCTION_QUALITY_REBUILD_THESIS_BREAK","trigger_type":"Stage4C","trigger_date":"2023-07-05","evidence_available_at_that_date":"전면 재시공/대규모 비용 인식이 확인된 hard 4C. 최초 사고 공개 대비 가격 보호는 늦음.","evidence_source":"공개 보도/공시/가격 row: stock-web 006360 2023 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-06","entry_price":14520,"MFE_30D_pct":3.9,"MFE_90D_pct":3.9,"MFE_180D_pct":3.9,"MFE_1Y_pct":58.1,"MFE_2Y_pct":58.1,"MAE_30D_pct":-7.4,"MAE_90D_pct":-12.7,"MAE_180D_pct":-12.7,"MAE_1Y_pct":-12.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-17","peak_price":15080,"drawdown_after_peak_pct":-16.0,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"hard_4c_late","trigger_outcome_label":"hard_4c_late","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L2_C04_GSENC_2023_2023-07-06_14520","dedupe_for_aggregate":true,"aggregate_group_role":"4C_overlay_only"}
```

### 27.4 Score simulation rows JSONL

```jsonl
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_to_selected_shadow","case_id":"R10L2_C01_DAEWOO_2020","trigger_id":"R10L2_C01_DAEWOO_2020_T01","symbol":"047040","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":0,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":100,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":0,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":100,"stage_label_after":"Stage3-Green","changed_components":["backlog_visibility_score","margin_bridge_score","relative_strength_score"],"component_delta_explanation":"shadow profile raises early backlog/margin/RS for construction-cycle entries and tightens safety/legal/accounting risk for construction-quality failures","selected_by_profile":false,"MFE_90D_pct":123.3,"MAE_90D_pct":-1.0,"score_return_alignment_label":"score_mid_return_high_promote_candidate","row_validation_status":"valid_component_breakdown"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_to_selected_shadow","case_id":"R10L2_C01_DAEWOO_2020","trigger_id":"R10L2_C01_DAEWOO_2020_T02","symbol":"047040","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":100,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":100,"stage_label_after":"Stage3-Green","changed_components":["backlog_visibility_score","margin_bridge_score","relative_strength_score"],"component_delta_explanation":"shadow profile raises early backlog/margin/RS for construction-cycle entries and tightens safety/legal/accounting risk for construction-quality failures","selected_by_profile":true,"MFE_90D_pct":90.3,"MAE_90D_pct":-4.5,"score_return_alignment_label":"score_mid_return_high_promote_candidate","row_validation_status":"valid_component_breakdown"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_to_selected_shadow","case_id":"R10L2_C01_DAEWOO_2020","trigger_id":"R10L2_C01_DAEWOO_2020_T03","symbol":"047040","trigger_type":"Stage3-Yellow","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":100,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":100,"stage_label_after":"Stage3-Green","changed_components":["backlog_visibility_score","margin_bridge_score","relative_strength_score"],"component_delta_explanation":"shadow profile raises early backlog/margin/RS for construction-cycle entries and tightens safety/legal/accounting risk for construction-quality failures","selected_by_profile":false,"MFE_90D_pct":50.9,"MAE_90D_pct":-16.8,"score_return_alignment_label":"score_mid_return_high_promote_candidate","row_validation_status":"valid_component_breakdown"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_to_selected_shadow","case_id":"R10L2_C01_DAEWOO_2020","trigger_id":"R10L2_C01_DAEWOO_2020_T04","symbol":"047040","trigger_type":"Stage3-Green","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":4,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":100,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":4,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":100,"stage_label_after":"Stage3-Green","changed_components":[],"component_delta_explanation":"shadow profile raises early backlog/margin/RS for construction-cycle entries and tightens safety/legal/accounting risk for construction-quality failures","selected_by_profile":false,"MFE_90D_pct":24.1,"MAE_90D_pct":-10.3,"score_return_alignment_label":"score_mid_return_high_promote_candidate","row_validation_status":"valid_component_breakdown"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_to_selected_shadow","case_id":"R10L2_C01_DAEWOO_2020","trigger_id":"R10L2_C01_DAEWOO_2020_T05","symbol":"047040","trigger_type":"Stage4B","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":100,"stage_label_before":"Stage4B-watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":100,"stage_label_after":"Stage4B-watch","changed_components":[],"component_delta_explanation":"shadow profile raises early backlog/margin/RS for construction-cycle entries and tightens safety/legal/accounting risk for construction-quality failures","selected_by_profile":false,"MFE_90D_pct":7.6,"MAE_90D_pct":-22.1,"score_return_alignment_label":"score_high_return_low_false_positive","row_validation_status":"valid_component_breakdown"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_to_selected_shadow","case_id":"R10L2_C02_SAMPYO_2021","trigger_id":"R10L2_C02_SAMPYO_2021_T01","symbol":"038500","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":3,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":97,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":3,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":100,"stage_label_after":"Stage3-Green","changed_components":["backlog_visibility_score","margin_bridge_score","relative_strength_score"],"component_delta_explanation":"shadow profile raises early backlog/margin/RS for construction-cycle entries and tightens safety/legal/accounting risk for construction-quality failures","selected_by_profile":false,"MFE_90D_pct":43.2,"MAE_90D_pct":-8.6,"score_return_alignment_label":"score_mid_return_high_promote_candidate","row_validation_status":"valid_component_breakdown"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_to_selected_shadow","case_id":"R10L2_C02_SAMPYO_2021","trigger_id":"R10L2_C02_SAMPYO_2021_T02","symbol":"038500","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":2,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":100,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":2,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":100,"stage_label_after":"Stage3-Green","changed_components":["backlog_visibility_score","margin_bridge_score","relative_strength_score"],"component_delta_explanation":"shadow profile raises early backlog/margin/RS for construction-cycle entries and tightens safety/legal/accounting risk for construction-quality failures","selected_by_profile":false,"MFE_90D_pct":25.0,"MAE_90D_pct":-7.4,"score_return_alignment_label":"score_mid_return_high_promote_candidate","row_validation_status":"valid_component_breakdown"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_to_selected_shadow","case_id":"R10L2_C02_SAMPYO_2021","trigger_id":"R10L2_C02_SAMPYO_2021_T03","symbol":"038500","trigger_type":"Stage3-Yellow","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":2,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":100,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":2,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":100,"stage_label_after":"Stage3-Green","changed_components":["backlog_visibility_score","margin_bridge_score","relative_strength_score"],"component_delta_explanation":"shadow profile raises early backlog/margin/RS for construction-cycle entries and tightens safety/legal/accounting risk for construction-quality failures","selected_by_profile":true,"MFE_90D_pct":31.6,"MAE_90D_pct":-3.0,"score_return_alignment_label":"score_mid_return_high_promote_candidate","row_validation_status":"valid_component_breakdown"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_to_selected_shadow","case_id":"R10L2_C02_SAMPYO_2021","trigger_id":"R10L2_C02_SAMPYO_2021_T04","symbol":"038500","trigger_type":"Stage4B","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":100,"stage_label_before":"Stage4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":100,"stage_label_after":"Stage4B-watch","changed_components":[],"component_delta_explanation":"shadow profile raises early backlog/margin/RS for construction-cycle entries and tightens safety/legal/accounting risk for construction-quality failures","selected_by_profile":false,"MFE_90D_pct":6.5,"MAE_90D_pct":-14.8,"score_return_alignment_label":"score_mid_return_high_promote_candidate","row_validation_status":"valid_component_breakdown"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_to_selected_shadow","case_id":"R10L2_C03_HDC_2022","trigger_id":"R10L2_C03_HDC_2022_T01","symbol":"294870","trigger_type":"Stage4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":1,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":0,"stage_label_after":"Stage4C","changed_components":["execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"shadow profile raises early backlog/margin/RS for construction-cycle entries and tightens safety/legal/accounting risk for construction-quality failures","selected_by_profile":true,"MFE_90D_pct":8.9,"MAE_90D_pct":-36.9,"score_return_alignment_label":"risk_high_drawdown_high_correct_protect","row_validation_status":"valid_component_breakdown"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_to_selected_shadow","case_id":"R10L2_C03_HDC_2022","trigger_id":"R10L2_C03_HDC_2022_T02","symbol":"294870","trigger_type":"Stage4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":4,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":5,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":4,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":0,"stage_label_after":"Stage4C","changed_components":["execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"shadow profile raises early backlog/margin/RS for construction-cycle entries and tightens safety/legal/accounting risk for construction-quality failures","selected_by_profile":false,"MFE_90D_pct":8.3,"MAE_90D_pct":-32.4,"score_return_alignment_label":"risk_high_drawdown_high_correct_protect","row_validation_status":"valid_component_breakdown"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_to_selected_shadow","case_id":"R10L2_C04_GSENC_2023","trigger_id":"R10L2_C04_GSENC_2023_T01","symbol":"006360","trigger_type":"Stage3-Green","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":97,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":100,"stage_label_after":"Stage3-Green","changed_components":["execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"shadow profile raises early backlog/margin/RS for construction-cycle entries and tightens safety/legal/accounting risk for construction-quality failures","selected_by_profile":false,"MFE_90D_pct":2.5,"MAE_90D_pct":-38.1,"score_return_alignment_label":"score_high_return_low_false_positive","row_validation_status":"valid_component_breakdown"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_to_selected_shadow","case_id":"R10L2_C04_GSENC_2023","trigger_id":"R10L2_C04_GSENC_2023_T02","symbol":"006360","trigger_type":"Stage4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":5,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":0,"stage_label_after":"Stage4C","changed_components":["execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"shadow profile raises early backlog/margin/RS for construction-cycle entries and tightens safety/legal/accounting risk for construction-quality failures","selected_by_profile":true,"MFE_90D_pct":8.0,"MAE_90D_pct":-34.8,"score_return_alignment_label":"risk_high_drawdown_high_correct_protect","row_validation_status":"valid_component_breakdown"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy_to_selected_shadow","case_id":"R10L2_C04_GSENC_2023","trigger_id":"R10L2_C04_GSENC_2023_T03","symbol":"006360","trigger_type":"Stage4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":5,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":0,"stage_label_after":"Stage4C","changed_components":["execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"shadow profile raises early backlog/margin/RS for construction-cycle entries and tightens safety/legal/accounting risk for construction-quality failures","selected_by_profile":false,"MFE_90D_pct":3.9,"MAE_90D_pct":-12.7,"score_return_alignment_label":"risk_high_drawdown_high_correct_protect","row_validation_status":"valid_component_breakdown"}
```

### 27.5 Profile comparison rows CSV

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,4,4,4,16.5,12.0,-20.7,-21.2,16.5,-22.6,0.5,0.5,0.25,1,1,0.68,not_applicable,not_applicable,reference; late Green and pre-4C false positive remain visible
profile_comparison,stage2_actionable_early_evidence_plus,4,4,4,36.2,24.3,-19.8,-18.9,58.0,-25.0,0.5,0.5,0.0,0,0,0.4,not_applicable,not_applicable,best blended profile; early cyclic entries + hard 4C protection
profile_comparison,stage3_yellow_entry_relaxed,4,3,3,28.0,31.6,-20.3,-9.9,34.7,-23.3,0.67,0.33,0.0,1,0,0.4,not_applicable,not_applicable,"useful, but misses Daewoo's very early Stage2-Actionable"
profile_comparison,green_confirmation_timing_relaxed,4,4,4,22.4,16.5,-19.2,-16.0,23.5,-22.0,0.5,0.5,0.25,1,1,0.68,not_applicable,not_applicable,too broad; GS false positive remains
profile_comparison,four_b_peak_timing_tuned,2,2,0,overlay_only,overlay_only,overlay_only,overlay_only,overlay_only,overlay_only,overlay_only,overlay_only,0.0,0,0,not_applicable,0.82,0.82,"Daewoo good full-window 4B; Sampyo price-only 4B should stay watch, not full exit"
profile_comparison,four_c_thesis_break_earlier,2,2,2,8.4,8.4,-35.8,-35.8,8.4,-45.2,0.0,1.0,0.0,0,0,not_applicable,not_applicable,not_applicable,"for protection, not entry; hard safety/legal risk should override long entry"
```

### 27.6 Shadow weight CSV

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_backlog_margin_rs_combo,0,2,+2,Daewoo Stage2-Actionable produced MFE90 90.3 and MFE180 165.4 with MAE90 -4.5 before Green.,baseline selected Green MFE90 24.1/MAE90 -10.4; after selected Stage2-Actionable MFE90 90.3/MAE90 -4.5.,R10L2_C01_DAEWOO_2020_T02,1,exploratory-to-moderate; needs additional housing-cycle counterexamples before production
shadow_weight,stage3_yellow_spread_margin_bridge,0,1,+1,"Sampyo Stage3-Yellow gave the best risk-adjusted cement-cycle entry: MFE90 31.6, MAE90 -2.9.",keeps Yellow tier for price/spread bridge cases instead of forcing delayed Green.,R10L2_C02_SAMPYO_2021_T03,1,exploratory; not enough cases for stronger delta
shadow_weight,construction_quality_execution_legal_4c_override,0,3,+3,HDC and GS safety/quality thesis-break rows produced deep MAE90/180; hard risk should override positive construction-cycle scores.,GS baseline Stage3-Green proxy had MFE90 2.5 and MAE90 -38.1; 4C-watch avoids treating this as a long entry. HDC early 4C captured -36.9 MAE90 risk.,R10L2_C03_HDC_2022_T01|R10L2_C04_GSENC_2023_T02,2,moderate/strong for shadow because two different large builders show same risk shape
shadow_weight,price_only_4b_reject_as_full_exit,1,0,-1,Sampyo 4B was near local peak but only price/positioning evidence; Daewoo 4B had clearer event/valuation overheat.,separating local price-only 4B from full 4B avoids prematurely killing cyclic winners without non-price risk.,R10L2_C01_DAEWOO_2020_T05|R10L2_C02_SAMPYO_2021_T04,2,exploratory; preserve as watch overlay
```

### 27.7 Optimization decision rows JSONL

```jsonl
{"row_type":"optimization_decision","decision_id":"R10L2_DECISION_01","hypothesis":"Backlog/margin bridge plus relative strength should promote some construction-cycle Stage2 rows to Stage2-Actionable.","tested_cases":["R10L2_C01_DAEWOO_2020","R10L2_C02_SAMPYO_2021"],"tested_trigger_ids":["R10L2_C01_DAEWOO_2020_T02","R10L2_C02_SAMPYO_2021_T02","R10L2_C02_SAMPYO_2021_T03"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus","backtest_result_summary":"Daewoo T02 greatly outperformed Green; Sampyo Yellow had better risk-adjusted profile than forcing Green.","accepted_or_rejected":"accepted_shadow_only","reason":"missed_structural risk falls without adding observed false positive in this small R10 set.","proposed_shadow_rule":"promote Stage2 to Stage2-Actionable when backlog/margin bridge + RS close together.","delta_magnitude":"+2 for Daewoo-type axis, +1 for spread-margin Yellow","why_not_larger_delta":"R10 sample is four cases and only two cyclical success cases.","risks":"construction cycles are macro-sensitive; raw/unadjusted price basis can overstate if corporate actions occur outside observed windows.","next_validation_needed":"Find 2020-2022 failed housing backlog cases and 2021-2022 cement false positives."}
{"row_type":"optimization_decision","decision_id":"R10L2_DECISION_02","hypothesis":"Construction quality/safety thesis breaks need hard 4C override before earnings confirmation catches up.","tested_cases":["R10L2_C03_HDC_2022","R10L2_C04_GSENC_2023"],"tested_trigger_ids":["R10L2_C03_HDC_2022_T01","R10L2_C04_GSENC_2023_T02"],"baseline_profile":"baseline_current_proxy","selected_profile":"four_c_thesis_break_earlier","backtest_result_summary":"HDC early 4C was followed by MAE90 -36.9 and MAE180 -52.2; GS early 4C-watch was followed by MAE90 -34.8.","accepted_or_rejected":"accepted_shadow_only","reason":"same pattern repeats across two large builders: safety/legal quality risk precedes or overwhelms financial confirmation.","proposed_shadow_rule":"execution/legal/accounting trust risk >= threshold blocks Green and promotes 4C-watch/hard 4C.","delta_magnitude":"+3 risk override","why_not_larger_delta":"GS non-price source URL should be revalidated before production; HDC source was easier to verify.","risks":"not every accident is thesis-breaking; require named site, material cost/liability, administrative/legal risk, or rebuild/order risk.","next_validation_needed":"Add non-fatal but recoverable accident cases to reduce false 4C breaks."}
```

### 27.8 Narrative-only rows JSONL

```jsonl
{"row_type":"narrative_only","case_id":"R10L2_EVIDENCE_SOURCE_NOTE","symbol":"006360","reason":"GS E&C Geomdan non-price URL needs DART/KRX/news revalidation before production scoring; OHLC row remains included for shadow 4C protection only","price_source":"Songdaiki/stock-web","usage":"not_production_weight_calibration_without_source_revalidation"}
```

### 27.9 Aggregate metric rows CSV

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,below_entry_90D_rate,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,2,2,83.2,83.2,-4.8,-4.8,137.8,-4.8,1.0,not_applicable,not_applicable,not_applicable,representative rows only; 4B/4C overlay rows separated
aggregate_metric,Stage2-Actionable,2,2,57.6,57.6,-6.0,-6.0,101.5,-6.0,1.0,0.4,not_applicable,not_applicable,representative rows only; 4B/4C overlay rows separated
aggregate_metric,Stage3-Yellow,2,2,41.2,41.2,-9.9,-9.9,41.2,-9.9,1.0,0.4,not_applicable,not_applicable,representative rows only; 4B/4C overlay rows separated
aggregate_metric,Stage3-Green,2,2,13.3,13.3,-24.2,-24.2,13.3,-25.8,1.0,0.7,not_applicable,not_applicable,representative rows only; 4B/4C overlay rows separated
aggregate_metric,Stage4B,2,0,not_applicable,not_applicable,not_applicable,not_applicable,not_applicable,not_applicable,overlay_only,not_applicable,0.8,0.8,overlay only
aggregate_metric,Stage4C,4,2,8.4,8.4,-35.8,-35.8,8.4,-45.2,1.0,not_applicable,not_applicable,not_applicable,representative rows only; 4B/4C overlay rows separated
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
- Revalidate GS E&C Geomdan non-price source against DART/KRX/news before any production 4C change.

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
current_round_completed = R10 Loop 2
next_round = R11 Loop 2
next_sector = 정책·지정학·재난·이벤트
carry_forward_focus = policy/event-driven thesis breaks, disaster/event 4C, and non-price 4B guardrails
```

## 30. Source Notes

This file is shadow-only historical calibration research. It is not investment advice, not live candidate discovery, and not a `stock_agent` implementation patch.

The strongest fully supported price conclusions are based on stock-web OHLC rows. Non-price evidence for GS E&C should be revalidated before production use. HDC event dating was externally cross-checked, but all weight changes remain shadow-only.
