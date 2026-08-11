# Phase 106 semantic retry 반복 사건

## 결론

2026-08-12 Phase 106 실행에서 남은 작업이 계속 늘어난 것처럼 보인 직접 원인은
Goal 범위가 추가된 것이 아니라, `SOURCE_QUERY_GENERATION`의 빈 응답을 소비할
때마다 상태기계가 새 semantic retry leaf를 열었고 운영 진행 보고가 그 leaf 수를
실제 진척으로 잘못 취급했기 때문이다.

이 문서는 반복을 완료 증거로 포장하지 않기 위한 운영 기록이다. 이 기록 자체는
score, Stage 또는 cutover authority가 아니다.

## 관측된 현상

- LLM이 `suggested_queries=[]`를 반환하면 응답 import는 정상 완료됐지만 Source
  Graph는 `QUERY_GENERATION_PENDING`에 남았다.
- 다음 resume은 이전 응답·feedback·prompt/response hash를 넣은 새 request를
  발행했다.
- 그 사이 생성된 component memo 응답은 파일로 존재해도 Source Graph ordering
  boundary가 닫히기 전에는 canonical memo가 될 수 없었다.
- operator는 새 request/response 수를 진척으로 계산했고, 고정 Goal gate가 아닌
  부정확한 완료율을 보고했다.

쉬운 예: 택배 검수대에 상자 하나가 아직 열려 있는데 송장만 세 번 다시 발행된
상태다. 송장 수는 늘었지만 검수가 세 건 끝난 것이 아니다.

## 정확한 원인

1. **의도된 무제한 semantic retry 계약**

   `source_graph_explorer._query_generation_semantic_retry_context()`는 빈 응답,
   중복 query, 미래누수 query를 낮은 점수나 source absence로 바꾸지 않는다.
   deterministic fallback과 fixed retry cap도 금지한다. 따라서 새 유효 query가
   없으면 같은 gap을 더 풍부한 lineage로 LLM에 다시 전달한다.

2. **비동기 collaboration ordering boundary**

   pending query의 `score_gap_context`와 unresolved objective roster는 exact request
   identity를 보존한다. response가 소비되어 Source Graph가 전진하기 전에는 뒤에서
   도착한 memo·judge를 먼저 canonical로 섞을 수 없다. 이는 서로 다른 evidence
   snapshot 혼합을 막는 정상 보호벽이다.

3. **지나치게 보수적인 query 판단**

   반복된 LLM 응답은 이미 정확한 URL·문서 ID가 prompt에 없다는 이유로 새 source
   class 탐색까지 포기하고 빈 답을 냈다. LLM의 역할은 URL을 미리 아는 것이 아니라
   현재 evidence와 failure ledger에서 중복되지 않는 검증 가능한 문서 class를
   제안하는 것이다. 예를 들어 기존 회사 뉴스 검색과 다른 인증기관 registry·기한
   있는 인증서 경로는 합법적인 새 route다.

4. **운영 보고 오류**

   canonical `until_pass`를 다시 실행하면서 생성된 leaf를 모두 필요한 잔여 작업으로
   설명했다. Phase 106의 고정 합격 조건인 `5 targets`, `7/7`, `material_gap=0`,
   `score_valid=true`, `StageCourt=FINAL` 중 몇 개가 닫혔는지를 보고했어야 했다.

5. **종료된 search lineage가 계속 reopen authority를 보유**

   terminal query에서 accepted fact가 나오지 않으면
   `source_query_lineage_gap_objectives`가 그 objective를 계속 미해결로 표시했다.
   canonical Supervisor가 `reasonable_positive_routes_remaining=false`, source
   direction 0건, retryable fetch/parser repair 0건이라고 판정한 뒤에도 이 과거
   lineage가 더 높은 우선순위로 남아 query generation을 다시 열었다. 그 결과
   Supervisor가 요구한 “현재 evidence로 memo를 다시 쓰고 새 judges를 실행”하는
   downstream 작업이 시작되지 못했다.

   수정 후에는 exact collaboration response가 먼저 journal에 들어간 뒤,
   Supervisor의 route-exhaustion snapshot이 과거 semantic retry의 reopen authority만
   제거한다. 실패 query와 material0 기록은 감사 ledger에 그대로 남고 source
   absence로 승격되지 않는다. 구체적인 source direction이나 retryable fetch/parser
   failure가 하나라도 있으면 이 종료 규칙은 적용되지 않는다.

6. **memo rewrite 중간 scaffold가 직전 Supervisor 판정을 가림**

   source lane을 한 번 닫은 뒤 `information_confidence` memo를 다시 쓰면, 새 memo에
   맞는 judges와 synthesis가 아직 없다는 뜻의 `RSUP-PENDING` checkpoint가 먼저
   저장된다. 이 객체의 `reasonable_positive_routes_remaining=true`는 안전한 pending
   기본값이지 LLM Supervisor의 새 판단이 아니다. 그런데 source planning이 이 값을
   그대로 읽으면서 직전의 서명된 `routes=false` 판정을 잃고 query를 다시 열었다.

   쉬운 예: “추가 배송 없음”이라는 서명된 지시서가 있는데 새 검토서의 서명이 아직
   안 끝났다는 이유로 임시 빈 양식의 기본값 “배송 가능”을 실행한 셈이다.

   수정 후 source routing만 append-only `research_epochs.jsonl`에서 checkpoint id/hash와
   nested schema가 검증된 가장 최근의 non-`RSUP-PENDING` Supervisor 판정을 사용한다.
   현재 pending checkpoint는 readiness·score·Stage에서 계속 pending으로 남는다. 즉,
   과거 판정으로 점수를 확정하지 않고 임시 scaffold가 새 검색 권한을 발명하는 것만
   막는다. 실제 C08 clean resume에서 Source Graph가
   `QUERY_GENERATION_PENDING`에서 `EPOCH_COMPLETE_REQUIRES_SUPERVISOR`로 전진하고 pending
   replay context가 제거되는 것을 확인했다.

7. **semantic route 종료가 별도 structured source gap까지 가림**

   Supervisor의 `routes=false`는 당시 semantic fact gap에 대한 판단이다. 그런데 C08의
   CompanyGuide consensus page는 `as_of_date` 뒤에 갱신된 mutable page라 point-in-time
   validator가 올바르게 거절했고, `FORWARD_PB`, `FORWARD_EV_EBITDA`, revision 등
   structured role은 계속 `SOURCE_PENDING`이었다. semantic route 종료를 전체 source
   종료로 적용하면 이 provider/source gap이 낮은 점수나 영구 pending으로 굳는다.

   수정 후 `prior_structured_source_gap.status=SOURCE_PENDING`이고 required role이 남아
   있으면 Supervisor의 semantic route 종료가 LLM source planning을 덮지 않는다.
   deterministic 코드는 검색어를 만들지 않고, LLM이 full broker PDF 같은 대체 문서
   class를 제안할 권한만 유지한다.

8. **원문을 확보해도 revision 역할을 저장할 수 없는 schema 단절**

   C08은 유진투자증권의 2026-05-11 full PDF를 실제 fetch했고, 원문에는
   `영업이익(26E) 현재 1,771 / 직전 1,719 / ▲`처럼 현 추정치와 직전 추정치가 함께
   있었다. 그러나 `EvidenceFact`와 collaboration output schema는
   `OPERATING_PROFIT_REVISION` 및 `EPS_REVISION`을 허용하지 않았고, structured
   materializer도 이 fact를 consensus revision record로 승격하는 경로가 없었다.
   따라서 검색을 더 반복해도 이미 확보한 정답을 structured gap에 연결할 수 없었다.

   쉬운 예: 창고에 정식 세금계산서가 도착했는데 전산 입력 화면에 “수정 전 금액”과
   “수정 후 금액” 칸이 없어서 계속 새 계산서만 찾던 상태다.

   수정 후에는 target/sector 조건 없이 두 revision 역할을 공통 fact schema에
   추가했다. 다만 숫자 하나만 있는 전망표는 revision으로 인정하지 않는다. dated
   full broker PDF, metric 이름, 수정 신호, 수정 전·후의 서로 다른 두 숫자, forward
   period, exact quote가 모두 있어야 한다. `1,771십억원`은 엔진에서 KRW
   1.771조원으로 정규화하되, 원문 숫자 1,771과 변환 결과를 함께 검증한다. semantics
   version 변경은 `PUBLIC_BROKER_PDF`만 선택 재추출하고 무관한 공시 수백 건은 다시
   열지 않는다.

9. **권위 사실 장부 복구와 source readiness를 같은 조건으로 판정**

   revision 역할 추가 후 과거 research epoch의 권위 장부에는 70개 fact가 있었지만,
   편의 스냅샷에는 67개만 남아 canonical rematerialization이 필요했다. 동시에 새
   ranking collaboration response가 아직 Source Graph에 소비되지 않아 checkpoint는
   `CANDIDATE_RANKING_PENDING`이었다. 기존 readonly hydration은 target/date/checkpoint
   id/hash가 모두 정확히 같아도 이 pending 상태를 identity drift로 잘못 분류했다.

   쉬운 예: 서명된 재고 장부 70줄을 복구해야 하는데 새 입고 검수표가 대기 중이라는
   이유로 “장부 자체가 다른 장부”라고 거절한 상태다. 올바른 순서는 정확한 장부
   스냅샷을 고정해 누락 3줄을 먼저 복구하고, 다음 clean resume에서 검수표를 소비하는
   것이다.

   수정 후 authoritative fact recovery는 source 작업이 terminal인지와 무관하게 exact
   target/date/checkpoint id/hash를 먼저 고정한다. 이어 기존과 동일하게 source graph
   재생성, persisted audit binding, safety critical count를 검증하므로 손상된 checkpoint를
   허용하지 않는다. 일반 readonly replay의 terminal 조건은 그대로 유지한다.

## 데이터 무결성 판단

- 빈 query response는 score/Stage authority가 아니었다.
- same-snapshot query 결과를 supervisor나 memo에 선반영하지 않았다.
- uncommitted memo를 current memo라고 간주하지 않았다.
- source absence를 zero result나 nonmaterial candidate만으로 선언하지 않았다.

따라서 이 사건은 점수 데이터 변조가 아니라 orchestration 및 진행 보고 실패다.

## 재발 방지 계약

1. retry/epoch/receipt 개수로 완료율을 계산하지 않는다.
2. 매 resume 전 현재 고정 Goal gate와 정확히 어떤 semantic state가 변하는지 확인한다.
3. empty response의 다음 LLM call에는 전체 prior semantic lineage를 넣되, 이미 실행한
   query의 동의어는 금지한다.
4. 미리 알려진 URL이 없다는 이유만으로 empty를 강제하지 않는다. target-scoped이며
   검증 가능한 새 document class가 있으면 LLM이 제안한다.
5. Source Graph가 pending이면 뒤에서 도착한 memo·judge는 response ledger에만 두고
   canonical 소비 전에는 완료로 보고하지 않는다.
6. supervisor가 source route가 아니라 semantic memo rewrite를 요구하면 해당 memo와
   memo-bound judge를 다시 만들고, 이를 새 source fact로 가장하지 않는다.
7. 진행 보고는 다음 고정 증거만 사용한다.

   - Phase 106 current live canary 5/5
   - 각 target component memo 7/7
   - material gap 0
   - score valid
   - deterministic StageCourt FINAL
   - provider error 0
   - tracked receipt 및 independent post-run review
8. `reasonable_positive_routes_remaining=false`는 source absence나 saturation 인증이
   아니다. search lane만 닫고 memo rewrite·judge·saturation·score gate는 그대로
   실행한다.
9. `RSUP-PENDING`은 source direction이 아니다. source routing은 마지막으로 검증된
   provider Supervisor 판정을 유지하되, readiness와 점수 계산은 현재 pending 상태를
   그대로 사용한다.
10. semantic source route 종료와 structured provider/source gap 종료를 같은 boolean으로
    취급하지 않는다. structured required role이 남으면 score를 확정하지 않고 LLM 대체
    source route를 다시 열어야 한다.
11. 새 문서 class를 찾기 전에 이미 fetch된 full document가 missing structured role을
    표현할 수 있는지 schema→fact→materializer→engine 전 경로를 검사한다. 원문이 있는데
    typed role 경로가 없으면 검색 재시도가 아니라 공통 schema 단절을 먼저 수리한다.
12. authoritative fact recovery는 source readiness와 분리한다. exact source identity와
    graph/audit 무결성을 검증한 뒤 사실 장부를 먼저 복구하고, pending query/ranking/fetch
    response는 다음 clean resume에서 소비한다. pending 상태를 identity drift라고 기록하지
    않는다.

## Goal 경계

이 수정은 query template, score weight, Stage rule 또는 target-specific branch를 추가하지
않는다. 최종 완료는 오직 `MEANINGFUL_E2R_OPERATIONAL_MARKET_CUTOVER_READY` hard gate가
clean clone과 Reviewer A~V에서 재검산될 때만 선언한다.
