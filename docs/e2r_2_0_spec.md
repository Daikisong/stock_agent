# E2R 2.0 Canonical Specification

이 문서는 `docs/레퍼런스1.md`부터 `docs/레퍼런스13.md`까지의 내용을 기준으로 고정한 E2R 2.0 표준 사양이다.

E2R 2.0은 한국 및 미국 상장주에서 "EPS/FCF 체급 변화가 시장에 아직 덜 반영된 리레이팅 후보"를 탐지하고, 신호 발생 뒤에는 논리가 유지되는지 계속 감시하는 에이전트다. 출력은 탐지와 모니터링 정보이며, 매수/매도 권고를 만들지 않는다.

## 1. Scope

### 1.1 목표

- 한국 및 미국 보통주 유니버스에서 리레이팅 후보를 매일 탐지한다.
- 숫자, 공시, 리포트, 뉴스, 산업 레짐, 가격 반영 정도를 함께 본다.
- Stage 0, 1, 2, 3-Green, 3-Yellow, 3-Red, 4A, 4B, 4C, 5 상태를 결정한다.
- Stage 3 이후에는 Red Team 감시로 논리 훼손과 과밀 구간을 추적한다.
- 모든 판단은 `as_of_date` 기준으로 재현 가능해야 한다.
- 백테스트는 그 날짜에 이미 공개된 데이터만 사용한다.
- 처음 구현은 mock/fallback connector로 동작하고, live API는 이후 교체 가능하게 둔다.

### 1.2 하지 않는 것

- 매수, 매도, 비중 축소 같은 투자 권고를 직접 출력하지 않는다.
- 과거 성공 종목 이름을 scoring logic에 하드코딩하지 않는다.
- 2026년에 알게 된 데이터를 2023년 stage 판정에 쓰지 않는다.
- LLM의 자유 판단만으로 점수를 만들지 않는다.

쉬운 예시:

- 나쁜 방식: "HD현대일렉트릭은 과거에 크게 올랐으니 비슷한 종목이면 점수 가산"
- 좋은 방식: "수주잔고/매출, OPM 개선폭, EPS revision, valuation runway가 같은 기준을 통과하면 점수 가산"

## 2. Reference Distillation

레퍼런스별 핵심 반영 사항은 아래와 같다.

| 파일 | 사양에 반영한 핵심 |
| --- | --- |
| `레퍼런스1.md` | 반도체 바닥에서는 후행 PER보다 forward EPS, PBR, 업황 반전 신호가 중요하다. |
| `레퍼런스2.md` | 좋은 발견 시점은 EPS 폭발 뒤가 아니라, 실적은 더럽지만 ASP, 고부가 제품, 재고 정상화가 먼저 움직이는 시점이다. |
| `레퍼런스3.md` | 생존 필터, EPS Explosion, Revision, Valuation, Rerating, Price Stage, 통합 점수, Red Team, 백테스트 설계를 반영한다. |
| `레퍼런스4.md` | 전력기기 사이클은 EPS 상승과 멀티플 리레이팅이 동시에 일어난 E2R 사례다. |
| `레퍼런스5.md` | 이미 오른 종목을 자동 탈락시키지 말고, 가격보다 EPS/수주/마진이 더 빠른지 비교해야 한다. |
| `레퍼런스6.md` | 전체 agent pipeline, source tier, DB 구조, daily briefing, JSON 출력, point-in-time 원칙을 반영한다. |
| `레퍼런스7.md` | Stage 1~4 판정 기준, report parser 추출 필드, scoring formula, morning brief 예시를 반영한다. |
| `레퍼런스8.md` | Stage 2와 Stage 3 인식일을 분리하고, historical fixture case를 stage별로 관리한다. |
| `레퍼런스9.md` | E2R 2.0 scoring을 100점 체계로 재정의하고, 4A/4B/4C 분리를 반영한다. |
| `레퍼런스10.md` | FCF, 영업현금흐름, 매출채권, 재고, 계약 질, Red Team field를 필수 필드로 반영한다. |
| `레퍼런스11.md` | Stage 0~5 전체 흐름과 Stage 3 Green/Yellow/Red 분기를 반영한다. |
| `레퍼런스12.md` | Stage 3 이후 MFE/MAE, pre-runup, below-entry, time-to metrics를 반영한다. |
| `레퍼런스13.md` | 4B Soft Exit Score, 4C thesis-break, 4B/4C backtest 지표를 반영한다. |

## 3. Core Principles

### 3.1 숫자 먼저, 해석은 나중

Pipeline은 다음 순서로 실행한다.

```text
Universe and risk filter
-> price and liquidity analysis
-> actual financials and consensus analysis
-> disclosures, contracts, CAPA, reports
-> news and sector regime
-> rerating thesis extraction
-> Red Team risk analysis
-> deterministic scoring
-> stage classification
-> Korean morning briefing
```

LLM이 쓰이는 경우에도 역할은 텍스트에서 구조화된 증거를 추출하는 것이다. 최종 점수와 stage는 deterministic rule engine이 계산한다.

### 3.2 Point-in-time 원칙

모든 입력은 아래 시간을 가진다.

- `published_at`: 문서가 공식적으로 나온 시각
- `observed_at`: 시스템이 수집한 시각
- `available_at`: 투자자가 합리적으로 사용할 수 있는 시각
- `as_of_date`: stage와 점수가 기준으로 삼는 날짜

예시:

- 리포트가 2024-03-27 장중에 나왔고 시스템이 그날 18시에 수집했다면, 한국 아침 브리핑에서는 2024-03-28 후보로 표시할 수 있다.
- 2026년 사업보고서에 나온 수주 감소는 2024년 stage 판정에 절대 쓰지 않는다.

### 3.3 Evidence-first

모든 score와 stage는 근거를 가진다.

Evidence item은 최소한 아래 필드를 가진다.

```text
evidence_id
source_type
source_name
source_tier
published_at
observed_at
available_at
as_of_date
market
symbol
title
url_or_identifier
excerpt_or_value
parsed_fields
confidence
```

## 4. Data Model Specification

Checkpoint 1에서 코드 모델로 구현할 개념 모델이다.

### 4.1 Instrument

```text
symbol
name
market: KR | US
exchange
sector_exchange
sector_custom
listed_date
currency
is_preferred
is_spac
is_reit
is_etf
is_managed
is_invest_warning
is_trading_halt
```

### 4.2 PriceBar

```text
symbol
date
open
high
low
close
adj_close
volume
trading_value
market_cap
source
as_of_date
```

### 4.3 FinancialActual

```text
symbol
fiscal_year
fiscal_quarter
period_end
reported_at
sales
operating_profit
net_income
eps
bps
roe
opm
debt_ratio
cashflow_from_operations
capex
fcf
receivables
inventory
source
as_of_date
```

### 4.4 ConsensusSnapshot

```text
symbol
date
fiscal_year
sales_e
op_e
net_income_e
eps_e
bps_e
roe_e
per_e
pbr_e
analyst_count
target_price
target_multiple_type
target_multiple
source
as_of_date
```

### 4.5 ConsensusRevision

```text
symbol
date
fiscal_year
eps_revision_1w
eps_revision_1m
eps_revision_3m
op_revision_1w
op_revision_1m
op_revision_3m
fcf_revision_1m
target_price_revision_1m
analyst_count_change
as_of_date
```

### 4.6 DisclosureEvent

```text
symbol
source
report_type
title
published_at
observed_at
rcept_no
raw_text
parsed_fields
as_of_date
```

Important parsed fields:

```text
contract_amount
contract_amount_to_prior_sales
contract_start
contract_end
contract_duration_months
counterparty
is_long_term
is_cancellable
prepayment_exists
capa_increase_pct
facility_investment_amount
facility_investment_to_market_cap
dilution_type
```

### 4.7 ResearchReport

```text
symbol
publish_date
broker
analyst
title
current_price
target_price
rating
target_revision_pct
target_multiple_before
target_multiple_after
fy1_sales
fy1_op
fy1_eps
fy2_sales
fy2_op
fy2_eps
est_per
est_pbr
investment_points
risk_points
raw_text
parsed_fields
as_of_date
```

### 4.8 NewsItem and SectorRegime

```text
news_item:
  symbol
  sector
  published_at
  source
  title
  body
  source_tier
  theme_tags
  sentiment
  parsed_fields
  as_of_date

sector_regime:
  sector
  date
  theme_regime_score
  high_quality_news_count
  official_data_confirmation
  sector_relative_strength
  report_keyword_density
  cross_company_disclosure_count
  as_of_date
```

### 4.9 ScoreSnapshot

```text
symbol
as_of_date
eps_fcf_explosion_score
earnings_visibility_score
bottleneck_pricing_score
market_mispricing_score
valuation_rerating_score
capital_allocation_score
information_confidence_score
risk_penalty
total_score
diagnostic_scores
evidence_ids
scoring_version
```

### 4.10 StageSnapshot

```text
symbol
as_of_date
stage
stage_color
previous_stage
stage_changed
grade
stage_reason
red_team_status
evidence_ids
classifier_version
```

Valid stages:

```text
0
1
2
3-Green
3-Yellow
3-Red
4A
4B
4C
5
```

### 4.11 RedTeamFinding

```text
symbol
as_of_date
risk_type
severity
is_hard_break
description
evidence_ids
```

### 4.12 BacktestResult

```text
symbol
stage3_date
stage3_price
pre_runup_252d
pre_runup_3y
mfe_30d
mfe_90d
mfe_180d
mfe_1y
mfe_2y
mae_30d
mae_90d
mae_180d
mae_1y
below_entry_flag
time_to_50pct
time_to_100pct
time_to_200pct
time_to_4b
time_to_4c
stage4b_date
stage4b_price
stage4b_return_from_stage3
stage4c_date
stage4c_price
peak_date
peak_price
peak_return_from_stage3
drawdown_after_peak
```

## 5. Deterministic Scoring

### 5.1 Canonical 100-point score

E2R 2.0 total score is:

```text
Total Score =
  EPS/FCF Explosion                 20
+ Earnings Visibility and Quality   20
+ Bottleneck and Pricing Power      20
+ Market Mispricing                 15
+ Valuation Rerating Runway         15
+ Capital Allocation                 5
+ Information Confidence             5
- Risk Penalty
```

### 5.2 Component definitions

#### EPS/FCF Explosion, 20 points

Measures whether future profit and cash flow are structurally larger than current or trailing numbers.

Inputs:

```text
FY1/FY2/FY3 OP growth
FY1/FY2/FY3 EPS growth
FY1/FY2/FY3 FCF growth
OP delta / market cap
OPM expansion
ROE expansion
turnaround flag
```

Example:

- TTM OP is 300억, FY2 OP estimate is 1,500억, current market cap is 4,000억.
- OP delta / market cap is 30%.
- This is stronger than a company whose OP delta is the same 1,200억 but market cap is 2조.

#### Earnings Visibility and Quality, 20 points

Measures whether the earnings change can last.

Inputs:

```text
order backlog / sales
new orders / sales
RPO / sales
contract duration
prepayment
non-cancellable contract terms
cashflow from operations / net income
FCF quality
receivables growth
inventory growth
customer concentration
```

#### Bottleneck and Pricing Power, 20 points

Measures whether customers have to buy despite higher prices.

Inputs:

```text
capacity constraint
lead time extension
ASP increase
high-margin mix increase
limited suppliers
customer capex pressure
Capa locked by long-term orders
```

#### Market Mispricing, 15 points

Measures whether the market still uses an old frame.

Inputs:

```text
old sector classification
new bottleneck classification
coverage initiation
street high/low dispersion
consensus lag
skeptical report tone despite improving numbers
```

Example:

- Old frame: "중공업 복합기업"
- New frame: "북미 전력망 병목 변압기 기업"

#### Valuation Rerating Runway, 15 points

Measures whether price and multiple have not already consumed the whole thesis.

Inputs:

```text
forward PER
forward PBR
ROE / PBR
OP delta / market cap
peer discount
PEG inverse
historical band relevance
price return vs EPS/FCF revision
```

Important rule:

- Already up is not an automatic fail.
- The fail case is "price and PER/PBR moved much faster than EPS/FCF, backlog, and margin".

#### Capital Allocation, 5 points

Inputs:

```text
buyback
dividend
efficient growth capex
low dilution risk
debt discipline
```

#### Information Confidence, 5 points

Inputs:

```text
source tier
number of independent sources
official filing confirmation
report and consensus consistency
freshness
parser confidence
```

### 5.3 Diagnostic scores

These are stored for explainability and stage rules.

```text
revision_score
price_stage_score
theme_regime_score
order_backlog_or_capa_score
quality_score
red_team_score
soft_4b_score
thesis_break_score
```

### 5.4 Risk penalty

Risk penalty is deterministic and evidence-based.

Penalty categories:

```text
demand_collapse
supply_glut
weak_contract_enforceability
valuation_overheat
cashflow_deterioration
dilution
accounting_or_auditor_issue
peak_out
customer_concentration
low_liquidity
management_or_listing_risk
```

Hard risk examples:

- 거래정지, 관리종목, 감사의견 비적정
- 회계감사인 사임, 횡령/배임
- 중장기 EPS/FCF 하향과 수주 감소가 동시에 발생

## 6. Stage State Machine

### 6.1 Stage 0: Industry Hypothesis

Industry-level regime exists, but no company has enough company-level evidence.

Typical conditions:

```text
theme_regime_score >= 60
official or high-tier evidence exists
no company-level EPS/FCF evidence yet
```

Output meaning:

- Sector watch only.

### 6.2 Stage 1: Company Radar

Company-level event appears, but numbers are not enough for candidate inclusion.

Typical conditions:

```text
company_event_score >= 60
or high-quality disclosure/report event exists
total_score < 65
```

Examples of events:

```text
new facility investment
large order
coverage initiation
ASP increase mention
high-value product mix increase
sector-relative price strength
```

### 6.3 Stage 2: Candidate

Numbers and thesis begin to align.

Minimum conditions:

```text
total_score >= 65
EPS/FCF Explosion >= 10/20
Valuation Rerating Runway >= 7/15
Information Confidence >= 3/5
no hard Red Team break
```

Additional supporting conditions:

```text
FY2 OP >= TTM OP * 2
or turnaround with positive FY2 OP
OP delta / market cap >= 10%
OPM improvement >= 2 percentage points
order backlog / sales >= 0.8
recent price rise is supported by EPS/FCF revision
```

### 6.4 Stage 3-Green: High-confidence, Thesis Alive

Stage 3 means rerating is no longer just an idea. Results, consensus, backlog, and multiple frame are moving together.

Green conditions:

```text
total_score >= 85
EPS/FCF Explosion >= 17/20
Earnings Visibility and Quality >= 15/20
Bottleneck and Pricing Power >= 15/20
Market Mispricing >= 10/15
Valuation Rerating Runway >= 10/15
revision_score positive
Red Team risk low
```

Typical triggers:

```text
OP beats consensus by 10-15% or more
FY1/FY2 EPS or OP revision rises 15%+ within 1 month
target price rises 20%+
target PER/PBR moves up
OPM improves 3 percentage points or more
backlog is record high or at least about 1 year of sales
supply shortage, lead time, ASP increase are confirmed
```

### 6.5 Stage 3-Yellow: High-confidence, Watch Risk

Stage 3 evidence exists, but one or more important risks prevent Green classification.

Typical conditions:

```text
total_score >= 80
but valuation runway is narrow
or contract quality is not strong enough
or additional consensus revision is needed
or Red Team risk is moderate
```

### 6.6 Stage 3-Red: Stage 3 Signal but Poor Risk/Reward Setup

The company has strong-looking results or theme, but the rerating case is weak or already over-consumed by price.

Typical conditions:

```text
price and PER/PBR moved far ahead of EPS/FCF
OPM/ROE quality weak
long-term contract, backlog, or FCF durability weak
theme buying dominates evidence
one-off EPS spike likely
Red Team risk high
```

### 6.7 Stage 4A: Rerating Ongoing, Thesis Maintained

The stock has moved a lot, but the thesis is still supported.

Typical conditions:

```text
previous stage is Stage 3
EPS/FCF continues upward
backlog, RPO, or long-term contracts remain strong
OPM is stable or rising
pricing power remains
soft_4b_score < 60
thesis_break_score < hard threshold
```

### 6.8 Stage 4B: Graduation / Crowding

The company may still be good, but the market has largely accepted the new frame.

Soft 4B Score:

| Item | Points |
| --- | ---: |
| Return since Stage 3 | 15 |
| 12-24 month return | 15 |
| Extreme forward PER/PBR | 15 |
| EPS/FCF revision slowdown | 20 |
| Backlog/RPO/contract quality slowdown | 15 |
| Market crowding and capitulation of skeptics | 10 |
| Insider sale, major event, index inclusion | 5 |
| Blow-off price pattern | 5 |

Classification:

```text
soft_4b_score >= 60 and < 70: Stage 4B watch
soft_4b_score >= 70 and < 80: Stage 4B elevated
soft_4b_score >= 80: Stage 4B graduated
```

Output language must remain descriptive:

- "신규 기대수익률이 낮아질 수 있는 과밀 구간"
- "다음 EPS/FCF 상향이 없으면 위험 증가"

Do not output direct buy/sell instructions.

### 6.9 Stage 4C: Thesis Break

Hard thesis damage has occurred.

Typical hard-break conditions:

```text
medium/long-term EPS or FCF revision turns down
backlog or RPO declines
new orders sharply slow
long-term contract cancelled or delayed
OPM falls
ASP falls
supply glut appears
customer capex declines
accounting or trust issue appears
```

Output meaning:

- Core E2R thesis is broken unless a new thesis is formed with new evidence.

### 6.10 Stage 5: Archive

The case is no longer actively monitored as an E2R candidate.

Typical conditions:

```text
Stage 4C hard break confirmed
or Stage 4B remains graduated without new EPS/FCF runway for configured period
or delisting/coverage impossibility
```

Archive does not delete evidence. It freezes the case and keeps quarterly monitoring if data remains available.

## 7. Red Team Monitoring

Red Team runs after every scoring pass and again for active Stage 3/4 cases.

### 7.1 Daily checks

```text
large price gap
volume spike
investment warning
new disclosure
large contract or cancellation
insider sale
accounting or auditor issue
```

### 7.2 Weekly checks

```text
EPS/OP/FCF revision
target price revision
report tone change
institutional/foreign positioning
peer multiple change
```

### 7.3 Quarterly checks

```text
sales growth
OPM
FCF
CFO / net income
backlog / sales
new orders
prepayment
RPO
inventory
receivables
CAPA utilization
guidance
```

### 7.4 Thesis-break examples

Simple example:

- 좋은 신호: 수주잔고가 늘고 OPM이 유지된다.
- 나쁜 신호: 수주잔고가 줄고, OPM이 하락하고, EPS revision도 내려간다.
- 판정: 가격이 아직 버티더라도 Stage 4C 후보로 본다.

## 8. Backtesting Specification

### 8.1 Required point-in-time constraints

Backtest engine must:

- Use only records with `available_at <= decision_time`.
- Use previous close for daily morning classification unless intraday mode is explicitly configured.
- Preserve delisted, managed, warning, failed, and weak cases.
- Separate fixture labels from scoring rules.

### 8.2 Required metrics

For each Stage 3 event:

```text
Stage3_Date
Stage3_Price
PreRunup_252D = Stage3_Price / min(low over prior 252 trading days) - 1
PreRunup_3Y = Stage3_Price / min(low over prior 3 years) - 1
MFE_30D / 90D / 180D / 1Y / 2Y
MAE_30D / 90D / 180D / 1Y
BelowEntry_Flag
Time_to_50pct
Time_to_100pct
Time_to_200pct
Time_to_4B
Time_to_4C
Stage4B_Date
Stage4B_Price
Stage4B_Return_From_Stage3
Stage4C_Date
Stage4C_Price
Peak_Date
Peak_Price
Peak_Return_From_Stage3
Drawdown_After_Peak
```

Definitions:

```text
MFE_N = max(high from Stage3_Date to N trading days) / Stage3_Price - 1
MAE_N = min(low from Stage3_Date to N trading days) / Stage3_Price - 1
BelowEntry_Flag = any(close < Stage3_Price or low < Stage3_Price after Stage3_Date)
Time_to_X = first trading day where high >= Stage3_Price * (1 + X)
```

### 8.3 Fixture case policy

Fixture cases are used to test behavior, not to tune by name.

Required fixture categories:

```text
successful transformer/power-equipment rerating
semiconductor turnaround rerating
consumer/defense non-power rerating
momentum/theme false positive
peak-out after early success
Stage 3 overheat case
US equity boom-and-bust case
```

## 9. Connectors Specification

Live connectors are not required before checkpoint 5. Earlier checkpoints must use mock/fallback connectors with the same interface shape.

Connector interface:

```text
list_instruments(market, as_of_date)
get_price_bars(symbol, start, end, as_of_date)
get_financial_actuals(symbol, as_of_date)
get_consensus(symbol, as_of_date)
get_disclosures(symbol, start, end, as_of_date)
get_research_reports(symbol, start, end, as_of_date)
get_news(symbol, start, end, as_of_date)
```

Initial source mapping:

| Domain | Korea | US |
| --- | --- | --- |
| Instruments and prices | KRX, broker API fallback | exchange/vendor mock, later live API |
| Filings | OpenDART, KIND | SEC EDGAR |
| Financials | OpenDART, licensed data | company filings, licensed data |
| Consensus | FnGuide, QuantiWise, WiseReport | licensed consensus data |
| News | Naver News, high-tier media | high-tier media/vendor |
| Reports | WiseReport, broker PDFs | broker PDFs/vendor |

## 10. Korean Morning Briefing

The daily briefing is generated in Korean and should be readable before the Korean market opens.

Required sections:

```text
[E2R Morning Brief / YYYY-MM-DD]

1. 신규 Stage 2 후보
2. Stage 3-Green / Yellow / Red 변화
3. Stage 4A / 4B / 4C 변화
4. Red Team thesis-break 감시
5. 섹터 레짐 변화
6. 오늘 확인할 공시, 실적, 리포트 일정
```

Each item must include:

```text
종목명 / 코드 / 시장 / 섹터
현재 Stage와 전일 대비 변화
총점과 주요 component score
핵심 변화
핵심 숫자
근거 source와 as_of_date
Red Team 리스크
다음 확인 트리거
```

Allowed language:

- "관찰 필요"
- "고확신 후보로 상향"
- "논리 훼손 위험 증가"
- "과밀 구간 가능성"

Disallowed language:

- "매수"
- "매도"
- "비중 축소"
- "오늘 사야 함"

## 11. Checkpoint Plan

### Checkpoint 0: Spec

Artifacts:

- This canonical spec.
- Checkpoint report.

Verification:

- All 13 references and repo instruction context reviewed.
- Spec contains the full stage machine, scoring, evidence, backtest, connector, and briefing requirements.

### Checkpoint 1: Data Models and Scoring Interfaces

Implement:

- Python package structure.
- Pydantic or dataclass models for all core concepts.
- Scoring interface with deterministic inputs and outputs.
- Unit tests for model validation and score payload shape.

### Checkpoint 2: Stage Classifier and Red Team Rules

Implement:

- Stage machine.
- Stage 3 Green/Yellow/Red rules.
- 4B Soft Exit and 4C thesis-break rules.
- Tests for boundary cases.

### Checkpoint 3: Backtesting Engine

Implement:

- Point-in-time backtest runner.
- MFE/MAE, pre-runup, time-to-4B/4C, below-entry metrics.
- Tests proving no future data leak.

### Checkpoint 4: Fixture Cases

Implement:

- Historical fixture records.
- Success, warning, failure, peak-out, US boom-and-bust cases.
- Tests that fixtures are used as expected outputs, not scoring shortcuts.

### Checkpoint 5: Data Connectors

Implement:

- Mock/fallback connectors first.
- Stable connector protocols for later live API integration.
- Tests using fixture connector data.

### Checkpoint 6: Morning Briefing

Implement:

- Korean briefing generator.
- Evidence and as_of_date rendering.
- No recommendation wording tests.

### Checkpoint 7: Integration Tests and Review

Implement:

- End-to-end fixture scan.
- Stage transition integration test.
- Documentation review against this spec.

