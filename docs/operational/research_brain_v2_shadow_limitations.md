# Research Brain v2 Shadow Limitations

- v2는 `READY_FOR_SHADOW_DAILY_RUN`이지 `PRODUCTION_READY`가 아니다.
- v2 candidate_event_count 60은 L2 59 / L6 1로 sector coverage가 치우쳤다.
- v2 SourceTask accepted claim은 local evidence handoff 기반이라 Evidence OS full acceptance path가 아니다.
- v2 watchlist `verified_score`는 cheap_scan preview였고 deterministic E2R score가 아니다.
- v2 A2 sample은 URL/snapshot/anchor/date/entity/primitive replay 전체 검증을 의미하지 않는다.
- v2 LLM planner는 schema/payload validation hook이었고 real provider planning run이 아니었다.
- v2 router fixture는 archetype id가 event에 들어간 쉬운 fixture라 raw market event routing 검증이 부족했다.

쉬운 예: v2는 시험장 입장권을 확인한 상태이고, v3는 실제 답안지를 근거 문서와 함께 채점기에 넣는 단계다.
