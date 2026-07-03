# Census v4 0701 v86 Full-Field Smoke Honesty Guard Patch

작성일: 2026-07-03

기준:

```text
artifact_truth_version = v82
previous_guard_patch = v85
this_patch = v86
```

## 1. 결론

v85에서 `FULL_THESIS_SMOKE_HONESTY_PASS`와 `FULL_THESIS_SMOKE_EXECUTION_PASS`를 분리했다.

그런데 v85에는 아직 느슨한 지점이 있었다.

```text
legacy minimal dict:
  {"verdict": "PENDING_FULL_THESIS_REFRESH"}

또는 summary-only dict:
  {
    "verdict": "PENDING_FULL_THESIS_REFRESH",
    "full_thesis_smoke_honesty_pass_allowed": true
  }
```

이런 최소 결과는 "아직 안 했다" 정도만 말한다.

하지만 아래를 증명하지 못한다.

```text
score_allowed_before_execution == False
hardcoded_query_count == 0
daily_event_and_full_thesis_separated == True
```

따라서 v86에서는 full-field 증거가 없으면 honesty pass를 주지 않는다.

쉬운 예:

```text
"시험 아직 안 봄"이라고만 적힌 메모는 정직한 성적표가 아니다.
"시험 전이라 점수에 쓰지 않음, 문제 유출 없음, 중간 쪽지시험과 최종시험 분리됨"
까지 있어야 정직한 pending으로 인정한다.
```

## 2. 패치 내용

패치 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_goal_required_audits.py
```

강화한 helper:

```text
_full_thesis_smoke_honesty_pass(full_thesis)
_full_thesis_smoke_execution_pass(full_thesis)
```

## 3. 변경 전후

### v85 이전

```text
full_thesis_smoke_honesty_pass_allowed = True
```

같은 요약값이 있으면 helper가 그대로 믿을 수 있었다.

또 `score_allowed_before_execution`, `hardcoded_query_count`, `daily_event_and_full_thesis_separated`가 빠져도 legacy compatibility 때문에 pass가 될 수 있었다.

### v86 이후

요약값은 단독 증거가 아니다.

```text
full_thesis_smoke_honesty_pass_allowed = True
```

가 있어도 아래 원 필드가 모두 맞아야 한다.

```text
verdict in {FULL_THESIS_SMOKE_PASS, PENDING_FULL_THESIS_REFRESH}
score_allowed_before_execution is False
hardcoded_query_count == 0
daily_event_and_full_thesis_separated is True
```

하나라도 없거나 틀리면:

```text
full_thesis_smoke_honesty_false
```

blocker가 생긴다.

## 4. execution pass도 요약값 단독 신뢰 금지

v86에서는 execution 쪽도 더 엄격하게 했다.

```text
full_thesis_smoke_execution_pass_allowed = True
```

만으로는 부족하다.

아래가 모두 있어야 execution pass다.

```text
verdict == FULL_THESIS_SMOKE_PASS
full_thesis_status == FULL_THESIS_REFRESH_RAN
per_symbol is non-empty list
per_symbol[*].smoke_pass_allowed == True
```

쉬운 예:

```text
"채점 완료"라고 요약에 적혀 있어도,
삼성전자와 하이닉스 각각의 claim-backed 채점표가 없으면 execution pass가 아니다.
```

## 5. 테스트 보강

보강한 테스트:

```text
tests/test_census_v4_goal_required_audits.py
```

검증한 케이스:

```text
summary-only smoke:
  {
    "verdict": "PENDING_FULL_THESIS_REFRESH",
    "full_thesis_smoke_honesty_pass_allowed": true
  }

expected:
  full_thesis_smoke_honesty_false in deferred_goal_blockers
  full_thesis_smoke_execution_pending in deferred_goal_blockers
```

즉 요약값 조작만으로 goal/self-repair blocker를 지울 수 없다.

## 6. 검증

좁은 회귀:

```bash
PYTHONPATH=src python -m unittest tests.test_census_v4_full_thesis_smoke_tasks tests.test_census_v4_goal_required_audits -v
```

결과:

```text
Ran 15 tests in 32.978s
OK
```

census v4 전체:

```bash
PYTHONPATH=src python -m unittest discover -s tests -p 'test_census_v4_*.py' -v
```

결과:

```text
Ran 139 tests in 84.571s
OK
```

전체 기본 테스트:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5122 tests in 231.047s
OK
```

## 7. 현재 운영 truth는 변하지 않음

이 패치는 READY를 만드는 패치가 아니다.

```text
FULL_THESIS 운영 Stage = 0
FULL_E2R_100 verified score row = 0
goal_completion_ready = false
```

달라진 것은 하나다.

```text
이제 "summary만 있는 smoke audit"가 honesty pass로 위장할 수 없다.
```

## 8. 다음 에이전트가 공격해야 할 지점

아직 남은 공격 지점:

```text
1. full_thesis_smoke_honesty_pass_allowed explicit false는 즉시 false인데,
   explicit true는 원 필드 검증을 통과해야 한다. 이 정책이 모든 audit call site에 적용되는지 확인.

2. execution pass에서 per_symbol row가 충분히 atomic StageCourt 결과와 연결되는지 확인.

3. goal_completion_ready가 FULL_THESIS_SMOKE_EXECUTION_PASS 없이 true가 되는 다른 경로가 없는지 확인.

4. controlled smoke target gate가 meaningful/full_thesis production gate를 우회하지 않는지 확인.

5. v82 artifact truth와 v86 code guard truth를 문서에서 계속 분리하는지 확인.
```

## 9. 남은 실제 작업

아직 해야 할 운영 본작업:

```text
1. FULL_THESIS refresh queue를 Research Brain이 consume
2. real LLM planner success
3. bounded official-first SourceTask 실행
4. fetched document / anchor 생성
5. accepted claim 생성
6. primitive state / score contribution / StageCourt trace 폐쇄
7. production FULL_THESIS row 생성
8. all-archetype source-backed replay 32/32 달성
```

v86은 위 본작업을 끝낸 것이 아니라, 그 전 단계에서 거짓 완료를 막는 guard다.
