# E2R Pro-First V2 P9 라이브 검증 진행 장부

기준 시각: `2026-08-24 22:18 KST`

작업 브랜치: `feature/e2r-pro-first-browser-platform-20260822`

기록 직전 HEAD: `b793f620130c0bb6bdf8670dc352a38103855283`

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
→ 17개 첫 bounded repair pass의 Pro 생성·capture 원자 완료
→ raw MD와 종료 marker 1자만 복구한 normalized MD를 모두 append-only 보존
→ Pro 응답: 새 fact 17 / repair 제안 17(NARROWED 13, REPLACED 4)
→ dialect adapter가 실행 register를 비워 0건 처리한 원인 확인·코드 교정
→ 14개 candidate의 multi-question packet과 Pro 단일 question row 불일치가 다음 blocker
→ 기존 no-op snapshot은 덮어쓰지 않고 append-only revision 재처리 대기
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
| 6 | `PROPASS-3ef919d661d3bfa39f201c4e` | `VERIFIER_REPAIR` | `COMPLETE` | 1 | 동일 응답을 재전송하지 않고 raw/normalized capture 완료. repair 적용 revision은 아직 대기 |

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

`2026-08-24 12:47:35Z`에 같은 visible 응답을 중복 전송 없이 원자 capture했다. durable
pass는 `COMPLETE / submit_count=1`이며 raw MD, normalized MD, parsed dossier, capture
receipt, READY를 같은 incoming bundle에 기록했다. 수동으로 DB 상태를 바꾸거나 같은
prompt를 다시 제출하지 않았다.

`repair/rejection_packets.jsonl`에는 현재 선택 batch, 별도
`repair/pending_rejection_packets.jsonl`에는 선택 전 전체 pending roster를 기록한다.
receipt에도 selected/deferred packet id를 모두 기록하므로 packet이 조용히 사라질 수 없다.

## 7. 첫 repair 응답 capture 복구와 다음 import blocker

입력·클릭·다운로드 없이 canonical conversation DOM을 읽어 다음을 확인했다.

| 검사 | 결과 |
| --- | --- |
| assistant turn | `2be36aa2-e447-4460-8814-af29af0e733f` |
| visible 본문 길이 | 68,788자 |
| exact job marker | 1개 |
| exact run marker | 1개 |
| exact pass marker | 1개 |
| exact parent marker | 1개 |
| `E2R_RESEARCH_DOSSIER_JSON_BEGIN` | 1개 |
| `E2R_RESEARCH_DOSSIER_JSON_END` | 0개 |
| 실제 visible 종료 문자열 | `E2R_RESEARCH_DOSSIER_SON_END` 1개 |

즉 Pro 연구가 비었거나 사실을 0개 반환한 상태가 아니었다. 본문 끝의 정상 종료 문자열
`JSON_END`에서 `J` 한 글자가 빠진 `SON_END`였고, 기존 completion monitor가 exact
`BEGIN/END` 쌍을 요구해 보수적으로 대기했던 것이다.

쉬운 예: 택배 상자와 내용물, 송장번호는 모두 맞지만 봉인 스티커 글자 하나가 깨져 있어
자동 입고기가 멈춘 상태다. 상자를 다시 주문하는 것이 아니라, 현재 상자가 exact
job/run/pass/parent scope인지 확인한 뒤 내용물을 검증해 입고해야 한다.

화면에 보이는 MD 버튼은 초기 응답 turn
`263c5818-5bb0-4a31-9a0f-f31a24a5adcb`에 속한
`E2R_SKHynix_2026-08-23_full_response.md`이며, 이번 repair turn의 새 첨부로 오인하지
않는다. 이번 repair의 근거는 마지막 assistant turn에 직접 보이는 68,788자 본문이다.

복구 결과:

| 항목 | 값 |
| --- | --- |
| capture source | `DIRECT_REPORT_DOM_NORMALIZED` |
| raw report hash | `89603d1d9e2c9458817959befcc4c8940662006575a136e851f007c3417632c2` |
| normalized report hash | `73ec0b51ec7630c56de500a4fa80280c9d28a39464482fdb71a38a6e4c140349` |
| normalization | `...SON_END → ...JSON_END` 단일 삭제 문자 복구 1건 |
| raw response facts | material 9 / counter 5 / resolution 3 = 17 |
| raw repair proposals | `NARROWED 13 / REPLACED 4` = 17 |
| normalized adapter validation | 17 facts / 10 lineages / 17 routes / schema PASS |
| automatic resubmit | `false` |

복구 코드는 임의 typo를 고치는 범용 퍼지가 아니다. exact begin marker가 하나 있고 정상
end marker가 없으며, 한 글자 삭제 후보가 정확히 하나이고, 그 사이가 JSON object로
strict parse될 때만 허용한다. 두 글자 이상 손상이나 invalid JSON은 계속 실패한다.
`pro_report.raw.md`와 `pro_report.md`를 둘 다 보존하고 receipt가 두 hash와 operation을
검증하므로 원문을 숨기지 않는다.

capture 뒤 첫 import가 0건이 된 원인도 확인했다.

```text
Pro 응답 verification_repair_register 17건
→ compact dialect adapter가 전부 diagnostics로 복사
→ 실행용 verification_repair_register=[] 강제
→ repair delta actions 0
→ unresolved 17 / no-op effective snapshot 생성
```

이는 Pro가 자료를 못 가져온 것이 아니라 adapter가 자료의 실행 연결을 버린 결함이다.
현재 코드는 `VERIFIER_REPAIR` pass에서 candidate/question/category/action/replacement ID가
모두 허용 형식인 row만 실행 register에도 보존한다. 그래도 Pro의 판단을 바로 채택하지
않고 exact rejection packet 결박과 deterministic source reverification을 계속 요구한다.

실제 응답을 수정 코드에 넣은 read-only 검증은 다음까지 통과했다.

```text
adapter/schema validation       PASS
response facts                  17
scoped repair proposals         17
NARROWED / REPLACED             13 / 4
source lineages / routes        10 / 17
```

다음 blocker는 parser가 아니라 packet scope 계약이다. 17개 중 14개 rejection packet은
원래 candidate가 2~6개 question에 연결돼 있지만 Pro register는 대표 question 한 개만
기록했다. 현재 strict delta builder는 exact question set을 요구하므로 이를 그대로
통과시키지 않았다.

쉬운 예: 원래 반려 fact 하나가 질문 A·B·C에 걸려 있는데 Pro가 “A를 고쳤다”는 row 하나만
보냈다. A의 수정을 B·C까지 자동 승인하면 안 된다. candidate-level repair를 A·B·C의
deterministic 재검증 입력으로 확장할지, 나머지를 pending으로 둘지 generic 정책과
회귀시험을 먼저 고정해야 한다.

첫 0건 적용으로 생성된 아래 파일도 감사 증거라 삭제·덮어쓰기하지 않는다.

```text
snapshot id       PRODOSSIERSNAPSHOT-374eb7b04d924c725676a390
dossier hash      6802144873d3fbec2bbb17bafd009feadd5d46213183103eed7f408e16da6acb
facts/routes      97 / 98
repair receipt    resolutions 0 / unresolved 17
score_valid       false
publication       withheld
```

교정된 pass 6 재처리는 exact parent인 pass 4 snapshot에서 시작해 별도 revision artifact와
새 hash를 append해야 한다. 기존 pass 6 `effective_dossier.json`이나 capture bundle을
제자리 수정하면 안 된다.

안전한 후속 원칙:

- 같은 pass를 재전송하지 않는다. durable `submit_count=1`을 유지한다.
- exact conversation과 assistant turn의 현재 본문만 capture 대상으로 삼는다.
- job/run/pass/parent marker와 JSON payload 자체를 먼저 검증한다.
- 한 글자 marker 복구는 transport normalization으로만 기록하며 fact, URL, quote,
  source lineage 내용은 수정하지 않는다.
- normalization 전후 hash와 적용 사유를 receipt로 남기고 deterministic verifier 전체를
  다시 실행한다.
- exact multi-question scope 정책과 회귀시험이 통과하기 전 repair를 승인하지 않는다.
- 검증이 끝나기 전 score, Stage, publication gate를 열지 않는다.

capture 전 관측 영수증은 `live_repair_capture_pending_20260824.json`, capture·import 후
상태는 `live_repair_capture_recovered_20260824.json`에 별도로 남겼다. 앞 영수증은 당시
사실을 보존하므로 삭제하거나 사후 수정하지 않는다.

## 8. 브라우저 안전 사고와 재발 방지

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

## 9. 현재 테스트 증거

### Windows Playwright — 실제 live와 같은 runtime

```text
tests.test_e2r_pro_first_browser_adapter
25 tests / OK

tests.test_e2r_pro_first_approval_submit
8 tests / OK

tests.test_e2r_pro_first_completion_capture
20 tests / OK (2026-08-24 22:17 KST 재실행)
```

이 중 50만 자 이상 prompt 보존·submit 0회, 승인 이전 send 차단, exactly-once submit,
canonical conversation rebind 감사 테스트와 단일 삭제 marker 복구, raw/normalized 동시
보존, 다중 문자 손상·invalid JSON 거절이 포함된다.

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

이번 미커밋 변경을 직접 대상으로 다시 실행한 결과:

```text
tests.test_e2r_pro_first_v2_dossier_status
tests.test_e2r_pro_first_v2_live_runtime
tests.test_e2r_pro_first_v2_verifier_repair
48 tests / OK

actual captured pass 6 adapter/schema read-only replay
17 facts / 17 scoped proposals / PASS
```

WSL Playwright 전체 실행은 코드 오류가 아니라 local headless Chromium의 `libnspr4.so`
부재로 시작 자체가 실패했다. 같은 테스트를 실제 운영 runtime인 Windows
Python/Playwright에서 실행해 25/25를 확인했다.

Windows approval suite의 첫 실행은 assertion이 아니라 임시 SQLite 파일 cleanup에서
열린 handle 7개를 발견했다. 조회 경로가 `sqlite3.Connection` context manager의 commit은
사용하면서 close까지 된다고 잘못 가정한 generic 결함이었다. `ProFirstJobStore`의 조회
connection 21곳을 `contextlib.closing`으로 명시 종료하도록 고쳤고, Linux state machine
13/13과 Windows approval/submit 8/8을 다시 통과했다.

## 10. 이번 커밋에 포함되는 핵심 변경

- Pro compact/full dossier dialect adapter와 exact prior-snapshot anchoring
- append-only source lineage·route ownership·resolution merge
- latest effective snapshot resume와 verification artifact hash binding
- 실제 Windows Codex structured provider transport 호환
- source verifier v8 semantic scope mapping 및 generic subject/date/hash 교정
- question-bound verifier repair만 계획하는 규칙
- repair prompt payload batching과 deferred roster 영수증
- ChatGPT large composer DOM 입력 및 50만 자 회귀시험
- P9 live canary CLI·recovery·progress receipt 기반
- submit_count=1 후 capture가 없는 follow-up은 절대 재전송하지 않고 visible result recovery
- 한 글자 삭제 end sentinel의 bounded normalization과 raw/normalized 이중 보존
- actual Pro hybrid fact ID·direct-source counter/resolution·prior lineage projection
- current verifier-repair pass의 scoped proposal을 deterministic repair 단계까지 보존
- read-only SQLite connection 명시 종료와 Windows cleanup 회귀 확인
- frozen V1 replay와 old diagnostic 의미 보존

## 11. 아직 남은 작업

다음 순서를 모두 완료하기 전 Goal 완료를 선언하지 않는다.

1. multi-question rejection packet과 단일 Pro register row의 generic scope 정책 및
   회귀시험을 고정한다. 승인 범위를 넓히지 않고 deterministic reverification에만 전달한다.
2. pass 4 exact parent에서 pass 6 capture를 append-only revision으로 재처리한다. 기존
   no-op snapshot과 raw capture를 덮어쓰지 않는다.
3. deferred 29개와 재검증 후 남은 rejection을 bounded repair pass로 0까지 처리한다.
4. 000660 mandatory questions terminal, public material gap 0, repair pending 0을 확인한다.
5. saturation audit pass와 deterministic 7 component / 21 Judge / score / StageCourt를 실행한다.
6. `011170 / C17`, `053800 / C28` live canary를 완료한다.
7. 서로 다른 3개 mechanism canary receipt와 no hidden authority를 검증한다.
8. full unit test, Phase100, production static audit, forbidden path audit를 실행한다.
9. 최종 P9/P10 receipt·운영 문서·Draft PR 상태를 갱신한다.

현재 외부 Pro 연구 생성과 capture는 끝났다. 새 연구나 같은 pass 재전송은 필요하지 않다.
즉시 blocker는 marker가 아니라 `한 candidate의 원래 multi-question scope`와 `Pro가 적은
대표 question 한 개`를 안전하게 결박하는 deterministic import 정책이다. 이 정책이
실패하면 score·Stage를 낮게 확정하지 않고 `score_valid=false / publication withheld`를
유지한다.

## 12. 외부 검수 체크리스트

- pass 5의 `submit_count=0`과 pass 6의 `submit_count=1`이 분리돼 있는가
- deferred 29개 packet id가 receipt와 pending JSONL 양쪽에 남는가
- prior fact anchor가 exact job/run/conversation/as_of/target/parent snapshot을 요구하는가
- accepted prior fact와 source lineage identity를 repair가 삭제·재결박할 수 없는가
- scope mapper가 score/Stage를 직접 결정하지 않는가
- verifier repair가 끝나기 전 component/scoring/publication gate가 열리지 않는가
- 다른 종목·다른 as_of_date에 현재 approval scope를 재사용할 수 없는가
- 브라우저 입력이 exact E2R page DOM/CDP에만 한정되는가
- `SON_END→JSON_END` 복구가 exact current turn과 marker 4종을 요구하며 payload 의미를
  바꾸지 않고 raw와 normalized를 모두 보존하는가
- current repair에 속하지 않은 초기 MD 첨부를 새 결과로 잘못 capture하지 않는가
- scoped repair proposal은 current `VERIFIER_REPAIR` pass에서만 남고 arbitrary self-report는
  diagnostics에만 남는가
- multi-question scope mismatch가 자동 acceptance로 바뀌지 않고 deterministic verifier
  앞에서 명시적으로 처리되는가
- pass 6 no-op snapshot을 삭제·덮어쓰기하지 않고 correction을 새 revision으로 남기는가
