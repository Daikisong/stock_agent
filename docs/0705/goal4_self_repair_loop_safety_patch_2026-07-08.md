# Goal4 Self-Repair Loop Safety Patch - 2026-07-08

작성 시점: 2026-07-08 KST

이 문서는 Goal4 runtime parity self-repair CLI에 추가한 안전장치를 설명한다.

## 왜 패치했나

2026-07-07 실행에서 완료 attempt와 partial attempt가 섞일 수 있는 구조가 확인됐다.

```text
self-repair-01: COMPLETED
self-repair-02: RUNNING 상태에서 중단
```

문제는 parent CLI가 `meaningful_full_thesis_evidence_pass=false`를 보고, 코드나 source-route 수리 여부를 확인하지 않은 채 다음 child runtime을 바로 시작했다는 점이다.

쉬운 예:

```text
시험에서 필수 서류가 빠져 탈락했다.
그런데 서류를 보완하지 않고 같은 답안지를 다시 제출했다.
시간만 쓰고 결과는 거의 같다.
```

Goal4에서는 이게 위험하다. partial run이 남으면 나중에 어떤 output root가 증거인지 헷갈리고, 전수 matrix가 완료 산출물과 중단 산출물을 섞어 읽을 수 있다.

## 패치 내용

수정 파일:

```text
src/e2r/cli/run_research_to_runtime_parity_until_pass.py
src/e2r/census/all_archetype_runtime_execution_manifest.py
tests/test_research_to_runtime_parity_goal4.py
```

핵심 변경:

```text
1. child runtime이 KeyboardInterrupt 또는 returncode 130으로 끝나면 partial_run_invalid.json을 남긴다.
2. partial_run_invalid가 있는 output root는 readiness/score/stage/Goal4 evidence로 쓰면 안 된다고 명시한다.
3. parent self-repair CLI는 기본값에서 child runtime 1회 뒤에도 meaningful=false이면 반복 실행을 멈춘다.
4. 반복 실행이 정말 필요하면 --allow-repeated-runtime-attempts true를 명시해야 한다.
5. stop reason을 self_repair_stop_reason에 기록한다.
```

새 stop reason:

```text
SELF_REPAIR_REQUIRES_CODE_OR_SOURCE_ROUTE_REPAIR_AFTER_RUNTIME_ATTEMPT
RUNTIME_ATTEMPT_PARTIAL_OUTPUT_INVALID
RUNTIME_ATTEMPT_INTERRUPTED
```

## 이 패치가 해결하는 것

해결:

```text
같은 blocker를 그대로 둔 장시간 runtime 반복
partial output root를 완료 evidence처럼 오해하는 문제
KeyboardInterrupt 후 marker 없이 RUNNING 상태 파일만 남는 문제
```

해결하지 않는 것:

```text
C08/C28 accepted claim 0
C15 required/Green primitive gap
C06/C17 score path only 상태
전 C01~C32 meaningful runtime parity 미완료
```

즉 이 패치는 Goal4 완료 패치가 아니다. 다음 수리를 정확히 하기 위한 안전장치다.

## 현재 최신 Goal4 상태

2026-07-07 self-repair attempt 01 기준:

```text
final_status = MEANINGFUL_RUNTIME_PARITY_NOT_READY
full_thesis_row_count = 6
distinct_full_thesis_archetype_count = 6
required_positive_missing_full_thesis_row_count = 5
green_gap_full_thesis_row_count = 5
mandatory_archetype_full_thesis_missing = C08, C15, C28
```

분류:

```text
C24 = mandatory 중 row-level meaningful pass
C06/C17 = production score path only, required/Green gap 남음
C08/C28 = source task executed, accepted full-thesis claim 0
C15 = accepted claim은 있으나 required/Green gap 때문에 full thesis blocked
```

쉬운 예:

```text
C24는 서류가 붙은 답안지 1장이다.
C06/C17은 점수는 적혔지만 필수 첨부서류가 빠진 답안지다.
C08/C28은 검색은 했지만 채점 가능한 답안 문장을 못 만든 상태다.
C15는 답안 문장은 일부 있지만 졸업 조건에 필요한 핵심 문장이 빠진 상태다.
```

## 검증

실행한 테스트:

```bash
PYTHONPATH=src python -m unittest tests/test_research_to_runtime_parity_goal4.py -v

PYTHONPATH=src python -m unittest \
  tests/test_all_archetype_runtime_status_matrix.py \
  tests/test_all_archetype_runtime_parity_matrix.py \
  tests/test_all_archetype_next_attempt_plan.py \
  tests/test_all_archetype_runtime_execution_manifest.py \
  tests/test_research_to_runtime_replay_mandatory_archetypes.py \
  tests/test_meaningful_full_thesis_production_acceptance.py \
  tests/test_full_thesis_evidence_completion_split.py \
  tests/test_full_thesis_score_path_not_meaningful_pass.py \
  -v
```

결과:

```text
Goal4 parity tests: 11 passed
All-archetype linked tests: 35 passed
```

## 다음 작업

다음 패치는 runtime을 다시 오래 돌리는 것이 아니라, source/claim 실패 원인을 먼저 쪼개야 한다.

우선순위:

```text
1. C08 accepted claim 0 원인: source acquisition vs claim extraction vs primitive mapping 분해
2. C28 accepted claim 0 원인: ARR/RPO/renewal/retention bridge가 어느 단계에서 탈락했는지 확인
3. C15 blocked candidate 원인: pass-through -> realized spread -> OPM/FCF 사슬 중 빠진 primitive 확인
4. C06/C17 score path only 원인: required-positive/Green gap contribution ledger 확인
```

이 네 항목을 고친 뒤에만 다음 runtime attempt가 의미 있다.
