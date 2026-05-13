# Checkpoint 15 Live Source Execution Report

## Scope

This checkpoint verifies the actual live execution path for Korea live-lite while keeping fixture mode as the default.

The important distinction is now visible in `run_log.json`:

```text
fixture
request_only
live_executed
fallback
```

Simple example:

```text
live_enabled=True + credentials present
-> OpenDART date-range request executes through HttpClient
-> source_modes.opendart = live_executed

live_enabled=True + credentials missing
-> fixture fallback
-> source_modes.opendart = fallback
```

## Added Components

- `src/e2r/sources/http_client.py`
  - `HttpClient`
  - `HttpClientStats`
  - `HttpResult`
  - JSON/text GET helpers
  - timeout and retry settings
  - optional cache read/write
  - clear non-throwing error results

- `src/e2r/pipeline/korea_live_lite.py`
  - OpenDART paginated live execution path
  - Naver Search live execution path
  - cache paths for raw JSON
  - source mode tracking
  - fallback reason tracking
  - request-only source tracking
  - API-key redaction in run log serialization

## OpenDART

OpenDART live execution is date-range based:

```text
list.json?bgn_de=YYYYMMDD&end_de=YYYYMMDD&page_no=N&page_count=100
```

It normalizes response rows into `DisclosureEvent`.

Raw JSON cache:

```text
data/cache/opendart/YYYY-MM-DD/
```

Tests mock a two-page OpenDART response and prove both symbols become disclosure evidence.

## Naver Search

Naver Search live execution uses the existing free search domains:

```text
news
web
doc
```

It normalizes JSON items into `SearchResult`, then the existing web research runner turns fetched text into parsed evidence.

Raw JSON cache:

```text
data/cache/naver/YYYY-MM-DD/
```

Tests mock a Naver response and prove it flows into news evidence.

## KRX/data.go.kr

KRX/data.go.kr remain explicit request-only sources in live-lite if credentials are present.

They are not silently treated as live.

Run log example:

```json
{
  "source_modes": {
    "krx": "request_only",
    "data_go_kr": "request_only"
  },
  "request_only_sources": ["krx", "data_go_kr"]
}
```

## Run Log Fields

Added:

```text
source_modes
live_requests_executed
live_requests_failed
cache_hits
cache_writes
fallback_reasons
request_only_sources
```

Sensitive values are redacted from serialized request metadata.

## Tests

Mocked HTTP tests prove:

- OpenDART paginated live response becomes `DisclosureEvent`
- Naver Search live response becomes evidence through the research runner
- valid live credentials set implemented sources to `live_executed`
- missing credentials use fallback mode without crashing
- KRX/data.go.kr are marked `request_only`
- API keys are not written to `run_log.json`
- existing budget tests still pass

No test performs a real network call.

## Guardrails

- Fixture mode remains the default.
- Live mode must be explicit.
- Tests use mocked HTTP.
- API keys are not logged.
- No paid data dependency was added.
- No aggressive scraping was added.
- Date-based OpenDART design is preserved.
- The system still produces rerating detection and monitoring output, not buy/sell wording.
