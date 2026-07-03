# Census v4 v94 - Stage Existence Truth / Seed Execution Gap Cross Validation

작성일: 2026-07-03

이 문서는 다음 질문에 대한 최신 검증 답변이다.

```text
뭔가 잘못되고 있는 거 맞지?
stage가 있는 애들이 있긴 해?
```

## 1. 짧은 결론

있다. 하지만 운영 Stage는 아니다.

```text
Stage row 자체:
  있음. census_stage_map.csv 기준 3,391개 row가 있다.

canonical_stage != 0:
  있음. 85개다.

운영 FULL_THESIS Stage:
  없음. 0개다.

운영 FULL_E2R_100 score:
  없음. 0개다.
```

쉬운 예:

```text
출석부에는 모든 학생 이름이 있고,
몇 명은 쪽지시험 점수도 있다.

하지만 기말고사 채점 완료자는 0명이다.

지금 v82 산출물의 Stage row는 출석부/쪽지시험에 가깝고,
운영 FULL_THESIS Stage는 기말고사다.
```

## 2. 직접 재검증한 산출물

기준 산출물:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v82
```

검증 파일:

```text
census_stage_map.csv
readiness_verdict.json
brain_web_readiness_gate_audit.json
brain_stage_promotion_audit.json
full_thesis_production_audit.json
samsung_hynix_full_thesis_smoke.json
```

직접 카운트:

```text
rows = 3,391

canonical_stage:
  0 = 3,306
  1 = 54
  2 = 30
  3-Red = 1

stage_scope:
  CENSUS_EVENT_BOARD = 3,390
  BRAIN_WEB_PARTIAL = 1
  FULL_THESIS = 0

score_scale:
  NO_SCORE = 3,324
  EVENT_WEIGHTED_PARTIAL = 67
  FULL_E2R_100 = 0

operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3,391

operator_score_use:
  NOT_FULL_E2R_SCORE = 3,391

full_thesis_stage:
  FULL_THESIS_NOT_RUN = 3,391
```

따라서 다음 말은 거짓이다.

```text
v82에는 운영 Stage가 85개 있다.
```

정확한 말은 이거다.

```text
v82에는 canonical_stage 표시는 85개 있지만,
그 85개 모두 운영 FULL_THESIS Stage가 아니다.
```

## 3. 삼성전자와 SK하이닉스 예시

### 삼성전자 005930

핵심 필드:

```text
stage_scope = CENSUS_EVENT_BOARD
canonical_stage = 1
score_scale = EVENT_WEIGHTED_PARTIAL
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
full_thesis_stage = FULL_THESIS_NOT_RUN
full_thesis_verified_score = empty
full_e2r_verified_score = empty
```

해석:

```text
삼성전자는 운영 Stage 1이 아니다.
공식 이벤트가 있어서 상태판에 Stage1처럼 보이는 행이 생긴 것이다.
FULL_THESIS 평가가 실행된 것이 아니고,
FULL_E2R_100 점수도 없다.
```

쉬운 예:

```text
"삼성전자에게 공시 이벤트가 하나 발견됐다"
-> 맞음.

"그래서 삼성전자 full thesis Stage 1이다"
-> 틀림.
```

### SK하이닉스 000660

핵심 필드:

```text
stage_scope = BRAIN_WEB_PARTIAL
canonical_stage = 1
event_evidence_score = 60.0
score_scale = EVENT_WEIGHTED_PARTIAL
score_scope = BRAIN_WEB_CLAIM_BACKED_PARTIAL
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
full_thesis_stage = FULL_THESIS_NOT_RUN
missing_primitives = hbm_capacity_constraint|hbm_capacity_pre_sold
next_actions = BRAIN_WEB_RECHECK|FULL_THESIS_REFRESH
```

해석:

```text
SK하이닉스는 Brain/Web partial 점수가 60.0까지는 닫혔다.
하지만 Green/FULL_THESIS에 필요한 primitive가 닫히지 않았다.
그래서 운영 Stage가 아니라 partial note다.
```

쉬운 예:

```text
"하이닉스 HBM 관련 부분 증거가 있어 60점짜리 중간 채점이 나왔다"
-> 맞음.

"하이닉스 운영 점수 60점, 운영 Stage 1 확정이다"
-> 틀림.
```

## 4. 관련 audit verdict

```text
readiness_verdict.json:
  verdict = NOT_READY

brain_web_readiness_gate_audit.json:
  verdict = BLOCKED

brain_stage_promotion_audit.json:
  verdict = PROMOTION_APPLIED

full_thesis_production_audit.json:
  verdict = PENDING_FULL_THESIS_PRODUCTION
  status = PENDING_FULL_THESIS_PRODUCTION

samsung_hynix_full_thesis_smoke.json:
  verdict = PENDING_FULL_THESIS_REFRESH
```

여기서 `PROMOTION_APPLIED`는 조심해서 읽어야 한다.

```text
BRAIN_WEB_PARTIAL 승격이 적용됐다는 뜻이지,
FULL_THESIS 운영 Stage 승격이 적용됐다는 뜻이 아니다.
```

## 5. v91, v92, v93가 해결한 것과 못 한 것

### v91

해결:

```text
FULL_THESIS 후보가 missing Green primitive 때문에 막히면
bounded official-first follow-up source task shell을 만든다.
```

못 한 것:

```text
task shell을 실제 source fetch/accepted claim으로 닫지는 않았다.
```

### v92

해결:

```text
v91 task shell을 다음 Research Brain 입력용 seed event로 변환한다.
seed는 planner_input_only이고 score/stage/current_score_eligible을 주입하지 않는다.
```

못 한 것:

```text
그 seed를 실제 Brain run에 넣어 planner/source/claim closure를 증명하지는 않았다.
```

### v93

해결:

```text
Research Brain v4 CLI에 --candidate-event-seed-path를 추가했다.
이제 v92 seed JSONL을 운영 명령줄에서 ProductionShadowV4Config로 전달할 수 있다.
```

못 한 것:

```text
live seed file을 실제로 넣어 FULL_THESIS까지 닫은 증거는 아직 없다.
```

## 6. 현재 구조에서 가장 큰 위험

다음 혼동이 다시 생기면 안 된다.

```text
canonical_stage != 0
-> 운영 Stage가 있다
```

이건 틀렸다.

앞으로 운영 Stage로 인정하려면 최소한 아래가 같이 닫혀야 한다.

```text
stage_scope = FULL_THESIS
score_scale = FULL_E2R_100
operator_stage_use = OPERATOR_FULL_THESIS_STAGE
operator_score_use = OPERATOR_FULL_E2R_SCORE
full_thesis_stage != FULL_THESIS_NOT_RUN
full_thesis_verified_score not empty
source-backed accepted_claim -> score_contribution -> primitive_state -> stagecourt_trace 연결
```

하나라도 빠지면 운영 Stage가 아니라 상태판 또는 partial이다.

## 7. 다음 패치 방향

다음 패치는 다시 문서나 이름 바꾸기가 아니라 실제 실행 증거를 만들어야 한다.

필수 흐름:

```text
1. v92/v93 코드로 Census live bounded run 재실행
2. output에 full_thesis_blocker_follow_up_seed_events.jsonl 생성 확인
3. 그 seed를 Research Brain CLI에 전달
4. planner_runs.jsonl에서 seed event 기반 planner run 확인
5. source_tasks.jsonl에서 bounded official-first task 생성 확인
6. source_task_executions.jsonl에서 실제 fetch 확인
7. evidence_documents.jsonl / evidence_anchors.jsonl 생성 확인
8. accepted_claims.jsonl에서 missing primitive를 닫는 claim 확인
9. primitive_states.jsonl에서 PRESENT_CURRENT 또는 필요한 상태 확인
10. score_contributions.jsonl에서 accepted_claim_id-backed score 확인
11. stagecourt_traces.jsonl에서 FULL_THESIS 재판정 확인
12. census_stage_map.csv에서 FULL_THESIS/FULL_E2R_100 row 확인
```

성공 조건:

```text
FULL_THESIS row가 1개 이상 생기는 것 자체가 성공이 아니다.
그 row가 accepted claim, source anchor, source task execution과 같은 trace 안에서 닫혀야 성공이다.
```

실패 조건:

```text
seed를 읽었지만 source fetch가 없다.
source fetch는 있지만 accepted_claim이 없다.
accepted_claim은 있지만 score_contribution support_claim_ids가 비어 있다.
score는 생겼지만 score_scale이 EVENT_WEIGHTED_PARTIAL이다.
stage는 생겼지만 operator_stage_use가 NOT_FULL_THESIS_STAGE다.
```

## 8. 다음 에이전트 공격 체크리스트

다음 에이전트는 아래를 공격해야 한다.

```text
1. 최신 artifact가 정말 v93 이후 실행인지 확인
2. census_stage_map.csv에서 stage_scope=FULL_THESIS row 수 확인
3. score_scale=FULL_E2R_100 row 수 확인
4. operator_stage_use가 OPERATOR_FULL_THESIS_STAGE인지 확인
5. operator_score_use가 OPERATOR_FULL_E2R_SCORE인지 확인
6. seed event가 planner_runs.jsonl로 실제 소비됐는지 확인
7. planner가 score/stage 없이 query/source task를 만들었는지 확인
8. source task가 bounded official-first였는지 확인
9. source_task_execution의 fetched_document_ids가 evidence_documents로 연결되는지 확인
10. evidence_anchor가 accepted_claim으로 연결되는지 확인
11. accepted_claim이 primitive_state를 닫았는지 확인
12. primitive_state가 score_contribution을 만들었는지 확인
13. score_contribution이 StageCourt trace와 같은 atomic decision에 들어갔는지 확인
14. missing primitive가 여전히 남아 있으면 score_valid를 FINAL로 확정하지 않았는지 확인
15. BRAIN_WEB_PARTIAL을 운영 Stage처럼 설명하지 않았는지 확인
```

## 9. 한 줄 결론

```text
Stage처럼 보이는 행은 있다.
하지만 운영에 쓸 FULL_THESIS Stage는 아직 0개다.
v93까지는 막힌 후보를 다시 Brain에 넣을 수 있는 길을 연 상태이고,
다음 증명은 seed -> planner -> source -> claim -> score -> StageCourt의 실제 live closure다.
```
