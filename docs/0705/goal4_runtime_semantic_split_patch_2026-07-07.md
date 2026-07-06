# Goal4 Runtime Semantic Split Patch

작성일: 2026-07-07

## 결론

이번 패치는 `FULL_THESIS_PRODUCTION_PASS`가 운영 thesis 완성처럼 보이는 문제를 줄이기 위해, 런타임 감사 산출물에 아래 두 상태를 명시적으로 분리한다.

```text
PRODUCTION_FULL_E2R_SCORE_PATH_PASS
= production FULL_E2R_100 row가 claim -> score -> StageCourt 경로를 통과했다는 뜻

MEANINGFUL_FULL_THESIS_EVIDENCE_PASS
= required-positive primitive와 Green primitive gap까지 닫힌 운영 thesis 증거 완성
```

쉬운 예:

```text
시험 점수 계산표는 만들어졌다
-> PRODUCTION_FULL_E2R_SCORE_PATH_PASS 가능

그런데 필수 증빙 서류가 비어 있다
-> MEANINGFUL_FULL_THESIS_EVIDENCE_PASS는 false
```

따라서 `27.9998`, `77.9998` 같은 점수가 찍혔다는 사실만으로는 Goal4 완료가 아니다.

## Strict Zero-Gap Rule

이번 패치 후 `MEANINGFUL_FULL_THESIS_EVIDENCE_PASS`는 아래 조건을 모두 만족해야만 true다.

```text
mandatory archetype full-thesis missing = 0
required-positive missing promoted row = 0
Green gap promoted row = 0
```

기존의 `required_positive_missing <= 30%` 같은 완화 기준은 Goal4 의미와 맞지 않는다.

쉬운 예:

```text
필수 서류가 10명 중 2명만 빠졌다
-> 80% 완성처럼 보일 수는 있음
-> 하지만 운영 full thesis 합격은 아님

필수 서류 0명 누락
Green gap 0명 누락
mandatory 아키타입 전부 production row 보유
-> 그때만 meaningful evidence pass 가능
```

## 왜 필요했나

기존 감사 출력은 다음 세 상태가 섞여 보일 위험이 있었다.

```text
1. 점수 경로가 실행됐다.
2. production FULL_THESIS row가 생겼다.
3. 운영 thesis에 필요한 증거가 충분하다.
```

Goal4 기준에서는 1번과 2번만으로 완료 처리하면 안 된다.

예를 들어 C05 row 7개가 production FULL_E2R score path를 지나도, 모든 row에 `required_positive_missing_primitives`가 남아 있으면 의미 있는 full thesis가 아니다.

## 코드 변경

변경 파일:

```text
src/e2r/census/research_to_runtime_parity.py
src/e2r/census/census_runner_v4.py
docs/operational/meaningful_full_thesis_production_acceptance.json
tests/test_full_thesis_score_path_not_meaningful_pass.py
tests/test_census_v4_goal_required_audits.py
tests/test_meaningful_full_thesis_production_acceptance.py
tests/test_no_c05_only_meaningful_pass.py
tests/test_required_positive_missing_blocks_meaningful_pass.py
```

새 helper:

```text
_full_thesis_score_path_pass_allowed(audit)
_meaningful_full_thesis_evidence_pass_allowed(audit)
_full_thesis_goal4_semantic_split(audit)
```

`_full_thesis_goal4_semantic_split`이 반환하는 핵심 필드:

```json
{
  "score_path_label": "PRODUCTION_FULL_E2R_SCORE_PATH_PASS",
  "meaningful_label": "MEANINGFUL_FULL_THESIS_EVIDENCE_PASS_FALSE",
  "production_full_e2r_score_path_pass": true,
  "meaningful_full_thesis_evidence_pass": false,
  "score_path_only_not_meaningful": true,
  "required_positive_missing_row_count": 7,
  "green_gap_row_count": 7,
  "blockers": [
    "production_score_path_is_not_meaningful_full_thesis_pass",
    "required_positive_missing_on_promoted_rows",
    "green_gap_on_promoted_rows"
  ]
}
```

## 연결된 감사 산출물

아래 감사 함수들이 새 split을 출력한다.

```text
_goal_requirement_matrix_audit
_goal_completion_audit
_self_repair_log_v4
```

따라서 이후 생성되는 산출물에서는 다음을 별도로 볼 수 있다.

```text
production_full_e2r_score_path_pass
meaningful_full_thesis_evidence_pass
full_thesis_goal4_semantic_split
```

## 막는 오류

이 패치는 아래 착시를 막는다.

```text
나쁜 해석:
production FULL_THESIS row가 있음
-> 점수가 있음
-> Goal4 full thesis 완료

패치 후 해석:
production FULL_THESIS row가 있음
-> score path는 닫힘
-> required-positive / Green gap이 남으면 meaningful thesis는 false
```

즉 `score path closed`와 `meaningful full thesis completed`는 서로 다른 도장이다.

## Goal4 현재 상태

이 패치는 Goal4 완료가 아니다.

현재까지 확인된 상태:

```text
전 아키타입 row / source route / blocker matrix
-> 존재

production FULL_E2R score path
-> 일부 닫힘

meaningful runtime parity
-> 아직 not ready

required-positive / Green primitive gap
-> 남아 있음

C15, C24 등 mandatory archetype production full-thesis row
-> 아직 missing 또는 source-backed parity 미완성
```

따라서 다음 문장이 현재의 정확한 운영 판단이다.

```text
점수 계산 경로가 일부 닫힌 것은 맞지만,
모든 아키타입의 운영 thesis 증거가 닫힌 것은 아니다.
```

## Latest Blocker Snapshot

현재 `docs/operational/all_archetype_runtime_status_matrix_2026-07-05.json` 기준 상태 분포:

```text
SCORE_PATH_CLOSED_WITH_THESIS_GAPS = 7
SCORE_PATH_NOT_CLOSED = 2
SOURCE_REPAIR_REQUIRED = 24
TARGET_MATERIALIZATION_REQUIRED = 3
```

핵심은 전 아키타입 row가 없어서가 아니라, row 이후 단계가 닫히지 않은 것이다.

쉬운 예:

```text
36개 과목 출석부는 있다.
그런데 7개 과목만 답안지 채점까지 갔고,
그 7개도 필수 첨부서류가 빠졌다.
나머지는 아직 답안지 자체가 없거나, 답안지는 있어도 채점표로 연결되지 않았다.
```

Mandatory canary 상태:

```text
C06: production score path 있음, required-positive/Green gap 남음
C08: production score path 있음, required-positive/Green gap 남음
C15: accepted claim은 있음, full thesis row로 닫히지 못함
C17: production score path 있음, required-positive/Green gap 남음
C24: replay accepted claim만 있고 production accepted claim 없음
C28: production score path 있음, required-positive/Green gap 남음
```

C15와 C24는 서로 다른 문제다.

```text
C15
-> 운영 원문에서 accepted claim은 만들어졌다.
-> 그런데 required-positive/Green primitive가 source-backed 상태로 닫히지 않아 full thesis row가 막혔다.

C24
-> 연구 replay에는 accepted claim이 있다.
-> 하지만 production source task에서는 accepted claim이 0개라 운영 full thesis로 올라오지 못했다.
```

따라서 다음 실제 패치 우선순위는 다음과 같다.

```text
1. C24 production source task -> accepted claim 생성 실패 원인 추적
2. C15 accepted claim -> required-positive/Green primitive closure 실패 원인 추적
3. 이미 score path가 닫힌 C06/C08/C17/C28의 missing primitive를 source-backed claim으로 닫기
4. SOURCE_REPAIR_REQUIRED 24개를 ACCEPTED_CLAIM_PRESENT 또는 명시적 external/source blocker로 승격
5. TARGET_MATERIALIZATION_REQUIRED 3개는 실제 symbol candidate materialization 여부를 분리 감사
```

## 검증

이번 패치 직후 통과한 targeted 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_to_runtime_parity_goal4 \
  tests.test_meaningful_full_thesis_production_acceptance \
  tests.test_no_c05_only_meaningful_pass \
  tests.test_required_positive_missing_blocks_meaningful_pass \
  tests.test_full_thesis_score_path_not_meaningful_pass \
  tests.test_census_v4_goal_required_audits -v
```

결과:

```text
Ran 18 tests
OK
```

전체 테스트:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5282 tests
OK
```

주의:

```text
테스트 로그에 MEANINGFUL_RUNTIME_PARITY_NOT_READY,
REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS 같은 문구가 출력되는 것은 의도된 실패 상태를 검증하는 것이다.
unittest suite 자체는 OK다.
```

쉬운 예:

```text
화재경보기 테스트에서 "경보 울림" 메시지가 출력되는 것은 정상이다.
경보가 울려야 하는 상황을 일부러 넣었고, 시스템이 그 상태를 정확히 잡았다는 뜻이다.
```

## 남은 작업

다음 단계는 이 split을 기준으로 Goal4 남은 blocker를 줄이는 것이다.

```text
1. C15 / C24 mandatory production row missing 해소
2. C05 외 archetype의 source-backed accepted claim materialization 증명
3. required-positive primitive missing row를 실제 source task / claim / primitive state로 닫기
4. Green gap primitive가 남은 row는 meaningful pass에서 계속 차단
5. all-archetype replay matrix가 external source-backed acceptance를 통과할 때까지 Goal4 완료 금지
```

운영 규칙:

```text
score path pass는 작업 진행 증거다.
meaningful evidence pass만 Goal4 완료 증거다.
```
