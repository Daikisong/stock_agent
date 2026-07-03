# Census v4 v95 - Full Thesis Seed Materialization Scope Split Patch

작성일: 2026-07-03

## 1. 문제

기존 `full_thesis_seed_materialization_audit.json`은 다음 상태에서도 `verdict=PASS`가 될 수 있었다.

```text
seed_event_count > 0
status_counts = PLANNER_NOT_RUN ...
full_thesis_promoted_seed_count = 0
critical_count = 0
verdict = PASS
```

이 PASS는 원래 “거짓 승급이 없고 장부 순서가 깨지지 않았다”는 뜻이었다.

하지만 이름만 보면 다음처럼 오해하기 쉽다.

```text
full thesis seed materialization audit PASS
-> seed가 실제 FULL_THESIS로 물질화됐다
```

이건 틀린 해석이다.

쉬운 예:

```text
신청서 접수 장부가 깨끗하다
-> 맞음.

신청이 최종 승인됐다
-> 아직 아님.
```

## 2. 패치

`_full_thesis_seed_materialization_audit()`에 의미를 나누는 필드를 추가했다.

```text
verdict
  기존 호환 필드. critical_count=0이면 PASS.

verdict_scope
  LEDGER_INTEGRITY_ONLY
  ACTUAL_FULL_THESIS_MATERIALIZATION

ledger_integrity_pass_allowed
  장부 무결성 pass 여부.

actual_materialization_pass_allowed
  실제 FULL_THESIS seed closure 여부.

full_thesis_seed_promotion_pass
  actual_materialization_pass_allowed와 같은 운영 성공 의미.

operator_materialization_status
  PENDING_FULL_THESIS_MATERIALIZATION
  FULL_THESIS_MATERIALIZED
```

즉 앞으로는 이렇게 읽어야 한다.

```text
verdict=PASS
+ verdict_scope=LEDGER_INTEGRITY_ONLY
+ actual_materialization_pass_allowed=false
-> 장부는 깨끗하지만 실제 FULL_THESIS는 아직 아니다.

verdict=PASS
+ verdict_scope=ACTUAL_FULL_THESIS_MATERIALIZATION
+ actual_materialization_pass_allowed=true
-> seed가 실제 source-backed StageCourt trace를 거쳐 FULL_THESIS로 닫혔다.
```

## 3. Readiness / Goal Audit 연결

`readiness_verdict.json`의 `full_thesis_seed_materialization_audit` 요약에도 새 필드를 노출한다.

```text
verdict_scope
ledger_integrity_pass_allowed
actual_materialization_pass_allowed
operator_materialization_status
```

`goal_completion_audit.json`에도 아래 필드를 추가했다.

```text
full_thesis_seed_ledger_integrity_pass_allowed
full_thesis_seed_actual_materialization_pass_allowed
```

기존 필드는 호환을 위해 유지한다.

```text
full_thesis_seed_materialization_audit_pass_allowed
```

하지만 이 필드는 이제 반드시 “장부 무결성”으로 읽어야 한다.

운영 성공은 아래 필드가 true여야 한다.

```text
full_thesis_seed_actual_materialization_pass_allowed
full_thesis_seed_promotion_pass_allowed
```

## 4. Readiness Label 보강

새 라벨을 추가했다.

```text
FULL_THESIS_SEED_LEDGER_INTEGRITY_PASS
FULL_THESIS_SEED_ACTUAL_MATERIALIZATION_PENDING
FULL_THESIS_SEED_ACTUAL_MATERIALIZATION_PASS
```

따라서 다음 조합은 정상적인 pending 상태다.

```text
FULL_THESIS_SEED_LEDGER_INTEGRITY_PASS
FULL_THESIS_SEED_PROMOTION_PENDING
FULL_THESIS_SEED_ACTUAL_MATERIALIZATION_PENDING
```

이 조합은 “장부는 안전하지만 운영 FULL_THESIS는 아직 없다”는 뜻이다.

## 5. 테스트 보강

보강한 테스트:

```text
tests/test_census_v4_full_thesis_smoke_tasks.py
tests/test_census_v4_goal_required_audits.py
tests/test_census_v4_brain_web_readiness_gate.py
```

검증 내용:

```text
기본 ledger-refresh run:
  verdict = PASS
  verdict_scope = LEDGER_INTEGRITY_ONLY
  ledger_integrity_pass_allowed = true
  actual_materialization_pass_allowed = false
  operator_materialization_status = PENDING_FULL_THESIS_MATERIALIZATION

혼합 fixture 중 FULL_THESIS_PROMOTED가 있는 경우:
  verdict = PASS
  verdict_scope = ACTUAL_FULL_THESIS_MATERIALIZATION
  actual_materialization_pass_allowed = true
  operator_materialization_status = FULL_THESIS_MATERIALIZED
```

## 6. 운영 해석

v95 이후에도 현재 최신 live truth는 바뀌지 않는다.

```text
운영 FULL_THESIS Stage = 0
FULL_E2R_100 score = 0
NOT_READY
```

이번 패치는 Stage를 만든 것이 아니다.

이번 패치는 다음 오해를 막는 패치다.

```text
full_thesis_seed_materialization_audit.verdict=PASS
-> 실제 FULL_THESIS materialization 성공
```

정확한 판정은 아래 필드로 해야 한다.

```text
actual_materialization_pass_allowed
```

## 7. 다음 에이전트 공격 포인트

다음 에이전트는 아래를 반드시 확인해야 한다.

```text
1. full_thesis_seed_materialization_audit.verdict만 보고 성공 처리하지 않았는가?
2. verdict_scope가 LEDGER_INTEGRITY_ONLY면 운영 Stage로 쓰지 않는가?
3. actual_materialization_pass_allowed=false인데 readiness가 READY가 되지 않는가?
4. goal_completion_audit가 full_thesis_seed_actual_materialization_pass_allowed를 노출하는가?
5. FULL_THESIS_SEED_ACTUAL_MATERIALIZATION_PENDING 라벨이 남아 있으면 다음 실행 과제로 보내는가?
```

## 8. 한 줄 결론

```text
v95는 seed materialization audit의 PASS 의미를 분리했다.
장부 무결성 PASS와 실제 FULL_THESIS materialization PASS는 이제 다른 필드다.
```
