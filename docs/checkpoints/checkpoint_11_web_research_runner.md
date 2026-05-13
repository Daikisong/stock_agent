# Checkpoint 11 Report

## Scope

Checkpoint 11 adds a fixture-first web research runner that reproduces the manual research workflow from the E2R references.

The new flow is:

```text
company context
-> E2R query plan
-> fixture search results or request-only provider
-> E2R usefulness ranking
-> fixture text fetch
-> report/news/disclosure parsing
-> Evidence
-> FeatureEngineeringInput
-> deterministic score
-> StageClassifier
```

Simple example:

```text
"HD현대일렉트릭 수주잔고 OPM 수출 비중 PDF"
-> broker PDF result titled "줄을 서시오"
-> local fixture text
-> ResearchReport + Evidence
-> contract/backlog/CAPA/ASP/revision fields
-> Stage 3-Green when deterministic thresholds pass
```

## Files Added

- `src/e2r/research/query_planner.py`
- `src/e2r/research/search_provider.py`
- `src/e2r/research/search_result_ranker.py`
- `src/e2r/research/page_fetcher.py`
- `src/e2r/research/pdf_text_extractor.py`
- `src/e2r/research/web_research_runner.py`
- `tests/test_web_research_runner.py`
- `docs/web_research_playbook.md`

## Query Planning

`QueryPlanner` creates four groups:

- Stage 1/2 discovery: backlog, long-term contracts, facility investment, CAPA, shortage, ASP, US/datacenter demand
- Stage 3 confirmation: consensus beat, review PDFs, target-price/EPS revision, backlog/OPM/export reports
- Stage 4B/4C monitoring: order slowdown, backlog decline, ASP/OPM decline, contract cancellation, accounting and audit issues, supply glut
- Sector regime: sector shortage, lead time, price increase, long-term contracts, prepayment, CAPA expansion

The planner only emits query strings. It does not call live search engines.

## Search Providers

Implemented providers:

- `FixtureSearchProvider`: returns local fixture search results.
- `EmptySearchProvider`: returns no results and allows graceful missing-data paths.
- `RequestOnlySearchProvider`: builds Naver/Bing/SerpAPI-style `SourceRequest` objects without making live API calls.

No tests require live credentials or network access.

## Ranking

`SearchResultRanker` scores results by E2R usefulness.

Positive signals include:

- recognized broker report domain
- PDF
- titles/snippets containing Review, 목표주가, 컨센서스, 수주잔고, CAPA, 장기공급계약, ASP, OPM
- high-tier source tokens
- fresh publish date
- company name match

Negative signals include:

- duplicate URL
- future publish date
- old result
- missing company name
- forum, rumor, advertising, or irrelevant pages

## Fetching and Extraction

`PageFetcher` is fixture-first:

- URL mapped to local text returns text.
- Missing fixture with live mode disabled returns a clear unavailable reason.
- Live scraping is not implemented by default.

`PDFTextExtractor` supports:

- exact fixture path mapping
- adjacent `.txt` fixture for a `.pdf`
- optional PyMuPDF/pdfplumber if installed
- clear capability errors when PDF extraction libraries are unavailable

## Parsing and Evidence

`WebResearchRunner` classifies selected documents as:

- `report`
- `news`
- `disclosure`
- `unknown`

Report-like text is parsed through `report_parser`.
News-like text uses the Naver news normalizer and E2R keyword augmentation.
Disclosure-like text uses the OpenDART normalizer.

The runner returns:

- `queries_run`
- `search_results`
- `ranked_results`
- `selected_results`
- `fetched_documents`
- `parsed_reports`
- `parsed_news`
- `parsed_disclosures`
- `evidence`
- `red_team_findings`
- `dropped_results`

## Feature Integration

The runner does not replace KRX/OpenDART/consensus connectors. It complements them.

Checkpoint 11 also lets feature engineering use report-level `est_per` and `est_pbr` as valuation fallbacks when licensed consensus rows are not present. This is needed because manual broker-report research often observes valuation directly from the report table before a normalized consensus export exists.

## Behavior Proven

Tests prove:

- HD현대일렉트릭-like query finds a broker PDF result titled "줄을 서시오", ranks it high, fetches fixture text, parses report fields, and emits Evidence.
- 효성중공업-like "저마진 수주 정리" report produces margin recovery and target revision evidence.
- 일진전기-like long-term contract disclosure parses contract ratio and duration.
- Zoom-like one-off pandemic demand evidence is marked as `shortage_type=one_off`.
- SMCI-like accounting issue emits a Red Team evidence candidate.
- Request-only provider builds future live request metadata without network calls.
- PDF extractor can use `.txt` fixtures without requiring PDF libraries.
- Web research output can flow into `FeatureEngineeringInput`, `DeterministicFeatureEngineer`, and `StageClassifier` to classify an HD-like case as Stage 3-Green.

## Guardrails

- No live scraping in tests.
- No API keys in code.
- Fixture mode is the default path.
- `as_of_date` filters future search results.
- Missing fields are not invented.
- Deterministic scoring remains separate from text parsing.
- No buy/sell recommendation wording is produced.
