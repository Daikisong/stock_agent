# Census v4 Subagent Cross Validation Findings - 2026-07-01

이 문서는 0701 문서와 v4 패치를 독립 subagent 3명이 읽고 지적한 내용을 정리한 것이다.
파일 수정은 본 agent가 반영했고, subagent들은 read-only로 검토했다.

## 결론

```text
v4 핵심 숫자와 문서의 방향은 대체로 맞다.
하지만 Brain/Web readiness gate와 acceptance 문구는 더 세게 조여야 했다.
```

쉬운 예:

```text
전에는 "책을 가져왔다"는 카운터 숫자만 있어도 시험 통과처럼 보일 수 있었다.
이제는 책 row, 인용 위치 row, 답안 문장 row, 채점 row가 실제로 연결되어야 한다.
```

## 반영한 코드 패치

### 1. attempt count와 실제 leaf row 분리

지적:

```text
brain_web_attempt.source_task_execution_count = 1
brain_web_attempt.real_document_fetched_count = 1
```

같은 집계 숫자가 있어도 실제 아래 파일에 row가 없으면 pass가 되면 안 된다.

```text
source_task_executions.jsonl
evidence_documents.jsonl
accepted_claims.jsonl
evidence_anchors.jsonl
```

반영:

```text
attempt_source_task_execution_count
attempt_real_document_fetched_count
attempt_accepted_claim_count
```

를 별도 필드로 남기고, gate pass 판단용:

```text
source_task_execution_count
real_document_fetched_count
web_or_llm_accepted_claim_count
```

는 실제 Brain/Web origin leaf row 기준으로 계산한다.

새 blocker:

```text
Brain/Web source task attempt count has no exported source_task_executions rows
Brain/Web real document attempt count has no exported evidence_documents rows
Brain/Web accepted claim attempt count has no exported accepted_claims rows
```

### 2. document_id / anchor_id row resolve 강제

지적:

```text
accepted claim에 document_id="DOC-MISSING" 문자열만 있어도
실제 document/anchor row가 없어 pass될 수 있다.
```

반영:

```text
brain_claim_unresolved_document_ref_count
brain_claim_unresolved_anchor_ref_count
brain_source_task_without_document_ref_count
brain_source_task_unresolved_document_ref_count
```

를 추가했다.

새 blocker:

```text
accepted Brain/Web claims reference missing evidence_documents rows
accepted Brain/Web claims reference missing evidence_anchors rows
Brain/Web source task rows missing fetched document refs
Brain/Web source task rows reference missing evidence_documents rows
```

쉬운 예:

```text
답안지에 "3쪽 5줄 참고"라고 썼으면,
실제 책과 3쪽 5줄 표시가 장부에 있어야 한다.
문자열만 있으면 근거가 아니다.
```

### 3. attempt audit의 cutover 신호 보수화

지적:

```text
accepted_claim_count > 0
stagecourt_trace_exported_count > 0
```

만으로 `cutover_export_ready=true`가 될 수 있었다.
하지만 StageCourt trace는 내부 판정 장부일 뿐이고, representative `census_stage_status` row 승격과 다르다.

반영:

```text
cutover_export_ready = blockers가 하나도 없을 때만 true
```

또 accepted claim이 있으면 최소:

```text
brain_to_claim_trace_count > 0
stagecourt_trace_exported_count > 0
promoted_stage_row_count > 0
```

가 있어야 `ATTEMPTED_WITH_SOURCE_TASKS`가 가능하다.

## 반영한 테스트

추가/강화된 테스트:

```text
test_attempt_counts_without_exported_source_rows_are_blocked
test_brain_claim_missing_document_or_anchor_row_is_blocked
test_brain_web_attempt_blocks_source_task_success_without_accepted_claims
test_brain_web_attempt_blocks_claims_that_have_no_stagecourt_trace
test_brain_web_attempt_blocks_stagecourt_trace_that_is_not_promoted
test_brain_web_attempt_accepts_only_real_provider_claim_export_stagecourt_and_promoted_row
```

검증 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_census_v4_brain_web_readiness_gate tests.test_census_v4_run_mode_honesty -v
```

결과:

```text
Ran 22 tests
OK
```

## 반영한 문서 패치

### 1. v3 문서 오해 방지

`census_v3_stage_map_audit_2026-07-01.md`는 v3 forensic 문서다.
최신 v4 숫자로 읽으면 충돌한다.

반영:

```text
문서 맨 위에 "최신 v4 현재값 문서가 아니다" 경고 추가.
```

### 2. FULL_THESIS_SMOKE_PENDING은 pass가 아님

반영할 원칙:

```text
FULL_THESIS_SMOKE_PASS
!= task planned
!= task pending
!= explicitly pending
```

Pass 조건:

```text
source task 실행
accepted claim 생성
primitive mapping
score contribution
StageCourt trace
representative census_stage_status row
```

또는 material blocker가 있으면:

```text
FULL_THESIS_SMOKE_PENDING
```

으로 남겨야 한다.

쉬운 예:

```text
시험장에 들어간 것은 pass가 아니다.
답안을 쓰고 채점까지 끝나야 pass다.
```

### 3. LLM classification은 proposal/diagnostic

반영할 원칙:

```text
LLM이 contract type이나 primitive를 제안할 수는 있다.
하지만 accepted primitive 확정과 score eligibility는 deterministic guard가 결정한다.
```

금지:

```text
LLM이 "contract_quality=true"라고 했다는 이유만으로 점수 반영
LLM이 "Stage2"라고 했다는 이유만으로 stage 반영
```

허용:

```text
LLM claim extraction:
  subject / predicate / value / date / quote / source span

LLM mapping proposal:
  이 claim이 어떤 primitive 후보인지 제안

deterministic guard:
  entity directness, date, current/open, document/anchor row, source quorum, primitive contract 검증
```

### 4. query provenance gate

반영할 원칙:

```text
non-official query는 반드시 LLM planner의 planner_run_id / prompt_response_id에서 나온다.
deterministic 코드는 query를 생성하지 않고 검증만 한다.
```

검증 항목:

```text
query_provenance_missing_count = 0
deterministic_query_template_count = 0
hardcoded_query_count = 0
future_leakage_query_count = 0
duplicate_query_count는 LLM에 feedback 후 재생성
```

쉬운 예:

```text
코드가 "HBM 장기공급계약 선수금" 검색어를 직접 만들면 하드코딩이다.
LLM이 현재 문서와 gap을 보고 query를 제안하고,
코드는 날짜/대상회사/중복만 검사해야 한다.
```

### 5. 종목명 분기 금지

Samsung/Hynix smoke는 중요한 fixture지만 종목명 예외가 되면 안 된다.

Gate:

```text
symbol_specific_scoring_branch_count = 0
symbol_specific_stage_branch_count = 0
hardcoded_query_count = 0
```

쉬운 예:

```text
삼성전자라서 봐주는 것도 안 되고,
하이닉스라서 C06으로 박는 것도 안 된다.
같은 Evidence Contract와 claim 검증 규칙으로 통과해야 한다.
```

## 남은 blocker

현재 닫힌 것:

```text
가짜 pass/가짜 stage 방지
attempt count만으로 readiness pass되는 경로 차단
document/anchor 문자열만 있는 claim 차단
disabled Brain/Web pass claim 차단
```

아직 남은 것:

```text
Brain/Web fetched document -> LLM extractor -> accepted claim 연결
accepted claim -> primitive state 연결
primitive state -> score contribution 연결
score contribution -> StageCourt trace 연결
실제 live run의 StageCourt trace -> representative census_stage_status strict promotion
Samsung/Hynix C06 full thesis smoke 실제 실행
전 아키타입 Evidence Contract v2 replay parity
```

주의:

```text
strict promotion producer 자체는 이후 패치로 구현됐고 fixture 테스트에서 통과한다.
여기서 남은 것은 실제 live/codex enabled run의 산출물이 그 producer 조건을 만족하는지다.
```

현재 상태를 한 문장으로 쓰면:

> Census v4는 이제 "없는 답안지를 성적표로 포장하는 경로"를 더 강하게 막지만, 아직 "답안지를 실제로 작성하고 채점하는 Brain/Web + full thesis 운영 파이프라인"은 완성되지 않았다.
