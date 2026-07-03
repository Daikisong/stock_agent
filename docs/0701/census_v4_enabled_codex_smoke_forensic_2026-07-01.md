# Census v4 Enabled Codex Smoke Forensic - 2026-07-01

이 문서는 canonical run이 아니라, Brain/Web enabled 경로를 작게 켰을 때 어디까지 실제로 닫히는지 확인한 별도 진단 기록이다.

## 결론

```text
Codex planner는 실제 provider success 1회를 만들었다.
Research Brain source task도 10개 실행했다.
attempt 문서 집계는 12개였다.
accepted claim은 5건 집계, unique accepted claim은 2개가 export됐다.
claim-backed score contribution 5개와 Brain StageCourt trace 1개도 생겼다.

하지만 representative census_stage_status row 승격은 0개다.
따라서 Brain/Web evidence pass도 아니고, 운영 Stage cutover도 아니다.
```

쉬운 예:

```text
자료 조사원이 계약서 사본을 찾았다.
채점자가 그 계약서로 점수 메모도 만들었다.
판사가 StageCourt 초안 판결도 썼다.

하지만 그 판결이 아직 공식 성적표(census_stage_status)에 등재되지 않았다.
그러면 "운영 Stage가 나왔다"가 아니라 "승격 직전 장부까지 생겼지만 아직 blocked"다.
```

## 실행 범위

이 실행은 `/tmp` 격리 output을 사용했다.
canonical 산출물인 `output/census_v4/2026-07-01`을 덮어쓰지 않았다.

관측 output:

```text
/tmp/census_v4_codex_smoke_gScqHy/out
```

명령 골격:

```bash
tmp=$(mktemp -d /tmp/census_v4_codex_smoke_XXXXXX)
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root "$tmp/out" \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --brain-planner-provider codex \
  --brain-source-acquisition live_official_first \
  --brain-universe-limit 3 \
  --brain-planner-success-limit 1 \
  --brain-planner-batch-size 1 \
  --brain-max-fetches-per-task 2 \
  --brain-stage-promotion-mode disabled \
  --target-gate meaningful \
  --max-iterations 1 \
  --fail-on-run-mode-overclaim false \
  --fail-on-atomic-mismatch false \
  --fail-on-semantic-guard false \
  --fail-on-critical-audit false \
  --write-operational-docs false
```

결과:

```text
exit: 1
readiness_verdict: NOT_READY
```

## Attempt Audit

`brain_web_attempt_audit.json`:

```text
verdict: ATTEMPTED_NOT_CUTOVER_READY
attempt_mode: research_brain_v4_production_shadow_attempt
planner_provider: codex
planner_run_count: 3
real_provider_success_count: 1
source_task_execution_count: 10
real_document_fetched_count: 12
accepted_claim_count: 5
unique_accepted_claim_count: 2
brain_to_census_claim_exported_count: 2
brain_stagecourt_trace_exported_count: 1
brain_to_census_stage_exported_count: 0
stagecourt_trace_ready: true
claim_acceptance_ready: true
cutover_export_ready: false
blockers:
  - Research Brain StageCourt traces are not promoted into census_stage_status rows
```

중요한 구분:

```text
brain_stagecourt_trace_exported_count = 1
```

은 "StageCourt 초안 trace가 있다"는 뜻이다.

```text
brain_to_census_stage_exported_count = 0
cutover_export_ready = false
```

은 "대표 운영 row에는 아직 들어가지 않았다"는 뜻이다.

## Promotion Audit

`brain_stage_promotion_audit.json`:

```text
verdict: PROMOTION_DISABLED_BY_POLICY
brain_claim_count: 2
brain_score_contribution_count: 5
brain_stage_trace_count: 1
brain_promoted_stage_row_count: 0
brain_snapshot_document_count: 3
unsafe_promoted_stage_row_count: 0
blockers:
  - Brain stage promotion mode is disabled
  - brain evidence documents include snapshot:// URLs
```

해석:

```text
StageCourt trace는 생겼다.
하지만 promotion mode가 disabled이고, source가 snapshot://라서 대표 row 승격은 막힌다.
```

이건 오류가 아니라 방어다.
snapshot 기반 trace가 곧바로 운영 Stage가 되면 다시 과거와 같은 사고가 난다.

## Readiness Gate

`brain_web_readiness_gate_audit.json`:

```text
verdict: BLOCKED
minimum_gate_applies: true
brain_web_evidence_pass_allowed: false

attempt_source_task_execution_count: 10
source_task_execution_count: 10
attempt_real_document_fetched_count: 12
real_document_fetched_count: 0
attempt_accepted_claim_count: 5
web_or_llm_accepted_claim_count: 2
brain_to_claim_trace_count: 2
brain_score_contribution_count: 5
brain_stage_trace_count: 1
brain_promoted_stage_row_count: 0
```

주요 blocker:

```text
- Brain/Web real fetched document count is zero
- Brain/Web real document attempt count has no exported evidence_documents rows
- Brain/Web acquisition mode requires web/news search task rows
- Brain/Web acquisition mode requires fetched full-source web/news documents
- Brain/Web source task rows missing fetched document refs: 3
- Brain/Web evidence documents include snapshot:// sources
- Brain/Web StageCourt traces are not promoted into census_stage_status
- brain stage promotion verdict is not PROMOTION_APPLIED: PROMOTION_DISABLED_BY_POLICY
```

주의:

```text
attempt_real_document_fetched_count = 12
real_document_fetched_count = 0
```

attempt 쪽 숫자는 Research Brain 내부 집계다.
readiness gate가 운영 admissible full-source web/news document로 인정한 숫자는 0이다.

## Leaf Audit

`leaf_artifact_audit.json`:

```text
verdict: FAIL
critical_count: 2
llm_claim_extractor_claimed_but_zero_count: 1
web_claimed_but_zero_search_count: 1

brain_attempt_cutover_without_promotion_count: 0
brain_attempt_overclaims_success_count: 0
brain_stage_promotion_unsafe_promoted_count: 0
brain_web_readiness_gate_overclaim_count: 0
```

해석:

```text
실행은 NOT_READY로 실패했다.
하지만 새로 막으려던 "cutover_ready=true인데 promoted row 0개" 같은 과대주장은 0으로 막혔다.
```

## 왜 이전 문서보다 결론이 달라졌나

이전 smoke에서는 accepted claim이 0개였다.
이후 패치로 다음 경로가 일부 열렸다.

```text
structured source document
-> accepted claim
-> primitive state
-> score contribution
-> StageCourt trace
```

다만 마지막 한 줄은 아직 닫히지 않았다.

```text
StageCourt trace
-> representative census_stage_status row
```

그래서 결론은 여전히 `NOT_READY`지만, 실패 위치가 바뀌었다.

```text
이전 실패 위치:
  답안 문장 accepted claim이 없음

현재 실패 위치:
  답안 문장과 채점 메모는 일부 생겼지만 공식 성적표 승격이 막힘
```

## 사용자가 물은 질문에 대한 답

질문:

```text
뭔가 잘못되고있는거맞지? stage가 있는애들이 있긴해?
```

답:

```text
canonical census_stage_status에는 Stage label이 있다.
하지만 그건 full thesis 운영 Stage가 아니라 daily/census event 상태판이다.

enabled smoke에는 Brain StageCourt trace 1개가 있다.
하지만 representative census_stage_status row로 승격된 Brain/Web 운영 Stage는 0개다.
```

쉬운 예:

```text
Stage label:
  "이 학생은 출석했고 관찰 대상이다" 같은 상태표시.

Brain StageCourt trace:
  "채점자가 초안 점수를 계산했다"는 내부 기록.

Promoted census_stage_status row:
  "공식 성적표에 반영됐다"는 운영 결과.

현재는 세 번째가 0개다.
```

## 이번 패치로 조인 것

이전 로직은 아래 상태를 너무 좋게 읽을 수 있었다.

```text
accepted claim 있음
score contribution 있음
StageCourt trace 있음
representative census_stage_status 승격 없음
```

이제 이 상태는 반드시 이렇게 남는다.

```text
ATTEMPTED_NOT_CUTOVER_READY
stagecourt_trace_ready=true
cutover_export_ready=false
blocker:
  Research Brain StageCourt traces are not promoted into census_stage_status rows
```

추가로 leaf audit도 방어한다.

```text
brain_attempt_cutover_without_promotion_count
```

이 값은 누가 다시 `cutover_export_ready=true`를 잘못 세팅했는데 promotion audit이 0개면 critical로 잡기 위한 장치다.

## 다음 패치 방향

1. snapshot source를 운영 admissible document로 오인하지 않게 유지한다.
2. live/full-source document fetch와 web/news acquisition row를 실제로 export한다.
3. LLM claim extractor attempt를 실제 fetched document에 연결한다.
4. accepted claim, score contribution, StageCourt trace가 생긴 뒤에도 strict promotion 조건을 통과해야 representative row로 올린다.
5. `brain_stage_promotion_mode=strict`에서만, snapshot/fake/provider blocker가 0이고 ID chain이 닫힌 경우에만 `census_stage_status` 승격을 허용한다.
6. 승격 뒤에도 `brain_to_claim_trace.census_stage_status_id`가 실제 representative row를 가리켜야 한다.

## 교차검증 질문

다음 에이전트는 이 문서를 보고 아래를 공격하면 된다.

```text
Q1. source_task_execution_count 10과 attempt_real_document_fetched_count 12가 진짜 운영 증거인가?
A1. 아니다. readiness gate 기준 full-source real_document_fetched_count는 0이고 snapshot blocker가 있다.

Q2. accepted claim 2개가 export됐으니 Brain/Web pass인가?
A2. 아니다. score contribution과 StageCourt trace까지 생겼지만 representative census_stage_status 승격이 0개다.

Q3. StageCourt trace 1개면 Stage가 나온 것 아닌가?
A3. 아니다. StageCourt trace는 내부 판정 장부이고, 운영 Stage는 census_stage_status promoted row다.

Q4. 왜 ATTEMPTED_WITH_SOURCE_TASKS가 아닌가?
A4. cutover_export_ready=false이기 때문이다. StageCourt trace가 representative row로 승격되지 않았다.

Q5. 지금 Stage가 있는 종목은 있나?
A5. canonical status label은 있다. Brain/Web promoted 운영 Stage는 0개다.
```
