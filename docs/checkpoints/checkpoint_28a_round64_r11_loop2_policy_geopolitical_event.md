# Checkpoint 28A Round 64 R11 Loop-2 Policy / Geopolitical / Disaster / Event

Round 64 반영 범위는 R11 정책·지정학·재난·전염병·과학테마 이벤트의 2회차 보정이다.

핵심 원칙은 단순하다. 큰 뉴스는 Stage 1 라우팅 신호일 수 있지만, 계약·예산·정부주문·프로젝트 파이낸싱·공사착수·반복매출·EPS/FCF 전환으로 이어지지 않으면 Stage 3-Green 근거가 아니다.

## 추가 파일

- `src/e2r/sector/round64_r11_loop2_policy_geopolitical_event.py`
- `src/e2r/cli/build_round64_r11_loop2_report.py`
- `tests/test_round64_r11_loop2_policy_geopolitical_event.py`
- `data/e2r_case_library/cases_r11_loop2_round64.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round64_r11_loop2_v2.csv`
- `output/e2r_round64_r11_loop2_policy_geopolitical_event/`

## 반영 내용

- `EVENT_TO_CONTRACT_ESCALATION` 보조 타깃을 추가했다.
- `THEME_VALUATION_OVERHEAT`는 양의 점수가 아니라 `gate` 전용 RedTeam 오버레이로 기록했다.
- North Korea 정책 이벤트, 우크라 재건, 폭염/전력망, 전염병 stockpile, 진단키트 정상화, LK-99 재현 실패 케이스를 가격 검증 대기 케이스로 정리했다.
- MFE/MAE 5D/20D/60D/90D/180D와 계약·예산·주문·financing·VPP·복제실패 등 이벤트별 가격 검증 필드를 확장했다.

## 쉬운 예시

`as_of_date=2024-08-15`에 엠폭스 뉴스로 백신주가 급등했다면 이것은 Stage 1 이벤트 신호다. 하지만 `government_order`, `stockpile_contract`, `guide_up`이 비어 있으면 Stage 3-Green이 아니라 `event_premium`으로 남긴다.

반대로 정부 stockpile 계약과 가이던스 상향이 확인되면 Stage 2 후보가 될 수 있다. 그래도 반복 조달과 non-event 매출이 확인되기 전에는 구조적 Green으로 올리지 않는다.

## 적용 제한

- 생산 점수 로직은 바꾸지 않았다.
- 케이스 레코드는 후보 생성 입력이 아니다.
- Stage 3-Green 임계값을 낮추지 않았다.
- 계약, 예산, 가격, 주문량, guidance, stage price는 만들지 않았다.

## 산출물

CLI:

```bash
PYTHONPATH=src python -m e2r.cli.build_round64_r11_loop2_report
```

주요 산출물:

- `round64_r11_loop2_policy_geopolitical_event_summary.md`
- `round64_r11_loop2_case_matrix.csv`
- `round64_r11_loop2_stage_date_plan.csv`
- `round64_r11_loop2_green_guardrails.md`
- `round64_r11_loop2_event_false_positive_caps.md`
- `round64_r11_loop2_price_validation_plan.md`
- `round64_r11_loop2_price_fields.csv`

## 검증

```bash
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest tests.test_round64_r11_loop2_policy_geopolitical_event -v
PYTHONPATH=src python -m unittest discover -s tests -v
```

최종 커밋 전 전체 테스트를 통과시킨다.
