# BrowserUse 기존 로그인 세션 인수인계 — 2026-09-25

초기 기록 시각: `2026-09-24 23:02 KST`
최종 갱신: `2026-09-25 02:24 KST`

작업 브랜치: `feature/e2r-pro-first-browser-platform-20260822`  
PR: `#7` draft 유지; 이 작업에서 merge 또는 draft 해제 금지  
이번 갱신 직전 HEAD: `81224b05826bd3be4b24510301181ad385a8dd41`

## 최신 인수인계 요약 — 2026-09-25 02:24 KST

**인증이 필요한 BrowserUse 작업은 사용자가 이미 로그인해 둔 바로 그 `extension` 세션과 기존 작업 탭에서만 한다.** 매 재개 시 `browser.user.openTabs()`로 현재 목록을 다시 확인하고, URL·계정 표시·작업 대화가 맞는 descriptor 하나를 `claimTab()`한 다음 그 반환 Tab 객체만 사용한다. 새 창·새 브라우저·새 탭·프로필·CDP attach·재로그인으로 옮기지 않는다. 새 Chat 대화가 필요하면 기존 로그인 탭 안에서만 연다. 세션/탭을 찾지 못하거나 기술 오류가 나면 새 세션으로 우회하지 말고, 기존 화면을 보존한 채 정확한 오류와 확인 범위만 기록하고 입력 전에 멈춘다. **다른 CDP 포트에서 안 보인다는 이유로 로그인 세션이 없다고 결론내리지 않는다.**

- 진행 중인 단일 live canary는 C15 `010950`, `as_of_date=2026-08-23`, job `PROJOB-df15a37c58ae7583924e58c0`; packet canonical SHA-256 `fa5845a055661c99c2ab1eb9cfb65f66fb84d2c85b267b3cde33b54843c320df`다. predecessor `PROJOB-7c02db014fefb06b1258ffe9`는 frozen/superseded이며 응답·계보를 재사용하지 않는다.
- 2026-09-25 02:21 KST경 BrowserUse `extension`의 기존 로그인 ChatGPT 탭을 다시 열거·claim한 뒤 같은 반환 Tab에서 실제 same-job 재개를 시도했다. 마지막 사후 read-only 확인에서 tab ID `1437795006`, `https://chatgpt.com/`, 계정 `대규 Pro`, 일반 `Chat`, 모델 `6 Pro`였고, composer 비어 있음, user/assistant turn `0/0`, 선택 파일 `0`이었다. 이 값은 관찰 시점 기록일 뿐 다음 재개 시 현재 화면을 다시 확인해야 한다.
- durable job은 `USER_ATTENTION_REQUIRED`, `state_version=26`, `submit_count=0`, `capture_count=0`; browser session/conversation 및 approval 값 없음, `fresh_v3_prepare_receipt.json` 없음이다. 최신 durable 오류는 `BrowserUIIncompatible: the exact BrowserUse packet file/hash was not visible in the claimed tab`이며 latest event의 `safe_unprepared_resume=false`다.
- 최신 시도는 같은 로그인 탭에서 BrowserUse filechooser 경로를 호출했으나 exact filename/canonical-hash 가시성 검증을 통과하지 못해 중단됐다. prompt 입력·send·Pro 요청·capture는 하지 않았다. 이 결과만으로 로그인 세션 문제라고 진단하지 않는다. 확인된 blocker는 **정확한 packet 파일/hash가 claimed tab에서 검증되지 않은 것**이며, 더 구체적인 원인은 미확정이다. 이 검증과 resume gate를 해결하기 전까지 같은 첨부를 재시도하지 않는다.
- 이번 시도 직전 feature HEAD `81224b05826bd3be4b24510301181ad385a8dd41`에서 PR #7은 `OPEN/DRAFT/MERGEABLE`이었다. Pro PR run [36029814504](https://github.com/Daikisong/stock_agent/actions/runs/36029814504)와 V6 PR run [36029816999](https://github.com/Daikisong/stock_agent/actions/runs/36029816999)은 `SUCCESS`; Pro push run [36029817123](https://github.com/Daikisong/stock_agent/actions/runs/36029817123)은 02:24 KST 확인 시 `in_progress`였고 `core-unit`/`static-security`는 성공, `full-regression`/`browser-mock-e2e`는 진행 중이었다. 이후 push run의 상태를 이 기록으로 추정하지 않는다.
- PR `#7`은 draft/open으로 유지하며 이 작업에서 draft 해제나 merge를 하지 않는다.

이 요약은 아래 상세 타임라인에서 이전 상태를 덮어쓴다. 특히 과거의 “첨부 메뉴가 펼쳐져 있음”, `state_version=24`, `No Chrome-owned Open dialog appeared`는 현재 상태가 아니다. 최신 확인은 exact packet filename/hash 검증 실패 뒤 composer와 선택 파일이 비어 있었고, 요청은 전송되지 않았다는 것이다.

## 핵심 원칙 — 로그인 작업은 사용자가 이미 로그인한 세션에서

인증이 필요한 ChatGPT Pro 작업의 유일한 기본 경로는 사용자가 이미 로그인해 둔 Chrome의 **BrowserUse `extension` 세션과 기존 작업 탭**이다. 설정 파일이나 machine preflight 성공만으로 연결됐다고 보지 말고, 활성 BrowserUse 도구에서 실제 extension 연결과 대상 탭을 확인한다.

매 실행·재개 때 아래 순서를 지킨다.

1. 현재 Codex 세션에서 BrowserUse `extension` browser를 얻고 `browser.user.openTabs()`로 현재 탭을 다시 열거한다.
2. `https://chatgpt.com/`, 로그인 계정 표시, 대화/작업 내용을 대조해 대상 descriptor 하나를 특정한다. 저장된 tab ID는 다음 실행 때 유효하다고 가정하지 않는다.
3. 그 descriptor를 `browser.user.claimTab()`에 넘기고, 이후에는 **claim이 반환한 동일 Tab 객체만** 사용한다.
4. 읽기·첨부·입력·전송 직전 URL/대화, 실제 Chat/Pro 선택, 기존 초안·응답·파일 상태를 확인한다. 새 대화가 필요해도 기존 로그인 탭 안에서만 시작한다.
5. 연결·탭 확인·화면 상태가 예상과 다르면 사용자의 세션과 화면을 보존하고, 실제 오류 및 확인 범위를 적은 뒤 입력 전에 멈춘다. 새 창이나 별도 세션으로 재시도하지 않는다.

금지 대체 경로: 새 창·새 브라우저·새 탭·새/임시 프로필·헤드리스 브라우저·별도 CDP attach·재로그인·쿠키 복사·전역 키 입력. 다른 CDP endpoint나 `browser.tabs.list()`에 사용자의 탭이 없다는 사실만으로 로그아웃 또는 세션 만료라고 결론내리지 않는다. 기술 연결 오류는 기술 오류로 기록한다. 종료·보류할 때 사용자의 기존 창·탭·로그인을 닫거나 초기화하지 않는다.

쉬운 예: 로그인된 기존 탭 A에서 Pro 자료를 받아야 하면 A를 현재 목록에서 다시 찾아 claim하고 A에서만 진행한다. A가 목록에 없거나 claim이 실패하면 새 Chrome B를 열어 로그인시키지 말고, 오류와 확인 범위를 남긴 뒤 멈춘다. “새 Chat”은 같은 탭 안의 새 대화이며, 새 브라우저 세션이 아니다.

## 이번 시도 식별자와 실제 상태

| 항목 | 확인값 |
| --- | --- |
| 목적 | `010950`, `as_of_date=2026-08-23`, `C15` fresh-session initial canary |
| 현재 job | `PROJOB-df15a37c58ae7583924e58c0` |
| fresh session | `FRESH-V2-1-C15-R6-20260907T212025Z` |
| packet SHA-256 | `fa5845a055661c99c2ab1eb9cfb65f66fb84d2c85b267b3cde33b54843c320df` |
| 기존 로그인 탭 | 마지막으로 관찰한 BrowserUse tab ID `1437795006`; 작업 재개 전 반드시 현재 목록에서 다시 확인하고 새로 claim할 것 |
| 마지막 사후 read-only 탭 확인 | 2026-09-25 02:21 KST경 `1437795006`; `https://chatgpt.com/`, `대규 Pro`, `Chat`/`6 Pro`; composer 비어 있음, user/assistant turn `0/0`, 선택 파일 `0`. 다음 실행 전에 반드시 재확인 |
| 첨부 검증 | BrowserUse filechooser를 호출했으나 exact filename/canonical packet hash가 claimed tab에서 확인되지 않아 실패; 검증된 첨부로 인정하지 않음 |
| 실제 전송 | **미전송** — prompt 입력, send, Pro 연구 요청, capture 없음 |
| durable 상태 | `USER_ATTENTION_REQUIRED`, `state_version=26`; `submit_count=0`, `capture_count=0`, browser/conversation/approval binding 및 prepare receipt 없음; `safe_unprepared_resume=false` |
| 이전 job | `PROJOB-7c02db014fefb06b1258ffe9`는 frozen/superseded. 과거 응답을 새 job에 재사용하거나 이전 대화를 추가 follow-up 하지 말 것 |

위 tab ID는 이전 관찰의 인수인계용 식별자일 뿐, 다음 시도의 권한이나 현재 탭 존재를 보장하지 않는다. 재개할 때 현재 BrowserUse 탭을 다시 열거하고 동일 로그인 작업 탭을 직접 확인해야 한다. 인증 토큰·쿠키는 문서화하지 않는다.

## 2026-09-25 02:21 KST: 기존 로그인 탭에서 same-job packet 검증 실패

- 기존 BrowserUse `extension` 세션에서 `openTabs()`로 ChatGPT 탭을 다시 찾고, 정확한 descriptor를 claim한 뒤 claim이 반환한 같은 Tab 객체로만 작업했다. 새 브라우저/창/탭/프로필/CDP/재로그인은 사용하지 않았다. 사후 read-only 확인에서도 해당 탭은 로그인된 `Chat`/`6 Pro` 홈 화면이었다.
- 정확한 C15 R6 job `PROJOB-df15a37c58ae7583924e58c0`과 packet hash `fa5845a055661c99c2ab1eb9cfb65f66fb84d2c85b267b3cde33b54843c320df`를 사용했다. read-only same-job recovery proof는 통과해 state v24에서 `BROWSER_PREPARING` v25로 진행했지만, BrowserUse filechooser 이후 claimed tab에서 exact packet file/hash 확인이 실패해 `USER_ATTENTION_REQUIRED` v26으로 돌아갔다.
- 오류는 `BrowserUIIncompatible: the exact BrowserUse packet file/hash was not visible in the claimed tab`이다. 최신 event payload는 `preparation_failure_stage=DRAFT_PREPARATION_OR_UNKNOWN`, `safe_unprepared_resume=false`, `submit_count=0`으로 fail-closed했다. DB read-only 재조회에서 `capture_count=0`, browser/conversation binding 없음, prepare receipt 없음도 확인했다.
- 실패 뒤 같은 기존 탭을 read-only로 확인했을 때 URL은 `https://chatgpt.com/`, 로그인 계정 표시는 `대규 Pro`, `Chat` 및 `6 Pro` 선택, composer 비어 있음, user/assistant turn `0/0`, 선택 파일 `0`이었다. Browser console error/warn 목록은 비어 있었고 CDP capability는 `Capability is not available: cdp`였다. 이는 이 탭에서 CDP capability가 없다는 기술 한계이며 세션 로그인 실패나 정책 거절을 뜻하지 않는다.
- 첨부 UI 경로는 시도됐지만 exact file/hash가 확인되지 않았으므로 **packet 첨부 성공으로 판정하지 않는다.** prompt 입력·send·Pro 요청·capture·새 job/pass, 검색/fetch, 다른 archetype 실행, score/Stage 변경은 없었다. 재개 전에 파일 선택 후 DOM `File`의 실제 name/content/hash가 왜 불일치했는지 코드/mock 경계에서 진단하고 회귀시험을 추가한다. 동일 job의 `safe_unprepared_resume=false`를 우회하거나 blind retry하지 않는다.
- 다음 실행의 첫 단계는 current `extension` tab 목록과 durable job을 각각 다시 read-only 확인하는 것이다. 과거 tab ID나 아래의 historical UI 상태를 현재 상태로 간주하지 않는다. 로그인 탭이 목록에 없거나 정확한 대상을 claim하지 못하면 새 창/세션을 열지 않고 오류를 기록한 뒤 멈춘다.

## 이전 chooser 실패와 당시 진단 — P98의 최신 실패와 구분

실제 오류:

```text
BRIDGE_OPERATION_FAILED: existing Chrome file chooser did not select the packet
(phase=dialog_not_found; exit=1;
error_id=No Chrome-owned Open dialog appeared;
no global keystrokes were sent)
```

2026-09-24 시점의 초진은 `attachPacket()`이 첨부 메뉴 단계를 놓쳤을 가능성에 초점을 뒀다. 그 뒤 installed extension API를 확인해 더 직접적인 불일치를 찾았다. bridge가 BrowserUse `filechooser` handle 대신 Windows Chrome-owned `Open` 창만 기다렸던 것이다. 따라서 이 절의 과거 메뉴 전이 가설은 원인 판정으로 사용하지 말고 아래 P96 기록을 따른다.

같은 세션에서 수행한 추가 관찰:

- `tab.dev.logs({levels:["error","warn","warning"], limit:200})`는 빈 결과였다.
- 해당 탭의 CDP 요청은 실제 오류 `Capability is not available: cdp`를 반환했다. 이는 기술 capability 부재이며 정책 거절이나 로그인 세션 부재가 아니다.
- 다른 탭·브라우저를 열거나 전역 키 입력을 보내지 않았다.
- 기존 화면은 보존했다. 메뉴가 이미 expanded일 수 있으므로 다음 시도에서 첨부 버튼을 무조건 다시 누르지 않는다.

## 초기 코드 수정 및 검증 상태 — 이후 P96 수정으로 대체됨

이번 수정에서 첨부 버튼을 누른 뒤 메뉴 단계를 건너뛰던 경로를 상태 인식형으로 바꿨다. `aria-expanded=true`이면 버튼을 다시 누르지 않고 보이는 일반 파일 업로드 항목을 고른다. 접혀 있으면 한 번 열고 항목을 찾는다. 열린 메뉴에 인식 가능한 업로드 항목이 없으면 파일 선택 단계로 넘어가지 않고 fail closed한다. 메뉴가 열리지 않는 UI 변형만 기존 direct native chooser 경로를 허용한다. 업로드 뒤의 filename·exact packet hash 확인은 유지했다.

당시 로컬 검증은 BrowserUse extension bridge 관련 단위/통합시험 `14/14 PASS`, V2 static audit `2/2 PASS`, `node --check` 및 `git diff --check` PASS였다. 두 Playwright/Chromium 기반 suite는 당시 WSL에서 `libnspr4.so` 누락으로 시작하지 못했다. 이는 제품 assertion 실패가 아니었다. 이 수치는 과거 revision 기록이며 현재 filechooser patch 검증은 상단 P96 요약을 따른다.

### 2026-09-24 23:02 KST: 기존 탭 재확인과 UI 문구 보정

수정 전 커밋 `33f94af21c7866eaa47cad8e3818ab64d2142393`의 Pro CI `36006574739`와 V6 CI `36006574637`는 모두 SUCCESS였다. 그 뒤 **같은 로그인 탭** `1437795006`을 BrowserUse extension의 `openTabs()` 결과에서 다시 찾고 claim하여 읽기 전용 확인했다.

```text
URL               https://chatgpt.com/
계정 표시          대규 Pro
모드               Chat 선택 / Work 미선택 / 6 Pro 표시
composer           길이 0
user turn          0
선택된 파일         0
첨부 메뉴           이미 펼쳐져 있음
전송               없음
```

캡처와 DOM에서 실제 업로드 선택 행은 ARIA `menuitem`이나 `button`이 아니라 `[role="group"]` 안의 `div[tabindex="0"]`였으며, 실제 Korean UI text는 `사진 및 파일 추가` / `컴퓨터에서 업로드하세요`였다. 따라서 이전 코드의 일반 `Upload file`/`파일 업로드` selector는 현재 화면의 항목을 찾지 못할 수 있다. 이를 바탕으로 generic selector `div[tabindex="0"]` + `사진 및 파일 추가`를 추가하고 회귀시험에 고정했다. 동일 claimed tab에서 read-only locator 확인 결과 selector count `1`, text `사진 및 파일 추가\n컴퓨터에서 업로드하세요`, `tabindex=0`이었다. 이 확인은 클릭하지 않고 끝냈다.

이번 재확인에서도 항목을 클릭하지 않았다. 파일 첨부·prompt 입력·전송 모두 0건이며, 이전 job은 여전히 `USER_ATTENTION_REQUIRED / submit_count=0` 상태다. 현재 변경은 새 코드이므로 새 commit의 PR CI가 통과하기 전에는 live canary를 재개하지 않는다.

## 당시 다음 단계 (2026-09-24 23:02 기준; 아래 최신 기록으로 대체)

1. 변경을 한글 커밋으로 현재 PR 브랜치에 푸시하고 해당 head의 필수 CI를 확인한다.
2. 실제 시도를 재개할 때 BrowserUse의 기존 로그인 세션에서 현재 탭을 다시 열거·claim하고, composer가 비어 있고 응답/첨부가 없는지 확인한다. 이 확인 전에는 과거 tab ID만 믿고 조작하지 않는다.
3. 검증된 코드가 같은 claimed tab에서 파일 메뉴를 선택하고 native chooser를 띄운 뒤, filename과 exact packet hash를 모두 확인할 때까지 prompt 입력·전송하지 않는다. 실패하면 해당 오류와 실제 전송 여부를 다시 기록하고 그 탭을 보존한다.

새 자료 수집, 추가 fetch, 다른 아키타입 실행, 점수 변경은 이 수리 범위에 포함되지 않는다.

## 2026-09-24 23:42 KST: 동일 로그인 세션 재확인과 재개 기준

사용자의 재요청에 따라 BrowserUse는 **사용자가 이미 로그인한 세션에서만** 사용한다. 같은 사이트의 다른 Chrome, 새 창, 새 프로필, 새 로그인, CDP 연결을 대체 경로로 만들지 않는다. 새 연구 대화가 필요하면 같은 로그인 탭 안에서만 만든다. 다음 실행자도 과거 tab ID를 권한처럼 재사용하지 말고, `browser.user.openTabs()`에서 현재 탭을 다시 찾은 뒤 그 반환 객체를 claim해야 한다.

2026-09-24 23:42 KST에 현재 BrowserUse extension 세션에서 읽기 전용으로 재확인한 내용:

| 확인 | 결과 |
| --- | --- |
| 기존 ChatGPT 탭 | tab ID `1437795006`, `https://chatgpt.com/`; 현재 목록에서 다시 찾아 정확한 탭 객체를 claim |
| 로그인/모드 | 계정 표시 `대규 Pro`; `Chat` 선택, 화면상 모델 `6 Pro` |
| 새 대화 상태 | 대화 route가 없는 홈 화면; composer 비어 있음, 보이는 user turn `0` |
| 첨부 | file input 선택 파일 `0`; 이 확인 과정에서 업로드 메뉴 클릭이나 파일 선택은 하지 않음 |
| 전송 | 이번 확인 중 입력·전송·새 탭 생성 없음 |
| 다른 탭 | 별도 Google 검색 탭이 목록에 있었으나 열거나 조작하지 않음 |
| BrowserUse 사전검사 | WSL preflight exit `0`; extension runtime과 기존 `node_repl` 세션 사용 가능 |

Durable ledger는 **읽기 전용**으로 확인했다. `PROJOB-df15a37c58ae7583924e58c0`은 `USER_ATTENTION_REQUIRED`, `state_version=22`, `submit_count=0`, `capture_count=0`, browser session/conversation 없음이다. packet hash는 `fa5845a055661c99c2ab1eb9cfb65f66fb84d2c85b267b3cde33b54843c320df`다. 마지막 실패는 `dialog_not_found` native chooser 선택 실패이고, 해당 attention event에는 `safe_unprepared_resume=false`가 기록되어 있다. 현재 코드가 이 예외를 허용하는 것은 이 정확한 오류·동일 job만 대상으로 한 뒤 같은 로그인 탭에서 수행하는 별도 read-only 복구 검증이 성공해야만 다음 단계로 가도록 제한했기 때문이다. 그 검증에서 URL/새 대화 경로, 로그인, 실제 Pro 모드, 빈 composer, user turn 0, chooser 닫힘, packet hash 및 durable job 불변성을 모두 확인하지 못하면 즉시 멈춘다. 이전 predecessor job `PROJOB-7c02db014fefb06b1258ffe9`는 계속 frozen/superseded이며 재사용하지 않는다.

재개 시에는 `startBrowserUseExtensionBridge({tab: claimedExistingTab, jobId: exactJobId})`로 **이 claim된 BrowserUse 탭**에 bridge를 묶고, in-memory config에서만 `BrowserConnectionMode.BROWSER_USE_EXTENSION`을 지정한다. 이후 기존 `resume_unprepared_attention_job_id` 경로를 이용한다. 수동으로 UI를 따로 조작하거나 별도 세션에서 첨부/전송하지 않는다. 안전 검증 뒤에도 패킷 파일명과 SHA-256이 정확히 일치하는지 파이프라인이 확인하기 전에는 prompt를 채우지 않는다. 사용자의 앞선 명시적 승인은 이 단일 C15 initial canary 전송에만 적용하며, 추가 검색·다른 archetype·점수 변경 권한으로 확대 해석하지 않는다.

### 당시 코드/CI 체크포인트 (2026-09-24 23:42 기록; 최신 head 상태는 상단 요약 참조)

- PR `#7`은 `draft/open/mergeable`, head `30fd11a1440d48a22d07cf3b30f6f4459a455ad8`; merge 또는 draft 해제 금지.
- 해당 SHA의 Pro push run `36010216991`과 V6 PR run `36010223818`은 `SUCCESS`다. Pro PR run `36010223810`은 마지막 확인 시 `in_progress`였으므로 이 문서 시점에 전체 PR CI green이라고 주장하지 않는다. NSLAB 선택 workflow 두 건은 `skipped`다.
- 로컬 브랜치를 `origin/feature/e2r-pro-first-browser-platform-20260822`와 fetch로 동기화했으며, 이번 문서 보강 전 worktree는 clean이었다.

다음 단계는 동일 탭에서 위 복구 preflight와 exact packet attach를 실행하고, 전송/수신 여부와 최종 durable 상태를 다시 기록하는 것이다. 새 창·새 프로필을 열어서 해결하려 하지 않는다.

## 2026-09-24 23:53 KST: 복구 gate의 오류문구 결함

재개 시도는 브라우저 준비 단계에 도달하기 전에 `_load_unprepared_attention_job()`에서 멈췄다. 원인은 job 데이터나 로그인 탭이 아니라, 기존 chooser 오류의 `error_id`에 들어 있던 `; no global keystrokes were sent` 구분자를 native chooser 실패 regex가 허용하지 않은 것이다. 실제 오류는 `dialog_not_found`였고 “Chrome Open dialog가 나타나지 않았으며 전역 키 입력을 보내지 않았다”고 명시했지만, 코드의 형식검사가 이를 safe exact failure로 인식하지 못했다.

수정은 좁게 제한했다. `_STRUCTURED_NATIVE_FILE_CHOOSER_FAILURE`가 error id 안의 정확한 문구 `; no global keystrokes were sent`만 추가로 허용하도록 하고, 이 실제 오류문구로 동일 unsent job이 read-only 복구 gate에 들어가는 회귀시험을 추가했다. 유사하지만 exact match가 아닌 오류는 계속 차단한다. 관련 native chooser/resume 회귀시험 `5/5 PASS`, `git diff --check` PASS.

차단 당시에도 기존 job은 `USER_ATTENTION_REQUIRED / state_version=22 / submit_count=0 / capture_count=0`이었다. 오류 gate가 browser worker보다 앞에서 실패했으므로 이 재시도에서는 BrowserUse page RPC, file upload, composer 입력, 전송이 하나도 일어나지 않았다. 시도용 bridge를 종료했고 기존 로그인 탭 `1437795006`은 보존했다. 이 코드 수정의 새 head CI가 확인되기 전에는 live resume를 다시 시작하지 않는다.

## 2026-09-25 00:45 KST: 최신 head 확인 후 동일 세션 재개 결과

### 코드와 workflow

복구 regex 수정은 한글 commit `0d35d5e143327b0fc6788a61aa203074e5d62fee` (`chooser 오류 상세문구 복구검사 보완`)에 반영됐다. 해당 Pro push run `36016191427`은 마지막 확인 시 `SUCCESS`(4/4 jobs)였다. PR Pro run `36016196506`은 그 확인 시점에 대기 중이었으므로 “PR 필수 workflow 전체가 green”이라고 확대하지 않는다. CI 성공은 그 revision의 정적/테스트 검증이며 native chooser 실사용 성공을 뜻하지 않는다.

### 실행 연결 실수와 정정

첫 복구 연결은 `bridge.runUntil()`을 한 `mcp__node_repl__js` 호출에서 분리해 둔 채, worker를 다른 shell/호출에서 실행하여 `node_repl exec context not found`로 실패했다. 이는 로그인 세션/탭 문제나 ChatGPT 응답이 아니라, 같은 Node REPL 실행 문맥에 묶여야 하는 bridge와 worker를 다른 호출로 나눈 실행 실수였다. 이 실패에서는 BrowserUse UI 조작, 첨부, 입력, 전송이 일어나지 않았다.

정정 후 bridge 준비와 WSL worker 실행을 **하나의 활성 `mcp__node_repl__js` 호출 안에서** 시작하고, 같은 호출에서 `await bridge.runUntil(workerClosePromise)`로 기다렸다. 이 방식으로 이전 context 오류는 사라졌고 같은 job은 read-only preflight를 지나 `USER_ATTENTION_REQUIRED v22 → BROWSER_PREPARING v23`으로 갔다.

### 기존 탭에서 실제로 확인한 결과

worker 직전 기존 BrowserUse `extension` 세션의 현재 탭 목록을 다시 열거하고, `https://chatgpt.com/`의 탭 ID `1437795006`을 직접 확인해 claim했다. 읽기 전용 preflight는 기존 로그인 계정 `대규 Pro`, 일반 `Chat`, 실제 모델 표시 `6 Pro`, 빈 composer 및 대화/첨부 없음이었다. 새 창·새 프로필·CDP·재로그인은 사용하지 않았다.

실패 지점은 packet 첨부의 Chrome-native 파일 chooser 대기였다. 정확한 오류:

```text
BRIDGE_OPERATION_FAILED: existing Chrome file chooser did not select the packet
(phase=dialog_not_found; exit=1;
error_id=No Chrome-owned Open dialog appeared;
no global keystrokes were sent;
category=OperationStopped;
message=No Chrome-owned Open dialog appeared; no global keystrokes were sent)
```

즉 worker가 첨부 단계까지 도달했지만 Chrome 소유 `Open` 창이 나타나지 않아 path 선택/packet hash 검증을 하지 못했고 fail-closed로 종료됐다. 이 관찰만으로 클릭이 ChatGPT 메뉴를 열지 못했는지, native chooser 전이가 일어나지 않았는지까지 확정하지 않는다. 원인은 아직 해결되지 않은 기술 문제다. 전역 키 입력은 보내지 않았다.

실패 직후 같은 탭을 읽기 전용으로 확인했다: ChatGPT composer 길이 `0`, user turn `0`, file input 5개 모두 선택 파일 `0`. Windows 창 목록 검사에서도 Open 창 및 Chrome 소유 chooser `0`이었다. 기존 탭을 닫거나 초기화하지 않았다. 별도 Google 검색 탭은 열거나 조작하지 않았다.

### Durable 상태와 전송 여부

실행 뒤 SQLite ledger를 `mode=ro` 및 `PRAGMA query_only=ON`으로 읽었다. `PROJOB-df15a37c58ae7583924e58c0`은 `USER_ATTENTION_REQUIRED`, `state_version=24`, `submit_count=0`, `capture_count=0`이다. Browser session/conversation 및 approval 값은 비어 있고, `fresh_v3_prepare_receipt.json`과 BrowserUse private handoff도 없다.

```text
packet 선택/첨부       미완료
prompt 입력            없음
ChatGPT 전송           없음 (submit_count=0)
응답 capture           없음 (capture_count=0)
점수/Stage 변경        없음
```

그러므로 이번 실행은 Pro 요청을 전송한 것이 아니다. 사용자의 기존 로그인 세션을 이용해 업로드 단계에 접근했지만, 파일 chooser가 열리지 않아 전송 전 중단한 것이다.

### 다음 안전 단계

1. 현재 탭과 ledger를 읽기 전용으로 다시 확인한 뒤, 같은 로그인 탭의 첨부 UI 상태 및 `attachPacket()` → visible upload row → native chooser 전이를 계측한다. 이전 tab ID만 믿거나 UI를 무조건 다시 클릭하지 않는다.
2. 재시도는 현재 탭을 다시 열거·claim한 후 동일 job의 safe resume gate를 통과하고, bridge와 worker를 단일 활성 `mcp__node_repl__js` 실행 문맥 안에서 구동할 수 있을 때만 한다.
3. Chrome-owned chooser가 실제 나타나고 선택 packet의 파일명·SHA-256을 검증하기 전에는 composer 입력이나 전송을 하지 않는다. chooser가 다시 없으면 정확한 오류와 `submit_count/capture_count`를 기록하고 즉시 중단한다.

새 창, 새 브라우저 세션, CDP 대체, 재로그인, 전역 키 입력으로 이 문제를 우회하지 않는다. 인증된 브라우저 작업이 필요하면 오직 사용자의 **이미 로그인된 기존 BrowserUse 세션과 확인된 기존 탭**을 쓴다.

## P96 — 기존 로그인 탭 유지와 BrowserUse filechooser 연결 수정 (2026-09-25 01:17 KST)

사용자가 다시 명시한 운영 요구는 “로그인이 필요한 BrowserUse 작업은 로그인되어 있는 바로 그 세션에서 진행”이다. 다음 작업자는 문서상의 tab ID를 그대로 쓰지 말고 현재 BrowserUse `extension` session에서 `browser.user.openTabs()`를 다시 호출해 작업 탭을 찾고, 반환 descriptor를 `claimTab()`한 후 **그 claim이 반환한 동일 Tab 객체**로만 진행한다. 세션 연결이나 탭 일치가 실패하면 기존 창을 그대로 둔 채 실제 오류를 기록하고 멈춘다. 새 브라우저·탭·프로필·CDP·로그인으로 옮기거나 사용자에게 다시 로그인하라고 하지 않는다. 새 대화가 필요한 경우에도 기존 로그인 탭 내부에서만 시작한다.

### 기술 원인 정정

앞선 `dialog_not_found`는 `https://chatgpt.com/` 로그인이 풀렸다는 증거가 아니다. installed Chrome plugin source와 현재 extension tab API를 확인한 결과 `tab.playwright.waitForEvent("filechooser")` 및 반환 `FileChooser.setFiles(path)`를 쓸 수 있었다. bridge의 과거 경로는 visible attach control/menu 이후 Windows Chrome-owned `Open` dialog만 기다렸기 때문에, BrowserUse가 제공하는 filechooser handle과 연결되지 않았다. 즉 실패는 **같은 로그인 탭은 살아 있었지만 첨부 chooser backend를 잘못 골랐던 bridge/API mismatch**로 기록한다.

### 코드 수정과 경계

- visible 첨부 버튼이 in-page menu를 여는 경우, menu toggle 전에 filechooser event를 기다리며 방치하지 않는다. 메뉴의 일반 파일 업로드 행을 찾은 뒤 **그 visible row click 직전** `waitForEvent("filechooser")`를 arm하고, 반환된 BrowserUse handle에 `setFiles(exact_packet_path)`를 호출한다.
- 메뉴가 아닌 UI가 attach click에서 곧바로 chooser를 여는 경우는 그 attach click 직전에 event를 arm한다. filechooser API가 없는 구형 extension에만 Windows dialog fallback을 쓰며 이 watcher 역시 triggering click 전에 arm한다.
- Python downstream은 기존처럼 화면 파일명과 browser-selected `File`의 canonical hash를 durable packet hash와 대조한다. 정확히 일치하기 전 prompt를 채우거나 보내지 않는다. event timeout·미확인 chooser·hash mismatch는 모두 실패로 남고 자동 전송하지 않는다.
- Windows path에서 Linux `path.basename()`이 파일명 대신 드라이브 경로 전체를 돌려줄 수 있어 cross-platform basename과 `path.win32.extname()` 검증을 추가했다.
- same-job read-only recovery gate는 정확히 확인된 BrowserUse filechooser timeout 오류만 허용하고, 문구가 조금이라도 다른 오류는 계속 차단한다.

### 확인 결과와 현재 상태

- 수정 검증: 관련 두 unittest module `111/111 PASS`; `PYTHONPATH=src python -m e2r.cli.audit_e2r_pro_first_v2 --repo-root .` `PASS`, critical `0`; `node --check`, `compileall`, `git diff --check` PASS.
- 로컬 수정 직전의 commit `4aca6686aa7155fcaedcaef90d3ff83f55b4586a`에서 Pro Actions [36022829567](https://github.com/Daikisong/stock_agent/actions/runs/36022829567)은 2026-09-25 01:17 KST 확인 시 `in_progress`(세 job SUCCESS, `full-regression` reviewer gate 진행 중), V6 [36022834278](https://github.com/Daikisong/stock_agent/actions/runs/36022834278)은 SUCCESS였다. **P96 수정 diff는 아직 commit/push 및 exact-head CI 검증 전이다.**
- 기존 탭에서 attach menu를 열었다가 다시 닫는 가시 UI 점검을 했지만 file chooser event 실 attach는 아직 시도하지 않았다. 같은 C15 job은 마지막 read-only DB snapshot에서 `USER_ATTENTION_REQUIRED`, version `24`, submit/capture `0/0`, conversation/session/approval 없음, prepare receipt 없음이다. packet hash는 `fa5845a055661c99c2ab1eb9cfb65f66fb84d2c85b267b3cde33b54843c320df`다.
- 결과: packet upload `0`, prompt input `0`, send `0`, capture `0`, score/Stage 변경 `0`. 이 작업은 성공 canary가 아니라 첨부 경로 코드 수정이다. 새 query/fetch, 새 job, 새 pass, 다른 archetype 실행도 하지 않았다.

### 다음 한 단계

현재 feature worktree의 변경을 한글 commit/push하고 그 정확한 head의 필수 Pro/V6 Actions를 확인한다. exact-head CI green이 확인되면 same-job durable state를 read-only로 재확인하고, 그때도 **사용자의 기존 BrowserUse 로그인 세션에서 현재 탭을 다시 열거·claim한 다음** filechooser 경로를 검증한다. 다른 창이나 세션은 열지 않는다. CI가 pending/fail이거나 같은 탭을 확실히 claim할 수 없으면 첨부/입력 전에 멈춘다.
