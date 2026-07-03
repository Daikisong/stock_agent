# Census v4 0701 v83 Full Thesis Source Linkage / Score Interval Guard Patch

작성일: 2026-07-03

대상 패치:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_brain_stage_promotion_gate.py
```

## 0. 결론

v82 감사에서 확인한 두 개의 FULL_THESIS 승급 구멍을 막았다.

```text
1. live source task가 "어딘가에 하나" 있으면 통과하던 약한 조건
   -> 각 accepted claim이 같은 source task의 accepted_claim_ids와 fetched_document_ids에 직접 연결되어야 통과

2. score_interval.lower만 확인하던 약한 조건
   -> lower와 upper가 모두 있어야 하고, upper >= lower여야 통과
```

쉬운 예:

```text
나쁜 상태:
  A 문서를 fetch했다.
  그런데 점수는 B 문서 claim으로 줬다.
  예전 gate는 "fetch 문서가 하나 있네" 하고 통과할 수 있었다.

패치 후:
  점수 claim B가 나온 document_id가 실제 source task의 fetched_document_ids에 있어야 한다.
  아니면 FULL_THESIS 승급 차단.
```

## 1. 왜 이 패치가 필요한가

v82 문서:

```text
docs/0701/census_v4_0701_v82_operational_stage_existence_deep_audit_and_next_patch_direction_2026-07-03.md
```

에서 교차검증이 다음 약점을 지적했다.

```text
production runner의 live source check가 후보 claim에 직접 묶여 있지 않다.
현재는 brain origin source execution 중 fetched_document_ids가 하나라도 있나를 본다.
후보 accepted claim과 같은 source task/document인지까지 직접 검증하지 않는다.
```

이건 운영 Stage에서 치명적이다.

예:

```text
삼성전자 리포트 A를 fetch했다.
월덱스 기사 B에서 추출된 claim이 삼성전자 점수에 들어갔다.
단순히 "fetch 문서가 있음"만 보면 이런 오귀속을 못 막는다.
```

이번 패치는 FULL_THESIS 승급 직전에 다음 사슬을 요구한다.

```text
accepted_claim_id
  -> accepted_claim.document_id / anchor_id
  -> source_task_execution.accepted_claim_ids contains accepted_claim_id
  -> source_task_execution.fetched_document_ids contains accepted_claim.document_id
  -> same candidate_event_id if both sides carry one
  -> source_origin is research_brain_v4_attempt
```

## 2. 코드 변경

### 2.1 claim-document-source task linkage helper 추가

새 helper:

```text
_production_full_thesis_source_linkage(...)
```

역할:

```text
각 FULL_THESIS 후보 accepted claim마다
  claim row 존재
  document_id 존재
  같은 source task가 accepted_claim_ids에 해당 claim을 포함
  같은 source task가 fetched_document_ids에 해당 document를 포함
  candidate_event_id가 있으면 동일 이벤트
를 확인한다.
```

실패 blocker:

```text
claim_not_linked_to_live_source_task_document
missing_live_source_task_document_execution
```

승급 row에는 다음 proof를 남긴다.

```text
full_thesis_source_linkage_proof
full_thesis_source_task_ids
```

이제 단순히 source task가 하나 있었다는 사실로는 FULL_THESIS가 되지 않는다.

### 2.2 score interval upper gate 추가

기존:

```text
score_interval.lower 없으면 blocker
score_interval.upper는 읽지만 blocker로 강제하지 않음
```

변경:

```text
missing_verified_score_interval_lower
missing_verified_score_interval_upper
invalid_score_interval_bounds
```

즉 `lower=84, upper=null`은 확정 점수가 아니다.

쉬운 예:

```text
점수 범위가 84~? 이면 경계가 열린 상태다.
운영 FULL_E2R_100 점수로 쓰면 안 된다.
```

## 3. 추가 테스트

`tests/test_census_v4_brain_stage_promotion_gate.py`에 추가:

```text
test_full_thesis_blocks_claim_not_linked_to_same_live_source_document
test_full_thesis_blocks_missing_score_interval_upper
```

기존 성공 테스트도 강화:

```text
test_full_green_gate_brain_stage_can_be_promoted_to_production_full_thesis
  -> full_thesis_source_task_ids == TASK-1..TASK-4
  -> full_thesis_source_linkage_proof all linked
```

## 4. 검증 결과

단위 테스트:

```bash
PYTHONPATH=src python -m unittest tests.test_census_v4_brain_stage_promotion_gate -v
```

결과:

```text
Ran 16 tests in 4.205s
OK
```

관련 full-thesis / brain-web / goal audit 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_goal_required_audits \
  -v
```

결과:

```text
Ran 33 tests in 38.067s
OK
```

## 5. 이번 패치가 해결하지 않은 것

이 패치는 FULL_THESIS 거짓 승급 방지 패치다. 운영 full thesis를 실제로 생성하는 패치가 아니다.

여전히 v82 기준 남은 blocker:

```text
FULL_THESIS row = 0
FULL_E2R_100 row = 0
삼성전자 full thesis source task 미실행
SK하이닉스 C06 Green/full-thesis primitive coverage 부족
Brain/Web operational minimum 미달
all-archetype source-backed replay 6/32, missing 26
```

즉 좋아진 것은:

```text
틀린 FULL_THESIS가 나오기 어려워졌다.
```

아직 안 된 것은:

```text
진짜 FULL_THESIS를 production mode에서 만들기.
```

다음 패치 방향은 그대로다.

```text
FULL_THESIS_REFRESH_TASK_PLANNED
  -> SOURCE_TASK_EXECUTED
  -> ACCEPTED_CLAIM
  -> PRIMITIVE_STATE
  -> SCORE_CONTRIBUTION
  -> STAGECOURT_TRACE
  -> FULL_THESIS row
```

이 사슬을 진짜 원문 기반으로 닫아야 한다.

