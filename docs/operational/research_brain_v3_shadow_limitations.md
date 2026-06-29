# Research Brain v3 Shadow Limitations

- v3의 정확한 라벨은 `DAILY_SHADOW_RUN_PASS`이며 `PRODUCTION_READY`가 아니다.
- v3 report는 `production_ready=False`를 유지한다.
- v3 acceptance의 real provider count는 0이고 fake provider가 사용되었다.
- v3 SourceAcquisitionRunner는 snapshot/event payload 기반이며 live provider는 not configured였다.
- v3 Evidence OS bridge는 CandidateEvent/SourceTask 기반 synthetic assertion을 만들 수 있었다.
- v4 목표는 real planner, real source acquisition, real extraction, deterministic score/stage 연결이다.

쉬운 예: v3는 모의 신분증으로 출입 절차를 연습한 상태이고, v4는 실제 신분증과 실제 서류로 출입 기록을 남기는 단계다.
