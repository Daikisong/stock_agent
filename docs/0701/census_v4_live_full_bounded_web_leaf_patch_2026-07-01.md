# Census v4 live_full_bounded Web Leaf Patch - 2026-07-01

이 문서는 `live_full_bounded`가 이름과 달리 실제 web/Naver leaf를 만들지 않던 문제에 대한 1차 코드 패치 기록이다.

## 결론

이번 패치로 바뀐 것:

```text
SourceTask.query_intents
-> target-scoped query 검증
-> bounded web/Naver search
-> page fetch
-> EvidenceDocument / EvidenceAnchor
-> web_search_tasks/results/fetched/rejected leaf
-> Census output export
```

아직 바뀌지 않은 것:

```text
unstructured web/news 원문을 LLM Claim Extractor로 accepted claim까지 만드는 단계
full thesis Stage promotion
Brain/Web evidence pass
Samsung/Hynix C06 full thesis Stage
```

쉬운 예:

```text
이전:
  "배달 포함"이라고 써놓고 실제로는 매장 재고와 snapshot만 봄.

이번 패치:
  LLM이 써준 배달 주소(query_intents)가 회사명/티커를 포함하면 실제 배달 주문(web search)과 물건 도착(fetch) 장부를 남김.

아직 남은 것:
  도착한 물건을 사람이/LLM이 뜯어보고 채점표의 어느 칸에 들어가는지 쓰는 단계.
```

## 구현 파일

```text
src/e2r/research_brain/v4_source_acquisition_runner.py
src/e2r/census/census_runner_v4.py
tests/test_research_brain_v4_real_source_acquisition.py
tests/test_census_v4_brain_bundle_export.py
tests/test_census_v4_run_mode_honesty.py
```

## SourceAcquisitionRunnerV4 변경

`live_full_bounded`의 흐름이 다음처럼 바뀌었다.

```text
1. live official connector 먼저 시도
2. official document가 PARSED면 그대로 사용
3. official 실패 + task가 external web source를 요청하면 web acquisition 실행
4. external web source가 아니면 기존 snapshot fallback 유지
```

새로 추가된 web acquisition 조건:

```text
task.preferred_source_classes / fallback_source_classes 중
NaverSearch, GeneralWebSearch, TrustedNews, News, IndustryMedia, CompanyNewsroom, ReportPDF, BrokerReportPublicPDF
중 하나가 있어야 한다.
```

검색어 생성 원칙:

```text
코드가 검색어를 만들지 않는다.
LLM planner가 만든 task.query_intents만 사용한다.
```

검증 원칙:

```text
query가 회사명 또는 티커를 포함해야 한다.
예: "삼성전자 HBM 고객 배정 qualification" -> 허용
예: "HBM 고객 배정 qualification" -> rejected leaf
```

공식소스 우선 원칙:

```text
contract / backlog / cash / fcf / revision / rpo gap은 Naver/Web fallback으로 바로 보내지 않는다.
```

쉬운 예:

```text
FCF가 비었다
-> 뉴스 검색으로 때우면 안 됨
-> DART/IR/CompanyGuide 같은 공식/구조화 소스가 먼저

고객 qualification 맥락이 비었다
-> LLM query_intents가 회사명 포함 검색어를 제안하면 bounded web search 가능
```

## 새 leaf row

`SourceAcquisitionResultV4`와 `EvidenceOSExecutionBundleV4`에 이미 추가했던 필드를 실제로 채우기 시작했다.

```text
web_search_tasks
web_search_results
web_fetched_documents
web_rejected_documents
```

row 의미:

```text
web_search_tasks:
  검색 주문서. query, provider, max_results, max_fetches, status를 기록.

web_search_results:
  검색 결과. snippet은 follow-up 재료일 뿐 score evidence가 아님.

web_fetched_documents:
  실제 원문 fetch 성공. document_id/anchor_id를 Evidence OS 문서와 연결.

web_rejected_documents:
  회사명 없는 query, future document, fetch 실패, 빈 본문 등을 이유와 함께 기록.
```

## Census Export 변경

`_export_brain_web_bundle_leafs()`가 bundle 내부 web leaf를 아래 파일로 export한다.

```text
web_search_tasks.jsonl       key: web_task_id
web_search_results.jsonl     key: web_result_id
web_fetched_documents.jsonl  key: web_fetch_id
web_rejected_documents.jsonl key: web_rejected_id
```

각 row에는 `source_origin=research_brain_v4_attempt`와 `brain_web_origin=research_brain_v4_attempt`가 붙는다.

이제 다음 에이전트는 "web을 돌렸다"는 말을 report가 아니라 leaf 파일로 검증할 수 있다.

## Web Audit 변경

기존 위험:

```text
web_search_tasks 한 줄만 있어도 REAL_ACQUISITION_PASS처럼 보일 수 있었다.
```

패치 후:

```text
web_fetched_documents > 0
  -> REAL_ACQUISITION_PASS

web_search_results > 0 and fetched == 0
  -> WEB_RESULTS_ONLY_NOT_FETCHED

web_search_tasks > 0 and results == 0 and fetched == 0
  -> WEB_TASKS_ONLY_NOT_FETCHED
```

즉 송장만 있으면 배송 완료가 아니다.

추가 카운트:

```text
web_search_call_count
naver_search_call_count
trusted_news_search_call_count
general_web_search_call_count
web_rejected_document_count
task_only_real_acquisition_pass_allowed: false
```

## 테스트

이번 패치 후 집중 테스트:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_census_v4_brain_bundle_export \
  tests.test_census_v4_run_mode_honesty \
  tests.test_census_v4_brain_web_readiness_gate -v

Ran 37 tests in 25.352s
OK
```

추가 정책 테스트:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_no_unbounded_production_fetch \
  tests.test_research_brain_v4_static_logic_audit \
  tests.test_research_brain_v4_real_planner_provider \
  tests.test_research_brain_v4_provider_failure_pending -v

Ran 6 tests in 0.132s
OK
```

전체 회귀 테스트:

```text
PYTHONPATH=src python -m unittest discover -s tests -v

Ran 4948 tests in 159.060s
OK
```

주의:

```text
이번 전체 테스트는 로컬 명령 결과다.
output/census_v4/2026-07-01/test_result_artifact.json을 새로 재생성한 것은 아니다.
```

검증된 케이스:

```text
1. target-scoped LLM query_intent가 web search/fetch leaf를 만든다.
2. 회사명/티커 없는 query는 search 없이 rejected leaf로 남는다.
3. official-solvable revision gap은 Naver/Web fallback으로 가지 않는다.
4. Brain bundle export가 web_search_tasks/results/fetched JSONL을 쓴다.
5. task-only web audit은 REAL_ACQUISITION_PASS가 아니다.
6. result-only web audit도 REAL_ACQUISITION_PASS가 아니다.
```

## 남은 병목

이 패치만으로 Brain/Web evidence pass가 되지는 않는다.

현재 남은 큰 병목:

```text
1. web/news/IR/report unstructured 원문을 LLM Claim Extractor로 읽는 경로
2. extractor prompt/response leaf
3. extracted RawAssertion -> AdjudicatedClaim -> PrimitiveMapping
4. accepted claim -> score contribution -> StageCourt
5. strict promotion into full_thesis_stage
```

특히 지금 `execute_source_tasks_with_evidence_os_v4()`의 structured extraction은 `anchor.normalized_value["row"]` 중심이다.

따라서 web text document가 fetch되어도:

```text
원문 document/anchor는 생김
하지만 accepted claim은 안 생길 수 있음
```

이 상태에서 낮은 점수나 Stage를 확정하면 안 된다.

정확한 상태명:

```text
web acquisition wiring: partially implemented
web full-source leaf export: implemented
web audit overclaim guard: implemented
LLM unstructured claim extraction: not implemented
Brain/Web evidence pass: not achieved
Full thesis pass: not achieved
```

## 다음 패치

다음 단계는 `LLM Claim Extractor Realness Gate`다.

필수 원칙:

```text
1. Extractor는 score/stage/gap을 보지 않는 contract-blind 입력으로 원문 사실만 뽑는다.
2. LLM 출력의 verified/current_score_eligible/source_tier를 믿지 않는다.
3. quote/span 검증은 코드가 한다.
4. subject/target/temporal/mapping은 별도 단계로 분리한다.
5. accepted claim 없으면 pending이지 낮은 점수 확정이 아니다.
```

완료 조건:

```text
web_fetched_documents row
-> claim_extractor_runs row
-> raw_assertions row
-> adjudicated_claims row
-> accepted or rejected reason
-> score contribution only if accepted and eligible
```

이 조건 전까지는 `live_full_bounded`가 원문을 가져올 수 있게 된 것이지, 아직 full thesis 운영 채점이 끝난 것이 아니다.
