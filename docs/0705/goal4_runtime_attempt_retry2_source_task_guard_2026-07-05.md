# Goal4 Runtime Attempt Retry2 Source-Task Guard - 2026-07-05

## 결론

이번 실행은 Goal4 완료가 아니다. `2026-07-05-goal4-all-archetype-next-runtime-attempt-retry2`는 중간에 `INVALID_PARTIAL_OUTPUT`으로 중단했으므로 score/stage 증거로 쓰면 안 된다.

대신 이번 실행에서 중요한 운영 결함을 확인하고 최소 패치했다.

```text
1. Codex planner batch timeout 하나가 batch 전체 후보를 실패로 만들던 문제
2. missing external web plan retry가 source/claim 실행 예산을 잡아먹을 수 있던 문제
3. R13 follow-up seed의 `REDTEAM` 표기가 explicit red-team 이벤트로 인식되지 않던 문제
4. 실행 가능한 official-first `source_task_drafts`가 있는데도 external-web gap retry 대상으로 잡히던 문제
```

쉬운 예:

```text
기존:
  5명 시험지를 한 번에 채점하다 timeout
  -> 5명 전부 결시 처리

패치:
  batch timeout이면 1명씩 다시 채점
  -> 실제로 답할 수 있는 후보는 살림
```

또 다른 예:

```text
기존:
  "도서관/공시/뉴스 중 어디를 찾을지" 신청서를 다시 쓰느라
  실제 원문 수집/claim 추출 시간이 사라질 수 있음

패치:
  source 실행 예산이 부족해지면 보강 retry를 멈추고 progress에 기록
```

## 실행 명령

실행 output root:

```text
output/census_v4/2026-07-05-goal4-all-archetype-next-runtime-attempt-retry2
```

핵심 옵션:

```text
--brain-planner-provider real
--brain-source-acquisition live_full_bounded
--brain-universe-limit 111
--brain-planner-success-limit 111
--brain-planner-batch-size 5
--brain-max-source-tasks-per-plan 5
--brain-max-fetches-per-task 3
--brain-accepted-claim-target 36
--brain-runtime-budget-seconds 7200.0
--brain-candidate-event-seed-path docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl
```

## 왜 중단했는가

실행은 planner 111개까지 도달했다. 중간 상태:

```text
planner_runs: 111
real_provider_success: 102
provider_error:
  R13 primary is only allowed for explicit red-team events: 9
```

그 뒤 `missing_external_web_plan_retry_start`로 들어갔다.

정정된 관찰은 다음과 같다.

```text
planner success rows: 102
with query_intents: 102
with source_task_drafts: 102
with exported source_tasks leaf in this partial root: 0
_external_web_plan_gaps 기준 retry target: 15
```

쉬운 예:

```text
"삼성전자 HBM 고객 배정 검색"이라는 검색어도 있고,
"DART/IR/CompanyGuide에서 먼저 찾고 필요하면 리포트 PDF를 보라"는 source_task_draft도 있었다.
그런데 partial root는 아직 source execution까지 못 갔기 때문에 exported source_tasks leaf가 없었다.
```

지난 문서의 `source_tasks: 없음` 표현은 부정확했다. 정확히는 `planner output.source_task_drafts`는 있었고, 아직 source execution 단계로 내려가기 전이라 `source_tasks.jsonl` leaf가 새로 생성되지 않은 상태였다.

그럼에도 retry가 시작된 이유는 일부 planner output에서 `_external_web_plan_gaps`가 `no_external_web_source_task`를 반환했기 때문이다. 이 15개는 대체로 다음 형태였다.

```text
source_task_drafts: 있음
primitive_gap: revenue_visibility_contract / contract_visibility / order_backlog_to_sales 등
route: DART/KIND/IssuerIR/CompanyGuide official-first
판정: no_external_web_source_task
```

즉 문제는 "LLM이 source task를 비웠다"가 아니라:

```text
실행 가능한 official-first source task가 있는데
external-web 보강 조건이 그것을 gap처럼 보아 retry를 먼저 태움
```

에 더 가까웠다.

이 자체는 source route를 더 좋게 만들 수도 있지만, 기존 코드에는 retry loop 내부 progress와 source 예산 중간 차단이 없었다.

즉 다음 위험이 있었다.

```text
이미 있는 source task를 실행하기 전에 external-web 보강 retry에 시간을 씀
-> 실제 source fetch / claim extractor / StageCourt까지 못 감
-> Goal4 검증이 또 partial로 끝남
```

또한 해당 output root에는 7월 1일 파일이 섞여 있었다.

```text
source_tasks.jsonl: 2026-07-01 06:18:10
source_task_executions.jsonl: 2026-07-01 06:18:10
accepted_claims.jsonl: 2026-07-01 06:18:10
planner_runs.jsonl: 2026-07-06 17:44:35
```

따라서 retry2 root는 "현재 planner 결과 + 과거 source/claim leaf가 섞일 수 있는 partial"로 봐야 한다.

중단 결과:

```text
INVALID_PARTIAL_OUTPUT
```

## 관찰된 blocker

### 1. R13 primary 정책 오류

9개 planner row가 다음 오류로 실패했다.

```text
R13 primary is only allowed for explicit red-team events
```

해석:

```text
R13은 정상 아키타입 full thesis primary가 아니라 cross-archetype red-team overlay다.
그런데 seed event가 일반 full-thesis refresh처럼 들어가면서 validator가 막았다.
```

쉬운 예:

```text
C06, C08은 "환자 진료 과목"이다.
R13은 "진료 후 위험 재검표"다.
위험 재검표를 진료 과목으로 접수하면 접수창에서 막히는 게 맞다.
```

다음 패치 방향:

```text
R13 seed는 explicit red-team event type/source_family로 생성하거나
Goal4 full-thesis primary count에서는 R13을 별도 overlay matrix로 분리해야 한다.
```

### 2. planner source task 초안은 있었지만 retry 판정이 과했다

102개 성공 planner에는 모두 `source_task_drafts`가 있었다. 다만 helper 기준으로 15개가 `no_external_web_source_task` retry 대상으로 잡혔다.

예시:

```text
symbol: 005930
top_arch: C06_HBM_MEMORY_CUSTOMER_CAPACITY
query_intents:
  - 005930 삼성전자 HBM revenue visibility customer allocation contract 2026 IR
  - Samsung Electronics 005930 HBM revenue visibility customer allocation broker report PDF 2026
source_task_drafts:
  - preferred: IssuerIR, DART, KIND, CompanyGuide
    fallback: BrokerReportPDF
    primitive_gap: revenue_visibility_contract
  - preferred: BrokerReportPublicPDF, BrokerReportPDF
    fallback: CompanyNewsroom
    primitive_gap: revenue_visibility_contract
helper external-web check: false
```

이건 LLM이 source task를 못 만든 문제가 아니다. official-first primitive는 웹 fallback을 함부로 타면 안 된다는 정책과 external-web retry 조건이 충돌한 것이다.

패치 방향:

```text
source_task_drafts가 이미 있으면 먼저 source execution으로 내려간다.
external-web 보강은 source task 자체가 비었거나 query가 비었을 때만 missing plan retry로 처리한다.
```

단, official-solvable gap을 TrustedNews/GeneralWebSearch로 강제로 보내면 안 된다. AGENTS.md 원칙대로 LLM이 source task를 작성하고, 코드는 검증/실행만 해야 한다.

### 3. missing external web retry가 너무 비가시적이었다

기존 progress:

```text
missing_external_web_plan_retry_start
... 장시간 무출력 ...
```

패치 후 progress:

```text
missing_external_web_plan_retry_batch_start
missing_external_web_plan_retry_batch_end
missing_external_web_plan_retry_stopped_insufficient_source_budget
```

쉬운 예:

```text
기존:
  대기실에 들어간 뒤 아무 알림 없음

패치:
  몇 번째 batch를 다시 묻는지,
  몇 개가 교체됐는지,
  source 실행 시간을 보존하려고 언제 멈췄는지 기록
```

## 코드 패치

### 1. planner batch timeout split retry

파일:

```text
src/e2r/research_brain/v4_planner_runtime.py
src/e2r/research_brain/v3_llm_planner_provider.py
```

변경:

```text
PlannerProviderUnavailable 중 timeout 계열 오류
+ len(events) > 1
-> 후보를 1개씩 재시도
```

효과:

```text
batch 하나가 timeout이어도 후보 전체를 provider_error로 버리지 않는다.
```

### 2. missing external web retry progress/budget guard

파일:

```text
src/e2r/research_brain/v4_production_orchestrator.py
```

변경:

```text
_retry_planner_for_missing_external_web_plan(
  started_at=...,
  progress_events=...
)
```

batch마다:

```text
1. source 실행 예산 부족 여부 확인
2. batch start/end progress 기록
3. 부족하면 retry를 멈추고 기존 planner run을 보존
```

중요한 점:

```text
이 패치는 점수/Stage를 올리거나 내리지 않는다.
source task를 만들기 위한 LLM retry가 운영 실행 전체를 잡아먹지 않게 하는 실행 안전장치다.
```

### 3. R13 explicit redteam 판정

파일:

```text
src/e2r/research_brain/v4_planner_runtime.py
```

변경:

```text
event text에 "redteam" 단일 토큰이 있으면 explicit R13 red-team event로 인정
```

효과:

```text
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM 같은 seed가
"red team" 띄어쓰기만 없다는 이유로 validator에서 막히지 않는다.
```

쉬운 예:

```text
"REDTEAM"이라고 적힌 재검표를 "red team" 띄어쓰기가 없다고 접수 거부하지 않게 한 것.
```

### 4. executable official-first draft는 retry 없이 source execution으로 진행

파일:

```text
src/e2r/research_brain/v4_production_orchestrator.py
```

변경:

```text
source_task_drafts가 비어 있지 않으면 no_external_web_source_task gap으로 보지 않음
```

효과:

```text
DART/KIND/IssuerIR/CompanyGuide로 바로 검증 가능한 task는
external-web 보강 retry 전에 source execution으로 내려간다.
```

## 검증

통과:

```text
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_real_planner_provider -v
  8 tests OK

PYTHONPATH=src python -m unittest tests.test_research_brain_v4_operational_modes -v
  78 tests OK

PYTHONPATH=src python -m unittest tests.test_research_brain_v4_real_planner_provider tests.test_research_brain_v4_operational_modes -v
  86 tests OK

PYTHONPATH=src python -m unittest tests.test_research_to_runtime_parity_goal4 -v
  8 tests OK

PYTHONPATH=src:tests python -m unittest tests.test_research_brain_v2_r13_overrouting tests.test_research_brain_v3_real_planner_provider -v
  7 tests OK

PYTHONPATH=src python -m unittest discover -s tests -v
  5267 tests OK

git diff --check
  OK
```

추가된 테스트:

```text
test_batch_timeout_retries_each_candidate_instead_of_failing_whole_batch
test_r13_redteam_reason_code_is_explicit_primary_signal
test_missing_external_web_plan_retry_does_not_block_executable_official_source_tasks
test_missing_external_web_plan_retry_stops_before_starving_source_budget_mid_loop
```

재계산:

```text
retry2 planner_runs.jsonl을 새 _external_web_plan_gaps 기준으로 재평가
rows: 111
gap_counts_after_patch:
  NO_GAP: 111

retry2 planner_runs.jsonl의 successful planner rows를 source_tasks_from_planner_output_v4로 재평가
successful planner rows: 102
materialized source tasks: 208
no_task_examples: 0
```

## Goal4 현재 상태

아직 미완료다.

이번에 확인된 상태:

```text
전 아키타입 seed 111개 입력은 planner까지 도달 가능
기존 retry2 planner success는 102/111
기존 retry2 R13 primary policy failure는 9개
패치 후 R13 REDTEAM 단일 토큰은 explicit red-team event로 인정됨
기존 retry2 성공 planner 102개에는 source_task_drafts가 있었음
패치 후 같은 planner output은 missing external web retry gap 0개로 재평가됨
패치 후 같은 planner output은 208개 source task로 materialize 가능함
retry2 output은 INVALID_PARTIAL_OUTPUT이라 score/stage 증거로 폐기
```

따라서 다음 Goal4 작업 우선순위:

```text
1. retry2 같은 실행은 반드시 clean output root에서 시작하게 강제
2. clean root에서 111개 재실행 후 source task, fetch, accepted claim, StageCourt matrix까지 다시 산출
3. source execution 이후 accepted claim 0 또는 mapping rejection이 남는 아키타입을 source route/primitive family 단위로 다시 좁힘
4. R13은 primary production full thesis가 아니라 overlay/readiness matrix로 분리해 해석
5. `PRODUCTION_FULL_E2R_SCORE_PATH_PASS`와 `MEANINGFUL_FULL_THESIS_PASS`를 계속 분리
```

## 운영 해석

이번 결과는 "stage가 있는 애들이 없다"는 질문에 더 가까운 답을 준다.

현재 문제는 점수표가 부족한 게 아니다.

```text
query는 생김
planner source_task_drafts도 생김
그런데 optional external-web retry가 먼저 끼어 source execution으로 내려가기 전에 partial 중단됨
이제 같은 planner output은 retry gap 없이 source execution으로 내려갈 수 있음
다음 병목은 fetch/claim/mapping 단계에서 실제로 accepted claim이 생기는지다
```

쉬운 예:

```text
연구원이 "삼성전자 HBM 고객 배정을 찾아야 한다"고 말은 했다.
그리고 "DART/IR/CompanyGuide를 먼저 보고, 필요한 경우 bounded report source를 보라"는 작업 지시서도 냈다.
그런데 접수대에서 "외부웹 신청이 더 필요하다"며 다시 줄을 세워 실제 검사실로 못 내려갔다.
이번 패치는 그 줄 세우기를 줄여, 다음 실행이 검사실(source fetch/claim extraction)로 내려가게 만든 것이다.
```

이번 패치는 그 실패를 덮어 점수를 만들지 않고, 실패 지점을 더 정확히 보이게 만든 것이다.
