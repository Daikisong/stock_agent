# Checkpoint 12 Report

## Scope

Checkpoint 12 adds the free web-research mode requested after Checkpoint 11.

The new path imitates the manual workflow:

```text
query generation
-> browser/search result discovery
-> result ranking
-> report/news/disclosure candidate selection
-> fixture or manual text extraction
-> Evidence
-> FeatureEngineeringInput
-> deterministic score
-> Stage classification
```

Simple example:

```text
HD현대일렉트릭 수주잔고 OPM 수출 비중 PDF
-> fixture search HTML
-> broker PDF result titled "HD현대일렉트릭 줄을 서시오"
-> extracted text fixture
-> ResearchReport + Evidence
-> Stage 3-Green
```

## Added Components

- `BrowserSearchProvider`
  - Parses fixture search-result HTML.
  - Provides optional Playwright execution when explicitly enabled.
  - Detects PDF, broker report domains, news domains, disclosure domains, CAPTCHA/block text.

- `NaverFreeSearchProvider`
  - Builds Naver Search API requests for news, web documents, and professional documents.
  - Uses fixture mode by default.
  - Uses `NAVER_CLIENT_ID` and `NAVER_CLIENT_SECRET` only when live mode is explicitly enabled.

- `SearchBudget`
  - Controls daily query count, per-symbol query count, deep-research symbol count, active-monitoring symbol count, query sleep, and CAPTCHA/block stop behavior.
  - Supports the free-mode architecture: cheap scan, event search, deep research, active monitoring.

- `ManualSourceProvider`
  - Allows optional URL/file/text fallback.
  - The default path remains search-driven.

- `FreeWebResearchRunner`
  - Runs search providers under budget.
  - Reuses the Checkpoint 11 ranking, fetching, parsing, and Evidence creation flow.
  - Produces `WebResearchPipelineResult` with web result, feature input, score, Red Team assessment, stage, skipped queries, provider errors, and budget state.

## Fixture Coverage

Added fixture HTML and extracted text under `data/raw/search_html/` for:

- HD현대일렉트릭-like broker report search
- 효성중공업-like margin recovery report search
- 일진전기-like long-term contract and CAPA search
- Zoom-like one-off pandemic demand search
- SMCI-like 4B/4C monitoring search

## Behavior Proven

Tests prove:

- Fixture HTML is parsed into normalized `SearchResult` objects.
- HD현대일렉트릭-like search fixture reaches Stage 3-Green.
- 효성중공업-like search fixture reaches Stage 3-Green.
- 일진전기-like search fixture extracts contract duration and contract-to-sales ratio, then reaches a Stage 2/3 candidate state.
- Zoom-like search fixture marks `shortage_type=one_off` and reaches Stage 3-Red.
- SMCI-like search fixture triggers Stage 4B before later Stage 4C hard break.
- Search budget skips excess queries.
- Naver free provider builds request metadata and gracefully handles missing credentials.
- Manual source fallback is optional and works through the same parser path.

## Guardrails

- No paid financial API was added.
- No live web call is required in tests.
- Playwright is optional.
- Naver credentials are optional.
- Fixture mode remains the default.
- CAPTCHA/block signals stop budgeted search when configured.
- Point-in-time filtering uses `published_at <= as_of_date`.
- Missing fields are not fabricated.
- The system still outputs rerating detection and monitoring information, not buy/sell instructions.
