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

Before the first live-lite smoke run, run the API raw probe:

```bash
PYTHONPATH=src python -m e2r.cli.probe_korea_apis --date YYYY-MM-DD --live --sample-symbol 005930
```

Inspect `docs/api_probe_runbook.md` for the expected review order. The probe checks raw response schemas and normalizer compatibility without running cheap scan, web research, or Stage classification.

## Source Modes

`run_log.json` separates source state explicitly:

```text
fixture
request_only
live_executed
fallback
disabled_optional
not_configured
```

Meaning:

- `fixture`: local CSV/JSON/TXT fixtures were used.
- `request_only`: request metadata was built, but live execution is not implemented or not enabled for that source.
- `live_executed`: a controlled HTTP request was executed or served from live cache.
- `fallback`: live mode was requested but the runner used fixture/fallback data because credentials were missing or the live request failed.
- `disabled_optional`: optional source is intentionally off.
- `not_configured`: optional source was enabled but is not wired for this run.

Simple example:

```json
{
  "source_modes": {
    "opendart": "live_executed",
    "krx": "request_only",
    "krx_openapi": "disabled_optional",
    "data_go_kr": "live_executed",
    "naver_search": "live_executed",
    "stock_issuance": "disabled_optional"
  }
}
```

OpenDART date-range disclosure search, Naver Search, and data.go.kr FSC listed-item/stock-price collection have live execution paths. data.go.kr is the primary live price/universe source. KRX Open API is optional backup/enrichment and stays disabled unless explicitly enabled.

`run_log.json` also records:

```text
live_requests_executed
live_requests_failed
cache_hits
cache_writes
rate_limit_waits
rate_limit_skips
actual_http_requests_by_source
logical_queries_by_source
max_concurrency_used_by_source
fallback_reasons
request_only_sources
```

API keys are not written into the run log.

`run_log.json` also includes `source_license_metadata`. This is an operator reminder, not legal advice. Verify each source's current terms before production or commercial use.

## Default Budgets

```text
max_opendart_calls_per_day = 1000
max_krx_calls_per_day = 500
max_data_go_kr_calls_per_day = 500
max_naver_search_calls_per_day = 2000
max_symbols_for_event_search = 200
max_symbols_for_deep_research = 30
```

## Rate Limits And Serial Live Execution

Live-lite starts with serial source calls.

Defaults:

```text
allow_parallel_live_requests = False
max_global_live_workers = 1
```

This is intentional. Early pilots should be easy to audit:

```text
request 1
-> rate-limit check
-> HTTP/cache result
-> run_log update
-> request 2
```

Source-level defaults are conservative:

```text
OpenDART:
  max_concurrency = 1
  min_interval_seconds = 0.2

Naver Search:
  max_concurrency = 1
  min_interval_seconds = 0.3

data.go.kr / KRX:
  max_concurrency = 1
  min_interval_seconds = 0.2
```

Daily request caps still come from `KoreaLiveLiteBudget`.

If the limiter has to wait, the run log shows:

```text
rate_limit_waits > 0
```

If the limiter blocks a request before network execution:

```text
rate_limit_skips > 0
```

Check source-level activity:

```text
actual_http_requests_by_source
logical_queries_by_source
max_concurrency_used_by_source
```

Example:

```text
logical_queries_by_source.naver_search = 25
actual_http_requests_by_source.naver_search = 75
```

This can happen because one logical search query may call multiple Naver search domains.

## Live Smoke Presets

Use smoke presets before broader live pilots.

```python
from datetime import date
from e2r.pipeline.korea_live_lite import KoreaLiveLiteConfig

config = KoreaLiveLiteConfig.smoke_preset("tiny", as_of_date=date.today())
```

Preset sizes:

```text
tiny:
  universe_limit = 50
  naver queries = 50
  event_search symbols = 5
  deep_research symbols = 1

small:
  universe_limit = 300
  naver queries = 300
  event_search symbols = 30
  deep_research symbols = 5

standard_shadow:
  universe_limit = all fixture/live universe
  naver queries = 2000
  event_search symbols = 200
  deep_research symbols = 30
```

Presets do not turn on live mode by themselves. To run live-lite explicitly:

```python
config = KoreaLiveLiteConfig.smoke_preset(
    "tiny",
    as_of_date=date.today(),
    fixture_mode=False,
    live_enabled=True,
)
```

Start with `tiny`, inspect `run_log.json`, then move to `small`.

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

1. Load the Korea universe from KRX/data.go.kr fixture or live-backed connectors.
2. Pull price bars under the KRX/data.go.kr call budget.
3. Pull same-day/prior-day OpenDART disclosures by date range, not symbol-by-symbol.
4. Run `KoreaCheapScanner`.
5. Select only `event_search` and `deep_research` candidates.
6. Run `FreeWebResearchRunner` under Naver/search query budgets.
7. Generate a Korean morning brief.
8. Write JSON and Markdown outputs.

## data.go.kr Price And Universe Live Execution

When `fixture_mode=False`, `live_enabled=True`, and `DATA_GO_KR_SERVICE_KEY` is present, the runner can execute the free Financial Services Commission data.go.kr path for:

```text
listed items -> Instrument
stock prices -> PriceBar
```

It uses bulk/date/page requests instead of one request per symbol.

Good:

```text
call listed item page 1
call stock price page 1 for the date window
normalize rows locally by symbol
```

Bad:

```text
for each listed company:
    call daily stock price API
```

The first safe live path currently uses:

```text
GetKrxListedInfoService/getItemInfo
GetStockSecuritiesInfoService/getStockPriceInfo
```

Raw JSON is cached under:

```text
data/cache/data_go_kr/YYYY-MM-DD/
```

If the data.go.kr call fails, the run log records:

```text
source_modes.data_go_kr = fallback
fallback_reasons.data_go_kr = data_go_kr_listed_items_failed
```

If the daily data.go.kr budget is too small to fetch both universe and price data, the runner falls back before making the calls. For example, `max_data_go_kr_calls_per_day=1` is too small because the pilot needs at least one listed-item page and one stock-price page.

KRX MDC-style metadata remains explicit request-only for now:

```text
source_modes.krx = request_only
```

KRX Open API is tracked separately:

```text
source_modes.krx_openapi = disabled_optional
```

If `enable_krx_openapi_source=True` and `KRX_OPENAPI_KEY` is present, the current pilot records:

```text
source_modes.krx_openapi = request_only
```

This means approved `data-dbg.krx.co.kr` request builders exist, but KRX Open API is not yet the default live executor. Use `source_modes` in `run_log.json` before interpreting the brief.

Approved KRX Open API request paths:

```text
/svc/apis/sto/stk_bydd_trd
/svc/apis/sto/ksq_bydd_trd
/svc/apis/sto/stk_isu_base_info
/svc/apis/sto/ksq_isu_base_info
/svc/apis/idx/kospi_dd_trd
/svc/apis/idx/kosdaq_dd_trd
```

Approved data.go.kr FSC request paths:

```text
GetStockSecuritiesInfoService/getStockPriceInfo
GetKrxListedInfoService/getItemInfo
GetFinaStatInfoService_V2/getSummFinaStat_V2
GetDiscInfoService_V2/getDiviDiscInfo_V2
GetCorpBasicInfoService_V2/getCorpOutline_V2
```

`GetCorpBasicInfoService_V2` is optional and used only as a company metadata fallback.

## Optional Stock Issuance Source

`금융위원회_주식발행정보` is optional and disabled by default.

Config:

```python
KoreaLiveLiteConfig(
    as_of_date=date.today(),
    enable_stock_issuance_source=False,
)
```

Default run log:

```text
source_modes.stock_issuance = disabled_optional
```

Why this is optional:

```text
OpenDART 유상증자 / 전환사채 / 신주인수권부사채
금융위원회_공시정보
Naver Search risk queries
```

are the primary dilution-risk sensors. The stock issuance API can be useful, but it is not required for E2R scoring.

Use it only if the API-specific public-data license allows the intended use.

Simple example:

```text
If 주식발행정보 is attribution + non-commercial only:
-> keep enable_stock_issuance_source=False
-> production run still detects dilution risk from OpenDART and risk searches
```

Fallback Red Team search queries include:

```text
{company} 유상증자
{company} 전환사채
{company} 신주인수권부사채
{company} 보호예수 해제
{company} 오버행
{company} CB 리픽싱
```

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
parser audit findings
planned OpenDART detail fetches
run notes
```

Use `source_modes` before reading the brief. For example:

```text
source_modes.opendart = fixture
-> the brief came from fallback data, not actual OpenDART live data.

source_modes.opendart = live_executed
-> OpenDART date-range collection actually ran through the HTTP executor or cache.
```

## Reviewing A Run

After every fixture or live-lite run, review the output bundle before reading the brief as a decision artifact.

Run:

```bash
PYTHONPATH=src python -m e2r.cli.review_korea_run 2024-05-21 --output-directory output
```

The review command reads:

```text
output/korea_live_lite/2024-05-21_candidates.json
output/korea_live_lite/2024-05-21_evidence.json
output/korea_live_lite/2024-05-21_brief.md
output/korea_live_lite/2024-05-21_run_log.json
```

It summarizes:

```text
total candidates
event_search and deep_research counts
Stage distribution if the brief contains stages
source_modes
live_requests_executed / failed
cache_hits / writes
missing credentials
top skipped and dropped reasons
low-confidence evidence
manual-review items
```

Simple example:

```text
source_modes.data_go_kr = live_executed
source_modes.opendart = fallback
manual review required = parser-audit:333333:...
```

This means the price/universe data came through the live executor, but disclosure evidence came from fallback data and at least one parsed item needs manual review.

## Parser Audit Findings

The runner audits parsed evidence before writing the final run log.

Audit findings are written to:

```text
run_log.audit_findings
```

Important checks include:

```text
contract_amount_to_prior_sales > 5.0
contract_duration_months > 120
opm > 80
est_per < 1 or est_per > 300
est_pbr < 0.1 or est_pbr > 50
target_revision_pct > 300
fifty_two_week_low > current_price
parser_confidence < 0.5
contract_quality score exists but contract amount/duration is missing
Stage 3-Green supported only by low-confidence evidence
```

Severity:

```text
info
warning
hard
```

Suggested action:

```text
allow
downgrade_to_yellow
manual_review
block_green
```

Trust Stage 3-Green only when all of these are true:

```text
source modes are understood
no hard audit finding exists for the symbol
evidence is available as of the run date
at least two independent evidence types support Green in live-lite mode
parser confidence is not low
```

Manual review is required when:

```text
run_log.notes contains manual_review_required
run_log.audit_findings has warning or hard findings
source_modes show fallback for a critical source
planned OpenDART detail fetches include a key disclosure that has not been parsed in detail yet
```

Example:

```text
계약 매출액 대비 600%
-> audit finding: contract_ratio_too_high
-> affected Stage 3-Green is blocked to Stage 3-Yellow
-> manually open the OpenDART detail document before trusting the case
```

## OpenDART Detail Fetch Planning

The runner plans detail fetches for high-value disclosure list rows, but does not execute them yet.

Watch disclosure types:

```text
단일판매·공급계약체결
신규시설투자
잠정실적
영업실적 전망
유상증자
전환사채
감사의견
거래정지
```

Planned metadata appears in:

```text
run_log.planned_opendart_detail_requests
```

Example:

```text
list.json row: 단일판매·공급계약체결 / rcept_no=202405210001
-> planned document.xml request is recorded
-> no network call is made in this checkpoint
```

## OpenDART Date-Based Collection

The runner intentionally avoids:

```text
2,500 listed companies * 1 disclosure search each
```

Bad:

```text
for each listed company:
    call OpenDART list.json
```

Good:

```text
call OpenDART list.json by bgn_de/end_de with pagination
group disclosures by stock_code/corp_code
scanner filters by symbol in memory
```

Instead:

```text
OpenDART list.json with bgn_de/end_de
-> all disclosures for the date window
-> local symbol filtering
```

This is the main reason live-lite can be operated safely before a full production scheduler exists.

OpenDART live execution uses paginated request metadata:

```text
bgn_de
end_de
page_no
page_count
```

Raw JSON is cached under:

```text
data/cache/opendart/YYYY-MM-DD/
```

Tests use mocked HTTP responses, not real network calls.

## Naver Search Live Execution

Naver Search live mode is explicit and credential-gated.

Required:

```text
NAVER_CLIENT_ID
NAVER_CLIENT_SECRET
```

The runner executes only budgeted candidate queries, not all-listed deep search. Raw JSON is cached under:

```text
data/cache/naver/YYYY-MM-DD/
```

The search result then flows through the existing ranking/fetch/parsing path:

```text
Naver Search JSON
-> SearchResult
-> fixture/manual text or fetchable text
-> NewsItem/ResearchReport/DisclosureEvent
-> Evidence
```

## Tiny Live Pilot

Start with a small live pilot:

```python
from datetime import date
from e2r.pipeline.korea_live_lite import KoreaLiveLiteBudget, KoreaLiveLiteConfig, KoreaLiveLiteRunner

result = KoreaLiveLiteRunner().run(
    KoreaLiveLiteConfig(
        as_of_date=date.today(),
        fixture_mode=False,
        live_enabled=True,
        universe_limit=100,
        budget=KoreaLiveLiteBudget(
            max_opendart_calls_per_day=20,
            max_krx_calls_per_day=100,
            max_data_go_kr_calls_per_day=100,
            max_naver_search_calls_per_day=30,
            max_symbols_for_event_search=10,
            max_symbols_for_deep_research=3,
        ),
    )
)

print(result.run_log_path)
```

Then inspect:

```text
missing_credentials
source_modes
live_requests_executed
fallback_reasons
request_only_sources
skipped_queries
dropped_search_results
```

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

## OpenDART List vs Detail

OpenDART `list.json` is a headline feed. It is good for discovering that something happened, but it usually does not contain the detailed numbers E2R needs.

Simple example:

```text
list.json title: 단일판매·공급계약체결
-> candidate can enter event_search
-> not enough for Stage 3-Green

document.xml detail:
계약금액, 매출액 대비, 계약기간, 상대방
-> stronger Evidence if fields are explicitly parsed
```

Detail fetch is capped by preset:

```text
tiny = 3
small = 10
standard_shadow = 50
```

Only watch disclosures are fetched. Routine rows such as repetitive prospectus filings or administrative corrections do not trigger detail fetch and do not count as independent Green evidence.

## Cheap-Scan Calibration Report

Each run writes:

```text
output/korea_live_lite/YYYY-MM-DD_cheap_scan_calibration.json
output/korea_live_lite/YYYY-MM-DD_cheap_scan_calibration.md
```

Use it when a run produces zero candidates.

Example interpretation:

```text
near_miss_top_50 has many price signals
-> price threshold may be too strict, or disclosures are missing

top_high_signal_disclosures is empty
-> OpenDART date window may be too narrow, or today had no official events

instruments_missing_price_bars is high
-> universe/price source join needs review
```

Do not lower thresholds just because one day has zero candidates. The report is for diagnosis first.

## Report Radar

Report Radar is an optional lightweight search path for high-signal E2R phrases:

```text
목표주가 상향 EPS 상향 PDF
컨센서스 상회 Review PDF
수주잔고 OPM 수출 비중 PDF
장기공급계약 매출액 대비 PDF
ASP 상승 판가 상승 리드타임 PDF
```

It is not a full-market deep search. It uses a capped universe slice, active watchlist symbols, and `SearchBudget`.

Report Radar candidates are marked:

```text
candidate_source_path = report_radar
```

They can route to event search or deep research, but they still need normal parsed evidence before any Stage 3-Green classification.

## Targeted Smoke

Targeted smoke is a pipeline test for Naver/search escalation.

It is marked:

```text
test_injected = True
candidate_source_path = targeted_smoke
production_candidate = False
```

It is excluded from production candidate JSON and the real morning brief. If the search returns no real document, the run log records `insufficient_evidence`.

Simple example:

```text
targeted_smoke_company = "테스트회사"
search returns nothing
-> no Stage 3-Green
-> only run_log.targeted_smoke_results records the pipeline test
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
