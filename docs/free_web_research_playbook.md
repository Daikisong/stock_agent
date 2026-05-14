# E2R 2.0 Free Web Research Playbook

## Purpose

Free web research is the closest implementation to the manual research workflow used in the references.

It is not a paid-data quant scanner. It is a search-first research agent:

```text
검색어 생성
-> 검색엔진 결과 확인
-> 리포트/PDF/뉴스/공시성 결과 선별
-> 문서 열람 또는 fixture text 로딩
-> 핵심 숫자 추출
-> Evidence
-> E2R 2.0 Stage
```

Simple example:

```text
"HD현대일렉트릭 수주잔고 OPM 수출 비중 PDF"
-> broker PDF result
-> target revision, backlog, OPM, CAPA, ASP, lead time
-> Stage 3-Green candidate
```

## Query Groups

The runner reuses `QueryPlanner`.

Discovery:

```text
{company} 수주잔고
{company} 장기공급계약
{company} 단일판매 공급계약
{company} 신규시설투자
{company} CAPA 증설
{company} 공급부족
{company} ASP 상승
{company} 판가 상승
{company} 미국향 수주
{company} 데이터센터 수주
```

Confirmation:

```text
{company} 컨센서스 상회 Review PDF
{company} 영업이익 컨센서스 상회
{company} 목표주가 상향 EPS 상향 PDF
{company} 수주잔고 OPM 수출 비중 PDF
{company} 실적 서프라이즈 목표주가 상향 PDF
{company} 1Q Review 영업이익 컨센서스 PDF
{company} 2Q Review 영업이익 컨센서스 PDF
{company} 3Q Review 영업이익 컨센서스 PDF
{company} 4Q Review 영업이익 컨센서스 PDF
```

Monitoring:

```text
{company} 수주 둔화
{company} 수주잔고 감소
{company} ASP 하락
{company} 영업이익률 하락
{company} 컨센서스 하향
{company} 계약 취소
{company} 계약 지연
{company} 회계 이슈
{company} 감사의견
{company} 공급과잉
```

Sector regime:

```text
{sector} 공급 부족
{sector} 리드타임
{sector} 가격 상승
{sector} 장기계약
{sector} 선수금
{sector} CAPA 증설
```

## Three-Layer Scan

The free architecture should avoid deep-searching every listed company every day.

```text
Layer 1. Cheap Scan
공시, 가격, 거래대금, 뉴스량, 52주 신고가 근접 같은 싼 신호로 후보를 줄인다.

Layer 2. Event Search
이벤트 후보만 짧은 검색어로 확인한다.

Layer 3. Deep Research
E2R 냄새가 나는 종목만 리포트/PDF/뉴스/공시를 깊게 읽는다.
```

`SearchBudget` enforces this with daily query caps, per-symbol caps, deep-research symbol caps, active-monitoring symbol caps, optional sleep, and CAPTCHA/block stop behavior.

## Result Ranking

`SearchResultRanker` ranks by E2R usefulness.

Positive:

- recognized broker report domain
- PDF
- Review, 컨센서스, 목표주가, 수주잔고, OPM, CAPA, 장기공급계약, ASP, 리드타임
- official, broker, high-tier news, DART, SEC-like source
- company name match
- publish date close to `as_of_date`

Negative:

- forum-only or rumor source
- irrelevant advertisement
- missing company name
- old result
- duplicate URL
- future publish date

## Candidate Selection

Report-like:

```text
broker PDF domain, PDF URL, Review/목표주가/OPM title
-> ResearchReport parser
```

News-like:

```text
news domain, Reuters/연합뉴스/한국경제/매일경제/이데일리-like source, news title
-> NewsItem parser
```

Disclosure-like:

```text
DART/OpenDART/KIND/SEC domain, 단일판매, 신규시설투자, 감사의견, 공시 title
-> DisclosureEvent parser
```

## Text Extraction

Current allowed paths:

- fixture HTML search results
- fixture TXT extracted report/news/disclosure text
- manual URL/file/text fallback
- optional Playwright page content when explicitly enabled
- optional Naver Search API when explicitly enabled

PDF parsing stays fixture-first. If PyMuPDF or pdfplumber is unavailable, the extractor returns a capability error instead of crashing.

## Free Mode vs Paid APIs

Paid-data mode might use licensed consensus or broker databases.

Free mode replaces that with:

- OpenDART and SEC public filings
- Naver free search request builders or credentials
- Playwright browser search when explicitly enabled
- broker report PDFs found by search
- local PDF/TXT fixtures
- report text fields such as EPS revision, OP revision, PER/PBR, target price revision

Example:

```text
2025E EPS 40% 상향
목표주가 33% 상향
2Q 영업이익 컨센서스 30% 상회
수주잔고 사상 최대
OPM 8% -> 15%
```

These can support Stage 3 evidence without a paid consensus API when they are parsed from a dated source.

## Running With Fixtures

Use `BrowserSearchProvider(fixture_html_by_query=...)` and pass URL-to-text fixtures into `FreeWebResearchInput.fixture_text_by_url`.

```text
fixture HTML
-> SearchResult
-> fixture TXT by URL
-> Evidence
-> Stage
```

This is the default test path.

## Running With Naver Credentials

Set:

```text
NAVER_CLIENT_ID
NAVER_CLIENT_SECRET
```

Then instantiate `NaverFreeSearchProvider(fixture_mode=False, live_enabled=True)`.

If credentials are missing, the provider records a clear missing-credential error and returns fixture results or empty results.

## Running With Playwright

Instantiate `BrowserSearchProvider(live_enabled=True)`.

If Playwright is not installed, it records `playwright_not_installed`.

Live browser mode must obey:

- low query rate
- query budget
- sleep between queries
- no aggressive crawling
- stop on CAPTCHA or blocking page
- site terms and robots cautions

## Point-In-Time Rules

- Results after `as_of_date` are dropped.
- Parsed reports keep their publish date.
- Evidence requires `available_at <= as_of_date`.
- Future accounting/news/result text cannot be used for an earlier stage.

Easy example:

```text
as_of_date = 2024-01-18
SMCI accounting issue result = 2024-08-28
-> dropped for January 2024 research
```

## Manual Source Fallback

`ManualSourceProvider` can accept local files, text, or URLs.

This is optional. It exists for cases where safe search cannot fetch a source, not as the default research path.

## Safety

The free web mode must not:

- use paid financial APIs by default
- require credentials
- make live web calls in tests
- bypass login or paywalls
- invent missing fields
- issue buy/sell recommendation wording

It should produce evidence-backed monitoring output only.

## Report Radar

Report Radar is a lightweight recall layer before symbol-specific deep research.

It searches high-signal phrases such as:

```text
목표주가 상향 EPS 상향 PDF
컨센서스 상회 Review PDF
실적 서프라이즈 목표주가 상향 PDF
수주잔고 OPM 수출 비중 PDF
신규시설투자 CAPA 증설 PDF
장기공급계약 매출액 대비 PDF
ASP 상승 판가 상승 리드타임 PDF
북미 미국향 데이터센터 수주 PDF
```

It differs from production confirmation:

```text
Report Radar result
-> "this looks worth checking"

Parsed report/news/disclosure evidence
-> "this can affect score/stage"
```

For example:

```text
검색 결과 제목: "효성중공업 저마진 수주 정리 Review PDF"
-> report_radar candidate
-> deep_research query
-> parser must still extract margin, target revision, backlog, or risk fields
```

Report Radar respects `SearchBudget` and should use a capped universe or watchlist. It is not allowed to deep-search every listed company every day.

## Targeted Smoke Is Not Evidence

Targeted smoke exists to test the search pipeline after a zero-candidate day.

It is marked:

```text
candidate_source_path = targeted_smoke
test_injected = True
production_candidate = False
```

Smoke output may appear in `run_log.targeted_smoke_results`, but it is excluded from production candidate ranking and the real morning brief.

Example:

```text
targeted smoke query returns no document
-> status = insufficient_evidence
-> no Stage 3-Green
```

This keeps the pipeline test separate from evidence creation.
