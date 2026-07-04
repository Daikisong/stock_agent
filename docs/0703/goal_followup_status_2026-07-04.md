# Goal follow-up status - 2026-07-04

## 결론

아직 `goal.md / goal2.md / goal3.md` 완료가 아니다.

이번 작업으로 여러 “거짓 완료” 가능성은 막았고, 전체 테스트는 통과했다. 하지만 실제 운영형 Brain/Web + full-thesis 실행은 아직 `NOT_READY`다. 쉽게 말하면, 채점표와 안전감사 장치는 더 정직해졌지만, 실제 현장 시험에서는 아직 증거 수집/LLM extractor가 최소 운영 조건을 채우지 못했다.

예시:

- 나쁜 상태: `source_task_claim_satisfaction_mismatch_count=330`인데 경고로만 두고 완료라고 말함.
- 지금 패치 후 방향: 이런 mismatch는 hard gate 쪽으로 올리고, score claim이 실제 contribution/stagecourt까지 닫히지 않으면 완료로 못 보게 함.

## 이번에 고친 것

### 1. 런타임 예산이 재현 명령에 빠지는 문제

`--brain-runtime-budget-seconds`는 CLI/config에는 있었지만, 산출물의 reproduction command에 빠질 수 있었다. 이제 재현 명령에도 기록된다.

예시:

```text
실제 실행: 240초 예산
재현 명령: 예산 옵션 없음
```

이면 다음 에이전트가 같은 조건으로 재현할 수 없다. 이 문제를 막았다.

관련 파일:

- `src/e2r/census/census_runner_v4.py`
- `tests/test_census_v4_run_mode_honesty.py`

### 2. source execution 뒤 예산 초과를 놓치는 문제

v139 smoke에서 `runtime_elapsed_seconds=245.5`, `runtime_budget_seconds=240.0`인데 `runtime_budget_exhausted=false`로 끝나는 문제가 잡혔다.

원인은 예산 체크가 source/extractor 큰 작업 덩어리 시작 전에는 있었지만, 그 덩어리 종료 후 최종 판정에는 없었기 때문이다.

패치 후에는 source execution 뒤 예산이 초과되면:

```text
runtime_budget_exhausted_after_source_execution
```

이 progress에 남고, 남은 이벤트는:

```text
not_attempted_after_runtime_budget_exhausted
```

로 기록된다.

v141에서 확인한 결과:

```text
runtime_budget_seconds: 120.0
runtime_elapsed_seconds: 239.202839
runtime_budget_exhausted: true
phase: runtime_budget_exhausted_after_source_execution
```

### 3. source task 사이 runtime budget skip hook

source execution 큰 덩어리가 시작된 뒤에는 각 source task 사이에서도 예산 초과를 확인해야 한다. 이제 `execute_source_tasks_with_evidence_os_v4`가 `runtime_budget_exhausted` callback을 받아 task 시작 전에 예산을 확인한다.

예시:

```text
첫 번째 source task: 예산 안쪽
두 번째 source task 시작 전: 예산 초과 확인
→ 두 번째 task는 fetch/extractor를 실행하지 않고 BUDGET_EXHAUSTED execution으로 남김
```

이때 산출물에는 다음처럼 남는다.

```text
status: BUDGET_EXHAUSTED
provider_name: research_brain_v4_runtime_budget
provider_errors: source_task_skipped_after_runtime_budget_exhausted
extraction_audit.runtime_budget_skipped_source_task_count += 1
```

다만 이것은 "이미 시작한 긴 LLM extractor 호출을 중간에 강제 중단"하는 기능은 아니다. 현재 패치는 task와 task 사이에서 멈추는 안전장치이고, extractor 호출 내부의 문서별 timeout/분할은 다음 작업으로 남아 있다.

v142 이후 추가 패치로, source task가 이미 fetch를 끝낸 뒤에도 document extraction에 들어가기 전에 budget을 한 번 더 확인한다.

예시:

```text
source task 시작 시점: 예산 안쪽
source fetch 완료
document claim extraction 시작 직전: 예산 초과 확인
→ 해당 task는 BUDGET_EXHAUSTED로 종료
→ LLM extractor 호출은 시작하지 않음
```

이 경우 산출물에는 다음이 남는다.

```text
provider_errors: source_task_document_extraction_stopped_after_runtime_budget_exhausted
stop_reason: source_task_extraction_stopped_after_runtime_budget_exhausted
extraction_audit.runtime_budget_stopped_document_extraction_count += 1
```

단, 이것도 이미 실행 중인 Codex/LLM subprocess를 중간에 죽이는 기능은 아니다. "새 긴 호출을 시작하지 않는 가드"다.

관련 파일:

- `src/e2r/research_brain/v4_evidence_extraction_bridge.py`
- `src/e2r/research_brain/v4_production_orchestrator.py`
- `tests/test_research_brain_v4_evidence_extraction_from_real_document.py`
- `tests/test_research_brain_v4_operational_modes.py`

### 4. real planner attempt cap 초과 문제

v137에서 `--brain-max-distinct-candidate-attempts 50`인데 planner 진행이 55까지 가는 문제가 있었다. 이제 real/fake planner loop 모두 `max_distinct_candidate_attempts`를 넘지 않게 막았다.

예시:

```text
최대 50명만 면접하라
→ 55명을 면접하고 나중에 “성공 30명”이라고 말함
```

이런 상태는 운영에서 안 된다. 이제 면접 자체가 cap 안에서 끝난다.

관련 파일:

- `src/e2r/research_brain/v4_production_orchestrator.py`
- `tests/test_research_brain_v4_operational_modes.py`

### 5. source task count 분해 기록

v142 progress에는 `source_task_count: 8`이 찍혔다. 명령은 `--brain-max-source-tasks-per-plan 3`이었기 때문에, 겉으로 보면 cap을 어긴 것처럼 보인다.

실제 구조는 다르다.

```text
planner_generated_source_task_count
+ event_origin_source_task_count
+ mandatory_official_source_task_count
= source_task_count
```

예를 들어:

```text
planner가 만든 task 3개
mandatory official status task 5개
→ total source_task_count 8개
```

이제 `source_execution_start` progress event에 세부 count를 같이 남긴다. 따라서 다음 live 산출물에서는 "3개 cap을 어겼다"가 아니라 "planner task 3개 + mandatory task N개"처럼 해석할 수 있다.

관련 파일:

- `src/e2r/research_brain/v4_production_orchestrator.py`
- `tests/test_research_brain_v4_operational_modes.py`

### 6. LLM claim extractor raw prompt/response 추적

LLM extractor run이 `prompt_hash`, `response_hash`만 있고 실제 raw prompt/response 파일이 없으면 추적이 불가능하다. 이제 성공 run은 raw prompt/response path와 파일을 남기고, audit가 이 파일 누락을 실패로 잡는다.

예시:

```text
해시만 있음
원문 prompt/response 없음
→ 다음 감사자가 “LLM이 뭘 보고 뭘 답했는지” 확인 불가
```

이제 이런 run은 통과할 수 없다.

관련 파일:

- `src/e2r/production/claim_extraction/extractor_provider.py`
- `src/e2r/research_brain/v4_evidence_extraction_bridge.py`
- `src/e2r/census/census_runner_v4.py`
- `tests/test_census_v4_brain_web_readiness_gate.py`

### 7. accepted claim과 score claim을 분리

기존에는 source task에서 accepted claim을 곧바로 score claim처럼 취급할 수 있었다. 이제 source task execution의 `score_claim_ids`는 실제 score contribution ledger가 만들어진 뒤에만 채운다.

예시:

```text
문서에서 “회사 언급” claim 추출
→ accepted claim은 맞을 수 있음
→ 그러나 점수 기여 claim은 아님
```

accepted claim 전체를 score chain으로 과대 계산하지 않게 했다.

### 8. source-task satisfaction mismatch hard gate 강화

`source_task_claim_satisfaction_mismatch_count`가 warning으로 남아 있으면, “source task가 claim을 만족했다”는 말과 “실제 score/stage chain이 닫혔다”는 말이 섞인다.

이번 패치에서는 source task의 score claim reference만 엄격히 score contribution/stagecourt까지 닫히는지 검사하고, mismatch를 critical gate에 올렸다.

### 9. full thesis missing primitive 승격 차단

`FULL_E2R_100` 같은 row가 `full_thesis_missing_primitives`를 갖고도 `FINAL/COMPLETE`로 승격되는 문제가 있었다. 이제 missing green primitive가 있으면 production full thesis 승격을 막고 follow-up/pending 쪽으로 남긴다.

예시:

```text
C06 Green 필수: customer allocation + revenue/cash bridge
현재: customer allocation만 있음
→ 점수 일부는 가능
→ full thesis Green 완료는 불가
```

### 10. controlled smoke와 production full thesis 대체 통과 분리

controlled smoke 또는 production substitute가 full thesis smoke requirement를 대신 통과시키는 흐름을 제거했다. smoke가 필요하면 smoke execution 자체가 pass해야 하고, production full thesis도 missing primitive 없이 별도로 pass해야 한다.

### 11. semantic guard 보강: 유동성공급계약 차단

`유동성공급계약`은 고객 매출 계약이 아니다. 증권 거래 유동성을 공급하는 계약을 `contract_quality` 점수로 보면 안 된다.

이번에 추가로 막은 예:

```text
원티드랩 유동성공급계약의 체결
→ accepted claim으로 기록될 수는 있음
→ customer revenue contract 점수는 0
```

이 때문에 cached artifact의 대표 score claim 수가 `79 -> 78`로 줄었다. 이는 의도한 변화다. 테스트도 “숫자 79 고정”이 아니라 “대표 claim chain이 모두 닫혔는가”를 보도록 바꿨다.

## 실행 결과

### 단위/통합 테스트

최종 전체 테스트:

```text
PYTHONPATH=src python -m unittest discover -s tests -v
Ran 5163 tests in 251.625s
OK
```

중간에 `79 -> 78` 고정 숫자 실패가 있었지만, 원인은 semantic guard가 `유동성공급계약` 점수 누수를 막은 정상 변화였다. 테스트를 구조 감사 방식으로 바꾼 뒤 전체 5163개 테스트가 통과했다.

추가로 source-task runtime budget skip hook을 검증하는 단위 테스트도 포함됐다.

```text
test_runtime_budget_callback_skips_remaining_source_tasks
test_runtime_budget_callback_stops_document_extraction_inside_source_task
test_runtime_budget_exhausted_after_source_execution_marks_remaining_events_pending
test_missing_external_web_plan_retry_preserves_source_execution_budget
```

### v137

경로:

```text
output/census_v4/2026-07-01-v137-goal-followup-hard-gates
```

상태:

```text
INVALID_PARTIAL_OUTPUT
```

의미:

- 사람이 중단한 partial run이다.
- readiness, score, Stage 증거로 쓰면 안 된다.
- 이 실행에서 planner attempt cap 초과 문제가 발견됐다.

### v138

경로:

```text
output/census_v4/2026-07-01-v138-goal-followup-capped
```

상태:

```text
INVALID_PARTIAL_OUTPUT
```

의미:

- cap 패치 후 planner attempt cap은 지켜졌다.
- 다만 source execution이 길어져 사람이 중단했다.
- readiness, score, Stage 증거로 쓰면 안 된다.

### v139

경로:

```text
output/census_v4/2026-07-01-v139-goal-followup-budgeted-smoke
```

상태:

```text
NOT_READY
```

의미:

- 정상 종료했지만, source execution 뒤 budget exhausted 판정 패치 전 산출물이다.
- `runtime_elapsed_seconds > runtime_budget_seconds`인데 exhausted flag가 false로 남는 문제가 이 실행에서 확인됐다.
- 완료 증거로 쓰면 안 되고, 버그 발견 증거로만 쓴다.

### v140

경로:

```text
output/census_v4/2026-07-01-v140-goal-followup-budgeted-smoke
```

상태:

```text
NOT_READY
```

주요 관찰:

```text
real_provider_success_count: 1
claim_extractor_run_count: 2
web_fetched_documents: 2
web/LLM accepted claim: 1
runtime_elapsed_seconds: 187.944941
runtime_budget_seconds: 240.0
runtime_budget_exhausted: false
```

의미:

- real planner와 LLM extractor가 실제로 실행됐다.
- raw prompt/response path audit는 파일 누락 없이 작동했다.
- 하지만 운영 최소 조건에는 한참 부족하다.

blocker 예:

```text
planner runs 21/30
web search tasks 3/20
fetched documents 2/10
claim extractor attempts 2/10
web/LLM accepted claims 1/3
LLM extractor timeout/provider error 1
```

### v141

경로:

```text
output/census_v4/2026-07-01-v141-goal-followup-budget-exhaustion-smoke
```

상태:

```text
NOT_READY
```

주요 관찰:

```text
runtime_budget_seconds: 120.0
runtime_elapsed_seconds: 239.202839
runtime_budget_exhausted: true
phase includes: runtime_budget_exhausted_after_source_execution
planner pending rows: not_attempted_after_runtime_budget_exhausted
```

의미:

- source execution 뒤 예산 초과를 놓치지 않는 패치는 실제 산출물에서도 확인됐다.
- 다만 LLM extractor 2건이 timeout으로 끝나 accepted Brain/Web claim은 0이다.
- 따라서 full thesis/Brain-Web readiness는 계속 `NOT_READY`가 맞다.

### v142

경로:

```text
output/census_v4/2026-07-01-v142-goal-followup-budget-hook-smoke
```

상태:

```text
NOT_READY
```

주요 관찰:

```text
runtime_budget_seconds: 60.0
runtime_elapsed_seconds: 156.967248
runtime_budget_exhausted: true
phase includes: runtime_budget_exhausted_after_source_execution
research_brain_v4 source task executions: 8
NO_EVIDENCE_FOUND: 2
PROVIDER_FAILED: 1
BUDGET_EXHAUSTED: 5
accepted Brain/Web claim: 0
```

의미:

- 새 source-task runtime budget hook이 실제 산출물에서도 확인됐다.
- 뒤쪽 mandatory official status task 5개가 `BUDGET_EXHAUSTED`로 남았다.
- 각 skipped task는 `provider_name=research_brain_v4_runtime_budget`, `provider_errors=source_task_skipped_after_runtime_budget_exhausted`, `budget_used={queries:0,candidates:0,fetches:0}`로 기록됐다.
- 즉 예산 초과가 "증거 없음으로 점수 0 확정"이 아니라 "예산 때문에 해당 source task를 못 끝냄"으로 남는다.
- 하지만 60초 runtime budget 실행이 156.9초에 끝났다. 이미 시작한 provider/extractor 호출은 아직 runtime budget으로 즉시 중단되지 않는다는 뜻이다.

쉬운 예:

```text
60분짜리 시험
58분에 긴 면접 하나를 시작함
면접 자체가 90분짜리라 60분에 바로 종료하지 못함
끝난 뒤 남은 면접은 budget exceeded로 skip
```

v142는 바로 이 상태다. task 사이 budget skip은 됐지만, "진행 중인 긴 면접"을 더 잘게 쪼개는 작업은 아직 필요하다.

### v143 / v144

경로:

```text
output/census_v4/2026-07-01-v143-goal-followup-source-count-budget-guard-smoke
output/census_v4/2026-07-01-v144-goal-followup-source-count-budget-guard-smoke
```

상태:

```text
INVALID_PARTIAL_OUTPUT
```

의미:

- 두 실행 모두 readiness, score, Stage 증거로 쓰면 안 된다.
- v143은 `brain_runtime_budget_seconds=45.0`, v144는 `90.0`이었다.
- 두 실행 모두 real planner는 성공했지만, `missing_external_web_plan_retry`까지 거친 뒤 source execution 시작 전에 budget이 소진됐다.
- 결과적으로 `source_task_execution_count=0`이고, source task count 분해 필드를 live 산출물에서 확인하지 못했다.

쉽게 말하면:

```text
목표: source task가 3개인지 8개인지 확인하려고 함
실제: 면접 계획과 재질문 단계에서 시간 다 씀
결과: source task 면접장에는 들어가지도 못함
→ 이 실행으로는 source task count를 판단하면 안 됨
```

다음 live 확인은 다음 중 하나가 필요하다.

```text
1. runtime budget을 planner+retry+source까지 충분히 크게 잡는다.
2. missing_external_web_plan_retry가 source 예산을 다 먹지 않도록 별도 budget/reserve를 둔다.
3. source count 분해는 우선 unit test와 다음 정상 NOT_READY run에서 확인한다.
```

v144 이후 코드에는 2번에 해당하는 패치가 들어갔다.

```text
remaining runtime budget < source_execution_reserved_budget_seconds
→ missing_external_web_plan_retry skip
→ phase: missing_external_web_plan_retry_skipped_insufficient_source_budget
→ source execution으로 넘어감
```

단위 테스트는 통과했고, 아래 v145에서 live 산출물도 확인했다.

### v145

경로:

```text
output/census_v4/2026-07-01-v145-goal-followup-retry-reserve-live-smoke
```

상태:

```text
NOT_READY
```

주요 관찰:

```text
phase: missing_external_web_plan_retry_skipped_insufficient_source_budget
runtime_budget_seconds: 90.0
runtime_budget_remaining_seconds: 36.408267075021286
source_execution_reserved_budget_seconds: 45.0

source_execution_start:
  planner_generated_source_task_count: 3
  event_origin_source_task_count: 0
  mandatory_official_source_task_count: 5
  source_task_count: 8

source task executions from Research Brain:
  NO_EVIDENCE_FOUND: 2
  PROVIDER_FAILED: 1
  BUDGET_EXHAUSTED: 5
  accepted Brain/Web claim: 0
```

의미:

- retry reserve가 live에서도 동작했다.
- v143/v144처럼 retry가 source budget을 다 먹고 source execution 0개가 되는 문제는 피했다.
- `source_task_count=8`의 구성도 live progress에 분해되어 남았다.
- 그래도 accepted Brain/Web claim은 0이므로 full thesis/Brain-Web readiness는 여전히 `NOT_READY`다.

쉬운 예:

```text
재질문을 더 하면 면접 시간이 없어짐
→ 재질문은 건너뜀
→ 면접은 진행함
→ 답안지는 아직 합격 수준으로 안 채워짐
```

## 현재 남은 blocker

### 1. Brain/Web evidence pass가 아직 false

v140/v141/v142/v145 모두 real planner와 extractor는 실행됐지만 운영 최소 조건을 못 채웠다.

쉽게 말하면:

```text
면접관은 실제로 불렀고
후보자도 일부 조사했지만
합격 판정을 내릴 만큼 답안지가 아직 채워지지 않았다.
```

### 2. LLM extractor timeout

SK하이닉스 C06 source execution에서 extractor가 timeout을 냈다. v141은 2건 모두 timeout이었다.

source task와 source task 사이의 budget skip hook은 들어갔다. v142 이후에는 document extraction 시작 직전 budget guard도 들어갔다. 하지만 이미 시작한 긴 extractor 호출 하나를 중간에 강제로 끊지는 못한다. 쉽게 말하면:

```text
task A 완료 후 예산 초과 확인
→ task B는 BUDGET_EXHAUSTED로 skip 가능

task A에서 source fetch 후 예산 초과 확인
→ LLM extractor 호출을 시작하지 않고 BUDGET_EXHAUSTED 가능

task A의 LLM 호출이 이미 120초짜리로 시작됨
→ 호출 중간에는 아직 runtime budget으로 자르지 못함
```

따라서 다음 패치 대상은 extractor 입력을 문서별/청크별로 더 작게 나누고, 이미 실행 중인 subprocess timeout을 더 짧고 명확한 budget과 연결하는 것이다.

### 3. source execution task 수가 planner cap보다 많아 보이는 문제

명령은:

```text
--brain-max-source-tasks-per-plan 3
```

인데 C06 source execution progress에는:

```text
source_task_count: 8
```

이 찍혔다.

원인은 planner task 3개 뒤에 mandatory official status tasks가 추가되기 때문이다. 이 자체가 무조건 버그는 아니다. 예를 들어 고객 계약을 보려면 DART/KIND/listing/trading status 같은 기본 확인은 별도 mandatory task일 수 있다.

v142 이후 코드에는 이 구분을 progress event에 남기는 패치가 들어갔다.

```text
planner_generated_task_count
mandatory_official_task_count
total_source_task_count
```

v145에서 이 분해 기록도 live progress에 확인됐다. 그리고 각 task도 계속 개별 budget/stop condition을 가져야 한다.

### 4. full thesis는 아직 production pass가 아니다

현재 blocker:

```text
full_thesis_smoke_pending
full_thesis_production_pass_false
full_thesis_seed_promotion_pass_false
brain_web_evidence_pass_false
```

따라서 “goal 완료”라고 쓰면 안 된다.

### 5. missing_external_web_plan_retry가 source budget을 먹는 문제

v143/v144에서 real planner는 성공했지만, 이후 `missing_external_web_plan_retry`가 runtime budget을 추가로 사용했다. 그 결과 source execution 시작 전에 budget이 소진되어 `source_task_execution_count=0`이 됐다.

이 자체는 "거짓 READY"를 막는 관점에서는 맞다. 하지만 source count 분해나 evidence extraction을 검증하려는 run에서는 비효율적이다.

예시:

```text
예산 90초
planner 52초
missing web plan retry 52초
→ source execution 시작 전 이미 104초
→ source task 전부 skip
```

다음 패치 후보:

```text
missing_external_web_plan_retry_budget_seconds
source_execution_reserved_budget_seconds
retry_skipped_insufficient_source_budget
```

현재 코드에는 우선 `source_execution_reserved_budget_seconds` 계산과 `retry_skipped_insufficient_source_budget` phase가 들어갔다. 즉 retry가 필요하더라도 source execution을 아예 못 하게 만들 정도면, retry를 skip하고 그 이유를 남기는 쪽으로 바꿨다.

v145에서 live 확인도 됐다. 아직 남은 부분:

```text
reserve 값을 config/CLI로 노출할지 판단
```

## 다음 작업 순서

1. extractor 호출 내부 budget 제어를 더 촘촘히 한다.
   - source task 사이 `BUDGET_EXHAUSTED` skip은 unit test와 v142 산출물에서 확인됐다.
   - document extraction 시작 전 `BUDGET_EXHAUSTED` guard는 unit test로 확인됐다.
   - 아직 이미 시작한 긴 LLM extractor/provider 호출을 runtime budget으로 즉시 끊지는 못한다.
   - 다음 패치는 더 작은 prompt 단위와 subprocess timeout/budget 연결이다.

2. LLM extractor timeout을 줄인다.
   - prompt compaction을 더 공격적으로 한다.
   - 한 task가 여러 긴 문서를 물고 들어가면 문서별로 쪼개거나 우선순위를 둔다.
   - 단, rule fallback으로 “성공한 척” 하면 안 된다.

3. source task count를 분해해서 감사한다.
   - progress field와 unit test는 추가됐다.
   - v145에서 `planner_generated_source_task_count`, `event_origin_source_task_count`, `mandatory_official_source_task_count`가 실제 산출물에 남는 것까지 확인됐다.
   - `max_source_tasks_per_plan`은 planner-generated task cap임을 문서에 계속 명시한다.

4. missing web plan retry reserve 값을 운영 config로 노출할지 판단한다.
   - unit test와 v145 live smoke는 통과했다.
   - 현재 reserve는 `max(30, min(90, claim_extractor_timeout_seconds * 3))` 계산값이다.
   - 운영자가 직접 조정해야 할 값이면 CLI/config로 노출한다.

5. bounded live run을 다시 한다.
   - 사람이 중단하지 않는다.
   - runtime budget/attempt cap/source task budget이 모두 산출물에 남아야 한다.
   - `NOT_READY`면 blocker가 정확히 기록돼야 하고, `READY`면 claim -> contribution -> StageCourt -> representative stage chain이 닫혀야 한다.

6. 그 뒤 subagent 5명에게 다시 교차검증을 맡긴다.
   - 지금은 아직 subagent final pass를 받을 단계가 아니다.
   - 이유: full thesis goal이 아직 `NOT_READY`이기 때문이다.

## 현재 판단

이번 작업은 goal 완료가 아니라 goal 진행 중의 안전장치 보강이다.

좋아진 점:

- full test 5163개 통과.
- real planner attempt cap 초과 수정.
- runtime budget reproduction command 누락 수정.
- source execution 뒤 budget exhausted 누락 수정.
- source task 사이 `BUDGET_EXHAUSTED` skip hook 추가.
- source fetch 후 document extraction 시작 전 `BUDGET_EXHAUSTED` guard 추가.
- source task count를 planner/event-origin/mandatory official로 분해 기록.
- missing web plan retry가 source budget을 다 먹지 않게 reserve guard 추가.
- LLM raw prompt/response 파일 감사 강화.
- source task score claim chain 과대 계산 방지.
- full thesis missing primitive 승격 차단.
- 유동성공급계약의 customer contract 점수 누수 차단.

아직 아닌 점:

- Brain/Web full thesis production pass 아님.
- Samsung/Hynix full live 운영 판정 완료 아님.
- LLM extractor timeout이 남아 있음.
- source task/document extraction 시작 전 budget guard는 생겼지만, 이미 실행 중인 extractor subprocess 제어는 아직 충분하지 않음.
- missing web plan retry reserve는 단위 테스트와 v145 live smoke 통과, config 노출 여부 미정.
- subagent 최종 재검증 전.

따라서 다음 에이전트는 이 문서를 보고 “완료된 goal”이 아니라 “테스트는 통과했지만 live full-thesis readiness가 아직 blocked인 상태”로 이어받아야 한다.
