# Goal4 Research Memory Symbol Support Provenance - 2026-07-08

작성 시점: 2026-07-08 KST

이 문서는 Goal4 진행 중 `all_archetype_next_runtime_attempt_plan`에 추가한 research-memory symbol support provenance를 기록한다.

## 결론

Goal4는 아직 완료가 아니다.

이번 패치는 `C01~C32/C36 runtime parity`를 증명한 것이 아니라, 다음 runtime attempt 입력 장부에서 연구자료 기반 target symbol provenance가 사라지는 문제를 고친 것이다.

쉬운 예:

```text
이전 장부:
  C28 다음 검사 대상 = 012510
  그런데 012510을 왜 골랐는지 장부에 안 보임

이번 장부:
  C28 다음 검사 대상 = 012510
  연구자료 reverse case inventory의 C28 사례가 이 symbol을 support함
  단, 이 support는 점수 증거가 아니라 다음 검사의 접수 메모임
```

핵심 원칙은 그대로다.

```text
research_memory_symbol_support != score evidence
```

연구자료는 target 후보와 query intent를 도울 수 있지만, 점수와 Stage는 current source-backed Evidence OS accepted claim이 생긴 뒤에만 계산된다.

## 왜 필요했나

직전 산출물은 C08, C15, C17, C28 같은 row에 실제 symbol이 있었다.

예:

```text
C08 = 058470
C15 = 001390
C17 = 011170
C28 = 012510
```

하지만 plan summary는 다음처럼 보였다.

```text
research_memory_target_materialized_archetype_count = 0
research_memory_target_materialized_task_count = 0
```

이러면 다음 에이전트가 이렇게 오해할 수 있다.

```text
연구자료가 다음 runtime attempt에 하나도 연결되지 않았다.
```

실제 상태는 달랐다. 이미 status matrix에는 symbol이 들어와 있었지만, 그 symbol이 research reverse case inventory와 어떻게 연결되는지 plan row/source task에 보존하지 못했다.

## 이번 변경

코드:

```text
src/e2r/census/all_archetype_next_attempt_planner.py
```

추가한 개념:

```text
target_symbol_research_memory_support
research_memory_supported_symbol_specific_archetype_count
research_memory_supported_symbol_specific_task_count
```

의미:

```text
target_symbol_mode = SYMBOL_SPECIFIC
```

이어도, 해당 symbol이 research reverse case inventory에서 support되면 source task에 그 provenance를 남긴다.

단, 모든 row는 계속 다음 안전장치를 가진다.

```text
score_allowed_before_execution = false
stage_promotion_allowed_before_execution = false
score_evidence_allowed_from_research = false
```

## 재생성된 수치

명령:

```bash
PYTHONPATH=src python -m e2r.cli.run_research_to_runtime_parity_until_pass --as-of-date 2026-07-05
```

결과는 예상대로 아직 not ready다.

```text
final_status = MEANINGFUL_RUNTIME_PARITY_NOT_READY
```

새 next-attempt summary:

```text
plan_row_count = 35
source_task_count = 105
seed_event_count = 105

target_symbol_mode_counts:
  SYMBOL_SPECIFIC = 32
  ARCHETYPE_LEVEL_DISCOVERY = 3

research_memory_supported_symbol_specific_archetype_count = 29
research_memory_supported_symbol_specific_task_count = 87
research_memory_target_materialized_archetype_count = 29
research_memory_target_materialized_task_count = 87

source_lineage_repair_archetype_count = 6
source_lineage_retry_task_count = 18
```

해석:

```text
C01~C32 중 대부분은 다음 실행에 실제 symbol이 있다.
그중 29개는 research reverse case inventory가 왜 그 symbol을 다음 검사 후보로 삼는지 support한다.
하지만 이것은 증거가 아니라 다음 source-backed claim 수집을 위한 입력이다.
```

## Canary 확인

대표 row:

```text
C08  symbol = 058470  research support 있음
C15  symbol = 001390  research support 있음
C17  symbol = 011170  research support 있음
C28  symbol = 012510  research support 있음
```

C28 source task query intent는 이제 이런 식으로 시작한다.

```text
Research memory supports `012510` as a candidate target for
`C28_SOFTWARE_SECURITY_CONTRACT_RETENTION` ...
Treat this only as a target candidate ...
verify current, direct target-company evidence ...
```

즉 과거 C28 연구가 `012510`을 다음 검사 후보로 제안한 이유는 보존하지만, 그 연구 row 자체로 ARR/NRR/retention 점수를 주지는 않는다.

## 남은 Goal4 상태

아직 blocker는 그대로다.

```text
GREEN_GAP_ON_PROMOTED_ROWS
MANDATORY_ARCHETYPE_FULL_THESIS_ROW_MISSING
PRODUCTION_SCORE_PATH_IS_NOT_MEANINGFUL_FULL_THESIS_PASS
REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS
```

특히 아직 missing mandatory full-thesis row가 있다.

```text
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
C15_MATERIAL_SPREAD_SUPERCYCLE
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

따라서 이번 패치의 정확한 의미는 다음이다.

```text
완료 아님:
  C01~C32/C36 전체 runtime parity 증명 완료

완료한 진행:
  다음 runtime attempt에서 C05 외 아키타입이 어떤 연구자료 기반 symbol과 source task로 재시도되는지
  provenance를 잃지 않게 만들었다.
```

## 다음 작업

1. `C28` source-lineage feedback retry를 실제 bounded runtime attempt로 돌려 `012510`의 ARR/NRR/retention claim이 accepted claim으로 닫히는지 확인한다.
2. `C08`은 source route뿐 아니라 semantic/primitive mapping 실패를 분해한다.
3. `C15`는 spread/utilization/inventory bridge가 current source-backed claim으로 이어지는지 확인한다.
4. Goal4 완료 선언은 계속 금지한다.
