# Census v4 Stage Truth Final Cross Validation Packet - 2026-07-01

작성 목적:

```text
뭔가 잘못되고 있는 거 맞지?
Stage가 있는 애들이 있긴 해?
다음 에이전트가 이걸 보고 빡세게 피드백할 수 있게 문서화해라.
```

짧은 결론:

```text
Stage label은 있다.
하지만 full E2R 100점 thesis 운영 Stage는 현재 0개다.
```

쉬운 예:

```text
지금은 전교생 출석부와 일부 "주의해서 볼 학생" 표시가 있다.
하지만 기말고사 100점 만점 점수와 최종 등급표는 아직 나오지 않았다.
```

이 문서는 칭찬용 문서가 아니다.
다음 에이전트가 바로 반박하고 공격할 수 있도록 현재 사실과 남은 구멍을 고정한다.

## 1. Source Of Truth

교차검증 기준 leaf artifact:

```text
output/census_v4/2026-07-01/census_stage_status.jsonl
output/census_v4/2026-07-01/census_stage_map.jsonl
output/census_v4/2026-07-01/readiness_verdict.json
output/census_v4/2026-07-01/goal_completion_audit.json
output/census_v4/2026-07-01/samsung_hynix_full_thesis_smoke.json
output/census_v4/2026-07-01/samsung_hynix_full_thesis_smoke_audit.json
output/census_v4/2026-07-01/brain_web_attempt_audit.json
output/census_v4/2026-07-01/brain_web_readiness_gate_audit.json
output/census_v4/2026-07-01/source_task_satisfaction_audit.json
output/census_v4/2026-07-01/primitive_state_chain_audit.json
output/census_v4/2026-07-01/test_result_artifact.json
```

원칙:

```text
docs/0701/*.md는 해설이다.
output/census_v4/2026-07-01/* leaf artifact와 문서가 충돌하면 leaf artifact가 이긴다.
```

## 2. Three-Way Cross Check

### A. stage_status와 stage_map은 같은 말을 한다

`census_stage_status.jsonl` 기준:

```text
rows: 3391

canonical_stage:
  0:       3306
    1:         54
    2:         30
  3-Red:      1

base_stage:
  Stage0:       3306
  Stage1:         54
  Stage2-Watch:   30
  Red:             1

stage_signal:
  NO_CURRENT_CATALYST: 3306
  OFFICIAL_EVENT_WATCH: 36
  MATERIAL_CLAIM_WATCH: 30
  SOURCE_PENDING: 8
  EVIDENCE_INSUFFICIENT: 10
  RISK_REVIEW: 1

stage_decision_status:
  NO_CURRENT_CATALYST: 3306
  FINAL: 36
  SOURCE_PENDING: 18
  PENDING_MATERIAL_GAPS: 30
  RISK_REVIEW: 1

stage_scope:
  CENSUS_EVENT_BOARD: 3391

score_scope:
  NO_SCORE:                 3324
  EVENT_WEIGHTED_PARTIAL:     67

operator_stage_use:
  NOT_FULL_THESIS_STAGE: 3391

operator_score_use:
  NOT_FULL_E2R_SCORE: 3391

full_thesis_stage:
  FULL_THESIS_NOT_RUN: 3391
```

`census_stage_map.jsonl`도 같은 분포다.
따라서 stage row와 exported stage map 사이의 숫자 불일치는 현재 없다.

중요한 음수 검산:

```text
verified_score_present: 0
full_e2r_verified_score_present: 0
is_full_thesis_stage=true: 0
is_full_e2r_score=true: 0
```

해석:

```text
현재 있는 Stage는 event-board 상태 label이다.
full thesis 운영 Stage가 아니다.
```

### B. readiness와 goal audit도 미완료라고 말한다

`readiness_verdict.json`:

```text
verdict: ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
run_mode: LEDGER_REFRESH_CENSUS
brain_web_mode: disabled
meaningful_operational_stage_pass: false
brain_web_evidence_pass: false
full_thesis_smoke_pass: false
```

`goal_completion_audit.json`:

```text
goal_completion_ready: false
full_thesis_status: PENDING_FULL_THESIS_REFRESH
full_thesis_smoke_pass_allowed: false
brain_web_evidence_pass_allowed: false
meaningful_operational_stage_pass_allowed: false
blockers:
  - brain_web_evidence_pass_false
  - full_thesis_smoke_pending
```

해석:

```text
현재 PASS는 anti-fake/status-board pass다.
운영 thesis pass가 아니다.
```

쉬운 예:

```text
"성적표 조작 방지 장치가 통과했다"
!=
"성적표 채점이 끝났다"
```

### C. Samsung/Hynix smoke도 full thesis pending이라고 말한다

삼성전자 `005930`:

```text
company_name: 삼성전자
canonical_stage: 1
base_stage: Stage1
stage_signal: OFFICIAL_EVENT_WATCH
score_valid_status: FINAL_WITH_NONMATERIAL_GAPS
full_thesis_stage: FULL_THESIS_NOT_RUN
operator_stage_use: NOT_FULL_THESIS_STAGE
operator_score_use: NOT_FULL_E2R_SCORE
verified_score: null
full_e2r_verified_score: null
score_contribution_count: 1
accepted_claim_count: 1
full_thesis_missing_primitives:
  - full_thesis_refresh_task_not_run
```

SK하이닉스 `000660`:

```text
company_name: SK하이닉스
canonical_stage: 1
base_stage: Stage1
stage_signal: OFFICIAL_EVENT_WATCH
score_valid_status: FINAL_WITH_NONMATERIAL_GAPS
full_thesis_stage: FULL_THESIS_NOT_RUN
operator_stage_use: NOT_FULL_THESIS_STAGE
operator_score_use: NOT_FULL_E2R_SCORE
verified_score: null
full_e2r_verified_score: null
score_contribution_count: 1
accepted_claim_count: 1
full_thesis_missing_primitives:
  - full_thesis_refresh_task_not_run
```

해석:

```text
맞는 말:
  삼성전자/하이닉스는 daily event board에 올라왔다.

틀린 말:
  삼성전자/하이닉스 HBM/C06 full thesis 점수와 Stage가 나왔다.
```

쉬운 예:

```text
삼성전자 Stage1은 "오늘 확인할 공시/이벤트가 있다"는 접수표다.
"HBM thesis가 Stage1로 확정됐다"가 아니다.
```

## 3. What Exists

현재 존재하는 것:

```text
1. full universe status board
2. CensusAssessmentEvent와 CandidateEvent 분리
3. 3306개 NoCurrentCatalyst row
4. 85개 CandidateEvent-present row
5. 67개 representative EVENT_WEIGHTED_PARTIAL row
6. 92개 accepted/evidence claim payload
7. 67개 representative score claim id-chain
8. primitive state/mapping leaf chain
9. known-bad regression pass
10. test artifact: 4942 tests, OK
```

대표 id-chain:

```text
SourceTaskExecution
-> accepted claim
-> EvidenceDocument
-> EvidenceAnchor
-> PrimitiveState
-> PrimitiveMapping
-> ScoreContribution
-> StageCourt trace
-> representative census_stage_status row
```

현재 SourceTask satisfaction:

```text
schema_version: e2r_census_v4_source_task_satisfaction_audit_v2
verdict: PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION
critical_count: 0
warning_count: 25
representative_score_claim_count: 67
source_task_chain_closed_to_representative_stage_count: 67
live_source_task_satisfaction_pass_allowed: false
```

현재 PrimitiveState chain:

```text
schema_version: e2r_census_v4_primitive_state_chain_audit_v1
verdict: PASS
critical_count: 0
primitive_state_count: 92
primitive_mapping_count: 92
representative_score_claim_count: 67
representative_score_claim_with_primitive_state_count: 67
mapping_leaf_resolution_supported: true
```

## 4. What Does Not Exist Yet

아직 존재하지 않는 것:

```text
1. FULL_E2R_100 verified score
2. full thesis operating Stage row
3. Stage3-Green / Stage3-Yellow thesis 판정
4. 4B / 4C thesis transition 판정
5. Brain/Web promoted operating Stage row in canonical run
6. live official-first source acquisition pass
7. LLM claim extraction production pass
8. Samsung/Hynix C06/HBM full thesis result
9. 전 아키타입 source-backed replay parity
10. meaningful operational stage pass
```

절대 금지할 해석:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
-> MEANINGFUL_OPERATIONAL_STAGE_PASS 로 읽기

EVENT_WEIGHTED_PARTIAL
-> FULL_E2R_100 로 읽기

FULL_THESIS_NOT_RUN
-> 낮은 Stage 확정으로 읽기

DISABLED_HONESTY_PASS
-> Brain/Web 성공으로 읽기

Stage2-Watch   30개
-> full thesis Stage2 30개로 읽기

canonical_stage=3-Red 1개
-> full thesis Stage3-Red 운영 판정 1개로 읽기
```

쉬운 예:

```text
"검사를 아직 안 했다"를 "검사 결과 나쁨"으로 읽으면 안 된다.
FULL_THESIS_NOT_RUN은 낮은 점수가 아니라 미실행 상태다.
```

## 5. 왜 사용자가 불안해한 게 맞나

현재 artifact에는 실제로 `canonical_stage`가 있다.

```text
0, 1, 2, 3-Red
```

이 필드명만 보면 운영 Stage처럼 보일 수 있다.
그래서 불안은 정상이다.

하지만 이 stage는 반드시 다음 필드와 같이 읽어야 한다.

```text
stage_scope
score_scope
operator_stage_use
operator_score_use
full_thesis_stage
verified_score
full_e2r_verified_score
```

현재 모든 row는:

```text
stage_scope=CENSUS_EVENT_BOARD
operator_stage_use=NOT_FULL_THESIS_STAGE
operator_score_use=NOT_FULL_E2R_SCORE
full_thesis_stage=FULL_THESIS_NOT_RUN
verified_score=null
full_e2r_verified_score=null
```

따라서 현재 `canonical_stage`는 "운영 thesis 등급"이 아니라 "상태판 표시값을 canonical enum에 맞춘 값"이다.

쉬운 예:

```text
상태판의 "Red"
= 고객센터에서 "주의 민원"으로 분류한 것
!= 병원에서 "중증 확정 진단"을 내린 것
```

## 6. Cross-Validation Commands

다음 에이전트는 아래 명령으로 이 문서를 다시 깨야 한다.

### Stage status vs stage map

```bash
python - <<'PY'
import json, collections
from pathlib import Path

root = Path("output/census_v4/2026-07-01")
for filename in ["census_stage_status.jsonl", "census_stage_map.jsonl"]:
    rows = [
        json.loads(line)
        for line in (root / filename).read_text().splitlines()
        if line.strip()
    ]
    print("\\n###", filename, len(rows))
    for key in [
        "canonical_stage",
        "base_stage",
        "stage_signal",
        "stage_decision_status",
        "operator_stage_use",
        "operator_score_use",
        "full_thesis_stage",
        "score_valid_status",
        "assessment_depth",
        "investigation_status",
        "stage_scope",
        "score_scope",
        "census_status",
    ]:
        print(key, dict(collections.Counter(str(r.get(key)) for r in rows)))
    print("verified_score_present", sum(1 for r in rows if r.get("verified_score") is not None))
    print(
        "full_e2r_verified_score_present",
        sum(
            1
            for r in rows
            if r.get("full_e2r_verified_score") is not None
            or r.get("full_thesis_verified_score") is not None
        ),
    )
    print(
        "event_score_present",
        sum(
            1
            for r in rows
            if r.get("event_evidence_score") is not None
            or r.get("daily_event_evidence_score") is not None
        ),
    )
    print("accepted_claim_rows", sum(1 for r in rows if r.get("accepted_claim_ids")))
    print("score_contribution_rows", sum(1 for r in rows if r.get("score_contribution_ids")))
PY
```

### Readiness and blockers

```bash
python - <<'PY'
import json
from pathlib import Path

root = Path("output/census_v4/2026-07-01")
for name in [
    "readiness_verdict.json",
    "goal_completion_audit.json",
    "brain_web_attempt_audit.json",
    "brain_web_readiness_gate_audit.json",
    "samsung_hynix_full_thesis_smoke.json",
    "source_task_satisfaction_audit.json",
    "primitive_state_chain_audit.json",
    "test_result_artifact.json",
]:
    data = json.loads((root / name).read_text())
    print("\\n###", name)
    for key in [
        "verdict",
        "status",
        "run_mode",
        "brain_web_mode",
        "meaningful_operational_stage_pass",
        "brain_web_evidence_pass",
        "full_thesis_smoke_pass",
        "goal_completion_ready",
        "blockers",
        "full_thesis_status",
        "full_thesis_smoke_pass_allowed",
        "brain_web_evidence_pass_allowed",
        "meaningful_operational_stage_pass_allowed",
        "critical_count",
        "warning_count",
        "representative_score_claim_count",
        "source_task_chain_closed_to_representative_stage_count",
        "primitive_state_count",
        "primitive_mapping_count",
        "mapping_leaf_resolution_supported",
        "test_count",
        "failed_count",
        "error_count",
        "duration_seconds",
    ]:
        if key in data:
            print(key, data[key])
PY
```

### Samsung/Hynix row check

```bash
python - <<'PY'
import json
from pathlib import Path

root = Path("output/census_v4/2026-07-01")
rows = [
    json.loads(line)
    for line in (root / "census_stage_status.jsonl").read_text().splitlines()
    if line.strip()
]
for symbol in ["005930", "000660"]:
    row = next(r for r in rows if r.get("symbol") == symbol)
    print("\\n###", symbol, row.get("company_name"))
    for key in [
        "canonical_stage",
        "base_stage",
        "stage_signal",
        "stage_decision_status",
        "investigation_status",
        "score_valid_status",
        "full_thesis_stage",
        "operator_stage_use",
        "operator_score_use",
        "verified_score",
        "full_e2r_verified_score",
        "score_contribution_count",
        "accepted_claim_count",
        "full_thesis_missing_primitives",
        "next_actions",
    ]:
        print(key, row.get(key))
PY
```

## 7. Required Next Patch Direction

다음 패치는 Stage label을 더 늘리는 작업이 아니다.
이미 Stage label은 있고, 오히려 오해를 만든다.

정확한 순서:

```text
P1. Brain/Web canonical enabled run을 실제 source-backed로 닫기
P2. Brain/Web strict promotion row를 representative census_stage_status에 올리기
P3. Samsung/Hynix C06/HBM full thesis smoke를 planning-only에서 execution으로 전환
P4. full thesis 점수는 FULL_E2R_100 scope로만 기록
P5. 전 아키타입 Evidence Contract v2와 source-backed replay parity를 닫기
P6. provider failure/material source gap은 낮은 점수 final이 아니라 Pending으로 유지
P7. meaningful/brain_web/full_thesis target gate가 exit 0이 되는지 별도 검증
```

### P1. Brain/Web source-backed run

현재 canonical run:

```text
brain_web_mode=disabled
planner_run_count=0
web_search_task_count=0
web_fetched_document_count=0
llm_claim_extractor_attempt_count=0
brain_to_census_stage_exported_count=0
```

다음 완료 조건:

```text
brain_web_mode=enabled
real planner provider success > 0
source task executions exist
evidence_documents / evidence_anchors exist
accepted claims are not snapshot-only
score contributions support accepted claim ids
StageCourt traces support same claim/contribution ids
representative stage row promotion > 0
brain_web_readiness_gate_audit.verdict = READY_FOR_BRAIN_WEB_EVIDENCE_PASS
```

### P2. Samsung/Hynix full thesis execution

현재:

```text
full_thesis_smoke_tasks.jsonl = 14 planning-only tasks
score_allowed_before_execution=false
full_thesis_stage=FULL_THESIS_NOT_RUN
```

다음 완료 조건:

```text
005930 / 000660 C06 HBM SourceTasks executed
required primitives investigated:
  - named_customer_or_customer_class
  - qualification_status
  - capacity_allocation_or_sold_out
  - shipment_or_revenue_mix
  - cash_or_revision_conversion
  - repeat_evidence_family
  - negative_guard_current_status
claim -> primitive -> contribution -> StageCourt -> full thesis row closed
material gap이면 Pending, 충분하면 full_thesis_stage 기록
```

주의:

```text
삼성전자/하이닉스는 fixture다.
symbol-specific scoring branch를 만들면 안 된다.
```

### P3. Full thesis scope guard

운영 thesis 점수는 아래 조건을 만족해야만 쓸 수 있다.

```text
score_scope=FULL_E2R_100
stage_scope=FULL_THESIS
verified_score not null
full_e2r_verified_score not null
nonzero ScoreContribution has support_claim_ids
source anchor exists
target relation direct/current/accepted
material gap interval resolved or explicitly pending
```

이 조건이 없으면:

```text
operator_stage_use=NOT_FULL_THESIS_STAGE
operator_score_use=NOT_FULL_E2R_SCORE
```

로 남겨야 한다.

## 8. Reviewer Attack List

다음 에이전트는 아래 질문으로 이 상태를 공격해야 한다.

```text
1. stage_status와 stage_map의 분포가 정말 같은가?
2. canonical_stage=2 또는 3-Red가 full thesis로 출력되는 곳이 남았는가?
3. verified_score가 null이 아닌 row가 하나라도 생겼는데 FULL_E2R_100 scope가 아닌가?
4. full_thesis_stage != FULL_THESIS_NOT_RUN인데 full thesis claim/score/StageCourt trace가 없는가?
5. Brain/Web disabled run인데 brain_web_evidence_pass=true가 되는가?
6. DISABLED_HONESTY_PASS를 live acquisition pass로 읽는 문서가 있는가?
7. Samsung/Hynix event_evidence_score=4.0을 HBM/C06 thesis score로 설명하는 문서가 있는가?
8. SourceTask satisfaction PASS가 live source pass처럼 표현되는가?
9. PrimitiveState chain PASS가 full thesis pass처럼 표현되는가?
10. source_proxy_only 연구자료가 운영 score contribution으로 들어갈 수 있는가?
11. provider failure가 낮은 점수 final로 바뀌는 경로가 남았는가?
12. Stage label을 늘리는 patch가 증거 claim execution보다 먼저 나오려 하는가?
```

## 9. Final Diagnosis

현재 상태를 한 문장으로:

> 지금은 "가짜 완료 선언을 막는 상태판"이 만들어진 상태이고, "실제 운영 thesis 점수/Stage 산출"은 아직 안 된 상태다.

정확한 답:

```text
Stage가 있는 애들은 있다.
그 Stage는 CENSUS_EVENT_BOARD 상태 label이다.
full thesis 운영 Stage가 있는 애들은 현재 없다.
```

다음 패치는:

```text
Stage 이름을 바꾸거나 늘리는 작업이 아니라,
실제 source-backed claim을 가져와 full thesis score/stage row까지 연결하는 작업이어야 한다.
```

쉬운 예:

```text
지금은 "채점표 위조 방지 장치"까지 만든 상태다.
이제 해야 할 일은 실제 답안지를 가져와 채점하는 것이다.
```
