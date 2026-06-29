# Research Brain v4 Production Readiness Verdict

- verdict: PRODUCTION_SHADOW_READY
- production_cutover_ready: False
- previous_v4_claim: PRODUCTION_READY
- reclassification: v4 was shadow-ready, not production-cutover-ready
- daily_watchlist_pass: True
- production_ready_interpretation: False
- original_v4_blockers: []
- cutover_blockers:
  - candidate_event_report contained fixture-like symbols and cached/source fixture paths.
  - SourceAcquisitionRunnerV4 counted stored source snapshots; `snapshot://` is not live source fetch.
  - A2_REAL_REPLAY_VERIFIED promoted count was 0.
  - deterministic_scorer_output_count was 5, below the cutover minimum of 15.
  - planner model identity was not fully recorded in rows where `model=null`.
  - full production cutover report reproducibility was not proven against the current HEAD.
- five_day_run_count: 5
- fake_provider_used_total: 0

## What v4 Proved

- planner schema guard ran.
- snapshot/source-record based SourceTask execution ran.
- Evidence OS bridge produced accepted claims from stored records.
- deterministic scorer and StageCourt were exercised for a small subset.
- v4 static audit counters were clean under the v4 shadow definition.

## What v4 Did Not Prove

- real market universe only.
- no fixture-like symbols.
- live official source connector execution.
- full text contract-blind claim extraction.
- A2 real replay promotion.
- multi-day real official source run.
- operational latency and budget SLA.
- current HEAD report reproducibility.

쉬운 예: v4는 시험장에서 모의 서류로 절차를 끝까지 연습한 상태다. 이번 cutover gate는 실제 창구에서 쓸 원본 서류와 신분 확인까지 요구하므로, v4 결과만으로 `PRODUCTION_CUTOVER_READY`라고 부르면 안 된다.
