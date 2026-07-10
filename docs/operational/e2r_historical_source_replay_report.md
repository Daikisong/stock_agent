# E2R Historical Source-Backed Replay 보고서

## 결과

- 상태: `HISTORICAL_SOURCE_BACKED_REPLAY_PASS`
- 실제 URL full fetch: 11개 문서, 11,476,353 bytes
- frozen Evidence OS replay: 13개 case
- canary: C06, C08, C15, C17, C24, C28 각각 positive 1개와 guard 1개
- wrong-subject guard: 1개, score 수용 0개
- future leakage: 0개
- source proxy score: 0개

각 READY 행은 URL 문자열만 가진 행이 아니다. 실제 응답의 raw SHA-256, 정규화한 전체 본문의 SHA-256, 게시일·가용일·historical `as_of_date`, 대상 회사 직접성, exact quote와 문자/PDF page locator를 함께 가진다.

쉬운 예: C06 positive는 SK하이닉스 문서에서 고객 공급 계획 문구가 실제 본문에 있는지 확인한다. 반대로 제품 용량이 36GB라는 문구만 있는 C06 guard는 “고객이 장기 물량을 잠갔다”는 증거로 바꾸지 않는다.

## Frozen replay

live fetch 뒤 `output/historical_replay/source_backed_v1/frozen_documents/`에 추출 본문을 고정했다. 이 snapshot을 네트워크 없이 다시 불러와 본문 해시와 quote locator를 재검증했다.

- live source corpus hash: `a1094a67eeed155c37b7dd914317b285dbc27673db6de909586cee965a9b86f0`
- frozen replay source corpus hash: `a1094a67eeed155c37b7dd914317b285dbc27673db6de909586cee965a9b86f0`
- live replay leaf hash: `ff2fb546d619d87a0a6a2f9fc80a63364ff61bd3493e6136bc23094da87c9977`
- frozen replay leaf hash: `ff2fb546d619d87a0a6a2f9fc80a63364ff61bd3493e6136bc23094da87c9977`
- variance: 0

동일 URL을 다시 live fetch하면 사이트 메뉴나 관련 기사 같은 동적 주변 문구가 달라질 수 있다. 이것은 새로운 source corpus다. 동일 historical 판단의 재현성은 이미 고정한 snapshot을 replay해 검증한다.

## Source repair queue

기존 research registry의 URL 보유 행 6,621개는 다음처럼 분리했다.

- `SOURCE_PROXY_ONLY`: 3,428개
- `EVIDENCE_URL_PENDING`: 43개
- `URL_ONLY_WITHOUT_FROZEN_CONTENT_AND_ANCHOR`: 3,150개

이 행들은 URL이 있다는 이유만으로 replay-ready나 score-ready가 되지 않는다. 예를 들어 리포트 링크만 있고 당시 본문 해시와 정확한 표/문장이 없으면 `SOURCE_REPAIR_REQUIRED`다.

## 안전 상태

Historical replay는 current operation 및 current watchlist와 분리되어 있다. 이 Phase는 과거 근거 재생 경로를 닫았다는 뜻이며, 현재 accepted claim이 없는 문제를 해결했다는 뜻은 아니다. 따라서 `production_runtime_ready=false`를 유지한다.

직접적인 투자 권고 문구는 출력하지 않는다.
