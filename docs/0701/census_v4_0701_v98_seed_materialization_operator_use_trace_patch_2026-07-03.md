# Census v4 0701 v98 Seed Materialization Operator-Use Trace 패치

작성일: 2026-07-03

## 0. 결론

v98은 운영 Stage를 새로 만든 패치가 아니다.

이번 패치는 v97 교차검증에서 드러난 audit 빈칸을 막는 패치다.

```text
기존:
  full_thesis_seed_materialization_trace에서
  final_operator_stage_use는 보이지만 final_operator_score_use가 비어 있을 수 있었다.

변경:
  seed materialization trace만 봐도
  해당 seed가 운영 Stage/score로 사용 가능한지 바로 보이게 했다.
```

쉬운 예:

```text
예전에는 택배 추적표에 "배송 상태"는 있는데
"이 물건을 매장 판매대에 올려도 되는지" 칸이 비어 있는 상태였다.

이제는 배송 상태와 판매 가능 여부를 둘 다 적는다.
```

## 1. 패치 이유

v97 live smoke 문서에서 확인한 문제:

```text
materialization trace sample:
  final_stage_scope = BRAIN_WEB_PARTIAL
  final_score_scale = EVENT_WEIGHTED_PARTIAL
  final_operator_stage_use = NOT_FULL_THESIS_STAGE
  final_operator_score_use = null
```

stage map에는 이미 다음이 있었다.

```text
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
```

하지만 seed materialization trace에는 `final_operator_score_use`가 빠져 있었다.

이러면 다른 에이전트가 trace만 보고 이렇게 공격할 수 있다.

```text
"score use가 null이면 빠진 건가?
 혹시 partial score를 운영 score로 써도 되는 건가?"
```

따라서 trace에도 operator-use를 완전히 기록하게 했다.

## 2. 코드 변경

수정 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_full_thesis_smoke_tasks.py
```

### 2.1 Trace 필드 추가

`_write_full_thesis_seed_materialization_trace()`에서 seed trace row에 다음 필드를 추가했다.

```text
final_operator_score_use
final_full_thesis_score_scale
final_is_full_thesis_stage
final_is_full_e2r_score
```

기존 필드도 명시 변수로 정리했다.

```text
final_stage_scope
final_operator_stage_use
final_score_scale
```

운영 의미:

```text
final_operator_stage_use = FULL_THESIS_STAGE
  -> 운영 Stage로 쓸 수 있는 후보

final_operator_stage_use = NOT_FULL_THESIS_STAGE
  -> 상태판/partial일 뿐 운영 Stage 아님

final_operator_score_use = FULL_E2R_SCORE
  -> 운영 full E2R score

final_operator_score_use = NOT_FULL_E2R_SCORE
  -> event/partial/no-score라 운영 score 아님
```

### 2.2 promoted_to_full_thesis 의미 강화

기존에는 다음 조건만 봤다.

```text
stage_scope == FULL_THESIS
and not controlled_smoke
```

이제 trace row의 boolean은 다음 조건을 쓴다.

```text
final_is_full_thesis_stage == true
and final_is_full_e2r_score == true
```

즉 Stage scope만 FULL_THESIS처럼 보여도 full E2R score가 같이 닫히지 않으면 운영 승급으로 보지 않는다.

주의:

```text
materialization_status 자체는 기존처럼
stage_scope + score_scale + planner/source/claim/stagecourt closure로 계산한다.
```

### 2.3 Audit 분포 추가

`full_thesis_seed_materialization_audit.json`에 다음 count를 추가했다.

```text
final_operator_stage_use_counts
final_operator_score_use_counts
```

이제 audit summary만 봐도 다음을 알 수 있다.

```text
FULL_THESIS_STAGE가 몇 개인가?
FULL_E2R_SCORE가 몇 개인가?
NOT_FULL_THESIS_STAGE가 몇 개인가?
NOT_FULL_E2R_SCORE가 몇 개인가?
```

### 2.4 Critical guard 추가

다음 critical count를 추가했다.

```text
final_operator_stage_use_missing_count
final_operator_score_use_missing_count
event_or_partial_stage_operator_use_allowed_count
event_or_partial_score_operator_use_allowed_count
full_thesis_promoted_operator_stage_use_not_full_count
full_thesis_promoted_operator_score_use_not_full_count
```

의미:

```text
1. final_operator_*_use가 비어 있으면 fail
2. event-board/partial인데 운영 Stage로 표시되면 fail
3. event/partial score인데 운영 E2R score로 표시되면 fail
4. FULL_THESIS_PROMOTED인데 operator-use가 운영 가능 값이 아니면 fail
```

쉬운 예:

```text
BRAIN_WEB_PARTIAL인데 operator_stage_use=FULL_THESIS_STAGE이면 바로 fail.
EVENT_WEIGHTED_PARTIAL인데 operator_score_use=FULL_E2R_SCORE이면 바로 fail.
```

### 2.5 Readiness / Goal summary 노출

다음 summary에도 operator-use 분포를 노출했다.

```text
readiness_verdict.full_thesis_seed_materialization_audit
goal_completion_audit.full_thesis_seed_materialization_summary
```

## 3. 테스트 변경

수정:

```text
tests/test_census_v4_full_thesis_smoke_tasks.py
```

추가 검증:

```text
seed trace에 final_operator_score_use가 존재한다.
event-board seed는 NOT_FULL_E2R_SCORE다.
full thesis promoted fixture는 FULL_E2R_SCORE다.
audit에 final_operator_stage_use_counts가 있다.
audit에 final_operator_score_use_counts가 있다.
```

## 4. 검증 결과

관련 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_brain_web_readiness_gate -v
```

결과:

```text
Ran 30 tests in 34.451s
OK
```

Census v4 전체 테스트:

```bash
PYTHONPATH=src python -m unittest discover -s tests -p 'test_census_v4_*.py' -v
```

결과:

```text
Ran 140 tests in 88.962s
OK
```

전체 테스트:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5125 tests in 230.636s
OK
```

## 5. 현재 운영 상태

이번 패치 후에도 운영 FULL_THESIS Stage가 생긴 것은 아니다.

v97 live smoke truth는 그대로다.

```text
stage_scope=FULL_THESIS row = 0
score_scale=FULL_E2R_100 row = 0
operator_stage_use usable row = 0
operator_score_use usable row = 0
```

v98이 바꾼 것은 이것이다.

```text
FULL_THESIS가 없다는 사실을 trace와 audit에서 더 명확하게 보이게 함.
partial/event-board를 운영 score/stage로 잘못 읽는 여지를 줄임.
```

## 6. 다음 패치 방향

아직 닫혀야 하는 P0는 그대로다.

```text
1. real LLM claim extractor 경로를 실제 Census Brain run에서 열기
2. external seed 85개 중 더 많은 seed를 real planner/source/claim/stagecourt까지 materialize하기
3. BRAIN_WEB_PARTIAL을 FULL_THESIS로 승급시키는 데 필요한 primitive coverage와 score interval closure 닫기
4. source-origin filtered current attempt count와 ledger total count를 모든 summary에서 더 명확히 분리하기
5. FULL_THESIS primary archetype과 event-board/partial archetype을 출력 필드에서 분리하기
```

다음 에이전트가 공격해야 할 질문:

```text
1. full_thesis_seed_materialization_trace의 모든 row에 final_operator_score_use가 있는가?
2. BRAIN_WEB_PARTIAL row가 FULL_E2R_SCORE로 표시되는 곳은 없는가?
3. EVENT_WEIGHTED_PARTIAL row가 FULL_E2R_SCORE로 표시되는 곳은 없는가?
4. FULL_THESIS_PROMOTED row의 operator_stage_use/operator_score_use가 둘 다 운영 가능 값인가?
5. v98을 근거로 운영 Stage가 생겼다고 과장한 문서가 있는가?
```

## 7. 한 줄 판단

v98은 `운영 Stage 생성 패치`가 아니라 `운영 Stage 오인 방지 패치`다.

```text
좋아진 것:
  seed materialization trace와 audit에서 operator stage/score 사용 가능 여부가 null 없이 드러난다.

아직 남은 것:
  실제 FULL_THESIS / FULL_E2R_100 row 생성과 real LLM claim extractor 기반 live closure.
```

