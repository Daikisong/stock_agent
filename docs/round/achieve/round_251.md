순서상 이번은 **R8 Loop 11 — 플랫폼·콘텐츠·SW·보안 가격경로 검증 라운드**다.

이번 R8 Loop 11은 **B2B SaaS, AI cloud/IT서비스, cloud-AI IPO price-fail, Webtoon/IP monetization, AI partnership, game/IP expansion, telecom cybersecurity hard gate, K-pop governance risk**를 같이 본다.

```text
round = R8 Loop 11
round_id = round_179
large_sector = PLATFORM_CONTENT_SW_SECURITY
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true
```

이번에도 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉 OHLC 전체 구간은 안정적으로 확보하지 못했다. 대신 Reuters / Barron’s / FT / WSJ / AP가 제공한 **가격 anchor, 이벤트 수익률, IPO 가격, 투자금액, 사용자·매출·보안사고·법적 리스크 지표**로 계산 가능한 값만 계산했다. 30D/90D/180D full OHLC가 없는 항목은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R8 = 플랫폼·콘텐츠·SW·보안
```

R8의 Stage 3는 “AI”, “플랫폼”, “웹툰”, “게임 IP”, “보안 수요”라는 단어가 아니다. **반복매출·paid usage·ARR proxy·bookings·IP monetization·OPM/FCF·운영신뢰·데이터보안**이 실제로 확인되는 순간이다.

---

# 2. 대상 canonical archetype

```text
B2B_SAAS_ERP_WORKFLOW
AI_CLOUD_CAPITAL_ALLOCATION
CLOUD_AI_SOFTWARE_INFRA
WEBTOON_PLATFORM_IP_MONETIZATION
AI_SOFTWARE_PARTNERSHIP_EVENT
GAME_IP_PLATFORM_EXPANSION
GAME_IP_M_AND_A_CONTENT_EXPANSION
SECURITY_OPERATIONAL_TRUST_HARD_4C
KPOP_PLATFORM_CONTENT_IP_GOVERNANCE
PRICE_ONLY_RALLY
EVENT_PREMIUM
EVIDENCE_GOOD_BUT_PRICE_FAILED
```

---

# 3. deep sub-archetype

```text
B2B SaaS:
- Douzone Bizon
- cloud ERP / accounting / tax / compliance
- SME workflow lock-in
- EQT operating improvement
- ARR proxy / churn / OPM / FCF before Green

AI cloud / IT services:
- Samsung SDS
- LG CNS
- enterprise AI / cloud / IT services
- AI infrastructure
- M&A funding
- capital allocation event vs recurring AI revenue

Webtoon / platform IP:
- NAVER / Webtoon Entertainment
- MAU / paid content / ARPU / IP licensing
- Disney collaboration
- post-IPO drawdown
- event spike vs operating leverage

AI partnership:
- Kakao / OpenAI
- KakaoTalk AI integration
- partnership headline vs paid AI usage
- ARPU / ad-commerce monetization before Green

Game IP:
- Krafton
- PUBG / BGMI India
- India tech fund
- ADK acquisition / animation IP expansion
- data-security regulatory risk
- AI-first restructuring risk

Security / operational trust:
- SK Telecom data breach
- USIM leak
- revenue guidance cut
- fine / compensation / governance overhaul

K-pop IP governance:
- HYBE
- BTS global IP
- founder legal risk
- IPO-related investigation
- warrant request / warrant declined
```

---

# 4. 국장 신규 후보 case

## Case A — Douzone Bizon `success_candidate / B2B SaaS ERP`

```text
symbol = 012510
case_type = success_candidate
archetype = B2B_SAAS_ERP_WORKFLOW
```

### stage date

```text
Stage 1:
2024~2025
- B2B SaaS / cloud ERP / SME workflow lock-in 기대
- 세무·회계·컴플라이언스 기반 반복매출 후보

Stage 2:
2025-11-07
- EQT가 더존비즈온 37.6% 지분을 약 $930M에 인수
- 23.2% from chairman, 14.4% from Shinhan affiliates
- cloud ERP / accounting / tax / compliance business 확인
- KFTC / 산업부 승인 필요

Stage 3:
없음
- EQT 거래 자체는 event / strategic validation
- ARR proxy, churn, OPM, FCF conversion, 고객 lock-in 확인 필요

Stage 4B:
PE 투자 발표 후 valuation이 먼저 크게 확장됐으면 후보

Stage 4C:
거래 승인 실패, churn 상승, cloud 전환 margin 훼손, growth 둔화
```

EQT는 더존비즈온 지분 37.6%를 약 9.3억 달러에 인수하기로 했고, 더존비즈온은 중소기업 대상 cloud ERP, 회계, 세무, compliance software를 제공한다. 이 거래는 B2B SaaS business quality를 외부 자본이 검증한 Stage 2지만, Green은 ARR proxy·churn·OPM·FCF가 확인되어야 한다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters transaction evidence

stage3_price:
N/A

EQT_investment:
$930M

stake_acquired:
37.6%

implied_equity_value:
930M / 0.376
= 약 $2.473B

stake_from_chairman:
23.2%

stake_from_Shinhan_affiliates:
14.4%

BPEA_Fund_IX_post_deal_exposure:
5~10% invested after completion

regulatory_approval:
KFTC merger clearance + Ministry licensing required

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

reason:
- Reuters는 transaction evidence를 제공하지만 Douzone raw adjusted OHLC를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq raw OHLC unavailable in this pass.
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = private_equity_software_rerating_candidate
stage_failure_type = stage2_watch_success_not_green
```

---

## Case B — Samsung SDS `success_candidate + 4B-watch / AI capital allocation`

```text
symbol = 018260
case_type = success_candidate + 4B-watch
archetype = AI_CLOUD_CAPITAL_ALLOCATION
```

### stage date

```text
Stage 1:
2025~2026
- enterprise AI transformation
- Samsung group AI infrastructure / IT services 기대

Stage 2:
2026-04-15
- KKR이 Samsung SDS 신규 CB $820M 인수
- AI infra / M&A / global expansion / capital allocation 기대
- existing cash 6.4T won
- KKR six-year advisory role

Stage 3:
없음
- CB 투자와 AI 투자계획만으로 Green 금지
- recurring cloud revenue, paid AI transformation revenue, margin, FCF 확인 필요

Stage 4B:
2026-04-15
- 장중 +20.8%
- 오전 +19.4%
- KOSPI +3.0%
- AI revenue보다 가격이 먼저 움직임

Stage 4C:
CB dilution, AI capex 대비 매출 부진, M&A 실패, stablecoin regulatory risk
```

KKR은 삼성SDS 신규 전환사채 8.2억 달러를 인수하기로 했고, 삼성SDS 주가는 장중 최대 20.8% 상승했다. 삼성SDS는 기존 현금 6.4조 원과 KKR 자금을 활용해 AI infrastructure, physical AI, stablecoin, M&A를 추진하겠다고 밝혔지만, recurring AI revenue와 FCF가 확인되기 전에는 Stage 3가 아니다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event return anchor

stage3_price:
N/A

stage2_event_MFE_1D:
+20.8%

morning_trade_return:
+19.4%

KOSPI_same_context_return:
+3.0%

relative_intraday_outperformance_vs_KOSPI:
20.8 - 3.0
= +17.8pp

CB_investment:
$820M

KRW_equivalent_at_Reuters_FX:
820M * 1,472
= 약 1.207T won

Samsung_SDS_existing_cash:
6.4T won

combined_cash_plus_CB:
6.4T + 1.207T
= 약 7.607T won

KKR_advisory_period:
6 years

MFE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
success
- recurring AI revenue 확인 전 +20.8%는 명확한 4B/event premium.
```

### alignment

```text
score_price_alignment = event_premium + success_candidate
rerating_result = AI_cloud_capital_allocation_watch
stage_failure_type = should_not_be_green_yet
```

---

## Case C — LG CNS `evidence_good_but_price_failed / AI-cloud IPO`

```text
symbol = LG CNS
case_type = evidence_good_but_price_failed
archetype = CLOUD_AI_SOFTWARE_INFRA
```

### stage date

```text
Stage 1:
2024~2025
- cloud / AI services provider IPO
- enterprise digital transformation 기대

Stage 2:
2025-02-05
- IPO price 61,900원
- opening price 60,500원
- debut trade 59,700원
- IPO proceeds 1.2T won
- 1Q~3Q 2024 cloud and AI services = 54% of sales
- 1Q~3Q 2024 revenue about 4T won, OP 313B won

Stage 3:
없음
- IPO와 cloud/AI 매출비중만으로 Green 금지
- recurring cloud revenue, retention, margin, FCF 확인 필요

Stage 4B:
IPO valuation이 AI/cloud narrative를 먼저 반영한 구간

Stage 4C:
IPO 후 가격 부진, M&A 실패, debt burden, AI growth 둔화
```

LG CNS는 cloud/AI services가 2024년 1~3분기 매출의 54%를 차지했고, 같은 기간 매출 약 4조 원, 영업이익 3,130억 원을 기록했다. 하지만 상장 첫날 공모가 61,900원 대비 59,700원으로 거래되어 -3.55%를 보였고, 이는 `evidence_good_but_price_failed`다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters IPO price anchor

stage3_price:
N/A

IPO_price:
61,900원

opening_price:
60,500원

opening_return_vs_IPO:
60,500 / 61,900 - 1
= -2.26%

debut_trade_price:
59,700원

debut_MAE:
59,700 / 61,900 - 1
= -3.55%

IPO_proceeds:
1.2T won

market_value_morning:
5.79T won

cloud_AI_sales_mix:
54% of sales in first three quarters of 2024

1Q_3Q_2024_revenue:
about 4T won

1Q_3Q_2024_OP:
313B won

OP_margin_1Q_3Q_2024:
313B / 4T
= 약 7.8%

MFE_30D / 90D:
price_data_unavailable_after_deep_search

score-price read:
사업 evidence는 있었지만 IPO price action은 바로 실패.
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed
rerating_result = IPO_cloud_AI_watch
stage_failure_type = stage2_not_green
```

---

## Case D — NAVER / Webtoon `success_candidate + event premium / IP monetization`

```text
symbol = 035420 / WBTN exposure
case_type = success_candidate + event_premium_watch
archetype = WEBTOON_PLATFORM_IP_MONETIZATION
```

### stage date

```text
Stage 1:
2024-06
- Webtoon Entertainment IPO
- Korean content/IP platform monetization 기대

Stage 2:
2024-06-27
- Webtoon IPO price $21
- shares rose as much as 14.3% on Nasdaq debut
- IPO raised $315M
- Naver private placement about $50M
- Naver retains majority exposure

Stage 3:
없음
- MAU와 IPO만으로 Green 금지
- paid content, ARPU, IP licensing, advertising, operating leverage, FCF 확인 필요

Stage 4B:
2024 IPO debut premium

Stage 4B 추가:
2025-08-13
- Disney collaboration / surprise profit
- shares +62% to $15.16 early trading
- revenue $348.3M, +8.5%
- adjusted profit $0.07/share vs expected -$0.14 loss
- but shares had fallen 55% from IPO period before event
```

Webtoon은 Naver의 content/IP platform Stage 2 후보로 유지한다. IPO 가격은 21달러였고, Nasdaq debut에서 장중 24달러까지 올라 +14.3%를 기록했다. 이후 Disney deal과 surprise profit 발표 후에는 주가가 62% 급등했지만, 그 직전까지 IPO 이후 55% 하락해 있었다. 즉 IP monetization 가능성은 있지만, R8 Green은 paid usage·ARPU·IP licensing·operating leverage·FCF가 확인될 때다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / Barron's price and earnings anchors

stage3_price:
N/A

Webtoon_IPO_price:
$21

Webtoon_debut_intraday_high:
$24

debut_MFE_from_IPO:
24 / 21 - 1
= +14.3%

IPO_raise:
$315M

Naver_private_placement:
about $50M

Disney_earnings_event_price:
$15.16 early trading

Disney_earnings_event_MFE:
+62%

pre_Disney_post_IPO_drawdown_context:
-55%

Disney_event_revenue:
$348.3M

Disney_event_revenue_growth:
+8.5% YoY

adjusted_Q2_profit:
$0.07/share

expected_adjusted_result:
-$0.14/share loss

MAU_context:
about 155M monthly active users in Barron's source

MFE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate / event_premium_watch
rerating_result = Webtoon_IP_monetization_watch
stage_failure_type = stage2_watch_success_not_green
```

---

## Case E — Kakao / OpenAI `price_moved_without_evidence`

```text
symbol = 035720
case_type = price_moved_without_evidence
archetype = AI_SOFTWARE_PARTNERSHIP_EVENT
```

### stage date

```text
Stage 1:
2025-02-04
- OpenAI-Kakao partnership
- KakaoTalk AI feature 기대
- Korea AI partnership headline

Stage 2:
약함
- AI product launch, paid usage, ARPU, ad/commerce monetization 확인 전

Stage 3:
없음
- partnership headline만으로 Green 금지

Stage 4B:
2025-02-03~04
- 전날 +9%
- 발표 당일 -2%
- price moved before monetization

Stage 4C:
founder governance/legal risk, platform trust risk, AI monetization failure
```

OpenAI는 Kakao와 한국용 AI products를 공동 개발한다고 발표했다. KakaoTalk은 국내 messaging market에서 압도적 지위를 갖고 있지만, Kakao 주가는 발표 전날 9% 오른 뒤 발표 당일 2% 하락했다. paid AI usage, ARPU, 광고·커머스 monetization이 확인되지 않았으므로 이 case는 Stage 3가 아니라 `price_moved_without_evidence`다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters event return anchor

stage3_price:
N/A

event_MFE_before_announcement:
+9%

event_MAE_following_day:
-2%

two_session_cumulative_return_from_pre_event:
1.09 * 0.98 - 1
= +6.8%

event_fade_from_peak:
+9% headline rally to -2% next-day move
= -11pp swing

KakaoTalk_market_share_context:
97% domestic market share in Reuters source

AI_revenue_confirmed:
false

paid_usage_confirmed:
false

MFE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = price_moved_without_evidence
rerating_result = AI_partnership_event_premium
stage_failure_type = should_have_been_stage1_or_4B_watch
```

---

## Case F — Krafton `success_candidate + game/IP expansion watch`

```text
symbol = 259960
case_type = success_candidate + execution_watch
archetype = GAME_IP_PLATFORM_EXPANSION / GAME_IP_M_AND_A_CONTENT_EXPANSION
```

### stage date

```text
Stage 1:
2024~2025
- PUBG / BGMI cash cow
- India gaming market expansion
- original IP / AI-first company / M&A expansion

Stage 2:
2025-06-24
- Krafton agrees to acquire Japan’s ADK for 75B yen / $516.21M
- ADK has participated in 300+ animations
- IP examples include Doraemon, Yu-Gi-Oh!, Crayon Shin-chan

Stage 2 추가:
2025-12-19
- Krafton / Naver / Mirae Asset India tech fund
- target $666M
- initial pool >$333M
- Krafton has invested >$200M in India
- BGMI 240M+ downloads

Stage 3:
없음
- M&A와 India fund만으로 Green 금지
- bookings, live-service retention, new-IP conversion, India regulation, FCF 확인 필요

Stage 4B:
ADK / India / AI-first narrative가 PUBG cash-flow보다 먼저 valuation화되면 후보

Stage 4C-watch:
BGMI regulatory/data-security risk
Subnautica 2 legal dispute / AI-first restructuring / voluntary resignation risk
```

Krafton은 R8에서 game/IP 확장 Stage 2 후보다. ADK를 750억 엔, 약 5.16억 달러에 인수하며 animation IP·content production capability를 붙였고, Naver·Mirae Asset과 인도 tech fund를 만들어 target 6.66억 달러, initial pool 3.33억 달러 이상으로 시작할 계획이다. BGMI는 2.4억 다운로드를 넘겼지만, 과거 data-security concern으로 temporary ban을 겪은 전력이 있어 India regulation과 data trust를 동시에 봐야 한다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters India fund / ADK acquisition anchors

stage3_price:
N/A

ADK_acquisition_value:
75B yen / $516.21M

ADK_animation_participation:
300+ animations

India_fund_target:
$666M

India_fund_initial_pool:
>$333M

Krafton_prior_India_investment:
>$200M

BGMI_downloads:
>240M

BGMI_risk:
temporary ban in India over data-security concerns

MFE / MAE:
price_data_unavailable_after_deep_search

reason:
- Reuters provides transaction/business metrics but not Krafton adjusted OHLC path.
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = game_IP_platform_expansion_watch
stage_failure_type = stage2_watch_success_not_green
```

---

## Case G — SK Telecom `hard 4C / cybersecurity operational trust break`

```text
symbol = 017670
case_type = 4C-thesis-break
archetype = SECURITY_OPERATIONAL_TRUST_HARD_4C
```

### stage date

```text
Stage 1:
2024~2025
- AI telecom / subscription base stability
- network infrastructure trust

Stage 2:
없음
- cybersecurity breach 이후 positive stage 부여 금지

Stage 3:
없음
- 데이터 신뢰 회복, 보상비용 정리, revenue guidance 회복 전 Green 금지

Stage 4C:
2025-04-28
- customer data leak due to cyberattack
- shares intraday -8.5%
- close -6.7%
- KOSPI +0.1%
- 23M users offered free USIM replacement

Stage 4C 강화:
2025-07-04
- 26.96M pieces of user data leaked
- shares close -5.6%
- 700B won / 5-year security investment
- 2025 revenue forecast cut by 800B won
- customer benefit package cost about 500B won

Stage 4C 강화:
2025-08-28
- PIPC fine about 134B won / $96.53M
```

SK Telecom은 R8의 hard 4C 기준점이다. 2025년 4월 cyberattack으로 고객정보가 유출됐다고 공시한 뒤 주가는 장중 -8.5%, 종가 -6.7% 하락했고 KOSPI는 +0.1%였다. 이후 정부 조사에서는 2,696만 건의 user data leak, 7,000억 원 규모 5년 보안투자, 2025년 매출전망 8,000억 원 하향, 고객보상 package 약 5,000억 원이 확인됐다. 8월에는 개인정보보호위원회가 약 1,340억 원 벌금을 부과했다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters breach / price / fine / revenue-cut anchors

stage3_price:
N/A

2025-04-28_event_intraday_MAE:
-8.5%

2025-04-28_close_MAE:
-6.7%

KOSPI_same_context:
+0.1%

relative_underperformance_close:
-6.7 - 0.1
= -6.8pp

affected_users_initial:
23M subscribers

USIM_replacement_stores:
2,600+

protection_service_signups:
5.54M

signup_share_of_23M:
5.54 / 23
= 24.1%

leaked_user_data_pieces:
26.96M

2025-07-04_close_MAE:
-5.6%

security_investment:
700B won over 5 years

annualized_security_investment:
700B / 5
= 140B won/year

2025_revenue_forecast_cut:
800B won

customer_benefit_package_cost:
about 500B won

PIPC_fine:
134B won / $96.53M

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4C 큰 하락 이전 포착 여부:
hard gate event itself
- breach disclosure day부터 hard 4C.
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = cybersecurity_operational_trust_break
stage_failure_type = hard_4C
```

---

## Case H — HYBE `4C-watch / K-pop IP governance risk`

```text
symbol = 352820
case_type = 4C-watch
archetype = KPOP_PLATFORM_CONTENT_IP_GOVERNANCE
```

### stage date

```text
Stage 1:
2024~2026
- BTS comeback
- Weverse platform / global K-pop IP
- tour revenue 기대

Stage 2:
보류
- IP monetization, tour revenue, paid Weverse usage, OPM 확인 필요

Stage 3:
없음
- legal/governance overhang 해소 전 Green 금지

Stage 4B:
BTS comeback / K-pop IP 기대만으로 가격이 먼저 확장되면 후보

Stage 4C-watch:
2025-07-24
- police raid HYBE offices over IPO/share probe

Stage 4C-watch:
2026-04-21
- police seek detention warrant for HYBE founder Bang Si-hyuk
- alleged illegal trading tied to IPO
- alleged profit about 190B won
- HYBE shares -2.4%, KOSPI +2.7%

4C relief:
2026-04-24
- prosecutors decline arrest warrant request
- hard 4C not confirmed
```

HYBE는 글로벌 K-pop IP와 Weverse platform 기대가 있어도 governance gate가 먼저다. 2025년 7월 경찰이 IPO 관련 share-trading probe로 HYBE 사무실을 압수수색했고, 2026년 4월에는 경찰이 방시혁 의장 구속영장을 신청했다. Reuters는 이 보도 후 HYBE가 2.4% 하락했고 같은 날 KOSPI는 2.7% 상승했다고 전했다. 이후 AP는 검찰이 구속 필요성이 충분하지 않다며 영장 신청을 기각하고 보완수사를 요구했다고 보도했다. 따라서 hard 4C는 아니지만 governance 4C-watch다. ([Reuters][8])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / AP legal event anchors

stage3_price:
N/A

stage4c_event_MAE_1D:
-2.4%

KOSPI_same_context:
+2.7%

relative_underperformance:
-2.4 - 2.7
= -5.1pp

alleged_profit:
190B won / $129.1M

travel_ban_since:
August 2025

hard_4C_status:
not confirmed

4C_relief:
prosecutors declined warrant request

MFE / MAE:
price_data_unavailable_after_deep_search beyond reported event return

Stage 4C 큰 하락 이전 포착 여부:
partial_success
- legal event 당일 4C-watch 가능.
- warrant declined, so hard 4C 보류.
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = governance_legal_overhang
stage_failure_type = should_have_been_red_or_watch
```

---

# 5. 이번 R8 case별 요약표

| case            | 분류                             |                                                  실제 가격검증 | alignment        |
| --------------- | ------------------------------ | -------------------------------------------------------: | ---------------- |
| Douzone Bizon   | success_candidate              |                EQT $930M / 37.6%, implied equity $2.473B | SaaS Stage 2     |
| Samsung SDS     | success_candidate + 4B         |                   KKR CB $820M, +20.8%, relative +17.8pp | AI capital event |
| LG CNS          | evidence_good_but_price_failed |          IPO 61,900 → 59,700, -3.55%; cloud/AI 54% sales | price failed     |
| NAVER / Webtoon | success_candidate + event      |   IPO +14.3%; Disney event +62%; pre-event drawdown -55% | IP event         |
| Kakao / OpenAI  | price_moved_without_evidence   |             +9% then -2%, two-session +6.8%, -11pp swing | price-only       |
| Krafton         | success_candidate              |         ADK $516M, India fund $666M, BGMI 240M downloads | game/IP Stage 2  |
| SK Telecom      | hard 4C                        | -8.5% intraday, -6.7% close; revenue cut 800B; fine 134B | security hard 4C |
| HYBE            | 4C-watch                       |             -2.4% vs KOSPI +2.7%; warrant declined later | governance watch |

---

# 6. score-price alignment 판정

```text
success_candidate:
- Douzone Bizon
- NAVER / Webtoon
- Krafton

event_premium + success_candidate:
- Samsung SDS
- NAVER / Webtoon Disney event

evidence_good_but_price_failed:
- LG CNS

price_moved_without_evidence:
- Kakao / OpenAI partnership

thesis_break:
- SK Telecom cybersecurity breach

thesis_break_watch:
- HYBE founder legal/governance risk

4B-watch:
- Samsung SDS +20.8%
- Webtoon IPO / Disney-event spikes
- Kakao OpenAI partnership +9% then -2%
- Krafton ADK / India fund / AI-first narrative if price outruns bookings
- HYBE BTS comeback/IP expectation with governance overhang

hard_4C:
- SK Telecom security/privacy operational trust break
```

---

# 7. 점수비중 교정

## 올릴 축

```text
recurring_revenue +5
ARR_proxy +5
paid_usage_conversion +5
bookings_repeatability +4
enterprise_contract_quality +4
OPM_improvement +5
FCF_conversion +5
customer_retention_or_churn +4
IP_monetization_beyond_launch +4
operational_trust +5
security_privacy_trust +5
data_governance +5
```

### 왜 올리나

Douzone은 SME workflow lock-in과 B2B SaaS 반복매출 후보이고, Krafton은 PUBG/BGMI cash cow와 ADK·India expansion이 있다. Webtoon은 IP monetization 가능성이 있다. 하지만 세 case 모두 Stage 3는 **반복매출·bookings·paid usage·OPM/FCF**가 확인되어야 한다. SK Telecom은 보안 신뢰가 깨지면 매출전망·보상비용·벌금으로 직접 내려온다는 hard 4C 기준이다.

## 내릴 축

```text
AI_feature_only -5
partnership_headline_only -5
MAU_without_ARPU -4
IPO_debut_premium -5
M&A_without_integration -4
AI_capex_without_revenue -5
game_downloads_without_bookings -4
single_IP_dependence -4
founder_legal_risk -5
privacy_security_trust_break -5
data_breach_revenue_cut -5
```

### 왜 내리나

Samsung SDS는 AI/M&A 자본배분 기대만으로 장중 20.8% 올랐다. Kakao는 OpenAI 제휴 전후로 +9% 뒤 -2%를 보였다. LG CNS는 cloud/AI 비중이 높았지만 IPO 첫날 가격이 실패했다. SK Telecom은 보안사고가 실제 매출전망 하향, 보상비용, 투자비, 벌금으로 연결됐다.

## Green gate 강화 조건

```text
R8 Stage 3-Green 필수:
1. 반복매출 또는 bookings 확인
2. ARPU / paid usage / ARR proxy 확인
3. OPM 또는 gross margin 개선
4. FCF conversion
5. 고객 retention / churn 안정
6. IP monetization이 단발 launch를 넘어 반복화
7. AI 기능이 실제 유료 매출 또는 비용절감으로 연결
8. privacy / security / governance hard risk 통과
9. 가격경로가 evidence 이후 따라옴

금지:
AI partnership headline
AI infra 투자계획만 있음
MAU만 있음
IPO/debut premium만 있음
M&A announcement만 있음
download count만 있음
founder legal risk 존재
security/privacy incident 존재
```

## 4B 조기감지 조건

```text
4B-watch:
AI partnership 발표 직후 급등
AI infra / KKR / M&A 기대만으로 +20%급 상승
IPO debut premium
Webtoon/IP valuation이 monetization보다 먼저 확장
게임 다운로드 수가 bookings보다 먼저 valuation을 설명
BTS/K-pop comeback 기대가 governance risk를 덮음
single-IP developer가 M&A/AI-first narrative로 premium을 받음

4B-elevated:
ARR growth 둔화
AI capex 증가로 margin 훼손
M&A integration cost 확대
single-IP 의존
governance/legal overhang 재점화
good news에도 주가 반응 둔화 또는 하락
post-IPO drawdown 후 event spike 반복
```

## 4C hard gate 조건

```text
privacy breach
security outage
data leak with compensation/revenue cut
founder / major shareholder legal break
regulatory sanction
AI product monetization failure
ARR churn spike
paid user decline
game launch failure
IP litigation
M&A integration failure
single-IP collapse
advertising / commerce take-rate damage
FCF deterioration from AI capex
```

이번 R8 Loop 11에서 **SK Telecom은 hard 4C**로 확정한다. HYBE는 hard 4C가 아니라 governance 4C-watch다. Samsung SDS와 Kakao/OpenAI는 4B/Event Premium이다.

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

---

# 9. patch-ready 출력

## docs/round/round_179.md 요약

```md
# R8 Loop 11. Platform / Content / Software / Security Price Validation

이번 라운드는 R8 Loop 11 price-validation 라운드다.

핵심 결론:
- Douzone Bizon is B2B SaaS Stage 2 candidate. EQT invests $930M for 37.6%, implying about $2.473B equity value. ARR, churn, OPM and FCF required before Green.
- Samsung SDS is Stage 2 + 4B-watch. KKR $820M CB and AI capital allocation drove +20.8%, relative +17.8pp vs KOSPI. Recurring AI revenue and FCF required before Green.
- LG CNS is evidence_good_but_price_failed. IPO price 61,900 won, opening 60,500, debut trade 59,700, -3.55%, despite cloud/AI services being 54% of sales in first three quarters of 2024.
- NAVER/Webtoon is Stage 2 IP platform candidate. Webtoon IPO $21 to $24, +14.3%. Disney/earnings event later drove +62%, but prior post-IPO drawdown was -55%. Paid usage, ARPU, IP licensing, FCF required.
- Kakao/OpenAI partnership is price_moved_without_evidence. Kakao rose +9% before the announcement and fell -2% on the day; monetization was not yet proven.
- Krafton is game/IP expansion Stage 2. ADK acquisition $516M, India tech fund $666M, BGMI >240M downloads. Bookings, live-service retention, new-IP conversion and India regulation must confirm.
- SK Telecom data breach is hard 4C. Shares fell -8.5% intraday and -6.7% close; later reports showed 26.96M leaked data pieces, 700B won security investment, 800B won revenue forecast cut, and 134B won fine.
- HYBE is governance/legal 4C-watch. Police sought detention warrant for founder Bang Si-hyuk; shares fell -2.4% versus KOSPI +2.7%, but prosecutors later declined the warrant request, so hard 4C not confirmed.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 179 R8 Loop 11 Platform Content SW Security Price Validation

## 반영 내용
- R8 Loop 11 price-validation 라운드를 추가했다.
- B2B SaaS, AI cloud capital allocation, cloud/AI IPO, Webtoon/IP platform, AI partnership, game/IP expansion, cybersecurity breach, K-pop governance risk를 비교했다.
- Reuters/Barron’s/FT/WSJ/AP anchors로 가능한 MFE/MAE 및 transaction/operational metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- recurring revenue, ARR proxy, paid usage, bookings repeatability, OPM/FCF, security/privacy trust, data governance 가중치 강화
- AI partnership headline, IPO/debut premium, M&A/capital allocation without revenue, downloads without bookings, founder legal risk, data breach 감점 강화
- R8 4B-watch와 security/privacy hard 4C 강화
```

## case row 초안

```jsonl
{"case_id":"r8_loop11_douzone_bizon_eqt_saas","symbol":"012510","company_name":"Douzone Bizon","case_type":"success_candidate","primary_archetype":"B2B_SAAS_ERP_WORKFLOW","stage2_date":"2025-11-07","price_validation":{"price_data_source":"Reuters transaction evidence","stage3_price":null,"eqt_investment_usd_mn":930,"stake_acquired_pct":37.6,"implied_equity_value_usd_bn":2.473,"stake_from_chairman_pct":23.2,"stake_from_shinhan_affiliates_pct":14.4,"bpea_fund_ix_post_deal_exposure_pct":"5-10","regulatory_approval_required":["KFTC","Ministry of Trade, Industry and Resources"],"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"private_equity_software_rerating_candidate","notes":"EQT investment is Stage 2; ARR, churn, OPM and FCF conversion required before Green."}
{"case_id":"r8_loop11_samsung_sds_kkr_ai_4b","symbol":"018260","company_name":"Samsung SDS","case_type":"success_candidate","primary_archetype":"AI_CLOUD_CAPITAL_ALLOCATION","stage2_date":"2026-04-15","stage4b_date":"2026-04-15","price_validation":{"price_data_source":"Reuters reported event return anchor","stage3_price":null,"stage2_event_mfe_1d_pct":20.8,"morning_trade_return_pct":19.4,"kospi_same_context_pct":3.0,"relative_intraday_outperformance_pp":17.8,"cb_investment_usd_mn":820,"cb_investment_krw_trn":1.207,"existing_cash_krw_trn":6.4,"combined_cash_plus_cb_krw_trn":7.607,"kkr_advisory_period_years":6,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"AI_cloud_capital_allocation_watch","notes":"KKR/AI capital allocation is Stage 2 and 4B-watch; recurring AI revenue and FCF required for Green."}
{"case_id":"r8_loop11_lg_cns_ai_cloud_ipo_price_failed","symbol":"LG_CNS","company_name":"LG CNS","case_type":"evidence_good_but_price_failed","primary_archetype":"CLOUD_AI_SOFTWARE_INFRA","stage2_date":"2025-02-05","price_validation":{"price_data_source":"Reuters IPO price anchor","stage3_price":null,"ipo_price":61900,"opening_price":60500,"opening_return_vs_ipo_pct":-2.26,"debut_trade_price":59700,"debut_mae_pct":-3.55,"ipo_proceeds_krw_trn":1.2,"morning_market_value_krw_trn":5.79,"cloud_ai_sales_mix_pct":54,"revenue_1q_3q_2024_krw_trn":4.0,"op_1q_3q_2024_krw_bn":313,"op_margin_1q_3q_2024_pct":7.8,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"IPO_cloud_AI_watch","notes":"Cloud/AI mix was high but IPO price action failed; Stage 3 requires recurring revenue, retention, margin and FCF."}
{"case_id":"r8_loop11_naver_webtoon_ip_platform","symbol":"035420/WBTN","company_name":"NAVER/Webtoon","case_type":"success_candidate","primary_archetype":"WEBTOON_PLATFORM_IP_MONETIZATION","stage2_date":"2024-06-27","stage4b_date":"2025-08-13","price_validation":{"price_data_source":"Reuters/Barron's price and event anchors","stage3_price":null,"webtoon_ipo_price_usd":21,"webtoon_debut_intraday_high_usd":24,"debut_mfe_from_ipo_pct":14.3,"ipo_raise_usd_mn":315,"naver_private_placement_usd_mn":50,"disney_event_price_usd":15.16,"disney_event_mfe_pct":62,"pre_disney_post_ipo_drawdown_context_pct":-55,"disney_event_revenue_usd_mn":348.3,"disney_event_revenue_growth_pct":8.5,"adjusted_q2_profit_per_share_usd":0.07,"expected_adjusted_loss_per_share_usd":-0.14,"mau_context_mn":155,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_event_premium_watch","rerating_result":"Webtoon_IP_monetization_watch","notes":"MAU/IP platform is Stage 2; paid usage, ARPU, IP licensing, operating leverage and FCF required before Green."}
{"case_id":"r8_loop11_kakao_openai_partnership_price_only","symbol":"035720","company_name":"Kakao","case_type":"overheat","primary_archetype":"AI_SOFTWARE_PARTNERSHIP_EVENT","stage1_date":"2025-02-04","stage4b_date":"2025-02-04","price_validation":{"price_data_source":"Reuters event return anchor","stage3_price":null,"event_mfe_before_announcement_pct":9.0,"event_mae_following_day_pct":-2.0,"two_session_cumulative_return_pct":6.8,"event_fade_from_peak_pp":-11.0,"kakaotalk_domestic_market_share_pct":97,"ai_revenue_confirmed":false,"paid_usage_confirmed":false,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"AI_partnership_event_premium","notes":"OpenAI partnership is Stage 1/2; paid AI usage, ARPU and margin required for Green."}
{"case_id":"r8_loop11_krafton_game_ip_india_adk_watch","symbol":"259960","company_name":"Krafton","case_type":"success_candidate","primary_archetype":"GAME_IP_PLATFORM_EXPANSION","stage2_date":"2025-06-24/2025-12-19","price_validation":{"price_data_source":"Reuters India fund / ADK acquisition anchors","stage3_price":null,"adk_acquisition_value_yen_bn":75,"adk_acquisition_value_usd_mn":516.21,"adk_animation_participation_count":300,"india_fund_target_usd_mn":666,"india_fund_initial_pool_usd_mn":333,"krafton_prior_india_investment_usd_mn":200,"bgmi_downloads_mn":240,"bgmi_risk":"temporary ban in India over data-security concerns","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"game_IP_platform_expansion_watch","notes":"ADK and India expansion are Stage 2; bookings, retention, IP conversion, regulation and FCF required before Green."}
{"case_id":"r8_loop11_skt_cybersecurity_operational_trust_hard_4c","symbol":"017670","company_name":"SK Telecom","case_type":"4c_thesis_break","primary_archetype":"SECURITY_OPERATIONAL_TRUST_HARD_4C","stage4c_date":"2025-04-28/2025-07-04/2025-08-28","price_validation":{"price_data_source":"Reuters breach/price/fine/revenue-cut anchors","stage3_price":null,"event_intraday_mae_pct":-8.5,"event_close_mae_pct":-6.7,"kospi_same_context_pct":0.1,"relative_underperformance_close_pp":-6.8,"affected_users_initial_mn":23,"usim_replacement_stores":2600,"protection_service_signups_mn":5.54,"signup_share_pct":24.1,"leaked_user_data_pieces_mn":26.96,"july4_close_mae_pct":-5.6,"security_investment_krw_bn":700,"annualized_security_investment_krw_bn":140,"revenue_forecast_cut_2025_krw_bn":800,"customer_benefit_package_cost_krw_bn":500,"pipc_fine_krw_bn":134,"pipc_fine_usd_mn":96.53,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"cybersecurity_operational_trust_break","notes":"Data breach caused price drop, revenue cut, security investment and fine; hard 4C."}
{"case_id":"r8_loop11_hybe_founder_legal_governance_watch","symbol":"352820","company_name":"HYBE","case_type":"4c_watch","primary_archetype":"KPOP_PLATFORM_CONTENT_IP_GOVERNANCE","stage4c_date":"2025-07-24/2026-04-21","price_validation":{"price_data_source":"Reuters/AP legal event anchors","stage3_price":null,"event_mae_1d_pct":-2.4,"kospi_same_context_pct":2.7,"relative_underperformance_pp":-5.1,"alleged_profit_krw_bn":190,"travel_ban_since":"2025-08","hard_4c_status":"not_confirmed_warrant_declined","legal_relief_date":"2026-04-24","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"governance_legal_overhang","notes":"Legal/governance risk blocks Green; warrant declined, so hard 4C not confirmed."}
```

## shadow weight row 초안

```csv
archetype,recurring_revenue,arr_proxy,paid_usage,bookings,enterprise_contract,opm_fcf,ip_monetization,operational_trust,security_privacy_trust,data_governance,event_penalty,legal_privacy_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
B2B_SAAS_ERP_WORKFLOW,+5,+5,+3,+3,+5,+5,+0,+3,+2,+3,-2,+1,+3,+3,Douzone/EQT is Stage 2 until ARR/churn/OPM/FCF confirm.
AI_CLOUD_CAPITAL_ALLOCATION,+3,+3,+3,+2,+4,+5,+0,+3,+2,+3,-5,+2,+5,+3,Samsung SDS KKR event is 4B-watch before AI revenue conversion.
CLOUD_AI_SOFTWARE_INFRA,+4,+4,+3,+2,+4,+5,+0,+3,+2,+3,-4,+2,+4,+3,LG CNS IPO weak price action blocks Green despite cloud/AI mix.
WEBTOON_PLATFORM_IP_MONETIZATION,+3,+3,+5,+4,+2,+5,+5,+3,+2,+2,-3,+2,+5,+4,Webtoon needs paid usage, ARPU, IP monetization and FCF beyond MAU/IPO.
AI_SOFTWARE_PARTNERSHIP_EVENT,+2,+2,+5,+2,+2,+4,+0,+3,+2,+2,-5,+2,+5,+3,Kakao/OpenAI partnership is price_moved_without_evidence until monetization.
GAME_IP_PLATFORM_EXPANSION,+3,+0,+3,+5,+0,+5,+5,+3,+3,+3,-4,+4,+4,+4,Krafton needs bookings/IP conversion and India regulation clearance beyond downloads/M&A.
SECURITY_OPERATIONAL_TRUST_HARD_4C,+0,+0,+0,+0,+0,+0,+0,+5,+5,+5,0,+5,+4,+5,SK Telecom breach is hard 4C with revenue/fine/compensation impact.
KPOP_PLATFORM_CONTENT_IP_GOVERNANCE,+2,+1,+3,+4,+0,+4,+5,+5,+2,+2,-3,+5,+4,+5,HYBE legal risk is 4C-watch; hard 4C only after legal outcome materially impairs business.
```

---

# 이번 R8 Loop 11 결론

R8은 **AI·플랫폼·콘텐츠·보안이 모두 “좋아 보이기 쉬운” 섹터**다. 그래서 Green은 느리게 주고, 4B와 4C는 빨리 붙여야 한다.

```text
1. Douzone Bizon은 B2B SaaS Stage 2다.
   하지만 ARR, churn, OPM, FCF 전 Stage 3는 아니다.

2. Samsung SDS는 AI capital allocation Stage 2와 4B가 동시에 떴다.
   KKR/AI/M&A 기대 +20.8%는 revenue 전 가격 선반영이다.

3. LG CNS는 cloud/AI 비중이 높았지만 IPO price action이 실패했다.
   evidence_good_but_price_failed다.

4. NAVER/Webtoon은 IP platform Stage 2다.
   Disney event +62%는 좋지만, post-IPO -55% drawdown이 있었고, paid usage·ARPU·FCF 전 Green은 아니다.

5. Kakao/OpenAI는 price_moved_without_evidence다.
   partnership headline 전후로 가격은 움직였지만, paid AI monetization은 없었다.

6. Krafton은 game/IP expansion Stage 2다.
   ADK와 India fund는 좋지만 bookings, retention, regulation, FCF 전 Green은 아니다.

7. SK Telecom은 R8 hard 4C다.
   cybersecurity breach가 주가, 매출전망, 보상비용, 벌금으로 그대로 내려왔다.

8. HYBE는 governance 4C-watch다.
   warrant declined로 hard 4C는 아니지만, IP monetization보다 legal overhang이 먼저다.
```

한 문장으로 압축하면:

> **R8에서 진짜 Stage 3는 “AI·웹툰·게임·SaaS·K-pop이 핫하다”가 아니라, 반복매출·paid usage·bookings·IP monetization·OPM/FCF와 security/privacy trust가 실제로 확인되는 순간이다.**

[1]: https://www.reuters.com/world/asia-pacific/swedish-firm-eqt-shells-out-930-million-slice-south-koreas-douzone-bizon-2025-11-07/?utm_source=chatgpt.com "Swedish firm EQT shells out $930 million for a slice of South Korea's Douzone Bizon"
[2]: https://www.reuters.com/world/asia-pacific/kkr-buy-820-million-samsung-sds-convertible-bonds-shares-jump-20-2026-04-15/?utm_source=chatgpt.com "KKR to buy $820 million of Samsung SDS convertible bonds, shares jump 20%"
[3]: https://www.reuters.com/technology/skorean-tech-services-firm-lg-cns-falls-stock-market-debut-2025-02-05/?utm_source=chatgpt.com "South Korean tech services firm LG CNS drops in market debut"
[4]: https://www.reuters.com/markets/us/webtoons-nasdaq-debut-sees-shares-jump-14-2024-06-27/?utm_source=chatgpt.com "South Korea's Naver-backed Webtoon shares jump about 14% in Nasdaq debut"
[5]: https://www.reuters.com/technology/artificial-intelligence/openai-kakao-jointly-develop-ai-products-south-korea-2025-02-04/?utm_source=chatgpt.com "OpenAI clinches deal with Kakao, talks with SoftBank and Samsung about Stargate"
[6]: https://www.reuters.com/en/south-korean-game-company-krafton-acquire-japans-adk-516-mln-2025-06-24/?utm_source=chatgpt.com "South Korean game company Krafton to acquire Japan's ADK for $516 mln"
[7]: https://www.reuters.com/sustainability/boards-policy-regulation/sk-telecom-shares-plunge-after-data-breach-due-cyberattack-2025-04-28/?utm_source=chatgpt.com "SK Telecom shares plunge after data breach due to cyberattack"
[8]: https://www.reuters.com/business/media-telecom/south-korea-police-raid-offices-k-pop-powerhouse-hybe-over-share-probe-2025-07-24/?utm_source=chatgpt.com "South Korea police raid offices of K-pop powerhouse HYBE over share probe"
