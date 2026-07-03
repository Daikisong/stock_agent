# Census v4 0701 v43 Full Thesis Queue Seed To Research Brain Input

작성일: 2026-07-02 KST

## 0. 결론

v42까지의 진실은 이랬다.

```text
full_thesis_refresh_queue = 85개
production FULL_THESIS candidate = 0개
FULL_THESIS 운영 Stage row = 0개
```

v43에서 확인하고 고친 핵심은 이거다.

```text
기존 순서:
  Research Brain 실행
  -> 그 다음 full_thesis_refresh_queue 생성

문제:
  queue가 생겨도 Research Brain이 그 queue를 입력으로 볼 수 없었다.

v43 순서:
  CENSUS_EVENT_BOARD stage row 생성
  -> full_thesis_refresh_queue 생성
  -> queue를 Research Brain용 seed event JSONL로 변환
  -> Research Brain이 seed event를 planner 입력 후보로 먼저 사용
```

쉬운 예:

```text
예전:
  병원 접수표를 의사가 진료 끝낸 뒤에 만든 상태.
  "진료 대기 85명"은 보이지만, 의사는 그 명단을 본 적이 없다.

이제:
  접수표 85명을 먼저 만들고,
  의사에게 "이 명단부터 봐라"라고 넘긴다.

단:
  접수표 자체는 진단서가 아니다.
  seed event 자체는 점수 증거가 아니며, Stage 승급도 아니다.
```

## 1. 현재 Stage가 있는가

정확히 나누면:

```text
CENSUS_EVENT_BOARD 상태판 Stage:
  있음.
  row_count = 3391
  non_Stage0 = 85

operator-admissible FULL_THESIS Stage:
  없음.
  row_count = 0

verified FULL_E2R_100 score:
  없음.
  row_count = 0
```

즉 "Stage가 있는 애들이 있긴 해?"라는 질문에는 이렇게 답해야 한다.

```text
상태판 Stage는 있다.
하지만 실제 운영 점수/Stage로 쓸 FULL_THESIS row는 아직 없다.
```

SK하이닉스 예:

```text
000660 SK하이닉스 seed event는 생성됐다.
source_stage_signal = OFFICIAL_EVENT_WATCH
source_stage_decision_status = FINAL

하지만 이건 "정밀평가 대기열에 올라갔다"는 뜻이다.
C06 HBM full-thesis 점수가 닫혔다는 뜻이 아니다.
```

## 2. 코드 패치

수정 파일:

```text
src/e2r/census/census_runner_v4.py
src/e2r/research_brain/v4_schemas.py
src/e2r/research_brain/v4_production_orchestrator.py
tests/test_census_v4_full_thesis_smoke_tasks.py
tests/test_research_brain_v4_operational_modes.py
```

### 2.1 Census 실행 순서 변경

`run_census_mode_v4()`에서 Research Brain 실행 전에 아래를 먼저 만든다.

```text
atomic_rows
stage_rows
pre_promotion_refresh_queue
research_brain_full_thesis_seed_events.jsonl
```

그 다음 `_run_brain_web_attempt()`에 seed path와 seed count를 넘긴다.

### 2.2 queue -> seed event 변환

새 artifact:

```text
output/census_v4/2026-07-01/research_brain_full_thesis_seed_events.jsonl
docs/operational/census_mode_v4_research_brain_full_thesis_seed_events.jsonl
```

각 seed event는 이렇게 표시된다.

```json
{
  "source_family": "CensusFullThesisQueue",
  "event_type": "full_thesis_refresh_seed",
  "seed_role": "planner_input_only",
  "score_evidence_allowed": false,
  "stage_promotion_allowed_before_execution": false
}
```

중요:

```text
score_evidence_allowed = false
stage_promotion_allowed_before_execution = false
```

이 두 필드가 핵심이다. seed는 조사 시작점이지 점수 증거가 아니다.

### 2.3 Research Brain config 확장

`ProductionShadowV4Config`에 추가:

```python
candidate_event_seed_path: str | None = None
```

`run_research_brain_v4_production_shadow()`는 이제:

```text
candidate_event_seed_path에서 seed event 로드
daily discovery event와 합침
중복 제거
planner 실행 순서에서 seed event 우선
```

### 2.4 seed 우선순위 고정

패치 전에는 seed를 합쳐도 `DART/KIND/KRX/IR/CompanyGuide` 우선순위 때문에
daily discovery 후보가 planner slot을 먼저 먹을 수 있었다.

v43은 다음을 고정했다.

```text
source_family = CensusFullThesisQueue
또는 event_type = full_thesis_refresh_seed
또는 structured_payload.seed_role = planner_input_only
이면 planner candidate order에서 우선 처리
```

이건 종목명/아키타입 하드코딩이 아니다.

```text
나쁜 하드코딩:
  if symbol == "005930": 먼저 조사
  if archetype == "C06": 특정 검색어 생성

이번 패치:
  이미 감사 queue로 만들어진 planner seed를 먼저 planner에 넘김
```

## 3. canonical 재생성 결과

명령:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode LEDGER_REFRESH_CENSUS \
  --brain-web-mode disabled \
  --target-gate anti_fake \
  --write-operational-docs true \
  --fail-on-critical-audit true
```

결과:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

핵심 숫자:

```text
stage_scope_distribution = {'CENSUS_EVENT_BOARD': 3391}
operator_stage_use_distribution = {'NOT_FULL_THESIS_STAGE': 3391}
stage_decision_status_distribution =
  FINAL: 36
  NO_CURRENT_CATALYST: 3306
  PENDING_MATERIAL_GAPS: 30
  RISK_REVIEW: 1
  SOURCE_PENDING: 18

event_board_non_stage0_count = 85
full_thesis_stage_row_count = 0
verified_score_present_count = 0

full_thesis_refresh_queue row count = 85
research_brain_full_thesis_seed_events row count = 85
operational copied seed row count = 85
```

`readiness_verdict.json`:

```text
brain_web_attempt.attempt_mode = disabled
brain_web_attempt.verdict = NOT_REQUESTED
brain_web_attempt.full_thesis_seed_event_count = 85
brain_web_attempt.full_thesis_seed_consumed_by_research_brain = false

brain_web_readiness_gate.verdict = NOT_REQUESTED
brain_web_readiness_gate.full_thesis_seed_event_count = 85
brain_web_readiness_gate.full_thesis_seed_consumed_by_research_brain = false
```

`full_thesis_production_runner_audit.json`:

```text
full_thesis_refresh_queue_candidate_count = 85
candidate_row_count = 0
candidate_source_counts = {}
refresh_queue_materialized_candidate_count = 0
refresh_queue_unmaterialized_candidate_count = 85
promoted_full_thesis_row_count = 0
```

## 4. enabled wiring 교차검증

점수나 Stage를 만들지 않고 배선만 보기 위해 임시 출력에서 실행했다.

조건:

```text
brain_web_mode = enabled
brain_planner_provider = none
brain_universe_limit = 2
brain_planner_success_limit = 1
brain_planner_batch_size = 1
write_operational_docs = false
fail_on_critical_audit = false
```

결과:

```text
full_thesis_seed_event_count = 85
full_thesis_seed_consumed_by_research_brain = true
planner_run_count = 21
first_planner_symbol = 000660
first_planner_source_family = CensusFullThesisQueue
brain_web_readiness_gate.verdict = BLOCKED
accepted_claim_count = 0
```

해석:

```text
seed는 Research Brain 입력으로 실제 전달된다.
planner 첫 대상도 queue seed다.
하지만 provider none이라 source-backed accepted claim은 0개다.
따라서 gate BLOCKED가 맞다.
```

이 교차검증은 "배선이 연결됐다"만 증명한다.
운영 Stage가 생겼다는 증거가 아니다.

## 5. 테스트

타깃 테스트:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_candidate_event_seed_path_is_prioritized_before_daily_discovery -v

OK
```

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks.CensusV4FullThesisSmokeTaskTests.test_event_board_non_stage0_rows_are_queued_for_full_thesis_refresh_not_promoted -v

OK
```

관련 묶음:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_artifact_manifest \
  tests.test_census_v4_manifest_counts_match_report -v

Ran 92 tests in 34.525s
OK
```

전체 suite:

```text
PYTHONPATH=src python -m unittest discover -s tests -v

Ran 5074 tests in 203.377s
OK
```

## 6. 아직 안 된 것

아직 안 된 것을 분명히 적는다.

```text
1. canonical run은 brain_web_mode=disabled라 seed를 생성만 하고 소비하지 않는다.
2. enabled wiring smoke는 planner_provider=none이라 accepted claim을 만들지 않는다.
3. source_task_execution -> evidence_document -> evidence_anchor -> accepted_claim -> score_contribution -> primitive_state -> stagecourt_trace -> FULL_THESIS row 경로는 아직 닫히지 않았다.
4. production FULL_THESIS row는 계속 0개다.
5. verified FULL_E2R_100 score row도 계속 0개다.
```

즉 이번 패치는:

```text
queue가 Research Brain 입력으로 들어갈 수 있는 배선을 만든 것
```

이지:

```text
queue 85개를 실제 Stage로 승격한 것
```

이 아니다.

## 7. 다음 에이전트 공격 포인트

다음 에이전트는 아래를 먼저 찌르면 된다.

```text
1. real planner/provider를 켠 production daily preset에서 seed 85개 중 몇 개가 source_task_execution으로 이어지는가?
2. source_task_execution이 official-first budget을 지키는가?
3. seed event의 score_evidence_allowed=false가 끝까지 유지되는가?
4. seed 자체가 score_contribution support_claim_id로 새지 않는가?
5. accepted_claim이 생긴 symbol만 stagecourt_trace candidate가 되는가?
6. refresh_queue_materialized_candidate_count가 candidate_row_count와 일치하는가?
7. materialized candidate가 있어도 Green gate/mandatory primitive coverage 없이 FULL_THESIS로 승격하지 않는가?
8. provider failure나 timeout이 낮은 점수 확정으로 바뀌지 않는가?
9. daily discovery 후보가 seed를 밀어내지 않는가?
10. seed가 많은 날에도 planner/source budget이 production daily 정책을 지키는가?
```

## 8. 다음 패치 방향

v44에서 해야 할 일:

```text
1. real planner/provider 또는 frozen-live provider로 full_thesis seed를 source task까지 실행한다.
2. source task가 official-first로 원문을 가져오는지 검증한다.
3. accepted_claim이 생기면 score_contribution/primitive_state/stagecourt_trace까지 leaf chain을 닫는다.
4. 그 trace가 있는 symbol만 production FULL_THESIS candidate로 materialize한다.
5. 여전히 source-backed claim이 없으면 Stage0/NoCurrentCatalyst 또는 Source/Provider Pending으로 남긴다.
```

절대 하면 안 되는 것:

```text
queue seed가 있으니 Stage1/Stage2로 승격
event title만 보고 점수 부여
provider none인데 낮은 점수 확정
daily discovery 후보를 이유로 queue seed planner 실행을 미룸
```

## 9. 최종 판정

```text
v43 patch verdict:
  PASS for queue -> Research Brain seed wiring

operational Stage verdict:
  NOT READY

FULL_THESIS production verdict:
  FALSE

Brain/Web evidence verdict:
  canonical disabled run = NOT_REQUESTED
  enabled wiring smoke = BLOCKED, as expected

current hard truth:
  CENSUS_EVENT_BOARD Stage exists.
  FULL_THESIS operating Stage does not exist yet.
```
