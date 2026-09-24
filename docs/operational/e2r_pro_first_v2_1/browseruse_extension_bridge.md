# 기존 BrowserUse 탭과 Pro-first pipeline 연결

최종 갱신: 2026-09-24 12:07 KST (P77 상태 요약; 구현 이력은 아래 각 phase 시점 기록).
현재 상태: PR #7의 P76 head `d294f395738254da1f616d361038a35548fa6c4e`에서 Pro push/PR 및 V6 PR GitHub Actions가 모두 SUCCESS다. 상세 CI 수치와 C15 R6 재개 지점은 [최신 BrowserUse 인수인계](browseruse_existing_session_handoff.md#최신-상태-인수인계-p77)와 [진행 장부 P77](implementation_progress.md#p77--기존-browseruse-로그인-탭-재확인과-p76-exact-head-ci-정정-2026-09-24-1207-kst)를 따른다. 로그인 작업은 사용자가 이미 로그인한 **동일 BrowserUse extension 세션의 기존 탭에서만** 수행하며, CDP·새 창/탭/프로필·재로그인 대체는 금지한다.

## 왜 이 연결이 필요한가

`ProBrowserWorker`의 기존 CDP backend는 사용자가 BrowserUse extension으로 열어 둔 ChatGPT 탭과 같은
브라우저 세션이라는 보장이 없다. 계정이나 구독 표시가 같아도 다른 Chrome/CDP endpoint는 대체 로그인 세션이
아니다. 따라서 로그인된 탭이 필요한 작업에서는 `browser.user.openTabs()`가 반환한 정확한 descriptor를
`browser.user.claimTab(descriptor)`에 넘기고, **claim이 반환한 실제 Tab 객체**를 pipeline까지 전달한다.

```text
현재 Chrome의 로그인 탭
  → BrowserUse extension의 exact claimed Tab 객체
  → 활성 Node REPL 안의 request dispatcher
  → private HTTP bridge + job 전용 임시 handoff
  → Python ProBrowserWorker(BROWSER_USE_EXTENSION)
  → 기존 ChatGPT adapter의 제한된 visible UI 동작
```

## 로그인 세션 사용 규칙 — 작업자 필수

ChatGPT 로그인이나 사용자의 현재 세션이 필요한 모든 작업(기존 대화 확인, Library 파일 다운로드, 첨부,
Pro 모드 확인, prompt 입력·전송, 응답 회수)은 BrowserUse Chrome plugin의 `extension`이 연결한 **사용자 기존
로그인 세션과 그 안의 기존 작업 탭**에서만 한다. 로그인 세션이 필요한데 이 탭을 열거·claim·제어할 수 없으면
그 단계에서 멈추고 실제 오류를 남긴다. 다른 창·CDP·프로필을 열거나 재로그인을 요청하지 않는다.

절차는 `openTabs()` → 대상 descriptor 확인 → `claimTab()`의 반환 Tab 객체 보관 → 같은 객체에서 현재 대화·초안·첨부
확인 순이다. 새 대화가 꼭 필요해도 이 기존 탭 안에서 시작한다. 입력·첨부·전송 직전에 URL, 작업 ID, 기존 요청·응답,
실제 선택 모델을 같은 탭에서 다시 확인하고, 탭이나 내용이 예상과 다르면 조작하지 않는다. 구독에 “Pro”라고 적힌 것만으로
실제 Pro 모델 선택으로 판정하지 않는다. 이 지침은 bridge 기술 구현보다 우선한다.

새 Chrome, 새 프로필, 새 로그인, 탭 복제, 새 browser context/tab, CDP attach, ChatGPT private API는 이 경로에
없다. 새 ChatGPT 대화가 필요하면 adapter가 **같은 탭** 안에서만 이동한다.

## 실행 수명과 동일 탭 보장

구현 파일은 [`browseruse_extension_bridge.mjs`](../../../src/e2r/pro_first/browser/browseruse_extension_bridge.mjs),
[`browseruse_extension_bridge.py`](../../../src/e2r/pro_first/browser/browseruse_extension_bridge.py),
[`worker.py`](../../../src/e2r/pro_first/browser/worker.py)다.

1. Node REPL에서 기존 외부 탭을 열거하고 정확한 descriptor를 claim한다. 반환 Tab 객체를 전역 변수에 보관한다.
2. 그 Tab 객체 하나만 `startBrowserUseExtensionBridge()`에 넘긴다. bridge는 시작·매 RPC 전후로
   `https://chatgpt.com` origin을 확인하고, job ID와 opaque claimed-tab session identity를 묶는다.
3. 임시 bearer token은 WSL의 `~/.cache/e2r/browseruse/<job_id>.json`에만 기록한다. 부모 디렉터리는 `0700`,
   파일은 `0600`, 소유자 일치·regular file·no symlink를 Python worker가 확인한다. token, tab ID, 계정 정보는
   source, receipt, 로그에 기록하지 않는다. 실행 종료 시 bridge가 자기 session identity와 일치하는 handoff만
   삭제한다.
4. **Python job은 같은 `mcp__node_repl__js` 호출 안에서 `bridge.runUntil(...)`로 실행해야 한다.** HTTP 요청
   handler는 JSON을 queue에 넣기만 한다. 실제 BrowserUse API 호출은 활성 Node REPL 실행 문맥의 dispatcher가
   수행한다. REPL 호출이 끝난 뒤 별도 shell에서 Python을 돌리면 `node_repl exec context not found`가 날 수 있다.
   이는 로그인 실패가 아니라 extension API 실행 문맥의 수명 문제다.
5. `BrowserWorkerSession.close()`는 Python HTTP client만 닫는다. 사용자의 탭·Chrome·로그인은 닫거나 초기화하지
   않는다. bridge 종료는 private server와 임시 handoff만 정리한다.

Bridge endpoint는 WSL의 현재 default route에서 Windows private gateway를 찾아 RFC1918 인터페이스에만 bind한다.
요청은 job 전용 256-bit random bearer token을 검사하고, Python 측도 loopback/RFC1918 endpoint만 받는다. 네트워크
응답 capture API나 browser-context request client는 노출하지 않는다.

## 허용된 UI 기능과 의도적 한계

- 읽기: URL/title, visible locator의 count/text/attribute/value, 허용된 read-only DOM expression.
- visible 조작: locator click/fill/press, ChatGPT origin 안의 navigation/reload. hidden network/API/storage 호출,
  synthetic DOM mutation, CDP 세션 생성은 거부한다.
- packet 첨부: visible attach locator를 누른 뒤 **기존 Chrome 프로세스 소유의 Windows Open dialog**에서 JSON을
  선택한다. global keystroke나 `set_input_files`를 쓰지 않는다. UI에 표시된 파일명뿐 아니라 browser-selected
  file 내용의 canonical hash도 durable packet hash와 일치해야 한다.
- 결과 회수: BrowserUse extension이 지원하는 visible `download` event와 `saveAs`만 연결한다. 현재 BrowserUse
  `playwright.waitForEvent`는 `download`와 `filechooser`만 제공하며 `response` event/body는 제공하지 않는다.
  그러므로 response-only 또는 private authenticated-fetch가 필요한 artifact 경로는 **fail-closed**한다. 새
  network/response 우회는 추가하지 않는다.
- model gate: 계정의 “Pro” 구독 표시는 충분하지 않다. Chat 일반 모드에서 실제 선택된 Pro model label을 같은
  탭에서 확인해야 한다. adapter는 직접 모델을 추정하지 않고, Pro가 확인되지 않으면 submit을 막는다.

## P68 실제 확인 결과

2026-09-24 KST에 BrowserUse preflight exit 0 뒤 현재 사용자 외부 탭 하나를 열거하고 exact claim 반환 객체를
보존했다. 현재 페이지는 Library다. 같은 claim 객체로 bridge를 열고 Python `ProBrowserWorker`를 실행해 handshake와
public DOM `title/origin` 읽기를 통과했다.

```text
URL/title      https://chatgpt.com/library?search=ResearchDossierV3
public DOM     ChatGPT - 라이브러리 / https://chatgpt.com
same-tab       exact claim 객체와 Python handshake identity 일치
new window/tab/profile  0 / 0 / 0
prompt/upload/submit/capture  0 / 0 / 0 / 0
source query/fetch, score/Stage change  0 / 0 / 0
actual Pro model   이번 Library 화면에서 확인 불가; 미검증
```

통합 smoke는 실제 탭의 URL을 바꾸거나 대화 본문을 읽지 않았다. handoff 파일은 run 종료 뒤 삭제됐다. 이 PASS는
**Python worker가 그 exact claimed tab의 공개 DOM에 읽기 전용으로 도달한 것**만 증명한다. C15 R6의 Pro 준비,
upload, send, capture 또는 live canary 결과는 증명하지 않는다. 활성 C15 R6는 별도 SQLite `mode=ro` 확인에서
`PACKET_READY`, state version 2, submit/capture 0/0, browser/conversation null로 유지됐다.

구현 중 드러난 API 차이도 재발 방지를 위해 기록한다.

- BrowserUse `tab.url()`/`tab.title()`은 비동기 함수다. property로 읽으면 `Invalid URL`이 난다.
- BrowserUse raw evaluate는 string expression을 받는다. arrow callback 문자열 자체는 결과가 `undefined`일 수 있어,
  코드가 검증된 read-only callback만 expression 안에서 호출한다. Node `new Function`은 REPL runtime에서 차단되어
  사용하지 않는다.
- 외부 HTTP callback 안에서 BrowserUse API를 부르면 `node_repl exec context not found`가 난다. 따라서 callback은
  queue only이고, browser action은 `runUntil`의 활성 REPL dispatcher에서만 수행한다.
- `waitForEvent("response")`는 실제 API가 지원하지 않는다. response body를 얻기 위해 CDP나 private API로 바꾸지
  않는다.

## 검증·다음 단계

- `node --check src/e2r/pro_first/browser/browseruse_extension_bridge.mjs`: PASS.
- 새 bridge 단위 테스트: 6/6 PASS (private endpoint, origin fail-closed, nested locator identity, secure handoff,
  exact session binding, selected JSON hash).
- 기존 browser adapter 회귀: 55/55 PASS. WSL Chromium shared libraries를 위해 다음 로컬 경로를 사용했다:
  `LD_LIBRARY_PATH=/home/eorb915/.cache/e2r-playwright-libs/usr/lib/x86_64-linux-gnu`.
- fresh-session orchestration 회귀: 76/76 PASS. Production static audit, V2 static/generalization audit,
  V2.1 fresh-efficiency audit 모두 PASS; 세 audit critical count는 각각 0이다.
- 실제 BrowserUse exact-tab read-only integration smoke: PASS.
- 상세 machine receipt: [`p68_browseruse_extension_bridge_smoke_receipt.json`](p68_browseruse_extension_bridge_smoke_receipt.json).

P70에서 PR #7 head `43524413c24ab5e4ff32eca7ee0aaaa64bd49477`의 Pro-first push/PR 및 V6 PR Actions
[35925176718](https://github.com/Daikisong/stock_agent/actions/runs/35925176718),
[35925180418](https://github.com/Daikisong/stock_agent/actions/runs/35925180418),
[35925180440](https://github.com/Daikisong/stock_agent/actions/runs/35925180440)이 모두 SUCCESS임을 확인했다.
전체 저장소 suite는 7,911 tests / skipped 38 / failure·error 0, Gate 1 receipt는 4/4, Phase100은 15/15,
production static audit은 critical 0이다. PR은 계속 Draft/open/mergeable이고 병합하지 않았다.

같은 P70 작업에서 사용자가 이미 로그인해 둔 BrowserUse `extension` 세션의 기존 사용자 탭 하나를 exact claim했다.
그 동일 탭 안에서만 새 Chat 화면을 열어 Chat 선택, `6 Pro`, Work 미선택, Deep Research 미선택, 빈 composer를 확인했다.
다른 브라우저·창·탭·프로필은 만들지 않았고, 과거 Library artifact도 사용하지 않았다. 이것은 Pro UI 상태 확인일 뿐
C15 R6 대화 결박이나 응답 증거가 아니다. prompt 입력/upload/submit/capture/query/fetch/score/Stage 변경은 0회다.

resume preflight에서 `FreshSessionBoundaryService.load_existing()`가 Windows absolute receipt path와 WSL `/mnt/c/...`
caller path를 같은 canonical path로 비교하지 않아 `FreshSessionBoundaryError: fresh boundary receipt failed hash/path validation`
을 냈다. SQLite/receipt를 읽기 전용으로 확인했고 이 오류 후에도 C15 R6는 `PACKET_READY`, submit/capture `0/0`이며
기존 artifact·승인·receipt를 수정하지 않았다. 이는 BrowserUse 로그인 오류가 아니다.

P70 시점의 다음 단계는 Windows/WSL runtime-root 정규화였다. 이는 P71에서 구현·검증했으며, 현재 남은 다음 단계는 아래
P71 절의 새 exact-head CI다. P70 상세 이력은 [implementation progress](implementation_progress.md)와
[BrowserUse handoff](browseruse_existing_session_handoff.md)에 보존했다.

## P71 — 실제 boundary resume와 미완료 범위

P71에서 `_resolve_runtime_root()`를 추가해 WSL의 absolute Windows drive path를 기존 `/mnt/<letter>` mount에만 대응시킨다.
receipt의 original path values는 건드리지 않고 hash를 먼저 검증한다. relative/UNC 경로, 없는 drive mount, `..`,
symlink resolution으로 mount 바깥을 가리키는 경로는 거부한다. `start`, `start_independent`, `load_existing` 모두 같은
resolver를 사용한다.

실제 C15 R6에 대해 persisted leakage-manifest hash를 확인하고, SQLite `mode=ro` + `query_only=ON`의 제한된 job-store
adapter로 `load_existing()`을 실행했다. 동일 job/state `PACKET_READY`/version 2, submit/capture `0/0`이 반환됐으며,
DB·boundary receipt·packet에 write하지 않았다. focused orchestration은 80/80 PASS이고 세 static audits도 PASS/critical 0이다.
이건 boundary resume만 입증하며 BrowserUse response, packet upload, submit, capture 또는 live canary PASS는 아니다.

P71 source/docs diff의 full unittest 및 exact-head CI는 아직 pending이다. CI가 green이 되기 전까지 live UI 입력을 하지 않는다.
그 후에도 로그인 필요 작업은 사용자의 **같은 BrowserUse `extension` 로그인 세션과 그 안의 기존 claimed tab**에서만 한다.
다른 창·CDP·프로필·재로그인으로 옮기지 않는다. 최신 handoff는
[`implementation_progress.md` P71](implementation_progress.md)와 [`browseruse_existing_session_handoff.md`](browseruse_existing_session_handoff.md)다.
