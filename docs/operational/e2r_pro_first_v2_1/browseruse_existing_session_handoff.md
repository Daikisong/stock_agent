# BrowserUse: 로그인된 기존 세션 사용 및 재개 지침

최종 갱신: 2026-09-24 04:03 KST (P63).
사용자의 명시적 요청을 기록한 운영 지침이며, 로그인 세션이 필요한 작업의 기준 backend는 BrowserUse다.
아래 P57/P58 실행 내용은 이력과 장애 범위를 구분해 보존한다. BrowserUse 세션을 CDP로 대체하라는 뜻이 아니다.

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
