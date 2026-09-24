# BrowserUse: 로그인된 기존 세션 사용 및 재개 지침

최종 갱신: 2026-09-25 07:49 KST (P109: 사용자의 기존 로그인 세션 지시와 최신 pushed head/CI 진행 상태 반영).
이 문서는 인증된 UI 작업의 실행 지침이다. **로그인이 필요한 BrowserUse 작업은 사용자가 이미 로그인해 둔 BrowserUse `extension` 세션의 기존 작업 탭에서만 한다.**

## 최우선 규칙 — 로그인된 그 세션에서만

로그인이 필요한데 기존 BrowserUse 연결에서 사용자의 로그인 세션/작업 탭을 쓸 수 없다면, **브라우저 작업은 거기서 멈춘다.** 새 Chrome이나 창을 띄우기, 새 탭·프로필·CDP 세션으로 갈아타기, 재로그인 요구, 같은 요청을 다른 대화로 다시 보내기는 복구 방법이 아니다. “새 대화”가 필요할 때도 현재 로그인된 기존 탭 안에서만 연다. 이 규칙은 편의상의 선호가 아니라 인증 작업의 필수 경계다.

실패 시에는 마지막으로 확인한 기존 탭/대상, 실제 수행 여부(입력·첨부·전송·다운로드), 도구가 반환한 정확한 오류, 읽기 전용으로 확인한 범위, 다음 한 단계만 기록한다. 기존 창·탭·로그인은 그대로 둔다. 화면이나 durable 상태가 불명확하면 재시도하지 않는다.

## 반드시 따를 실행 순서 — 같은 로그인 세션·같은 탭

1. 현재 Codex 대화에서 실제 BrowserUse 연결 도구를 사용한다. WSL이면 canonical persistent `mcp__node_repl__js` bootstrap을 쓰고 `setupBrowserRuntime()`이 반환한 Agent를 `globalThis.agent`에 저장한 뒤 `agent.browsers.get("extension")`을 사용한다. 설정 파일이나 preflight 성공만으로 브라우저 연결 성공이라고 하지 않는다.
2. `browser.user.openTabs()`로 사용자가 이미 열어 둔 탭을 확인하고, 서비스·대화·작업이 일치하는 정확한 descriptor 하나를 `browser.user.claimTab()`에 넘긴다. 이후에는 claim이 반환한 **바로 그 tab 객체 하나**만 사용한다.
3. 입력·첨부·다운로드·전송 전에 같은 탭의 URL/대화와 로그인 상태를 다시 확인한다. 기존 응답이나 파일이 있으면 새 요청을 보내지 말고 그 탭에서 회수한다. 새 대화가 필요해도 기존 로그인 탭 안에서만 연다.
4. extension 연결, 기존 탭 열거/claim, 대상 대화 확인 중 하나라도 실패하면 즉시 멈춘다. 확인 범위와 **실제 오류 문자열**만 기록한다. 새 Chrome/창/탭/프로필, 별도 CDP 세션, 재로그인, 다른 대화에서의 재전송·재다운로드로 우회하지 않는다. 다른 backend는 동일한 로그인 세션과 정확한 탭을 보존한다는 사실이 확인될 때만 사용할 수 있다.
5. 기존 초안·응답·첨부를 덮어쓰거나, 결과가 이미 있을 수 있는 요청을 중복 전송하지 않는다. 전송은 durable job의 approval/exactly-once gate까지 통과한 경우에만 한다.

WSL에서 직접 BrowserUse runtime을 연결하기 전에는 machine preflight를 한 번 실행한다. Exit code `23`은 stale BrowserUse session이므로 새 Chrome/profile을 열거나 다시 로그인해 우회하지 말고, 같은 로그인 세션을 보존할 수 있는 현재 경로가 없으면 그 자리에서 오류와 확인 범위를 기록하고 멈춘다.

```powershell
powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -Command '& "$env:LOCALAPPDATA\CodexBrowserUseRuntime\Repair-CodexBrowserUse.ps1" -Quiet -FailIfCurrentSessionStale'
```

`browser.tabs.list()`의 빈 목록이나 CDP endpoint의 탭 부재는 사용자의 로그인 세션 부재를 증명하지 않는다. 새 브라우저를 열기 전에 반드시 위 `extension → openTabs() → claimTab()` 경로를 따른다. 인증 토큰·쿠키는 기록하지 않는다.

예: 로그인된 같은 ChatGPT 탭의 Library 미리보기에 JSON과 다운로드 버튼이 이미 있으면, 그 탭을 claim해 그대로 다운로드한다. 새 브라우저/대화를 열어 같은 요청을 다시 보내지 않는다.

## 최신 인계 — P109, 2026-09-25 07:49 KST

### 사용자 지시 — 로그인된 바로 그 세션에서 작업

사용자가 재확인했다. **BrowserUse가 필요하고 로그인 상태가 필요하면, 이미 로그인되어 있는 사용자의 세션에서 하라.** 따라서 실행 직전에 현재 BrowserUse `extension`의 `browser.user.openTabs()`로 기존 탭을 다시 열거하고, 정확한 작업 ChatGPT 탭을 확인해 `claimTab()`한 뒤 반환된 동일 Tab 객체만 사용한다. 새 창/브라우저/탭/프로필/CDP 세션을 만들거나 재로그인을 요구하지 않는다. 새 대화가 필요하면 기존 로그인 탭 안에서만 연다. 연결·claim·대상 대화 확인이 안 되면 입력·첨부·다운로드·전송 전에 중단하고 오류와 확인 범위만 남긴다.

### 현재 저장소/CI 상태

- PR #7은 `OPEN/DRAFT`, URL [PR #7](https://github.com/Daikisong/stock_agent/pull/7), head `617e204b4c0b4f9dce15f4185eff589af9042920`이다. worktree와 `origin/feature/e2r-pro-first-browser-platform-20260822`는 해당 SHA로 같고, 확인 당시 worktree는 clean이다. main 미병합이다.
- 해당 exact source head의 [Pro PR run 36069234793](https://github.com/Daikisong/stock_agent/actions/runs/36069234793), [Pro push run 36069233229](https://github.com/Daikisong/stock_agent/actions/runs/36069233229), [V6 run 36069234853](https://github.com/Daikisong/stock_agent/actions/runs/36069234853)는 모두 `IN_PROGRESS`다. 두 Pro run의 `static-security`만 `SUCCESS`; full regression/core-unit/browser mock E2E와 V6 offline-contract는 완료 전이다. `SUCCESS`로 부르지 않는다.
- 이번 P109에서 브라우저 연결·탭 열거/claim·UI 입력·첨부·다운로드·전송·capture를 하지 않았다. C15 durable DB도 다시 읽지 않았다. 마지막 저장 상태는 P107 기준 C15 `PROJOB-df15a37c58ae7583924e58c0`, `USER_ATTENTION_REQUIRED` v26, submit/capture `0/0`, packet hash `fa5845a055661c99c2ab1eb9cfb65f66fb84d2c85b267b3cde33b54843c320df`, approval/browser/conversation binding 없음이며, 이는 현재 상태 재확인이 아니라 **마지막 기록 증거**다.
- 새 조사·query/fetch·job/pass·다른 archetype·점수/Stage 변경은 이번 문서 checkpoint에 없다. 전체 master goal 미완료: P9 full-thesis Pro canary는 기존 확인 기준 `1/3` (C06만 완료, C17/C28 미완료). PR #7은 draft로 두며 main에 병합하지 않는다.

### 다음 한 단계

세 필수 workflow가 이 source head에서 끝날 때까지 기다린다. 모두 `SUCCESS`면 먼저 C15 durable state를 read-only로 다시 확인한다. 이후 BrowserUse가 필요할 때만 로그인된 기존 `extension` 세션에서 탭을 재열거·claim해 같은 탭에서 재개한다. 세션이나 대상을 확인할 수 없으면 새 세션으로 우회하지 않고 멈춘다.

P109 상태 receipt: [p109_existing_login_session_and_exact_head_ci_receipt.json](p109_existing_login_session_and_exact_head_ci_receipt.json).

## 과거 인계 — P108, 2026-09-25 07:42 KST (P109에서 superseded)

### 로그인된 기존 세션 원칙

사용자의 지시는 유지한다. 인증이 필요한 BrowserUse 작업은 매번 실행 직전에 로그인된 BrowserUse Chrome `extension` 세션에서 기존 탭을 다시 열거하고(`browser.user.openTabs()`), 정확한 ChatGPT 작업 탭 descriptor를 `claimTab()`한 후 반환된 동일 Tab 객체만 사용한다. 새 브라우저·창·탭·프로필·CDP 연결·재로그인은 금지된 대체 경로다. 연결/대상 확인이 되지 않으면 기존 UI를 보존하고 입력 전에 중단한다. P108에는 live BrowserUse 작업이 없으므로 탭·로그인 상태를 다시 확인하거나 조작하지 않았다. P107에서 확인한 기존 세션/탭 상태는 그 시점의 증거로만 남긴다.

### 코드 WIP와 검증

- 기존 visible composer file tile을 download event로 간주하거나 filename button을 다운로드로 클릭하던 경로를 제거했다. 파일 선택이 남아 있지 않은 tile은 `VISIBLE_PACKET_HASH_UNVERIFIED_REPLACEMENT_REQUIRED`로 분류한다.
- 같은 adapter/tab 안에서 정확한 accessible group이 current composer form에 속하는지 확인하고, exact filename이 포함된 단 하나의 영어/한국어 remove action만 찾는다. 제거 후 composer/file chooser/turn 상태를 read-only로 다시 확인하고, 그 다음에만 같은 BrowserUse session의 file chooser로 durable local packet을 선택한다. BrowserUse filechooser receipt의 raw SHA-256, canonical packet hash, visible filename이 모두 맞아야 성공이다. 다른 파일·여러 tile·모호한 제거 버튼·일치하지 않는 hash는 fail-closed다.
- 실제 upload 수행 여부와 packet byte/hash 증거를 `PreparedBrowserJob`, prepared state/event, versioned runtime replacement receipt에 연결했다. live canary의 upload count도 “무조건 1”이 아니라 실제 수행 여부를 반영한다.
- 최종 수정 뒤 focused adapter/orchestration 회귀 **9/9 PASS**, `py_compile`/`git diff --check` PASS. Production static audit **PASS**, `critical_count=0`, hash `731b15cb0631ee40a836fb12f1c507e8aaf91354ef44930d585e04886e8c688c`.
- 전체 로컬 `PYTHONPATH=src python -m unittest discover -s tests -q`는 약 3분 30초 뒤 exit `137`로 종료돼 **완주/통과로 간주하지 않는다**. `dmesg`에는 그 시각 OOM killer가 Python process 하나를 종료한 기록이 있다. 테스트 failure/error summary는 나오지 않았다. 재실행으로 메모리를 더 압박하지 않고 원격 full suite로 확인한다.
- PR #7 remote head `8f3845454519127cbc840449e80115a5b693801e`는 `OPEN/DRAFT`; 동일 head의 Pro push [36067050644](https://github.com/Daikisong/stock_agent/actions/runs/36067050644)와 V6 [36067055253](https://github.com/Daikisong/stock_agent/actions/runs/36067055253)는 `SUCCESS`. Pro PR [36067055134](https://github.com/Daikisong/stock_agent/actions/runs/36067055134)는 07:42 KST 조회 때 independent Reviewer A–H leaf gates 실행 중이었다. 이 CI는 문서 P107 commit만 포함하며 아래 local code WIP를 검증하지 않는다.

### 현재 경계와 다음 한 단계

현재 local source/test 변경은 미커밋이다. C15 `PROJOB-df15a37c58ae7583924e58c0`의 최신 durable evidence는 P107 read-only receipt(`USER_ATTENTION_REQUIRED` v26, submit/capture `0/0`, binding 없음)이며 P108에서 DB/UI는 다시 읽거나 변경하지 않았다. 새 연구/job/pass, source query/fetch, 다른 archetype, 점수/Stage 변경은 없다. 다음 한 단계는 이 source/test/P108 문서를 Korean commit으로 PR #7 branch에 push하고 새 exact-head Pro PR, Pro push, V6 CI를 끝까지 통과시키는 것이다. green 이후에만 C15 state를 read-only 재확인한 다음, 로그인된 기존 `extension` 탭을 다시 열거·claim해 그 same session에서 재개한다. PR #7은 draft/open 유지, main 미병합이다. 전체 goal은 미완료다.

P108 상태 receipt: [p108_c15_attachment_replacement_and_validation_receipt.json](p108_c15_attachment_replacement_and_validation_receipt.json).

## 과거 인계 — P107, 2026-09-25 07:16 KST (P108으로 superseded)

### 사용자가 재확인한 필수 실행 방식

사용자는 “BrowserUse를 쓸 때 로그인이 필요하면 로그인되어 있는 세션 쪽에서 하라”고 재차 요청했다. 이 작업에서는 사용자가 이미 로그인해 둔 BrowserUse Chrome `extension` 세션이 유일한 인증 브라우저다. 작업 직전에 `browser.user.openTabs()`로 기존 탭을 새로 열거하고, 대상 ChatGPT 작업 탭의 URL·대화·실제 Pro 모드를 확인한 뒤 그 descriptor를 `claimTab()`에 넘긴다. 이후 모든 확인/입력은 claim이 돌려준 **같은 Tab 객체**에서만 한다. 새 창·새 탭·새 프로필·별도 CDP 브라우저·재로그인은 대체 경로가 아니다. 연결/claim/대상 확인이 안 되면 UI를 보존하고 실제 오류만 기록한 뒤 입력 전에 멈춘다. 새 대화가 꼭 필요해도 로그인된 기존 탭 안에서만 연다.

쉬운 구분: JSON이 Library 미리보기 안에 열려 있고 그 화면에 실제 다운로드 버튼이 있으면 같은 로그인 탭에서 그 버튼을 사용한다. 반대로 빈 Chat composer에 붙어 있는 파일 이름 tile은 첨부 상태 표시일 수 있으므로 다운로드 링크라고 간주하거나 파일 이름 버튼을 다운로드로 무조건 클릭하지 않는다. 먼저 현재 탭의 화면/DOM에서 실제 action을 확인하고, 원본 bytes/hash를 증명할 수 없으면 그 상태를 그대로 기록하고 멈춘다.

### 현재 checkpoint와 사실 경계

- PR #7은 `OPEN/DRAFT/CLEAN`, remote head 및 origin feature head는 `f49ff8a0d8d56ac5ca4d1dda9292ebc6e0d52013`이다. 이 SHA의 Pro PR [36064013627](https://github.com/Daikisong/stock_agent/actions/runs/36064013627), Pro push [36064009596](https://github.com/Daikisong/stock_agent/actions/runs/36064009596), V6 [36064013622](https://github.com/Daikisong/stock_agent/actions/runs/36064013622)는 `SUCCESS`다. 이 run들은 현재 로컬 미커밋 adapter/protocol 변경 전의 SHA를 검증한 것이며, 그 미커밋 변경을 검증했다고 해석하면 안 된다.
- 현재 worktree에는 `src/e2r/pro_first/browser/chatgpt_adapter.py`와 `protocol.py`에만 미커밋 변경이 있다. 목적은 visible attachment tile을 다운로드 증거로 오인하지 않도록 하고, 실제 첨부 시 선택한 로컬 파일의 SHA-256/packet hash와 upload 발생 여부를 prepare receipt에 전달하는 것이다. 현재 diff는 아직 회귀 테스트·orchestration 통합·정확한 원격 CI 검증을 마치지 않은 WIP이며 완료된 수정으로 취급하지 않는다.
- 이번 기록 시점의 기존 로그인 탭은 읽기 전용으로 확인했다. 주소는 ChatGPT root, 선택 모드는 Chat, 실제 `6 Pro` 표시가 있었고 composer는 비어 있었으며 timestamped packet tile 하나가 보였다. tile 자체에는 download URL/action이 확인되지 않았고 file input 5개는 모두 비어 있었다. 탭을 이동하지 않았고 prompt 입력·첨부 교체·다운로드·전송·capture도 하지 않았다. CDP capability는 실제 오류 `Capability is not available: cdp`로 사용할 수 없었다. 인증 문제로 분류하지 않는다.
- C15 `PROJOB-df15a37c58ae7583924e58c0`은 SQLite `mode=ro` + `PRAGMA query_only=ON`으로 확인했다. 상태는 `USER_ATTENTION_REQUIRED` v26, packet canonical hash `fa5845a055661c99c2ab1eb9cfb65f66fb84d2c85b267b3cde33b54843c320df`, submit/capture `0/0`, approval/browser/conversation binding 없음, `safe_unprepared_resume=false`, successor 없음이다. 새 job/pass, query/fetch, 다른 archetype, 점수/Stage 변경은 하지 않았다.

### 다음 한 단계

먼저 generic adapter의 safe-replacement 경로를 끝까지 구현하고, “기존 exact-name tile은 다운로드 없이 replacement-required”, “다른/multiple 파일은 fail-closed”, “같은 탭에서 hash 확인된 로컬 packet만 첨부” 회귀 테스트를 추가한다. orchestration이 그 증거를 durable receipt에 남기는지도 검증한다. source/test/docs 변경을 Korean commit으로 PR #7 branch에 push한 뒤 새 exact-head Pro PR, Pro push, V6 CI가 모두 끝나고 성공한 경우에만 same-job C15 작업을 재개한다. 그때도 실행 직전에 로그인된 `extension` 탭을 다시 열거·claim해 그 탭에서만 한다. 현재 열린 tab tile을 삭제/교체하거나 prompt를 입력하지 않는다. PR #7은 draft/open 유지, main 미병합이다. 전체 master goal은 미완료다.

P107 상태 receipt: [p107_c15_existing_login_session_checkpoint_receipt.json](p107_c15_existing_login_session_checkpoint_receipt.json).

## 최신 인계 — P106, 2026-09-25 06:47 KST

### 기존 로그인 세션만 사용

로그인이 필요한 BrowserUse 작업은 사용자가 이미 로그인해 둔 Chrome plugin `extension` 세션의 기존 탭에서만 진행한다. 실행 직전에 `browser.user.openTabs()`로 현재 탭을 열거하고 정확한 ChatGPT 작업 탭을 `claimTab()`한 뒤, 반환된 동일 Tab 객체만 사용한다. 이번 P106도 열린 탭 4개에서 기존 ChatGPT root 탭을 다시 찾아 claim했다. 새 브라우저·창·탭·프로필·CDP 세션을 만들거나 재로그인하지 않았다. 인증값·쿠키·tab ID는 기록하지 않는다.

### exact-head CI

P105 수정 commit/head `1fc9e8024a9103e56c9d94f1fa0d42c4d583b62c`의 아래 필수 run은 모두 `SUCCESS`다.

- [Pro PR 36058257097](https://github.com/Daikisong/stock_agent/actions/runs/36058257097)
- [V6 PR 36058257109](https://github.com/Daikisong/stock_agent/actions/runs/36058257109)
- [Pro push 36058250305](https://github.com/Daikisong/stock_agent/actions/runs/36058250305)

Pro PR, Pro push, V6 전체 테스트는 각각 **7,948개 실행 / skip 38 / failure 0 / error 0**으로 끝났다. 이 exact-head CI는 root `get_by_role` bridge fix와 회귀를 검증하지만, C15 live request 완료를 의미하지 않는다. PR #7은 OPEN/DRAFT이며 main에 병합하지 않았다.

### C15 same-job 재개 결과

- 대상은 동일 C15 R6 job `PROJOB-df15a37c58ae7583924e58c0`, S-Oil `010950`, `as_of_date=2026-08-23`; fresh session `FRESH-V2-1-C15-R6-20260907T212025Z`; packet canonical hash `fa5845a055661c99c2ab1eb9cfb65f66fb84d2c85b267b3cde33b54843c320df`다. predecessor-bound `FreshInitialCanarySpec`를 사용했고, 새 job/pass를 만들지 않았다.
- root locator 수정 후 같은 탭에서 worker가 `FRESH_PACKET_READY`와 `FRESH_UNPREPARED_ATTENTION_RESUME`까지 진행했다. 이후 visible composer packet 다운로드를 검증하는 단계에서 다음으로 fail-closed했다.

```text
BrowserUIIncompatible: visible composer packet download was not observed in the claimed tab
```

- 별도 BrowserUse 직접 다운로드 이벤트 확인도 같은 기존 탭에서 exact filename button을 대상으로 한 번 수행했으나 `Timed out after 12000ms waiting for download`였다. 다운로드 사본/새 첨부는 얻지 못했다. DOM snapshot에는 `research_packet(20260924-172107).json` file group/button 및 제거 버튼만 있었고 file card subtree에 download link/href가 보이지 않았다. file input 5개 모두 `files.length=0`이었다.
- **이전 P100의 실제 다운로드/hash 증거는 별도로 보존한다:** P100에서는 같은 filename tile의 visible download event로 175,126 bytes 사본을 받았고 raw SHA-256 `e1d1c44edfd0467aeac3aff1bd362cbb927bf01da135e91f3d9d5cd39f81324f`가 당시 local packet과 일치했으며 canonical hash도 durable hash와 같았다. 하지만 P106의 두 다운로드 재검증은 성공하지 않았으므로 과거 P100 결과를 이번 시점의 새 다운로드 성공으로 표현하지 않는다.
- 기존 탭의 최종 read-only 확인: `https://chatgpt.com/` root, Chat 선택, 실제 `6 Pro` 표식, 빈 prompt composer, visible packet tile 1개. `tab.dev.logs({levels:["error","warn","warning"],limit:200})`는 0건. CDP capability 오류는 정확히 `Capability is not available: cdp`였다. 화면/탭을 이동하거나 파일을 제거하지 않았고 prompt 입력·upload·submit·capture는 없다.
- 첫 harness 재시도는 detached Node REPL promise로 인해 `BRIDGE_OPERATION_FAILED: node_repl exec context not found`에서 실패했다. 이는 내 실행 순서 오류였으며 UI/DB 변화가 없었다. 이후 `runUntil(workerPromise)`를 같은 awaited Node REPL call에 넣어 재실행했고, 위의 실제 packet download gate까지 도달했다.

### 최종 durable 상태와 다음 한 단계

실패 후 SQLite를 `mode=ro` 및 `PRAGMA query_only=ON`으로 다시 읽었다. 같은 job은 계속 `USER_ATTENTION_REQUIRED`, version `26`, packet hash 불변, approval/browser/conversation binding 없음, submit/capture `0/0`, successor 없음이며 기존 last error/event도 변경되지 않았다. 같은 다운로드 event를 재시도하거나 파일 tile을 삭제하지 않는다.

현재 blocker는 인증이 아니다. 이전 P100은 exact bytes를 확인했지만 현재 visible packet tile에서 download event가 재현되지 않아 이번 same-job gate를 통과하지 못했다. 다음 동작은 generic BrowserUse file-card verification 경로를 회귀시험과 exact-head CI로 수리하는 것이다. 현재 단일 tile을 제거하고 다시 첨부하는 행동은 아직 하지 않는다. submit/upload 권한 상태가 명확하지 않으므로 사용자가 그 대체를 명시적으로 승인하지 않는 한 기존 draft를 보존한다. query/fetch, 새 research pass/job, 다른 archetype, score/Stage 변경은 모두 0이다.

P106 machine receipt: [p106_c15_download_event_recovery_receipt.json](p106_c15_download_event_recovery_receipt.json). 전체 master goal은 미완료다.

## 과거 인계 — P105, 2026-09-25 05:52 KST (P106으로 superseded)

### 인증 세션은 사용자의 기존 로그인 탭만 사용

사용자가 다시 요청한 대로 로그인 UI가 필요하면 이미 로그인된 사용자의 BrowserUse `extension` 세션에서 작업한다. 이번 same-job 복구도 기존 extension session의 현재 탭을 열거하고 ChatGPT 탭 descriptor를 claim한 뒤 claim이 반환한 동일 객체 하나로만 진행했다. 새 Chrome/창/탭/프로필/CDP 세션이나 재로그인은 사용하지 않았다. 이후 CI 대기 뒤 실제 재개 전에도 `openTabs()` 결과를 다시 확인하고 그때 반환된 정확한 탭만 claim한다. 새 연결·탭·작업 대화가 확인되지 않으면 대체 창을 열지 않고 중단한다.

### exact-head CI와 same-job 상태

- PR #7은 `OPEN/DRAFT`, head `ff929834f2d6f87576d6c80c54f5bec08ca60763`, 확인 시 `mergeStateStatus=CLEAN`이다. draft 해제 및 main 병합은 하지 않았다.
- 이 head의 [Pro PR 36052355870](https://github.com/Daikisong/stock_agent/actions/runs/36052355870), [V6 PR 36052354380](https://github.com/Daikisong/stock_agent/actions/runs/36052354380), [Pro push 36052348009](https://github.com/Daikisong/stock_agent/actions/runs/36052348009)은 모두 `SUCCESS`다. 이 결과는 아래 P105 로컬 수정은 포함하지 않는다.
- 중앙 DB는 `mode=ro`와 `PRAGMA query_only=ON`으로 재확인했다. C15 `PROJOB-df15a37c58ae7583924e58c0`은 `USER_ATTENTION_REQUIRED` v26, packet hash `fa5845a055661c99c2ab1eb9cfb65f66fb84d2c85b267b3cde33b54843c320df`, submit/capture `0/0`, approval/browser/conversation binding 없음, 기존 `safe_unprepared_resume=false` event 유지다. 마지막 durable error는 기존 `BrowserUIIncompatible: the exact BrowserUse packet file/hash was not visible in the claimed tab`이며 이번 bridge 오류가 DB를 변경하지 않았다.

### P105 실제 시도와 기술 원인

같은 `https://chatgpt.com/` 탭에서 읽기 전용 확인한 상태는 인증된 계정 표시 있음, Chat의 실제 `6 Pro`, 빈 composer, user/assistant turns `0/0`, visible packet tile 1개(`research_packet(20260924-172107).json`), file input 선택 0개였다. recovery worker는 same-job packet을 재사용하고 사전 검증에 진입했으나 prompt/attachment/submit 전에 BrowserUse RPC가 다음 오류로 멈췄다.

```text
BRIDGE_OPERATION_FAILED: Cannot read properties of null (reading 'getByRole')
```

원인은 `BrowserUsePage.get_by_role()`가 root locator descriptor를 보내지만 MJS dispatcher가 부모 locator가 없을 때도 `base.getByRole()`을 호출하던 일반 wrapper bug다. 이는 로그인/세션 문제가 아니다. Python BrowserUse page의 root `get_by_role`은 `tab.playwright.getByRole()`을 사용해야 한다. `getByRoleLocator(base, page, ...)` helper에서 parent가 없으면 page, 있으면 parent를 사용하도록 수정하고 root/nested 회귀 테스트를 추가했다.

이 시도 직후 DB와 같은 claimed tab을 다시 확인했다: job은 여전히 v26/`USER_ATTENTION_REQUIRED`, submit/capture `0/0`; UI는 같은 root Chat, 실제 `6 Pro`, 빈 composer, 대화 0/0, 기존 tile 1개다. prompt 입력·추가 첨부·다운로드·전송·capture·query/fetch는 모두 0이며 새 job/pass도 없다. 앞선 두 harness 오류도 worker/UI 이전에 중단됐다: Node REPL `globalThis.require` 부재로 spawn 이전 실패, 그리고 recovery에 independent spec을 잘못 넘긴 frozen-predecessor identity mismatch. 원본 predecessor job/run/conversation spec으로 고친 read-only boundary check는 PASS했다.

### 로컬 검증과 다음 한 단계

- BrowserUse adapter/bridge/fresh orchestration 테스트: **174/174 PASS**.
- `node --check`, `py_compile`, `git diff --check`: PASS.
- production static audit: **PASS**, `critical_count=0`; production hash `dd4ff07ac1579bc8e8c43940cb7bc162b7b4e4e7708b67b1b83264a5e645fdee`.
- P105 bridge/test/document diff는 현재 로컬 변경이다. ff929 exact-head CI는 수정 전 코드만 검증했으므로 P105 수정의 원격 green으로 세지 않는다.

다음 한 단계는 root `get_by_role` 수정·회귀시험·P105 문서를 기존 PR #7 branch에 한글 commit/push하고, Pro push/Pro PR/V6 Actions를 새 exact head에서 끝까지 확인하는 것이다. **그 새 exact-head CI가 모두 SUCCESS가 되기 전에는 same-job BrowserUse 재개/입력을 하지 않는다.** 통과한 뒤 durable state를 다시 read-only로 확인하고 사용자의 현재 기존 `extension` 탭을 재열거·claim해 그 세션에서만 이어간다. 전체 master goal은 미완료다.

P105 machine receipt: [p105_c15_root_locator_recovery_receipt.json](p105_c15_root_locator_recovery_receipt.json).

## 과거 인계 — P104, 2026-09-25 05:22 KST (P105로 superseded)

사용자는 다시 분명히 지시했다: **로그인 상태가 필요한 BrowserUse 작업이면 그 작업을 사용자가 이미 로그인해 둔 바로 그 세션/기존 탭에서 한다.** 이는 기록만 해 둘 문구가 아니라 실행 조건이다. 새 창이나 별도 Chrome을 열지 않고, 현재 Codex 대화에서 BrowserUse `extension`을 연결한 뒤 `browser.user.openTabs()`로 기존 탭을 그때 다시 찾는다. 대상 탭을 `claimTab()`하고 claim이 반환한 동일 객체만 사용한다. 기존 세션을 연결·claim·대상 확인하지 못하면 새 세션으로 대체하지 말고 거기서 멈춘다. 이전 기록의 tab ID나 로그인 화면은 이번 실행의 증거로 재사용하지 않는다.

### 현재 코드·CI checkpoint

- PR #7은 `OPEN/DRAFT`, head `ff929834f2d6f87576d6c80c54f5bec08ca60763`, 확인 시 `mergeStateStatus=UNSTABLE`이다. Draft 해제나 main 병합은 하지 않았다.
- [Pro PR workflow 36052355870](https://github.com/Daikisong/stock_agent/actions/runs/36052355870): `static-security`, `core-unit`, `browser-mock-e2e` 성공; `full-regression` 전체 테스트 실행 중이며 Reviewer A–H와 compile/whitespace는 대기.
- [V6 PR workflow 36052354380](https://github.com/Daikisong/stock_agent/actions/runs/36052354380): portable checkout, Gate 1 receipt consistency, production static audit 성공; 전체 unit suite 실행 중.
- [Pro push workflow 36052348009](https://github.com/Daikisong/stock_agent/actions/runs/36052348009): `static-security`, `core-unit`, `browser-mock-e2e` 성공; `full-regression` 전체 테스트 실행 중.
- 세 workflow 모두 위 exact head에서 아직 종료되지 않았다. 따라서 이를 green이라고 부르지 않으며, BrowserUse live retry도 아직 시작하지 않는다.

P104는 문서 및 GitHub 상태만 확인했다. BrowserUse preflight/extension 연결/탭 열거·claim/UI 접근, prompt 입력, attachment·download·submit·capture, query/fetch는 모두 수행하지 않았다. 마지막으로 알려진 same-job C15 durable 상태는 P102의 read-only snapshot인 `USER_ATTENTION_REQUIRED` v26, submit/capture `0/0`, approval/browser/conversation binding 및 prepare receipt 없음이다. 현재 상태는 다음 live 시도 직전에 다시 read-only로 확인해야 한다.

### 다음 한 단계

먼저 위 세 workflow가 exact SHA `ff929834f2d6f87576d6c80c54f5bec08ca60763`에서 모두 끝나는지 확인한다. 요구 workflow가 SUCCESS가 된 뒤 same-job durable state를 read-only로 다시 읽는다. 그 다음에만 사용자의 현재 BrowserUse `extension` 세션에서 기존 탭을 다시 열거하고 exact tab을 claim한다. 모든 인증 UI 작업은 **그 기존 세션 안에서만** 한다. 연결이나 탭 확인이 안 되면 입력·첨부·전송 없이 중단하고 실제 오류와 확인 범위만 기록한다.

## 과거 인계 — P103, 2026-09-25 05:02 KST (후속 P104/P105 참조)

### 사용자의 인증 세션 지시

BrowserUse에서 로그인이 필요한 작업이면 사용자가 이미 로그인한 바로 그 `extension` 세션과 그 세션 안의 기존 작업 탭을 사용한다. 새 Chrome/창/탭/프로필을 띄우거나 CDP의 다른 프로필·세션으로 옮기거나 재로그인하지 않는다. 실행 직전 `openTabs()`를 다시 열거하고 대상 descriptor를 확인해 claim한 다음, claim이 반환한 동일 Tab 객체만 쓴다. 필요한 새 Chat은 기존 탭 안에서만 연다. 연결/탭/대화/모드가 일치하지 않으면 기존 로그인 UI를 보존하고 입력 전에 멈춰 실제 오류를 기록한다.

### C15 R6 재개 차단 원인과 수정

P102의 실제 실패는 로그아웃/Pro 모드 문제가 아니었다. 기존 로그인 `https://chatgpt.com/` 탭의 실제 모드는 `6 Pro`, visible composer tile은 정확히 하나였다. 그 tile의 파일명은 attachment DIV와 attachment BUTTON의 accessible label로 나타났고, 또 다른 제거 버튼은 `파일 1 제거: research_packet(20260924-172107).json`라는 label을 가졌다. BrowserUse snapshot callback이 제거 버튼의 label 안 파일명 suffix를 추가 attachment로 세어 `unprepared recovery found multiple visible composer attachments`로 fail-closed했다.

P103 code patch는 다음 경계를 수리했다.

- BrowserUse `readonlyCallback`와 Python adapter의 두 composer snapshot 경로 모두 button/role=button의 명확한 remove/delete/clear/detach/cancel action label을 attachment filename 신호에서 제외한다. 영어 동사와 한국어 제거/삭제/지우기/해제/취소 label을 처리한다. 특정 종목이나 packet basename에는 분기하지 않는다.
- 기존 packet tile 재검증에도 같은 reviewed read-only composer snapshot callback marker를 사용하게 해 callback 경로가 둘로 갈라지지 않게 했다.
- exact packet button이 현재 composer form에 속하는지 검사하는 `E2R_PACKET_ATTACHMENT_IN_COMPOSER`용 reviewed read-only BrowserUse callback을 추가했다. 이전 extension callback allowlist에는 이 코드 경로가 없어 exact attachment hash 확인 다음 단계에서 별도 기술 오류가 날 수 있었다.
- regression은 tile 1개+한국어 제거 button이 signal 1개로 남고, 실제 다른 파일이 추가되면 signal 2개가 유지되는지 검사한다. packet button과 composer가 같은 form인지도 PASS/FAIL 경계를 테스트한다.

### 검증과 다음 한 단계

- `tests.test_e2r_pro_first_browseruse_extension_bridge` + `UnpreparedRecoveryReadOnlyGateTest`: **19/19 PASS**.
- 변경 영향 파일 전체 묶음 `tests.test_e2r_pro_first_browser_adapter`, `tests.test_e2r_pro_first_browseruse_extension_bridge`, `tests.test_e2r_pro_first_v2_1_fresh_orchestration`: **174/174 PASS**. 로컬 Chromium test를 위해 기존 Playwright shared-library 경로를 사용했다.
- `python -m e2r.cli.audit_e2r_pro_first_v2 --repo-root .`: **PASS**, `critical_count=0`, static/generalization/prompt/scoring-publication/verifier-repair/contract audits 모두 PASS.
- `node --check`, `python -m py_compile`, `git diff --check`: **PASS**.
- P102 문서 commit의 Pro/V6 CI runs `36051031300`, `36051031101`, push run `36051024824`는 확인 시 `in_progress`였고, 이전 head `6679186fe6c279230a069e134a3fa39c5057b840`에서 실행 중이었다. 이들은 P103 code patch를 포함하지 않아 새 patch의 CI 증거로 쓰지 않는다. P103 changes를 한글 commit/push하고 새 exact-head Pro/V6 CI SUCCESS를 기다린다.

실제 C15 재개/BrowserUse 재시도는 **아직 하지 않았다**. P102 마지막 read-only durable snapshot은 C15 `PROJOB-df15a37c58ae7583924e58c0`, `USER_ATTENTION_REQUIRED` v26, submit/capture `0/0`, approval/binding/prepare receipt 없음, `safe_unprepared_resume=false`였다. P103 code/test 작업은 DB 및 browser UI를 조작하지 않았다. CI가 green이면 그때 durable state를 read-only로 다시 확인하고, 사용자의 현재 기존 로그인 BrowserUse `extension` 세션에서 tab list를 다시 열거·claim해 same-job만 진행한다. hash/recovery gate가 통과하기 전 prompt 입력/전송하지 않는다.

machine receipt: [P103 attachment-label recovery patch receipt](p103_c15_attachment_label_recovery_patch_receipt.json).

## 과거 인계 — P102, 2026-09-25 04:49 KST (P103으로 superseded)

### 사용자의 인증 세션 지시

사용자는 다시 분명히 지시했다. **BrowserUse에서 로그인이 필요한 작업이면 사용자가 이미 로그인해 둔 바로 그 세션과 그 세션 안의 기존 작업 탭을 사용한다.** 새 Chrome/창/탭/프로필을 띄우거나, CDP의 다른 프로필로 옮기거나, 재로그인·새 세션으로 대신하지 않는다. 새 Chat 대화가 필요한 경우에도 기존 로그인 탭 안에서만 연다.

실행 직전 현재 BrowserUse `extension` 연결과 `openTabs()`를 확인하고, 서비스 URL·작업 대화·실제 Pro 모드가 맞는 기존 탭 descriptor를 고른 다음 정확히 그 descriptor를 `claimTab()`한다. 이후 입력·첨부·다운로드·전송은 claim이 반환한 동일 Tab 객체에서만 수행한다. 탭이 안 보이거나 연결/claim/화면 확인이 실패하면 사용자의 세션을 보존하고 실제 오류와 확인 범위를 기록한 뒤 입력 전에 멈춘다. 이전 관찰의 tab ID/로그인 상태는 새 실행의 확인으로 재사용하지 않는다.

### C15 R6 — 같은 로그인 탭 재개 시도와 실제 원인

2026-09-25 이번 재개 시도에서도 이미 로그인된 BrowserUse Chrome plugin `extension` 세션을 사용했다. 현재 `openTabs()`에서 기존 `https://chatgpt.com/` Chat 탭을 찾아 claim하고, claim이 반환한 바로 그 Tab 객체만 사용했다. 화면의 실제 모드는 `6 Pro`, composer는 비어 있었고 기존 첨부 tile은 `research_packet(20260924-172107).json` 하나였다. 새 창·브라우저·탭·프로필/CDP 세션을 만들거나 재로그인하지 않았다.

job `PROJOB-df15a37c58ae7583924e58c0`의 정확한 R6 packet을 대상으로 기존 unsent recovery 경로를 실행했지만, 전송 전 read-only gate가 다음으로 fail-closed했다.

```text
BrowserUIIncompatible: unprepared recovery found multiple visible composer attachments
FAILED_SAFE_NO_AUTOMATIC_RESUBMIT
submitObserved=false
```

화면에는 실제 tile 하나뿐이었다. 같은 composer form snapshot에서 첨부 파일명은 `DIV[aria-label]`과 첨부 `BUTTON[aria-label]`로 표현됐고, 별도의 제거 버튼에는 `파일 1 제거: research_packet(20260924-172107).json`라는 accessible label이 있었다. snapshot parser는 제거 action label 안의 끝 파일명도 파일 신호로 잘못 세어 **보이는 파일이 여러 개라고 오판**했다. 이건 로그인 실패, Pro 모드 실패, 실제 중복 첨부가 아니다. 원인은 generic UI snapshot classifier가 remove/delete 동작 label을 attachment identity로 취급하는 파서 결함으로 확인됐다.

실패는 preparation/입력/전송 분기 전 발생했다. prompt 입력, 신규 첨부, 다운로드, submit, response capture, query/fetch는 이번 시도에서 모두 0이다. read-only SQLite 재확인 전후 C15는 `USER_ATTENTION_REQUIRED`, version `26`, `submit_count/capture_count=0/0`으로 동일하며 approval/binding/prepare receipt는 여전히 없고 `safe_unprepared_resume=false`다. 과거 durable error `BrowserUIIncompatible: the exact BrowserUse packet file/hash was not visible in the claimed tab`는 그대로다. 이번 parser 오류는 durable job error를 덮어쓰지 않았다.

같은 claimed tab의 `tab.dev.logs({levels:["error","warn","warning"], limit:200})` 결과는 빈 목록이었다. 해당 tab의 CDP capability 요청은 실제 `Capability is not available: cdp` 오류를 돌려줬다. 이는 기술 capability 제한이지 정책 거절/로그인 부재가 아니다. DOM snapshot은 read-only로 확인했으며 브라우저를 닫거나 초기화하지 않았다.

### 다음 한 단계 — generic 파서 수정, 그 전에는 재개 금지

1. composer file-signal 수집에서 제거/삭제 action accessible label을 첨부 이름으로 세지 않도록 generic 수정한다. 특정 종목/packet 파일명 하드코딩은 하지 않는다.
2. regression test를 추가한다: 실제 첨부 tile 1개 + `파일 1 제거: <filename>`는 파일 1개로 인식되고, 실제 서로 다른 파일 2개는 계속 fail-closed한다.
3. focused tests, static audit, `git diff --check` 및 PR #7의 exact-head CI를 확인한다.
4. 그 뒤에도 C15를 새로 만들지 않는다. durable job/hash를 read-only로 다시 확인하고, 사용자의 **현재 기존 로그인 BrowserUse `extension` 세션**에서 `openTabs()`→정확한 `claimTab()`을 반복해 같은 job을 재개한다. 첨부/file hash/recovery gate가 통과하기 전에는 prompt 입력/submit하지 않는다.

이번 P102에서는 위 코드 수정을 아직 하지 않았다. 문서화 시점의 feature branch pushed head는 P101에서 확인한 `3eb10efecfe652877f56566e4f1b0c0b6f53a5e8`이며, P101의 문서 diff와 이번 P102 문서/receipt는 로컬 미커밋 상태다. P101의 CI SUCCESS는 해당 pushed code SHA 기준이고 이번 문서 변경은 포함하지 않는다. PR #7은 기존 기준대로 `OPEN/DRAFT` 유지하며 main에 병합하지 않는다. 전체 master goal은 미완료다.

기계 판독형 시도 receipt: [P102 C15 existing-session receipt](p102_c15_existing_session_attachment_label_misclassification_receipt.json).

## 과거 인계 — P101, 2026-09-25 04:26 KST (P102로 superseded)

### 인증 작업을 할 때 사용할 세션

사용자가 다시 명시했다: **로그인이 필요한 BrowserUse 작업은 사용자가 이미 로그인해 둔 바로 그 세션과 그 안의 기존 작업 탭에서 한다.** 인증 여부를 확인하려고 별도 Chrome을 띄우거나, 현재 탭을 못 찾았다는 이유로 새 창·프로필·CDP 연결·재로그인으로 갈아타지 않는다. 새 Chat 대화가 정말 필요하면 기존 로그인 탭 안에서만 시작한다. 연결·탭 대조·claim이 실패하면 기존 화면/로그인을 보존하고, 실제 오류와 확인 범위만 남긴 뒤 입력 전에 중단한다.

실행 전에 현재 Codex 세션에서 BrowserUse `extension`을 실제로 연결하고, `openTabs()`로 현재 탭을 새로 열거한다. URL·작업 대화·실제 Pro 모드를 확인한 기존 탭 하나를 `claimTab()`하고, 반환된 동일 Tab 객체만 입력·첨부·다운로드·전송에 쓴다. 이전 기록의 tab ID나 로그인 상태는 현재 연결 권한으로 간주하지 않는다. 이 규칙은 backend 선택의 취향이 아니라 인증 UI 작업의 필수 조건이다.

### 코드·CI·goal 현황

- PR #7은 `OPEN/DRAFT/MERGEABLE`; head 및 `origin/feature/e2r-pro-first-browser-platform-20260822`는 `3eb10efecfe652877f56566e4f1b0c0b6f53a5e8`다. 문서 갱신 전 worktree는 clean이었으며, 현재 P101의 이 handoff와 progress 문서는 아직 local uncommitted 상태다. merge 또는 draft 해제는 하지 않는다.
- 같은 SHA의 V6 offline-contract run [36045098343](https://github.com/Daikisong/stock_agent/actions/runs/36045098343)은 `SUCCESS`다.
- Pro PR run [36045098375](https://github.com/Daikisong/stock_agent/actions/runs/36045098375)은 동일 SHA `3eb10efecfe652877f56566e4f1b0c0b6f53a5e8`에서 `SUCCESS`로 완료했다. `core-unit`, `static-security`, `browser-mock-e2e`, full existing regression suite와 independent Reviewer A–H leaf gates가 모두 통과했다. 이는 이 pushed head의 코드 검증이며, 로컬 P101 문서 diff는 아직 remote head에 포함되지 않았다.
- 같은 SHA의 Pro push run [36045089867](https://github.com/Daikisong/stock_agent/actions/runs/36045089867)은 `SUCCESS`로 끝났다. 그래도 현재 PR run은 별도 필수 확인으로 남아 있다.
- 전체 master goal은 미완료이며 실제 Pro full-thesis canary는 현재 기록상 C06 `1/3`; PR #7은 계속 draft/open, `main` 미병합이다.

### C15 및 기존 로그인 BrowserUse 탭 read-only 재검증

- Pro PR CI `36045098375`와 V6 CI `36045098343` 모두 pushed code head `3eb10efecfe652877f56566e4f1b0c0b6f53a5e8`에서 `SUCCESS`다.
- SQLite는 `mode=ro` 및 `query_only=ON`으로 열었다. C15 `PROJOB-df15a37c58ae7583924e58c0`는 `010950`, `as_of_date=2026-08-23`, `USER_ATTENTION_REQUIRED`, version `26`; packet hash `fa5845a055661c99c2ab1eb9cfb65f66fb84d2c85b267b3cde33b54843c320df`; `submit_count/capture_count=0/0`다. approval packet hash/consumed timestamp, browser session 및 conversation binding은 모두 null이다. 마지막 event도 `safe_unprepared_resume=false`, `automatic_resubmit_allowed=false`, `automatic_login_allowed=false`다. 마지막 오류는 `BrowserUIIncompatible: the exact BrowserUse packet file/hash was not visible in the claimed tab`이며 job row/event는 변경하지 않았다.
- BrowserUse preflight exit code는 `0`이었다. 현재 세션에서 Chrome plugin `extension`을 실제 연결하고 `openTabs()`의 현재 결과에서 ChatGPT root 탭 descriptor를 다시 찾아 claim한 뒤, 반환된 같은 Tab 객체만 읽었다. 페이지에는 로그인 profile, Chat, 실제 `6 Pro`, 빈 composer, `research_packet(20260924-172107).json` 첨부 tile 하나가 보였다. 새 창/브라우저/탭/프로필/CDP/로그인을 만들거나 바꾸지 않았고 tile을 누르거나 다시 다운로드하지 않았다. P100에서 이 tile의 downloaded bytes와 canonical hash가 exact C15 packet과 일치함을 이미 확인했다.
- 이 확인은 같은 세션/탭을 현재 다시 찾을 수 있음을 증명하지만 durable approval이나 `safe_unprepared_resume`을 만들지 않는다. 따라서 이번 확인에서 첨부 재선택, 전송, capture는 하지 않았고 `submit/capture`는 계속 `0/0`이다. **approval/recovery gate가 durable state에서 성립하기 전에는 send하지 않는다.**

이번 P101은 위 문서와 원격 CI, durable state, 이미 로그인된 BrowserUse 탭을 read-only로 확인한 checkpoint다. BrowserUse DOM 평가 외 UI 변경은 없었고 prompt 입력·첨부·다운로드·전송·capture, 새 job/pass, 검색/fetch, 다른 archetype, 점수/Stage 변경은 0이다. 인증 비밀·쿠키·tab ID는 기록하지 않는다. P101 문서는 현재 local uncommitted다.

다음 한 단계는 exact C15 job의 durable approval/recovery gate가 성립하는지 확인하는 것이다. 이를 통과하는 경우에도 인증 UI는 위 규칙에 따라 현재 사용자의 기존 로그인 `extension` 세션과 그 안에서 새로 재확인한 exact target tab만 사용한다. 승인/상태가 불일치하거나 같은 탭 연결이 안 되면 새 세션·재전송으로 우회하지 말고 멈춘다. 추가 canary·job·pass 또는 전송은 이 승인 경계와 master goal 범위 안에서만 판단하며, 전체 goal 완료를 선언하지 않는다.

## 과거 기준 상태 — P100, 2026-09-25 03:56 KST (P101로 superseded)

- **사용자가 지정한 인증 세션 원칙:** 로그인 필요한 BrowserUse 작업은 사용자가 이미 로그인해 둔 `extension` 세션 안의 기존 작업 탭에서만 한다. 이번 확인도 현재 BrowserUse 세션의 열린 사용자 탭을 다시 열거하고 ChatGPT 탭 하나를 정확히 claim한 뒤, claim이 돌려준 같은 Tab 객체에서만 진행했다. 새 브라우저/창/프로필/CDP 세션/재로그인/새 탭은 만들지 않았고, 기존 ChatGPT 탭과 로그인은 닫거나 초기화하지 않았다. 다음 실행에서도 과거 tab ID나 이 관찰을 현재 상태로 간주하지 말고 `openTabs() → 대상 대조 → claimTab()`을 새로 한다.
- **같은 탭의 packet 파일 관찰:** 관찰 당시 `https://chatgpt.com/` 기존 Chat 탭에 로그인 상태와 실제 `6 Pro` 선택이 보였고, user/assistant turn `0/0`, 빈 composer, `input.files` 0개였지만 `research_packet(20260924-172107).json` 타일 하나가 있었다. 다른 대화/탭으로 이동하지 않고 같은 composer의 해당 파일 타일만 눌러 BrowserUse visible download event로 확인했다. 받은 파일은 175,126 bytes, raw SHA-256 `e1d1c44edfd0467aeac3aff1bd362cbb927bf01da135e91f3d9d5cd39f81324f`로, C15의 exact local packet bytes와 일치했다. canonical packet hash도 durable packet hash `fa5845a055661c99c2ab1eb9cfb65f66fb84d2c85b267b3cde33b54843c320df`와 일치한다. 파일 타일의 동일성은 파일명 추정이 아니라 다운로드한 실제 bytes의 이중 hash로 확인한 것이다.
- 이 UI 증거는 “첨부 tile이 exact C15 packet이다”를 확인하지만 prompt 전송, Pro 요청, response/capture 또는 canary 성공을 뜻하지 않는다. 이번 동작은 파일 타일의 **다운로드 1회**였고, prompt 입력·submit·capture·새 대화·새 job/pass·query/fetch·다른 archetype·점수/Stage 변경은 0회다. 화면/다운로드 이벤트만으로 durable job을 바꾸지 않았다.
- 로컬 코드 candidate는 `input.files`가 이미 소비됐더라도 현재 composer 안의 정확한 단일 파일 버튼만 visible download event로 내려받아 raw SHA-256과 canonical hash를 모두 대조한다. hash 불일치, 이름 alias 불일치, 여러 첨부, 다른 composer/route, download 미관찰은 fail-closed다. 일치한 receipt는 같은 adapter 인스턴스에서만 재사용해 prepare 때 중복 upload를 막는다. 이 generic code path는 live ChatGPT에서 아직 실행하지 않았다.
- **로컬 검증:** Browser adapter의 비브라우저 mock recovery gate + BrowserUse bridge + fresh orchestration **118/118 PASS** (2026-09-25). `py_compile`, Node `--check`, `git diff --check`도 PASS. E2R v2 static audit **PASS / critical_count=0**, production static audit hash `930614b9868fcfba1cfb4455194beae4474ab23639344912b2445b516f2523be`. 브라우저 실행이 필요한 `ProFirstBrowserAdapterTest` 전체 묶음은 WSL의 Playwright Chromium process가 `libnspr4.so`를 찾지 못해 setup 단계에서 error가 났다. 이는 source assertion 결과가 아니며 이번 로컬 전체 adapter pass로 세지 않는다. exact-head GitHub Actions에서 변경분 전체 검증이 필요하다.
- **C15 durable state:** 마지막 read-only SQLite snapshot은 `PROJOB-df15a37c58ae7583924e58c0`, `USER_ATTENTION_REQUIRED` v26, `submit_count=0`, `capture_count=0`, browser/conversation binding 없음, prepare receipt 없음, `safe_unprepared_resume=false`였다. UI의 파일 hash 일치가 durable recovery permission을 대체하지 않는다. 재개 직전 DB row/event/version/hash를 다시 read-only 확인하고, same-tab proof와 교차 검사한다.
- **현재 코드/CI 위치:** pushed base head는 `cdf8f20478fdc1302730462d1e010c6b652b15b4`이며 해당 head의 Pro PR/push, V6 Actions는 SUCCESS였다. P100 변경은 현재 local candidate라 아직 그 원격 run에 포함되지 않았으며, static audit, 한글 commit/push, 변경 SHA의 exact-head CI는 다음 한 단계다. PR #7은 OPEN/DRAFT로 유지하고 merge/draft 해제를 하지 않는다.
- **다음 한 단계:** code+회귀시험+이 문서를 같은 feature branch에 한글 commit/push하고 새 exact-head Pro/V6 Actions가 끝날 때까지 기다린다. green 전에는 same-job prepare/resume/send를 하지 않는다. green 뒤에도 현재 durable job과 사용자의 기존 BrowserUse 로그인 탭을 각각 다시 확인한 후, 같은 탭의 exact attachment proof가 통과할 때만 다음 승인 경계를 판단한다.

## 역사적 상태 — P99, 2026-09-25 02:47 KST

- **로그인된 BrowserUse 세션 사용은 필수다.** 인증이 필요한 작업은 사용자가 이미 로그인해 둔 BrowserUse `extension`의 기존 세션에서만 한다. 작업 직전 `openTabs()`로 현재 탭을 다시 열거하고, URL·대화·계정·모드를 확인해 정확한 기존 탭 descriptor를 `claimTab()`한 뒤 claim이 반환한 바로 그 Tab 객체만 사용한다. 새 브라우저/창/탭/프로필/CDP 세션, 재로그인, 다른 대화로 재전송하는 우회는 하지 않는다. 같은 세션의 대상 탭을 연결하거나 확인하지 못하면 입력/첨부/다운로드/전송 전에 중단하고 실제 오류와 확인 범위만 기록한다. 과거 tab ID와 로그인 관찰은 현재 상태를 보장하지 않는다.
- P98의 C15 R6 실패는 로그인 문제로 판정하지 않았다. 당시 같은 로그인 탭에서 발생한 정확한 오류는 `BrowserUIIncompatible: the exact BrowserUse packet file/hash was not visible in the claimed tab`이다. 그 이후 재시도나 BrowserUse UI 조작은 이번 P99에서 하지 않았다.
- 코드 수정 가설: 앱이 파일을 받아 첨부 타일을 렌더링하며 `input.files`를 비울 수 있어, 타일 렌더링을 기다린 뒤 DOM `File`을 읽는 방식이 실패 원인일 수 있다. **아직 live UI에서 검증되지 않은 가설**이다. 수정은 로컬 packet raw SHA-256을 BrowserUse `FileChooser.setFiles(exact_path)` 전후 Windows 쪽에서 확인하고, 같은 SHA/파일명 선택 receipt를 Python 경계에서 검증하도록 했다. DOM File이 남아 있으면 canonical packet hash도 대조하며, 첨부 파일명의 화면 확인은 계속 요구한다. 이 경로가 실제 ChatGPT 탭에서 정확한 첨부로 수락되는지는 아직 미확인이다.
- 로컬 검증: BrowserUse bridge + fresh orchestration 관련 **113/113 tests PASS**; `py_compile`, Node `--check`, `git diff --check` PASS; E2R v2 static audit `PASS`, `critical_count=0`, audit hash `3bce37f9cc4b76787d1ccfe00fc2452e7a3d9a5cb6d80ab3774be9af1d923303`. 이는 현재 uncommitted local candidate의 검증이며 GitHub CI나 live BrowserUse 성공을 뜻하지 않는다.
- C15 durable 상태는 이 P99에서 재조회하지 않았다. 마지막 read-only snapshot(P98, 02:24 KST)은 `PROJOB-df15a37c58ae7583924e58c0`, `USER_ATTENTION_REQUIRED`, v26, submit/capture `0/0`, browser/conversation binding 없음, prepare receipt 없음, `safe_unprepared_resume=false`였다. 어떤 재개 전에도 DB row/event와 packet hash를 다시 read-only 확인해야 한다.
- PR #7은 마지막 확인 시 `OPEN/DRAFT/MERGEABLE`, pushed head `cbedcf2c5d7a7dcb946b3466623eebf0df23e0b7`였다. 그 head의 Pro PR run [36034866981](https://github.com/Daikisong/stock_agent/actions/runs/36034866981)은 `pending`, Pro push run [36034858436](https://github.com/Daikisong/stock_agent/actions/runs/36034858436)은 `in_progress`, V6 run [36034866695](https://github.com/Daikisong/stock_agent/actions/runs/36034866695)은 `SUCCESS`였다. 새 로컬 변경은 아직 이 head에 포함되지 않았으므로 새 한글 commit/push 뒤의 exact-head CI가 별도로 필요하다. PR은 draft 상태를 유지하고 이 목표에서 merge하지 않는다.
- P99에서는 브라우저를 연결하거나 탭을 열거/claim하지 않았고, UI 입력·첨부·다운로드·전송·capture도 하지 않았다. 새 query/fetch/job/pass, 다른 archetype, score/Stage 변경도 0이다.
- **다음 한 단계:** 이 수정과 본 handoff/progress 문서를 같은 PR #7 feature branch에 한글 commit/push하고 exact-head 필수 CI를 기다린다. CI가 green이면 그때 현재 durable job과 사용자의 기존 BrowserUse 로그인 탭을 각각 다시 확인한다. 탭 확인 실패 시 browser action 없이 멈춘다. 같은 탭에서 read-only recovery가 통과하고 exact attachment 경로를 확인하기 전에는 prompt 입력/전송하지 않는다.

## 역사적 상태 — P98, 2026-09-25 02:24 KST

- **인증 UI는 사용자의 기존 로그인 BrowserUse `extension` 세션과 기존 작업 탭에서만 한다.** 실행 때마다 `openTabs()`로 현재 탭을 확인하고, 서비스/계정/작업 대화를 대조해 정확한 descriptor를 claim한 뒤 반환된 동일 Tab 객체만 쓴다. 새 창·브라우저·탭·프로필·CDP 세션·재로그인으로 옮기지 않는다. 새 Chat이 필요하면 현재 로그인 탭 안에서만 시작한다. 목록/claim/대상 확인 실패 시 실제 오류와 확인 범위를 기록하고 입력 전에 정지한다.
- 최근 C15 R6 same-job 시도는 기존 로그인 탭에서 진행됐지만 exact packet filename/canonical hash visibility check가 실패했다. **이는 로그인 실패로 판정된 것이 아니다.** 현재 확인된 오류는 `BrowserUIIncompatible: the exact BrowserUse packet file/hash was not visible in the claimed tab`이며 root cause는 미확정이다. exact packet attachment는 성공으로 인정하지 않는다.
- 마지막 durable snapshot: `PROJOB-df15a37c58ae7583924e58c0`, `USER_ATTENTION_REQUIRED`, version `26`, `submit_count=0`, `capture_count=0`, browser/conversation/approval binding 없음, prepare receipt 없음, `safe_unprepared_resume=false`. prompt/send/capture는 없고 요청은 미전송이다. 다음 재개 전에 현재 SQLite row/event를 read-only로 다시 확인한다.
- 사후 read-only UI snapshot(2026-09-25 02:21 KST경): 기존 tab `1437795006`, ChatGPT root, 로그인 프로필 `대규 Pro`, `Chat`/`6 Pro`; composer 빈 값, user/assistant turn `0/0`, selected file `0`. 이건 기록 시각의 관찰이지 현재 탭 상태 보장이 아니다. 다음 동작 전에 반드시 목록을 재열거하고 재-claim한다.
- 해당 시도 뒤 PR #7 head `81224b05826bd3be4b24510301181ad385a8dd41`: Pro PR [36029814504](https://github.com/Daikisong/stock_agent/actions/runs/36029814504)와 V6 PR [36029816999](https://github.com/Daikisong/stock_agent/actions/runs/36029816999)은 `SUCCESS`; Pro push [36029817123](https://github.com/Daikisong/stock_agent/actions/runs/36029817123)은 02:24 KST 기준 `in_progress`였다. PR은 `OPEN/DRAFT/MERGEABLE`, 이 목표에서 merge/draft 해제하지 않는다.
- **다음 한 단계:** 동일 packet을 다시 첨부/전송하지 말고, 기존 job을 건드리지 않은 채 filename/content/hash visibility 경계를 코드/mock로 진단하고 회귀시험을 추가한다. 수정의 exact-head CI와 안전한 same-job 재개 조건이 확인된 뒤에만, 사용자의 현재 로그인 `extension` 탭을 다시 확인해 다음 동작을 판단한다.

상세 장애 타임라인/DB event/마지막 UI 관찰은 [P98 상세 BrowserUse handoff](../e2r_pro_first_v2/browseruse_existing_session_handoff_20260924.md#2026-09-25-0221-kst-기존-로그인-탭에서-same-job-packet-검증-실패), 전체 progress는 [P98 implementation progress](implementation_progress.md#p98--기존-로그인-browseruse-탭에서-c15-packet-검증-실패-및-재개-상태-갱신-2026-09-25-0224-kst)를 본다.

P95 및 그 이전 기록은 역사적 checkpoint다. 현재 C15 상태와 다음 한 단계는 이 문서 상단 P98만 기준으로 한다.

## P95 — 사용자의 로그인 세션 사용 지시 재확인 (2026-09-24 20:47 KST)

사용자가 다시 명확히 요청했다: 인증이 필요한 BrowserUse 작업은 **이미 로그인되어 있는 사용자의 세션 쪽에서** 해야 한다. 이 프로젝트의 다음 인증 UI 작업은 아래 한 경로만 따른다.

```text
현재 Codex 세션의 BrowserUse 연결 확인
→ 사용자의 기존 Chrome `extension` 세션
→ openTabs()로 실제 열린 탭 열거
→ 대상 서비스/작업과 정확히 일치하는 기존 탭 descriptor 선택
→ claimTab() 반환 객체 하나만 계속 사용
→ 입력/첨부/다운로드/전송 직전에 같은 탭과 현재 상태 재확인
```

- 사용자가 로그인한 기존 탭을 쓰며, 새 Chrome/창/탭/프로필, 별도 CDP 연결, 재로그인으로 대체하지 않는다. “새 Chat”은 새 브라우저 세션을 뜻하지 않는다. 정말 새 대화가 필요하면 로그인된 기존 탭 안에서만 만든다.
- 기존 응답이나 Library 파일이 이미 있으면 새 요청을 다시 보내지 말고 같은 탭에서 회수한다. 전송이 필요하면 기존 durable job의 approval/exactly-once gate도 별도로 통과해야 한다.
- extension 연결, 대상 탭 claim, 로그인/작업 대상 확인에 실패하거나 화면 상태가 예상과 다르면 상호작용을 중단한다. 실제 오류 문자열, 확인한 범위, 전송 등 실제 실행 여부만 기록하고 세션을 바꿔 우회하지 않는다.
- BrowserUse preflight 성공이나 다른 브라우저에서 탭이 보이지 않는 사실만으로 연결/로그인 상태를 단정하지 않는다. 인증 정보·쿠키·토큰은 기록하지 않는다.
- 이번 P95 문서 갱신은 저장소 문서만 수정했다. BrowserUse 연결, 탭 열거, 화면 확인, 입력/첨부/다운로드/전송은 수행하지 않았다. 다음 C15 same-job recovery 전에 P94에 기록된 CI 상태를 다시 확인하고, 위 same-session 절차로 새로 관찰한다.

이 지시는 새 작업이 시작될 때마다 적용한다. 이전 탭 관찰 결과를 현재 상태로 재사용하지 않는다.

## P94 — C06 live full-thesis receipt 재검산 및 P93 정정 (2026-09-24 20:44 KST)

P93에서 C06 pass row의 `score_valid=0` 및 pass 19 detail의 `research_status=RESEARCH_RUNNING`을 전체 canary 미증명 근거로 쓴 판단은 **잘못되었고 여기서 정정한다**. 두 필드는 pass-local 레코드다. `pro_research_passes` schema 자체가 `score_valid=0` 및 `publication_withheld=1`만 허용하며, 이후 생성된 독립 hashed saturation receipt와 final score/StageCourt receipts가 completion authority다. `full_thesis_eligibility`는 score/Stage 권한을 갖지 않고 scorer 전에는 `score_valid=false`, `FULL_THESIS_SCORE_PENDING`으로 기록하는 gate receipt다. deterministic scorer의 `production_score_authority=true` 및 StageCourt의 `production_stage_authority=true`는 별도 권한 계층이므로 nested eligibility의 false와 모순이 아니다.

### 현재 C06의 직접 증거

2026-09-24 20:42 KST에 runtime 파일과 DB를 읽기 전용으로 다시 대조했다. Runtime job root는 `C:\Users\eorb9\AppData\Local\E2R\ProFirstRuntime\fresh_v2_1\20260828T203034Z\jobs\PROJOB-287556cc59c10f124d615c4d`이고, durable DB snapshot은 `live_v2\20260823T145430Z\pro_first.sqlite3`다.

| Gate | 저장된 증거 |
|---|---|
| Multi-pass | 동일 job, 동일 conversation, 동일 approval scope에 19개 submitted pass row. Pass roster에는 PUBLIC_GAP_CLOSURE, VERIFIER_REPAIR, SATURATION_AUDIT가 있고, 일부 transport `FAILED_HARD` 이후에도 후속 pass가 완료됨 |
| Saturation | `research_saturation_receipt.json`: `FULL_THESIS_READY`, hash `34416085416b25dfefcc09b1891dfe0740063d45833bea7a229a41664a0d24e7`, 28/28 mandatory question decisions, nonterminal/public gap/verifier/provider-parser/lifecycle/source-linkage blocker 각각 0, `component_entry_allowed=true` |
| Question outcomes | `SUPPORTED_NON_SCORING` 16, `PARTIALLY_SUPPORTED_SCORING` 7, `COUNTER_SUPPORTED` 1, `EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH` 2, `NOT_APPLICABLE_WITH_REASON` 2 |
| Full-thesis canary | `fresh_v3_full_thesis_receipt.json`: `FRESH_V3_FULL_THESIS_FINAL`, job `FINAL`, saturation valid, public gap 0, repair/provider/lifecycle/source-linkage blocker 0, `hidden_chatgpt_api_used=false` |
| Score/StageCourt | 56 accepted claims; component 7/7; Judge 21/21; deterministic score `23.275`, `score_valid=true`, `full_score_valid=true`; AtomicStageCourt decision `FINAL`, canonical Stage `0` |

따라서 C06은 **실제 Pro multi-pass research → saturation → component/Judge → deterministic score → StageCourt** canary로 통과했다. “P93에서 canary를 보류했다”는 문장을 현재 판정으로 사용하지 않는다. 000660 frozen-MD partial-corpus replay와는 별도 run이며, 그 replay의 partial guard 결과를 변경하지 않는다.

### 남은 publish 경계

- 이 fresh live-canary runner는 `ProScoringPipelineService.run_job()` 뒤 full-thesis receipt만 만들고 종료한다. 현재 해당 job의 `published_at`은 null이고 `pro_publications` row도 없다. 즉 C06 canary는 score/StageCourt까지 증명했지만 **이 run만으로 publish를 증명하지는 않는다**.
- 일반 `ProFirstPostImportCoordinator`는 `FINAL`에서 `ProResultPublisher.publish()`를 호출한다. unit/integration 경로가 그 full-thesis/partial-withheld 동작을 검증하는지 별도로 audit한다. historical canary를 실제 dashboard에 publish하거나 runtime DB를 변경하지 않았다.
- C06은 goal의 actual live full-thesis canary 3개 중 **1/3**로 센다. C17/C28 live full-thesis canary와 exact-head Pro CI는 여전히 미완료다.

### exact-head CI 재확인

2026-09-24 20:44 KST, code head `100346caf0a31886e9aff6d1a0ef65e22e6820b6`에서 V6 run [35992525826](https://github.com/Daikisong/stock_agent/actions/runs/35992525826)은 `SUCCESS`; Pro push [35992521406](https://github.com/Daikisong/stock_agent/actions/runs/35992521406)과 Pro PR [35992525796](https://github.com/Daikisong/stock_agent/actions/runs/35992525796)은 `full-regression` 진행 중이다. PR #7 latest ref는 문서 전용 commit `f648cd3f179ea47d4f15855efb518b18270d892f`, draft/open이며 main은 미병합이다. `CLEAN`/`UNSTABLE` mergeability 표시는 CI 결론을 대체하지 않는다.

이번 P94는 Windows runtime DB와 artifact에 read-only로 접근했다. BrowserUse UI, input/attachment/submit/capture, query/fetch, new job/pass, score/Stage/publication 변경은 0이다. 다음 순서는 exact Pro CI가 끝날 때까지 확인하고, 그 후 C15 existing-job same-tab recovery proof를 진행하는 것이다. 인증 UI가 필요하면 이 문서 상단의 기존 로그인 `extension` 세션·동일 탭 규칙만 사용한다.

## P93 — 세션 규칙 재확인 및 현재 blocker handoff (2026-09-24 20:31 KST; C06 결론은 P94에서 정정)

### 로그인 세션에 대한 사용자 요청 — 실행 시 최우선

- 인증이 필요한 BrowserUse 작업은 반드시 사용자가 이미 로그인한 BrowserUse `extension` 세션과 그 안의 기존 대상 탭에서 한다. Pro 모드 대화 입력·파일 첨부·Library 다운로드도 예외가 아니다.
- 새 Chrome/창/탭/프로필/CDP 세션을 열어 대신 작업하거나, 새 로그인·다른 대화에서 같은 요청을 다시 보내는 것은 금지한다. 새 Chat 대화가 꼭 필요하면 기존 로그인 탭 안에서 시작한다.
- 작업 직전 `openTabs()`로 현재 탭을 다시 확인하고 대상 descriptor를 정확히 `claimTab()`한 뒤, 그 반환 객체만 사용한다. 사전 점검 성공은 실제 세션 연결이나 로그인 확인을 뜻하지 않는다.
- 현재 연결에서 기존 세션·대상 탭을 읽고 조작할 수 없으면 즉시 멈춘다. 마지막으로 확인한 범위와 도구의 정확한 오류만 기록한다. 창·탭을 바꾸거나 재전송해 우회하지 않는다.
- 이 P93 문서 갱신에서는 BrowserUse를 연결하거나 브라우저 화면을 읽지 않았다. 앞선 P92 탭 관찰을 현재 상태로 간주하지 않는다. 다음 인증 작업 직전에 위 절차를 다시 수행한다.

### 현재 저장소·CI 상태

- PR #7은 `OPEN`, `DRAFT`, head `100346caf0a31886e9aff6d1a0ef65e22e6820b6`이며 `main`에는 병합되지 않았다. 2026-09-24 20:31 KST에 GitHub 상태는 `mergeStateStatus=UNSTABLE`이었다.
- 이 exact head의 GitHub Actions는 아직 전부 성공 완료가 아니다: Pro push run [35992521406](https://github.com/Daikisong/stock_agent/actions/runs/35992521406)은 `in_progress` (core-unit, browser-mock-e2e, static-security 성공; full regression 진행 중), Pro PR run [35992525796](https://github.com/Daikisong/stock_agent/actions/runs/35992525796)은 `in_progress` (full regression, browser-mock-e2e, core-unit jobs 진행 중), V6 run [35992525826](https://github.com/Daikisong/stock_agent/actions/runs/35992525826)은 `in_progress` (전체 unit suite 실행 중). 완료 판정이나 canary 작업 재개 조건으로 사용하지 않는다.
- goal acceptance의 live full-thesis canary는 미완료다. PR CI가 끝나기 전에 BrowserUse에 prompt 입력·첨부·전송을 하지 않는다. 인증 세션을 쓸 때도 기존 세션·기존 탭 원칙은 그대로 적용한다.

### C06 receipt authority/status 정합성 — 미해결, canary 성공으로 집계 금지

2026-09-24 20:25 KST에 Windows runtime DB를 `mode=ro` 및 `PRAGMA query_only=ON`으로 읽어 C06 / 000660 최신 job `PROJOB-287556cc59c10f124d615c4d`를 재확인했다. job row는 `FINAL`이고 pass 19개지만 아래 authority/terminal 값의 계층 간 관계가 확인되지 않았다.

| 근거 위치 | 관찰값 |
|---|---|
| pass receipts 19개 | 모두 `score_valid=0`, `publication_withheld=1`; 마지막 pass는 `SATURATION_AUDIT / COMPLETE`이나 `research_status=RESEARCH_RUNNING` |
| score receipt 상위 필드 | `score_valid=true`, `production_score_authority=true`; 결정론 점수 `23.275` 및 내부 scorer audit의 `full_score_valid=true` |
| 같은 receipt의 `full_thesis_eligibility` | `status=FULL_THESIS_SCORE_ELIGIBLE`와 동시에 `score_valid=false`, `score_authority=false`, `stage_authority=false`, `stage_status=FULL_THESIS_SCORE_PENDING`, `publication_status=WITHHELD_UNTIL_DETERMINISTIC_STAGECOURT` |
| StageCourt receipt | decision은 `FINAL`, canonical stage `0`, 점수 `23.275`; receipt 필드는 `production_score_authority=false`, `production_stage_authority=true` |

이 필드들은 서로 다른 authority 계층을 뜻할 수도 있어 현재 스냅샷만으로 코드 결함이라고 단정하지 않는다. 다만 `job.status=FINAL`, score receipt 단독 `score_valid=true`, 또는 StageCourt `decision_status=FINAL`만으로 C06 live full-thesis canary를 통과 처리하지 않는다. `full_thesis_eligibility`와 producer authority 관계 및 `RESEARCH_RUNNING` terminal status의 대응을 코드/receipt 계보에서 확인하기 전까지 C06은 **판정 보류**다. runtime DB는 읽기 전용으로 확인했으며 고치거나 점수·Stage를 바꾸지 않았다.

### 다음 한 단계

1. exact head의 Pro push, Pro PR, V6 Actions가 모두 종료될 때까지 확인한다.
2. C06 receipt authority/status 계층을 source code와 receipt 생성 순서에서 추적한다. 의미 관계를 확인하기 전에는 C06을 canary PASS로 세지 않는다.
3. 승인·same-job recovery gate가 허용할 때만 기존 로그인 BrowserUse 탭에서 기존 durable job을 이어간다. 새 browser/session이나 중복 job/전송으로 우회하지 않는다.

이번 P93 기록은 DB read-only 확인과 문서화만 수행했다. BrowserUse 조작, prompt/attachment/download/submit/capture, query/fetch, 새 job/pass, 점수/Stage 변경은 모두 0이다. P92 아래 기록은 당시 snapshot으로 보존하며, 현재 상태와 충돌하면 이 P93 handoff가 우선한다.

## P92 — 기존 로그인 탭과 same-job recovery 재개 지점 (2026-09-24 20:17 KST; historical snapshot)

- **로그인 세션:** WSL BrowserUse preflight exit `0`. persistent `mcp__node_repl__js`의 canonical bootstrap에서 `extension` 연결이 성공했다. `openTabs()`로 사용자가 이미 열어 둔 탭 2개를 확인했고, 그중 기존 `https://chatgpt.com/` / `ChatGPT` 탭 descriptor를 정확히 claim해 이후 read-only 검사에 같은 반환 tab 객체를 썼다. 새 창·브라우저·탭·프로필·CDP 세션, 재로그인, navigation은 없었다. 탭 ID·쿠키·토큰은 기록하지 않는다.
- **현재 화면의 read-only 증거:** login password input `0`, visible composer `1`이 빈 상태, user/assistant message `0/0`, file input `5` 중 선택 파일 `0`. 계정 표시 `Pro`, model control label `6 Pro`가 보였다. 이는 현재 기존 탭에서 읽은 UI 상태이며, native chooser의 현재 상태나 어떤 canary turn이 실제 전송됐다는 증거는 아니다. prompt 입력·첨부·다운로드·submit/capture는 모두 0이다.
- **미완료 C15 same-job:** Windows 중앙 SQLite를 `mode=ro` + `PRAGMA query_only=ON`으로 확인했다. `PROJOB-df15a37c58ae7583924e58c0`, C15 / `010950`, `USER_ATTENTION_REQUIRED`, version `20`; packet hash `fa5845a055661c99c2ab1eb9cfb65f66fb84d2c85b267b3cde33b54843c320df`; submit/capture `0/0`; browser/conversation binding 및 approval binding 없음; successor 없음. 최신 event의 `safe_unprepared_resume=false`, stage `DRAFT_PREPARATION_OR_UNKNOWN`는 그대로다.
- **P92 recovery 코드:** commit `43251f9d29f3d003da96996adcc612b12becaae2`는 실제로 저장된 legacy PowerShell CLIXML chooser 오류와 새 구조화 chooser 실패만 좁게 same-tab read-only recovery gate의 후보로 허용한다. 이 허용만으로 job을 준비/전송하지 않는다. 기존 `_load_unprepared_attention_job`의 packet/job identity, zero submit/capture, 미결박 approval/browser/conversation, prepare receipt 부재 검사를 통과하고, 그 뒤에도 same claimed `extension` tab에서 exact packet hash·로그인/실제 `6 Pro`·new-chat route·빈 composer·turn 0·Stop 0·닫힌/owner 불명 native chooser 0·선택 파일 없음 또는 hash가 일치하는 exact packet을 read-only로 검증해야 한다. durable state가 중간에 바뀌어도 실패 처리한다. 성공해도 기존 job에서 **prepare only**, submit은 별도 approval gate 전까지 0이다.
- **검증:** fresh orchestration + BrowserUse bridge `107/107 PASS`, P92 static audit `PASS / critical_count=0`, compile/diff 검사 PASS. 이 작업 시점의 origin head `8184f38f831909649caac66bec5da1c2f44c5e4b`에서는 Pro push [35990247608](https://github.com/Daikisong/stock_agent/actions/runs/35990247608), Pro PR [35990252048](https://github.com/Daikisong/stock_agent/actions/runs/35990252048), V6 PR [35990251811](https://github.com/Daikisong/stock_agent/actions/runs/35990251811)이 아직 full regression/unit suite 진행 중이었다. 이 run들은 P92 commit을 포함하지 않으며 P92 CI green으로 표현하지 않는다.
- **다음 한 단계:** 두 P92 한글 커밋을 PR #7에 push한 뒤 그 exact head의 Pro push·Pro PR·V6 PR CI를 확인한다. 모두 성공한 뒤에만 같은 BrowserUse 로그인 탭을 다시 열거·claim해 C15 R6 durable identity와 native-dialog 포함 read-only recovery proof를 실행한다. 증명 전에는 packet/prompt를 쓰지 않는다. 성공 시에도 새 job이 아니라 이 exact job에서 prepare only로 멈춘다. 새 창·세션·재로그인으로 우회하지 않는다.
- 전체 실행 기록은 [implementation progress P92](implementation_progress.md#p92--기존-로그인-browseruse-세션-재확인과-chooser-복구-gate-보강-2026-09-24-2017-kst)에 있다. P91 아래는 당시 상태 이력이며 충돌 시 이 P92 handoff가 우선한다.

## P91 checkpoint — historical (P92가 현재 판정)

- **세션 지침:** 인증이 필요하면 기존 BrowserUse `extension` 연결 → `openTabs()` → 작업과 일치하는 descriptor를 `claimTab()` → claim이 반환한 바로 그 tab 객체만 사용한다. 기존 로그인 탭을 확인할 수 없다면 멈춘다. 이번 P91은 문서·코드·로컬 테스트 작업뿐이며 브라우저 UI를 연결하거나 조작하지 않았다. 따라서 live 탭의 현재 상태는 P90 이후 새로 확인한 것으로 취급하지 않는다.
- **P91 코드 변경:** Windows native chooser bridge가 구조화된 `E2R_FILE_CHOOSER_RESULT` marker로 단계/오류 ID/category/message를 반환하고 PowerShell progress stream은 억제한다. JavaScript 쪽은 structured result와 exit code를 함께 검증하며, marker 누락/잘못된 JSON/성공 marker와 비정상 종료는 모두 실패로 처리한다. 진단 문자열은 제한 길이로 자르고 packet 경로를 숨긴다. 예상 밖 dialog control이 보일 때 취소 버튼을 자동 클릭하는 동작을 제거해 사용자 창을 임의 조작하지 않는다.
- **재개 안전성:** chooser 선택 실패는 같은 unsent job을 자동 재개 가능하게 바꾸지 않는다. 회귀 테스트는 `safe_unprepared_resume=false`인 같은 job에서 prepare receipt 생성, browser/conversation binding, submit/capture가 계속 차단되는지 확인한다. 이 코드 변경은 과거 실제 첨부 실패의 원인을 확정하거나 해당 job을 재개 승인하지 않는다.
- **로컬 검증:** bridge + fresh orchestration focused suite `105/105 PASS`; Pro-first static audit `PASS`, `critical_count=0`; `node --check`와 `git diff --check` PASS. 전체 master-goal acceptance battery는 374건 중 371 PASS, 3건 ERROR이며 모두 이 WSL 환경에서 Playwright Chromium이 `libnspr4.so`를 찾지 못한 browser-fixture setup 오류다. full unittest discover도 해당 시스템 라이브러리 누락으로 끝까지 검증되지 않았고 exit 137로 종료됐다. 이를 테스트 전체 성공이나 제품 실패로 표현하지 않는다. GitHub Actions는 CI dependency install이 포함된 exact code head에서 다시 확인해야 한다.
- **현재 live 증거의 한계:** 마지막 실제 기존 로그인 탭 및 durable C15 R6 검사는 P90 (19:29 KST) 기록이다. 그때 same tab은 로그인된 ChatGPT/Pro로 read-only 관찰됐지만 chooser는 닫혀 있었고, 같은 C15 R6 job `PROJOB-df15a37c58ae7583924e58c0`은 `USER_ATTENTION_REQUIRED`, state version 20, submit/capture `0/0`, `safe_unprepared_resume=false`였다. 이는 P91 현재 화면 증거가 아니며, 새 코드도 durable gate를 덮어쓰지 않는다.
- **다음 한 단계:** 변경분과 문서를 PR #7 branch에 한글 commit/push하고 새 exact-head CI를 확인한다. CI가 green이더라도 live UI 작업을 할 때는 먼저 동일 BrowserUse 로그인 세션의 기존 탭을 다시 열거·claim하고, 같은 job의 durable identity/recovery gate를 read-only로 확인한다. 기존 탭을 쓸 수 없거나 gate/상태가 불명확하면 멈춘다. 새 창·세션·재로그인은 사용하지 않는다.
- 상세 구현과 실행 기록은 [implementation progress P91](implementation_progress.md#p91--기존-로그인-browseruse-세션-원칙과-첨부-오류-진단-보강-2026-09-24-1954-kst)에 있다. P90 아래는 당시 관찰의 기록이며, 충돌 시 이 P91 handoff가 우선한다.

## P90 checkpoint — historical (P91이 현재 판정)

- **로그인이 필요한 작업은 사용자가 이미 로그인해 둔 BrowserUse `extension` 세션의 기존 ChatGPT 탭에서만 한다.** 이번 확인은 persistent BrowserUse 세션에서 이미 claim해 둔 동일 tab 객체만 사용했다. 새 브라우저·창·탭·프로필·CDP 세션, 재로그인, 탭 이동/재전송은 없었다. 사용자의 창과 세션은 열린 채 보존한다.
- 같은 탭의 읽기 전용 DOM 확인: `https://chatgpt.com/`, 로그인 prompt 없음, 계정 `Pro` 표시와 화면의 `6 Pro` control, 빈 composer, user turn 0, packet 파일명 미표시, file input 5개 모두 선택 파일 0. native chooser inspector도 동일 extension 탭에 연결해 조회했다. 첫 worker 실행은 작업 경로의 `PYTHONPATH` 누락으로 `ModuleNotFoundError: No module named 'e2r'`를 반환했다. `PYTHONPATH=src`를 지정한 재실행 결과는 `open=false`, `chrome_owned_dialog_count=0`, `unknown_owner_count=0`이다. 이는 **검사 시점**만 설명하며 이전 첨부 실패의 결과를 소급 입증하지 않는다.
- 중앙 SQLite를 `mode=ro`와 `PRAGMA query_only=ON`으로 확인했다. 같은 C15 R6 `PROJOB-df15a37c58ae7583924e58c0` / S-Oil `010950` / packet hash `fa5845a055661c99c2ab1eb9cfb65f66fb84d2c85b267b3cde33b54843c320df`는 `USER_ATTENTION_REQUIRED`, state version 20이다. `submit_count=0`, `capture_count=0`, approval/browser/conversation binding은 모두 null, `superseded_by_fresh_job_id=null`이다. 최신 event는 `BROWSER_PREPARING → USER_ATTENTION_REQUIRED`, event time `2026-09-24T10:21:46.569280Z`, `DRAFT_PREPARATION_OR_UNKNOWN`, `safe_unprepared_resume=false`, `automatic_resubmit_allowed=false`다.
- same-job 첨부 시도의 영속 오류는 `BrowserUseBridgeError: BRIDGE_OPERATION_FAILED: existing Chrome file chooser did not select the packet (exit=1; #< CLIXML …)`다. DB에 저장된 상세 문자열은 PowerShell CLIXML 출력부터 잘려 있어 실제 선택 실패 원인은 확정하지 않았다. 현재 검사에서 파일 선택창이 닫혀 있어도 이전 시도에서 packet이 선택되지 않았다고 단정하지 않는다. durable gate가 `safe_unprepared_resume=false`이므로 동일 packet 재첨부·prompt 재입력·재전송은 금지한다.
- 이번 확인 중 BrowserUse 입력·첨부 재시도·다운로드·submit/capture, navigation, 새 job/pass, source query/fetch, score/Stage 변경은 0이다. 첫 worker의 `PYTHONPATH` 오류는 읽기 전용 검사 실행 문제이며 로그인 실패나 정책 거부가 아니다.
- PR #7은 확인 시 OPEN/DRAFT/MERGEABLE, base `main`, 미병합이었다. 기준 branch/document head는 `d88f6ff41546b8396fa21128c0612ca4df24272e`; 코드 검증 head `c4155c5ca6f75602928d123c48446c08160860a8`의 Pro push [35982213116](https://github.com/Daikisong/stock_agent/actions/runs/35982213116), Pro PR [35982218832](https://github.com/Daikisong/stock_agent/actions/runs/35982218832), V6 PR [35982218910](https://github.com/Daikisong/stock_agent/actions/runs/35982218910)은 모두 SUCCESS였다. P90은 문서 갱신이며 이 green run을 새 문서 SHA의 CI로 표현하지 않는다.
- **다음 한 단계:** 첨부 실패를 코드/mock 경로에서 원인 분리하고 ambiguous chooser 결과를 다루는 회귀 검증을 보강한 뒤 기존 PR #7 branch의 exact-head CI를 확인한다. 그 전에 사용자 탭에서 재첨부/전송하지 않는다. live 재개가 안전해지면 기존 BrowserUse 세션에서 같은 탭을 다시 열거·claim하고 durable identity와 read-only gate를 대조한다. 상태가 불명확하면 중단하며 새 세션으로 우회하지 않는다.
- 상세 실행 경계와 P90 증거는 [implementation progress P90](implementation_progress.md#p90--기존-로그인-browseruse-세션의-same-job-첨부-오류와-파일-선택창-읽기-전용-확인-2026-09-24-1929-kst)을 따른다. 아래 P89/P86 블록은 과거 체크포인트이며 충돌 시 P90이 우선한다.

## P89 checkpoint — historical (P90이 현재 판정)

- **사용자 로그인 세션 원칙은 바뀌지 않는다.** BrowserUse가 필요한 다음 단계는 사용자가 이미 로그인해 둔 BrowserUse Chrome `extension` 연결에서 시작한다. `browser.user.openTabs()`로 기존 탭을 다시 열거하고, 대상 작업 대화와 일치하는 정확한 descriptor를 `browser.user.claimTab()`에 넘긴다. 이후 read-only 확인부터 결과 회수까지 claim이 반환한 같은 tab 객체만 쓴다. 새 Chrome/창/탭/프로필/CDP 세션, 재로그인, 다른 대화에서의 재전송·재다운로드는 하지 않는다.
- **P89 문서 갱신에서는 브라우저 UI를 호출하거나 조작하지 않았다.** 마지막 실제 existing-session 화면 관찰은 P88의 2026-09-24 18:32 KST 검사다. 그 시점에 기존 `https://chatgpt.com/` ChatGPT 탭을 claim하여 login prompt 없음, `6 Pro` 표시, 빈 composer, user turn 0, 선택 파일 0을 read-only 확인했다. 이를 P89 현재 화면 상태로 간주하지 않으며, 다음 작업 때 같은 세션에서 다시 확인한다.
- PR #7은 OPEN/DRAFT/MERGEABLE, base `main`, 미병합이다. 문서 전용 커밋 push 이후 현재 local/origin branch HEAD는 모두 `42df5bad8bc709f68520394c56298f46a576f04b` (`P89 기존 로그인 BrowserUse 세션 인수인계 문서화`)다. **코드 검증 head는 직전 `c4155c5ca6f75602928d123c48446c08160860a8`** (`BrowserUse 재개 오류 매칭과 로그인 세션 인수인계 보강`)다.
- 코드 검증 head `c4155c5…`의 GitHub Actions를 2026-09-24 19:01 KST에 조회했다. Pro push [35982213116](https://github.com/Daikisong/stock_agent/actions/runs/35982213116), Pro PR [35982218832](https://github.com/Daikisong/stock_agent/actions/runs/35982218832), V6 PR [35982218910](https://github.com/Daikisong/stock_agent/actions/runs/35982218910)이 모두 `completed / success`다. `42df5bad…`는 문서 두 개만 바꾼 후속 commit이며 해당 SHA에서 별도 Actions run은 생성되지 않았다.
- C15 R6 durable job의 마지막 DB 증거도 P88 mode=ro + `PRAGMA query_only=ON` 검사다: `PROJOB-df15a37c58ae7583924e58c0`, S-Oil `010950`, `USER_ATTENTION_REQUIRED` v18, packet hash `fa5845a055661c99c2ab1eb9cfb65f66fb84d2c85b267b3cde33b54843c320df`, submit/capture `0/0`, browser/conversation binding 없음, `safe_unprepared_resume=false`. 다음 UI 작업 전에 durable state를 다시 read-only 조회하고 same-tab proof와 exact identity를 대조해야 한다. 화면만 보고 재개 안전성을 추론하지 않는다.
- **사용자 로그인 세션 원칙은 바뀌지 않는다.** BrowserUse가 필요한 다음 단계는 사용자가 이미 로그인해 둔 BrowserUse Chrome `extension` 연결에서 시작한다. `browser.user.openTabs()`로 기존 탭을 다시 열거하고, 대상 작업 대화와 일치하는 정확한 descriptor를 `browser.user.claimTab()`에 넘긴다. 이후 read-only 확인부터 결과 회수까지 claim이 반환한 같은 tab 객체만 쓴다. 새 Chrome/창/탭/프로필/CDP 세션, 재로그인, 다른 대화에서의 재전송·재다운로드는 하지 않는다.
- **P89 문서 갱신에서는 브라우저 UI를 호출하거나 조작하지 않았다.** 마지막 실제 existing-session 화면 관찰은 P88의 2026-09-24 18:32 KST 검사다. 그 시점에 기존 `https://chatgpt.com/` ChatGPT 탭을 claim하여 login prompt 없음, `6 Pro` 표시, 빈 composer, user turn 0, 선택 파일 0을 read-only 확인했다. 이를 P89 현재 화면 상태로 간주하지 않으며, 다음 작업 때 같은 세션에서 다시 확인한다.
- C15 R6 durable job의 마지막 DB 증거도 P88 mode=ro + `PRAGMA query_only=ON` 검사다: `PROJOB-df15a37c58ae7583924e58c0`, S-Oil `010950`, `USER_ATTENTION_REQUIRED` v18, packet hash `fa5845a055661c99c2ab1eb9cfb65f66fb84d2c85b267b3cde33b54843c320df`, submit/capture `0/0`, browser/conversation binding 없음, `safe_unprepared_resume=false`. 다음 UI 작업 전에 durable state를 다시 read-only 조회하고 same-tab proof와 exact identity를 대조해야 한다. 화면만 보고 재개 안전성을 추론하지 않는다.
- P89에서 새 ChatGPT 입력·첨부·전송·다운로드, research query/fetch, 새 job/pass, score/Stage 변경은 하지 않았다. 기존 로그인 세션은 유지하며 종료·초기화하지 않는다.
- 상세 진행은 [implementation progress](implementation_progress.md)의 P89 항목을 따른다. P88 이하 블록은 기록 시점의 역사이며, 충돌하면 이 P89 지침이 우선한다.

## P86 확인 기록 — historical (P89가 현재 판정)

이 P86 checkpoint는 17:10 KST 당시의 기록이다. 아래 P83/P84/P80/P81 등 이전 체크포인트도 당시 이력이며 현재 다음 단계에는 적용하지 않는다.

**로그인이 필요한 작업이면 사용자가 이미 로그인해 둔 BrowserUse Chrome `extension` 세션에서 기존 작업 탭을 찾아, 그 정확한 탭에서 진행한다.** 새 창·새 탭·새 프로필·별도 CDP 세션을 만들거나 다시 로그인하는 것은 대체 방법이 아니다. 기존 탭을 찾거나 claim할 수 없으면 브라우저 작업을 멈추고 실제 오류와 확인 범위를 문서화한다. “새 Chat”이 필요해도 같은 로그인 탭 안에서만 연다.

- **P86에서 실제로 확인한 세션:** 이미 로그인된 BrowserUse `extension`에서 열거한 사용자의 기존 ChatGPT 탭 하나를 계속 사용했다. 새 browser/window/tab/profile/CDP session을 만들거나 재로그인하지 않았다. 해당 탭의 읽기 전용 관찰에서는 로그인 prompt 없음, 실제 `Pro`, 빈 composer, user turn 0, 빈 파일 input 5개, 화면상 packet 이름 없음이었다.
- 같은 세션의 read-only Windows UI Automation 검사에서 top-level window 24개를 열거했고, Chrome 소유 `Open` dialog 후보 0개, 소유자를 판별하지 못한 후보 0개였다. 이는 **검사 시점**의 상태만 말하며, 앞선 attach 시도에서 어떤 결과가 났는지를 소급 증명하지 않는다. 창/탭은 닫거나 조작하지 않았다.
- 해당 탭의 `tab.dev.logs()`에는 `2026-09-24T07:27:36.329Z`의 React `RecoverableError: Minified React error #418` 한 건이 있었다. 같은 시간대 관찰만으로 이번 attach timeout의 원인이라고 단정할 수 없다.
- durable C15 R6 job `PROJOB-df15a37c58ae7583924e58c0`은 마지막 read-only SQLite 확인 시 `USER_ATTENTION_REQUIRED`, version 18, `submit_count=0`, `capture_count=0`, browser/conversation binding 없음, successor 없음이다. 최신 event는 `DRAFT_PREPARATION_OR_UNKNOWN`, `safe_unprepared_resume=false`, `automatic_resubmit_allowed=false`; packet hash는 `fa5845a055661c99c2ab1eb9cfb65f66fb84d2c85b267b3cde33b54843c320df`다. **이 durable 차단을 live 화면 관찰만으로 덮어쓰지 않는다.**
- 마지막 첨부 RPC의 실제 오류는 다음과 같다. 이것은 파일이 첨부되지 않았거나 전송되지 않았다는 증거가 아니다.

```text
BrowserUseBridgeError: BrowserUse bridge transport failed (TimeoutError: timed out)
```

- 직전 오류 시점의 durable snapshot (`2026-09-24T07:28:13.906437Z`, mode=ro 및 `PRAGMA query_only=ON`)은 그대로 기록한다. 그 당시에는 native chooser를 확인하지 못했으므로 안전한 재개 여부를 알 수 없었다. P86의 후속 read-only UI Automation 결과는 현재 검사 시점의 열린 대화상자 유무를 보완할 뿐, durable job의 `safe_unprepared_resume=false`를 바꾸지 않는다.
- 코드에서 확인한 timeout은 BrowserUse RPC 기본 30초, Windows file chooser polling 45초다. 불일치가 원인일 가능성은 있지만 이번 timeout의 근본 원인으로 입증되지는 않았다. P86 변경은 packet-attach RPC만 60초로 늘리고 다른 RPC의 기본 timeout은 유지한다.
- **재개는 아래 코드·회귀 검증이 원격 exact-head CI까지 통과하기 전에는 하지 않는다.** CI 이후에도 exact same-job / same-session read-only gate가 통과해야 한다. gate는 packet hash, existing ChatGPT new-chat route, 로그인, 실제 Pro, 빈 composer, user turn 0, stop 없음, Chrome file chooser 닫힘/owner 불명 없음, 선택 파일이 없거나 exact packet hash의 visible file임을 검사한다. proof 전에는 navigation·upload·prompt 입력·submit을 하지 않고, durable job이 바뀌었으면 중단한다.
- 이번 recovery 분석에서 새 job, source query/fetch, prompt 전송, response capture, 점수/Stage 변경은 0이다.

### P86 코드·검증·다음 한 단계

- `BrowserUseBridgeClient`의 packet attach RPC만 60초 timeout을 받도록 바꾸고, native picker의 45초 wait를 공유 상수로 명시했다. 같은 `extension` page에 read-only native file chooser inspector를 추가했다. owner가 불명확하면 fail closed한다.
- exact historical attach timeout은 live recovery 시도 후보로만 허용된다. 실제 재개 시 orchestrator는 BrowserUse extension에서 claim한 **기존 같은 탭**으로 read-only recovery proof를 수행하고 durable job version/count/hash/approval/binding을 재확인한다. 일치하면 append-only event를 남기고 그 다음에만 준비 단계를 진행한다. 자동 재전송은 허용하지 않는다.
- 로컬 회귀 `browseruse_extension_bridge` + `UnpreparedRecoveryReadOnlyGateTest` + 전체 `fresh_orchestration` **106/106 PASS**; Node `--check` 및 `git diff --check` PASS; production static audit `PASS`, `critical_count=0`.
- 이 검증 범위는 이번 diff가 추가한 focused/orchestration tests와 static audit다. PR #7의 원격 exact-head workflow가 아직 새 diff를 검증하지 않았으므로, 현재는 same-job 재개 금지 상태다.
- PR #7은 OPEN/DRAFT/MERGEABLE, main 미병합이다. 현재 원격 head `e199b5271d17f1e0e9359de805dd2d91baae462c`다. 이 head의 Pro-first run [35970550958](https://github.com/Daikisong/stock_agent/actions/runs/35970550958)은 SUCCESS, V6 run [35970582856](https://github.com/Daikisong/stock_agent/actions/runs/35970582856)은 SUCCESS이며, 동일 head의 후속 Pro-first run [35970583010](https://github.com/Daikisong/stock_agent/actions/runs/35970583010)은 마지막 조회 시 `in_progress`였다. 이것들은 아직 수정 전 head의 run이다.
- 다음 한 단계는 변경과 이 handoff를 기존 PR #7 branch에만 한글 commit/push한 뒤 새 exact-head Actions를 기다리는 것이다. 그 뒤에만 같은 durable job을 같은 로그인 BrowserUse `extension` 세션·기존 탭에서 재확인한다. **기존 로그인 탭을 사용할 수 없으면 새 창을 열지 않고 멈춘다.**

다음 상세 기록: [implementation progress P86](implementation_progress.md#p86--기존-로그인-browseruse-세션과-same-tab-재개-gate-2026-09-24-1710-kst).

## 가장 중요한 규칙 — 로그인된 바로 그 세션과 탭

인증이 필요한 BrowserUse 작업은 **사용자가 이미 로그인해 둔 Chrome의 BrowserUse `extension` 세션과 그 안의 정확한 기존 작업 탭에서 한다.** 로그인된 탭을 못 찾거나 claim할 수 없으면 다른 세션을 새로 만들지 말고 멈춘다.

- `setupBrowserRuntime()`이 반환한 Agent에서 `extension`을 얻고, `browser.user.openTabs()`로 기존 사용자 탭을 확인한 다음, 작업 대화에 맞는 descriptor 하나를 `browser.user.claimTab()`한다. 이후 입력·확인·파일 회수까지 claim이 반환한 **동일 tab 객체**만 사용한다.
- 새 창·새 탭·새 프로필·별도 CDP 세션을 열어 대체하거나 재로그인하지 않는다. 새 대화가 실제로 필요하면 기존 로그인 탭 안에서만 시작한다.
- 응답/JSON/파일이 이미 있으면 새 요청을 보내지 말고 그 응답을 같은 탭에서 회수·다운로드한다. 입력·첨부·전송 전에는 같은 탭의 URL/대화, 로그인, 실제 선택 모드, 초안·첨부 상태를 다시 확인한다.
- BrowserUse 도구, 세션 또는 정확한 탭의 연결이 실패하면 확인한 범위·마지막 안전 상태·**실제 오류 문자열**을 기록하고 그 단계에서 멈춘다. 다른 세션으로 전송·다운로드를 반복하지 않는다. 기술 오류를 정책 거부로 바꿔 적지 않는다.
- 기록에는 민감정보를 남기지 않는다. 사용자의 기존 창·탭·로그인은 종료하거나 초기화하지 않는다.

## 이전 재개 이력 — P83 (P84/P85/P86에서 후속 갱신)

### P84 당시 인수인계 요약 (2026-09-24 15:43 KST)

- 로그인 필요한 작업은 사용자의 **기존 BrowserUse `extension` 세션에서 이미 로그인된 정확한 작업 탭**에서만 한다. 새 창·탭·프로필·별도 CDP 세션·재로그인은 대체 경로가 아니다. 새 Chat 대화가 필요해도 같은 로그인 탭 안에서만 시작한다.
- 먼저 기존 탭을 열거하고 대상 대화를 확인해 정확한 탭 하나를 claim한다. 이후 그 tab 객체에서 URL/대화, 로그인, 실제 Pro 모드, 기존 응답·초안·첨부를 확인한다. 응답/파일이 이미 있으면 같은 탭에서 재사용·다운로드한다. 입력·첨부·전송 직전에도 같은 탭과 상태를 재확인한다.
- 세션이나 정확한 탭을 연결·claim하지 못하면 실제 오류 문자열과 확인 범위를 기록하고 멈춘다. 다른 세션에서 재로그인·다운로드·재전송하지 않는다. 사용자의 기존 창·탭·로그인은 보존한다.
- 이번 문서 갱신에서는 BrowserUse를 호출하지 않았다. 마지막 실제 브라우저 확인(15:23 KST)은 기존 로그인 ChatGPT 탭, 일반 Chat의 실제 Pro, 빈 composer였다. C15 R6 packet은 업로드·전송되지 않았다.
- 현재 PR #7 head `65493bcc939168dd40eef88de37abfa7d0b5d3b3`의 Pro push [35964475812](https://github.com/Daikisong/stock_agent/actions/runs/35964475812), Pro PR [35964479716](https://github.com/Daikisong/stock_agent/actions/runs/35964479716), V6 PR [35964479682](https://github.com/Daikisong/stock_agent/actions/runs/35964479682)은 확인 시 모두 같은 SHA에서 `in_progress`였다. 세 run이 모두 SUCCESS가 되기 전에는 same-job 브라우저 재개/전송을 하지 않는다.
- P83 경로 수정 후 persistent Windows Node REPL에서 cache-busted bridge import로 `/mnt/c/...`가 native `C:\Users\...`로 변환되고 파일을 읽을 수 있음을 확인했다. REPL은 이전 모듈을 cache할 수 있으므로 이후 source 변경 검증은 commit SHA query를 붙인 import를 사용한다.

- 현재 작업은 기존 C15 R6 job PROJOB-df15a37c58ae7583924e58c0 하나다. DB read-only 기준 USER_ATTENTION_REQUIRED v16, packet hash 불변, browser/conversation binding 없음, submit/capture 0/0, approval 미발급, 새 successor 없음이다.
- 이전 3초 selector timeout은 P81 bounded read-path 수정 후 같은 로그인 탭의 ensure_logged_in()/inspect_state()에서 재현되지 않았다. 실제 Pro/Chat, 로그인, 빈 composer가 확인됐고 같은 탭에서 C15 R6 canary runner가 packet/prompt 해시를 재검증했다.
- 파일 첨부 단계는 Windows 파일 선택기를 누르기 전 경로 검사에서 실패했다: BRIDGE_OPERATION_FAILED: packet file is not readable from the Windows file chooser. 원인은 WSL /mnt/c/...를 \\wsl.localhost\\Ubuntu-22.04\\mnt\\c\\...로 잘못 변환한 것이며, Windows native C:\\... 경로는 같은 파일을 읽었다. 그래서 packet 업로드·prompt 입력·전송은 발생하지 않았다.
- P83 수정은 /mnt/<drive>/...를 C:\\... native path로 변환하고, 기존 /home/...는 distro UNC로 유지한다. 현재 job의 이 정확한 pre-click path-validation 실패만 동일 unsent job에서 재개 가능하게 좁게 허용하고 near-match는 계속 막는다.
- 다음 브라우저 시도는 P83 변경의 exact-head Pro push/Pro PR/V6 PR Actions가 모두 SUCCESS인 뒤에만 한다. 기존 BrowserUse extension 세션에서 같은 사용자 탭을 다시 claim하고, packet/prompt/빈 composer/실제 Pro/submit 0을 재확인한다. 새 창·탭·프로필·CDP 대체·재로그인·새 job은 금지다.

## 실제 실행 순서 — 로그인 세션 작업이면 여기부터

로그인된 화면에서 ChatGPT 응답 확인·다운로드·Pro 전송을 해야 한다면, **사용자가 로그인해 둔 BrowserUse Chrome `extension` 세션과 그 안의 기존 작업 탭을 실제로 사용한다.** 별도 창이 더 편해 보여도 새 Codex Chrome/CDP 창을 열어 대체하지 않는다.

여기서 “새 대화”는 기존 로그인 탭 안의 대화를 바꾸는 것이지 새 브라우저나 별도 탭을 띄우는 뜻이 아니다. Library에 결과가 보이거나 기존 대화에 응답이 있으면 그 같은 탭에서 먼저 회수한다. 아래 경계가 서로 헷갈리면 오른쪽 행동만 한다.

| 상황 | 해야 할 일 | 하지 말 것 |
|---|---|---|
| 로그인이 필요한 화면 | `extension`의 기존 사용자 탭을 찾아 claim하고 계속 재사용 | 새 Chrome/창/프로필/CDP를 열어 같은 계정으로 다시 로그인 |
| 기존 응답·JSON·파일이 있음 | 같은 탭에서 응답을 확인하고 다운로드 | 새 대화를 만들어 같은 요청을 다시 보내기 |
| 새 Chat이 실제로 필요함 | 기존 로그인 탭 안에서만 새 Chat 시작 | 새 브라우저나 별도 로그인 세션 생성 |
| extension/탭 claim/대상 확인 실패 | 읽기 전용으로 확인된 상태와 정확한 오류를 남기고 정지 | 다른 세션으로 이동, 재로그인, 첨부·전송 재시도 |

1. 정식 BrowserUse runtime bootstrap을 하고 `setupBrowserRuntime()`이 돌려준 Agent를 보관한다. `agent.browsers.get("extension")`으로 BrowserUse extension을 가져온다.
2. `browser.user.openTabs()`에서 기존 사용자 탭을 열거한다. 서비스 주소·현재 대화·작업 목적이 일치하는 descriptor 하나를 고르고 `browser.user.claimTab()`으로 claim한다.
3. 이후 작업은 claim이 반환한 **그 tab 객체 하나**에서만 한다. 먼저 현재 대화, 기존 응답/첨부, 로그인, 실제 Pro 선택을 확인한다. 결과물이 이미 있으면 그 대화의 결과물을 같은 탭에서 회수한다.
4. 새 대화가 꼭 필요해도 같은 로그인 탭 안에서만 연다. 기존 초안이나 응답을 덮어쓰지 않는다. 실제 입력·첨부·전송은 대상 tab과 요청 내용을 다시 확인한 뒤 승인된 범위에서 한다.
5. BrowserUse extension 도구를 현재 실행에서 사용할 수 없거나 기존 탭 claim이 실패하면 확인 범위와 **실제 오류**를 남기고 거기서 멈춘다. 다른 backend는 바로 그 로그인 세션·같은 탭을 제어할 수 있음이 확인될 때만 고려한다. 새 창·새 탭·새 프로필·다른 CDP 세션·재로그인·재전송으로 우회하지 않는다. 실제 정책 거부가 확인된 경우에만 정책 문제로 기록하고, 그 외 연결 문제는 기술 실패로 정확히 분류한다.

금지 예: 기존 ChatGPT 탭을 확인하지 않고 Codex가 새 브라우저를 띄워 같은 계정으로 로그인하려고 시도하는 것.
올바른 예: BrowserUse extension에서 사용자의 기존 로그인 탭을 claim하고, 이미 표시된 응답의 다운로드를 그 탭에서 실행하는 것.

## 최우선 실행 규칙 (P67)

사용자가 이미 로그인해 둔 세션이 필요한 작업은 **그 기존 BrowserUse `extension` 세션의 탭에서만** 한다.
새 Codex Chrome/CDP 창이나 별도 프로필은 같은 서비스·계정처럼 보여도 대체 세션이 아니다. 기존 세션에
연결하거나 정확한 작업 탭을 제어할 수 없으면 다른 창으로 옮기지 말고, 실제 오류와 확인 범위를 기록한 뒤
그 브라우저 단계에서 멈춘다. 재로그인·새 창·대체 세션 전송은 하지 않는다.

BrowserUse `extension`에서 `browser.user.openTabs()`로 기존 사용자 탭을 찾고, 정확한 descriptor를
`browser.user.claimTab()`에 전달한다. 이후 claim이 반환한 제어 객체 하나를 유지해 로그인 확인, 기존 대화·첨부
확인, 필요할 때만 같은 탭 안에서 새 대화 시작, 파일 회수, 승인된 전송까지 수행한다.

```text
기존 사용자 탭 열거 → 정확한 탭 claim → 그 탭에서 현재 대화/첨부 확인
→ 있던 결과는 같은 탭에서 다운로드 / 새 대화는 같은 탭 안에서만 시작
→ 같은 탭에서 대상/실제 모드/초안 재확인
→ 요청된 입력·전송 → 그 대화의 결과만 회수
```

새 대화는 새 브라우저가 아니다. 이미 응답이나 JSON이 있으면 새 요청을 보내지 말고 그 결과를 같은 탭에서
회수한다. Library 검색 한 번에서 결과가 없다는 사실만으로 계정 전체에 파일이 없다고 단정하지 않는다.
영수증에는 확인 범위와 정확한 도구 오류만 남기고 tab ID, 계정 식별자, 쿠키·인증값은 남기지 않는다.

## 먼저 읽을 규칙 — 현재 로그인 탭에서 그대로 이어가기

로그인이 필요한 BrowserUse 작업은 사용자가 이미 로그인해 둔 **그 BrowserUse 세션과 기존 작업 탭**에서만
한다. 새 브라우저 창·프로필·CDP 세션은 같은 계정처럼 보여도 대체물이 아니다.

1. BrowserUse 스킬의 절차로 기존 사용자 탭을 열거하고, 정확히 일치하는 탭 descriptor를
   `browser.user.claimTab()`에 전달한다. descriptor가 아니라 claim이 반환한 실제 tab 객체를 보관해 사용한다.
2. 새 입력을 만들기 전에 그 탭의 현재 대화와 완료 응답·첨부 상태를 확인한다. 필요한 JSON/파일이 이미
   응답이나 Library에 있으면 **같은 로그인 탭에서 그 기존 결과물을 다운로드해 현재 파이프라인에 전달**한다.
   같은 결과를 얻으려고 새 창을 열거나, 이미 보낸 요청을 다시 전송하지 않는다.
3. 진짜 새 대화가 필요한 경우에도 기존 로그인 탭 안에서만 연다. 새 대화는 새 브라우저 세션이 아니다.
   사용자의 초안·진행 중 응답은 유지하고, 입력·첨부·전송 직전에 같은 tab ID를 재확인한다.
4. 정확한 탭을 제어할 수 없거나 해당 탭에서 파일 회수가 실패하면, 확인된 오류와 마지막 상태를 기록하고
   멈춘다. CDP/새 창/재로그인으로 우회하지 않는다.

쉬운 예: 기존 ChatGPT 응답이나 Library에 JSON이 보이면 그 화면의 다운로드 동작을 같은 탭에서 수행하고,
받은 파일을 준비된 E2R job에 연결한다. “새 세션에서 다시 생성”은 기본 복구 방법이 아니다.

## 이전 상태 인수인계 (P81, 2026-09-24 14:37 KST)

- PR #7은 OPEN/DRAFT/MERGEABLE, main 미병합이다. 새 head `7830b9a5baccaa7119d52892480504c82014ea26`를 한글 commit `7830b9a5`로 push했다. 이 head의 Pro push [35960262909](https://github.com/Daikisong/stock_agent/actions/runs/35960262909), Pro PR [35960267593](https://github.com/Daikisong/stock_agent/actions/runs/35960267593), V6 PR [35960267632](https://github.com/Daikisong/stock_agent/actions/runs/35960267632)은 14:37 KST 확인 시 모두 `in_progress`다. 기존 SHA `281354cf`의 세 성공 run은 과거 코드 검증이며 P81 결과와 혼동하지 않는다.
- 로그인 필요 화면 작업은 P80에서 연결한 BrowserUse `extension`의 **동일 사용자 ChatGPT 탭**으로만 한다. 그 탭의 login/Pro/composer read-only preflight는 PASS였지만, same-job initial runner가 `first_visible()`의 selector 조회에서 다시 3초 timeout을 냈다. 현재 화면은 여전히 ChatGPT home이고 login prompt 없음, composer 1개, `Pro` 선택 control, user turn 0, packet attachment 0이다. `tab.dev.logs()`는 0건이고 `tab.capabilities.get("cdp")`는 `Capability is not available: cdp`를 반환했다.
- SQLite mode=ro + `PRAGMA query_only=ON`의 active C15 R6는 `PROJOB-df15a37c58ae7583924e58c0`, `USER_ATTENTION_REQUIRED` version 14다. packet hash `fa5845a055661c99c2ab1eb9cfb65f66fb84d2c85b267b3cde33b54843c320df` 그대로, approval/browser/conversation 미결박, submit/capture `0/0`, successor 없음이다. 새 실패 이벤트는 `READ_ONLY_BROWSER_PREFLIGHT`, `safe_unprepared_resume=true`; 현재 last error는 기존과 동일한 3000ms selector timeout이다.
- 이 시도는 전송·첨부 전에 멈췄다. 같은 탭에서 새 window/tab/profile/CDP, 재로그인, navigation, prompt/file/upload/download/submit/capture, source query/fetch, score/Stage 변경은 0이다. 사용자 기존 탭은 열린 상태로 보존했다.
- 원인 범위: P79가 `evaluate` 계열에 10초 상한을 전달했지만, 설치된 BrowserUse API에서 `locator.count()`, `isVisible()`, `isEnabled()`는 해당 timeout option을 노출하지 않는다. E2R의 selector helper/attachment lookup이 이 raw API를 바로 호출해 3초 selector deadline이 남아 있었다. 어느 단일 API call에서 이번 timeout이 발생했는지는 직접 계측 전이므로 단정하지 않는다.
- P81 local patch는 읽기 전용 count/visibility/enabled 조회를 reviewed `evaluateAll/evaluate` callback으로 우회하고 10초 상한을 전달한다. `innerText/textContent/getAttribute`에도 bounded timeout을 전달하며, adapter preflight와 attachment lookup이 같은 helper를 사용한다. action (`click/fill/submit`)은 read-only 경로로 바꾸지 않았다.
- P81 tests: BrowserUse bridge 10/10 PASS, fresh orchestration 85/85 PASS, JS `node --check` PASS. 추가 문서 확인 뒤 bridge+orchestration 로컬 재실행 95/95 PASS, `git diff --check` PASS다. 코드는 commit/push됐으며 exact-head CI는 아직 진행 중이다.
- 다음 한 단계: 위 세 run이 정확한 SHA `7830b9a5…`에서 모두 SUCCESS인지 확인한다. 그 전에는 같은 job 재시도/전송을 하지 않는다. Green 뒤에는 정확히 같은 C15 R6 job과 같은 BrowserUse 탭만 다시 사용한다. mismatch가 있으면 멈춘다.

P81 상세 진행기록은 [implementation progress P81](implementation_progress.md#p81--browseruse-selector-read-path-timeout-보강과-same-job-실패-경계-기록-2026-09-24-1423-kst)을 참조한다.

## 이전 상태 인수인계 (P80, 2026-09-24 14:08 KST)

- PR #7은 OPEN/DRAFT/MERGEABLE이며 main에는 미병합이다. 현재 local/origin head는 `281354cfc6d8e88f21c2bd1b32db72fea6f2f155` (`BrowserUse 읽기 전용 평가 timeout 전달을 보정`)이다.
- 이 정확한 head의 Pro push [35955888505](https://github.com/Daikisong/stock_agent/actions/runs/35955888505), Pro PR [35955892468](https://github.com/Daikisong/stock_agent/actions/runs/35955892468), V6 PR [35955892448](https://github.com/Daikisong/stock_agent/actions/runs/35955892448)은 모두 SUCCESS로 종료됐다. 각 실행의 head SHA는 `281354cfc6d8e88f21c2bd1b32db72fea6f2f155`다.
- P79 수정 범위와 기술적 근거는 아래 P79 기록을 참조한다. 같은 로그인 탭에서 수정 전후 live 비교는 아직 하지 않았고, 따라서 timeout의 단독 근본 원인을 확정하지 않았다.
- C15 R6 durable job은 `PROJOB-df15a37c58ae7583924e58c0` / 010950, `USER_ATTENTION_REQUIRED` version 12, packet hash `fa5845a055661c99c2ab1eb9cfb65f66fb84d2c85b267b3cde33b54843c320df`다. 기존 latest event는 read-only preflight이며 `safe_unprepared_resume=true`; approval/browser/conversation 미결박, submit/capture 0/0, successor 없음이다.
- exact-head CI green 뒤 canonical BrowserUse bootstrap으로 `extension` 사용자 탭을 열거했고, 기존 ChatGPT 탭 하나(`chatgpt.com` home)를 정확히 claim했다. 로그인 prompt 없음, composer 1개, composer 근처 실제 선택 `Pro` control, 기존 conversation 없음이 확인됐다. production adapter의 동일 bridge-worker `ensure_logged_in()` + `inspect_state()`도 `DEEP_RESEARCH_MODE_READY` / `pro_mode_ready=true`, editor ready, packet/prompt 없음, submit control 비활성, stop 없음으로 PASS했다. 수정된 10초 read-only evaluate 경로에서 이전 3초 timeout은 재현되지 않았다. 이 성공은 기존 오류의 유일한 root cause까지 입증하지는 않는다.
- 같은 시점 SQLite mode=ro + `query_only=ON` 재확인: 동일 C15 R6 `PROJOB-df15a37c58ae7583924e58c0`, state version 12, packet hash `fa5845a055661c99c2ab1eb9cfb65f66fb84d2c85b267b3cde33b54843c320df` 그대로다. `USER_ATTENTION_REQUIRED`, browser/conversation/approval 미결박, submit/capture `0/0`, successor 없음이다. 역사적 `last_error`에는 이전 3초 timeout이 남아 있지만 새 read-only preflight는 성공했다.
- 이번 P80 브라우저 확인은 claim한 그 기존 사용자 탭에서만 수행했다. 새 창/탭/프로필/CDP 세션, 재로그인, navigation, prompt 입력, upload/download, submit/capture, 새 source query/fetch, score/Stage 변경은 전부 0이다. 사용자 탭은 열린 상태로 두었다. 실제 로그인 브라우저 작업의 필수 경로는 이 문서 위쪽 “실제 실행 순서”다.
- 다음 한 단계: 사용자가 앞서 허가한 실제 전송 범위 안에서 **같은 C15 R6 job만** `resume_unprepared_attention_job_id`로 초기 Pro pass에 재개한다. 전송 직전 동일 packet hash, version/unsent 상태, 같은 tab, 실제 Pro 선택을 다시 확인한다. 하나라도 예상과 다르면 전송하지 말고 오류를 기록한다. 새 job·새 브라우저·새 세션은 만들지 않는다.
- CI green과 read-only 재확인만으로 full goal이 완료되는 것은 아니다. master goal, 동일 Pro conversation, 승인 범위, multi-pass saturation, verifier repair, full thesis gate와 canary 요구사항은 계속 열린다.

P79 receipt: [P79 receipt](p79_browseruse_evaluate_timeout_bridge_receipt.json). P80 same-tab read-only 결과와 다음 동작은 위 checkpoint에 기록했다. 이전 3초 오류 및 그 전의 같은 탭 실패 이력은 [P78 progress](implementation_progress.md#p78--사용자-기존-browseruse-세션-유지와-same-job-preflight-timeout-기록-2026-09-24-1259-kst)를 참조한다.

## 이전 상태 인수인계 (P78)

- 현재 PR #7 head는 `96b73876a5d0fb58f2b226bb31420c4b6cf37b24`; local branch와 `origin/feature/e2r-pro-first-browser-platform-20260822`가 일치한다. PR은 OPEN/DRAFT/MERGEABLE이고 `main`에는 병합하지 않았다.
- 이 exact SHA의 Pro push [35950648915](https://github.com/Daikisong/stock_agent/actions/runs/35950648915), Pro PR [35950652188](https://github.com/Daikisong/stock_agent/actions/runs/35950652188), V6 PR [35950652197](https://github.com/Daikisong/stock_agent/actions/runs/35950652197)은 모두 SUCCESS다. Pro regression은 7,923 tests / skipped 38 / failure·error 0, Reviewer A–H PASS다. V6는 Gate 1 receipt 4/4, Phase100 15/15, production static audit critical 0, 전체 테스트 failure·error 0이다.
- 사용자의 반복 지시를 실행 우선 규칙으로 다시 명시한다: 인증이 필요한 작업은 **사용자가 로그인해 둔 기존 BrowserUse `extension` 세션과 그 기존 작업 탭에서만** 한다. 새 창·탭·프로필·CDP 대체 세션·재로그인을 만들지 않는다. 연결·제어가 실패하면 그 오류와 확인 범위를 기록하고 멈춘다. 이 규칙은 로그인 만료를 가정하거나 별도 창으로 재시도할 권한을 주지 않는다.
- 2026-09-24 12:54 KST 무렵 동일 C15 R6의 재개 과정에서 첫 harness는 Windows-hosted Node REPL의 `spawn("python")`을 사용해 Windows Python이 WSL UNC DB 경로에 접근하다 `WinError 5`로 runner 시작 전 실패했다. 이를 로그인/브라우저 오류로 취급하지 않고, 이후 `/usr/bin/python3`을 `wsl.exe --distribution Ubuntu-22.04 --cd <worktree> --exec ...`로 실행하는 방식으로 바로잡았다. 첫 실패에서 브라우저 UI 호출이나 job 전이는 없었다.
- 바로잡은 worker는 **동일 BrowserUse extension 세션에서 열거·claim한 기존 ChatGPT 탭**으로 연결됐다. read-only `inspect_state()` 중 composer selector의 text 조회가 아래 3초 timeout으로 실패했다. 새 탭·창·프로필, navigation, 입력, 파일 선택·다운로드, submit, capture는 하지 않았다.

```text
BrowserUseBridgeError: BRIDGE_OPERATION_FAILED: Timed out after 3000ms evaluating selector div.ProseMirror[contenteditable="true"] >> nth=0: Playwright selector deadline exceeded
```

- 실패 후 같은 기존 탭을 읽기 전용으로 확인했다: `https://chatgpt.com/` / `ChatGPT`, 일반 Chat, 실제 선택 Pro, 빈 composer, file input 0, Stop control 0, Deep Research 비활성, 기존 user turn 0. `tab.dev.logs()`의 error/warn 결과는 `[]`; `tab.capabilities.get("cdp")`는 `Capability is not available: cdp`를 반환했다. 이것은 기술 capability 한계이지 정책 거부나 로그인 실패 증거가 아니다. 프로젝트 SQLite 및 adapter/bridge 근거로 selector timeout은 확인했지만, extension RPC timeout의 근본 원인은 아직 확정하지 않았다.
- SQLite mode=ro 기준 같은 `PROJOB-df15a37c58ae7583924e58c0` / `010950` / C15 R6는 `USER_ATTENTION_REQUIRED`, version 12, packet hash `fa5845a055661c99c2ab1eb9cfb65f66fb84d2c85b267b3cde33b54843c320df`다. `preparation_failure_stage=READ_ONLY_BROWSER_PREFLIGHT`, `safe_unprepared_resume=true`; approval/browser/conversation 미결박, submit/capture `0/0`, successor 없음이다. 새 job이나 새 조사 pass는 만들지 않았다.
- 현재 한 단계는 selector/evaluate의 Python→BrowserUse RPC 경로와 deadline을 코드·테스트에서 조사하는 것이다. 같은 selector를 무작정 재시도하지 않는다. 코드 변경이 필요하면 generic regression을 추가해 기존 PR #7에만 반영하고 exact-head 필수 CI를 확인한다. 그 뒤에도 동일 unsent C15 R6만 기존 BrowserUse 세션·기존 탭에서 재개한다. bridge/worker는 한 active `mcp__node_repl__js` call에서 `await bridge.runUntil(workerPromise)`로 함께 실행하고, REPL reset 뒤에는 canonical bootstrap과 기존 탭 확인을 다시 한다.
- P78 중 prompt input/upload/download/submit/capture, source query/fetch, score/Stage 변경은 모두 `0`이다. master goal 미완료, PR #7은 계속 draft/open이며 main merge 금지다.
- 기계 판독 상태와 P78 실행 범위는 [P78 receipt](p78_browseruse_same_session_preflight_receipt.json), 이전 CI/세션 확인은 [P77 progress](implementation_progress.md#p77--기존-browseruse-로그인-탭-재확인과-p76-exact-head-ci-정정-2026-09-24-1207-kst)를 본다.

## 이전 상태 인수인계 (P77)

- 현재 PR #7 head는 `d294f395738254da1f616d361038a35548fa6c4e`; local branch와 `origin/feature/e2r-pro-first-browser-platform-20260822`가 일치한다. PR은 OPEN/DRAFT/MERGEABLE이고 `main`에는 병합하지 않았다.
- 이 exact SHA에서 Pro push [35947967714](https://github.com/Daikisong/stock_agent/actions/runs/35947967714), Pro PR [35947970682](https://github.com/Daikisong/stock_agent/actions/runs/35947970682), V6 PR [35947970654](https://github.com/Daikisong/stock_agent/actions/runs/35947970654)이 모두 SUCCESS다. Pro full regression은 7,923 tests / skipped 38 / failure·error 0이며 independent Reviewer A–H PASS. V6는 Gate 1 receipt 4/4, Phase100 15/15, production static audit critical 0, 전체 unittest failure·error 0이다.
- 2026-09-24 12:07 KST에 **이미 연결된 BrowserUse extension 세션과 기존에 claim한 tab 객체**만 읽기 전용으로 재확인했다. `browser.user.openTabs()`는 사용자 탭 1개를 반환했고 claim 객체의 origin/title은 `https://chatgpt.com` / `ChatGPT`였다. 새 창·탭·프로필, CDP 대체 세션, 재로그인, navigation, 입력·첨부·전송은 하지 않았다. P76 당시 같은 탭에서 실제 Pro 선택, 빈 composer, 첨부 0을 확인한 이후에도 탭을 reset/닫지 않았다.
- 다음 작업에서 지켜야 할 bootstrap 순서: 현재 persistent `mcp__node_repl__js`에서 BrowserUse runtime이 반환한 Agent를 `globalThis.agent`에 보관하고, `globalThis.browser = await globalThis.agent.browsers.get("extension")`로 extension을 기다린 뒤 `browser.user.openTabs()` → 정확한 기존 descriptor를 `browser.user.claimTab()` → 반환된 실제 tab 객체 하나를 계속 사용한다. 탭 선택 API의 Promise를 await하지 않으면 이후 `tabs`/browser 접근이 실패할 수 있다. `browser.tabs.list()`는 사용자 외부 탭을 찾는 대체 수단이 아니다.
- 실제 C15 R6 재개에서는 bridge 생성과 Python worker promise를 별도 Node REPL 호출로 나누지 않는다. 둘을 같은 활성 `mcp__node_repl__js` 호출에서 실행하고 `await bridge.runUntil(workerPromise)`를 완료한다. 이 실행문맥 조건은 로그인/인증과 별개이며, 실패해도 새 창이나 재로그인으로 우회하지 않는다.
- 마지막 SQLite read-only 검증의 active job은 `PROJOB-df15a37c58ae7583924e58c0` / `010950` / C15 R6, `USER_ATTENTION_REQUIRED` version 10, 동일 packet hash다. approval/browser/conversation 미결박, submit/capture `0/0`, successor 없음. P76의 exact handshake 오류 외에는 같은 job을 임의 재시도하지 않는다.
- 이번 P77 문서/상태 확인 중 prompt input/upload/submit/capture, source query/fetch, score/Stage 변경은 모두 0이다. 현재 한 단계는 위 same-job 경계를 지켜 C15 R6를 **그 기존 로그인 탭**에서 재개하는 것이다. 새 browser/session/job을 만들지 않는다.
- 세부 CI/진행 기록은 [P77 progress](implementation_progress.md#p77--기존-browseruse-로그인-탭-재확인과-p76-exact-head-ci-정정-2026-09-24-1207-kst), [P77 receipt](p77_browseruse_existing_session_docs_ci_receipt.json)을 본다.

## 직전 상태 인수인계 (P76, P77에서 exact-head CI 상태 갱신)

- 로그인 필요 작업은 사용자가 이미 로그인한 BrowserUse `extension`의 **그 기존 세션과 기존 ChatGPT 탭**에서만 한다.
  새 browser/window/tab/profile, CDP 대체 연결, 재로그인은 하지 않는다. claim한 바로 그 tab object를 유지하며 tab ID,
  계정 식별자, cookie/token은 기록하지 않는다.
- 2026-09-24 11:29 KST에 같은 탭을 읽기 전용 확인했다: ChatGPT origin/title, Pro control 활성, composer 1개·빈 상태,
  selected file 0, legacy Deep Research 비활성. C15 R6 runner 실패 뒤에도 job marker는 화면에 없었다. 사용자의 탭을 닫거나 reset하지 않았다.
- P75 CI 통과 후 C15 R6 same-job resume를 시도했지만, `BrowserUseBridgeClient.connect()` handshake에서
  `BRIDGE_OPERATION_FAILED: node_repl exec context not found`로 멈췄다. bridge `runUntil()`을 이전 Node REPL 호출에서 background로
  남긴 뒤 다음 도구 호출에서 Python worker를 실행해 BrowserUse가 요구하는 활성 `node_repl` execution context를 놓친 것이다.
  로그인/인증 문제는 아니다. handshake 단계라 runner가 `page.goto`, prompt 입력, upload, submit, capture에 도달하지 않았다.
- 이 미전송 job 오류는 `USER_ATTENTION_REQUIRED` / version 10, submit/capture `0/0`, approval/browser/conversation 미결박,
  packet hash unchanged다. 당시 attention event가 `safe_unprepared_resume=false`여서 그대로 재시도하지 않았다.
- P76 local patch는 (1) BrowserUse worker-open failure를 `BROWSER_SESSION_OPEN`으로 안전 기록하고, (2) 기존 durable row는
  정확한 이 handshake 오류·동일 unsent identity·미결박·prepare receipt 부재일 때만 복구하며, (3) 근접 문자열/기타 오류는 차단한다.
  Focused bridge + orchestration 94/94 PASS; P76 exact-head CI는 아직 pending이다.
- 중요한 실행 방식: 실제 worker를 재개할 때 bridge와 Python worker를 별도 Node REPL 호출로 나누지 않는다.
  **하나의 active `mcp__node_repl__js` 호출 안에서 `await bridge.runUntil(workerPromise)`를 실행**해 RPC 서비스와 브라우저 callback의
  실행문맥을 유지한다. 사용자의 기존 탭은 그대로 두고 새로운 브라우저를 만들지 않는다.
- 다음 한 단계: P76 코드를 한글 커밋으로 기존 PR #7 branch에 push하고 exact-head Pro push/PR + V6 PR Actions SUCCESS를 기다린다.
  그 뒤에만 동일 C15 R6 job을 동일 BrowserUse 로그인 탭에서 재개한다.
- 세부 내역: [P76 progress](implementation_progress.md#p76--same-tab-browseruse-실행문맥-실패의-무전송-복구-게이트-보강-2026-09-24-1130-kst),
  [P76 receipt](p76_browseruse_exec_context_recovery_receipt.json).

## 직전 상태 인수인계 (P75, P76이 최신 상태를 대체)

- **로그인·Pro 작업은 사용자가 이미 로그인한 BrowserUse `extension`의 같은 기존 탭에서만 한다.** 새 창/탭/프로필,
  CDP 대체 세션, 재로그인을 열지 않는다. 정확한 기존 사용자 탭을 claim한 객체를 계속 쓰고, tab ID·계정 식별자·cookie/token은 기록하지 않는다.
- 2026-09-24 10:42 KST에 그 기존 탭을 다시 읽기 전용으로 확인했다: `https://chatgpt.com/`, title `ChatGPT`, editor 1개,
  editor 빈 상태. 같은 탭을 Python worker에 연결한 `inspect_state()` smoke도 통과했다. adapter guard는 일반 Chat + 실제 Pro,
  Work 비활성, legacy Deep Research 비활성을 확인하는 경로다. 새 navigation, prompt 입력, packet 첨부, submit, capture는 없었다.
- P75에서 발견한 오류는 BrowserUse extension의 `evaluate()`가 callback 함수 객체를 요구하는데 bridge가 문자열로 함수를 호출했던 것이다.
  기존 탭의 read-only login preflight는 selector 평가 3초 timeout으로 멈췄다. 동적 코드 생성 대신 검토된 static read-only callback allowlist를
  추가했고, 모르는 callback은 fail-closed한다. bridge + fresh orchestration 91/91 PASS, `node --check`와 `git diff --check` PASS.
- 중앙 DB를 read-only로 확인한 동일 C15 R6 job `PROJOB-df15a37c58ae7583924e58c0` / `010950`은 기존 packet hash를 보존하며
  `USER_ATTENTION_REQUIRED` / version 8이다. approval/browser/conversation 미결박, submit/capture `0/0`; 마지막 event는
  `READ_ONLY_BROWSER_PREFLIGHT`, `safe_unprepared_resume=true`다. 현재 오류는 callback selector timeout이며 login 실패나 사용자 인증 요청이 아니다.
- 원격에서 확인한 이전 P74 head `8b86d2db6479c40d4bc0463354dc9a3de711087e`의 Pro push, Pro PR, V6 PR Actions는 모두 SUCCESS
  (7,920 tests / 38 skipped / failure·error 0)였다. P75 diff는 이보다 뒤의 변경이므로 새 exact-head CI가 끝나기 전까지 canary를 재개하지 않는다.
- 이번 smoke와 DB 재조회에서도 prompt input/upload/submit/capture `0/0/0/0`, 새 source query/fetch `0/0`, score/Stage 변경 `0/0`이다.
  다음 한 단계는 P75 코드·회귀·문서·receipt를 한글 commit으로 기존 PR #7 branch에 push하고 exact-head Pro push/PR 및 V6 PR CI SUCCESS를 확인하는 것.
  green 뒤에만 동일한 unsent C15 R6 job을 **같은 기존 BrowserUse 로그인 세션·같은 기존 탭**에서 재개한다.
- 세부 기록: [P75 progress](implementation_progress.md#p75--browseruse-dom-evaluate-callback-계약-보정과-동일-로그인-탭-smoke-2026-09-24-1042-kst),
  [P75 machine receipt](p75_browseruse_evaluate_callback_receipt.json), [P74 prior CI and attachment fix](p74_browseruse_attachment_locator_receipt.json).

## 직전 상태 인수인계 (P74, P75가 최신 상태를 대체)

- P74 변경은 attachment helper의 callable `first()`와 Playwright property형 `first`를 함께 지원하도록 고쳤다.
- 그 P74 head `8b86d2db6479c40d4bc0463354dc9a3de711087e`는 Pro push run [35940763725](https://github.com/Daikisong/stock_agent/actions/runs/35940763725),
  Pro PR run [35940765268](https://github.com/Daikisong/stock_agent/actions/runs/35940765268), V6 PR run
  [35940765227](https://github.com/Daikisong/stock_agent/actions/runs/35940765227)이 모두 SUCCESS였다.
- P74 당시 same-tab attachment locator read-only smoke는 PASS; click/upload는 하지 않았다. 상세는 [P74 progress](implementation_progress.md#p74--browseruse-native-packet-attachments-first-호출-보완-2026-09-24-0955-kst)와 receipt에 있다.

## 이전 상태 인수인계 (P73, superseded)

- 최우선 사용 규칙: 로그인 작업은 사용자가 이미 로그인한 BrowserUse `extension` 세션의 **기존 작업 탭 하나**에서만 한다.
  이번에도 기존 ChatGPT 탭을 exact claim한 반환 객체 하나로 확인했다. 새 browser/window/profile/tab, 재로그인은 0회다.
  tab ID, 계정 식별자, 쿠키·token은 기록하지 않는다.
- P73에서 P72와 같은 C15 R6 job을 안전 재개했지만, 실제 입력·첨부·전송 전에 BrowserUse locator bridge의 두 번째
  계약 차이로 read-only login preflight가 실패했다: `locator.count is not a function`. traceback의 원인은 BrowserUse
  extension이 `first()`/`last()`를 함수로 제공하는데 bridge가 Playwright property처럼 handle에 저장한 것이다.
- 함수형과 property형을 모두 지원하도록 bridge를 로컬 수정했고, 같은 기존 BrowserUse 탭을 통해 read-only bridge smoke를
  통과했다. visible composer locator `count=1`, `is_visible=true`; composer는 빈 상태였다. 이 smoke는 UI 입력, 첨부, 클릭,
  전송 또는 navigation을 수행하지 않았다.
- 현재 compact composer의 공개 선택값은 `ChatGPT 모델 선택` control의 `Pro`이며 Chat 버튼 활성, Work 비활성,
  Deep Research 활성 control 없음, 빈 composer다. 직전 `page.goto` 이전 snapshot의 `6 Pro`와 구별해 기록한다.
  이 `Pro`는 로그인 계정의 구독 badge가 아니라 adapter가 요구하는 선택된 composer control의 값이다.
- 실제 실패 뒤 SQLite read-only 조회 결과 active
  `PROJOB-df15a37c58ae7583924e58c0`는 `USER_ATTENTION_REQUIRED` / version 6이며 packet hash는 동일하다.
  approval/browser/conversation binding은 없고 submit/capture `0/0`이다. 최근 event는 안전한 read-only preflight resume를
  허용한다. job successor를 만들지 않았다.
- 로컬 BrowserUse bridge + fresh orchestration tests **91/91 PASS**, Node syntax / whitespace checks PASS.
  이 P73 patch의 전체 회귀 및 exact-head CI는 아직 pending이다. 이전 `b8c4c77e...`의 CI 결과를 P73 green으로 세지 않는다.
- 현 시점 C15 R6의 prompt/upload/submit/capture/query/fetch/score/Stage 변경은 모두 0이다. 다음 한 단계는 한글 commit/push로
  PR #7 exact head를 만들고 CI SUCCESS를 기다리는 것. 그 뒤에도 same existing BrowserUse tab과 same R6 job만 쓴다.
- 상세 root cause, 각 시도, read-only evidence, local test 범위는 [P73 progress](implementation_progress.md)와
  [P73 receipt](p73_browseruse_locator_api_receipt.json)에 있다.

## 이전 상태 인수인계 (P72, superseded)

- 로그인 필요 작업은 사용자의 BrowserUse Chrome plugin `extension`이 연결한 **이미 로그인된 기존 세션과 정확히 claim한 기존 탭**에서만 한다.
  이번 확인에서도 사용자 탭은 ChatGPT 하나였고, 기존 tab 객체를 유지했다. 탭 ID·계정·쿠키·인증값은 기록하지 않았다.
  새 브라우저/창/탭/프로필/재로그인은 없었다.
- P72 직전 읽기 전용 검사에서 일반 Chat 선택, 모델 label `6 Pro`, Work 미선택, 빈 composer를 확인했다. pipeline은 같은 탭의
  ChatGPT origin에서 read-only login preflight에 도달했으나 bridge locator 응답 계약 오류로 멈췄다. 실제 prompt input/upload/submit/capture는
  각각 0회이며, 실패 뒤 composer blank와 packet attachment 없음도 확인했다.
- 정확한 blocker: JS `locator.create`는 top-level `{handle: ...}`를 반환했으나 Python `BrowserUseBridgeClient.call()`은 `value`만 반환했다.
  이에 반환을 `{value: {handle: ...}}`로 통일하고, missing handle이면 명시적 bridge error로 멈추도록 수정했다. 이 문제는 로그인 인증이나
  Pro/Deep Research 모드 선택 오류가 아니다. ChatGPT React hydration #418도 별도로 관찰됐으나, 현재 traceback상 locator RPC envelope가 직접 원인이다.
- active C15 R6 `PROJOB-df15a37c58ae7583924e58c0`은 현재 `USER_ATTENTION_REQUIRED` / version 4이며 기존 packet hash를 유지한다.
  중앙 DB read-only 확인상 browser/conversation 미결박, approval 미발급/미소비, submit/capture `0/0`이다. 기존 job이며 successor는 없다.
- read-only preflight에서 실패한 attention job만 같은 job으로 재개하는 명시 게이트와 테스트를 추가했다. prepare receipt 존재, 승인/브라우저 결박,
  submit/capture가 있으면 이 경로는 거부된다. P72 회귀 세트 90/90 PASS, Python compileall, Node syntax check, diff check PASS.
  P72 code diff의 full repository unittest / Actions는 아직 pending이며, P71 head의 green CI는 새 diff를 증명하지 않는다.
- 세부 사건 시각, exact error, 바뀐 파일, CI 상태, 다음 한 단계는 [P72 implementation progress](implementation_progress.md)와
  [P72 receipt](p72_browseruse_rpc_preflight_recovery_receipt.json)에 있다. 이번 시도는 research answer/canary PASS가 아니며 score/Stage 권한을 만들지 않았다.

## 이전 상태 인수인계 (P71, superseded)

- 로그인 필요 작업은 사용자의 BrowserUse Chrome plugin `extension`이 연결한 **이미 로그인된 세션과 기존 작업 탭**에서만 한다.
  `browser.user.openTabs()`로 탭을 열거하고, 정확한 descriptor를 `browser.user.claimTab()`에 넘긴 뒤 반환된 Tab 객체 하나를 유지한다.
  새 Codex/CDP 창·프로필·대체 탭·재로그인은 사용하지 않는다. 연결이 안 되면 실제 오류를 기록하고 멈춘다.
- 마지막 BrowserUse UI 관찰은 P70이다. 그때 기존 탭 안의 Chat 화면에서 `6 Pro`, Chat 선택, Work/Deep Research 미선택,
  빈 composer를 확인했다. P71에는 브라우저를 조작하지 않았다. 재개 시 같은 로그인 세션을 다시 열거·claim하고, 입력 직전에
  탭·job·대화·실제 Pro model·사용자 초안을 재확인한다.
- 코드상 Windows/WSL path blocker를 수리했다. 기존 C15 R6 leakage manifest hash와 Windows path boundary receipt를 확인하고,
  중앙 SQLite를 `mode=ro` + `query_only=ON`으로 열어 `FreshSessionBoundaryService.load_existing()`가 같은 job을 재개하는 데 성공했다.
  현재 job은 `PROJOB-df15a37c58ae7583924e58c0` / `010950` / `PACKET_READY`, version 2, submit/capture `0/0`,
  browser/conversation 미결박이다.
- Regression은 fresh orchestration 80/80 PASS. Production static audit critical 0, V2 contract/generalization/static audit PASS,
  V2.1 efficiency audit PASS/critical 0이다. 다만 이 P71 diff의 exact-head GitHub Actions와 full repository unittest는 **pending**이다.
  P70의 head `43524413...` CI success는 P71 diff의 CI로 세지 않는다.
- 이 업데이트 전까지 prompt 입력, packet upload, submit, capture, 새 query/fetch, score/Stage 변경은 0회다.
  PR #7은 기존 Draft/open 상태이고 main에 병합하지 않는다. CI green 뒤에도 같은 BrowserUse 로그인 세션의 같은 작업 탭만 사용한다.
- 세부 변경·검증·다음 순서는 [implementation progress P71](implementation_progress.md)와
  [P71 machine receipt](p71_wsl_boundary_resume_receipt.json)에 기록한다. token/cookie/account/tab ID는 기록하지 않는다.

## 이전 상태 인수인계 (P70, superseded)

- 로그인 필요 작업은 사용자의 BrowserUse Chrome plugin `extension`이 연결한 **이미 로그인된 세션과 그 세션 안의 기존 작업 탭**에서만 한다.
  `browser.user.openTabs()`로 탭을 열거하고, 정확한 descriptor를 `browser.user.claimTab()`에 넘긴 뒤 반환된 Tab 객체 하나를 유지한다.
  CDP/Codex 새 창·프로필·대체 탭·재로그인은 사용하지 않는다. 연결이 안 되면 실제 오류를 기록하고 멈춘다.
- P70에서 그 기존 BrowserUse 세션의 기존 탭을 claim해 같은 탭 안에서 새 Chat 화면으로 이동했다. 새 브라우저·창·탭·프로필은 만들지 않았다.
  확인한 화면은 Chat 선택, 실제 model label `6 Pro`, Work 미선택, Deep Research 미선택, 빈 composer였다. 이 확인은 로그인 세션 및
  현재 모드 확인이지 C15 응답·대화 결박 확인은 아니다. 기존 Library의 오래된 다른 job 결과는 사용하지 않았다.
- 실제 입력/작업 상태: prompt `0`, packet upload `0`, submit `0`, capture `0`, 새 query/fetch `0`, score/Stage 변경 `0`.
  활성 C15 R6 `PROJOB-df15a37c58ae7583924e58c0` / `010950`은 SQLite read-only 확인상 `PACKET_READY`, state version 2,
  submit/capture `0/0`, browser/conversation 미결박이다.
- PR #7은 head `43524413c24ab5e4ff32eca7ee0aaaa64bd49477`, `OPEN / DRAFT / MERGEABLE`이다. 동일 head의 Pro-first push/PR 및 V6 PR
  Actions run 35925176718, 35925180418, 35925180440은 모두 SUCCESS다. 전체 suite 7,911 (skipped 38, failure/error 0),
  Gate 1 receipt 4/4, Phase100 15/15, production static audit critical 0이다.
- 현재 blocker는 BrowserUse 로그인/탭 문제가 아니다. Python `FreshSessionBoundaryService.load_existing()`의 WSL 재개 검증이
  persisted Windows path와 `/mnt/c/...` caller path의 표현 차이로 `FreshSessionBoundaryError: fresh boundary receipt failed hash/path validation`
  을 던졌다. DB와 receipt를 바꾸지 않은 read-only 실패다. 다음 단계는 일반적인 WSL/Windows runtime-root normalization과 fail-closed 테스트다.
- 그 수리가 끝나고 새 exact-head CI green인 뒤에도 packet upload/전송은 이 기존 BrowserUse 세션의 same claimed tab에서만 한다.
  입력 직전에는 탭·job·대화·실제 Pro 모델·기존 초안/첨부를 다시 확인한다. 탭 제어가 실패하면 새 창에서 보내지 않는다.
- 세부 진행·run 링크·남은 작업은 [implementation progress P70](implementation_progress.md#p70--exact-head-ci-완료-기존-browseruse-pro-확인-wsl-경계-재개-오류-2026-09-24-kst)와
  [P70 machine receipt](p70_current_status_receipt.json)을 본다. token/cookie/account/tab ID는 기록하지 않는다.

## 현재 인수인계 요약 (P63)

- 로그인된 사용자 브라우저가 필요한 작업은 기존 BrowserUse `extension` 세션에서 한다. 이 규칙은 아래의
  과거 CDP 진단과 별개이며, CDP의 `C:\\ChromeDebug` 탭을 대체 세션으로 사용하지 않는다.
- P59에서 `browser.user.openTabs()`로 찾고 정확한 반환 객체를 `browser.user.claimTab()`한 ChatGPT 외부 탭의
  동일 참조를 유지했다. P60의 읽기 전용 재확인에서 URL `https://chatgpt.com/`, 제목 `ChatGPT`, 일반 Chat
  토글 `Chat=선택 / Work=미선택`, 모델 표시 `6 Pro`, composer 1개·빈 입력, 생성 중 제어 없음이 확인됐다.
  채팅 본문은 읽지 않았다. P60 확인에서 prompt 입력·업로드·전송은 각각 0회였다. 이것은 마지막
  관찰 기록이지 이후 화면을 재확인했다는 뜻은 아니다.
- P62에서는 preflight exit 0 후 같은 BrowserUse `extension`의 사용자 탭 1개 중 기존 ChatGPT 탭을
  `browser.user.openTabs()`로 찾고, 그 descriptor를 `claimTab()`에 넘긴 **반환 객체**로 현재 UI를 다시
  읽었다. Chat 선택, Work 미선택, 모델 control `6 Pro`, 빈 composer 1개, 생성 중 아님이 확인됐다.
  대화 본문과 composer 문구는 읽지 않았으며 입력·업로드·전송은 각각 0회다. P62 영수증에는 tab ID,
  계정 식별자, 쿠키나 인증값을 보존하지 않았다.
- 별도 `ProBrowserWorker`가 붙는 CDP endpoint와 claim한 BrowserUse 탭이 같은 Chrome page라는 증거는 없다.
  파이프라인이 정확한 BrowserUse 탭을 제어하지 못하면 수동 별도 세션으로 전송하지 말고 해당 live 단계를 보류한다.
- P62 중앙 SQLite read-only 조회에서 C15 R6는 `PACKET_READY`, state version 2, submit/capture 0/0,
  browser/conversation 미결박 상태다. 기존 job을 유지하며 새 successor를 만들지 않는다.
- 04:03 KST 상태 snapshot에서 PR #7 head `84e085b4922cde7abefe8fd47555ea0a0a325dcf`는 Draft/open/mergeable이었다.
  당시 확인에서
  해당 head의 Pro-first push/PR run과 V6 PR run은 진행 중이었다. Pro-first의 core-unit, browser-mock-e2e,
  static-security는 성공했고 full-regression은 실행 중이었다. 완료 전에는 이 head의 전체 CI 성공으로
  표현하지 않는다. 이전 f26 문서 전용 head의 성공 run은 아래 이력에만 해당한다.
- master goal은 현재 active이며 완료가 아니다. live full-thesis PASS는 C06 1/3이다.
  P63은 사용자가 강조한 기존 로그인 탭 사용 규칙을 문서화했으며 브라우저 조작·live canary 전송은 하지 않았다.

## 절대 게이트 — 로그인된 BrowserUse 세션에 결박

사용자가 로그인해 둔 세션이 작업 대상이면 **반드시 그 세션에서 한다.** 같은 사이트·계정·구독 화면을
보여주는 별도 브라우저는 대체물이 아니다. 대상 세션과 탭의 동일성이 입증돼야 하는 필수 조건이다.

| 확인 상태 | 반드시 할 일 | 금지되는 판단/행동 |
| --- | --- | --- |
| BrowserUse `extension` 연결 가능 | `browser.user.openTabs()`에서 기존 사용자 탭을 찾고, 반환된 정확한 객체를 `browser.user.claimTab(tab)`으로 결박 | `browser.tabs.list()`가 비었다는 이유로 사용자 탭이 없다고 결론내리기 |
| 기존 탭을 찾음 | 같은 객체·tab ID를 유지하면서 URL, 로그인 상태, 대화, 초안·응답 상태를 읽기 전용으로 확인 | 다른 탭/터미널에 전역 키 입력, 사용자 초안 덮어쓰기 |
| 새 대화가 필요함 | 확인된 로그인 탭 **안에서만** 새 대화를 시작 | 새 Chrome 창·새 프로필·시크릿 세션 만들기 |
| BrowserUse 연결·탭 확인 실패 | 정확한 도구 오류와 확인 범위를 기록하고 중단 | 재로그인 요구, CDP·`C:\\ChromeDebug` 창을 대체 세션으로 열기 |
| 앱 파이프라인이 별도 CDP worker만 지원 | worker가 claim한 바로 그 BrowserUse 탭을 제어한다는 증거가 생길 때까지 live submit 보류 | 같은 계정이라는 이유로 별도 창에서 전송하거나 성공 처리하기 |

입력·첨부·전송 직전에는 동일 탭에서 대상 job/run/pass, 대화 URL, 실제 선택 모델, composer 내용,
기존 첨부를 다시 확인한다. 사용자 초안이나 진행 중 응답은 보존한다. 준비물이 현재 요청과 정확히 일치하지
않으면 덮어쓰지 않는다. 전송 후에는 그 정확한 대화·응답·파일만 회수하고, 연결이 끊겼다는 이유로
이미 보낸 요청을 다시 전송하지 않는다.

이번 P61 문서 작업에서는 Chrome/BrowserUse를 열거나 조작하지 않았다. 다음 브라우저 작업 재개 시 위
게이트로 읽기 전용 재확인을 먼저 한다. 특히 `ProBrowserWorker`의 별도 CDP endpoint가 claim한 BrowserUse
탭과 다르다는 P59/P60 진단은 그대로 유효하다. 정확한 BrowserUse 탭에 결박되는 구현이 준비되지 않으면
prompt 입력·파일 업로드·Pro 전송은 하지 않는다.

## 최우선 원칙

로그인이 필요한 작업은 **이미 로그인된 사용자의 Chrome 세션과 기존 작업 탭에서 한다.**
새 Chrome 창·프로필을 열어 같은 서비스를 다시 로그인하는 방식으로 바꾸지 않는다.
새 대화가 필요하다는 것은 새 브라우저나 새 로그인 세션이 필요하다는 뜻이 아니다.

예: 기존 ChatGPT 탭에 이번 응답의 JSON이 보이면 그 탭에서 해당 파일을 확인해 다운로드한다.
fresh 연구가 승인돼 있으면 같은 로그인 세션의 기존 작업 탭 안에서 새 대화를 시작한다.
사용자 초안이나 진행 중 응답이 있는 탭을 비우거나, 다른 작업의 탭을 가져다 쓰지는 않는다.

## Backend 선택 — BrowserUse 세션을 그대로 사용

- 로그인된 기존 Chrome 세션이 필요한 요청이거나 사용자가 BrowserUse를 지정했으면 Chrome plugin의 `extension` 연결을 사용한다. 사용자 외부 탭은 `browser.user.openTabs()`에서 찾고, 정확히 일치하는 반환 객체를 `browser.user.claimTab(tab)`에 넘겨 결박한다.
- `browser.tabs.list()`는 agent가 만든 탭을 열거한다. 이 목록이나 `tabs.selected()`가 비어 있어도 사용자의 Chrome 탭이 없다는 뜻이 아니므로, 외부 탭 확인에는 반드시 `browser.user.openTabs()`를 사용한다.
- Codex가 새로 띄운 CDP Chrome, `C:\ChromeDebug`, 다른 디버깅 포트는 별도의 브라우저 backend다. 동일 계정이나 Pro 구독 표시가 보여도 사용자가 지정한 BrowserUse 로그인 세션과 같다는 증거가 되지 않는다.
- BrowserUse 연결이 성공했는데 탭 목록이 비었거나 대상 탭이 보이지 않으면 “사용자가 로그아웃됨”으로 단정하지 않는다. 기존 세션을 보존한 채 연결 범위·오류만 진단하고, 새 창·새 탭·새 프로필·CDP 대체 화면을 열지 않는다.
- 다른 backend는 동일 Chrome instance, 기존 세션, 대상 tab ID를 보존한다는 것을 실제로 확인할 수 있을 때만 허용한다. 그 확인이 안 되면 브라우저 작업을 보류하고 정확한 기술적 제한을 기록한다.
- 새 conversation이 필요한 경우에는 정확히 확인한 로그인 탭 안에서만 새 대화를 시작한다. 새 conversation은 새 브라우저 세션이나 새 창이 아니다.

## 다음 작업자의 확인 순서

1. 적용되는 BrowserUse 스킬을 읽고 사용자의 작업 범위와 기존 탭 사용 지시를 확인한다.
2. 현재 세션에 실제 호출 가능한 Chrome plugin/Node REPL 도구가 있는지 확인한다.
   설정의 `enabled=true`는 도구 호출 성공이나 Chrome 연결 성공의 증명이 아니다.
3. 브라우저 작업을 재개할 때 스킬의 preflight와 직접 연결 절차를 따른다.
   preflight 성공만으로 로그인 탭 접근이 된 것으로 보고하지 않는다.
4. Chrome plugin의 `extension` 연결로 기존 탭 목록을 읽는다. 해당 서비스의 기존 탭에서
   주소, 로그인 계정, 작업 대화, 미전송 초안·진행 중 응답을 확인하고 tab ID를 결박한다.
   계정 확인은 필요한 최소 범위로 하며 토큰·쿠키·인증값은 추출하거나 문서화하지 않는다.
5. 입력·업로드·전송 직전에 동일 tab ID의 URL, 대화와 입력창을 다시 확인한다.
   ChatGPT Pro 작업이라면 일반 Chat의 실제 Pro 모드를 확인한다. 구독 표시는 모드 증명이 아니다.
6. 기존 응답 회수는 그 응답의 job/run/pass와 첨부를 확인해서 수행한다.
   이미 전송한 요청은 연결을 복구했다는 이유로 다시 보내지 않는다.
7. 창·탭이 다른 작업으로 바뀌거나 연결이 실패하면 입력을 멈춘다. 확인 범위와 실제 오류를 기록하고
   기존 로그인·탭·초안·산출물을 보존한다. 재개에 필요한 조건만 간결하게 전달한다.

## 하지 말아야 할 우회

- 새 창, 임시 프로필, 시크릿 또는 헤드리스 브라우저를 만들어 재로그인 요청하기.
- 다른 디버깅 포트에 ChatGPT 탭이 없다는 이유로 사용자의 기존 탭도 없다고 판단하기.
- Node REPL 도구 미노출/연결 실패를 ChatGPT 로그아웃이나 Pro 응답 실패로 보고하기.
- 다른 backend가 실행된다는 이유만으로 로그인되지 않은 별도 세션으로 작업 대상을 바꾸기.
- 현재 활성 창만 믿고 전역 키 입력/붙여넣기를 해서 다른 탭이나 터미널에 입력하기.
- 사용자가 쓰는 Codex·Chrome을 임의로 재시작하거나 창·탭·로그인을 정리하기.
- 연결 실패 중 새 job/pass를 반복 생성하거나, 이미 제출된 요청을 재전송하기.

다른 backend는 적용 스킬의 허용 조건을 충족하고 **동일 로그인 세션·정확한 기존 탭**을 보존할 수
있을 때만 검토한다. 이 조건을 만족하지 못하면 새 창으로 진행하지 않는다.
서버 저장 검증에 독립적인 fresh 관찰이 필요하더라도 새 창·탭을 임의 생성하는 근거로 삼지 않는다.
허용된 기존 탭에서 검증 요건을 충족할 수 없다면 검증을 생략하거나 PASS로 바꾸지 말고 보류한다.

## P57/P58에서 확인된 사실과 미확인 부분

- P57에서 사용자의 로그인된 ChatGPT는 일반 Chrome의 기존 탭에 실제로 있었다.
  처음 점검한 9222/9234 디버깅 브라우저만으로 탭이 없다고 판단한 것은 작업자의 대상 선택 오류였다.
- 진단 당시 `node_repl` 설정은 활성화돼 있었지만 현재 에이전트의 실제 도구 목록에는 없었다.
  직접 호출 오류는 `TypeError: tools.mcp__node_repl__js is not a function`이었다.
- Codex 프로세스 시작 이후 연결 설정/bridge가 변경된 사실은 확인했다. 실행 중 세션에 설정 변경이
  반영되지 않았을 가능성은 있으나, 초기화 실패 로그가 없어 세부 원인은 확정하지 않았다.
- 화면이 확인 사이에 다른 사이트/GPT로 바뀐 이유는 미확인이다. 사용자나 다른 자동화의 탓으로
  단정하지 않는다. 불안정한 대상에 연구 prompt를 입력하거나 전송하지 않았다.
- P58에서 BrowserUse preflight와 extension runtime 초기화는 성공했으나 기존 탭 목록은 비어 있었다.
  이는 `browser.tabs.list()`/`tabs.selected()`의 agent-tab 결과만 확인한 것이며 사용자 외부 탭 목록을
  조회한 것은 아니다. 이 결과만으로 BrowserUse 연결의 외부 사용자 탭 범위를 판단하면 안 된다.
- 그 뒤 CDP의 `C:\ChromeDebug` 화면에 ChatGPT 탭을 열어 확인했으나, 그것이 BrowserUse가 지정한
  기존 로그인 탭과 같은 Chrome instance/session인지는 입증하지 못했다. 계정의 Pro 구독은 보였지만
  실제 Pro 모델 모드도 확인되지 않았다. 그러므로 이 CDP 탭은 다음 live 작업 대상으로 재사용하지 않는다.
- 이어진 화면 전환으로 무관한 금융 주문 화면이 보였으나 클릭·입력은 하지 않았다. 원인은 미확인이다.
  C15 R6 prompt 입력 0, upload 0, submit 0이며, 새 Pro 응답을 받거나 전송하지 않았다.

위 내용은 마지막 진단 이력이다. 다음 재개 때 BrowserUse `extension`으로 현재의 도구·탭·로그인을
다시 읽기 전용으로 확인해야 한다. BrowserUse 목록이 여전히 비면 대체 CDP 창으로 진행하지 않는다.
과거 process ID, window handle, tab ID를 현재 대상이라고 가정하거나 하드코딩하지 않는다.

P59에서 바로잡은 실제 외부 탭 확인과 CDP 대상 불일치는
[P59 영수증](p59_browseruse_external_tab_and_cdp_mismatch_receipt.json) 및 진행 장부에 기록했다.
P59 시점에는 기존 BrowserUse ChatGPT 탭을 찾고 결박했지만 E2R 대화가 아니었으며 모델 표시는 `Instant`였다.
CDP helper가 확인한 `C:\\ChromeDebug`의 페이지 목록에는 해당 ChatGPT 탭이 없어 같은 세션으로
간주할 수 없었다. 그 뒤 P60에서 같은 BrowserUse 탭 안에 새 대화 화면을 열고 `6 Pro` 모델 표시를
확인했으며, P62에서 해당 기존 extension 탭의 UI를 다시 읽기 전용으로 확인했다.

## P62 — 기존 BrowserUse 세션 재확인과 claim 객체 형식 진단

- BrowserUse Windows preflight는 exit 0이었다. 실제 도구 `mcp__node_repl__js`에서 canonical bootstrap 후
  `browser.user.openTabs()`는 사용자 탭 1개와 ChatGPT 후보 1개를 반환했다. agent의 탭 목록만으로 세션
  유무를 판단하지 않았다.
- `openTabs()` 항목은 `id`, `lastOpened`, `providerTabId`, `title`, `url`만 있는 metadata descriptor라서
  `.playwright`가 없다. 첫 진단 코드는 이 descriptor를 claim한 뒤에도 그 객체에 `.playwright.evaluate()`를
  호출해 `Cannot read properties of undefined (reading 'evaluate')`를 냈다. 로그인/Chrome 연결 실패가
  아니라 claim 반환 객체를 저장하지 않은 호출 실수였다.
- 수정된 호출은 `const claimed = await browser.user.claimTab(exactListedTab)`의 **반환값**을 잡아 사용했다.
  반환 객체의 `id`가 descriptor와 일치했고 `playwright` API가 있었다. 해당 exact claimed object에서 읽기 전용
  UI를 얻었다. 오류 후 새 창·다른 backend·재로그인으로 바꾸지 않았다.
- 마지막 확인 `2026-09-24 03:48 KST`: URL `https://chatgpt.com/`, Chat 선택, Work 미선택, model control
  label `6 Pro`, composer 1개·빈 상태, stop/generation control 없음. 본문과 composer 원문은 읽지 않았다.
  입력/첨부/전송 0/0/0이며 tab ID·계정·cookie/token은 receipt에 기록하지 않았다.
- Windows 중앙 SQLite를 `mode=ro`로 재조회한 C15 R6는 `PACKET_READY`, state version 2, submit/capture 0/0,
  `browser_session_id`/`conversation_id` null이었다. 기존 run만 보존했다.
- Python `ProBrowserWorker`는 여전히 별도 `CDP_ATTACH` endpoint를 쓴다. P62에서 BrowserUse tab을 직접
  확인했지만 Python pipeline과 결박되지 않았으므로 실제 prompt 입력·업로드·Pro 전송은 하지 않았다.
  다음 구현은 정확한 claimed extension tab에 Python worker를 연결하는 bridge와 non-submit integration test다.
- PR #7의 P62 기록 시점 head는 `f26b6f654b8f577790630afe7ee2900a0c0f1b2d`, Draft/open/mergeable다.
  기록 시점에는 세 run이 in-progress였고 static-security job만 완료됐지만, 이어진 read-only 재확인에서
  Pro-first `35902761257`, V6 `35902761194`, push `35902757082` 전체 conclusion이 SUCCESS로 바뀌었다.
  이는 f26 문서 전용 head 결과이며, P62 adapter/test diff는 포함하지 않는다.

기계 판독형 상세 기록은 [P62 영수증](p62_browseruse_existing_session_revalidation_receipt.json)이다.
위 표면 상태는 그 시점의 관찰로만 유효하다. 이후 재개 때마다 현재 BrowserUse 탭을 다시 열거하고
정확한 `claimTab()` 반환 객체에서 재확인한다.

## P63 — 기존 로그인 탭에서 결과물 회수 후 파이프라인에 연결

사용자는 로그인 세션이 필요한 BrowserUse 작업은 새 창을 열지 말고 이미 로그인된 기존 세션에서 하라고
재강조했다. 이 단계의 순서는 **기존 탭 claim → 현재 응답/첨부 확인 → 기존 결과물 회수 → 준비된 job에
연결**이다. JSON이나 응답이 이미 보이는 경우 새 세션에서 재생성하거나 같은 요청을 다시 보낼 이유가 없다.
새 conversation이 실제로 필요할 때만 기존 로그인 탭 안에서 시작한다.

이 규칙을 이번에 문서로 명확히 했을 뿐, P63에서는 BrowserUse/Chrome을 열거나 조작하지 않았다. 따라서
P62의 UI 관찰(2026-09-24 03:48 KST)이 마지막 실제 관찰이며, 지금 로그인·탭 상태를 재확인한 것처럼
취급하지 않는다. 입력·파일 다운로드·업로드·전송·source query/fetch는 이번 문서 작업에서 모두 0회다.

04:03 KST GitHub 확인에서 PR #7은 head `84e085b4922cde7abefe8fd47555ea0a0a325dcf`, Draft/open/mergeable였다.
Pro-first push run [35905532661](https://github.com/Daikisong/stock_agent/actions/runs/35905532661)과 PR run
[35905539789](https://github.com/Daikisong/stock_agent/actions/runs/35905539789), V6 PR run
[35905539730](https://github.com/Daikisong/stock_agent/actions/runs/35905539730)은 조회 시 진행 중이었다.
push run의 core-unit, browser-mock-e2e, static-security job은 성공했고 full-regression은 진행 중이었다.
나머지 run이 끝나기 전에는 현재 head의 전체 CI 성공으로 보고하지 않는다.

## 중단된 연구 인수인계

- 전체 goal은 9월 8일 연결 문제로 `BLOCKED` 처리됐으나 9월 24일 사용자가 재개했고 현재 상태는 `active`다.
  아직 완료가 아니다. 이 문서 작성이나 CI 성공을 live 연구 완료로 해석하지 않는다.
- 마지막 검증 기준 C15 R6는 `PACKET_READY`, 제출 0회다. 다음에 재개하면 준비된 같은 R6를 확인한다.
  job: `PROJOB-df15a37c58ae7583924e58c0`, run: `PRORUN-ff542ef979f09bcaf7cf2545`.
- C15 R5의 과거 원본·전송 이력은 진단용으로 보존하며 재전송하지 않는다.
- 상세 준비 이력과 검증 범위는 [진행 장부](implementation_progress.md)의 P57 및 9월 8일 보완 기록을 따른다.
- P58 packet-ready 복구와 P59 BrowserUse 외부 탭/CDP 경계는 각 [P58 영수증](p58_packet_ready_resume_and_browser_boundary_receipt.json), [P59 영수증](p59_browseruse_external_tab_and_cdp_mismatch_receipt.json) 및 진행 장부 끝부분을 따른다.
- 마지막 외부 탭/일반 Chat/Pro UI 관찰과 P62 PR/CI/R6 snapshot은 [P62 영수증](p62_browseruse_existing_session_revalidation_receipt.json)에 기록한다. P60의 이전 snapshot은 [P60 영수증](p60_existing_browseruse_session_handoff_receipt.json)에 보존한다.
- BrowserUse 로그인 세션 결박 절대 게이트와 진행 이력은 [진행 장부](implementation_progress.md)의 P61/P62에 기록했다. P62 문서화만으로 pipeline bridge 또는 live canary가 완료된 것은 아니다.
- 이 지침은 문서 변경이다. 브라우저 연결 복구나 운영 코드의 자동 강제가 구현·검증됐다는 주장이 아니다.

## P65 — 최신 탭 결과와 활성 R6 준비물 구분

- 사용자는 로그인된 BrowserUse 작업은 이미 로그인된 세션과 그 기존 탭에서 하라고 재강조했다. 새 창·새
  프로필·별도 CDP 브라우저에서 대신 로그인하거나 작업을 이어가지 않는다. 기존 응답/파일이 있으면 같은
  탭에서 회수한다. 정확한 기존 탭을 제어할 수 없으면 실제 오류와 확인 범위를 남기고 멈춘다.
- 마지막 실제 BrowserUse 확인(P64)은 Library 화면의 읽기 전용 확인이었다. 화면의 모델 표시는
  `GPT-6 Sol Light`였으며 실제 Pro 모드가 아니므로, Pro 구독을 실제 Pro 모델 선택 증거로 세지 않는다.
  이어진 `cdp` 요청은 `Capability is not available: cdp`였고 다른 브라우저로 전환하지 않았다.
- Library에서 활성 C15 R6 ID는 발견되지 않았다. 화면에 확인된 기존 C15 파일은 과거 job
  `PROJOB-7c02db014fefb06b1258ffe9`(frozen, `NEEDS_PUBLIC_GAP_CLOSURE`) 또는 별도 partial job
  `PROJOB-384a8e0aad776a6d99391a6f`에 속했다. 두 파일 모두 C15 R6 결과가 아니며 R6 증거로 재사용하지 않는다.
- 유지 중인 R6는 `010950 / S-Oil`, `2026-08-23`, `C15_MATERIAL_SPREAD_SUPERCYCLE`이다. job
  `PROJOB-df15a37c58ae7583924e58c0`, run `PRORUN-ff542ef979f09bcaf7cf2545`, initial pass
  `PROPASS-a7654d1d80c9c041afb5777f`다. SQLite read-only 상태는 `PACKET_READY`, version 2, submit/capture
  `0/0`, browser/conversation 미결박이다.
- 오프라인 prompt 재컴파일은 기존 immutable receipt와 27개 필수 질문, transport/contract prompt hash가
  일치했다. 이것은 packet 준비 일관성일 뿐, 브라우저 업로드·전송 또는 live canary 성공이 아니다.
- 이번 문서화에서 BrowserUse/Chrome 조작, 다운로드, prompt 입력, 업로드, submit, source query/fetch,
  점수 변경은 0회다. 다음 작업은 exact claimed BrowserUse 탭에 대한 generic bridge와 non-submit
  identity 검증이다. 그 연결 전에는 Python CDP worker를 통해서도 Pro 전송하지 않는다.

P65 문서 갱신 시각은 2026-09-24 04:57 KST다. 이 기록은 그 시점 이후 상태를 보장하지 않는다. 재개 시 기존 `extension`
세션의 사용자 탭을 다시 열거·claim한 후 작업 대화와 실제 선택 모델을 재확인한다. 인증값과 tab ID는 저장하지 않는다.

## P66 — 기존 Library C15 artifact 회수와 import 경계

- 2026-09-24 05:14 KST에 BrowserUse `extension`이 열거한 사용자 ChatGPT 탭 1개를 정확히 claim한 뒤,
  같은 탭의 Library에서 `S-OIL_010950_E2R_ResearchDossierV3_PROJOB-04140b7ffd8accef505deeda.json`을
  열고 visible Download 메뉴로 내려받았다. 새 창·탭·프로필은 만들지 않았다. 다운로드는
  `suggestedFilename()` 형식 불일치(`globalThis.e2rDownload.suggestedFilename is not a function`)로 후처리
  단계에서 오류가 났지만, BrowserUse download event는 이미 완료됐고 기본 Downloads 파일이 존재함을
  확인했다. 재다운로드하지 않았다. 파일 SHA-256은
  `332c4be02d598f143567ec9366904e5e4bf4eb9c524ba9a2fa6baf20003a78e5`, 크기는 180,794 bytes다.
- 파일은 활성 R6가 아닌 이전 C15 job `PROJOB-04140b7ffd8accef505deeda`, run
  `PRORUN-87c15cd5bef1e1723bf19129`, initial pass `PROPASS-64ef728f2ff790e7fce6ae95`에 결박되어 있다.
  target `010950 / S-Oil`, as-of `2026-08-23`, `C15_MATERIAL_SPREAD_SUPERCYCLE`; raw status는
  `NEEDS_PUBLIC_GAP_CLOSURE`다. 따라서 C15 R6 결과나 full-thesis PASS로 세지 않는다.
- 기존 `ResearchDossierParser`는 `DOWNLOADED_JSON`으로 이 파일을 읽었고 입력/출력 JSON hash는 동일했다.
  material/counter/resolution fact는 각각 `16/3/3` (총 22), question family 27, source documents 8,
  lineages 8, search routes 62, unresolved gaps 10이다. 이어진 dialect/pre-schema/identity 처리와 JSON
  schema validator는 **placeholder conversation ID를 유지한 구조 검증**으로 통과했다. 이 검증은 source
  verification, capture-bound import, 서버 대화 결박 또는 canary PASS가 아니다.
- 로컬 DB의 동일 job은 `USER_ATTENTION_REQUIRED`, submit/capture `1/0`, `conversation_id=null`이다.
  terminal event는 exact initial user turn에 job/run marker가 없다는 server-persistence 오류를 기록한다.
  `browser_capture_receipt.json`, normalized import 파일 및 dossier import 행은 없다. 따라서 기존
  `ProDossierImporter`의 capture-bound 경로로는 아직 적재할 수 없다. 실제 대화 ID·assistant turn을
  복구하거나 정식 Library-artifact recovery 경계를 구현해야 하며, 둘 중 어느 것도 임의로 꾸며내지 않았다.
- 활성 R6 `PROJOB-df15a37c58ae7583924e58c0`는 기존 packet 그대로 `PACKET_READY`, submit/capture `0/0`다.
  다운로드한 이전 artifact를 R6에 섞거나 DB를 변경하지 않았다. 마지막 화면 캡처에는 `GPT-6 Sol Light`와
  빈 입력창이 보였으므로 현재 Pro 모드의 증거도 아니며, 이 단계에서 prompt 입력·업로드·전송은 없었다.
- 상세 machine-readable 기록은 [P66 회수 영수증](p66_c15_library_artifact_recovery_receipt.json)이다.
  기존 Library 파일과 새로 받은 사본은 repo에 추가하지 않았다. artifact 자체는 사용자 Downloads에 남아 있다.

## P67 — 로그인된 BrowserUse 세션만 사용한다는 우선 규칙 재확인

- 사용자는 로그인된 세션이 필요한 BrowserUse 작업을 **이미 로그인해 둔 그 세션에서** 하라고 재강조했다.
  이에 따라 이 문서 맨 앞에 기존 `extension` 세션과 정확한 기존 작업 탭만 사용한다는 규칙을 단일 우선 지침으로
  명시했다. 새 Codex Chrome/CDP 창, 별도 프로필, 재로그인은 대체 수단이 아니다.
- 절차는 기존 사용자 탭 열거 → 정확한 탭 claim → 반환된 실제 제어 객체 유지 → 현재 대화·초안·첨부 확인이다.
  기존 결과가 있으면 같은 탭에서 회수하고, 실제 새 대화가 승인된 경우에도 같은 로그인 탭 안에서만 시작한다.
  입력·첨부·전송 직전에 URL, 대상, 실제 모드, 초안과 기존 응답을 같은 탭에서 재확인한다.
- 탭 연결이나 제어가 실패하면 확인 범위와 실제 오류를 남기고 그 단계에서 멈춘다. 다른 창에서 계속하거나
  재로그인·재전송하지 않는다. 사용자 초안, 진행 중 응답, 기존 탭과 로그인 상태를 보존한다.
- P67은 문서 변경만 수행했다. BrowserUse 연결·탭 재확인, 입력, 업로드, 다운로드, 전송, 새 query/fetch,
  점수/Stage 변경은 0회다. 마지막 실제 브라우저 관찰은 P66의 같은 사용자 탭 Library 작업이며, 당시 화면의
  모델 표시는 `GPT-6 Sol Light`였다. 이를 현재 세션이나 실제 Pro 모드의 확인으로 취급하지 않는다.
- P66 artifact/import 경계와 수치는 [P66 회수 영수증](p66_c15_library_artifact_recovery_receipt.json)을,
  전체 작업 순서는 [진행 장부](implementation_progress.md)의 P66/P67을 참조한다.

이번 문서 갱신은 2026-09-24 05:27 KST다. 이는 브라우저 상태 재확인이 아니다. 다음 로그인 필요 작업 전에 기존
`extension` 세션의 사용자 탭을 다시 열거하고 exact `claimTab()` 객체에서 대상 대화와 실제 모드를 확인한다.
tab ID, 계정 식별자, 쿠키·토큰은 보관하지 않는다.

## P68 — Python worker를 기존 BrowserUse claimed tab에 read-only 결박

- 사용자가 요청한 대로 로그인 세션 작업은 기존 BrowserUse `extension` 탭에서만 수행했다. Windows preflight는
  exit 0, 현재 도구의 `mcp__node_repl__js` 호출 가능, 외부 사용자 탭 하나가 확인됐다. 정확한 descriptor를 claim한
  반환 객체를 유지했다. 새 Chrome/프로필/창/탭은 만들지 않았다.
- 현재 해당 탭은 `https://chatgpt.com/library?search=ResearchDossierV3` / `ChatGPT - 라이브러리`다. bridge를 통해
  Python `ProBrowserWorker(BROWSER_USE_EXTENSION)`가 handshake한 다음 공개 DOM의 title/origin을 읽는 통합 smoke를
  통과했다. conversation 본문은 읽지 않았다. Library 화면에서는 실제 선택 모델이 드러나지 않아 Pro model은
  **미검증**이다.
- 구현 파일은 [bridge 설계·한계 문서](browseruse_extension_bridge.md), Python RPC/worker 연결,
  BrowserUse `extension` Node module이다. job별 token은 user cache의 `0600` handoff에만 잠시 존재했고 smoke 종료 뒤
  server와 파일을 닫고 삭제했다. token, tab ID, 계정 식별자는 영수증에 넣지 않았다.
- 중요한 런타임 규칙: HTTP callback은 요청을 queue에 넣기만 하고 browser API를 직접 부르지 않는다. Python job과
  `bridge.runUntil(...)`를 **같은 활성 Node REPL 호출 안에서** 돌려야 BrowserUse execution context가 유지된다.
  별도 shell에서 나중에 연결하면 실제 오류 `node_repl exec context not found`가 발생한다. 이는 로그인 만료가 아니다.
- BrowserUse API에서 `tab.url()`/`tab.title()`은 비동기 함수이며, `waitForEvent`는 download/filechooser만 지원한다.
  따라서 response body 캡처는 지원하지 않고 해당 경로는 fail-closed한다. CDP/private API로 우회하지 않는다.
- 실제 통합 smoke는 read-only다: prompt/upload/submit/capture/query/fetch/score/Stage 변경은 모두 0회다. 중앙 SQLite를
  `mode=ro` + `query_only=ON`으로 다시 확인한 C15 R6 `PROJOB-df15a37c58ae7583924e58c0`은 `PACKET_READY`, version 2,
  submit/capture `0/0`, browser/conversation null로 유지됐다.
- `node --check` PASS, bridge 6/6, 기존 Browser adapter 55/55, fresh-session orchestration 76/76 PASS다. 세 static audit도 모두
  PASS / critical 0이다. base head `96438f3fd9660a9f7ff71f3284c9063fa2dd8910`의 Pro-first/V6/push CI는 SUCCESS였지만
  P68 diff를 포함하지 않는다. P68 diff의 전체 repository regression과 exact-head Actions는 아직 **PENDING**이다.
- machine receipt: [P68 bridge smoke 영수증](p68_browseruse_extension_bridge_smoke_receipt.json).

다음 단계는 P68 diff의 전체 repository regression과 새 exact-head CI다. 이들이 성공한 뒤에도 기존 같은 BrowserUse 탭에서
actual Pro 선택 상태를 직접 확인해야 한다. 확인 전에는 동일 C15 R6 prompt 입력, upload, submit을 하지 않는다. master
goal은 미완료이며 live full-thesis는 계속 C06 1/3이다.

## P69 — 기존 로그인 세션 원칙 재강조 및 검증 상태 최신화 (2026-09-24 06:47 KST)

- 사용자는 로그인된 세션이 필요한 BrowserUse 작업은 이미 로그인된 그 세션에서 하라고 다시 요청했다. 위 최우선 규칙을 bridge
  기술 문서에도 적용해, 로그인 필요한 작업 범위·정확한 탭 claim 절차·실패 시 정지·대체 창/CDP/profile/재로그인 금지를 명시했다.
- 문서와 P68 receipt의 오래된 “미실행” 상태를 바로잡았다. bridge 6/6, adapter 55/55, orchestration 76/76, 세 static audit
  PASS / critical 0을 재확인했다. 전체 repository unittest와 변경분 exact-head CI는 여전히 PENDING이다.
- 마지막 실제 BrowserUse 조작은 06:43 KST의 existing-tab read-only smoke이며, P69는 문서와 로컬 검증만 했다. 실제 Pro 선택은
  미검증이다. 새 browser/window/tab/profile 0, prompt/upload/submit/capture/query/fetch/score/Stage 변경 0.
- machine receipt는 [P68 bridge smoke 영수증](p68_browseruse_extension_bridge_smoke_receipt.json), 기술 경계는
  [BrowserUse bridge 문서](browseruse_extension_bridge.md)에 기록했다. 인증 토큰·쿠키·계정·tab ID는 저장하지 않는다.
