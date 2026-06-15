# E2R Stock-Web v12 Residual Research — R3 / C11 Battery Orderbook Rerating / Loop 220

```text
selected_round: R3
selected_loop: 220
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 original index; session-aware quality-repair after C07 loop219
round_schedule_status: coverage_index_selected_not_sequential
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: C11_BATTERY_ORDERBOOK_QUALITY_REVENUE_TIMING_AND_RESET_ENTRY_GATE_V4
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: False
shadow_weight_only: True
new_independent_case_count: 6
usable_trigger_row_count: 12
representative_trigger_count: 12
positive_case_count: 6
counterexample_count: 6
high_MAE90_count: 6
current_profile_error_count: 12
```

## 1. Selection and novelty check
No-Repeat Index 원본에서 C11_BATTERY_ORDERBOOK_RERATING은 18 rows / need to 30 = 12 / need to 50 = 32인 Priority 0 구역이다. 이번 세션에서는 C11을 이미 여러 차례 다뤘으므로, 이전 C11 패스의 코윈테크·윤성에프앤씨·원익피앤이·하나기술·티에스아이·포스코퓨처엠·에코프로비엠·피엔티·씨아이에스·필에너지·엠플러스·나인테크·탑머티리얼·브이원텍·엔시스·에이프로·원준을 피했다. 이번 loop는 이노메트리·지아이텍·이닉스·자비스·디이엔티·아바코로 battery inspection / logistics automation / safety parts / slot-die / laser notching leaf를 압축한다.

## 2. Price source validation
- primary_price_source: Songdaiki/stock-web
- calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
- price_basis: tradable_raw
- price_adjustment_status: raw_unadjusted_marcap
- manifest max_date: 2026-02-20
- MFE/MAE method: entry_date의 close를 entry_price로 사용하고, 이후 N개 tradable rows의 high max / low min을 entry_price와 비교한다.
- profile caveat: selected windows are after any visible corporate-action candidate dates in the opened profiles, except no 2024~2025 candidate overlap was used for the selected rows. Raw/unadjusted caveat remains.

## 3. Case table
| case_id | symbol | name | entry_date | entry_price | trigger_type | label | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | proposed_stage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C11-220-01 | 083930 | 아바코 | 2024-03-05 | 13280.0 | Stage2-Actionable | positive | 34.86 | -1.81 | 61.14 | -1.81 | 61.14 | -5.12 | Stage2-Actionable |
| C11-220-02 | 302430 | 이노메트리 | 2024-04-26 | 11330.0 | Stage2-FalsePositive | counterexample | 9.44 | -8.21 | 9.44 | -30.27 | 9.44 | -39.89 | Stage2-Watch or Stage2-FalsePositive |
| C11-220-03 | 302430 | 이노메트리 | 2024-07-17 | 9700.0 | Stage2-Watch | counterexample | 21.75 | -18.56 | 23.71 | -22.68 | 25.15 | -30.41 | Stage2-Watch or Stage2-FalsePositive |
| C11-220-04 | 302430 | 이노메트리 | 2025-02-27 | 8210.0 | Stage2-Actionable | positive | 47.87 | -10.96 | 47.87 | -10.96 | 47.87 | -20.22 | Stage2-Actionable |
| C11-220-05 | 382480 | 지아이텍 | 2024-05-22 | 2710.0 | Stage2-FalsePositive | counterexample | 14.02 | -5.35 | 14.02 | -28.78 | 14.02 | -33.8 | Stage2-Watch or Stage2-FalsePositive |
| C11-220-06 | 382480 | 지아이텍 | 2025-02-07 | 2045.0 | Stage2-Actionable | positive | 14.67 | -2.2 | 49.14 | -2.2 | 49.14 | -3.18 | Stage2-Actionable |
| C11-220-07 | 452400 | 이닉스 | 2024-02-01 | 37100.0 | Stage2-FalsePositive | counterexample | 16.71 | -43.94 | 16.71 | -61.62 | 16.71 | -76.42 | Stage2-Watch or Stage2-FalsePositive |
| C11-220-08 | 452400 | 이닉스 | 2024-12-17 | 9630.0 | Stage2-Watch | positive | 11.63 | -8.52 | 16.41 | -20.04 | 52.65 | -20.04 | Stage2-Watch / staged-entry positive |
| C11-220-09 | 254120 | 자비스 | 2024-03-18 | 2480.0 | Stage2-FalsePositive | counterexample | 0.2 | -18.55 | 20.16 | -18.55 | 20.16 | -53.63 | Stage2-Watch or Stage2-FalsePositive |
| C11-220-10 | 254120 | 자비스 | 2024-12-10 | 1260.0 | Stage2-Actionable | positive | 11.43 | -3.89 | 71.83 | -3.89 | 71.83 | -3.89 | Stage2-Actionable |
| C11-220-11 | 079810 | 디이엔티 | 2024-08-01 | 8920.0 | Stage2-FalsePositive | counterexample | -1.12 | -25.45 | 5.72 | -48.65 | 5.72 | -48.65 | Stage2-Watch or Stage2-FalsePositive |
| C11-220-12 | 079810 | 디이엔티 | 2024-12-05 | 5140.0 | Stage2-Actionable | positive | 25.1 | -10.89 | 52.72 | -10.89 | 61.48 | -10.89 | Stage2-Actionable |

## 4. Case notes and evidence ledger
### C11-220-01 — 아바코 (083930)
- trigger_type: Stage2-Actionable / proposed_stage: Stage2-Actionable / label: positive
- evidence_date: 2024-03-05 / entry_date: 2024-03-05 / entry_price: 13280.0
- evidence_summary: LG Energy Solution Michigan향 2차전지 자동화장비 109억원 추가 계약과 2023년 신규수주 3060억원/2024년 실적 반영 기대가 결합된 order-to-revenue bridge.
- evidence_url: https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2024/03/12/240313_avaco.pdf
- current_profile_residual_error: old profile may underweight named customer + accumulated logistics order backlog conversion
- path_read: 30D 34.86 / -1.81, 90D 61.14 / -1.81, 180D 61.14 / -5.12

### C11-220-02 — 이노메트리 (302430)
- trigger_type: Stage2-FalsePositive / proposed_stage: Stage2-Watch or Stage2-FalsePositive / label: counterexample
- evidence_date: 2024-04-26 / entry_date: 2024-04-26 / entry_price: 11330.0
- evidence_summary: 2023년 최대 실적과 529억원 수주잔고, 2024년 매출/OP 성장 전망은 강했지만 entry 후 MFE가 작고 MAE가 깊었다.
- evidence_url: https://kbthink.com/securities-view.html?docId=20240426164648983K
- current_profile_residual_error: Stage2 bridge exists but orderbook quality/timing and EV tape were insufficient
- path_read: 30D 9.44 / -8.21, 90D 9.44 / -30.27, 180D 9.44 / -39.89

### C11-220-03 — 이노메트리 (302430)
- trigger_type: Stage2-Watch / proposed_stage: Stage2-Watch or Stage2-FalsePositive / label: counterexample
- evidence_date: 2024-07-17 / entry_date: 2024-07-17 / entry_price: 9700.0
- evidence_summary: 신규 검사장비 수주 1000억원 돌파와 라인업 다변화 evidence가 있었으나, 이미 weak EV tape/late-entry geometry가 섞였다.
- evidence_url: https://www.etnews.com/20240717000012
- current_profile_residual_error: large order number alone would over-promote; high-MAE guard needed
- path_read: 30D 21.75 / -18.56, 90D 23.71 / -22.68, 180D 25.15 / -30.41

### C11-220-04 — 이노메트리 (302430)
- trigger_type: Stage2-Actionable / proposed_stage: Stage2-Actionable / label: positive
- evidence_date: 2025-02-27 / entry_date: 2025-02-27 / entry_price: 8210.0
- evidence_summary: 국내 대형 고객사 ESS/LFP 라인향 CT 및 간극 검사장비 일괄 수주 증가가 reset price와 맞물렸다.
- evidence_url: https://www.innometry.com/pr/pr_view.html?code=news&idx=91
- current_profile_residual_error: current profile may be too late after reset when named line/order language appears
- path_read: 30D 47.87 / -10.96, 90D 47.87 / -10.96, 180D 47.87 / -20.22

### C11-220-05 — 지아이텍 (382480)
- trigger_type: Stage2-FalsePositive / proposed_stage: Stage2-Watch or Stage2-FalsePositive / label: counterexample
- evidence_date: 2024-05-22 / entry_date: 2024-05-22 / entry_price: 2710.0
- evidence_summary: LGES 단일 고객에서 SK온·삼성SDI로 고객이 넓어졌다는 전략 narrative는 있었지만 signed order/revenue timing은 약했다.
- evidence_url: https://m.thebell.co.kr/m/newsview.asp?newskey=202405211455159240109393&svccode=
- current_profile_residual_error: customer-vocabulary bridge insufficient without amount/timing/margin
- path_read: 30D 14.02 / -5.35, 90D 14.02 / -28.78, 180D 14.02 / -33.8

### C11-220-06 — 지아이텍 (382480)
- trigger_type: Stage2-Actionable / proposed_stage: Stage2-Actionable / label: positive
- evidence_date: 2025-02-07 / entry_date: 2025-02-07 / entry_price: 2045.0
- evidence_summary: LG에너지솔루션에 슬롯다이 연계 펌프 시스템 공급 개시. customer + product + supply route가 직접 확인됐다.
- evidence_url: https://www.gitech.com/bbs/board.php?bo_table=board&page=1&sod=desc&sop=and&sst=wr_hit&wr_id=67
- current_profile_residual_error: qualified customer/product supply route should unlock after reset
- path_read: 30D 14.67 / -2.2, 90D 49.14 / -2.2, 180D 49.14 / -3.18

### C11-220-07 — 이닉스 (452400)
- trigger_type: Stage2-FalsePositive / proposed_stage: Stage2-Watch or Stage2-FalsePositive / label: counterexample
- evidence_date: 2024-02-01 / entry_date: 2024-02-01 / entry_price: 37100.0
- evidence_summary: 2028년까지 3444억원 수주잔고와 현대모비스/H그린파워/SKBA 고객사가 확인됐지만, IPO entry는 valuation/EV chasm MAE가 너무 컸다.
- evidence_url: https://plus.hankyung.com/apps/newsinside.view?aid=2024010550726&category=&sns=y
- current_profile_residual_error: orderbook exists, but IPO valuation and downstream EV tape must gate promotion
- path_read: 30D 16.71 / -43.94, 90D 16.71 / -61.62, 180D 16.71 / -76.42

### C11-220-08 — 이닉스 (452400)
- trigger_type: Stage2-Watch / proposed_stage: Stage2-Watch / staged-entry positive / label: positive
- evidence_date: 2024-12-17 / entry_date: 2024-12-17 / entry_price: 9630.0
- evidence_summary: 수주잔고는 긍정적이나 업황 부담이라는 reset framing. early promotion은 금지하되 reset/staged entry는 작동했다.
- evidence_url: https://m.irgo.co.kr/IR-COMP/452400/
- current_profile_residual_error: need staged-entry rather than clean positive due to call-off/demand burden
- path_read: 30D 11.63 / -8.52, 90D 16.41 / -20.04, 180D 52.65 / -20.04

### C11-220-09 — 자비스 (254120)
- trigger_type: Stage2-FalsePositive / proposed_stage: Stage2-Watch or Stage2-FalsePositive / label: counterexample
- evidence_date: 2024-03-18 / entry_date: 2024-03-18 / entry_price: 2480.0
- evidence_summary: 2023년 2차전지 검사장비 수주 확대와 매출/OP 개선은 있었지만 BW 평가손실·당기순손실과 price drawdown이 컸다.
- evidence_url: https://m.thebell.co.kr/m/newsview.asp?newskey=202403151353425760106314&svccode=
- current_profile_residual_error: revenue/order bridge must be paired with financing/accounting drag check
- path_read: 30D 0.2 / -18.55, 90D 20.16 / -18.55, 180D 20.16 / -53.63

### C11-220-10 — 자비스 (254120)
- trigger_type: Stage2-Actionable / proposed_stage: Stage2-Actionable / label: positive
- evidence_date: 2024-12-10 / entry_date: 2024-12-10 / entry_price: 1260.0
- evidence_summary: Xscan 2차전지 검사장비 매출 CAGR와 2024년 매출 반영 route가 reset price 이후 강하게 작동했다.
- evidence_url: https://stock.pstatic.net/stock-research/company/1/20241210_company_470912000.pdf
- current_profile_residual_error: current profile may miss reset + revenue conversion combination
- path_read: 30D 11.43 / -3.89, 90D 71.83 / -3.89, 180D 71.83 / -3.89

### C11-220-11 — 디이엔티 (079810)
- trigger_type: Stage2-FalsePositive / proposed_stage: Stage2-Watch or Stage2-FalsePositive / label: counterexample
- evidence_date: 2024-08-01 / entry_date: 2024-08-01 / entry_price: 8920.0
- evidence_summary: NextStar/Honda/LGES Michigan laser notching delivery chronology는 있었지만, 2024년 8월 entry는 demand tape와 가격경로가 나빴다.
- evidence_url: https://www.saramin.co.kr/zf_user/company-info/view/csn/QUNGclVSRm0xMW1kQndDcXdtekxjQT09/company_nm/%28%EC%A3%BC%29%EB%94%94%EC%9D%B4%EC%97%94%ED%8B%B0?srsltid=AfmBOoqmR5vFxRxeNPsBBnAqQxXizMjwZIdeiajOTF1Baa7rVT8vgip1
- current_profile_residual_error: delivery list alone should not unlock without fresh order/revenue conversion
- path_read: 30D -1.12 / -25.45, 90D 5.72 / -48.65, 180D 5.72 / -48.65

### C11-220-12 — 디이엔티 (079810)
- trigger_type: Stage2-Actionable / proposed_stage: Stage2-Actionable / label: positive
- evidence_date: 2024-12-05 / entry_date: 2024-12-05 / entry_price: 5140.0
- evidence_summary: Laser Notching 장비 전문성과 빠른 수주 증가 기대가 낮아진 가격대에서 revenue bridge로 작동했다.
- evidence_url: https://w4.kirs.or.kr/download/research/241205_%EA%B8%B0%EA%B3%84%2C%EC%9E%A5%EB%B9%84_%EB%94%94%EC%9D%B4%EC%97%94%ED%8B%B0%28079810%29_%EB%B9%A0%EB%A5%B8%20%EC%86%8D%EB%8F%84%EC%9D%98%20%EC%88%98%EC%A3%BC%20%EC%A6%9D%EA%B0%80%EA%B0%80%20%EA%B8%B0%EB%8C%80%EB%90%98%EB%8A%94%20Laser%20Notching%20%EC%9E%A5%EB%B9%84%20%EC%A0%84%EB%AC%B8%20%EA%B8%B0%EC%97%85_NICE%EB%94%94%EC%95%A4%EB%B9%84.pdf
- current_profile_residual_error: reset entry plus specific equipment order-growth should get higher watch/actionable score
- path_read: 30D 25.1 / -10.89, 90D 52.72 / -10.89, 180D 61.48 / -10.89

## 5. Current calibrated profile stress test
The current calibrated profile already blocks price-only blowoff and requires non-price evidence for full 4B. The residual error in C11 is narrower: many rows have non-price orderbook evidence, but the evidence layer is not always strong enough to become issuer-level revenue conversion. 이노메트리 2024-04/07, 이닉스 IPO, 자비스 2024-03, 디이엔티 2024-08처럼 “수주잔고/고객/장비명”은 있으나 call-off, revenue timing, margin bridge, valuation reset이 약하면 Stage2-Actionable이 과하다. 반대로 아바코 2024-03, 지아이텍 2025-02, 자비스 2024-12, 디이엔티 2024-12처럼 reset price와 customer/product/revenue bridge가 같이 붙으면 Stage2-Actionable을 과잉 차단하면 too-late error가 된다.

## 6. Shadow rule candidate
```text
rule_id = C11_ORDERBOOK_QUALITY_REVENUE_TIMING_AND_RESET_ENTRY_GATE_V4
scope = C11_BATTERY_ORDERBOOK_RERATING
if evidence contains named_customer + signed_order_or_orderbook_amount + delivery_or_revenue_window:
    allow Stage2-Actionable, unless MAE geometry is already local 4B
elif evidence contains orderbook/backlog/customer vocabulary but no call-off/revenue timing/margin bridge:
    cap at Stage2-Watch
if IPO/late-headline/high-valuation context and MAE90 <= -20 with MFE90 < 20:
    route to Stage2-FalsePositive or local 4B watch
if reset-entry after prior drawdown and MFE90 >= 35 with MAE90 > -15:
    lift to Stage2-Actionable even if prior sector tape was weak
```

## 7. Machine-readable trigger rows JSONL
{"case_id": "C11-220-01", "symbol": "083930", "name": "아바코", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-Actionable", "label": "positive", "fine": "battery_logistics_automation_signed_lges_order", "evidence_date": "2024-03-05", "entry_date": "2024-03-05", "entry_price": 13280.0, "MFE_30D_pct": 34.86, "MAE_30D_pct": -1.81, "MFE_90D_pct": 61.14, "MAE_90D_pct": -1.81, "MFE_180D_pct": 61.14, "MAE_180D_pct": -5.12, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "proposed_stage": "Stage2-Actionable", "evidence_url": "https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2024/03/12/240313_avaco.pdf", "duplicate_key": "C11_BATTERY_ORDERBOOK_RERATING|083930|Stage2-Actionable|2024-03-05"}
{"case_id": "C11-220-02", "symbol": "302430", "name": "이노메트리", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-FalsePositive", "label": "counterexample", "fine": "battery_xray_inspection_backlog_but_customer_capex_drag", "evidence_date": "2024-04-26", "entry_date": "2024-04-26", "entry_price": 11330.0, "MFE_30D_pct": 9.44, "MAE_30D_pct": -8.21, "MFE_90D_pct": 9.44, "MAE_90D_pct": -30.27, "MFE_180D_pct": 9.44, "MAE_180D_pct": -39.89, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "proposed_stage": "Stage2-Watch or Stage2-FalsePositive", "evidence_url": "https://kbthink.com/securities-view.html?docId=20240426164648983K", "duplicate_key": "C11_BATTERY_ORDERBOOK_RERATING|302430|Stage2-FalsePositive|2024-04-26"}
{"case_id": "C11-220-03", "symbol": "302430", "name": "이노메트리", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-Watch", "label": "counterexample", "fine": "battery_inspection_order_1000b_but_late_high_mae", "evidence_date": "2024-07-17", "entry_date": "2024-07-17", "entry_price": 9700.0, "MFE_30D_pct": 21.75, "MAE_30D_pct": -18.56, "MFE_90D_pct": 23.71, "MAE_90D_pct": -22.68, "MFE_180D_pct": 25.15, "MAE_180D_pct": -30.41, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "proposed_stage": "Stage2-Watch or Stage2-FalsePositive", "evidence_url": "https://www.etnews.com/20240717000012", "duplicate_key": "C11_BATTERY_ORDERBOOK_RERATING|302430|Stage2-Watch|2024-07-17"}
{"case_id": "C11-220-04", "symbol": "302430", "name": "이노메트리", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-Actionable", "label": "positive", "fine": "battery_lfp_ess_inspection_reset_order_route", "evidence_date": "2025-02-27", "entry_date": "2025-02-27", "entry_price": 8210.0, "MFE_30D_pct": 47.87, "MAE_30D_pct": -10.96, "MFE_90D_pct": 47.87, "MAE_90D_pct": -10.96, "MFE_180D_pct": 47.87, "MAE_180D_pct": -20.22, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "proposed_stage": "Stage2-Actionable", "evidence_url": "https://www.innometry.com/pr/pr_view.html?code=news&idx=91", "duplicate_key": "C11_BATTERY_ORDERBOOK_RERATING|302430|Stage2-Actionable|2025-02-27"}
{"case_id": "C11-220-05", "symbol": "382480", "name": "지아이텍", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-FalsePositive", "label": "counterexample", "fine": "slot_die_customer_expansion_without_order_amount", "evidence_date": "2024-05-22", "entry_date": "2024-05-22", "entry_price": 2710.0, "MFE_30D_pct": 14.02, "MAE_30D_pct": -5.35, "MFE_90D_pct": 14.02, "MAE_90D_pct": -28.78, "MFE_180D_pct": 14.02, "MAE_180D_pct": -33.8, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "proposed_stage": "Stage2-Watch or Stage2-FalsePositive", "evidence_url": "https://m.thebell.co.kr/m/newsview.asp?newskey=202405211455159240109393&svccode=", "duplicate_key": "C11_BATTERY_ORDERBOOK_RERATING|382480|Stage2-FalsePositive|2024-05-22"}
{"case_id": "C11-220-06", "symbol": "382480", "name": "지아이텍", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-Actionable", "label": "positive", "fine": "lges_pump_system_supply_conversion", "evidence_date": "2025-02-07", "entry_date": "2025-02-07", "entry_price": 2045.0, "MFE_30D_pct": 14.67, "MAE_30D_pct": -2.2, "MFE_90D_pct": 49.14, "MAE_90D_pct": -2.2, "MFE_180D_pct": 49.14, "MAE_180D_pct": -3.18, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "proposed_stage": "Stage2-Actionable", "evidence_url": "https://www.gitech.com/bbs/board.php?bo_table=board&page=1&sod=desc&sop=and&sst=wr_hit&wr_id=67", "duplicate_key": "C11_BATTERY_ORDERBOOK_RERATING|382480|Stage2-Actionable|2025-02-07"}
{"case_id": "C11-220-07", "symbol": "452400", "name": "이닉스", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-FalsePositive", "label": "counterexample", "fine": "ipo_orderbook_but_initial_valuation_and_ev_chasm", "evidence_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 37100.0, "MFE_30D_pct": 16.71, "MAE_30D_pct": -43.94, "MFE_90D_pct": 16.71, "MAE_90D_pct": -61.62, "MFE_180D_pct": 16.71, "MAE_180D_pct": -76.42, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "proposed_stage": "Stage2-Watch or Stage2-FalsePositive", "evidence_url": "https://plus.hankyung.com/apps/newsinside.view?aid=2024010550726&category=&sns=y", "duplicate_key": "C11_BATTERY_ORDERBOOK_RERATING|452400|Stage2-FalsePositive|2024-02-01"}
{"case_id": "C11-220-08", "symbol": "452400", "name": "이닉스", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-Watch", "label": "positive", "fine": "orderbook_positive_but_industry_burden_reset", "evidence_date": "2024-12-17", "entry_date": "2024-12-17", "entry_price": 9630.0, "MFE_30D_pct": 11.63, "MAE_30D_pct": -8.52, "MFE_90D_pct": 16.41, "MAE_90D_pct": -20.04, "MFE_180D_pct": 52.65, "MAE_180D_pct": -20.04, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "proposed_stage": "Stage2-Watch / staged-entry positive", "evidence_url": "https://m.irgo.co.kr/IR-COMP/452400/", "duplicate_key": "C11_BATTERY_ORDERBOOK_RERATING|452400|Stage2-Watch|2024-12-17"}
{"case_id": "C11-220-09", "symbol": "254120", "name": "자비스", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-FalsePositive", "label": "counterexample", "fine": "battery_xray_order_but_bond_loss_and_high_mae", "evidence_date": "2024-03-18", "entry_date": "2024-03-18", "entry_price": 2480.0, "MFE_30D_pct": 0.2, "MAE_30D_pct": -18.55, "MFE_90D_pct": 20.16, "MAE_90D_pct": -18.55, "MFE_180D_pct": 20.16, "MAE_180D_pct": -53.63, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "proposed_stage": "Stage2-Watch or Stage2-FalsePositive", "evidence_url": "https://m.thebell.co.kr/m/newsview.asp?newskey=202403151353425760106314&svccode=", "duplicate_key": "C11_BATTERY_ORDERBOOK_RERATING|254120|Stage2-FalsePositive|2024-03-18"}
{"case_id": "C11-220-10", "symbol": "254120", "name": "자비스", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-Actionable", "label": "positive", "fine": "battery_xscan_revenue_conversion_after_reset", "evidence_date": "2024-12-10", "entry_date": "2024-12-10", "entry_price": 1260.0, "MFE_30D_pct": 11.43, "MAE_30D_pct": -3.89, "MFE_90D_pct": 71.83, "MAE_90D_pct": -3.89, "MFE_180D_pct": 71.83, "MAE_180D_pct": -3.89, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "proposed_stage": "Stage2-Actionable", "evidence_url": "https://stock.pstatic.net/stock-research/company/1/20241210_company_470912000.pdf", "duplicate_key": "C11_BATTERY_ORDERBOOK_RERATING|254120|Stage2-Actionable|2024-12-10"}
{"case_id": "C11-220-11", "symbol": "079810", "name": "디이엔티", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-FalsePositive", "label": "counterexample", "fine": "laser_notching_delivery_vocabulary_but_late_ev_tape", "evidence_date": "2024-08-01", "entry_date": "2024-08-01", "entry_price": 8920.0, "MFE_30D_pct": -1.12, "MAE_30D_pct": -25.45, "MFE_90D_pct": 5.72, "MAE_90D_pct": -48.65, "MFE_180D_pct": 5.72, "MAE_180D_pct": -48.65, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "proposed_stage": "Stage2-Watch or Stage2-FalsePositive", "evidence_url": "https://www.saramin.co.kr/zf_user/company-info/view/csn/QUNGclVSRm0xMW1kQndDcXdtekxjQT09/company_nm/%28%EC%A3%BC%29%EB%94%94%EC%9D%B4%EC%97%94%ED%8B%B0?srsltid=AfmBOoqmR5vFxRxeNPsBBnAqQxXizMjwZIdeiajOTF1Baa7rVT8vgip1", "duplicate_key": "C11_BATTERY_ORDERBOOK_RERATING|079810|Stage2-FalsePositive|2024-08-01"}
{"case_id": "C11-220-12", "symbol": "079810", "name": "디이엔티", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "trigger_type": "Stage2-Actionable", "label": "positive", "fine": "laser_notching_order_growth_reset_positive", "evidence_date": "2024-12-05", "entry_date": "2024-12-05", "entry_price": 5140.0, "MFE_30D_pct": 25.1, "MAE_30D_pct": -10.89, "MFE_90D_pct": 52.72, "MAE_90D_pct": -10.89, "MFE_180D_pct": 61.48, "MAE_180D_pct": -10.89, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "proposed_stage": "Stage2-Actionable", "evidence_url": "https://w4.kirs.or.kr/download/research/241205_%EA%B8%B0%EA%B3%84%2C%EC%9E%A5%EB%B9%84_%EB%94%94%EC%9D%B4%EC%97%94%ED%8B%B0%28079810%29_%EB%B9%A0%EB%A5%B8%20%EC%86%8D%EB%8F%84%EC%9D%98%20%EC%88%98%EC%A3%BC%20%EC%A6%9D%EA%B0%80%EA%B0%80%20%EA%B8%B0%EB%8C%80%EB%90%98%EB%8A%94%20Laser%20Notching%20%EC%9E%A5%EB%B9%84%20%EC%A0%84%EB%AC%B8%20%EA%B8%B0%EC%97%85_NICE%EB%94%94%EC%95%A4%EB%B9%84.pdf", "duplicate_key": "C11_BATTERY_ORDERBOOK_RERATING|079810|Stage2-Actionable|2024-12-05"}

## 8. Machine-readable score_simulation JSONL
{"case_id": "C11-220-01", "symbol": "083930", "component_scores": {"earnings_visibility": 16, "orderbook_quality": 20, "customer_calloff_visibility": 16, "margin_conversion_bridge": 14, "entry_geometry_risk_guard": 2, "source_confidence": 8}, "simulated_total_score": 76, "proposed_stage": "Stage2-Actionable", "current_profile_residual_error": "old profile may underweight named customer + accumulated logistics order backlog conversion"}
{"case_id": "C11-220-02", "symbol": "302430", "component_scores": {"earnings_visibility": 9, "orderbook_quality": 7, "customer_calloff_visibility": 8, "margin_conversion_bridge": 6, "entry_geometry_risk_guard": -4, "source_confidence": 8}, "simulated_total_score": 34, "proposed_stage": "Stage2-Watch or Stage2-FalsePositive", "current_profile_residual_error": "Stage2 bridge exists but orderbook quality/timing and EV tape were insufficient"}
{"case_id": "C11-220-03", "symbol": "302430", "component_scores": {"earnings_visibility": 9, "orderbook_quality": 7, "customer_calloff_visibility": 8, "margin_conversion_bridge": 6, "entry_geometry_risk_guard": -4, "source_confidence": 8}, "simulated_total_score": 34, "proposed_stage": "Stage2-Watch or Stage2-FalsePositive", "current_profile_residual_error": "large order number alone would over-promote; high-MAE guard needed"}
{"case_id": "C11-220-04", "symbol": "302430", "component_scores": {"earnings_visibility": 16, "orderbook_quality": 11, "customer_calloff_visibility": 16, "margin_conversion_bridge": 14, "entry_geometry_risk_guard": 2, "source_confidence": 8}, "simulated_total_score": 67, "proposed_stage": "Stage2-Actionable", "current_profile_residual_error": "current profile may be too late after reset when named line/order language appears"}
{"case_id": "C11-220-05", "symbol": "382480", "component_scores": {"earnings_visibility": 9, "orderbook_quality": 7, "customer_calloff_visibility": 8, "margin_conversion_bridge": 6, "entry_geometry_risk_guard": -4, "source_confidence": 8}, "simulated_total_score": 34, "proposed_stage": "Stage2-Watch or Stage2-FalsePositive", "current_profile_residual_error": "customer-vocabulary bridge insufficient without amount/timing/margin"}
{"case_id": "C11-220-06", "symbol": "382480", "component_scores": {"earnings_visibility": 16, "orderbook_quality": 20, "customer_calloff_visibility": 16, "margin_conversion_bridge": 14, "entry_geometry_risk_guard": 2, "source_confidence": 8}, "simulated_total_score": 76, "proposed_stage": "Stage2-Actionable", "current_profile_residual_error": "qualified customer/product supply route should unlock after reset"}
{"case_id": "C11-220-07", "symbol": "452400", "component_scores": {"earnings_visibility": 9, "orderbook_quality": 7, "customer_calloff_visibility": 8, "margin_conversion_bridge": 6, "entry_geometry_risk_guard": -4, "source_confidence": 8}, "simulated_total_score": 34, "proposed_stage": "Stage2-Watch or Stage2-FalsePositive", "current_profile_residual_error": "orderbook exists, but IPO valuation and downstream EV tape must gate promotion"}
{"case_id": "C11-220-08", "symbol": "452400", "component_scores": {"earnings_visibility": 16, "orderbook_quality": 11, "customer_calloff_visibility": 16, "margin_conversion_bridge": 14, "entry_geometry_risk_guard": -4, "source_confidence": 8}, "simulated_total_score": 61, "proposed_stage": "Stage2-Watch / staged-entry positive", "current_profile_residual_error": "need staged-entry rather than clean positive due to call-off/demand burden"}
{"case_id": "C11-220-09", "symbol": "254120", "component_scores": {"earnings_visibility": 9, "orderbook_quality": 7, "customer_calloff_visibility": 8, "margin_conversion_bridge": 6, "entry_geometry_risk_guard": 2, "source_confidence": 8}, "simulated_total_score": 40, "proposed_stage": "Stage2-Watch or Stage2-FalsePositive", "current_profile_residual_error": "revenue/order bridge must be paired with financing/accounting drag check"}
{"case_id": "C11-220-10", "symbol": "254120", "component_scores": {"earnings_visibility": 16, "orderbook_quality": 11, "customer_calloff_visibility": 16, "margin_conversion_bridge": 14, "entry_geometry_risk_guard": 2, "source_confidence": 8}, "simulated_total_score": 67, "proposed_stage": "Stage2-Actionable", "current_profile_residual_error": "current profile may miss reset + revenue conversion combination"}
{"case_id": "C11-220-11", "symbol": "079810", "component_scores": {"earnings_visibility": 9, "orderbook_quality": 7, "customer_calloff_visibility": 8, "margin_conversion_bridge": 6, "entry_geometry_risk_guard": -4, "source_confidence": 8}, "simulated_total_score": 34, "proposed_stage": "Stage2-Watch or Stage2-FalsePositive", "current_profile_residual_error": "delivery list alone should not unlock without fresh order/revenue conversion"}
{"case_id": "C11-220-12", "symbol": "079810", "component_scores": {"earnings_visibility": 16, "orderbook_quality": 20, "customer_calloff_visibility": 16, "margin_conversion_bridge": 14, "entry_geometry_risk_guard": 2, "source_confidence": 8}, "simulated_total_score": 76, "proposed_stage": "Stage2-Actionable", "current_profile_residual_error": "reset entry plus specific equipment order-growth should get higher watch/actionable score"}

## 9. Aggregate row
```json
{
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING",
  "trigger_rows": 12,
  "unique_symbols": 6,
  "positive_case_count": 6,
  "counterexample_count": 6,
  "high_MAE90_count": 6,
  "avg_MFE90": 32.41,
  "avg_MAE90": -21.69,
  "rule_candidate": "C11_ORDERBOOK_QUALITY_REVENUE_TIMING_AND_RESET_ENTRY_GATE_V4"
}
```

## 10. Residual contribution summary
```text
new_axis_proposed: c11_orderbook_quality_revenue_timing_and_reset_entry_gate_v4
existing_axis_strengthened: full_4b_requires_non_price_evidence|price_only_blowoff_blocks_positive_stage
existing_axis_weakened: none
sector_specific_rule_candidate: L3_BATTERY_ORDERBOOK_REVENUE_TIMING_AND_CALL_OFF_GATE_V4
canonical_archetype_rule_candidate: C11_ORDERBOOK_QUALITY_REVENUE_TIMING_AND_RESET_ENTRY_GATE_V4
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 11. Deferred Coding Agent Handoff Prompt — do not execute in this research session
```text
Read this MD as a v12 research artifact only. Do not infer production scoring changes from one file. In the batch calibration session, parse trigger_rows JSONL, validate duplicate keys, recompute MFE/MAE from Songdaiki/stock-web, then consider a scoped C11 rule candidate that requires named customer/orderbook amount plus delivery/revenue timing before Stage2-Actionable. Treat IPO/late-headline rows with MAE90 <= -20 and MFE90 < 20 as false-positive/local-4B candidates. Keep production scoring unchanged until batch validation passes.
```

## 12. Next research state
```text
completed_round = R3
completed_loop = 220
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 original index; session-aware quality-repair
next_recommended_archetypes = C01_ORDER_BACKLOG_MARGIN_BRIDGE|C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|C02_POWER_GRID_DATACENTER_CAPEX
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```