# Checkpoint 28A Round 268: R12 Loop 12 Agri / Life-Service / Misc Price Validation

## 반영 범위

`docs/round/round_268.md`의 라운드 196 내용을 케이스 라이브러리 보정 자료로 구조화했다. 이번 패치는 production scoring, StageClassifier, candidate generation을 바꾸지 않는다.

쉬운 예시: `의대정원 확대` 뉴스는 교육주 가격을 움직일 수 있지만, 실제 유료수강 전환, ARPU, 반복수강 매출, OPM, 현금전환이 확인되기 전에는 Stage 3-Green 증거가 아니다.

## 추가된 아키타입

- `K_FOOD_EXPORT_CAPACITY_RECURRING_CONSUMPTION`
- `EDUCATION_POLICY_MEDICAL_QUOTA_EVENT`
- `EDTECH_POLICY_ROLLBACK_4C`
- `CHILDCARE_FOREIGN_HELPER_POLICY_EVENT`
- `PET_WELFARE_TRANSITION_POLICY_EVENT`

## 케이스 팩

생성 경로:

- `data/e2r_case_library/cases_r12_loop12_round268.jsonl`
- `data/sector_taxonomy/round268_r12_loop12_agri_life_service_misc_price_validation_audit.json`
- `output/e2r_round268_r12_loop12_agri_life_service_misc_price_validation/`

케이스 8개:

- 농심 신라면 수출/CAPA: Stage 2 후보, Green 보류
- 배추·김치 원가 shock: 4C-watch
- 사료밀·축산 원가 shock: 4C-watch
- 의대정원 교육 이벤트: event premium
- AI 교과서 정책 rollback: 4C-watch
- 외국인 가사관리사·출산율 정책: Stage 2 후보, Green 보류
- 개식용 금지·펫 전환 정책: event premium
- 젠슨 황 치킨 이벤트: price_moved_without_evidence / 4B-watch

## 가드레일

- 케이스는 보정/검증용이며 후보 생성 입력이 아니다.
- shadow weight는 리포트용이며 production scoring에 적용하지 않는다.
- K-food, 교육, 돌봄, 펫, 외식 이벤트 headline만으로 Green을 만들지 않는다.
- OHLC, peak, MFE, MAE가 없으면 값을 만들지 않고 `price_data_unavailable_after_deep_search`로 남긴다.

## 검증

- 새 테스트: `tests/test_round268_r12_loop12_agri_life_service_misc_price_validation.py`
- CLI: `PYTHONPATH=src python -m e2r.cli.build_round268_r12_loop12_report`

## 다음 단계

Round 268은 생활서비스/식품/교육/펫 이벤트가 왜 Green이 아니라 watch 또는 event premium인지 분리하는 자료다. 이후 라운드에서도 같은 방식으로 `가격이 움직인 이유`와 `EPS/FCF로 닫힌 증거`를 나눠야 한다.
