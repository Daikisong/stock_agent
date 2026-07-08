# Goal4 Rerouted Claim Score Path Patch Audit

작성일: 2026-07-08
대상 실행: `output/census_v4/2026-07-05-goal4-all-archetype-next-runtime-attempt-e0e9399`
관련 목표: `docs/core/goal4.md`

## 결론

이번 패치는 Goal4 완료가 아니다.

이번에 줄인 blocker는 하나다.

```text
Brain/Web official-first violation reached score evidence
```

이 blocker의 실제 원인은 `official-first` 자체보다 더 근본적인 score-path 오류였다. source task가 요청한 primitive를 직접 만족하지 못한 `REROUTED_ACCEPTED_CLAIM`이 accepted claim으로 보존된 뒤, score contribution과 StageCourt export까지 들어갔다.

패치 후 원칙은 다음이다.

```text
direct accepted claim
→ 점수 후보 가능

rerouted accepted claim
→ planner feedback / follow-up seed 가능
→ 현재 source task의 score evidence 불가
```

쉬운 예:

```text
가동률(utilization_rate)을 찾는 task 실행
→ 문서에서 FCF 문장을 발견
→ 이 문장은 "FCF task를 새로 열어라"라는 힌트
→ 가동률 task가 해결된 것처럼 점수에 넣으면 안 됨
```

## 발견된 실제 문제

기존 0705 산출물에서 KG케미칼 C15 row가 문제를 만들었다.

```text
task_id: ST-001390-C15-UTIL-NEWSROOM-ORIGINAL-002
symbol: 001390
requested primitive_gap: utilization_rate
accepted primitive: fcf_quality_score
satisfaction_type: REROUTED_ACCEPTED_CLAIM
satisfies_source_task: false
source: 2017년 하나증권 PDF
quote: 2018/2019 영업이익 기여 추정
```

그런데 기존 export는 이 rerouted claim에 여섯 개 component score contribution을 만들었다.

```text
eps_fcf_explosion
earnings_visibility
bottleneck_pricing
market_mispricing
valuation_rerating
information_confidence
```

이건 과거에 문제가 됐던 "월덱스/삼성전자 감사의견" 오류와 같은 계열이다.

```text
원래 조사 칸과 다른 문장
또는 오래된/current 불명확 문장
→ accepted claim처럼 보임
→ 점수 계산기로 들어감
```

## 패치 내용

수정 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_brain_bundle_export.py
tests/test_census_v4_brain_web_readiness_gate.py
```

핵심 변경:

1. `_brain_claim_score_eligibility_reasons()`에 source task satisfaction 축을 추가했다.
2. `satisfies_source_task=false` 또는 `satisfaction_type=REROUTED_ACCEPTED_CLAIM`이면 `source_task_not_satisfied_rerouted_claim` 사유로 score ineligible 처리한다.
3. `_brain_score_stage_export_rows()`는 score-admissible claim만 남긴 임시 ledger로 primitive/state/score contribution을 계산한다.
4. rerouted claim은 accepted leaf와 mapping trace에는 남지만 score contribution과 StageCourt trace에는 들어가지 않는다.
5. readiness gate의 `_source_task_execution_reached_score_evidence()`도 rerouted-only execution을 score evidence로 세지 않는다.

## 검증 결과

추가/갱신 테스트:

```text
test_rerouted_claim_is_planner_feedback_not_score_export
test_official_first_rerouted_claim_is_not_score_evidence
```

관련 테스트 묶음:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_bundle_export \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_source_task_satisfaction_chain \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_research_brain_v4_operational_modes -v
```

결과:

```text
Ran 162 tests in 42.389s
OK
```

전체 unittest 결과도 별도 machine-readable artifact로 남겼다.

```text
artifact: docs/0705/goal4_full_unittest_result_2026-07-08.json
command: PYTHONPATH=src python -m unittest discover -s tests -v
result: Ran 5300 tests, OK
duration_seconds: 440.044
log_path: output/test_results/goal4_full_unittest_2026-07-08.log
log_sha256: e8080d26d8639f4c47f3466cb41c8e54ae9d8979597a922d7690e7aedafb89b8
```

기존 0705 leaf 파일에 새 readiness gate 로직만 다시 적용한 빠른 재감사:

```json
{
  "verdict": "READY_FOR_BRAIN_WEB_EVIDENCE_PASS",
  "official_first_violation_count": 0,
  "official_first_violation_examples": [],
  "blockers": []
}
```

주의: 이 빠른 재감사는 전체 live census 재실행이 아니다. 기존 output leaf를 새 gate 함수로 다시 판정한 것이다.

## 남은 Goal4 상태

Goal4는 아직 완료가 아니다.

남은 큰 blocker는 full thesis 쪽이다.

```text
full thesis seed materialization audit failed
full thesis production pass false
production rows with required_positive_missing_primitives
meaningful runtime parity not ready
```

이번 패치로 정리된 것은 Brain/Web partial evidence가 잘못된 rerouted score evidence를 만들던 경로다.

다음 작업은 full thesis production row가 왜 의미 있는 full thesis가 아니라 score-path closed / missing positive 상태로 남는지 줄여야 한다.

특히 봐야 할 축:

```text
seed target_archetype
planner top_k_archetype
final assigned archetype
required_positive_missing_primitives
source task direct satisfaction
full thesis stage/use 분리
```
