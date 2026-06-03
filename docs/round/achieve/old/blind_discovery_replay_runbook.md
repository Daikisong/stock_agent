# Blind Discovery Replay Runbook

Checkpoint 26 separates two backtest types:

```text
asof_research_replay
-> current main historical research backtest
-> official universe first
-> current/local search reconstructs old public evidence
-> rejects documents after replay date

forward_archive_replay
-> strict future validation
-> uses only search/report snapshots saved by live operation
```

Blind discovery replay asks:

```text
Could E2R_STANDARD discover candidates without using the answer key?
```

The answer key is `data/benchmark_labels/e2r_known_winners.json`.
It is evaluation-only.

## Command

```bash
PYTHONPATH=src python -m e2r.cli.run_blind_discovery_replay \
  --start-date 2023-01-01 \
  --end-date 2026-05-14 \
  --frequency monthly \
  --market KR \
  --flow E2R_STANDARD \
  --no-fixture-source-proxy \
  --output-directory output/backtests/blind_discovery
```

Defaults:

```text
fixture_source_proxy = false
use_search_snapshots = true
use_report_snapshots = true
llm_enabled = false
```

Diagnostic comparison, not proof of blind discovery:

```bash
PYTHONPATH=src python -m e2r.cli.run_blind_discovery_replay \
  --start-date 2023-01-01 \
  --end-date 2026-05-14 \
  --frequency monthly \
  --market KR \
  --flow E2R_STANDARD \
  --allow-fixture-source-proxy \
  --output-directory output/backtests/blind_discovery_fixture_proxy
```

## Output

```text
blind_discovery_summary.md/json
discovered_candidates.csv/json
benchmark_recall_report.md/json
missed_benchmark_labels.md
false_positive_report.md
stage_lifecycle_report.md
evidence_coverage_report.md
limitations.md
source_coverage_report.md
benchmark_leakage_audit.md
llm_review.md/json
```

## Evaluation Order

Correct order:

```text
1. run E2R_STANDARD candidate generation
2. write discovered candidates
3. load benchmark labels
4. compare labels against outputs
```

Wrong order:

```text
benchmark labels -> candidate generation
```

## Success Criteria

Structural labels:

```text
should appear at least in event_search/deep_research or Stage 2
within expected window tolerance
```

One-off / boom-bust labels:

```text
must not become Stage 3-Green
```

Missing historical report/news snapshots:

```text
must be reported, not hidden
```

## Current Limitation

The current repo has a small point-in-time search/report snapshot fixture set.
It does not yet have complete archived search snapshots for the full Korea universe.

So a miss can mean:

```text
source_missing
no_report_snapshot
no_news_snapshot
not_in_universe
search_snapshot_unavailable
report_snapshot_unavailable
```

That is why future live runs should store search/report snapshots.

For the practical 2023~2026 research replay, run:

```bash
PYTHONPATH=src python -m e2r.cli.run_asof_research_replay \
  --start-date 2023-01-01 \
  --end-date 2026-05-14 \
  --frequency monthly \
  --market KR
```

This is closer to the manual ChatGPT-style workflow, but it is not strict
forward-archive proof.

## What Changed In Checkpoint 24

Before:

```text
BlindDiscoveryReplay
-> HistoricalUniverseReplay(mode=hybrid)
-> benchmark comparison
```

That was useful as a regression proxy, but it was not a true blind replay.

Now:

```text
BlindDiscoveryReplay
-> E2RStandardReplay
-> E2R_STANDARD
-> benchmark comparison
```

This is closer to the real agent. If the historical source archive is thin, the output is allowed to be sparse. Sparse but honest is preferred over a curated success that looks like discovery.
