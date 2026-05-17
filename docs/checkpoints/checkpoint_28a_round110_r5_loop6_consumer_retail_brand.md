# Checkpoint 28A Round 110: R5 Loop 6 Consumer / Retail / Brand

`docs/round/round_110.md`의 R5 Loop 6 내용을 반영했다. 이번 라운드는 소비재·유통·브랜드에서 `잘 팔린다`, `미국에 입점했다`, `틱톡에서 떴다` 같은 신호를 구조적 Green 근거로 바로 쓰지 않도록 더 촘촘한 케이스팩과 RedTeam gate를 추가한 작업이다.

## 반영 내용

- `src/e2r/sector/round110_r5_loop6_consumer_retail_brand.py` 추가
- `src/e2r/cli/build_round110_r5_loop6_report.py` 추가
- `tests/test_round110_r5_loop6_consumer_retail_brand.py` 추가
- R5 Loop 6 canonical target 30개 정의
- case candidate 17개 정의
- `data/e2r_case_library/cases_r5_loop6_round110.jsonl` 생성
- `data/sector_taxonomy/score_weight_profiles_round110_r5_loop6_v6.csv` 생성
- `output/e2r_round110_r5_loop6_consumer_retail_brand/` 보고서 생성

## 신규 분리축

Round 110은 기존 R5를 다음처럼 더 세분화했다.

- `K_FOOD_VIRAL_BRAND_CULTURE`
- `K_BEAUTY_TARIFF_IMPORT_REVIEW`
- `BEAUTY_DEVICE_REGULATORY_SAFETY`
- `BEAUTY_FAST_PRODUCT_CYCLE_RISK`
- `ECOMMERCE_TRUST_SECURITY`
- `ECOMMERCE_SUPPLIER_MARGIN_QUALITY`
- `FAST_FASHION_IP_SUPPLIER_LITIGATION`
- `FAST_FASHION_PRODUCT_SAFETY_DSA`
- `DISCLOSURE_CONFIDENCE_CAP`

쉬운 예시:

- `Ulta 입점`은 Stage 2 근거가 될 수 있지만, sell-through와 재주문이 없으면 Green 근거가 아니다.
- `TikTok Shop 매출`은 좋은 힌트지만, CAC와 할인율이 높으면 OPM이 깨질 수 있다.
- `Buldak 수출 성장`은 강한 구조 후보지만, 단일제품 의존과 국가별 리콜은 항상 4B/4C overlay로 본다.

## 핵심 산출물

- `output/e2r_round110_r5_loop6_consumer_retail_brand/round110_r5_loop6_consumer_retail_brand_summary.md`
- `output/e2r_round110_r5_loop6_consumer_retail_brand/round110_r5_loop6_case_matrix.csv`
- `output/e2r_round110_r5_loop6_consumer_retail_brand/round110_r5_loop6_stage_date_plan.csv`
- `output/e2r_round110_r5_loop6_consumer_retail_brand/round110_r5_loop6_green_guardrails.md`
- `output/e2r_round110_r5_loop6_consumer_retail_brand/round110_r5_loop6_risk_overlays.md`
- `output/e2r_round110_r5_loop6_consumer_retail_brand/round110_r5_loop6_price_validation_plan.md`
- `output/e2r_round110_r5_loop6_consumer_retail_brand/round110_r5_loop6_price_fields.csv`

## 요약

- target_count: 30
- case_candidate_count: 17
- green_possible_count: 4
- watch_yellow_first_count: 12
- redteam_first_count: 14
- gate_only_target_count: 11
- production_scoring_changed: false
- case_records_are_candidate_generation_input: false

## 적용하지 않은 것

- production scoring 변경 없음
- StageClassifier threshold 변경 없음
- case record를 candidate generation input으로 사용하지 않음
- 수출액, sell-through, 재주문, 재고, 매출채권, CAC, stage price를 추정으로 채우지 않음

## 검증

실행:

```bash
PYTHONPATH=src python -m unittest tests.test_round110_r5_loop6_consumer_retail_brand -v
PYTHONPATH=src python -m e2r.cli.build_round110_r5_loop6_report
```

결과:

- Round 110 단위 테스트 통과
- Round 110 JSONL/CSV/Markdown 보고서 생성 완료
