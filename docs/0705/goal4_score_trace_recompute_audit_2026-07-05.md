# Goal4 Score Trace Recompute Audit - 2026-07-05

## 결론

최신 0705 runtime attempt의 삼성전자 C06 full-thesis trace는 raw component 합계와 StageCourt 총점이 다르지만, 이는 점수 오류가 아니라 C06 runtime weight 적용 결과로 재현된다.

```text
trace: SCT-BRAIN-1e999f3308d1bc0f3d6b
symbol: 005930
archetype: C06_HBM_MEMORY_CUSTOMER_CAPACITY
raw contribution sum: 40.8334
deterministic recompute verified_score: 44.1667
stagecourt score_interval.lower: 44.1667
score recompute mismatch: 0
```

쉬운 예:

```text
과목 원점수 합계가 40.8334점이어도,
C06 전용 배점표가 EPS/FCF 쪽 비중을 더 크게 주면
최종 weighted 총점은 44.1667점이 될 수 있다.

따라서 raw 합계와 총점이 다르다는 사실만으로는 오류가 아니다.
같은 배점표로 다시 채점했을 때 같은 총점이 나오는지가 진짜 검산이다.
```

## 이번 패치

`census_v4_auditor`에 StageCourt score recompute audit을 추가했다.

새 critical counters:

```text
stagecourt_score_recompute_mismatch_count
stagecourt_score_contribution_ref_missing_count
```

검사 방식:

```text
stagecourt trace
→ score_contribution_ids 로 persisted score_contributions 조회
→ primary_archetype/canonical_archetype 확인
→ ScoreContributionV2 재구성
→ DeterministicScorer 재실행
→ recomputed total_score 와 score_interval.lower 비교
```

이전처럼 `raw_points 합계 == score_interval`로 검사하지 않는다.
그 방식은 아키타입 runtime weight가 적용되는 정상 케이스까지 실패로 오판한다.

## 최신 0705 실런 상태

새 감사 기준으로 operational score audit은 PASS다.

```text
docs/operational/census_mode_v4_score_scale_audit.json
verdict: PASS
stagecourt_score_recompute_mismatch_count: 0
stagecourt_score_contribution_ref_missing_count: 0
```

추가 패치 후 전체 leaf audit도 PASS로 내려왔다.

```text
docs/operational/census_mode_v4_leaf_artifact_audit.json
verdict: PASS
critical_count: 0
nonzero critical: {}
```

즉 현재 문제는 "점수가 수학적으로 안 맞는다"도 아니고 "promoted row가 snapshot 문서를 점수 근거로 썼다"도 아니다.
promoted 삼성전자 row의 문서는 CompanyGuide/OpenDART이고, snapshot 문서 2개는 unpromoted 후보 쪽에 남아 있다.

쉬운 예:

```text
계산기 검산은 맞는다.
정식 성적표에 첨부된 서류도 DART/CompanyGuide다.
다만 다른 후보 파일함에 snapshot 서류가 남아 있었고, 이전 audit은 그것까지 삼성 row의 문제처럼 막았다.
```

## Goal4 판단

이번 패치 후에도 Goal4는 완료가 아니다.

이유:

```text
1. 전 아키타입 runtime parity가 아직 증명되지 않았다.
2. latest runtime attempt는 C06 row를 만들었지만 required positive primitive가 부족하다.
3. Brain/Web readiness gate는 web/LLM accepted claim 0개와 source task budget cap 초과로 아직 BLOCKED다.
4. 하이닉스 controlled smoke와 production row는 여전히 분리되어 있다.
```

다음 패치 우선순위:

```text
1. web/LLM accepted claim 0개가 왜 발생했는지 claim extractor/source task 단위로 분해한다.
2. C05/C06 외 아키타입이 왜 production full-thesis로 승급하지 못했는지 matrix를 갱신한다.
3. score formula trace에는 raw component, weighted component, scorer version을 operator-facing으로 남긴다.
4. 삼성/하이닉스는 smoke 결과와 production 결과를 계속 분리해서 보고한다.
```
