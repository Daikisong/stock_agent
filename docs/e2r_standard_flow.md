# E2R_STANDARD Flow

`E2R_STANDARD` is the canonical production flow.

It is the path that live runs and serious blind backtests should use.

```text
Universe
-> official cheap scan
-> OpenDART detail fetch for watch disclosures
-> Report Radar
-> Free Web Research
-> Evidence Builder
-> Feature Engineering
-> optional LLM Evidence Analyst
-> Deterministic Score
-> StageClassifier
-> RedTeam
-> Parser Audit
-> Stage Lifecycle Monitor
-> Brief / Report
```

Simple example:

```text
OpenDART finds 단일판매·공급계약체결
-> detail parser extracts amount/duration if available
-> Report Radar searches "수주잔고 OPM PDF"
-> evidence becomes feature input
-> deterministic StageClassifier decides Stage
-> LLM may explain, but cannot override Stage
```

## Production vs Diagnostic

Production flow:

```text
E2R_STANDARD
```

Diagnostic replay modes:

```text
official_only
case_fixture
hybrid
```

Diagnostic modes are useful for evidence coverage and regression tests, but they are not production flow.

## Blind Discovery Rule

Blind discovery tests must use `E2R_STANDARD`.

Benchmark labels are never input evidence.

Example:

```text
Wrong:
known winner label -> candidate generation

Correct:
E2R_STANDARD output -> compare against benchmark labels afterward
```

## Checkpoint 24 Replay Rule

Blind replay now calls the same `E2R_STANDARD` flow that live runs use.

The default path is:

```text
historical point-in-time sources
-> E2R_STANDARD
-> discovered candidates
-> benchmark label evaluation
```

It does not use `official_only`, `case_fixture`, or `hybrid` as a hidden proxy.

If old search/report snapshots are missing, the replay says:

```text
search_snapshot_unavailable
report_snapshot_unavailable
candidate_generation_limited_by_missing_snapshots
```

Example:

```text
HD현대일렉트릭 appears only if a historical search/report snapshot exists
or official evidence independently routes it into research.
The benchmark label itself cannot create the candidate.
```

`--allow-fixture-source-proxy` is available only for diagnostic regression. Its report is marked:

```text
fixture proxy mode; not proof of live discovery
```

## LLM Role

The LLM layer is optional.

Allowed:

```text
query expansion
document extraction review
contradiction flags
Korean stage explanation
```

Not allowed:

```text
final Stage decision
score override
invent missing contract amount or EPS
buy/sell wording
```

The deterministic score and StageClassifier remain the source of truth.
