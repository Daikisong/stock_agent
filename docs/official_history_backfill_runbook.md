# Official History Backfill Runbook

The as-of replay must start from official historical data, not from search or
report snapshots.

Backfill target:

```text
data/historical_official/universe/
data/historical_official/prices/
data/historical_official/disclosures/
data/historical_official/financials/
data/historical_official/risks/
```

## Command

```bash
PYTHONPATH=src python -m e2r.cli.backfill_official_history \
  --start-date 2023-01-01 \
  --end-date 2026-05-14 \
  --market KR \
  --output-directory data/historical_official \
  --max-opendart-detail-fetches-per-day 50
```

Current checkpoint behavior:

```text
creates directory structure
writes backfill_plan.json
does not execute network in tests/default path
does not use benchmark labels
does not use search snapshots to define universe
```

Future live executor should fill:

```text
KRX/data.go.kr listed universe
KRX/data.go.kr price ranges
OpenDART date-range disclosure lists
OpenDART detail XML for watch disclosures
data.go.kr financial actuals if available
```

Example:

```text
Good:
load KOSPI/KOSDAQ universe from official historical files

Bad:
build universe from old broker report snapshots
```
