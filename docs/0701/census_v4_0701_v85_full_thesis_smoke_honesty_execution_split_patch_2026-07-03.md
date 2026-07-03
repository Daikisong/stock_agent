# Census v4 0701 v85 Full Thesis Smoke Honesty / Execution Split Patch

작성일: 2026-07-03

기준 실행물:

```text
artifact_truth_version = v82
latest reviewed output = output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v82
code_guard_patch_version = v83
this patch direction = v85 smoke honesty/execution split
```

## 1. 결론

현재 0701 Census v4 산출물에는 Stage row가 있다.

하지만 운영에 쓸 수 있는 FULL_THESIS / FULL_E2R Stage는 아직 없다.

```text
Stage row 자체 = 3,391개
Stage0이 아닌 표시 row = 85개
stage_scope:
  CENSUS_EVENT_BOARD = 3,390
  BRAIN_WEB_PARTIAL = 1
  FULL_THESIS = 0

operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3,391

operator_score_use:
  NOT_FULL_E2R_SCORE = 3,391

FULL_E2R_100 verified score row = 0
```

쉬운 예:

```text
출석부에는 이름이 3,391명 있다.
쪽지시험 점수처럼 보이는 표시도 85명 있다.
하지만 최종 성적표에 올라간 학생은 0명이다.
```

따라서 "stage가 있는 애들이 있긴 해?"에 대한 정확한 답은:

```text
있다 = 상태판/부분 평가 Stage row는 있다.
없다 = 운영용 FULL_THESIS/FULL_E2R 최종 Stage는 아직 0개다.
```

## 2. 이번에 발견한 추가 문제

기존 `FULL_THESIS_SMOKE_PASS`라는 표현이 두 의미를 섞고 있었다.

```text
의미 A:
  아직 full-thesis 실행은 안 됐지만,
  event-board 점수나 pending 상태를 운영 Stage처럼 속이지는 않았다.

의미 B:
  source task -> accepted claim -> primitive -> score contribution -> StageCourt
  경로가 실제로 닫혀 삼성전자/하이닉스 FULL_THESIS smoke가 통과했다.
```

이 둘은 완전히 다르다.

쉬운 예:

```text
시험지를 아직 채점하지 않았다.
  -> "채점 전"이라고 솔직히 말하면 honesty는 pass다.

시험지를 채점했고 점수 근거까지 확인됐다.
  -> execution pass다.

"채점 전"을 "채점 완료"라고 부르면 실패다.
```

## 3. 패치 목표

이번 패치는 READY를 만드는 패치가 아니다.

목표는:

```text
1. pending을 성공으로 오해하지 않게 한다.
2. controlled smoke와 production full-thesis를 계속 분리한다.
3. goal completion이 execution 없이 true가 되지 못하게 한다.
4. 다음 에이전트가 "어디서 막혔는지" 한눈에 보게 한다.
```

## 4. 새 의미 체계

### 4.1 FULL_THESIS_SMOKE_HONESTY_PASS

뜻:

```text
삼성전자/하이닉스 full-thesis smoke가 아직 실행되지 않았더라도,
그 상태를 운영 Stage나 FULL_E2R 점수로 둔갑시키지 않았다.
```

필요 조건:

```text
verdict in {FULL_THESIS_SMOKE_PASS, PENDING_FULL_THESIS_REFRESH}
score_allowed_before_execution == False
hardcoded_query_count == 0
daily_event_and_full_thesis_separated == True
```

쉬운 예:

```text
삼성전자는 CENSUS_EVENT_BOARD에서 Stage1처럼 보인다.
하지만 full_thesis_stage는 FULL_THESIS_NOT_RUN이다.
operator_stage_use도 NOT_FULL_THESIS_STAGE다.
이러면 honesty pass다.
```

### 4.2 FULL_THESIS_SMOKE_EXECUTION_PASS

뜻:

```text
삼성전자/하이닉스 full-thesis smoke가 claim-backed FULL_E2R 경로로 실제 통과했다.
```

필요 조건:

```text
verdict == FULL_THESIS_SMOKE_PASS
full_thesis_status == FULL_THESIS_REFRESH_RAN
per_symbol[*].smoke_pass_allowed == True
```

`smoke_pass_allowed`는 각 symbol에서 아래를 요구한다.

```text
stage_scope == FULL_THESIS
score_scale == FULL_E2R_100
full_thesis_score_valid_status == FINAL
full_thesis_accepted_claim_ids 존재
full_thesis_score_contribution_ids 존재
full_thesis_stagecourt_trace_ids 존재
full_thesis_missing_primitives == []
```

쉬운 예:

```text
SK하이닉스 HBM sold-out claim,
capacity allocation primitive,
score contribution,
StageCourt trace가 모두 연결됐다.
그때만 execution pass다.
```

## 5. 코드 패치 내용

패치 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_full_thesis_smoke_tasks.py
tests/test_census_v4_goal_required_audits.py
```

추가된 helper:

```text
_full_thesis_smoke_honesty_pass(full_thesis)
_full_thesis_smoke_execution_pass(full_thesis)
```

추가된 smoke artifact 필드:

```text
full_thesis_smoke_honesty_pass_allowed
full_thesis_smoke_execution_pass_allowed
full_thesis_smoke_honesty_status
full_thesis_smoke_execution_status
```

추가된 readiness verdict 필드:

```text
full_thesis_smoke_honesty_pass
full_thesis_smoke_execution_pass
```

추가된 goal completion 필드:

```text
full_thesis_smoke_honesty_pass_allowed
full_thesis_smoke_execution_pass_allowed
full_thesis_smoke_summary
```

추가된 goal matrix gate:

```text
FULL_THESIS_SMOKE_HONESTY_PASS
```

기존 `FULL_THESIS_SMOKE_PASS`는 유지하지만, 의미를 execution pass로 고정했다.

```text
FULL_THESIS_SMOKE_PASS =
  controlled Samsung/Hynix full-thesis wiring smoke executed with claim-backed FULL_E2R evidence
```

## 6. blocker 변경

기존 호환 blocker:

```text
full_thesis_smoke_pending
```

새 명시 blocker:

```text
full_thesis_smoke_execution_pending
full_thesis_smoke_honesty_false
```

정상 pending이면:

```text
full_thesis_smoke_honesty_false 없음
full_thesis_smoke_pending 있음
full_thesis_smoke_execution_pending 있음
```

즉:

```text
정직하게 "아직 안 했다" = honesty pass
그래도 "했다"는 아님 = execution pending
```

## 7. v82/v83 상태에 적용하면

현재 최신 reviewed 상태는 다음처럼 해석해야 한다.

```text
FULL_THESIS_SMOKE_HONESTY_PASS = true로 볼 수 있음
FULL_THESIS_SMOKE_EXECUTION_PASS = false
FULL_THESIS_SMOKE_PASS = false
goal_completion_ready = false
```

예:

```text
삼성전자:
  CENSUS_EVENT_BOARD row 있음
  event_evidence_score 있음
  full_thesis_score 없음
  operator_stage_use = NOT_FULL_THESIS_STAGE
  결론 = 운영 Stage 아님

SK하이닉스:
  BRAIN_WEB_PARTIAL row 있음
  event_evidence_score = 60.0
  missing C06 primitives 있음
  score_scale != FULL_E2R_100
  결론 = 운영 Stage 아님
```

## 8. 검증

좁은 회귀:

```bash
PYTHONPATH=src python -m unittest tests.test_census_v4_full_thesis_smoke_tasks tests.test_census_v4_goal_required_audits -v
```

결과:

```text
Ran 15 tests in 32.530s
OK
```

census v4 전체 회귀:

```bash
PYTHONPATH=src python -m unittest discover -s tests -p 'test_census_v4_*.py' -v
```

결과:

```text
Ran 139 tests in 80.991s
OK
```

전체 기본 테스트:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5122 tests in 239.197s
OK
```

주의:

```text
처음 넓은 테스트를 돌릴 때 모듈명을 잘못 만들어 import error가 났다.
그건 코드 실패가 아니라 `tests.` prefix가 빠진 잘못된 테스트 명령이었다.
위 discover 명령이 실제 검증 결과다.
```

## 9. 리뷰어가 공격해야 할 지점

다음 에이전트는 아래를 강하게 봐야 한다.

```text
1. FULL_THESIS_SMOKE_HONESTY_PASS가 너무 느슨하지 않은가?
2. score_allowed_before_execution이 누락된 legacy dict를 pass로 보는 호환 로직이 위험하지 않은가?
3. goal_completion_ready가 execution pass 없이 true가 될 수 있는 다른 경로가 남아 있지 않은가?
4. target_gate=full_thesis_smoke가 production/meaningful gate를 우회하지 않는가?
5. controlled smoke row가 production FULL_THESIS row로 계산되는 경로가 남아 있지 않은가?
6. acceptance_report와 readiness_verdict가 같은 의미를 말하는가?
7. self_repair의 deferred blocker가 "정직한 pending"과 "실행 실패"를 구분하는가?
```

2번은 v85 작성 시점의 남은 취약점이었다.

이 취약점은 v86에서 닫았다.

```text
legacy minimal dict:
  {"verdict": "PENDING_FULL_THESIS_REFRESH"}

v85 helper는 이것을 honesty pass로 볼 수 있었다.
v86 helper는 더 이상 이것을 honesty pass로 보지 않는다.

필수 field:
  score_allowed_before_execution
  hardcoded_query_count
  daily_event_and_full_thesis_separated

이 셋 중 하나라도 없으면 full_thesis_smoke_honesty_false다.
```

v86에서 바뀐 원칙:

```text
full field가 없는 smoke artifact는 HONESTY_UNKNOWN 또는 HONESTY_FAIL로 내려야 한다.
```

현재 구현은 `full_thesis_smoke_honesty_false` blocker로 내려간다.

## 10. 남은 실제 작업

이번 패치 후에도 운영 READY가 아니다.

남은 핵심:

```text
1. FULL_THESIS refresh queue 85개를 Research Brain이 실제 consume해야 한다.
2. LLM planner real-provider success가 있어야 한다.
3. bounded official-first SourceTask가 실행되어야 한다.
4. fetched document -> anchor -> accepted claim이 생겨야 한다.
5. accepted claim -> primitive state -> score contribution -> StageCourt trace가 닫혀야 한다.
6. production FULL_THESIS row가 생겨야 한다.
7. all-archetype source-backed replay가 6/32에서 32/32로 올라가야 한다.
```

쉬운 예:

```text
지금은 "삼성전자도 최종채점 필요"라는 작업표가 있다.
하지만 실제로 삼성전자 IR/DART/뉴스를 bounded source task로 가져와
HBM primitive를 채우고 StageCourt까지 닫은 상태는 아니다.
```

## 11. 최종 판단

이번 v85 패치는 다음을 고쳤다.

```text
기존:
  FULL_THESIS_SMOKE_PASS 하나로
  "정직한 pending"과 "실제 실행 성공"이 섞일 수 있었다.

변경:
  FULL_THESIS_SMOKE_HONESTY_PASS
  FULL_THESIS_SMOKE_EXECUTION_PASS
  두 축으로 분리했다.
```

그래서 앞으로는:

```text
honesty pass + execution pending
```

상태를 정확하게 표현할 수 있다.

하지만 이건 운영 Stage 생성이 아니다.

```text
v85 결론:
  거짓 READY 방지 패치 완료.
  FULL_THESIS 운영 Stage는 여전히 0개.
  다음 작업은 source acquisition -> accepted claim -> StageCourt 폐쇄다.
```
