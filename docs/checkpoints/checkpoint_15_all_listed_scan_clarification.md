# Checkpoint 15 Report

## Scope

Checkpoint 15 clarifies and hardens the Korea cheap-scan architecture around:

```text
all-listed scan
vs.
per-symbol OpenDART API calls
```

The correct design is:

```text
load every KOSPI/KOSDAQ instrument
collect OpenDART disclosures once by date range with pagination
group/filter disclosures locally by symbol
evaluate every instrument with price, financial, risk, and event rules
```

## Important Distinction

All-listed scan means every listed instrument is evaluated.

It does not mean:

```text
for each listed company:
    call OpenDART list.json
```

That pattern would turn 2,500 listed companies into 2,500 OpenDART disclosure calls before any real research starts.

## Date-Based OpenDART Collection

The live-lite runner now exposes:

```text
build_opendart_date_range_requests(start, end, as_of_date, page_count=100, max_pages=None)
```

It builds `SourceRequest` metadata with:

```text
page_no
page_count
bgn_de
end_de
```

Tests do not call the network. The helper is a pagination-ready request builder.

## Scanner Behavior

`_DateBasedOpenDARTConnector` keeps the scanner interface unchanged.

When `KoreaCheapScanner` asks for disclosures for one symbol, the connector filters the preloaded date-range disclosure set in memory.

Simple example:

```text
OpenDART date range returns disclosures for 111111, 222222, 333333
scanner evaluates 444444 too
444444 has no disclosure, but price/volume sensors can still produce a candidate
```

## Tests Added

Tests prove:

- a no-disclosure instrument with price/volume spike is still evaluated
- a no-disclosure instrument can become `event_search` through financial rules
- date-based disclosure collection includes multiple symbols
- per-symbol scanner disclosure lookup does not increment `opendart_symbol_disclosure_calls`
- the OpenDART page request builder emits `page_no` and `page_count`

## Guardrails

- No live API call is required in tests.
- No paid data dependency was added.
- Date-based OpenDART design is preserved.
- Symbols without disclosures still participate in Layer 1.
- Per-symbol OpenDART calls remain reserved for deep research or active watchlist details.
- No buy/sell recommendation wording is introduced.
