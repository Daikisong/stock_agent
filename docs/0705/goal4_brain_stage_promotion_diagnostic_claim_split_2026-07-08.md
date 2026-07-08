# Goal4 Brain Stage Promotion Diagnostic Claim Split - 2026-07-08

작성 시점: 2026-07-08 KST

이번 패치는 Goal4 0705 bounded runtime output이 `INVALID_PARTIAL_OUTPUT`으로 떨어진 직접 원인 하나를 수리한다.

결론:

```text
대표 Stage row가 실제로 쓴 claim과,
ledger에 diagnostic/planner feedback으로 남아 있는 accepted claim을 분리했다.

대표 row의 claim이 score-eligible이면,
대표 row 밖의 rerouted/diagnostic score-ineligible claim 때문에
unsafe promotion으로 오판하지 않는다.
```

쉬운 예:

```text
시험 답안지에 1개 문항이 채점됐다.
그 문항의 근거는 정상이다.

옆 연습장에는 "다음에 더 찾아볼 후보 문장" 76개가 남아 있다.
이 연습장 문장은 점수에 쓰면 안 되지만,
답안지 문항이 정상이라면 "답안지 오염"은 아니다.
```

## 기존 문제

이전 0705 output root:

```text
output/census_v4/2026-07-05-research-to-runtime-parity-self-repair-01-20260708T082837Z
```

old audit:

```text
brain_claim_count = 87
brain_claim_score_ineligible_count = 76
brain_promoted_stage_row_count = 1
unsafe_promoted_stage_row_count = 1
verdict = FAIL_UNSAFE_PROMOTION
```

하지만 실제 promoted FULL_THESIS row는:

```text
symbol = 011170
company = 롯데케미칼
stage_scope = FULL_THESIS
claim_id = CLM-3b5ec525951042243c82
claim score_eligible = true
eligibility_reasons = []
satisfaction_type = DIRECT_ACCEPTED_CLAIM
primitive = spread_expansion
```

즉 대표 row 자체는 score-eligible claim을 썼다.

문제는 audit이 아래를 섞었다는 점이다.

```text
대표 row가 쓴 score evidence claim
!=
run 전체 accepted ledger에 남은 diagnostic/rerouted accepted claim
```

기존 계산은 사실상:

```text
run 전체에 score-ineligible accepted claim이 76개 있음
AND promoted row가 1개 있음
=> unsafe_promoted_stage_row_count = 1
```

이었다.

이건 너무 거칠다. score-ineligible accepted claim이 대표 row에 들어가지 않았고, non-representative audit에서 score leak도 없으면, 그것은 unsafe promotion이 아니라 diagnostic gap이다.

## 코드 패치

수정 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_brain_stage_promotion_gate.py
```

변경 1:

```text
_promote_brain_stage_rows()
```

대표 Stage row로 올릴 때, StageCourt trace의 claim 중 `score_eligible=True`인 claim만 대표 accepted claim으로 사용한다.

변경 전:

```text
trace_claim_ids
-> web_llm / official claim이면 대표 Stage accepted_claim_ids에 들어갈 수 있음
```

변경 후:

```text
trace_claim_ids
-> accepted_claim.score_eligible is True
-> web_llm / official lane 확인
-> 대표 Stage accepted_claim_ids
```

따라서 trace가 score-ineligible claim만 갖고 있으면 대표 Stage row로 승격되지 않는다.

변경 2:

```text
_brain_stage_promotion_audit()
```

아래 두 집합을 분리한다.

```text
promoted_brain_claims
  대표 Stage row가 실제로 쓴 claim

diagnostic_brain_claims
  run ledger에는 남아 있지만 대표 row 점수에 쓰이지 않은 claim
```

새 audit 필드:

```text
promoted_brain_claim_count
promoted_brain_claim_score_ineligible_count
diagnostic_brain_claim_score_ineligible_count
promoted_brain_claim_missing_verifiable_anchor_count
promoted_brain_claim_unresolved_document_ref_count
promoted_brain_claim_unresolved_anchor_ref_count
promoted_brain_claim_missing_date_count
promoted_brain_claim_not_direct_target_count
promoted_brain_claim_not_current_count
```

대표 row blocker는 `promoted_brain_claim_*` 기준으로만 건다.

## 실제 0705 output 재감사

원본 output은 건드리지 않고 임시 복사본에서 현재 코드로 재감사했다.

결과:

```text
brain_verdict = PROMOTION_APPLIED
unsafe_promoted_stage_row_count = 0
promoted_brain_claim_score_ineligible_count = 0
diagnostic_brain_claim_score_ineligible_count = 76
leaf critical_count = 0
```

즉 이번 패치는 `INVALID_PARTIAL_OUTPUT`의 직접 원인이던 unsafe promotion false positive를 제거한다.

중요한 제한:

```text
brain_web_readiness_gate verdict = BLOCKED
brain_web_readiness_gate blocker_count = 2
```

따라서 이것은 Goal4 완료가 아니다.

## 왜 readiness는 아직 blocked인가

diagnostic score-ineligible claim 76개는 대표 row 오염은 아니지만, 운영적으로는 여전히 중요한 신호다.

의미:

```text
대표 row 하나는 깨끗하게 승격 가능하다.
하지만 run 전체 Brain/Web evidence pass는 아직 아니다.
rerouted/diagnostic claim이 많다는 것은 source route와 primitive closure가 아직 약하다는 뜻이다.
```

쉬운 예:

```text
한 문제는 정답 처리할 수 있다.
하지만 시험 전체가 완성된 것은 아니다.
틀린 풀이 메모가 76개나 남아 있으면 다음 시험 준비에는 반드시 반영해야 한다.
```

## 회귀 테스트

추가 테스트:

```text
test_nonrepresentative_score_ineligible_claim_does_not_make_clean_promotion_unsafe
test_score_ineligible_trace_claim_is_not_promoted_as_representative_stage
```

검증 내용:

```text
1. 대표 row 밖 diagnostic score-ineligible claim은 unsafe promotion으로 계산하지 않는다.
2. 대표 trace 자체가 score-ineligible claim만 갖고 있으면 Stage row로 승격하지 않는다.
3. 기존 brain_web_readiness_gate는 score-ineligible claim을 여전히 blocker로 본다.
```

실행:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_stage_promotion_gate.CensusV4BrainStagePromotionGateTests.test_nonrepresentative_score_ineligible_claim_does_not_make_clean_promotion_unsafe \
  tests.test_census_v4_brain_stage_promotion_gate.CensusV4BrainStagePromotionGateTests.test_score_ineligible_trace_claim_is_not_promoted_as_representative_stage \
  tests.test_census_v4_brain_stage_promotion_gate.CensusV4BrainStagePromotionGateTests.test_strict_live_connected_promoted_brain_row_is_promotion_applied \
  tests.test_census_v4_brain_web_readiness_gate.CensusV4BrainWebReadinessGateTests.test_brain_claim_score_ineligible_is_blocked -v
```

결과:

```text
Ran 4 tests
OK
```

추가 전체 회귀:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5305 tests in 505.465s
OK
```

## Goal4 현재 상태

이번 패치로 전진한 것:

```text
partial invalid의 직접 원인 하나 제거
representative score evidence와 diagnostic accepted claim 분리
score-ineligible trace claim의 대표 승격 차단
실제 0705 output 임시 재감사에서 leaf critical_count=0 확인
```

아직 남은 것:

```text
Goal4 meaningful runtime parity는 아직 NOT_READY
Brain/Web readiness gate blocker 2개 남음
C01~C36 전수 matrix는 상태판으로 존재하지만 모든 runtime parity가 증명된 것은 아님
diagnostic score-ineligible claim 76개는 다음 source-route/primitive closure 수리 입력으로 남음
```

따라서 다음 단계는:

```text
1. patched code로 bounded runtime을 다시 돌려 clean output root를 만든다.
2. partial_run_invalid 없이 all-archetype runtime status/parity matrix를 재생성한다.
3. brain_web_readiness_gate blocker 2개를 source route/claim closure 관점에서 줄인다.
4. MEANINGFUL_FULL_THESIS_EVIDENCE_PASS 또는 명확한 EXTERNAL_SOURCE_BLOCKER_NOT_READY 전까지 Goal4 완료 금지.
```
