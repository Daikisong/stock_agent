# Checkpoint 28A Round 287 R5 Loop 14 Consumer Retail Brand Price Validation

## Scope

`docs/round/round_287.md`를 R5 소비재/유통/브랜드 가격경로 검증팩으로 구조화했다.

이번 패치는 calibration/evaluation 자료만 추가한다.

- production scoring 변경 없음
- candidate generation 변경 없음
- StageClassifier threshold 변경 없음
- 케이스 레코드를 후보 생성 입력으로 사용하지 않음

쉬운 예시: `Buldak 수출`은 ASP, 미국/유럽 shipment, CAPA, OP 추정치가 같이 붙으면 강한 후보가 될 수 있다. 그러나 덴마크 리콜처럼 현지 규제 적합성 문제가 있으면 Green 전에 별도 4C-watch 게이트로 남겨야 한다.

## Added Archetypes

다음 canonical archetype을 추가했다.

- `K_FOOD_EXPORT_BRAND_STAGE3_CANDIDATE`
- `K_FOOD_EXPORT_REGULATORY_4C_WATCH`
- `K_BEAUTY_DEVICE_BRAND_4B`
- `K_BEAUTY_US_EXPANSION_STAGE2`
- `CHINA_TOURISM_RETAIL_EVENT_PREMIUM`
- `ECOMMERCE_CROSS_BORDER_JV_STAGE2_DATA_GATE`
- `ECOMMERCE_TRUST_BREAK_HARD_REFERENCE`
- `RETAIL_FULFILLMENT_UNIT_ECONOMICS_STAGE2`
- `DOMESTIC_CONSUMPTION_SHOCK_4C_WATCH`

## Case Pack

생성 파일:

- `data/e2r_case_library/cases_r5_loop14_round287.jsonl`
- `data/sector_taxonomy/round287_r5_loop14_consumer_retail_brand_price_validation_audit.json`
- `output/e2r_round287_r5_loop14_consumer_retail_brand_price_validation/round287_r5_loop14_price_validation_summary.md`
- `output/e2r_round287_r5_loop14_consumer_retail_brand_price_validation/round287_r5_loop14_case_matrix.csv`
- `output/e2r_round287_r5_loop14_consumer_retail_brand_price_validation/round287_r5_loop14_green_gate_review.md`
- `output/e2r_round287_r5_loop14_consumer_retail_brand_price_validation/round287_r5_loop14_stage4b_4c_review.md`

요약:

- cases: 9
- Stage 3 dated candidates: 1
- Stage 4B watch: 6
- Stage 4C watch: 6
- hard 4C: 1
- service trust hard reference: 1
- full adjusted OHLC complete: false

## Key Interpretation

Samyang/Buldak은 이번 R5에서 가장 Stage 3에 가까운 케이스로 기록했다. 다만 `local regulatory fit`이 Green gate로 남는다.

Nongshim/Shin Ramyun, K-beauty U.S. expansion, APR/Medicube, CJ Logistics는 Stage 2 또는 4B-watch 성격이다. 가격 anchor와 sell-through, tariff absorption, repeat purchase, unit economics가 부족한 부분은 그대로 부족하다고 기록했다.

관광/면세/백화점 basket은 방문객 수가 아니라 객단가, 구매전환율, duty-free margin이 닫혀야 한다. 그래서 `CHINA_TOURISM_RETAIL_EVENT_PREMIUM`은 Green 후보가 아니라 event premium 중심으로 둔다.

Gmarket/AliExpress JV는 JV 규모와 5천만 고객 DB만으로 Green이 될 수 없다. take-rate, GMV, fulfillment margin, data compliance가 필요하다.

Coupang data breach는 hard trust reference다. Naver/CJ Logistics 같은 경쟁사 read-through가 있어도 그것만으로 Green을 만들 수 없게 기록했다.

## Green Gates

Round 287의 Green required fields:

- export_sellthrough_confirmed
- brand_ASP_power_confirmed
- capacity_to_revenue_conversion_confirmed
- offline_channel_sellthrough_confirmed
- tariff_absorption_confirmed
- tourist_spend_per_head_confirmed
- ecommerce_take_rate_confirmed
- data_trust_internal_control_confirmed
- fulfillment_unit_economics_confirmed
- domestic_consumption_sensitivity_measured
- price_path_after_evidence

Forbidden patterns:

- viral_brand_headline_only
- visitor_count_only
- online_ecommerce_growth_without_offline_sellthrough
- JV_scale_without_take_rate
- revenue_uplift_without_unit_economics
- IPO_or_stock_pop_without_repeat_purchase
- consumer_export_story_without_local_regulatory_fit
- domestic_retail_ignored
- data_breach_or_customer_trust_failure

## Verification

실행한 명령:

```bash
PYTHONPATH=src python -m py_compile src/e2r/sector/archetypes.py src/e2r/sector/round287_r5_loop14_consumer_retail_brand_price_validation.py src/e2r/cli/build_round287_r5_loop14_report.py tests/test_round287_r5_loop14_consumer_retail_brand_price_validation.py
PYTHONPATH=src python -m unittest tests.test_round287_r5_loop14_consumer_retail_brand_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round287_r5_loop14_report
```

현재까지 round-specific 테스트는 통과했다.

## What Not To Change

- Stage 3-Green threshold를 낮추지 않는다.
- K-food/K-beauty/tourism/JV headline만으로 Green을 만들지 않는다.
- 케이스 레코드를 후보 생성 입력으로 쓰지 않는다.
- 전체 OHLC가 없는 구간의 MFE/MAE를 만들지 않는다.
- 투자 권고 문구를 만들지 않는다.
