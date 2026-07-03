# Census v4 Brain Stage Promotion Gate - 2026-07-01

이 문서는 `Research Brain/Web` 산출물이 `census_stage_status.jsonl`의 대표 Stage row로 올라가도 되는지 검증하는 별도 감사 기록이다.

관련 최종 bundle gate:

```text
brain_web_readiness_gate_audit.json
```

`brain_web_readiness_gate_audit.json`은 Brain/Web을 실제로 실행했는지, real provider/source/claim/trace/score/stage/promotion이 모두 이어졌는지를 최종적으로 본다.
이 문서의 promotion gate는 그 안에 들어가는 하위 조건으로, "Brain/Web StageCourt trace를 대표 Stage row로 올려도 되는가"만 따로 본다.

핵심 질문은 이것이다.

```text
Brain/Web이 claim, score contribution, StageCourt trace를 만들면
그걸 바로 Census 대표 Stage로 써도 되는가?
```

현재 답은 아니다.

```text
canonical run에서는 Brain/Web 자체가 disabled다.
따라서 Brain claim도, Brain StageCourt trace도, Brain promoted representative Stage row도 없다.
```

쉬운 예:

```text
서류 검토자가 메모를 써도,
그 메모가 교무실 공식 성적표에 자동 반영되면 안 된다.

공식 성적표에 반영하려면:
  누가 메모를 썼는지,
  원문 서류가 실제 운영 서류인지,
  점수 칸과 claim이 연결됐는지,
  snapshot/fake가 아닌지,
  승격 감사가 통과했는지
를 모두 확인해야 한다.
```

## 새 산출물

이번 패치로 항상 아래 파일을 남긴다.

```text
output/census_v4/2026-07-01/brain_stage_promotion_audit.json
docs/operational/census_mode_v4_brain_stage_promotion_audit.json
output/census_v4/2026-07-01/brain_web_readiness_gate_audit.json
docs/operational/census_mode_v4_brain_web_readiness_gate_audit.json
```

`leaf_artifact_audit.json`도 이 파일을 필수 JSON 산출물로 요구한다.

즉 파일이 빠지면 audit가 실패해야 한다.

## canonical run 현재값

기준 명령:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root output/census_v4/2026-07-01 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode LEDGER_REFRESH_CENSUS \
  --brain-web-mode disabled \
  --research-brain-report-dir docs/operational \
  --fail-on-critical-audit true \
  --write-operational-docs auto
```

관측값:

```json
{
  "verdict": "NOT_REQUESTED",
  "brain_web_mode": "disabled",
  "brain_stage_promotion_mode": "disabled",
  "brain_stage_trace_count": 0,
  "brain_promoted_stage_row_count": 0,
  "unsafe_promoted_stage_row_count": 0,
  "brain_claim_count": 0,
  "brain_score_contribution_count": 0,
  "brain_snapshot_document_count": 0,
  "blockers": []
}
```

선행 readiness gate 현재값:

```text
brain_web_readiness_gate_verdict: NOT_REQUESTED
brain_web_evidence_pass_allowed: false
```

해석:

```text
Brain/Web을 요청하지 않았으므로 실패가 아니다.
동시에 Brain/Web 통과도 아니다.
```

중요한 점:

```text
NOT_REQUESTED
!= PASS
!= BRAIN_WEB_EVIDENCE_PASS
!= FULL_THESIS_SMOKE_PASS
```

`NOT_REQUESTED`는 말 그대로 실행하지 않았다는 뜻이다.

## 승격 조건

`brain_stage_promotion_audit.json`에는 아래 조건이 `promotion_requirements_if_enabled`로 기록된다.

```text
brain_web_mode=enabled
brain_stage_promotion_mode=strict
real planner/provider success > 0
source task executions > 0
accepted brain claims > 0
claim-backed score contributions > 0
brain StageCourt traces > 0
zero snapshot:// promoted evidence documents
zero fake provider rows
zero unsafe promoted representative rows
```

이 조건을 만족하지 못하면 Brain/Web trace가 있더라도 `census_stage_status.jsonl` 대표 row로 승격하면 안 된다.

쉬운 예:

```text
frozen_real_source_snapshot으로 만든 trace
  -> claim과 stage trace는 만들 수 있다.
  -> 하지만 snapshot:// 자료라 운영 대표 Stage로 승격 금지.

brain_planner_provider=none
  -> planner row는 남을 수 있다.
  -> real_provider_success_count=0이면 운영 승격 금지.

score contribution이 없는 claim
  -> 증거 메모는 있을 수 있다.
  -> 점수 칸에 기여하지 않았으므로 Stage 승격 금지.
```

## 차단해야 하는 위험

### 위험 1. Brain leaf export를 대표 Stage로 오해

`brain_web_mode=enabled`를 켜면 다음 leaf 파일이 생길 수 있다.

```text
planner_runs.jsonl
research_brain_plans.jsonl
source_tasks.jsonl
source_task_executions.jsonl
evidence_documents.jsonl
evidence_anchors.jsonl
raw_assertions.jsonl
adjudicated_claims.jsonl
accepted_claims.jsonl
primitive_states.jsonl
score_contributions.jsonl
stagecourt_traces.jsonl
brain_to_claim_trace.jsonl
```

하지만 이 파일들이 있다는 것만으로 대표 Stage가 된 것은 아니다.

대표 Stage가 되려면 `census_stage_status.jsonl` row가 Brain StageCourt trace를 참조해야 한다.
현재 canonical run에서는 그런 row가 0개다.

### 위험 2. snapshot trace 승격

기존 Research Brain v4 보고서에는 `snapshot://` source가 255개 있다.

이것은 replay/backfill 분석에는 쓸 수 있지만, production cutover evidence로 바로 쓰면 안 된다.

```text
snapshot:// 문서
= 과거 저장본 또는 fixture성 재생 자료
!= live production source fetch
```

따라서 snapshot 기반 Brain StageCourt trace가 대표 row로 올라오면 실패해야 한다.

### 위험 3. provider failure를 낮은 점수로 확정

provider-none negative smoke에서 real provider success가 0이면 다음이 맞다.

```text
NOT_READY
Provider/Source Pending
대표 Stage 승격 없음
```

다음은 틀리다.

```text
provider가 실패했으니 claim이 없다
-> 낮은 점수로 확정
-> Stage0/Red로 최종 확정
```

provider 실패는 낮은 점수의 증거가 아니다.

## 새 테스트

추가된 테스트:

```text
tests/test_census_v4_brain_stage_promotion_gate.py
```

검증 내용:

```text
1. canonical disabled run은 promotion verdict NOT_REQUESTED다.
2. brain_stage_trace_count=0, promoted row=0, unsafe promoted row=0이다.
3. frozen snapshot Brain bundle은 claim/score/stage trace를 export해도 대표 Stage로 승격하지 않는다.
4. blocker가 있는데 Brain row가 대표 Stage로 올라오면 FAIL_UNSAFE_PROMOTION이다.
5. strict/live/real/provider/source/claim/contribution/stage가 연결된 대표 row는 PROMOTION_APPLIED가 가능하다.
```

타깃 검증 명령:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_bundle_export \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_run_mode_honesty \
  -v
```

관측 결과:

```text
Ran 22 tests in 14.024s
OK
```

## negative smoke: strict mode but provider none

임시 출력으로 아래를 실행했다.

```bash
tmp=$(mktemp -d)
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root "$tmp/out" \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --brain-planner-provider none \
  --brain-stage-promotion-mode strict \
  --brain-universe-limit 5 \
  --brain-planner-success-limit 5 \
  --fail-on-critical-audit false \
  --write-operational-docs auto
```

관측값:

```text
stdout: NOT_READY
exit: 1

brain_stage_promotion_audit:
  verdict: BLOCKED
  brain_stage_promotion_mode: strict
  brain_stage_trace_count: 0
  brain_promoted_stage_row_count: 0
  unsafe_promoted_stage_row_count: 0
  blockers:
    - planner provider is not a real promotion provider: none
    - LLM planner has zero real-provider successes
    - source task execution count is zero
    - accepted brain claim count is zero
    - brain score contribution count is zero
    - brain StageCourt trace count is zero
```

해석:

```text
strict 모드를 켰다는 사실만으로 승격되지 않는다.
real provider, source task, accepted claim, score contribution, StageCourt trace가 모두 없으므로 BLOCKED가 맞다.
```

## leaf audit에 추가된 항목

`leaf_artifact_audit.json` metrics:

```text
brain_stage_promotion_verdict: NOT_REQUESTED
brain_stage_promotion_mode: disabled
brain_stage_trace_count: 0
brain_stage_promoted_row_count: 0
brain_stage_promotion_unsafe_promoted_count: 0
brain_stage_promotion_snapshot_document_count: 0
brain_stage_promotion_blocker_count: 0
```

`leaf_artifact_audit.json` critical_counts:

```text
brain_stage_promotion_unsafe_promoted_count: 0
brain_stage_promotion_trace_promoted_reference_count: 0
brain_stage_trace_not_promoted_marker_missing_count: 0
brain_stage_promotion_overclaim_count: 0
```

이 중 하나라도 0이 아니면 다음 에이전트는 반드시 실패로 봐야 한다.

## 다음 패치 방향

아직 해야 할 일은 `Brain/Web trace export`가 아니라 `strict promotion`이다.

순서는 다음이 맞다.

```text
1. brain_web_mode=enabled에서 real provider success를 실제로 만든다.
2. SourceTask가 live official-first/bounded로 실행됐는지 검증한다.
3. snapshot://, fake provider, fixture source를 promotion 대상에서 제거한다.
4. accepted claim -> primitive state -> score contribution -> StageCourt trace를 만든다.
5. brain_stage_promotion_mode=strict에서 promotion audit가 BLOCKED, ELIGIBLE_NOT_PROMOTED, PROMOTION_APPLIED를 각각 정확히 구분하는지 확인한다.
6. 그 다음에만 census_stage_status 대표 row 병합을 구현한다.
7. 병합 후 모든 score/stage delta가 claim delta로 설명되는지 audit한다.
```

다음 에이전트가 가장 먼저 때려야 할 질문:

```text
Brain StageCourt trace가 있다면 그 trace는 live source인가?
그 trace의 claim은 source anchor가 있는가?
그 score contribution은 accepted claim id를 갖는가?
그 trace가 census_stage_status에 올라갔다면 promotion audit verdict가 무엇인가?
snapshot:// 또는 fake provider가 하나라도 있는데 대표 Stage로 승격됐는가?
```

현재 답:

```text
canonical disabled run에는 Brain StageCourt trace가 없다.
따라서 Brain 대표 Stage 승격도 없다.
```
