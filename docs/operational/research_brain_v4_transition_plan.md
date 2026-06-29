# Research Brain v4 Transition Plan

목표: fake/snapshot shadow를 real planner + real source + real extraction production shadow로 전환한다.

- planner는 fake/none/real을 분리한다.
- fake provider 사용 시 production-ready 판정은 금지한다.
- source task는 저장된 실제 source snapshot 또는 live official provider 결과만 EvidenceDocument로 쓴다.
- event_summary는 quote나 accepted claim으로 쓰지 않는다.
- Evidence OS accepted claim만 deterministic scorer와 StageCourt에 들어간다.
- source_proxy_only/evidence_url_pending/price_path_only memory는 current score evidence가 아니다.
