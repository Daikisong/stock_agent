# Checkpoint 28A Round 248: R5 소비재/유통/브랜드 가격경로 검증

## 목적

`docs/round/round_248.md`의 R5 Loop 11 내용을 calibration/evaluation 전용 데이터팩으로 반영했다. 이번 라운드는 K-food, K-beauty, 이커머스, 관광/면세 리테일을 한 묶음으로 보되, 단순 브랜드 열기나 정책 이벤트를 Stage 3-Green으로 오해하지 않도록 Green gate와 4B/4C 감시축을 명시하는 작업이다.

쉬운 예시는 이렇다. `중국 단체관광 무비자` 뉴스로 면세점 주가가 하루 오를 수는 있지만, 관광객 지출, 면세 매출, OPM, FCF가 확인되기 전에는 Stage 3-Green 증거가 아니라 event premium이다.

## 반영 파일

- `src/e2r/sector/round248_r5_loop11_consumer_retail_brand_price_validation.py`
- `src/e2r/cli/build_round248_r5_loop11_report.py`
- `tests/test_round248_r5_loop11_consumer_retail_brand_price_validation.py`
- `data/e2r_case_library/cases_r5_loop11_round248.jsonl`
- `data/sector_taxonomy/round248_r5_loop11_consumer_retail_brand_price_validation_audit.json`
- `output/e2r_round248_r5_loop11_consumer_retail_brand_price_validation/`

## 추가/확인한 Archetype

- `K_FOOD_EXPORT_RECURRING`
- `K_FOOD_GLOBAL_STAPLE_BRAND`
- `K_FOOD_INPUT_PACKAGING_4C`
- `K_BEAUTY_DEVICE_GLOBAL_BRAND`
- `K_BEAUTY_INDIE_BRAND_US_CHANNEL`
- `K_BEAUTY_ODM_DISTRIBUTOR_LEVERAGE`
- `LEGACY_BEAUTY_CHINA_EXPOSURE_4C`
- `ECOMMERCE_JV_SCALE_AND_DATA_GATE`
- `ECOMMERCE_TRUST_BREACH_HARD_4C`
- `TOURISM_RETAIL_DUTYFREE_EVENT`
- `PRICE_ONLY_RALLY`
- `EVENT_PREMIUM`

## 케이스 요약

- 총 케이스: 8
- structural_success: 2
- success_candidate: 2
- overheat: 1
- event_premium: 1
- failed_rerating: 1
- hard_4C reference: 1
- dated Stage 3 케이스: 1
- Stage 4B-watch 케이스: 6
- 4C-watch/reference 케이스: 3
- full OHLC 완료: false
- price validation 상태: `partial_with_reported_price_anchors`

주요 케이스는 삼양식품, 농심, APR/메디큐브, d'Alba/Silicon2/Cosmax/Kolmar basket, 아모레퍼시픽/LG생활건강, 이마트/신세계-Alibaba JV, Coupang breach reference, 관광/면세 리테일 이벤트다.

## Green Gate

R5 Stage 3-Green은 `K-food`, `K-beauty`, `tourism policy`, `e-commerce JV`라는 이름표만으로 부여하지 않는다. 필요한 필드는 다음이다.

- 반복수요 확인
- 해외 매출 mix 증가
- 채널 sell-through 확인
- 오프라인 매장 sell-through 확인
- ASP 또는 product mix 개선
- OPM 또는 FCF 개선
- 재고와 매출채권 품질
- 관세/포장재/input shock 통과
- 고객 데이터 또는 플랫폼 신뢰 gate 통과
- 증거 이후 가격경로 확인

반대로 TikTok viral, 입점 논의, 상장/데뷔 급등, 관광정책 단독, JV headline 단독, 중국 부진 미상쇄, 단일 제품 스토리, data breach는 Green 금지 또는 RedTeam 입력이다.

## 4B/4C 판단

4B-watch는 다음처럼 “가격이 먼저 간” 상태를 감시한다.

- Stage 3 이후 2~4배 rerating
- 상장/데뷔 후 1개월 내 급등
- 단일 SKU/단일 device 집중
- 미국 상장 기대가 sell-through보다 먼저 가격에 반영
- 관광정책 basket rally
- JV/data scale headline rally

Hard 4C gate는 식품 recall, 포장재/input shortage, tariff margin squeeze, channel stuffing, inventory/receivables 악화, data breach, platform trust break, GMV/user spending deterioration 등이다.

## 산출물

- `round248_r5_loop11_price_validation_summary.md`
- `round248_r5_loop11_case_matrix.csv`
- `round248_r5_loop11_target_aliases.csv`
- `round248_r5_loop11_score_adjustments.csv`
- `round248_r5_loop11_shadow_weights.csv`
- `round248_r5_loop11_deep_sub_archetypes.csv`
- `round248_r5_loop11_price_validation_fields.csv`
- `round248_r5_loop11_green_gate_review.md`
- `round248_r5_loop11_price_validation_plan.md`
- `round248_r5_loop11_stage4b_4c_review.md`

## 검증

실행 명령:

```bash
PYTHONPATH=src python -m e2r.cli.build_round248_r5_loop11_report
PYTHONPATH=src python -m unittest tests.test_round248_r5_loop11_consumer_retail_brand_price_validation -v
```

전체 검증은 커밋 전 `compileall`, 전체 unittest, `git diff --check`로 확인했다.

## 변경하지 않은 것

- production scoring 변경 없음
- candidate generation 입력으로 사용하지 않음
- Stage 3-Green threshold 완화 없음
- full OHLC나 stage price를 임의 생성하지 않음
- 투자 권고 문구 없음

이번 라운드는 점수 엔진을 바꾼 것이 아니라, 나중에 R5 소비재/유통/브랜드 scoring을 설계할 때 쓸 검증용 케이스와 gate를 추가한 것이다.
