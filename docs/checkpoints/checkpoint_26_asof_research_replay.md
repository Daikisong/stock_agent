# Checkpoint 26: As-Of Research Replay

## What Changed

Checkpoint 26 adds the correct historical backtest flow for the current
research stage:

```text
asof_research_replay
```

It starts from official historical data, not search/report snapshots.

Flow:

```text
replay date D
-> official historical KOSPI/KOSDAQ universe as of D
-> official cheap scan from price/disclosure/financial/risk data
-> Layer-1 candidates
-> web research only for Layer-1 candidates
-> reject documents published after D
-> Evidence / Feature Engineering / deterministic Stage
-> benchmark labels only after output
```

Simple example:

```text
2023-08-01 replay
-> HD현대일렉트릭 is in official universe
-> 2023-07-27 supply-contract/report evidence is allowed
-> 2023-08-15 evidence would be rejected
```

## New Modules

```text
src/e2r/backtest/asof_research_replay.py
src/e2r/backtest/historical_official_store.py
src/e2r/research/asof_web_research.py
src/e2r/cli/run_asof_research_replay.py
src/e2r/cli/backfill_official_history.py
```

New docs:

```text
docs/asof_research_replay_runbook.md
docs/official_history_backfill_runbook.md
```

## Naming Clarification

Snapshot-only replay is now documented as future validation:

```text
forward_archive_replay
```

It means:

```text
use only search/report snapshots saved during live operation
```

The current main historical research backtest is:

```text
asof_research_replay
```

It means:

```text
use official historical universe first,
then reconstruct old public documents with strict as_of date filtering
```

## Validation Run

Command run:

```bash
PYTHONPATH=src python -m e2r.cli.run_asof_research_replay \
  --start-date 2023-01-01 \
  --end-date 2026-05-14 \
  --frequency monthly \
  --market KR \
  --max-candidates-per-date 50 \
  --max-web-research-candidates-per-date 20 \
  --max-queries-per-candidate 8 \
  --max-results-per-query 5 \
  --require-date-verified-for-green \
  --allow-undated-docs-for-yellow-only \
  --save-reconstructed-snapshots \
  --output-directory output/backtests/asof_research_replay
```

Output root:

```text
output/backtests/asof_research_replay/2023-01-01_to_2026-05-14
```

Run summary:

```text
replay_dates: 41
total_universe_rows_scanned: 514
layer1_candidates: 120
web_researched_candidates: 120
documents_rejected_after_asof: 49
documents_date_verified: 646
documents_date_unverified: 0
discovered_candidates: 120
Stage 3-Green count: 0
Stage 3-Yellow count: 0
Stage 3-Red count: 0
```

Benchmark recall:

```text
detected: 11 KR labels
missed/outside window: 2 KR labels
unsafe one-off/overheat Green: 0
```

Detected examples:

```text
HD현대일렉트릭 -> 2023-08-01, deep_research
효성중공업 -> 2023-06-01, event_search
일진전기 -> 2023-12-01, deep_research
산일전기 -> 2025-03-01, event_search
삼양식품 -> 2024-06-01, event_search
한화에어로스페이스 -> 2024-08-01, deep_research
```

## Interpretation

This run proves the replay now starts from official historical universe data
and only uses web research after Layer-1 candidate generation.

It does not prove strict forward-archive discovery because reconstructed
search/report snapshots are labeled:

```text
point_in_time_status = retrospective_reconstructed
strict_pit_proof = false
```

The zero Stage 3-Green count is intentional conservatism. Layer 1 recall can
improve through better official history and report parsing, but Stage 3-Green
was not loosened.

## Output Reports

Generated:

```text
asof_replay_summary.md/json
discovered_candidates.csv/json
benchmark_recall_report.md/json
missed_benchmark_labels.md
failure_stage_report.md
stage_lifecycle_report.md
evidence_coverage_report.md
reconstructed_snapshot_report.md
false_positive_report.md
limitations.md
```

## Remaining Limits

```text
official historical archive is still fixture-sized
OpenDART detail history is represented by local fixtures only
Stage lifecycle detection is not yet fully integrated into as-of replay output
report/news reconstruction is not strict forward proof
```

## Next Step

Run a weekly as-of replay after expanding official historical data:

```text
more KRX/data.go.kr price history
more OpenDART disclosure/detail history
more report/news reconstructed snapshots with verified dates
```

After several real daily runs have saved search/report snapshots, use
`forward_archive_replay` for strict proof.
