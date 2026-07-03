# Census v4 0701 v37 Source Lineage Retry Drop Leaf Audit Patch

작성일: 2026-07-02 KST

## 0. 결론

v37은 운영 Stage를 새로 만든 패치가 아니다.

v37은 v36에서 차단한 retry task가 조용히 사라지는 문제를 막는 패치다.

```text
v36:
  source_lineage_unverified_original feedback 이후
  NaverSearch / GeneralWeb / IndustryMedia / News / Web 같은
  discovery-only retry task를 실행하지 않음

v37:
  실행하지 않은 retry task도
  REJECTED_BY_POLICY source_task_execution으로 leaf artifact에 남김
```

쉬운 예:

```text
1차 시도:
  네이버 검색으로 HBM 뉴스 발견
  -> 원문 lineage 미검증이라 reject

retry planner:
  또 NaverSearch + IndustryMedia만 제안

v36:
  실행하지 않고 버림

v37:
  실행하지 않지만 source_task_executions.jsonl에
  "왜 버렸는지" row를 남김
```

이 패치 후에도 현재 운영 truth는 그대로다.

```text
CENSUS_EVENT_BOARD 상태판 Stage는 있다.
FULL_THESIS 운영 Stage는 아직 0개다.
FULL_E2R_100 verified score row도 아직 0개다.
```

## 1. 왜 필요한가

goal 문서의 핵심은 report 문구가 아니라 leaf artifact로 증명하라는 것이다.

따라서 실행하지 않은 task도 운영적으로 중요하면 leaf에 남아야 한다.

```text
조용히 사라지는 bad retry:
  다음 에이전트가 "LLM이 뭘 냈는지", "왜 멈췄는지" 확인 불가

leaf에 남는 bad retry:
  source task
  source task execution
  rejection reason
  zero budget
  stop reason
  reason_from_memory
  모두 감사 가능
```

이건 점수를 만들기 위한 패치가 아니다.
오히려 잘못된 retry를 점수로 만들지 않으면서도, 그 실패를 숨기지 않는 패치다.

## 2. 코드 변경

수정 파일:

```text
src/e2r/research_brain/v4_production_orchestrator.py
tests/test_research_brain_v4_operational_modes.py
tests/test_census_v4_brain_bundle_export.py
docs/0701/README.md
docs/0701/census_v4_0701_v37_source_lineage_retry_drop_leaf_audit_patch_2026-07-02.md
```

### 2.1 retry filter가 rejected execution도 반환

기존 호환 helper:

```text
_deduplicated_feedback_retry_tasks(...)
  -> kept SourceTask만 반환
```

새 내부 helper:

```text
_deduplicated_feedback_retry_tasks_with_rejections(...)
  -> kept SourceTask
  -> rejected SourceTaskExecutionV4
```

기존 테스트/호출자가 깨지지 않도록 기존 helper는 유지했다.

### 2.2 드롭 execution schema

드롭된 retry는 다음 형태로 남는다.

```text
status = REJECTED_BY_POLICY
provider_name = research_brain_v4_retry_policy
source_task_origin = feedback_retry
budget_used = {"queries": 0, "candidates": 0, "fetches": 0}
stop_reason = source_lineage_retry_discovery_only_after_unverified_original
not_eligible_reasons =
  source_lineage_retry_discovery_only_after_unverified_original
provider_errors =
  source_lineage_retry_discovery_only_after_unverified_original
```

source task의 reason_from_memory에는 다음이 붙는다.

```text
feedback_retry:source_lineage_unverified_original
dropped:source_lineage_retry_discovery_only_after_unverified_original
```

### 2.3 bundle에 append

retry task가 모두 드롭되어 실제 fetch가 없더라도,
기존 bundle에 드롭 execution을 append한다.

```text
bundle.executions += dropped_retry_executions
bundle.extraction_audit.source_lineage_feedback_retry_dropped_count += dropped_count
```

따라서 Census v4 exporter가 기존 경로로 leaf를 만든다.

```text
source_task_executions.jsonl
source_tasks.jsonl
```

## 3. 하드코딩이 아닌 이유

이 패치는 검색어를 만들지 않는다.

코드가 판단하는 것은 하나다.

```text
source_lineage_unverified_original feedback 이후에
retry source task가 또 discovery-only source class만 가지고 있는가?
```

나쁜 방식:

```text
if symbol == "005930":
  force IR query
```

이번 방식:

```text
LLM이 만든 task를 보고
source class가 원문 검증 가능 route인지 정책 검증
```

query 내용이 "삼성전자 HBM 고객 배정 기사"인지,
"SK하이닉스 HBM IR 원문"인지는 deterministic code가 만들지 않는다.

## 4. 테스트

타깃 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_source_lineage_feedback_retry_drop_has_auditable_execution_row \
  tests.test_census_v4_brain_bundle_export.CensusV4BrainBundleExportTests.test_brain_bundle_exports_source_lineage_retry_drop_execution -v
```

결과:

```text
Ran 2 tests
OK
```

관련 모듈 테스트:

```bash
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_operational_modes -v
```

결과:

```text
Ran 46 tests
OK
```

```bash
PYTHONPATH=src python -m unittest tests.test_census_v4_brain_bundle_export -v
```

결과:

```text
Ran 8 tests
OK
```

확장 교차검증:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_brain_bundle_export \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_run_mode_honesty -v
```

결과:

```text
Ran 133 tests in 42.317s
OK
```

## 5. 검증된 동작

### 5.1 retry drop execution row

테스트가 확인한 값:

```text
status = REJECTED_BY_POLICY
provider_name = research_brain_v4_retry_policy
budget_used = {"queries": 0, "candidates": 0, "fetches": 0}
stop_reason = source_lineage_retry_discovery_only_after_unverified_original
not_eligible_reasons includes source_lineage_retry_discovery_only_after_unverified_original
source_task.reason_from_memory includes feedback_retry:source_lineage_unverified_original
source_task.reason_from_memory includes dropped:source_lineage_retry_discovery_only_after_unverified_original
```

### 5.2 Census leaf export

테스트가 확인한 값:

```text
source_task_execution_exported_count = 1
source_task_exported_count = 1
source_task_executions.jsonl row status = REJECTED_BY_POLICY
source_task_executions.jsonl row provider_name = research_brain_v4_retry_policy
source_task_executions.jsonl row stop_reason = source_lineage_retry_discovery_only_after_unverified_original
source_tasks.jsonl row reason_from_memory includes dropped:source_lineage_retry_discovery_only_after_unverified_original
```

즉 다음 에이전트는 source_task_executions leaf만 봐도:

```text
LLM이 retry를 냈다.
하지만 source lineage feedback 이후 같은 discovery-only route라 실행하지 않았다.
실행 budget은 0이었다.
낮은 점수나 Red로 확정하지 않았다.
```

를 확인할 수 있다.

## 6. 남은 문제

v37은 운영 성공 패치가 아니다.

아직 남은 큰 문제:

```text
1. actual TrustedNews / ReportPDF / CompanyNewsroom connector는 아직 충분히 닫히지 않았다.
2. Brain/Web enabled run에서 web_or_llm accepted claim은 아직 0개다.
3. FULL_THESIS production row는 아직 0개다.
4. 삼성전자/하이닉스 C06 production FULL_THESIS path는 아직 source-backed live path로 닫히지 않았다.
5. dropped retry audit은 남지만, 좋은 retry를 실제 원문 claim으로 성공시키는 것은 다음 패치다.
```

## 7. 다음 패치 방향

### P0. dropped retry audit을 canonical audit에도 집계

v37은 `source_task_executions.jsonl`에 row를 남긴다.
다음에는 `brain_web_readiness_gate_audit.json` 또는 별도 audit에 아래 count를 명시해야 한다.

```text
source_lineage_feedback_retry_dropped_count
discovery_only_retry_after_unverified_original_count
```

### P1. original-capable source connector 실제화

다음 source class를 실제 원문 fetch/lineage 검증까지 닫아야 한다.

```text
CompanyNewsroom
ReportPDF
BrokerReportPublicPDF
TrustedNews original URL
IR
KIND/DART web-discovered detail
```

### P2. good retry가 accepted claim으로 이어지는 positive test

필요한 positive chain:

```text
source_lineage_unverified_original feedback
  -> LLM retry proposes CompanyNewsroom/ReportPDF
  -> source fetch succeeds
  -> EvidenceAnchor
  -> accepted_claim
  -> primitive_state
  -> score_contribution
  -> StageCourt trace
```

## 8. 최종 판정

v37 이후 상태:

```text
나쁜 retry 반복:
  차단됨

차단된 retry의 leaf audit:
  source_task_executions.jsonl / source_tasks.jsonl에 남음

운영 FULL_THESIS Stage:
  아직 0개
```

따라서 이 패치는 목표에 필요한 감사 가능성을 한 단계 올렸지만,
전체 goal 완료는 아니다.

## 9. 교차검증: Stage가 있긴 한가

현재 `docs/operational/census_mode_v4_acceptance_report.md` 기준으로 Stage row는 있다.
다만 전부 `CENSUS_EVENT_BOARD` scope다.

```text
eligible rows = 3391
stage rows = 3391

base/display stage distribution:
  Stage0 = 3306
  Stage1 = 54
  Stage2-Watch = 30
  Red = 1

stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3391

operator_stage_use_distribution:
  NOT_FULL_THESIS_STAGE = 3391

FULL_THESIS stage rows = 0
FULL_E2R verified score rows = 0
event-board non-Stage0 rows = 85
```

쉬운 예:

```text
CENSUS_EVENT_BOARD Stage:
  "이 종목은 이번 전체지도에서 확인했고, 현재 이벤트가 있거나 없다"는 상태판

FULL_THESIS Stage:
  "이 종목의 투자 논문이 claim-backed score와 StageCourt를 통과했다"는 운영 판정
```

따라서 "Stage가 있긴 하냐"의 답은 둘로 나뉜다.

```text
상태판 Stage:
  있음. 3391개.

운영 FULL_THESIS Stage:
  없음. 0개.
```

이 구분을 흐리면 다시 같은 문제가 생긴다.

```text
나쁜 표현:
  Stage2-Watch가 30개 있으니 운영 Stage가 나온다.

정확한 표현:
  CENSUS_EVENT_BOARD의 Stage2-Watch가 30개 있다.
  하지만 FULL_THESIS 운영 Stage는 아직 0개다.
```

## 10. 교차검증: Brain/Web와 FULL_THESIS 상태

현재 canonical ledger refresh artifact는 Brain/Web을 요청한 실행이 아니다.

`docs/operational/census_mode_v4_brain_web_readiness_gate_audit.json`:

```text
run_mode = LEDGER_REFRESH_CENSUS
verdict = NOT_REQUESTED
brain_web_mode = disabled
llm_planner_call_count = 0
llm_claim_extractor_attempt_count = 0
web_search_task_count = 0
web_fetched_document_count = 0
web_or_llm_accepted_claim_count = 0
brain_promoted_stage_row_count = 0
```

`docs/operational/census_mode_v4_full_thesis_production_runner_audit.json`:

```text
production_mode_requested = false
candidate_row_count = 0
promoted_full_thesis_row_count = 0
verdict = NOT_REQUESTED
```

따라서 v37이 증명한 것은 다음이 아니다.

```text
Brain/Web 운영 성공
FULL_THESIS 운영 Stage 생성
삼성전자/하이닉스 live C06 운영 판정 완료
```

v37이 증명한 것은 다음 하나다.

```text
source_lineage_unverified_original 이후
discovery-only retry가 실행 전 차단되면
그 차단도 leaf artifact에 남는다.
```

## 11. 리뷰어가 공격해야 할 지점

다음 에이전트는 이 패치를 통과로만 보지 말고 아래를 공격적으로 확인해야 한다.

```text
1. REJECTED_BY_POLICY row가 source_task_executions.jsonl에 실제 export되는가
2. 같은 row가 source_tasks.jsonl에도 task 단위로 추적되는가
3. budget_used가 0이라서 실제 fetch로 오해되지 않는가
4. retry drop이 낮은 score / Red / FULL_THESIS failure로 둔갑하지 않는가
5. discovery-only source class 판정이 종목명이나 검색어 하드코딩이 아닌가
6. original-capable source class는 과도하게 차단하지 않는가
7. source_lineage_feedback_retry_dropped_count가 bundle audit에 남는가
8. canonical readiness audit에도 이 count가 들어가야 하는지 남은 작업으로 추적되는가
```

현재 답:

```text
1~7은 v37 코드와 테스트로 확인됨.
8은 아직 남은 작업이다.
```

## 12. 반박 예상과 답

### 반박 A: 이건 또 하드코딩 아닌가

답:

```text
종목명, 아키타입명, 검색어를 만들지 않는다.
LLM이 낸 SourceTask의 source class만 정책 검증한다.
```

나쁜 하드코딩 예:

```text
if symbol == "005930":
  NaverSearch 차단
```

v37 방식:

```text
if previous_feedback == source_lineage_unverified_original
and retry source class가 NaverSearch/GeneralWeb/News만 있음
and 원문 검증 가능한 CompanyNewsroom/ReportPDF/TrustedNews/DART/IR 등이 없음:
  실행하지 않고 REJECTED_BY_POLICY row로 남김
```

### 반박 B: 그럼 좋은 retry도 막히는가

답:

```text
CompanyNewsroom / ReportPDF / BrokerReportPublicPDF / TrustedNews /
DART / IR / IssuerOfficial / KIND / KRX 같은 original-capable class가 있으면 유지한다.
```

테스트:

```text
test_source_lineage_feedback_retry_keeps_original_capable_source_task
```

### 반박 C: 이 패치로 Stage가 만들어졌는가

답:

```text
아니다.
Stage 생성 패치가 아니라 실패 감사 패치다.
FULL_THESIS rows는 여전히 0개다.
```

## 13. 추가 검증 결과

v37 적용 후 전체 테스트도 다시 돌렸다.

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5069 tests in 205.543s
OK
```

주의:

```text
이 full suite 결과는 수동 로컬 검증 결과다.
docs/operational/census_mode_v4_acceptance_report.md 안의
machine-readable test artifact count는 이전 runner artifact 기준으로 남아 있다.
따라서 operational acceptance report 자체를 새로 생성했다는 뜻은 아니다.
```

## 14. 다음 패치의 정확한 목표

다음 패치는 더 이상 "나쁜 retry를 숨기지 않기"가 아니라
"좋은 retry가 실제 source-backed claim으로 닫히기"여야 한다.

필수 chain:

```text
1. source_lineage_unverified_original feedback 발생
2. LLM이 CompanyNewsroom / ReportPDF / TrustedNews original / DART detail 같은 retry를 제안
3. Source Router가 bounded budget 안에서 실제 원문을 fetch
4. EvidenceDocument 생성
5. EvidenceAnchor 생성
6. Contract-blind extractor가 raw assertion 생성
7. adjudicator가 target/direct/current/polarity를 통과
8. primitive mapper가 accepted mapping 생성
9. primitive state가 PRESENT_CURRENT 또는 명확한 상태로 갱신
10. score contribution이 support_claim_id를 가진다
11. StageCourt trace가 생긴다
12. FULL_THESIS candidate가 production scope로 promotion될 수 있는지 gate가 판단
```

중간에 하나라도 빠지면 낮은 score나 Red로 확정하지 않고,
`Source Pending` 또는 `PENDING_MATERIAL_GAPS`로 남겨야 한다.
