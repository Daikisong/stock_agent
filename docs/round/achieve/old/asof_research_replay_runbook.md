# As-Of Research Replay Runbook

`asof_research_replay` is the main historical backtest flow for now.

It asks a practical question:

```text
If the E2R_STANDARD agent had run on date D,
using the same manual-style research workflow,
would it have found the right candidates?
```

## Flow

```text
replay date D
-> official historical KOSPI/KOSDAQ universe as of D
-> official price/disclosure/financial/risk data visible as of D
-> official cheap scan
-> Layer-1 candidates
-> web research only for those candidates
-> accept documents only if published_at/report_date <= D
-> Evidence
-> Feature Engineering
-> deterministic Stage
-> benchmark labels only after output
```

Simple example:

```text
2023-08-01 replay
-> official universe includes HD현대일렉트릭
-> 2023-07-27 supply-contract disclosure is visible
-> it becomes a Layer-1 candidate
-> the agent searches old public reports for HD현대일렉트릭
-> a 2023-07-27 report is accepted
-> a 2023-08-15 report would be rejected
```

## Not Forward Archive Proof

This mode may use current search or local search fixtures to reconstruct old
public evidence. Therefore it must be labeled:

```text
point_in_time_status = retrospective_reconstructed
strict_pit_proof = false
```

For strict proof later, use `forward_archive_replay`, which can only use
search/report snapshots saved during actual live operation.

## Command

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

## Output

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

## Date Rules

```text
published_at <= replay date
-> allowed

published_at > replay date
-> rejected

undated document
-> date_unverified
-> may support observation/Yellow
-> cannot create Stage 3-Green alone
```

## Failure Stages

The report says where a benchmark failed:

```text
not_in_universe
failed_official_cheap_scan
free_web_research_not_executed
free_web_research_no_results
documents_after_asof_date
documents_date_unverified
evidence_not_created
stage_not_high_enough
```

## What Not To Do

```text
do not use benchmark labels as input
do not define the universe from search snapshots
do not fabricate missing report/news evidence
do not lower Stage 3-Green thresholds just to improve recall
do not call this strict forward-archive proof
```
