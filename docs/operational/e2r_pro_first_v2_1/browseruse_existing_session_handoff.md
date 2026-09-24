# BrowserUse: 로그인된 기존 세션 사용 및 재개 지침

최종 갱신: 2026-09-24 18:32 KST (P88: exact-head CI, 기존 탭 관찰, durable recovery 오류 불일치 수리 기록).
이 문서는 인증된 UI 작업의 실행 지침이다. **로그인이 필요한 BrowserUse 작업은 사용자가 이미 로그인해 둔 BrowserUse `extension` 세션의 기존 작업 탭에서만 한다.**

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

## 최신 재개 지점 — P88 (2026-09-24 18:32 KST)

- PR #7은 OPEN/DRAFT/MERGEABLE, main 미병합이다. exact head는 `956535588feda0fef6c07b9ca4bd2630b4beccde`이며 한글 commit은 `BrowserUse recovery 테스트에 미확정 picker 상태 보완`이다.
- 같은 SHA의 Pro push [35975891389](https://github.com/Daikisong/stock_agent/actions/runs/35975891389)와 Pro PR [35975895348](https://github.com/Daikisong/stock_agent/actions/runs/35975895348)은 SUCCESS다. V6 [35975895401](https://github.com/Daikisong/stock_agent/actions/runs/35975895401)은 18:32 KST 조회 시 `offline-contract / Run full unit-test suite`가 계속 `in_progress`; receipt consistency와 production static audit은 PASS, 전체 테스트는 아직 결론 전이다.
- P88에서는 machine preflight exit `0` 뒤 기존 BrowserUse `extension`의 사용자 탭 두 개를 읽기 전용 열거하고, `https://chatgpt.com/` / title `ChatGPT`인 기존 탭 하나를 정확히 claim했다. 같은 탭의 관찰은 로그인 prompt 없음, 모델 메뉴 표시 `6 Pro`, 빈 composer 1개, user turn 0, file input 5개, 선택 파일 0이었다. 탭 이동·새 창/탭 생성·입력·첨부·전송은 없었다. 이는 검사 시점의 화면 증거이며, P86 상태를 재사용하거나 durable same-job gate를 대신하지 않는다.
- durable C15 R6 job을 P88에 mode=ro + `PRAGMA query_only=ON`으로 다시 읽었다. DB상 최신 갱신은 여전히 `2026-09-24T07:28:13.906437Z`: S-Oil `010950`, `USER_ATTENTION_REQUIRED`, version 18, submit/capture `0/0`, browser/conversation binding 없음, `safe_unprepared_resume=false`; last error class/message는 `BrowserUseBridgeError` / `BrowserUse bridge transport failed (TimeoutError: timed out)`. 새 pass/event나 DB write는 없다.
- P87의 CI 실패 원인은 테스트 proxy fixture 두 곳에 `unknown_owner_count`가 빠진 것이었다. 생산 fail-closed 판정은 완화하지 않고 fixture만 고쳤으며, exact-head Pro push/PR은 통과했다. P88 NSLAB Raw acquire/recover는 `skipped`여서 새 fetch는 없었다.
- 해당 exact DB message에는 `BRIDGE_OPERATION_FAILED:` 접두사가 없다. 기존 allowlist/test는 접두사가 있을 때만 열려 있어 같은 job을 복구 함수가 거부할 결함을 확인했다. production allowlist를 DB에 실제 기록된 단일 exact message에 맞추고, suffix near-match 차단을 유지한 채 orchestration 91/91과 local production static audit (`critical_count=0`)을 통과시켰다. 이 수정은 아직 remote PR head `95653558…`에 포함되지 않았으며 현재 V6 run도 수정 전 head를 검사 중이다.
- 상세 진행 기록은 [implementation progress](implementation_progress.md)의 P88 항목에 있다. 아래 P87/P86 항목은 당시 시각의 이력이며, 현재 상태는 이 P88 블록을 우선한다.

## P86 확인 기록 — historical (P88이 현재 판정)

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
