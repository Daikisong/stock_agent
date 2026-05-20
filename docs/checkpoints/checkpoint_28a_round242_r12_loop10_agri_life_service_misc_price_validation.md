# Checkpoint 28A Round 242 R12 Loop 10 Agri Life Service Misc Price Validation

## 반영 내용

- `docs/round/round_242.md`의 R12 Loop 10 내용을 calibration-only 케이스팩으로 구조화했다.
- 신규 canonical archetype을 추가했다:
  - `HOME_LIVING_RENTAL_RECURRING`
  - `EDUCATION_POLICY_MEDICAL_QUOTA`
  - `EDTECH_AI_TEXTBOOK_POLICY_REVERSAL`
  - `CHILDCARE_DEMOGRAPHIC_POLICY_EVENT`
  - `AGRI_FOOD_INPUT_COST_SHOCK`
  - `FEED_GRAIN_INPUT_COST_4C`
  - `PET_WELFARE_POLICY_TRANSITION`
  - `FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM`
- 신규 CLI를 추가했다:
  - `PYTHONPATH=src python -m e2r.cli.build_round242_r12_loop10_report`
- production scoring과 candidate generation은 변경하지 않았다.

## 케이스 요약

| case | 판정 | 핵심 앵커 |
| --- | --- | --- |
| Coway recurring rental | 구조 후보 | 렌탈/서비스 반복매출 구조, 해외 법인 존재, 계정/churn/ARPU/FCF 미확인 |
| Medical quota education basket | policy watch | 의대정원 3,058명에서 2027년 3,548명, 2030년 3,871명 |
| AI textbook rollback / phone ban | 4C-watch | AI 교과서 보조자료화, 교실 기기 규제 2026-03 |
| Fertility / childcare policy | Stage 2 policy watch | 출산율 0.72에서 0.80, 혼인 +8.1%, 출생 +6.8% |
| Kimchi cabbage input shock | 4C-watch | 배추 3,000원에서 9,537원, 정부 24,000t 방출 |
| Feed wheat / livestock cost | 4C-watch | 65,000t tender no purchase, effective offer $300.50/t |
| Dog-meat ban / pet welfare | policy event | 지원 약 1,000억원, 약 50만 마리 전환, 마리당 최대 600,000원 |
| Kyochon / Cherrybro / Neuromeka | price_moved_without_evidence | Kyochon +20%, Cherrybro +30%, 매출 전환 미확인 |

## Green Gate 원칙

R12에서 Stage 3-Green은 “정책 수혜”, “출산율 반등”, “원재료 가격 상승”, “유명인 이벤트”가 아니다.

예: `의대정원 확대`는 교육주를 Stage 1/2 관심으로 보낼 수 있지만, 실제 수강생 증가, 반복 강좌, ARPU, OPM, 현금전환이 없으면 Green이 아니다.

필수 조건:

- 반복매출 또는 반복구매 확인
- churn / retention 안정
- ARPU 또는 가격전가 확인
- paid enrollment / utilization / service usage 확인
- unit economics 확인
- cash conversion 확인
- input cost pass-through 확인
- 재고·매출채권 안정
- 보조금 의존도 낮음
- 가격경로가 evidence 이후 따라옴

금지 패턴:

- 정책 뉴스만 있음
- 의대정원 headline만 있음
- AI textbook theme만 있음
- 출산율 반등만 있음
- pet-welfare policy만 있음
- 농산물 가격 spike만 있음
- celebrity food event만 있음

## 산출 파일

- `data/e2r_case_library/cases_r12_loop10_round242.jsonl`
- `data/sector_taxonomy/round242_r12_loop10_agri_life_service_misc_price_validation_audit.json`
- `output/e2r_round242_r12_loop10_agri_life_service_misc_price_validation/round242_r12_loop10_price_validation_summary.md`
- `output/e2r_round242_r12_loop10_agri_life_service_misc_price_validation/round242_r12_loop10_case_matrix.csv`
- `output/e2r_round242_r12_loop10_agri_life_service_misc_price_validation/round242_r12_loop10_shadow_weights.csv`
- `output/e2r_round242_r12_loop10_agri_life_service_misc_price_validation/round242_r12_loop10_stage4b_4c_review.md`

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m py_compile src/e2r/sector/archetypes.py src/e2r/sector/round242_r12_loop10_agri_life_service_misc_price_validation.py src/e2r/cli/build_round242_r12_loop10_report.py tests/test_round242_r12_loop10_agri_life_service_misc_price_validation.py
PYTHONPATH=src python -m unittest tests.test_round242_r12_loop10_agri_life_service_misc_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round242_r12_loop10_report
```

후속 전체 테스트는 커밋 전 최종 검증 단계에서 수행한다.

## 다음 작업

- R12는 반복서비스와 정책/이벤트가 섞여 있어, Green gate를 특히 보수적으로 둔다.
- Coway류 반복 렌탈은 계정 수, churn, ARPU, OPM/FCF, 가격경로를 백필해야 한다.
- 교육/돌봄/펫 정책은 실제 유료수요와 회사 단위 매출 전환 전까지 Stage 1/2 또는 event premium으로 유지한다.
- 배추·사료곡물 input-cost shock은 pass-through와 margin 안정이 없으면 RedTeam/4C-watch로 유지한다.
