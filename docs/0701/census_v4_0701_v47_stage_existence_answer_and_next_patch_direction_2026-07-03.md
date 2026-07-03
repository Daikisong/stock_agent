# Census v4 0701 v47 Stage Existence Answer And Next Patch Direction

작성일: 2026-07-03 KST

## 0. 한 줄 결론

질문:

```text
뭔가 잘못되고 있는 거 맞지?
stage가 있는 애들이 있긴 해?
```

답:

```text
Stage label은 있다.
하지만 현재 canonical run에는 운영 FULL_THESIS Stage가 0개다.
```

즉 지금 output을 이렇게 읽으면 맞다.

```text
전체 종목 상태판:
  있음

실제 E2R full thesis 진단서:
  아직 없음
```

쉬운 예:

```text
병원 접수표에는 "감기 의심", "정밀검사 필요", "응급 아님" 같은 상태가 적혀 있다.
하지만 의사가 검사 결과와 진단서를 작성한 것은 아니다.

현재 Census v4 canonical output은 접수표에 가깝다.
FULL_THESIS 운영 Stage는 진단서에 해당하는데, 현재 0개다.
```

## 1. 직접 검증 숫자

검증 대상:

```text
output/census_v4/2026-07-01
```

직접 leaf를 세면 아래와 같다.

```text
census_stage_status rows = 3391

stage_scope:
  CENSUS_EVENT_BOARD = 3391

operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3391

base_stage:
  Stage0 = 3306
  Stage1 = 54
  Stage2-Watch = 30
  Red = 1

full_thesis_stage:
  FULL_THESIS_NOT_RUN = 3391

score_scale:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67

FULL_THESIS rows = 0
FULL_E2R_100 verified score rows = 0
non-Stage0 event-board rows = 85
```

해석:

```text
Stage1 / Stage2-Watch / Red row 85개는 있다.
하지만 전부 CENSUS_EVENT_BOARD다.
운영자가 "E2R thesis Stage"로 써도 되는 row는 0개다.
```

## 2. 왜 헷갈렸나

기존 output에는 `base_stage`가 있었다.

예:

```text
base_stage = Stage2-Watch
```

이 값만 보면 사람이 이렇게 오해한다.

```text
이 종목은 진짜 Stage2-Watch thesis구나.
```

하지만 같은 row의 다른 필드를 같이 보면 실제 의미는 다르다.

```text
stage_scope = CENSUS_EVENT_BOARD
operator_stage_use = NOT_FULL_THESIS_STAGE
full_thesis_stage = FULL_THESIS_NOT_RUN
score_scale = EVENT_WEIGHTED_PARTIAL 또는 NO_SCORE
```

따라서 올바른 해석은 이렇다.

```text
이 종목은 Census 상태판에서 watch/event 신호가 있다.
아직 full thesis 운영 Stage는 아니다.
```

쉬운 예:

```text
택배 앱에서 "배송 준비 중"이라고 떴다.
이건 물건이 도착했다는 뜻이 아니다.
도착 여부를 보려면 "배송 완료" 상태를 봐야 한다.

여기서 "배송 완료"가 FULL_THESIS다.
현재 배송 완료는 0개다.
```

## 3. v46 패치가 막은 오해

v46에서 새 leaf artifact를 추가했다.

```text
full_thesis_seed_materialization_trace.jsonl
```

이 leaf는 non-Stage0 event-board row 85개가 full thesis refresh seed로 들어간 뒤 어디서 멈췄는지 보여준다.

직접 카운트:

```text
full_thesis_seed_materialization_trace rows = 85

materialization_status:
  PLANNER_NOT_RUN = 85

final_stage_scope:
  CENSUS_EVENT_BOARD = 85

final_operator_stage_use:
  NOT_FULL_THESIS_STAGE = 85

final_full_thesis_stage:
  FULL_THESIS_NOT_RUN = 85

planner_run_count sum = 0
source_task_execution_count sum = 0
accepted_claim_count sum = 0
stagecourt_trace_count sum = 0
```

이제 다음 에이전트는 합계 report를 믿지 않아도 된다.

```text
seed 85개 각각이 planner/source/claim/StageCourt 중 어디까지 갔는지
row 단위로 직접 검증할 수 있다.
```

## 4. 현재 상태가 잘못인가

두 가지로 나눠야 한다.

### 4.1 정직한 상태판으로 보면 맞다

현재 canonical disabled run은 아래처럼 말하면 정직하다.

```text
전체 KRX universe 3391개를 Census 상태판에 올렸다.
그중 85개는 Stage0이 아닌 event-board signal이 있다.
하지만 Brain/Web full thesis는 disabled였고,
planner/source/claim/StageCourt materialization은 아직 없다.
따라서 운영 FULL_THESIS Stage는 없다.
```

이건 틀린 게 아니다.

### 4.2 운영 Stage처럼 말하면 틀리다

아래처럼 말하면 틀리다.

```text
Stage2-Watch 30개가 있으니 운영 E2R Stage2 후보 30개다.
Red 1개가 있으니 운영 reject thesis 1개다.
삼성전자/하이닉스도 Census row가 있으니 HBM/C06 thesis 평가가 끝났다.
```

왜냐하면 현재 row들은 accepted claim과 score contribution을 거쳐 StageCourt에서 full thesis로 승격된 row가 아니기 때문이다.

## 5. anti-fake pass의 정확한 의미

현재 canonical rerun 결과:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

이 pass는 아래를 뜻한다.

```text
가짜로 FULL_THESIS인 척하지 않는다.
leaf artifact와 manifest가 있고,
legacy/v1/v3 runner로 production pass를 주장하지 못하게 막는다.
상태판 row의 scope/score scale/operator-use가 분리되어 있다.
```

하지만 이 pass는 아래를 뜻하지 않는다.

```text
운영 daily watchlist가 완성됐다.
전 아키타입 full thesis Stage가 닫혔다.
삼성전자/하이닉스 같은 live candidate 점수가 확정됐다.
Brain/Web/IR/report 수집이 source-backed claim으로 이어졌다.
```

## 6. 새 artifact 검증

manifest entry:

```text
name = full_thesis_seed_materialization_trace.jsonl
row_count = 85
byte_size = 89627
sha256 = 9f48ac0117dd6779adcbc965fe9b22ebacdefcc3807b38ccae94f3d62a27deb1
```

즉 다음 에이전트는 아래 두 파일을 비교하면 된다.

```text
output/census_v4/2026-07-01/full_thesis_seed_materialization_trace.jsonl
docs/operational/census_mode_v4_full_thesis_seed_materialization_trace.jsonl
```

같은 row count와 같은 상태 분포가 나와야 한다.

## 7. 코드 패치 범위

이번 패치는 점수나 Stage threshold를 건드리지 않았다.

주요 목적:

```text
full thesis seed가 어디서 멈췄는지 leaf로 남긴다.
docs/operational에도 같은 leaf를 복사한다.
manifest가 새 leaf hash/row_count/size를 포함하게 한다.
테스트가 seed별 materialization status를 검증한다.
```

주요 코드:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_full_thesis_smoke_tasks.py
tests/test_census_v4_artifact_manifest.py
```

주의:

```text
이 패치는 FULL_THESIS를 만들지 않는다.
FULL_THESIS가 아직 없다는 사실을 더 못 속이게 만든다.
```

## 8. 테스트 결과

타깃 테스트:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks.CensusV4FullThesisSmokeTaskTests.test_event_board_non_stage0_rows_are_queued_for_full_thesis_refresh_not_promoted \
  tests.test_census_v4_full_thesis_smoke_tasks.CensusV4FullThesisSmokeTaskTests.test_enabled_provider_none_measures_seed_planner_consumption_without_materialization \
  tests.test_census_v4_artifact_manifest.CensusV4ArtifactManifestTests.test_manifest_has_hash_size_and_row_count_for_every_leaf -v

Ran 3 tests in 11.369s
OK
```

관련 감사 suite:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_artifact_manifest \
  tests.test_census_v4_manifest_counts_match_report \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_goal_required_audits -v

Ran 93 tests in 40.287s
OK
```

전체 unittest:

```text
PYTHONPATH=src python -m unittest discover -s tests -v

Ran 5075 tests in 214.423s
OK
```

## 9. 다음 패치가 닫아야 할 실제 경로

현재는 아래에서 멈췄다.

```text
event-board row
  -> full thesis refresh queue
  -> full thesis seed
  -> PLANNER_NOT_RUN
```

다음 패치는 최소한 아래 전체 사슬을 실제 artifact로 닫아야 한다.

```text
full thesis seed
  -> real planner output
  -> bounded source task
  -> source document / anchor
  -> accepted claim
  -> primitive mapping
  -> score contribution
  -> StageCourt trace
  -> FULL_THESIS promotion decision
```

중간에서 실패하면 낮은 점수로 확정하면 안 된다.

예:

```text
planner provider 실패
  -> ProviderPending / PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS
  -> 0점 Stage0 확정 금지

source task는 했지만 원문 anchor 없음
  -> ACCEPTED_CLAIM_NOT_CREATED
  -> 점수 반영 금지

claim은 있지만 Green 필수 primitive 부족
  -> STAGECOURT_READY_NOT_PROMOTED 또는 material gap pending
  -> Green 확정 금지
```

## 10. 다음 에이전트 공격 질문

다음 에이전트는 아래를 먼저 물어야 한다.

```text
1. FULL_THESIS row가 아직 0개인가?
2. FULL_E2R_100 verified score row가 아직 0개인가?
3. non-Stage0 85개가 아직 CENSUS_EVENT_BOARD인가?
4. seed 85개 materialization_status가 아직 PLANNER_NOT_RUN인가?
5. planner/source/claim/stagecourt count 합계가 아직 0인가?
6. anti-fake pass를 operational pass처럼 말하고 있지는 않은가?
7. EVENT_WEIGHTED_PARTIAL을 verified_score처럼 쓰고 있지는 않은가?
8. CandidateEvent나 CensusAssessmentEvent 자체가 score evidence로 새고 있지는 않은가?
9. source_proxy_only 연구자료가 production claim으로 들어가지는 않았는가?
10. provider failure를 낮은 score로 확정하고 있지는 않은가?
```

## 11. 최종 판정

```text
현재 상태:
  상태판 Stage label은 있다.
  운영 FULL_THESIS Stage는 없다.

이번 v46/v47 보강:
  그 사실을 seed row 단위 trace로 검증 가능하게 만들었다.

다음 목표:
  seed -> planner -> source -> claim -> contribution -> StageCourt -> FULL_THESIS
  이 실제 경로를 닫는 것.
```

따라서 현재 정답은 이 문장이다.

```text
뭔가 잘못되고 있는 것은 맞다.
다만 output이 완전히 무의미한 것은 아니다.
지금 있는 것은 운영 Stage가 아니라 상태판 Stage이고,
운영 Stage처럼 말하는 순간 잘못이다.
```
