# Checkpoint 18 API Raw Probe And Schema Discovery

## Scope

This checkpoint adds a tiny raw-probe layer before running the full Korea live-lite flow.

The goal is:

```text
approved API endpoint
-> one tiny request
-> save raw response
-> profile schema
-> compare expected fields
-> dry-run normalizers
-> report parser/normalizer gaps
```

Simple example:

```text
data.go.kr stock-price response has clpr, mkp, hipr, lopr
-> schema profiler confirms expected fields
-> PriceBar dry-run succeeds
-> safe to use that response shape in tiny live-lite smoke
```

If the response instead uses different field names, the probe does not run E2R scoring. It writes the mismatch into the schema and normalizer reports.

## Added Components

- `src/e2r/probe/api_probe.py`
  - `APIProbeConfig`
  - `APIProbeRunner`
  - raw response storage
  - probe run log
  - normalizer dry-run

- `src/e2r/probe/schema_profiler.py`
  - top-level key detection
  - item/list path detection
  - field type inference
  - sample values
  - missing and unexpected field reporting
  - schema markdown rendering

- `src/e2r/probe/expected_fields.py`
  - expected field groups for OpenDART, Naver, data.go.kr, and KRX Open API
  - missing-field comparison

- `src/e2r/cli/probe_korea_apis.py`
  - command-line probe entry point

- `tests/test_api_probe.py`
  - mocked/fixture coverage for raw files, schema profiling, expected fields, normalizer dry-runs, CLI parsing, and secret redaction

## Approved APIs Covered

OpenDART:

```text
list.json disclosure search
```

Naver:

```text
news search
web search
doc/professional material search
```

data.go.kr:

```text
GetStockSecuritiesInfoService/getStockPriceInfo
GetKrxListedInfoService/getItemInfo
GetCorpBasicInfoService_V2/getCorpOutline_V2
GetFinaStatInfoService_V2/getSummFinaStat_V2
GetDiscInfoService_V2/getDiviDiscInfo_V2
```

KRX Open API:

```text
/svc/apis/sto/stk_bydd_trd
/svc/apis/sto/ksq_bydd_trd
/svc/apis/sto/stk_isu_base_info
/svc/apis/sto/ksq_isu_base_info
/svc/apis/idx/kospi_dd_trd
/svc/apis/idx/kosdaq_dd_trd
```

## Output

The runner writes:

```text
output/api_probe/YYYY-MM-DD/raw/*.json
output/api_probe/YYYY-MM-DD/schema_summary.json
output/api_probe/YYYY-MM-DD/schema_summary.md
output/api_probe/YYYY-MM-DD/normalizer_report.json
output/api_probe/YYYY-MM-DD/normalizer_report.md
output/api_probe/YYYY-MM-DD/probe_run_log.json
```

If a response is XML, it is stored as `.xml`; when possible, a parsed `.parsed.json` companion file is also written.

## Guardrails

- Fixture mode remains default.
- Live mode is explicit.
- Tests use mocked HTTP only.
- Probe requests are tiny and do not run deep research.
- Probe does not run cheap scan, Stage classification, or morning briefing.
- API keys are not written to output files.
- Failed normalizer dry-runs do not crash the probe.

## Tests

Tests prove:

- raw response files are stored
- schema profiler extracts top-level keys and item fields
- expected-field comparison detects missing fields
- unexpected fields are recorded for operator review
- stock-price normalizer dry-run succeeds for mocked response
- normalizer failures are reported without crashing
- probe run log does not contain API keys
- CLI argument parsing works
- missing credentials skip source probes instead of crashing
- existing tests pass
