# Checkpoint 28A Round 300 R5 Loop 15 Consumer/Retail/Brand Trigger Validation

## 목적

`docs/round/round_300.md`의 R5 Loop 15 내용을 calibration-only 자료로 반영했다.

이번 라운드의 핵심은 “브랜드가 유명하다”가 아니라 ASP, shipment, capacity, OP estimate, ecommerce sell-through, physical channel, tourist spending conversion, data rights, control execution이 실제 Stage 승격 근거인지 분리하는 것이다.

쉬운 예:

- Samyang/Buldak은 ASP 상승, 미국/유럽 shipment, capacity, OP estimate +84%가 같이 닫혀 Stage3-Yellow 후보가 된다.
- Kyochon/Cherrybro는 Jensen Huang 치킨 이벤트로 움직였지만 Kkanbu는 비상장이고 직접 매출 연결이 없어 `price_moved_without_evidence`다.

## 반영 파일

- `src/e2r/sector/round300_r5_loop15_consumer_retail_brand_trigger_validation.py`
- `src/e2r/cli/build_round300_r5_loop15_report.py`
- `tests/test_round300_r5_loop15_consumer_retail_brand_trigger_validation.py`
- `data/e2r_case_library/cases_r5_loop15_round228.jsonl`
- `data/e2r_trigger_calibration/triggers_r5_loop15_round228.jsonl`
- `data/sector_taxonomy/round300_r5_loop15_consumer_retail_brand_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round228_r5_loop15_v1.csv`
- `output/e2r_round300_r5_loop15_consumer_retail_brand_trigger_validation/`

## 추가 archetype

- `K_FOOD_EXPORT_STAGE2_TO_STAGE3_YELLOW`
- `K_FOOD_REGULATORY_FALSE_BREAK_4C_WATCH`
- `K_BEAUTY_US_EXPORT_STAGE2_ACTIONABLE`
- `BEAUTY_DEVICE_VIRAL_STAGE3_WITH_4B`
- `CHINA_TOURIST_DUTYFREE_STAGE2_ACTIONABLE`
- `ECOMMERCE_JV_STAGE2_WITH_DATA_REGULATORY_4B`
- `BRAND_MA_CONTROL_RIGHTS_STAGE2`
- `FRIED_CHICKEN_MEME_PRICE_MOVED_WITHOUT_EVIDENCE`
- `RAMEN_GLOBAL_EXPANSION_STAGE2`
- `TOURISM_REROUTE_EVENT_PREMIUM`

## 산출 요약

- cases: 8
- triggers: 9
- Stage2-Actionable candidates: 4
- Stage3-Yellow candidates: 2
- Stage3-Green candidates: 0
- Stage3-Green confirmed: 0
- 4B watch cases: 5
- 4C watch cases: 4
- hard 4C cases: 0
- missed structural count: 1
- production scoring changed: false
- candidate generation input: false
- full adjusted OHLC complete: false
- shadow weight only: true

## 주요 판정

Samyang Foods / Buldak은 R5의 핵심 missed-structural 후보로 기록했다. ASP, U.S./Europe shipment, capacity expansion, OP estimate +84%, target revision이 같이 닫혀 Stage2보다 강하고 Stage3-Yellow 후보가 맞다.

Samyang Denmark recall은 4C-watch였지만 hard 4C는 아니다. 일부 ban reversal이 있었으므로 “품질 붕괴”가 아니라 regulatory false-break watch로 분리했다.

Nongshim / Shin Ramyun은 Stage2 success candidate다. 글로벌 매출과 미국 목표는 강하지만 OP estimate / event price anchor가 없어 Yellow로 올리지 않았다.

K-beauty basket은 Stage2-Actionable이다. U.S. ecommerce sell-through, export rank, physical retail channel 논의가 확인됐지만 store sell-through와 tariff/margin gate가 남는다.

APR / Medicube는 Stage3-Yellow + 4B-watch다. 해외 매출 비중과 device category가 붙었지만 주가 4배 이후라 valuation overlay가 필요하다.

Chinese tourist / duty-free basket은 Stage2-Actionable이다. 비자정책과 소비주 동반 상승이 있었지만 actual arrivals, card spending, duty-free sales, hotel ADR 전에는 Green이 아니다.

E-Mart / Shinsegae / Alibaba-Gmarket JV는 Stage2 with data-regulatory overlay다. 고객 데이터와 cross-border share는 강하지만 data-sharing restriction, GMV, take-rate, margin gate가 남는다.

F&F / TaylorMade는 Stage2 brand M&A optionality다. consent rights / ROFR는 중요하지만 funding, control execution, ROIC 전에는 Green이 아니다.

Kyochon / Cherrybro / Neuromeka Jensen rally는 `price_moved_without_evidence`다. 유명인 이벤트는 direct same-store sales, franchise fee, repeat purchase 전에는 Stage3 금지다.

## 점수축 보정 방향

올릴 축:

- `export_shipment_growth`
- `asp_increase`
- `op_estimate_revision`
- `production_capacity_expansion`
- `us_europe_sellthrough`
- `physical_retail_channel_entry`
- `repeat_purchase_or_same_store_sales`
- `tourist_arrival_spending_conversion`
- `customer_data_monetization_permission`
- `brand_ma_control_execution`

내릴 축:

- `viral_celebrity_event_only`
- `brand_name_only`
- `tourism_policy_without_spending`
- `jv_without_data_rights`
- `ma_option_without_funding_control`
- `target_market_size_only`
- `social_media_hype_without_repeat_purchase`

## 주의

- production scoring은 변경하지 않았다.
- Stage3-Green threshold를 낮추지 않았다.
- round300 case와 trigger record는 candidate-generation input으로 쓰면 안 된다.
- celebrity meme, policy headline, JV headline, M&A optionality만으로는 Green 금지다.
- full OHLC가 없는데 MFE/MAE를 발명하지 않는다.

## 검증 명령

```bash
PYTHONPATH=src python -m unittest tests.test_round300_r5_loop15_consumer_retail_brand_trigger_validation -v
PYTHONPATH=src python -m e2r.cli.build_round300_r5_loop15_report
```
