# Checkpoint 14 Report

## Scope

Checkpoint 14 adds a controlled Korea live-lite pilot runner.

The new path is:

```text
Korea universe
-> date-based OpenDART disclosure collection
-> KoreaCheapScanner
-> top cheap candidates
-> budgeted FreeWebResearchRunner
-> Korean MorningBrief
-> JSON/Markdown output files
```

Simple example:

```text
2024-05-21 OpenDART disclosures are collected once by date range
-> supply contract candidate appears
-> targeted queries are generated only for event/deep candidates
-> run log records skipped queries and dropped search results
```

## Added Components

- `src/e2r/pipeline/korea_live_lite.py`
  - `KoreaLiveLiteBudget`
  - `KoreaLiveLiteConfig`
  - `KoreaLiveLiteRunner`
  - `KoreaLiveLiteRunLog`
  - fixture source factory for the Checkpoint 13 Korea fixtures

- `tests/test_korea_live_lite.py`
  - validates budgets
  - confirms missing credentials fall back to fixture mode
  - checks output files
  - verifies date-based OpenDART collection
  - verifies event/deep symbol budgets
  - verifies Stage 3-Green cross-evidence requirement
  - verifies hard-risk candidates are not escalated

- `docs/korea_live_lite_runbook.md`
  - fixture-mode execution
  - live-lite credential requirements
  - output files
  - budget controls
  - operating cautions

## Budget Defaults

```text
OpenDART calls: 1,000/day
KRX/data.go.kr calls: 500/day
Naver Search calls: 2,000/day
event_search symbols: 200/day
deep_research symbols: 30/day
```

The runner estimates source calls and uses `SearchBudget` for web query limits.

## Date-Based Disclosure Collection

The runner avoids this expensive pattern:

```text
for each symbol:
    OpenDART disclosure search
```

Instead it does:

```text
OpenDART list by date range once
-> group/filter disclosures by symbol inside the scanner
```

This keeps the first live-lite pilot from becoming one API call per listed company.

## Output Files

For `YYYY-MM-DD`, the runner writes:

```text
output/korea_live_lite/YYYY-MM-DD_candidates.json
output/korea_live_lite/YYYY-MM-DD_evidence.json
output/korea_live_lite/YYYY-MM-DD_brief.md
output/korea_live_lite/YYYY-MM-DD_run_log.json
```

## Stage 3-Green Guardrail

Live-lite mode requires at least two independent evidence types for Stage 3-Green by default.

Example:

```text
broker report only
-> strong deterministic score
-> downgraded to Stage 3-Yellow in live-lite mode

OpenDART disclosure + broker report
-> two independent evidence types
-> Stage 3-Green is allowed if deterministic rules also pass
```

This can be explicitly disabled with `require_cross_evidence_for_stage3_green=False`.

## Guardrails

- Live calls are optional.
- Fixture mode is the default.
- Missing live credentials do not crash the run.
- Missing credentials are recorded in the run log.
- OpenDART disclosure collection is date-based.
- The runner does not deep-search every listed company.
- Every skipped query and dropped search result is recorded.
- Hard-risk candidates are not escalated to Green.
- Point-in-time filtering remains based on `as_of_date` and `available_at`.
- Output remains rerating detection/monitoring context, not buy/sell wording.
