# Goal4 Materialized Runtime Attempt Final Audit - 2026-07-05

작성 시점: 2026-07-06 KST

이 문서는 `docs/core/goal4.md` 진행 중 실행한 materialized all-archetype runtime attempt의 최종 감사 기록이다.

대상 실행:

```text
output_root = output/census_v4/2026-07-05-goal4-all-archetype-next-runtime-attempt-materialized-v1
seed_path = docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl
run_mode = BRAIN_AND_WEB_ACQUISITION_ENABLED
target_gate = full_thesis
seed_event_count = 111
```

짧은 결론:

```text
Goal4 완료 아님.

좋아진 점:
- C01~C32 전체가 target_archetype을 가진 seed로 들어갔다.
- planner는 seed 111개 중 81개에서 real provider success를 냈다.
- C01~C32 전부 최소 1개 planner success를 확보했다.
- source task execution은 570개까지 실행됐다.
- accepted claim은 전체 102개, 이번 seed 쪽은 47개까지 생겼다.

막힌 점:
- 실행 산출물은 INVALID_PARTIAL_OUTPUT이다.
- readiness verdict는 NOT_READY다.
- operator가 써도 되는 production FULL_THESIS는 4개뿐이고 전부 required-positive/Green gap이 남아 있다.
- Brain/Web gate 기준 web/LLM accepted claim은 0개다.
- promoted row 4개는 unsafe promotion으로 감사에서 막혔다.
- StageCourt trace와 ScoreContribution의 candidate_event_id가 일부 섞인다.
```

쉬운 예:

```text
36개 과목 시험지를 전부 시험장에는 올렸다.
그런데 채점 완료 답안지는 4장뿐이고,
그 4장도 필수 증빙 서류가 빠져 있어 합격 처리하면 안 된다.
```

## 1. 실행 결과 상태

`brain_web_runtime_progress.json` 기준:

```text
status = COMPLETED
latest_phase = completed
event_count = 435
planner_run_count = 111
real_provider_success_count = 81
source_task_execution_count = 570
accepted_claim_count = 47
```

하지만 CLI 세션은 `INVALID_PARTIAL_OUTPUT`으로 종료됐다.

`partial_run_invalid.json` 기준:

```text
status = FAILED
verdict = INVALID_PARTIAL_OUTPUT
score_or_stage_evidence_allowed = false
readiness_evidence_allowed = false
reason = runner_exception
```

`readiness_verdict.json` 기준:

```text
verdict = NOT_READY
target_gate_pass = false
brain_web_evidence_pass = false
full_thesis_production_pass = false
meaningful_operational_stage_pass = false
operational_stage_use_allowed = false
```

즉 `progress=COMPLETED`는 실행 루프가 끝났다는 뜻이지, goal이 완료됐다는 뜻이 아니다.

## 2. 질문 1: 왜 production FULL_THESIS가 C05로 보였나?

이번 최신 실행에서는 과거처럼 `10개 전부 C05`가 아니라, production FULL_THESIS-like row가 4개였다.

그런데 대표 row의 `primary_archetype` 필드는 여전히 틀어져 있었다.

| symbol | company | seed target | planner top1 | StageCourt primary | 기존 final primary | score | stage |
|---|---|---|---|---|---|---:|---|
| 003380 | 하림지주 | C05 | C05 | C05 | C05 | 27.9998 | 0 |
| 005930 | 삼성전자 | C06 | C06 | C06 | C05 | 44.1667 | 1 |
| 047810 | 한국항공우주 | C03 | C03 | C03 | null | 37.0 | 0 |
| 052400 | 코나아이 | C01 | C01 | C01 | C05 | 11.9999 | 0 |

핵심:

```text
seed와 planner는 C01/C03/C05/C06을 구분했다.
StageCourt trace도 C01/C03/C05/C06을 들고 있었다.
그런데 census_stage_status 대표 row의 primary_archetype만 이전 event-board 값을 그대로 물고 있었다.
```

쉬운 예:

```text
삼성전자 시험지는 C06 과목으로 접수됐고,
채점 선생님도 C06으로 채점했다.
그런데 성적표 표지의 과목명 칸만 예전 C05가 남아 있었다.
```

원인 코드:

```text
src/e2r/census/census_runner_v4.py

_apply_production_full_thesis_from_brain()
  item = dict(row)
  item.update({
      "full_thesis_primary_archetype": archetype_id,
      ...
  })

기존에는 primary_archetype 자체를 archetype_id로 갱신하지 않았다.
```

이번 패치:

```text
production FULL_THESIS row update 때 primary_archetype = archetype_id도 같이 쓴다.
```

검증:

```text
PYTHONPATH=src python -m unittest tests.test_census_v4_brain_stage_promotion_gate -v
Ran 26 tests ... OK
```

주의:

```text
이미 생성된 output/census_v4/.../census_stage_status.jsonl은 패치 전 artifact다.
패치 효과는 다음 재실행부터 반영된다.
```

## 3. 질문 2: target_archetype_counts가 UNKNOWN인데 C05가 된 경로인가?

이번 materialized 실행에서는 이 문제는 대부분 해소됐다.

`full_thesis_seed_materialization_audit.json` 기준:

```text
target_archetype_counts:
  C01~C32 = 각 3개
  C29 = 6개
  R13 4종 = 각 3개

target_symbol_mode_counts:
  RESEARCH_MEMORY_TARGET_CANDIDATE = 87
  SYMBOL_SPECIFIC = 15
  ARCHETYPE_LEVEL_DISCOVERY = 9

target_materialization_status_counts:
  TARGET_SYMBOL_READY = 102
  TARGET_MATERIALIZATION_REQUIRED = 9
```

즉 최신 seed 장부에서는 `target_archetype`이 `UNKNOWN`이라서 C05로 몰린 게 아니다.

이번 C05 표시 문제는 다음 경로다.

```text
seed target_archetype = C06
planner top1 = C06
StageCourt primary_archetype = C06
production row full_thesis_primary_archetype = C06
production row primary_archetype = 기존 CENSUS_EVENT_BOARD 값 C05
```

그래서 문제의 성격은:

```text
아키타입 materialization 실패
-> 아님

final representative row 필드 갱신 누락
-> 맞음
```

## 4. 질문 3: 27.9998 / 44.1667 / 37.0 / 11.9999 점수 formula trace

점수 경로:

```text
ScoreContribution raw_points
-> component별 raw component
-> archetype runtime weight 적용
-> calibration/risk/floor 확인
-> 0~100 clamp
-> StageCourt threshold 적용
```

StageCourt threshold:

```text
Stage1 = 40
Stage2 = 65
Yellow = 80
Green = 90
```

### 003380 하림지주, C05

```text
raw components:
  earnings_visibility = 13.3333 / 20
  information_confidence = 3.3333 / 5

C05 weights:
  earnings_visibility weight = 22
  information_confidence weight = 20

weighted:
  13.3333 / 20 * 22 = 14.6666
  3.3333 / 5 * 20 = 13.3332

total = 27.9998
stage = 0
score_source = BRAIN_WEB_PRODUCTION_FULL_THESIS_STAGECOURT
score_scale = FULL_E2R_100
```

### 005930 삼성전자, C06

```text
raw components:
  eps_fcf_explosion = 20.0 / 20
  earnings_visibility = 6.6667 / 20
  bottleneck_pricing = 5.0 / 20
  market_mispricing = 3.75 / 15
  valuation_rerating = 3.75 / 15
  information_confidence = 1.6667 / 5

C06 weighted components:
  eps_fcf_explosion = 24.0
  earnings_visibility = 7.0
  bottleneck_pricing = 4.75
  market_mispricing = 3.75
  valuation_rerating = 3.0
  information_confidence = 1.6667

total = 44.1667
stage = 1
score_source = BRAIN_WEB_PRODUCTION_FULL_THESIS_STAGECOURT
score_scale = FULL_E2R_100
```

### 047810 한국항공우주, C03

```text
raw components:
  earnings_visibility = 10.0 / 20
  bottleneck_pricing = 10.0 / 20
  market_mispricing = 7.5 / 15
  valuation_rerating = 7.5 / 15
  information_confidence = 2.5 / 5

C03 weighted total = 37.0
stage = 0
```

### 052400 코나아이, C01

```text
raw components:
  earnings_visibility = 3.3333 / 20
  bottleneck_pricing = 3.3333 / 20
  market_mispricing = 2.5 / 15
  valuation_rerating = 2.5 / 15
  information_confidence = 0.8333 / 5

C01 weighted total = 11.9999
stage = 0
```

정리:

```text
27.9998 같은 숫자는 epsilon으로 만든 값이 아니다.
13.3333 같은 fractional raw_points에 runtime weight를 곱한 round artifact다.
```

다만 더 큰 문제는 점수식이 아니라 lineage다.

일부 StageCourt trace는 `candidate_event_id=A`인데, 참조한 `score_contribution_id`의 row는 `candidate_event_id=B`로 덮여 있다.

예:

```text
삼성전자 trace event = CEV4-RTATTEMPT-7f33...
삼성전자 contribution rows event = CEV4-RTATTEMPT-dd318...

코나아이 trace event = CEV4-RTATTEMPT-4f00...
코나아이 contribution rows event = CEV4-RTATTEMPT-d280...
```

쉬운 예:

```text
A 시험지 표지에 B 시험지 채점표가 끼워진 상태다.
점수 자체는 재현되지만, 어느 seed/gap의 점수인지 감사하기 어렵다.
```

남은 패치 필요:

```text
Research Brain export score_contribution_id를 candidate_event_id까지 포함해 event-scoped로 만들거나,
merge key를 candidate_event_id + contribution_id 복합키로 바꿔야 한다.
```

## 5. 질문 4: C05가 아닌 아키타입은 왜 0개 또는 미완료인가?

최신 materialized seed 기준 전체 상태:

| archetype | seeds | planner success | source execs | accepted claims | stagecourt | promoted | main status |
|---|---:|---:|---:|---:|---:|---:|---|
| C01 | 3 | 3 | 21 | 6 | 3 | 1 | promoted but required/green gap |
| C02 | 3 | 2 | 14 | 0 | 0 | 0 | claim not created, timeout 1 |
| C03 | 3 | 2 | 14 | 6 | 2 | 1 | promoted but required/green gap |
| C04 | 3 | 1 | 7 | 0 | 0 | 0 | timeout 2, claim not created |
| C05 | 3 | 3 | 21 | 6 | 3 | 1 | promoted but required/green gap |
| C06 | 3 | 3 | 21 | 6 | 3 | 1 | promoted but required/green gap |
| C07 | 3 | 3 | 21 | 0 | 0 | 0 | claim not created |
| C08 | 3 | 2 | 14 | 0 | 0 | 0 | claim not created, timeout 1 |
| C09 | 3 | 2 | 14 | 0 | 0 | 0 | claim not created, timeout 1 |
| C10 | 3 | 3 | 21 | 0 | 0 | 0 | claim not created |
| C11 | 3 | 3 | 21 | 0 | 0 | 0 | claim not created |
| C12 | 3 | 3 | 21 | 0 | 0 | 0 | claim not created |
| C13 | 3 | 2 | 17 | 0 | 0 | 0 | claim not created, timeout 1 |
| C14 | 3 | 2 | 14 | 0 | 0 | 0 | claim not created, timeout 1 |
| C15 | 3 | 2 | 14 | 0 | 0 | 0 | claim not created, timeout 1 |
| C16 | 3 | 2 | 14 | 0 | 0 | 0 | claim not created, timeout 1 |
| C17 | 3 | 3 | 21 | 0 | 0 | 0 | claim not created |
| C18 | 3 | 2 | 14 | 0 | 0 | 0 | claim not created, timeout 1 |
| C19 | 3 | 2 | 14 | 0 | 0 | 0 | claim not created, timeout 1 |
| C20 | 3 | 2 | 14 | 0 | 0 | 0 | claim not created, timeout 1 |
| C21 | 3 | 2 | 14 | 0 | 0 | 0 | claim not created, timeout 1 |
| C22 | 3 | 2 | 14 | 0 | 0 | 0 | claim not created, timeout 1 |
| C23 | 3 | 3 | 21 | 0 | 0 | 0 | claim not created |
| C24 | 3 | 3 | 21 | 0 | 0 | 0 | claim not created |
| C25 | 3 | 2 | 14 | 0 | 0 | 0 | claim not created, timeout 1 |
| C26 | 3 | 3 | 21 | 0 | 0 | 0 | claim not created |
| C27 | 3 | 3 | 21 | 0 | 0 | 0 | claim not created |
| C28 | 3 | 3 | 21 | 0 | 0 | 0 | claim not created |
| C29 | 6 | 5 | 35 | 0 | 0 | 0 | claim not created, timeout 1 |
| C30 | 3 | 2 | 14 | 0 | 0 | 0 | claim not created, timeout 1 |
| C31 | 3 | 2 | 14 | 2 | 2 | 0 | stagecourt ready, not promoted |
| C32 | 3 | 1 | 7 | 0 | 0 | 0 | timeout 2, claim not created |
| R13 4B/4C | 3 | 0 | 0 | 0 | 0 | 0 | R13 primary policy reject / no success |
| R13 Accounting | 3 | 0 | 0 | 0 | 0 | 0 | R13 primary policy reject / no success |
| R13 High MAE | 3 | 0 | 0 | 0 | 0 | 0 | timeout/no success |
| R13 Stage2 FP | 3 | 3 | 21 | 0 | 0 | 0 | claim not created |

주요 canary 해석:

```text
C06:
  seed/planner/source/claim/stagecourt/promotion까지 갔지만 Green primitive가 남아 meaningful pass가 아니다.

C08/C15/C17/C24/C28:
  planner와 source task는 갔지만 accepted claim이 0이다.
  즉 검색/공식 route가 "현재 직접 점수 가능한 claim"으로 닫히지 않았다.
```

쉬운 예:

```text
C08, C15, C17, C24, C28은 택배 출고까지는 됐는데,
받은 물건이 검수 통과품으로 창고에 입고되지 않은 상태다.
```

## 6. 질문 5: required_positive_missing_primitives가 있는데 PASS를 허용했나?

이번 최신 audit 기준으로는 허용하지 않는다.

`full_thesis_production_audit.json`:

```text
production_full_thesis_row_count = 4
production_full_thesis_row_with_required_positive_missing_primitives_count = 4
production_full_thesis_row_with_green_gap_primitives_count = 4
production_pass_allowed = false
completion_eligible = false
blockers = ['production_full_thesis_rows_with_required_positive_missing_primitives']
```

즉 현재 구분은 이렇다.

```text
FULL_THESIS_PROMOTED row exists
  = source-backed score path 형태는 만들어졌다.

FULL_THESIS_PRODUCTION_PASS
  = false.

meaningful full thesis passed
  = false.
```

쉬운 예:

```text
답안지가 제출함 상태로 바뀌었지만,
필수 서류 미첨부라 합격 처리하지 않는다.
```

## 7. 질문 6: 삼성전자/하이닉스는 왜 production full-thesis row로 다르게 나왔나?

### 삼성전자

이번 materialized seed에는 삼성전자가 C06 seed로 들어갔다.

```text
symbol = 005930
seed target_archetype = C06_HBM_MEMORY_CUSTOMER_CAPACITY
planner top1 = C06_HBM_MEMORY_CUSTOMER_CAPACITY
StageCourt primary = C06_HBM_MEMORY_CUSTOMER_CAPACITY
full_thesis_primary_archetype = C06_HBM_MEMORY_CUSTOMER_CAPACITY
score = 44.1667
stage = 1
```

하지만 operator pass는 아니다.

남은 gap:

```text
full_thesis_required_positive_missing_primitives:
  customer_preorder_or_allocation
  hbm_capacity_constraint
  hbm_capacity_pre_sold
  memory_price_increase_mentioned

full_thesis_green_gap_primitives:
  customer_preorder_or_allocation
  hbm_capacity_constraint
  hbm_capacity_pre_sold
```

그리고 패치 전 artifact에서는 대표 `primary_archetype` 표시가 C05로 남아 있었다.

### SK하이닉스

이번 materialized seed에는 `000660` SK하이닉스가 들어가지 않았다.

현재 SK하이닉스는:

```text
census_stage_status:
  base_stage = Stage1
  score_scale = EVENT_WEIGHTED_PARTIAL
  operator_score_use = NOT_FULL_E2R_SCORE
  operator_stage_use = NOT_FULL_THESIS_STAGE
  full_thesis_stage = FULL_THESIS_NOT_RUN

full_thesis_refresh_queue:
  queue_task_id = FTQUEUE-2026-07-01-000660-0031
  task_status = PLANNING_REQUIRED
  target_archetype = null
  target_archetype_status = BRAIN_HYPOTHESIS_REQUIRED
```

즉 하이닉스는 controlled smoke와 daily event-board에는 있었지만, 이번 materialized all-archetype seed 실행에서 production FULL_THESIS로 승격되지 않았다.

쉬운 예:

```text
삼성전자는 이번 정밀검진실에 들어갔지만 서류 미비로 합격은 아니다.
하이닉스는 대기표에는 있지만 이번 정밀검진실 호출 명단에는 없었다.
```

## 8. 이번에 실제로 고친 것

패치:

```text
src/e2r/census/census_runner_v4.py
  production FULL_THESIS row update 때 primary_archetype도 StageCourt archetype으로 갱신

tests/test_census_v4_brain_stage_promotion_gate.py
  기존 event-board primary_archetype이 C05여도 C06 full-thesis promotion이면 primary_archetype이 C06으로 바뀌는 회귀 테스트 추가
```

검증:

```text
PYTHONPATH=src python -m unittest tests.test_census_v4_brain_stage_promotion_gate -v
Ran 26 tests in 14.277s
OK
```

## 9. 아직 반드시 고쳐야 하는 blocker

### A. contribution id가 event-scoped가 아니다

증상:

```text
StageCourt trace candidate_event_id = A
score_contribution row candidate_event_id = B
```

원인 추정:

```text
ScoreContributionV2 contribution_id가 component/support claims 중심으로 안정 생성된다.
같은 symbol의 여러 seed가 같은 claim set을 쓰면 contribution_id가 충돌한다.
_merge_jsonl_by_key(..., key='score_contribution_id')가 뒤쪽 row로 candidate_event_id를 덮어쓴다.
```

필요 패치:

```text
Research Brain export contribution_id = stable_hash(candidate_event_id, original_contribution_id)
또는 merge key = candidate_event_id + score_contribution_id
```

### B. Brain/Web acceptance gate가 아직 닫히지 않았다

`readiness_verdict` blocker:

```text
web/LLM accepted claim count is zero
Brain/Web source task budget caps were exceeded: 3
Brain/Web evidence documents include snapshot:// sources
Brain/Web stage row was promoted despite blockers
brain stage promotion verdict is not PROMOTION_APPLIED: FAIL_UNSAFE_PROMOTION
```

해석:

```text
official claim은 일부 생겼지만,
운영 gate가 요구하는 web/LLM claim-backed route는 아직 0이다.
snapshot source가 섞인 row는 production cutover에 쓰면 안 된다.
```

### C. accepted claim 0 아키타입이 너무 많다

현재 상태:

```text
ACCEPTED_CLAIM_NOT_CREATED = 68 seed
PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS = 30 seed
STAGECOURT_READY_NOT_PROMOTED = 9 seed
FULL_THESIS_PROMOTED = 4 seed
```

즉 다음 작업은 점수 threshold 조정이 아니다.

```text
source task 실행
-> fetched document
-> accepted claim
-> primitive state
-> score contribution
-> StageCourt
```

이 연결을 C08/C15/C17/C24/C28 같은 non-C05 canary에서 먼저 닫아야 한다.

## 10. 최종 판단

이번 materialized 실행은 중요한 진전이지만 Goal4 완료가 아니다.

```text
planner monoculture:
  상당 부분 해소. C01~C32 모두 planner success가 있다.

source route:
  대부분 실행됐다.

accepted claim:
  C01/C03/C05/C06/C31 외에는 거의 닫히지 않았다.

production full thesis:
  4개뿐이고 모두 required-positive/Green gap이 남아 pass 불가.

operator use:
  금지. INVALID_PARTIAL_OUTPUT / NOT_READY.
```

다음 agent가 이 문서를 볼 때 가장 먼저 봐야 할 수리 순서:

```text
1. contribution_id event scoping 수리
2. Brain/Web snapshot source promotion 차단 재검증
3. C08/C15/C17/C24/C28 accepted claim 0 원인 추적
4. R13 primary policy reject를 explicit red-team seed 형식으로 수리
5. materialized seed 재실행 후 primary_archetype drift가 사라졌는지 확인
6. required-positive gap이 0인 non-C05 production full-thesis row 확보
```

이 상태에서 점수를 운영 결과로 말하면 안 된다.

말할 수 있는 것은:

```text
전 아키타입 seed/planner/source attempt는 많이 진전됐다.
하지만 production full-thesis 운영 검증은 아직 실패다.
```
