# Census v4 0701 v40 Source Lineage Retry Outcome Readiness Counts

작성일: 2026-07-02 KST

## 0. 결론

v40은 v39의 양성 경로를 readiness audit에 노출하는 패치다.

v39에서 검증한 것:

```text
source_lineage_unverified_original로 1차 일반검색/뉴스가 탈락해도
LLM retry가 DART/IR/회사뉴스룸/원문PDF 같은 원문 가능 source task를 내면
그 task는 실행되고 accepted claim까지 갈 수 있다.
```

v40에서 추가한 것:

```text
brain_web_readiness_gate_audit.json과 readiness_verdict.json에서
source-lineage feedback retry의 결과를 good/bad로 나눠 볼 수 있다.
```

새 필드:

```text
source_lineage_feedback_retry_execution_count
source_lineage_feedback_retry_accepted_execution_count
source_lineage_feedback_retry_no_evidence_execution_count
source_lineage_feedback_retry_dropped_count
discovery_only_retry_after_unverified_original_count
```

쉬운 예:

```text
1. 일반검색 뉴스가 원문 lineage 미검증으로 탈락
2. LLM retry가 DART 원문 계약 공시를 제안
3. DART anchor에서 accepted claim 생성

v40 readiness:
  source_lineage_feedback_retry_execution_count = 1
  source_lineage_feedback_retry_accepted_execution_count = 1
  source_lineage_feedback_retry_no_evidence_execution_count = 0
  source_lineage_feedback_retry_dropped_count = 0
```

반대로 LLM retry가 다시 네이버/일반웹만 내면:

```text
source_lineage_feedback_retry_execution_count = 1
source_lineage_feedback_retry_accepted_execution_count = 0
source_lineage_feedback_retry_no_evidence_execution_count = 0
source_lineage_feedback_retry_dropped_count = 1
```

중요:

```text
v40은 점수/Stage 승격 패치가 아니다.
FULL_THESIS 운영 Stage row는 여전히 별도 leaf-chain 증명이 필요하다.
```

## 1. 왜 필요한가

v38은 bad retry drop을 readiness에 노출했다.
v39는 good retry가 accepted claim까지 갈 수 있음을 테스트했다.

하지만 v39 이후에도 readiness를 보면 다음 질문이 남았다.

```text
source-lineage retry가 몇 번 실행됐는가?
그중 몇 번 accepted claim으로 회복됐는가?
그중 몇 번 다시 no evidence로 끝났는가?
그중 몇 번 discovery-only라 정책적으로 drop됐는가?
```

기존에는 이 질문에 바로 답하기 어려웠다.
`source_task_execution_count`와 `accepted_claim_count`에 섞여 있었기 때문이다.

v40은 source-lineage retry만 따로 잘라 보여준다.

## 2. 코드 변경

수정 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_brain_web_readiness_gate.py
docs/0701/README.md
docs/0701/census_v4_0701_v40_source_lineage_retry_outcome_readiness_counts_2026-07-02.md
```

### 2.1 새 helper

추가:

```text
_is_source_lineage_feedback_retry_execution(row)
```

판정 기준:

```text
reason_from_memory
source_task.reason_from_memory
source_task_origin
source_task_execution_origin
not_eligible_reasons
provider_errors
```

중 하나에 다음 tag가 있으면 source-lineage feedback retry로 본다.

```text
feedback_retry:source_lineage_unverified_original
```

종목명, 섹터명, 아키타입명은 조건으로 쓰지 않는다.

### 2.2 readiness gate 추가 fields

`_brain_web_readiness_gate_audit()`가 다음 fields를 반환한다.

```text
source_lineage_feedback_retry_execution_count
source_lineage_feedback_retry_accepted_execution_count
source_lineage_feedback_retry_no_evidence_execution_count
source_lineage_feedback_retry_dropped_count
discovery_only_retry_after_unverified_original_count
```

`readiness_verdict.json`의 `brain_web_readiness_gate` 요약에도 같은 fields를 추가했다.

## 3. 상태별 의미

### 3.1 execution_count

```text
source_lineage_feedback_retry_execution_count
```

의미:

```text
source-lineage 실패 feedback을 받은 뒤 실행 또는 정책처리된 retry source task row 수
```

여기에는 accepted, no evidence, provider failed, dropped가 모두 포함될 수 있다.

### 3.2 accepted_execution_count

```text
source_lineage_feedback_retry_accepted_execution_count
```

의미:

```text
feedback retry가 EVIDENCE_OS_ACCEPTED로 끝났고
accepted_claim_ids 또는 direct_accepted_claim_ids를 가진 row 수
```

쉬운 예:

```text
일반검색 뉴스 탈락
-> LLM이 DART 원문 공시로 재시도
-> 계약금액 claim accepted
```

### 3.3 no_evidence_execution_count

```text
source_lineage_feedback_retry_no_evidence_execution_count
```

의미:

```text
feedback retry를 실행했지만 NO_EVIDENCE_FOUND / PROVIDER_FAILED / BUDGET_EXHAUSTED로 끝난 row 수
```

쉬운 예:

```text
LLM이 IR PDF를 찾으라고 했지만 실제 provider가 원문을 못 가져옴
-> 낮은 점수로 확정하지 않고 no evidence/pending 쪽으로 남김
```

### 3.4 dropped_count

```text
source_lineage_feedback_retry_dropped_count
```

의미:

```text
source-lineage 실패 뒤 retry가 다시 discovery-only source만 내서
실행하지 않고 REJECTED_BY_POLICY로 남긴 row 수
```

쉬운 예:

```text
네이버 검색 결과가 원문 미검증으로 탈락했는데
LLM이 또 NaverSearch / GeneralWeb / IndustryMedia만 제안
-> 다시 긁지 않고 drop
```

## 4. 하드코딩 여부

이 패치는 검색어를 만들지 않는다.
점수도 만들지 않는다.
Stage도 올리지 않는다.

하지 않은 것:

```text
if symbol == "005930": ...
if archetype == "C06": ...
if query contains "HBM": ...
```

한 것:

```text
source_task_executions leaf row의 retry reason tag와 실행 결과를 집계
```

즉 LLM이 낸 retry plan의 결과가 readiness에서 숨지 않게 만든 감사 패치다.

## 5. 테스트

타깃 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_web_readiness_gate.CensusV4BrainWebReadinessGateTests.test_source_lineage_retry_drop_is_counted_in_readiness_gate \
  tests.test_census_v4_brain_web_readiness_gate.CensusV4BrainWebReadinessGateTests.test_source_lineage_good_retry_outcomes_are_counted_in_readiness_gate -v
```

결과:

```text
Ran 2 tests in 0.002s
OK
```

관련 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_run_mode_honesty \
  tests.test_census_v4_brain_bundle_export \
  tests.test_research_brain_v4_operational_modes -v
```

결과:

```text
Ran 92 tests in 41.515s
OK
```

전체 테스트:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v > /tmp/census_v40_full_unittest.log 2>&1
```

결과:

```text
Ran 5072 tests in 222.590s
OK
```

로그:

```text
/tmp/census_v40_full_unittest.log
```

주의:

```text
전체 테스트 통과는 v40 감사 필드가 회귀를 만들지 않았다는 뜻이다.
FULL_THESIS 운영 Stage가 실제로 생겼다는 뜻은 아니다.
```

## 6. 현재 진실표

v40 이후에도 현재 진실은 변하지 않는다.

```text
CENSUS_EVENT_BOARD 상태판 Stage:
  존재

FULL_THESIS 운영 Stage row:
  아직 0

FULL_E2R_100 verified score row:
  아직 0
```

v40이 증명한 것:

```text
source-lineage feedback retry의 결과가 readiness에서 숨지 않는다.
bad retry drop과 good retry accepted가 같은 숫자에 섞이지 않는다.
```

v40이 아직 증명하지 않은 것:

```text
accepted claim -> score contribution -> primitive state -> StageCourt -> FULL_THESIS row
```

## 7. 다음 공격 지점

다음 에이전트가 봐야 할 지점:

```text
1. source_lineage_feedback_retry_accepted_execution_count가 실제 output에서 0인지 아닌지.
2. accepted retry가 있더라도 score_contributions / primitive_states / stagecourt_traces까지 이어지는지.
3. no_evidence retry가 많을 때 provider/source pending으로 정직하게 남는지.
4. drop count만 높고 accepted count가 0이면 LLM retry가 source policy를 학습하지 못하는 상태인지.
5. readiness verdict가 accepted retry count를 과장해서 Brain/Web PASS로 만들지 않는지.
```

다음 패치 방향:

```text
source-lineage good retry accepted execution
-> accepted_claims.jsonl
-> score_contributions.jsonl
-> primitive_states.jsonl
-> stagecourt_traces.jsonl
-> census_stage_status.jsonl
```

이 전체 leaf chain을 실제 connector fixture 또는 frozen live snapshot으로 닫아야 한다.
