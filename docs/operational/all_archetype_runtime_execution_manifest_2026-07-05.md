# All Archetype Runtime Execution Manifest - 2026-07-05

이 문서는 next runtime attempt plan을 실제 Census v4 Research Brain 입력으로 연결하는 실행 장부다.

쉬운 예: 이전 문서가 병원 예약 목록이라면, 이 문서는 실제 접수 창구에 내는 예약 파일 경로와 실행 명령이다.

## Summary

- execution_status: `READY_FOR_RESEARCH_BRAIN_INPUT_NOT_EXECUTED_BY_PARITY_CLI`
- seed_event_path: `docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl`
- seed_event_count: `105`
- source_task_shell_path: `docs/operational/all_archetype_next_runtime_source_tasks_2026-07-05.jsonl`
- source_task_shell_count: `105`
- output_root: `output/census_v4/2026-07-05-goal4-all-archetype-next-runtime-attempt`
- brain_candidate_event_seed_path: `docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl`
- brain_planner_batch_size: `1`
- brain_runtime_budget_seconds: `14400.0`
- expected_seed_source_in_census_v4: `external_candidate_event_seed_path`

## Command

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass --as-of-date 2026-07-05 --universe krx --output-root output/census_v4/2026-07-05-goal4-all-archetype-next-runtime-attempt --v3-output-root output/census_v3/2026-07-01 --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED --brain-web-mode enabled --research-brain-report-dir docs/operational --brain-planner-provider real --brain-source-acquisition live_full_bounded --brain-universe-limit 105 --brain-planner-success-limit 105 --brain-planner-batch-size 1 --brain-max-source-tasks-per-plan 5 --brain-max-fetches-per-task 3 --brain-accepted-claim-target 35 --brain-max-distinct-candidate-attempts 105 --brain-retry-max 1 --brain-claim-extractor-provider auto --brain-claim-extractor-timeout-seconds 180.0 --brain-runtime-budget-seconds 14400.0 --brain-candidate-event-seed-path docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl --brain-stage-promotion-mode strict --full-thesis-smoke-mode disabled --target-gate full_thesis --max-iterations 1 --fail-on-run-mode-overclaim true --fail-on-atomic-mismatch true --fail-on-semantic-guard true --fail-on-critical-audit true --write-operational-docs true
```

## Safety

- 이 manifest는 parity CLI에서 실행하지 않는다.
- 실행 전 source-task shell은 점수/Stage 입력이 아니다.
- Research Brain이 source-backed Evidence OS claim을 만든 뒤에만 score/stage promotion을 검토한다.
- Goal4 next-attempt 실행은 planner batch size 1을 사용해 provider timeout을 후보별 failure로 남긴다.
- Goal4 next-attempt 실행은 111개 후보를 batch size 1로 전수 planner 처리한 뒤 source/claim 단계까지 갈 수 있도록 14400초 finite runtime budget을 사용한다.
