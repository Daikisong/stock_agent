# Checkpoint 28A Round 313 R5 Loop 16 Consumer / Retail / Brands Trigger Validation

## 반영 내용

- `docs/round/round_313.md`의 R5 Loop 16 소비재·유통·브랜드 trigger-level 검증을 calibration-only 데이터로 반영했다.
- 신규 canonical archetype 7개를 추가하고, 기존 `SHRINKFLATION_PRICE_REGULATION_4C_WATCH`와 함께 8개 target archetype을 검증 대상으로 묶었다.
- Samyang Buldak, K-beauty U.S. channel, APR Medicube, China visa-free tourism, Coupang breach/rival shift, Shinsegae-E-Mart/Alibaba JV, Homeplus restructuring, shrinkflation regulation을 case record와 trigger row로 저장했다.
- full adjusted OHLC는 아직 없으므로 reported event return과 event price anchor만 저장하고, full-window MFE/MAE는 `price_data_unavailable_after_deep_search`로 분리했다.

## 핵심 보정

- K-food는 `ASP + shipment + capacity + OP estimate`가 같이 닫히면 Stage2-Actionable 또는 Stage3-Yellow 후보가 될 수 있다.
- K-beauty는 e-commerce growth보다 physical-store sell-through, repeat order, listed-company margin이 Green gate다.
- Beauty device는 viral/celebrity trigger와 해외 매출이 강해도 recurring revenue 전에는 4B overheat를 붙인다.
- Tourism policy는 event return이 있어도 visitor spending, duty-free sales, hotel occupancy, margin 전에는 Stage2다.
- E-commerce는 customer trust와 security breach가 hard gate다. Rival opportunity는 GMV와 logistics margin 전에는 Stage2다.
- Offline grocery는 liquidation value가 going-concern value보다 높으면 asset story가 아니라 hard 4C reference다.
- Shrinkflation regulation은 hidden ASP pass-through를 제한하므로 price-power 4C-watch로 기록한다.

## 산출물

- `src/e2r/sector/round313_r5_loop16_consumer_retail_brand_trigger_validation.py`
- `src/e2r/cli/build_round313_r5_loop16_report.py`
- `tests/test_round313_r5_loop16_consumer_retail_brand_trigger_validation.py`
- `data/e2r_case_library/cases_r5_loop16_round241.jsonl`
- `data/e2r_trigger_calibration/triggers_r5_loop16_round241.jsonl`
- `data/sector_taxonomy/round313_r5_loop16_consumer_retail_brand_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round241_r5_loop16_v1.csv`
- `output/e2r_round313_r5_loop16_consumer_retail_brand_trigger_validation/`

## 검증

- Targeted test: passed.
- Full suite는 커밋 전 실행 대상이다.

## 변경하지 않은 것

- Production scoring은 변경하지 않았다.
- Candidate generation input으로 case library를 사용하지 않았다.
- Stage 3-Green threshold를 낮추지 않았다.
- full OHLC 없이 MFE/MAE를 만들지 않았다.

쉬운 예시: 중국 단체관광 비자면제 발표로 면세·백화점 주가가 움직였더라도, 그날 기준 실제 객단가와 면세점 마진이 아직 없으면 Stage 3-Green이 아니라 Stage2 event로 남긴다.
