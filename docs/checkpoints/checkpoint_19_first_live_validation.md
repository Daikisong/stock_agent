# Checkpoint 19 First Live Validation

## Date

2026-05-14

## Commands Run

Preflight:

```bash
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
git diff --check
```

API probe:

```bash
PYTHONPATH=src python -m e2r.cli.probe_korea_apis \
  --date 2026-05-14 \
  --fixture \
  --output-directory output/api_probe \
  --sample-symbol 005930 \
  --sample-company 삼성전자 \
  --sample-query "삼성전자 수주잔고" \
  --max-requests-per-source 3

PYTHONPATH=src python -m e2r.cli.probe_korea_apis \
  --date 2026-05-14 \
  --live \
  --no-cache \
  --output-directory output/api_probe \
  --sample-symbol 005930 \
  --sample-company 삼성전자 \
  --sample-query "삼성전자 수주잔고" \
  --max-requests-per-source 3
```

Live-lite:

```bash
PYTHONPATH=src python -m e2r.cli.review_korea_run 2026-05-14 --output-directory output
```

Tiny and small smoke presets were run through `KoreaLiveLiteConfig.smoke_preset(...)`.

## API Probe Result

The live raw probe passed.

```text
requests_attempted: 15
requests_succeeded: 15
requests_failed: 0
secret_leaks: 0
```

Live-executed probe sources:

```text
OpenDART list.json
Naver news / web / doc
data.go.kr listed items / stock prices / corp basic / financial stat / disclosure info
KRX Open API approved endpoints
```

The only probe warning was `naver_doc` returning zero rows for the sample query. That is not a hard failure because Naver news and web normalized successfully.

## Normalizer Result

Successful dry-runs:

```text
OpenDART list -> DisclosureEvent: 10 / 10
Naver news -> SearchResult: 3 / 3
Naver web -> SearchResult: 3 / 3
data.go.kr listed items -> Instrument: 10 / 10
data.go.kr stock prices -> PriceBar: 10 / 10
data.go.kr corp basic -> Instrument-like metadata: 10 / 10
data.go.kr financial stat -> FinancialActual: 10 / 10
data.go.kr disclosure info -> DisclosureEvent: 10 / 10
KRX daily trading -> PriceBar: 948 / 948 and 1821 / 1821
KRX issue base info -> Instrument: 948 / 948 and 1821 / 1821
KRX index daily -> PriceBar: 50 / 51 and 39 / 40
```

The KRX index dry-run skipped one unpriced aggregate row per index response. There were no normalizer failures after the patch.

## Schema Mismatches Fixed

- data.go.kr V2 operation names were aligned to the live-approved endpoints:
  - `GetCorpBasicInfoService_V2/getCorpOutline_V2`
  - `GetFinaStatInfoService_V2/getSummFinaStat_V2`
  - `GetDiscInfoService_V2/getDiviDiscInfo_V2`
- KRX/data.go.kr market-data probes now use a settled prior date because same-day official files can be empty before publication.
- `PriceBar` normalization now tolerates zero or missing open/high/low by falling back to valid close-derived values instead of accepting invalid zero prices.
- KRX issue-base schema accepts `MKT_TP_NM` as the market-name field.
- KRX index schema accepts `CLSPRC_IDX`, `OPNPRC_IDX`, `HGPRC_IDX`, and `LWPRC_IDX`.
- Failed probe responses now overwrite stale raw files with redacted failure metadata.
- The run-review CLI now limits low-confidence evidence output to keep terminal review readable.

## Fixture Live-Lite

Fixture live-lite passed.

```text
total candidates: 2
event_search: 1
deep_research: 0
source modes: fixture for KRX/data.go.kr/OpenDART/Naver
secret_leaks: 0
```

## Tiny Live Smoke

Tiny live smoke completed without HTTP failures.

```text
source_modes:
  data_go_kr: live_executed
  opendart: live_executed
  krx: request_only
  krx_openapi: disabled_optional
  naver_search: request_only
  stock_issuance: disabled_optional

live_requests_executed: 517
live_requests_failed: 0
actual_http_requests_by_source:
  data_go_kr: 501
  opendart: 17
rate_limit_skips: 0
max_concurrency_used_by_source:
  data_go_kr: 1
  opendart: 1
candidates: 0
evidence: 1687
hard_audit_findings: 0
secret_leaks: 0
```

Tiny produced no E2R candidates in the first 50-symbol scan window. This is acceptable as a safety pass, but it also means Naver live search was not exercised by the full live-lite flow. Naver was exercised successfully in the raw probe.

## Small Live Pilot

Small was run only after tiny completed.

```text
source_modes:
  data_go_kr: live_executed
  opendart: live_executed
  krx: request_only
  krx_openapi: disabled_optional
  naver_search: request_only
  stock_issuance: disabled_optional

live_requests_executed: 0
cache_hits: 517
live_requests_failed: 0
rate_limit_skips: 0
candidates: 0
evidence: 1687
hard_audit_findings: 0
secret_leaks: 0
```

Small reused the tiny cache and did not issue additional live HTTP requests. It also produced no E2R candidates.

## Standard Shadow

`standard_shadow` was not run.

Reason:

```text
tiny and small both proved API execution and caching, but produced zero cheap-scan candidates.
Running the broader shadow pass now would mostly test scale, not candidate quality.
```

The safer next step is to reduce OpenDART list-noise, add detail fetch execution for watch disclosures, and calibrate cheap-scan live universe/price handling before a full shadow run.

## Remaining Risks

- OpenDART `list.json` is useful for event discovery, but it does not contain detailed contract amount, duration, CAPA, RPO, or prepayment fields. The current audit correctly marks these list-derived evidence rows as low confidence.
- The live-lite review found 1686 low-confidence audit findings from OpenDART list evidence. They are not hard blockers, but they show that detail fetch and parser confidence filtering are needed before daily operation.
- Tiny required 517 live calls because price/universe collection still pulls broad data.go.kr pages before candidate filtering. This is safe under the current budget but too heavy for a "tiny" operator experience.
- Naver live search was validated by raw probe, but not by live-lite smoke because no cheap-scan candidates escalated to web research.
- KRX Open API raw probe works, but live-lite still uses data.go.kr as the primary price/universe executor unless KRX Open API execution is explicitly enabled later.

## Next Recommended Patches

1. Add OpenDART detail execution for planned watch disclosures, with strict cap and cache.
2. Filter OpenDART list evidence so routine fund filings and low-signal reports do not flood parser audit.
3. Add a live-lite price collection mode that limits tiny/small to a settled-date range and/or selected universe while preserving point-in-time rules.
4. Calibrate cheap-scan live candidate rules so date disclosures and price signals can produce candidates beyond fixture-only examples.
5. Run a targeted live-lite case for a known same-day disclosure symbol to exercise Naver search escalation.
