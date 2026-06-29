# Research Brain v4 Readiness Reclassification

`research_brain_v4_production_readiness_verdict.md`의 과거 `PRODUCTION_READY` 표기는 실제 live production cutover readiness가 아니라 `PRODUCTION_SHADOW_READY`로 재라벨링한다.

## v4가 통과한 것

- planner schema guard
- snapshot/source-record 기반 SourceTask execution
- Evidence OS bridge 일부
- deterministic scorer 일부
- static audit counters

## v4가 아직 통과하지 못한 것

- real market universe only
- no fixture-like symbol
- live official source connector execution
- full text claim extraction
- A2 real replay promotion
- multi-day real official source run
- operational latency/budget SLA
- report/current HEAD reproducibility

## 운영 해석

- 기존 v4 reports는 삭제하지 않는다.
- 기존 수치는 shadow run의 증거로 보존한다.
- `PRODUCTION_READY`는 이번 Production Cutover Gate 완료 전까지 금지한다.
- 현재 허용 라벨은 `PRODUCTION_SHADOW_READY` 또는 `READY_FOR_CUTOVER_AUDIT`이다.

쉬운 예: 저장된 스냅샷으로 채점기가 돌아간 것은 “채점 절차 연습 성공”이다. 하지만 실제 운영은 오늘 실제 공시, 실제 provider request id, 실제 원문 anchor가 있어야 한다.
