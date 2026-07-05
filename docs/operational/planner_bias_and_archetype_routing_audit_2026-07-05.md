# Planner Bias And Archetype Routing Audit - 2026-07-05

이 문서는 Research Brain planner가 어떤 아키타입을 1순위로 골랐는지 본다.

쉬운 예: 선생님이 모든 과목 시험을 봐야 하는데, 채점할 때마다 건설 계약형(C05) 답안지만 먼저 꺼내면 전체 시험 검증이 아니다.

## Summary

- status: `PLANNER_ARCHETYPE_ROUTING_BIAS_NOT_READY`
- planner_run_count: `350`
- hypothesis_run_count: `35`
- distinct_top1_archetype_count: `4`
- c05_top1_share: `0.828571`
- planner_output_score_stage_key_count: `0`

## Top1 Counts

- `C01`: `2`
- `C05`: `29`
- `C06`: `2`
- `C29`: `2`

## Blockers

- `planner_top1_c05_share_over_limit`
- `planner_top1_distinct_archetype_count_below_minimum`
- `target_unknown_rows_promoted_after_planner`
- `source_primary_context_survived_into_promotion`
- `mandatory_archetypes_not_planner_attempted`
