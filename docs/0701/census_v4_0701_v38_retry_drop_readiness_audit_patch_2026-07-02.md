# Census v4 0701 v38 Retry Drop Readiness Audit Patch

작성일: 2026-07-02 KST

## 0. 결론

v38은 v37의 남은 P0를 닫는 관측성 패치다.

v37:

```text
source_lineage_unverified_original 이후 discovery-only retry drop을
source_task_executions.jsonl에 REJECTED_BY_POLICY row로 남김
```

v38:

```text
그 dropped retry row를 brain_web_readiness_gate_audit.json과
readiness_verdict.json 요약에도 count로 노출
```

쉬운 예:

```text
1차 시도:
  네이버/일반 웹 결과가 원문 lineage 미검증으로 reject

LLM retry:
  또 NaverSearch / GeneralWeb / IndustryMedia만 제안

실행 정책:
  다시 크롤링하지 않고 REJECTED_BY_POLICY로 leaf에 기록

v38 readiness:
  source_lineage_feedback_retry_dropped_count = 1
  policy_rejected_source_task_execution_count = 1
  zero_budget_policy_rejected_source_task_execution_count = 1
```

즉 readiness를 보는 리뷰어도 "왜 source task가 있었는데 claim이 없었는지"를 바로 추적할 수 있다.

## 1. 왜 필요한가

goal 문서는 Brain/Web 성공 여부를 report 문구가 아니라 leaf artifact로 증명하라고 요구한다.

v37은 leaf에는 drop row를 남겼지만, canonical readiness audit은 그 숫자를 직접 드러내지 않았다.

그러면 다음 문제가 생긴다.

```text
source_task_executions.jsonl:
  REJECTED_BY_POLICY drop row 있음

brain_web_readiness_gate_audit.json:
  source_task_execution_count만 보이고 drop 성격이 잘 안 보임
```

v38은 이 간극을 줄인다.

```text
source_task_executions leaf
  -> brain_web_readiness_gate_audit
  -> readiness_verdict 요약
```

까지 같은 실패 원인을 연결한다.

## 2. 코드 변경

수정 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_brain_web_readiness_gate.py
docs/0701/README.md
docs/0701/census_v4_0701_v38_retry_drop_readiness_audit_patch_2026-07-02.md
```

### 2.1 brain_web_readiness_gate_audit 추가 fields

추가된 fields:

```text
policy_rejected_source_task_execution_count
zero_budget_policy_rejected_source_task_execution_count
source_lineage_feedback_retry_dropped_count
discovery_only_retry_after_unverified_original_count
```

`source_lineage_feedback_retry_dropped_count`와
`discovery_only_retry_after_unverified_original_count`는 같은 사건을 다른 감사자가 이해하기 쉽게 별칭으로 노출한다.

### 2.2 count 조건

`source_lineage_feedback_retry_dropped_count`는 다음 조건으로 계산한다.

```text
source_origin = research_brain_v4_attempt
status = REJECTED_BY_POLICY
그리고 stop_reason / not_eligible_reasons / provider_errors /
source_task.reason_from_memory 중 하나에
source_lineage_retry_discovery_only_after_unverified_original 포함
```

`zero_budget_policy_rejected_source_task_execution_count`는 다음 조건으로 계산한다.

```text
status = REJECTED_BY_POLICY
budget_used.queries = 0
budget_used.candidates = 0
budget_used.fetches = 0
```

중요한 점:

```text
이 count는 점수나 Stage를 만들지 않는다.
오직 감사와 readiness 설명에만 사용한다.
```

## 3. 하드코딩 여부

이 패치는 종목명, 섹터명, 아키타입명, 검색어를 만들지 않는다.

나쁜 방식:

```text
if symbol == "005930":
  dropped_count += 1
```

v38 방식:

```text
leaf row의 status / stop_reason / budget_used / reason tag를 집계
```

즉 LLM이 만든 query를 deterministic code가 새로 짜는 게 아니다.
이미 발생한 정책 거절 실행 row를 canonical audit에 반영하는 것이다.

## 4. 테스트

타깃 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_web_readiness_gate.CensusV4BrainWebReadinessGateTests.test_source_lineage_retry_drop_is_counted_in_readiness_gate -v
```

결과:

```text
Ran 1 test
OK
```

관련 묶음 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_bundle_export \
  tests.test_census_v4_run_mode_honesty -v
```

결과:

```text
Ran 44 tests in 43.109s
OK
```

전체 테스트:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5070 tests in 213.234s
OK
```

## 5. 검증된 동작

새 테스트가 만든 상황:

```text
planner row 있음
source_task_executions.jsonl에 REJECTED_BY_POLICY row 있음
accepted claim 없음
real document 없음
budget_used = 0/0/0
stop_reason = source_lineage_retry_discovery_only_after_unverified_original
```

기대 결과:

```text
verdict = BLOCKED
source_task_execution_count = 1
policy_rejected_source_task_execution_count = 1
zero_budget_policy_rejected_source_task_execution_count = 1
source_lineage_feedback_retry_dropped_count = 1
discovery_only_retry_after_unverified_original_count = 1
```

그리고 다음 blocker는 나오면 안 된다.

```text
Brain/Web source task attempt count has no exported source_task_executions rows
```

이유:

```text
source task execution row는 실제로 export됐다.
다만 그 row가 evidence success가 아니라 zero-budget policy rejection일 뿐이다.
```

## 6. 현재 운영 상태

v38도 운영 FULL_THESIS Stage를 만든 패치가 아니다.

현재 중요한 truth는 그대로다.

```text
CENSUS_EVENT_BOARD Stage row:
  있음

FULL_THESIS 운영 Stage row:
  아직 0개

FULL_E2R verified score row:
  아직 0개
```

즉 v38은 "성공했다"가 아니라 "실패와 차단을 더 정확히 볼 수 있다"에 해당한다.

## 7. 다음 패치 방향

이제 관측성 P0는 한 단계 닫혔다.

다음 핵심은 실제 source-backed positive chain이다.

```text
1. source_lineage_unverified_original feedback
2. LLM retry가 original-capable source class 제안
3. CompanyNewsroom / ReportPDF / TrustedNews original / DART detail fetch
4. EvidenceDocument
5. EvidenceAnchor
6. LLM claim extractor
7. accepted claim
8. primitive state
9. score contribution
10. StageCourt trace
11. FULL_THESIS promotion gate 판단
```

리뷰어가 봐야 할 다음 질문:

```text
좋은 retry가 실제 원문 claim으로 성공하는 positive test가 있는가?
web_or_llm_accepted_claim_count가 0이 아닌 운영 경로가 있는가?
삼성전자/하이닉스 C06이 source-backed FULL_THESIS path로 닫히는가?
```

현재 답은 아직 "아니다"다.

## 8. 최종 판정

v38 이후 개선:

```text
drop leaf row:
  있음

drop readiness count:
  있음

drop readiness verdict summary:
  있음
```

아직 미완:

```text
Brain/Web accepted claim 운영 성공
FULL_THESIS production row
삼성전자/하이닉스 source-backed live C06 운영 판정
전 아키타입 live source-backed parity
```

따라서 전체 goal 완료는 아니다.
