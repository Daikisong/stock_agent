# Census v4 Brain/Web Readiness Gate - 2026-07-01

이 문서는 `brain_web_readiness_gate_audit.json`을 다음 리뷰어가 바로 공격할 수 있게 정리한 것이다.

## 결론

```text
현재 canonical v4 run:
  run_mode: LEDGER_REFRESH_CENSUS
  brain_web_mode: disabled
  verdict: NOT_REQUESTED
  brain_web_evidence_pass_allowed: false

즉 Brain/Web이 통과한 것이 아니다.
Brain/Web을 실행하지 않았고, 실행하지 않았다고 정직하게 기록한 것이다.
```

쉬운 예:

```text
시험을 안 봤으면 "결시"라고 써야 한다.
"틀린 답이 없으니 합격"이라고 쓰면 안 된다.

이번 gate는 Brain/Web에 대해 그 구분을 강제한다.
```

## 왜 추가했나

기존에는 아래 개별 감사가 있었다.

```text
brain_planner_audit
web_naver_acquisition_audit
llm_claim_extraction_audit
brain_to_claim_trace_audit
brain_stage_promotion_audit
```

문제는 canonical disabled run에서 이 파일들이 대체로 0건이고, 어떤 파일은 `PASS`로 보일 수 있다는 점이다.

```text
0건 PASS
!= Brain/Web 준비 완료

0건 PASS
= disabled 상태에서 내부 모순이 없었다
```

따라서 새 gate는 개별 감사들을 한 번 더 묶어서, 운영자가 주장할 수 있는 말을 제한한다.

구조상 역할은 이렇게 나뉜다.

```text
brain_stage_promotion_audit
  = Brain/Web StageCourt trace를 대표 census_stage_status row로 올려도 되는지 보는 하위 gate

brain_web_readiness_gate_audit
  = planner/source/extractor/claim/trace/contribution/StageCourt/promotion을 모두 묶어
    "Brain/Web evidence pass라고 말해도 되는가"를 최종 판정하는 bundle gate
```

쉬운 예:

```text
promotion gate는 "답안지를 공식 성적표에 옮겨도 되는가"를 본다.
readiness gate는 "시험지 배부, 답안 작성, 채점, 성적표 반영까지 전부 끝났는가"를 본다.
```

## 새 산출물

Canonical output:

```text
output/census_v4/2026-07-01/brain_web_readiness_gate_audit.json
```

Docs copy:

```text
docs/operational/census_mode_v4_brain_web_readiness_gate_audit.json
```

Manifest:

```text
artifact_manifest.json에 포함됨
```

Readiness:

```text
readiness_verdict.json의 brain_web_readiness_gate 필드에 요약 포함
```

## 현재값

```text
verdict: NOT_REQUESTED
minimum_gate_applies: false
brain_web_evidence_pass_allowed: false

llm_planner_call_count: 0
llm_real_provider_success_count: 0
source_task_execution_count: 0
real_document_fetched_count: 0
web_search_task_count: 0
web_fetched_document_count: 0
llm_claim_extractor_attempt_count: 0
web_or_llm_accepted_claim_count: 0
brain_to_claim_trace_count: 0
brain_score_contribution_count: 0
brain_stage_trace_count: 0
brain_promoted_stage_row_count: 0
brain_trace_missing_accepted_claim_count: 0
brain_trace_missing_score_contribution_ref_count: 0
brain_trace_missing_stagecourt_ref_count: 0
brain_contribution_without_accepted_support_count: 0
brain_stage_trace_without_accepted_claim_count: 0
promoted_stage_without_brain_trace_count: 0

snapshot_document_count: 0
fake_provider_used_count: 0
snippet_to_score_count: 0
provider_failure_final_score_count: 0
blockers: []
nonblocking_gaps:
  - Brain/Web was not requested in this ledger-refresh run
```

해석:

```text
Brain/Web을 실행하지 않았으므로 blockers가 없는 것은 정상이다.
하지만 pass_allowed=false이므로 Brain/Web pass label을 붙일 수 없다.
```

## enabled run에서는 어떻게 막나

Brain/Web을 요청했는데 실제 provider/source/extractor가 없으면 `BLOCKED`가 떠야 한다.

테스트 케이스:

```text
run_mode: BRAIN_AND_WEB_ACQUISITION_ENABLED
brain_web_mode: enabled
brain_planner_provider: none

expected:
  verdict: BLOCKED
  brain_web_evidence_pass_allowed: false
```

대표 blocker:

```text
LLM planner real-provider success count is zero
Brain/Web source task execution count is zero
Brain/Web real fetched document count is zero
web/LLM accepted claim count is zero
Brain/Web StageCourt traces are not promoted into census_stage_status
brain stage promotion verdict is not PROMOTION_APPLIED
```

쉬운 예:

```text
선생님이 시험지를 나눠주지도 않았고,
학생 답안지도 없고,
채점지도 없는데,
"합격자 명단에 올림"이 나오면 안 된다.

이 gate는 그 상황을 BLOCKED로 만든다.
```

## Codex-enabled smoke 확인

별도 `/tmp` 격리 output에서 Codex planner를 켠 작은 smoke를 돌렸다.
이 실행은 canonical run이 아니며, 운영 통과 증거가 아니라 실패 위치를 확인하기 위한 진단이다.

관측값:

```text
readiness_verdict: NOT_READY
brain_web_attempt.verdict: ATTEMPTED_NOT_CUTOVER_READY
planner_provider: codex
real_provider_success_count: 1
source_task_execution_count: 10
attempt_real_document_fetched_count: 12
real_document_fetched_count: 0
accepted_claim_count: 5
unique_accepted_claim_count: 2
brain_to_census_claim_exported_count: 2
brain_stagecourt_trace_exported_count: 1
brain_to_census_stage_exported_count: 0
claim_acceptance_ready: true
stagecourt_trace_ready: true
cutover_export_ready: false
brain_web_readiness_gate.verdict: BLOCKED
brain_web_evidence_pass_allowed: false
```

핵심 blocker:

```text
Brain/Web real fetched document count is zero
Brain/Web real document attempt count has no exported evidence_documents rows
Brain/Web acquisition mode requires web/news search task rows
Brain/Web acquisition mode requires fetched full-source web/news documents
Brain/Web evidence documents include snapshot:// sources
Brain/Web StageCourt traces are not promoted into census_stage_status
brain stage promotion verdict is not PROMOTION_APPLIED: PROMOTION_DISABLED_BY_POLICY
```

쉬운 예:

```text
책을 가져왔고, 답안 문장도 일부 썼고, 채점 초안도 만들었다.
하지만 그 채점 초안이 공식 성적표에 옮겨지지 않았다.
따라서 운영 Stage라고 말하면 안 된다.
```

이번 패치로 `real_provider_success_count > 0`이고 `source_task_execution_count > 0`이어도
representative `census_stage_status` 승격이 0개면 `ATTEMPTED_WITH_SOURCE_TASKS`가 아니라
`ATTEMPTED_NOT_CUTOVER_READY`가 된다.

추가 교차검증 반영:

```text
attempt count는 proof가 아니다.
```

따라서 readiness gate는 아래 집계값을 그대로 pass 조건으로 쓰지 않는다.

```text
brain_web_attempt.source_task_execution_count
brain_web_attempt.real_document_fetched_count
brain_web_attempt.accepted_claim_count
brain_web_attempt.brain_stagecourt_trace_exported_count
```

이 값들은 `attempt_*` 진단 필드로만 남기고, pass 판단은 실제 leaf row로 한다.

```text
source_task_executions.jsonl의 Brain/Web origin row
evidence_documents.jsonl의 Brain/Web origin row
evidence_anchors.jsonl의 anchor row
accepted_claims.jsonl의 Brain/Web origin row
score_contributions.jsonl의 Brain/Web origin row
stagecourt_traces.jsonl의 Brain/Web origin row
brain_to_claim_trace.jsonl의 같은 accepted_claim_id
```

새 blocker:

```text
Brain/Web source task attempt count has no exported source_task_executions rows
Brain/Web real document attempt count has no exported evidence_documents rows
Brain/Web accepted claim attempt count has no exported accepted_claims rows
accepted Brain/Web claims reference missing evidence_documents rows
accepted Brain/Web claims reference missing evidence_anchors rows
Brain/Web source task rows reference missing evidence_documents rows
```

쉬운 예:

```text
"책 10권 가져옴"이라는 숫자만으로는 부족하다.
실제 책 목록, 인용 위치, 답안 문장, 채점 기록이 같은 번호로 이어져야 한다.
```

상세 기록:

```text
docs/0701/census_v4_enabled_codex_smoke_forensic_2026-07-01.md
docs/0701/census_v4_subagent_cross_validation_findings_2026-07-01.md
```

## Brain/Web evidence pass 조건

현재 코드가 요구하는 최소 조건:

```text
1. Brain/Web이 실제로 requested 상태여야 한다.
2. LLM planner real-provider success가 있어야 한다.
3. source task execution이 있어야 한다.
4. real fetched document가 있어야 한다.
5. web/news/Naver 또는 source acquisition 결과가 accepted claim으로 이어져야 한다.
6. accepted claim은 brain_to_claim_trace를 가져야 한다.
7. brain_to_claim_trace의 accepted_claim_id가 실제 accepted Brain/Web claim ID와 같아야 한다.
8. trace는 score_contribution_id와 stagecourt_trace_id를 모두 가져야 한다.
9. score contribution의 support_claim_ids가 accepted Brain/Web claim을 실제로 지지해야 한다.
10. StageCourt trace의 accepted_claim_ids가 accepted Brain/Web claim과 연결되어야 한다.
11. strict promotion으로 census_stage_status 대표 row에 승격된 row도 같은 StageCourt trace와 claim ID를 가져야 한다.
12. snapshot://, fake provider, snippet-only score, provider-failure final score가 없어야 한다.
```

중요:

```text
이 gate가 pass 가능 상태가 되어도 LLM이 Stage를 직접 결정하는 것은 아니다.
LLM은 source-backed claim을 만들고,
Stage는 deterministic StageCourt가 결정해야 한다.
```

## 현재 acceptance report 반영

```text
19. Brain/Web readiness gate: NOT_REQUESTED; pass_allowed=False; blockers=0
```

이 줄의 의미:

```text
Brain/Web 준비 완료가 아니라,
disabled ledger-refresh run에서 Brain/Web pass를 주장하지 않는다는 뜻이다.
```

## 추가 테스트

```text
tests/test_census_v4_brain_web_readiness_gate.py
```

검증 내용:

```text
1. canonical disabled run은 NOT_REQUESTED이고 pass_allowed=false다.
2. enabled/provider-none run은 BLOCKED이고 pass_allowed=false다.
3. 연결된 claim -> trace -> contribution -> StageCourt -> promoted row는 pass 가능하다.
4. 숫자는 모두 1개여도 claim ID가 서로 다르면 BLOCKED다.
```

전체 테스트:

```text
PYTHONPATH=src python -m unittest discover -s tests -v
Ran 4942 tests in 170.248s
OK
```

## 다음 리뷰어 공격 질문

```text
1. brain_web_readiness_gate_audit.json이 artifact_manifest에 들어 있는가?
2. disabled run에서 NOT_REQUESTED가 아니라 PASS로 보이는 문서가 있는가?
3. brain_web_evidence_pass_allowed=false인데 BRAIN_WEB_EVIDENCE_PASS label이 붙는가?
4. enabled/provider-none run에서 BLOCKED가 아니라 pass가 나오는가?
5. source_task_execution_count=0인데 Brain/Web evidence pass가 가능한가?
6. real_document_fetched_count=0인데 accepted claim이나 score contribution이 생기는가?
7. accepted Brain/Web claim이 있는데 brain_to_claim_trace가 없는가?
8. brain_to_claim_trace의 accepted_claim_id가 실제 accepted claim ID와 다른가?
9. score contribution의 support_claim_ids가 다른 claim을 가리키는데 통과하는가?
10. StageCourt trace의 accepted_claim_ids가 다른 claim을 가리키는데 통과하는가?
11. promoted census row가 Brain/Web StageCourt trace와 같은 claim ID를 갖지 않는데 통과하는가?
12. Brain/Web StageCourt trace가 strict promotion 없이 census_stage_status 대표 row로 들어가는가?
13. snapshot:// 문서가 production Brain/Web evidence로 pass되는가?
14. provider failure row가 낮은 점수 final로 확정되는가?
```

## 다음 패치 방향

```text
P0 완료:
  disabled Brain/Web을 pass로 오해하지 못하게 gate를 추가했다.

P1 필요:
  Brain/Web enabled run에서 real provider, bounded source acquisition, claim extractor, accepted claim,
  score contribution, StageCourt trace를 실제로 만드는 production path를 완성한다.

P2 필요:
  그 trace를 strict promotion audit 통과 후에만 representative census_stage_status row에 반영한다.

P3 필요:
  삼성전자/하이닉스 C06 full thesis smoke를 이 경로로 실행하고,
  daily event score와 full thesis score가 섞이지 않는지 확인한다.
```

최종 문장:

```text
Brain/Web readiness gate는 점수를 잘 내는 기능이 아니다.
"실제로 안 했는데 했다고 말하는 것"을 막는 안전문이다.
```
