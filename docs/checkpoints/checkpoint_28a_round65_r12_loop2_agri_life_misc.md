# Checkpoint 28A Round 65 R12 Loop-2 Agriculture / Life Services / Misc

Round 65 반영 범위는 R12 농업·생활서비스·기타의 2회차 보정이다.

핵심 원칙은 단순하다. `생활 필수`, `정책 수혜`, `질병 이벤트`, `AI 교육`, `무인화`, `규제 완화`라는 이름은 Stage 1 라우팅 신호일 수 있지만, 반복계약·반복매출·unit economics·판가전가·해지율·CAC·규제 승인 범위·FCF 전환이 없으면 Stage 3-Green 근거가 아니다.

## 추가 파일

- `src/e2r/sector/round65_r12_loop2_agri_life_misc.py`
- `src/e2r/cli/build_round65_r12_loop2_report.py`
- `tests/test_round65_r12_loop2_agri_life_misc.py`
- `data/e2r_case_library/cases_r12_loop2_round65.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round65_r12_loop2_v2.csv`
- `output/e2r_round65_r12_loop2_agri_life_misc/`

## 반영 내용

- R12 Loop-2 타깃 14개를 정리했다.
- `AGRI_DISEASE_EVENT_OVERLAY`, `AI_EDUCATION_DISRUPTION_OVERLAY`, `REGULATED_CONSUMER_APPROVAL_OVERLAY`를 gate-only RedTeam overlay로 추가했다.
- John Deere, Zoetis, Cal-Maine, Bowery, AppHarvest, Duolingo, Chegg, 2U, Coway, Whirlpool, Target, Juul, cannabis rescheduling 사례를 케이스 라이브러리 v2 보정 팩으로 기록했다.
- 수직농장 unit economics, 농기계 cycle/right-to-repair, 교육 AI disruption, 렌탈 churn, 키오스크 운영마찰, 규제형 소비재 approval scope를 가격 검증 필드로 확장했다.

## 쉬운 예시

스마트팜 회사가 “AI 농업”을 발표하면 Stage 1 신호는 된다. 하지만 `actual_order`, `capacity_utilization`, `unit_economics_margin`, `fcf_conversion`이 비어 있으면 Green이 아니다. Bowery와 AppHarvest처럼 에너지비와 CAPEX가 안 맞으면 오히려 4C 반례가 된다.

반대로 Coway 같은 렌탈 모델은 단순 생활가전 판매와 다르다. `rental_accounts`, `rental_churn`, `recurring_service_revenue_ratio`, `filter_service_revenue`가 확인되면 더 좋은 후보가 될 수 있다. 그래도 해지율과 해외 마진이 비어 있으면 Green으로 올리지 않는다.

## 적용 제한

- 생산 점수 로직은 바꾸지 않았다.
- 케이스 레코드는 후보 생성 입력이 아니다.
- Stage 3-Green 임계값을 낮추지 않았다.
- unit economics, 계약, CAC, churn, 규제 범위, stage price는 만들지 않았다.

## 산출물

CLI:

```bash
PYTHONPATH=src python -m e2r.cli.build_round65_r12_loop2_report
```

주요 산출물:

- `round65_r12_loop2_agri_life_misc_summary.md`
- `round65_r12_loop2_case_matrix.csv`
- `round65_r12_loop2_stage_date_plan.csv`
- `round65_r12_loop2_green_guardrails.md`
- `round65_r12_loop2_unit_economics_caps.md`
- `round65_r12_loop2_price_validation_plan.md`
- `round65_r12_loop2_price_fields.csv`

## 검증

```bash
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest tests.test_round65_r12_loop2_agri_life_misc -v
PYTHONPATH=src python -m unittest discover -s tests -v
```

최종 커밋 전 전체 테스트를 통과시킨다.
