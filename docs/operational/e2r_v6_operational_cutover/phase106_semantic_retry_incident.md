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

19. **1분기 QoQ를 요구하면서 직전 4분기를 만드는 데 필요한 3분기 누적값을 안 가져옴**

   `QOQ_GROWTH`는 현재 분기와 바로 전 분기를 비교해야 한다. 그런데 기준일의 최신
   실적이 2026년 1분기일 때 materializer는 2025년 연간값만 가져오고 2025년 3분기
   누적값은 가져오지 않았다. 따라서 `2025 Q4 = 2025 연간 - 2025 Q3 누적`이라는
   공식 숫자끼리의 계산을 할 수 없었고, QoQ가 영원히 비어 있었다.

   쉬운 예: 1년 총매출과 9개월 누적매출이 있으면 마지막 3개월 매출은 뺄셈으로
   구할 수 있다. 그런데 9개월 장부를 아예 요청하지 않았던 것이다.

   수정 후 latest period가 Q1이면 전년도 Q3를 bounded supplemental period로 한 번
   가져온다. 같은 official statement에서 annual minus Q3 cumulative로 sales, operating
   profit, net income, OCF, CAPEX, FCF의 Q4를 계산한다. 파생값은 `DERIVED_Q4_FROM_ANNUAL_MINUS_Q3`
   로 명시하며 어느 한쪽이 없으면 만들지 않는다. Q3 balance sheet는 `FY2025Q3`로
   identity를 분리해 연간 `FY2025` 행과 충돌하지 않게 했다.

20. **사업부 공시에 금액이 함께 있다는 이유로 유일한 매출비중까지 버림**

   리노공업의 공식 표는 `639억원; 64.10%; 수출 596억원; 내수 43억원`처럼 금액과
   비중을 함께 적는다. generic numeric parser는 여러 숫자가 있다는 이유로 전체를
   거절했고 `SEGMENT_CONTRIBUTION`이 비었다.

   쉬운 예: “사과 매출 639원, 전체의 64.10%”에서 요구값이 비중임이 분명한데,
   숫자가 둘이라는 이유로 둘 다 버린 셈이다.

   수정 후 이 역할에만 좁은 parser를 쓴다. 정확한 `%` 토큰이 하나일 때만 그 비중을
   받으며, `수출 78.62%; 내수 10.13%`처럼 퍼센트가 둘이면 계속 거절한다. LLM이
   역할을 지정하고 exact quote를 제시해야 한다는 경계는 바꾸지 않는다.

21. **공식 공시에 선행 투자계획·상각비가 있는데 typed structured role이 없어 재검색**

   full fetched KIND/OpenDART 문서에는 2026-11-10까지의 971.82억원 공장 투자계획과
   과거 기간 감가·무형자산상각비가 있었다. 하지만 fact output schema에는 실제 상각비
   역할이 없었고, 향후 CAPEX 계획이 `FORWARD_GUIDANCE`에 해당한다는 설명도 불충분했다.
   원문을 갖고도 engine 입력으로 전달하지 못해 broker 검색을 다시 열었다.

   수정 후 fact semantics를 v7으로 올려 LLM이 기존 full document를 다시 읽게 한다.
   issuer-owned numeric future operating/capacity/capital plan은 `FORWARD_GUIDANCE`, 이미
   끝난 기간의 단일 상각비 숫자는 `LATEST_ACTUAL_DEPRECIATION_AMORTIZATION`으로만
   제안할 수 있다. deterministic validator는 source family, exact quote, 숫자, 기간,
   lifecycle을 다시 검증한다. 상각비는 EBITDA를 직접 주장하지 않고, actual operating
   margin과 actual D&A margin을 유지한 명시적 deterministic scenario에만 들어간다.

22. **공식 자본과 scenario 순이익으로 계산 가능한 forward book/PB도 provider 값만 기다림**

   engine은 이미 actual trend로 forward EPS/FCF scenario를 만들면서도, 같은 경계에서
   book value를 만들지 않았다. 그래서 공식 actual equity와 projected net income이
   있어도 `FORWARD_BOOK_VALUE`와 `FORWARD_PB`가 provider pending으로 남았다.

   수정 후 base/bear/bull scenario에 `latest reported equity + projected net income`을
   shares로 나눈 book value per share를 추가한다. 배당과 OCI는 0으로 고정했다는 가정을
   metadata에 적고 confidence 0.65의 `DETERMINISTIC_SCENARIO`로 유지한다. 이는 관측된
   미래값이나 consensus가 아니며, 최종 점수는 계속 deterministic engine이 계산한다.

23. **v7 의미 버전 전환이 과거 v6 프롬프트 문구를 정확히 복원하지 못해 사실 42건을 분실로 오판**

   v7은 새 D&A 역할만 추가한 것이 아니라 `FORWARD_GUIDANCE` 설명과 바로 뒤의
   `Tags` 문장도 바꿨다. authority recovery는 v6 JSON payload와 output schema가 정확히
   같아도, 현재 v7 문구에서 D&A 문장만 제거해 만든 prompt hash를 과거 v6 hash와
   비교했다. 그 결과 실제로 존재하는 v6 공식 영수증 다섯 묶음을 모두 invalid로
   처리하고, 권위 epoch의 사실 42건이 사라진 것처럼
   `CURRENT_FACT_LINEAGE_RECOVERY_BINDING_REQUIRED`에 멈췄다.

   쉬운 예: 장부의 숫자와 서명은 그대로인데 새 양식의 안내문 한 줄이 다르다는 이유로
   과거 장부 전체를 위조로 판정한 셈이다.

   수정 후 v7에서 v6을 복원할 때 enum뿐 아니라 v7에서 추가·변경된 모든 안내문을
   제거·복원한다. 과거 v6 instruction의 SHA-256을 회귀 테스트로 고정해, 이후 문구를
   바꿀 때 새 버전의 frozen builder를 함께 만들지 않으면 테스트가 실패한다. 저장된
   request/response 자체의 hash·schema·provider·Codex provenance 검증은 그대로 유지한다.

24. **복구할 과거 사실과 이미 커밋된 새 사실이 함께 있으면 안전장치가 둘 다 거부**

   원인 23을 고친 뒤 과거 v6 영수증은 42개 누락 사실을 정확히 재현했다. 하지만 그
   전에 v7 full-document 응답에서 미래 배당계획 사실 1개가 이미 durable checkpoint에
   저장됐다. 편의 스냅샷은 `기존 29 + 새 v7 1 = 30`, 권위 epoch는 기존 71개였으므로
   필요한 최종 집합은 `권위 71 + 새 v7 1 = 72`였다. 기존 장부 코드는 “권위 손실”과
   “다음 epoch 대기 사실”이 동시에 보이면 무조건
   `MIXED_AUTHORITY_LOSS_AND_PENDING_NEW_FACTS_BLOCKED`로 중단했다.

   더 까다로운 점은 누락 42개 중 8개와 새 사실 1개가 같은 공식 문서에서 나왔다는
   것이다. 과거 disposition과 최신 v7 disposition을 단순히 이어 붙이면 같은 문서가
   두 번 처리된 것처럼 되어 또 fail-closed했다.

   쉬운 예: 원장 71줄 중 42줄이 복사본에서 빠진 사이 새 거래 1줄이 정상 기입됐다.
   정답은 원장 71줄을 복원하고 새 거래 1줄을 보존하는 72줄이다. 그런데 기존 코드는
   “복원할 줄과 새 줄이 동시에 있다”는 이유만으로 장부 전체를 거부했고, 같은 영수증의
   과거 검수도 최신 검수와 중복으로 셌다.

   수정 후 mixed 상태는 별도
   `AUTHORITY_LOSS_RECOVERY_WITH_PENDING_NEW_REQUIRED` 전이로 처리한다. 새 fact id/body/
   source는 committed result와 compiler replay로 이미 증명된 경우만 허용하고, 과거
   영수증은 권위 장부의 정확한 누락 교집합만 복원한다. 최종 fact 집합은
   `authority ∪ attested pending-new`와 byte-equivalent여야 한다. 같은 문서가 겹치면
   과거 claim은 복구하되 top-level disposition은 최신 v7 행 하나만 유지한다. 결과는
   atomic writer로 먼저 저장하고 canonical-refresh barrier에서 멈춘 뒤 다음 clean
   resume에서만 남은 semantics 작업을 계속한다. 새 행이 projection에 없거나 출처·본문이
   다르면 기존처럼 provider 호출 없이 fail-closed한다.

25. **복구 직후 의미 재추출이 끝나기 전에 기존 사실을 먼저 지워 다시 복구 루프로 진입**

   원인 24의 `71 + 새 사실 1 = 72` atomic 복구는 실제로 성공했다. 그러나 다음 clean
   resume에서 boundary-context 의미 재추출을 시작할 때, 4개 문서 전체의 새 응답이
   끝나기 전에 과거 provider call의 사실 34개를 top-level checkpoint에서 먼저
   제거했다. 첫 문서의 새 page response는 아직 전체 교체가 아니었으므로 편의
   스냅샷은 다시 38개로 줄었고, append-only epoch 권위는 71개였다. 다음 실행은 이
   의도적 중간 상태를 실제 authority loss로 판정해 같은 34개를 다시 복구했다.

   쉬운 예: 장부 72줄을 복구한 뒤 4장짜리 교체 서류를 작성하면서, 1장만 쓴 시점에
   기존 34줄을 먼저 지웠다. 다음 담당자는 지워진 34줄을 분실로 보고 되살렸고,
   시스템은 `복구 → 먼저 삭제 → 다시 복구`를 반복했다.

   수정 후 boundary-context 재추출은 선택된 document/call closure 전체가 current
   semantics로 끝날 때까지 하나의 replacement transaction으로 취급한다. 부분 완료
   page의 새 claims는 exact provider-call receipt 안에만 보관해 resume에 사용하고,
   top-level claims/dispositions/facts에는 과거 baseline을 그대로 유지한다. 모든 문서가
   끝난 한 시점에만 새 projection으로 원자 교체한다. 그때 사라진 과거 fact는
   `pending_retired_fact_ids`로 별도 attestation한다. 즉 result-last snapshot, current
   semantics dispositions, Collaboration provider receipts, official journal lineage,
   source roster가 모두 맞을 때만 의도적 retirement로 인정하고, 그 외 축소는 계속
   authority loss로 fail-closed한다.

26. **공식 원문의 반증 사실도 반드시 별도 반증 검색을 거쳐야 한다는 교착**

   의미 재추출과 judge 합성이 끝난 뒤에도 Supervisor의
   `counter_route_proof_complete`가 false로 남았다. 기존 증명기는
   `반증 query의 양수 검색 결과 → full document → extractor → COUNTER/RESOLUTION fact`
   계보만 인정했다. 이미 fetch·parse된 공식 공시에서 모든 component의 반증·해소 fact를
   확보했어도, 그 문서가 `counter_or_supersession_search=true` query를 통해 들어오지
   않았으면 무시했다. 반대로 남은 반증 검색이 0건으로 끝나면 0건을 absence나 증명으로
   쓸 수 없으므로, `빈 검색 → counter 미완료 → 다시 검색`에서 빠져나올 수 없었다.

   쉬운 예: 감사보고서에 “고객 집중 위험”이 명시돼 있고 exact quote까지 검증했는데,
   그 보고서를 “위험 검색” 버튼으로 찾지 않았다는 이유로 위험 검토를 안 했다고 판정한
   셈이다. 이후 위험 검색 결과가 0건이어도 기존 공식 문서는 계속 무시됐다.

   수정 후 두 증명 경로를 명시적으로 분리한다. 검색으로 얻은 반증은 종전처럼 양수
   result의 query→document→fact 계보를 전부 요구한다. 이미 보유한 공식/full document의
   반증은 `DIRECT_SOURCE_BACKED_FACT`로 표시하고, objective→deterministic component,
   document objective, `FACTS_EXTRACTED` disposition, fact source,
   `allowed_component_ids`, COUNTER/RESOLUTION lifecycle이 모두 exact 일치할 때만 인정한다.
   0건 검색, snippet, 비적격 문서, component가 다른 fact는 어느 경로에서도 증명이
   아니다. 따라서 검색 실패를 source absence로 과장하지 않으면서도, 더 강한 공식
   반증을 검색 운송 계보가 없다는 이유로 버리지 않는다.

27. **완료된 제한사항을 material gap으로 다시 적어 만든 출구 없는 상태**

   direct 공식 반증 증명까지 연결한 실제 재개에서 Supervisor는 7개 메모 충분,
   structured 완료, counter/supersession 완료, 추가 합법 경로 없음이라는 네 상태를
   모두 `true/true/true/false`로 정확히 냈다. 그런데 이미 점수 상단을 제한하는 데
   반영한 고객·마진·CAPA 공개 공백과 다음 정기공시 점검 항목을 다시
   `missing_material_facts`와 `unresolved_material_questions`에 넣고 readiness만 false로
   냈다. 기존 validator는 ready일 때 gap이 없는지는 검사했지만, 반대 방향인
   “모든 gate 완료 + 실행할 route 없음 + blocking gap 있음” 모순은 거부하지 않았다.

   쉬운 예: 졸업시험을 모두 통과했고 재시험 과목도 없다고 판정한 뒤, “졸업 후에도
   실력을 계속 점검해야 한다”는 이유로 졸업만 영구 보류한 셈이다. 점검 항목은
   monitoring이지 지금 수행 가능한 보충시험이 아니다.

   수정 후 `missing_material_facts`가 있는 component는 반드시
   `memo_sufficient=false`여야 한다. 또한 component·structured·red-team·counter proof와
   failure 상태가 모두 완료되고 provider가 actionable route도 없다고 판정했다면,
   gap/unresolved blocking field를 남길 수 없다. 실제로 새 자료를 찾을 합법적 route가
   있다면 objective-bound direction과 함께 memo를 불충분으로 열고, 없다면 그 제한은
   rationale의 monitoring/counterweight로만 보존하고 readiness를 true로 맞춘다.

28. **수정 전 저장된 모순 판정이 수정 후에도 7개 메모를 먼저 재개방**

   원인 27의 validator를 고친 뒤에도 이미 append-only epoch에 저장된 과거 판정은
   사라지지 않았다. 현재 checkpoint가 synthesis pending scaffold가 되자 source routing은
   직전 non-scaffold 판정을 찾아 썼고, 그 과거 판정의 `missing_material_facts` 7건이
   새 validator에 도달하기도 전에 7개 `COMPONENT_RESEARCH` 요청으로 변환됐다. 새
   validator는 새 Supervisor 응답만 검사하므로 이미 저장된 모순의 파생 작업을 막지
   못했다.

   쉬운 예: 잘못 작성된 보충수업 지시서를 고치는 규칙은 만들었지만, 이미 배부된
   지시서가 출석부에 먼저 반영돼 학생 7명을 다시 수업에 등록한 상태다. 정답은 7개
   수업을 진행하는 것이 아니라, 옛 지시서의 등록 권한을 정지하고 교무실이 새 양식으로
   한 번 재판정하게 하는 것이다.

   수정 후 호환 복구기는 `memos=true`, `structured=true`, `counter=true`,
   `routes=false`인데 monitoring gap 때문에 `ready=false`인 구 판정만 일반 규칙으로
   식별한다. append-only 원문과 failure ledger는 보존하지만 component/source routing용
   projection에서는 그 gap·finding을 제거한다. readiness를 임의로 true로 바꾸거나
   score/Stage를 확정하지 않고, 현재 Supervisor가 강화된 validator로 정확히 한 번
   재판정해야만 다음 단계가 열린다. 종목명·아키타입·문구 키워드 조건은 사용하지 않는다.

29. **terminal receipt가 append-only 과거 요청까지 현재 provider error로 계산**

   C08의 현재 연구·saturation·Stage mapping이 모두 끝난 뒤에도 compact receipt는 journal
   전체의 `request_count == response_count`를 요구했다. 원인 28에서 실행 권한을 잃은
   과거 요청과 정식 quarantine된 교정 전 응답까지 현재 실패로 합산했기 때문에, 정확한
   현재 결과가 있어도 receipt를 만들 수 없었다.

   쉬운 예: 현재 월 장부는 모두 결재됐는데, 취소된 과거 신청서에 승인 도장이 없다는
   이유로 이번 달 결산을 거부한 셈이다. 취소 신청서를 몰래 승인하는 것이 아니라,
   취소·미응답 이력을 보존하고 현재 결산에 쓰인 서류가 모두 완료됐는지를 봐야 한다.

   수정 후 journal은 invalid request/response, orphan, quarantine envelope·reason receipt,
   active response와 quarantine의 동시 존재, request/response/pending 수식을 별도로
   검증한다. 과거 미응답·quarantine은 terminal score, FINAL Stage, saturation certificate,
   material gap 0이 이미 exact이고 이번 실행의 logical call 전부가 성공했을 때만 non-active
   history로 허용한다. terminal 전이나 이번 실행에 실패 call이 있으면 같은 미응답은 계속
   hard pending이다. 이를 provider success로 세거나 score/Stage authority로 사용하지 않는다.
   교정 전 저장된 audit에 새 분리 필드가 없으면 숫자를 역산하지 않는다. 실제 immutable
   journal을 새 validator로 다시 읽고, 기존 audit의 request/response/pending/quarantine
   count와 전부 일치할 때만 새 분리 필드를 보충한다.

30. **compact receipt가 같은 계보의 두 표현과 counter view를 결함으로 오판**

   Evidence OS claim은 검증된 추출 호출을 `FACTPROMPT-*`/`FACTRESP-*` 안정 ID로
   보존하지만 compact receipt는 실제 transport의 64자리 prompt/payload hash를 요구했다.
   또 `evidence_facts.jsonl`은 모든 방향의 canonical ledger이고 `counterfacts.jsonl`은 그중
   COUNTER 행을 그대로 반복하는 materialized view인데, projector는 이 동일 행도 duplicate
   identity 오류로 처리했다.

   쉬운 예: 같은 결제에 주문번호와 카드 승인번호가 둘 다 있는데 주문번호가 카드 승인번호
   형식이 아니라고 결제를 거부했고, 전체 거래장과 환불 거래장에 같은 환불 행이 보인다고
   이중 결제로 오해한 셈이다.

   수정 후 안정 ID는 검증된 Collaboration request/response envelope와 다시 결속해 실제
   64자리 hash를 가져온다. 동일 fact ID가 두 view에 있으면 byte-equivalent semantic row만
   한 fact로 합치며, 내용이 조금이라도 다르면 계속 fail-closed한다.

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
21. latest actual이 Q1이면 전년도 Q3 누적을 bounded로 가져와 annual-minus-Q3 Q4를
    계산한다. balance sheet period identity는 annual과 quarter를 구분한다.
22. multi-number segment claim은 `SEGMENT_CONTRIBUTION`의 explicit percent가 정확히
    하나일 때만 허용하며, 두 개 이상이면 deterministic 선택을 하지 않는다.
23. 이미 full-fetch한 공식 문서가 새 typed role을 공급할 수 있으면 fact semantics를
    버전업해 해당 source family만 재추출한다. 검색 query를 대신 만들지 않는다.
24. deterministic scenario에서 만든 book value·EBITDA는 observed/consensus로 표시하지
    않고 formula, input lineage, 가정을 metadata에 남긴다.
25. fact semantics 버전업은 JSON schema뿐 아니라 instruction 전문을 버전별 frozen
    hash로 재생성해야 한다. 현재 문구로 과거 prompt를 재생성해 비교하지 않는다.
26. 권위 손실과 pending-new fact가 함께 있어도 둘 중 하나를 버리지 않는다. 단,
    pending-new fact id/body/source가 committed snapshot과 compiler replay에 exact attested되고,
    historical journal이 권위 누락 집합을 유일하게 재현할 때만 atomic union recovery를
    허용한다. 같은 문서의 disposition은 최신 committed 행 하나만 남기고, 복구된 과거
    claim과 immutable journal receipt는 보존한다.
27. semantics replacement는 페이지·문서별 부분 결과를 canonical fact projection에
    노출하지 않는다. 선택된 call/document closure 전체가 완료될 때까지 baseline fact를
    유지하고, 완료 후 사라진 fact는 exact `pending_retired_fact_ids` attestation으로만
    epoch 대기 projection에 반영한다. 단순히 convenience snapshot에서 fact가 없다는
    이유만으로 retirement를 추정하지 않는다.
28. counter/supersession 완료는 검색 transport 자체가 아니라 검증된 반증 증거의
    계보를 확인한다. query 기반 경로는 양수 검색 결과를 계속 요구한다. direct 공식
    경로는 objective/component/document/fact 결속을 모두 검증하며, zero-result나
    provider error를 완료 또는 source absence로 바꾸지 않는다.
29. `component_memos_sufficient=true`인 component에 `missing_material_facts`를 동시에
    둘 수 없다. 모든 비검색 gate가 완료되고 `reasonable_positive_routes_remaining=false`
    이면 monitoring 문구를 blocking gap으로 재분류하지 않는다. material gap이라면
    memo를 다시 열고 실행 가능한 LLM-owned route를 제시해야 하며, 그렇지 않으면
    Supervisor correction retry가 gap을 monitoring rationale로 이동하고 readiness를
    완료 상태와 일치시킨다.

30. validator 강화 전에 저장된 모순 Supervisor review는 append-only 감사 기록에서
    삭제하거나 현재 완료로 승격하지 않는다. 대신 모든 비검색 gate 완료, actionable
    route 0, retryable repair 0이라는 구조적 조건이 exact할 때만 과거 review의 routing
    authority를 일시 정지한다. 이 호환 projection은 component rewrite와 source query를
    열 수 없고, 새 Supervisor validation 한 건만 허용한다.
31. terminal provider accounting은 immutable journal의 모든 과거 request에 응답을
    강요하지 않는다. 대신 현재 terminal boundary가 먼저 성립해야 하고, active response,
    unresolved historical request, validated quarantine가 request roster를 exact 분할해야
    한다. current-run logical/successful call 수도 exact해야 한다. quarantine envelope와
    reason receipt가 하나라도 손상되거나 count가 맞지 않으면 fail-closed한다.
32. compact fact lineage는 `FACTPROMPT`/`FACTRESP`를 임의 hash 변환하지 않는다.
    검증된 fact provider-call receipt가 품은 exact Collaboration envelope에서 full
    prompt/payload hash를 복구해야 한다. canonical evidence ledger와 counter-only view의
    동일 행은 한 번만 세되, same-ID content drift는 거부한다.

## Goal 경계

이 수정은 query template, score weight, Stage rule 또는 target-specific branch를 추가하지
않는다. 최종 완료는 오직 `MEANINGFUL_E2R_OPERATIONAL_MARKET_CUTOVER_READY` hard gate가
clean clone과 Reviewer A~V에서 재검산될 때만 선언한다.
