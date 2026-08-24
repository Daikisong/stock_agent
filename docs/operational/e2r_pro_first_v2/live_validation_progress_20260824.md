# E2R Pro-First V2 P9 라이브 검증 진행 장부

기준 시각: `2026-08-25 01:54 KST`

작업 브랜치: `feature/e2r-pro-first-browser-platform-20260822`

이번 기록의 부모 HEAD: `030223ab6125623ab1c6c9be19c2787887d5c645`

PR: Draft PR #7, 병합·draft 해제·auto-merge를 수행하지 않음

이 문서는 P8 이후의 실제 라이브 실행, 발견된 결함, 코드 수정, 테스트, 아직 남은
작업을 외부 검수자가 한 번에 추적할 수 있도록 기록한다. 이 시점은 P9 진행 중이며
`FULL_THESIS_READY` 또는 production-ready 완료를 주장하지 않는다.

## 1. 현재 한 줄 상태

```text
000660 initial/gap/gap/counter 4개 pass 완료
→ pass 6 repair capture 17건을 원본 runtime에서 무전송 재처리
→ 원본 pass 6 revision 2: 97 facts / 28 questions / 115 routes
→ 5건 accepted / 12건 pending, 기존 revision 1 no-op 감사 증거 보존
→ pass 7 ChatGPT Pro visible 결과를 재전송 없이 durable 입고 완료
→ pass 7 snapshot: 111 facts / 21 lineages / 133 routes / 28 questions
→ pass 7 COMPLETE / submit_count=1 / response hash·snapshot hash 장부 고정
→ 기존 판정기는 공유 fact를 질문마다 새 route로 다시 요구해 공개 gap을 28개로 잘못 열었음
→ acquisition route와 question ownership을 분리한 generic 수정 후 실제 pass 7 재판정: 28개→10개
→ pass 8을 재제출 없이 회수: 새 fact 0 / 새 질문별 route 28 / 누적 route 161
→ pass 8 COMPLETE / submit_count=1 / response·snapshot hash 장부 고정
→ 28개 전부에 실제 URL 또는 no-new-evidence 사유가 생겨 공개검색 반복 조건은 해소
→ pass 9는 follow-up 안전 한도에서 TRANSPORT_PENDING / submit_count=0으로 미전송 보존
→ N/A 별칭·same-pass direct fact 영수증·무결성 수리 분리의 generic 결함 3건 수정
→ 수정 코드로 read-only 재판정: 신규 공개검색 queue 0 / verifier repair 5
→ pass 8 revision 2 append 완료: 원본 revision 1 보존, facts/questions/routes 불변
→ 오래된 pass 4 verifier roster가 최신 dossier repair에 섞이는 결함을 재개 실행에서 차단
→ 최신 111-fact deterministic 재검증 완료: accepted 49 / query·search 0/0
→ mandatory-linked rejection packet 51개를 prompt budget에 따라 15 + 36으로 bounded batching
→ pass 10 VERIFIER_REPAIR는 상한에서 TRANSPORT_PENDING / submit_count=0, 아직 미전송
→ 명시적 상한 증가 때 cap 영수증만 append-only supersede하고 실제 UI failure는 재전송 금지
→ pass 11 first repair batch DOM click 1회 실행, Playwright navigation wait timeout
→ pass 11 TRANSPORT_PENDING / submit_count=1: 재전송 금지, exact visible result recovery만 허용
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
| 원본 runtime latest snapshot | `PRODOSSIERSNAPSHOT-d29e57e360f0db59c43f4f2b` (pass 8 revision 2) |
| 원본 runtime latest dossier hash | `ad7ddf67b76eabddb210cd1d5b6d2c1d6b01433c8565e0bfd7769016036f7f5c` |
| pass 6 exact repair parent | `PRODOSSIERSNAPSHOT-2c8a29d511db4f97ffb922b3` (pass 4) |
| 원본 pass 6 revision lineage | revision 1 `PRODOSSIERSNAPSHOT-374eb7b04d924c725676a390` → revision 2 `PRODOSSIERSNAPSHOT-235d2b608cbda1622f500445` |
| pass 7 capture hash | report `b1d3a9b3d55a3bd2a3bd6c9d4363bc013a52c0fce43c52b00d8803ad8b7b06e9` / dossier `b59a49240140274580b9bb8a4c739b91d58accd98acee766f07756f042eefb2f` |
| pass 8 response hash | `3f4dcdbb3c196a8f19e3f4b52ee2b0823aabdd59c1eab6a5711f89d712b648bf` |
| pass 8 corrected preflight hash | `ad7ddf67b76eabddb210cd1d5b6d2c1d6b01433c8565e0bfd7769016036f7f5c` |
| pass 8 revision lineage | revision 1 `PRODOSSIERSNAPSHOT-a6eca08aa35d81fd9f461b6d` → revision 2 `PRODOSSIERSNAPSHOT-d29e57e360f0db59c43f4f2b` |
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
| 6 | `PROPASS-3ef919d661d3bfa39f201c4e` | `VERIFIER_REPAIR` | `COMPLETE` | 1 | raw/normalized capture를 재전송 없이 재처리해 원본 revision 2 반영 완료. 5 accepted / 12 pending |
| 7 | `PROPASS-5c7b3b52569b6744cc2686d9` | `PUBLIC_GAP_CLOSURE` | `COMPLETE` | 1 | 기존 capture를 재전송 없이 입고. snapshot `PRODOSSIERSNAPSHOT-6273c68ce026516e4cb600ce`, 111 facts / 133 routes |
| 8 | `PROPASS-7392f80853f11b8cdde93640` | `PUBLIC_GAP_CLOSURE` | `COMPLETE` | 1 | 재제출 없이 기존 결과 회수. 새 fact 0 / 새 route 28. availability correction은 append-only revision 2, 누적 111 facts / 161 routes |
| 9 | `PROPASS-19f49da97db889f081930dec` | `PUBLIC_GAP_CLOSURE` | `TRANSPORT_PENDING` | 0 | bounded follow-up 안전 한도 6에서 생성만 되고 미전송. corrected routing에서는 공개검색 대상이 0이므로 제출하지 않음 |

pass 5는 실패한 연구 답변이 아니라 실제 제출 전 transport 계획이다. 삭제하거나
`COMPLETE`로 바꾸지 않았고, `submit_count=0`, `prepared_at=null`, `submitted_at=null`을
보존했다. pass 6~8은 각각 별도 prompt/input hash와 exactly-once claim으로 1회만 제출됐다.
pass 7과 pass 8은 durable 완료됐으므로 어느 쪽도 두 번째 제출을 허용하지 않는다. pass 9는
prompt 전송 전 안전 정지된 계획 영수증이며 `submit_count=0`을 그대로 보존한다.

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

## 7. 첫 repair 응답 capture 복구와 append-only 재처리 rehearsal

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

multi-question packet 계약은 다음처럼 고정했다. Pro가 선언한 대표 question과 replacement
fact의 question은 모두 immutable rejection packet roster 안에 있어야 한다. 둘 중 하나라도
packet 밖이면 hard fail한다. packet 안이라면 원래 packet의 전체 question roster를
`승인 범위`가 아니라 deterministic reverification scope로만 복원한다. 이후 각 question의
실제 acceptance는 기존 source verifier가 다시 결정한다.

쉬운 예: 원래 반려 fact 하나가 질문 A·B·C에 걸려 있고 Pro가 A를 대표로 적고 replacement
fact에 B를 적었다면, A와 B가 모두 원래 packet 안인지 먼저 확인한다. 맞으면 A·B·C를 다시
검문하지만 세 질문을 자동 통과시키지는 않는다. 반대로 Pro가 원래 packet에 없던 D를 적으면
즉시 거절한다. 이 정책은 원본 응답 객체를 수정하지 않고 derived repair action에만 기록된다.

실제 pass 6 capture를 원본과 분리한 전체 runtime 복제본에서 무전송 재처리했다. 복제본은
원본 DB, pass artifact, capture bundle과 source page cache를 포함하지만 ChatGPT browser를
열거나 prompt를 제출하지 않는다. 결과는 다음과 같다.

```text
repair actions/resolutions       17 / 17
REVERIFIED_ACCEPTED               5
REVERIFIED_REJECTED              12
prior accepted preserved         43
facts                            97 (17 rejected 원본을 17 replacement로 교체)
route receipts                  115 (기존 98 + repair route 17)
score_valid                    false
publication                 withheld
```

accepted replacement는 `MF051`, `MF054`, `CF018`, `RF034`, `RF035`다. 남은 12건은
`WRONG_SUBJECT 8`, `HISTORICAL_ONLY 3`, `QUOTE_MISMATCH 1`로 deterministic verifier가
거절했다. 특히 `WRONG_SUBJECT`는 영문 원문에 한국어 설명형 subject를 넣은 사례가 섞여
있다. source quote가 그럴듯하다는 이유로 verifier를 느슨하게 하지 않고, 다음 Pro repair가
원문 언어의 실제 entity/economic object를 subject에 쓰도록 prompt 계약을 보강했다.

이는 “Pro가 가져온 17건을 parser가 0건으로 버림”과 다르다. 현재는 17건 모두 repair
action으로 전달됐고, 5건은 실제 점수 입력 후보로 복구됐으며, 12건은 구체적인 반려 사유와
함께 다음 pass에 남았다. 예를 들어 과거 KRX 문서가 quote를 지지해도 기준일 현재성을
충족하지 않으면 `HISTORICAL_ONLY`이지 현재 사실로 자동 승인하지 않는다.

첫 0건 적용으로 생성된 아래 파일도 감사 증거라 삭제·덮어쓰기하지 않는다.

```text
snapshot id       PRODOSSIERSNAPSHOT-374eb7b04d924c725676a390
dossier hash      6802144873d3fbec2bbb17bafd009feadd5d46213183103eed7f408e16da6acb
facts/routes      97 / 98
repair receipt    resolutions 0 / unresolved 17
score_valid       false
publication       withheld
```

append-only 저장도 복제본에서 확인했다.

```text
revision 1 snapshot  PRODOSSIERSNAPSHOT-374eb7b04d924c725676a390
revision 1 hash      6802144873d3fbec2bbb17bafd009feadd5d46213183103eed7f408e16da6acb
revision 2 snapshot  PRODOSSIERSNAPSHOT-235d2b608cbda1622f500445
revision 2 hash      20919dfa73dce80c58c7be860bdb5aa03a0d95d87d5c097c7a91b37791cf1848
revision 2 parent    revision 1 snapshot
DB foreign_key_check []
```

기존 `effective_dossier.json`과 새
`effective_dossier.r2-20919dfa73dce80c58c7be86.json`은 서로 다른 SHA-256을 가지며 동시에 남아
있다. schema migration은 legacy snapshot row를 revision 1로 byte-for-byte 보존하고,
같은 pass의 새 hash만 revision 2로 추가한다. latest pointer만 revision 2를 가리킨다.
원본 runtime에는 아직 이 rehearsal을 적용하지 않았으므로, 원본 최신 상태를 revision 2로
오해하면 안 된다.

안전한 후속 원칙:

- 같은 pass를 재전송하지 않는다. durable `submit_count=1`을 유지한다.
- exact conversation과 assistant turn의 현재 본문만 capture 대상으로 삼는다.
- job/run/pass/parent marker와 JSON payload 자체를 먼저 검증한다.
- 한 글자 marker 복구는 transport normalization으로만 기록하며 fact, URL, quote,
  source lineage 내용은 수정하지 않는다.
- normalization 전후 hash와 적용 사유를 receipt로 남기고 deterministic verifier 전체를
  다시 실행한다.
- exact packet 밖 question은 hard fail하고 packet 전체는 재검증 scope로만 복원한다.
- source verifier가 거절한 replacement는 다음 repair 대상으로 남기고 자동 승인하지 않는다.
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

이번 변경을 직접 대상으로 다시 실행한 결과:

```text
multi_pass + prompt_compiler + dossier_status + live_runtime + verifier_repair
78 tests / 77 PASS / code assertion failure 0
1 environment error: WSL Chromium launch 전에 libnspr4.so 부재

actual captured pass 6 adapter/schema read-only replay
17 facts / 17 scoped proposals / PASS

actual runtime full clone pass 6 reprocess
17 actions / 5 accepted / 12 pending / append-only revision 2 / PASS
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
- representative question을 immutable packet 전체 deterministic 재검증 scope로 복원하되
  packet 밖 question은 거절
- 동일 pass의 교정 결과를 기존 snapshot을 덮어쓰지 않고 revision ordinal·별도 artifact로 추가
- 이미 제출된 pass의 template가 진화해도 durable original prompt hash로 capture/reprocess 재개
- 이미 COMPLETE인 repair pass를 재개할 때 latest no-op이 아니라 exact parent snapshot에서
  response delta를 재구성
- read-only SQLite connection 명시 종료와 Windows cleanup 회귀 확인
- frozen V1 replay와 old diagnostic 의미 보존

## 11. 아직 남은 작업

다음 순서를 모두 완료하기 전 Goal 완료를 선언하지 않는다.

1. 현재 코드·문서 커밋을 푸시한 뒤 pass 7을 `REUSE_CAPTURE`로 재개한다. 이미 저장된
   READY/capture bundle만 읽고 ChatGPT에는 다시 보내지 않는다.
2. pass 7의 예상 누적 `111 facts / 21 lineages / 133 routes / 28 questions`와 실제 durable
   snapshot hash를 대조하고 `COMPLETE / response_hash`를 확인한다.
3. pass 7 신규 fact를 deterministic source verifier에 통과시키고, pass 6에서 남은 12건과
   deferred roster를 최신 검증 결과 기준의 bounded repair queue로 다시 계산한다.
4. 남은 material verifier rejection만 같은 승인 범위의 bounded repair pass로 순차 처리한다.
   이미 accepted된 fact나 likely-nonpublic remainder를 새 검색 부족으로 오인하지 않는다.
5. 000660 mandatory questions terminal, public material gap 0, repair pending 0을 확인한다.
6. saturation audit와 deterministic 7 component / 21 Judge / score / StageCourt를 실행한다.
7. `011170 / C17`, `053800 / C28` live canary를 완료한다.
8. 서로 다른 3개 mechanism canary receipt와 no hidden authority를 검증한다.
9. full unit test, Phase100, production static audit, forbidden path audit를 실행한다.
10. 최종 P9/P10 receipt·운영 문서·Draft PR 상태를 갱신한다.

pass 6 원본 revision 2 반영과 pass 7 외부 Pro 연구/capture는 끝났다. 지금 남은 첫 단계는
새 연구가 아니라 이미 capture한 pass 7을 durable snapshot으로 입고하고 검문하는 일이다.
그동안 score·Stage를 낮게 확정하지 않고 `score_valid=false / publication withheld`를
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
- representative question과 replacement question이 모두 immutable packet 안인지 검사하고,
  packet 전체 복원이 자동 acceptance가 아닌 deterministic 재검증 scope에만 쓰이는가
- same-pass revision schema migration이 기존 row를 revision 1로 보존하고 correction을
  revision 2·별도 파일로 추가하는가
- 이미 제출된 pass의 현재 prompt template가 바뀌어도 original durable prompt hash를
  유지하고 재전송하지 않는가
- 원본 pass 6 revision 1과 revision 2가 모두 남고 parent lineage 및 full hash가 맞는가
- pass 7의 cross guard 네 개가 primary selected scope로 승격되지 않고 diagnostics에만 남는가
- 반복된 `SL01~SL03`의 이름표는 prior identity를 유지하고 새 URL/fact/state만 append하는가
- Pro의 top-level `research_status`가 아니라 누적 mandatory question closure로 effective
  status를 계산하는가
- pass 7 capture가 존재하는 상태에서 resume이 `REUSE_CAPTURE`를 선택하고 submit_count를
  1보다 늘리지 않는가

## 13. 23:05 KST 원본 재개와 public/repair queue 분리

커밋 `9d3ee28d941b954fde0aeb24b01bb797cac414ad`에서 원본 runtime을 재개했다. initial
capture, initial import, pass 4 counter audit와 pass 6 no-op snapshot은 모두 durable
artifact를 재사용했고, 기존 pass의 submit은 0회였다.

재개 직후 상태기계는 아래 새 pass를 같은 canonical conversation에 정확히 1회 제출했다.

```text
pass id       PROPASS-5c7b3b52569b6744cc2686d9
ordinal       7
pass name     PUBLIC_GAP_CLOSURE
parent        PROPASS-3ef919d661d3bfa39f201c4e
submit_count  1
status        RESEARCH_RUNNING
question ids  18
```

그런데 pass input을 읽어보니 18개 결정의 `deterministic_status`가
`VERIFIER_REPAIR_REQUIRED`인데도 기존 `_close_public_gaps()`가 이를 public search queue에
포함했다. 원인은 이 함수가 `public_material_gap_question_ids`를 사용하지 않고, 모든
non-terminal mandatory question에서 provider/lifecycle만 뺀 집합을 사용한 것이다.

쉬운 예: `새 공시를 더 찾아야 함`과 `이미 가져온 공시의 subject/quote를 고쳐야 함`은
서로 다른 작업인데, 기존 코드는 둘 다 “추가 검색” 바구니에 넣었다. 이 상태를 두면 pass 7
완료 뒤 같은 repair-required 질문으로 public-gap pass가 반복될 수 있다.

교정 규칙:

```text
public gap queue = missing mandatory + deterministic public material gap
                  - verifier repair pending
                  - provider/parser pending
                  - lifecycle hard-break pending
```

이미 제출된 pass 7은 취소하거나 다시 보내지 않았다. ChatGPT 연구는 그대로 계속되고,
monitor process만 종료했다. `submit_count=1 / RESEARCH_RUNNING`이므로 다음 재개는 visible
result recovery만 가능하다. 새 routing 의미를 적용하기 전에 `submit_count=1`인데 effective
snapshot이 없는 동일 pass를 먼저 찾고, 빈 prompt text와 durable original prompt hash로
capture/import만 재개한다. 따라서 routing 코드를 고친 뒤에도 이미 전송된 pass 7을
건너뛰거나 새 repair를 동시에 보내지 않는다. 새 helper와 회귀시험은 repair-required
`Q-REPAIR`가 public queue로 들어가지 않고 `Q-MISSING`, `Q-PUBLIC`만 남으며, running pass는
snapshot 생성 전 반드시 recovery plan으로 반환되는 것을 검증한다.

교정 후 관련 `live_runtime + saturation + verifier_repair`는 `64/64 PASS`다. 같은 HEAD의
GitHub Actions run `32735981403`은 Playwright system library를 설치한 clean runner에서
full regression `7,560 tests`와 browser mock `57 tests`를 모두 SUCCESS로 완료했다. WSL
직접 full suite의 58개 error는 정확히 browser mock 57개와 multi-pass browser 1개이며,
로컬 Chromium의 `libnspr4.so` 부재로 launch 전에 발생했다. 비브라우저 assertion failure는
0이고, 별도 핵심 122개와 이번 관련 63개는 모두 통과했다.

## 14. 23:51 KST 대기 중 상태와 V2 정적 판정 통합

pass 7은 코드 교정 전 이미 ChatGPT Pro에 제출된 pass이므로 취소하거나 새 prompt로
덮어쓰지 않는다. 현재 monitor는 동일 canonical conversation의 상태만 읽고 있다.

```text
pass id                 PROPASS-5c7b3b52569b6744cc2686d9
pass name               PUBLIC_GAP_CLOSURE
parent                  PROPASS-3ef919d661d3bfa39f201c4e
submit_count            1
automatic resubmit      false
latest observed state   RESEARCH_RUNNING
latest observed poll    132
latest observed at      2026-08-24T14:51:07Z
```

쉬운 예로, 분류가 잘못된 택배 주문이라도 이미 배송 중이면 같은 주문을 다시 보내지 않는다.
도착한 상자를 한 번 입고하고, 그 다음 주문부터 올바른 `public gap`과 `verifier repair`
바구니를 적용한다. 그래서 현재 대기는 중복 전송이 아니라 이미 1회 전송된 결과의 안전한
회수 대기다.

master goal의 정적 판정을 기존 여러 audit 출력에서 사람이 손으로 합치지 않도록 전용
명령을 추가했다.

```bash
PYTHONPATH=src python -m e2r.cli.audit_e2r_pro_first_v2 \
  --repo-root . --output /tmp/e2r_pro_first_v2_static_audit.json
```

이 명령은 contract totality, prompt snapshot, production security/authority, scoring
publication, verifier repair, generalization audit를 다시 실행하고 목표 문서가 요구한 아래
20개 카운터를 하나의 receipt로 만든다.

```text
canonical/research contract missing
required primitive/green gate/guard unmapped
generic filler/prompt snapshot/forced complete/gold leakage
component count adequacy/public-gap downgrade/material gap no-followup
verifier repair skipped/partial score publication/research-incomplete final
Pro score authority/Pro Stage authority/future leakage
symbol-specific branch/deterministic query template
```

현재 실제 재계산 결과는 `20/20 zero`, `critical_count=0`, `status=PASS`다. 고의로
`repair 뒤 scoring` 순서를 뒤집고 public gap을 corroboration보다 늦게 판정하며
`component_fact_count`를 사용한 mutation 입력은 각각 nonzero로 검출하는 회귀시험도
통과했다. GitHub workflow에는 이 명령을 `static-security` job의 필수 단계로 추가했고,
V2 문서 변경도 workflow path filter가 놓치지 않도록 포함했다.

현재 Git 상태와 외부 CI 상태:

```text
local HEAD/origin branch  bb39967fc871bf4bd4e9178a39015815612a23bf
Draft PR                  #7 / OPEN / MERGEABLE / draft 유지
last completed clean CI   32735981403 / SUCCESS / head 9d3ee28d
newer bb39967 CI           32739985977, 32739981872 / pending
new live research submit  0회 (pass 7 기존 submit_count=1 그대로)
score/Stage authority      false / false
```

이 문서 커밋 이후 workflow의 새 V2 audit 단계까지 clean runner에서 통과하는지 다시
확인한다. 아직 pass 7 capture, 원본 pass 6 revision 2 반영, 남은 bounded repair,
000660 saturation과 점수, C17/C28 canary가 남아 있으므로 완료 표시는 하지 않는다.

## 15. 00:04 KST pass 6 correction 선행 gate

대기 중 DB와 snapshot lineage를 다시 대조해, pass 7을 먼저 capture하면 pass 6의 교정
응답을 원본에 append-only revision으로 추가할 수 없다는 순서 위험을 확인했다.

```text
pass 6  COMPLETE / submit_count=1 / response_hash 있음
pass 6  original snapshot revision 1 / repair resolution 0
pass 6  captured raw proposal 17개
pass 7  RESEARCH_RUNNING / submit_count=1 / 아직 snapshot 없음
```

snapshot store는 의도적으로 descendant가 생긴 historical pass의 사후 revision을 거절한다.
따라서 pass 7 snapshot이 먼저 생기면 pass 6 revision 2를 뒤늦게 끼워 넣을 수 없다.
이는 append-only 안전장치가 맞게 작동하는 것이며, 해결은 안전장치를 끄는 게 아니라
이미 capture된 pass 6 correction을 descendant보다 먼저 적용하는 것이다.

쉬운 예: 장부 6쪽의 정정지를 붙이기 전에 7쪽을 제본하면, 나중에 6쪽 뒤에 정정지를
끼우는 순간 장부 순서가 바뀐다. 그래서 7쪽 원고가 외부에서 작성 중이더라도 입고는 잠시
멈추고 `6쪽 정정지 → 7쪽 입고` 순서로 처리한다.

이를 generic recovery gate로 구현했다.

- 현재 latest dossier pass가 `VERIFIER_REPAIR / COMPLETE / submit_count=1`인지 확인한다.
- 그 pass가 전체 latest snapshot이며 아직 revision 1인지 확인한다.
- exact pass의 capture에 repair proposal이 있으나 durable repair receipt의 resolution이
  0개인 경우만 no-op correction 대상으로 인정한다.
- 현재 재계산한 rejection packet과 unresolved question의 `pass_input_hash`가 immutable
  completed pass와 정확히 같을 때만 recovery를 허용한다.
- exact parent snapshot에서 response delta를 다시 만들고 기존 revision 1을 보존한 채
  revision 2를 추가한다.
- 이 recovery 호출은 기존 completed pass 한 개만 처리하고 즉시 반환한다. 다음 repair를
  새로 제출하지 않으며, 그 다음 단계가 이미 제출된 pass 7을 회수한다.
- revision 2가 이미 있거나 descendant snapshot이 있으면 recovery를 반복하지 않는다.

브라우저의 Pro 연구는 ChatGPT 서버에서 계속되지만, 잘못된 snapshot 순서를 만들지 않도록
상태만 읽던 local runner를 poll 168에서 종료했다. 이는 pass 7 취소가 아니며 browser
composer 입력·클릭·재전송은 0회다. 원본 DB의 pass 7은 계속
`RESEARCH_RUNNING / submit_count=1`로 보존된다.

원본 8.0MB runtime 전체를 별도 임시 복제한 뒤, 브라우저를 전혀 열지 않고 새 선행 gate를
실행한 결과는 다음과 같다.

```text
clone root                 /tmp/e2r-pass6-preflight-rehearsal-Wf7yRn
automatic resubmit         false
pass                       PROPASS-3ef919d661d3bfa39f201c4e
revision 2 snapshot        PRODOSSIERSNAPSHOT-235d2b608cbda1622f500445
parent revision 1          PRODOSSIERSNAPSHOT-374eb7b04d924c725676a390
dossier hash               20919dfa73dce80c58c7be860bdb5aa03a0d95d87d5c097c7a91b37791cf1848
facts / routes             97 / 115
repair resolutions         17
reverified accepted        5
reverified pending         12
score_valid                false
```

이 값은 이전 수동 clone rehearsal과 byte-identical dossier hash 및 동일 5/12 결과다.
관련 `live runtime + verifier repair`는 `43/43 PASS`, 확장 logic suite는 browser 1건을
제외한 84건이 PASS다. 제외된 1건은 WSL Chromium이 `libnspr4.so` 부재로 launch 전에
종료된 기존 환경 오류이며 코드 assertion failure가 아니다. V2 static audit는 다시
`20/20 zero / critical_count=0 / PASS`다.

다음 재개는 이 커밋의 코드를 사용해 원본 pass 6 revision 2부터 추가한 뒤, 같은 canonical
conversation의 pass 7 visible result만 capture한다. 그 전후 snapshot, DB foreign key,
submit_count를 다시 기록한다.

### Windows 원본 첫 적용에서 발견한 경로 길이 결함

커밋 `cac977baafbbc20b340a43de589156e3c6e2518c`으로 원본을 재개해 exact-parent
reprocess와 17건 source reverification까지 끝냈지만, revision 파일의 `.part`를 만드는
마지막 단계에서 Windows `MAX_PATH` 경계에 걸렸다.

```text
실패 파일명  effective_dossier.revision-{64자 dossier hash}.json.part
전체 길이    264자
Windows 경계 260자
DB revision  추가 전
pass 7       RESEARCH_RUNNING / submit_count=1 / snapshot 없음
new submit   0
```

따라서 원본에는 revision 2 row나 불완전 `.part` 파일이 남지 않았고 revision 1이 계속
latest다. 해결은 full hash를 버리는 것이 아니다. ledger와 receipt에는 64자 full SHA-256을
그대로 저장하고, 파일명만 `effective_dossier.r2-{앞 24자}.json`으로 줄인다. 같은 짧은
파일이 이미 있으면 내용의 full hash 검증이 실패하므로 충돌을 조용히 재사용하지 않는다.
revision ordinal과 full dossier hash의 DB unique constraint도 그대로다.

쉬운 예: 긴 송장번호 64자는 장부에 모두 적되, 서랍 라벨은 `2번 정정-앞 24자`만 쓰고
서랍을 열 때 전체 송장번호를 다시 대조하는 방식이다.

원본과 동일한 길이의 Windows runtime 복제본
`C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\live_v2\20260823T145431Z`에서 실제
snapshot persist를 실행해 다음을 확인했다.

```text
revision path  research_passes/06_PROPASS-3ef919d661d3bfa39f201c4e/
               effective_dossier.r2-20919dfa73dce80c58c7be86.json
.part 포함 전체 길이  218자
snapshot id             PRODOSSIERSNAPSHOT-235d2b608cbda1622f500445
full dossier hash        20919dfa73dce80c58c7be860bdb5aa03a0d95d87d5c097c7a91b37791cf1848
file exists              true
```

즉 filename은 짧아졌지만 snapshot ID와 full dossier hash는 Linux clone rehearsal과
동일하며 Windows 실제 파일 생성도 통과했다.

첫 원본 시도는 verifier receipt와 `effective_repaired_dossier.json`을 원자적으로 기록한
뒤 snapshot persist에서 멈췄다. 따라서 다음 재개 감지는 resolution 0인 과거 adapter
no-op뿐 아니라 다음 crash window도 처리한다.

```text
repair receipt resolutions > 0
+ effective repaired artifact full hash == receipt hash
+ normalized repaired hash != latest snapshot hash
→ snapshot persist 전 crash로 판정
→ exact completed pass를 무전송 재처리
```

반대로 normalized repaired hash가 latest snapshot full hash와 같으면 이미 반영된 정상
repair이므로 반복하지 않는다. 원본 read-only 검사에서 pass 6이 다시 recovery candidate로
정확히 검출됐고, 이 두 분기와 revision 2 반복 차단 회귀시험이 통과했다.

## 16. 00:37 KST 원본 pass 6 반영과 pass 7 capture 병합 사전검증

원본 runtime에서 pass 6 correction recovery를 다시 실행했고, ChatGPT 전송 없이 기존
capture의 17개 repair action을 exact parent pass 4에 재적용했다. Windows 짧은 revision
경로와 snapshot-persist crash recovery가 실제 원본에서 함께 작동했다.

```text
revision 1 snapshot  PRODOSSIERSNAPSHOT-374eb7b04d924c725676a390
revision 1 hash      6802144873d3fbec2bbb17bafd009feadd5d46213183103eed7f408e16da6acb
revision 2 snapshot  PRODOSSIERSNAPSHOT-235d2b608cbda1622f500445
revision 2 parent    PRODOSSIERSNAPSHOT-374eb7b04d924c725676a390
revision 2 hash      20919dfa73dce80c58c7be860bdb5aa03a0d95d87d5c097c7a91b37791cf1848
revision 2 path      research_passes/06_PROPASS-3ef919d661d3bfa39f201c4e/
                     effective_dossier.r2-20919dfa73dce80c58c7be86.json
facts/questions/routes 97 / 28 / 115
repair resolutions     17
accepted/pending       5 / 12
foreign_key_check      []
new browser submit     0
```

그 뒤 pass 7의 visible Pro 연구 결과가 완료됐다. monitor가 보이는 마지막 assistant turn만
읽어 원자 capture했고 같은 prompt를 다시 제출하지 않았다.

| 항목 | 값 |
| --- | --- |
| pass | `PROPASS-5c7b3b52569b6744cc2686d9` |
| capture source | `DIRECT_REPORT_DOM` |
| submit count | `1` |
| report | 61,738 bytes / `b1d3a9b3d55a3bd2a3bd6c9d4363bc013a52c0fce43c52b00d8803ad8b7b06e9` |
| dossier | 59,768 bytes / `b59a49240140274580b9bb8a4c739b91d58accd98acee766f07756f042eefb2f` |
| raw facts | material 4 / counter 5 / resolution 5 = 14 |
| raw lineages/routes/questions | 5 / 18 / 18 |
| READY/receipt | 존재, scope·conversation·pass hash 일치 |
| automatic resubmit | `false` |

capture는 정상인데 append-only merge 사전검증에서 실제 Pro 표현 차이 다섯 가지가 순서대로
드러났다. 각각 종목명이나 질문명을 조건으로 예외 처리하지 않고 schema/ledger 일반 규칙으로
교정했다.

1. compact 응답이 canonical ID와 route 필드를 일부 사용해 canonical V2로 오인됐다.
   이제 fact ID만 보지 않고 schema의 정식 fact 필수 필드 전체가 있을 때만 canonical로
   판정한다. compact direct-source counter에서 빠진 nullable segment/product는 `null`,
   subject는 응답의 exact target 또는 publisher로 구조화하며 문장·URL·quote는 바꾸지 않는다.
2. Pro가 primary C06과 함께 R13 guard 네 개를 `selected_archetypes`에 반복했다. prior의
   compiled scope와 exact match를 요구하고 C06만 immutable selected scope로 유지하며 R13은
   `pro_reported_canonical_followup_cross_guards` diagnostics에 남긴다.
3. 기존 `SL01~SL03`을 더 좁은 제목으로 다시 설명했다. raw capture는 그대로 두고 effective
   dossier에서는 prior lineage identity를 유지한다. 새 URL/fact/publisher/current-state만
   기존 append-only merger가 합친다.
4. pass 6 repair ledger row에만 `conversation_id` 보조 필드가 있었는데 SQL 표준 행 재구성이
   이를 지워 immutable-row rewrite로 보였다. pass id/parent/name/status/prompt/response hash가
   SQL과 모두 같을 때만 prior row 전체를 보존하고 현재 pass 7 행만 새로 추가한다.
5. Pro는 최상위 상태를 `NEEDS_VERIFIER_REPAIR`로 적었지만 repair-required 질문은 0개였다.
   follow-up effective 상태는 Pro 문자열을 채택하지 않고 누적 mandatory question closure로
   계산하며, Pro 원문 상태는 saturation diagnostics에 남긴다.

쉬운 예: pass 7은 새 자료가 없는 빈 답안이 아니다. 답안 14개와 출처 경로 18개는 있으나,
표지의 분류명과 기존 장부의 이름표가 달랐다. 표지를 억지로 정답으로 쓰거나 답안을 버리지
않고, 원본 답안은 그대로 보존한 채 장부의 고정 식별자와 deterministic 체크박스로 입고한다.

수정 코드로 실제 capture를 DB 변경 없이 read-only replay한 최종 결과:

```text
parser normalization       REMOVE_STANDALONE_JSON_LANGUAGE_LABEL
new facts                  14
new lineages                2
new route receipts         18
updated questions          18
effective facts           111
effective lineages         21
effective routes          133
effective questions        28
effective hash             6d9edd34819b57d3635f94fb3ec5454576b298cc3062eefb43ce66a6c3f2661c
normalized hash            87e1a7abc73de8e739e3495d2735705043474b87d427e7abdf23a0bfc3b610be
deterministic status       COMPLETE_WITH_LIKELY_NONPUBLIC_REMAINDER
focused regression         56 / 56 PASS
```

여기서 `COMPLETE_WITH_LIKELY_NONPUBLIC_REMAINDER`는 score/Stage 완료가 아니다. public
question closure의 누적 상태이며, source verifier·repair pending·saturation gate는 다음
단계에서 다시 판정한다. 이 절을 기록한 당시 durable DB는 pass 7을
`RESEARCH_RUNNING / submit_count=1 / response_hash=null`로 유지했고, 다음 절에 기록한 resume이
저장된 READY/capture bundle을 `REUSE_CAPTURE`로 입고했다.

## 17. 01:03 KST pass 7 durable 입고, pass 8 exactly-once 제출, 공유 fact 계보 교정

### 17.1 pass 7은 재전송 없이 COMPLETE가 됐다

커밋 `d3fc875b134ebf09315c8a4042e16f8bd64d23ce`에서 원본 runner를 재개했다. runner는
기존 pass 7 READY/capture bundle을 감지해 `FOLLOWUP_CAPTURE_REUSED`로 처리했고 browser에
같은 prompt를 다시 보내지 않았다.

```text
pass id                 PROPASS-5c7b3b52569b6744cc2686d9
status                  COMPLETE
submit_count            1
response hash           b1d3a9b3d55a3bd2a3bd6c9d4363bc013a52c0fce43c52b00d8803ad8b7b06e9
snapshot id             PRODOSSIERSNAPSHOT-6273c68ce026516e4cb600ce
snapshot parent         PRODOSSIERSNAPSHOT-235d2b608cbda1622f500445
snapshot hash           87e1a7abc73de8e739e3495d2735705043474b87d427e7abdf23a0bfc3b610be
facts / lineages        111 / 21
routes / questions      133 / 28
new browser submit      0
```

즉 16절의 read-only 사전검증 수치와 실제 durable snapshot이 일치했다. raw capture는
수정하지 않았고, normalized effective dossier만 append-only 장부에 추가됐다.

### 17.2 pass 8은 한 번만 제출됐고 로컬 monitor만 멈췄다

pass 7 입고 직후 당시 saturation 판정이 28개 질문 모두를 공개 gap으로 열어 pass 8을
계획·제출했다. 이 제출은 이미 승인된 동일 scope·conversation의 bounded follow-up이다.

```text
pass id                 PROPASS-7392f80853f11b8cdde93640
ordinal / name          8 / PUBLIC_GAP_CLOSURE
parent                  PROPASS-5c7b3b52569b6744cc2686d9
status                  RESEARCH_RUNNING
submit_count            1
response_hash           null
submitted_at            2026-08-24T15:45:03.074410Z
last local poll         84 / 2026-08-24T15:52:39Z
browser resubmit        금지
```

로컬 runner는 pass 8 결과를 기다리다가 후속 pass를 자동 제출하는 것을 막기 위해 poll 84에서
중지했다. 중지한 것은 monitor process뿐이고, ChatGPT Pro의 이미 시작된 연구는 browser에서
계속된다. 다음 실행은 durable `submit_count=1`을 우선 읽어 같은 pass의 visible 결과를
회수해야 하며 새로운 submit으로 시작하면 안 된다.

### 17.3 28개 전부를 다시 연 원인은 fact 부족이 아니라 계보 소유권 혼동이었다

기존 질문 closure는 다음 두 조건을 동시에 같은 질문의 route에 요구했다.

```text
질문 Q가 fact F를 사용함
+ route.question_family_id == Q
+ route.accepted_fact_ids 안에 F가 있음
```

하지만 한 번 취득한 source fact는 여러 질문의 근거가 될 수 있다. 예를 들어 issuer 실적
공시 하나에서 `HBM 매출 성장`과 `CAPA 잠김`을 함께 확인했다면, 공시를 연 route는 첫 질문
소유로 남아도 같은 검증 fact를 두 번째 질문이 사용할 수 있다. 두 번째 질문을 위해 동일
공시를 다시 검색·fetch하고 새 route를 만들 필요는 없다.

또 counter/resolution relationship은 새 기사 문장이 아니라 기존 direct fact 사이의 관계다.
이 관계 fact가 `source_anchor_fact_ids`로 두 원문 fact를 가리킬 때, 원문 fact가 현재 배열에서
superseded되어도 immutable route history에 실제 accepted 기록이 있으면 acquisition provenance는
사라지지 않는다.

그래서 다음 두 축을 분리했다.

- `route ownership`: 어느 질문이 그 검색을 열었는지는 그대로 유지한다. 다른 질문 route로
  재라벨하지 않는다.
- `acquisition provenance`: durable route 전체의 `accepted_fact_ids`를 합친 immutable 취득
  장부로 현재 verified direct fact를 결박한다. derived relationship은 선언한 모든 anchor가
  이 장부에 있을 때만 계보를 상속한다.

반대로 route에도 없고 anchor도 없는 direct fact는 여전히 차단한다. 따라서 “Pro가 썼으니
전부 믿는다”가 아니라, 한 번 검증된 영수증을 질문마다 중복 요구하지 않는 수정이다.

### 17.4 실제 pass 7 재판정은 28개에서 10개로 줄었고 10개는 그대로 남았다

public-gap planning과 동일하게 pass 7의 누적 111 facts를 provisional roster로 사용하고,
7개 durable snapshot의 route binding과 exact fixpoint confirmation을 다시 컴파일했다.

```text
deterministic status     NEEDS_PUBLIC_GAP_CLOSURE
research_saturation     false
기존 잘못 열린 질문       28
수정 후 공개 질문          10
fact-route 결박 미완료       9
question-source 미완료     10
verified fact 자체 없음      1
receipt hash             88c171334929933f48beefbdd3f4a77ea456f04d54dce83e78a7dc71e15846f8
```

남은 질문은 다음과 같다.

```text
C06 Q03, Q05, Q08
R13 Stage2 false-positive Q03, Q05
R13 4B/4C red-team Q03
R13 accounting/trust/price Q01, Q03
R13 high-MAE guardrail Q01, Q03
```

이 10개를 코드에서 억지로 terminal 처리하지 않았다. 9개는 direct/anchor fact가 immutable
accepted route에 실제로 결박되지 않았고, 1개는 linked verified fact 자체가 없다. pass 8은
이미 28개를 조사했으므로 결과를 한 번만 회수한 뒤 새 fact/route가 이 10개를 얼마나 닫았는지
다시 판정한다. 이 순서는 추가 제출을 먼저 하는 것이 아니라 이미 발생한 전송의 결과를
소비하는 것이다.

### 17.5 회귀시험, Windows 자원 정리, 정적 감사

세 가지 경계 시험을 추가했다.

1. 첫 질문 소유 route에서 취득한 verified fact를 두 번째 질문이 공유해도 source linkage가
   완성된다.
2. 현재 목록에서 빠진 과거 anchor라도 immutable accepted-route history가 있으면 verified
   derived relationship이 계보를 상속한다.
3. route와 anchor가 모두 없는 direct fact는 계속
   `QUESTION_FACT_NOT_BOUND_TO_ROUTE_RECEIPT`로 차단된다.

Windows browser mock은 기능 assertion을 모두 통과한 뒤 임시 SQLite를 삭제할 때만
`WinError 32`가 났다. `sqlite3.Connection`의 context manager는 commit/rollback은 하지만
연결 자체를 닫지 않으므로, multi-pass ledger의 initialize/read 연결 7곳을
`contextlib.closing`으로 닫았다. 같은 Windows mock 재실행은 `1/1 OK`다.

```text
saturation focused tests          26 / 26 PASS
V2 WSL suite                      136 code tests PASS
V2 WSL browser mock               1 environment ERROR: libnspr4.so 없음
동일 browser mock / Windows       1 / 1 PASS
Windows 전체 교차 실행            128 PASS / 9 environment ERROR
Windows 9 errors 원인              UNC worktree에서 Windows git rev-parse 불가
production static audit           20 / 20 zero, critical_count=0, PASS
```

WSL의 유일한 error는 Chromium 시작 전 shared library 부재이고 같은 테스트를 실제 Windows
Chromium에서 통과시켰다. Windows 전체 교차 실행의 9개 error는 code assertion이 아니라
Windows `git.exe`가 `\\wsl.localhost` UNC 작업 디렉터리에서 `rev-parse`를 거부한 환경 차이다.
정식 Linux Git 경로에서 해당 9개를 포함한 나머지 136개는 통과했다.

부모 HEAD `d3fc875b`의 GitHub Actions도 모두 끝까지 green이다.

| workflow | run | conclusion |
| --- | --- | --- |
| E2R Pro-first verification | `32746543317` | `SUCCESS` |
| E2R Pro-first verification | `32746545521` | `SUCCESS` |
| E2R v6 operational cutover verification | `32746545416` | `SUCCESS` |

이 절의 변경을 푸시한 뒤 새 head의 clean-runner CI를 다시 확인한다. 현재도 score/Stage 권한은
없으며 P9 saturation, source verifier/repair, score/Stage, C17/C28 canary가 남아 있다.

## 18. 01:30 KST pass 8 회수 완료와 공개검색·verifier 수리 분리

### 18.1 기존 pass 8 결과만 회수했고 새 제출은 없었다

같은 Windows runner를 원본 job에 `--resume-job-id`로 연결해 이미 1회 제출된 pass 8의
ChatGPT Pro 결과만 회수했다. 재개 시 실제 제출 횟수를 기준으로 follow-up 상한을 6으로
고정해, pass 8 capture 뒤 새 browser submit이 자동으로 발생하지 못하게 했다.

```text
pass id                 PROPASS-7392f80853f11b8cdde93640
status                  COMPLETE
submit_count            1
response hash           3f4dcdbb3c196a8f19e3f4b52ee2b0823aabdd59c1eab6a5711f89d712b648bf
snapshot id             PRODOSSIERSNAPSHOT-a6eca08aa35d81fd9f461b6d
snapshot parent         PRODOSSIERSNAPSHOT-6273c68ce026516e4cb600ce
snapshot hash           9d0ee27056ec4561e89af7436d15c50378a2bcdd4aa0d37d6bbe5a131b2850e9
facts / lineages        111 / 21
routes / questions      161 / 28
new facts / new routes  0 / 28
new browser submit      0
```

Pass 8은 28개 질문마다 실제로 연 URL과 `새 material evidence 없음` 사유를 남겼다. 새 fact가
0인 것은 파싱 실패가 아니다. 이미 누적된 111개 fact는 그대로이고, 이번 답변은 각 질문에
대해 추가 공개 경로를 조사했으나 새 사실을 찾지 못했다는 28개 route 영수증을 추가했다.

그 직후 생성된 pass 9는 다음처럼 전송 전에 멈췄다.

```text
pass id                 PROPASS-19f49da97db889f081930dec
ordinal / name          9 / PUBLIC_GAP_CLOSURE
status                  TRANSPORT_PENDING
submit_count            0
reason                  bounded browser pass limit 6 reached
```

이는 실패한 ChatGPT 응답이 아니라 미전송 계획이다. 수정된 판정에서는 신규 공개검색 queue가
0이므로 pass 9를 보내지 않고 append-only 안전 영수증으로 보존한다.

### 18.2 pass 8에서 드러난 generic 결함 세 가지

첫째, compact 응답의 `availability_class=NOT_APPLICABLE_WITH_REASON`은 뜻은 맞지만 canonical
enum보다 구체적인 별칭이었다. adapter가 이 값을 모르면 기본값 `PUBLIC_SEARCHABLE`로
내려가 같은 질문을 다시 검색하게 됐다. 별칭을 canonical `NOT_APPLICABLE`로만 정규화하고
raw status와 사유는 그대로 보존한다.

둘째, 정상 route가 같은 pass에서 direct fact의 정확한 source URL을 열었지만 Pro가 route의
`accepted_fact_ids`에 그 fact ID 하나를 빠뜨린 경우가 있었다. 다음 조건을 모두 만족할
때에만 취득 계보를 결박하도록 했다.

- 현재 deterministic verifier에서 승인된 direct fact다.
- fact의 `research_pass_id`와 route의 `pass_id`가 정확히 같다.
- route provider/parser가 모두 `SUCCESS`이고 exact source URL을 실제 열었다.
- derived relationship이 아니다.

다른 pass에서 같은 URL을 연 기록은 사용할 수 없고, derived fact는 계속 모든
`source_anchor_fact_ids`의 immutable accepted 계보를 요구한다. 예를 들어 이번 상자에 든
물건의 URL과 이번 배송 영수증이 정확히 같을 때 누락된 품목 번호를 복구할 수 있지만, 지난
배송의 영수증이나 다른 물건의 관계 설명으로 대신할 수는 없다.

셋째, 공개 경로를 충분히 조사했고 핵심 source role도 비어 있지 않은 terminal fact-backed
질문이 오직 fact/lineage 결박 때문에 실패하면, 추가 웹 검색으로는 장부 무결성을 고칠 수
없다. 이 경우를 `verifier_repair_pending`으로 보내고 public follow-up에서는 제외했다.

```text
잘못된 반복
공개 URL 조사 완료 + fact 계보 결함
→ 다시 Pro 공개검색
→ 새 route만 늘고 계보 결함은 그대로

수정된 전이
공개 URL 조사 완료 + fact 계보 결함
→ verifier repair
→ 기존 fact를 승인·철회·교체한 뒤 deterministic 재검증
```

### 18.3 immutable raw를 바꾸지 않은 correction 사전검증

Pass 8 원본 capture와 pass 7 부모 snapshot을 다시 adapter에 통과시켰다. revision 1과 수정
결과의 차이는 질문 한 건의 availability canonicalization 한 필드뿐이었다.

```text
revision 1 hash         9d0ee27056ec4561e89af7436d15c50378a2bcdd4aa0d37d6bbe5a131b2850e9
corrected preflight     ad7ddf67b76eabddb210cd1d5b6d2c1d6b01433c8565e0bfd7769016036f7f5c
changed leaf            $.question_family_results[20].availability_class
before / after          PUBLIC_SEARCHABLE / NOT_APPLICABLE
facts / routes          111 / 161, 변화 없음
raw status              NOT_APPLICABLE_WITH_REASON, 변화 없음
```

기존 snapshot을 덮어쓰지 않고 같은 pass의 append-only revision 2로 persist했다.

```text
revision 2 snapshot     PRODOSSIERSNAPSHOT-d29e57e360f0db59c43f4f2b
parent snapshot         PRODOSSIERSNAPSHOT-a6eca08aa35d81fd9f461b6d
relative path           research_passes/08_PROPASS-7392f80853f11b8cdde93640/
                        effective_dossier.r2-ad7ddf67b76eabddb210cd1d.json
same-pass revisions     2
foreign-key violations  0
```

revision 1과 raw capture는 감사 증거로 그대로 남아 있다.

수정 코드로 DB write 없이 saturation을 다시 계산한 결과는 다음과 같다.

```text
deterministic status      NEEDS_VERIFIER_REPAIR
research_saturation      false
new public route queue   0
verifier repair pending  5
nonterminal questions    0
receipt hash             8825fd17e2876218586ea388eeb3b9e827c471ca61c130faca9dae9355c5fa5b
```

수리 대상은 `C06 Q03`, `C06 Q08`, `R13 Stage2 false-positive Q05`, `R13 4B/4C Q03`,
`R13 high-MAE Q01`이다. 공통 원인은 competitor-derived relationship이 Samsung 관련 anchor
`MF016`을 포함하고, 현재 verifier가 이를 `WRONG_SUBJECT`로 거절한 점이다. 따라서 다음
단계는 새 검색이 아니라 정확한 rejection packet을 같은 대화의 verifier repair로 보내고,
수정 응답을 deterministic verifier로 다시 판정하는 것이다.

### 18.4 이번 경계의 검증 증거

```text
saturation focused tests           28 / 28 PASS
dossier status tests               14 / 14 PASS
live runtime targeted routing       1 / 1 PASS
V2 11-module suite                 139 code tests PASS
WSL browser mock                    1 environment ERROR: libnspr4.so 없음
동일 browser mock / Windows         1 / 1 PASS
production static audit            20 / 20 zero, critical_count=0, PASS
static audit hash                  575d42c5395ae28d65fa4628194f7b00e4b0096158015d6c6502d01755d94ff5
```

추가한 핵심 회귀시험은 N/A 별칭 정규화, 같은 pass exact URL 결박, 다른 pass 같은 URL 차단,
계보가 없는 terminal fact를 public 검색이 아니라 verifier repair로 보내는 경계다. WSL의
유일한 error는 Chromium 실행 전 shared library 부재이며 실제 live와 같은 Windows
Chromium에서는 같은 browser mock이 통과했다.

### 18.5 recovered snapshot과 stale verifier receipt의 결박

Revision 2 저장 뒤 browser submit 상한을 그대로 6에 잠그고 runner를 재개했다. 새 전송은
없었지만 repair packet 생성 직전에 다음 오류가 났다.

```text
latest effective dossier hash     ad7ddf67b76eabddb210cd1d5b6d2c1d6b01433c8565e0bfd7769016036f7f5c
reused verification dossier hash  fee5aebe622a97340f9199c5d11bf9cf26cbae1c051a4bb6482274498dbde4c6
latest dossier facts              111
stale verification rows           97
stale rejected facts not current  8
failure                            verifier rejection references an unknown dossier fact
browser submit                     0
```

Pass 6 repair에서 철회·교체된 `MF015`, `MF016`, `MF017`, `MF048`, `CF003`, `CF004`,
`CF005`, `CF007`의 예전 rejection이 pass 4 verification receipt에 남아 있었다. runner는
recovered public pass가 이번 process에서 새로 실행되지 않았다는 이유로 old receipt를 그대로
재사용했다. 최신 dossier에는 이 ID가 없으므로 repair compiler의 hard fail은 옳았고, 그 전에
최신 dossier를 재검증하지 않은 orchestration이 문제였다.

다음 generic gate를 repair packet 생성 앞에 추가했다.

```text
verification.result가 durable reuse이고
receipt.effective_dossier_hash != canonical_hash(latest dossier)
→ request_effective_dossier_reverification
→ 최신 hash-bound dossier를 같은 deterministic verifier로 1회 검증
→ 그 결과로만 rejection packet 생성
```

hash가 같으면 재검증하지 않고, verifier 결과가 이번 실행에서 이미 생성됐어도 반복하지 않는다.
따라서 의미 없는 verifier loop도 열리지 않는다. 검증 결과는 다음과 같다.

```text
live-runtime regression           26 / 26 PASS
source-verifier regression        29 / 29 PASS
production static audit           20 / 20 zero, critical_count=0, PASS
static audit hash                 438acfc0546f8bdcbc6d30d74780f546bf880bacde4a5540fde52abe7868ed14
```

이 시점에도 full-thesis score와 canonical Stage 권한은 없다. 최신 111-fact source 재검증은
완료됐고 다음 순서는 51개 verifier packet의 최대 4회 bounded repair, saturation 재판정,
deterministic score/Stage, C17/C28 canary다.

### 18.6 최신 111-fact verification과 bounded repair batch

Stale-roster gate를 적용한 재개 실행은 pass 8 revision 2의 exact hash를 verifier 입력으로
사용했다. 새 검색 query는 없었고, 이미 알려진 source URL의 full document 검증만 수행했다.

```text
verification id          PROVERIFY-d426e1b62210ef2277a5272f
verification attempt     4
effective snapshot       PRODOSSIERSNAPSHOT-d29e57e360f0db59c43f4f2b
effective dossier hash   ad7ddf67b76eabddb210cd1d5b6d2c1d6b01433c8565e0bfd7769016036f7f5c
candidate / accepted     111 / 49
compiled evidence facts  49
document cache reuse     105
full document fetch      6
query / search           0 / 0
verification hash        ec09bda0ad661fa9d4d0083c3a7b65f415a426b8dd883bdc8787615d4a2edfdc
```

111개 중 verifier 비승인 candidate가 모두 repair 대상은 아니다. mandatory question에 연결된
51개만 packet이 됐다. 한 browser composer에 모두 넣지 않고 21만 자 예산으로 deterministic
prefix를 고른다.

```text
pending repair packets   51
first batch              15
deferred                 36
first payload chars      199,646 / 210,000
repair pass limit        최대 4
publication              withheld
```

첫 batch 계획은 pass 10 `PROPASS-2c64ccb7b9a86a8e7cbd5922`로 장부에 생겼지만, 실행을
안전하게 조사하려고 follow-up 상한을 6으로 고정했기 때문에
`TRANSPORT_PENDING / submit_count=0`에서 멈췄다. browser 전송은 없었다.

기존 구현은 나중에 사용자가 상한을 명시적으로 높여도 동일 input의 pending row를 계속
반환해 영원히 재개할 수 없었다. 반대로 pending row를 PLANNED로 되돌리면 append-only 감사
규칙을 깬다. 다음과 같이 분리했다.

```text
사유가 bounded browser pass limit이고 submit_count=0
+ 새 max_followup_passes가 실제 제출 수보다 큼
→ 기존 pending row 보존
→ supersedes_pass_id를 가진 새 pass append

composer size / UI incompatibility 등 실제 transport failure
→ 상한을 높여도 기존 TRANSPORT_PENDING 유지
→ 자동 재전송 금지
```

재개 pass는 original logical input hash와 transport-resume input hash를 둘 다 장부에 결박한다.
같은 재개 호출을 반복해도 새 pass가 더 생기지 않고 이미 생성된 pass를 idempotent하게
반환한다. 회귀 결과는 Windows 실제 Chromium을 포함한 multi-pass `19/19`, verifier repair
`18/18 PASS`다.

이 시점의 다음 실제 작업은 명시적으로 follow-up 상한을 올려 first repair batch를 같은
ChatGPT conversation에 exactly once 전송하는 것이다. 아직 score/Stage 권한은 없다.

### 18.7 first repair click 뒤 navigation timeout의 exactly-once 복구

Follow-up 상한을 10으로 명시해 pass 10의 cap-only 영수증을 보존하고 새 pass 11을 만들었다.
첫 repair batch 15개 prompt는 exact 동일 conversation의 visible composer에 준비됐고 send
button DOM click도 한 번 실행됐다.

```text
pass id                 PROPASS-7a551c28c37e8ca775a056a4
pass name               VERIFIER_REPAIR
parent                  PROPASS-7392f80853f11b8cdde93640
supersedes cap receipt  PROPASS-2c64ccb7b9a86a8e7cbd5922
DOM click               1
submit_count            1
durable status          TRANSPORT_PENDING
error                   Locator.click navigation wait timeout after click action done
automatic resubmit      forbidden
```

Playwright 로그는 element가 visible/enabled/stable인 상태에서 `click action done`까지 완료한
뒤 scheduled navigation을 기다리다 30초 timeout이 났다고 기록한다. 이 경우 click 전 실패로
간주해 다시 누르면 중복 전송 위험이 있다.

다음 복구 규칙을 추가했다.

```text
TRANSPORT_PENDING + submit_count=1 + capture 없음
→ RECOVER_SUBMITTED_RESULT
→ prompt 준비·DOM click 경로 금지
→ 같은 conversation의 result를 read-only poll
→ exact PASS_ID와 PARENT_PASS_ID marker가 각각 1개일 때만
   RESEARCH_RUNNING 복구 후 COMPLETE 가능
```

반대로 `submit_count=0`인 transport failure는 이 경로에 들어올 수 없다. 향후 click timeout
자체도 한 번의 post-click visible state 검사에서 `RESEARCH_RUNNING`이 확인되면 성공으로
처리하며, 상태가 증명되지 않으면 예외와 recovery-only 장부를 그대로 남긴다. 어느 경우에도
두 번째 click은 없다.

```text
Windows Chromium multi-pass       20 / 20 PASS
live-runtime recovery             27 / 27 PASS
production static audit           20 / 20 zero, critical_count=0, PASS
```

이 시점의 pass 11 결과는 아직 durable capture되지 않았다. 다음 실행은 새 전송이 아니라
현재 대화의 pass 11 결과만 회수한다. full-thesis score와 canonical Stage 권한은 없다.
