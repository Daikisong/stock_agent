# Census v4 PrimitiveState Chain Audit

작성일: 2026-07-01

이 문서는 SourceTask ID-chain 다음에 남아 있던 중간 다리를 고정한다.

```text
accepted claim
-> primitive state
-> score contribution
-> AtomicStageDecision
-> representative census_stage_status row
```

## 결론

현재 canonical run 기준:

```text
primitive_state_chain_audit.json: PASS
critical_count: 0
primitive_state_count: 92
primitive_state_with_id_count: 92
primitive_mapping_count: 92
representative_score_claim_count: 67
representative_score_claim_with_primitive_state_count: 67
mapping_leaf_resolution_supported: true
representative_stage_row_with_evidence_chain_count: 67
```

즉 대표 event-board score claim 67개는 이제 primitive state까지 닫힌다.

쉬운 예:

```text
전에는 "숙제 제출 기록 -> 채점표 -> 성적표"는 맞췄지만,
"이 숙제가 어떤 문제 번호의 답인지"가 약했다.

지금은 "CLM-123 claim이 PRIM-456 primitive를 채우고,
그 primitive가 SCON-789 score contribution과 같은 대표 decision에 들어갔다"
까지 검사한다.
```

## 왜 필요했나

SourceTask v2 감사는 아래 chain을 닫았다.

```text
SourceTask
-> accepted claim
-> document
-> anchor
-> score contribution
-> StageCourt trace
-> representative row
```

하지만 중간의 `primitive_states.jsonl`가 약하면 이런 문제가 생긴다.

```text
claim은 계약 관련인데
primitive는 엉뚱하게 margin으로 열리고
score contribution은 visibility 점수에 들어가는 경우
```

이건 월덱스/삼성전자 같은 주체 오류와 형태는 다르지만, 본질은 같다.

```text
원문 사실이 어느 점수 칸에 들어갔는지 추적할 수 없으면
점수는 다시 흔들릴 수 있다.
```

## 이번 코드 패치

### 1. primitive_state_id 보강

파일:

```text
src/e2r/census/existing_ledger_loader.py
```

추가:

```text
primitive_state_id_for_row(...)
with_primitive_state_id(...)
```

기존 ledger refresh primitive row에 ID가 없으면 deterministic ID를 붙인다.

예:

```text
PRIM-1ba2d8a15795d81baf28
```

ID seed:

```text
symbol
primitive_id
status
support_claim_ids
counter_claim_ids
as_of_date
source_cutover_date
```

### 2. v4 copy 후 primitive row normalization

파일:

```text
src/e2r/census/census_runner_v4.py
```

추가:

```text
_primitive_rows_with_ids(...)
```

v3 leaf를 복사한 뒤에도 `primitive_states.jsonl`에 ID를 보강한다.

### 3. AtomicStageDecision에 primitive_state_ids 연결

파일:

```text
src/e2r/census/atomic_stage_decision.py
```

변경:

```text
build_atomic_stage_decisions(..., primitive_states=...)
```

accepted claim의 support primitive row를 찾아 `primitive_state_ids`에 넣는다.

### 4. representative census row에 primitive_state_ids 노출

파일:

```text
src/e2r/census/census_runner_v4.py
```

대표 row에 다음 필드가 생긴다.

```text
primitive_state_ids
blocked_primitive_state_ids
```

예:

```json
{
  "symbol": "000660",
  "accepted_claim_ids": ["CLM-14057362610ae62c7e02"],
  "score_contribution_ids": ["SCON-8da68431606c7699ece3"],
  "primitive_state_ids": ["PRIM-1ba2d8a15795d81baf28"],
  "atomic_stage_decision_id": "ATOMIC-cc4d4c6610353bea363b"
}
```

### 5. primitive_state_chain_audit 추가

파일:

```text
src/e2r/census/census_runner_v4.py
```

새 output:

```text
output/census_v4/2026-07-01/primitive_state_chain_audit.json
docs/operational/census_mode_v4_primitive_state_chain_audit.json
```

### 6. primitive_mappings leaf 추가

파일:

```text
src/e2r/census/census_runner_v4.py
```

새 output:

```text
output/census_v4/2026-07-01/primitive_mappings.jsonl
docs/operational/census_mode_v4_primitive_mappings.jsonl
```

현재 row count:

```text
primitive_mappings.jsonl: 92
```

역할:

```text
score_contribution.mapping_ids의 MAP-* 값이
accepted_claim_id, primitive_state_id, score_contribution_id를 실제로 가리키는지 보여준다.
```

## Audit Rule

대표 score row는 아래 조건을 모두 만족해야 한다.

```text
1. primitive_states.jsonl의 모든 row에는 primitive_state_id가 있다.
2. representative score claim은 적어도 하나의 primitive_state가 support해야 한다.
3. representative row의 primitive_state_ids는 실제 primitive_states.jsonl에 존재해야 한다.
4. representative row의 accepted_claim_ids는 primitive_state.support_claim_ids에 포함되어야 한다.
5. representative row의 primitive_state_ids와 AtomicStageDecision.primitive_state_ids가 같아야 한다.
6. score contribution에는 mapping_ids가 있어야 한다.
7. 모든 mapping_ids는 primitive_mappings.jsonl의 mapping_id로 resolve되어야 한다.
```

현재 critical counts:

```text
primitive_state_missing_id_count: 0
primitive_state_claim_id_not_found_count: 0
primitive_state_claim_primitive_mismatch_count: 0
primitive_mapping_missing_id_count: 0
primitive_mapping_claim_id_not_found_count: 0
primitive_mapping_state_id_not_found_count: 0
primitive_mapping_contribution_id_not_found_count: 0
representative_score_claim_without_primitive_state_count: 0
representative_stage_row_missing_primitive_state_ids_count: 0
representative_stage_primitive_id_not_found_count: 0
representative_stage_primitive_claim_set_mismatch_count: 0
atomic_decision_primitive_set_mismatch_count: 0
representative_score_contribution_missing_mapping_ids_count: 0
representative_score_mapping_id_not_found_count: 0
```

## Leaf Auditor 강화

`src/e2r/census/census_v4_auditor.py`에도 critical 항목을 추가했다.

새 critical keys:

```text
primitive_state_missing_id_count
primitive_state_id_not_found_count
scored_row_missing_primitive_state_ids
scored_claim_without_primitive_state_count
```

현재 `leaf_artifact_audit.json`도 critical 0으로 통과한다.

## 테스트

새 테스트 파일:

```text
tests/test_census_v4_primitive_state_chain.py
```

검증 내용:

```text
1. 현재 artifact의 representative primitive chain이 닫혀 있는지 확인
2. representative score claim에 primitive state가 없으면 FAIL
3. representative row에 primitive_state_ids가 없으면 FAIL
```

타깃 테스트:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_primitive_state_chain \
  tests.test_census_v4_source_task_satisfaction_chain \
  tests.test_census_v4_goal_required_audits -v

Ran 10 tests
OK
```

## 추가로 닫힌 점

이번 패치는 primitive state ID chain뿐 아니라 MAP-* mapping leaf도 닫는다.

현재 audit 값:

```text
mapping_leaf_resolution_supported: true
primitive_mapping_count: 92
```

뜻:

```text
score_contribution.mapping_ids가 존재하는지는 검사한다.
MAP-* ID가 primitive_mappings.jsonl row로 resolve되는지도 검사한다.
```

다음 refinement:

```text
live/Brain/Web/full thesis claim도 같은 mapping leaf chain을 통과시킨다.
대표 row 밖 25개 claim의 exclusion reason을 더 세분화한다.
```

## 이 PASS가 의미하지 않는 것

아래는 아직 아니다.

```text
live source acquisition pass
Brain/Web evidence pass
full thesis smoke pass
FULL_E2R_100 verified score
삼성전자/하이닉스 C06/HBM full thesis Stage
전 아키타입 Evidence Contract replay pass
```

현재 의미:

```text
ledger-refresh canonical run에서
대표 event-board score claim 67개는
claim -> primitive -> score -> atomic decision -> representative row까지 닫힌다.
```

한 줄로 정리:

> SourceTask 체인 다음의 primitive/mapping 체인도 대표 event-board score claim 67개 기준으로 닫혔다. 다만 live/full-thesis 실행은 아직 남아 있다.
