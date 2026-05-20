# Checkpoint 28A Round 294 R12 Loop 14 Agriculture Life Services Misc Price Validation

## 반영 내용

- `docs/round/round_294.md`의 R12 Loop 14 농업·생활서비스·기타 가격경로 검증을 case-library 팩으로 반영했다.
- 새 calibration 전용 archetype 8개를 추가했다.
  - `AGRI_EQUIPMENT_EXPORT_CYCLE_4C_WATCH`
  - `AGRI_FOOD_INPUT_COST_4C_WATCH`
  - `FRIED_CHICKEN_MEME_EVENT_PREMIUM`
  - `FOOD_DELIVERY_CONSOLIDATION_STAGE2`
  - `DELIVERY_LABOR_SERVICE_CONTINUITY_REFERENCE`
  - `WASTE_RECYCLING_INFRA_STAGE2`
  - `DEMOGRAPHIC_CHILDCARE_STAGE2`
  - `PRIVATE_EDUCATION_HAGWON_STAGE2_4C`
- 케이스팩, shadow weight, green gate review, price-validation plan, 4B/4C review를 생성했다.
- production scoring, staging, candidate generation은 변경하지 않았다.

## 핵심 케이스

| case | 판정 | 핵심 해석 |
|---|---|---|
| Daedong / TYM | 4C-watch | 농기계 수출 thesis는 농가소득, dealer inventory, 수출 order, ASP/margin으로 닫혀야 한다. |
| 식품 원가 basket | 4C-watch | 쌀·귤·농수산물 가격 상승은 가격전가 전에는 pricing power가 아니라 margin gate다. |
| Kyochon / Cherrybro / Neuromeka | price_moved_without_evidence | Jensen Huang 치킨 이벤트는 주가를 움직였지만 동일점 매출·가맹 수수료 증거가 없다. |
| Naver / Uber / Baemin | Stage 2 candidate | 8T won bid headline보다 approval, take-rate, rider cost, merchant churn이 중요하다. |
| CJ Logistics / Hanjin / Coupang | service-continuity reference | 배송 moat는 빠른 배송뿐 아니라 노동·규제·운영 연속성으로 검증해야 한다. |
| Waste / recycling infra | Stage 2 + 4C-watch | EV와 인구권역은 강하지만 recycling yield, gate fee, cleanup liability가 Green gate다. |
| Birthrate / childcare | demographic Stage 2 | 출산율 0.80 반등은 의미 있지만 실제 고객수, ARPU, 보조금 capture, margin이 필요하다. |
| Hagwon / private education | demand Stage 2 + policy 4C-watch | 수요는 강하지만 인구감소, 가계부담, 규제 내구성이 동시에 gate다. |

## 산출물

- `data/e2r_case_library/cases_r12_loop14_round294.jsonl`
- `data/sector_taxonomy/round294_r12_loop14_agriculture_life_services_misc_price_validation_audit.json`
- `output/e2r_round294_r12_loop14_agriculture_life_services_misc_price_validation/round294_r12_loop14_price_validation_summary.md`
- `output/e2r_round294_r12_loop14_agriculture_life_services_misc_price_validation/round294_r12_loop14_case_matrix.csv`
- `output/e2r_round294_r12_loop14_agriculture_life_services_misc_price_validation/round294_r12_loop14_shadow_weights.csv`
- `output/e2r_round294_r12_loop14_agriculture_life_services_misc_price_validation/round294_r12_loop14_green_gate_review.md`
- `output/e2r_round294_r12_loop14_agriculture_life_services_misc_price_validation/round294_r12_loop14_stage4b_4c_review.md`

## 검증

```bash
PYTHONPATH=src python -m unittest tests.test_round294_r12_loop14_agriculture_life_services_misc_price_validation -v
PYTHONPATH=src python -m compileall -q src/e2r/sector/round294_r12_loop14_agriculture_life_services_misc_price_validation.py src/e2r/cli/build_round294_r12_loop14_report.py tests/test_round294_r12_loop14_agriculture_life_services_misc_price_validation.py src/e2r/sector/archetypes.py
PYTHONPATH=src python -m e2r.cli.build_round294_r12_loop14_report
```

## 해석

이번 라운드의 핵심은 “생활서비스 headline이 좋아 보인다”와 “E2R Stage 3-Green”을 분리하는 것이다.

예를 들어 `Jensen Huang이 치킨집에 갔다`는 이벤트는 Kyochon이나 Cherrybro 주가를 움직일 수 있다. 하지만 그 자체로 Kyochon의 동일점 매출, franchise fee, 닭고기 원가 spread, 반복수요가 좋아졌다는 증거는 아니다. 그래서 이 케이스는 `price_moved_without_evidence`로 남긴다.

마찬가지로 `출산율이 올랐다`는 것은 육아·교육 basket의 Stage 2 재료가 될 수 있지만, 실제 매출·고객수·ARPU·margin이 확인되기 전에는 Green으로 올리지 않는다.

## 변경하지 않은 것

- production scoring 변경 없음
- StageClassifier threshold 변경 없음
- candidate generation 입력 사용 없음
- direct KRX hard 4C 확정 없음
- full adjusted OHLC 또는 stage price를 임의 생성하지 않음
