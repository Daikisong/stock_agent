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
