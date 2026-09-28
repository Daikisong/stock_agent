# 상태기계

주요 정상 경로:

```text
CANDIDATE_SELECTED
→ PACKET_BUILDING
→ PACKET_READY
→ BROWSER_PREPARING
→ AWAITING_USER_APPROVAL
→ APPROVED
→ SUBMITTING
→ RESEARCH_RUNNING
→ RESULT_DETECTED
→ CAPTURING_ARTIFACTS
→ CAPTURE_COMPLETE
→ IMPORTING
→ DOSSIER_IMPORTED
→ VERIFYING_SOURCES
→ GAP_ADJUDICATION
→ COMPONENT_RESEARCH
→ JUDGING
→ SCORING
→ STAGECOURT
→ FINAL
```

중요한 원자 조건:

- `SUBMITTING`: packet/prompt/browser session에 묶인 single-use approval nonce가 소비돼야 한다.
- `IMPORTING`: READY가 마지막에 기록된 capture receipt의 모든 hash가 맞아야 한다.
- `JUDGING`: component memo 7개가 완성돼야 한다.
- `SCORING`: evidence-only Judge 21개가 완성돼야 한다.
- `FINAL`: deterministic score와 `AtomicStageCourtV2` 결과가 모두 있어야 한다.

전송 클릭이 실패해도 `submit_count=1`을 되돌리지 않는다. 예를 들어 버튼 클릭 직후 브라우저 연결이 끊기면 자동 재전송하지 않고 `USER_ATTENTION_REQUIRED`로 남긴다. 실제 요청이 서버에 도착했는지 모르는 상태에서 다시 누르면 중복 연구가 생길 수 있기 때문이다.
