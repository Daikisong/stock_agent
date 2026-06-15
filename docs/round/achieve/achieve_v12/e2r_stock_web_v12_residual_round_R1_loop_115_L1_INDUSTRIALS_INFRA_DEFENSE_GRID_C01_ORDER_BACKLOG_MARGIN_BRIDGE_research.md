# E2R Stock-Web V12 Residual Research — R1 Loop 115 / C01_ORDER_BACKLOG_MARGIN_BRIDGE

```yaml
output_file: e2r_stock_web_v12_residual_round_R1_loop_115_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
selected_round: R1
selected_loop: 115
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: mixed_C01_shipbuilding_engine_supplier_backlog_margin_bridge_set
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection Rationale / No-Repeat Check

`V12_Research_No_Repeat_Index.md`의 Priority 0 표에서 C01_ORDER_BACKLOG_MARGIN_BRIDGE는 19 rows / need-to-30 11로 남아 있었다. 직전 GitHub `docs/round` 표준 C01 파일은 `R1_loop_114`였으므로 이번 산출물은 selected_loop=115로 둔다. 이번 case set은 기존 top covered symbols인 `012450`, `064350`, `079550`, `000720`, `004960`, `006360`과 직전 C01 shipbuilding/power-equipment 표본군을 피했다.

Novelty guard:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
reused_case_count = 0
same_archetype_new_symbol_count = 6
same_archetype_new_trigger_family_count = 6
calibration_usable_cases = 6
positive_case_count = 4
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
current_profile_error_count = 3
```

## 2. Price Atlas / Validation Scope

Stock-Web manifest 기준으로 가격 데이터는 FinanceData/marcap 기반 `tradable_raw`, `raw_unadjusted_marcap`이며, `max_date=2026-02-20`이다. MFE/MAE는 schema 정의대로 entry_date close를 entry_price로 두고, entry_date부터 30/90/180개 tradable rows의 high/low 경로로 계산했다.

```yaml
source_name: Songdaiki/stock-web
source_repo_url: https://github.com/Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
schema_path: atlas/schema.json
trigger_rows: 6
calibration_usable_rows: 6
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
```

## 3. Case Table

| role | symbol | name | trigger | entry | entry_price | 90D MFE/MAE | 180D MFE/MAE | evidence family | proposed interpretation |
|---|---:|---|---|---|---:|---:|---:|---|---|
| positive | 329180 | HD현대중공업 | Stage3-Yellow | 2025-02-17 | 326,500 | 45.79% / -16.85% | 96.02% / -16.85% | SHIPBUILDER_COMMERCIAL_ORDER_ENGINE_MARGIN_BRIDGE | Stage3-Yellow |
| positive_with_high_MAE_guard | 010620 | HD현대미포 | Stage3-Yellow | 2025-01-17 | 128,300 | 59.78% / -22.45% | 72.64% / -22.45% | MID_SHIPBUILDER_PROFIT_SWING_ORDER_TARGET_BRIDGE | Stage3-Yellow_with_high_MAE_entry_guard |
| positive | 082740 | 한화엔진 | Stage3-Yellow | 2024-08-21 | 14,170 | 35.29% / -18.77% | 123.36% / -18.77% | ENGINE_SUPPLIER_BACKLOG_REVENUE_RECOGNITION_MARGIN_BRIDGE | Stage3-Yellow |
| positive | 075580 | 세진중공업 | Stage2-Actionable | 2024-04-02 | 6,850 | 59.42% / -7.74% | 59.42% / -7.74% | SHIP_COMPONENT_TANK_DECKHOUSE_CUSTOMER_BACKLOG_MARGIN_BRIDGE | Stage2-Actionable_to_Stage3-Yellow_when_delivery_confirms |
| counterexample_stage_timing_high_MAE | 071970 | HD현대마린엔진 | Stage2-Actionable | 2024-07-31 | 23,050 | 7.81% / -32.06% | 67.68% / -32.06% | ENGINE_PLATFORM_REORG_EVENT_WITH_DELAYED_REVENUE_BRIDGE | Stage2-Actionable_not_Stage3_until_revenue_bridge |
| counterexample_revenue_recognition_delay_high_MAE | 100090 | SK오션플랜트 | Stage4B | 2024-08-22 | 14,270 | 13.52% / -22.14% | 55.22% / -22.14% | OFFSHORE_WIND_BACKLOG_REVENUE_RECOGNITION_DELAY_4B_CAP | Stage4B_watch_until_revenue_recognition_recovers |

Aggregate path:

```yaml
avg_MFE_90D_pct: 36.94
avg_MAE_90D_pct: -20.0
avg_MFE_180D_pct: 79.06
avg_MAE_180D_pct: -20.0
MFE_90D_ge_20pct_count: 4
MAE_90D_le_minus_20pct_count: 3
```

## 4. Case Notes

### 1. 329180 HD현대중공업 — positive

- **Trigger / entry:** Stage3-Yellow / 2025-02-17 close 326,500
- **Evidence:** 1월 LNG 이중연료 컨테이너선 12척, US$2.58bn 계약으로 2025년 상선 수주목표 41%를 이미 달성했고, 엔진/기계 부문은 대형엔진 mix 개선으로 저/중 teens OPM 유지가 가능하다는 증거가 같은 리포트에 함께 제시됐다.
- **Source:** https://securities.miraeasset.com/bbs/download/2134494.pdf?attachmentId=2134494
- **180D path:** peak 2025-10-27 640,000, trough 2025-03-31 271,500, post-peak drawdown -22.42%
- **Residual contribution:** C01에서는 backlog 그 자체보다 backlog→마진 mix→엔진 수익성 bridge가 동시 확인될 때 Yellow 이상으로 볼 수 있다.

### 2. 010620 HD현대미포 — positive_with_high_MAE_guard

- **Trigger / entry:** Stage3-Yellow / 2025-01-17 close 128,300
- **Evidence:** 4Q24 영업이익은 컨센서스 18.9% 상회 전망, 흑자전환, 2025년 revenue guidance 달성 가능성, order target 초과 가능성, 2025/2026 OPM 6.2%/9.7% forecast가 한 묶음으로 제시됐다.
- **Source:** https://securities.miraeasset.com/bbs/download/2133913.pdf?attachmentId=2133913
- **180D path:** peak 2025-07-31 221,500, trough 2025-03-28 99,500, post-peak drawdown -20.77%
- **Residual contribution:** Yellow 방향은 맞지만 90D MAE -22.45%라 Green 즉시승격보다는 drawdown-tolerant staged entry guard가 필요하다.

### 3. 082740 한화엔진 — positive

- **Trigger / entry:** Stage3-Yellow / 2024-08-21 close 14,170
- **Evidence:** 2Q24 매출 +52% YoY, 영업이익 +436% YoY, 컨센서스 상회, 2022년부터 증가한 수주잔고의 매출 인식 시작과 2021년 이전 저가수주 소진이 동시에 확인됐다.
- **Source:** https://www.asiae.co.kr/en/article/2024082109271255004
- **180D path:** peak 2025-05-09 31,650, trough 2024-09-06 11,510, post-peak drawdown -12.64%
- **Residual contribution:** 엔진 기자재에서는 수주잔고 증가만이 아니라 저가수주 소진과 매출 인식 시작이 같이 나올 때 C01 positive로 압축된다.

### 4. 075580 세진중공업 — positive

- **Trigger / entry:** Stage2-Actionable / 2024-04-02 close 6,850
- **Evidence:** HD현대중공업/현대미포 Deck House와 LPG Tank 외주물량 독점공급, HD한국조선해양 수주잔고의 15년 만의 역대 최대치, 2024년 두 자릿수 OPM 회복과 2025년 고성장 전망이 제시됐다.
- **Source:** https://ssl.pstatic.net/imgstock/upload/research/company/1712013384054.pdf
- **180D path:** peak 2024-07-17 10,920, trough 2024-05-23 6,320, post-peak drawdown -34.52%
- **Residual contribution:** 부품/기자재 하위 archetype은 고객사 수주잔고와 독점공급 구조가 있어도, delivery cadence가 확인되기 전에는 Stage2-Actionable로 시작하는 쪽이 보수적이다.

### 5. 071970 HD현대마린엔진 — counterexample_stage_timing_high_MAE

- **Trigger / entry:** Stage2-Actionable / 2024-07-31 close 23,050
- **Evidence:** HD현대마린엔진 공식 출범, 생산 포트폴리오 강화, 부품 국산화/원가 경쟁력, HD현대중공업과의 시너지, 친환경 엔진 수요 대응은 확인됐지만, 출범 이벤트 당시에는 실제 revenue/margin bridge가 아직 미확정이었다.
- **Source:** https://www.hd.com/en/newsroom/media-hub/press/view?detailsKey=3176
- **180D path:** peak 2025-04-28 38,650, trough 2024-09-06 15,660, post-peak drawdown -6.47%
- **Residual contribution:** 이 케이스는 180D로 보면 상승했지만 30/90D MAE -32.06%였다. 출범/재편 이벤트만으로 C01 Green unlock을 하면 timing error가 커진다.

### 6. 100090 SK오션플랜트 — counterexample_revenue_recognition_delay_high_MAE

- **Trigger / entry:** Stage4B / 2024-08-22 close 14,270
- **Evidence:** 대만 Fengmiao 계약/해상풍력 수주잔고 급증은 있었지만 2Q24 매출액 -32.8% YoY, 영업이익 -50.2% YoY, 해상풍력 매출 비중 감소와 revenue recognition 지연이 동시에 확인되어 backlog headline만으로 positive 승격하기 어렵다.
- **Source:** https://www.hanaw.com/download/research/FileServer/WEB/industry/enterprise/2024/08/21/SKO_240822_Initiation.pdf
- **180D path:** peak 2025-05-19 22,150, trough 2024-12-02 11,110, post-peak drawdown -20.50%
- **Residual contribution:** 수주잔고가 급증해도 현재 매출인식/마진이 꺾이면 C01 positive가 아니라 4B watch 또는 Stage2 block으로 남겨야 한다.

## 5. Raw Component Score Breakdown

C01 runtime weight proxy used for stress simulation: EPS/Visibility/Bottleneck/Mispricing/Valuation/Capital/Info = `20/25/18/12/12/8/5`.

| symbol | EPS | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | weighted_total | proposed stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 329180 | 84 | 90 | 82 | 65 | 58 | 60 | 85 | 77.9 | Stage3-Yellow |
| 010620 | 82 | 88 | 75 | 65 | 60 | 50 | 82 | 75.0 | Stage3-Yellow_with_high_MAE_entry_guard |
| 082740 | 86 | 88 | 84 | 65 | 55 | 50 | 80 | 76.7 | Stage3-Yellow |
| 075580 | 78 | 82 | 84 | 68 | 76 | 60 | 74 | 77.0 | Stage2-Actionable_to_Stage3-Yellow_when_delivery_confirms |
| 071970 | 52 | 55 | 70 | 54 | 38 | 45 | 78 | 55.3 | Stage2-Actionable_not_Stage3_until_revenue_bridge |
| 100090 | 42 | 38 | 48 | 40 | 38 | 35 | 78 | 42.6 | Stage4B_watch_until_revenue_recognition_recovers |

Interpretation: C01의 weighted_total만으로는 충분하지 않다. HD현대마린엔진과 SK오션플랜트처럼 구조적 방향은 맞아도 revenue recognition/margin bridge가 늦는 사례는 180D MFE가 좋아도 30~90D MAE가 커진다. 따라서 C01은 `수주잔고 → 매출인식 → margin bridge → FCF/현금흐름`의 네 칸이 서로 이어져야 Stage3-Yellow 이상으로 승격하는 것이 안전하다.

## 6. Residual Rule Candidate

```yaml
sector_specific_rule_candidate: L1_C01_BACKLOG_MARGIN_FCF_BRIDGE_WITH_SUPPLIER_REVENUE_TIMING_GATE
canonical_archetype_rule_candidate: C01_ORDER_BACKLOG_REQUIRES_MARGIN_AND_REVENUE_RECOGNITION_BRIDGE
new_axis_proposed:
  - C01_BACKLOG_TO_REVENUE_RECOGNITION_GATE
  - C01_SUPPLIER_CUSTOMER_BACKLOG_DELIVERY_CADENCE_GATE
  - C01_REORG_SYNERGY_EVENT_STAGE2_CAP_UNTIL_MARGIN_BRIDGE
  - C01_REVENUE_DELAY_OR_LOW_MARGIN_4B_WATCH
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
do_not_propose_new_weight_delta: false
shadow_weight_only: true
```

### Proposed gating logic

```text
IF canonical_archetype_id == C01_ORDER_BACKLOG_MARGIN_BRIDGE:
  Stage3-Yellow requires at least two of:
    - named order/backlog increase with customer or project quality
    - revenue recognition has started or is explicitly dated
    - OP margin bridge is visible through mix, low-priced order depletion, pricing, or productivity
    - forward earnings visibility is supported by non-price evidence
  Stage3-Green requires all of:
    - backlog conversion is already visible in reported or near-confirmed earnings
    - margin bridge is not purely ASP/theme-driven
    - 30/90D MAE guard is not flashing high-MAE timing risk
  IF evidence is reorganization/synergy/capacity event only:
    cap at Stage2-Actionable until revenue/margin bridge appears
  IF backlog headline coexists with revenue recognition delay or margin decline:
    route to Stage4B watch or Stage2 block, not positive Stage3
```

## 7. Machine-Readable Rows — trigger

```jsonl
{"row_type":"trigger","case_id":"C01_R1L115_329180_20250217_hhi_commercial_ship_engine_margin","same_entry_group_id":"C01_R1L115_G01_329180_20250217","dedupe_role":"representative","representative_for_aggregate":true,"selected_round":"R1","selected_loop":115,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDER_COMMERCIAL_ORDER_ENGINE_MARGIN_BRIDGE","symbol":"329180","name":"HD현대중공업","trigger_type":"Stage3-Yellow","trigger_date":"2025-02-17","entry_date":"2025-02-17","entry_price":326500.0,"entry_timing_rule":"same_trading_day_close","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","profile_url":"https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/329/329180.json","price_csv_paths":["atlas/ohlcv_tradable_by_symbol_year/329/329180/2025.csv"],"source_url":"https://securities.miraeasset.com/bbs/download/2134494.pdf?attachmentId=2134494","MFE_30D_pct":8.58,"MAE_30D_pct":-16.85,"MFE_90D_pct":45.79,"MAE_90D_pct":-16.85,"MFE_180D_pct":96.02,"MAE_180D_pct":-16.85,"peak_180D_date":"2025-10-27","peak_180D_price":640000.0,"trough_180D_date":"2025-03-31","trough_180D_price":271500.0,"window_end_date":"2025-11-11","drawdown_after_peak_pct":-22.42,"corporate_action_candidate_dates":[],"corporate_action_contaminated":false,"calibration_usable":true,"outcome_role":"positive","current_profile_error":false,"proposed_stage":"Stage3-Yellow"}
{"row_type":"trigger","case_id":"C01_R1L115_010620_20250117_mipo_profit_swing_order_target","same_entry_group_id":"C01_R1L115_G02_010620_20250117","dedupe_role":"representative","representative_for_aggregate":true,"selected_round":"R1","selected_loop":115,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"MID_SHIPBUILDER_PROFIT_SWING_ORDER_TARGET_BRIDGE","symbol":"010620","name":"HD현대미포","trigger_type":"Stage3-Yellow","trigger_date":"2025-01-17","entry_date":"2025-01-17","entry_price":128300.0,"entry_timing_rule":"same_trading_day_close","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","profile_url":"https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/010/010620.json","price_csv_paths":["atlas/ohlcv_tradable_by_symbol_year/010/010620/2025.csv"],"source_url":"https://securities.miraeasset.com/bbs/download/2133913.pdf?attachmentId=2133913","MFE_30D_pct":12.47,"MAE_30D_pct":-18.86,"MFE_90D_pct":59.78,"MAE_90D_pct":-22.45,"MFE_180D_pct":72.64,"MAE_180D_pct":-22.45,"peak_180D_date":"2025-07-31","peak_180D_price":221500.0,"trough_180D_date":"2025-03-28","trough_180D_price":99500.0,"window_end_date":"2025-10-17","drawdown_after_peak_pct":-20.77,"corporate_action_candidate_dates":["1999-07-14","2004-01-29","2018-12-04","2018-12-26"],"corporate_action_contaminated":false,"calibration_usable":true,"outcome_role":"positive_with_high_MAE_guard","current_profile_error":true,"proposed_stage":"Stage3-Yellow_with_high_MAE_entry_guard"}
{"row_type":"trigger","case_id":"C01_R1L115_082740_20240821_hanwha_engine_backlog_revenue_recognition","same_entry_group_id":"C01_R1L115_G03_082740_20240821","dedupe_role":"representative","representative_for_aggregate":true,"selected_round":"R1","selected_loop":115,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"ENGINE_SUPPLIER_BACKLOG_REVENUE_RECOGNITION_MARGIN_BRIDGE","symbol":"082740","name":"한화엔진","trigger_type":"Stage3-Yellow","trigger_date":"2024-08-21","entry_date":"2024-08-21","entry_price":14170.0,"entry_timing_rule":"same_trading_day_close","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","profile_url":"https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/082/082740.json","price_csv_paths":["atlas/ohlcv_tradable_by_symbol_year/082/082740/2024.csv","atlas/ohlcv_tradable_by_symbol_year/082/082740/2025.csv"],"source_url":"https://www.asiae.co.kr/en/article/2024082109271255004","MFE_30D_pct":7.9,"MAE_30D_pct":-18.77,"MFE_90D_pct":35.29,"MAE_90D_pct":-18.77,"MFE_180D_pct":123.36,"MAE_180D_pct":-18.77,"peak_180D_date":"2025-05-09","peak_180D_price":31650.0,"trough_180D_date":"2024-09-06","trough_180D_price":11510.0,"window_end_date":"2025-05-22","drawdown_after_peak_pct":-12.64,"corporate_action_candidate_dates":["2018-06-19","2021-03-17","2022-08-25"],"corporate_action_contaminated":false,"calibration_usable":true,"outcome_role":"positive","current_profile_error":false,"proposed_stage":"Stage3-Yellow"}
{"row_type":"trigger","case_id":"C01_R1L115_075580_20240402_sejin_tank_deckhouse_customer_backlog","same_entry_group_id":"C01_R1L115_G04_075580_20240402","dedupe_role":"representative","representative_for_aggregate":true,"selected_round":"R1","selected_loop":115,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIP_COMPONENT_TANK_DECKHOUSE_CUSTOMER_BACKLOG_MARGIN_BRIDGE","symbol":"075580","name":"세진중공업","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-02","entry_date":"2024-04-02","entry_price":6850.0,"entry_timing_rule":"same_trading_day_close","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","profile_url":"https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/075/075580.json","price_csv_paths":["atlas/ohlcv_tradable_by_symbol_year/075/075580/2024.csv"],"source_url":"https://ssl.pstatic.net/imgstock/upload/research/company/1712013384054.pdf","MFE_30D_pct":10.66,"MAE_30D_pct":-5.55,"MFE_90D_pct":59.42,"MAE_90D_pct":-7.74,"MFE_180D_pct":59.42,"MAE_180D_pct":-7.74,"peak_180D_date":"2024-07-17","peak_180D_price":10920.0,"trough_180D_date":"2024-05-23","trough_180D_price":6320.0,"window_end_date":"2024-12-27","drawdown_after_peak_pct":-34.52,"corporate_action_candidate_dates":["2020-11-23"],"corporate_action_contaminated":false,"calibration_usable":true,"outcome_role":"positive","current_profile_error":false,"proposed_stage":"Stage2-Actionable_to_Stage3-Yellow_when_delivery_confirms"}
{"row_type":"trigger","case_id":"C01_R1L115_071970_20240731_hd_marine_engine_launch_stage_timing","same_entry_group_id":"C01_R1L115_G05_071970_20240731","dedupe_role":"representative","representative_for_aggregate":true,"selected_round":"R1","selected_loop":115,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"ENGINE_PLATFORM_REORG_EVENT_WITH_DELAYED_REVENUE_BRIDGE","symbol":"071970","name":"HD현대마린엔진","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-31","entry_date":"2024-07-31","entry_price":23050.0,"entry_timing_rule":"same_trading_day_close","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","profile_url":"https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/071/071970.json","price_csv_paths":["atlas/ohlcv_tradable_by_symbol_year/071/071970/2024.csv","atlas/ohlcv_tradable_by_symbol_year/071/071970/2025.csv"],"source_url":"https://www.hd.com/en/newsroom/media-hub/press/view?detailsKey=3176","MFE_30D_pct":7.81,"MAE_30D_pct":-32.06,"MFE_90D_pct":7.81,"MAE_90D_pct":-32.06,"MFE_180D_pct":67.68,"MAE_180D_pct":-32.06,"peak_180D_date":"2025-04-28","peak_180D_price":38650.0,"trough_180D_date":"2024-09-06","trough_180D_price":15660.0,"window_end_date":"2025-04-29","drawdown_after_peak_pct":-6.47,"corporate_action_candidate_dates":["2013-01-17","2013-12-18","2015-05-07","2017-05-25","2018-12-27"],"corporate_action_contaminated":false,"calibration_usable":true,"outcome_role":"counterexample_stage_timing_high_MAE","current_profile_error":true,"proposed_stage":"Stage2-Actionable_not_Stage3_until_revenue_bridge"}
{"row_type":"trigger","case_id":"C01_R1L115_100090_20240822_sk_oceanplant_backlog_revenue_delay","same_entry_group_id":"C01_R1L115_G06_100090_20240822","dedupe_role":"representative","representative_for_aggregate":true,"selected_round":"R1","selected_loop":115,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"OFFSHORE_WIND_BACKLOG_REVENUE_RECOGNITION_DELAY_4B_CAP","symbol":"100090","name":"SK오션플랜트","trigger_type":"Stage4B","trigger_date":"2024-08-22","entry_date":"2024-08-22","entry_price":14270.0,"entry_timing_rule":"same_trading_day_close","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","profile_url":"https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/100/100090.json","price_csv_paths":["atlas/ohlcv_tradable_by_symbol_year/100/100090/2024.csv","atlas/ohlcv_tradable_by_symbol_year/100/100090/2025.csv"],"source_url":"https://www.hanaw.com/download/research/FileServer/WEB/industry/enterprise/2024/08/21/SKO_240822_Initiation.pdf","MFE_30D_pct":13.52,"MAE_30D_pct":-6.45,"MFE_90D_pct":13.52,"MAE_90D_pct":-22.14,"MFE_180D_pct":55.22,"MAE_180D_pct":-22.14,"peak_180D_date":"2025-05-19","peak_180D_price":22150.0,"trough_180D_date":"2024-12-02","trough_180D_price":11110.0,"window_end_date":"2025-05-23","drawdown_after_peak_pct":-20.5,"corporate_action_candidate_dates":["2012-03-26","2012-04-24","2018-08-08","2022-09-16"],"corporate_action_contaminated":false,"calibration_usable":true,"outcome_role":"counterexample_revenue_recognition_delay_high_MAE","current_profile_error":true,"proposed_stage":"Stage4B_watch_until_revenue_recognition_recovers"}
```

## 8. Machine-Readable Rows — score_simulation

```jsonl
{"row_type":"score_simulation","case_id":"C01_R1L115_329180_20250217_hhi_commercial_ship_engine_margin","symbol":"329180","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","weights_EPS_Vis_Bott_Mis_Val_Cap_Info":"20/25/18/12/12/8/5","eps_fcf_explosion":84,"earnings_visibility":90,"bottleneck_pricing":82,"market_mispricing":65,"valuation_rerating":58,"capital_allocation":60,"information_confidence":85,"weighted_total":77.9,"trigger_type":"Stage3-Yellow","proposed_stage":"Stage3-Yellow","current_profile_error":false}
{"row_type":"score_simulation","case_id":"C01_R1L115_010620_20250117_mipo_profit_swing_order_target","symbol":"010620","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","weights_EPS_Vis_Bott_Mis_Val_Cap_Info":"20/25/18/12/12/8/5","eps_fcf_explosion":82,"earnings_visibility":88,"bottleneck_pricing":75,"market_mispricing":65,"valuation_rerating":60,"capital_allocation":50,"information_confidence":82,"weighted_total":75.0,"trigger_type":"Stage3-Yellow","proposed_stage":"Stage3-Yellow_with_high_MAE_entry_guard","current_profile_error":true}
{"row_type":"score_simulation","case_id":"C01_R1L115_082740_20240821_hanwha_engine_backlog_revenue_recognition","symbol":"082740","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","weights_EPS_Vis_Bott_Mis_Val_Cap_Info":"20/25/18/12/12/8/5","eps_fcf_explosion":86,"earnings_visibility":88,"bottleneck_pricing":84,"market_mispricing":65,"valuation_rerating":55,"capital_allocation":50,"information_confidence":80,"weighted_total":76.7,"trigger_type":"Stage3-Yellow","proposed_stage":"Stage3-Yellow","current_profile_error":false}
{"row_type":"score_simulation","case_id":"C01_R1L115_075580_20240402_sejin_tank_deckhouse_customer_backlog","symbol":"075580","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","weights_EPS_Vis_Bott_Mis_Val_Cap_Info":"20/25/18/12/12/8/5","eps_fcf_explosion":78,"earnings_visibility":82,"bottleneck_pricing":84,"market_mispricing":68,"valuation_rerating":76,"capital_allocation":60,"information_confidence":74,"weighted_total":77.0,"trigger_type":"Stage2-Actionable","proposed_stage":"Stage2-Actionable_to_Stage3-Yellow_when_delivery_confirms","current_profile_error":false}
{"row_type":"score_simulation","case_id":"C01_R1L115_071970_20240731_hd_marine_engine_launch_stage_timing","symbol":"071970","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","weights_EPS_Vis_Bott_Mis_Val_Cap_Info":"20/25/18/12/12/8/5","eps_fcf_explosion":52,"earnings_visibility":55,"bottleneck_pricing":70,"market_mispricing":54,"valuation_rerating":38,"capital_allocation":45,"information_confidence":78,"weighted_total":55.3,"trigger_type":"Stage2-Actionable","proposed_stage":"Stage2-Actionable_not_Stage3_until_revenue_bridge","current_profile_error":true}
{"row_type":"score_simulation","case_id":"C01_R1L115_100090_20240822_sk_oceanplant_backlog_revenue_delay","symbol":"100090","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","weights_EPS_Vis_Bott_Mis_Val_Cap_Info":"20/25/18/12/12/8/5","eps_fcf_explosion":42,"earnings_visibility":38,"bottleneck_pricing":48,"market_mispricing":40,"valuation_rerating":38,"capital_allocation":35,"information_confidence":78,"weighted_total":42.6,"trigger_type":"Stage4B","proposed_stage":"Stage4B_watch_until_revenue_recognition_recovers","current_profile_error":true}
```

## 9. Machine-Readable Rows — aggregate / shadow_weight / residual_contribution

```jsonl
{"row_type":"aggregate","selected_round":"R1","selected_loop":115,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","trigger_rows":6,"calibration_usable_rows":6,"positive_case_count":4,"counterexample_count":2,"current_profile_error_count":3,"avg_MFE_90D_pct":36.94,"avg_MAE_90D_pct":-20.0,"avg_MFE_180D_pct":79.06,"avg_MAE_180D_pct":-20.0,"MFE_90D_ge_20pct_count":4,"MAE_90D_le_minus_20pct_count":3,"new_independent_case_count":6,"same_archetype_new_symbol_count":6,"same_archetype_new_trigger_family_count":6}
{"row_type":"shadow_weight","scope":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","proposal":"increase gating weight on earnings_visibility and bottleneck_pricing only when revenue-recognition bridge is present; block pure reorganization/synergy event from Stage3","axis":"C01_ORDER_BACKLOG_REQUIRES_MARGIN_AND_REVENUE_RECOGNITION_BRIDGE","shadow_only":true,"production_scoring_changed":false}
{"row_type":"residual_contribution","contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"C01_BACKLOG_TO_REVENUE_RECOGNITION_GATE","existing_axis_strengthened":"stage2_required_bridge | local_4b_watch_guard | full_4b_requires_non_price_evidence","why_it_matters":"C01의 실패는 수주잔고 부재보다 수주잔고가 매출인식과 margin bridge로 언제 전환되는지에서 발생한다. 같은 backlog headline이라도 조선 본체, 엔진, 탱크, 해상풍력 하부구조물은 revenue timing이 다르다."}
```

## 10. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
all_rows_have_entry_date: true
all_rows_have_entry_price: true
all_rows_have_MFE_30D_pct: true
all_rows_have_MAE_30D_pct: true
all_rows_have_MFE_90D_pct: true
all_rows_have_MAE_90D_pct: true
all_rows_have_MFE_180D_pct: true
all_rows_have_MAE_180D_pct: true
calibration_usable_rows: 6
representative_rows: 6
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent for stock_agent. Do not rerun web research. Ingest this MD as a v12 residual research artifact. Validate every row_type=trigger for required fields: canonical_archetype_id, large_sector_id, trigger_type, symbol, entry_date, entry_price, MFE_30D_pct, MAE_30D_pct, MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, MAE_180D_pct, calibration_usable, corporate_action_contaminated, same_entry_group_id, dedupe_role. Then evaluate the shadow rule candidate C01_ORDER_BACKLOG_REQUIRES_MARGIN_AND_REVENUE_RECOGNITION_BRIDGE against existing representative rows. If accepted, apply only a scoped C01 rule patch that caps reorganization/synergy-only events at Stage2-Actionable and routes backlog-headline-with-revenue-delay cases to 4B watch. Do not alter non-C01 archetypes from this file alone.
```

## 12. Next Research State

```yaml
completed_round: R1
completed_loop: 115
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
  - C01_ORDER_BACKLOG_MARGIN_BRIDGE_followup_if_still_below_30
  - C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```
