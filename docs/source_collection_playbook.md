# E2R 2.0 Source Collection Playbook

## Purpose

The collection layer exists to support this research workflow:

```text
scan universe
-> collect filings, news, reports, prices, consensus
-> parse evidence
-> engineer raw features
-> score deterministically
-> classify Stage 3/4 state
-> backtest and monitor thesis break
```

Simple example:

```text
Company A has a 5-year supply contract, 50% of prior-year sales, customer prepayment, and CAPA locked for 3 years.
That evidence maps to contract_quality, backlog_rpo_visibility, and structural_shortage.
```

## Source Map

| Source | Used For | Output Models |
| --- | --- | --- |
| KRX | KR instruments, daily prices, trading value, market cap, 52-week range, halt/listing flags from fallback files | `Instrument`, `PriceBar` |
| OpenDART | KR disclosures, contracts, facility investment, event filings, periodic reports | `DisclosureEvent`, `Evidence` |
| data.go.kr FSC listed/price | KR listed-item and stock-price live-lite fallback where license permits | `Instrument`, `PriceBar` |
| data.go.kr FSC stock issuance | Optional only. Use only if the API-specific license permits intended use | raw issuance rows |
| KIND | managed issue, caution, halt, unfaithful disclosure, delisting-risk status | `Instrument` flags, `Evidence`, Red Team candidates |
| Naver News | company and sector event search | `NewsItem`, `Evidence`, optional Red Team candidate |
| Naver Web/Doc | report-like web documents and broker PDFs | `ReportSearchResult` |
| Report Search | broker PDF/report metadata from fixture or future provider search | `ReportSearchResult` |
| SEC EDGAR | US submissions, companyfacts, 10-K, 10-Q, 8-K evidence | `FinancialActual`, `DisclosureEvent`, `NewsItem`, `Evidence` |
| Consensus CSV | licensed-provider exports in CSV/JSON form | `ConsensusSnapshot`, `ConsensusRevision` |

## Query Templates

Company news:

```text
{company} 수주잔고
{company} 장기공급계약
{company} 단일판매 공급계약
{company} 신규시설투자
{company} CAPA 증설
{company} 영업이익 컨센서스 상회
{company} 목표주가 상향
{company} 미국향 수주
{company} 데이터센터 수주
{company} 공급부족
{company} ASP 상승
{company} 판가 상승
{company} 유상증자
{company} 전환사채
{company} 신주인수권부사채
{company} 보호예수 해제
{company} 오버행
{company} CB 리픽싱
```

Sector news:

```text
{sector} 공급 부족
{sector} 리드타임
{sector} 가격 상승
{sector} 장기계약
{sector} 선수금
```

Report search:

```text
{company} 목표주가 상향 EPS 상향 PDF
{company} 컨센서스 상회 Review PDF
{company} 1Q Review 영업이익 컨센서스 PDF
{company} 2Q Review 영업이익 컨센서스 PDF
{company} 3Q Review 영업이익 컨센서스 PDF
{company} 4Q Review 영업이익 컨센서스 PDF
{company} 수주잔고 OPM 수출 비중 PDF
{company} 신규시설투자 CAPA 증설 PDF
{company} 장기공급계약 매출액 대비 PDF
{company} ASP 상승 판가 상승 리드타임 PDF
{company} 북미 미국향 데이터센터 수주 PDF
{company} 실적 서프라이즈 목표주가 상향 PDF
```

Recognized report locations include Naver stock research PDFs, AlphaSquare report PDFs, Hana research downloads, Samsung POP, IBK, and major Korean broker PDF domains.

## Expected Parsed Fields

OpenDART disclosure fields:

```text
contract_amount
contract_amount_to_prior_sales
contract_start
contract_end
contract_duration_months
counterparty
product_or_service
region
is_long_term
is_cancellable
prepayment_exists
rpo_mentioned
backlog_mentioned
facility_investment_amount
facility_investment_to_market_cap
capa_increase_pct
expected_completion_date
dilution_type
```

Naver News fields:

```text
event_type
mentioned_product
mentioned_region
customer_type
contract_amount
capex_amount
backlog_amount
margin_comment
asp_comment
capa_comment
shortage_comment
risk_comment
source_tier
confidence
```

Research report fields include report date, broker, analyst, title, current and target prices, target revision, upside, 52-week range, 1/3/12-month returns, FY1-FY3 sales/OP/EPS, PER/PBR, ROE, OPM, backlog, new orders, backlog-to-sales, CAPA increase, export ratio, US revenue ratio, ASP, lead-time, shortage mention, target multiple change, investment points, and risk points.

## Evidence Rules

Every evidence record must include:

- source type and source name
- source tier
- published, observed, available timestamps
- `as_of_date`
- market and symbol
- title
- parsed fields
- parser confidence when parsing is partial

Do not invent missing fields. If a contract amount is absent, store the raw text and leave `contract_amount` unset.

## Raw Feature Creation Rules

Feature engineering reads normalized models only:

```text
FinancialActual
ConsensusSnapshot
ConsensusRevision
DisclosureEvent
ResearchReport
NewsItem
PriceBar
```

For example:

```text
contract_duration_months=60
contract_amount_to_prior_sales=0.37
prepayment_exists=true
```

maps into `contract_quality`.

```text
order_backlog_to_sales=1.55
rpo_to_sales=1.30
backlog_yoy_pct=48
```

maps into `backlog_rpo_visibility`.

```text
capa_utilization_pct=96
lead_time_months=24
capa_locked_years=3
```

maps into `capa_constraint` and `structural_shortage`.

## Sub-Score Mapping

| Sub-score | Positive Evidence | Risk Evidence |
| --- | --- | --- |
| `contract_quality` | long duration, large sales ratio, prepayment, non-cancellable or repeat demand | weak contract terms, short duration |
| `backlog_rpo_visibility` | backlog/RPO to sales, growth, record backlog | backlog decline |
| `capa_constraint` | high utilization, long lead time, locked capacity, precommitted expansion | supply glut, fast shortage relief |
| `asp_pricing_power` | ASP/price increase, premium mix, customer acceptance | ASP decline |
| `structural_shortage` | contract + backlog + CAPA + ASP together | one-off or cyclical-only evidence |
| `one_off_shortage_risk` | pandemic spike, temporary demand, single-product special demand | durable contract/backlog evidence lowers it |

## Structural vs One-Off Shortage

Structural shortage requires several of these together:

- multi-year contract or recurring demand
- backlog/RPO visibility
- CAPA utilization or lead-time evidence
- ASP or pricing-power evidence
- no clear temporary-demand label

One-off shortage is used when the evidence says demand is temporary.

Example:

```text
Diagnostic-kit demand during a pandemic spike
-> one_off_shortage_risk high
-> Stage 3-Red if EPS revision is strong but durability is weak
```

Structural example:

```text
5-year transformer contract + backlog above annual sales + 24-month lead time + price increase
-> structural_shortage high
-> eligible for Stage 3-Green when revision and valuation evidence also pass
```

## Point-In-Time Rules

- A record cannot enter scoring if `available_at` is after the decision date.
- A restated financial row cannot replace what was known earlier.
- Price bars before the Stage 3 date must have been available by the Stage 3 date.
- Historical outcome prices are allowed only in backtest windows, not in feature scoring.
- Search results and parsed reports keep their own publish dates.

## Licensed Data Still Needed

The repository uses CSV/JSON fallback for consensus because several KR and US estimate providers require licenses.

## Optional Stock Issuance API

`금융위원회_주식발행정보` / `GetStockIssuanceInfoService/getStockIssueInfo` is optional.

It is not required for E2R scoring or Korea live-lite operation.

Why:

```text
OpenDART 유상증자 / 전환사채 / 신주인수권부사채
금융위원회_공시정보
Naver Search risk queries
```

already cover the core dilution-risk workflow.

Use the stock issuance API only if the latest public-data license allows the intended use. Do not assume commercial use is allowed. If the API is attribution-only, non-commercial-only, or otherwise constrained, keep it disabled for production and future commercial expansion.

Current default:

```text
enable_stock_issuance_source = False
source_modes.stock_issuance = disabled_optional
```

Still licensed or provider-dependent:

- FnGuide, QuantiWise, WiseReport consensus history
- detailed broker report databases
- intraday or adjusted vendor price feeds
- complete corporate action history
- normalized global fundamentals beyond SEC/OpenDART fixtures

Until those are connected, tests must rely on local fixture files and request builders only.
