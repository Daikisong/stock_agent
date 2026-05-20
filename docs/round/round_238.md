순서상 이번은 **R8 Loop 10 — 플랫폼·콘텐츠·SW·보안 가격경로 검증 라운드**다.

이번 R8은 **B2B SaaS, AI cloud/IT서비스, IPO price-fail, Webtoon/IP monetization, AI partnership, 게임 IP, telecom cybersecurity trust, K-pop governance risk**를 같이 본다.

```text
round = R8 Loop 10
round_id = round_166
large_sector = PLATFORM_CONTENT_SW_SECURITY
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = false
```

이번 환경에서는 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉 OHLC를 안정적으로 직접 확보하지 못했다. 대신 Reuters / Barron’s / Investopedia / GamesRadar / AP가 제공한 **가격 anchor, 이벤트 수익률, IPO 가격, 거래금액, 매출·사용자·보안사고 지표**로 계산 가능한 값만 계산했다. 원시 OHLC가 없는 구간은 `price_data_unavailable_after_deep_search`로 표시한다.

---

# 1. 이번 라운드 대섹터

```text
R8 = 플랫폼·콘텐츠·SW·보안
```

R8의 Stage 3는 “AI다”, “플랫폼이다”, “IP가 있다”, “웹툰/게임이 흥행했다”가 아니다. **반복매출·paid usage·ARR proxy·bookings·IP monetization·OPM/FCF·운영신뢰가 확인되는 순간**이다.

---

# 2. 대상 canonical archetype

```text
B2B_SAAS_ERP_WORKFLOW
AI_CLOUD_CAPITAL_ALLOCATION
CLOUD_AI_SOFTWARE_INFRA
WEBTOON_PLATFORM_IP_MONETIZATION
AI_SOFTWARE_PARTNERSHIP_EVENT
GAME_IP_REPEAT_MONETIZATION
GAME_IP_IPO_PREMIUM
SECURITY_OPERATIONAL_TRUST_OVERLAY
KPOP_PLATFORM_CONTENT_IP
PLATFORM_GOVERNANCE_LEGAL_RISK
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
- Shift Up
- Stellar Blade / Nikke
- repeat franchise / PC port / sequel
- single-IP dependence
- bookings / royalty / platform expansion before Green

Security / operational trust:
- SK Telecom data breach
- USIM leak
- customer compensation
- revenue guidance cut
- cybersecurity trust hard gate candidate

K-pop IP governance:
- HYBE
- BTS / Weverse / global IP
- founder legal risk
- IPO-related investigation
- warrant request / warrant declined
```

---

# 4. 국장 신규 후보 case

## Case A — 더존비즈온 `success_candidate / B2B SaaS ERP`

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
- cloud ERP / accounting / tax / compliance business 확인
- 장기 운영개선 기대
- KFTC / 산업부 승인 필요

Stage 3:
보류
- EQT 거래 자체는 event premium 성격도 있음
- ARR proxy, churn, OPM, FCF conversion, 고객 lock-in 확인 필요

Stage 4B:
거래 발표 후 valuation이 먼저 크게 확장됐으면 후보

Stage 4C:
거래 승인 실패, churn 상승, cloud 전환 margin 훼손, growth 둔화 시 후보
```

EQT는 더존비즈온 지분 37.6%를 약 9.3억 달러에 인수하기로 했다. 더존비즈온은 중소기업 대상 cloud ERP, 회계, 세무, compliance software를 제공하고, EQT는 장기 운영개선과 핵심 사업 강화를 추진한다고 밝혔다. 이 거래는 공정위 승인과 산업통상자원부 인허가가 필요하다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters transaction evidence anchor

stage3_price:
N/A

stage2_price:
price_data_unavailable_after_deep_search
- Reuters는 더존비즈온 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

EQT_investment:
$930M

stake_acquired:
37.6%

implied_equity_value:
930M / 0.376
= 약 $2.473B

BPEA Fund IX post-deal exposure:
5~10% invested after completion

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = private_equity_software_rerating_candidate
stage_failure_type = stage2_watch_success
```

---

## Case B — 삼성SDS `success_candidate + 4B-watch / AI capital allocation`

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
- 장중 +20.8%

Stage 3:
없음
- CB 투자와 AI 투자계획만으로 Green 금지
- enterprise AI 계약, recurring cloud revenue, AI transformation revenue, margin, FCF 확인 필요

Stage 4B:
2026-04-15
- 발표 당일 장중 +20.8%
- AI + KKR + value-up 기대가 가격에 먼저 반영

Stage 4C:
CB dilution, AI capex 대비 매출 부진, M&A 실패, stablecoin regulatory risk 시 후보
```

KKR은 삼성SDS가 신규 발행하는 8.2억 달러 규모 전환사채를 인수하기로 했고, 삼성SDS 주가는 장중 최대 20.8% 상승했다. KKR은 M&A, 자본배분, full-stack AI solutions 확장에 자문하기로 했고, 삼성SDS는 기존 현금 6.4조 원과 KKR 자금을 활용해 AI infrastructure, physical AI, stablecoin 등 신사업을 추진하겠다고 밝혔다. ([Reuters][2])

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

KRW_equivalent_at_Reuters_FX_approx:
820M * 1,472
= 약 1.207T won

Samsung_SDS_existing_cash:
6.4T won

combined_cash_plus_CB:
6.4T + 1.207T
= 약 7.607T won

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
success
- AI revenue 확인 전 장중 +20.8%는 명확한 4B/event premium.
```

### alignment

```text
score_price_alignment = event_premium + success_candidate
rerating_result = AI_cloud_capital_allocation_watch
stage_failure_type = should_not_be_green_yet
```

---

## Case C — LG CNS `evidence_good_but_price_failed / AI cloud IPO`

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
- IPO
- IPO proceeds 1.2조 원
- IPO price 61,900원
- opening price 60,500원
- debut trading price 59,700원
- cloud and AI services가 2024년 1~3분기 매출의 절반 이상

Stage 3:
없음
- IPO와 AI/cloud 매출비중만으로 Green 금지
- recurring cloud revenue, customer retention, margin, FCF 확인 필요

Stage 4B:
IPO valuation이 AI/cloud narrative를 먼저 반영한 구간

Stage 4C:
IPO 후 가격 부진, M&A 실패, debt burden, AI growth 둔화 시 후보
```

LG CNS는 상장 첫날 공모가 61,900원 대비 59,700원으로 하락했다. IPO는 1.2조 원을 조달했고, 회사는 AI 관련 M&A, 부채상환, 설비투자에 자금을 쓸 계획이었다. Reuters는 cloud and AI services가 2024년 1~3분기 매출의 절반 이상을 차지했다고 전했다. 좋은 AI/cloud 설명이 있었지만 가격은 데뷔 당일 바로 실패했다. ([Reuters][3])

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
(60,500 / 61,900) - 1
= -2.26%

debut_trade_price:
59,700원

debut_MAE:
(59,700 / 61,900) - 1
= -3.55%

IPO_proceeds:
1.2T won

morning_market_value:
5.79T won

cloud_AI_sales_mix:
more than half of sales in first three quarters of 2024

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

score-price read:
AI/cloud evidence existed, but IPO price action failed immediately.
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed
rerating_result = IPO_cloud_AI_watch
stage_failure_type = stage2_not_green
```

---

## Case D — NAVER / Webtoon `success_candidate + event premium watch`

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
- mobile-native global comics platform

Stage 3:
없음
- MAU와 IPO만으로 Green 금지
- paid content, ARPU, IP licensing, advertising, operating leverage, FCF 확인 필요

Stage 4B:
2024 IPO debut premium
2025 Disney collaboration / earnings spike

Stage 4C:
post-IPO drawdown, loss persistence, paid user stagnation, IP monetization failure 시 후보
```

Webtoon Entertainment는 Naver가 지배하는 온라인 comics platform으로, IPO 가격은 주당 21달러였고, Nasdaq 데뷔에서 장중 14.3%까지 상승했다. 회사는 IPO에서 3.15억 달러를 조달했고, Naver에는 같은 가격으로 약 5,000만 달러 규모 private placement가 이뤄졌다. 이건 좋은 Stage 2 evidence지만, Stage 3는 paid usage·ARPU·IP licensing·FCF 확인 뒤다. ([Reuters][4])

2025년에는 Disney 협업과 실적 발표 후 Webtoon 주가가 큰 폭으로 튀었다. Barron’s는 Webtoon이 Disney deal과 surprise profit을 발표하면서 장 초반 62% 오른 15.16달러까지 갔다고 보도했고, 동시에 IPO 이후 전날까지 주가가 55% 하락해 있었다고 설명했다. 이것은 IP monetization 가능성과 동시에 post-IPO volatility / 4B-watch를 보여준다. ([배런스][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / Investopedia / Barron's reported price and financial anchors

stage3_price:
N/A

Webtoon_IPO_price:
$21

Webtoon_debut_intraday_high:
$24

debut_MFE_from_IPO:
(24 / 21) - 1
= +14.3%

Webtoon_first_day_close:
$23.00

first_day_close_return:
(23 / 21) - 1
= +9.5%

next_day_intraday_high:
$25.66

MFE_from_IPO_to_next_day_high:
(25.66 / 21) - 1
= +22.2%

Disney_earnings_event_price:
$15.16 early trading

Disney_earnings_event_MFE:
+62%

pre-Disney post-IPO_drawdown_context:
-55% from IPO period

Disney_event_revenue:
$348.3M

Disney_event_revenue_growth:
+8.5% YoY

adjusted_Q2_profit:
$0.07/share vs expected -$0.14/share loss

MAU_context:
about 155M monthly active users, per Barron's

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate / event_premium_watch
rerating_result = Webtoon_IP_monetization_watch
stage_failure_type = stage2_watch_success
```

---

## Case E — 카카오 / OpenAI `price_moved_without_evidence`

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
보류
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
founder governance/legal risk, platform trust risk, AI monetization failure 시 후보
```

OpenAI는 카카오와 한국용 AI product를 공동 개발한다고 발표했다. KakaoTalk 제품 개선 가능성은 Stage 1~2 event가 될 수 있지만, Reuters는 카카오 주가가 발표 전 9% 급등한 뒤 발표 당일 2% 하락했다고 보도했다. 즉 paid AI usage, ARPU, 광고·커머스 monetization이 확인되기 전 가격이 먼저 움직였다. ([Reuters][6])

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

AI_revenue_confirmed:
false

paid_usage_confirmed:
false

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = price_moved_without_evidence
rerating_result = AI_partnership_event_premium
stage_failure_type = should_have_been_stage1_or_4B_watch
```

---

## Case F — Shift Up `success_candidate / game IP repeat monetization`

```text
symbol = 462870
case_type = success_candidate + IPO_watch
archetype = GAME_IP_REPEAT_MONETIZATION / GAME_IP_IPO_PREMIUM
```

### stage date

```text
Stage 1:
2024-04
- Stellar Blade launch success
- Goddess of Victory: Nikke recurring mobile game revenue
- Sony second-party developer narrative

Stage 2:
2024-06~07
- IPO priced near/top band
- raised about 435B won
- market valuation about 3.5T won
- Tencent ownership after IPO about 35%
- 2023 revenue 169B won, OP 111B won

추가 Stage 2:
2025-06
- Stellar Blade PC version sold >1M copies in 3 days
- total sales >3M units
- sequel / Project Spirits pipeline

Stage 3:
보류
- IPO와 launch success만으로 Green 금지
- repeat bookings, royalty/revenue recognition, platform expansion, IP pipeline conversion, OPM/FCF 확인 필요

Stage 4B:
IPO/debut premium, single-IP hype, sequel 기대가 가격에 먼저 반영되면 후보

Stage 4C:
Stellar Blade sequel delay, Nikke revenue normalization, PC launch fade, Tencent/platform risk, single-IP dependence 시 후보
```

Reuters는 Shift Up이 IPO를 top end에서 가격 책정할 경우 4,350억 원을 조달하고 valuation이 3.5조 원이 될 수 있다고 보도했다. 2023년 매출은 1,690억 원, 영업이익은 1,110억 원이었고, 모바일 게임 Goddess of Victory: Nikke는 2022년 말부터 2024년 1분기까지 2,550억 원을 벌어들인 것으로 보도됐다. ([Reuters][7])

Stellar Blade는 PC 출시 후 3일 만에 100만 장 이상 팔렸고, PS5와 PC 합산 300만 장 이상 판매된 것으로 보도됐다. Shift Up은 Stellar Blade sequel과 Project Spirits pipeline을 갖고 있지만, R8 Stage 3는 단순 launch success가 아니라 repeat bookings·royalty/revenue recognition·IP pipeline conversion·FCF가 필요하다. ([GamesRadar+][8])

### 실제 가격경로 검증

```text
price_data_source:
Reuters IPO anchor + GamesRadar sales/pipeline anchor

stage3_price:
N/A

stock_OHLC:
price_data_unavailable_after_deep_search
- Reuters는 IPO valuation과 financial anchor는 제공하지만 listing-day OHLC anchor는 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 일봉 OHLC 직접 확보 실패.

IPO_raise:
435B won

IPO_valuation:
3.5T won

Tencent_post_IPO_stake:
about 35%

Tencent_pre_IPO_stake:
about 40%

stake_change:
35 - 40
= -5pp

2023_revenue:
169B won

2023_operating_profit:
111B won

2023_OP_margin:
111 / 169
= 65.7%

Nikke_revenue_late_2022_to_1Q2024:
255B won

Stellar_Blade_PC_sales_3D:
>1M copies

Stellar_Blade_total_sales_mid_2025:
>3M copies

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = game_IP_repeat_monetization_watch
stage_failure_type = stage2_watch_success
```

---

## Case G — SK텔레콤 `strong 4C-watch / cybersecurity operational trust`

```text
symbol = 017670
case_type = 4C-watch / operational_trust_break
archetype = SECURITY_OPERATIONAL_TRUST_OVERLAY
```

### stage date

```text
Stage 1:
2024~2025
- telecom data platform / AI telecom / subscription base stability

Stage 2:
없음
- cybersecurity breach 이후 positive stage 부여 금지

Stage 3:
없음
- 데이터 신뢰 회복, 보상비용 정리, revenue guidance 회복 전 Green 금지

Stage 4C-watch:
2025-04-28
- customer data leak due to cyberattack
- shares intraday -8.5%
- close -6.7%
- 23M users offered free USIM replacement

추가 4C-watch:
2025-07-04
- government says negligent
- 26.96M pieces of user data leaked
- 700B won / 5-year security investment
- 2025 revenue forecast cut by 800B won

추가 hard-risk candidate:
2025-08-28
- Personal Information Protection Commission fine about 134B won / $96.5M
```

SK Telecom은 2025년 4월 cyberattack에 따른 고객 데이터 유출을 공개한 뒤 장중 최대 8.5%, 종가 기준 6.7% 하락했다. 회사는 2,300만 명 고객에게 무료 USIM 교체를 제공하기로 했고, 약 554만 명이 보호서비스에 가입했다. 이 사건은 R8에서 보안·개인정보 신뢰가 가격과 비용으로 바로 연결되는 4C-watch다. ([Reuters][9])

이후 정부는 SK Telecom이 USIM 데이터 보호 의무를 다하지 못했다고 판단했고, 2,696만 건의 사용자 데이터 유출, 7,000억 원 규모 5년 보안투자, 2025년 매출전망 8,000억 원 하향이 보도됐다. 2025년 8월에는 개인정보보호위원회가 약 1,348억 원 벌금을 부과했다. ([Reuters][10])

### 실제 가격경로 검증

```text
price_data_source:
Reuters breach/price/cost anchors

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
134.8B won / about $96.5M

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4C 큰 하락 이전 포착 여부:
partial_success
- breach 공개 당일 4C-watch 가능.
- revenue cut, fine, security investment까지 나오며 hard 4C에 가까워짐.
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = cybersecurity_operational_trust_break
stage_failure_type = strong_4C_watch
```

---

## Case H — HYBE `4C-watch / K-pop IP governance risk`

```text
symbol = 352820
case_type = 4C-watch
archetype = KPOP_PLATFORM_CONTENT_IP / PLATFORM_GOVERNANCE_LEGAL_RISK
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
2026-04-21
- police seek detention warrant for HYBE founder Bang Si-hyuk
- alleged illegal trading tied to IPO
- alleged profit about 190B won
- HYBE shares -2.4%

4C relief:
2026-04-24
- prosecutors decline arrest warrant request
- hard 4C not confirmed
```

한국 경찰은 HYBE 창업자 방시혁에 대해 IPO 관련 자본시장법 위반 혐의로 구속영장을 신청했고, HYBE 주가는 보도 후 2.4% 하락했다. 경찰은 방시혁이 초기 투자자를 오도해 지분을 사모펀드에 팔게 하고, IPO 후 해당 펀드 매각이익의 일부를 받아 약 1,900억 원의 이익을 얻었다고 봤다. 다만 AP는 검찰이 구속 필요성이 충분하지 않다며 경찰의 영장 신청을 기각하고 보완수사를 요청했다고 보도했다. 따라서 hard 4C가 아니라 governance/legal 4C-watch다. ([Reuters][11])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / AP legal event anchors

stage3_price:
N/A

stage4c_event_MAE_1D:
-2.4%

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

below_stage3_price_flag:
N/A

Stage 4C 큰 하락 이전 포착 여부:
partial_success
- legal event 당일 4C-watch 가능.
- warrant declined, so hard 4C는 보류.
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = governance_legal_overhang
stage_failure_type = should_have_been_red_or_watch
```

---

# 5. 이번 R8 case별 요약표

| case          | 분류                             |                                                           실제 가격검증 | alignment            |
| ------------- | ------------------------------ | ----------------------------------------------------------------: | -------------------- |
| 더존비즈온         | success_candidate              |                          EQT $930M / 37.6%, implied value $2.473B | success_candidate    |
| 삼성SDS         | success_candidate + 4B         |                            KKR CB $820M, +20.8%, relative +17.8pp | event_premium        |
| LG CNS        | evidence_good_but_price_failed |                IPO 61,900 → 59,700, -3.55%; cloud/AI > half sales | price failed         |
| NAVER/Webtoon | success_candidate + event      |   WBTN $21→$25.66, +22.2%; Disney event +62%; prior drawdown -55% | event watch          |
| 카카오/OpenAI    | price_moved_without_evidence   |                         +9% 후 -2%, two-session +6.8%, swing -11pp | price-only           |
| Shift Up      | success_candidate              | IPO 435B, valuation 3.5T, 2023 OP margin 65.7%, Stellar Blade >3M | stage2 watch         |
| SK텔레콤         | strong 4C-watch                |        -8.5% intraday, -6.7% close; revenue cut 800B; fine 134.8B | security trust break |
| HYBE          | 4C-watch                       |                                     -2.4%; warrant declined later | governance watch     |

---

# 6. score-price alignment 판정

```text
success_candidate:
- 더존비즈온
- NAVER/Webtoon
- Shift Up

event_premium + success_candidate:
- 삼성SDS
- NAVER/Webtoon Disney / IPO event

evidence_good_but_price_failed:
- LG CNS

price_moved_without_evidence:
- 카카오/OpenAI partnership

thesis_break_watch:
- SK텔레콤 cybersecurity breach
- HYBE founder legal/governance risk

4B-watch:
- 삼성SDS +20.8%
- Webtoon IPO / Disney-event spikes
- 카카오 OpenAI partnership +9% then -2%
- Shift Up IPO / single-IP premium
- HYBE BTS comeback/IP expectation with governance overhang

4C-watch:
- SK텔레콤 security/privacy operational trust
- HYBE governance/legal risk

hard_4C_confirmed:
- false
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
```

### 왜 올리나

더존비즈온은 B2B SaaS 구조와 SME workflow lock-in을 가진 Stage 2 후보다. Shift Up은 Stellar Blade와 Nikke라는 IP monetization 후보를 갖고 있고, Webtoon은 MAU와 IP licensing 가능성이 있다. 하지만 이 셋 모두 Stage 3는 **반복매출·bookings·paid usage·OPM/FCF**가 확인될 때다.

## 내릴 축

```text
AI_feature_only -5
partnership_headline_only -5
MAU_without_ARPU -4
IPO_debut_premium -5
M&A_without_integration -4
AI_capex_without_revenue -5
game_launch_first_week_only -4
single_IP_dependence -4
founder_legal_risk -5
privacy_security_trust_break -5
data_breach_revenue_cut -5
```

### 왜 내리나

삼성SDS는 AI/M&A 자본배분 기대만으로 장중 20.8% 올랐고, 카카오는 OpenAI 제휴 전후로 +9% 뒤 -2%를 보였다. LG CNS는 cloud/AI 매출비중이 절반 이상이었지만 IPO 첫날 가격이 -3.55%로 실패했다. SK텔레콤은 보안사고가 실제 매출전망 하향, 보안투자, 벌금으로 연결됐다.

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
신작 첫 주 판매만 있음
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
신작 판매량이 retention보다 먼저 valuation을 설명
BTS/K-pop comeback 기대가 governance risk를 덮음
single-IP developer가 IPO 이후 valuation premium을 받음

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

이번 R8 Loop 10에서 **SK텔레콤은 hard 4C에 가까운 strong 4C-watch**, **HYBE는 hard 4C가 아닌 governance 4C-watch**, **Kakao/OpenAI는 price_moved_without_evidence**, **Samsung SDS는 Stage 2 + 4B-watch**로 둔다.

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

## docs/round/round_166.md 요약

```md
# R8 Loop 10. Platform / Content / Software / Security Price Validation

이번 라운드는 R8 Loop 10 price-validation 라운드다.

핵심 결론:
- Douzone Bizon is B2B SaaS Stage 2 candidate. EQT invests $930M for 37.6%, implying about $2.473B equity value. ARR, churn, OPM and FCF required before Green.
- Samsung SDS is Stage 2 + 4B-watch. KKR $820M CB and AI capital allocation drove +20.8%, relative +17.8pp vs KOSPI. Recurring AI revenue and FCF required before Green.
- LG CNS is evidence_good_but_price_failed. IPO price 61,900 won, opening 60,500, debut trade 59,700, -3.55%, despite cloud/AI services being more than half of sales in first three quarters of 2024.
- NAVER/Webtoon is Stage 2 IP platform candidate. Webtoon IPO $21 to $24, +14.3%, first-day close $23, next-day high $25.66. Disney/earnings event later drove +62%, but prior post-IPO drawdown was -55%. Paid usage, ARPU, IP licensing, FCF required.
- Kakao/OpenAI partnership is price_moved_without_evidence. Kakao rose +9% before the announcement and fell -2% on the day; monetization was not yet proven.
- Shift Up is Stage 2 game-IP candidate. IPO raise 435B won, valuation 3.5T won, 2023 OP margin 65.7%, Stellar Blade PC sold >1M in 3 days and total >3M. Repeat bookings and pipeline conversion required.
- SK Telecom data breach is strong 4C-watch. Shares fell -8.5% intraday and -6.7% close; later reports showed 26.96M user-data pieces leaked, 700B won security investment, 800B won revenue forecast cut, and 134.8B won fine.
- HYBE is governance/legal 4C-watch. Police sought detention warrant for founder Bang Si-hyuk; shares fell -2.4%, but prosecutors later declined the warrant request, so hard 4C not confirmed.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 166 R8 Loop 10 Platform Content SW Security Price Validation

## 반영 내용
- R8 Loop 10 price-validation 라운드를 추가했다.
- B2B SaaS, AI cloud capital allocation, cloud/AI IPO, Webtoon/IP platform, AI partnership, game IP, cybersecurity breach, K-pop governance risk를 비교했다.
- Reuters/Barron’s/Investopedia/GamesRadar/AP reported anchors로 가능한 MFE/MAE 및 transaction/operational metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- recurring revenue, ARR proxy, paid usage, bookings repeatability, OPM/FCF, security/privacy trust 가중치 강화
- AI partnership headline, IPO/debut premium, M&A/capital allocation without revenue, single launch sales, founder legal risk, data breach 감점 강화
- AI/cloud and content/IP 4B-watch, security/privacy 4C-watch 민감도 강화
```

## case row 초안

```jsonl
{"case_id":"r8_loop10_douzone_bizon_eqt_saas","symbol":"012510","company_name":"Douzone Bizon","case_type":"success_candidate","primary_archetype":"B2B_SAAS_ERP_WORKFLOW","stage2_date":"2025-11-07","price_validation":{"price_data_source":"Reuters transaction evidence","stage3_price":null,"eqt_investment_usd_mn":930,"stake_acquired_pct":37.6,"implied_equity_value_usd_bn":2.473,"bpea_fund_ix_post_deal_exposure_pct":"5-10","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"private_equity_software_rerating_candidate","notes":"EQT investment is Stage 2; ARR, churn, OPM and FCF conversion required before Green."}
{"case_id":"r8_loop10_samsung_sds_kkr_ai_4b","symbol":"018260","company_name":"Samsung SDS","case_type":"success_candidate","primary_archetype":"AI_CLOUD_CAPITAL_ALLOCATION","stage2_date":"2026-04-15","stage4b_date":"2026-04-15","price_validation":{"price_data_source":"Reuters reported event return anchor","stage3_price":null,"stage2_event_mfe_1d_pct":20.8,"morning_trade_return_pct":19.4,"kospi_same_context_pct":3.0,"relative_intraday_outperformance_pp":17.8,"cb_investment_usd_mn":820,"cb_investment_krw_trn":1.207,"existing_cash_krw_trn":6.4,"combined_cash_plus_cb_krw_trn":7.607,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"AI_cloud_capital_allocation_watch","notes":"KKR/AI capital allocation is Stage 2 and 4B-watch; recurring AI revenue and FCF required for Green."}
{"case_id":"r8_loop10_lg_cns_ai_cloud_ipo_price_failed","symbol":"LG_CNS","company_name":"LG CNS","case_type":"evidence_good_but_price_failed","primary_archetype":"CLOUD_AI_SOFTWARE_INFRA","stage2_date":"2025-02-05","price_validation":{"price_data_source":"Reuters IPO price anchor","stage3_price":null,"ipo_price":61900,"opening_price":60500,"opening_return_vs_ipo_pct":-2.26,"debut_trade_price":59700,"debut_mae_pct":-3.55,"ipo_proceeds_krw_trn":1.2,"morning_market_value_krw_trn":5.79,"cloud_ai_sales_mix":"more_than_half_of_1Q_3Q_2024_sales","price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"IPO_cloud_AI_watch","notes":"Cloud/AI mix was high but IPO price action failed; Stage 3 requires recurring revenue, retention, margin and FCF."}
{"case_id":"r8_loop10_naver_webtoon_ip_platform","symbol":"035420/WBTN","company_name":"NAVER/Webtoon","case_type":"success_candidate","primary_archetype":"WEBTOON_PLATFORM_IP_MONETIZATION","stage2_date":"2024-06-27","stage4b_date":"2025-08-13","price_validation":{"price_data_source":"Reuters/Investopedia/Barron's price and event anchors","stage3_price":null,"webtoon_ipo_price_usd":21,"webtoon_debut_intraday_high_usd":24,"debut_mfe_from_ipo_pct":14.3,"webtoon_first_day_close_usd":23,"first_day_close_return_pct":9.5,"next_day_intraday_high_usd":25.66,"mfe_from_ipo_to_next_day_high_pct":22.2,"disney_earnings_event_price_usd":15.16,"disney_earnings_event_mfe_pct":62,"pre_disney_post_ipo_drawdown_context_pct":-55,"disney_event_revenue_usd_mn":348.3,"disney_event_revenue_growth_pct":8.5,"adjusted_q2_profit_per_share_usd":0.07,"mau_context_mn":155,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_event_premium_watch","rerating_result":"Webtoon_IP_monetization_watch","notes":"MAU/IP platform is Stage 2; paid usage, ARPU, IP licensing, operating leverage and FCF required before Green."}
{"case_id":"r8_loop10_kakao_openai_partnership_price_only","symbol":"035720","company_name":"Kakao","case_type":"overheat","primary_archetype":"AI_SOFTWARE_PARTNERSHIP_EVENT","stage1_date":"2025-02-04","stage4b_date":"2025-02-04","price_validation":{"price_data_source":"Reuters event return anchor","stage3_price":null,"event_mfe_before_announcement_pct":9.0,"event_mae_following_day_pct":-2.0,"two_session_cumulative_return_pct":6.8,"event_fade_from_peak_pp":-11.0,"ai_revenue_confirmed":false,"paid_usage_confirmed":false,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"AI_partnership_event_premium","notes":"OpenAI partnership is Stage 1/2; paid AI usage, ARPU and margin required for Green."}
{"case_id":"r8_loop10_shiftup_stellarblade_game_ip","symbol":"462870","company_name":"Shift Up","case_type":"success_candidate","primary_archetype":"GAME_IP_REPEAT_MONETIZATION","stage2_date":"2024-07/2025-06","price_validation":{"price_data_source":"Reuters IPO anchor + GamesRadar sales/pipeline anchor","stage3_price":null,"ipo_raise_krw_bn":435,"ipo_valuation_krw_trn":3.5,"tencent_post_ipo_stake_pct":35,"tencent_pre_ipo_stake_pct":40,"stake_change_pp":-5,"revenue_2023_krw_bn":169,"operating_profit_2023_krw_bn":111,"op_margin_2023_pct":65.7,"nikke_revenue_late_2022_to_1q2024_krw_bn":255,"stellar_blade_pc_sales_3d_mn_copies":1,"stellar_blade_total_sales_mid_2025_mn_copies":3,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"game_IP_repeat_monetization_watch","notes":"Game IP and strong profitability are Stage 2; repeat bookings, platform expansion, pipeline conversion and FCF required for Green."}
{"case_id":"r8_loop10_skt_cybersecurity_operational_trust_4c","symbol":"017670","company_name":"SK Telecom","case_type":"4c_watch","primary_archetype":"SECURITY_OPERATIONAL_TRUST_OVERLAY","stage4c_date":"2025-04-28/2025-07-04/2025-08-28","price_validation":{"price_data_source":"Reuters breach/price/cost anchors","stage3_price":null,"event_intraday_mae_pct":-8.5,"event_close_mae_pct":-6.7,"kospi_same_context_pct":0.1,"relative_underperformance_close_pp":-6.8,"affected_users_initial_mn":23,"usim_replacement_stores":2600,"protection_service_signups_mn":5.54,"signup_share_pct":24.1,"leaked_user_data_pieces_mn":26.96,"security_investment_krw_bn":700,"annualized_security_investment_krw_bn":140,"revenue_forecast_cut_2025_krw_bn":800,"customer_benefit_package_cost_krw_bn":500,"pipc_fine_krw_bn":134.8,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"cybersecurity_operational_trust_break","notes":"Data breach caused price drop, revenue cut, security investment and fine; strong 4C-watch approaching hard gate."}
{"case_id":"r8_loop10_hybe_founder_legal_governance_watch","symbol":"352820","company_name":"HYBE","case_type":"4c_watch","primary_archetype":"PLATFORM_GOVERNANCE_LEGAL_RISK","stage4c_date":"2026-04-21","price_validation":{"price_data_source":"Reuters/AP legal event anchors","stage3_price":null,"event_mae_1d_pct":-2.4,"alleged_profit_krw_bn":190,"hard_4c_status":"not_confirmed_warrant_declined","legal_relief_date":"2026-04-24","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"governance_legal_overhang","notes":"Legal/governance risk blocks Green; warrant declined, so hard 4C not confirmed."}
```

## shadow weight row 초안

```csv
archetype,recurring_revenue,arr_proxy,paid_usage,bookings,opm_fcf,ip_monetization,operational_trust,security_privacy_trust,event_penalty,legal_privacy_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
B2B_SAAS_ERP_WORKFLOW,+5,+5,+3,+3,+5,+0,+3,+2,-2,+1,+3,+3,Douzone/EQT is Stage 2 until ARR/churn/OPM/FCF confirm.
AI_CLOUD_CAPITAL_ALLOCATION,+3,+3,+3,+2,+5,+0,+3,+2,-5,+2,+5,+3,Samsung SDS KKR event is 4B-watch before AI revenue conversion.
CLOUD_AI_SOFTWARE_INFRA,+4,+4,+3,+2,+5,+0,+3,+2,-4,+2,+4,+3,LG CNS IPO weak price action blocks Green despite cloud/AI mix.
WEBTOON_PLATFORM_IP_MONETIZATION,+3,+3,+5,+4,+5,+5,+3,+2,-3,+2,+5,+4,Webtoon needs paid usage, ARPU, IP monetization and FCF beyond MAU/IPO.
AI_SOFTWARE_PARTNERSHIP_EVENT,+2,+2,+5,+2,+4,+0,+3,+2,-5,+2,+5,+3,Kakao/OpenAI partnership is price_moved_without_evidence until monetization.
GAME_IP_REPEAT_MONETIZATION,+3,+0,+3,+5,+5,+5,+3,+2,-3,+2,+4,+4,Shift Up needs repeat bookings/pipeline conversion beyond launch and IPO.
SECURITY_OPERATIONAL_TRUST_OVERLAY,+0,+0,+0,+0,+3,+0,+5,+5,-2,+5,+4,+5,SK Telecom breach is strong 4C-watch with revenue/fine/compensation impact.
PLATFORM_GOVERNANCE_LEGAL_RISK,+0,+0,+0,+0,+0,+3,+5,+2,-3,+5,+4,+5,HYBE legal risk is 4C-watch; hard 4C only after legal outcome materially impairs business.
```

---

# 이번 R8 Loop 10 결론

R8은 Stage 3 후보가 있지만, **false positive가 가장 쉽게 쌓이는 섹터**다.

```text
1. 더존비즈온은 B2B SaaS 구조가 좋아 Stage 2 후보가 된다.
   하지만 EQT 투자 발표가 아니라 ARR·churn·OPM·FCF가 Stage 3다.

2. 삼성SDS는 KKR/AI capital allocation 이벤트로 장중 +20.8% 올랐다.
   이건 Stage 2와 4B-watch이지, AI revenue 전 Stage 3가 아니다.

3. LG CNS는 cloud/AI 매출비중이 절반 이상이었지만 IPO 첫날 -3.55%였다.
   좋은 사업 설명만으로 가격검증을 통과하지 못한 케이스다.

4. NAVER/Webtoon은 MAU와 IP platform 잠재력이 강하지만,
   post-IPO drawdown, Disney event spike가 섞여 있다.
   paid usage·ARPU·IP licensing·FCF 전 Green 금지다.

5. 카카오/OpenAI는 전형적인 price_moved_without_evidence다.
   partnership headline은 Stage 1~2이고, monetization 전 Green 금지다.

6. Shift Up은 게임 IP 후보지만,
   IPO·신작 흥행만으로 Stage 3가 아니다.
   repeat bookings, pipeline conversion, FCF가 필요하다.

7. SK텔레콤은 R8 security/privacy hard gate에 가깝다.
   데이터 유출이 주가 하락, 보상비용, 매출전망 하향, 벌금으로 연결됐다.

8. HYBE는 콘텐츠 IP가 좋아도 founder legal risk가 Green을 막는다.
   영장이 기각되어 hard 4C는 아니지만, governance 4C-watch다.
```

한 문장으로 압축하면:

> **R8에서 진짜 Stage 3는 “AI·게임·웹툰·K-pop이 핫하다”가 아니라, 반복매출·paid usage·bookings·ARR proxy·OPM/FCF와 운영신뢰가 확인되는 순간이다.**
> **R8은 AI partnership, IPO, M&A, 신작 흥행, IP 기대를 먼저 4B/Event Premium으로 분리하고, privacy/security/governance 사고는 강한 4C gate로 둬야 한다.**

[1]: https://www.reuters.com/world/asia-pacific/swedish-firm-eqt-shells-out-930-million-slice-south-koreas-douzone-bizon-2025-11-07/?utm_source=chatgpt.com "Swedish firm EQT shells out $930 million for a slice of South Korea's Douzone Bizon"
[2]: https://www.reuters.com/world/asia-pacific/kkr-buy-820-million-samsung-sds-convertible-bonds-shares-jump-20-2026-04-15/?utm_source=chatgpt.com "KKR to buy $820 million of Samsung SDS convertible bonds, shares jump 20%"
[3]: https://www.reuters.com/technology/skorean-tech-services-firm-lg-cns-falls-stock-market-debut-2025-02-05/?utm_source=chatgpt.com "South Korean tech services firm LG CNS drops in market debut"
[4]: https://www.reuters.com/markets/us/webtoons-nasdaq-debut-sees-shares-jump-14-2024-06-27/?utm_source=chatgpt.com "South Korea's Naver-backed Webtoon shares jump about 14% in Nasdaq debut"
[5]: https://www.barrons.com/articles/webtoon-earnings-stock-price-disney-884625a2?utm_source=chatgpt.com "Webtoon Stock Soars 55% After Earnings. Thank Luke Skywalker and Spider-Man."
[6]: https://www.reuters.com/technology/artificial-intelligence/openai-kakao-jointly-develop-ai-products-south-korea-2025-02-04/?utm_source=chatgpt.com "OpenAI clinches deal with Kakao, talks with SoftBank and Samsung about Stargate"
[7]: https://www.reuters.com/markets/deals/tencent-backed-shift-up-may-price-ipo-top-end-band-source-says-2024-06-27/?utm_source=chatgpt.com "Tencent-backed Shift Up may price IPO at top end of band, source says"
[8]: https://www.gamesradar.com/games/action-rpg/stellar-blade-sequel-will-feature-an-expanded-world-and-enhanced-gameplay-as-developer-shift-up-believes-itll-result-in-even-greater-success-than-the-original/?utm_source=chatgpt.com "Stellar Blade sequel will feature an \"expanded\" world and \"enhanced gameplay\" as developer Shift Up believes it'll \"result in even greater success than the original"
[9]: https://www.reuters.com/sustainability/boards-policy-regulation/sk-telecom-shares-plunge-after-data-breach-due-cyberattack-2025-04-28/?utm_source=chatgpt.com "SK Telecom shares plunge after data breach due to cyberattack"
[10]: https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-orders-sk-telecom-strengthen-data-security-after-leak-2025-07-04/?utm_source=chatgpt.com "South Korea penalises 'negligent' SK Telecom over major data leak"
[11]: https://www.reuters.com/world/asia-pacific/south-korea-police-seek-detention-warrant-hybe-chairman-yonhap-says-2026-04-21/?utm_source=chatgpt.com "South Korea police seek detention warrant for BTS agency founder Bang"
