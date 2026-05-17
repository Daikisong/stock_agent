# Checkpoint 28A Round 52: R12 Agriculture / Life Services / Misc

## 목적

`docs/round/round_52.md` 내용을 R12 농업·생활서비스·기타 케이스팩으로 반영했다.

이번 라운드는 생산 점수 변경이 아니다. R12는 “작은 생활 테마”가 아니라 질병, 날씨, 곡물, 교육, 렌탈, 키오스크, 규제형 소비재에서 생기는 오탐을 줄이는 calibration 자료다.

쉬운 예:

- 스마트팜 뉴스가 나와도 실제 수주, 운영계약, 에너지비, unit economics, FCF가 없으면 Stage 3-Green이 아니다.
- 교육 앱은 사용자 증가보다 bookings, monetization, CAC, completion rate가 중요하다.
- 생활가전은 렌탈·필터·관리 반복매출이면 좋아질 수 있지만, 단순 하드웨어 교체수요는 주택경기와 소비 사이클에 묶인다.

## 추가된 코드

- `src/e2r/sector/round52_r12_agri_life_misc.py`
- `src/e2r/cli/build_round52_r12_report.py`
- `tests/test_round52_r12_agri_life_misc.py`

## 추가된 enum

`src/e2r/sector/archetypes.py`에 R12 canonical archetype을 추가했다.

- `SMART_FARM_AGRI_TECH`
- `AGRI_MACHINERY_PRECISION_CYCLE`
- `AGRI_LIVESTOCK_FOOD_COMMODITY`
- `FOOD_INPUT_REGULATED_CYCLE`
- `POLICY_LOCAL_SERVICE_THEME`

기존 `ANIMAL_HEALTH_BIOSECURITY`, `EDUCATION_SPECIALTY_SERVICES`, `HOME_CHILD_EDUCATION`, `HOME_LIVING_APPLIANCE_RENTAL`, `SERVICE_KIOSK_SELF_CHECKOUT`, `CONSUMER_REGULATED_PRODUCT`도 R12 score target으로 함께 사용한다.

## 산출물

- `data/e2r_case_library/cases_r12_round52.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round52_r12_v1.csv`
- `output/e2r_round52_r12_agri_life_misc/round52_r12_agri_life_misc_summary.md`
- `output/e2r_round52_r12_agri_life_misc/round52_r12_case_matrix.csv`
- `output/e2r_round52_r12_agri_life_misc/round52_r12_stage_date_plan.csv`
- `output/e2r_round52_r12_agri_life_misc/round52_r12_green_guardrails.md`
- `output/e2r_round52_r12_agri_life_misc/round52_r12_unit_economics_caps.md`
- `output/e2r_round52_r12_agri_life_misc/round52_r12_price_validation_plan.md`
- `output/e2r_round52_r12_agri_life_misc/round52_r12_price_fields.csv`

## 요약

- target_count: 11
- case_candidate_count: 15
- success_candidate_count: 5
- cyclical_success_count: 1
- event_premium_count: 1
- failed_rerating_count: 1
- stage4b_case_count: 2
- stage4c_case_count: 7
- green_possible_count: 0
- watch_yellow_first_count: 8
- redteam_first_count: 3
- production_scoring_changed: false
- case_records_are_candidate_generation_input: false

## 반영한 핵심 판단

R12에서 Green이 가능해지는 조건은 “생활 필수”가 아니라 반복성과 현금흐름이다.

- 스마트팜·수직농장: 실제 수주, 운영계약, unit economics, 에너지비, FCF 필요.
- 농기계·정밀농업: 기술 발표보다 농가소득, 금리, 장비 교체 사이클, software attach 확인 필요.
- 농축산·식품 원가 cycle: 계란·육계·사료·대두 가격 급등은 수익 기회가 될 수 있지만 대부분 cyclical success로 분리.
- 동물백신·방역: 조건부 승인과 정부 비축은 Stage 2 후보지만, one-off stockpile 리스크 유지.
- 교육·성인교육: B2B/B2G 반복계약, completion rate, student ROI, CAC, OPM 필요.
- 생활가전·렌탈: 렌탈 계정, 해지율, 필터·관리 반복매출, 해외 마진 확인 필요.
- 키오스크·셀프체크아웃: 설치대수보다 유지보수, 결제수수료, loss prevention 효과 확인 필요.
- 규제형 소비재: FDA/DEA 이벤트는 강한 Stage 1~2 신호가 될 수 있지만 허가 범위와 법적 충돌이 핵심.

## 생산 점수 영향

생산 scoring/staging/red-team 로직은 변경하지 않았다.

이번 파일들은 calibration/evaluation material이다. 예를 들어 `cases_r12_round52.jsonl`은 나중에 점수 가중치를 검증할 때 쓰는 참고 자료이지, 라이브 후보 생성 입력이 아니다.

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m e2r.cli.build_round52_r12_report
PYTHONPATH=src python -m unittest tests.test_round52_r12_agri_life_misc -v
```

결과:

- Round52 R12 테스트 11개 통과.

전체 테스트 결과는 최종 커밋 전 별도로 확인한다.
