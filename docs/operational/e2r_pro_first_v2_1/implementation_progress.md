# E2R Pro-First V2.1 구현 진행 장부

기준 시각: `2026-08-29 세 기존 canary fail-closed 봉인 / 독립 새 C06 ChatGPT Pro 실행 중`

기준 Goal:
`C:\Users\eorb9\Downloads\e2r_pro_first_v2_all_archetype_research_saturation_master_goal.md`

작업 브랜치: `feature/e2r-pro-first-browser-platform-20260822`

phase commit 계보:

```text
P0 b6c30eb9  기존 repair-heavy Pro 실행을 진단 자료로 봉인
P1 10c7269b  Pro fact 반려 원인을 최초 출력·로컬 결함·의미 결함으로 분해
P2 152db6a7  source 문서와 atomic fact를 분리한 검증 친화 dossier를 도입
P3 d5d62bc2  최초 Pro 조사에서 verifier-ready 증거를 생성하도록 계약 강화
P4 788e14d2  URL 날짜 인용 alias scope의 기계적 결함을 로컬에서 자동 정규화
P5 cad578af  전체 dossier 재출력을 제거하고 의미 오류만 compact delta로 수리
P6 8b0e27bd  기존 대화를 봉인하고 새 Pro 세션의 blind canary 실행 경계를 구현
P7 fdf4ac40  Pro JSON 첨부를 동일 응답 증거로 봉인하고 C06 Gate를 통과
P8 f719b94b  C17/C28 독립 fresh target 생성을 고정
P8 dca86ae9  C17 fresh Pro 초기 검문 통과를 기록
P8 a62e4895  C28 fresh Pro 초기 검문과 3-target 효율 영수증을 확정
P10 7abc9ecb C06 V3 JSON 후반 포화도 실행 경로 연결
P10 377e0c36 과거 경로 실패와 검문 수리의 무한 재검색을 차단
P10 df2925bf 현재 Pro 응답 오인과 질문별 무한 재전송을 차단
P10 e3c2f2e8 C06 11차 캡처와 실제 질문 중복 제거를 기록
P10 e0fabc43 같은 경로 영수증 반복을 의미 지문으로 차단
P10 1eaa4260 C06 12차 검문 통과와 13차 근거를 기록
```

PR #7은 계속 Draft/open이며 main 병합, draft 해제, auto-merge를 하지 않는다.

## 현재 판정

```text
P0 old run freeze                         COMPLETE
P1 rejection A/B/C taxonomy              COMPLETE
P2 ResearchDossierV3                      COMPLETE
P3 Initial Prompt V3                      COMPLETE
P4 local preflight                        COMPLETE
P5 compact RepairDeltaV3                  COMPLETE
P6 fresh-session orchestration            COMPLETE
P7 000660 fresh canary                    COMPLETE
P8 C17/C28 fresh initial canary           COMPLETE
P9 live multi-pass saturation             IN_PROGRESS (기존 3개 terminal pending 봉인, 새 C06 blind chat 실행 중)
P10 final CI/audit                        IN_PROGRESS (Reviewer A~H PASS, 새 live 결과 뒤 최종 회귀·CI 대기)
```

아직 선언할 수 있는 최종 verdict는 없다. 특히 old run을 완료한 것으로 간주하거나
`PRO_FIRST_V2_1_OPERATIONAL_RESEARCH_READY`를 선언하지 않는다.

## P14 — 화면상 전송과 서버 저장 분리, C06 대화 폐기

### 원인

Pass 24는 원래 탭에서 user turn과 stop 버튼이 보여 7,900초 넘게 `RESEARCH_RUNNING`으로
감시됐지만, 같은 로그인 context의 새 공개 대화 화면에는 Pass 24 user turn이 없었다. 같은 화면의
낙관적 DOM을 서버 저장 증거로 사용한 것이 장시간 무한 대기의 원인이었다.

쉬운 예로 전송함 화면에 편지가 보인 것만 확인했고, 실제 우편 서버의 발송 기록은 확인하지 않은
상태였다. 이제는 별도 새 탭의 같은 `/c/{conversation_id}`에서 정확한 job/run/pass/parent marker가
한 user turn 안에 모두 있어야 연구 실행으로 인정한다.

### generic 수리

```text
동일 화면 stop/user turn                 서버 저장 권한 없음
새 공개 conversation의 exact user turn   서버 저장 확인
두 독립 새 화면에서 부재                  해당 pass FAILED_HARD/TRANSPORT 봉인
동일 pass 추가 click                      금지
별도 replacement pass                     정확히 1회만 허용
replacement도 두 번 부재                  conversation 폐기, 새 fresh run 필요
```

Library나 다른 대화가 현재 탭이어도 mutable history search에 의존하지 않는다. ledger가 가진 exact
conversation ID의 공개 `/c/...` URL을 읽기 전용으로 연다. 새 탭 관측과 exact URL 이동은 composer를
편집하거나 send를 누르지 않는다. 물리적 DOM send surface는 계속 `submit_once()` 한 곳뿐이다.

### 실제 C06 결과

Pass 24는 두 번의 독립 새 화면 관측에서 모두 부재했다.

```text
pass                         PROPASS-0b188e6ae08632f0773af6d8
status                       FAILED_HARD / TRANSPORT
ledger submit count          1
actual DOM send click        1 (기존 modal 복구 때의 1회)
새 수리 뒤 추가 click         0
absence observations         2
automatic resubmit           false
```

그 뒤 실패 evidence hash를 prompt context에 넣은 별도 Pass 25를 한 번 만들었다. Pass 24를 다시 누른
것이 아니며 `supersedes_unpersisted_pass_id`로 두 pass를 명시적으로 연결했다. 그러나 Pass 25도 같은
대화에서 서버에 저장되지 않았다.

```text
replacement pass             PROPASS-098c6fa0009b452f1f4d6662
supersedes                    PROPASS-0b188e6ae08632f0773af6d8
status                        FAILED_HARD / TRANSPORT
ledger submit count           1
absence observations          2
same-pass retry               0
automatic resubmit            false
```

따라서 conversation `6a8db0ad-8ed0-83e8-888e-dce26c950343`은 더 사용하지 않는다. accepted fact 66과
기존 score/Stage 미확정 상태는 감사 자료로 보존하지만 새 prompt의 답안으로 주입하지 않는다. 다음
C06은 기존 job/run/conversation을 diagnostic-only로 봉인하고 새 runtime/session/job/run/pass/chat을
가진 blind successor로 시작한다.

### 검증

```text
낙관적 initial/follow-up 서버 미저장 회귀      PASS
stale prior-pass marker 오인 방지               PASS
두 부재 봉인·동일 pass 재전송 차단              PASS
별도 replacement 1회·두 번째 실패 차단         PASS
Library/다른 chat -> exact URL 무전송 이동       PASS
집중 회귀                                      78/78 PASS
CI 동일 Pro-first core                         238/238 PASS
browser mock E2E                               69/69 PASS
전체 unittest                                  7,769 PASS
failure/error                                  0/0
production static audit critical               0
guarded DOM send-click path                    1
```

기계 판독 영수증은 `p14_server_persistence_and_new_chat_successor_receipt.json`이다. 현재는 새 successor
chat을 시작하기 전 checkpoint이므로 `completion_claimed=false`다.

## P13 — Pass 23 실패 봉인과 Pass 24 exactly-once 복구

### 왜 화면의 과거 결과를 잘못 잡았는가

ChatGPT는 완료된 응답 안쪽에 `[data-message-author-role=assistant]`를 두지만, 현재 생각/실패 카드는
바깥 `section[data-turn=assistant]`만 두는 UI가 있다. 기존 adapter는 selector별 결과를 이어 붙여
과거 완료 응답이 최신 실패 카드보다 뒤에 온 것처럼 읽었다.

이제 assistant turn selector를 CSS union으로 한 번에 읽어 실제 DOM 순서를 보존하고, 안쪽 요소는
같은 최상위 assistant section으로 정규화한다. 최신 카드의 `생각 실패`가 과거의 완성 dossier보다
우선한다.

쉬운 예로 22번 답안과 23번 실패지가 책상에 같이 있을 때, 종이 종류별로 모아서 순서를 추측하지
않고 책상 위 실제 시간 순서로 읽는다.

### Pass 23 fail-closed 결과

Pass 23 디렉터리에 잘못 붙어 있던 capture는 실제로 Pass 22 marker를 가진 결과였다. 삭제하거나
덮어쓰지 않고 hash-addressed quarantine으로 통째로 이동했다.

```text
expected pass                PROPASS-e403f96cfbc9d058ab96521b
observed pass                PROPASS-01b7ec312cf2422e4efbf228
observed report hash         2afebf6805aa723863878b1f8a9e7c389b3694dc46857ef7394a256cc593690b
quarantine receipt hash      50715d7ab4e56413f468332cb10da2f0aa28c1464b25544d80a04a245b1ef2a5
status                       PRESERVED_NOT_IMPORTED
fact/score/Stage authority   false / false / false
```

그 뒤 실제 최신 assistant turn `request-...-12`의 `생각 실패` 원문을 별도 failure artifact로
봉인하고 Pass 23을 `FAILED_HARD`로 닫았다. 중간 사고문에 있던 거래대금이나 패키징 설명은 최종
구조화 dossier가 아니므로 fact로 가져오지 않았다.

```text
Pass 23 status               FAILED_HARD
submit_count                 1
automatic resubmit           0
failure response hash        bd9b9c5864646967b516f49f7c554877243f65b13bde74b7df6ced845e39bf9a
failure receipt hash         3b8ea91449c83ed4e846f0965d0af1e11246c767d3a647af22105620cc86dc05
```

### 같은 논리 입력의 실패 피드백 재시도는 한 번만

Pass 23 자체를 다시 보내지 않았다. 실패 class/hash/reason을 새 prompt의
`provider_failure_feedback`에 넣은 Pass 24를 만들었다. 같은 root context에서 이 새 pass까지
실패하면 자동 반복을 막는다.

처음 Pass 24를 준비할 때 과거 대화 검색 modal이 화면 위에 남아 전송 버튼 클릭을 모두
가로막았다. Playwright call log가 `modal-global-search intercepts pointer events`를 반복 기록했고
실제 user turn에는 Pass 24 marker가 없었다. 다음 조건을 모두 확인한 뒤 기존 ledger claim 아래에서
실제 DOM click 한 번만 수행했다.

```text
Pass 24                    PROPASS-0b188e6ae08632f0773af6d8
supersedes                 PROPASS-e403f96cfbc9d058ab96521b
ledger submit_count        1 유지
actual DOM send click      1
new pass on modal recovery 0
automatic resubmit         false
current state              RESEARCH_RUNNING
```

이미 정확한 conversation URL이 열려 있으면 바뀐 history-search UI를 찾지 않고 현재 대화를 그대로
쓴다. 단, URL의 conversation ID가 durable ID와 다를 때만 visible history search로 이동한다.

첫 completion monitor는 1,440회/7,923초 동안 마지막까지 `RESEARCH_RUNNING`을 확인하고 bounded
종료했다. 이 종료는 연구 실패나 완료가 아니다. 같은 Pass 24에 monitor만 다시 붙였고
`browser_submit_delta=0`, poll 1 `RESEARCH_RUNNING`을 다시 확인했다.

현재 accepted fact 66과 saturation 상태는 변하지 않았다. Pass 24 최종 JSON을 아직 받지 않았으므로
새 fact, score, Stage를 만들지 않는다. 기계 판독 영수증은
`p13_pass23_failure_and_pass24_exactly_once_recovery_receipt.json`이며 `completion_claimed=false`다.

이번 수리의 직접 관련 회귀 119개는 실행 환경의 책임을 분리해 전부 통과했다.

```text
Windows Chromium browser adapter       30/30 PASS
Windows Chromium multi-pass            23/23 PASS
Linux runtime + fresh orchestration     66/66 PASS
합계                                     119/119 PASS
```

한 번에 Windows에서 네 모듈을 돌렸을 때 8개는 WSL worktree의 `.git` 파일이 가리키는 Linux
절대경로를 Windows Git이 읽지 못해 실패했고, Linux에서 세 모듈을 돌렸을 때 2개는 test body 전에
Chromium의 `libnspr4.so`가 없어 실패했다. 전자는 Linux 66개 green으로, 후자는 Windows Chromium
23개 green으로 각각 실제 책임 환경에서 재검증했다. 따라서 이 환경 오류를 제품 회귀로 숨기거나
PASS 수에 중복 계산하지 않았다.

첫 P13 push의 GitHub `static-security`는 normal submit과 modal recovery에 물리적
`send.click()`이 각각 하나씩 있어 `guarded_dom_submit_path_count=2`로 차단했다. 복구 흐름도 기존
`submit_once()` 경계로 다시 들어가게 합쳐 실제 DOM send surface를 하나로 만들었다. modal을 닫는
Escape도 전역 keyboard가 아니라 확인된 modal 요소에만 보낸다.

```text
production static audit critical         0
guarded DOM send-click path               1
Windows browser adapter                   30/30 PASS
Windows multi-pass                        23/23 PASS
census run-mode honesty                    24/24 PASS
```

쉬운 예로 정상 전송문과 복구 전송문을 따로 두지 않고, durable approval와
`_submit_attempted` 잠금이 붙은 문 하나만 함께 사용한다. 첫 실패 CI를 삭제하거나 green으로
간주하지 않으며, 수리 commit의 새 GitHub Actions가 끝나야 이 항목을 완료로 올린다.

두 번째 P13 push에서는 static/security와 browser E2E는 통과했지만 core-unit 236개 중 정적 보안
계약 2개가 실패했다. 공통 helper나 adapter 내부 재호출도 허용하지 않고 다음처럼 권한을 더 좁혔다.

```text
adapter recovery preflight    modal·lineage·unsent user turn만 검증
physical DOM send click       submit_once 내부 정확히 1개
submit_once caller            durable multi-pass recovery coordinator
global keyboard path          0
production static critical    0
focused security/recovery     63/63 PASS
```

static audit에는 정확한 `resume_intercepted_followup_submit`만 허용되고 이름이 비슷한 unchecked 함수는
계속 `submit_without_approval_count`로 잡히는 회귀를 추가했다.

CI와 동일한 local readiness runner를 다시 실행한 결과 core unit은 237/237 PASS,
failure/error/skip 0/0/0, `PRO_FIRST_PLATFORM_IMPLEMENTATION_READY`로 닫혔다. 이 구현 readiness는
Pass 24 연구 완료나 전체 master goal 완료를 뜻하지 않는다.

현재 commit `52d611cf3ac432bbd3e9d08e2253761ca6a17e1c`에서 clean local 전체 회귀도 끝까지
재실행했다. 7,764개가 통과했고 failure/error는 0/0, 기존 skip은 38개였으며 실행 시간은
714.125초다. 테스트가 만든 임시 `output/`은 격리된 temporary directory 안에서 정리됐고 Git
worktree에는 추적·미추적 변경을 남기지 않았다. 같은 commit의 GitHub core-unit,
static-security, browser-mock-e2e는 이미 SUCCESS이고 full-regression과 operational 전체 테스트는
아직 실행 중이므로 이 장부에서는 원격 전체 green이나 live full-thesis 완료를 선언하지 않는다.

## P12 — Pass 17 fail-closed 수리와 실제 포화도 재개

### 화면 JSON의 의미

ChatGPT 화면의 `ResearchDossierV3_SKHynix_000660_asof_2026-08-23.json`은 정상적으로
다운로드·capture된 응답이다. 따라서 이 시점의 문제는 “파일을 못 받음”이 아니었다.

```text
ChatGPT Pro 응답 JSON 다운로드
→ 같은 assistant turn·conversation에 결박
→ dossier 구조 검증
→ source-backed fact를 로컬 verifier로 재검문
→ 통과한 현재 근거만 saturation 질문에 연결
```

쉬운 예로 택배 상자는 이미 도착했다. 후속 작업은 택배를 다시 주문하는 것이 아니라 상자
안의 증거가 `as_of_date`, 발행 주체, 인용문, URL 계보를 통과하는지 확인하는 단계다.

### Pass 17 compact repair 수리

Pass 17은 파일 다운로드가 아니라 같은 대화의 화면에 직접 표시된 compact repair JSON이었다.
화면에서 확인한 86,263바이트 응답을 별도 재전송 없이 capture했다.

```text
pass                 PROPASS-e28bda224af4e7ceb393f04a
submit_count         1
automatic resubmit   0
raw repair actions   48
withdraw             40
replacement verify   8
accepted             6
failed               2
verification query   0
verification search  0
Pro resubmit         0
```

전송 형식 정규화는 진단용 `fetched_excerpt`가 candidate quote와 다르다는 이유만으로 반려하지
않고, source URL 중복을 제거하고, 실제 source가 바뀐 correction을 replacement로 승격한다.
단, issuer scope가 다르거나 로컬 재검문에 실패한 replacement는 원래 fact를 살려 두지 않고
fail-closed 철회한다.

완료된 Pass 17에도 이 규칙을 append-only로 적용했다.

```text
revision                         2
facts before / after             71 / 69
successful replacement retained 6
failed replacement withdrawn    2
terminal question restored       17
effective dossier hash           42a560ae54ea1e61926c3e5149944b11f1e530d4273578ba0c536867b1ab2a82
```

### 포화도 판정의 로컬 오류 2건

첫째, 과거에 정상 검문됐지만 지금은 `HISTORICAL_ONLY` 또는 `SUPERSEDED`인 fact를 현재
질문의 verifier 수리 대상으로 다시 열던 오류를 고쳤다. 이런 fact는 현재 점수 근거로 쓰지
않지만, 단지 과거 근거라는 이유만으로 새 Pro 수리를 만들지도 않는다. 현재 근거가 하나도
없다면 기존처럼 질문 자체는 닫히지 않는다.

둘째, 이유가 명시된 `NOT_APPLICABLE_WITH_REASON` 질문에 남아 있던 stale source-role 표기가
질문을 다시 여는 오류를 고쳤다. 일반 fact-backed 질문의 거짓 source-role 주장은 계속
차단한다.

### SATURATION_AUDIT 100k 입력 경계

28개 질문에 append-only route 전체를 그대로 반복해 넣어 감사 prompt가 248,906자로 커지던
문제를 해결했다. SATURATION_AUDIT에만 의미 보존 digest를 쓰며, 일반 gap closure 입력은
원래 상세 상태를 유지한다.

```text
before context chars       248,906
before question state      180,118
after context chars         85,293
after question state        57,637
question count                  28
raw route progress hash     보존
score/stage authority       없음
```

예를 들어 “같은 길을 40번 확인한 route ID 40개”를 모두 다시 쓰는 대신 “40회 확인, 성공/실패
요약, 전체 목록 hash”를 보낸다. 의미가 바뀌면 hash도 바뀌므로 중복 방지 경계는 유지된다.

### 같은 Pro 대화의 실제 후속 실행

아래 pass는 새 대화나 새 세션이 아니라 기존 conversation
`6a8db0ad-8ed0-83e8-888e-dce26c950343`의 exactly-once 후속 실행이다.

```text
Pass 18 PUBLIC_GAP_CLOSURE  facts +0 / routes +6 / accepted 57
Pass 19 SATURATION_AUDIT    facts +0 / routes +0 / 질문 5개 재개방
Pass 20 PUBLIC_GAP_CLOSURE  facts +4 / routes +8 / accepted 61
Pass 21 PUBLIC_GAP_CLOSURE  facts +4 / routes +8 / accepted 63 (검문 통과 +2)
Pass 22 PUBLIC_GAP_CLOSURE  facts +3 / routes +7 / accepted 66 (검문 통과 +3)
Pass 23 PUBLIC_GAP_CLOSURE  현재 RESEARCH_RUNNING / submit_count 1
```

Pass 23 직전 deterministic 상태:

```text
mandatory questions                28
nonterminal                         3
public material gap                 2
source linkage incomplete           1
verifier repair pending              1
provider/parser core pending         0
lifecycle hard break pending         0
accepted facts                      66
```

Pass 20~22는 accepted fact와 남은 gap이 실제로 변했으므로 동일 prompt 무한 재전송이 아니다.
progress hash가 같고 의미 진전이 없으면 기존 dedup 경계가 새 전송을 막는다.

현재 코드 검증:

```text
수정 직접 회귀       90/90 PASS
전체 unittest        7,754 PASS / failure·error 0 / skipped 38
compileall           PASS
git diff --check     PASS
Pro-first static     PASS / critical 0
Pro-first V2 static  PASS / critical 0
fresh efficiency     PASS / critical 0
production static    PASS / critical 0
```

기계 판독 영수증은
`p12_pass17_fail_closed_and_saturation_resume_receipt.json`에 기록했다. Pass 23과 최종
full-thesis가 아직 끝나지 않았으므로 이 영수증은 `completion_claimed=false`다.

## P7 최종 CI 봉인

`fdf4ac402861db2c12be2eeeafa7c24727e59f3c`를 checkout한 세 GitHub 실행이 모두
완료됐다.

```text
push E2R Pro-first verification
https://github.com/Daikisong/stock_agent/actions/runs/32881804962
SUCCESS / full regression 7,683 tests / failure·error 0

PR E2R Pro-first verification
https://github.com/Daikisong/stock_agent/actions/runs/32881810946
SUCCESS / full regression 7,683 tests / failure·error 0

PR E2R v6 operational cutover verification
https://github.com/Daikisong/stock_agent/actions/runs/32881811183
SUCCESS / Gate 1 receipt·production static audit·7,683 tests PASS
```

따라서 P7은 로컬 영수증만 통과한 상태가 아니라 GitHub의 별도 checkout에서도 전체
회귀를 통과한 상태로 봉인한다.

## P8 독립 cross-archetype fresh 경계

C17 `011170 롯데케미칼`과 C28 `053800 안랩`에는 C06처럼 실제 old repair-heavy job이
없다. 기존 `FreshSessionBoundaryService.start()`를 그대로 쓰면 old job의 종목을 상속하므로,
C06 job을 부모로 넣을 경우 011170을 요청해도 000660 패킷이 만들어지는 잘못된 실행이 된다.

이를 피하려고 다음 경계를 추가했다.

```text
INDEPENDENT_CROSS_ARCHETYPE_CANARY
→ symbol/company/as_of/archetype를 새 candidate와 job에 직접 결박
→ 가짜 frozen old job 생성 0
→ C06 old answer·score·Stage 입력 0
→ 새 runtime/job/run/pass/conversation 요구 유지
→ 기존 대화 화면에는 입력하지 않고 new-chat route로 이동 후 exactly-once submit
```

쉬운 예로 C17 실행은 “C06 문서를 지운 사본”이 아니다. 처음부터 `011170 / 롯데케미칼 /
C17`인 빈 fresh job을 만들고, old-answer deny 목록은 비어 있는 상태로 시작한다.

실행 전 검증:

```text
independent target/boundary regression          PASS
Linux V2.1 non-browser focused                  72/72 PASS
Windows Playwright fresh browser+orchestration  21/21 PASS
Pro-first V2 static audit                       PASS / critical 0
Pro-first production static audit               PASS / critical 0
compileall / git diff --check                    PASS
```

다음 실제 전송 순서는 C17을 별도 새 대화에서 먼저 닫고, 그 결과가 efficiency gate를
통과한 뒤 C28을 또 다른 새 대화에서 실행하는 것이다. 두 실행 모두 점수·Stage 권한은 없다.

## P0 — old repair-heavy run 봉인

봉인 대상:

```text
job              PROJOB-cdd91020f15891533e61431f
run              PRORUN-a7dacadb7088fc23535bfdde
conversation     6a8b09c3-bfcc-83ee-b15b-9f76eca52249
target/as_of     000660 / 2026-08-23
archetype        C06_HBM_MEMORY_CUSTOMER_CAPACITY
frozen_at        2026-08-24T19:28:25.387533Z
```

마지막 in-flight pass15는 새 Goal을 받기 전에 이미 `submit_count=1`이었다. 지시대로 결과를
한 번만 capture하고 deterministic import/receipt까지만 수행했다. 이후 old conversation에
새 입력은 없었다.

```text
last pass          PROPASS-5cafcd69a1577739808ba25b
status             COMPLETE
response hash      570484b5d4d46921c2aa6bf064d768f7d4b3637e4cf6dcc3496302ab38d1e27e
repair candidates  6
withdrawn          2
unresolved         4
effective facts    69
questions/routes   28 / 211
snapshot           PRODOSSIERSNAPSHOT-05656ec8f80ad8d8e58fb94d
dossier hash       6e6fcc84784ba93be41589689e5f0c2d6952078396d016de33ae5ff22f83c675
```

old job의 canonical 의미:

```text
OLD_V2_REPAIR_HEAVY_DIAGNOSTIC_RUN
SUPERSEDED_BY_FRESH_SESSION_EFFICIENCY_VALIDATION
NOT_OPERATIONAL_EFFICIENCY_PROOF
```

SQLite `pro_research_jobs`에 다음 immutable transition state를 추가했다.

```text
old_job_frozen_at
superseded_by_fresh_job_id
```

현재 successor는 아직 만들지 않았으므로 `superseded_by_fresh_job_id=null`이다. P6에서 완전히
새 job/conversation이 만들어질 때 same target/as_of를 검사한 뒤 결박한다.

## 권한 차단

freeze 뒤 다음 세 경로를 모두 막는다.

```text
initial job claim_submit
follow-up plan / prepare
follow-up ledger claim_submit
```

실제 old DB에서 재검증한 결과:

```text
freeze 시 initial submit                  1
freeze 시 follow-up submit               10
freeze 이후 새 submit                     0
old follow-up plan             TransportPendingDecision
reason                         SUPERSEDED_BY_FRESH_SESSION_EFFICIENCY_VALIDATION
```

쉬운 예로 기존 대화는 삭제한 것이 아니라 “읽기·감사용 보관함”으로 잠갔다. 남은 4개를 같은
대화에 또 묻는 버튼은 코드의 계획 단계와 최종 전송 단계 양쪽에서 모두 잠긴다.

## runtime 보존과 Git 경계

runtime receipt:

```text
C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\live_v2\20260823T145430Z\
jobs\PROJOB-cdd91020f15891533e61431f\fresh_session\old_run_freeze_receipt.json
```

```text
logical receipt hash  2e3daa189aa98b38dacd978cafdb744b1e8e7d6069362f869b0a35cdb0338d3d
file SHA-256          597f0924056d6a3def2b99aa35f7578ff14654859179135a47f4c551468b89ae
runtime_preserved     true
```

원문 Pro 보고서, fetched document, SQLite, screenshot은 runtime에 그대로 보존한다. Git에는
원문을 복제하지 않고 외부 검수에 필요한 ID, hash, 수치, 의미, 테스트만 기록한다.

## 검증

```text
new P0 freeze tests                         3/3 PASS
parser/live/repair/static focused          63/63 PASS
Windows mock browser multi-pass E2E        PASS
freeze CLI idempotent replay               PASS
actual old plan blocked                    PASS
```

Windows 전체 live-runtime 묶음에서 `git rev-parse`가 WSL UNC 경로를 repository로 인식하지
못한 환경 오류는 코드 회귀로 세지 않는다. 같은 테스트는 Linux에서 통과했고 실제 browser
mock test는 Windows 환경에서 성공했다. 최종 판단은 push 뒤 Linux GitHub Actions 결과로 한다.

## P1 — rejection taxonomy

old runtime의 전체 rejection register를 삭제·샘플링하지 않고 읽어 다음을 생성했다.

```text
old_run_rejection_taxonomy.json
old_run_rejection_taxonomy.md
```

append-only snapshot의 register 302행을 `candidate_id + original_candidate_hash`로 결박해
고유 후보 74개로 환원했다. 원문 statement와 quote는 runtime에만 두고 Git 문서에는 식별자,
canonical source document ID, 원인, routing, generic 수정 위치, regression test ID만 넣었다.

```text
고유 rejection                               74
A INITIAL_PROMPT_OUTPUT_DEFECT               50 / 67.57%
B LOCAL_NORMALIZATION_OR_VERIFIER_DEFECT      24 / 32.43%
C GENUINE_SEMANTIC_OR_SOURCE_DEFECT            0 / 0.00%
같은 source가 반복된 후보                    63 / 17 source groups
중복 mechanical rejection                     8
old audit에서 확인된 genuine semantic repair   0
```

가장 큰 원인은 source 부족이 아니라 lifecycle 계약이었다. `UNSUPPORTED_DERIVATION` 38건은
모두 `current_status=UNKNOWN`이어서 old lifecycle bridge가 `UNVERIFIED_PENDING`으로 만든
후보였다. 쉬운 예로 “소송이 해결됐다”는 resolution fact를 가져왔는데 상태 필드가 비어 있으면,
자료를 다시 찾을 문제가 아니라 V3가 `RESOLVED/OPEN/...` 중 하나를 반드시 출력하게 해야 한다.

다음 24건은 Pro에게 다시 물으면 안 되는 로컬 결함이다.

```text
nonissuer subject alias/scope resolver       14
compact repair segment/product 상속           5
same-source quote representation              2
unavailable source representation             3
```

C가 0이라는 수치는 old fact가 전부 의미적으로 정답이라는 뜻이 아니다. old verifier가 A/B에서
먼저 막았기 때문에, P2~P4 수정 뒤 fresh run의 재검문에서 실제 C가 새로 드러날 수 있다.
그때만 compact Pro semantic repair에 보낸다.

검증:

```text
taxonomy unit test                           3/3 PASS
고유 candidate / required field             74/74 PASS
original_candidate_hash binding             74/74 PASS
원문 statement/quote Git 복제                0 PASS
deterministic CLI replay                     PASS
```

## P2 — ResearchDossierV3

source document와 atomic fact를 분리하는 append-only `ResearchDossierV3`를 구현했다.

```text
SourceDocumentV3 1개
├─ AtomicFactV3 N개 (각각 predicate/quote/locator 1개)
└─ SourceLineageV3 1개

DerivedMetricV3
└─ input_fact_ids로만 원천 fact를 참조
```

old taxonomy의 가장 큰 A 결함 38건을 막기 위해 V3 lifecycle에서 `UNKNOWN`을 제거했다.
`CURRENT|OPEN|RESOLVED|SUPERSEDED|HISTORICAL_ONLY` 중 하나가 아니면 schema 단계에서
거절된다. old B 결함처럼 compact replacement가 segment/product를 잃는 것도 V3에서는
빈 값이 schema를 통과하지 못한다.

추가 deterministic graph gate:

```text
fact 안 source URL 반복                          금지
fact 안 derived metric 혼합                     금지
source/predicate/subject/excerpt 동일 중복       금지
tracking canonical URL / fragment                금지
publication/availability/event 미래누수          금지
source document/fact/lineage roster 불일치        금지
fact_kind/collection 또는 question binding 불일치 금지
failed verifier_preflight                        금지
```

provider failure는 예외적으로 빈 evidence graph + `PROVIDER_PENDING`으로 보존한다. 이는
0점이나 정상 점수 확정이 아니다.

V1/V2 schema·validator는 그대로 등록해 read/verification compatibility를 유지했다. 새 V3
transport binding은 최초 conversation placeholder와 durable pass receipt만 바꾸며 fact,
quote, source document는 바꾸지 않는다.

검증:

```text
V3 schema/evidence graph test                   13/13 PASS
P0/P1 + 기존 V1/V2 focused regression          99/99 PASS
기존 dossier parser/import regression           16/16 PASS
합계                                            128/128 PASS
JSON Schema Draft 2020-12 self-check            PASS
compileall / git diff --check                    PASS
```

상세 계약은 `research_dossier_v3_contract.md`에 기록했다.

## P3 — Initial Prompt V3와 36-contract compiler

master goal의 Initial Full Research Prompt V3를 별도 template으로 추가했다. V2 template과
compiler는 바꾸지 않았으므로 기존 receipt와 snapshot의 의미도 유지된다.

실제 V3 initial prompt는 다음을 동적으로 결합한다.

```text
공통 verifier-ready base prompt
+ target / as_of_date / ResearchPacketV3 context
+ 선택된 primary contract 1~3개
+ 모든 실제 job에 붙는 R13 cross guard 4개
+ mandatory question / source role policy
+ exact ResearchDossierV3 JSON Schema
```

쉬운 예로 C06 한 개를 선택하면 C06 질문과 공통 R13 질문만 들어간다. C17 질문은 들어가지
않는다. C06 전용 검색어나 HBM 전용 규칙은 template/compiler에 없고, C17이나 C28도 같은
코드가 해당 contract를 읽어 prompt를 만든다.

V3 compiler의 강제 경계:

```text
입력 packet schema                  e2r_pro_research_packet_v3만 허용
primary contract                    1~3개
R13 cross guard                     실제 job마다 4개 자동 부착
output                              exact e2r_pro_research_dossier_v3 schema
atomic evidence                     16개 공통 규칙
verifier_preflight                  9 true + derived 혼합 false
score_authority / stage_authority   false
gold/expected/future outcome input  compile 전에 거절
initial prompt hard boundary        100,000 characters
```

36개 canonical contract마다 tracked snapshot을 다시 만들고 deterministic audit JSON/Markdown을
함께 게시했다. primary 32개 snapshot은 실제 one-primary job과 똑같이 R13 4개를 포함하고,
R13 4개 snapshot은 contract 자체의 unit coverage를 확인하는 감사 전용이다.

```text
36/36 compile                        PASS
mandatory question missing           0
atomic contract missing              0
verifier preflight missing           0
derived metric separation missing    0
forced COMPLETE                      0
score/Stage leakage                  0
other-archetype question pollution   0
source role policy missing           0
output V3 schema missing             0
prompt over 100k                     0
prompt size range                    34,909~57,956 chars
```

검증:

```text
P3 전용 regression                   10/10 PASS
P0/P1 + dossier import + V2/V3/P3    64/64 PASS
36 snapshot audit CLI                PASS / critical 0
production static audit              PASS / critical 0
git diff --check                     PASS
```

더 넓은 local Pro-first discovery도 실행했지만 Playwright 사용 묶음은 test body 전에 Linux
`libnspr4.so` 부재로 browser process를 시작하지 못했다. 이는 P2에서 기록한 같은 host 환경
제약이며 P3 코드 실패로 PASS에 포함하지 않았다. push 뒤 의존성을 설치하는 GitHub Actions를
최종 외부 실행 기준으로 확인한다.

이 단계에서는 fresh ChatGPT conversation을 만들거나 Pro에 전송하지 않았다. 따라서 P3
PASS는 “Pro 답변이 좋았다”는 뜻이 아니라 “최초 요청부터 verifier가 읽을 구조를 모든
contract에 동일하게 요구한다”는 뜻이다.

## P4 — Local Evidence Preflight

`ResearchDossierV3`를 source verifier에 바로 넘기지 않고 다음 경계를 강제했다.

```text
V3 사전 정규화
→ URL/source representation/text/alias/scope/date/atomic fact preflight
→ deterministic source verifier
→ rejection root-cause classifier
```

V3의 canonical source/fact 분리는 유지하면서 기존 verifier만 읽는 projection을 별도로 만든다.
preflight가 가져온 원문은 verifier가 다시 fetch하지 않는다. V3가 preflight를 우회해 verifier를
직접 호출하면 명시적으로 실패한다.

로컬에서 닫는 대표 사례:

```text
tracking URL/fragment/query/trailing slash
redirect final URL
CRLF/HTML entity/Unicode quote·dash·whitespace
issuer 및 주입된 publisher alias
V2/V3 field, source ID, lineage ID alias
segment/product closed enum
published date와 HTTP Last-Modified 충돌
동일 official lineage의 alternate representation
```

quote는 byte/Unicode/locator/alternate official representation의 literal exact 순서만 허용한다.
semantic similarity로 검문을 통과시키지 않는다. compound fact도 각 part에 독립 literal quote
span이 있을 때만 쪼갠다.

모든 verifier rejection은 5개 root cause 중 하나로 분류한다.

```text
LOCAL_NORMALIZABLE
SOURCE_REPRESENTATION_RESOLVABLE
INITIAL_PROMPT_OUTPUT_DEFECT
GENUINE_SEMANTIC_OR_SOURCE_DEFECT
NONMATERIAL_AUXILIARY_REJECTION
```

앞의 두 분류는 Pro 전송이 항상 0이다. 현재 P4는 분류·영속 receipt까지만 구현했으며 실제
compact repair 전송은 P5 범위다.

영속 runtime 산출물:

```text
verification/preflight/research_dossier.preflight.json
verification/preflight/verifier_projection.json
verification/preflight/preflight_operations.jsonl
verification/preflight/preflight_issues.jsonl
verification/preflight/preflight_receipt.json
verification/rejection_classifications.jsonl
```

상세 설계와 외부 검수용 경계는 `local_evidence_preflight.md`에 기록했다. 이 단계에서도 fresh
ChatGPT conversation 생성, browser 전송, 새 web search는 하지 않았다.

검증:

```text
P4 local preflight regression                 17/17 PASS
영속 V3 preflight → verifier lifecycle         PASS
P0~P4 + dossier import + source verifier       91/91 PASS
production static audit                        1/1 PASS / critical 0
focused 합계                                  92/92 PASS
compileall / git diff --check                   PASS
실제 Pro·query·search 호출                      0/0/0
```

P3 head `d5d62bc2`의 GitHub Actions는 P4 커밋 직전에도 장시간 `in_progress`였고 실패로
판정되지 않았다. P4 push로 새 head CI를 시작하며 그 결과는 다음 phase 장부에서 head SHA와
run URL로 이어서 기록한다.

## P5 — Compact RepairDeltaV3

기존 V2 old-run repair 경로는 과거 receipt 호환을 위해 그대로 두고, V3 전용 compact repair를
별도 경로로 추가했다. 새 경로는 전체 dossier를 prompt/response에 다시 넣지 않는다.

```text
P4 rejection classifications
→ Pro-repairable material candidate만 선택
→ same source + same root cause + same question scope grouping
→ RepairDeltaV3 prompt
→ CORRECT|REPLACE|NARROW|WITHDRAW
→ V3 graph validation
→ local preflight
→ deterministic source reverification
```

prompt와 output의 강제 경계:

```text
target prompt chars                        <= 60,000
hard max                                   <= 100,000
hard 초과 transport batching 성공 처리        금지
full dossier re-output                     0
accepted fact delete/modify                 0
score/Stage authority                       false/false
repair pass ordinal                         1만 허용
```

`fetched_excerpt`는 반려된 claimed quote가 아니라 실제 fetched source에서 literal locator로
잘라낸 문장이다. locator도 없으면 빈 값이며 semantic similarity로 문장을 만들지 않는다.

`WITHDRAW`는 replacement 없이 public gap을 다시 열고, `CORRECT/NARROW/REPLACE`는 새 atomic
fact와 current-pass route receipt를 요구한다. replacement는 Initial V3 preflight 계약을 그대로
만족해야 하며 full effective dossier graph validation과 source verifier를 모두 다시 통과해야 한다.
repair 전 accepted fact는 hash가 동일해야 하고 재검문에서도 accepted여야 한다.

새 source lineage의 independence group은 publisher + URL host로 보수적으로 생성해 같은
publisher의 여러 문서를 독립 증거로 부풀리지 않는다.

영속 runtime 산출물:

```text
repair_v3/compact_repair_prompt.md
repair_v3/compact_repair_prompt_receipt.json
repair_v3/repair_delta_v3.json
repair_v3/repair_actions.jsonl
repair_v3/reverification_rows.jsonl
repair_v3/research_dossier.repaired.json
repair_v3/compact_repair_receipt.json
```

검증:

```text
P5 compact RepairDeltaV3 regression            13/13 PASS
P5 + legacy V2 repair + P4 + source verifier   77/77 PASS
production static audit                          1/1 PASS / critical 0
focused 합계                                    78/78 PASS
compileall / schema self-check / diff check       PASS
실제 Pro·query·search 호출                        0/0/0
```

상세 설계는 `compact_repair_delta_v3.md`에 기록했다. 현재 P5 서비스는 deterministic
compiler/parser/apply/reverify까지 완성했지만 browser pass에 아직 연결하지 않았다. 따라서
실제 fresh Pro 전송은 여전히 0이다.

## P6 — Fresh-session orchestration

old conversation을 새 prompt의 답안지로 재사용하지 못하도록 runtime/job/run/pass/conversation
identity를 하나의 경계로 묶었다.

```text
frozen old job
→ disjoint fresh runtime root
→ fresh_session_id가 포함된 새 candidate/job
→ ResearchPacketV3 blind leakage audit
→ ChatGPT new-chat route에서 V3 packet/prompt 준비
→ user approval 뒤 exactly-once initial submit
→ old와 다른 conversation ID 확인
→ same-conversation bounded follow-up scope
```

ResearchPacketV3에는 old fact, route, rejection, question answer, score/Stage, expected URL/fact ID를
담는 필드가 없다. 별도 `OldAnswerLeakageManifest`의 exact identity/token도 packet과 initial prompt에서
다시 세어 0이 아니면 browser 준비 전에 실패한다.

새 대화가 아닌 `/c/<old-id>`에서 준비하려 하면 입력 전에 `USER_ATTENTION_REQUIRED`로 돌아간다.
사용자가 new-chat route로 이동한 뒤에는 submit_count 0인 같은 packet/prompt만 재준비할 수 있다.
전송 뒤 old conversation ID가 다시 나오면 그 fresh run을 diagnostic-only로 봉인하고, 새
fresh_session_id/runtime/job/run/pass를 가진 successor만 허용한다.

initial approval이 허용하는 operational tail:

```text
public-gap/counter closure     합쳐서 0~1회
semantic RepairDeltaV3        0~1회
saturation                    1회
```

두 번째 repair/gap/saturation은 같은 conversation을 길게 끌지 않고
`NEW_CONVERSATION_REQUIRED`로 차단한다. compact repair response는 MD attachment가 없어도 화면의
`E2R_REPAIR_DELTA_JSON_BEGIN/END`를 production adapter가 완료 결과로 capture한다.

production adapter mock E2E:

```text
old frozen → fresh V3 initial → local preflight → compact repair → saturation
initial DOM submit                 1
repair DOM submit                  1
saturation DOM submit              1
old conversation submit            0
모든 fresh pass same conversation  true
모든 pass submit_count             1
```

검증:

```text
P6 fresh identity/orchestration regression       13/13 PASS
P6 production adapter browser E2E                 1/1 PASS
large prompt DOM integrity + V2 browser regression 3/3 PASS
P0~P6 phase regression                            60/60 PASS
전체 Pro-first regression                         447/447 PASS
실제 Pro·query·search 호출                         0/0/0
```

상세 설계와 runtime receipt는 `fresh_session_orchestration_v3.md`에 기록했다. P6는 offline
orchestration proof이므로 아직 000660 initial acceptance 80%나 score/Stage를 주장하지 않는다.

## 다음 단계 P7

로그인된 사용자 전용 E2R Chrome/CDP의 ordinary Chat + visible Pro mode에서 완전히 새 conversation을
만들고 000660 / `as_of_date=2026-08-23` / C06+R13 fresh blind packet을 정확히 한 번 전송한다.
initial result에 local preflight와 source verification을 적용해 acceptance ratio를 계산한다. 80%
미만이면 repair로 메워 PASS하지 않고 해당 conversation을 diagnostic-only로 봉인한다.

## P7 live 실행 장부 — fresh initial 1회

마스터 Goal의 사용자 승인 범위에 따라 ordinary Chat + visible Pro mode에서 실제 fresh canary를
시작했다. 기존 대화에 follow-up을 보내지 않았고, 새 conversation을 만든 뒤 initial prompt를
정확히 한 번만 제출했다.

```text
runtime          C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260824T221229Z
fresh session    FRESH-V2-1-C06-20260824T221229Z
fresh job        PROJOB-ee3f7609d478547f60e3aff8
fresh run        PRORUN-886983514379a2248fe03d3c
initial pass     PROPASS-fe8dc97296863bea30fb5151
durable transient conversation WEB:08326745-1438-42bb-a18b-9355869dab22
visible canonical conversation 6a8cc4ce-095c-83e8-b375-8d40084b818e
old conversation 6a8b09c3-bfcc-83ee-b15b-9f76eca52249
submit count     1
capture count    0 (연구 완료 대기 시점)
current status   RESEARCH_RUNNING
```

blind packet과 prompt 경계:

```text
packet hash                     dcefe680d4f0d079e6af236e7e8744ef21f0afbeac8187935d191fb292bf3712
prompt hash                     a0d4a9a98d255b82fe2db641cfbe1a3c6889226b68d0c6ce837e7e62db981ecc
prompt chars                    58,648
packet old-answer leakage       0
old score/Stage leakage         0
mandatory question families     28
score/stage authority           false/false
```

첫 prepare 시 ChatGPT의 과거 오류 toast 때문에 send-ready 판정이 30초 안에 끝나지 않아
`USER_ATTENTION_REQUIRED`로 안전 정지했다. 이때 `submit_count=0`이었다. 동일 브라우저 draft의
prompt hash와 첨부 File SHA-256을 다시 검증해 새 upload나 composer 입력 없이 복구했고,
그 뒤 제출 횟수는 정확히 1이 됐다. 쉬운 예로 서류가 접수 창구에 이미 놓여 있는지를 hash로
확인한 뒤 접수 버튼만 한 번 누른 것이며, 같은 서류를 두 번 올리지 않았다.

제출 직후 ChatGPT UI가 임시 `WEB:...` 대화 ID를 사용하다 정식 `/c/<id>` URL로 전환하는 것도
live에서 확인했다. 감시 프로세스를 브라우저 연구와 분리해 종료하고, `submit_count=1`을 요구하는
no-submit recovery 경로를 추가했다. 완료 결과 안의 exact job/run marker와 report hash가 모두
맞을 때만 정식 conversation ID로 재결박한 뒤 capture한다. 이 복구 경로에는 upload, composer
입력, DOM send가 없다.

live 실행에 앞서/실행 중 확인한 회귀:

```text
fresh efficiency + orchestration unit tests       19/19 PASS
Windows production adapter browser E2E             2/2 PASS
prepared draft no-mutation recovery browser E2E     1/1 PASS
submitted packet reuse regression                    PASS
transient→canonical conversation rebind regression  PASS
현재 live 새 conversation 확인                       PASS
현재 live exactly-once submit                        PASS (1)
```

이 장부는 중간 상태다. Pro 응답 capture, DossierV3 import, local preflight, source verification과
초기 material acceptance 80% gate가 끝나기 전에는 P7 PASS나 score/Stage를 선언하지 않는다.

## P7 fresh initial 최종 판정 — 1차 conversation은 diagnostic-only

2026-08-25에 첫 fresh initial의 완료 결과를 캡처하고 initial efficiency gate까지 실행했다. 이
conversation은 P7 PASS가 아니다. 마스터 Goal 13~14절에 따라 낮은 acceptance를 repair로 메우지
않고 diagnostic-only로 봉인했다.

```text
visible mode                    ordinary Chat + visible Pro
canonical conversation         6a8cc4ce-095c-83e8-b375-8d40084b818e
submit / capture               1 / 1
additional browser send        0
mandatory questions            28 / 28
serialized source documents    0
serialized material facts      0
accepted material facts        0
initial acceptance             0.0%
source verifier fetch          0
query / search                 0 / 0
score / Stage authority        false / false
score receipt / Stage receipt  없음 / 없음
gate                           FAIL
failure reasons                NO_INITIAL_MATERIAL_CANDIDATES,
                               INITIAL_ACCEPTANCE_RATIO_BELOW_80_PERCENT
publication                    withheld
new conversation required      true
```

Pro가 조사 내용을 전혀 만들지 않은 것은 아니다. 화면 보고서에는 28개 question 판정, 공식 issuer·
경쟁사·시장자료에 대한 서술, 11개 공개/비공개·parser/provider gap, self-audit가 들어 있다. 다만
Pro가 마지막에 exact excerpt 총량을 자체 점검하다 한 단어 초과를 발견했다고 서술한 뒤, 유효한
`E2R_RESEARCH_DOSSIER_JSON_BEGIN/END` 블록과 fact별 excerpt–URL 결박을 출력하지 않았다. 쉬운 예로
조사 메모는 도착했지만 각 주장에 원문 문장과 출처를 붙인 증빙 명세서는 제출되지 않은 상태다.

사람이 읽을 수 있는 모든 보고서 내용은 버리지 않았다.

```text
raw visible report chars                 8,817
normalized report chars                  9,379 (파일 newline 포함 9,380)
visible citation href registry           3
reported material/source/route counts    28 / 18 / 122
serialized usable material facts         0
question results preserved               28
explicit unresolved gaps preserved       11
```

Codex structurer는 새 검색이나 점수 판단 없이 완료 보고서만 읽어 V3 representation을 만들었다.
보고서에 exact excerpt와 explicit URL이 fact 단위로 함께 있지 않은 주장은 material fact로 만들지
않고 question result와 unresolved gap으로 보존했다. 따라서 0개는 “Pro의 모든 설명을 폐기했다”는
뜻이 아니라 “검증 불가능한 설명을 점수 사실로 몰래 승격하지 않았다”는 뜻이다.

live에서 확인된 generic 결함과 조치는
`p7_fresh_initial_failure_taxonomy.md`에 기록했다. 핵심 수정은 다음과 같다.

```text
완료 보고서에 JSON block 없음       → readable report + citation registry를 원문 보존 capture
보고서 representation 복구           → Codex-only structurer, browse/fetch/score/Stage 금지
fact roster 0에서 mapper 예외         → provider 호출 없이 zero-count verification receipt
post-capture verifier 재개             → 브라우저를 다시 열지 않고 immutable capture에서 재개
post-import USER_ATTENTION 재개        → 기존 import ledger 재사용
중단된 중복 import timestamp drift     → evidence 필드 동일할 때 durable ledger timestamp로 복구
```

첫 run의 canonical receipts:

```text
capture source                  DIRECT_REPORT_DOM_NORMALIZED
capture report SHA-256          8ae172543c9a2beba7ec98937efca00c3989a7b73cac3608b1b16dae2c22848c
browser result SHA-256          dd595f8e27c58e22a72e37677adee2b46d231ba81d6080987ba56312a07d2efa
dossier snapshot SHA-256        0c0a4a2fae10db5cea7166ab9db6c20bdfc466fecbcda3f8b5c59b075af5ce9b
efficiency receipt SHA-256      8e751564ceb0f03b0c92015a4ea268c5cffd6a6d0aa129fb40dc2a7927fb4160
source verification semantics  e2r_pro_source_verification_v10
current durable state           GAP_ADJUDICATION + old_job_frozen_at set
```

root-cause prompt patch는 모든 아키타입 공통 Initial Prompt V3에 적용했다. self-audit 오류나 응답
길이 압력이 있어도 dossier 전체를 생략하지 않고, 문제가 있는 fact만 gap으로 내린 뒤 유효한 JSON을
먼저 보장하도록 했다. C06·000660 전용 문구는 추가하지 않았다. 36개 prompt snapshot을 다시 만들었고
compile/오염/누수/길이 critical은 0이다.

다음 P7 시도는 같은 conversation의 repair가 아니다. 새 runtime, fresh_session_id, job, run, pass,
ChatGPT conversation을 사용한 blind fresh rerun이어야 한다. 새 run이 initial acceptance 80%를
통과하기 전에는 C17/C28, 점수, Stage, 운영 준비를 진행하지 않는다.

커밋 전 검증:

```text
fresh/structurer/import/source/prompt 집중 회귀       83/83 PASS
변경된 Windows Playwright browser 회귀                3/3 PASS
Initial Prompt V3 canonical snapshot                 36/36 PASS
Pro-first V2 requirement static audit                PASS / critical 0
Pro-first production static audit                    PASS / critical 0
Python compileall / git diff check                    PASS / PASS
```

WSL 전체 Pro-first discovery에서는 463개 중 browser-dependent 60개가 동일하게 `libnspr4.so` 부재로
시작하지 못했고 나머지 403개는 통과했다. 이는 코드 assertion 실패가 아니라 WSL Chromium 실행환경
문제다. 변경으로 영향을 받은 browser assertion 3개는 Playwright가 설치된 Windows Python에서 다시
실행해 모두 통과했다.

GitHub의 최신 보존 head `05cb9726cfa3f451cf3df8c5be1d097b5c205552`에서도 독립 Linux CI를
확인했다.

```text
E2R Pro-first verification (push)         SUCCESS  run 32793935843
E2R Pro-first verification (PR)           SUCCESS  run 32793940414
E2R v6 operational cutover verification   SUCCESS  run 32793940623
core-unit / browser-mock / full-regression / static-security   모두 SUCCESS
PR #7                                      Draft / OPEN / MERGEABLE
local HEAD == origin branch                true
```

1차 fresh job은 원래 live runtime의 중앙 SQLite 장부에 기록되지만, 그 job의 report와 receipt는
1차 fresh runtime에 있다. 따라서 2차 successor는 서로 다른 두 위치를 함께 써야 한다.

```text
predecessor artifact root  = 1차 fresh runtime
durable state database     = 원래 live runtime/pro_first.sqlite3
successor artifact root    = 완전히 새로운 2차 fresh runtime
```

이를 위해 live runner/CLI에 optional `state_database_path` 경계를 추가했다. 기본값은 기존과 같아
호환성을 유지하고, successor일 때만 중앙 장부를 명시한다. 쉬운 예로 이전 시험 답안지는 1차 서랍에서
읽되, 수험번호 장부는 계속 중앙 금고에서 읽고, 새 답안은 2차 빈 서랍에 쓰는 구조다. 세 위치를
섞거나 복사하지 않는다. 분리 경로 회귀를 포함한 orchestration test는 `18/18 PASS`다.

## P7 최종 — 2차 fresh C06 initial efficiency PASS

1차 diagnostic-only run을 predecessor로 봉인한 뒤 새 runtime/session/job/run/pass/conversation에서
blind fresh initial을 다시 실행했다. 초기 prompt에는 1차 fact, URL, question 답, score, Stage를
넣지 않았으며 submit/capture는 각각 정확히 한 번이다.

```text
runtime          C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260825T150833Z
fresh session    FRESH-V2-1-C06-20260825T150833Z
fresh job        PROJOB-ab48ce7e94097cf9b6846602
fresh run        PRORUN-683f5a5423a6e367f443c6de
initial pass     PROPASS-e49762cc3ad556d6b211d92b
conversation     6a8db0ad-8ed0-83e8-888e-dce26c950343
assistant turn   request-WEB:a63d3897-9bd3-4749-996d-52a56adc7a89-0
submit/capture   1 / 1
```

### visible JSON 산출물 복구

Pro는 응답 본문에 0-fact 실패 결과를 낸 것이 아니었다. 본문에는 응답 길이를 줄인 transport manifest를
두고, 같은 assistant turn에 전체 `ResearchDossierV3` JSON 파일을 visible attachment로 제공했다.
기존 adapter가 `.md/.pdf`만 찾았기 때문에 inline manifest를 전체 dossier로 오인했다.

generic 수정은 종목명이나 파일명을 하드코딩하지 않는다.

```text
inline V3가 expanded_artifact_required_for_verification=true 선언
→ sandbox:/mnt/data/<safe-json-basename> exact reference 검사
→ 같은 conversation + 같은 assistant turn + 같은 filename 1개만 선택
→ visible download control 사용
→ 기존 capture/incoming과 READY는 변경하지 않음
→ capture/supplemental에 별도 JSON + receipt + READY를 written-last로 봉인
→ job/run/target/as_of/conversation/turn/capture receipt/report hash/count 결박
→ browser submit delta=0일 때만 importer가 expanded JSON 선택
```

쉬운 예로 본문은 “전체 명세서는 동봉 파일에 있다”는 운송장이었고, JSON은 실제 명세서였다. 기존
운송장 봉인을 뜯어 바꾸지 않고 동봉 파일에 별도 인수증을 붙였다. 첨부 READY가 없거나 다른 turn,
파일명, hash, 선언 수량이면 0-fact 본문을 import하지 않고 fail-closed한다.

실제 attachment/result:

```text
downloaded bytes                  169,993
expanded source documents         16
expanded facts                    25 (material 18 / counter 5 / resolution 2)
derived metrics                   3
mandatory question results        28
search route receipts             37
unresolved gaps                   12
post-cutoff / duplicate credit    0 / 0
browser submit delta              0
expanded dossier SHA-256          e32c98c78934c2d62c39cbec67d11032948269e62d086a0cdf418dcc7153c1a0
supplemental receipt hash          108ca7596c88bf05c61cbedcf908d73c3db136ca8531339fa07ecf1c8afa48e5
```

Pro가 marker 표기용 `PENDING_NEW_CONVERSATION`과 `NONE`을 JSON identity에 복사한 경우도 initial pass의
top-level/current pass row가 정확히 일치할 때만 로컬에서 canonical placeholder/null로 바꾼다.
follow-up의 `NONE`은 고치지 않고 lineage 오류로 막는다. evidence, quote, URL은 이 정규화가 바꾸지 않는다.

### initial source verification과 efficiency Gate

전체 25개 fact를 source verifier에 넣었고, Initial Gate의 분모인 material candidate는 18개다.
그중 16개가 accepted여서 `16 / 18 = 88.8889%`로 80% 기준을 통과했다. 낮은 비율을 repair로 메운
결과가 아니라 follow-up 전 initial artifact만으로 계산한 값이다.

```text
mandatory question coverage                 28/28
material candidate / accepted               18 / 16
post-preflight acceptance                    88.8889% PASS
all fact terminal                            25/25
accepted all-kind fact                       21
genuine semantic repair candidate            3 <= limit 5
initial prompt output defect                 0
local-normalizable sent to Pro               0
source-representation sent to Pro            0
source-document unbound material             0
question-unbound material                    0
tracking URL                                 0
multi-source atomic fact                     0
derived metric mixed fact                    0
query/search                                 0/0
old conversation new submit                  0
score/Stage authority                        false/false
publication                                  withheld
Gate                                         PASS
```

canonical hashes와 수치는 `p7_c06_fresh_initial_success_receipt.json`에 별도 기록했다. 원문 보고서,
전체 source/fact JSON, fetched document는 Git에 복제하지 않고 보존 runtime의 hash로 결박한다.

검증:

```text
expanded attachment fail-closed unit regression     5/5 PASS
preflight/fresh/import 포함 focused regression      60/60 PASS
Windows MD/PDF/capture browser regression           20/20 PASS
actual visible JSON download                         PASS
actual expanded import                               PASS
actual source verification                           PASS
actual C06 Initial Efficiency Gate                   PASS (88.8889%)
actual Pro extra submit                              0
Linux non-browser Pro-first regression              392/392 PASS
Windows real-browser Pro-first regression            79/79 PASS
split-platform Pro-first total                       471/471 PASS
failure / error                                        0 / 0
Pro-first V2 static audit                         PASS / critical 0
Pro-first production static audit                 PASS / critical 0
E2R v6 production static audit                    PASS / critical 0
Pro-first V2 audit hash                            f0eec38d973de9ae5b5c7b52b505ccdec9b9fd78a1fc749bee7b7ad8998e8acc
E2R v6 static audit hash                           5f4df78b1870afe90511928f88bc76eefc46095e5746b882e80c9f0a068c3b41
compileall / git diff check                        PASS / PASS
```

따라서 P7 verdict는 `PRO_FIRST_V2_1_C06_FRESH_SESSION_PASS`다. 이는 아직 7 component/21 Judge/score/
Stage나 multi-archetype 완료를 뜻하지 않는다. 다음 단계는 각각 새 conversation을 쓰는 P8 C17/C28
fresh initial canary다.

## P8 진행 — 독립 target 경계와 C17 최초 capture

P8은 C06의 종목·conversation·증거를 복사하지 않고 C17과 C28을 각각 완전히 독립된 target으로
시작해야 한다. 이전 구현은 predecessor job이 있는 successor만 만들 수 있었으므로, 과거 진단 job이
없는 target에는 가짜 old job을 만들지 않는 `start_independent` 경계를 추가했다.

쉬운 예로 C06 수험표에 종목명만 롯데케미칼로 바꿔 재사용하지 않는다. 롯데케미칼의 target ID,
아키타입, job, run, pass와 새 ChatGPT conversation을 처음부터 따로 만든다.

```text
boundary commit       f719b94b5bcf99aec6de7e785675ecd16be89b49
target identity test  PASS (old diagnostic job 생성 0)
Linux focused tests   72/72 PASS
GitHub push CI        SUCCESS  run 32884242262
GitHub PR CI          SUCCESS  run 32884248916
GitHub v6 CI          SUCCESS  run 32884248976
```

C17 actual fresh initial은 visible ChatGPT Pro에서 정확히 한 번 전송됐고 새 conversation에서 약 55분간
조사된 뒤 완료됐다. 결과는 inline JSON으로 보존됐으며 자동 재전송은 없었다.

```text
runtime          C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260825T183156Z
fresh session    FRESH-V2-1-C17-20260825T183156Z
fresh job        PROJOB-bd77f3912ada3fdc878330c6
fresh run        PRORUN-6d2c7188521024cf65e94101
initial pass     PROPASS-6de9211605df22e8d1e255ce
conversation     6a8ddfc4-f27c-83e8-829d-919ecb97c815
assistant turn   request-WEB:38f40b92-5b48-45bf-9f26-a853b4009662-0
submit/capture   1 / 1
automatic resend 0
report SHA-256   db1b50f30ee4070e69895b14529dc85abd8cbd288dcb6a55612b996b8a9b2090
dossier SHA-256  517c4af5e78253afda0fcf9b63006bc6329ff50a10c534c4bfde33549613c4a8
```

### C17 local representation 정규화

최초 import는 조사 부족이 아니라 표현 계층의 양방향 연결 불일치에서 fail-closed했다. Pro에 같은 내용을
다시 묻거나 종목별 예외를 넣지 않고, 증거를 절대 늘리지 않는 공통 정규화만 추가했다.

```text
nonissuer source보다 강한 fact issuer scope     true → false  1건
material fact를 counter 칸에서 중복 참조         참조 삭제      1건
fact 쪽 question backlink가 없는 question 참조  참조 삭제      5건
새 fact 생성 / fact kind 승격 / scope 상향       0 / 0 / 0
Pro follow-up / browser submit 증가               0 / 0
```

예를 들어 “공시 가격은 국제 기준가다”라는 중립 fact가 어떤 질문에서는 참고 근거이고 다른 질문에서는
낙관론의 제약처럼 읽힐 수 있다. 그러나 전역 종류가 `MATERIAL`인 fact를 question의 `counter_fact_ids`에
동시에 넣으면 저장 규격이 충돌한다. 로컬 정규화는 그 fact를 `COUNTER`로 바꾸거나 새 사실을 만들지 않고,
잘못된 question 참조만 제거한다. 원문 fact와 closure 설명은 그대로 남는다.

이 규칙은 모든 target에 동일하게 적용하며 알 수 없는 fact ID는 지우지 않는다. 알 수 없는 ID는 기존
strict validator가 계속 오류로 막는다. Initial Prompt V3에도 issuer/source scope 일치, fact kind별
question reference, fact→question backlink 규칙을 공통으로 넣어 36개 snapshot을 다시 만들었다.

현재 C17 exact capture의 parser→dialect adapter→pre-schema→identity binding→strict validator 결과:

```text
source documents             8
material/counter/resolution  9 / 8 / 3
all facts                    20
mandatory questions          26
search route receipts        26
strict graph validation      PASS
focused regression           72/72 PASS
Initial Prompt V3 snapshots  36/36 PASS / critical 0
Pro-first static audit       PASS / critical 0
Pro-first V2 static audit    PASS / critical 0
E2R v6 production audit      PASS / critical 0
compileall / diff check      PASS / PASS
```

이 시점은 C17의 **capture·import 전 검문 PASS**이지 Initial Efficiency Gate PASS가 아니다. 다음 재개는
같은 submitted job과 immutable capture를 사용하며 browser upload·composer 입력·DOM send를 실행하지
않는다. source verification과 initial acceptance를 마친 뒤에만 C17 Gate 판정을 기록한다. C17이 끝나기
전에는 C28이나 P8 최종 verdict를 선언하지 않는다. 상세 수치와 hash는
`p8_c17_fresh_initial_preflight_receipt.json`에 기록했다.

첫 post-capture 재개는 브라우저를 열기 전에 fail-closed했다. 원인은 resume 경로가 이미 제출된 prompt를
영수증에서 복원하지 않고 최신 공통 template로 다시 compile한 뒤 immutable prompt receipt와 비교했기
때문이다. C17 제출 뒤 scope/reference 규칙 3개가 공통 template에 추가됐으므로 두 hash가 다른 것은
정상이다. 이 실패에서 browser submit과 runtime artifact 변경은 모두 0이다.

resume 경로를 다음처럼 분리했다.

```text
새 제출 전 경로       현재 template로 compile → prepare/upload/send 가능
submit_count=1 재개   기존 packet + manifest + prompt receipts만 exact-load
                     → current template compile 금지
                     → browser prepare/upload/send 금지
```

recovery loader는 당시 packet의 commit/config/hash, durable job의 packet/prompt hash, run/pass identity,
blind packet audit, prompt leakage receipt, mandatory question roster와 score/Stage authority false를 모두
검사한다. prompt 본문은 복원·전송하지 않고 영수증의 글자 수만 보존한다. compile이 호출되면 즉시
실패하도록 만든 회귀를 포함해 fresh orchestration `20/20 PASS`를 확인했다.

### C17 Initial Efficiency Gate — diagnostic-only FAIL

receipt-only recovery로 동일 capture를 import한 뒤 8개 source를 각 1회 full fetch하고 전체 20개 fact를
검증했다. query/search와 Pro follow-up은 모두 0이다. 결과는 9개 material candidate 중 3개 accepted로
80% Gate를 통과하지 못했다. 같은 conversation에서 repair로 비율을 올리지 않고 즉시 봉인했다.

```text
material candidate / accepted        9 / 3
post-preflight acceptance             33.3333% FAIL
mandatory question coverage           26 / 26
all fact terminal                      20 / 20
genuine repair candidate / limit       9 / 5
initial prompt output defect           1
local/representation sent to Pro       0 / 0
query/search                            0 / 0
same-conversation repair               0
score/Stage authority                  false / false
publication                            withheld
durable state                          GAP_ADJUDICATION + frozen_at
new conversation required              true
```

불변 Gate failure 수치와 runtime 파일 hash는 `p8_c17_fresh_initial_failure_receipt.json`에 기록했다.
이 33.3333%를 이후 verifier 개선으로 소급 변경하지 않는다.

거절 10건을 원문과 대조한 결과, 실제 output defect와 generic verifier 오탐이 섞여 있었다.

```text
원문 표 cell이 newline, excerpt가 vertical `|` delimiter  오탐 3건
본문 회사채 만기일 2028-01-31을 게시일로 오인          오탐 1건
exact excerpt에 target이 있는데 subject 띄어쓰기로 거절  오탐 1건
중간 문구를 생략한 비연속 quote                         실제 defect
떨어진 표 header/value를 한 excerpt로 합성               실제 defect
target도 subject도 exact excerpt에 없는 project label     실제 defect
```

표 delimiter 수정은 셀의 값과 순서가 실제 문서에 연속할 때만 punctuation-normalized exact match로
인정한다. 중간에 다른 셀이 끼면 계속 거절한다. 날짜 수정은 `재무제표 작성기준`, `발행일 만기일`처럼
본문/표 header에 포함된 단어를 게시일 label로 보지 않고, 줄 시작의 실제 `게시일 2026-...` 같은
metadata만 읽는다. subject 수정도 exact excerpt 자체에 target alias가 있을 때만 nonissuer subject의
띄어쓰기 차이를 허용한다.

sealed source page를 사용한 read-only projection 결과는 다음과 같다. 이것은 과거 Gate 재채점이 아니라
새 verifier 규칙의 단위 확인이다.

```text
vertical table quote exact match       3/3 PASS
synthetic header/value quote reject    2/2 PASS
SK filing publication date             2026-08-13 PASS
MOTIR target-specific subject scope    PASS
source/quote/publication regression    212/212 PASS
```

새 Initial Prompt V3에는 표 cell 합성 금지, publication date와 본문 미래일 분리, 최신 predicate와
HISTORICAL_ONLY 분리를 모든 아키타입 공통 규칙으로 추가했다. C17 종목명·질문명·검색어를 코드에
하드코딩하지 않았다. 다음 C17은 새 runtime/session/job/run/pass/conversation에서 blind fresh initial로
다시 시작한다.

### C17 두 번째 fresh initial — lifecycle 분모 결함 봉인

첫 실패에서 확인한 공통 prompt/verifier 결함을 고친 뒤, 첫 C17 job을 predecessor로 동결하고 완전히
새 runtime/job/run/pass/ChatGPT conversation에서 두 번째 actual Pro 조사를 정확히 한 번 실행했다.

```text
runtime          C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260825T200105Z
fresh session    FRESH-V2-1-C17-R2-20260825T200105Z
fresh job        PROJOB-2136f20fb124e6b76760230b
fresh run        PRORUN-e53f79d5009fb8a7248a71ac
initial pass     PROPASS-68c4c79b446b0c16bdb9ff40
conversation     6a8df4a7-1690-83ee-bd01-036d058c979f
submit/capture   1 / 1
automatic resend 0
prompt/response  58,327 / 138,146 chars
research/total   3,076.970388 / 3,132.240946 seconds
report SHA-256   e353b051332af43ab60af225b7b535a3d8fb93e5d87f2f99edcede76ec48c19e
```

26개 mandatory question/route가 모두 채워졌고 8개 dossier source를 full fetch했다. 전체 21개 fact는
모두 terminal이었으며 query/search와 same-conversation repair는 0이었다. 그러나 당시 Gate 구현은
`material_facts` 배열의 12개를 lifecycle과 무관하게 모두 현재 acceptance 분모로 세어 `6/12=50%`로
FAIL을 봉인했다.

```text
당시 immutable Gate                         6 / 12 = 50.0000% FAIL
mandatory question                          26 / 26
all fact terminal                            21 / 21
initial prompt output defect                  0
genuine repair candidate / limit              4 / 5
query/search                                  0 / 0
same-conversation repair                      0
score/Stage authority                        false / false
publication                                  withheld
```

원인은 evidence 부족이 아니라 현재성 분모 오염이었다. 12개 중 Q1 과거 비교 fact 5개는 Pro가 명시적으로
`HISTORICAL_ONLY`로 보존했고, Q2/current material은 7개였다. 과거 사실을 삭제하거나 CURRENT로 승격하지
않고, `EvidenceLifecycleBridge.compile_as_evidence`가 true인 material만 현재 Gate 후보와 repair roster에
포함하도록 공통 계산을 고쳤다.

쉬운 예로 2026년 2분기 현재 성적을 평가하면서 2026년 1분기 비교표 5줄까지 새 답안의 분모에 넣으면 안
된다. 비교표는 이력으로 그대로 남기되 현재 답안은 `6/7=85.7143%`로 계산해야 한다.

```text
serialized material facts                    12 (모두 보존)
excluded HISTORICAL_ONLY                       5
current material candidate / accepted          7 / 6
read-only fixed-rule projection                85.7143% PASS
current genuine repair candidate               1 <= limit 5
```

과거 immutable FAIL receipt를 새 규칙으로 덮어쓰지 않았다. 위 PASS는 계산 수리 검증용 read-only projection
이라 operational Gate 권한이 없고, 실제 PASS는 새 conversation에서만 얻는다. 두 번째 실패의 전체 ID,
hash, 수치와 projection hash는 `p8_c17_fresh_initial_failure_receipt_r2.json`에 별도 봉인했다.

범용 회귀는 `현재 7개 중 6개 accepted + HISTORICAL_ONLY 5개 + 과거 rejection 5개`를 입력해 다음을
동시에 확인한다.

```text
과거 fact/ID 보존                              PASS
현재 분모                                      7
accepted                                       6
acceptance                                     85.7143% PASS
현재 genuine repair roster                     1
focused lifecycle/fresh/verifier regression   94/94 PASS
Pro-first static audit                        PASS / critical 0
Pro-first V2 static audit                     PASS / critical 0
E2R v6 production static audit                PASS / critical 0
compileall / diff check                       PASS / PASS
```

이 수정도 target, 종목명, C17 질문명으로 분기하지 않는다. 다음 단계는 이 commit을 push한 뒤 새
runtime/session/job/run/pass/conversation에서 C17 initial을 한 번 더 실행하는 것이다. 두 번째 실패 job은
감사용으로 동결하며 같은 conversation에는 어떤 추가 질문도 보내지 않는다.

### C17 세 번째 fresh initial — 전 후보 일괄 withholding 봉인

current-material Gate 수리를 push하고 CI green을 확인한 뒤, 두 번째 C17 job을 predecessor로 봉인하고
세 번째 actual Pro 조사를 새 conversation에 정확히 한 번 전송했다.

```text
runtime          C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260825T210303Z
fresh session    FRESH-V2-1-C17-R3-20260825T210303Z
fresh job        PROJOB-8d0471204d7de2826e879f2e
fresh run        PRORUN-69358af2127fa7984988fb83
initial pass     PROPASS-cc762a119f46a3f109bf08e6
conversation     6a8e0320-0f28-83ee-9a1e-5c0bc2d148c7
submit/capture   1 / 1
automatic resend 0
prompt/response  58,327 / 59,779 chars
research elapsed 4,946.447733 seconds
report SHA-256   8891d29aba3eb0c6c6f8e0a3aeca595c93932aad3d0cb550fba5c0aaea4368e5
```

Pro는 11개 source document와 26개 mandatory question result를 만들었지만, 조사 마지막에 fact-question
양방향 binding과 전체 schema 검증을 끝내지 못했다는 이유로 후보 50개 전부를 accepted candidate
배열에서 제거했다. 조사 부족과 구분하면 다음과 같다.

```text
opened source documents                 11
mandatory question results              26 / 26
self-reported candidate facts           50
serialized material/counter/resolution   0 / 0 / 0
search route receipts                     0
terminal/nonterminal questions            0 / 26
complete claimed                          false
```

최초 import는 `conversation_id=PENDING_NEW_CONVERSATION`, top-level/pass `parent_pass_id=null` 조합에서
fail-closed했다. 기존 transport normalizer가 같은 placeholder를 parent 문자열 `NONE`과 함께 쓴 경우만
처리하고 더 정확한 JSON null 조합을 놓쳤기 때문이다. exact initial pass와 명시적 parent field를 모두
확인한 뒤 null 또는 `NONE`만 허용하도록 공통 수정했다. parent field 누락과 follow-up pass는 계속
정규화하지 않는다.

실제 immutable capture를 browser 재개 없이 parser→dialect→pre-schema→identity binding→strict V3
validator에 다시 넣은 결과는 `0 facts / 11 sources / 26 questions` graph로 PASS했다. 동일 submitted job을
receipt-only recovery한 뒤 Gate를 실행했고 추가 upload/composer/send는 0이었다.

```text
Initial Gate material / accepted          0 / 0
acceptance                                0.0% FAIL
failure reasons                           NO_INITIAL_MATERIAL_CANDIDATES,
                                          INITIAL_ACCEPTANCE_RATIO_BELOW_80_PERCENT
full source fetch                         11
query/search                              0 / 0
same-conversation repair                  0
score/Stage authority                     false / false
publication                               withheld
durable state                             GAP_ADJUDICATION + frozen_at
```

과거 Gate receipt는 당시 코드대로 output defect 0을 보존한다. 새 공통 Gate는 dossier가 명시한
`candidate_fact_count_withheld > 0`인데 current material이 0이면 synthetic fact를 만들지 않고
`INITIAL_PROMPT_OUTPUT_DEFECT` 하나를 추가 기록한다. sealed dossier의 read-only projection은 withheld
50, output defect 1이며 operational PASS 권한은 없다.

근본 prompt 수정은 마지막 일괄 직렬화를 금지한다.

```text
조사 시작        mandatory question skeleton 생성
source를 열 때   SourceDocument + route 즉시 append
quote 확인 때    AtomicFact + 양방향 question binding 즉시 append
후속 조사        이미 검증된 core subset 보존 후 한 건씩 추가
후보 실패        해당 후보만 gap, 기존 valid fact는 유지
도구 시간 감소   새 탐색 중지 → 현재 graph를 JSON-first로 봉인
```

source와 후보를 찾았는데 마지막 일괄 schema 검사를 못 끝냈다는 이유로 세 fact 배열을 모두 비우는 행동을
모든 36개 아키타입에서 명시적으로 금지했다. JSON을 최종 응답의 첫 번째 주 산출물로 두고 Markdown은
그 뒤 짧게만 허용한다. 특정 target·C17·롯데케미칼·후보 개수로 분기하지 않는다.

검증:

```text
exact captured V3 transport recovery             PASS
focused prompt/preflight/gate/orchestration     65/65 PASS
Initial Prompt V3 snapshots                     36/36 PASS / critical 0
Pro-first static audit                          PASS / critical 0
Pro-first V2 static audit                       PASS / critical 0
E2R v6 production static audit                  PASS / critical 0
compileall / diff check                         PASS / PASS
```

세 번째 immutable failure의 전체 hash와 old/new Gate 의미는
`p8_c17_fresh_initial_failure_receipt_r3.json`에 기록했다. 다음 C17은 이 수정 commit을 packet에 결박한
새 runtime/session/job/run/pass/conversation에서 다시 시작한다. 세 번째 conversation에는 추가 질문을
보내지 않는다.

### C17 네 번째 fresh initial — analyst subject verifier 과잉반려 봉인

전 후보 일괄 withholding 방지 수정 commit과 독립 CI green을 확인한 뒤, 세 번째 C17 job을 predecessor로
봉인하고 네 번째 actual Pro 조사를 새 conversation에 정확히 한 번 전송했다.

```text
runtime          C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260825T223036Z
fresh session    FRESH-V2-1-C17-R4-20260825T223036Z
fresh job        PROJOB-2ceb6e7eccad3ab6e4a8446b
fresh run        PRORUN-609870c1cb8f7e5c4de98c97
initial pass     PROPASS-db2ed0ab0d2b0d93bb84b5ee
commit binding   14d0c7f24f082b19d99f2e5df508965fa3c4fdcf
conversation     6a8e17a3-44a8-83ee-92a9-e941133c33a3
submit/capture   1 / 1
automatic resend 0
prompt/response  59,254 / 122,693 chars
research elapsed 5,997.813202 seconds
report SHA-256   c36b18248c1a7db2229aca6f97d2e5ecb8f1d5649a9d453f6db3f836f253f9ea
```

Pro는 이전 실행처럼 후보 전부를 버리지 않고 `10 material / 9 counter / 7 resolution`, source 7개,
question 26개, route receipt 26개를 실제 JSON graph에 보존했다. 26개 질문 중 23개가 terminal이고 3개
`PUBLIC_SEARCHABLE`이 남아 `NEEDS_PUBLIC_GAP_CLOSURE`로 정직하게 끝났다.

```text
serialized material                         10
excluded HISTORICAL_ONLY                     4
current material / accepted                6 / 4
acceptance                              66.6667% FAIL
output contract defect                        0
query/search                               0 / 0
score/Stage authority              false / false
publication                          withheld
```

두 current material과 counter 하나는 source fetch, date, exact quote까지 통과했지만 subject가
`KB증권의 롯데케미칼 추정`, `iM증권의 롯데케미칼 가치평가`처럼 구조화된 관계 라벨이라는 이유로
`REJECTED_WRONG_SUBJECT`가 됐다. 원문에는 대상명·종목코드와 quote가 실제로 존재하지만 그 합성 라벨
전체가 글자 그대로 나오지 않아 생긴 verifier 과잉반려다.

공통 verifier는 non-issuer structured subject가 target alias를 포함하고, 이미 literal 검증된 quote의 앞뒤
2,000자 bounded context에도 같은 target alias가 있을 때만 target analyst fact를 인정하도록 고쳤다.
target 언급이 멀리 떨어진 다중 회사 문서는 계속 `WRONG_SUBJECT`로 막는다. 쉬운 예로 문서 첫머리에
`롯데케미칼(011170) 주가전망`이 있고 바로 뒤에 `2026년 EPS 추정치 +15%`가 있으면 같은 대상 분석이다.
반대로 5,000자 앞에 롯데케미칼이 한 번 나오고 quote는 비교기업 얘기면 통과하지 않는다.

네 번째 immutable capture와 내려받은 7개 원문을 `/tmp` projection에서 재검증한 결과는 다음과 같다.

```text
all fact candidates / accepted                26 / 20
current material / accepted                     6 / 6
acceptance                                     100% PASS
genuine semantic repair                           0
query/search                                   0 / 0
read-only Gate projection                       PASS
projection receipt b1524db518f1d5d50d71acdd2a3339c84c22684ab73b922cff9c92d761aaba7b
```

과거 FAIL receipt는 덮어쓰지 않았고 projection에는 operational 권한이 없다. 전체 ID, hash, old/new Gate와
과잉반려 근거는 `p8_c17_fresh_initial_failure_receipt_r4.json`에 봉인했다. source verification semantics는
`e2r_pro_source_verification_v11`로 올린다. 회귀·정적 감사·CI green 뒤 새 conversation에서 실제 C17
initial PASS를 다시 증명하며 네 번째 conversation에는 어떤 추가 입력도 보내지 않는다.

코드 변경 후 로컬 검증은 다음과 같이 닫혔다.

```text
source/local-preflight/Gate/known-bad focused   72/72 PASS
Playwright 직접 실행 6 modules              79/79 PASS
전체 unittest                                 7,698 PASS
failure / error / skipped                        0 / 0 / 38
Pro-first static audit                         PASS / critical 0
Pro-first V2 static audit                      PASS / critical 0
E2R v6 production static audit                 PASS / critical 0
compileall / git diff check                     PASS / PASS
```

첫 전체 실행의 browser 60 ERROR는 assertion 실패가 아니라 WSL에
`libnspr4.so`, `libnss3.so`, `libasound.so.2`가 없어 Chromium이 시작 전 종료된 환경 실패였다.
관리자 인증이 필요한 시스템 설치 대신 공개 Ubuntu 패키지를 `/tmp/e2r-playwright-deps`에만 풀고
`LD_LIBRARY_PATH`로 테스트 Chromium에 연결했다. 그 후 browser 79개와 전체 7,698개가 모두
통과했다. Windows ChatGPT 로그인 프로필과 봉인된 C17 대화는 변경하지 않았다.

## 2026-08-26 — C17 다섯 번째 fresh initial은 짧은 인용의 dossier 일괄 반려를 드러냄

네 번째 C17 실패 원인의 공통 verifier 수정과 독립 CI green을 확인한 뒤, 다섯 번째 actual Pro 조사를
새 conversation에 정확히 한 번 전송했다.

```text
runtime          C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260826T010453Z
fresh session    FRESH-V2-1-C17-R5-20260826T010453Z
fresh job        PROJOB-6ed24292874ceae06e5e7f27
fresh run        PRORUN-10f8b5284f7fe8bd52ca12d8
initial pass     PROPASS-25f410895f717db11ff4fe5a
commit binding   e8f0b25c8d6858bd6bf0b5d0b998f3b540c20c43
conversation     6a8e3c60-3b58-83ee-ad02-e81700c63463
submit/capture   1 / 1
automatic resend 0
prompt/response  59,254 / 148,393 chars
research elapsed 3,812.572911 seconds
report SHA-256   c9fe840b8923d5b8f210608abaed306943a78a02cb8db4ec9fffeb9e48700fd3
```

Pro 응답 캡처와 canonical conversation 복구는 성공했다. 그러나 import schema가 첫 counterfact의
`supporting_excerpt="정기보수 영향"`을 8자 미만이라는 이유만으로 거절해 initial efficiency Gate까지
도달하지 못했다. 이때 실제 응답에는 source 9개와 fact 33개가 있었다.

```text
source documents                       9
material / counter / resolution    12 / 15 / 6
all facts                              33
derived metrics                         1
questions / routes                 26 / 26
short nonempty excerpt                  1
actual import verdict                FAIL
```

이 실패는 Pro 자료 부족이나 파싱 누락이 아니라 pre-downstream schema의 일괄 반려다. 쉬운 예로 33개
후보 중 `정기보수 영향` 한 줄이 7자라는 이유로 33개 전체를 버린 셈이다. initial dossier와 compact
repair schema는 이제 `supporting_excerpt`가 비어 있지 않으면 후보 graph를 보존한다. 빈 문자열은 계속
거절한다. 1~7자 후보는 자동 증거 승격되지 않으며 기존 literal source verifier가 fact 단위로 보류·거절한다.
따라서 나머지 dossier를 살리면서 점수 안전성은 유지한다.

R5 immutable capture를 새 schema로 읽기 전용 projection한 결과는 다음과 같다.

```text
schema projection                      PASS
source / all facts                   9 / 33
material / counter / resolution    12 / 15 / 6
questions / routes                 26 / 26
query / fetch                         0 / 0
operational Gate authority              false
projection hash       1809818ec02bdf546e2741e1275ae33e1305fd1218e6c55a03ea10eccf39fc5f
```

이 projection으로 R5를 소급 PASS 처리하지 않았다. R5 job은
`FRESH_SESSION_DIAGNOSTIC_ONLY / NEW_CONVERSATION_REQUIRED`로 봉인했고 같은 conversation에는 어떤
추가 입력도 보내지 않는다. 전체 ID, hash와 immutable 실패는
`p8_c17_fresh_initial_failure_receipt_r5.json`에 기록했다.

공통 schema와 36개 prompt snapshot을 갱신한 뒤 로컬 검증은 다음과 같이 닫혔다.

```text
focused dossier/preflight/repair tests          56/56 PASS
Initial Prompt V3 snapshots                     36/36 PASS / critical 0
전체 unittest                                   7,701 PASS
failure / error                                   0 / 0
Pro-first static audit                           PASS / critical 0
Pro-first V2 static audit                        PASS / critical 0
E2R v6 production static audit                  PASS / critical 0
compileall / git diff check                      PASS / PASS
```

다음 실제 C17 검문은 이 schema hash가 반영된 commit과 CI green을 먼저 확인한 뒤, 여섯 번째 새
conversation에서 수행한다. R5 raw capture와 중앙 ledger는 수정하지 않는다.

## 2026-08-26 — C17 R6 전송 전 predecessor denylist 경계를 보완

짧은 인용 일괄 반려 수정 commit `953eede0ae6b81dddce19277aa4661f4b4c6ef2f`를 push한 뒤 같은
head의 독립 CI 세 개가 모두 성공했다.

```text
push Pro-first CI       32923567286 SUCCESS
PR Pro-first CI         32923570626 SUCCESS
E2R v6 offline CI       32923570621 SUCCESS
PR #7 state             Draft / Open / Mergeable
```

그 뒤 C17 R6을 위한 새 runtime/session을 준비했지만 ChatGPT 전송보다 앞선 old-answer leakage
manifest 단계에서 멈췄다. R5는 schema import 전에 캡처는 완료했지만
`research_passes/effective_dossier.latest.json`은 만들지 못한 diagnostic predecessor다. 기존 manifest
builder가 verifier-complete predecessor만 가정해 이 파일을 무조건 열었다.

```text
intended runtime     C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260826T025720Z
intended session     FRESH-V2-1-C17-R6-20260826T025720Z
fresh runtime/job/run/pass/conversation created   0 / 0 / 0 / 0 / 0
upload/composer fill/submit/capture                0 / 0 / 0 / 0
automatic resend                                      0
R5 ledger mutation                                     0
actual Pro initial attempt                              0
```

따라서 이 사건은 C17 initial efficiency Gate 실패가 아니라 전송 전 boundary 진단이다. 위 intended
identity는 감사용으로 폐기하고 실제 R6에는 새 timestamp를 사용한다.

공통 manifest builder는 verifier-complete predecessor에서는 기존 effective dossier를 계속 우선한다.
그 파일이 없는 schema-failed predecessor에서만 `READY.json`, capture receipt identity와 전체 capture
bundle SHA-256을 모두 확인한 뒤 기존 bounded `ResearchDossierParser`로 캡처 JSON을 읽는다. 여기서
읽은 값은 오직 이전 answer token denylist에만 들어가며 source verification, score, Stage 권한은 없다.
쉬운 예로 R5의 `PROFACT-C01`이라는 이름이 새 packet에 우연히 복사되는지는 막지만, 그 fact를 새
증거 또는 점수로 인정하지는 않는다. 캡처 JSON을 한 글자라도 바꾸면 hash mismatch로 실패한다.

실제 R5 캡처에 대한 읽기 전용 manifest projection은 다음과 같다.

```text
old fact ids              33
old route receipt ids     26
old research pass ids      1
old question answers      26
expected source URLs      14
expected fact ids         33
score / Stage authority  false / false
```

수정 후 검증:

```text
focused fresh orchestration                    21/21 PASS
tampered capture rejection                         PASS
전체 unittest                                  7,702 PASS
failure / error / skipped                    0 / 0 / 38
Pro-first static audit                    PASS / critical 0
Pro-first V2 static audit                 PASS / critical 0
E2R v6 production static audit            PASS / critical 0
compileall / git diff check                PASS / PASS
```

전체 identity와 zero-submit 증거는
`p8_c17_fresh_pre_submit_boundary_failure_receipt_r6.json`에 기록했다. 다음 actual R6은 이 수정 commit과
독립 CI green을 확인한 뒤 새 runtime/session/job/run/pass/conversation에서 정확히 한 번만 보낸다.

## 2026-08-26 — C17 여섯 번째 actual fresh initial 100% PASS

전송 전 boundary 수정 commit `b4493b26e9f1aadbc3789ff0bda70b14122f6895`와 독립 CI 세 개가 모두
SUCCESS인 것을 확인한 뒤, 폐기한 pre-submit identity와 다른 새 runtime/session에서 C17 actual Pro
조사를 정확히 한 번 전송했다.

```text
runtime          C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260826T033612Z
fresh session    FRESH-V2-1-C17-R6-20260826T033612Z
fresh job        PROJOB-41ec024bdbc0c9c8d56c9d05
fresh run        PRORUN-b9e5878d77b712aa7a378561
initial pass     PROPASS-6a68e3062040f1f73f6d9487
commit binding   b4493b26e9f1aadbc3789ff0bda70b14122f6895
conversation     6a8e5f55-a7f8-83e8-bd89-82c1e4529916
submit/capture   1 / 1
automatic resend 0
prompt/response  59,254 / 120,503 chars
research elapsed 3,665.403214 seconds
total elapsed    3,732.263675 seconds
report SHA-256   e71dabb85fba62901fbe8ad6089cd5782f7de7b6d826b774e70d0c30f7bf0364
```

ChatGPT 결과 카드의 JSON을 실제 capture bundle에 저장했고 importer는
`parser_source=DOWNLOADED_JSON`으로 읽었다. 보고서 MD는 visible report를 보존하는 별도 감사 산출물이고,
선택 PDF는 요청하지 않아 `null`이며 오류도 없다. 쉬운 예로 JSON은 계산기에 넣는 구조화 입력이고 MD는
사람이 당시 답변을 다시 읽는 영수증이다. 둘 중 하나를 예전 대화 파일과 혼동해 선택하지 않았다.

Pro dossier는 source 8개와 fact 26개를 만들었다. material 15개 중 7개는 `as_of_date` 현재 판단이 아닌
historical-only 자료라 efficiency 분모에서 제외했다. 남은 current material 8개는 preflight와 source
verification 후 8개 모두 승인됐다.

```text
source documents                               8
material / counter / resolution          15 / 8 / 3
all facts                                     26
historical-only material excluded              7
current material / accepted                8 / 8
post-preflight acceptance                    100% PASS
mandatory question coverage               26 / 26
search route receipts                          34
genuine semantic repair                         0
repair pass / deferred batch                 0 / 0
output contract defect                          0
query / search                               0 / 0
source fetch                                    8
score / Stage authority              false / false
publication                          withheld
```

여기서 `100% PASS`는 C17 초기 조사 효율 검문 통과이며 점수나 Stage 확정이 아니다. 예를 들어 질문 26개가
모두 dossier에 답을 갖고 current material 8개가 검증됐어도, 남은 public/parser gap을 닫고 7 component와
21 Judge를 계산하기 전에는 운영 점수를 게시하지 않는다. 그래서 job은 `GAP_ADJUDICATION`, publication은
withheld, score/Stage authority는 false를 유지한다.

DB와 파일을 교차 확인한 결과 job은 `submit_count=1`, `capture_count=1`, `last_error=null`이고 initial pass는
`COMPLETE`다. capture receipt, downloaded JSON, normalized dossier, source verification, efficiency receipt의
identity와 hash는 `p8_c17_fresh_initial_success_receipt_r6.json`에 기록했다. raw 보고서, source page, 중앙
ledger는 Git에 넣지 않는다. 다음 단계는 완전히 다른 새 conversation에서 C28 initial canary를 실행하는
것이다.

## 2026-08-26 — C28 첫 fresh initial은 비공개 종결 근거 1개 누락으로 봉인

C17 R6의 100% PASS와 commit `dca86ae95f1356bcbd95c7e6202ca1b0e622b162`의 독립 CI green을 확인한
뒤, C17과 다른 종목·아키타입인 안랩 C28 actual Pro 조사를 새 conversation에 정확히 한 번 전송했다.

```text
runtime          C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260826T050004Z
fresh session    FRESH-V2-1-C28-R1-20260826T050004Z
fresh job        PROJOB-8df8121eb03759d7f8a883ac
fresh run        PRORUN-584b325f46a1fc5d02249a1a
initial pass     PROPASS-df09bfe4987bc857a1a42780
commit binding   dca86ae95f1356bcbd95c7e6202ca1b0e622b162
conversation     6a8e72fe-b6fc-83e8-9c03-b760986e7d78
submit/capture   1 / 1
automatic resend 0
prompt/response  60,479 / 129,708 chars
```

ChatGPT 결과 카드에서 JSON을 실제로 내려받아 `parser_source=DOWNLOADED_JSON` 경로로 연결했다. MD는
사람이 읽는 감사용 보고서이고 선택 PDF는 요청하지 않았다. 즉 이번 실패는 다운로드 버튼이나 MD/JSON
선택 문제가 아니다. JSON에는 source 6개, fact 37개, mandatory question 27개, route receipt 32개가
보존됐다.

strict schema가 멈춘 곳은 C28 Q02 하나다. Pro는 이 질문을 `LIKELY_NONPUBLIC`으로 표시하고 성공한
검색 경로 2개를 연결했지만, 그중 한 경로의 `no_new_route_reason`이 비어 있었다.

```text
failing question                         C28...Q02
claimed status                    LIKELY_NONPUBLIC
linked routes / SUCCESS                    2 / 2
route missing no-new-route reason              1
actual import                                 FAIL
initial efficiency Gate reached             false
score / Stage authority             false / false
publication                           withheld
```

쉬운 예로 “공개자료에서 못 찾았다”는 기록만 있고 “공식 공시 범위상 왜 더 볼 경로가 없는가”가 한 경로에
없으므로 `비공개로 종결`할 수 없다. 그렇다고 없는 이유를 코드가 만들어 넣어서도 안 된다. 공통
pre-schema normalizer는 이런 terminal absence/nonpublic 주장을 `PUBLIC_SEARCHABLE`,
`adequate_search_proven=false`로 한 방향 하향하고, mandatory question이면 dossier 상태도 우선순위에 맞춰
`NEEDS_PUBLIC_GAP_CLOSURE`로 되돌리도록 수정했다. 이미 모든 경로에 이유가 있는 정상
`LIKELY_NONPUBLIC`은 그대로 보존한다. 종목명·C28·질문 ID 조건은 사용하지 않았다.

R1 immutable JSON을 수정 코드에 읽기 전용으로 투영한 결과는 source 6개와 fact 37개를 그대로 보존한 채
strict V3 schema를 통과했다. 이 projection에는 initial efficiency Gate, score, Stage, publication 권한이
없으며 R1을 소급 PASS 처리하지 않는다. R1 job은 state version 15에서 다음 disposition으로 봉인했다.

```text
FRESH_SESSION_DIAGNOSTIC_ONLY
OPERATIONAL_EFFICIENCY_GATE_FAILED
NEW_CONVERSATION_REQUIRED
same-conversation follow-up / automatic resend   0 / 0
```

회귀검사는 근거 없는 `LIKELY_NONPUBLIC` 하향, 정상 종결 보존, 근거 없는 evaluated absence 하향,
이유 미생성을 함께 확인했다. local preflight 31개와 dossier/status/saturation/prompt focused 72개가 모두
통과했다. 전체 ID, hash, raw/projection 경계와 봉인 증거는
`p8_c28_fresh_initial_failure_receipt_r1.json`에 기록했다. 전체 테스트·정적 감사·독립 CI green을 먼저
확인한 뒤에만 두 번째 완전 새 C28 conversation을 시작한다.

수정 후 로컬 검증은 다음과 같이 닫혔다.

```text
local preflight focused                              31/31 PASS
dossier/status/saturation/prompt focused             72/72 PASS
실제 C28 R1 JSON read-only strict projection             PASS
전체 unittest                                       7,705 PASS
failure / error / skipped                         0 / 0 / 38
Phase100                                             15/15 PASS
Pro-first static audit                        PASS / critical 0
Pro-first V2 static audit                     PASS / critical 0
E2R v6 production static audit                 PASS / critical 0
compileall / git diff check                          PASS / PASS
```

첫 전체 실행에서 브라우저 테스트가 낸 ERROR는 코드 실패가 아니라 `/tmp`에 풀어 둔 Chromium 공유
라이브러리의 상위 경로를 잘못 지정한 실행 환경 오류였다. 실제 경로
`/tmp/e2r-playwright-deps/root/usr/lib/x86_64-linux-gnu`로 브라우저 어댑터 25개를 먼저 통과시킨 뒤,
전체 7,705개를 처음부터 새로 실행해 failure/error 0을 확인했다. 중단한 환경 오류 실행은 위 최종 수치에
합산하지 않았다.

## 2026-08-26 — C28 두 번째 fresh initial은 다른 질문 route 오결박으로 봉인

C28 R1 수정 commit `b136f02bdae86587bef4eb65159ff8011bee8423`의 독립 CI 세 개가 모두
SUCCESS인 것을 확인한 뒤, R1과 다른 runtime/session/conversation에서 C28 actual Pro 조사를 정확히 한
번 전송했다. 일반 Chat의 Pro 모드이며 legacy Deep Research 전송은 사용하지 않았다.

```text
runtime          C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260826T073534Z
fresh session    FRESH-V2-1-C28-R2-20260826T073534Z
fresh job        PROJOB-92a788cb99d245f007457792
fresh run        PRORUN-7c3e60dacd5b3ea2e022d1df
initial pass     PROPASS-fbc13f5eb3f4c9e20d8af44c
commit binding   b136f02bdae86587bef4eb65159ff8011bee8423
conversation     6a8e975e-fd30-83ee-9f62-cfaf58836274
submit/capture   1 / 1
automatic resend 0
```

ChatGPT 결과 카드의 JSON을 실제로 내려받아 `parser_source=DOWNLOADED_JSON`으로 읽었다. visible DOM의
원본에는 JSON 문자열 안 raw control character 35개가 있었고, 기존 bounded parser가 의미를 바꾸지 않고
JSON escape만 적용했다. MD 실다운로드·새 JSON·선택 PDF 경계도 유지됐고 PDF는 요청하지 않아 `null`이다.
즉 이번에도 예전 MD를 잘못 집어온 문제가 아니다.

다운로드 JSON에는 source 6개, fact 11개, mandatory question 27개와 route receipt 17개가 있었다. strict
schema는 question row 15개가 자기 질문이 아닌 route receipt ID를 참조해 Gate 전에 멈췄다. 주로 공통 R13
cross-guard 질문에서 C28 본 질문 또는 이웃 질문의 route를 재사용한 경우였다.

```text
source documents                               6
material / counter / resolution          7 / 4 / 0
all facts                                     11
mandatory questions / route receipts      27 / 17
derived metrics / unresolved gaps          3 / 11
research status          NEEDS_PUBLIC_GAP_CLOSURE
actual import                              FAIL
initial efficiency Gate reached            false
score / Stage authority            false / false
publication                          withheld
```

쉬운 예로 Q02가 “Q03 검색에서 이 URL을 봤다”는 영수증을 자기 영수증처럼 연결한 상태다. URL과 자료를
삭제할 이유는 없지만, 그 영수증으로 Q02 검색이 충분했다고 증명할 수는 없다. 공통 pre-schema normalizer는
각 question이 정확히 같은 `archetype_id × question_family_id` 소유 route만 보존하도록 수정했다. unknown,
foreign, duplicate link는 해당 question에서만 제거하고 `adequate_search_proven=false`로 되돌린다. 전역
route receipt와 모든 fact는 그대로 보존한다. 종목·C28·질문 ID 하드코딩은 없다.

R2 immutable JSON을 parser → 공개 dialect adapter → pre-schema normalizer → transport identity binding →
strict V3 validator 순서로 읽기 전용 투영한 결과는 PASS다.

```text
initial placeholder alias normalization          1
source / route URL canonicalization           2 / 3
foreign question route links removed             15
source / facts / questions / global routes  6 / 11 / 27 / 17
research status          NEEDS_PUBLIC_GAP_CLOSURE
Gate / score / Stage authority      false / false / false
```

이 projection으로 R2를 소급 PASS 처리하지 않았다. R2 job은 state version 15에서
`FRESH_SESSION_DIAGNOSTIC_ONLY / OPERATIONAL_EFFICIENCY_GATE_FAILED / NEW_CONVERSATION_REQUIRED`로 봉인했고,
같은 conversation에는 후속 입력이나 자동 재전송을 하지 않는다. 전체 실행 identity, artifact hash, 오류와
봉인 증거는 `p8_c28_fresh_initial_failure_receipt_r2.json`에 기록했다.

수정 후 검증은 다음과 같이 닫혔다.

```text
focused dossier/preflight/fresh tests              182/182 PASS
전체 unittest                                      7,707 PASS
failure / error / skipped                        0 / 0 / 38
Phase100                                            15/15 PASS
Pro-first static audit                       PASS / critical 0
Pro-first V2 static audit                    PASS / critical 0
E2R v6 production static audit                PASS / critical 0
compileall / git diff check                         PASS / PASS
```

다음 단계는 이 범용 수정을 한글 commit으로 push하고 독립 CI green을 확인한 뒤, 세 번째 완전 새 C28
conversation에서 actual initial canary를 한 번만 전송하는 것이다. R2 raw capture와 중앙 ledger는 수정하지
않는다.

## 2026-08-26 — C28 R3와 P9 다중 아키타입 fresh-session 검문 통과

C28 R2 범용 수정 commit `fdac32990ba8d29fb6b596c6f5bbb8d5a372538e`의 독립 CI 세 개가 모두
SUCCESS인 것을 확인한 뒤, R1/R2와 다른 runtime/session/conversation에서 안랩 C28 actual Pro 조사를
정확히 한 번 전송했다. 일반 Chat의 Pro 모드이며 legacy Deep Research를 사용하지 않았다.

```text
runtime          C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260826T091553Z
fresh session    FRESH-V2-1-C28-R3-20260826T091553Z
fresh job        PROJOB-e3d57e985cd3a1617b717ccd
fresh run        PRORUN-d0f7e7834ed81f0c9bb324a1
initial pass     PROPASS-13e168efd50ba39ed8e94102
conversation     6a8eaee3-d670-83ee-9c01-6f7d438db2f0
submit/capture   1 / 1
automatic resend 0
prompt/response  60,479 / 116,288 chars
research elapsed 3,678.863673 seconds
total elapsed    3,738.385957 seconds
```

ChatGPT 결과 카드에서 새 JSON을 실제로 다운로드해 `parser_source=DOWNLOADED_JSON`으로 import했다.
JSON 문자열 안 raw control character 84개는 bounded parser가 escape만 적용했고, source/fact 의미는
바꾸지 않았다. 예전 MD를 잘못 고른 것이 아니며 선택 PDF는 요청하지 않아 `null`이다.

```text
source documents                              9
all facts                                    22
initial current material candidate/accepted 10 / 10
post-preflight acceptance ratio             100%
mandatory question coverage                 27 / 27
verified/compiled facts                         17
genuine repair candidate / actual pass       0 / 0
query / search / fetch                       0 / 0 / 9
score / Stage authority                      false / false
publication                                  withheld
initial efficiency Gate                      PASS
```

R3 job은 `GAP_ADJUDICATION`, dossier는 `NEEDS_PUBLIC_GAP_CLOSURE`다. 이 PASS는 C28 초기 조사 효율
통과이지 최종 점수나 Stage가 아니다. 전체 identity, artifact hash, parser operation, source verification과
Gate 수치는 `p8_c28_fresh_initial_success_receipt_r3.json`에 고정했다. raw report, downloaded JSON,
source page와 중앙 ledger는 Git에 넣지 않는다.

P9에서는 동결 구 실행과 세 fresh 실행을 `fresh_session_comparison.json/.md`로 비교했다. 새 독립 감사기는
비교표의 자기주장을 믿지 않고 다섯 source receipt를 다시 읽어 합계와 hard-zero counter를 계산한다.

```text
fresh archetypes / conversations            3 / 3
initial material candidate/accepted        36 / 34
aggregate acceptance ratio                94.4444%
mandatory question coverage                81 / 81
verified facts                                    56
actual Pro repair pass                              0
required hard-zero counters                    13/13
fresh efficiency audit               PASS / critical 0
audit hash       47d96d1f3b602ef0b963ce3772ffc70cbacdb655fb399aefdcf0a61fb9b87b6a
```

동결 구 실행은 11 pass, prompt defect 50개, local/verifier defect 24개였고 마지막 source verification은
53 fact를 accepted/compiled했다. 다만 구 pipeline은 initial acceptance 경계와 11 pass 전체 문자 telemetry를
보존하지 않았으므로 comparison에는 `null`과 이유를 남겼다. 서로 source corpus가 달라 score parity도
금지했다.

현재 verdict는 verifier-ready pipeline, C06, C17, C28, multi-archetype fresh session까지 PASS다. 세 live
canary에는 공개자료/parser gap 합계 41개가 남아 있고 score/Stage publication 권한도 없으므로
`operational_research_readiness=WITHHELD_FULL_THESIS_PENDING`을 유지한다. 즉 초기 효율 검문을 최종 thesis
완료로 과장하지 않는다.

P9 코드·영수증·문서 작성 후 로컬 검증은 다음과 같이 닫혔다.

```text
P9 fresh efficiency focused tests                   5/5 PASS
Linux headless browser tests                       79/79 PASS
전체 unittest                                     7,712 PASS
failure / error / skipped                       0 / 0 / 38
Phase100                                           15/15 PASS
Gate 1 tracked receipt                               4/4 PASS
Pro-first static audit                     PASS / critical 0
Pro-first V2 static audit                  PASS / critical 0
Pro-first V2 static audit hash 0928a78b0411df4e885760d24be84d6a53edad45613963c0b53146aafad07b9a
E2R v6 production static audit             PASS / critical 0
E2R v6 static audit hash       ff981d5bed53ebaec938dbcc3049c4e31a854766cd6517ac306376609c94a27a
compileall / git diff check                       PASS / PASS
```

첫 전체 실행에서 난 브라우저 ERROR 60개는 Playwright가 `libnspr4.so`를 찾지 못한 실행환경 오류였다.
`/tmp/e2r-playwright-deps/root/usr/lib/x86_64-linux-gnu`를 `LD_LIBRARY_PATH`에 연결해 브라우저 79개를
독립 통과시킨 뒤 전체 7,712개를 처음부터 다시 실행했다. 최종 실행은 failure/error 0이며 앞선 환경 오류
실행은 PASS 수치에 포함하지 않았다.

```text
final full unittest elapsed       655.522 seconds
final full unittest log sha256    9bccf1f209803306de93029cdab105aa762253c5915d594183dcc88c094eba91
```

## 2026-08-26 — P10 V3 JSON full-thesis tail 구현 및 actual 3종 read-only 검문

P9는 fresh initial 효율 검문까지였고 세 canary 모두 `GAP_ADJUDICATION`에서 멈춰 있었다. P10은 이미
성공한 각 initial pass를 다시 보내지 않고, **동일한 일반 Chat + Pro conversation**에서 deterministic
saturation이 지목한 공백만 후속 조사한 뒤 score/Judge/Stage로 넘기는 후반 실행 경로다.

화면에 보이는 `ResearchDossierV3_...json`의 정확한 처리 순서는 다음과 같다.

```text
같은 assistant turn의 JSON 다운로드
→ conversation/run/pass/hash 결박
→ V3 strict schema와 source/fact lineage 검증
→ append-only effective dossier
→ deterministic saturation
→ 남은 question만 같은 Pro conversation에 delta 요청
```

이전 진행 문구의 “새 MD 실다운로드”는 legacy capture 테스트 이름을 그대로 옮긴 부정확한 표현이었다.
현재 fresh V3 actual의 정확한 표현은 “예전 MD/다른 turn JSON을 오인하지 않고, 같은 turn의 새 V3 JSON을
실다운로드하며, 별도 PDF가 존재할 때만 선택 캡처한다”이다. 쉬운 예로 화면에 C06 JSON 카드가 이미 있으면
그 버튼으로 파일을 받아 연결하면 되고, 새 MD가 다시 생기기를 기다리지 않는다.

C06 actual은 이미 다음 경로로 다운로드·연결돼 있다.

```text
capture mode       CHATGPT_WEB_VISIBLE_CHAT_PRO_FRESH_V3
capture source     DIRECT_REPORT_DOM
dossier path       capture/incoming/research_dossier.json
dossier hash       0e43559193138e74d69a22f1c081cca1baa02fd110fba4490b9b95e381e9d9cd
conversation       6a8db0ad-8ed0-83e8-888e-dce26c950343
submit/capture     1 / 1
expanded JSON      capture/supplemental/expanded_research_dossier.json
schema/import      e2r_pro_research_dossier_v3 / PASS
PDF                없음(null, 오류 아님)
```

새 runner는 fresh boundary와 old-answer leakage manifest를 다시 검증하고, 기존 conversation을
`recover_conversation_without_submit`으로 연 뒤 initial submit delta 0을 보장한다. 후속 응답은 전체 dossier
재출력이 아니라 새 source/fact/route와 변경 question/gap만 담는 `ResearchDossierV3 delta JSON`이다.
deterministic merger가 기존 accepted lineage를 append-only로 합친다.

동일 semantic gap을 pass/dossier transport hash 변화만으로 재전송하지 않도록
`research_gap_context_hash`를 pass ledger에 영구 저장한다. 공개 gap, counter/supersession, verifier repair,
saturation audit은 순서와 권한이 분리되어 있다. Pro는 증거만 추가하며 score/Stage는 계속 deterministic
pipeline만 계산한다. semantic progress가 없거나 source gap이 남으면 낮은 점수를 확정하지 않고 honest
pending으로 종료한다.

기존 durable verification receipt 재사용에서 실제 accepted fact를 0개로 오인하던 원인도 수정했다.
검산 hash를 재계산할 때 `preflight_receipt_hash`와 `rejection_classifications`가 빠져 모든 actual receipt가
불일치로 보였던 문제다. 두 artifact를 exact hash 재계산에 포함한 뒤 actual 3종이 모두 회복됐다.

```text
canary   accepted facts   next public questions   material repair candidates
C06      21               25                      3
C17      18               21                      1
C28      17               24                      3
```

질문 수가 P9의 unresolved 41보다 큰 것은 같은 질문이 `공식 route 미시도`, `verified fact linkage 누락`,
`source-route quorum 미달`처럼 여러 deterministic failure family에 겹칠 수 있기 때문이다. 종목별 query
문자열을 코드가 만드는 방식은 사용하지 않는다. runner는 failure code와 source-role 공백만 같은 Pro에
되돌리고, 실제 검색 판단과 query 생성은 Pro가 수행한다.

코드 변경 후 검증은 다음과 같다.

```text
V3/fresh/runtime/JSON capture focused                 72/72 PASS
Phase100                                               15/15 PASS
Pro-first static audit                          PASS / critical 0
Pro-first V2 static audit                       PASS / critical 0
V2.1 fresh efficiency audit                     PASS / critical 0
compileall / git diff check                           PASS / PASS
WSL full discovery                           7,717 executed
WSL code assertion failure                                0
WSL Playwright startup environment error                  60
Windows browser bundle                            78 PASS
Windows-only POSIX subprocess check environment error      1
```

WSL의 60개 오류는 production adapter 코드가 아니라 headless Chromium이 `libnspr4.so`를 찾지 못해
각 browser test의 setup에서 종료된 동일 환경 오류다. 해당 browser 동작은 Playwright가 설치된 Windows
Python에서 전부 통과했다. 반대로 Windows에서 남은 1개는 POSIX provider의 지연 import를 새 subprocess로
검사하는 Linux 전용 항목이며 WSL 전체 실행에서 통과했다. 독립 GitHub CI에서는 Playwright system
library를 설치한 Ubuntu runner로 전체 suite를 다시 검증한다.

이 시점에는 actual 후속 Pro 전송을 아직 하지 않았다. code/receipt/document를 먼저 한글 commit으로
push하고 독립 CI green을 확인한 뒤 C06 → C17 → C28 순서로 같은 conversation tail을 실행한다. 따라서
score/Stage publication은 계속 withheld이며 `p10_full_thesis_tail_preflight_receipt.json`은 구현·검문
receipt이지 최종 full-thesis receipt가 아니다.

## 2026-08-26 — P10 C06 actual `PUBLIC_GAP_CLOSURE` 1차 회수와 V3 병합 수리

독립 CI green 뒤 C06의 기존 conversation `6a8db0ad-8ed0-83e8-888e-dce26c950343`을 URL로 직접
회복했다. initial prompt는 다시 보내지 않았고 browser submit delta는 0이었다. deterministic saturation이
지목한 공개자료·provider/parser·source-linkage 공백만 `PUBLIC_GAP_CLOSURE` pass로 정확히 한 번 전송했다.

```text
pass id             PROPASS-1db540b7e696ffc05d1c94a1
parent pass         PROPASS-e49762cc3ad556d6b211d92b
submit count        1
automatic resubmit  0
research elapsed    약 110분
capture source      DIRECT_REPORT_DOM_NORMALIZED
new source docs     7
new facts           14
new routes          33
updated questions   25
```

Pro 완료 뒤 같은 assistant turn에서 후속 V3 JSON을 실다운로드했다. raw capture는 runtime에만 보존하고
Git에는 hash와 검문 결과만 둔다.

```text
prompt hash      1b93bf9ec67200eedd51da4b6f8ad8676a010f2eb0948ba49c0949d610001442
raw report hash  32c8873c366852a16aa13775f7321889e45cacd4cff73e64a2932639e8ea2828
report hash      b561736ef2c6c90147ed6053dd5e4c60810675d4b18389ce130239592528f44f
V3 JSON hash     5c708857249957f3dd2e2d26347750f6ef366ecb48df457bd5fe473158c899dd
```

첫 병합은 fail-safe로 멈췄다. 원인은 V2 lineage의 URL·publisher·상태이력 필드를 V3 lineage에도
추가하던 schema 혼용이었다. V3는 `lineage_id`, `source_document_ids`, `fact_ids`,
`independence_group_id`, `status`만 두고 URL은 `source_documents`가 소유한다. merger를 schema별로
분리하고 기존 lineage에 새 문서/사실을 합치는 회귀 테스트를 추가했다.

두 번째 실제-data 오프라인 병합에서는 Pro가 `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_Q01`을
`EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH`로 닫았지만 exact route roster에 기존
`PARSER_PENDING` 영수증이 남아 있음을 검문이 잡았다. 전체 답안을 폐기하지 않고 새 증거는 보존하되,
그 질문 하나만 deterministic하게 `PARSER_PENDING / PARSER_BLOCKED`로 낮춘다. raw Pro 주장은 capture에
그대로 남고 effective dossier의 `research_saturation.route_truth_question_status_projections`에 투영 이유와
blocking route를 기록한다.

쉬운 예: 새 답안 14개 중 13개가 정상이고 감사 원문 1개가 파서에 막혔다면 14개를 전부 버리거나
“감사 문제 없음”으로 확정하지 않는다. 14개를 모두 ledger에 넣고 감사 질문만 pending으로 둔다.

실제 저장된 capture를 브라우저·전송 없이 다시 병합한 결과는 다음과 같다.

```text
exact capture offline merge                  PASS
new / effective facts                       14 / 39
new / effective source documents             7 / 23
new / effective source lineages               6 / 21
new / effective route receipts               33 / 70
effective mandatory questions                    28
route-truth status projection                     1
effective research status              PROVIDER_PENDING
score / Stage authority                  false / false
```

따라서 이 시점의 PASS는 **capture 보존과 exact-data 병합 PASS**이지 full-thesis 완료가 아니다. 다음 실행은
동일 pass capture를 `REUSE_CAPTURE`로 사용해 submit 0으로 effective snapshot을 영구 저장한 뒤, 남은 exact
parser/source 공백만 같은 conversation에서 이어간다. 상세 수치는
`p10_c06_public_gap_capture_merge_receipt.json`에 고정했다.

첫 actual 재개에서는 browser submit delta 0과 conversation recovery는 통과했지만, ledger가 capture를 가진
`RESEARCH_RUNNING` pass를 “이미 시도한 context”로 간주해 건너뛴 뒤 다음 pass를 만들려 했다. 그 결과
`another fresh follow-up is still incomplete`로 fail-safe 정지했다. 원인은 context dedup 조건이
`submit_count=1`만 보고 `status=COMPLETE`를 요구하지 않은 것이었다.

수정 뒤에는 다음처럼 분리한다.

```text
submit_count=1 + RESEARCH_RUNNING/TRANSPORT_PENDING
→ 같은 durable pass 재계획
→ READY capture가 있으면 REUSE_CAPTURE
→ 새 submit 0

submit_count=1 + COMPLETE
→ 같은 semantic context 재시도 금지
```

즉 “한 번 보냈다”와 “그 답안을 병합·검증까지 완료했다”를 같은 상태로 취급하지 않는다. 회귀 테스트는
submit 직후 `_context_already_attempted=false`, durable completion 뒤 `true`를 검증하며 기존 submitted-result
recovery 두 사례와 함께 3/3 통과했다.

재개 뒤 pass 02 capture는 submit delta 0으로 실제 재사용됐고 새 사실 14개와 route 33개가 effective
dossier에 영구 저장됐다. 재검증 accepted fact는 21개에서 32개로 증가했고 deterministic 공백은 다음처럼
줄었다.

```text
public material gap       21 → 13
source linkage incomplete  9 →  6
accepted facts            21 → 32
```

변경된 snapshot의 exact gap context에 대해 pass 03
`PROPASS-5e45eef5db23629f4e757e04`를 같은 conversation에 한 번 전송했다. 약 105분 뒤 새 V3 JSON을
같은 assistant turn에서 회수했으며 자동 재전송은 0이었다.

```text
prompt hash      402094b1bd5c0ce8f30d8855877f18b42a6a8c56dff0e4aa1078b8f7c7de0ecd
raw report hash  cbc113bf637d5648e392145f57f9489c958206eb269cd9f6f9459877d02432f4
report hash      e8b7ca893c6894f80f8f18421fbaa0673c2977ab1330e0bb47f3f4094230aa3f
V3 JSON hash     c2d01adb0b9cc9eef89be822a96875e958fbfc3661ae6527384240a28ff222d0
```

pass 03 delta는 기존 검증 문서를 재사용해 새 사실 3개를 만들고 source document와 lineage row는 다시
출력하지 않았다. V3 graph의 사실은 각각 기존 `source_document_id`를 정확히 가리켰지만, 중복 색인인
`source_lineages[*].fact_ids`에는 그 3개가 없어서 strict roster 검문이 fail-safe 정지했다.

merger는 이제 기존 source document의 immutable `lineage_id`와 새 fact의 `source_document_id` edge에서
누락 roster member만 추가한다. 새 URL, 새 문서, 새 fact 내용, lineage identity는 만들지 않는다. 반대로
lineage에 잘못 들어간 초과 member는 삭제하지 않고 strict validator가 계속 거부한다.

실제 pass 03 capture 오프라인 재병합 결과는 다음과 같다.

```text
exact capture offline merge                  PASS
new / effective facts                        3 / 42
new / effective source documents             0 / 23
new / effective source lineages               0 / 21
new / effective route receipts               20 / 90
effective mandatory questions                    28
graph-derived roster additions                    3
effective research status              PROVIDER_PENDING
```

관련 V2/V3 delta·saturation·fresh orchestration·repair 회귀는 128/128, compileall과 diff check는 PASS다.
상세 capture identity와 정확한 roster addition은
`p10_c06_public_gap_second_capture_merge_receipt.json`에 고정했다.

## 2026-08-27 — P10 C06 actual 3차 V3 JSON 회수와 질문–사실 계보 검문 수리

pass 03을 submit 0으로 재사용·병합한 뒤 같은 conversation에서 pass 04
`PROPASS-b2a41069565bc54d9c941209`를 정확히 한 번 전송했다. 약 80분 뒤 화면에 표시된
`ResearchDossierV3_SKHynix_000660_asof_2026-08-23.json`을 같은 assistant turn에서 실제 다운로드했다.
이 단계의 필수 산출물은 MD가 아니라 **V3 JSON**이다. 정규화 전후 MD는 전송 감사용이고, PDF는 같은
응답에 존재할 때만 받는 선택 항목이다.

```text
capture source      DIRECT_REPORT_DOM_NORMALIZED
assistant turn      request-6a8db0ad-8ed0-83e8-888e-dce26c950343-2
submit / resubmit   1 / 0
prompt hash         57db2da444a4a826b15128f12620711264146fa6c7134c7dbb00b0a3e296af98
raw report hash     926a1b81e05bdea335a1920922c7d24a0b3965c9f7277d15652e66601114fa4c
report hash         25666253b3fc0a52a248dfef50642b8a2e684d9d9c659052d607cc321c8fd796
V3 JSON hash        980fc98d71817c5afaa3d2027cf5b8c0aa63bd00e1248f6d8d4f041cd5224161
PDF                 없음(null, 오류 아님)
```

첫 실제 병합은 `question references a fact bound to another question` 검문에서 fail-safe 정지했다.
initial V3는 strict schema 앞에서 `PreSchemaV3Normalizer`를 거치지만 follow-up V3만 이 경계를 건너뛰던
것이 원인이었다. 또한 follow-up이 이전 pass의 immutable fact를 참조하면 delta 단독으로는 그 fact의
backlink를 볼 수 있으므로, 누적 graph를 만든 뒤 한 번 더 같은 보수적 투영이 필요했다.

수리는 두 경계를 일반화했다.

```text
현재 follow-up delta
→ initial과 동일한 V3 pre-schema normalization
→ job/run/pass identity 결박
→ append-only 누적 graph 병합
→ 누적 graph에서 fact backlink가 없는 질문 참조만 제거
→ strict V3 validation
```

쉬운 예: 사실 F가 질문 A의 증거라고 사실 원장에 적혀 있는데 질문 B가 F 번호를 실수로 함께 적었다면,
사실 F를 삭제하거나 “B도 지원한다”고 바꾸지 않는다. 질문 B의 중복 번호만 제거한다. 알 수 없는 fact id는
자동 삭제하지 않아 strict validator가 계속 조작·오타를 거부한다.

actual pass 04에서는 정확히 두 참조가 이 원칙에 따라 제거됐다.

```text
현재 delta:
R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_Q03 (`resolution_fact_ids`)
→ PROFACT-P4-R13-CONSOLIDATED-GOING-CONCERN-NOT-APPLICABLE 제거

누적 graph:
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_Q01 (`resolution_fact_ids`)
→ PROFACT-C06-HBM4-MASS-SHIPMENT 제거
```

사실 statement, excerpt, source document, fact의 question roster는 하나도 수정하지 않았다. 종목명·아키타입·
질문명별 예외도 추가하지 않았다. actual capture를 브라우저·전송 없이 정확히 재생한 결과는 다음과 같다.

```text
exact capture offline merge                  PASS
new / effective facts                       10 / 52
new / effective source documents             3 / 26
new effective / total source lineages        3 / 24
new / effective route receipts              25 / 115
effective mandatory questions                    28
effective research status              PROVIDER_PENDING
focused regression                         144/144 PASS
score / Stage authority                  false / false
```

따라서 이 기록도 full-thesis 최종 점수 receipt가 아니라 **실제 V3 JSON 다운로드와 안전한 병합 경계의
검증 receipt**다. 다음 실행은 이 READY capture를 `REUSE_CAPTURE`로 읽어 browser submit 0을 확인한 뒤
재검증·saturation을 계속한다. 상세 identity, hash, 두 투영은
`p10_c06_public_gap_third_capture_merge_receipt.json`에 고정했다.

이후 실제 runner 재개에서도 pass 04 READY capture를 `FOLLOWUP_CAPTURE_REUSED`로 읽었고
`browser_submit_delta=0`을 확인했다. effective dossier 52 facts / 26 documents / 24 lineages / 115 routes /
28 questions가 영구 저장됐으며 파일 hash는
`e60b7a109e4ea00e7003590b578891a764914c93d1dd603ad992c64ca939f125`다. source-backed 재검증 뒤
accepted fact는 32 → 33, nonterminal question은 9 → 7, provider/parser core pending은 5 → 4,
source-linkage incomplete는 8 → 6으로 줄었다.

다만 이 snapshot에서 아직 공개자료로 조사 가능한 material gap 15개가 남아 deterministic saturation이
pass 05 `PROPASS-26c03ab89ff306eec50c9e3c`를 같은 conversation에 한 번 전송했다. pass 05가 실행 중인
동안 score/Stage는 계속 withheld다. 이 전송은 pass 04 재사용 실패로 인한 중복 제출이 아니라, pass 04
병합으로 바뀐 exact snapshot을 입력으로 만든 다음 semantic gap pass다.

pass 05는 약 59분 뒤 완료됐고 같은 assistant turn의 V3 JSON을 자동 다운로드했다. 사용자가 화면의
다운로드 버튼을 다시 누르지 않았으며 submit은 1, automatic resubmit은 0이다.

```text
assistant turn      request-6a8db0ad-8ed0-83e8-888e-dce26c950343-3
prompt hash         0d5f0b61adfa86544ccf4987e58a2cf4b0e51bbdba0704d42efe86a0ed1b6a6e
raw report hash     4403d04d1a70f2beba18e23512dbc4ac5ffaaf24d7fd53c7bdc9c8678ab4e41e
report hash         432b9d72dcbc13b88ead8cae113456b65d14fade6c646d7be4f165c439b4bc54
V3 JSON hash        95e7b4cb6c85cf5029f4da69c3882ee487a2ecb19e400bfbfb710879ff2ae745
new docs / facts    2 / 17
new routes          27
updated questions   19
PDF                 없음(null, 오류 아님)
```

병합 뒤 effective dossier는 69 facts / 28 documents / 26 lineages / 142 routes / 28 questions다.
누적 graph에서 `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_Q05`가 backlink 없이 참조한
`PROFACT-R13-TOTAL-ISSUED-SHARES` 한 edge만 제거됐고 fact 내용은 유지됐다. persisted file hash는
`f6de52e011c4cb48a3804cf3649aa1e113b0b4756ede80aee6b66c1a81dd7eb8`다.

source-backed 재검증 결과 accepted fact는 33 → 36, nonterminal question은 7 → 3,
provider/parser core pending은 4 → 1, source-linkage incomplete는 6 → 2로 줄었다. 공개 material gap은
15 → 18로 늘었지만 이는 실패 증가가 아니라 새 evidence graph가 이전의 넓은 질문을 더 구체적인 공개자료
확인 항목으로 펼친 결과다. saturation은 아직 invalid이므로 score/Stage는 계속 withheld다.

변경된 exact snapshot을 입력으로 pass 06 `PROPASS-330252bb6db7ee3267fab916`을 같은 conversation에
한 번 전송했다. 상세 capture와 post-merge 수치는
`p10_c06_public_gap_fourth_capture_merge_receipt.json`에 고정했다.

pass 06은 약 44분 뒤 완료됐고 같은 assistant turn의 V3 JSON capture는 정상 저장됐다.

```text
assistant turn      request-6a8db0ad-8ed0-83e8-888e-dce26c950343-4
prompt hash         71bd8763eda7bb2b93bbab2f777164570ca0ee6cb58663825ebe2c638046f04d
raw report hash     6eb13d9c8a80096a48d40ad3218c45a37d711e6057398465217eb8bc07cad2c1
report hash         8c8a483dd74d20f6424bcf6ccb02ecdacafeac45ad1020b6364e4b1cc2f748dc
V3 JSON hash        4a033c7741892968c20c894b43bdb2cefd0ee8120fb8f223f1eedcd3b65bc479
raw fact rows       15
new docs / routes   1 / 28
updated questions   19
PDF                 없음(null, 오류 아님)
```

첫 병합은 `duplicate atomic predicate/source/excerpt identity` 검문에서 fail-safe 정지했다. 실제 JSON을
이전 effective graph와 strict validator의 동일 identity로 대조하니 15개 중 9개가 이전 fact와 같은
`source_document_id + predicate_id + normalized subject + normalized excerpt`를 새 ID로 반복한 것이었다.
첫 오류 ID 하나만 예외 처리하면 뒤의 8개에서 다시 멈추므로, exact atomic identity 정책을 validator와
merger가 공유하도록 일반화했다.

follow-up merger는 이제 이전 valid graph와 fact kind까지 같은 exact duplicate만 기존 canonical fact로
투영한다. 새 duplicate row의 statement, confidence, period 같은 변경값은 채택하지 않고 기존 fact를 그대로
보존한다. question, lineage, route, derived input의 fact reference만 canonical ID로 바꾼다. 동일 pass 안의
중복, MATERIAL/COUNTER/RESOLUTION kind 충돌, unknown fact는 계속 strict failure다.

쉬운 예: 이전 장부의 영수증 `F1`과 출처·항목·주체·원문이 완전히 같은 영수증을 다음 pass가 `F9`로
다시 냈다면 `F9`를 새 실적으로 두 번 세지 않는다. `F9`가 가리키던 경로만 `F1`로 연결한다. 반면 원문이나
항목이 다르면 자동으로 합치지 않는다.

실제 pass 06 capture의 parser → dialect adapter → pre-schema → identity binding → delta merge 전체를
브라우저·전송 없이 재생한 결과는 다음과 같다.

```text
exact capture offline merge                  PASS
Pro fact rows                                  15
prior exact duplicates                         9
actual new facts                                6
effective facts                               75
effective source documents                    29
effective source lineages                     27
effective route receipts                     170
effective mandatory questions                 28
effective research status       PROVIDER_PENDING
focused regression                       145/145 PASS
score / Stage authority            false / false
```

raw capture와 기존 canonical fact는 수정하지 않았다. 다음 실행은 동일 pass 06 READY capture를
`REUSE_CAPTURE`로 읽어 browser submit 0으로 영구 병합·재검증한 뒤 saturation을 계속한다. 상세 9개 mapping과
신규 6개 fact ID는 `p10_c06_public_gap_fifth_capture_merge_receipt.json`에 고정했다.

실제 runner 재개에서도 pass 06은 `FOLLOWUP_CAPTURE_REUSED`, `browser_submit_delta=0`으로 처리됐다.
중복 9개를 제외한 신규 fact 6개와 route 28개만 반영됐고 effective dossier는 75 facts / 29 documents /
27 lineages / 170 routes / 28 questions로 영구 저장됐다. persisted file hash는
`0b6c41c9fa33239fdbe44a142d658f8b0a23d2a087843dc11c7ad9171a3d697a`다.

재검증 accepted fact는 36 → 39로 늘었다. provider/parser core pending은 1로 유지됐고, 새 graph가 이전
질문 edge를 정직하게 다시 열면서 nonterminal question은 3 → 4, source-linkage incomplete는 2 → 3이 됐다.
따라서 아직 score/Stage로 넘기지 않았다.

다음 pass 07 계획 직후 Playwright의 dialog 자동 처리 경합이 `No dialog is showing`으로 driver를 닫았다.
ledger를 직접 확인했을 때 pass 07 `PROPASS-73881856ab23461cd67a18c1`은 `PLANNED`, submit count 0,
submitted_at/response_hash null이었다. runner 재시작은 기존 planned row를 회복해 정확히 한 번 전송했고
현재 `RESEARCH_RUNNING`이다. 즉 transient browser-driver 오류가 새 pass 생성이나 중복 전송으로 이어지지
않았다.

### 2026-08-27 — C06 pass 07 V3 JSON과 중복 문서 범위 충돌 처리

pass 07은 약 69분 뒤 완료됐고 같은 assistant turn의 V3 JSON이 READY capture로 저장됐다. 이 단계의
필수 산출물은 **같은 응답의 `ResearchDossierV3` JSON**이다. 이전 진행 문구의 “새 MD 실다운로드”는
과거 전송 형식에 끌려간 부정확한 표현이었다. 현재 운영 경로는 JSON을 먼저 읽고, 화면 보고서 텍스트는
transport 보존본, PDF는 같은 응답에 실제 export가 있을 때만 받는 선택 증빙으로 취급한다.

```text
assistant turn      request-6a8db0ad-8ed0-83e8-888e-dce26c950343-5
prompt hash         070df189a5dffe764c7c31088d0241b6e43708abc08a9097331c05d1147fe540
raw report hash     8f89ca980eeaa8c9d3f0b1f5e43efa53f8d3455b7baf7ebd0f76f9975744a468
report hash         c46ac1188e9dd83a5b53fc567279125c2417e36f5dbb11a6923cb7a1485bb1c0
V3 JSON hash        bef6a8697fb288bad1ea3c2c8cb8c722d085ba80950f583543b7657d3c5e1b05
raw docs / facts    1 / 10
raw lineages/routes 4 / 19
updated questions   19
PDF                 없음(null, 오류 아님)
```

첫 병합은 `duplicate or empty canonical source URL identity`에서 fail-safe 정지했다. 같은 KRX URL이
pass 04의 `PROSRC-P4-SKH-AUDIT-KRX-20260304`와 pass 07의
`PROSRC-P7-KRX-SKH-SUBSIDIARY-AUDIT-20260304`로 반복됐지만, 기존 document는 issuer 범위이고 새
document는 non-issuer 자회사 범위였다. URL만 보고 새 ID를 기존 ID로 바꾸면 자회사 사실이 본사 사실처럼
보일 수 있으므로 그렇게 합치지 않았다.

일반 병합 규칙은 다음처럼 고정했다.

```text
같은 URL + 같은 target/issuer scope
→ 기존 canonical document ID 재사용
→ 새 fact의 source reference만 canonical ID로 연결

같은 URL + 서로 다른 target/issuer scope
→ 기존 document 불변 보존
→ 충돌하는 새 duplicate document와 그 document에만 의존하는 새 fact 제외
→ raw JSON과 검색 route receipt는 감사용으로 보존

같은 pass 안에서 URL 중복
→ 자동 합치지 않고 strict validation 실패 유지
```

쉬운 예: 한 공시 URL 안에 본사와 자회사 표가 함께 있어도 “같은 링크”라는 이유만으로 자회사 감사 결과를
본사 감사 결과로 바꾸면 안 된다. 어느 범위인지 deterministic하게 결박할 수 없는 새 행만 점수 그래프에서
빼고, 기존 장부와 원본 캡처는 그대로 두는 편이 안전하다.

실제 pass 07에서는 자회사 범위 resolution fact 3개만 제외됐고, 나머지 7개 사실은 정상 반영됐다.
parser → V3 dialect → pre-schema → durable pass identity → append-only merge → strict validator 전 경로를
브라우저 전송 없이 정확히 재생한 결과는 다음과 같다.

```text
exact capture offline merge                    PASS
Pro fact rows                                    10
scope-conflicting dependent facts excluded        3
actual new facts                                  7
effective facts                                  82
effective source documents                       29
effective source lineages                        27
effective route receipts                        189
effective mandatory questions                    28
effective research status          PROVIDER_PENDING
V3 targeted regression                       20/20 PASS
WSL non-browser focused                      128/128 PASS
Windows Chromium capture                       20/20 PASS
assertion failures                                  0
score / Stage authority                 false / false
```

WSL의 browser 20개는 test body 전에 `libnspr4.so`가 없어 환경 오류가 났고, 동일 20개를 실제 Windows
Chromium에서 실행해 failure/error 0을 확인했다. 특히 이전 MD 버튼 미선택, 현재 산출물 실다운로드,
일치하는 PDF의 선택 캡처가 유지됐다. 상세 hash, 제외 fact ID, cross-platform test 수는
`p10_c06_public_gap_sixth_capture_merge_receipt.json`에 고정했다.

현재 SQL ledger의 pass 07은 `RESEARCH_RUNNING`, submit count 1, response hash null, snapshot 0이고
READY capture는 hash-bound 상태다. 다음 실행은 새로 전송하지 않고 이 capture를 `REUSE_CAPTURE`로 읽어
browser submit delta 0을 확인한 뒤 영구 snapshot·source 재검증·deterministic saturation을 계속한다.

실제 runner 재개에서도 pass 07은 `FOLLOWUP_CAPTURE_REUSED`, `browser_submit_delta=0`으로 처리됐다.
신규 사실 7개와 경로 19개가 반영됐고 effective dossier는 82 facts / 29 documents / 27 lineages / 189
routes / 28 questions로 영구 저장됐다. persisted file hash는
`e2fdc72738c52e87a74082561c7769cdbac7847102f700b89f629bea0970468b`다. 재검증 accepted fact는
39로 유지됐고, 변경된 exact graph에서 nonterminal 6, provider/parser core pending 4, public material gap
15, source-linkage incomplete 5가 남았다.

따라서 pass 08 `PROPASS-c2dd5ebc4e49628f26459c3e`를 같은 conversation에 한 번 전송했다. pass 08은
약 49분 뒤 완료됐고 같은 assistant turn의 V3 JSON을 자동 캡처했다.

```text
assistant turn      request-6a8db0ad-8ed0-83e8-888e-dce26c950343-6
prompt hash         ba29a00623a8abdb8b84a49906856bf1a02efb36f498caa693182bf40eb30833
raw report hash     0ba772b5a288a28de02db059de06b281d57c245d664990bd461576ad793c77c5
report hash         878ab8fce2e3596170bc0d40be281c52289e9183d3d4571a95d3edba957074d9
V3 JSON hash        3e7205f69cfbb60e7b978b2314b6cafe327f6e21fd9610a4ed8c0be68a79a183
raw docs / facts    1 / 9
raw lineages/routes 4 / 28
updated questions   19
PDF                 없음(null, 오류 아님)
```

원본 사실 9개 중 3개는 pass 07과 source document, predicate, normalized subject, excerpt, fact kind까지
같은 exact atomic identity였다. 기존 canonical fact를 수정하지 않고 새 ID의 참조만 기존 ID로 연결해 실제
신규 사실은 6개가 됐다. 병합과 source-backed 재검증 결과는 다음과 같다.

```text
actual new facts                               6
effective facts                               88
effective source documents                    30
effective source lineages                     28
effective route receipts                     217
accepted source-backed facts                  42
verification query / search                  0 / 0
nonterminal mandatory questions                4
provider/parser core pending                    2
public material gaps                           17
source-linkage incomplete                       3
research saturation valid                   false
score / Stage authority            false / false
```

쉬운 예: pass 07의 “HBM4 샘플 출하” 문장을 pass 08이 새 번호로 다시 제출했어도 판매 실적으로 두 번 세지
않는다. 대신 새로 확인된 감사인 지정·현재 감사 범위 같은 별도 원자는 보존하고, 실제 원문 검문을 통과한
것만 accepted fact 42개에 넣는다.

이 snapshot도 아직 saturation이 아니므로 pass 09 `PROPASS-ed72e2b8b8c1328e8e98a5b4`를 같은
conversation에 정확히 한 번 제출했고 현재 `RESEARCH_RUNNING`이다. 코드 commit `16570d85`의 E2R
Pro-first와 E2R v6 GitHub Actions는 모두 SUCCESS다. 상세 pass 07 reuse와 pass 08 identity·hash·검증 수는
각각 sixth/seventh capture merge receipt에 고정했다.

pass 09는 약 48분 뒤 완료됐고 같은 assistant turn의 V3 JSON capture는 정상 저장됐다.

```text
assistant turn      request-6a8db0ad-8ed0-83e8-888e-dce26c950343-7
prompt hash         4790fba98dba798a23731b72e98f94f848d9098231c79102e98aee50fbeec8f5
raw report hash     e86a496c9116dc0d52bd72d9db65c0bb682f9417187be7c48e4e1e6d1214b549
report hash         d272dbce15bca6af8fcd632c2fff1bb378d10ad1e40004da9b8373b6e82e2ab9
V3 JSON hash        14014ecad82958c4c7e112e80cbf71f50e77079a07d12e4b6a9209ad73c95d46
raw docs / facts    2 / 4
raw lineages/routes 3 / 24
updated questions   19
PDF                 없음(null, 오류 아님)
```

첫 병합은 `SL-SKH-DRSA-20260508`의 기존 `independence_group_id`를 pass 09가 다른 값으로 적어
`follow-up rewrote source lineage identity`에서 fail-safe 정지했다. 같은 lineage를 새 independence group으로
바꾸면 동일 출처를 독립 출처 두 개처럼 셀 위험이 있으므로 새 값을 채택해서는 안 된다.

V3 follow-up은 이제 기존 lineage ID가 있으면 그 lineage의 `independence_group_id`와 `status`를 prior valid
graph 그대로 보존한다. 새 document/fact edge만 append하고, 나머지 graph는 strict validator가 그대로
검사한다. 원본 capture와 fact statement/excerpt는 수정하지 않으며 투영 내역과 전후 값 hash를 saturation
감사 필드에 남긴다. V2의 기존 identity 재결박 시도는 계속 strict failure다.

쉬운 예: 기존 영수증 묶음 `L1`을 이미 “발행사 공시 한 묶음”으로 세었는데 다음 답변이 `L1`을 “새 독립
출처 묶음”이라고 이름만 바꿔도 독립 증거 하나를 둘로 세면 안 된다. 묶음 identity는 그대로 두고, 실제 새
영수증과 사실만 그 묶음에 추가한다.

실제 pass 09 capture의 parser → pre-schema → identity binding → lineage identity preservation → append-only
merge → strict validation 전체를 브라우저·전송 없이 재생한 결과는 다음과 같다.

```text
exact capture offline merge                  PASS
actual new facts                                4
effective facts                                92
effective source documents                     32
effective source lineages                      30
effective route receipts                      241
effective mandatory questions                  28
effective research status        PROVIDER_PENDING
focused regression                         72/72 PASS
V2 strict identity-rebind failure        unchanged
score / Stage authority              false / false
```

raw capture는 READY로 보존됐고 SQL pass는 submit count 1인 `RESEARCH_RUNNING`, response hash null이다.
다음 실행은 같은 capture를 `REUSE_CAPTURE`로 읽어 browser submit delta 0을 확인한 뒤 source 재검증과
deterministic saturation을 계속한다. 상세 identity hash와 신규 fact ID는
`p10_c06_public_gap_eighth_capture_merge_receipt.json`에 고정했다.

실제 runner 재개에서도 pass 09는 `FOLLOWUP_CAPTURE_REUSED`, `browser_submit_delta=0`으로 처리됐다.
신규 사실 4개와 route 24개가 반영됐고 effective dossier는 92 facts / 32 documents / 30 lineages /
241 routes / 28 questions가 됐다. source-backed 재검증 accepted fact는 42 → 45로 늘었다. 같은 변경
snapshot에서 pass 10 `PROPASS-222c4db866a10be35f8aa25b`를 같은 conversation에 정확히 한 번 전송했다.

### 2026-08-27 — 과거 parser 실패 영구 오염과 검문 실패의 검색 오배송 수리

pass 10 응답을 기다리는 동안 pass 09 기준 saturation receipt를 질문별로 역추적했다. 기존
`evaluate_route_adequacy()`는 질문에 누적된 **모든 과거 route**의 provider/parser가 SUCCESS여야 현재
질문도 정상이라고 판단했다. 이 때문에 이전 pass에서 oversized filing parser가 실패한 뒤 후속 pass가
같은 질문의 공식 filing을 정상으로 읽고 새 fact까지 검증해도 과거 실패 한 줄이 질문을 계속 막았다.

쉬운 예: 2차에 문이 잠겨 영수증을 못 읽었지만 9차에 같은 질문의 영수증을 정상으로 읽었다면, 2차 실패는
감사 이력으로 남겨야 하지만 9차 현재 상태까지 실패로 만들면 안 된다. 반대로 9차 한 묶음 안에서 영수증
두 장 중 한 장이 여전히 안 읽히면 다른 한 장의 성공으로 덮어서는 안 된다.

따라서 질문 route ID의 append-only 순서를 이용해 마지막으로 추가된 pass cohort를 현재 provider/parser
상태로 판정한다. 과거 route와 hash는 삭제하지 않는다. 최신 cohort의 route는 전부 정상이어야 하며,
absence fixpoint의 exact question/gap/fact snapshot/lineage snapshot 결박은 그대로 유지한다.

동시에 누적 question row가 rejected fact ID를 계속 참조하는 경우도 `PUBLIC_GAP_CLOSURE`로 보내고 있었다.
이는 새 웹 검색으로 고칠 문제가 아니라 기존 후보를 정확한 quote로 수정하거나 철회하는 verifier repair
문제다. terminal fact-backed 질문이고 현재 source route와 core source role은 충분하지만 fact/lineage
무결성 failure가 남은 경우를 `verifier_repair_pending_ids`로 분리했다. core source role 자체가 없으면 계속
public acquisition blocker라서 repair 하나로 다른 core gap을 가리지 않는다.

pass 09의 실제 45 accepted fact snapshot을 새 코드로 읽기 전용 재계산한 결과는 다음과 같다.

```text
                                    before   after projection
nonterminal questions                    4                  4
public material gaps                    17                 16
verifier repair pending                  0                 13
provider/parser core pending             2                  2
source linkage incomplete                3                  3
historical failure가 현재를 오염          yes                 no
rejected reference를 다시 검색            yes                 no
research saturation valid            false              false
```

즉 blocker를 지운 것이 아니라 잘못된 작업 대기열을 바로잡았다. 현재 실제 provider/parser pending 2개와
공개 hard-break gap은 그대로 남고, rejected fact 참조 13개는 compact verifier repair로 간다.

이 수정 중 pass 10은 ChatGPT에서 이미 작성 중이었다. runner를 새 코드로 교체한 첫 시도에서 새 routing을
먼저 계산해 기존 `submit_count=1` pass와 충돌하는 복구 순서 결함도 확인했다. fresh V3 tail은 이제 코드나
검증 결과가 바뀌어 다음 pass 종류가 달라져도, 이미 전송됐고 snapshot이 없는 pass를 항상 먼저 회수한다.
pass 10 recovery의 실제 결과는 다음과 같다.

```text
pass id                 PROPASS-222c4db866a10be35f8aa25b
durable submit count    1
conversation            6a8db0ad-8ed0-83e8-888e-dce26c950343
recovery event           FRESH_FULL_THESIS_SUBMITTED_PASS_RECOVERY
browser submit delta     0
current browser state    RESEARCH_RUNNING
```

회귀는 과거 실패→최신 성공, 과거 성공→최신 실패, 같은 최신 cohort의 성공+실패 혼합, rejected 누적 fact의
repair routing, routing 변경 중 submitted-pass 우선 recovery를 각각 검사한다.

```text
saturation unit tests                  32/32 PASS
saturation + fresh recovery            57/57 PASS
cross-module focused                  109/109 PASS
Pro-first static audit              PASS / critical 0
Pro-first V2 static audit           PASS / critical 0
fresh efficiency static audit       PASS / critical 0
production static audit             PASS / critical 0
compileall / git diff check          PASS / PASS
```

상세 전후 수치와 pass 10 exactly-once recovery 식별자는
`p10_c06_route_state_and_repair_routing_receipt.json`에 고정했다. 이 시점은 아직 saturation이 아니므로
score/Stage authority는 계속 false다.

### 2026-08-27 — pass 10 현재 JSON 회수와 질문 단위 반복 차단

pass 10 `PROPASS-222c4db866a10be35f8aa25b`는 같은 Pro 대화에서 약 55분 뒤 완료됐다. 현재
assistant turn에는 최초 전체 dossier가 아니라 다음 이름의 pass delta JSON이 붙었다.

```text
ResearchDossierV3_SKHynix_000660_PUBLIC_GAP_CLOSURE_
PROPASS-222c4db866a10be35f8aa25b_delta.json
```

Library에 남아 있는 `ResearchDossierV3_SKHynix_000660_asof_2026-08-23.json`은 최초 전체 dossier다.
따라서 파일 형식이 JSON이라는 사실만으로 고르지 않고, **현재 assistant turn + 현재 job/run/pass marker**가
일치하는 첨부만 다운로드한다. 쉬운 예로 pass 10을 기다리는 중에 최초 JSON의 다운로드 버튼이 보여도
그 파일을 pass 10 결과로 합치지 않는다.

첫 회수에서는 유효한 보고서 본문에 DART gateway에서 `오류가 발생`했다는 문장이 있다는 이유로 전체
대화 본문 검색이 `RETRYABLE_ERROR`를 잘못 만들었다. 실제 ChatGPT 오류 alert나 quota toast는 없었고,
현재 turn에는 완결 marker와 정확한 JSON 첨부가 있었다. 운영 오류 판정은 이제 `role=alert`, assertive
live region, error/quota/toast 같은 **별도 가시 UI 표면**만 읽는다. 연구 본문이 parser 오류를 사실로
설명해도 브라우저 장애로 재라벨하지 않는다. 장시간 누적된 전체 대화 본문도 매 poll마다 Python으로
옮기지 않는다. 첨부 파일명 존재 여부와 최신 assistant 상태는 브라우저 안에서 boolean으로만 계산하고,
진단 문자열이 꼭 필요할 때만 마지막 2,000자를 가져온다.

수리 후 같은 pass를 다시 전송하지 않고 현재 turn을 회수했다.

```text
pass id                              PROPASS-222c4db866a10be35f8aa25b
submit count                         1
automatic resubmit                   0
browser submit delta during recovery 0
assistant turn                       2190eb6d-3952-4570-9fd0-57bc90392435
capture source                       DIRECT_REPORT_DOM_NORMALIZED
raw/effective new facts              8 / 5
effective facts                      92 -> 97
source documents                     32 -> 32
source lineages                      30 -> 30
route receipts                       241 -> 255
accepted source-backed facts         45 -> 48
verification query/search            0 / 0
```

새 fact 8개 중 이전 source/document/predicate 원자와 같은 3개는 중복 계보로 두 번 세지 않았다. 실제로
추가된 5개는 SEC 잠정 실적표의 매출·영업이익 원자 2개와 감사보고서안 승인·감사결과 보고·회사 관계자
없는 외부감사인 회의 원자 3개다. 새 문서나 새 독립 계보를 가장해 만들지 않고 기존 source graph에
append했다.

pass 10 뒤에는 mandatory 28개 중 nonterminal 4개, public material gap 16개, verifier repair pending
13개, provider/parser core pending 2개, source-linkage incomplete 3개가 남았다. 따라서 점수·Stage 권한은
계속 false이고 pass 11에는 실제 상태가 바뀐 다섯 질문만 보냈다.

```text
C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q07
R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_Q05
R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_Q01
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_Q01
R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_Q01
```

기존 pass는 여러 질문의 aggregate snapshot hash만 저장했다. 그래서 A 질문이 닫혀 전체 fact hash가
바뀌면 상태가 그대로인 B 질문도 다시 보낼 수 있었다. 이제 각 question마다 status, failure, verified
fact, source lineage, linked route를 canonical hash로 저장한다. 완료된 같은 question hash는 다음 pass에서
제외한다. 예를 들어 A에 새 fact가 생겨도 B의 근거·상태가 같으면 B는 재전송하지 않는다.

또한 top-level route receipt만 늘고 새 fact·source lineage·question closure가 전혀 없으면 research
semantic progress로 세지 않는다. 질문에 실제로 연결되어 attempted role/status가 바뀌는 route는 question
state 변화로 남지만, 질문과 연결되지 않은 영수증만 반복 생성해서 다음 pass를 여는 일은 막는다.

pass 11의 prompt는 18,275자였다. 장시간 열린 ProseMirror에서 Playwright `fill`의 actionability가
60초 동안 끝나지 않아 첫 준비는 submit 0으로 안전하게 종료됐다. 8,000자 이상 prompt는 이미 검증된
browser-local visible DOM 입력을 쓰도록 범위를 넓힌 뒤 같은 durable pass를 정확히 한 번 전송했다.
현재 pass 11은 같은 conversation에서 `RESEARCH_RUNNING`, submit count 1이며 score/Stage authority는
false다.

현재 코드 검증은 다음과 같다.

```text
browser/dossier/saturation/fresh 관련 회귀       161/161 PASS
최신 browser state poll 회귀                      28/28 PASS
전체 unittest                                  7,732 PASS
전체 failure / error                                0 / 0
기존 skip                                             38
Pro-first static audit                         PASS / critical 0
Pro-first V2 static audit                      PASS / critical 0
fresh efficiency static audit                  PASS / critical 0
production static audit                        PASS / critical 0
compileall / git diff check                     PASS / PASS
```

pass 11의 현재-turn JSON이 생성되면 같은 다운로드·marker 결박·append-only merge·source 재검문을 수행하고,
그 결과를 별도 receipt로 고정한다. 아직 C06 saturation을 선언하지 않는다.

#### pass 11 현재-turn JSON 병합과 실운영 질문 dedup

pass 11은 약 40분 뒤 완료됐다. 최초 전체 JSON이나 pass 10 첨부를 다시 받지 않고, 현재 assistant turn의
다음 delta만 `DIRECT_REPORT_DOM_NORMALIZED`로 캡처했다.

```text
ResearchDossierV3_SKHynix_000660_PUBLIC_GAP_CLOSURE_
PROPASS-ca6f4aba9e077315067b5f67_delta.json
```

```text
submit count                         1
automatic resubmit                   0
raw report hash                      7ecf102e...f96a283
normalized report hash               51fe5707...598ad5d
V3 JSON hash                         64de2962...841c93
effective facts                      97 -> 102
source documents                     32 -> 35
source lineages                      30 -> 33
route receipts                       255 -> 266
mandatory questions                  28 -> 28
```

새 row는 cutoff-day 종가·거래량·거래대금·외국인 순매수·기관 순매수 5개다. append-only 병합은 성공했지만
deterministic source verifier는 이 5개를 점수 facts로 채택하지 않았다. accepted fact는 48로 유지됐고,
quote mismatch 17→21, source unavailable 12→13으로 반려 사유가 정확히 남았다. 즉 Pro가 값을 가져왔다고
바로 쓰지 않고, 원문 검문을 통과하지 못한 값은 점수 그래프 밖에 둔다.

재검문 후 변화는 다음과 같다.

```text
nonterminal mandatory questions       4 -> 2
provider/parser core pending           2 -> 2
source linkage incomplete              3 -> 2
verifier repair pending               13 -> 14
public material gaps                  16 -> 16
accepted facts                        48 -> 48
verification query/search              0 / 0
research saturation valid              false
```

nonterminal은 audit/restatement residual 두 질문만 남았다. cutoff positioning 질문은 Pro가 terminal로
제안했지만 새 사실이 verifier에서 탈락했으므로 전체 thesis는 열리지 않고 repair/public gap으로 남았다.

pass 11은 다섯 질문을 받았지만, 다음 routing에서 상태가 그대로인
`R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_Q01`은 per-question hash가 일치해 제외됐다. pass 12
`PROPASS-787438355e0c6f2da764cd1e`는 실제로 바뀐 네 질문만 같은 대화에 submit count 1로 전송됐다.

```text
C06_HBM_MEMORY_CUSTOMER_CAPACITY_Q07
R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_Q05
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_Q01
R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_Q01
```

이는 단위테스트만의 주장이 아니라 실제 SQL ledger의 pass 11/12 question hash와 submit row로 확인했다.
pass 12 결과가 나올 때까지 점수·Stage authority는 계속 false다.

#### pass 12 입력의 같은 gap·같은 route 의미 중복 차단

pass 11 뒤의 질문 단위 dedup은 서로 다른 질문이 같이 묶여 재전송되는 문제를 막았지만, route receipt
ID 자체가 질문 hash에 남아 있었다. append-only ledger에서는 같은 KRX endpoint를 다시 시도해도
`ROUTE-P11-...`에서 `ROUTE-P12-...`처럼 ID가 달라진다. 따라서 내용·결과가 같은 경로도 ID만 보고
새 진행으로 오인할 수 있었다.

이제 재시도 권한에는 receipt ID나 Pro의 raw terminal 문구를 쓰지 않고 다음 의미만 쓴다.

```text
source role + 조사 목적 + query + opened URLs
+ 최신 provider/parser 결과
+ verifier가 실제 채택한 fact
+ accepted question lineage
+ deterministic status/closure/fixpoint
```

쉬운 예로 같은 KRX URL·같은 query가 또 `PARSER_PENDING`이면 새 receipt가 생겨도 재질문하지 않는다.
반대로 다른 공식 regulator URL을 열었거나, 같은 route의 parser가 `PARSER_PENDING -> SUCCESS`로 바뀌거나,
새 fact가 verifier를 통과하면 실제 진행으로 인정한다. Pro가 `accepted_fact_ids`에 적은 값도 deterministic
verifier의 48개 accepted roster와 교집합을 취하므로, pass 11처럼 Pro가 제안했으나 검문에서 탈락한
fact만으로 다음 pass를 열지 않는다.

이미 전송된 pass 12의 네 질문에는 이 semantic identity를 metadata-only로 결박했다. status는
`RESEARCH_RUNNING`, submit count는 1로 그대로이고 prompt·response·dossier lineage는 바꾸지 않았다.
이는 새 전송이 아니라 pass 12가 시작될 때의 의미 상태를 고정한 것이다.

```text
새 focused 회귀                              3/3 PASS
fresh orchestration module                  29/29 PASS
관련 browser/dossier/saturation/fresh      108/108 PASS
Pro-first static audit                      PASS / critical 0
Pro-first V2 static audit                   PASS / critical 0
fresh efficiency static audit               PASS / critical 0
production static audit                     PASS / critical 0
```

전체 unittest도 이 변경 기준으로 7,734개 PASS, failure/error 0/0, 기존 skip 38로 끝났다. pass 12
current-turn JSON을 회수·병합·재검문한 뒤, 현재 의미 지문과 pass 12 입력 지문을 비교해 같은 경로
반복이면 추가 submit 없이 pending/fixpoint/repair 경로로 보낸다. 실제 새 경로나 parser 정상화가 있을
때만 다음 same-conversation pass를 허용한다. score/Stage authority는 계속 false다.

#### pass 12 current-turn JSON과 검문 통과 2개

pass 12는 약 57분 뒤 완료됐다. runner 코드를 새 semantic identity 버전으로 바꾸는 동안에도 ChatGPT
연구는 중단하지 않았고, 기존 submitted pass를 `browser_submit_delta=0`, submit count 1로 복구했다.
현재 assistant turn의 다음 delta만 캡처했다.

```text
ResearchDossierV3_SKHynix_000660_PUBLIC_GAP_CLOSURE_
PROPASS-787438355e0c6f2da764cd1e_delta.json
```

```text
capture source                   DIRECT_REPORT_DOM_NORMALIZED
raw/normalized report hash       5de16341... / 216fbb8a...
effective facts                  102 -> 108
source documents                 35 -> 35
source lineages                  33 -> 33
route receipts                   266 -> 276
verification query/search        0 / 0
```

새 6개 중 deterministic source verifier를 통과한 것은 2개다.

```text
PROFACT-P12-R13-CLOSE-20260821
  2026-08-21 SK하이닉스 종가 1,730,000원
  서울신문 원문 exact normalized match

PROFACT-P12-R13-AUDIT-REPORTS-DISCLOSED-THREE-WEEKS-EARLY
  외부감사인 의견이 있는 국·영문 감사보고서를 주총 3주 전 공시
  KIND issuer-scoped 원문 punctuation/whitespace normalized match
```

나머지 revision/counter 4개는 S&P Global 원문이 verifier fetch에서 HTTP 403을 반환해
`REJECTED_SOURCE_UNAVAILABLE`로 남겼다. Pro가 fact라고 적었다는 이유로 점수 그래프에 넣지 않았다.
accepted fact는 48→50, fact snapshot과 accepted-lineage roster가 모두 바뀌었다.

pass 12 뒤에도 nonterminal 2, provider/parser core pending 2, public material gap 16, verifier repair pending
14, source-linkage incomplete 2라 saturation은 false다. 다만 pass 13은 receipt ID만 바뀌어서 열린 것이
아니다. 두 accepted fact, 새 route signature, 네 질문의 deterministic progress identity가 모두 실제로
바뀌었으므로 같은 conversation에 정확히 한 번 전송됐다.

```text
pass id             PROPASS-fad7cbf692ef68afca4ac459
pass ordinal        13
prompt chars        32,096
question count      4
submit count        1
score/Stage authority false/false
```

pass 13이 같은 KRX/SEC route와 같은 parser failure만 새 receipt ID로 반복하면 새 semantic guard가 다음
submit을 막는다. 반대로 새 accepted evidence나 provider/parser 정상화가 있으면 그 변화만 다음 단계에
쓴다.

#### 현재-turn JSON 다운로드 버튼과 follow-up pass 직접 결박

최초 전체 dossier의 expanded JSON은 이미 같은 assistant turn의 다운로드 버튼으로 회수했지만,
pass 10~12의 delta JSON은 follow-up orchestration이 과거 .md 이름을 기대해 화면 DOM 텍스트
fallback으로 캡처됐다. JSON 내용과 hash는 보존됐으나, 화면에 보이는 JSON 다운로드 버튼을 직접
누르는 경로가 follow-up까지 일반화되지 않은 상태였다.

이제 기대 이름이 .json이면 그 파일을 직접 고르고, 기존 follow-up처럼 기대 이름이 .md여도
현재 assistant turn에 새 JSON 첨부가 정확히 하나면 그 JSON을 우선 다운로드한다. 단순히 .json
문자열만 보고 받지 않고 다음 검문을 모두 통과해야 한다.

~~~text
현재 conversation 일치
+ 현재 assistant turn 일치
+ 새 JSON 첨부 정확히 1개
+ 브라우저 suggested filename 일치
+ UTF-8 JSON object
+ dossier job_id / run_id 일치
= DOWNLOAD_JSON으로 현재 pass에 연결
~~~

쉬운 예로 이전 turn의 old_result.md나 다른 job의 JSON이 화면에 남아 있어도 받지 않는다. 현재
pass의 JSON만 받고, 같은 basename의 선택 PDF가 있으면 기존처럼 PDF magic header를 확인해 함께
보존한다. JSON 다운로드는 composer나 send를 건드리지 않으므로 submit count도 증가하지 않는다.

회귀 결과는 JSON 집중 5/5 PASS, browser/expanded JSON/E2E 관련 60/60 PASS다. pass 13이 연구 중일
때 폴링 프로그램만 최신 코드로 복구했고, conversation과 pass id는 유지됐으며
browser_submit_delta=0, submit count 1, automatic resubmit false를 확인했다. 따라서 pass 13
완료 결과부터 이 직접 JSON 다운로드 경로가 적용된다.

최신 코드 전체 unittest는 7,738개 PASS, failure/error 0/0, 기존 skip 38로 끝났다. 네 static
audit도 모두 PASS/critical 0이며, 직전 pushed head 1eaa4260의 GitHub Actions 두 필수 workflow도
SUCCESS다. 새 commit의 GitHub Actions는 push 뒤 다시 별도로 확인한다.

#### pass 13·14의 현재-turn JSON 실다운로드와 문장·receipt 반복 차단

pass 13 완료 화면에는 MD가 아니라 현재 assistant turn의 JSON 파일이 있었다. 실제 ChatGPT DOM에서
먼저 잡힌 바깥 side-pane shell은 비어 있었고, 다운로드 버튼은 잠시 뒤 별도
`[data-testid=stage-thread-flyout]`에 나타났다. 따라서 첫 visible root 하나만 고르는 방식은 실제
`다운로드` 버튼을 놓쳤다. 다운로드 뒤에도 원자 저장기는 파일을 MD로 보고 sentinel을 찾으려 했다.

이제 허용된 모든 visible preview root를 최대 5초 동안 확인하고, `앱 다운로드`가 아닌 실제 다운로드
버튼을 누른다. 받은 파일이 `DOWNLOAD_JSON`이면 UTF-8 JSON object를 그대로 canonical dossier로
저장한다. 기존 MD sentinel 경로와 같은 basename의 선택 PDF 경로는 그대로 유지했다. 쉬운 예로 화면에
빈 서랍이 먼저 뜨고 1.5초 뒤 실제 파일 서랍이 생겨도, 빈 서랍에서 실패하지 않고 실제 서랍의 버튼을
기다린다.

pass 13은 이 경로로 처음 실캡처됐다.

```text
pass id / ordinal                 PROPASS-fad7cbf692ef68afca4ac459 / 13
capture source                    DOWNLOAD_JSON
submit / automatic resubmit       1 / 0
new facts / routes                0 / 10
effective facts                   108
source documents / lineages       35 / 33
route receipts                    286
next questions                    2
```

10개 receipt가 모두 새 연구를 뜻하지는 않았다. KRX·SEC의 같은 URL을 목적 문장만 바꿔 다시 적거나,
두 URL을 한 receipt에서 두 receipt로 나눈 경우도 있었다. 기존 진행 hash는 목적 문장, source-role label,
raw distinct receipt count와 최신 pass의 일부 route만 보아 이런 표현 차이를 새 진행으로 오인할 수 있었다.

진행 identity는 다음처럼 바꿨다.

```text
opened URL이 있으면 URL 하나씩 atomic route identity
opened URL이 없을 때만 normalized query가 route identity
URL도 query도 없으면 한 개의 NO_ROUTE identity
각 URL의 최신 provider/parser 결과는 이전 pass까지 포함해 유지
receipt id / 목적 문장 / source-role 재라벨 / URL 묶음 분할은 진행 아님
```

질문과 unresolved gap의 `closure_reason`/`closure_note`, append-only route receipt ID도 semantic progress
hash에서 제외했다. 대신 status, availability, verified fact 연결, source-role 충족, score/stage/hard-break
materiality처럼 구조화된 변화만 남겼다. 배열 순서도 집합 의미로 정규화했다. 쉬운 예로
`감사보고서 확인이 남음`을 `동일 감사 원문 parser가 남음`으로 바꾼 것만으로 다음 pass를 열지 않는다.
반대로 `could_change_stage=true -> false` 또는 `PARSER_PENDING -> ANSWERED`는 실제 진행이다.

이 규칙으로 pass 12와 pass 13을 다시 비교하면 prose·receipt 차이를 제거한 뒤 남는 변화는 C06 Q07과
accounting Q05의 structured materiality flag뿐이었다. 따라서 두 질문을 닫고 남은 audit 질문 두 개로
pass 14를 연 것은 정당했다.

pass 14도 현재 turn JSON을 직접 받았다.

```text
pass id / ordinal                 PROPASS-5d18230eac68945d66051427 / 14
capture source                    DOWNLOAD_JSON
submit / automatic resubmit       1 / 0
economic-id dedup 뒤 new facts     2
new routes                        4
effective facts                   110
source documents / lineages       37 / 35
route receipts                    290
```

새 fact 2개는 deterministic verifier에서 모두 `REJECTED_QUOTE_MISMATCH`였으므로 accepted fact는 50을
유지했다. accounting Q01은 기존 검증 fact만으로 terminal이 됐지만, 4B/4C hard-break Q01은 미검증
P14 fact를 참조해 nonterminal로 남았다. nonterminal mandatory는 2→1, source-linkage incomplete는
2→0이 됐다. verifier 재검문 query/search는 계속 0/0이다.

따라서 pass 15 `PROPASS-b0ed66f61e76c999cf8555f1`는 그 hard-break 질문 하나만 19,615자로 같은
conversation에 submit count 1로 전송됐다. score/Stage authority는 계속 false다. pass 15 결과가 같은
URL·같은 결과를 문장이나 receipt ID만 바꾼 것이면 새 pass를 열지 않고 pending/fixpoint로 멈춘다.

검증은 다음과 같다.

```text
completion capture module                    26/26 PASS
browser JSON/MD/PDF/E2E related              65/65 PASS
fresh orchestration/no-progress guards       31/31 PASS
full unittest                              7,742 PASS
failure/error/skip                           0 / 0 / 38
Pro-first static audit                       PASS / critical 0
Pro-first V2 static audit                    PASS / critical 0
fresh efficiency static audit                PASS / critical 0
production static audit                      PASS / critical 0
```

직전 pushed head `6eb9467c`의 필수 GitHub Actions 두 workflow도 SUCCESS이고 PR #7은 계속
Draft/open/mergeable이다. 이 시점은 전체 목표 완료가 아니라 pass 15의 정확한 current-turn JSON을
기다리는 중간 checkpoint다.

#### pass 15 실캡처와 append-only 과거 경로의 현재 상태 오염 수리

pass 15는 현재 assistant turn의 JSON을 `DOWNLOAD_JSON`으로 직접 받았다. submit은 처음 전송한
1회뿐이고 자동 재전송은 없었다.

```text
pass id / ordinal                 PROPASS-b0ed66f61e76c999cf8555f1 / 15
capture source                    DOWNLOAD_JSON
question                          R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_Q01 한 개
raw question status               EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH
current route receipts            4개 / 모두 SUCCESS
new economic-id fact              1개
accepted fact                     50 -> 51
verification query/search         0 / 0
```

새 fact `PROFACT-P15-R13-MAJOR-CLIENT-DISCUSSIONS-CONTINUE`는 2026년 2분기 issuer 원문의
“major industry clients와 추가 논의를 계속한다”는 문장에 exact match하여 deterministic verifier가
ACCEPTED했다. pass 15의 raw question은 support에 현재 검증 roster만 사용하고, 현재 4개 route도 모두
정상이었다. 즉 Pro 응답 자체는 마지막 hard-break 질문을 정상적으로 평가했다.

그런데 effective question의 `search_route_receipt_ids`는 삭제 불가능한 감사 장부라 pass 3의 과거
`PARSER_PENDING` receipt도 함께 보존한다. 기존 delta projection과 strict dossier validator가 이
누적 전체를 다시 현재 route처럼 검사하면서 정상 pass 15를 `PARSER_PENDING`으로 되돌렸다. 쉬운
예로 3회차에 문서를 못 연 사실은 장부에 남아야 하지만, 15회차에 다시 연 네 경로가 모두 성공했으면
현재 상태는 15회차 네 경로로 판단해야 한다.

이를 다음처럼 분리했다.

```text
감사 ledger              과거와 현재 route id를 append-only로 모두 보존
현재 provider/parser 판정 최신 research pass의 route cohort 전체만 사용
같은 최신 pass 안의 실패   성공 한 건으로 숨기지 않고 계속 차단
과거 rejected fact 참조    새 공개검색이 아니라 verifier repair로 이동
```

공통 `latest_question_route_cohort` 선택기를 delta projection, strict dossier validator, saturation
route adequacy가 함께 사용하도록 했다. 현재 응답이 true delta이든 누적 dossier이든 마지막 pass의
경로 묶음으로 같은 판정을 내린다. latest pass에 성공과 실패가 같이 있으면 전체가 정상일 때까지
차단하므로 fail-closed 성질도 유지한다.

실제 pass 14 effective dossier와 pass 15 incoming JSON을 수정 엔진에 그대로 재생한 결과는 다음과
같다.

```text
effective route receipt count     29 (과거 감사 기록 삭제 없음)
question status                   EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH
adequate_search_proven            true
route-truth demotion              없음
dossier research status           COMPLETE_WITH_LIKELY_NONPUBLIC_REMAINDER
strict validation                 PASS
```

회귀 테스트는 과거 parser 실패+현재 성공, 최신 parser 실패, 같은 최신 cohort의 일부 실패, adequately
searched absence의 과거 rejected fact 참조를 각각 분리해 검증한다. V3 delta merge·V2 saturation·fresh
orchestration 84/84와 V2 dossier status 19/19가 통과했다.

pass 16 `PROPASS-851f67ee70d8dd5cd0a394cf`는 수정 전에 이미 같은 conversation에 정확히 한 번
제출돼 현재 Pro 연구 중이다. 로컬 감시기만 최신 코드로 재시작했고 두 번 모두
`browser_submit_delta=0`, `submit_count=1`, `automatic_resubmit_allowed=false`를 확인했다. 서버의
연구 생성은 중단하거나 다시 제출하지 않았다. 완료 뒤 최신 cohort 판정과 verifier repair routing을
실제 결과로 다시 확인한다.

직전 pushed head `dd36c073`의 GitHub Actions는 E2R Pro-first verification 두 run과 E2R v6
operational cutover verification이 모두 SUCCESS다. 이 섹션의 cohort 수정은 아직 로컬 검증 중이며,
pass 16 회수와 receipt 작성 뒤 별도 한글 commit으로 push한다.

#### pass 16 terminal closure와 48-candidate compact verifier repair

pass 16도 현재 turn JSON을 직접 다운로드했고, 새 fact 없이 현재 route 5개를 모두 SUCCESS로
정리했다. latest cohort 규칙을 적용한 실제 saturation 결과는 다음과 같다.

```text
mandatory question                 28
nonterminal mandatory               0
provider/parser core pending         0
source-linkage incomplete            0
lifecycle hard-break pending         0
accepted fact                       51
deterministic research status        NEEDS_VERIFIER_REPAIR
```

따라서 공개조사를 계속하는 pass 17은 만들지 않았다. 다만 counter router가 question의 현재 상태가
아니라 `materiality=HARD_BREAK`만 보고 terminal hard-break 22개까지 counter 검색 대상으로 다시
모으는 별도 결함이 있었다. hard-break는 중요도이지 미종료 상태가 아니다. 이제 실제
`CONTRADICTED_UNRESOLVED && terminal=false` 또는 lifecycle pending인 질문만 counter follow-up에
들어간다.

verifier에는 question 기준 18개 수리가 남지만, rejected candidate 기준으로는 48개다. 기존 compact
compiler는 후보마다 긴 atomic fact 필드명과 preflight object를 반복하고 source group마다 최대
12,000자를 고정해 100,000자 상한을 넘었다. 상한을 올리지 않고 다음처럼 무손실 compact했다.

```text
atomic fact field name       context에 field_order 한 번만 기록
candidate fact semantics     같은 순서의 values 배열로 보존
고정 verifier_preflight      prompt 계약에 한 번만 기록
source text                  candidate와 literal overlap이 큰 원문 window
출력 schema/context          공백 indent 없는 canonical compact JSON
크기 조절                    60,000 target을 향해 source window를 반감,
                             단 100,000 hard limit 안에서 1회 pass는 유지
```

실제 48개 candidate와 17개 source group을 재컴파일한 결과는 88,559자였고, 실제 pass id를 넣어
ledger에 기록된 전송 prompt는 88,571자다. full dossier 재출력, local-normalizable 전송,
source-representation 전송은 모두 0이다. literal candidate excerpt는 28개가 보존됐다. 나머지는
verifier가 원문을 확보하지 못한 후보이므로 Pro가 quote를 만들지 않고 WITHDRAW할 수 있게 빈 값으로
남는다.

```text
repair pass id          PROPASS-e28bda224af4e7ceb393f04a
pass ordinal/name       17 / VERIFIER_REPAIR
candidate/group         48 / 17
prompt chars            88,571 (< 100,000)
submit count            1
score/Stage authority   false / false
current browser state   RESEARCH_RUNNING
```

관련 V3 repair·fresh orchestration·dossier·saturation 모듈은 119/119 PASS다. Pro-first, Pro-first V2,
fresh efficiency, production static audit도 모두 PASS/critical 0이다. checkpoint receipt는
`p11_pass15_pass16_route_cohort_and_compact_repair_receipt.json`이며 payload hash는
`0e79d1ed8fc85995373df2c1e544d982c78ff3f210c7a47d741b0f781e9f2fdd`다. 전체 목표 완료가 아니라
pass 17 결과의 deterministic 재검문을 기다리는 중간 checkpoint다.

#### compact repair의 현재-turn JSON 실다운로드 연결

ChatGPT Pro가 긴 repair 결과를 Markdown 첨부 대신 JSON 첨부로 반환할 수 있다. 브라우저 adapter는
현재 assistant turn에 새로 생긴 JSON 하나만 선택해 `DOWNLOAD_JSON`으로 캡처하도록 이미 수리돼
있었지만, fresh full-thesis 실행기는 캡처 뒤에도 Markdown marker를 먼저 요구했다. 이 상태에서는
정상 JSON을 다운로드하고도 `TRANSPORT_PENDING`으로 되돌릴 수 있었다.

repair transport 검증을 다음 두 경로로 분리했다.

```text
현재-turn JSON 다운로드  payload의 job/run/research_pass/parent_pass를 exact match
Markdown/direct capture  본문의 job/run/pass/parent marker를 각각 정확히 1개 요구
```

쉬운 예로 pass 16 JSON이 파일 목록에 남아 있더라도 pass 17 결과로 재사용할 수 없다. JSON 안의
`research_pass_id`와 `parent_pass_id`가 현재 repair plan과 다르면 즉시 차단한다. 반대로 현재 pass 17의
네 identity가 모두 맞는 raw JSON은 Markdown marker가 없어도 `RepairDeltaV3Parser`와 전체 repair
schema/verifier 검문으로 넘긴다.

관련 raw JSON identity 회귀, 실제 browser E2E, compact repair V3 테스트는 18/18 PASS다. 실행 중인
pass 17은 서버 연구를 중단하거나 재제출하지 않고 로컬 감시기만 새 코드로 재접속했다.
재접속 직후 `browser_submit_delta=0`, 기존 `submit_count=1`, 같은 conversation/pass를 확인했다.
화면에 열려 있던 `ResearchDossierV3_SKHynix_000660_asof_2026-08-23.json`은 최초 dossier이므로
현재 repair 결과로 연결하지 않았다. 현재 pass 17 전용 첨부가 생성될 때만 자동 캡처한다.

## P15 — 폐기한 C06 대화 대신 새 Pro 채팅에서 Initial Gate 통과

### 새 채팅 전환 판정

기존 conversation `6a8db0ad-8ed0-83e8-888e-dce26c950343`은 pass 24·25가 화면에는
보였지만 새로 연 공개 conversation에는 서버 user turn으로 존재하지 않았다. 그러므로 계속 사용하지
않고 diagnostic-only로 봉인했다. 기존 accepted fact 66은 감사 자료로만 보존하고, 새 prompt에 주입한
개수는 0이다.

쉽게 말하면 기존 채팅은 “임시 저장된 화면”만 보이고 서버 편지함에는 없던 상태였다. 그 화면에서
계속 보내지 않고, 아예 새 편지함을 만들어 처음부터 서버 저장을 다시 확인한 것이다.

```text
fresh runtime       20260827T174738Z
fresh session       FRESH-V2-1-C06-SUCCESSOR-20260827T174738Z
job / run           PROJOB-821fd91d8204a7c366ec86f0 / PRORUN-f34eb764254e9fd6c7e21cb4
initial pass        PROPASS-05c3820ffb6f29285d34d702
new conversation    6a90786a-8234-83e8-b7b4-c03f18b4e725
durable user turn   58089b79-d992-487c-920e-4089ae859769
submit / capture    1 / 1
old-chat submit     0
```

### 큰 user turn의 느린 서버 hydration과 무전송 복구

61,286자 initial prompt는 새 공개 페이지에 30초 안에 모두 펼쳐지지 않아 최초 서버 저장 검사가
실패했다. 하지만 같은 pass를 다시 send하지 않고, exact conversation의 새 읽기 전용 화면에서
job/run marker가 한 user turn에 모두 있는지 다시 검사했다. 실제 durable user turn을 확인한 후에만
약 5,442초의 Pro 조사를 읽기 전용으로 감시했다.

이 경로는 `USER_ATTENTION_REQUIRED + submit_count=1 + capture_count=0`에서만 열리고 추가 DOM click은
0이다. 초기 결과 다운로드가 0 byte로 끝났을 때도 prompt를 다시 보내지 않고 같은 완료 turn의 JSON만
재다운로드했다. 결과적으로 `DOWNLOAD_JSON`이 성공했고 assistant turn·conversation·job·run이 모두
일치했다.

### 새 C06 initial 결과

```text
Pro 출력 전체 fact             45
source document                  16
mandatory question              28/28
material current candidate       27
post-preflight accepted          23
acceptance ratio                 85.1852%
genuine semantic repair           4 (상한 5)
initial output defect             0
unclassified rejection            0
source verification query/search  0/0
Initial Efficiency Gate          PASS
```

45개 전체 fact에는 current support뿐 아니라 counter·historical·rejected도 들어 있다. 그래서 Gate는
전체 45개를 임의로 나눈 값이 아니라, 현재 핵심 후보 27개 중 23개가 통과한
`23 / 27 = 85.1852%`로 계산했다. deterministic source verifier의 전체 분류는 accepted current 25,
accepted counter 5, historical 2, rejected 13이다.

최초 import는 같은 source·subject·excerpt·coarse predicate를 쓴 두 fact를 중복으로 보았다. 하지만
하나는 M15X 양산 일정 단축이고 다른 하나는 용인 CAPA 투자로, 실제 statement가 달랐다. 종목명이나
C06을 조건으로 하드코딩하지 않고, “동일한 충돌 그룹에서 정규화 statement가 서로 다를 때”에만
statement hash로 predicate를 분리했다. 증거 문장, fact ID, source 결박, question 결박은 바꾸지 않았고
정말 같은 statement 중복은 여전히 검증기가 차단한다.

### 현재 경계와 검증

```text
focused regression               111/111 PASS
Pro-first core                   238/238 PASS
failure / error                    0 / 0
production static audit critical   0
guarded DOM submit path             1
score / Stage authority          false / false
publication                      withheld
```

기계 판독 영수증은 `p15_c06_new_chat_initial_success_receipt.json`이다. 이 시점은 C06 Initial Gate를
통과한 것이지 전체 목표 완료가 아니다. 다음은 같은 새 C06 conversation에서 bounded full-thesis tail을
실행하고, 이후 C17·C28 tail과 전체 suite·GitHub Actions를 닫는 것이다.

## P16 — C06 full-thesis tail 100,000자 사전 차단과 무손실 compact

새 C06 job을 읽기 전용 점검한 결과는 `GAP_ADJUDICATION`, accepted fact 30, 공개 gap 23,
비종료 mandatory 4, provider/parser core pending 2, source-linkage incomplete 9였다. 같은 conversation의
bounded tail을 시작했지만 실제 send 전에 follow-up prompt 100,000자 상한이 작동했다.

```text
initial resubmit                 0
follow-up submit                 0
browser submit delta             0
failure                          FreshSessionBoundaryError
publication / score / Stage      withheld / false / false
```

원인은 25개 질문 context의 내용 자체가 아니라 JSON 들여쓰기였다. context를 보기 좋게 출력하면
96,167자였고, 동일 객체를 canonical JSON으로 직렬화하면 73,242자였다. 질문, fact ID, route outcome을
삭제하거나 batch 상한을 올리지 않고 공백만 제거했다.

쉬운 예로 보고서 25장을 버린 것이 아니라 각 줄 앞의 스페이스만 없앤 것이다. 회귀 테스트는 100,000자를
넘는 pretty context를 새 compiler에 넣고, prompt 안의 compact JSON을 다시 파싱해 원래 객체와 완전히
같은지 비교한다.

```text
lossless JSON roundtrip regression     PASS
focused fresh/preflight/submit tests   112/112 PASS
failure / error                        0 / 0
```

기계 판독 영수증은 `p16_c06_full_tail_prompt_compaction_receipt.json`이다. 이 checkpoint도 전체 완료가
아니며, 같은 C06 conversation에 compact된 bounded tail을 아직 전송하지 않은 상태다.

## P17 — C06 새 채팅 full-tail pass 11 수리와 실제 응답 무전송 복구

### 새 채팅 상태와 실제 병목

기존 conversation은 서버 저장 부재로 이미 봉인했고, C06은 새 conversation
`6a90786a-8234-83e8-b7b4-c03f18b4e725`에서 계속 실행한다. 새 채팅의 Initial Gate는 앞서
`23/27`, mandatory `28/28`로 통과했다. 이번 병목은 새 채팅 세션 고장이 아니라 pass 11 Pro
repair JSON의 전송 표현이었다.

쉬운 예로 아래 두 URL은 같은 query 값을 뜻한다.

```text
contentType=application%2Fpdf&fileName=4010%2Freport.pdf
contentType=application/pdf&fileName=4010/report.pdf
```

`CanonicalURLResolver`로 두 URL을 풀었다가 다시 canonicalize하면 같은 URL이 된다. 기존 repair
normalizer는 이 표현 차이를 immutable URL 변경으로 오인했다. 또한 Pro는 replacement fact 28개에
원래 rejected `candidate_id`를 그대로 재사용했다. statement·excerpt·source는 유효할 수 있지만,
append-only dossier에는 기존 fact와 같은 ID를 다시 넣을 수 없다.

### generic 수리

종목명, C06, source host를 조건으로 쓰지 않고 다음 두 transport envelope만 결정적으로 정규화했다.

```text
동일 canonical URL의 % encoding 차이
→ prompt의 exact canonical URL로 복원

replacement_fact.dossier_fact_id == rejected candidate_id
→ repair pass + candidate + replacement semantic payload로 새 PROFACT ID 생성
→ 현재 repair route accepted_fact_ids도 같은 새 ID로 교체

실제로 다른 canonical URL
→ 계속 hard fail
```

새 source document도 resolved canonical URL이 기존 source와 같을 때만 기존 source ID로 결박한다.
원문 statement, excerpt, value, question scope, target, score/Stage authority는 바꾸지 않는다. 앞으로의
repair prompt에는 replacement fact가 원래 candidate 및 기존 fact와 다른 새 ID를 사용하라고 명시했다.

별도로 terminal question에 repair 가능한 rejected fact가 결박돼 있으면 public search보다 compact
repair를 먼저 실행하도록 router를 고쳤다. 하나의 repair candidate가 있는 질문만 보류하며, 관계없는
진짜 public gap은 계속 조사할 수 있다. 예를 들어 Q-A의 인용 오류를 고치는 동안 Q-B의 미확인 공시까지
숨기지 않는다.

### pass 11 무전송 복구 결과

완료된 browser capture와 raw Pro JSON은 수정하지 않았다. 기존 prompt hash가 달라지지 않도록 당시
prompt를 그대로 사용해 `REUSE_CAPTURE`했고, browser submit delta는 0이었다.

```text
pass id / ordinal               PROPASS-bc8734afba8b99d9a7d37be1 / 11
status / submit                 COMPLETE / 1
recovery browser submit delta   0
repair actions                  31
Pro replacement / withdraw      28 / 3
URL encoding normalization       3
replacement ID reassignment     28
existing source remap             2
replacement local reverify       28
accepted / failed-withdrawn      16 / 12
unresolved replacement            0
query / search                    0 / 0
prior accepted preserved        54 / 54
effective facts/routes          74 / 138
effective dossier hash          d096a27de31d0e1ecb11c92b942c0125eca81a501e9a876167f0053e07c30547
repair receipt hash             4358d29381e55f48a5aa5ccae4dc35ebab9090d57997afaa1508e8ba923e2c83
```

deterministic source verifier 기준 accepted fact는 `54 → 70`으로 늘었다. 검문에 실패한 replacement
12개는 두 번째 repair로 보내지 않고 fail-closed 철회했다. 따라서 Pro가 고쳤다는 이유만으로 전부
사실로 승격하지 않았다.

```text
nonterminal mandatory            2
provider/parser core pending      0
source-linkage incomplete         4
public material gap              11
verifier repair pending           1
research saturation              PENDING
score / Stage / publication      false / false / withheld
```

focused compact repair `22/22`, fresh orchestration `44/44`가 통과했다. 새 회귀는 URL의 `%2F`와 `/`가
같은 주소일 때만 복원되는지, 다른 host/path는 거절되는지, candidate ID 재사용 시 새 ID와 route가 함께
바뀌는지, repair 가능한 fact가 있는 질문만 public router에서 보류되는지를 검증한다.

### pass 12 현재 상태

pass 11 직후 상태기계는 남은 실제 source gap 7개를 25,658자 context로 묶어 같은 새 conversation에
pass 12를 정확히 한 번 제출했다.

```text
pass id / ordinal               PROPASS-b38c8ccfb3aca623f77e9538 / 12
pass name                       PUBLIC_GAP_CLOSURE
parent                          PROPASS-bc8734afba8b99d9a7d37be1
question count                  7
prompt chars                    25,658
submit count                    1
status                          TRANSPORT_PENDING
automatic resubmit             false
```

최초 별도 공개 화면 관측은 job/run marker만 보고 pass/parent marker를 아직 보지 못했다. 이 시점에
runner는 `TRANSPORT_PENDING`으로 안전 중단했고 자동 재전송은 0이다. 앞선 pass 7·9·10도 서버 화면
hydration이 수분 늦은 뒤 exact turn이 나타났으므로, 같은 pass를 보내지 않고 읽기 전용 late audit만
수행한다. 결과가 capture·검증되기 전에는 C06 saturation, component/Judge, score 또는 Stage를 선언하지
않는다. PR #7은 계속 Draft/open이며 병합하지 않는다.

## P18 — C06 pass 12 의미 진전과 saturation replacement 1회 경계

### pass 12 완료

pass 12의 첫 공개 화면 관측은 marker가 일부만 보여 `TRANSPORT_PENDING`이었지만, 약 2분 뒤 같은
conversation을 읽기 전용으로 재관측했을 때 exact pass/parent marker와 durable user turn이 나타났다.
추가 submit 없이 기존 assistant turn을 감시했고 42분 뒤 현재-turn JSON을 직접 다운로드했다.

```text
pass id / ordinal               PROPASS-b38c8ccfb3aca623f77e9538 / 12
status / submit                 COMPLETE / 1
server observations             2
absence / confirmed             1 / true
recovery browser submit delta   0
capture source                  DOWNLOAD_JSON
new fact / route                3 / 16
accepted fact                   70 -> 73
effective facts/routes          77 / 154
effective dossier hash          9742c07af6e51d9d0b2e5927699be6c9b2da0c2b9fce02f9ef15023cc403a87b
response hash                   b3e56d432e0f90951f0cb05503522e6f5dc7c9faa90930c1f926f13d24d1c731
query / search                  0 / 0
```

세 fact는 모두 deterministic verifier를 통과했다. Pro 출력이라는 이유로 채택한 것이 아니라 현재
source 원문과 excerpt·target·date를 다시 대조한 결과다. saturation은 다음처럼 줄었다.

```text
nonterminal mandatory            2 -> 1
provider/parser core pending      0 -> 0
source-linkage incomplete         4 -> 3
public material gap              11 -> 4
verifier repair pending           1 -> 1
```

남은 nonterminal은 `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_Q04` 한 개다. 나머지 public gap 4개와 linkage
3개가 공개자료로 더 닫히는지, 이미 조사한 공개 경로 밖인지 최종 판정하기 위해 새 search pass가 아닌
28-question `SATURATION_AUDIT`을 만들었다.

### pass 13 미저장 봉인과 pass 14 replacement

pass 13은 68,037자였고 DOM send click은 한 번 발생했지만, 두 개의 독립 fresh public view 모두에서
exact pass/parent marker가 없었다. 화면상 전송을 서버 저장으로 간주하지 않고 `FAILED_HARD`로 봉인했다.

```text
pass 13                         PROPASS-b1184fe6bd83e5f7de8ca23c
input root hash                 1f01a43575204b42e80390c296e60df038fd7b3ada458dea7bebe1be785bcb49
submit / absence                1 / 2
server persistence              false
status                          FAILED_HARD
automatic resubmit              false
```

같은 pass를 다시 보내지 않고, 정책상 허용된 서로 다른 replacement pass를 정확히 한 번 만들었다.
pass 14는 `supersedes_unpersisted_pass_id=pass 13`과 동일 root input hash를 장부에 남긴다. 첫 관측은
늦었지만 두 번째 읽기 전용 관측에서 durable user turn을 확인했다.

```text
pass 14                         PROPASS-739ea5decbf04f0a0298e25f
pass name                       SATURATION_AUDIT
prompt chars                    68,512
submit count                    1
server observations             2
absence / confirmed             1 / true
browser submit delta on recovery 0
status                          RESEARCH_RUNNING
```

pass 14도 저장되지 않았다면 동일 saturation 입력의 세 번째 전송은 차단됐을 것이다. 현재는 서버 저장이
확인돼 같은 assistant turn의 완료만 감시한다. score/Stage/publication authority는 계속
`false/false/withheld`다.

커밋 `88ec6111`의 GitHub 독립 검증은 다음과 같다.

```text
E2R Pro-first push run          SUCCESS / 33135805748
E2R Pro-first PR run            SUCCESS / 33135803705
E2R v6 operational cutover      SUCCESS / 33135805745
full regression                 7,779 tests / failure·error 0
fresh efficiency static audit  PASS / critical 0
Pro-first V2 static audit       PASS / critical 0
```

## P19 — 봉인된 saturation pass 계보 수리와 새 4-question gap

pass 14 응답은 8분 만에 완료돼 `DIRECT_REPORT_DOM`으로 캡처됐다. 첫 적용은 SQL ledger의 pass 13을
`research_passes`에 넣으려다 중단됐다. pass 13은 두 공개 화면에서 서버 미저장이 증명돼 response
hash가 없는 것이 정상인데, 기존 함수는 submit count 1인 모든 과거 pass에 response hash를 요구했다.

이를 “실패 pass를 전부 무시”하는 방식으로 풀지 않았다. 다음 조건을 모두 만족하는 정확한 pass 하나만
실행 dossier 계보에서 제외한다.

```text
current pass가 supersedes_unpersisted_pass_id로 exact pass를 지목
failed pass status / submit             FAILED_HARD / 1
failed response hash                    null
failed server persistence               false
replacement root hash                   failed pass_input_hash와 exact match
pass name / parent                      replacement와 exact match
```

조건 하나라도 다르면 기존처럼 hard fail한다. SQL pass ledger에서는 pass 13 실패 이력을 삭제하지 않고,
ResearchDossier의 “실제로 응답을 받은 pass” roster에서만 제외한다. 쉬운 예로 반송된 택배 송장은 감사
장부에 남기되, 내용물을 받은 목록에는 넣지 않는 것이다.

수리 뒤 pass 14 READY 캡처를 추가 전송 0으로 재사용했다.

```text
pass id / response hash          PROPASS-739ea5decbf04f0a0298e25f
                                b086e703ff955b88268be5a693fe48f7f8660e8d6db0802e7100edc309b50946
capture / recovery submit        DIRECT_REPORT_DOM / 0
new fact / route                 0 / 0
question semantic progress       true
effective facts/routes           77 / 154
effective dossier hash           901243418201805ebc9e7cba7ff35882abb545cb17563b7d7a2a94620148114b
accepted fact                    73
```

audit 응답의 phantom route ID 5개는 실제 route receipt가 없어 local preflight가 question 참조에서
제거했다. 그래서 숨겨져 있던 비종료 질문이 1개에서 5개로 드러났다. 이 결과를 낮은 점수로 덮지 않고
saturation pending을 유지한다.

```text
nonterminal mandatory            5
provider/parser core pending      0
source-linkage incomplete         5
public material gap               4
verifier repair pending           1
```

public gap 4개는 pass 12가 조사한 질문과 다르다. phantom route 때문에 조사된 것처럼 보였던
Stage2 false-positive Q04/Q05와 High-MAE Q03/Q04다. 상태기계는 이 exact 4개만 22,533자 pass 15로
한 번 제출했다. 첫 공개 화면은 늦었지만 두 번째 읽기 전용 관측에서 durable turn을 확인했고 추가
submit은 0이다. 현재 pass 15는 `RESEARCH_RUNNING`이다.

live-runtime와 fresh orchestration 회귀는 `74/74 PASS`다.

### 대체 계보의 후손 유지

pass 15 current-turn 응답은 새 fact 1개와 route 9개를 정상 캡처했지만, 첫 적용에서 pass 13 response
hash 오류가 다시 나타났다. pass 14 적용 때는 pass 14가 current라 exact supersession을 찾았지만,
pass 15에서는 그 edge가 과거 row가 됐기 때문이다.

따라서 current row 하나가 아니라 현재 ordinal까지의 durable pass 전체에서 explicit
`supersedes_unpersisted_pass_id` edge를 수집한다. 각 edge는 앞 절의 status·submit·persistence·root
hash·pass name·parent 검문을 똑같이 통과해야 한다. 여러 replacement claim, 미래 ordinal, unknown
failed pass는 거절한다. 검증된 edge는 후손 dossier에서도 유지돼 봉인 pass가 부활하지 않는다.

pass 15 READY 캡처를 추가 submit 0으로 재사용했고 accepted fact는 `73 → 74`, nonterminal은
`5 → 3`, public material gap은 `4 → 2`, source-linkage incomplete는 `5 → 1`로 줄었다. 남은 exact
Stage2 Q04/Q05 두 질문만 pass 16으로 한 번 제출됐고 서버 저장도 확인됐다. descendant 회귀를 포함한
live-runtime·fresh orchestration은 `75/75 PASS`다.

## P20 — C06 공개 조사 포화와 검문 수리 1건 fail-closed

pass 16은 남아 있던 Stage2 false-positive Q04/Q05 두 질문만 조사했다. 최초 공개 화면 관측은 marker가
늦게 보였지만 두 번째 읽기 전용 관측에서 exact user turn을 확인했고 재전송하지 않았다. 응답은
`DIRECT_REPORT_DOM_NORMALIZED`로 캡처됐으며 새 fact는 없고 새 route 5개가 추가됐다.

```text
pass 16                         PROPASS-82648e2e8bc7485d5678edbb
status / submit                 COMPLETE / 1
server observations             2
absence / confirmed             1 / true
recovery browser submit delta   0
new fact / route                0 / 5
accepted fact                   74
effective facts / routes        78 / 168
public material gap             2 -> 0
response hash                   a75ca0fdace81a6598903ce25159d8f8d4fe93ac351dd3c9f63471a3c8789fac
```

마지막 pass 17은 28개 mandatory question 전체를 다시 묶은 `SATURATION_AUDIT`이다. 이 pass도 최초
관측 1회만으로 다시 보내지 않았고, 두 번째 읽기 전용 관측에서 서버 저장을 확인했다. 신규 fact/route는
`0/0`이며 동일한 마지막 검문 공백을 다시 확인했다.

```text
pass 17                         PROPASS-feba50bd0347872546862752
status / submit                 COMPLETE / 1
recovery browser submit delta   0
capture source                  DIRECT_REPORT_DOM
new fact / route                0 / 0
accepted fact                   74
effective facts / routes        78 / 168
public material gap             0
provider/parser core pending    0
nonterminal mandatory           1
verifier repair pending         1
saturation receipt hash         7a5df230711f416248c82d819f312fc0fd396164000eeb6c2f56f75daec5dec9
```

남은 exact 질문은 `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_Q04`다. 공식 filing fact 한 개는 verifier를
통과했지만, contract가 요구하는 issuer official과 서로 다른 route quorum을 모두 채우지 못했다.
compact V3 repair는 이미 pass 11에서 정책상 허용된 1회를 사용했으므로 두 번째 repair를 보내지 않는다.
쉬운 예로 원문 영수증 한 장은 유효하지만 계약이 서로 다른 영수증 두 장을 요구하는 상황이다. 한 장을
두 장으로 세지 않고 해당 canary만 보류한다.

> **P24 현재 판정으로 대체:** 위의 “정책상 1회” 설명은 P20 당시 구현의 기록이며 현재 운영 규칙이
> 아니다. generic multi-repair 수리 뒤 C06을 읽기 전용으로 다시 검문한 결과
> `verifier_repair_pending=1`이지만 `repairable_candidate_count=0`이었다. 따라서 현재 C06이 멈춘 이유는
> 횟수 cap이 아니라 서로 다른 source-route quorum을 채울 수 있는 유효 repair 후보가 없기 때문이다.
> 질문/종목별 우회나 두 번째 repair 금지 규칙으로 막은 것이 아니다.

따라서 C06은 공개 검색을 반복하지 않고 다음 truth로 봉인한다.

```text
status                          NEEDS_VERIFIER_REPAIR
research saturation valid       false
component entry allowed          false
score / Stage                    null / null
score / Stage authority          false / false
publication                      withheld
additional query / search        0 / 0
```

이는 세션 실패가 아니다. 이전 채팅은 재사용하지 않았고, 새 C06 채팅에서 Initial Gate와 pass 11~17의
exact lineage를 유지했다. 공개적으로 더 조사 가능한 material gap은 0이며, 남은 verifier blocker를 낮은
점수나 임의 Stage로 덮지 않은 정상 fail-closed 결과다. 다음 실행은 별도 dossier와 conversation을 가진
C17의 기존 fresh initial 결과에서 full tail을 이어간다.

## P21 — C17 pass 2 진전과 pass 3 무전송 JSON 인코딩 복구

C17은 기존 fresh conversation `6a8e5f55-a7f8-83e8-bd89-82c1e4529916`을 정확히 복구했다. initial
보고서를 다시 보내거나 새 job을 만들지 않았다. 첫 full-tail 상태는 accepted fact 18개, mandatory
question 26개 중 nonterminal 7개였다.

pass 2는 41,402자 public-gap prompt를 한 번 제출했고 85분 뒤 현재 turn을
`DIRECT_REPORT_DOM_NORMALIZED`로 캡처했다. Pro가 제안한 phantom route 참조 17개는 실제 receipt가
없어 preflight에서 제거했다.

```text
pass 2                          PROPASS-7aa73ba6775dbd43a441ce57
status / submit                 COMPLETE / 1
new fact / route                13 / 33
accepted fact                   18 -> 27
effective facts/routes/sources  39 / 67 / 11
public material gap             15 -> 10
provider/parser pending          6 -> 4
source-linkage incomplete        9 -> 5
nonterminal mandatory            7 -> 6
verifier repair pending          1 -> 3
```

pass 3은 남은 공개 공백을 23,090자로 묶어 한 번 제출했다. 69분 뒤 assistant turn이 완료됐고, raw와
normalized report, extracted dossier, READY, capture receipt까지 모두 저장됐다. 하지만
`supporting_excerpt`의 `(이하 "당사")` 두 따옴표가 JSON용 escape 없이 출력돼 parser가 적용 전에
fail-closed 중단했다. 브라우저 재전송은 0이다.

기존 parser는 raw key control 6개와 value control 11개를 이미 내용 보존 방식으로 처리했다. 여기에
표준 JSON decoder가 `Expecting ',' delimiter`로 조기 문자열 종료를 정확히 증명하고, 실패 문자가 바로
앞의 unescaped quote에 붙어 있으며 구조 문자가 아닌 경우만 `"` JSON encoding을 삽입한다. 누락 쉼표,
잘못된 key, 임의 구조 오류는 고치지 않는다.

쉬운 예로 `그는 "당사"라고 말했다`라는 원문은 그대로 두고, JSON 봉투 안에서만 내부 따옴표를
`\"당사\"`로 인코딩한다. 디코딩된 evidence 값은 원문과 같다.

실제 pass 3 캡처를 대상으로 확인한 결과는 다음과 같다.

```text
raw key control 삭제             6
raw value control JSON escape    11
decoder-proven quote escape       2
captured fact / route            13 / 16
protected value before==after    true
browser submit delta              0
actual capture parse             PASS
```

dossier import `20/20`, fresh orchestration·live runtime `75/75`, 합계 `95/95`가 통과했다. 다음 실행은
pass 3의 hash-bound READY capture를 재사용하며 브라우저 submit 없이 merge·source verifier·saturation을
재개한다.

## P22 — C17 세션 정상 확인, blocker fixpoint 봉인, 무한 반복 방지

pass 3 캡처를 무전송으로 적용한 뒤 pass 4~6은 같은 fresh conversation에서 각각 한 번만 제출됐다.
pass 5가 끝난 직후 fact는 1개 늘었지만 deterministic blocker 수가 pass 4와 같았다. 기존 라우터는
`verified_fact_id`가 달라졌다는 이유로 이 상태를 새 context로 보아 pass 6을 이미 제출했다.

pass 6은 중단하거나 새 채팅에 중복 전송하지 않았다. 별도 fresh public view에서 exact pass marker와
durable user turn을 확인했고, `server_persistence_confirmed=true`인 같은 assistant turn만 회수했다.
따라서 이 대화는 맛간 세션이 아니었다.

```text
pass 6                         PROPASS-e048e03952a3c592799113fe
submit / recovery submit       1 / 0
server persistence             true
capture                         DIRECT_REPORT_DOM_NORMALIZED
new fact / route               1 / 12
accepted fact                  41 -> 42
effective facts/routes/sources 61 / 124 / 14
response hash                  d3e3eddf118cb894e1c684fcfc1c1f439c68656e46237c6a89fbbbd324bd4352
next pass submit               0
```

Pass 6 회수 뒤 브라우저를 열지 않는 `VERIFY_CURRENT_DOSSIER_NO_BROWSER`로 61개 candidate를 다시
검문했다. 42개가 채택됐고 query/search는 `0/0`이다. 이어서 완전 read-only inspection도 같은
saturation receipt를 재현했다.

```text
verification hash              40b2f56c03d353fdbf6fa8b63455fc9dd82ffa0970e21f7587b4432b1626723c
saturation receipt hash        aa766263865d7113c168e72d33f7beba203d45d54cd2c7f1d51b113ebfe25a1e
mandatory / nonterminal        26 / 7
provider/parser core pending   5
public material gap            9
source-linkage incomplete      6
verifier repair pending        3
component entry                false
score / Stage                  null / null
publication                    withheld
```

pass 4~6의 fact·route는 `59/98 -> 60/112 -> 61/124`, accepted fact는 `40 -> 41 -> 42`로 늘었지만
위 blocker는 세 번 연속 같았다. 쉬운 예로 서류철은 두꺼워졌지만 미해결 체크박스 7개가 하나도
줄지 않은 상태다. 여기서 같은 공개 조사를 더 보내지 않고 C17을
`RESEARCH_BLOCKER_FIXPOINT_PENDING`으로 fail-closed 봉인했다.

재발 방지는 종목이나 C17 조건문이 아닌 세 가지 generic 경계로 구현했다.

```text
--recover-submitted-only
  이미 제출된 unsnapshotted turn 하나만 회수하고 새 pass 계획 없이 종료

--verify-and-inspect-only
  브라우저를 열지 않고 현재 dossier만 source 재검문·saturation 계산

saturation_blocker_identity_hash
  fact ID와 설명 문구는 제외하고 질문 상태, 누락 source role, linkage,
  provider/parser 및 route adequacy가 실제로 바뀌었는지만 비교
```

따라서 fact ID만 바뀌고 blocker identity가 같으면 `RESEARCH_BLOCKER_FIXPOINT_PENDING`에서 멈춘다.
반대로 누락 source role이 줄거나 provider/parser 상태, route adequacy가 바뀌면 후속 pass를 허용한다.
fresh orchestration `46/46`, live runtime `31/31`, dossier import `20/20`, Windows browser E2E `2/2`,
합계 `99/99 PASS`다. 다음 실행은 별도 dossier/job/conversation을 가진 C28 기존 fresh initial에서
이어간다.

## P23 — C28 full tail 종료, 다중 repair와 질문별 재개 한도 검증

C28은 기존 fresh conversation `6a8eaee3-d670-83ee-9c01-6f7d438db2f0`에서 pass 16까지 이어갔다.
새 채팅이나 initial 재전송은 사용하지 않았다. pass 12는 fact 2개와 route 8개를 추가했고, pass 13과
14는 같은 Q04 공개 공백을 각각 한 번씩 재확인했다. 두 응답은 fact를 늘리지 못했으며 route만
`2`, `3`개 추가했다.

```text
pass 12  PUBLIC_GAP_CLOSURE  PROPASS-6356b4f1d941c920205fe57a  fact/route +2/+8
pass 13  PUBLIC_GAP_CLOSURE  PROPASS-a452995d67d0f319b0ae4500  fact/route +0/+2
pass 14  PUBLIC_GAP_CLOSURE  PROPASS-21913aaccf85396ea4d2bcde  fact/route +0/+3
pass 15  VERIFIER_REPAIR     PROPASS-3130cedeb6aee4c22b3c8fc7  candidate/action 2/2
pass 16  SATURATION_AUDIT    PROPASS-b88c55a3bd13ed600d251c40  fact/route +0/+0
```

pass 13과 14처럼 응답 batch가 바뀌어도 같은 질문의 안정 공백은 같은 재개 예산을 써야 한다. 이를
위해 pass detail에 질문별 `question_stable_gap_hashes`를 저장하고, 새 context hash가 생겼다는 이유만으로
같은 공백을 세 번째 다시 열지 못하게 했다. 반대로 공개 공백이 재개 한도에 도달했더라도 별도의
verifier repair 후보는 굶기지 않는다. 그래서 pass 15의 compact repair가 실제로 실행됐고, pass 16
감사까지 완료됐다.

최종 C28 read-only 재현은 다음과 같다.

```text
accepted fact                    41
mandatory / nonterminal          27 / 4
provider/parser core pending     1
public material gap              4
source-linkage incomplete        4
verifier repair pending          1
repairable candidate             0
effective dossier hash           d1c163fedcf93a107aae76c5befe785ef3048a48c23f92e23574da89bc92b654
saturation receipt hash          2199565bb208b4785c14badbc82629a3f8ff41b706d8102d27adee7cc93bbd4b
normal terminal status           RESEARCH_GAP_REOPEN_LIMIT_PENDING
normal terminal new pass/submit  0 / 0
score / Stage                    null / null
publication                      withheld
```

쉬운 예로 공개적으로 확인할 수 없는 계약 세부를 세 번째 묻지 않았지만, 그 때문에 별도의 영수증
수리까지 막지는 않았다. 수리 가능한 것은 먼저 처리하고, 그래도 남은 핵심 공백만 pending으로 봉인했다.

브라우저에서 첨부 JSON 미리보기를 연 뒤 React 입력창이 오래된 파일 상태를 유지하는 문제도 확인했다.
이는 conversation context limit가 아니었다. exact 파일 미리보기를 닫고 같은 `/c/{conversation_id}` URL을
다시 로드하면 로그인·대화 ID·Pro 모드를 보존한 채 입력창만 정상화됐다. 새 채팅과 재전송은 0이다.

## P24 — C17 repair starvation 해소와 3-canary 최종 정직한 판정

P22에서 C17을 blocker fixpoint로 봉인한 뒤 generic 라우터를 다시 감사했다. 공개자료 공백이 먼저
잡히면 독립된 verifier repair 후보가 계속 뒤로 밀리는 starvation이 있었다. 공백 종류별로 독립 라우팅하고
repair ordinal을 양수 전체로 확장한 뒤, 같은 C17 conversation에서 pass 7 repair를 정확히 한 번 수행했다.

```text
pass 7  VERIFIER_REPAIR
  pass id                        PROPASS-36260e1001f007cd9ceffa10
  candidate ids                  2
  fact / route snapshot          61/124 -> 61/126
  accepted fact                  42 -> 44
  verifier repair pending        3 -> 1
  response hash                  22ab2add8ecdcbc200bd91d2abbad0923eb6c756e2b5f6624515162bd4efc8aa

pass 8  PUBLIC_GAP_CLOSURE
  pass id                        PROPASS-7ab9fef365033d28accad74d
  new fact / route               3 / 6
  accepted fact                  44 -> 46
  public material gap            6 -> 2
  response hash                  d699a3e7218abdb0c3bfe7b64ed2f44e321335c04e965c4160467563d804f426

pass 9  SATURATION_AUDIT
  pass id                        PROPASS-d770d317bc6680a959dc4ce9
  new fact / route               0 / 0
  invalid route reference 정리   yes

pass 10 SATURATION_AUDIT
  pass id                        PROPASS-fc8f5edbcf70735f89072588
  new fact / route               0 / 0
  semantic progress              false
```

pass 8과 pass 10은 최초 fresh public 관측에서 exact marker가 늦게 보여 fail-safe 중단됐지만,
`--recover-submitted-only`가 같은 conversation의 이미 제출된 turn만 회수했다. 두 경우 모두
`browser_submit_delta=0`, 최종 `submit_count=1`이다. 이는 새 채팅으로 우회한 것이 아니라 서버에 이미
도착한 한 건의 답변을 인수한 것이다.

C17 최종 상태는 verify-and-inspect, inspect-only, 마지막 normal no-submit 세 경로에서 동일하게
재현됐다.

```text
accepted fact                    46 (current 31 / counter 13 / resolution 2)
mandatory / nonterminal          26 / 8
provider/parser core pending     5
public material gap              2
source-linkage incomplete        6
verifier repair pending          1
repairable candidate             0
effective dossier hash           63b01a00581d3d0b2e73a2c706d1e4f565b7e38cf4968052852b7b309c00d6a7
source verification hash         f4729b5e6fec26cd8d0ba72a743c7d1fbcaca6f73a585773499ccc80bcb1c3b4
saturation receipt hash          304dd2e46a09cf1c876d032105a8dafd02a994debe335eb34259a6896dd3b603
normal terminal status           RESEARCH_GAP_REOPEN_LIMIT_PENDING
normal terminal new pass/submit  0 / 0
score / Stage                    null / null
publication                      withheld
```

C06도 multi-repair 코드에서 재감사했다. `accepted=74`, `public_material_gap=0`,
`verifier_repair_pending=1`, `repairable_candidate=0`으로 재현됐다. 즉 P20의 낡은 “한 번만 repair” 설명이
현재 blocker가 아니다.

세 live canary의 최종 판정은 다음과 같다.

```text
C06  NEEDS_VERIFIER_REPAIR             score/Stage null, publication withheld
C17  RESEARCH_GAP_REOPEN_LIMIT_PENDING score/Stage null, publication withheld
C28  RESEARCH_GAP_REOPEN_LIMIT_PENDING score/Stage null, publication withheld
```

따라서 fresh-session, same-conversation recovery, compact multi-repair, 무한 재개 차단, fail-closed 경계는
운영 계약대로 작동했다. 그러나 세 canary가 모두 full-thesis component entry에 도달한 것은 아니다.
이번 단계의 정직한 verdict는 `LIVE_FULL_THESIS_NOT_ACHIEVED`이며
`PRO_FIRST_V2_1_OPERATIONAL_RESEARCH_READY`를 선언하지 않는다. 새 검색, 점수 보정, Stage 추정으로 이
결론을 덮지 않는다.

최종 변경분 로컬 검증은 다음과 같다.

```text
fresh orchestration focused       50/50 PASS
compact multi-repair focused      23/23 PASS
browser adapter focused           31/31 PASS
focused total                    104/104 PASS
full unittest suite            7,791/7,791 PASS (skip 38, failure/error 0)
compileall                         PASS
git diff --check                  PASS
fresh efficiency audit            PASS / critical 0
  audit hash                       47d96d1f3b602ef0b963ce3772ffc70cbacdb655fb399aefdcf0a61fb9b87b6a
production static audit            PASS / critical 0
  audit hash                       ff981d5bed53ebaec938dbcc3049c4e31a854766cd6517ac306376609c94a27a
```

Playwright focused/전체 테스트는 WSL 시스템에 설치되지 않은 `libnspr4` 등을 저장소 밖
`/tmp/e2r-playwright-deps`에서만 로드해 실행했다. 최초 기동 실패는 코드 실패로 세지 않았고, 동일
테스트를 의존성 경로와 함께 다시 실행해 `31/31 PASS` 및 전체 suite PASS를 확인했다. 저장소·시스템
패키지·로그인 브라우저는 변경하지 않았다.

## P25 — C06 완전 새 채팅 재실행과 최종 계약 누락 감사

사용자 확인에 따라 장시간 사용한 기존 conversation을 더 재사용하지 않고, 로그인된 전용 Chrome의
`새 채팅`에서 C06 blind initial을 다시 시작했다. 기존 canary의 accepted fact, score, Stage, 질문
종결 답안은 새 packet에 넣지 않았다.

```text
runtime root       C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260828T203034Z
job                PROJOB-287556cc59c10f124d615c4d
run                PRORUN-b412396d383c92aaf08e9837
initial pass        PROPASS-802906d09c9f8769cc87b378
conversation        6a91f0dd-4fa4-83ee-b2b9-434f39437b07
durable user turn   7a00534a-f0ed-4c91-94a4-b3432793d5ea
fresh session       FRESH-V2-1-C06-INDEPENDENT-20260828T203034Z
prompt chars        61,302
gold leakage        0
upload count        1
submit count        1
recovery submit     0
current state       RESEARCH_RUNNING
```

첫 monitor가 공개 conversation hydration에서 marker를 늦게 읽어 fail-safe 종료했지만, 실제 DOM의 exact
user turn과 job/run marker가 서버에 저장된 것을 확인했다. 이후에는
`--resume-submitted-job-id`로 같은 job을 감시할 뿐 composer 입력이나 click을 다시 하지 않는다.

쉬운 예로 택배 접수증은 이미 한 장 발급됐다. 배송 조회 화면이 늦게 뜬다고 같은 택배를 다시 접수하지
않고, 기존 송장번호만 조회하는 상태다.

새 응답을 기다리는 동안 master goal의 56개 명시 테스트와 운영 연결을 역감사해 다음 누락을 찾고
수정했다.

```text
DeltaResearchContext
  previous verified question closure map
  impacted question family
  stale primitive
  monitoring/future-event question
  new/superseding fact
  exact affected component

DELTA_RESEARCH prompt
  영향받은 question만 contract 본문에 다시 열기
  변화 없는 question은 closure hash 재검산 뒤 reuse
  같은 snapshot은 job/submit/query/fetch 전에 중단

delta scoring
  영향받은 component/Judge만 재계산
  superseded current risk는 penalty에서 제외
```

이전에는 `DELTA_RESEARCH requires the dedicated V2 delta path` 오류만 있었으나, 이제
`build_delta_job_packet_v2()`와 `prepare_delta_v2_job_in_logged_in_browser()`가 explicit prior thesis와
`DeltaResearchContext`를 받아 실제 packet/prompt/browser-prepare 경로로 연결된다. durable packet 재사용
시 요청한 prior thesis/delta context와 다르면 hard fail한다. prior question closure는 64자리 문자열 존재만
보지 않고 closure payload의 canonical hash와 일치하는지 재계산한다.

Section 30의 Reviewer A~H도 공통 report counter를 읽는 방식이 아니라 담당 leaf test command를 직접
실행하도록 추가했다. 각 reviewer receipt에는 exact command, 입력 파일별 SHA-256, aggregate input hash,
raw command output hash, test count, finding이 따로 남는다. 첫 rehearsal에서 C는 WSL Chromium shared
library 부재, H는 공통 browser prepare helper의 `job_id` 전달 누락을 각각 찾아냈다. H 코드 오류는
수정했다. C의 Chromium shared library는 이전 전체 회귀와 동일하게 저장소 밖
`/tmp/e2r-playwright-deps`를 `LD_LIBRARY_PATH`에 연결해 전체 adapter/multi-pass를 다시 실행한다.
GitHub workflow는 `playwright install --with-deps` 뒤 같은 전체 경로를 실행한다.

현재 focused 검증은 다음과 같다.

```text
delta packet/prompt/context binding       PASS
tampered prior closure hash rejection     PASS
same snapshot zero-submit/query/fetch     PASS
impacted component/Judge only             PASS
superseded risk current penalty removal   PASS
Reviewer C Chromium/whole multi-pass      57/57 PASS
Reviewer H static/efficiency/runtime      40/40 PASS
Reviewer A~H direct leaf gate             PASS (8/13/57/54/50/57/15/44)
Reviewer A~H receipt hash                 73de48aa804873149de4e6672b9f0a27e6e50228f8faa690c88054c3da55e9a0
compileall                                PASS
git diff --check                          PASS
```

기준 committed head `229369a586fb9530649498d9bec619701eb4f609`의 GitHub Actions 세 개는 모두
SUCCESS다. 위 P25 변경은 아직 검토·전체 회귀·한글 commit/push 전 working tree에 있으며, 새 C06 응답의
capture/import/verify/saturation 결과와 Reviewer A~H 최종 receipt가 확정된 뒤 P9/P10 단계로 나눈다.
PR #7은 계속 Draft/open이고 main은 병합하지 않는다.

## P26 — C06 새 채팅 full-thesis FINAL과 V3 component 계보 수리

P25에서 시작한 완전 새 C06 Pro 채팅은 같은 conversation과 exact job/run marker를 유지한 채
공개 조사·검증·saturation을 끝냈다. 이전 Gate 1의 996-fact snapshot, 70.2점, Stage 2를 prompt나
scoring 입력에 답안으로 넣지 않았다.

```text
job / run                        PROJOB-287556cc59c10f124d615c4d
                                 PRORUN-b412396d383c92aaf08e9837
conversation                     6a91f0dd-4fa4-83ee-b2b9-434f39437b07
as_of_date                        2026-08-23
mandatory / nonterminal          28 / 0
public material gap              0
verifier repair pending          0
provider/parser core pending     0
hard-break lifecycle pending     0
source-linkage incomplete        0
candidate / compiled facts       69 / 56
current/counter/resolution       46 / 6 / 4
historical/superseded            12 / 1
saturation                       FULL_THESIS_READY
component / Judge / impact       7 / 21 / 19
```

첫 scoring 재개에서 `validated impact lacks fact lineage in its component memo`가 발생했다. 자료가
부족한 문제가 아니라 V3 dossier와 기존 component bridge의 field dialect가 달랐다.

```text
V3 dossier                       support_fact_ids
기존 bridge가 읽던 field         positive_fact_ids
결과                              C06 support fact가 positive roster에서 사라짐
추가 문제                         다른 component에도 eligible한 verified fact가 memo에서 완전 소실
```

generic 수리는 두 부분이다.

1. V2 `positive_fact_ids`와 V3 `support_fact_ids`를 같은 검증 positive roster로 투영한다.
2. 해당 component의 explicit positive/counter/resolution에 직접 배치되지 않았더라도 contract상
   eligible한 verified fact는 삭제하지 않고 `context_fact_ids`에 둔다. context는 Judge가 positive
   support로 인용할 수 없지만 impact의 source/fact lineage 검문에는 남는다.

쉬운 예로 Pro가 현금흐름 fact를 EPS/FCF의 직접 support 목록에 쓰고 earnings visibility에도 의미가
있다고 판정한 경우, 전자는 positive이고 후자는 context다. 같은 fact를 두 번 점수 주거나 어느 쪽에서도
버리지 않는다.

이 변경은 아직 점수 영수증이 없던 `SCORING` 상태에서 발견됐다. 이전 component/Judge artifact는
덮어쓰거나 삭제하지 않고 runtime의 hash-bound `semantic_migrations` 아래 보존했다. score receipt와
StageCourt receipt가 하나라도 존재하면 이 복구 경로를 사용할 수 없다. score 확정 전 Judge artifact가
없는 경우에만 21개를 재구축하는 회귀시험도 추가했다.

```text
focused scoring tests            41 / 41 PASS
new Pro research submit          0
recovery browser submit          0
scoring query / fetch            0 / 0
component bridge semantics       e2r_pro_component_bridge_v2_support_alias_and_context_retention
```

수리 뒤 기존 deterministic scorer와 `AtomicStageCourtV2`가 낸 canonical 결과는 다음과 같다.

```text
score_valid                       true
score                             23.275
interval                          23.275 ~ 23.275
component vector                 EPS/FCF 7.0
                                  visibility 8.65
                                  bottleneck/pricing 1.5
                                  market mispricing 1.0
                                  valuation 2.0
                                  capital allocation 2.125
                                  information confidence 1.0
canonical Stage                  0 FINAL
scorer critical                  0
new scorer / Stage engine        0 / 0
```

이 점수는 기존 Gate 1의 `70.2 / Stage 2`를 대체하거나 비교 재현하는 값이 아니다. Gate 1은 frozen
996-fact corpus이고, P26은 새 Pro-first 56-fact corpus다. master goal의 live canary PASS 기준은 높은
점수가 아니라 mandatory question terminality, verifier 완료, public-gap closure, source-backed lineage다.
따라서 낮다는 이유로 추가 검색하거나 threshold를 조정하지 않는다.

정규화된 외부 검수 영수증은
`p26_c06_full_thesis_scoring_final_receipt.json`에 기록했다. raw Pro report, browser profile, runtime DB,
source cache는 Git에 넣지 않았고 SHA-256과 canonical count만 게시했다. C06 하나로
`OPERATIONAL_RESEARCH_READY`를 선언하지 않으며, 서로 다른 mechanism의 C17·C28 live full-thesis
canary와 P10 전체 회귀·CI가 남아 있다.

## P27 — C17 R7 V3 상태 투영 수리와 손상 conversation 봉인

C17 독립 fresh canary R7은 새 ChatGPT Pro conversation에서 initial submit/capture를 각각 한 번만
수행했고, 같은 conversation의 공개 공백 및 verifier repair를 이어 갔다. initial V3 dossier의 전체
mandatory question detail에는 `PARSER_PENDING`이 있었지만 Pro의 최상위 요약 상태는
`NEEDS_PUBLIC_GAP_CLOSURE`였다. 기존 adapter는 V2에만 deterministic 상태 투영을 적용해 V3 import를
거부했다.

generic 수리는 V2와 V3 모두에서 Pro의 요약 상태를 diagnostics로 보존하고, 운영 상태는 전체 mandatory
question roster로 다시 계산하도록 통일했다. source document와 material fact는 고치거나 추가하지 않는다.

```text
Pro top-level status             research_saturation.pro_reported_research_status
deterministic operational state  mandatory question closure로 계산
focused V2/V3 status tests       41 / 41 PASS
fact/source mutation             0 / 0
```

수리 뒤 R7은 같은 conversation에서 pass 7까지 실자료 보완을 진행했다. 그러나 다음 follow-up 전송 직전
브라우저 public history에서 직전 exact follow-up turn을 다시 확인하지 못해 `FollowupSubmitBlocked`로
fail-closed됐다.

```text
job                              PROJOB-9c71890eb783720160b97e4e
run                              PRORUN-30cbfcaf7502aa7cbafc6ada
conversation                     6a92600d-77c4-83e8-ac7f-203415582daa
last accepted facts              33
remaining nonterminal questions  2
verifier repair pending          0
failure                          exact follow-up turn persistence 미확인
automatic resubmit               금지
score / Stage authority          없음
```

이는 연구 내용 부족이나 낮은 점수 판정이 아니라 conversation transport 계보 실패다. R7 답을 새 답처럼
재라벨하거나 같은 채팅에 자동 재전송하지 않는다. R7은 진단용으로 보존하고, 새 `fresh_session_id`, job,
run, pass, conversation을 가진 C17 successor를 initial prompt부터 다시 시작한다.

## P28 — C17 R8 repair-heavy 진단 봉인과 기존 탭 전용 transport 수리

C17 R8은 별도 fresh job/run/conversation에서 initial을 시작했지만 full-thesis tail이 18개 pass까지
늘어났다. 최초 efficiency receipt는 mandatory `26/26`과 acceptance `6/6`을 PASS로 기록했으나, 실제
최초 question status를 다시 세면 terminal은 4개뿐이었다.

```text
PUBLIC_SEARCHABLE                   16
PARSER_PENDING                       6
NOT_APPLICABLE_WITH_REASON           3
SUPPORTED_NON_SCORING                1
```

즉 question row 26개가 존재한다는 사실을 research coverage로 센 것이 문제였다. 쉬운 예로 시험지
26칸에 `아직 더 찾아야 함`이라고 적어 놓고 26문제를 완료했다고 집계한 셈이다. R8 tail은 이를
public-gap 11회와 verifier repair 5회로 뒤늦게 메웠고, accepted fact 44개까지 갔지만 mandatory 3개와
core parser/source-linkage 공백을 닫지 못했다.

```text
job / run                         PROJOB-22fdf2fdb1c458be082f3cbd
                                  PRORUN-56ff66fa86b4ab918f0d5e55
conversation                      6a92a26e-bee8-83e8-a424-bbd9eb59ff79
pass total / complete / failed    18 / 16 / 2
initial / public / repair / audit 1 / 11 / 5 / 1
accepted facts                    44
remaining mandatory              3
score / Stage receipt             없음 / 없음
```

브라우저 transport에도 두 결함이 있었다. 첫째, extension shadow root 안의 가짜 `html > body`를
Playwright CSS가 main document body로 오인할 수 있었다. 둘째, 서버 저장 확인이 임시 ChatGPT 탭을
열어 사용자 화면에 중복 탭을 남길 수 있었다. main-document XPath body를 사용하고, 서버 저장 확인은
기존 탭에서 exact conversation을 새로고침하도록 바꿨다. user-turn 검사는 한 번의 atomic DOM
evaluation으로 합쳤다.

Pass 17은 한 번 제출된 뒤 기존 탭 새로고침에서 서버 결과가 복구되어 새 fact 2개와 route 3개를
캡처했다. Pass 18은 사용자 턴이 뒤늦게 서버에 나타났지만 정확한 assistant pass 결과가 생성되지
않았다. 이제 completion monitor가 current `PROPASS` marker를 요구하므로 같은 job/run의 오래된 답을
현재 답으로 잘못 캡처하지 않고 `FAILED_HARD`로 봉인한다. `FAILED_HARD`는 다음 compact repair
planner의 active pass에서도 제외한다.

fresh operational proof에는 master goal의 좁은 pass budget을 강제했다.

```text
public-gap + counter              최대 1회
verifier repair                   최대 1회
saturation audit                  최대 1회
초과 시                            OPERATIONAL_EFFICIENCY_GATE_FAILED
                                    DIAGNOSTIC_ONLY
                                    NEW_CONVERSATION_REQUIRED
```

이는 일반 연구 상태기계의 의미 탐색을 COMPLETE로 잘라내는 cap이 아니다. 운영 효율 canary가
repair-heavy해졌다는 사실을 성공으로 포장하지 않는 proof gate다. 최초 prompt에도 모든 종목에 공통인
source-saturation gate를 추가했다. required official route를 실제로 시도하지 않은
`PUBLIC_SEARCHABLE`, 대체 HTML/PDF/regulator representation을 시도하지 않은 `PARSER_PENDING`을 남긴
채 직렬화하지 못하게 한다. 종목명·C17·누락 슬롯별 검색어 하드코딩은 추가하지 않았다.

```text
browser/completion/multi-pass      88 / 88 PASS
same-tab persistence/multi-pass    60 / 60 PASS
all-archetype prompt/fresh         68 / 68 PASS
R8 final disposition               OPERATIONAL_EFFICIENCY_GATE_FAILED
old job frozen                     true
new browser submit during freeze   0
```

정규화된 외부 검수 영수증은
`p28_c17_r8_operational_efficiency_failure_receipt.json`에 기록했다. raw Pro report, runtime DB,
source cache와 브라우저 profile은 추적하지 않고 SHA-256과 canonical count만 게시한다. 다음 실행은 새
브라우저 창이 아니라 현재 로그인된 기존 탭 안에서 새 ChatGPT conversation을 만든 C17 R9 blind fresh
run이다.

## P29 — C17 R9 초기 전송 취소 경계 봉인

C17 R9은 기존 로그인된 ChatGPT 탭 하나를 새 대화 화면으로 이동한 뒤 packet 1회 업로드와 submit
claim 1회를 수행했다. 그러나 60,439자 initial prompt의 exact user turn이 화면과 서버 conversation에
남지 않았고 conversation ID도 만들어지지 않았다.

```text
fresh session                    FRESH-V2-1-C17-R9-20260830T030222Z
job                              PROJOB-61af1aacb152d31ff4af16f3
run                              PRORUN-278c60ac5d42c6bea0e317f9
initial pass                     PROPASS-b9831d09cdaa64b34e4c7fa0
packet / prompt leakage          0 / 0
upload / submit claim            1 / 1
conversation / exact user turn   없음 / 없음
새 ChatGPT 탭                    0
```

원인은 새 창 여부가 아니라 같은 탭의 검증 순서였다. 큰 요청의 클릭 직후 user turn이 아직 DOM에
나타나기 전에 같은 탭을 conversation URL로 새로고침할 수 있었고, 그 navigation이 진행 중인
new-chat 요청을 취소할 수 있었다. 쉬운 예로, 우편물을 접수 창구에 내려놓자마자 접수 도장이 찍혔는지
기다리지 않고 창구 페이지를 닫아 버린 것과 같다.

운영 adapter는 이제 exact job/run marker를 가진 optimistic user turn이 현재 DOM에 실제로 나타날
때까지 먼저 기다린다. 나타나지 않으면 같은 탭 새로고침을 생략해 진행 중인 요청을 취소하지 않는다.
나타난 경우에도 최소 1초를 더 기다린 뒤, 그 **기존 탭 하나**에서만 exact conversation을 새로고침해
서버 저장을 검사한다. CDP worker에 남아 있던 `ChatGPT 탭 없음 -> context.new_page()` fallback도
제거했다. 이제 기존 ChatGPT 탭을 찾지 못하면 새 탭을 열지 않고 명시적으로 실패한다.
`new_page()`나 임시 검증 탭은 운영 경로에 남기지 않았다.

```text
exact optimistic turn 없음       same-tab refresh 금지
exact optimistic turn 있음       최소 1초 settle 후 같은 탭 reload
새 창/새 탭                       항상 0
기존 ChatGPT 탭 없음              fail closed
자동 재전송                       금지
```

R9은 `FRESH_SESSION_DIAGNOSTIC_ONLY / NEW_CONVERSATION_REQUIRED`로 공식 봉인했다. submit count는 1로
유지되고 자동 재전송은 불가능하다. Windows Python 3.14 Playwright에서 browser adapter,
exactly-once submit, completion capture, multi-pass 97개 회귀 테스트와, 새로고침이 없을 때만 살아남는
DOM sentinel 검증을 모두 통과했다. worker의 새 탭 fallback 제거 뒤에는 CDP attach worker test를
1/1로 다시 실행해 기존 탭 1개 유지와 ChatGPT 탭 부재 시 fail-closed를 확인했다. 정규화된 외부 검수 영수증은
`p29_c17_r9_initial_transport_failure_receipt.json`에 기록했고 raw runtime DB·browser profile·packet
본문은 추적하지 않았다. 다음 C17 R10은 새 브라우저 창이 아니라 현재 로그인된 기존 탭을 새 대화로
이동해 실행한다.

## P30 — C17 R10 public composer 60,000자 경계와 무손실 schema compact

R10을 처음 predecessor 방식으로 준비하려 한 호출은 브라우저 전 단계에서 멈췄다. R9에는 answer-bearing
dossier/capture가 없으므로 old-answer manifest의 선행 실행이 될 수 없었다. runtime/job/upload/submit은
모두 0이었고, 같은 R10 ID를 원래 C17 계약에 맞는 independent fresh boundary로 다시 시작했다.

```text
fresh session                    FRESH-V2-1-C17-R10-20260830T032712Z
job                              PROJOB-fa068a50ec045802bbb8d448
run                              PRORUN-7b5e5a8f4454bd8dd8a31954
prompt chars                    60,455
packet / prompt leakage          0 / 0
upload / submit claim            1 / 1
conversation / exact user turn   없음 / 없음
same-tab post-submit reload       0
새 ChatGPT 탭                    0
```

R10은 R9에서 고친 safe-no-refresh 경로를 탔다. click 뒤 composer는 0자로 비워졌지만 conversation ID,
user turn, assistant turn은 모두 0이었고 job/run marker도 남지 않았다. read-only CDP 점검 당시
ChatGPT page는 기존 탭 1개뿐이고 URL은 `https://chatgpt.com/`, Pro control은 보였으며 별도 오류 문구는
없었다. 따라서 이번 실패는 너무 이른 reload가 요청을 취소한 R9과 다르다.

직전 성공한 R8 prompt는 59,270자였고 R9/R10 실패 prompt는 각각 60,439/60,455자였다. 두 실행 모두
60,000자를 넘긴 composer가 로컬에서 비워졌지만 durable user turn을 만들지 못했다. 최근 추가한
source-saturation 계약을 삭제하거나 축약하지 않고, prompt에 그대로 들어가던 complete JSON Schema의
비의미 공백만 compact했다.

```text
JSON Schema pretty               23,412 chars
JSON Schema compact              13,813 chars
제거한 비의미 공백                9,599 chars
schema hash before / after        동일
R10 packet 재컴파일 prompt       50,856 chars
live initial 사전 차단            59,800 chars
```

쉬운 예로 계약서 조항을 지운 것이 아니라 JSON의 들여쓰기와 줄바꿈만 제거했다. compact block을 다시
`json.loads`했을 때 `e2r_pro_research_dossier_v3`와 모든 properties가 유지됐고 schema hash도
`40647e7e...`로 동일하다. compiler의 offline 1~3 contract 100,000자 능력은 유지하되, 실제 live initial
browser transport만 59,800자를 넘으면 upload/approval/send 전에 fail closed한다.

36개 canonical prompt snapshot을 모두 재생성했다. 최소/최대는 29,200/52,247자, audit 36/36 PASS,
critical 0이다. initial prompt와 fresh orchestration 테스트도 69/69 PASS다. R10은
`FRESH_SESSION_DIAGNOSTIC_ONLY / NEW_CONVERSATION_REQUIRED`로 공식 봉인했으며 정규화 영수증은
`p30_c17_r10_public_composer_boundary_receipt.json`에 기록했다. 다음 R11도 새 창이 아니라 현재
로그인된 기존 ChatGPT 탭 하나를 새 대화로 이동해 실행한다.

## P31 — C17 R11·R12 framework 입력 계층 진단과 기존 탭 경계 확정

R11은 P30에서 compact한 동일 50,856자 prompt를 기존 로그인 ChatGPT 탭 하나에서 다시 전송했지만,
conversation과 exact user turn이 생성되지 않았다. 따라서 `60,000자 초과가 유일한 원인`이라는 P30
가설은 기각됐다. schema compact와 59,800자 live preflight는 안전 경계로 유지하지만, 그것만으로
transport 문제가 해결됐다고 보지 않는다.

```text
R11 prompt                      50,856 chars
upload / submit claim           1 / 1
conversation / exact user turn  없음 / 없음
same-tab reload / 새 탭         0 / 0
```

R12는 같은 계약을 새 job/run/pass로 준비하되 approval과 submit을 모두 0으로 둔 pre-submit
진단이었다. 현재 UI에서 선택된 전송 control은 실제 `BUTTON#composer-submit-button`,
`data-testid=send-button`, `aria-label=프롬프트 보내기`였고 enabled/form 내부 상태도 확인됐다. 즉 잘못된
버튼을 누른 문제가 아니다. 이어서 Playwright의 framework `fill()`로 동일 prompt를 넣자 약 27.165초
뒤 ProseMirror 581개 paragraph가 생성됐고, 각 paragraph를 줄바꿈 하나로 이어 붙인 값이 compiled
prompt와 끝 줄바꿈 제외 문자 단위로 일치했다. 이 진단은 submit하지 않은 채 봉인했다.

실제 원인은 8,000자 이상 prompt에 쓰던 `replaceChildren + synthetic InputEvent`였다. 이 방식은 화면
DOM과 send button을 정상처럼 보이게 하지만 ChatGPT framework가 소유한 editor state를 갱신하지 않을
수 있다. 쉬운 예로 종이 신청서 위에 글자는 보이지만 접수 시스템에는 빈 신청서로 남은 상태다. 클릭하면
화면 글자만 사라지고 서버 user turn은 생기지 않는다.

운영 adapter는 이제 길이에 관계없이 public framework `fill()`만 사용하고 최대 120초를 기다린다.
실패하면 approval/send 전 중단하며 synthetic-DOM fallback은 없다. ProseMirror가 실제 ChatGPT처럼
top-level paragraph를 쓰거나 테스트 Chromium처럼 첫 줄 text node와 후속 `div`를 섞어도 모든 줄과
들여쓰기를 복원한다. Chromium이 contenteditable 선행 공백을 NBSP로 보존하는 경우에는
`NBSP -> 일반 공백` 하나만 정규화하고, 나머지 전체 prompt가 100% 같아야 통과한다. 과거의 95% 길이
허용은 제거했다.

```text
운영 src/e2r/pro_first new_page()  0
현재 로그인 ChatGPT page          1
기존 탭 없음                       fail closed
새 탭/새 창 fallback               없음
focused framework tests            4 / 4 PASS
browser/approval/capture/multi-pass 98 / 98 PASS
```

정규화된 외부 검수 영수증은
`p31_c17_r11_r12_framework_input_diagnosis_receipt.json`에 기록했다. R11·R12의 raw runtime DB, packet
본문, browser profile은 추적하지 않고 SHA-256과 canonical count만 게시한다. 다음 R13은 새 창을 열지
않고 지금 로그인된 기존 ChatGPT 탭 하나를 새 대화 화면으로 이동한 뒤, framework input 경로로 initial
prompt를 실제 전송한다.

## P32 — C17 R13 inline 계약 전송 실패와 첨부 기반 envelope 전환

R13은 P31의 framework `fill()` 수리를 사용해 50,856자 prompt를 문자 단위로 보존했고, 올바른 send
button과 기존 로그인 ChatGPT 탭 하나에서 정확히 한 번 전송했다. 그런데도 conversation ID와 exact user
turn이 서버에 남지 않았다.

```text
fresh session                    FRESH-V2-1-C17-R13-20260830T042425Z
job / run                        PROJOB-3dc5a68ca72b7f687251488f
                                 PRORUN-9de41d057e09c2535da38e8c
initial pass                     PROPASS-5d4f1b9d099234d90fadc023
prompt chars                     50,856
upload / approval / submit       1 / 1 / 1
conversation / exact user turn   없음 / 없음
capture                          0
새 ChatGPT 탭                    0
```

최초 CDP 연결은 browser mutation 전에 180초 timeout이 났다. 누적된 `chrome-devtools-mcp` 18개만
종료하고 전용 E2R Chrome을 같은 profile로 재시작했으며 로그인 상태와 ChatGPT 탭 1개를 유지했다. 그 뒤
새 job을 만들지 않고 같은 R13 job/run/pass를 복구해 준비·승인·전송했다. 전송 후 exact marker가 없는
것을 확인했으므로 재전송하지 않고 `USER_ATTENTION_REQUIRED`로 봉인했다.

이 결과로 P31 설명도 좁혀졌다. synthetic DOM 입력은 실제 결함이었지만 **유일한 원인**은 아니었다.
R13은 framework 입력을 썼는데도 실패했기 때문이다. 쉬운 예로 신청서 입력 방식 하나를 고쳤는데도
50쪽짜리 계약서 전체를 접수창에 다시 붙여 넣는 방식 자체가 여전히 안정적으로 접수되지 않은 셈이다.

수리는 계약을 줄이지 않고 전달 위치만 바꾼다. `research_packet.json` 안에 다음 세 가지 전체를 넣고
각각 canonical hash로 결박했다.

```text
initial_research_protocol.instructions_markdown   공통 조사·검증 규칙 전체
research_contract_snapshot.contracts              선택 contract와 cross guard 전체
dossier_output_schema                             ResearchDossierV3 schema 전체
```

composer에는 job/run/pass와 위 field path·hash를 가리키는 짧은 transport envelope만 넣는다. 격리된
C17 fixture 기준 packet은 153,508자, 외부 감사용 full contract prompt는 50,206자 그대로이고, 실제
composer envelope만 1,553자다. 즉 문제를 피하려고 질문이나 schema를 삭제한 것이 아니라, 서류 원본은
첨부하고 접수창에는 “첨부 원본의 1~3번 조항을 모두 실행하라”는 표지만 넣은 것이다.

packet의 protocol·contract roster·mandatory question roster·schema가 로컬 canonical 원본과 정확히
같지 않으면 브라우저 준비 전에 실패한다. full contract prompt도 계속 컴파일해 별도 receipt로 남기고,
transport envelope와 contract/question/schema roster가 다르면 중단한다. 종목명이나 누락 슬롯별 검색어
하드코딩, 점수/Stage 권한, 자동 재전송은 추가하지 않았다. CDP에 기존 browser context가 없는 경우도
새 context를 만들지 않고 실패하도록 해, 운영 경로에는 새 context/page/window fallback이 하나도 없다.

```text
Linux initial/fresh/live-runtime regression       106 / 106 PASS
Windows fresh browser E2E                            2 / 2 PASS
Windows browser/approval/capture/multi-pass         99 / 99 PASS
운영 src/e2r/pro_first new_page()                    0
기존 ChatGPT 탭 없음                                 fail closed
```

정규화된 외부 검수 영수증은
`p32_c17_r13_inline_transport_failure_and_attachment_envelope_receipt.json`에 기록했다. raw runtime DB,
packet 본문, browser profile은 추적하지 않고 SHA-256과 canonical count만 게시한다. 다음 R14는 새 창이나
새 탭을 열지 않고 지금 로그인된 기존 ChatGPT 탭 하나를 새 대화로 이동해, JSON packet 1회 첨부와 짧은
transport envelope로 독립 C17 initial을 시작한다.

## P33 — C17 R14 pre-browser CDP 실패와 기존 ChatGPT page 격리 연결

R14 packet은 새 attachment-backed 방식으로 정상 생성됐다. full contract 50,856자는 packet에 유지되고
composer envelope는 1,585자였으며 packet/prompt leakage는 0이었다. 그러나 browser-level WebSocket에
연결된 뒤 Playwright 초기화가 180초 안에 끝나지 않아 prepare 전에 안전 중단됐다.

```text
fresh session                    FRESH-V2-1-C17-R14-20260830T050553Z
job / run                        PROJOB-3de09b498e48dcd86c35625b
                                 PRORUN-f401ed47f41227ada896c41f
initial pass                     PROPASS-fb547d9210da25bcc09e4f4f
transport / full contract        1,585 / 50,856 chars
browser session                  없음
upload / approval / submit       0 / 0 / 0
새 탭 / Chrome 재시작            0 / 0
```

raw CDP의 `Browser.getVersion`, `Target.getTargets`, ChatGPT page attach와 `document.title`은 즉시
응답했다. 반면 Playwright protocol log에서는 browser가 가진 페이지 5개를 전부 auto-attach한 뒤, 실제
작업과 무관한 Naver page session 2개가 `Page.enable`, `Runtime.enable` 등에 답하지 않았다. 사용할 수
있는 ChatGPT 탭 1개가 다른 탭의 디버깅 초기화에 같이 묶여 막힌 것이다.

쉬운 예로 ChatGPT 방 하나에 들어가려는데 건물의 다른 방 네 개까지 모두 안전점검이 끝나야 문을 열어
주는 구조였다. 다른 방 두 개가 응답하지 않자 ChatGPT 방이 정상이어도 입장이 멈췄다. 해결은 다른 방을
닫는 것이 아니라, 점검 대상에서 ChatGPT 방만 선택하는 것이다.

`ExistingPageCDPProxy`는 loopback 임시 WebSocket에서 client 한 개만 받고, 기존 browser CDP와
Playwright 사이에서 다음 경계만 적용한다.

```text
ChatGPT origin의 기존 page       Playwright에 전달
다른 page / browser_ui target    Playwright에서 숨김, 실제 탭은 계속 열어 둠
root Target.getTargetInfo        Playwright가 값은 쓰지 않는 동기화 응답만 제공
그 외 CDP message                변경 없이 전달
```

proxy는 context/page/window를 생성하지 않고 사용자 탭을 닫지도 않는다. CDP endpoint와 proxy listener
모두 loopback만 허용한다. 기존 ChatGPT page가 없으면 Worker가 새 탭을 만들지 않고 fail closed한다.
Windows 실행환경도 저장소 요구사항인 Playwright 1.62로 맞췄고, WebSocket dependency를 explicit
`pro-first` dependency와 hash lock에 추가했다.

실제 같은 Chrome에서 read-only Worker proof를 실행하자 5개 page는 그대로인 채 Worker에는
`https://chatgpt.com/` page 1개만 보였고 editor ready까지 4.2초에 확인한 뒤 정상 분리됐다. R14는
browser mutation·submit 모두 0인 진단으로 봉인했으며 새 commit에 묶인 successor만 시작한다.

```text
Linux proxy unit                                  2 / 2 PASS
Windows proxy + worker targeted                   4 / 4 PASS
Windows proxy + browser regression               38 / 38 PASS
운영 new_page/new_context fallback                 0 / 0
실제 Chrome page / ChatGPT page 유지               5 / 1
```

정규화된 외부 검수 영수증은
`p33_c17_r14_existing_page_cdp_proxy_receipt.json`에 기록했다. raw protocol log, runtime DB, packet 본문,
browser profile은 추적하지 않는다. 다음 R15는 새 창·새 탭·Chrome 재시작 없이 지금 로그인된 기존
ChatGPT 탭 하나만 격리 연결해 독립 C17 initial을 시작한다.

## P34 — C17 R15 initial PASS와 기존 탭 artifact 재내보내기 복구

R15는 P33의 기존 page 격리 proxy와 attachment-backed 1,585자 envelope로 실제 C17 initial을 전송했다.
새 창·새 탭·새 context는 만들지 않았고, 현재 로그인된 ChatGPT 대화 하나에서 initial user turn을 정확히
한 번 서버에 남겼다. Pro는 13개 source document, 60개 atomic fact, 26개 mandatory question, 57개
search-route receipt를 포함한 ResearchDossierV3를 작성했다.

```text
fresh session                    FRESH-V2-1-C17-R15-20260830T052335Z
job / run                        PROJOB-312387371378cd5a5c1e378c
                                 PRORUN-6121ceae520bb75519b0acfa
initial / re-export pass         PROPASS-4b0a65bd8315e8bc2ed18aaf
                                 PROPASS-b025ba306b41347200a148d0
conversation                     6a93be74-db60-83ee-a7ab-c8262cbb0b39
initial submit / capture          1 / 1
새 탭 / 새 창 / 자동 재전송          0 / 0 / 0
```

최초 Pro 응답의 연구 내용은 존재했지만, 첨부 링크 세 개가 가리키는 sandbox 파일은 실제로 생성되지
않았다. 대화 내부 실행 기록에서는 dossier를 읽으려던 코드가 `FileNotFoundError`를 냈고, 화면의 다운로드
control도 `file_not_found`를 반환했다. 링크가 오래돼 만료된 문제가 아니라, 파일을 만들기 전에 검증하려다
실패한 뒤 존재하지 않는 링크를 최종 응답에 붙인 transport 결함이었다.

따라서 새 조사나 새 initial을 시작하지 않고 같은 대화에 `ARTIFACT_REEXPORT` 한 번만 보냈다. 이 pass는
웹 검색·새 자료·새 fact 판단·점수·Stage 권한을 모두 금지하고, initial dossier의
`research_pass_id=PROPASS-4b0a65bd8315e8bc2ed18aaf`를 그대로 보존한 채 파일만 다시 쓰게 한다.

첫 전송 시 Playwright가 계속 움직이는 send control의 `stable` 상태를 기다리다 click timeout을 냈지만,
native DOM click은 이미 서버에 도달해 exact user turn이 생겼다. 재시작 복구는 먼저 job/pass/parent marker가
모두 같은 durable user turn을 읽고, 있으면 click하지 않는다. 실제 R15에서도 두 번째 click 없이
`browser_submit_delta=0`으로 기존 pass를 복구했다.

생성된 파일을 누르면 실제 dossier보다 먼저 다음 다운로드 안내 JSON이 온다는 사실도 확인했다.

```text
1차 응답    status/file_name/file_id/download_url를 가진 약 500-byte manifest
2차 응답    같은 origin의 /backend-api/estuary/content 실제 파일
실제 파일    279,348 bytes / SHA-256 f857328a6a74...
```

쉬운 예로 1차 응답은 택배 내용물이 아니라 수령 주소가 적힌 송장이다. adapter는 이제 화면 filename,
manifest `file_name/file_id`, signed URL의 `fn/id`, same-origin estuary path가 전부 일치할 때만 2차 파일을
받는다. 다른 origin·다른 filename·다른 file ID는 거부한다. 다운로드는 기존 파일 control에서 시작하며
private endpoint를 추측하거나 composer를 건드리지 않는다.

Chrome Memory Saver가 백그라운드 ChatGPT renderer를 잠들게 해 browser socket은 응답하지만 page의
`Page.enable/Runtime.enable`이 멈춘 사례도 있었다. Worker는 loopback target 목록에 ChatGPT page가 정확히
하나일 때 그 **기존 target만 activate**해 깨운다. page/window/context를 생성하지 않고, 여러 ChatGPT
page가 있거나 기존 page가 없으면 기존 fail-closed 경계를 유지한다. iframe·service worker도 허용 origin이
아니면 Playwright 초기화에서 숨기되 실제 사용자 탭과 worker는 닫지 않는다.

최종 dossier capture/import/source verification 결과는 다음과 같다.

```text
schema / validation              e2r_pro_research_dossier_v3 / PASS
source / atomic fact             13 / 60
material / counter / resolution  38 / 14 / 8
derived metric                   7
mandatory question               26 / 26
compiled evidence fact           45
현재성 제외 material              4
post-preflight material          31 accepted / 34 = 91.1765%
genuine semantic repair 후보      3
query / search                    0 / 0
partial score publication         0
initial efficiency gate           PASS
```

관련 Windows browser/proxy/multi-pass/fresh regression은 134/134 PASS, focused Linux recovery는 4/4
PASS이며 `compileall`과 `git diff --check`도 통과했다. 임시 probe·다운로드 manifest 사본은 0개로
정리했다. 정규화 영수증은
`p34_c17_r15_initial_efficiency_and_artifact_reexport_receipt.json`에 기록하고 raw runtime DB, source page
본문, dossier 원문, browser profile은 추적하지 않는다.

저장소 전체 Windows 회귀도 `PYTHONPATH=src python -m unittest discover -s tests -q`로 실제 실행했다.
7,714개를 2,883.265초 동안 수행한 결과는 76 failure, 462 error, 38 skip으로 **전체 PASS가 아니다**.
대표 원인은 이 변경의 선택 테스트가 아니라 Windows Python이 명시적 encoding 없는 UTF-8 fixture를
CP949로 읽은 오류, clean PR에서 의도적으로 제외한 legacy `output/`·과거 giant research fixture를
unrelated 테스트가 요구한 오류, Windows Git이 WSL UNC worktree를 `safe.directory`로 거부한 오류다.
따라서 외부 판정에서는 134/134 관련 회귀 PASS와 7,714개 전체 실행의 환경·legacy fixture 비호환을
분리하며, 후자를 전체 PASS로 주장하지 않는다.

R15는 initial efficiency gate를 통과했지만 아직 점수/Stage 완료가 아니다. 현재 durable job 상태는
`GAP_ADJUDICATION`이고 genuine semantic repair 후보가 3개 남아 있다. 다음 작업은 새 initial이나 다른
창이 아니라 **이 R15의 deterministic adjudication과 bounded same-conversation full-thesis tail**이다.

## P35 — C17 R15 pass 3 무전송 복구와 response/artifact hash 계보 분리

R15 full-thesis 첫 `PUBLIC_GAP_CLOSURE`는 기존 conversation에서 정확히 한 번 전송돼 응답 캡처까지
끝났지만, effective dossier를 durable pass 장부와 대조하는 단계에서 멈췄다. 원인은 Pro 연구 내용이나
fact가 아니라 P34의 artifact 재내보내기 경로가 서로 다른 두 byte stream의 SHA-256을 같은 필드로
취급한 것이었다.

```text
initial visible response hash   d811ba7b29e03cf6...
downloaded dossier file hash    f857328a6a740765...
허용한 변경                      research_passes.initial.response_hash 한 칸
fact / score / Stage 변경        0 / 0 / 0
```

쉬운 예로 편지 본문과 그 편지를 담은 JSON 첨부파일은 내용상 연결돼도 바이트는 다르므로 지문도 다르다.
기존 initial import는 첨부파일 지문을 편지 본문 지문 칸에 적었고, 후속 pass 병합기의 엄격한 대조가 이를
정상적으로 잡았다.

수리는 종목·아키타입 조건문 없이 generic fail-closed 경계로 구현했다. 초기 import는 이미 durable
approval scope가 있으면 그 scope의 initial response hash를 사용한다. 과거 R15 snapshot은 exact initial
pass, 정확히 하나인 `ARTIFACT_REEXPORT` 자식, 같은 conversation/prompt, 검증된 `DOWNLOAD_JSON` capture,
`COMPLETE/submit_count=1`, score/Stage 권한 없음이 모두 맞을 때만 initial pass row의 response hash 한 칸을
메모리에서 정규화한다. 원본 snapshot과 runtime DB를 손으로 고치지 않고 새 후속 snapshot이 정정된
계보를 이어받게 했다.

`ARTIFACT_REEXPORT`는 SQL/browser 감사 장부에는 계속 남지만 semantic ResearchDossier pass가 아니다.
이 pass의 지시문 자체가 original initial `research_pass_id`를 보존하고 새 연구·fact 판단을 금지했기
때문이다. 따라서 durable pass projection은 이 운송 전용 행을 dossier의 새 연구 행으로 넣지 않는다.
이 경계를 회귀 테스트로 추가했다.

같은 기존 탭에 이미 있던 pass 3 capture를 `--recover-submitted-only`로 회수한 결과는 다음과 같다.

```text
pass                             PROPASS-32e644fe538d1b659cd982bd
status / submit_count            COMPLETE / 1
recovery browser submit delta    0
new fact / lineage / route       5 / 2 / 23
effective fact / question/route  65 / 26 / 80
effective dossier hash           8af6f88eb814747f...
새 탭 / 새 창 / 새 initial         0 / 0 / 0
```

복구 직후 이전 verification receipt는 새 dossier보다 오래됐으므로 read-only inspection이 그대로 쓰지 않고
거부했다. 이어서 브라우저를 열지 않는 `VERIFY_CURRENT_DOSSIER_NO_BROWSER`로 65개 fact를 재검문했고,
그 뒤 완전 read-only inspection도 같은 결과를 재현했다.

```text
candidate / terminal / accepted  65 / 65 / 47
accepted current/counter/resolve  32 / 10 / 5
semantic/source repair candidate  6
query / search                    0 / 0
mandatory / nonterminal           26 / 6
provider-parser core pending      5
public material gap               14
source linkage incomplete         5
verifier repair pending           7
component entry                   false
score / Stage publication         없음 / 없음
```

관련 네 모듈의 Windows 회귀는 명시적 `E2R_SOURCE_COMMIT_SHA`로 148/148 PASS다. 첫 실행에서는 Windows
Git이 WSL UNC worktree에서 `HEAD`를 읽지 못해 10개가 setup error였고 assertion failure는 0이었다. 공식
cross-runtime source SHA 입력으로 같은 148개를 재실행해 전부 통과했다. targeted Windows/Linux는 각각
2/2 PASS, `compileall`과 `git diff --check`도 PASS다. 정규화 영수증은
`p35_c17_r15_pass3_recovery_and_hash_lineage_receipt.json`에 기록한다.

현재 R15는 initial과 pass 3이 유효하지만 saturation·점수·Stage 완료 상태는 아니다. 다음 단계는 새 창이나
새 채팅이 아니라 conversation `6a93be74-db60-83ee-a7ab-c8262cbb0b39`의 기존 ChatGPT 탭에서 bounded
full-thesis tail을 계속하는 것이다.

## P36 — C17 R15 operational efficiency FAIL과 R16 공통 prompt guard

P35 이후 R15 full-thesis runner를 기존 ChatGPT 탭·기존 conversation으로 재개했다. 브라우저 연결은
정상이었고 전송 delta는 0이었지만, deterministic operational efficiency gate가 두 번째 public-gap pass를
보내기 전에 중단했다.

```text
initial                         1
public-gap/counter              1 / allowed 1
semantic repair                0
saturation audit               0
두 번째 public-gap submit       0
verdict                         OPERATIONAL_EFFICIENCY_GATE_FAILED
```

이는 세션 고장이나 브라우저 창 문제가 아니다. master goal의 정상 목표는 initial 1회,
public-gap/counter 0~1회, semantic repair 0~1회, saturation audit 1회다. fixed pass limit 때문에 연구가
COMPLETE인 것처럼 만들지 않고, 더 조사가 필요하면 현재 run을 diagnostic-only로 봉인해 새 blind
conversation에서 초기 품질을 다시 검증해야 한다. 따라서 R15는 score/Stage 없이
`FRESH_SESSION_DIAGNOSTIC_ONLY`로 봉인했다.

새 conversation은 새 창이나 새 탭을 뜻하지 않는다. 로그인된 기존 ChatGPT 탭을 그대로 두고 그 탭의
URL만 새 채팅으로 전환한다. 쉬운 예로 브라우저 책상은 그대로 두고 같은 책상 위의 새 빈 종이를 쓰는
것이다.

R15의 6개 genuine semantic/source defect를 원문과 verification row로 분해했다.

```text
REJECTED_WRONG_SUBJECT          4
REJECTED_SOURCE_UNAVAILABLE     2
```

wrong-subject 4개는 `issuer_scoped=false` fact가 원문에 실제로 연속 등장하지 않는 합성 subject를 쓴
사례였다. 예를 들어 source의 짧은 표현 여러 개를 합쳐 “시설+거래+당사회사” 같은 구조화 subject를
만들면 exact quote는 맞아도 후속 verifier가 그 주체 문자열을 원문에서 확인할 수 없다. unavailable 2개는
시장 데이터 canonical page가 Pro에서는 보였지만 verifier의 공개 fetch에는 HTTP 403을 반환한 사례였다.

수리는 C17·롯데케미칼·시장가격 검색어를 코드에 넣지 않고 모든 아키타입의 Initial V3와 follow-up delta
계약에 적용했다.

```text
issuer_scoped=false subject     source 원문의 가장 짧은 연속 주체 표현을 직구
여러 위치의 주체 합성           금지
material source replay          login/cookie/JS challenge 없는 공개 representation
401/403/login/anti-bot          official/filing/issuer-data/public mirror로 교체
대체 representation 없음        fact 대신 attempted route와 source gap
```

36개 canonical prompt snapshot을 모두 재생성해 critical 0 PASS를 확인했다. prompt/fresh orchestration
회귀는 Windows 75/75, Linux 75/75 PASS이며 `compileall`과 `git diff --check`도 통과했다. 정규화
영수증은 `p36_c17_r15_efficiency_failure_and_r16_prompt_guard_receipt.json`에 기록한다.

다음 R16은 이 수정 commit에 묶인 새 packet/job/run/conversation을 사용한다. 기존 R15 dossier, score,
Stage, fact checkpoint는 재사용하지 않으며, Chrome을 재시작하거나 새 window/tab을 만들지 않는다.

## P37 — C17 R16 서버 지속성 FAIL과 기존 탭 소유권 봉인

R16은 P36 commit에 묶인 새 job/run/pass와 blind packet으로 시작했다. 운영 Chrome에서 이미 열려 있던
ChatGPT page 한 개를 사용해 새 대화를 준비했고 새 browser window/tab/context는 만들지 않았다. 승인된
initial 전송은 한 번 claim됐지만, 전송 직후 공개 conversation에서 정확한 job/run marker를 찾지 못했다.

```text
job / run                     PROJOB-6ec66fa741cd95ba92bc9672 / PRORUN-9986fb0a09050c540cbbb5aa
initial pass                  PROPASS-fc5bbd72814520298efeeaf6
submit / capture              1 / 0
server persistence            false (job/run marker 2개 미확인)
durable status                USER_ATTENTION_REQUIRED
automatic resend              금지
score / Stage                 없음 / 없음
query / search                0 / 0
```

쉬운 예로 우체국 접수 버튼은 한 번 눌렀지만 서버 우편함에서 봉투의 job/run 이름표를 확인하지 못한
상태다. 이때 같은 봉투를 다시 보내면 중복 전송이 될 수 있으므로 R16은 재전송하지 않는다. 나중에 정확한
서버 turn이 확인될 때만 submitted-only 복구를 사용한다.

실패 후 read-only CDP 목록에서 운영 Chrome의 page는 8개였지만 ChatGPT page는 0개였다. 정상적인
attached-session 종료를 fixture에서 반복해도 기존 page는 닫히지 않아, 실제 탭 소실 원인은 재현하거나
단정하지 못했다. 원인 미확인을 코드 문제 없음으로 오해하지 않도록 existing-page proxy의 소유권 경계를
더 강하게 봉인했다.

```text
허용                         이미 열려 있는 ChatGPT page의 같은 탭 navigation
Browser/Page/Target close     upstream에 보내지 않고 local success로 무해화
Browser/Page crash            upstream에 보내지 않고 local success로 무해화
Target/context 생성           protocol error로 거부
ChatGPT page 없음             새 탭을 만들지 않고 fail closed
cleanup 뒤 검증               동일 URL뿐 아니라 동일 target id 유지
```

예를 들어 `/c/old`에서 `새 채팅`을 눌러 `/c/new`로 가는 것은 같은 책상에서 종이만 바꾸는 일이라
허용한다. `Target.createTarget`으로 새 책상을 들이거나 `Target.closeTarget`으로 사용자 책상을 치우는 것은
proxy 경계에서 막는다.

현재 코드의 proxy unit은 Linux 3/3 PASS다. Linux 실제 Chromium 테스트는 test body 전에
`libnspr4.so` 부재로 실행되지 않았고 assertion failure는 아니다. 동일 변경을 실제 Windows Chromium에서
검증한 targeted 회귀는 4/4, proxy+browser 전체 관련 회귀는 45/45 PASS다. 기존 page URL과 target id가
cleanup 뒤에도 같고, 같은 Worker가 그 target에 재접속한 뒤 종료해도 browser process가 살아 있음을
확인했다. `compileall`과 `git diff --check`도 PASS다.

요구사항 단위 V2 static audit은 critical 0으로 PASS다. 더 오래된 production static audit은 이번 변경과
무관한 `multi_pass/orchestrator.py`의 두 번째 guarded `submit_once` 호출을
`duplicate_submit_path_count=1`로 계속 집계해 FAIL이다. 이번 patch의 변경 경로에는 submit coordinator가
없으며 이 값을 0으로 숨기지 않았다. R16도 동일 job 자동 재전송 금지를 그대로 유지한다.

정규화 영수증은
`p37_c17_r16_persistence_failure_and_existing_tab_ownership_receipt.json`에 기록한다. runtime DB, packet
본문, browser profile, screenshot은 추적하지 않는다. 다음 단계의 선행조건은 같은 E2R Chrome 창에
로그인된 ChatGPT page 한 개가 다시 존재하는 것이다. 코드는 대체 page를 자동 생성하지 않는다. page가
존재하면 R16의 이미 보낸 turn이 늦게 지속됐는지 먼저 확인하고, R16 요청은 재전송하지 않는다.

## P38 — master goal 전수 완료 감사와 CI hard gate 복구

원본 master goal 2,669줄과 fresh-session 보조 goal 1,659줄을 현재 파일 hash 기준으로 다시 전수
검토했다. 구현 존재 여부가 아니라 각 hard gate를 증명하는 현재 leaf receipt와 runtime 상태를 대조했다.

```text
36 contract totality                 PASS / 36·36 / critical 0
Initial Prompt V3 snapshot           PASS / 36 / critical 0
generalization                       PASS / critical 0
fresh efficiency static receipt      PASS / critical 0
C06 live full thesis                 PASS / 28 terminal / 7 component / 21 Judge
C17 live full thesis                 PENDING / R16 persistence 미확인
C28 live full thesis                 PENDING / 과거 repair-heavy run 대체 필요
operational live canary              1 / required 3
OPERATIONAL_RESEARCH_READY           선언 금지
```

현재 production static audit가 `duplicate_submit_path_count=1`로 FAIL하던 원인은 실제 두 번째 submit 경로가
아니었다. ChatGPT의 움직이는 send control 때문에 production adapter가 한 번의
`send.evaluate("element => element.click()")`를 사용하는데, audit visitor는 `send.click()`만 세어 실제
dispatch 한 개를 0개로 오인했다. audit가 coordinate click과 locator-scoped native DOM click을 모두 같은
물리적 dispatch로 세도록 수정한 뒤에도 정확히 한 개만 허용한다. 두 방식을 같이 둔 fixture는 2개로
집계되므로 중복 경로를 숨기지 않는다.

```text
before guarded dispatch / critical   0 / 1
actual production dispatch           1
after guarded dispatch / critical    1 / 0
production static audit              PASS
V2 requirement static audit          PASS / critical 0
```

CI도 master goal의 입력 범위를 정확히 보지 못했다. V2.1 문서, V3 research/repair schema, dynamic Pro prompt,
V2 fixture만 변경하면 전용 workflow가 실행되지 않을 수 있었다. 이 경로들을 push/PR trigger에 추가하고,
현재 전체 unittest discovery `7,858`을 하한으로 고정했다. 삭제 test와 새 skip/xfail 금지에 더해 discovery
roster가 7,858보다 작아져도 CI가 실패한다. workflow YAML parse와 실제 floor shell은 PASS다.

현재 master 핵심 offline 묶음은 논리적 430개를 검증했다. Linux에서 427개는 PASS했고 세 browser test는
test body 전에 `libnspr4.so` 부재로 종료됐다. 같은 세 test를 Playwright가 설치된 Windows Chromium에서
실행해 3/3 PASS를 확인했으므로 코드 failure는 0이다. 최종 patch compileall·diff check·GitHub Actions는
commit/push 뒤 별도 receipt로 갱신한다.

정규화 완료 감사는
`p38_master_goal_completion_audit_and_ci_guard_receipt.json`에 기록한다. 현재 운영 Chrome의 CDP page는
10개지만 ChatGPT page는 0개다. 임의의 unrelated shopping tab을 덮어쓰거나 새 target을 만들지 않는다.
남은 실제 완료 경로는 R16 무재전송 서버 확인, C17 full thesis, 새 blind C28 full thesis, 최종 A~H·full
suite·CI green이다.

## P39 — artifact 다운로드 결박과 CI 회귀 복구

`aed9f813` head의 GitHub Actions에서 Pro-first core/browser/full-regression과 V6 offline-contract가 함께
실패했다. V6 별도 결함이 아니라 같은 artifact capture 결함이었다. 로컬 전체 7,858개에서도 정확히 네
건만 재현됐고 나머지 failure/error는 없었다.

첫 번째 원인은 파일 후보의 direct download control을 찾는 ancestor XPath가 artifact row를 벗어나
`BODY`까지 올라갈 수 있었던 점이다. 예를 들어 MD 다운로드 뒤 PDF를 고르면, 화면에 남은 MD preview의
다운로드 버튼이 `BODY` 아래 유일한 control이라는 이유만으로 PDF 후보에 다시 붙었다. 그래서 실제 클릭은
`MD → PDF`가 아니라 `MD → MD`였다. 이제 page 전체·assistant turn 전체 container는 direct binding으로
인정하지 않고, local container의 visible filename roster와 control의 `download` filename이 정확히 현재
후보 하나에 결박될 때만 direct control을 쓴다. 애매하면 현재 PDF 후보를 눌러 그 파일 preview의 다운로드
control을 찾는다.

두 번째 원인은 Chromium의 CDP `Network.responseReceived`가 실제 body 준비보다 먼저 도착할 수 있다는
순서 경쟁이었다. 이미 같은 exact URL에 대해 Playwright download/response observer를 걸어 두었으므로,
CDP가 먼저 와도 짧게 그 observer를 우선 기다린다. CDP body가 아직 없으면 새로 클릭하지 않고 같은 observer
결과만 사용한다. exact origin, sandbox basename, manifest filename/file id 검사는 낮추지 않았다.

세 번째로 canonical ResearchDossierV3 schema는 맞지만 job/run이 다른 JSON을 본 사실을 candidate loop
끝까지 보존한다. 따라서 일반 `no match`로 뭉개지 않고 exact identity mismatch로 차단한다.

```text
base full suite                    7,858 / failure 4 / error 0
targeted reproduction             4 / failure 4
targeted after repair             4 / PASS
browser adapter + capture         70 / PASS
static + submit guards            14 / PASS
master key offline bundle         430 / 430 PASS / 단일 Linux 환경
final full suite                  7,858 / failure 0 / error 0 / skip 38
production static audit           PASS / critical 0 / guarded submit 1
V2 requirement static audit       PASS / critical 0
```

P38의 Linux 427 PASS + 환경 오류 3이라는 분할 결과도 로컬 Playwright 공유 라이브러리를 보완한 뒤 같은
23-module 명령을 재실행해 430/430 단일 환경 PASS로 대체됐다. 정규화 영수증은
`p39_artifact_capture_ci_repair_and_full_regression_receipt.json`이다.

브라우저 경계는 바꾸지 않았다. E2R Chrome PID 18964는 살아 있지만 현재 page 14개 중 ChatGPT page는
0개다. Threads·Amazon·Coupang 등 사용자 page를 이동시키지 않았고, 새 window/tab도 만들지 않았다.
R16도 재전송하지 않았다. 다음 browser 단계는 기존 E2R Chrome 창에 로그인된 ChatGPT page 한 개가
존재할 때 그 동일 target만 재사용하는 것이다.

master 완료 상태는 아직 1/3 live full thesis다. C17의 R16 무재전송 복구와 C17 full thesis, 새 blind C28
full thesis가 남았으므로 `OPERATIONAL_RESEARCH_READY`는 계속 금지한다.

## P40 — Windows UTF-8 이식성 수리와 최신 Reviewer A–H 재검증

최신 `e7b650d4` head에서 Reviewer A–H를 다시 실행하던 중 Linux와 Windows가 서로 다른 실패를 보였다.
Linux Reviewer C는 Playwright headless shell의 `libnspr4/libnss3/libasound2` 공유 라이브러리가 없어 test
body 전에 종료됐고, Windows Reviewer D는 Evidence Contract JSON을 CP949로 해석하다
`UnicodeDecodeError`가 났다. Windows Reviewer H의 Git 오류는 `\\wsl.localhost` UNC 경로에서 Windows Git을
실행한 환경 경계였으므로, 저장소가 실제로 존재하는 Linux 환경에 사용자 권한 Playwright 라이브러리를
연결해 A–H를 한 환경에서 다시 검증했다.

코드 결함은 Evidence Contract V1/V2 loader가 `Path.read_text()`에 encoding을 명시하지 않은 것이었다.
Linux의 기본 UTF-8에서는 숨어 있었지만 Windows 기본 CP949에서는 한글 JSON을 읽을 수 없었다. 두 loader를
`read_text(encoding="utf-8")`로 고치고, 두 공개 loader가 어느 플랫폼에서도 UTF-8을 명시하는지 mock으로
직접 검사하는 회귀 2개를 추가했다. Reviewer D의 leaf input manifest에도 두 loader와 새 테스트를 넣어
간접 테스트만 하고 입력 hash에서 빠지는 일이 없게 했다.

```text
portable loader regression          2 / 2 PASS
Reviewer C browser/exactly-once      70 / 70 PASS
Reviewer D gap/saturation            63 / 63 PASS
changed-surface focused              91 / 91 PASS
Reviewer A~H                         PASS / A8 B13 C70 D63 E50 F62 G15 H47
review receipt hash                  ac0e3e60146c28243d98882d17dc5b7ffa74420945bcbca60532aecf1deae097
full unittest discovery              7,860 / exit 0 / failure·error 0
production static audit              PASS / critical 0 / guarded submit 1
V2 requirement static audit          PASS / critical 0
compileall / diff check              PASS / PASS
```

새 테스트 2개를 보존하도록 Pro-first CI discovery 하한도 7,858에서 7,860으로 올렸다. 과거 P38/P39의
7,858 결과는 당시 head의 사실이므로 수정하지 않는다. 정규화 영수증은
`p40_windows_utf8_portability_and_current_independent_review_receipt.json`이며, 이 patch의 GitHub Actions는
commit/push 뒤 별도로 확인한다.

R16 제출 후 복구 preflight도 다시 확인했다. durable job은 `submit_count=1`, `capture_count=0`,
`USER_ATTENTION_REQUIRED`이고, packet manifest와 Windows runtime config hash는 모두
`f079a7a459ca58e17046f1d0e566d20501ef193cef4ec9dd62ec91587f8e7a1c`로 정확히 같다. 같은 ChatGPT page가
있으면 현 CLI로 재전송 없이 복구할 수 있다. 현재 E2R Chrome은 page 12개, ChatGPT page 0개이므로 다른
Threads·쇼핑 탭을 이동시키지 않았고 새 window/tab도 만들지 않았다. live full thesis는 여전히 1/3이며,
C17과 새 blind C28이 닫히기 전 `OPERATIONAL_RESEARCH_READY`는 금지한다.

## P41 — 최신 head CI 확정과 R16 방문 기록 복구 단서

`2ba0151d` head에서 두 GitHub Actions를 다시 검산했다. Pro-first run `33311986597`과 V6 operational
cutover run `33311986620`은 모두 `SUCCESS`다. Pro-first full suite는 7,860개, failure/error 0,
기존 skip 38이며 Reviewer A~H도 `A8 B13 C70 D63 E50 F62 G15 H47`로 모두 PASS했다. V6 workflow는
Gate 1 tracked receipt 4/4와 전체 7,860개를 함께 통과했고 production static critical 합계도 0이다.
먼저 시작된 중복 run `33311984958`은 취소됐으며 완료 권한으로 세지 않는다.

R16 durable state를 실제 중앙 DB에서 다시 읽었다. 상태는 여전히 다음과 같다.

```text
job / run              PROJOB-6ec66fa741cd95ba92bc9672 / PRORUN-9986fb0a09050c540cbbb5aa
status                 USER_ATTENTION_REQUIRED
conversation           null
submit / capture       1 / 0
missing exact markers  2
automatic resend       금지
```

E2R Chrome profile의 `History`를 immutable read-only SQLite로 확인하자 R16 전송 시각에
`/c/6a940328-b848-83e8-ab85-ee7079eaeac2`가 약 0.5초 보인 뒤 다시 ChatGPT root로 이동한 기록이 있었다.
이는 복구 후보 URL이지 전송 성공 증거가 아니다. 쉬운 예로 우편함 번호표가 잠깐 보였다는 뜻일 뿐,
봉투 안에 정확한 job/run 이름표가 들어갔다는 뜻은 아니다. 기존 로그인 ChatGPT target 하나가 다시
존재할 때 이 URL의 화면에서 두 marker를 직접 확인해야만 `--resume-submitted-job-id` 경로를 사용한다.
marker가 없으면 R16을 재전송하지 않고 실패 상태를 그대로 봉인한다.

55초 동안 CDP page 목록을 감시했지만 ChatGPT page는 0개였다. 새 window/tab을 만들지 않았고,
Threads·쇼핑 등 12개 기존 page도 이동시키지 않았다. 정규화 영수증은
`p41_current_ci_and_r16_history_recovery_receipt.json`이다. master 완료 상태는 여전히 live full thesis
1/3이며 C17·C28이 실제로 닫히기 전 운영 준비 판정과 PR draft 해제·main 병합은 금지한다.
