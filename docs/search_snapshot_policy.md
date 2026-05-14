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

## Why This Matters

Example:

```text
2026 search finds a 2023 broker PDF
```

That proves the PDF exists now.
It does not prove the agent could have found it in July 2023.

The snapshot store is how future daily live runs create a backtestable archive.
