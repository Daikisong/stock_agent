# Census Mode v1 Deep Backfill Plan

이번 Goal에서는 full deep backfill을 실행하지 않고 계획만 생성한다.

- shard_count: 10
- pending_symbol_count: 8
- Stage2plus_candidate_count: 37
- top source/provider gaps: ['report_event_without_accepted_claim', 'market_anomaly_requires_source_claim']
- checkpoint_strategy: per-shard checkpoint with source/config hash
- resume_strategy: skip processed symbols and merge deterministic stage rows
