순서상 이번은 **R8 Loop 8 — 플랫폼·콘텐츠·SW·보안 가격경로 검증 라운드**다.

이번 라운드도 원시 수정주가 일봉 OHLC를 안정적으로 직접 추출하지 못한 종목은 숫자를 만들지 않았다. 대신 Reuters / FT / MarketWatch / Investopedia / AP에 남은 **가격 anchor, 이벤트 수익률, IPO 가격, 거래금액, 매출·손실 지표**로 계산 가능한 값은 직접 계산했다.

```text
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

---

# 1. 이번 라운드 대섹터

```text
R8 = 플랫폼·콘텐츠·SW·보안
large_sector = PLATFORM_CONTENT_SW_SECURITY
round = R8 Loop 8 / price-path validation
```

R8의 기본 검증축은 `arr`, `opm`, `fcf`, `churn`, `paid_usage`, `ip_monetization`, `privacy_security_incident`다. R8은 SaaS, 클라우드, AI software, 플랫폼, 웹툰, 게임 IP, K-pop IP, 광고, 보안, privacy/security overlay를 포함한다. 

Round 119 기준으로 R8에서 부족한 증거는 `ai_feature`, `mau_growth`이고, 필요한 증거는 `arr`, `churn`, `arpu`, `fcf`, `operational_trust`다. Green blocker는 `outage`, `privacy_breach`, `regulatory_take_rate_damage`다. 

---

# 2. 대상 canonical archetype

```text
B2B_SAAS_ERP_WORKFLOW
CLOUD_AI_SOFTWARE_INFRA
AI_CLOUD_CAPITAL_ALLOCATION
PLATFORM_SOFTWARE_INTERNET
WEBTOON_PLATFORM_IP_MONETIZATION
GAME_CONTENT_IP_REPEAT_MONETIZATION
SINGLE_IP_RELEASE_EVENT_PREMIUM
KPOP_PLATFORM_CONTENT_IP
PLATFORM_GOVERNANCE_LEGAL_RISK
SECURITY_OPERATIONAL_TRUST_OVERLAY
PRICE_ONLY_RALLY
EVENT_PREMIUM
```

이번 R8의 핵심 질문은 이거다.

```text
AI·플랫폼·콘텐츠·게임 테마인가?
아니면 반복매출, ARR proxy, paid usage, bookings, OPM/FCF가 실제로 확인되는가?
```

---

# 3. deep sub-archetype

```text
B2B SaaS / ERP:
- Douzone Bizon
- cloud ERP
- accounting / tax / compliance
- SME lock-in
- EQT operational improvement
- recurring revenue vs transaction event

AI cloud / IT services:
- Samsung SDS
- LG CNS
- AI infrastructure
- cloud and AI services
- global M&A
- CB / IPO funding
- AI revenue conversion vs capital-allocation event

플랫폼 / 웹툰:
- Naver
- Webtoon Entertainment IPO
- global MAU
- paid content / IP monetization
- holdco discount
- valuation boost vs company-level earnings

AI partnership / 포털:
- Kakao
- OpenAI partnership
- KakaoTalk AI integration
- AI feature vs monetization
- governance overhang

게임 IP:
- Krafton
- inZOI
- ADK acquisition
- PUBG dependence
- repeat bookings
- single-IP / launch event premium

K-pop IP / governance:
- HYBE
- BTS / Weverse
- artist concentration
- founder legal risk
- IPO-related investigation
- operational/legal trust
```

---

# 4. 국장 신규 후보 case

## Case A — 더존비즈온 `success_candidate / B2B SaaS ERP`

```text
symbol = 012510
case_type = success_candidate
archetype = B2B_SAAS_ERP_WORKFLOW / PRIVATE_EQUITY_SOFTWARE_RERATING
```

### evidence

2025년 11월 7일 EQT는 더존비즈온 지분 37.6%를 약 9.3억 달러에 인수하기로 했다. Reuters는 더존비즈온이 중소기업 대상 클라우드 ERP, 회계, 세무, 컴플라이언스 소프트웨어를 제공하며, EQT가 장기적으로 운영 개선과 핵심 사업 강화를 추진한다고 보도했다. 이 거래는 공정위 승인과 산업통상자원부 인허가가 필요하다. ([Reuters][1])

### stage date

```text
Stage 1:
2024~2025
- B2B SaaS / cloud ERP / AI ERP 기대
- SME lock-in software rerating 기대

Stage 2:
2025-11-07
- EQT 37.6% stake acquisition
- cloud ERP / accounting / tax / compliance recurring business 확인
- PE operational improvement 기대

Stage 3:
보류
- EQT 거래 자체는 event premium 성격도 있음
- ARR proxy, churn, OPM, FCF conversion, 고객 lock-in 확인 필요

Stage 4B:
거래 발표 후 valuation이 먼저 크게 확장됐다면 후보

Stage 4C:
거래 승인 실패, churn 상승, cloud 전환 margin 훼손, growth 둔화 시 후보
```

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

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = private_equity_software_rerating_candidate
stage_failure_type = stage2_watch_success
```

### 교정

더존비즈온은 R8에서 `recurring_revenue`, `SME_lock_in`, `ARR_proxy`, `OPM_improvement`를 올릴 수 있다. 하지만 Stage 3는 EQT 투자 발표가 아니라 **반복매출·churn·OPM·FCF 개선 확인일**에 줘야 한다.

---

## Case B — 삼성SDS `success_candidate + 4B-watch / AI capital allocation`

```text
symbol = 018260
case_type = success_candidate + 4B-watch
archetype = AI_CLOUD_CAPITAL_ALLOCATION / CLOUD_AI_SOFTWARE_INFRA
```

### evidence

2026년 4월 15일 KKR은 삼성SDS가 신규 발행하는 8.2억 달러 규모 전환사채를 인수하기로 했고, 삼성SDS 주가는 장중 최대 20.8% 상승했다. Reuters는 KKR이 삼성SDS의 M&A, 자본배분, full-stack AI solutions 확장에 자문할 것이며, 삼성SDS가 6.4조 원의 현금과 KKR 자금을 바탕으로 AI 인프라, AI transformation, physical AI, stablecoin 등 신사업을 추진하겠다고 보도했다. ([Reuters][2])

### stage date

```text
Stage 1:
2025~2026
- 기업 AI 전환
- Samsung group AI infrastructure / IT services 기대

Stage 2:
2026-04-15
- KKR $820M CB investment
- AI infra / M&A / capital allocation 기대
- 장중 +20.8%

Stage 3:
없음
- CB 투자와 AI 투자 계획만으로 Green 금지
- enterprise AI 계약, recurring cloud revenue, margin, FCF 확인 필요

Stage 4B:
2026-04-15
- 발표 당일 장중 +20.8%
- AI + KKR + value-up 기대가 가격에 먼저 반영

Stage 4C:
CB dilution, AI capex 대비 매출 부진, M&A 실패, stablecoin regulatory risk 시 후보
```

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
= +17.8 percentage points

CB_investment:
$820M

KRW_equivalent_at_Reuters_FX_1472:
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

below_stage3_price_flag:
N/A

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

### 교정

삼성SDS는 `AI_capital_allocation`을 Stage 2로 인정할 수 있지만, `AI_revenue_conversion`, `enterprise_contract_quality`, `OPM/FCF` 전 Stage 3는 금지다. 전환사채는 동시에 `dilution_watch`다.

---

## Case C — LG CNS `evidence_good_but_price_failed / AI cloud IPO`

```text
symbol = LG CNS
case_type = evidence_good_but_price_failed / IPO_event
archetype = CLOUD_AI_SOFTWARE_INFRA / AI_SOFTWARE_APPLICATION
```

### evidence

2025년 2월 5일 LG CNS는 상장 첫날 공모가 61,900원 대비 59,700원으로 하락했다. Reuters는 이 IPO가 1.2조 원을 조달한 대형 IPO였고, 회사가 IT·cloud·AI services를 제공하며 2024년 1~3분기 매출의 절반 이상이 cloud and AI services에서 나왔다고 보도했다. ([Reuters][3])

### stage date

```text
Stage 1:
2024~2025
- cloud / AI services provider IPO
- enterprise digital transformation 기대

Stage 2:
2025-02-05
- IPO
- cloud and AI services가 2024년 1~3분기 매출의 절반 이상
- IPO proceeds 1.2조 원

Stage 3:
없음
- IPO와 사업설명만으로 Green 금지
- recurring cloud revenue, margin, customer retention, FCF 확인 필요

Stage 4B:
IPO valuation이 AI/cloud narrative를 먼저 반영한 구간

Stage 4C:
IPO 후 가격 부진, M&A 실패, debt burden, AI growth 둔화 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters IPO price anchor

stage3_price:
N/A

IPO_price:
61,900원

debut_price:
59,700원

debut_MAE:
(59,700 / 61,900) - 1
= -3.55%

IPO_proceeds:
1.2T won

cloud_AI_sales_mix:
>50% of sales in first three quarters of 2024

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

score_price_read:
AI/cloud evidence existed, but price failed immediately at IPO.
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed
rerating_result = IPO_cloud_AI_watch
stage_failure_type = stage2_not_green
```

### 교정

LG CNS는 R8에서 “AI/cloud 매출 비중이 높다”는 사실만으로 Stage 3를 주면 안 된다는 케이스다. IPO 가격경로가 바로 약했다.

---

## Case D — NAVER / Webtoon `success_candidate + holdco discount / IP monetization watch`

```text
symbol = 035420
case_type = success_candidate
archetype = WEBTOON_PLATFORM_IP_MONETIZATION / PLATFORM_SOFTWARE_INTERNET
```

### evidence

2024년 6월 Webtoon Entertainment는 미국 IPO를 주당 21달러로 책정해 2.7B달러 valuation을 목표로 했고, 315M달러를 조달했다. FT는 Webtoon이 170M monthly active users를 보유했지만, 전년 1.28B달러 매출에 145M달러 순손실을 냈다고 보도했다. ([Financial Times][4])

MarketWatch는 2024년 6월 19일 Nomura가 Naver의 Webtoon IPO valuation boost가 예상보다 약할 수 있다며 Webtoon 지분가치에 50% holding-company discount를 적용했고, Naver 목표가를 22% 낮춰 210,000원으로 제시했다고 보도했다. 당시 Naver 주가는 0.9% 하락해 165,300원이었다. ([마켓워치][5])

Webtoon Entertainment는 IPO 가격 21달러 대비 첫날 23달러에 마감했고, 다음 날 장중 25.66달러까지 올랐다. ([Investopedia][6])

### stage date

```text
Stage 1:
2024-06
- Webtoon IPO
- Korean content/IP platform monetization 기대

Stage 2:
2024-06-19 / 2024-06-27
- Webtoon valuation $2.7B
- 170M MAU
- IPO price $21
- Naver stake valuation with 50% holdco discount

Stage 3:
없음
- MAU와 IPO만으로 Green 금지
- paid content, ARPU, IP monetization, operating margin, FCF 확인 필요

Stage 4B:
Webtoon IPO debut rally / valuation premium 구간

Stage 4C:
Webtoon valuation 하락, 적자 지속, paid content growth 둔화, Naver commerce/search 둔화 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
FT / MarketWatch / Investopedia reported price anchors

Naver_stage2_price:
165,300원

Naver_event_MAE:
-0.9%

Naver_target_price:
210,000원

target_upside_from_Naver_stage2_price:
(210,000 / 165,300) - 1
= +27.0%

Webtoon_IPO_price:
$21

Webtoon_first_day_close:
$23

Webtoon_first_day_close_return:
(23 / 21) - 1
= +9.5%

Webtoon_next_day_intraday_high:
$25.66

Webtoon_MFE_from_IPO_to_intraday_high:
(25.66 / 21) - 1
= +22.2%

Webtoon_revenue_prior_year:
$1.28B

Webtoon_net_loss_prior_year:
$145M

net_loss_margin:
145M / 1.28B
= 11.3%

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

### 교정

NAVER/Webtoon은 `MAU`와 `IPO valuation`만으로 Stage 3 금지다. Stage 3는 **paid content, ARPU, IP licensing, operating leverage, FCF**가 확인되어야 한다.

---

## Case E — 카카오 `price_moved_without_evidence / OpenAI partnership`

```text
symbol = 035720
case_type = price_moved_without_evidence
archetype = PLATFORM_SOFTWARE_INTERNET / AI_SOFTWARE_APPLICATION
```

### evidence

2025년 2월 4일 OpenAI는 카카오와 한국 AI 제품을 공동 개발한다고 발표했다. Reuters는 카카오톡이 한국에서 97% 국내 점유율을 가진 dominant messaging app이라고 설명했다. 하지만 카카오 주가는 전날 9% 급등한 뒤 발표 당일 2% 하락했다. ([Reuters][7])

### stage date

```text
Stage 1:
2025-02-04
- OpenAI-Kakao partnership
- KakaoTalk AI feature 기대

Stage 2:
보류
- AI product launch, paid usage, ARPU, ad/commerce monetization 확인 전

Stage 3:
없음
- partnership headline만으로 Green 금지

Stage 4B:
2025-02-03~04
- 전날 +9%, 다음날 -2%
- price moved before monetization

Stage 4C:
founder governance/legal risk, platform trust risk, AI monetization failure 시 후보
```

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
from +9% headline rally to -2% next-day move
= -11 percentage points swing

KakaoTalk_domestic_market_share:
97%

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

### 교정

카카오는 `OpenAI partnership`을 Stage 1~2 routing으로만 써야 한다. Stage 3는 **AI product paid usage, ARPU, OPM/FCF 개선**이 나온 뒤다.

---

## Case F — 크래프톤 `success_candidate / game IP repeat monetization watch`

```text
symbol = 259960
case_type = success_candidate
archetype = GAME_CONTENT_IP_REPEAT_MONETIZATION / SINGLE_IP_RELEASE_EVENT_PREMIUM
```

### evidence

2025년 6월 24일 크래프톤은 일본 광고·애니메이션 기업 ADK Holdings를 750억 엔, 약 516.21M달러에 인수하기로 했다. ADK는 일본 top-three comprehensive advertising group 중 하나이며, Doraemon, Yu-Gi-Oh!, Crayon Shin-chan 등 300개 이상 애니메이션 제작에 참여했다. ([Reuters][8])

inZOI는 2025년 3월 28일 early access로 출시된 뒤 첫 주 100만 장 이상 판매됐고, Krafton publisher history상 가장 빠른 판매 milestone을 기록했다. 출시 직후 Steam Global Top Sellers 1위에 올랐고, Steam 동시접속 peak 87,377명, Twitch peak 175,000 viewers를 기록했다. ([위키백과][9])

### stage date

```text
Stage 1:
2025-03-28
- inZOI early access launch
- PUBG 이후 second IP 기대

Stage 2:
2025-04
- inZOI first-week sales >1M
- Steam top seller / user engagement

추가 Stage 2:
2025-06-24
- ADK Holdings acquisition
- anime/IP pipeline 확장

Stage 3:
보류
- first-week sales와 M&A만으로 Green 금지
- repeat bookings, retention, DLC/console expansion, IP monetization 확인 필요

Stage 4B:
신작 launch / ADK acquisition / AI-first narrative로 가격이 먼저 뛴 구간이면 후보

Stage 4C:
retention 부진, review deterioration, single-IP 의존, M&A integration 실패 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters ADK transaction + InZOI release/sales evidence

stage3_price:
N/A

stock_event_price:
price_data_unavailable_after_deep_search
- Reuters ADK 기사와 InZOI evidence는 Krafton 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

ADK_transaction_value:
75B yen / $516.21M

InZOI_first_week_sales:
>1M copies

Steam_peak_concurrent_players:
87,377

Twitch_peak_viewers:
175,000

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

### 교정

크래프톤은 `single launch success`와 `repeat monetization`을 분리해야 한다. Stage 3는 첫 주 판매량이 아니라 **retention, DLC, live-service bookings, IP extension revenue**에서 나온다.

---

## Case G — HYBE `4C-watch / governance legal risk`

```text
symbol = 352820
case_type = 4C-watch
archetype = KPOP_PLATFORM_CONTENT_IP / PLATFORM_GOVERNANCE_LEGAL_RISK
```

### evidence

2026년 4월 21일 한국 경찰은 HYBE 창업자 방시혁에 대해 IPO 관련 자본시장법 위반 혐의로 구속영장을 신청했다. Reuters는 방시혁이 초기 투자자를 오도하고 관련 펀드를 통해 약 1,900억 원의 이익을 얻은 혐의를 받고 있으며, HYBE 주가가 해당 소식 후 2.4% 하락했다고 보도했다. ([Reuters][10])

AP는 이후 검찰이 경찰의 구속영장 신청을 기각하고, 증거가 부족하다고 판단해 보완수사를 요청했다고 보도했다. 즉 이 이벤트는 hard 4C 확정이 아니라 **governance/legal 4C-watch**다. ([AP News][11])

### stage date

```text
Stage 1:
2024~2026
- BTS / Weverse / K-pop global IP 기대
- BTS comeback 기대

Stage 2:
보류
- IP monetization, tour revenue, Weverse paid usage, OPM 확인 필요

Stage 3:
없음
- legal/governance overhang 해소 전 Green 금지

Stage 4B:
BTS comeback / K-pop IP 기대만으로 가격이 먼저 확장되면 후보

Stage 4C-watch:
2026-04-21
- Bang Si-hyuk detention warrant request
- HYBE -2.4%
- alleged profit about 190B won

4C relief:
2026-04-24
- prosecutors declined arrest warrant request
- hard 4C는 보류
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters / AP legal event anchors

stage3_price:
N/A

stage4c_event_MAE_1D:
-2.4%

alleged_profit:
190B won

hard_4C_status:
not confirmed

MFE / MAE:
price_data_unavailable_after_deep_search beyond reported event return

below_stage3_price_flag:
N/A

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search

Stage 4C 큰 하락 이전 포착 여부:
partial_success
- legal event 당일 4C-watch 가능.
- AP 보도상 arrest warrant declined, so hard 4C는 보류.
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = governance_legal_overhang
stage_failure_type = should_have_been_red_or_watch
```

### 교정

HYBE는 `content IP`가 좋아도 `founder_legal_risk`, `artist/label conflict`, `governance_trust`가 Green을 막을 수 있다는 기준점이다.

---

# 5. 이번 R8 case별 요약표

| case          | 분류                             |                                                                  실제 가격검증 | alignment                               |
| ------------- | ------------------------------ | -----------------------------------------------------------------------: | --------------------------------------- |
| 더존비즈온         | success_candidate              |                                 EQT $930M / 37.6%, implied value $2.473B | success_candidate                       |
| 삼성SDS         | success_candidate + 4B         |                                KKR CB $820M, 장중 +20.8%, relative +17.8pp | event_premium + success_candidate       |
| LG CNS        | evidence_good_but_price_failed |                                              IPO 61,900 → 59,700, -3.55% | evidence_good_but_price_failed          |
| NAVER/Webtoon | success_candidate              | Naver 165,300원 -0.9%; WBTN $21→$25.66, +22.2%; Webtoon loss margin 11.3% | success_candidate / event premium watch |
| 카카오           | price_moved_without_evidence   |                         +9% 후 -2%, two-session +6.8%, peak-to-fade -11pp | price_moved_without_evidence            |
| 크래프톤          | success_candidate              |                                ADK $516.21M, inZOI first-week >1M copies | success_candidate                       |
| HYBE          | 4C-watch                       |       legal event -2.4%, alleged profit 1,900억 원, warrant declined later | thesis_break_watch                      |

---

# 6. score-price alignment 판정

```text
success_candidate:
- 더존비즈온
- NAVER/Webtoon
- 크래프톤

event_premium + success_candidate:
- 삼성SDS

evidence_good_but_price_failed:
- LG CNS

price_moved_without_evidence:
- 카카오 OpenAI partnership

thesis_break_watch:
- HYBE legal/governance risk

4B-watch:
- 삼성SDS KKR/AI event +20.8%
- Kakao OpenAI partnership +9% 후 -2%
- Webtoon IPO debut premium
- HYBE BTS/IP expectation with governance overhang
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
```

### 이유

더존비즈온은 cloud ERP·accounting·tax·compliance 기반 반복매출이 있고, EQT가 장기 운영개선을 추진하는 Stage 2 후보다. 크래프톤은 inZOI 첫 주 100만 장 판매와 ADK acquisition으로 game/IP 확장 가능성을 보여준다. 다만 둘 다 Stage 3는 ARR/retention/bookings/FCF 확인 뒤다. ([Reuters][1])

## 내릴 축

```text
AI_feature_only -5
partnership_headline_only -5
MAU_without_ARPU -4
IPO_debut_premium -4
M&A_without_integration -4
AI_capex_without_revenue -5
game_launch_first_week_only -4
single_IP_dependence -4
founder_legal_risk -5
privacy_security_trust_break -5
```

### 이유

삼성SDS는 AI/M&A 자본배분 기대만으로 장중 +20.8% 올랐고, 카카오는 OpenAI 제휴 발표 전후로 +9% 뒤 -2%를 보였다. LG CNS는 cloud/AI 매출 비중이 높았지만 IPO 첫날 -3.55%로 가격검증이 약했다. ([Reuters][2])

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
IPO debut premium만 있음
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

4B-elevated:
ARR growth 둔화
AI capex 증가로 margin 훼손
M&A integration cost 확대
single-IP 의존
governance/legal overhang 재점화
good news에도 주가 반응 둔화
```

## 4C hard gate 조건

```text
privacy breach
security outage
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

이번 R8에서는 HYBE를 hard 4C로 확정하지 않고 4C-watch로 둔다. 검찰이 구속영장 청구를 기각했기 때문에 hard 4C가 아니라 governance/legal overhang이다. ([AP News][11])

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

이번 세션에서 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉을 안정적으로 직접 확보하지 못했다. 대신 Reuters / FT / MarketWatch / Investopedia / AP의 가격 anchor와 이벤트 수익률을 사용해 계산 가능한 부분은 직접 계산했다.

---

# 9. patch-ready 출력

## docs/round/round_140.md 요약

```md
# R8 Loop 8. Platform / Content / Software / Security Price Validation

이번 라운드는 R8 price-validation 라운드다.

핵심 결론:
- 더존비즈온은 EQT $930M / 37.6% investment로 B2B SaaS Stage 2 후보가 된다. Implied equity value는 약 $2.473B다.
- 삼성SDS는 KKR $820M CB 투자와 AI capital allocation 기대만으로 장중 +20.8% 올랐다. Stage 2 / 4B-watch이며 AI revenue conversion 전 Green 금지다.
- LG CNS는 cloud/AI sales mix가 높았지만 IPO 첫날 61,900원에서 59,700원으로 -3.55% 하락했다. Evidence good but price failed.
- NAVER/Webtoon은 Webtoon IPO와 global MAU가 Stage 2 evidence지만, Naver holdco discount와 Webtoon loss margin 때문에 Stage 3 보류다.
- Kakao/OpenAI partnership은 전날 +9%, 발표일 -2%로 price moved before monetization이다.
- Krafton은 inZOI first-week >1M sales와 ADK $516M acquisition으로 game IP Stage 2 후보지만, repeat bookings/retention 전 Stage 3 금지다.
- HYBE는 legal/governance 4C-watch다. Founder detention warrant news에 -2.4%였으나 warrant declined later, so hard 4C는 보류한다.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 140 R8 Loop 8 Platform Content SW Security Price Validation

## 반영 내용
- R8 Loop 8 price-validation 라운드를 추가했다.
- B2B SaaS, AI cloud/IT services, Webtoon/IP platform, AI partnership, game IP, K-pop governance risk를 비교했다.
- Reuters/FT/MarketWatch/Investopedia/AP reported anchors로 가능한 MFE/MAE 및 transaction/valuation 지표를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- ARR proxy, recurring revenue, paid usage, bookings repeatability, OPM/FCF 가중치 강화
- AI partnership headline, IPO premium, M&A without integration, single launch sales, founder legal risk 감점 강화
- AI/cloud and content/IP 4B-watch 민감도 강화
```

## case row 초안

```jsonl
{"case_id":"r8_loop8_douzone_bizon_eqt_saas","symbol":"012510","company_name":"더존비즈온","case_type":"success_candidate","primary_archetype":"B2B_SAAS_ERP_WORKFLOW","stage2_date":"2025-11-07","price_validation":{"price_data_source":"Reuters transaction evidence","stage3_price":null,"eqt_investment_usd_mn":930,"stake_acquired_pct":37.6,"implied_equity_value_usd_bn":2.473,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"private_equity_software_rerating_candidate","notes":"EQT investment is Stage 2; ARR, churn, OPM and FCF conversion required before Green."}
{"case_id":"r8_loop8_samsung_sds_kkr_ai_event","symbol":"018260","company_name":"삼성SDS","case_type":"success_candidate","primary_archetype":"AI_CLOUD_CAPITAL_ALLOCATION","stage2_date":"2026-04-15","stage4b_date":"2026-04-15","price_validation":{"price_data_source":"Reuters reported event return","stage3_price":null,"stage2_event_mfe_1d_pct":20.8,"kospi_same_context_return_pct":3.0,"relative_outperformance_pp":17.8,"cb_investment_usd_mn":820,"cb_investment_krw_trn":1.207,"existing_cash_krw_trn":6.4,"combined_cash_cb_krw_trn":7.607,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"AI_cloud_capital_allocation_watch","notes":"KKR/AI capital allocation is Stage 2 and 4B-watch; AI revenue conversion required for Stage 3."}
{"case_id":"r8_loop8_lg_cns_ai_cloud_ipo_failed_price","symbol":"LG_CNS","company_name":"LG CNS","case_type":"evidence_good_but_price_failed","primary_archetype":"CLOUD_AI_SOFTWARE_INFRA","stage2_date":"2025-02-05","price_validation":{"price_data_source":"Reuters IPO price anchor","stage3_price":null,"ipo_price":61900,"debut_price":59700,"debut_mae_pct":-3.55,"ipo_proceeds_krw_trn":1.2,"cloud_ai_sales_mix_pct":50,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"IPO_cloud_AI_watch","notes":"Cloud/AI sales mix was high but IPO price action failed; Stage 3 requires recurring cloud revenue, margin and FCF."}
{"case_id":"r8_loop8_naver_webtoon_ip_platform","symbol":"035420","company_name":"NAVER/Webtoon","case_type":"success_candidate","primary_archetype":"WEBTOON_PLATFORM_IP_MONETIZATION","stage2_date":"2024-06-19","price_validation":{"price_data_source":"FT/MarketWatch/Investopedia reported anchors","naver_stage2_price":165300,"naver_event_mae_pct":-0.9,"naver_target_price":210000,"target_upside_pct":27.0,"webtoon_ipo_price_usd":21,"webtoon_first_day_close_usd":23,"webtoon_first_day_return_pct":9.5,"webtoon_intraday_high_usd":25.66,"webtoon_mfe_from_ipo_pct":22.2,"webtoon_revenue_usd_bn":1.28,"webtoon_net_loss_usd_mn":145,"webtoon_net_loss_margin_pct":11.3,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_event_premium_watch","rerating_result":"Webtoon_IP_monetization_watch","notes":"MAU and IPO valuation are Stage 2; paid content, ARPU, IP monetization and FCF required for Stage 3."}
{"case_id":"r8_loop8_kakao_openai_ai_partnership","symbol":"035720","company_name":"카카오","case_type":"overheat","primary_archetype":"AI_SOFTWARE_APPLICATION","stage1_date":"2025-02-04","stage4b_date":"2025-02-04","price_validation":{"price_data_source":"Reuters event return anchor","stage3_price":null,"event_mfe_prior_day_pct":9.0,"event_mae_next_day_pct":-2.0,"two_session_cumulative_return_pct":6.8,"peak_to_fade_swing_pp":-11.0,"kakaotalk_domestic_share_pct":97,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"AI_partnership_event_premium","notes":"OpenAI partnership is Stage 1/2; paid AI usage, ARPU and margin required for Green."}
{"case_id":"r8_loop8_krafton_inzoi_adk_ip","symbol":"259960","company_name":"크래프톤","case_type":"success_candidate","primary_archetype":"GAME_CONTENT_IP_REPEAT_MONETIZATION","stage2_date":"2025-04-04","price_validation":{"price_data_source":"Reuters ADK transaction + InZOI sales evidence","stage3_price":null,"adk_transaction_value_jpy_bn":75,"adk_transaction_value_usd_mn":516.21,"inzoi_first_week_sales_mn":1.0,"steam_peak_concurrent_players":87377,"twitch_peak_viewers":175000,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"game_IP_repeat_monetization_watch","notes":"inZOI launch and ADK acquisition are Stage 2; repeat bookings, retention and IP monetization required for Stage 3."}
{"case_id":"r8_loop8_hybe_legal_governance_watch","symbol":"352820","company_name":"HYBE","case_type":"4c_watch","primary_archetype":"PLATFORM_GOVERNANCE_LEGAL_RISK","stage4c_date":"2026-04-21","price_validation":{"price_data_source":"Reuters/AP legal event anchors","stage3_price":null,"stage4c_event_mae_1d_pct":-2.4,"alleged_profit_krw_bn":190,"hard_4c_status":"not_confirmed_warrant_declined","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"governance_legal_overhang","notes":"Legal risk blocks Green; prosecutors later declined warrant, so hard 4C is not confirmed."}
```

## shadow weight row 초안

```csv
archetype,recurring_revenue,arr_proxy,paid_usage,bookings,opm_fcf,ip_monetization,operational_trust,event_penalty,legal_privacy_redteam,4b_watch_sensitivity,notes
B2B_SAAS_ERP_WORKFLOW,+5,+5,+3,+3,+5,+0,+3,-2,+1,+3,Douzone/EQT is Stage 2 until ARR/churn/OPM/FCF confirm.
AI_CLOUD_CAPITAL_ALLOCATION,+3,+3,+3,+2,+5,+0,+3,-5,+2,+5,Samsung SDS KKR event is 4B-watch before AI revenue conversion.
CLOUD_AI_SOFTWARE_INFRA,+4,+4,+3,+2,+5,+0,+3,-4,+2,+4,LG CNS IPO weak price action blocks Green despite cloud/AI sales mix.
WEBTOON_PLATFORM_IP_MONETIZATION,+3,+3,+5,+4,+5,+5,+3,-3,+2,+4,Naver/Webtoon needs paid content, ARPU, IP monetization and FCF.
AI_SOFTWARE_APPLICATION,+2,+2,+5,+2,+4,+0,+3,-5,+2,+5,Kakao/OpenAI partnership is price_moved_without_evidence until monetization.
GAME_CONTENT_IP_REPEAT_MONETIZATION,+3,+0,+4,+5,+5,+5,+3,-3,+2,+4,Krafton needs retention/repeat bookings beyond first-week sales.
PLATFORM_GOVERNANCE_LEGAL_RISK,+0,+0,+0,+0,+0,+0,+5,-3,+5,+4,HYBE legal risk is 4C-watch; hard 4C only after legal outcome materially impairs business.
```

---

# 이번 R8 Loop 8 결론

R8은 Stage 3 후보가 있지만, **false positive가 가장 쉽게 쌓이는 섹터**다.

```text
1. 더존비즈온은 B2B SaaS 구조가 좋아 Stage 2 후보가 된다.
   하지만 EQT 투자 발표가 아니라 ARR·churn·OPM·FCF가 Stage 3다.

2. 삼성SDS는 KKR/AI capital allocation 이벤트로 장중 +20.8% 올랐다.
   이건 Stage 2와 4B-watch이지, AI revenue 전 Stage 3가 아니다.

3. LG CNS는 cloud/AI 매출 비중이 높았지만 IPO 첫날 -3.55%였다.
   좋은 사업 설명만으로 가격검증을 통과하지 못한 케이스다.

4. NAVER/Webtoon은 MAU와 IPO valuation이 강하지만,
   Webtoon은 여전히 손실이고 Naver는 holdco discount를 받는다.
   paid content·ARPU·IP monetization·FCF가 필요하다.

5. 카카오/OpenAI는 전형적인 price_moved_without_evidence다.
   partnership headline은 Stage 1~2이고, monetization 전 Green 금지다.

6. 크래프톤은 inZOI 첫 주 100만 장과 ADK 인수로 Stage 2 후보지만,
   repeat bookings와 retention 전 Stage 3가 아니다.

7. HYBE는 콘텐츠 IP가 좋아도 founder legal risk가 Green을 막는다.
   이번 건은 warrant가 기각되어 hard 4C는 아니지만, governance 4C-watch다.
```

한 문장으로 압축하면:

> **R8에서 진짜 Stage 3는 “AI·게임·웹툰·K-pop이 핫하다”가 아니라, 반복매출·paid usage·bookings·ARR proxy·OPM/FCF가 확인되는 순간이다.**
> **R8은 AI partnership, IPO, M&A, 신작 첫 주 판매, IP 기대를 먼저 4B/Event Premium으로 분리해야 점수표가 산다.**

[1]: https://www.reuters.com/world/asia-pacific/swedish-firm-eqt-shells-out-930-million-slice-south-koreas-douzone-bizon-2025-11-07/?utm_source=chatgpt.com "Swedish firm EQT shells out $930 million for a slice of South Korea's Douzone Bizon"
[2]: https://www.reuters.com/world/asia-pacific/kkr-buy-820-million-samsung-sds-convertible-bonds-shares-jump-20-2026-04-15/?utm_source=chatgpt.com "KKR to buy $820 million of Samsung SDS convertible bonds, shares jump 20%"
[3]: https://www.reuters.com/technology/skorean-tech-services-firm-lg-cns-falls-stock-market-debut-2025-02-05/?utm_source=chatgpt.com "South Korean tech services firm LG CNS drops in market debut"
[4]: https://www.ft.com/content/e362807c-701a-4bc2-9918-58d3bb940e05?utm_source=chatgpt.com "Webtoon Entertainment to debut on Nasdaq as latest Korean cultural export success"
[5]: https://www.marketwatch.com/story/naver-could-get-weaker-valuation-boost-from-webtoon-ipo-market-talk-98b65635?utm_source=chatgpt.com "Naver Could Get Weaker Valuation Boost From Webtoon IPO -- Market Talk"
[6]: https://www.investopedia.com/webtoon-entertainment-stock-rises-further-after-strong-debut-8671110?utm_source=chatgpt.com "Webtoon Entertainment Stock Rises Further After Strong Debut"
[7]: https://www.reuters.com/technology/artificial-intelligence/openai-kakao-jointly-develop-ai-products-south-korea-2025-02-04/?utm_source=chatgpt.com "OpenAI clinches deal with Kakao, talks with SoftBank and Samsung about Stargate"
[8]: https://www.reuters.com/en/south-korean-game-company-krafton-acquire-japans-adk-516-mln-2025-06-24/?utm_source=chatgpt.com "South Korean game company Krafton to acquire Japan's ADK for $516 mln"
[9]: https://en.wikipedia.org/wiki/InZOI?utm_source=chatgpt.com "InZOI"
[10]: https://www.reuters.com/world/asia-pacific/south-korea-police-seek-detention-warrant-hybe-chairman-yonhap-says-2026-04-21/?utm_source=chatgpt.com "South Korea police seek detention warrant for BTS agency founder Bang"
[11]: https://apnews.com/article/625a450e8d721c768c4698bbca3af7f9?utm_source=chatgpt.com "South Korean prosecutors deny police request for arrest warrant for K-pop mogul behind BTS"
