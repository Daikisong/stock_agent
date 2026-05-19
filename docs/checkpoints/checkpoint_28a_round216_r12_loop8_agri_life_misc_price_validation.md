# Checkpoint 28A Round 216 R12 Loop 8 Agri Life Misc Price Validation

## 목적

`docs/round/round_216.md`의 R12 농업·생활서비스·교육·스마트팜·이벤트성 식품·규제소비재 내용을 케이스 라이브러리용 calibration pack으로 구조화했다.

이 라운드는 production scoring 변경이 아니다. 예를 들어 코웨이 같은 렌탈 서비스는 반복 계정, churn, ARPU, OPM, FCF가 붙으면 Stage 3 후보가 될 수 있지만, 유명인 치킨 이벤트처럼 하루에 20~30% 움직인 사례는 매출과 마진 증거 전에는 `price_moved_without_evidence`로 남긴다.

## 반영 내용

- `EDUCATION_POLICY_EVENT`, `FOOD_SERVICE_EVENT_PREMIUM` canonical archetype을 추가했다.
- R12 Loop 8 전용 케이스 팩을 추가했다.
- R12 전용 shadow weight, Green gate, 4B/4C gate, 가격검증 필드를 산출한다.
- CLI `python -m e2r.cli.build_round216_r12_loop8_report`를 추가했다.
- 테스트로 case library가 scoring input이 아니라 calibration/evaluation material이라는 guardrail을 확인한다.

## 케이스 요약

| 케이스 | 분류 | 판단 |
|---|---|---|
| 코웨이 | success_candidate | 반복 렌탈 모델 후보. churn, ARPU, OPM, FCF, 가격경로 전 Green 보류 |
| 대동 / TYM | success_candidate | 농기계 수출 후보. dealer sell-through, 재고, farmer financing, FCF 전 Green 보류 |
| 메가스터디교육 | event_premium | 의대 정원 정책은 routing evidence. 실제 수강생/ARPU/OPM 전 Green 금지 |
| 교육·에듀테크 basket | 4b_watch | 스마트폰 금지 정책은 회사별 방향성이 달라 Stage 1 watch |
| Poultry basket | event_premium | 브라질 조류독감 수입 제한은 35일 이벤트. 완화 시 fade 가능 |
| Kyochon/chicken basket | overheat | 유명인 식사 이벤트와 +20~30% 주가 움직임은 evidence 없는 event premium |
| 스마트팜 basket | event_premium | 논문/정책보다 상업 설치, 유지보수 매출, unit economics 필요 |
| KT&G | success_candidate | 규제소비재 cashflow 후보. HNB/환원/volume/규제 리스크 확인 전 Green 보류 |

## Green Gate

R12에서 Green은 보수적으로 둔다.

- 필수: 반복매출 또는 반복구매, churn/retention 안정, ARPU 또는 가격전가, unit economics, cash conversion, 재고/채권 안정, 규제 리스크 통과, 가격경로
- 금지: 정책 뉴스만, 질병 이벤트만, 수입금지 이벤트만, 스마트팜 테마만, 농기계 수출 테마만, 유명인/바이럴 식품 이벤트만

쉬운 예시는 이렇다. `렌탈 계정 증가 + churn 안정 + ARPU 상승 + FCF 개선`은 구조적 증거가 될 수 있다. 반대로 `누가 치킨을 먹어서 치킨주가 하루 급등`은 매출과 마진이 확인되기 전에는 구조적 E2R이 아니다.

## 산출물

- `data/e2r_case_library/cases_r12_loop8_round216.jsonl`
- `data/sector_taxonomy/round216_r12_loop8_agri_life_misc_price_validation_audit.json`
- `output/e2r_round216_r12_loop8_agri_life_misc_price_validation/round216_r12_loop8_price_validation_summary.md`
- `output/e2r_round216_r12_loop8_agri_life_misc_price_validation/round216_r12_loop8_case_matrix.csv`
- `output/e2r_round216_r12_loop8_agri_life_misc_price_validation/round216_r12_loop8_green_gate_review.md`
- `output/e2r_round216_r12_loop8_agri_life_misc_price_validation/round216_r12_loop8_stage4b_4c_review.md`

## 검증

```bash
PYTHONPATH=src python -m unittest tests.test_round216_r12_loop8_agri_life_misc_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round216_r12_loop8_report
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
git diff --check
```

## 결론

Round 216은 R12 생활서비스·농업·교육 이벤트 묶음을 더 보수적으로 분리했다. 반복 서비스와 규제소비재는 후보로 남기되, 정책·질병·스마트팜 논문·유명인 이벤트는 Stage 3-Green으로 올리지 않는 기준을 명시했다.
