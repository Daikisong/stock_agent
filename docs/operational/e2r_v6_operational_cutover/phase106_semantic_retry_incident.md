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

10. **typed-role semantics 교체와 권위 장부 복구 순서가 충돌**

   원인 9를 고친 뒤 권위 장부의 누락 3개 fact를 복구하는 단계가 열렸지만, 복구기는
   현재 v6 semantics의 새 response만 조회했다. 권위 장부의 3개 fact는 직전 v5
   semantics response가 만든 것이고, 새 v6 response는 이를 1개 typed revision fact로
   다시 쓰기 위한 응답이었다. 따라서 복구기의 기대 집합 3개와 새 응답의 집합 1개가
   다를 수밖에 없었다.

   쉬운 예: 구 장부 세 줄을 먼저 복원한 다음 새 회계 양식 한 줄로 대체해야 하는데,
   복원 단계부터 새 양식 영수증을 대입해 “세 줄이 아니다”라고 실패한 상태다.

   수정 후 authoritative recovery는 현재 semantics와 명시적으로 지원되는 직전
   semantics의 immutable Collaboration 영수증을 각각 검증한다. target/date/document,
   정규화·mechanism·objective scope 계약이 모두 같아야 하며, official validator와
   compiler를 다시 통과해 권위 장부의 정확한 claim/fact intersection을 재현하는
   유일한 영수증만 선택한다. 두 영수증이 모두 맞거나 어느 것도 맞지 않으면 계속
   fail-closed한다. 복구가 끝난 다음 clean resume에서만 새 typed-role response를
   소비한다.

11. **직전 semantics 허용 목록과 역사적 prompt/schema 검증기가 불일치**

   원인 10의 복구 후보 목록에는 직전 v5 semantics가 포함됐지만, journal 검증기는
   그 요청을 현재 v6 instruction과 output schema로 다시 생성해 비교했다. v5 요청은
   valuation 역할은 포함하지만 새 `EPS_REVISION`·`OPERATING_PROFIT_REVISION` 역할과
   revision 전용 instruction은 없는 것이 정상이다. 따라서 올바른 과거 영수증이
   prompt/schema hash 불일치로 `INVALID` 처리되고, 복구기는 다시 binding을 찾지
   못했다.

   쉬운 예: 2025년 양식으로 정상 발행된 영수증을 2026년 양식 칸 수와 비교한 뒤
   위조라고 판단한 셈이다. 발행 당시 양식을 재현해서 검증해야 한다.

   수정 후 authority-recovery journal 검증과 실제 semantic replay는 모두 명시적으로
   지원되는 semantics version별 frozen instruction과 schema를 deterministic하게
   재생성한다. 직전 v5는 valuation 역할을 보존하고 revision 두 역할과 revision 전용
   문장만 제거한다. 저장된 prompt를 그대로 믿지 않고 재생성한 prompt/schema/hash와
   exact 비교하며, 그 뒤에도 official response validator와 compiler가 권위 장부의
   정확한 intersection을 재현해야만 복구에 사용한다.

12. **복구 성공과 semantics 교체를 한 checkpoint에서 동시에 적용**

   직전 v5 영수증이 누락 3개를 정확히 재현한 뒤에도 같은 extractor 호출이 해당
   broker PDF를 v6 revision-role 재추출 대상으로 즉시 분류했다. 그 결과 메모리에서는
   3개를 복구했지만 writer 직전 다시 제외되어 67개만 저장됐고, authoritative epoch는
   계속 70개였기 때문에 다음 resume이 같은 3개 복구를 반복했다.

   쉬운 예: 장부 누락 3줄을 복원한 직후 같은 거래에서 새 양식 전환 대상이라는 이유로
   그 3줄을 다시 지우고, 다음 날 또 복원하는 상태다.

   수정 후 authority restoration은 정확한 과거 claim/fact/disposition을 먼저 하나의
   atomic checkpoint로 저장하고 `CANONICAL_STATE_REFRESH_REQUIRED`에서 멈춘다. 그
   checkpoint의 audit에는 다음 clean resume에서 처리할 semantics re-extraction 문서와
   invalidated claim 수를 그대로 남긴다. 다음 resume에서만 v5 3개를 제거하고 이미
   검증된 v6 response를 소비한다. 즉 복구 commit과 교체 commit이 섞이지 않는다.

13. **KRX 종목코드 순서가 forced canary 후보 우선순위가 됨**

   Phase 105의 full-KRX 확장기는 공식 OpenDART 업종 quota가 차는 순간 탐색을
   종료했다. 2026-08-09 실행에서는 2,689개 중 앞쪽 578개만 경량 조회한 뒤
   `QUOTAS_FILLED`가 되었고, 뒤쪽의 별도 상장 직접 사업자는 profile 후보에도
   들어오지 못했다. 업종 quota는 수집 budget일 뿐 사업 적합성 순위가 아닌데,
   종목코드 순서를 사실상 적합성 점수로 사용한 셈이다.

   쉬운 예: 전국 카페를 검증하면서 전화번호부 앞 578개에서 "음식점" quota가
   찼다는 이유로 뒤쪽의 실제 카페는 보지도 않고 첫 복합몰을 고른 것과 같다.

   수정 후에는 점수·Stage·Gold를 전혀 보지 않는 별도 Collaboration shortlist가
   full current KRX issuer roster에서 아키타입별 bounded full-report 후보를 먼저
   고른다. deterministic 코드는 KRX membership, roster order, budget, request/response
   hash, authority=false를 검증하고, shortlist 밖 후보도 fallback discovery pool에서
   제거하지 않는다. 최종 선택은 계속 OpenDART full periodic report의 literal quote와
   compatibility 검증을 통과해야 한다.

14. **별도 상장 자회사 메커니즘을 모회사 직접 사업으로 봉인**

   기존 compatibility schema에는 exact quote와 selected issuer만 있었고, 그 문구의
   실제 사업 주체를 별도로 선언하는 필드가 없었다. 그 결과 `000150 두산` 연결
   보고서 안의 별도 상장 자회사 두산테스나 R&D 표에서 `Socket`을 찾은 뒤, 모회사
   두산을 C08 직접 issuer로 봉인했다. 이후 구조화 재무·valuation은 두산 전사 기준,
   fact/memo는 두산테스나 기준으로 갈라져 `wrong segment`와 missing role이 반복됐다.

   쉬운 예: 쇼핑몰 연결 매출과 입점 카페의 원두 품질을 한 회사의 같은 손익으로
   합산한 것이다. 두 숫자가 모두 사실이어도 평가 대상은 같지 않다.

   수정 후 compatibility response는 `mechanism_owner_target_id`와
   `mechanism_owner_company_name`을 반드시 낸다. deterministic validator는 이 owner가
   selected KRX issuer와 정확히 같을 때만 SELECTED를 허용한다. prompt도 별도 상장
   자회사 메커니즘이면 모회사를 ABSTAIN하도록 명시한다. 이 규칙은 종목명이나 C08에
   한정되지 않고 모든 forced canary에 동일하게 적용한다.

15. **현재 상태 포인터를 영구 영수증처럼 봉인**

   Phase-105의 tracked profile/selection 파일은 이름과 소비 방식상 "현재 선택"
   포인터인데, writer는 영구 영수증과 똑같은 create-only 정책을 썼다. 그래서 owner
   검증 버그를 고쳐 `C08=058470 리노공업`을 COMPLETE로 다시 계산해도, 기존
   `C08=000150 두산` 파일이 존재한다는 이유로 새 결과를 게시할 수 없었다. 뒤 단계는
   계속 낡은 두산 선택을 읽었고, 그 선택에서 생긴 정보 공백을 새 검색 문제로 오판해
   재시도했다.

   쉬운 예: 주소 정정 신청은 승인됐는데, "현재 주소" 칸을 한 번만 쓸 수 있게 만들어
   예전 주소가 계속 배송지로 사용된 것과 같다. 신청 영수증은 불변이어야 하지만 현재
   주소 포인터는 검증된 정정 절차로 바뀔 수 있어야 한다.

   수정 후 historical Collaboration 요청/응답은 그대로 append-only다. tracked current
   profile/selection만 CLI의 명시적 `--replace-current-seal`에서 교체할 수 있다. 교체 시
   기존 파일과 새 파일이 같은 `as_of_date`, COMPLETE/PASS, authority=false인지
   확인하고, symlink/hardlink/동시 변경을 거부한 뒤 원자적 compare-and-swap으로
   게시한다. 기본 실행은 여전히 기존과 같은 create-only라 우발적 덮어쓰기는 불가능하다.

16. **이미 실행한 exact report 경로를 Supervisor가 다시 남은 경로로 선언**

   C08의 LS 2026-07-07 report `1110945 / 1F04720260707_058470.pdf`는 exact
   literal query로 한 번 실행됐고 결과가 0건이었다. 그 다음 query planner는 prior
   query와 failure ledger를 보고 새 verified document identity가 없다고 정직하게
   `LLM_RETURNED_NO_NEW_VALID_QUERY`를 반환했다. 그런데 다음 Supervisor 응답은
   `reasonable_positive_routes_remaining=true`만 남기고 objective-bound source/query
   direction은 0건이었다. 상태기계는 이 빈 `true`를 새 조사 권한으로 읽어
   Supervisor → empty query → Supervisor를 반복했다.

   쉬운 예: 이미 폐점 확인한 매장을 “다른 주소나 담당자 정보 없이 다시 방문”이라고
   작업지시서에 쓰고, 방문 담당자는 중복이라 거절하고, 관리자는 같은 지시를 다시
   내리는 상태다.

   수정 후 `LLM_RETURNED_NO_NEW_VALID_QUERY`가 기록된 snapshot에서 Supervisor가
   routes=true를 유지하려면 concrete missing fact와 연결된 새 source-family direction
   또는 semantic query brief를 반드시 내야 한다. `next_actions`의 자유문장만으로는
   query 권한을 만들 수 없다. deterministic fallback query는 여전히 만들지 않는다.

17. **structured pending을 이유로 닫힌 web-query lane까지 강제 reopen**

   `_supervisor_explicitly_exhausted_source_routes()`는 structured role이 하나라도
   `SOURCE_PENDING`이면 Supervisor의 routes=false를 무조건 무시했다. 그래서 exact
   broker search가 끝났어도 structured gap이 남아 있는 동안 같은 web query lane을
   닫을 방법이 없었다.

   수정 후 query lane 종료와 structured-data 해결을 분리한다. query lane을 닫아도
   missing structured role은 그대로 `SOURCE_PENDING`, `score_valid=false`, StageCourt
   non-final로 남는다. 즉 “같은 검색을 그만한다”를 “사실이 없다”나 “0점”으로 바꾸지
   않는다. 새로운 actionable route가 있거나 retryable fetch/parser repair가 있으면
   기존과 같이 lane을 열어 둔다.

18. **OpenDART 연결재무제표(CFS)만 조회해 별도재무제표(OFS) issuer를 빈 회사로 처리**

   current structured materializer는 모든 issuer·period에 `fs_div=CFS`만 요청했다.
   리노공업의 2026년 1분기는 CFS가 status `013 / 조회된 데이터 없음`이지만 OFS에는
   공식 재무행 89개가 있었다. 그런데 OFS fallback이 없어 revenue, operating profit,
   net income, OCF, CAPEX, FCF 역할이 모두 비었고, 이 structured gap이 원인 16·17의
   query loop를 계속 자극했다.

   쉬운 예: 자회사가 없는 회사에 연결 장부가 없다고 해서, 실제 별도 장부 89줄까지
   없는 것으로 처리한 셈이다.

   수정 후 period마다 bounded official-first 순서 `CFS 1회 → usable row가 없을 때만
   OFS 1회 → 첫 usable statement에서 stop`을 적용한다. CFS와 OFS가 둘 다 있으면 CFS를
   우선하고 중복 합산하지 않는다. cache identity에도 `fs_div`를 포함해 resume 시 서로
   다른 장부가 섞이지 않게 한다.

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
    취급하지 않는다. structured required role이 남으면 score를 확정하지 않는다. 다만
    web-query lane은 objective-bound 새 direction이 있을 때만 다시 열고, 공식 structured
    connector retry는 별도 pending 상태로 유지한다.
11. 새 문서 class를 찾기 전에 이미 fetch된 full document가 missing structured role을
    표현할 수 있는지 schema→fact→materializer→engine 전 경로를 검사한다. 원문이 있는데
    typed role 경로가 없으면 검색 재시도가 아니라 공통 schema 단절을 먼저 수리한다.
12. authoritative fact recovery는 source readiness와 분리한다. exact source identity와
    graph/audit 무결성을 검증한 뒤 사실 장부를 먼저 복구하고, pending query/ranking/fetch
    response는 다음 clean resume에서 소비한다. pending 상태를 identity drift라고 기록하지
    않는다.
13. fact semantics upgrade 중 authority loss가 함께 보이면 새 semantics response로 과거
    장부를 복구하지 않는다. 지원되는 직전 semantics 영수증까지 재검증하고, 권위 epoch의
    exact claim/fact intersection을 유일하게 재현한 영수증으로 구 장부를 먼저 복구한 뒤
    다음 resume에서 새 response를 적용한다.
14. 지원 semantics 목록을 늘릴 때는 버전 문자열만 허용하지 않는다. 각 버전의 frozen
    instruction·output schema·hash를 재생성하는 회귀 테스트를 함께 두고, 현재 builder로
    과거 요청을 검증하지 않는다.
15. authority recovery와 semantics rewrite가 동시에 필요하면 recovery 결과를 먼저
    durable commit하고 canonical refresh barrier를 둔다. 한 호출에서 복구한 행을 다시
    invalidation filter에 넣지 않으며, 다음 rewrite intent는 audit에 보존한다.
16. full-KRX forced discovery에서 입력 순서를 business compatibility 순위로 사용하지
    않는다. score-blind bounded shortlist를 별도 영수증으로 남기고, shortlist 결과는
    full official report 검증 전까지 선택 authority가 아니다.
17. 연결 보고서의 자회사 문구로 issuer를 선택할 때는 실제 mechanism owner를 별도
    필드로 선언·검증한다. 별도 상장 자회사와 selected issuer가 다르면 parent selection을
    fail-closed하며, parent valuation/FCF와 subsidiary mechanism을 섞지 않는다.
18. tracked `current` profile/selection 파일은 기본 create-only를 유지하되, validator
   수리로 같은 기준일의 COMPLETE 결과가 바뀐 경우에만 명시적 compare-and-swap
   교체를 허용한다. 기존·신규 파일의 기준일/완결성/권한 없음과 regular-file
    identity를 모두 검증하며, 과거 Collaboration 영수증 자체는 덮어쓰지 않는다.
19. `reasonable_positive_routes_remaining=true`는 그 자체로 실행계획이 아니다. 직전
    query planner가 `LLM_RETURNED_NO_NEW_VALID_QUERY`를 반환했다면 새 source/query
    direction이 반드시 함께 있어야 하며, 없으면 Supervisor 응답을 fail-closed한다.
20. OpenDART actuals는 period별 CFS 우선, CFS 무자료일 때만 OFS fallback을 수행한다.
    둘 다 없는 경우에만 해당 period를 unavailable로 남기며, 무자료를 0으로 만들지
    않는다.

## Goal 경계

이 수정은 query template, score weight, Stage rule 또는 target-specific branch를 추가하지
않는다. 최종 완료는 오직 `MEANINGFUL_E2R_OPERATIONAL_MARKET_CUTOVER_READY` hard gate가
clean clone과 Reviewer A~V에서 재검산될 때만 선언한다.
