# E2R Pro-First V2 P9 라이브 검증 진행 장부

기준 시각: `2026-08-24 20:32 KST`

작업 브랜치: `feature/e2r-pro-first-browser-platform-20260822`

기록 직전 HEAD: `7865714866a3bd957c8153423e82ef6e27fb803a`

PR: Draft PR #7, 병합·draft 해제·auto-merge를 수행하지 않음

이 문서는 P8 이후의 실제 라이브 실행, 발견된 결함, 코드 수정, 테스트, 아직 남은
작업을 외부 검수자가 한 번에 추적할 수 있도록 기록한다. 이 시점은 P9 진행 중이며
`FULL_THESIS_READY` 또는 production-ready 완료를 주장하지 않는다.

## 1. 현재 한 줄 상태

```text
000660 initial/gap/gap/counter 4개 pass 완료
→ effective dossier 97 facts / 28 questions / 98 routes
→ source verifier v8: 43 accepted
→ verifier rejection 46개
→ 17개 첫 bounded repair pass가 같은 Pro 대화에서 RESEARCH_RUNNING
→ 나머지 29개는 다음 batch로 이월 대기
```

현재 full-thesis score, canonical Stage, publication 권한은 모두 없다.

## 2. 라이브 scope와 재현 식별자

| 필드 | 값 |
| --- | --- |
| target | `000660 / SK하이닉스` |
| archetype | `C06_HBM_MEMORY_CUSTOMER_CAPACITY` |
| as_of_date | `2026-08-23` |
| job | `PROJOB-cdd91020f15891533e61431f` |
| run | `PRORUN-a7dacadb7088fc23535bfdde` |
| canonical conversation | `6a8b09c3-bfcc-83ee-b15b-9f76eca52249` |
| effective snapshot | `PRODOSSIERSNAPSHOT-2c8a29d511db4f97ffb922b3` |
| effective dossier hash | `fee5aebe...` |
| runtime root | `C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\live_v2\20260823T145430Z` |

runtime root에는 ChatGPT 응답 원문과 fetched documents가 포함될 수 있어 Git에 복제하지
않는다. 대신 코드, schema, prompt contract, 테스트, 상태·해시·count 영수증을 PR에
추적한다. 외부 검수자는 위 식별자로 로컬 runtime과 Git 변경을 대조할 수 있다.

## 3. append-only pass 장부

| ordinal | pass id | pass name | status | submit_count | 설명 |
| ---: | --- | --- | --- | ---: | --- |
| 1 | `PROPASS-e2fba20afb08b81db0d4d6d6` | `INITIAL_FULL_RESEARCH` | `COMPLETE` | 1 | 최초 Pro full research |
| 2 | `PROPASS-6f6edd56e3a877f9265c032c` | `PUBLIC_GAP_CLOSURE` | `COMPLETE` | 1 | 공개 material gap 보충 1 |
| 3 | `PROPASS-b806a55651acd4e6dfbf87bf` | `PUBLIC_GAP_CLOSURE` | `COMPLETE` | 1 | 공개 material gap 보충 2 |
| 4 | `PROPASS-ab2d8bd7520a8ce7de71f306` | `COUNTER_SUPERSESSION_CLOSURE` | `COMPLETE` | 1 | counter·supersession 감사 |
| 5 | `PROPASS-7694a86ac9e996eeabd03394` | `VERIFIER_REPAIR` | `TRANSPORT_PENDING` | 0 | 51.8만 자 prompt가 visible composer transport 한도를 초과, 미전송 보존 |
| 6 | `PROPASS-3ef919d661d3bfa39f201c4e` | `VERIFIER_REPAIR` | `RESEARCH_RUNNING` | 1 | 첫 bounded repair batch 17개 |

pass 5는 실패한 연구 답변이 아니라 실제 제출 전 transport 계획이다. 삭제하거나
`COMPLETE`로 바꾸지 않았고, `submit_count=0`, `prepared_at=null`, `submitted_at=null`을
보존했다. pass 6만 별도 prompt/input hash와 exactly-once claim으로 1회 제출됐다.

## 4. dossier 누적 결과

pass 4까지 실제 merge 결과는 다음과 같다.

```text
material facts      50
counterfacts        15
resolution facts    32
total facts         97
question families   28
route receipts      98
```

pass 4 compact 응답은 새 fact `MF047~MF050`과 prior fact를 연결하는 resolution
relationship를 반환했다. 초기 adapter는 current delta 안의 fact만 anchor로 인정해 prior
fact reference를 거절했다. 이를 다음처럼 고쳤다.

- prior dossier가 exact job/run/conversation/target/as_of/parent pass와 일치할 때만 prior
  fact를 관계 anchor로 허용한다.
- prior source URL, publisher, published_at, supporting excerpt는 byte-for-byte 유지한다.
- source lineage identity는 바꿀 수 없고 URL/fact/publisher/reprint roster만 append한다.
- 다른 question의 route reference는 해당 question canonical row에서 제거하되 raw
  cross-reference는 diagnostics에 남긴다.
- latest hash-bound effective snapshot을 재개 시 직접 읽어 initial dossier 재병합을 막는다.

쉬운 예: 새 응답이 `기존 사실 MF003을 새 공시가 보강한다`고 쓰면 MF003을 새 fact로
다시 만들지 않는다. exact prior snapshot의 MF003을 확인한 뒤 relationship만 append한다.

## 5. source verifier 진단과 교정

같은 97개 candidate에 대한 verifier 변화는 다음과 같다.

| semantics | accepted | 의미 |
| --- | ---: | --- |
| v6 | 0/97 | economic subject label에 회사명 문자열을 강제한 결함 |
| v7 | 5/97 | issuer alias/date/file hash 교정 후 일부 복구 |
| v8 | 43/97 | closed-enum semantic scope mapper와 deterministic validator 연결 |

v8에서도 score와 Stage는 LLM이 정하지 않는다.

```text
Codex scope mapper
→ natural-language segment/product/mechanism을 closed enum으로만 매핑
→ exact quote/date/target은 deterministic verifier가 검사
→ component credit은 MechanismScopeValidator가 결정
→ score_authority=false / stage_authority=false
```

함께 수정한 generic verifier 결함:

- `subject`는 회사명 복사가 아니라 경제적 대상 label일 수 있다.
- issuer publisher/domain에서 한국어·영문 issuer alias를 scope 제한하에 얻는다.
- 명시된 과거 published date가 있으면 미래 HTTP `Last-Modified`가 이를 덮어쓰지 않는다.
- Windows text file을 `newline=""`으로 읽어 검증한 content hash와 실제 bytes를 맞춘다.
- question binding이 없는 auxiliary rejection은 diagnostics로만 남기고 repair question을
  발명하지 않는다.

## 6. verifier repair transport batching

v8 이후 question-bound material rejection은 46개였다. 최초 prompt payload는 약
51.8만 자로 실제 ChatGPT composer가 처리하지 못했다. 해당 pass는 제출 전이었으므로
중복 연구는 발생하지 않았다.

새 규칙:

```text
pending rejection packets 전체 compile
→ canonical 순서에서 prompt payload 210,000자 이하 prefix 선택
→ selected packet만 같은 대화에 제출
→ 응답을 전체 dossier에 append/withdraw
→ deterministic verifier를 전체 dossier에 재실행
→ 남은 packet을 다음 pass로 다시 계획
```

첫 batch receipt:

```text
pending               46
selected              17
deferred              29
payload chars         200,334
payload budget        210,000
transport batching    true
publication withheld  true
```

`repair/rejection_packets.jsonl`에는 현재 선택 batch, 별도
`repair/pending_rejection_packets.jsonl`에는 선택 전 전체 pending roster를 기록한다.
receipt에도 selected/deferred packet id를 모두 기록하므로 packet이 조용히 사라질 수 없다.

## 7. 브라우저 안전 사고와 재발 방지

이 작업 중 한 차례 OS 전역 키 입력 방식이 잘못된 window focus를 받아 다른 terminal에
문자열을 입력한 사고가 있었다. 해당 방식은 즉시 폐기했다.

현재 강제 규칙:

- OS 전역 keyboard automation 금지
- clipboard automation 금지
- window focus 전환 자동화 금지
- E2R 격리 Chrome의 exact page CDP/DOM만 사용
- `Chat + Pro`만 허용하고 legacy Deep Research를 대체재로 사용하지 않음
- send 전에 DB prompt hash·job/pass/parent/conversation marker 확인
- send는 durable `submit_count 0→1` claim 뒤 한 경로에서만 클릭

초대형 미전송 prompt 때문에 동일 conversation 탭 하나가 renderer-level로 고착됐다.
복구 시 두 탭의 exact URL과 CDP target id를 확인했고, 정상 탭은 보존하고 응답하지 않는
중복 탭 하나만 닫았다. conversation 삭제, cookie 복사, hidden ChatGPT API, 다른 탭 입력은
없었다. 정상 canonical 대화에 다시 붙은 뒤 첫 bounded repair가 시작됐다.

large prompt adapter 회귀시험은 50만 자 이상 원문과 줄바꿈을 editor-local DOM에 보존하고
submit 0회를 검증한다. actual repair에서는 이 기능에만 기대지 않고 payload batching도
동시에 적용한다.

## 8. 현재 테스트 증거

### Windows Playwright — 실제 live와 같은 runtime

```text
tests.test_e2r_pro_first_browser_adapter
25 tests / OK

tests.test_e2r_pro_first_approval_submit
8 tests / OK
```

이 중 50만 자 이상 prompt 보존·submit 0회, 승인 이전 send 차단, exactly-once submit,
canonical conversation rebind 감사 테스트가 포함된다.

### Linux deterministic focused suites

```text
source verification
dossier status/dialect
live runtime resume/hash binding
verifier repair/batching

73 tests / OK
```

추가로 state machine 13개, frozen replay·saturation·prompt compiler 41개가 통과했다.

추가 transport budget 시험 2개도 통과했다.

```text
기존 bounded follow-up count 유지
submit_count=0 TRANSPORT_PENDING 계획은 실제 follow-up 예산을 소비하지 않음
```

WSL Playwright 전체 실행은 코드 오류가 아니라 local headless Chromium의 `libnspr4.so`
부재로 시작 자체가 실패했다. 같은 테스트를 실제 운영 runtime인 Windows
Python/Playwright에서 실행해 25/25를 확인했다.

Windows approval suite의 첫 실행은 assertion이 아니라 임시 SQLite 파일 cleanup에서
열린 handle 7개를 발견했다. 조회 경로가 `sqlite3.Connection` context manager의 commit은
사용하면서 close까지 된다고 잘못 가정한 generic 결함이었다. `ProFirstJobStore`의 조회
connection 21곳을 `contextlib.closing`으로 명시 종료하도록 고쳤고, Linux state machine
13/13과 Windows approval/submit 8/8을 다시 통과했다.

## 9. 이번 커밋에 포함되는 핵심 변경

- Pro compact/full dossier dialect adapter와 exact prior-snapshot anchoring
- append-only source lineage·route ownership·resolution merge
- latest effective snapshot resume와 verification artifact hash binding
- 실제 Windows Codex structured provider transport 호환
- source verifier v8 semantic scope mapping 및 generic subject/date/hash 교정
- question-bound verifier repair만 계획하는 규칙
- repair prompt payload batching과 deferred roster 영수증
- ChatGPT large composer DOM 입력 및 50만 자 회귀시험
- P9 live canary CLI·recovery·progress receipt 기반
- read-only SQLite connection 명시 종료와 Windows cleanup 회귀 확인
- frozen V1 replay와 old diagnostic 의미 보존

## 10. 아직 남은 작업

다음 순서를 모두 완료하기 전 Goal 완료를 선언하지 않는다.

1. 현재 17개 repair 응답 capture/import/reverify
2. deferred 29개와 재검증 후 남은 rejection을 bounded repair pass로 0까지 처리
3. 000660 mandatory questions terminal, public material gap 0, repair pending 0 확인
4. saturation audit pass와 deterministic 7 component / 21 Judge / score / StageCourt 실행
5. `011170 / C17` live canary 완료
6. `053800 / C28` live canary 완료
7. 서로 다른 3개 mechanism canary receipt와 no hidden authority 검증
8. full unit test, Phase100, production static audit, forbidden path audit
9. 최종 P9/P10 receipt·운영 문서·Draft PR 상태 갱신

현재 blocker는 없다. 외부 Pro 연구 시간이 진행 중일 뿐이며, timeout limit 도달은
`COMPLETE`가 아니라 `TRANSPORT_PENDING / score_valid=false`로 남는다.

## 11. 외부 검수 체크리스트

- pass 5의 `submit_count=0`과 pass 6의 `submit_count=1`이 분리돼 있는가
- deferred 29개 packet id가 receipt와 pending JSONL 양쪽에 남는가
- prior fact anchor가 exact job/run/conversation/as_of/target/parent snapshot을 요구하는가
- accepted prior fact와 source lineage identity를 repair가 삭제·재결박할 수 없는가
- scope mapper가 score/Stage를 직접 결정하지 않는가
- verifier repair가 끝나기 전 component/scoring/publication gate가 열리지 않는가
- 다른 종목·다른 as_of_date에 현재 approval scope를 재사용할 수 없는가
- 브라우저 입력이 exact E2R page DOM/CDP에만 한정되는가
