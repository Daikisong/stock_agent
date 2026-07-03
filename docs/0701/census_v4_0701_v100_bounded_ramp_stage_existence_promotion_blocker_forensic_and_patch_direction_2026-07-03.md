# Census v4 0701 v100 Bounded Ramp Stage Existence / Promotion Blocker Forensic

검증 기준 산출물:

```text
output/census_v4/2026-07-01-v100-external-seed-real-extractor-bounded-ramp
```

이 문서는 다음 에이전트가 빡세게 공격할 수 있게 만든 v100 정밀 감사 기록이다.

핵심 질문은 이것이었다.

```text
뭔가 잘못되고 있는가?
Stage가 있는 애들이 있긴 한가?
```

짧은 답:

```text
StageCourt trace는 있다.
하지만 운영용 FULL_THESIS Stage는 없다.

census_stage_status에도 Stage row는 있지만 전부 CENSUS_EVENT_BOARD다.
Research Brain이 만든 StageCourt trace 21개도 최종 census_stage_status에는 0개 승격됐다.

즉 "Stage가 아예 없다"가 아니라,
"Stage의 종류가 전부 운영 Stage가 아니고, Brain StageCourt 결과가 최종 상태판에 올라가지 못한다"가 정확하다.
```

쉬운 예:

```text
학생 21명이 답안지를 냈다.
채점표에도 부분 점수는 있다.
그런데 성적표에 반영하는 교무실 승인이 0건이다.

그래서 "답안지가 없었다"가 아니라
"성적표 반영 규칙에서 막혔다"가 맞다.
```

## 1. 실행 명령

v100은 external seed를 받아 real planner, bounded live acquisition, real LLM claim extractor를 켠 bounded ramp다.

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01-v100-external-seed-real-extractor-bounded-ramp \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --brain-planner-provider real \
  --brain-source-acquisition live_full_bounded \
  --brain-candidate-event-seed-path output/census_v4/2026-07-01-v97-seed-source/research_brain_full_thesis_seed_events.jsonl \
  --brain-universe-limit 30 \
  --brain-planner-success-limit 30 \
  --brain-planner-batch-size 5 \
  --brain-max-source-tasks-per-plan 3 \
  --brain-max-fetches-per-task 2 \
  --brain-retry-max 1 \
  --brain-claim-extractor-provider auto \
  --brain-claim-extractor-timeout-seconds 120 \
  --brain-stage-promotion-mode strict \
  --target-gate brain_web \
  --write-operational-docs false \
  --fail-on-critical-audit false
```

결과:

```text
readiness_verdict = NOT_READY
```

## 2. v100 핵심 숫자

### 2.1 최종 census_stage_status

파일:

```text
output/census_v4/2026-07-01-v100-external-seed-real-extractor-bounded-ramp/census_stage_status.jsonl
```

분포:

```text
rows = 3391

canonical_stage:
  0      = 3306
  1      = 54
  2      = 30
  3-Red  = 1

stage_scope:
  CENSUS_EVENT_BOARD = 3391
  BRAIN_WEB_PARTIAL  = 0
  FULL_THESIS        = 0

score_scale:
  NO_SCORE               = 3324
  EVENT_WEIGHTED_PARTIAL = 67
  FULL_E2R_100           = 0

operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3391

operator_score_use:
  NOT_FULL_E2R_SCORE = 3391
```

판정:

```text
최종 상태판에 Stage row는 있다.
하지만 운영자가 써도 되는 FULL_THESIS Stage/Score는 0개다.
```

쉬운 예:

```text
005930 삼성전자는 census_stage_status에서 Stage1처럼 보인다.
하지만 stage_scope=CENSUS_EVENT_BOARD이고 score_scale=EVENT_WEIGHTED_PARTIAL이다.
즉 "오늘 전체지도에서 후보로 봤다"는 상태이지, 삼성전자 Full Thesis 점수/Stage가 아니다.
```

### 2.2 Research Brain StageCourt trace

파일:

```text
output/census_v4/2026-07-01-v100-external-seed-real-extractor-bounded-ramp/stagecourt_traces.jsonl
```

Research Brain origin StageCourt:

```text
brain_stage_trace_count = 21

base_stage:
  0 = 19
  1 = 2

score_status:
  FINAL = 21

not_promoted_to_census_stage_status:
  true = 21
```

판정:

```text
Research Brain이 StageCourt까지 만든 종목은 21개다.
하지만 21개 모두 최종 census_stage_status로 승격되지 않았다.
```

### 2.3 Brain/Web operational minimum

파일:

```text
brain_web_readiness_gate_audit.json
brain_stage_promotion_audit.json
llm_claim_extraction_audit.json
source_task_realness_audit.json
```

v99까지의 병목은 "real LLM extractor가 없다"와 "수집량이 부족하다"였다.
v100에서는 이 병목 대부분이 닫혔다.

```text
llm_claim_extractor_attempt_count      = 31
llm_claim_extractor_real_provider_count = 31
web_search_task_count                  = 37
web_search_call_count                  = 37
web_fetched_document_count             = 31
real_provider_success_count            = 30
source_task_execution_count            = 228
brain_claim_count                      = 93
brain_score_contribution_count         = 53
brain_to_claim_trace_count             = 93
brain_stage_trace_count                = 21
```

통과한 감사:

```text
llm_claim_extraction_audit.verdict = REAL_EXTRACTION_PASS
source_task_realness_audit.verdict = LIVE_SOURCE_PASS
brain_to_claim_trace_audit.verdict = PASS
source_task_satisfaction_audit.verdict = PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION
```

하지만 최종 readiness는 막혔다.

```text
brain_web_readiness_gate_audit.verdict = BLOCKED

blockers:
  Brain/Web trace rows missing stagecourt_trace_id: 3
  Brain/Web StageCourt traces are not promoted into census_stage_status
  brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED
```

가장 중요한 blocker:

```text
brain_stage_promotion_audit.verdict = BLOCKED
brain_stage_trace_without_web_or_llm_claim_count = 19
blocker = brain StageCourt traces have no web/LLM accepted claim support: 19
```

## 3. Stage는 있는데 왜 최종표에 0개 승격됐나

현재 `_promote_brain_stage_rows()`는 먼저 `_brain_stage_promotion_audit()` preflight를 호출한다.
preflight가 `ELIGIBLE_NOT_PROMOTED`가 아니면 아무 Stage도 승격하지 않는다.

현재 preflight에서 다음 조건이 전체 run blocker다.

```text
brain StageCourt traces have no web/LLM accepted claim support: 19
```

즉 21개 StageCourt 중 19개가 official-only라는 이유로 blocker가 생기고,
그 결과 web/LLM claim을 가진 나머지 2개까지 함께 승격되지 않는다.

현재 데이터 분해:

```text
Research Brain StageCourt 21개 중
  LLM/BrokerReport claim 포함 = 2
  OpenDART official-only = 19
```

LLM 포함 trace:

```text
000660 SK하이닉스
  stagecourt_trace_id = SCT-BRAIN-8f6dfdf950b185d76dac
  lower score interval = 31.6667
  accepted_claim_count = 2
  llm claim = 2
  official claim = 0

034020 두산에너빌리티
  stagecourt_trace_id = SCT-BRAIN-6826c46904e9274944fc
  lower score interval = 64.0002
  accepted_claim_count = 2
  llm claim = 1
  official claim = 1
```

official-only trace 예:

```text
005930 삼성전자
  stagecourt_trace_id = SCT-BRAIN-52f4af11b2a72a3c9e36
  lower score interval = 39.8333
  accepted_claim_count = 1
  llm claim = 0
  official claim = 1
  source_provider = OpenDART
```

쉬운 예:

```text
21명 중 19명은 DART 공시만 제출했다.
2명은 리포트/LLM 추출 claim도 제출했다.

현재 규칙은 "DART 공시만 낸 사람이 하나라도 있으면 반 전체 성적표 반영 금지"처럼 동작한다.
이건 너무 전역적인 차단이다.
```

## 4. 이게 안전장치인가, 버그인가

둘 다 조금씩 맞다.

### 4.1 안전장치인 부분

official-only claim만으로 `BRAIN_WEB_PARTIAL`이라고 부르면 이름이 틀린다.

예:

```text
OpenDART 공급계약 claim만 있음
web search / LLM report claim 없음
-> BRAIN_WEB_PARTIAL로 부르면 안 됨
```

또 official-only claim만으로 바로 FULL_THESIS 또는 Green을 주면 안 된다.

예:

```text
공급계약 공시에 납기만 있음
매출 규모, 마진 bridge, 반복성, 현금흐름 확인 없음
-> C05 Green 불가
```

이 안전장치는 유지해야 한다.

### 4.2 버그 또는 정책 충돌인 부분

프로젝트 원칙은 official-first다.
OpenDART, KIND, KRX, IR 같은 공식 원문은 일반 웹보다 약한 증거가 아니다.

그런데 v100에서는 official-only StageCourt trace 19개가 모두 "web/LLM claim 없음"으로 막혔다.
그 결과 official-only 부분 Stage도 최종 상태판에 올라오지 않는다.

더 큰 문제:

```text
official-only 19개가 blocker를 만들면서,
LLM/web claim이 있는 2개 trace까지 같이 승격되지 않는다.
```

이건 per-trace blocker가 아니라 run-global blocker라서 너무 거칠다.

정확한 정책은 이렇게 나뉘어야 한다.

```text
official-only direct/current claim-backed StageCourt
  -> BRAIN_OFFICIAL_PARTIAL 또는 BRAIN_CLAIM_PARTIAL로 승격 가능
  -> operator_stage_use = NOT_FULL_THESIS_STAGE
  -> operator_score_use = NOT_FULL_E2R_SCORE
  -> FULL_THESIS/Green은 아님

web/LLM claim-backed StageCourt
  -> BRAIN_WEB_PARTIAL로 승격 가능
  -> operator_stage_use = NOT_FULL_THESIS_STAGE
  -> operator_score_use = NOT_FULL_E2R_SCORE
  -> FULL_THESIS/Green은 아님

full thesis-ready StageCourt
  -> source linkage, direct/current eligibility, score interval, archetype Green primitives, source quorum 통과 시에만 FULL_THESIS
```

## 5. Full Thesis는 왜 아직 0개인가

파일:

```text
full_thesis_production_audit.json
full_thesis_production_runner_audit.json
full_thesis_seed_materialization_audit.json
```

결론:

```text
production_full_thesis_row_count = 0
full_thesis_row_count = 0
full_thesis_seed_actual_materialization_pass_allowed = false
```

`full_thesis_production_runner_audit.json`은 21개 StageCourt를 production full thesis 후보로 직접 스캔한다.
즉 Brain/Web partial 승격이 안 되어도 Full Thesis 후보 판정 자체는 시도한다.

하지만 21개 모두 막힌 이유는 동일하다.

```text
blockers = ["missing_green_gate_primitives"]
```

예:

```text
000660 SK하이닉스
  primary_archetype = C06_HBM_MEMORY_CUSTOMER_CAPACITY
  present_primitives =
    customer_preorder_or_allocation
    hbm_capacity_pre_sold
  missing_green_primitives =
    hbm_capacity_constraint
    revenue_visibility_contract
  verdict = blocked, not FULL_THESIS

005930 삼성전자
  primary_archetype = C06_HBM_MEMORY_CUSTOMER_CAPACITY
  present_primitives =
    revenue_visibility_contract
  missing_green_primitives =
    customer_preorder_or_allocation
    hbm_capacity_constraint
    hbm_capacity_pre_sold
  verdict = blocked, not FULL_THESIS

034020 두산에너빌리티
  primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  present_primitives =
    delivery_schedule
    margin_bridge_visible
  missing_green_primitives =
    contract_amount_to_prior_sales
    contract_duration_months
  verdict = blocked, not FULL_THESIS
```

쉬운 예:

```text
하이닉스는 "고객 배정/프리솔드" 쪽 증거가 잡혔다.
하지만 "실제 병목/제약"과 "매출 가시성 계약" 칸이 비어 있다.
그래서 Green이나 Full Thesis로 올리면 안 된다.

삼성전자는 반대로 "매출 가시성 계약" 비슷한 한 칸만 잡혔다.
고객 배정, capacity constraint, pre-sold가 비어 있다.
그래서 더더욱 운영 Stage가 아니다.
```

## 6. seed materialization 상태

파일:

```text
full_thesis_seed_materialization_trace.jsonl
full_thesis_seed_materialization_audit.json
```

분포:

```text
seed rows = 85

materialization_status:
  PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS = 55
  STAGECOURT_READY_NOT_PROMOTED           = 21
  ACCEPTED_CLAIM_NOT_CREATED             = 8
  STAGECOURT_TRACE_NOT_CREATED            = 1

final_stage_scope:
  CENSUS_EVENT_BOARD = 85

final_score_scale:
  EVENT_WEIGHTED_PARTIAL = 67
  NO_SCORE               = 18

final_operator_stage_use:
  NOT_FULL_THESIS_STAGE = 85

final_operator_score_use:
  NOT_FULL_E2R_SCORE = 85
```

판정:

```text
seed가 Research Brain으로 들어간 것은 맞다.
일부는 StageCourt까지 갔다.
하지만 최종 operator-use 가능한 row는 0개다.
```

## 7. v100에서 확실히 좋아진 부분

이전 v97/v99 대비 v100에서 실제로 닫힌 것:

```text
1. real LLM claim extractor가 실제로 31회 성공했다.
2. bounded live source acquisition이 실제 문서를 가져왔다.
3. accepted_claim -> score_contribution -> stagecourt_trace 경로가 일부 닫혔다.
4. source task realness audit은 LIVE_SOURCE_PASS다.
5. brain_to_claim_trace audit은 PASS다.
6. source_task_satisfaction audit은 critical 0이다.
```

즉 이제 병목은 "LLM이 전혀 안 돈다"가 아니다.

현재 병목은 다음이다.

```text
1. partial Stage 승격 정책이 official-only와 web/LLM을 제대로 분리하지 못한다.
2. per-trace로 승격 가능한 것을 global blocker로 모두 막는다.
3. Full Thesis는 Green primitive coverage가 아직 모자라다.
4. trace rows 3개는 stagecourt_trace_id가 없다.
5. all-archetype source-backed replay가 6/32로 아직 부족하다.
```

## 8. 지금 바로 코드 패치해야 할 방향

### P1. StageCourt partial 승격 lane을 분리한다

현재:

```text
Research Brain StageCourt
  -> web/LLM claim이 없으면 전체 promotion blocked
  -> 공식공시-only trace도 최종표에 안 올라감
```

목표:

```text
Research Brain StageCourt
  -> per-trace 판정

web/LLM claim-backed trace
  -> stage_scope = BRAIN_WEB_PARTIAL
  -> score_scope = BRAIN_WEB_CLAIM_BACKED_PARTIAL

official-only claim-backed trace
  -> stage_scope = BRAIN_OFFICIAL_PARTIAL 또는 BRAIN_CLAIM_PARTIAL
  -> score_scope = BRAIN_OFFICIAL_CLAIM_BACKED_PARTIAL

둘 다:
  -> operator_stage_use = NOT_FULL_THESIS_STAGE
  -> operator_score_use = NOT_FULL_E2R_SCORE
  -> full_thesis_stage = FULL_THESIS_NOT_RUN
```

주의:

```text
BRAIN_OFFICIAL_PARTIAL을 FULL_THESIS처럼 쓰면 안 된다.
그건 "공식 원문으로 일부 칸을 닫았다"는 상태판 신호다.
운영 점수/Green은 아니다.
```

### P2. global blocker를 per-trace blocker로 바꾼다

현재:

```text
19개 official-only trace가 blocker
-> 2개 web/LLM trace도 같이 승격 안 됨
```

목표:

```text
trace A: web/LLM claim 있음
  -> BRAIN_WEB_PARTIAL 승격 가능

trace B: official-only claim 있음
  -> BRAIN_OFFICIAL_PARTIAL 승격 가능

trace C: accepted_claim 또는 score_contribution 없음
  -> not promoted

run-level verdict:
  -> 일부 승격이면 PARTIAL_PROMOTION_APPLIED
  -> unsafe promotion 0이어야 pass
```

다만 readiness 문구는 정직해야 한다.

```text
BRAIN_WEB_PARTIAL 2개가 승격됐다고 FULL_THESIS_READY가 아니다.
official-only 19개가 승격됐다고 Brain/Web minimum을 충족한 것도 아니다.
```

### P3. readiness gate를 source lane별로 쪼갠다

현재:

```text
brain_stage_promotion verdict 하나가 BLOCKED면 Brain/Web readiness 전체 BLOCKED
```

목표:

```text
brain_web_partial_promotion_count
brain_official_partial_promotion_count
full_thesis_promotion_count
unsafe_promoted_count
```

처럼 분리한다.

권장 verdict:

```text
NO_PROMOTION
PARTIAL_PROMOTION_APPLIED
FULL_THESIS_PROMOTION_APPLIED
BLOCKED_UNSAFE
```

`target_gate=brain_web`에서는 `brain_web_partial_promotion_count > 0`가 의미 있을 수 있다.
하지만 `target_gate=full_thesis` 또는 운영 readiness에서는 `full_thesis_promotion_count > 0`와 Green coverage가 필요하다.

### P4. trace ID 없는 3개 brain_to_claim_trace를 닫는다

v100:

```text
brain_trace_missing_stagecourt_ref_count = 3
```

이 3개는 accepted claim은 있지만 StageCourt trace가 없다.

해야 할 것:

```text
1. 왜 StageCourt trace가 생성되지 않았는지 claim 단위로 audit row를 만든다.
2. NO_SCORE_CONTRIBUTION이면 material gap인지, mapping reject인지 분리한다.
3. readiness blocker 문구를 "3개 누락"에서 claim_id/symbol/primitive까지 추적 가능하게 만든다.
```

### P5. Full Thesis runner는 유지하되 Green coverage를 더 닫는다

v100의 Full Thesis runner 자체는 방향이 맞다.
Brain/Web partial 승격과 별개로 `stagecourt_trace_direct_scan`으로 후보 21개를 보며,
source linkage proof도 확인한다.

그러나 Green gate가 아직 닫히지 않았다.

다음 패치는 여기에 집중해야 한다.

```text
1. missing_green_primitives를 follow-up source task로 다시 Brain에 넣는다.
2. official-first source task가 비어 있는 query_intents를 LLM planner input으로 넘긴다.
3. follow-up 결과가 accepted claim으로 닫히면 기존 StageCourt를 append-only로 갱신한다.
4. score delta는 claim delta로 설명한다.
```

## 9. 반드시 추가할 테스트

### 9.1 official-only partial promotion

목표:

```text
OpenDART direct/current score-eligible claim
+ score_contribution
 + StageCourt trace
-> BRAIN_OFFICIAL_PARTIAL로 census_stage_status에 올라간다.
-> operator_stage_use는 NOT_FULL_THESIS_STAGE다.
-> FULL_THESIS로는 올라가지 않는다.
```

나쁜 결과:

```text
official-only라서 아예 상태판에 안 올라감
또는
official-only인데 FULL_THESIS로 올라감
```

### 9.2 mixed trace run에서 global blocker 금지

fixture:

```text
web/LLM trace 2개
official-only trace 19개
invalid trace 1개
```

기대:

```text
web/LLM trace 2개 -> BRAIN_WEB_PARTIAL
official-only trace 19개 -> BRAIN_OFFICIAL_PARTIAL
invalid trace 1개 -> not promoted
run verdict -> PARTIAL_PROMOTION_APPLIED
unsafe_promoted_count -> 0
```

### 9.3 Full Thesis guard 유지

fixture:

```text
BRAIN_OFFICIAL_PARTIAL 또는 BRAIN_WEB_PARTIAL은 존재하지만
missing_green_primitives가 남아 있음
```

기대:

```text
FULL_THESIS row = 0
operator_stage_use = NOT_FULL_THESIS_STAGE
full_thesis_stage = FULL_THESIS_NOT_RUN
```

### 9.4 Samsung / Hynix regression

v100 기준:

```text
005930 삼성전자:
  present = revenue_visibility_contract
  missing = customer_preorder_or_allocation, hbm_capacity_constraint, hbm_capacity_pre_sold
  expected = partial only, not FULL_THESIS

000660 SK하이닉스:
  present = customer_preorder_or_allocation, hbm_capacity_pre_sold
  missing = hbm_capacity_constraint, revenue_visibility_contract
  expected = BRAIN_WEB_PARTIAL possible, not FULL_THESIS
```

테스트 기대:

```text
둘 다 FULL_THESIS/Green으로 승격되면 실패.
둘 다 흔적 없이 CENSUS_EVENT_BOARD에만 묻히면 부분 승격 정책 실패.
```

### 9.5 trace ID 누락 진단

기대:

```text
brain_to_claim_trace row가 stagecourt_trace_id를 못 받으면
symbol, accepted_claim_id, primitive_id, score_support_status, missing_reason을 audit에 남긴다.
```

## 10. 절대 하면 안 되는 패치

```text
1. OpenDART면 무조건 Stage 승격
2. 삼성전자/하이닉스 종목명 예외처리
3. web/LLM claim requirement를 없애고 모든 partial을 BRAIN_WEB_PARTIAL로 부르기
4. missing_green_primitives가 있는데 FULL_THESIS로 올리기
5. EVENT_WEIGHTED_PARTIAL을 FULL_E2R_100처럼 표시하기
6. operator_stage_use를 FULL_THESIS_STAGE로 바꾸기
7. 점수 가중치나 Green threshold를 다시 만지기
8. claim delta 없이 score delta를 허용하기
```

쉬운 예:

```text
삼성전자가 DART 공시 하나로 revenue_visibility_contract를 얻었다.
이건 "한 칸은 채웠다"는 뜻이다.
하지만 HBM 고객 배정, capacity pre-sold, 병목, FCF bridge가 없으면 Green이 아니다.

따라서 올바른 패치는
  CENSUS_EVENT_BOARD에 묻지 말고 BRAIN_OFFICIAL_PARTIAL로 보여준다.
  하지만 FULL_THESIS/Green은 막는다.
```

## 11. 다음 에이전트 공격 포인트

다음 에이전트는 아래를 반드시 확인해야 한다.

```text
1. official-only partial promotion이 프로젝트 official-first 원칙과 맞는가?
2. BRAIN_OFFICIAL_PARTIAL이라는 새 stage_scope가 필요한가,
   아니면 BRAIN_CLAIM_PARTIAL 같은 더 일반 이름이 맞는가?
3. BRAIN_WEB readiness에서 official-only partial을 통과로 세면 안 된다는 점이 audit에 유지되는가?
4. partial promotion 후에도 operator_stage_use가 전부 NOT_FULL_THESIS_STAGE로 남는가?
5. Full Thesis runner가 partial 승격 여부와 무관하게 direct stagecourt scan을 계속 하는가?
6. 삼성전자/하이닉스 fixture가 partial only / not full thesis로 고정되는가?
7. source_proxy_only나 research memory가 production score로 들어오지 않는가?
8. `brain StageCourt traces have no web/LLM accepted claim support`가 run-global blocker가 아니라 per-trace reason으로 내려갔는가?
9. 3개 missing stagecourt_trace_id row의 원인이 audit에 claim 단위로 나온다.
10. full unittest와 census_v4 focused tests가 모두 통과한다.
```

## 12. 최종 판단

v100은 실패가 맞다.
하지만 실패의 성격이 v97/v99와 다르다.

```text
v97/v99:
  real LLM extractor와 충분한 live acquisition 자체가 부족했다.

v100:
  real LLM extractor, live source acquisition, accepted claim, score contribution, StageCourt trace는 상당 부분 생겼다.
  그런데 StageCourt 결과를 최종 상태판에 올리는 promotion policy가 official-only와 web/LLM을 잘못 한 덩어리로 막고 있다.
  Full Thesis는 여전히 Green primitive coverage 부족으로 0개다.
```

따라서 다음 패치 목표는 이것이다.

```text
1. official-only / web-LLM / full-thesis lane을 분리한다.
2. per-trace promotion으로 바꿔 global blocker를 제거한다.
3. partial stage는 상태판에 보여주되 operator-use 불가를 유지한다.
4. Full Thesis/Green은 source linkage + current direct claim + Green primitive coverage가 닫힐 때만 허용한다.
5. 삼성전자/하이닉스는 현재 v100 기준 partial evidence만 있으며 운영 Stage/Score가 아니다.
```

