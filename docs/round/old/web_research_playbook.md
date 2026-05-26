# E2R 2.0 Web Research Playbook

## Purpose

The web research runner imitates the manual research workflow used in the references.

It does not replace KRX, OpenDART, SEC, or consensus connectors. It fills the gap where a human would search news, broker PDFs, report-like pages, and public documents to verify whether a rerating thesis has real evidence.

Simple example:

```text
Search: "HD현대일렉트릭 수주잔고 OPM 수출 비중 PDF"
Find: broker PDF result
Read: extracted local fixture text
Parse: target revision, backlog, OPM, CAPA, ASP, shortage
Emit: Evidence
Score: deterministic feature engineer
Classify: Stage 3-Green / Yellow / Red
```

## Query Planning

`QueryPlanner` creates four query groups.

Stage 1/2 discovery:

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

Stage 3 confirmation:

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

Stage 4B/4C monitoring:

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

## Search Providers

The runner supports a `SearchProvider` protocol:

```text
search(query, as_of_date, max_results)
```

Implemented providers:

- `FixtureSearchProvider`: returns local CSV/JSON/in-memory fixture results.
- `EmptySearchProvider`: returns no results for graceful missing-data tests.
- `RequestOnlySearchProvider`: builds request metadata for Naver, Bing, or SerpAPI-style adapters without live calls.

What fixture mode allows:

- local search result metadata
- local text fixtures
- local PDF-adjacent `.txt` files
- deterministic tests

What requires credentials later:

- Naver Search API
- Bing Search API
- SerpAPI
- licensed broker report search databases

## Ranking Rules

`SearchResultRanker` ranks by likely E2R evidence value.

Positive weights:

- recognized broker report domain
- PDF
- title or snippet contains Review, 목표주가, 컨센서스, 수주잔고, CAPA, 장기공급계약, ASP, OPM
- high-tier source tokens such as broker, research, OpenDART, KIND, SEC
- publish date near `as_of_date`
- company name in title or snippet

Negative weights:

- forum or rumor-only source
- result too old
- company name missing
- advertising or irrelevant page
- duplicate URL
- future publish date

Easy example:

```text
Broker PDF on 2023-07-27 with company name and "수주잔고 OPM"
-> ranked high

Anonymous forum post from 2020 without company name
-> ranked low or dropped
```

## Trusted Report Domains

Recognized report domains come from the source layer and include:

- `ssl.pstatic.net/imgstock/upload/research/company`
- `file.alphasquare.co.kr/media/pdfs`
- `hanaw.com/download/research`
- Samsung POP domains
- IBK domains
- major Korean broker report domains already listed in `src/e2r/sources/report_search.py`

This does not mean every result is true. It only means the page is more likely to contain structured research evidence.

## Fetching and PDF/Text Extraction

`PageFetcher` is fixture-first:

- URL mapped to fixture text returns the text.
- URL without fixture text returns an unavailable reason if live mode is disabled.
- Live scraping is not enabled by default.

`PDFTextExtractor` supports:

- exact fixture mapping
- `.pdf` with adjacent `.txt`
- optional PyMuPDF or pdfplumber

If PDF libraries are missing, the extractor returns a capability error instead of crashing.

## Evidence Creation

The runner creates Evidence only after fetched text is parsed into normalized domains.

Report-like document:

```text
fetched text
-> ResearchReport
-> Evidence(source_type="research_report")
```

News-like document:

```text
fetched text
-> NewsItem
-> Evidence(source_type="news")
```

Disclosure-like document:

```text
fetched text
-> DisclosureEvent
-> Evidence(source_type="disclosure")
```

Missing fields stay missing. For example, if a contract article has duration but no contract amount, the runner records duration and raw text but does not invent an amount.

## Raw Feature Creation

Parsed objects flow into `FeatureEngineeringInput`:

```text
FeatureEngineeringInput(
  disclosures=web_result.parsed_disclosures,
  research_reports=web_result.parsed_reports,
  news_items=web_result.parsed_news,
)
```

Then:

```text
DeterministicFeatureEngineer
-> ScoringPayload
-> DeterministicScorer
-> StageClassifier
```

The runner itself does not make final stage judgments. It prepares evidence and normalized objects.

## Sub-Score Mapping

Examples:

```text
계약기간 60개월 + 매출액 대비 55% + 선수금 + 해지 불가
-> contract_quality
```

```text
수주잔고/매출 155% + 사상 최대 수주잔고
-> backlog_rpo_visibility
```

```text
CAPA utilization 96% + 리드타임 24개월 + CAPA 선점 3년
-> capa_constraint
```

```text
ASP YoY 18% + 판가 전가
-> asp_pricing_power
```

```text
구조적 공급부족 + 장기계약 + 수주잔고 + CAPA + ASP
-> structural_shortage
```

```text
팬데믹, 코로나, 일회성, temporary demand
-> shortage_type=one_off
-> one_off_shortage_risk
```

## Point-In-Time Rules

- Search results with `published_at` after `as_of_date` are not used.
- Fetched text is treated as available only as of the selected result date or decision date.
- Parsed reports keep their publish date.
- Evidence uses `available_at <= as_of_date`.
- Future outcome prices are never used by the web research runner.

Easy example:

```text
as_of_date = 2023-07-27
result published_at = 2023-08-01
-> dropped as future_result
```

## Terms of Service and Source Safety

Allowed now:

- fixture search results
- fixture text
- request metadata construction
- manually supplied public text

Not allowed by default:

- aggressive crawling
- bypassing login or paywalls
- uncontrolled PDF downloading
- live scraping in tests

Later live adapters should use official APIs, rate limits, source terms, and explicit credentials.

## Manual Source Input

When a report or article cannot be fetched safely, the operator can save extracted text into a fixture and map the URL to that text.

Example:

```text
fixture_text_by_url = {
  "https://broker.example/report.pdf": "발행일 2023.07.27 ... 수주잔고 ..."
}
```

This preserves reproducibility and avoids brittle scraping.

## Licensed Data Still Needed

The web research runner does not solve licensed data gaps.

Still provider-dependent:

- full FnGuide/QuantiWise/WiseReport consensus history
- complete broker report databases
- normalized target-price revision history
- high-quality historical PDF archives
- vendor-grade financial estimate tables
