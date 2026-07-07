# Goal4 Full Bounded Self-Repair Result - 2026-07-08

작성 시점: 2026-07-08 KST

이 문서는 research-memory symbol support provenance 패치 이후 실제 bounded runtime self-repair를 한 번 돌린 결과를 기록한다.

## 실행

실행 명령:

```bash
PYTHONPATH=src python -m e2r.cli.run_research_to_runtime_parity_until_pass --as-of-date 2026-07-05 --max-iterations 2
```

child runtime attempt:

```text
output/census_v4/2026-07-05-research-to-runtime-parity-self-repair-01-20260707T173522Z
```

특징:

```text
seed event = 105개
planner run = 105개
source execution 포함 full bounded attempt
partial_run_invalid = false
child returncode = 1
stdout_tail = NOT_READY
```

쉬운 예:

```text
이번 실행은 "접수표만 만든 것"이 아니라
실제로 105개 follow-up 후보를 planner/source task까지 다시 돌린 것이다.
다만 결과가 아직 Goal4 통과는 아니다.
```

## 최종 상태

최신 parity audit:

```text
final_status = MEANINGFUL_RUNTIME_PARITY_NOT_READY
full_thesis_row_count = 6
distinct_full_thesis_archetype_count = 6
required_positive_missing_full_thesis_row_rate = 1.0
green_gap_full_thesis_row_rate = 1.0
```

남은 blockers:

```text
GREEN_GAP_ON_PROMOTED_ROWS
MANDATORY_ARCHETYPE_FULL_THESIS_ROW_MISSING
PRODUCTION_SCORE_PATH_IS_NOT_MEANINGFUL_FULL_THESIS_PASS
REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS
```

즉 이번 실행은 Goal4 완료가 아니다.

## 무엇이 좋아졌나

직전 mandatory missing:

```text
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
C15_MATERIAL_SPREAD_SUPERCYCLE
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

이번 mandatory missing:

```text
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
C24_BIO_TRIAL_DATA_EVENT_RISK
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

해석:

```text
C08은 source task executed no accepted claim 상태에서
PRODUCTION_FULL_E2R_SCORE_PATH_ONLY로 전진했다.

C15도 blocked candidate 상태에서
PRODUCTION_FULL_E2R_SCORE_PATH_ONLY로 전진했다.
```

하지만 둘 다 아직 meaningful pass가 아니다.

```text
C08:
  runtime_full_thesis_row_count = 1
  runtime_accepted_claim_count = 24
  required_positive_missing = 1
  green_gap = 1

C15:
  runtime_full_thesis_row_count = 1
  runtime_accepted_claim_count = 1
  required_positive_missing = 1
  green_gap = 1
```

쉬운 예:

```text
C08/C15는 시험지 제출까지는 성공했다.
하지만 필수 서류와 Green 서류가 아직 빠져 있어서 합격증은 아니다.
```

## 무엇이 여전히 막혔나

### C17

```text
runtime_parity_status = FULL_THESIS_BLOCKED_BY_REQUIRED_OR_GREEN_GAP
runtime_full_thesis_row_count = 0
runtime_accepted_claim_count = 3
source_lineage route_only_candidate_count = 4
```

의미:

```text
C17은 claim은 생겼지만 full thesis promotion이 required/green primitive gap에서 막혔다.
특히 미래에셋/BNK 등 report route lineage가 아직 route-only repair 후보로 남았다.
```

### C24

```text
runtime_parity_status = PLANNER_ATTEMPTED_BUT_NO_RUNTIME_SOURCE_CLOSURE
runtime_full_thesis_row_count = 0
runtime_source_task_execution_count = 0
target_symbol_mode = RESEARCH_MEMORY_TARGET_CANDIDATE
target_symbols = 000100
```

의미:

```text
C24는 research memory로 000100 target 후보는 붙었지만
아직 bounded source task 실행으로 닫히지 않았다.
```

### C28

```text
runtime_parity_status = SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM
runtime_full_thesis_row_count = 0
runtime_accepted_claim_count = 0
runtime_source_task_execution_count = 48
```

의미:

```text
C28은 source task를 많이 실행했지만 accepted claim이 없다.
이번에는 신영증권 PDF route가 잡혔으나 primitive mapping이 accepted되지 않았다.
```

쉬운 예:

```text
C28은 서류를 여러 장 냈는데
"ARR/NRR/renewal을 직접 증명하는 문장"으로 인정된 서류가 아직 0개다.
```

## Next Attempt Plan 변화

최신 next-attempt summary:

```text
plan_row_count = 36
source_task_count = 108
seed_event_count = 108

target_symbol_mode_counts:
  SYMBOL_SPECIFIC = 32
  ARCHETYPE_LEVEL_DISCOVERY = 3
  RESEARCH_MEMORY_TARGET_CANDIDATE = 1

research_memory_supported_symbol_specific_archetype_count = 29
research_memory_supported_symbol_specific_task_count = 87
research_memory_target_materialized_archetype_count = 30
research_memory_target_materialized_task_count = 90
research_memory_target_candidate_task_count = 3
```

의미:

```text
C01~C32 대부분은 실제 symbol이 붙은 상태다.
29개는 research reverse case inventory가 symbol 선택 이유를 support한다.
C24는 이번에 별도 RESEARCH_MEMORY_TARGET_CANDIDATE로 남았다.
```

## 다음 작업

우선순위:

```text
1. C28 accepted claim 0 원인 분해
   - shinyoung.com broker PDF route
   - primitive_mapping_rejected: no_allowed_primitive_for_predicate
   - ARR/NRR/retention primitive와 실제 extracted predicate mismatch 확인

2. C17 required/green gap closure
   - route_only_candidate_count = 4
   - securities.miraeasset.com / bnkfn.co.kr report lineage repair
   - spread/utilization/raw_material_cost_risk 중 어떤 primitive가 promotion을 막는지 분리

3. C24 planner-only를 source task execution으로 전환
   - 000100 target 후보는 생겼지만 source_task_execution_count = 0
   - trial_quality_visible / binary_event_unresolved / approval_not_confirmed source route 생성 필요

4. C08/C15는 완료가 아니라 score-path-only 상태로 추적
   - required_positive_missing과 green_gap이 1.0인 동안 meaningful pass 금지
```

## 검증

관련 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests/test_all_archetype_next_attempt_plan.py \
  tests/test_all_archetype_runtime_parity_matrix.py \
  tests/test_research_to_runtime_parity_goal4.py \
  tests/test_research_reverse_case_extractor.py \
  tests/test_source_lineage_repair_audit.py -v
```

결과:

```text
33 tests OK
```

## 완료 판단

Goal4 완료 선언은 금지한다.

6개 질문 기준의 forensic 답변은 아래 문서에 최신 수치로 정리했다.

```text
docs/0705/goal4_full_thesis_six_question_final_audit_2026-07-05.md
```

현재 상태:

```text
MEANINGFUL_RUNTIME_PARITY_NOT_READY
```

이번 작업으로 증명된 것은:

```text
연구자료 기반 symbol support가 실제 bounded runtime attempt로 들어갔고,
C08/C15는 score path까지 전진했다.
```

아직 증명되지 않은 것은:

```text
C01~C32/C36 전체에 대해 accepted claim/full thesis/meaningful thesis parity가 완료됐다는 것.
```
