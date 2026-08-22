# Final readiness

현재 tracked P14 판정:

```text
implementation: 검증 중
browser shadow: CHATGPT_WEB_SHADOW_NOT_YET_RUN
live pilot: LIVE_PILOT_NOT_YET_PREPARED
```

Implementation ready 판정 조건은 core unit, golden E2E 4/4, browser mock, 전체 회귀, compile, diff, static critical 0, CI 4 jobs green이다.

실제 로그인 세션에서 `submit_count=0` shadow를 통과해야 `CHATGPT_WEB_SHADOW_COMPATIBILITY_PASS`를 쓸 수 있다. 그 뒤 explicit approval nonce를 소비해 실제 canary를 한 번 전송하고 capture→StageCourt까지 닫혀야 `PRO_FIRST_LIVE_CANARY_PASS`다.

첫 live canary 전에는 `PRO_FIRST_LIVE_OPERATION_READY`라고 부르지 않는다.
