# Goal4 Next Runtime Attempt Mapping Collision Audit

작성일: 2026-07-07

## 결론

Goal4 전수 runtime parity를 진행하기 위해 다음 실행을 실제로 돌렸다.

```text
output root:
output/census_v4/2026-07-07-goal4-all-archetype-next-runtime-attempt

target gate:
full_thesis

seed input:
docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl

seed count:
111
```

결과는 완료가 아니라 `INVALID_PARTIAL_OUTPUT`이다.

```text
exception:
ValueError: mapping_id collision with different mapping: MAP-b4dea8afc76a6f94d13e
```

따라서 이 실행 output은 readiness, score, Stage 근거로 쓰면 안 된다.

쉬운 예:

```text
시험을 보다가 25번 문제 근처에서 답안지 번호가 충돌해 채점기가 멈췄다.
앞의 몇 문제 채점 흔적이 있더라도, 이 시험 전체를 합격 증거로 쓰면 안 된다.
```

## 실행에서 확인된 것

실패 전까지 확인된 사실:

```text
planner_runs = 111
real LLM planner success = 111
C15 planner gaps processed = 3 / 3
C24 planner gaps processed = 3 / 3
source execution reached run_index around 25
partial_run_invalid.json emitted
```

즉 이번 실패는 planner/provider 부재가 아니다.

```text
아닌 것:
LLM planner가 없어서 실패
seed가 C15/C24를 포함하지 않아서 실패
전수 planning이 시작되지 않아서 실패

맞는 것:
Evidence OS ledger의 primitive mapping id가 ACCEPTED/REJECTED 상태 차이를 구분하지 못해 실패
```

## 원인

기존 `PrimitiveMappingProposal.build()`는 mapping id를 다음 값으로 만들었다.

```text
claim_id
archetype_id
primitive_id
support_direction
```

하지만 ledger가 mapping identity를 비교할 때는 `mapping_status`도 material field로 본다.

```text
mapping_status = ACCEPTED
mapping_status = REJECTED
```

이 둘은 서로 다른 mapping이다.

그런데 기존 ID에는 status가 없었기 때문에 같은 claim이 같은 primitive에 대해 한 번은 `REJECTED`, 한 번은 `ACCEPTED`로 들어오면 같은 `MAP-*` ID가 생성됐다.

쉬운 예:

```text
같은 서류 번호 123번에
첫 번째 기록: "승인"
두 번째 기록: "반려"
가 동시에 들어온 상황이다.

서류 번호가 같으니 덮어쓰면 위험하고,
내용이 다르니 ledger가 멈춘 것이 맞다.
```

## 패치

수정 파일:

```text
src/e2r/agentic/evidence_os.py
tests/test_agentic_evidence_os.py
```

변경:

```text
mapping_id 구성요소에 mapping_status.value 추가
```

패치 후 ID 구성:

```text
claim_id
archetype_id
primitive_id
support_direction
mapping_status
```

의미:

```text
같은 claim/primitive라도 ACCEPTED와 REJECTED는 서로 다른 mapping id를 가진다.
같은 ACCEPTED mapping에서 rationale 또는 contract_rule_id만 다른 경우는 기존처럼 같은 id로 접힌다.
```

## 추가 테스트

추가한 회귀 테스트:

```text
test_mapping_id_separates_accepted_and_rejected_status
```

검증한 내용:

```text
같은 claim
같은 archetype
같은 primitive
같은 support_direction
다른 mapping_status
-> 서로 다른 mapping_id
-> ledger에 둘 다 append 가능
```

기존 테스트도 유지:

```text
test_mapping_id_ignores_llm_rule_and_rationale_noise
```

검증한 내용:

```text
같은 mapping_status에서 LLM rationale만 다르면 같은 mapping_id로 접힌다.
```

## 테스트 결과

직접 회귀 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_agentic_evidence_os.AgenticEvidenceOSTests.test_mapping_id_ignores_llm_rule_and_rationale_noise \
  tests.test_agentic_evidence_os.AgenticEvidenceOSTests.test_mapping_id_separates_accepted_and_rejected_status -v
```

결과:

```text
Ran 2 tests
OK
```

관련 운영 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_goal_required_audits \
  tests.test_full_thesis_score_path_not_meaningful_pass -v
```

결과:

```text
Ran 85 tests
OK
```

## Goal4 상태

이 패치는 Goal4 완료가 아니다.

현재 의미:

```text
전수 next-runtime attempt를 실제로 돌려봤다.
planner 111개는 real provider로 성공했다.
C15/C24도 planner 단계는 3개 gap 모두 들어갔다.
하지만 source execution 중 mapping ledger 충돌로 run이 invalid partial output이 됐다.
충돌 원인은 코드 패치로 제거했다.
```

다음 단계:

```text
1. 같은 111 seed full-thesis run을 다시 실행한다.
2. INVALID_PARTIAL_OUTPUT이 재발하지 않는지 확인한다.
3. source execution이 C15/C24까지 도달하는지 확인한다.
4. accepted claim / full thesis / meaningful evidence pass matrix를 다시 산출한다.
5. required-positive / Green gap이 남으면 점수 완료가 아니라 material gap으로 유지한다.
```

한 줄 결론:

```text
이번 턴에서 Goal4를 완료한 것이 아니라,
Goal4 전수 runtime 실행을 막던 Evidence OS mapping id 충돌 버그를 하나 제거했다.
```
