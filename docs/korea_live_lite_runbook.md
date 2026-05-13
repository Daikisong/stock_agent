# Korea Live-Lite Runbook

## Purpose

Korea live-lite mode is the controlled pilot between fixture-only research and a full live data system.

It uses free sources with strict budgets:

```text
official/free source scan
-> cheap candidates
-> targeted web research
-> morning brief
```

It is not designed to deep-search every KOSPI/KOSDAQ company.

## Fixture Mode

Fixture mode is the default and requires no credentials.

Example:

```python
from datetime import date
from e2r.pipeline.korea_live_lite import KoreaLiveLiteConfig, KoreaLiveLiteRunner

result = KoreaLiveLiteRunner().run(
    KoreaLiveLiteConfig(as_of_date=date(2024, 5, 21))
)
```

The default fixture sources point to:

```text
data/raw/korea_cheap_scan/
```

This is useful for local development and CI because no network call is made.

## Live-Lite Mode

Live-lite mode can be enabled explicitly:

```python
result = KoreaLiveLiteRunner().run(
    KoreaLiveLiteConfig(
        as_of_date=date.today(),
        fixture_mode=False,
        live_enabled=True,
    )
)
```

Required environment variables for live mode:

```text
OPENDART_API_KEY
KRX_OPENAPI_KEY or DATA_GO_KR_SERVICE_KEY
NAVER_CLIENT_ID
NAVER_CLIENT_SECRET
```

If credentials are missing, the runner falls back to fixture mode and records the missing names in:

```text
output/korea_live_lite/YYYY-MM-DD_run_log.json
```

## Default Budgets

```text
max_opendart_calls_per_day = 1000
max_krx_calls_per_day = 500
max_data_go_kr_calls_per_day = 500
max_naver_search_calls_per_day = 2000
max_symbols_for_event_search = 200
max_symbols_for_deep_research = 30
```

Example with a smaller pilot:

```python
from e2r.pipeline.korea_live_lite import KoreaLiveLiteBudget, KoreaLiveLiteConfig

config = KoreaLiveLiteConfig(
    as_of_date=date.today(),
    budget=KoreaLiveLiteBudget(
        max_opendart_calls_per_day=100,
        max_krx_calls_per_day=100,
        max_data_go_kr_calls_per_day=100,
        max_naver_search_calls_per_day=300,
        max_symbols_for_event_search=30,
        max_symbols_for_deep_research=5,
    ),
)
```

## Pipeline Steps

1. Load the Korea universe from KRX/data.go.kr fixture or request-backed connectors.
2. Pull price bars under the KRX/data.go.kr call budget.
3. Pull same-day/prior-day OpenDART disclosures by date range, not symbol-by-symbol.
4. Run `KoreaCheapScanner`.
5. Select only `event_search` and `deep_research` candidates.
6. Run `FreeWebResearchRunner` under Naver/search query budgets.
7. Generate a Korean morning brief.
8. Write JSON and Markdown outputs.

## Output Files

For `YYYY-MM-DD`, live-lite writes:

```text
output/korea_live_lite/YYYY-MM-DD_candidates.json
output/korea_live_lite/YYYY-MM-DD_evidence.json
output/korea_live_lite/YYYY-MM-DD_brief.md
output/korea_live_lite/YYYY-MM-DD_run_log.json
```

`candidates.json` contains cheap-scan candidates:

```text
symbol, company_name, reason_codes, scores, recommended_next_layer
```

`evidence.json` contains parsed evidence records visible as of the run date.

`brief.md` contains the Korean monitoring brief.

`run_log.json` contains:

```text
missing credentials
source call counts
built request metadata
skipped candidates
skipped queries and reasons
dropped search results and reasons
run notes
```

## OpenDART Date-Based Collection

The runner intentionally avoids:

```text
2,500 listed companies * 1 disclosure search each
```

Instead:

```text
OpenDART list.json with bgn_de/end_de
-> all disclosures for the date window
-> local symbol filtering
```

This is the main reason live-lite can be operated safely before a full production scheduler exists.

## Search Escalation

Reason codes become targeted queries.

Example:

```text
DISC_SUPPLY_CONTRACT
-> {company} 장기공급계약 매출액 대비
-> {company} 단일판매 공급계약 계약기간
-> {company} 수주잔고
```

Risk-only candidates are not escalated.

Example:

```text
거래정지 + 관리종목
-> recommended_next_layer = none
-> web research skipped
```

## Stage 3-Green Evidence Rule

Live-lite mode requires at least two independent evidence types for Stage 3-Green unless explicitly disabled.

Counts as independent evidence types:

```text
disclosure
research_report
news
financial_actual
consensus
consensus_revision
```

Simple example:

```text
broker report only
-> can be Stage 3-Yellow

OpenDART disclosure + broker report
-> can be Stage 3-Green if deterministic scoring also passes
```

Disable only for controlled experiments:

```python
KoreaLiveLiteConfig(
    as_of_date=date.today(),
    require_cross_evidence_for_stage3_green=False,
)
```

## Safety Rules

Do:

- keep fixture mode as the default
- set small budgets for first live pilots
- review `run_log.json` after every run
- stop on CAPTCHA/blocking signals
- preserve `as_of_date`

Do not:

- deep-search every listed company
- scrape aggressively
- store API keys in code or output files
- invent missing contract fields
- use future data
- output buy/sell recommendation wording

## What Still Requires Paid Or Manual Data

Free live-lite mode does not replace:

- full licensed consensus history
- broker database coverage metadata
- complete analyst revision time series
- paid normalized financial databases
- proprietary sector aggregates

The intended use is early detection and monitoring:

```text
free official event
-> cheap candidate
-> targeted web research
-> evidence-backed E2R stage monitoring
```
