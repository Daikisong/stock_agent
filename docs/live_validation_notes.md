# Live Validation Notes

## 2026-05-14 First Korea Live Validation

### What Worked

- API keys were present when loaded from `.env`; key values were never printed.
- Fixture API probe completed.
- Live API raw probe completed with 15 successful requests and 0 failures.
- Raw API responses were saved under `output/api_probe/2026-05-14/raw/`.
- Schema and normalizer reports were created.
- No API key values were found in `output/` or `data/cache/`.
- Tiny live smoke completed with serial execution and no HTTP failures.
- Small live pilot completed from cache with no additional HTTP requests.

Simple example:

```text
data.go.kr stock price row
-> clpr/mkp/hipr/lopr/trqu/trPrc parsed
-> PriceBar dry-run succeeds
-> live-lite can safely use that row shape
```

### Source Mode Summary

API probe:

```text
opendart_list: live_executed
naver_news/web/doc: live_executed
data_go_kr listed/prices/basic/financial/disclosure: live_executed
KRX approved endpoints: live_executed
```

Tiny and small live-lite:

```text
data_go_kr: live_executed
opendart: live_executed
krx: request_only
krx_openapi: disabled_optional
naver_search: request_only
stock_issuance: disabled_optional
```

Naver is `request_only` in live-lite because no cheap-scan candidates were produced, so the runner never escalated to web search. Naver itself was verified in the raw probe.

### Patches Applied During Validation

- Corrected approved data.go.kr V2 operation paths:
  - `getCorpOutline_V2`
  - `getSummFinaStat_V2`
  - `getDiviDiscInfo_V2`
- Used prior-date market probes for KRX/data.go.kr because same-day files can be empty.
- Added data.go.kr financial-stat dry-run normalization.
- Added KRX field aliases for actual live response names.
- Made price normalization tolerate zero open/high/low fields by falling back to valid close-derived values.
- Limited review CLI output so thousands of low-confidence rows do not flood the terminal.
- Added `output/` and `data/cache/` to `.gitignore`.

### Results

Tiny:

```text
live_requests_executed: 517
live_requests_failed: 0
candidates: 0
evidence: 1687
hard_audit_findings: 0
rate_limit_skips: 0
max_concurrency: 1
```

Small:

```text
live_requests_executed: 0
cache_hits: 517
live_requests_failed: 0
candidates: 0
evidence: 1687
hard_audit_findings: 0
rate_limit_skips: 0
```

### Interpretation

The live data path works, but this is not ready for unattended daily operation yet.

The main issue is not API access. The issue is evidence quality and candidate calibration:

```text
OpenDART list gives many disclosure headlines
-> list rows become low-confidence evidence
-> parser audit correctly demands manual review
-> no Stage 3 candidate should be trusted from list-only evidence
```

This is the right conservative behavior.

### Standard Shadow Decision

`standard_shadow` was not run.

It is technically safer after the successful probe/tiny/small cycle, but it is not yet useful enough because:

```text
tiny candidates: 0
small candidates: 0
OpenDART list audit noise: high
Naver live-lite escalation: not exercised
```

Run standard shadow after detail fetch and cheap-scan calibration are patched.

### Next

1. Execute OpenDART detail fetches only for watch disclosures.
2. Drop or down-rank routine fund/security issuance filings from cheap-scan evidence unless they are risk-relevant.
3. Add a tiny/small price fetch mode that is genuinely small.
4. Add a targeted same-day disclosure smoke test that forces one candidate into Naver search.
5. Re-run tiny and small, then consider standard shadow.
