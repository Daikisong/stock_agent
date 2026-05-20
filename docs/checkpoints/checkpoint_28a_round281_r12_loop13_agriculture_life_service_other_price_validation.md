# Checkpoint 28A Round 281 R12 Loop 13 농업·생활서비스·기타 검증팩

## 요약

- 원문: `docs/round/round_281.md`
- analyst round id: `round_209`
- 대섹터: `AGRICULTURE_LIFE_SERVICE_OTHER`
- 케이스 수: 9
- production scoring 변경: false
- candidate generation input: false
- shadow weight only: true
- 가격 검증 상태: `partial_with_reported_price_anchors`
- full adjusted OHLC: false
- direct listed hard 4C: false

이번 라운드는 농식품, 사료·축산, 농기계, 물류, 생활서비스 trust, 폐기물, 저출산·교육, IPO 품질 게이트를 다룬다. 핵심은 “생활필수재”, “배추값 상승”, “출생률 반등”, “폐기물 정책”, “물류 제휴”, “IPO 대형주” 같은 headline을 Stage 3-Green으로 보지 않는 것이다.

쉬운 예로, 배추 도매가격이 한 포기 9,537원까지 올라도 식품기업의 이익이 좋아졌다는 뜻은 아니다. 판가 전가, 재고/폐기 관리, gross margin, 현금전환이 확인되기 전에는 원가율 4C-watch로 본다.

## 추가된 canonical archetype

- `FOOD_INFLATION_CLIMATE_INPUT_4C`
- `ANIMAL_FEED_GRAIN_COST_4C`
- `POULTRY_EGG_BIRD_FLU_SUPPLY_SHOCK`
- `AGRI_MACHINERY_LABOR_SUBSTITUTION_OPTIONALITY`
- `LIFE_SERVICE_LOGISTICS_CONTRACT_STAGE2`
- `ECOMMERCE_SERVICE_TRUST_HARD_REFERENCE`
- `WASTE_RECYCLING_INFRA_PLATFORM_STAGE2`
- `DEMOGRAPHIC_CHILDCARE_EDUCATION_POLICY_EVENT`
- `OTHER_MANUFACTURING_TOOLS_IPO_QUALITY_GATE`

## 케이스 반영

| case | 판정 |
|---|---|
| Kimchi cabbage / food-input inflation | 원가율 4C-watch |
| Feed wheat / livestock input cost | 사료·축산 margin 4C-watch |
| Poultry / egg supply shock | event premium + 질병/수입규제 4C-watch |
| Daedong / TYM agricultural machinery | success candidate, evidence insufficient |
| CJ Logistics / Shinsegae alliance | Stage 2 계약, price failed |
| Coupang data breach | 생활서비스 trust hard reference |
| Waste treatment / food-waste RFID | policy infra Stage 2 |
| Birthrate rebound / childcare-education | demographic Stage 2, company Green 아님 |
| DN Solutions IPO | IPO quality gate Stage 2 |

## Green 필수 확인

- input cost pass-through
- inventory / waste control
- gross margin stability
- feed cost hedge
- disease supply-chain resilience
- actual order backlog
- dealer sell-through
- logistics unit economics
- data trust and service continuity
- waste tipping fee and utilization
- enrolment, ARPU, retention
- post-listing order book and export margin
- cash conversion
- evidence 이후 price path

## 금지 패턴

- food inflation headline only
- grain price event only
- disease supply shock as benefit only
- aging farm theme only
- logistics revenue uplift without margin
- birthrate headline without enrolment
- recycling policy without tipping fee
- IPO size without aftermarket demand
- data breach or trust failure

## 산출물

- `data/e2r_case_library/cases_r12_loop13_round281.jsonl`
- `data/sector_taxonomy/round281_r12_loop13_agriculture_life_service_other_price_validation_audit.json`
- `output/e2r_round281_r12_loop13_agriculture_life_service_other_price_validation/round281_r12_loop13_price_validation_summary.md`
- `output/e2r_round281_r12_loop13_agriculture_life_service_other_price_validation/round281_r12_loop13_case_matrix.csv`
- `output/e2r_round281_r12_loop13_agriculture_life_service_other_price_validation/round281_r12_loop13_target_aliases.csv`
- `output/e2r_round281_r12_loop13_agriculture_life_service_other_price_validation/round281_r12_loop13_score_adjustments.csv`
- `output/e2r_round281_r12_loop13_agriculture_life_service_other_price_validation/round281_r12_loop13_shadow_weights.csv`
- `output/e2r_round281_r12_loop13_agriculture_life_service_other_price_validation/round281_r12_loop13_deep_sub_archetypes.csv`
- `output/e2r_round281_r12_loop13_agriculture_life_service_other_price_validation/round281_r12_loop13_price_validation_fields.csv`
- `output/e2r_round281_r12_loop13_agriculture_life_service_other_price_validation/round281_r12_loop13_green_gate_review.md`
- `output/e2r_round281_r12_loop13_agriculture_life_service_other_price_validation/round281_r12_loop13_price_validation_plan.md`
- `output/e2r_round281_r12_loop13_agriculture_life_service_other_price_validation/round281_r12_loop13_stage4b_4c_review.md`

## 검증

실행 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round281_r12_loop13_agriculture_life_service_other_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round281_r12_loop13_report
PYTHONPATH=src python -m compileall -q src tests
git diff --check
PYTHONPATH=src python -m unittest discover -s tests -v
```

현재 완료:

- 라운드 281 전용 단위 테스트 6개 통과
- CLI 산출물 생성 완료
- compileall 통과
- `git diff --check` 통과
- 전체 unittest 3,220개 통과

테스트 후 생성된 `__pycache__`는 커밋 전 정리했다.
