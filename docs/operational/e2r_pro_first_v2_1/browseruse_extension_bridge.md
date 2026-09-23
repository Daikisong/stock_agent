# 기존 BrowserUse 탭과 Pro-first pipeline 연결

최종 갱신: 2026-09-24 06:47 KST (P69 문서·검증 상태 동기화).
상태: **동일 로그인 탭에서 read-only 통합 smoke PASS. 실제 Pro 선택, packet upload, submit, 응답 capture는 미검증.**

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

P69에서 bridge 6/6, browser adapter 55/55, fresh-session orchestration 76/76을 다시 확인했고, 세 정적 감사도 모두
PASS / critical 0이었다. 이것은 변경분의 targeted 검증이며 **전체 저장소 unittest 및 P68 변경을 포함한 새 exact-head
GitHub Actions는 아직 미완료**다. 다음 순서는 한글 커밋으로 현재 변경을 PR #7 브랜치에 push하고 새 head CI가 끝날 때까지
확인하는 것이다. 새 head CI green 전에는 live 입력을 하지 않는다. 그 뒤에도 로그인 필요 작업은 반드시 기존 BrowserUse
extension 세션의 같은 작업 탭에서 actual Pro model을 직접 확인해야 한다. 보이지 않거나 Pro가 아니면 멈춘다. 새 창·CDP·다른
프로필로 바꾸지 않는다. 모든 조건이 충족돼도 기존 C15 R6의 승인 경계만 이어간다.
