# Checkpoint 24: True E2R_STANDARD Blind Replay

## What Changed

Blind replay no longer uses `HistoricalUniverseReplay(mode=hybrid)` as the default candidate generator.

Default path now:

```text
historical point-in-time source adapter
-> E2R_STANDARD
-> discovered candidates
-> benchmark labels loaded afterward
-> recall / false-positive / coverage reports
```

Diagnostic fixture proxy still exists, but only when explicitly requested:

```text
--allow-fixture-source-proxy
```

That report is labeled:

```text
fixture proxy mode; not proof of live discovery
```

## Files Added

```text
src/e2r/backtest/historical_source_adapter.py
src/e2r/backtest/e2r_standard_replay.py
tests/test_historical_source_adapter.py
tests/test_benchmark_leakage.py
data/search_snapshots/search_snapshots.jsonl
data/report_snapshots/report_snapshots.jsonl
data/report_snapshots/*.txt
```

## Files Updated

```text
src/e2r/backtest/blind_discovery_replay.py
src/e2r/cli/run_blind_discovery_replay.py
src/e2r/research/search_snapshot_store.py
src/e2r/research/report_snapshot_store.py
src/e2r/backtest/stage_lifecycle_detector.py
docs/e2r_standard_flow.md
docs/blind_discovery_replay_runbook.md
docs/flow_mode_glossary.md
docs/search_snapshot_policy.md
docs/monthly_replay_report_runbook.md
```

## Verification

Commands run:

```bash
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
git diff --check
```

Result:

```text
209 tests passed
diff check passed
```

Blind replay sanity run:

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

No-proxy result:

```text
true_standard_flow_used: yes
fixture_proxy_used: no
benchmark_labels_used_before_candidate_generation: no
discovered_candidates: 135
benchmark_labels_appeared: 3/13
unsafe_warning_green_count: 0
Stage 3-Green count: 0
```

No-proxy benchmark labels that appeared:

```text
HD현대일렉트릭
효성중공업
삼양식품
```

Explicit fixture-proxy diagnostic run:

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

Fixture-proxy result:

```text
true_standard_flow_used: no
fixture_proxy_used: yes
benchmark_labels_used_before_candidate_generation: no
discovered_candidates: 234
benchmark_labels_appeared: 7/13
unsafe_warning_green_count: 0
Stage 3-Green count: 101
```

Fixture-proxy benchmark labels that appeared:

```text
HD현대일렉트릭
효성중공업
일진전기
산일전기
삼양식품
한화에어로스페이스
대한전선-like
```

Interpretation:

```text
fixture-proxy success is regression success, not proof of live discovery
```

## Benchmark Label Separation

Benchmark labels are loaded only after candidate generation.

Added leakage tests prove:

```text
E2RStandardFlow does not import benchmark labels
cheap_scan does not import benchmark labels
features/staging/red_team do not import benchmark labels
research modules do not import benchmark labels
LLM prompts do not include benchmark labels
fake Green label without evidence does not become a candidate
```

Example:

```text
label says "가짜그린 should be Green"
no search/report/official evidence exists
-> no candidate
-> label appears only in missed_benchmark_labels
```

## Source Snapshot Behavior

Search snapshots now support:

```text
save_snapshot
load_snapshots(query, symbol, company_name, as_of_date)
SearchResult conversion
point-in-time filter: search_date <= replay_date
```

Report snapshots now support:

```text
save_snapshot
load_snapshots(symbol, company_name, as_of_date)
fixture_text_by_url
point-in-time filter: as_of_date <= replay_date
```

Minimal historical source snapshots were added for:

```text
HD현대일렉트릭
효성중공업
삼양식품
씨젠
```

These are evidence snapshots, not benchmark labels.

## 4A/4B/4C Safety

The lifecycle detector now returns:

```text
unknown_insufficient_evidence
```

when there is no price, slowdown, backlog, margin, crowding, or thesis-break evidence.

Price-only overheat remains:

```text
price_only_4b_watch
```

and is not promoted to full 4B.

## Remaining Limitations

The no-proxy replay is still limited by historical source coverage:

```text
price_unavailable
disclosure_unavailable
financial_unavailable
```

The current snapshot fixtures are small. Therefore:

```text
HD현대일렉트릭 / 효성중공업 / 삼양식품 appear from stored snapshots
many labels remain missed because no historical source snapshot exists
Stage 3-Green is not forced
```

## Next Recommended Action

Before a real large-scale blind backtest:

```text
1. Store daily search snapshots from live E2R_STANDARD runs.
2. Add historical official source archives: prices, disclosures, financial actuals.
3. Add report/news snapshots for missed known winners.
4. Rerun no-fixture-proxy blind replay.
5. Only then evaluate weekly/daily large backtest readiness.
```
