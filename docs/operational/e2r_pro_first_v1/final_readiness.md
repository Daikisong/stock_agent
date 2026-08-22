# Final readiness

현재 P15 판정:

```text
implementation: PRO_FIRST_PLATFORM_IMPLEMENTATION_READY
browser shadow: CHATGPT_WEB_SHADOW_PENDING_USER_ENV
live pilot: LIVE_PILOT_PENDING_DEDICATED_PROFILE_LOGIN
```

구현 판정 근거는 core unit 152/152, browser mock 36/36, golden E2E 4/4, 전체 회귀 7,366개 failure/error 0, compile PASS, `git diff --check` PASS, static critical 0이다. conditional live-provider skip은 기존 38개이며 Pro-first 전용 검증 skip은 0이다.

후반 production 경로는 `import → finite URL verification → deterministic gap adjudication → material-gap-only bounded supplement → 7 component → 21 evidence-only Judge → 기존 deterministic scorer → AtomicStageCourtV2 → publication`으로 연결됐다. provider가 없거나 유효한 7-component impact roster를 만들지 못하면 0점으로 확정하지 않고 pending에 머문다.

실제 Windows CDP attach는 성공했지만 전용 E2R Chrome profile에는 로그인 세션이 없어 prompt editor가 나타나지 않았다. job `PROJOB-70e6a50ae757bd874e602a85`는 `USER_ATTENTION_REQUIRED`, submit/capture `0/0`이다. 기존 기본 Chrome profile의 cookie나 token은 복사하지 않았다.

전용 profile에서 수동 로그인한 뒤 `submit_count=0` shadow가 끝나야 `CHATGPT_WEB_SHADOW_COMPATIBILITY_PASS`를 쓸 수 있다. 그 다음 one-use approval nonce를 소비해 실제 canary를 한 번 전송하고 capture→StageCourt까지 닫혀야 `PRO_FIRST_LIVE_CANARY_PASS`다.

첫 live canary 전에는 `PRO_FIRST_LIVE_OPERATION_READY`라고 부르지 않는다.
