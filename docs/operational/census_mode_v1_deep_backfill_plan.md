# Census Mode v1 Deep Backfill Plan

이번 Goal에서는 full deep backfill을 실행하지 않고 계획만 생성한다.

- shard_count: 10
- pending_symbol_count: 0
- Stage2plus_candidate_count: 0
- top source/provider gaps: []
- checkpoint_strategy: per-shard checkpoint with source/config hash
- resume_strategy: skip processed symbols and merge deterministic stage rows
