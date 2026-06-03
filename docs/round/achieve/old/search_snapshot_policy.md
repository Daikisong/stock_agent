# Search Snapshot Policy

Historical blind discovery needs point-in-time search data.

If the agent searches the web today and finds an old report, that does not prove the report would have appeared in search results on the old replay date.

So future live runs should save snapshots.

## Search Snapshot Stores

Search snapshots store:

```text
query
search_date
result title
result URL
snippet
published_at if available
fetched_at
source_type
extracted_text_hash
evidence_ids
symbol if known
company_name if known
```

Code:

```text
src/e2r/research/search_snapshot_store.py
src/e2r/research/report_snapshot_store.py
```

## Historical Replay Rule

There are now two different replay meanings.

### Forward Archive Replay

If a snapshot exists:

```text
use it if search_date <= replay as_of_date
```

If a snapshot does not exist:

```text
mark search_snapshot_unavailable
```

Do not use modern search results as if they were historical.

Report snapshots store fetched text separately:

```text
url
title
symbol/company if known
fetched_at
as_of_date
source_type
extracted_text_path or hash
```

If no report snapshot exists:

```text
mark report_snapshot_unavailable
do not pretend a PDF was readable historically
```

This is strict future validation. It becomes powerful only after the live
agent has saved snapshots for a while.

### As-Of Research Replay

For the current 2023~2026 historical research backtest, use:

```text
asof_research_replay
```

That mode may search today's/local index for old public documents, but it must
accept only documents whose `published_at` or `report_date` is not after the
replay date.

Example:

```text
2026 search finds a report dated 2023-07-27
2023-08-01 replay accepts it

2026 search finds a report dated 2023-08-15
2023-08-01 replay rejects it
```

Undated documents are marked `date_unverified`; they cannot create Stage
3-Green alone.

## Why This Matters

Example:

```text
2026 search finds a 2023 broker PDF
```

That proves the PDF exists now.
It does not prove the agent could have found it in July 2023.

The snapshot store is how future daily live runs create a backtestable archive.
