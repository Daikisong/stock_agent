# BrowserUse 기존 로그인 세션 인수인계 — 2026-09-24

기록 시각: `2026-09-24 22:26 KST`

작업 브랜치: `feature/e2r-pro-first-browser-platform-20260822`  
PR: `#7` draft 유지; 이 작업에서 merge 또는 draft 해제 금지  
수정 전 HEAD: `1bcd33033390fab8403db8b4efa7ac442bf30bee`

## 핵심 원칙

로그인이 필요한 ChatGPT Pro 작업은 사용자가 이미 로그인해 둔 Chrome의 **기존 BrowserUse extension 세션과 기존 작업 탭**에서만 한다. 새 창·새 프로필·임시/헤드리스 브라우저·CDP로 대체하지 않는다. 로그인 세션을 다시 만들거나 재로그인시키지 않는다.

실행 전에는 현재 Codex 세션의 BrowserUse 도구를 통해 `extension` browser를 얻고 `browser.user.openTabs()`로 사용자의 탭을 열거한다. 대상 ChatGPT 탭을 URL·계정·작업 대화로 확인한 뒤 반환된 그 탭 객체를 `browser.user.claimTab(tab)`으로 결박한다. 이후 탐색·첨부·전송·결과 확인은 동일한 claimed tab 객체만 쓴다. `browser.tabs.list()`에 탭이 없거나 다른 CDP 포트에서 발견되지 않는다는 사실은 사용자 세션이 없다는 증거가 아니다.

새 연구 대화가 필요해도 같은 로그인 탭 안에서만 만든다. 전송 직전 tab, URL/대화, 일반 Chat 모드, 실제 `Pro` 선택, 초안·첨부 상태를 다시 확인한다. 화면이 예상과 다르면 변경을 중단하고 읽기 전용으로 조사한다. 종료·보류 시 사용자의 창·탭·로그인을 닫거나 초기화하지 않는다.

쉬운 예: ChatGPT에 로그인된 기존 탭 A에서 자료를 받아야 하면 탭 A를 BrowserUse로 claim해 그 안에서 받는다. 탭 A를 찾지 못하면 새 Chrome B를 열어 로그인을 요청하지 않고, BrowserUse 연결/탭 확인 오류를 기록한 뒤 멈춘다.

## 이번 시도 식별자와 실제 상태

| 항목 | 확인값 |
| --- | --- |
| 목적 | `010950`, `as_of_date=2026-08-23`, `C15` fresh-session initial canary |
| 현재 job | `PROJOB-df15a37c58ae7583924e58c0` |
| fresh session | `FRESH-V2-1-C15-R6-20260907T212025Z` |
| packet SHA-256 | `fa5845a055661c99c2ab1eb9cfb65f66fb84d2c85b267b3cde33b54843c320df` |
| 기존 로그인 탭 | 마지막으로 관찰한 BrowserUse tab ID `1437795006`; 작업 재개 전 반드시 현재 목록에서 다시 확인하고 새로 claim할 것 |
| 당시 탭 상태 | `https://chatgpt.com/`, 로그인 프로필 `대구 Pro`, 일반 `Chat` 선택, 실제 모델 `6 Pro`; composer 비어 있음, user turn 0, 첨부 파일 0 |
| 마지막 UI 상태 | `파일 등 추가` 버튼 `aria-expanded=true`; 첨부 메뉴를 연 상태였고 Chrome 파일 열기 창은 없었음 |
| 실제 전송 | **미전송** — packet 첨부 실패 전에 멈춤. prompt 입력·send·Pro 연구 요청 없음 |
| durable 상태 | `USER_ATTENTION_REQUIRED`; `submit_count=0`, capture 0, pass/approval/prepare receipt 없음 |
| 이전 job | `PROJOB-7c02db014fefb06b1258ffe9`는 frozen/superseded. 과거 응답을 새 job에 재사용하거나 이전 대화를 추가 follow-up 하지 말 것 |

위 tab ID는 이전 관찰의 인수인계용 식별자일 뿐, 다음 시도의 권한이나 현재 탭 존재를 보장하지 않는다. 재개할 때 현재 BrowserUse 탭을 다시 열거하고 동일 로그인 작업 탭을 직접 확인해야 한다. 인증 토큰·쿠키는 문서화하지 않는다.

## 실패 원인과 코드 경로

실제 오류:

```text
BRIDGE_OPERATION_FAILED: existing Chrome file chooser did not select the packet
(phase=dialog_not_found; exit=1;
error_id=No Chrome-owned Open dialog appeared;
no global keystrokes were sent)
```

`src/e2r/pro_first/browser/browseruse_extension_bridge.mjs`의 `attachPacket()`은 현재 보이는 첨부 버튼을 클릭한 직후 Windows의 Chrome-owned `Open` 창만 기다린다. ChatGPT의 `파일 등 추가`는 먼저 웹페이지 안의 첨부 메뉴를 여는 버튼인데, 이 흐름은 메뉴에서 실제 업로드 항목을 선택하지 않고 native file chooser 대기로 넘어갔다. 따라서 클릭이 무조건 실패한 것이 아니라, **웹 메뉴 단계와 Windows 파일 선택 단계 사이의 전이가 빠진 것**이 원인이다.

같은 세션에서 수행한 추가 관찰:

- `tab.dev.logs({levels:["error","warn","warning"], limit:200})`는 빈 결과였다.
- 해당 탭의 CDP 요청은 실제 오류 `Capability is not available: cdp`를 반환했다. 이는 기술 capability 부재이며 정책 거절이나 로그인 세션 부재가 아니다.
- 다른 탭·브라우저를 열거나 전역 키 입력을 보내지 않았다.
- 기존 화면은 보존했다. 메뉴가 이미 expanded일 수 있으므로 다음 시도에서 첨부 버튼을 무조건 다시 누르지 않는다.

## 코드 수정 및 검증 상태

이번 수정에서 첨부 버튼을 누른 뒤 메뉴 단계를 건너뛰던 경로를 상태 인식형으로 바꿨다. `aria-expanded=true`이면 버튼을 다시 누르지 않고 보이는 일반 파일 업로드 항목을 고른다. 접혀 있으면 한 번 열고 항목을 찾는다. 열린 메뉴에 인식 가능한 업로드 항목이 없으면 파일 선택 단계로 넘어가지 않고 fail closed한다. 메뉴가 열리지 않는 UI 변형만 기존 direct native chooser 경로를 허용한다. 업로드 뒤의 filename·exact packet hash 확인은 유지했다.

로컬 검증: BrowserUse extension bridge 관련 단위/통합시험 `14/14 PASS`, V2 static audit `2/2 PASS`, `node --check` PASS, `git diff --check` PASS. 두 Playwright/Chromium 기반 suite는 테스트 setup의 브라우저 시작 단계에서 환경 오류로 멈췄다: `libnspr4.so: cannot open shared object file`. 이는 제품 assertion 실패가 아니라 현재 WSL 런타임 의존성 누락이며, PR CI에서 같은 head의 전체 결과를 확인해야 한다. 실제 브라우저 조작은 하지 않았고 실제 전송·파일 첨부도 여전히 0건이다.

## 다음 단계

1. 변경을 한글 커밋으로 현재 PR 브랜치에 푸시하고 해당 head의 필수 CI를 확인한다.
2. 실제 시도를 재개할 때 BrowserUse의 기존 로그인 세션에서 현재 탭을 다시 열거·claim하고, composer가 비어 있고 응답/첨부가 없는지 확인한다. 이 확인 전에는 과거 tab ID만 믿고 조작하지 않는다.
3. 검증된 코드가 같은 claimed tab에서 파일 메뉴를 선택하고 native chooser를 띄운 뒤, filename과 exact packet hash를 모두 확인할 때까지 prompt 입력·전송하지 않는다. 실패하면 해당 오류와 실제 전송 여부를 다시 기록하고 그 탭을 보존한다.

새 자료 수집, 추가 fetch, 다른 아키타입 실행, 점수 변경은 이 수리 범위에 포함되지 않는다.
