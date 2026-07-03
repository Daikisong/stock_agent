# Census v4 0701 v45 Stage Existence / Seed Materialization Cross-Audit

작성일: 2026-07-03 KST

## 0. 결론

질문:

```text
뭔가 잘못되고 있는 거 맞지?
stage가 있는 애들이 있긴 해?
```

직접 답:

```text
Stage처럼 보이는 row는 있다.
하지만 운영 FULL_THESIS Stage가 있는 row는 없다.
```

현재 canonical output 기준으로 정확히 나누면:

```text
CENSUS_EVENT_BOARD 상태판 Stage:
  있음
  rows = 3391
  non-Stage0 rows = 85

운영 FULL_THESIS Stage:
  없음
  rows = 0

FULL_E2R_100 verified score:
  없음
  rows = 0
```

따라서 지금 상태를 이렇게 말하면 틀리다.

```text
Stage가 85개 있으니 운영 Stage가 생겼다.
```

이렇게 말해야 한다.

```text
상태판 Stage1/Stage2-Watch/Red row는 85개 있다.
하지만 그 row는 전부 CENSUS_EVENT_BOARD이고,
operator가 쓸 FULL_THESIS 운영 Stage는 아직 0개다.
```

쉬운 예:

```text
병원 접수 화면에 "진료 필요"라고 뜬 환자가 85명 있다.
하지만 의사가 진료하고 검사 결과까지 보고 최종 진단서를 쓴 환자는 아직 0명이다.

CENSUS_EVENT_BOARD = 접수/상태판
FULL_THESIS = 진료 + 검사 + 진단서 + 최종 판정
```

## 1. 검증 기준 파일

이번 확인은 아래 산출물을 직접 대조했다.

```text
output/census_v4/2026-07-01/census_stage_status.jsonl
output/census_v4/2026-07-01/full_thesis_refresh_queue.jsonl
output/census_v4/2026-07-01/research_brain_full_thesis_seed_events.jsonl

docs/operational/census_mode_v4_acceptance_report.md
docs/operational/census_mode_v4_readiness_verdict.md.json
docs/operational/census_mode_v4_brain_web_readiness_gate_audit.json
docs/operational/census_mode_v4_full_thesis_refresh_queue_audit.json
docs/operational/census_mode_v4_full_thesis_production_runner_audit.json
```

주의:

```text
docs/operational/census_mode_v4_readiness_verdict.md.json
```

에는 PASS/FAIL 핵심값이 있고, Stage 분포 전체는 `census_stage_status.jsonl`과
`census_mode_v4_acceptance_report.md`에서 확인해야 한다.

## 2. Stage row 직접 카운트

`output/census_v4/2026-07-01/census_stage_status.jsonl` 기준:

```text
stage_status rows = 3391

stage_scope:
  CENSUS_EVENT_BOARD = 3391

operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3391

full_thesis_stage:
  FULL_THESIS_NOT_RUN = 3391

base_stage:
  Stage0 = 3306
  Stage1 = 54
  Stage2-Watch = 30
  Red = 1

stage_signal:
  NO_CURRENT_CATALYST = 3306
  OFFICIAL_EVENT_WATCH = 36
  EVIDENCE_INSUFFICIENT = 10
  MATERIAL_CLAIM_WATCH = 30
  SOURCE_PENDING = 8
  RISK_REVIEW = 1

score_scale:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67

FULL_THESIS rows = 0
FULL_E2R_100 rows = 0
non-Stage0 event-board rows = 85
```

해석:

```text
base_stage 값만 보면 Stage1/Stage2-Watch/Red가 있다.
하지만 stage_scope가 전부 CENSUS_EVENT_BOARD이고,
operator_stage_use가 전부 NOT_FULL_THESIS_STAGE다.
```

즉 `base_stage` 하나만 보고 운영 Stage라고 말하면 audit fail이다.

## 3. 실제 샘플 해석

예를 들어 첫 non-Stage0 샘플 중 하나:

```text
symbol = 000660
company_name = SK하이닉스
base_stage = Stage1
stage_signal = OFFICIAL_EVENT_WATCH
stage_scope = CENSUS_EVENT_BOARD
operator_stage_use = NOT_FULL_THESIS_STAGE
full_thesis_stage = FULL_THESIS_NOT_RUN
score_scale = EVENT_WEIGHTED_PARTIAL
accepted_claim_count = 1
```

이 row를 이렇게 해석하면 틀리다.

```text
SK하이닉스 운영 Stage1이다.
```

정확한 해석:

```text
SK하이닉스는 census 상태판에서 공식 이벤트 watch로 잡혔다.
하지만 C06 HBM 전체 thesis 운영 Stage는 아직 안 돌았다.
따라서 운영 점수/Stage로 말하면 안 된다.
```

쉬운 예:

```text
"접수됨"과 "최종 진단됨"은 다르다.
SK하이닉스 Stage1 row는 접수/상태판 쪽이고,
FULL_THESIS_NOT_RUN이면 최종 진단은 아직 없는 것이다.
```

## 4. Seed chain 직접 카운트

`full_thesis_refresh_queue`와 Research Brain seed는 생겼다.

```text
full_thesis_refresh_queue rows = 85
research_brain_full_thesis_seed_events rows = 85
```

하지만 canonical disabled run에서는 Brain/Web 자체가 꺼져 있다.

`docs/operational/census_mode_v4_readiness_verdict.md.json` 기준:

```text
brain_web_attempt.verdict = NOT_REQUESTED
brain_web_attempt.full_thesis_seed_event_count = 85
brain_web_attempt.full_thesis_seed_consumed_by_research_brain = false
brain_web_attempt.full_thesis_seed_planner_run_count = 0
brain_web_attempt.full_thesis_seed_real_provider_success_count = 0
brain_web_attempt.full_thesis_seed_source_task_execution_count = 0
brain_web_attempt.full_thesis_seed_accepted_claim_count = 0
brain_web_attempt.full_thesis_seed_stagecourt_trace_count = 0
brain_web_attempt.full_thesis_seed_materialized_to_stagecourt = false
```

`docs/operational/census_mode_v4_brain_web_readiness_gate_audit.json` 기준도 같다.

```text
verdict = NOT_REQUESTED
full_thesis_seed_event_count = 85
full_thesis_seed_consumed_by_research_brain = false
full_thesis_seed_planner_run_count = 0
full_thesis_seed_real_provider_success_count = 0
full_thesis_seed_source_task_execution_count = 0
full_thesis_seed_accepted_claim_count = 0
full_thesis_seed_stagecourt_trace_count = 0
full_thesis_seed_materialized_to_stagecourt = false
```

해석:

```text
queue -> seed file
```

까지는 생겼다.

하지만 canonical run에서는 아직:

```text
seed -> real planner provider success
seed -> source task execution
seed -> accepted claim
seed -> score contribution
seed -> StageCourt trace
seed -> FULL_THESIS row
```

가 전부 0이다.

## 5. Provider-none smoke의 의미

v44에서 `brain_web_mode=enabled`, `brain_planner_provider=none` smoke를 추가했다.

이 smoke의 목적은 점수/Stage 생성이 아니라 배선 정직성 확인이다.

현재 기대값:

```text
full_thesis_seed_event_count = 85
full_thesis_seed_consumed_by_research_brain = false
full_thesis_seed_planner_run_count = 2
full_thesis_seed_real_provider_success_count = 0
full_thesis_seed_source_task_execution_count = 0
full_thesis_seed_accepted_claim_count = 0
full_thesis_seed_stagecourt_trace_count = 0
full_thesis_seed_materialized_to_stagecourt = false
brain_web_readiness_gate.verdict = BLOCKED
blocker includes:
  full-thesis seed planner runs have no real-provider success
```

중요한 점:

```text
planner_run_count > 0
```

는 "접수 시스템에 예약 row가 생김"이다.

아래와 같지 않다.

```text
real provider가 seed를 실제로 처리했다
source task가 실행됐다
accepted claim이 생겼다
StageCourt trace가 생겼다
```

따라서 provider-none smoke에서 `consumed=false`가 맞다.

## 6. 지금 잘못되고 있는 지점

파이프라인 전체가 아무것도 못 하는 상태는 아니다.

실제로 되는 것:

```text
전 종목 census 상태판 생성
CensusAssessmentEvent / CandidateEvent 분리
공식 이벤트 기반 accepted claim 일부 생성
EVENT_WEIGHTED_PARTIAL 상태판 점수 일부 생성
비 Stage0 상태판 row를 FULL_THESIS refresh queue로 분리
queue를 Research Brain seed event 파일로 변환
seed/materialization count를 honesty audit에 노출
```

하지만 아직 운영으로 부족한 것:

```text
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0
seed source task execution = 0
seed accepted claim = 0
seed StageCourt trace = 0
required 32개 아키타입 source-backed replay = 6/32
Brain/Web evidence pass = false
Meaningful operational stage pass = false
```

핵심 문제:

```text
상태판은 생겼지만,
상태판 row를 운영 FULL_THESIS thesis로 완성하는 실행 체인이 아직 닫히지 않았다.
```

## 7. 다음 패치 방향

다음 패치는 가중치, threshold, Stage 이름을 만지는 작업이 아니다.

우선 닫아야 하는 체인:

```text
CENSUS_EVENT_BOARD non-Stage0 row
  -> full_thesis_refresh_queue
  -> research_brain_full_thesis_seed_event
  -> real/frozen-live planner provider success
  -> bounded source task execution
  -> Evidence OS accepted claim
  -> primitive state
  -> score contribution
  -> StageCourt trace
  -> FULL_THESIS stage row
```

구현 원칙:

```text
1. seed event는 planner input일 뿐 score evidence가 아니다.
2. provider none / provider error는 낮은 점수 확정이 아니라 BLOCKED/PENDING이다.
3. source task가 실행되지 않았으면 materialized=false다.
4. accepted claim이 없으면 score contribution도 StageCourt trace도 만들면 안 된다.
5. StageCourt trace가 있어도 FULL_THESIS green/yellow gate primitive coverage가 없으면 승격하지 않는다.
6. event-board partial score를 FULL_E2R_100으로 복사하면 안 된다.
```

쉬운 예:

```text
공식 이벤트가 "계약 공시 있음"을 알려 준다.
이건 "조사해라"라는 알림이다.

점수에 들어가려면 원문에서:
  계약 금액
  기간
  상대방
  대상회사 직접성
  현재성
이 accepted claim으로 닫혀야 한다.

제목만 보고 C05/C06 계약 품질 점수를 주면 다시 같은 오류가 난다.
```

## 8. 다음 에이전트 공격 질문

다음 에이전트는 완료 주장 전에 아래를 먼저 공격해야 한다.

```text
1. base_stage만 보고 Stage가 있다고 주장하지 않았는가?
2. stage_scope=FULL_THESIS row가 실제로 생겼는가?
3. operator_stage_use=FULL_THESIS_STAGE row가 실제로 생겼는가?
4. full_thesis_stage가 FULL_THESIS_NOT_RUN이 아닌 row가 있는가?
5. score_scale=FULL_E2R_100 verified score row가 있는가?
6. EVENT_WEIGHTED_PARTIAL을 운영 점수로 읽고 있지 않은가?
7. full_thesis_refresh_queue 85개를 Stage 승격으로 착각하지 않았는가?
8. seed planner pending row를 consumed=true로 착각하지 않았는가?
9. seed source task execution이 candidate_event_id와 연결되어 있는가?
10. seed accepted claim이 source anchor, target directness, as_of_date, lifecycle을 통과했는가?
11. accepted claim이 primitive state로 이어졌는가?
12. primitive state가 score contribution으로 이어졌는가?
13. score contribution이 StageCourt trace로 이어졌는가?
14. StageCourt trace가 FULL_THESIS row로 승격되었는가?
15. source task / claim / stage trace 중 하나라도 비었는데 materialized=true로 표시하지 않았는가?
16. provider failure를 낮은 점수 확정으로 바꾸지 않았는가?
17. 삼성전자/SK하이닉스 smoke를 운영 pass로 오해하지 않았는가?
18. CENSUS_EVENT_BOARD Stage1/Stage2-Watch를 C06/C08/C15 thesis Stage로 섞지 않았는가?
```

## 9. 패치 완료 기준

다음 중 하나라도 없으면 아직 완료가 아니다.

```text
FULL_THESIS rows > 0
FULL_E2R_100 verified score rows > 0
seed source task execution count > 0
seed accepted claim count > 0
seed StageCourt trace count > 0
all nonzero score contributions claim-backed
full thesis promotion blocked when green primitives missing
provider failure remains pending/blocker, not low score
```

다만 `FULL_THESIS rows > 0` 자체도 충분조건은 아니다.

아래가 같이 맞아야 한다.

```text
stage_scope = FULL_THESIS
operator_stage_use = FULL_THESIS_STAGE
score_scale = FULL_E2R_100
support_claim_ids present
source anchors valid
target direct/current
primitive coverage sufficient
StageCourt blocker empty or non-material
```

## 10. 현재 판정

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS:
  true

상태판 Stage 존재:
  true

운영 FULL_THESIS Stage 존재:
  false

Brain/Web evidence pass:
  false

Meaningful operational stage pass:
  false

다음 패치:
  seed -> real provider/source task/claim/StageCourt/FULL_THESIS full chain materialization
```

짧게 말하면:

```text
현재 결과는 "전 종목 상태판"으로는 의미가 있다.
하지만 "실제 운영 E2R full thesis 점수/Stage"로는 아직 0건이다.
```

## 11. 검증 명령

관련 묶음:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_artifact_manifest \
  tests.test_census_v4_manifest_counts_match_report -v

Ran 93 tests in 36.941s
OK
```

전체 suite:

```text
PYTHONPATH=src python -m unittest discover -s tests -v

Ran 5075 tests in 205.207s
OK
```
