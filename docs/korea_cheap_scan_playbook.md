# Korea Free Cheap Scan Playbook

## Why Cheap Scan Exists

Free web research should not deep-search every listed company every day.

The Korea flow is intentionally layered:

```text
Layer 1. Cheap Scan
공시, 가격, 거래대금, 재무, 거래소 위험 상태로 후보를 줄인다.

Layer 2. Event Search
cheap scan에 걸린 종목만 짧은 검색어를 돌린다.

Layer 3. Deep Research
E2R 구조가 보이는 종목만 리포트/PDF/뉴스/공시를 깊게 읽는다.
```

Simple example:

```text
전 종목 2,500개
-> 공급계약/신규시설투자/거래대금 급증 등 50개 후보
-> 후보별 3~5개 검색어
-> E2R 후보만 deep research
```

## Free Source Map

OpenDART:

- disclosure list
- corp code mapping request
- single-company financials
- periodic reports
- supply contracts, facility investment, earnings preannouncements, dilution/risk disclosures

KRX fixture or KRX request metadata:

- KOSPI/KOSDAQ instruments
- daily price bars
- trading value
- market cap
- 52-week high/low support through historical bars
- delisting/trading halt status when available in fallback rows

data.go.kr Financial Services Commission APIs:

- `금융위원회_KRX상장종목정보`
- `금융위원회_주식시세정보`
- `금융위원회_기업 재무정보`
- `금융위원회_공시정보`
- `금융위원회_주식발행정보`

KIND fixture/fallback:

- managed issue
- trading halt
- investment warning/caution
- unfaithful disclosure
- delisting risk

## Event Rules

Positive disclosure signals:

- `DISC_SUPPLY_CONTRACT`: supply contract disclosure
- `DISC_LONG_TERM_CONTRACT`: contract duration at least 24 months
- `DISC_CONTRACT_TO_SALES_10P`: contract amount to prior sales at least 10%
- `DISC_FACILITY_INVESTMENT`: facility investment disclosure
- `DISC_FACILITY_TO_MARKET_CAP_5P`: facility investment to market cap at least 5%
- `DISC_CAPA_INCREASE`: CAPA or production capacity increase
- `DISC_EARNINGS_PREANNOUNCE`: preliminary earnings or earnings outlook
- `DISC_OP_YOY_100P`: operating profit YoY at least 100%
- `DISC_BUYBACK_OR_CANCELLATION`: buyback or cancellation

Negative disclosure/risk signals:

- `DISC_RIGHTS_OFFERING`
- `DISC_CONVERTIBLE_BOND`
- `DISC_BOND_WITH_WARRANT`
- `DISC_LAWSUIT`
- `DISC_AUDIT_OPINION_ISSUE`
- `DISC_TRADING_HALT`
- `DISC_MANAGED_ISSUE`
- `DISC_DELISTING_RISK`
- `DISC_CONTRACT_CANCEL_OR_DELAY`
- `RISK_MANAGED_ISSUE`
- `RISK_TRADING_HALT`
- `RISK_INVESTMENT_WARNING`
- `RISK_UNFAITHFUL_DISCLOSURE`
- `RISK_DELISTING`

Price signals:

- `PRICE_VOLUME_SPIKE`: trading value is at least 3 times the 20-day average
- `PRICE_NEAR_52W_HIGH`: close is within 5% of the 52-week high
- `PRICE_60D_TOP_PERCENTILE`: 60-day return is top quintile in the local fixture universe
- `PRICE_GAP_WITH_DISCLOSURE`: same-day disclosure plus at least 5% intraday close/open gap

Financial signals:

- `FIN_OP_TURNAROUND`: operating profit turns positive
- `FIN_OPM_EXPANSION_5P`: OPM expands by at least 5 percentage points
- `FIN_FCF_TURNAROUND`: FCF turns positive
- `FIN_CFO_NET_INCOME_IMPROVEMENT`: CFO/net income ratio improves meaningfully
- `FIN_RECEIVABLES_INVENTORY_SPIKE`: receivables or inventory spike as a risk flag

## Scoring Thresholds

Cheap scan total score is a deterministic weighted score:

```text
positive =
  disclosure_event_score * 0.45
  + price_event_score * 0.25
  + financial_event_score * 0.30

total = positive - risk_drag
```

Risk does not become a positive E2R signal. For example:

```text
유상증자 공시
-> risk_event_score rises
-> disclosure_event_score stays 0
-> no deep_research escalation
```

Next-layer routing:

- structural disclosure plus price or financial confirmation -> `deep_research`
- structural disclosure alone -> `event_search`
- strong financial or price event alone -> `event_search`
- hard exchange risk -> `none`

## Reason Code To Query Mapping

Supply contract:

```text
{company} 장기공급계약 매출액 대비
{company} 단일판매 공급계약 계약기간
{company} 수주잔고
{company} 미국향 수주
{company} 장기공급계약 PDF
```

Facility investment:

```text
{company} 신규시설투자 CAPA 증설
{company} 생산능력 증가
{company} CAPA 증설 PDF
{company} 수요 증가 대응 신규 공장
```

Earnings preannouncement:

```text
{company} 실적 서프라이즈
{company} 영업이익 컨센서스 상회
{company} 목표주가 상향 EPS 상향 PDF
{company} Review PDF
```

Price/volume spike:

```text
{company} 수주잔고
{company} 공급부족
{company} 목표주가 상향
{company} 컨센서스 상회
```

Risk event:

```text
{company} 유상증자
{company} 전환사채
{company} 감사의견
{company} 거래정지
{company} 상장폐지 위험
```

## Naver Search Escalation

`KoreaCheapScanner.escalate_candidates_to_web_research()` only escalates candidates whose `recommended_next_layer` is `event_search` or `deep_research`.

It uses:

- `EscalationQueryPlanner`
- `FreeWebResearchRunner`
- `SearchBudget`

Example:

```text
DISC_SUPPLY_CONTRACT + PRICE_VOLUME_SPIKE
-> deep_research
-> "케이전력 장기공급계약 매출액 대비"
-> "케이전력 단일판매 공급계약 계약기간"
```

## Point-In-Time Rules

- Instruments must be listed on or before `as_of_date`.
- Price bars must have `date <= as_of_date` and `as_of_date <= scan_as_of_date`.
- Disclosures must have `published_at <= as_of_date` and `available_at <= as_of_date`.
- Financial actuals must have `reported_at <= as_of_date`.
- KIND risk rows must have `as_of_date <= scan_as_of_date`.

Easy example:

```text
scan_as_of_date = 2024-05-21
future 유상증자 disclosure = 2024-05-22
-> not used in 2024-05-21 candidate
```

## Limitations Of Free Mode

Free sources can detect event candidates, but they do not replace licensed consensus data.

Still likely to require paid or manually supplied data:

- full sell-side consensus history
- official analyst-level revision history
- complete intraday institutional flow
- broker database metadata
- normalized sector-wide forecast aggregates

The free mode uses public evidence first:

```text
official disclosure
-> broker PDF found by search
-> news/report text
-> Evidence
-> deterministic feature engineering
```

## Safety

The cheap scan layer must not:

- use paid financial APIs by default
- require credentials in tests
- scrape aggressively
- fabricate missing contract fields
- use future data
- turn risk disclosures into Green-style scoring
- output buy/sell recommendation wording
