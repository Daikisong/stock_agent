# Checkpoint 28A Round 326 R5 Loop 17 Consumer / Retail / Brand

## 반영 내용

- `docs/round/round_326.md`의 R5 Loop 17 소비재·유통·브랜드 trigger-level validation을 반영했다.
- 신규 canonical archetype 7개를 추가하고, 기존 `FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B`와 함께 8개 target archetype으로 묶었다.
- Samyang/Buldak, APR/Medicube, K-beauty indie, China visa-free tourism, Coupang trust break, Baemin/Naver-Uber M&A, Amorepacific China weakness, Dr.G/L'Oreal M&A reference를 case library와 trigger calibration으로 저장했다.
- full adjusted OHLC가 없으므로 MFE/MAE는 만들지 않고 `price_data_unavailable_after_deep_search`로 분리했다.

## 핵심 판정

- Samyang/Buldak: ASP, U.S./Europe shipment, capacity, OP estimate +84%, +5.7% event return이 닫힌 `Stage2-Actionable`.
- APR/Medicube: 해외매출 비중과 valuation rerating은 강하지만 celebrity/viral, tariff, device regulation 때문에 `Stage3-Yellow_candidate`, Green 아님.
- K-beauty indie/Silicon2/d'Alba: U.S. e-commerce +71%와 channel expansion은 `Stage2`, physical-store sell-through가 Green gate.
- China visa-free tourism: retail basket price reaction이 강한 `Stage2-Actionable`, basket size와 OP conversion 필요.
- Coupang: MAU/spending 악화가 붙은 hard `4C`, rival Stage2는 GMV/revenue/margin conversion 확인 전 Green 금지.
- Baemin/Naver-Uber: 큰 M&A trigger지만 final SPA/approval/Naver economics 전까지 `Stage2 + 4B-watch`.
- Amorepacific: China prestige exposure 때문에 failed rerating/4B. U.S.-focused indie K-beauty와 분리해야 한다.
- Dr.G/L'Oreal: K-beauty M&A appetite reference이지만 valuation과 public price anchor가 없어 Stage2 reference only.

## 생성 파일

- `src/e2r/sector/round326_r5_loop17_consumer_retail_brand_trigger_validation.py`
- `src/e2r/cli/build_round326_r5_loop17_report.py`
- `tests/test_round326_r5_loop17_consumer_retail_brand_trigger_validation.py`
- `data/e2r_case_library/cases_r5_loop17_round254.jsonl`
- `data/e2r_trigger_calibration/triggers_r5_loop17_round254.jsonl`
- `data/sector_taxonomy/round326_r5_loop17_consumer_retail_brand_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round254_r5_loop17_v1.csv`
- `output/e2r_round326_r5_loop17_consumer_retail_brand_trigger_validation/`

## 금지 사항

- production scoring은 변경하지 않았다.
- case library를 candidate-generation input으로 쓰지 않는다.
- viral brand, tourism policy, M&A teaser, private M&A reference만으로 Stage3-Green을 만들지 않는다.
- full adjusted OHLC 없이 MFE/MAE를 만들지 않는다.

쉬운 예시: `Samyang`은 숫자가 좋아도 “반복 sell-through와 margin이 계속된다”는 증거가 아직 부족하면 Green이 아니라 Stage2-Actionable이다. 반대로 `Coupang`은 사용자 신뢰와 spending이 깨졌으므로 반등 가능성을 보더라도 먼저 4C로 표시한다.
