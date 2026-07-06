# Goal4 All-Archetype Registry Parity Patch - 2026-07-06

## 결론

이번 패치는 Goal4를 완료 처리한 것이 아니다.

이번에 고친 것은 **전수 matrix의 기준을 사람 손으로 적은 36개/대표 6개가 아니라 현재 registry 자체로 바꾼 것**이다.

쉬운 예:

```text
이전 위험:
출석부에 원래 학생이 37명인데 시험 결과표 테스트가 "36명 있으면 OK"라고 되어 있으면
새로 들어온 학생 1명이 빠져도 통과할 수 있다.

이번 패치:
출석부(registry)를 먼저 읽고,
결과표(matrix)에 그 학생이 정확히 한 줄 있는지 검사한다.
없으면 "점수 없음"으로 숨기지 않고 "결과표 입력 row 누락"으로 표시한다.
```

따라서 이번 패치는 `C05 외 전체 아키타입의 attempt/source route/accepted claim/full thesis 상태를 전수 matrix로 증명`해야 한다는 Goal4 요구에 맞춰, matrix의 source of truth를 강화한 작업이다.

## 왜 필요했나

`docs/core/goal4.md`는 다음을 요구한다.

```text
C06/C08/C15/C17/C24/C28은 대표 canary일 뿐이다.
C01~C32/C36 전체에 대해
attempt / source route / accepted claim / primitive coverage / blocker를 matrix로 만들어야 한다.
```

그런데 기존 테스트 일부는 다음처럼 현재 레포 상태를 숫자로 고정했다.

```text
registry_contract_count == 36
c01_to_c32_contract_count == 32
r13_cross_archetype_contract_count == 4
```

현재는 이 숫자가 맞지만, 이 방식은 목표와 미묘하게 어긋난다.

```text
목표:
현재 registry에 있는 전체 아키타입을 자동 로드해 전수 증명

취약한 방식:
현재 우연히 36개니까 36개인지 확인
```

그래서 registry ID 목록 자체를 산출물에 넣고, downstream matrix가 그 목록을 기준으로 행을 만들도록 바꿨다.

## 코드 변경

### 1. `research_to_runtime_parity.py`

추가한 출력 필드:

```json
{
  "registry_archetype_ids": ["..."],
  "registry_scope_counts": {
    "C_CANONICAL_ARCHETYPE": 32,
    "R13_CROSS_ARCHETYPE": 4
  }
}
```

의미:

```text
registry_archetype_ids
= 현재 evidence contract registry에서 읽은 정식 아키타입 ID 목록

registry_scope_counts
= C canonical / R13 cross-archetype 같은 scope 분포
```

이제 다른 module은 "36개일 것이다"라고 추측하지 않고 이 목록을 기준으로 검증할 수 있다.

### 2. `all_archetype_runtime_status_matrix.py`

변경 전:

```text
parity_audit["rows"]에 들어온 row만 matrix row로 사용
```

변경 후:

```text
registry_archetype_ids를 먼저 읽음
→ registry의 모든 archetype에 대해 row를 생성
→ parity audit row가 없으면 누락 row로 표시
```

추가한 matrix 필드:

```json
{
  "registry_archetype_ids": ["..."],
  "matrix_row_archetype_ids": ["..."],
  "missing_parity_source_row_ids": [],
  "duplicate_parity_source_row_ids": [],
  "extra_parity_source_row_ids": [],
  "missing_parity_source_row_count": 0,
  "duplicate_parity_source_row_count": 0,
  "extra_parity_source_row_count": 0,
  "all_registered_archetypes_have_exactly_one_runtime_status_row": true,
  "canonical_c_archetype_count": 32,
  "cross_archetype_contract_count": 4,
  "registry_scope_counts": {
    "C_CANONICAL_ARCHETYPE": 32,
    "R13_CROSS_ARCHETYPE": 4
  }
}
```

각 row에는 다음 필드도 추가했다.

```json
{
  "parity_source_row_present": true
}
```

만약 registry에는 있는데 parity audit 입력 row가 빠지면:

```json
{
  "parity_source_row_present": false,
  "runtime_attempt_status": "NOT_ATTEMPTED",
  "runtime_status": "NOT_ATTEMPTED",
  "primary_blocker_class": "RUNTIME_PARITY_SOURCE_ROW_MISSING",
  "next_required_action": "REBUILD_PARITY_AUDIT_FROM_CURRENT_REGISTRY_BEFORE_RUNTIME_CLAIM"
}
```

쉬운 예:

```text
아키타입이 실패한 것인지,
아예 결과표에 안 적힌 것인지,
둘은 다르다.

이번 패치는 "결과표에 안 적힌 것"도 별도 blocker로 드러낸다.
```

## 갱신된 운영 산출물

테스트 중 CLI writer가 다음 파일을 새 schema로 갱신했다.

```text
docs/operational/research_to_runtime_parity_matrix_2026-07-05.json
docs/operational/all_archetype_runtime_status_matrix_2026-07-05.json
docs/operational/all_archetype_runtime_status_matrix_2026-07-05.md
docs/operational/all_archetype_runtime_status_matrix.json
docs/operational/all_archetype_runtime_parity_matrix.json
docs/operational/all_archetype_runtime_parity_summary.md
docs/operational/research_to_runtime_acceptance_report.md
```

현재 값:

```text
registry_contract_count = 36
canonical_c_archetype_count = 32
cross_archetype_contract_count = 4
registry_scope_counts = {"C_CANONICAL_ARCHETYPE": 32, "R13_CROSS_ARCHETYPE": 4}
all_registered_archetypes_have_exactly_one_runtime_status_row = true
missing_parity_source_row_count = 0
duplicate_parity_source_row_count = 0
extra_parity_source_row_count = 0
meaningful_runtime_parity_ready = false
```

중요:

```text
exact row coverage = true
```

는 Goal4 완료가 아니다.

의미는:

```text
현재 registry 전체에 대해 상태판 행은 빠짐없이 있다.
```

아직 의미 있는 완료가 아닌 이유:

```text
meaningful_runtime_parity_ready = false
SCORE_PATH_CLOSED_WITH_THESIS_GAPS = 4
SOURCE_REPAIR_REQUIRED = 28
TARGET_MATERIALIZATION_REQUIRED = 3
PLANNING_ONLY = 1
```

즉 "출석부와 결과표 행 수는 맞췄지만, 대부분 과목은 아직 실제 합격 답안지가 아니다."

## 테스트 변경

강화한 테스트:

```text
tests/test_research_to_runtime_parity_goal4.py
tests/test_all_archetype_runtime_status_matrix.py
tests/test_all_archetype_runtime_parity_matrix.py
tests/test_all_archetype_next_attempt_plan.py
```

핵심 추가 검증:

```text
1. config registry의 archetype_id 목록과 matrix row 목록이 정확히 일치한다.
2. 테스트가 36이라는 숫자에만 기대지 않는다.
3. missing_parity_source_row_count / duplicate / extra가 0이어야 한다.
4. 일부 parity row가 빠져도 registry 기준 row가 남고 RUNTIME_PARITY_SOURCE_ROW_MISSING blocker가 생긴다.
5. next attempt plan row count도 고정 36이 아니라 unproven row 수를 기준으로 본다.
```

추가한 회귀 테스트 예:

```text
test_registry_source_of_truth_keeps_missing_parity_row_visible
```

이 테스트는 C08 parity row를 일부러 제거한 audit을 넣는다.

기대 결과:

```text
C08 row는 matrix에 계속 존재
parity_source_row_present = false
primary_blocker_class = RUNTIME_PARITY_SOURCE_ROW_MISSING
```

즉 "C08이 없으니 조용히 사라짐"을 금지한다.

## 실행한 검증

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_to_runtime_parity_goal4 \
  tests.test_all_archetype_runtime_status_matrix \
  tests.test_all_archetype_runtime_parity_matrix \
  tests.test_all_archetype_next_attempt_plan -v
```

결과:

```text
Ran 27 tests in 21.077s
OK
```

추가로 Goal4 acceptance 주변 테스트까지 넓혀 실행했다.

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_to_runtime_parity_goal4 \
  tests.test_all_archetype_runtime_status_matrix \
  tests.test_all_archetype_runtime_parity_matrix \
  tests.test_all_archetype_next_attempt_plan \
  tests.test_all_archetype_runtime_execution_manifest \
  tests.test_meaningful_full_thesis_production_acceptance \
  tests.test_full_thesis_evidence_completion_split \
  tests.test_full_thesis_no_c05_monoculture \
  tests.test_required_positive_missing_blocks_meaningful_pass -v
```

결과:

```text
Ran 37 tests in 20.978s
OK
```

`git diff --check`도 통과했다.

전체 테스트도 실행했다.

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5278 tests in 439.745s
OK
```

테스트 중 `parity_cli_main`은 현재 goal 상태를 그대로 실패 코드로 반환했다.

```text
final_status = MEANINGFUL_RUNTIME_PARITY_NOT_READY
meaningful_acceptance_status = MEANINGFUL_FULL_THESIS_EVIDENCE_PASS_FALSE
failed_on = REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS
```

이건 정상이다. 이번 패치는 완료 선언이 아니라 미완료 상태를 더 정확히 증명하는 패치다.

## 현재 Goal4 상태

이번 패치 후에도 Goal4는 아직 완료가 아니다.

## 추가 패치: next-attempt task 성공조건 고정

registry 기준 상태판은 각 아키타입이 어디서 막혔는지 보여준다. 하지만 그 상태판을 다음 실행 입력으로 바꾸는 `all_archetype_next_runtime_attempt_plan`에는 아직 한 가지 구멍이 있었다.

```text
기존 next source task:
  primitive_gap = named_customer_quality
  LLM query required = true
  score before execution = false

부족했던 점:
  어떤 claim이 들어와야 이 task가 성공인지,
  못 찾으면 어떤 상태로 남겨야 하는지가 task 자체에 없었다.
```

쉬운 예:

```text
의사가 "C08 고객 품질을 다시 검사"라고 써 놓았지만,
검사 통과 기준이 없으면 다음 사람이 또 DART 표지나 회사 개요를 가져와서
"조사했다"고 말할 수 있다.

이번 패치는 처방전에 "직접 대상 회사, 현재 유효, 검증 anchor, primitive mapping ACCEPTED"
까지 적어 둔 것이다.
```

변경된 전수 source task 필드:

```json
{
  "success_condition": "Create at least one accepted Evidence OS claim ...",
  "expected_claim_schema": {
    "target_scope_status": "DIRECT",
    "temporal_status": "CURRENT_OR_AS_OF_VALID",
    "anchor_status": "VERIFIED_SOURCE_ANCHOR",
    "mapping_status": "ACCEPTED",
    "required_claim_status": "ACCEPTED_FOR_SCORE",
    "score_forbidden_until_claim_accepted": true
  },
  "fallback_if_not_found": "PENDING_SOURCE|PENDING_MATERIAL_GAP|SOURCE_REPAIR_REQUIRED|TARGET_MATERIALIZATION_REQUIRED"
}
```

전수 산출물 현재 값:

```text
plan_row_count = 36
source_task_count = 111
seed_event_count = 111
all_tasks_have_success_condition = true
all_tasks_have_expected_claim_schema = true
all_tasks_have_fallback_if_not_found = true
```

샘플:

```text
C08 named_customer_quality:
  success = 058470에 대한 직접 대상 회사 accepted Evidence OS claim 필요
  fallback = SOURCE_REPAIR_REQUIRED

C24 approval_not_confirmed:
  success = 000100에 대한 직접 대상 회사 accepted Evidence OS claim 필요
  fallback = SOURCE_REPAIR_REQUIRED

R13 contract_cancelled_or_delayed:
  success = 실제 current target symbol을 먼저 materialize한 뒤 직접 대상 회사 accepted claim 필요
  fallback = TARGET_MATERIALIZATION_REQUIRED
```

중요한 점:

```text
이번 패치는 검색어를 하드코딩하지 않는다.
LLM이 query를 만들되, 그 query 결과가 운영 점수에 들어가기 위한 claim 합격 기준을 고정한다.
```

즉 다음 실행에서 generic disclosure, source proxy, snippet, evidence_url_pending이 다시 들어와도 source task 성공으로 인정되지 않는다.

현재 증명된 것:

```text
1. registry 기준 전체 아키타입 row는 빠짐없이 존재한다.
2. C06/C08/C15/C17/C24/C28만 보는 축소 테스트는 아니다.
3. C01~C32 + R13 4개 전체의 attempt/source route/accepted claim/full thesis 상태축이 matrix에 있다.
4. missing parity source row가 생기면 숨기지 않고 별도 blocker로 표시한다.
```

아직 미완료인 것:

```text
1. SOURCE_REPAIR_REQUIRED 28개를 accepted claim/full thesis로 더 닫아야 한다.
2. SCORE_PATH_CLOSED_WITH_THESIS_GAPS 4개는 required-positive/Green gap을 닫아야 한다.
3. TARGET_MATERIALIZATION_REQUIRED 3개는 실제 target symbol materialization이 필요하다.
4. PLANNING_ONLY 1개는 source task 실행까지 이어져야 한다.
5. meaningful_runtime_parity_ready는 여전히 false다.
```

다음 작업 방향:

```text
전수 matrix가 보여주는 primary blocker 순서대로,
ACCEPTED_CLAIM_NOT_CREATED / REQUIRED_POSITIVE_MISSING / CANDIDATE_SELECTOR_DID_NOT_ATTEMPT / SOURCE_TASK_NOT_CREATED
를 실제 source route와 claim extraction 단계에서 줄여야 한다.
```

## 추가 패치: next-runtime planner batch isolation

위 next-attempt plan을 실제 Census v4 Research Brain 입력으로 넣어 보니, 실행 장부에 또 하나의 감사 문제가 보였다.

관찰:

```text
실행 대상:
  all_archetype_next_runtime_seed_events_2026-07-05.jsonl

seed_event_count:
  111

기존 manifest:
  brain_planner_batch_size = 5

runtime_progress:
  planner_batch_start에서 오래 머무름

planner_runs:
  0 rows
```

쉬운 예:

```text
5명을 한꺼번에 면접장에 넣었다.
면접장이 오래 멈추면 밖에서는 "첫 면접 묶음 시작"까지만 보인다.
실제로는 안에서 5명을 다시 한 명씩 재면접하고 있을 수도 있지만,
장부에는 어느 후보가 실패했는지 아직 남지 않는다.
```

코드상 `run_planner_provider_v4`는 batch timeout이 나면 후보별 단일 재시도를 한다. 이 보호장치 자체는 맞다. 문제는 그 내부 재시도 동안 `brain_web_runtime_progress.json`은 계속 같은 `planner_batch_start`로 보인다는 점이다.

따라서 Goal4 next-runtime manifest는 throughput보다 감사성을 우선해야 한다.

변경:

```text
src/e2r/census/all_archetype_runtime_execution_manifest.py

GOAL4_NEXT_RUNTIME_PLANNER_BATCH_SIZE = 1
brain_planner_batch_size = 1
safety_assertions.planner_batch_isolation_required = true
safety_assertions.planner_batch_size = 1
```

변경된 실행 명령:

```text
--brain-planner-batch-size 1
```

의미:

```text
이제 특정 후보에서 provider timeout이 나면
그 후보 단위의 provider failure / planner row로 남고,
다음 후보로 넘어갈 수 있다.
```

이건 검색어 하드코딩도 아니고, gate 완화도 아니다.

```text
점수/Stage/weight 변경 없음
accepted claim 기준 변경 없음
source task 성공조건 변경 없음
실행 감사 단위를 batch에서 후보 단위로 좁힘
```

쉬운 예:

```text
기존:
  "5명 묶음이 아직 면접 중"으로만 보임

변경:
  "1번 후보 timeout, 2번 후보 진행, 3번 후보 provider failure"처럼
  Goal4 matrix에 넣을 수 있는 실패 장부가 생김
```

재생성된 manifest:

```text
docs/operational/all_archetype_runtime_execution_manifest_2026-07-05.json
docs/operational/all_archetype_runtime_execution_manifest_2026-07-05.md
docs/operational/all_archetype_runtime_execution_manifest.json
```

parity CLI 재실행 결과:

```text
final_status = MEANINGFUL_RUNTIME_PARITY_NOT_READY
failed_on = REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS

blockers:
  GREEN_GAP_ON_PROMOTED_ROWS
  MANDATORY_ARCHETYPE_FULL_THESIS_ROW_MISSING
  REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS
```

즉 이번 패치 후에도 Goal4는 완료가 아니다. 다만 다음 실제 full runtime attempt가 멈춘 것처럼 보이는 batch 내부 대기를 줄이고, 후보별 provider/source blocker를 더 정직하게 남길 수 있게 됐다.

## 추가 런타임 감사: batch=1, finite budget=14400

이 섹션은 `--brain-planner-batch-size 1`로 후보별 감사성을 확보한 뒤 실제 full runtime을 다시 돌린 결과다.

이번 실행도 Goal4 완료가 아니다. 다만 이전처럼 `INVALID_PARTIAL_OUTPUT`으로 폐기되는 결과가 아니라, critical audit은 깨끗하고 남은 blocker가 명확한 `NOT_READY` 결과다.

쉬운 예:

```text
이전 7200초 실행:
  시험 도중 답안지 한 장에 "평가 이벤트만 있는데 점수 있음" 같은 형식 오류가 생김
  → 그 결과 전체가 무효 처리됨

이번 14400초 실행:
  형식 오류는 사라짐
  실제 채점도 일부 됨
  하지만 111개 중 대부분이 아직 증거 claim/full thesis로 닫히지 않음
  → "불합격 사유가 분명한 NOT_READY"
```

### 7200초 실행에서 폐기된 이유

output root:

```text
output/census_v4/2026-07-06-goal4-next-runtime-full-attempt-batch1
```

결과:

```text
exit_code = 1
status = INVALID_PARTIAL_OUTPUT
leaf critical_count = 2
```

원인:

```text
assessment_only_nonzero_score_count = 1
assessment_event_used_as_score_evidence_count = 1
```

실제 문제는 Research Brain이 만든 candidate event가 stage row로 승격될 때 `candidate_event_id`가 빠진 것이다.

```text
064760 티씨케이:
  Brain/Web accepted claim과 partial score는 있었음
  그런데 stage row에는 candidate_event_count=0으로 남음
  그래서 감사기가 "CensusAssessmentEvent만 있는데 점수가 붙었다"고 판단
```

쉬운 예:

```text
실제 서류는 있었는데 서류번호가 최종 답안지에 안 적힘
→ 감사 입장에서는 "서류 없이 점수 준 것"처럼 보임
```

패치:

```text
src/e2r/census/census_runner_v4.py
```

`_promote_brain_stage_rows`가 StageCourt trace의 `candidate_event_id`를 최종 row에 보존하도록 바꿨다.

중요한 점:

```text
점수/Stage/weight는 바꾸지 않았다.
CensusAssessmentEvent를 점수 증거로 허용한 것도 아니다.
Research Brain candidate event를 잃어버리지 않게 장부를 맞춘 패치다.
```

테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_all_archetype_runtime_execution_manifest -v
```

결과:

```text
Ran 32 tests
OK
```

### finite budget 상향

batch size를 1로 줄인 뒤 111개 seed를 전수 시도하면 planner/source/claim extraction이 모두 후보별로 직렬화된다.

기존:

```text
brain_runtime_budget_seconds = 7200
```

변경:

```text
GOAL4_NEXT_RUNTIME_BUDGET_SECONDS = 14400
brain_runtime_budget_seconds = 14400
```

주의:

```text
이건 무제한 설정이 아니다.
Goal4 next-runtime manifest에만 들어간 finite budget이다.
Production daily의 unbounded fetch를 허용하는 변경도 아니다.
```

쉬운 예:

```text
한 명씩 111명을 면접하면 2시간으로는 부족했다.
그래서 4시간짜리 회의실을 예약했다.
면접 기준을 낮춘 것이 아니라 시간을 정확히 배정한 것이다.
```

갱신된 manifest:

```text
docs/operational/all_archetype_runtime_execution_manifest.json
docs/operational/all_archetype_runtime_execution_manifest_2026-07-05.json
docs/operational/all_archetype_runtime_execution_manifest_2026-07-05.md
```

### 14400초 실행 결과

output root:

```text
output/census_v4/2026-07-06-goal4-next-runtime-full-attempt-batch1-budget14400
```

명령 핵심:

```text
--brain-planner-batch-size 1
--brain-runtime-budget-seconds 14400.0
--brain-universe-limit 111
--brain-planner-success-limit 111
--brain-accepted-claim-target 36
--brain-stage-promotion-mode strict
--full-thesis-smoke-mode disabled
--target-gate full_thesis
```

결과:

```text
exit_code = 1
final verdict = NOT_READY
runtime_budget_exhausted = false
runtime_elapsed_seconds = 13357.865408
```

핵심 수치:

```text
planner_run_count = 458
full_thesis_seed_planner_attempted_event_count = 111
full_thesis_seed_real_provider_success_count = 110
full_thesis_seed_runtime_budget_exhausted_count = 0
full_thesis_seed_source_task_execution_count = 809
source_task_execution_count = 809
accepted_claim_count = 135
unique_accepted_claim_count = 86
real_document_fetched_count = 729
unique_real_document_fetched_count = 142
```

Leaf artifact audit:

```text
verdict = PASS
critical_count = 0
assessment_event_score_evidence_allowed_count = 0
assessment_event_used_as_score_evidence_count = 0
assessment_only_nonzero_score_count = 0
```

의미:

```text
CensusAssessmentEvent를 점수 증거로 잘못 쓴 문제는 이번 run에서는 재발하지 않았다.
```

### 111개 seed materialization 상태

`full_thesis_seed_materialization_audit.json`:

```text
verdict = FAIL
critical_count = 48
```

하지만 실패 원인이 무작위가 아니라 다음처럼 분리됐다.

```text
FULL_THESIS_PROMOTED = 7
STAGECOURT_READY_NOT_PROMOTED = 16
ACCEPTED_CLAIM_NOT_CREATED = 83
STAGECOURT_TRACE_NOT_CREATED = 4
PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS = 1
```

아키타입별 promoted:

```text
C01_ORDER_BACKLOG_MARGIN_BRIDGE = 1
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG = 1
C05_EPC_MEGA_CONTRACT_MARGIN_GAP = 1
C06_HBM_MEMORY_CUSTOMER_CAPACITY = 1
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY = 1
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD = 1
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION = 1
```

중요:

```text
예전 문제처럼 C05 10개가 전부 FULL_THESIS로 올라간 상태는 아니다.
이번에는 promoted 7개가 여러 아키타입으로 분산됐다.
```

하지만 이것도 완료가 아니다.

```text
83개는 accepted claim 자체가 생성되지 않았다.
16개는 StageCourt까지 갔지만 FULL_THESIS로 승격되지 않았다.
4개는 StageCourt trace도 만들지 못했다.
1개는 real provider success가 없었다.
```

쉬운 예:

```text
111개 과제 중 7개만 답안지 형태로 채점됐다.
나머지는 "자료 못 찾음", "채점 준비는 됐지만 승격 실패", "채점표 생성 실패"로 남아 있다.
```

### FULL_THESIS stage rows

최종 FULL_THESIS row 7개:

```text
052400 코나아이        C01 gap=contract_quality             score=11.9999 stage=0
047810 한국항공우주    C03 gap=export_contract              score=37.0000 stage=0
003380 하림지주        C05 gap=contract_duration_months     score=27.9998 stage=0
005930 삼성전자        C06 gap=revenue_visibility_contract  score=44.1667 stage=1
058470 리노공업        C08 gap=named_customer_quality       score=65.2000 stage=2
011170 롯데케미칼      C17 gap=raw_material_cost_risk       score=18.7500 stage=0
012510 더존비즈온      C28 gap=retention_or_renewal         score=13.2666 stage=0
```

공통:

```text
score_scale = FULL_E2R_100
score_source = BRAIN_WEB_PRODUCTION_FULL_THESIS_STAGECOURT
```

삼성전자/하이닉스 기준:

```text
삼성전자 005930:
  이번 run에서는 production FULL_THESIS row로 올라왔지만 stage=1, score=44.1667이다.
  예전 90점대 provisional smoke와 비교할 수 없다.
  이번 점수는 source-backed full thesis 경로의 별도 실행 결과다.

SK하이닉스 000660:
  refresh queue에는 남아 있지만 production FULL_THESIS row로는 올라오지 않았다.
  refresh_queue_unmaterialized_sample에 full_thesis_refresh_task_not_run으로 남았다.
```

쉬운 예:

```text
삼성전자는 이번 시험지에 들어와 채점은 받았다.
하이닉스는 이번 시험지 후보 명단에는 있었지만, 최종 채점 답안지로 올라오지 못했다.
```

### Production pass가 막힌 이유

`full_thesis_production_audit.json`:

```text
status = PENDING_FULL_THESIS_PRODUCTION
production_pass_allowed = false
full_thesis_row_count = 7
full_thesis_refresh_queue_candidate_count = 82
production_full_thesis_row_with_required_positive_missing_primitives_count = 7
production_full_thesis_row_with_green_gap_primitives_count = 7
blockers = ["production_full_thesis_rows_with_required_positive_missing_primitives"]
```

의미:

```text
7개 row는 score path가 열렸지만,
7개 모두 required-positive 또는 Green gap이 남아 있어 meaningful production pass가 아니다.
```

쉬운 예:

```text
답안지를 7장 채점하긴 했다.
하지만 7장 모두 필수 증빙 서류가 빠져 있어 "최종 합격" 도장을 찍지 못한다.
```

### Brain/Web readiness gate blockers

`brain_web_readiness_gate_audit.json`:

```text
verdict = BLOCKED
blockers:
  - Brain/Web official-first violations reached score evidence: 5
  - Brain/Web source task budget caps were exceeded: 8
```

세부:

```text
official_first_violation_count = 5
source_task_budget_cap_exceeded_count = 8
zero_budget_policy_rejected_source_task_execution_count = 33
```

예시:

```text
055550 C21 roe:
  source_class=BrokerReportPublicPDF
  status=NO_EVIDENCE_FOUND

003380 C05 margin_bridge_visible:
  source_class=BrokerReportPublicPDF
  status=PROVIDER_FAILED

003670 C11 call_off_risk:
  source_class=BrokerReportPublicPDF
  status=EVIDENCE_OS_ACCEPTED
  stop_reason=rerouted_claim_accepted_original_gap_unsatisfied
```

의미:

```text
official-first로 먼저 풀어야 하는 gap이 일반 broker/report/web 경로에서 score evidence까지 닿은 사례가 있다.
또 일부 SourceTask는 budget cap을 초과했다.
```

쉬운 예:

```text
재무제표로 확인해야 할 항목을 먼저 DART/공식자료에서 닫지 않고,
증권사 PDF나 웹 경로로 점수 재료까지 보낸 셈이다.
그래서 Brain/Web gate가 막는 것이 맞다.
```

### 아직 남은 구조적 문제

1. 최종 `census_stage_status.jsonl`의 FULL_THESIS row에는 `canonical_archetype_id`가 비어 있고, 아키타입은 materialization trace/StageCourt trace 쪽에 남아 있다.

쉬운 예:

```text
채점표에는 "삼성전자 44.1667점"이 있는데,
그 점수가 C06 시험지 점수라는 라벨이 최종 row에 직접 적혀 있지 않은 상태다.
감사할 때 trace를 따라가면 알 수 있지만, 최종 row 자체도 라벨을 가져야 한다.
```

2. `ACCEPTED_CLAIM_NOT_CREATED` 83개가 대부분이다.

쉬운 예:

```text
LLM/planner/source task는 돌았지만,
점수에 쓸 수 있는 accepted Evidence OS claim으로 변환되지 않았다.
```

3. `STAGECOURT_READY_NOT_PROMOTED` 16개는 StageCourt trace까지 갔지만 production FULL_THESIS로 못 올라왔다.

쉬운 예:

```text
채점 준비는 됐는데,
필수 서류나 gap 조건이 남아 있어 최종 성적표에 반영되지 않았다.
```

4. official-first 위반과 source task budget cap 초과가 남아 있다.

쉬운 예:

```text
공식 문서로 먼저 확인해야 하는 gap을 웹/리포트로 우회하거나,
정해진 source task 예산을 넘겨서 찾은 claim은 운영 evidence pass로 인정하면 안 된다.
```

## 현재 결론

이번 작업으로 고쳐진 것:

```text
1. batch=1 실행에서 Research Brain candidate_event_id가 최종 row에 보존된다.
2. CensusAssessmentEvent만으로 점수가 붙은 것처럼 보이는 critical 오류가 사라졌다.
3. Goal4 next-runtime manifest는 후보별 감사성과 14400초 finite budget을 명시한다.
4. 실제 full runtime은 111개 seed를 모두 planner attempt했고, 809개 source task와 135 accepted claims까지 진행됐다.
5. C05-only monoculture는 최신 promoted FULL_THESIS 7개 기준으로는 재발하지 않았다.
```

아직 완료가 아닌 것:

```text
1. Goal4 final verdict는 NOT_READY다.
2. full thesis seed materialization audit은 FAIL이다.
3. Brain/Web readiness gate는 BLOCKED다.
4. production full thesis pass는 false다.
5. 7개 FULL_THESIS row 모두 required-positive/Green gap이 남아 있다.
6. 82개 refresh queue 후보가 아직 FULL_THESIS로 materialize되지 않았다.
7. machine-readable test result artifact도 아직 Goal4 requirement matrix blocker로 남아 있다.
```

따라서 이 문서의 최종 판단은 다음이다.

```text
Goal4는 계속 active다.
이번 실행은 "전보다 정직한 NOT_READY"를 만든 것이지,
운영 파이프라인 완료나 전 아키타입 meaningful full thesis pass가 아니다.
```
