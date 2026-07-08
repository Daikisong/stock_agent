# Goal4 0705 Commit Handoff

작성일: 2026-07-08

대상 실행:

```text
output/census_v4/2026-07-05-goal4-all-archetype-next-runtime-attempt-e0e9399
```

## 결론

이번 커밋은 Goal4 완료 커밋이 아니다.

이번 커밋의 의미는 두 가지다.

```text
1. rerouted accepted claim이 점수/Stage로 새는 경로를 막음
2. 0705 full-thesis 상태를 다시 문서화하고 전체 unittest artifact를 남김
```

쉬운 예:

```text
가동률을 찾으러 갔는데 문서에서 FCF 문장만 발견했다.
그 FCF 문장은 다음 조사 힌트는 될 수 있다.
하지만 "가동률 증거를 찾았다"며 점수에 넣으면 안 된다.
```

## 이번에 고친 실제 오류

기존 0705 산출물의 KG케미칼 C15 source task에서 다음 일이 있었다.

```text
requested primitive_gap: utilization_rate
accepted primitive: fcf_quality_score
satisfaction_type: REROUTED_ACCEPTED_CLAIM
satisfies_source_task: false
```

기존 코드에서는 이 rerouted claim이 accepted claim으로 남은 뒤 score contribution과 StageCourt trace까지 만들어졌다.

이번 패치 후 원칙:

```text
direct accepted claim
-> score 후보 가능

rerouted accepted claim
-> planner feedback / follow-up seed 가능
-> 현재 source task의 score evidence 불가
```

수정 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_brain_bundle_export.py
tests/test_census_v4_brain_web_readiness_gate.py
docs/0705/goal4_rerouted_claim_score_path_patch_audit_2026-07-08.md
docs/0705/goal4_full_unittest_result_2026-07-08.json
```

## 현재 0705 full-thesis 상태

현재 e0e9399 output 기준 production full-thesis row는 6개다.

| symbol | company | archetype | score | stage | required-positive gap |
|---|---|---|---:|---|---|
| 003380 | 하림지주 | C05 | 27.9998 | 0 | contract_amount_to_prior_sales, margin_bridge_visible |
| 005930 | 삼성전자 | C06 | 39.8333 | 0 | customer_preorder_or_allocation, hbm_capacity_constraint, hbm_capacity_pre_sold, medium_term_revision_visibility, memory_price_increase_mentioned |
| 011170 | 롯데케미칼 | C17 | 37.5 | 0 | inventory_cycle, opm_expansion_pctp |
| 047810 | 한국항공우주 | C03 | 37.0 | 0 | government_customer, order_backlog_to_sales |
| 052400 | 코나아이 | C01 | 11.9999 | 0 | contract_quality, fcf_quality_score, named_customer_quality, opm_expansion_pctp, order_backlog_to_sales |
| 058470 | 리노공업 | C08 | 50.8 | 1 | qualification_confirmed, repeat_order_confirmed, socket_or_test_demand_visible |

감사 결과:

```text
full_thesis_row_count = 6
production_full_thesis_row_count = 6
production_full_thesis_row_with_required_positive_missing_primitives_count = 6
production_full_thesis_row_with_green_gap_primitives_count = 6
production_pass_allowed = false
verdict = PENDING_FULL_THESIS_PRODUCTION
blocker = production_full_thesis_rows_with_required_positive_missing_primitives
```

즉 현재 상태는 다음이다.

```text
score path 일부 실행됨
!= meaningful full thesis 완료
```

쉬운 예:

```text
6개 답안지는 채점표까지 갔다.
하지만 6개 모두 필수 증빙 서류가 빠져 있다.
따라서 "채점 시스템이 일부 돈다"는 말은 가능하지만,
"운영 full thesis가 합격했다"는 말은 아직 틀리다.
```

## 예전 C05-only 6개 질문의 위치

예전 질문:

```text
1. 왜 production FULL_THESIS 10개가 전부 C05인가?
2. target_archetype_counts가 UNKNOWN인데 왜 최종 C05인가?
3. 27.9998 / 77.9998 점수는 어디서 나왔나?
4. C05가 아닌 아키타입은 왜 0개인가?
5. required_positive_missing이 있는데 왜 FULL_THESIS_PRODUCTION_PASS인가?
6. 삼성전자/하이닉스 controlled smoke와 production row가 왜 다른가?
```

답은 아래 기존 0705 문서에 정리되어 있다.

```text
docs/0705/census_v4_full_thesis_production_c05_audit_2026-07-05.md
docs/0705/goal4_runtime_semantic_split_patch_2026-07-07.md
docs/0705/goal4_live_bounded_runtime_attempt_e0e9399_not_ready_audit_2026-07-08.md
```

현재 e0e9399 기준으로는 예전 C05-only 10개 상태가 그대로 유지되지 않는다.

```text
이전: production FULL_THESIS 10개가 전부 C05
현재: production FULL_THESIS 6개가 C05/C06/C17/C03/C01/C08로 분산
```

하지만 본질적 문제는 아직 남아 있다.

```text
전 아키타입 meaningful full thesis는 아직 아님
6개 production row 모두 required-positive gap 보유
C15/C24/C28 등 주요 아키타입은 production full-thesis parity 미완성
```

## 검증

Targeted regression:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_bundle_export.CensusV4BrainBundleExportTests.test_rerouted_claim_is_planner_feedback_not_score_export \
  tests.test_census_v4_brain_web_readiness_gate.CensusV4BrainWebReadinessGateTests.test_official_first_rerouted_claim_is_not_score_evidence -v
```

결과:

```text
OK
```

관련 162-test slice:

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
Ran 162 tests
OK
```

전체 unittest artifact:

```text
docs/0705/goal4_full_unittest_result_2026-07-08.json
Ran 5300 tests
OK
```

## 남은 작업

다음 blocker는 아직 해결되지 않았다.

```text
full thesis seed materialization audit failed
full thesis production pass false
production rows with required-positive missing primitives
meaningful runtime parity not ready
```

다음 패치 우선순위:

```text
1. C15/C24/C28 production accepted claim 생성 실패 원인 추적
2. production row 6개의 required-positive gap을 source-backed claim으로 닫기
3. full thesis score path pass와 meaningful thesis pass가 모든 감사 출력에서 계속 분리되는지 확인
4. Goal4 완료 선언은 전 아키타입 replay/production parity가 모두 닫힌 뒤에만 하기
```
