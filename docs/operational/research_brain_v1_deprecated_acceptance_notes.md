# Research Brain v1 Deprecated Acceptance Notes

Research Brain v1 산출물의 `READY`는 production-ready가 아니라 `IMPLEMENTATION_READY`로 재라벨링한다.

## v1이 검증한 것

- 연구 메모리 import, leakage guard, 기본 planner task generation
- SourceTask budget 존재 여부
- Evidence OS를 직접 mutate하지 않는 bridge guard

## v1이 검증하지 못한 것

- expected archetype routing correctness
- R13 over-routing 방지
- URL row의 실제 EvidenceAnchor replay 검증
- CandidateEvent 30개 이상 운영 dry-run
- SourceTask execution과 accepted claim 연결

쉬운 예: C06 replay가 R13으로 라우팅됐는데도 task가 만들어졌다는 이유로 pass되면, 그건 `뭔가 조사했다`는 smoke test일 뿐 `HBM 사건을 HBM으로 이해했다`는 증거가 아니다.
