순서상 이번은 **R8 Loop 12 — 플랫폼·콘텐츠·SW·보안 가격경로 검증 라운드**다.

```text
round = R8 Loop 12
round_id = round_192
large_sector = PLATFORM_CONTENT_SW_SECURITY
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true
```

이번 R8 Loop 12는 지난 R8의 Douzone/Samsung SDS/LG CNS/Webtoon/Kakao/OpenAI/Krafton India/SKT/HYBE 반복을 줄이고, **게임 IPO, 키즈·애니 콘텐츠 IPO, K-pop IP 지분거래, 플랫폼·거래소 M&A trust gate, e-commerce data breach, 게임 M&A governance, telecom cybersecurity hard 4C**를 중심으로 본다.

원시 수정주가 일봉 OHLC 전체 구간은 이번 환경에서 안정적으로 확보하지 못했다. 대신 Reuters / FT / Barron’s / IBD / Guardian / WSJ 계열 보도에서 확인된 **가격 anchor, IPO 가격반응, 이벤트 수익률, 거래금액, 매출·영업이익, breach 비용, 법원 판결, abnormal withdrawal**만 계산했다. 30D/90D/180D full OHLC가 없는 항목은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R8 = 플랫폼·콘텐츠·SW·보안
```

R8에서 Stage 3는 “플랫폼”, “AI”, “게임 IP”, “K-content”, “글로벌 흥행”, “M&A”, “IPO”가 아니다.

진짜 Stage 3는 **paid user, ARPU, retention, repeat content hit, IP licensing, ad/commerce take-rate, platform trust, cybersecurity control, operating leverage, FCF**가 같이 닫힐 때다.

---

# 2. 대상 canonical archetype

```text
GAME_IP_IPO_SINGLE_TITLE_RISK
KIDS_CONTENT_IP_IPO_EVENT_PREMIUM
KPOP_IP_CHINA_OPTIONALITY
DIGITAL_ASSET_PLATFORM_M_AND_A_TRUST_GATE
ECOMMERCE_PLATFORM_DATA_BREACH_4C
GAME_STUDIO_M_AND_A_GOVERNANCE_4C
TELECOM_CYBERSECURITY_OPERATIONAL_TRUST_HARD_4C
```

---

# 3. deep sub-archetype

```text
게임 IPO:
- Shift Up
- Goddess of Victory: Nikke
- Stellar Blade
- Sony exclusive / Tencent stake
- single-title concentration / live-service retention

키즈·애니 IP:
- Pinkfong
- Baby Shark / Bebefinn / Sealook
- YouTube views / merchandise / licensing
- IPO event premium vs repeat-hit durability

K-pop IP:
- SM Entertainment
- Tencent Music 9.7% stake
- China performance-ban thaw optionality
- Kakao control stake / China revenue recovery

디지털 플랫폼 M&A:
- NAVER Financial / Dunamu / Upbit
- all-stock deal
- abnormal withdrawal
- exchange trust / crypto-cycle / regulatory approval

E-commerce platform trust:
- Coupang
- 33M+ account data breach
- delayed detection / CEO resignation / police raid
- non-KRX but Korean platform hard reference

게임 M&A governance:
- Krafton / Unknown Worlds / Subnautica 2
- $500M acquisition + $250M earnout
- Delaware court ruling
- franchise trust / developer governance

통신·보안:
- SK Telecom
- USIM / customer data breach
- revenue guidance cut / compensation / fine
- direct KRX hard 4C benchmark
```

---

# 4. 국장 신규 후보 case

## Case A — Shift Up `success_candidate + single-title 4B-watch`

```text
symbol = 462870
case_type = success_candidate + 4B-watch
archetype = GAME_IP_IPO_SINGLE_TITLE_RISK
```

### stage date

```text
Stage 1:
2024-04~06
- Stellar Blade PS5 launch
- Goddess of Victory: Nikke live-service revenue
- Tencent-backed Korean game IPO

Stage 2:
2024-06-27
- IPO top-end pricing expected
- raise 435B won / $313M
- implied market cap 3.5T won / $2.52B
- Nikke booked 255B won sales from global launch to 1Q 2024
- 2023 revenue 169B won
- 2023 OP 111B won

Stage 3:
없음
- IPO와 hit title만으로 Green 금지
- live-service retention, new-title pipeline, PC/console sales, repeat hit, OPM/FCF 확인 필요

Stage 4B:
IPO valuation이 Nikke/Stellar Blade proof보다 먼저 확장되면 watch

Stage 4C:
single-title fade, Tencent/platform risk, Sony exclusivity limit, new-title delay
```

Shift Up은 게임 IP 구조가 강하지만, 이번 라운드에서는 **IPO valuation과 single-title concentration을 분리**한다. Reuters 기준 IPO는 4,350억 원 조달, 시총 3.5조 원으로 책정될 가능성이 있었고, 2023년 매출 1,690억 원, 영업이익 1,110억 원을 기록했다. 이 숫자는 훌륭하지만, Stage 3는 live-service retention과 다음 타이틀 매출이 확인되어야 한다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters IPO / sales / earnings anchor

entry_date:
N/A

stage3_price:
N/A

IPO_raise:
435B won / $313M

implied_market_cap:
3.5T won / $2.52B

Nikke_sales_from_launch_to_1Q2024:
255B won

2023_revenue:
169B won

2023_OP:
111B won

2023_OP_margin:
111 / 169
= 65.7%

IPO_valuation_to_2023_revenue:
3.5T / 169B
= 20.7x

IPO_valuation_to_2023_OP:
3.5T / 111B
= 31.5x

Tencent_post_IPO_stake:
about 35%

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

reason:
- Reuters provides IPO / valuation / sales / OP anchors.
- Reliable adjusted daily OHLC window was not available in this pass.
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = game_IP_IPO_watch
stage_failure_type = IPO_and_hit_title_not_green
```

---

## Case B — Pinkfong `event_premium / kids-content IP IPO`

```text
symbol = Pinkfong Company, KRX newly listed
case_type = event_premium + success_candidate
archetype = KIDS_CONTENT_IP_IPO_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2025-11-18
- Baby Shark / Bebefinn / Sealook IP
- kids content / toy / licensing expansion
- Korean entertainment IPO demand

Stage 2:
2025-11-18
- IPO raised 76B won
- shares intraday +62%
- close +9% at 41,550 won
- Baby Shark video >16B YouTube views
- prior-year sales 97.4B won
- OP 18.8B won

Stage 3:
없음
- Baby Shark legacy IP만으로 Green 금지
- repeat hit, licensing revenue, merchandise margin, platform retention 확인 필요

Stage 4B:
2025-11-18
- intraday +62% IPO pop
```

Pinkfong은 R8 콘텐츠 IP에서 좋은 Stage 2지만, 동시에 IPO event premium이다. FT는 Pinkfong이 IPO로 760억 원을 조달했고, 상장 첫날 장중 +62%, 종가 +9%를 기록했으며, 전년 매출 974억 원과 영업이익 188억 원을 냈다고 보도했다. “Baby Shark”의 160억 회 이상 조회수는 강력한 IP proof지만, Stage 3는 반복 hit와 licensing/merchandise 수익성이 확인될 때다. ([Financial Times][2])

### 실제 가격경로 검증

```text
price_data_source:
FT IPO / price / sales anchor

entry_date:
2025-11-18

stage3_price:
N/A

IPO_raise:
76B won

intraday_MFE:
+62%

close_price:
41,550 won

close_return:
+9%

implied_IPO_price_from_close:
41,550 / 1.09
= about 38,119 won

intraday_high_from_62pct:
38,119 * 1.62
= about 61,552 won

Baby_Shark_views:
>16B

prior_year_sales:
97.4B won

prior_year_OP:
18.8B won

OP_margin:
18.8 / 97.4
= 19.3%

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium
rerating_result = kids_content_IP_IPO_watch
stage_failure_type = IPO_pop_not_repeat_hit_green
```

---

## Case C — SM Entertainment / Tencent Music `success_candidate / China optionality, not Green`

```text
symbol = 041510
case_type = success_candidate
archetype = KPOP_IP_CHINA_OPTIONALITY
```

### stage date

```text
Stage 1:
2025-05-27
- Tencent Music buys 9.7% SM Entertainment stake from HYBE
- possible China K-pop performance thaw
- Kakao / Kakao Entertainment controlling stake remains

Stage 2:
2025-05-30 expected close
- HYBE sells 2.2M SM shares
- deal value 243B won / $177M
- Tencent becomes second-largest shareholder
- Kakao + Kakao Entertainment control 42%

Stage 3:
없음
- 중국 공연 재개 기대만으로 Green 금지
- China concerts, ticket revenue, artist schedule, margin, regulatory durability 확인 필요

Stage 4B:
China thaw 기대만으로 엔터주가 먼저 rerating되면 watch

Stage 4C:
China restriction returns, Kakao governance overhang, artist schedule miss
```

SM Entertainment는 K-pop IP의 China optionality Stage 2다. Reuters는 HYBE가 SM 지분 9.7%, 220만 주를 Tencent Music에 2,430억 원에 매각한다고 보도했고, Tencent는 Kakao/Kakao Entertainment 다음 2대 주주가 된다. 하지만 중국 공연 재개가 실제 티켓 매출과 margin으로 내려오기 전에는 Green이 아니다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters SM / Tencent stake transaction anchor

stage3_price:
N/A

stake_sold:
9.7%

shares_sold:
2.2M shares

transaction_value:
243B won / $177M

implied_SM_equity_value:
243B / 0.097
= about 2.51T won

Kakao_and_Kakao_Entertainment_control_stake:
42%

China_ban_context:
unofficial K-pop performance restrictions since 2016

SM_stock_OHLC:
price_data_unavailable_after_deep_search

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = Kpop_China_optional_reopen_watch
stage_failure_type = shareholder_transaction_not_ticket_revenue_green
```

---

## Case D — NAVER Financial / Dunamu `event_premium + exchange-trust 4C-watch`

```text
symbol = 035420
case_type = success_candidate + event_premium + 4C-watch
archetype = DIGITAL_ASSET_PLATFORM_M_AND_A_TRUST_GATE
```

### stage date

```text
Stage 1:
2025-11-27
- NAVER Financial acquires Dunamu
- Upbit / Naver Pay / fintech / digital asset synergy
- stablecoin and platform finance optionality

Stage 2:
2025-11-27
- all-stock deal value 15.13T won / $10.27B
- exchange ratio 2.54 Naver Financial shares per Dunamu share
- Upbit market share about 70%

Stage 4B:
2025-11-27
- NAVER initially +7%+

Stage 4C-watch:
2025-11-27
- abnormal withdrawal 54B won from Upbit
- NAVER later -4.2%
- Upbit to cover loss with own assets

Stage 3:
없음
- regulatory approval, closing, platform revenue, trust recovery, stablecoin regulation 확인 전 Green 금지
```

NAVER/Dunamu는 R8 플랫폼 M&A에서 가장 좋은 “Stage 2 + trust gate” case다. Reuters는 NAVER Financial이 Dunamu를 15.13조 원 all-stock deal로 인수한다고 보도했고, NAVER 주가는 초반 +7% 이상 올랐다가 Upbit의 540억 원 abnormal withdrawal 뉴스로 -4.2%까지 뒤집혔다. 플랫폼 M&A에서 trust incident가 얼마나 빨리 thesis를 꺾는지 보여준다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters deal / event-return / trust-risk anchor

stage3_price:
N/A

deal_value:
15.13T won / $10.27B

exchange_ratio:
2.54 Naver Financial shares per Dunamu share

Upbit_market_share:
about 70%

event_initial_MFE:
> +7%

event_later_MAE:
-4.2%

event_swing:
-11.2pp

abnormal_withdrawal:
54B won

loss_coverage:
Upbit to cover using own assets

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium_trust_watch
rerating_result = digital_asset_platform_merger_watch
stage_failure_type = platform_stage2_with_exchange_trust_4C_watch
```

---

## Case E — Coupang `platform trust 4C reference / non-KRX`

```text
symbol = CPNG, non-KRX Korean platform reference
case_type = 4C-watch / non-KRX sector reference
archetype = ECOMMERCE_PLATFORM_DATA_BREACH_4C
```

### stage date

```text
Stage 1:
2025-06~11
- unauthorized access via overseas servers
- e-commerce platform data trust risk

Stage 4C-watch:
2025-12-01
- Coupang discloses major data breach affecting 33.7M accounts
- stock down more than 4% at 26.86
- names, phone numbers, emails, shipping addresses, order information exposed
- login credentials and credit card data reportedly not compromised

Stage 4C relief:
2025-12-26
- stock +9.2%
- internal investigation says former employee accessed about 33M accounts but retained data from only about 3,000 customers
- South Korea CEO resignation / Seoul office police raid context

Stage 3:
없음
- platform growth보다 trust restoration, customer retention, regulatory fine, compensation 확인 필요
```

Coupang은 KRX 상장사는 아니지만, 한국 e-commerce platform trust의 hard reference다. IBD는 data breach disclosure 뒤 Coupang 주가가 4% 넘게 하락해 26.86달러 부근에서 거래됐다고 보도했고, Barron’s는 내부 조사 발표 후 데이터가 약 3,000명분만 보관됐다는 점이 안도감을 주며 주가가 9.2% 반등했다고 보도했다. 이 case는 R8에서 “트래픽이 많다”보다 **data governance**가 먼저라는 기준점이다. ([Investors][5])

### 실제 가격경로 검증

```text
price_data_source:
IBD / Barron's breach and event-return anchors

stage3_price:
N/A

breach_affected_accounts:
33.7M

event_MAE:
> -4%

event_price_anchor:
$26.86

retained_data_after_internal_investigation:
about 3,000 customers

retained_data_share:
3,000 / 33,000,000
= 0.0091%

relief_event_MFE:
+9.2%

data_exposed:
names
phone numbers
email
shipping addresses
order information

not_compromised_according_to_company_context:
login credentials
credit card data

MFE_30D / 90D:
price_data_unavailable_after_deep_search

note:
non-KRX Korean platform reference
```

### alignment

```text
score_price_alignment = thesis_break_watch_then_relief
rerating_result = platform_data_trust_4C_reference
stage_failure_type = non_KRX_but_R8_platform_trust_reference
```

---

## Case F — Krafton / Unknown Worlds / Subnautica 2 `game M&A governance 4C-watch`

```text
symbol = 259960
case_type = 4C-watch
archetype = GAME_STUDIO_M_AND_A_GOVERNANCE_4C
```

### stage date

```text
Stage 1:
2021~2025
- Krafton acquired Unknown Worlds
- Subnautica 2 expected franchise expansion
- earnout / studio autonomy agreement

Stage 4C-watch:
2026-03-16
- Delaware court rules against Krafton
- Krafton ordered to reinstate Unknown Worlds CEO Ted Gill
- dispute over $250M earnout
- Unknown Worlds acquired for $500M upfront
- judge says Krafton CEO followed ChatGPT-suggested takeover plan

Stage 3:
없음
- acquired-studio IP expansion is not Green until release, sales, retention, review score, legal risk resolution

Stage 4B:
IP acquisition / Subnautica sequel 기대가 legal governance보다 먼저 가격화되면 watch
```

Krafton은 게임 IP M&A에서 **earnout governance risk**를 보여준다. Reuters는 Delaware court가 Krafton에게 Unknown Worlds CEO를 복귀시키라고 명령했고, 분쟁은 $500M upfront acquisition과 최대 $250M earnout에서 비롯됐다고 보도했다. 게임 M&A는 “좋은 IP를 샀다”가 Stage 3가 아니라, studio governance와 release execution을 통과해야 한다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters legal ruling / acquisition / earnout anchor

stage3_price:
N/A

Unknown_Worlds_acquisition_upfront:
$500M

earnout_at_issue:
up to $250M

court_event:
Krafton ordered to reinstate Unknown Worlds CEO Ted Gill

disputed_action:
studio leadership removal / operational control dispute

Subnautica_2_status:
in development / early access preparation context

Krafton_stock_OHLC:
price_data_unavailable_after_deep_search

MFE / MAE:
price_data_unavailable_after_deep_search

reason:
- Reuters provides legal and deal-value anchors.
- Reliable adjusted KRX OHLC around the ruling was not available in this pass.
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = game_studio_M&A_governance_watch
stage_failure_type = IP_acquisition_not_release_revenue_green
```

---

## Case G — SK Telecom `direct KRX hard 4C / cybersecurity operational trust`

```text
symbol = 017670
case_type = 4C-thesis-break
archetype = TELECOM_CYBERSECURITY_OPERATIONAL_TRUST_HARD_4C
```

### stage date

```text
Stage 1:
2024~2025
- telecom subscriber base / AI telecom / stable cash flow

Stage 4C:
2025-04-28
- cyberattack / customer data leak disclosed
- shares intraday -8.5%
- close -6.7%
- KOSPI +0.1%
- 23M users offered free USIM replacement

Stage 4C 강화:
2025-07-04
- 26.96M pieces of user data leaked
- shares close -5.6%
- 700B won / 5-year data-protection investment
- 2025 revenue forecast cut by 800B won
- customer benefit package cost about 500B won

Stage 4C 강화:
2025-12-21
- consumer agency to order compensation for 58 users
- 100,000 won per applicant
- agency may seek compensation for all victims
- possible total cost nearly 2.3T won

Stage 3:
없음
- trust recovery, churn, revenue guidance restoration, security audit 통과 전 Green 금지
```

SK Telecom은 R8 direct-KRX hard 4C benchmark다. Reuters는 최초 disclosure day에 SKT가 장중 -8.5%, 종가 -6.7% 하락했고, KOSPI는 +0.1%였다고 보도했다. 7월에는 2,696만 건 user data leak, 7,000억 원 보안투자, 2025년 매출전망 8,000억 원 하향이 확인됐다. 12월에는 소비자원이 피해자 보상명령을 추진하며 전 피해자로 확대할 경우 총 비용이 2.3조 원에 이를 수 있다고 보도됐다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters breach / July investigation / compensation anchors

stage3_price:
N/A

initial_intraday_MAE:
-8.5%

initial_close_MAE:
-6.7%

KOSPI_same_context:
+0.1%

relative_underperformance_initial_close:
-6.7 - 0.1
= -6.8pp

affected_users_initial:
23M

protection_service_signups:
5.54M

protection_signup_share:
5.54 / 23
= 24.1%

July_event_MAE:
-5.6%

leaked_data_pieces:
26.96M

data_protection_investment:
700B won over 5 years

annualized_security_investment:
700 / 5
= 140B won/year

2025_revenue_forecast_cut:
800B won

customer_benefit_package:
about 500B won

individual_compensation_order:
100,000 won per applicant

applicant_count:
58

possible_all_victim_compensation_cost:
nearly 2.3T won

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = cybersecurity_operational_trust_break
stage_failure_type = hard_4C
```

---

# 5. 이번 R8 case별 요약표

| case                 | 분류                     |                                                                  실제 가격검증 | alignment           |
| -------------------- | ---------------------- | -----------------------------------------------------------------------: | ------------------- |
| Shift Up             | success_candidate + 4B |               IPO value/revenue 20.7x, OP margin 65.7%, OHLC unavailable | game IP Stage 2     |
| Pinkfong             | event premium          |                                intraday +62%, close +9%, OP margin 19.3% | content IPO 4B      |
| SM / Tencent         | success_candidate      |                              243B won for 9.7%, implied equity 2.51T won | China optionality   |
| NAVER / Dunamu       | event + 4C-watch       |                                 +7% → -4.2%, abnormal withdrawal 54B won | platform trust gate |
| Coupang              | non-KRX 4C reference   |                                         -4%, later +9.2%, 33.7M accounts | data trust          |
| Krafton / Subnautica | 4C-watch               |               $500M acquisition, $250M earnout dispute, OHLC unavailable | M&A governance      |
| SK Telecom           | hard 4C                | -8.5% / -6.7%, later -5.6%, revenue cut 800B, possible compensation 2.3T | direct hard 4C      |

---

# 6. score-price alignment 판정

```text
success_candidate:
- Shift Up
- SM Entertainment / Tencent
- NAVER / Dunamu, but with exchange trust gate
- Krafton, only if Subnautica legal overhang clears
- CJ / Olive Young는 이번 라운드에서 제외하고 R5에서 처리

event_premium:
- Pinkfong IPO
- NAVER / Dunamu initial +7%
- Shift Up IPO valuation if price moves before repeat-title revenue

price_moved_without_evidence:
- Pinkfong intraday +62% before repeat-hit / licensing proof
- Shift Up IPO valuation before next title / retention proof
- SM China thaw expectation before concerts/ticket revenue

thesis_break_watch:
- NAVER / Dunamu abnormal withdrawal
- Coupang data breach
- Krafton / Unknown Worlds legal-governance dispute

hard_4C:
- SK Telecom cybersecurity operational trust break

non_KRX_reference:
- Coupang platform data breach
```

---

# 7. 점수비중 교정

## 올릴 축

```text
paid_user_retention +5
ARPU_or_take_rate +5
repeat_hit_generation +5
IP_licensing_revenue +5
live_service_retention +5
platform_trust +5
cybersecurity_control +5
data_governance +5
regulatory_closing +4
operating_leverage_FCF +5
```

### 왜 올리나

Shift Up은 IP와 수익성이 강하지만 next hit와 retention이 필요하다. Pinkfong은 Baby Shark legacy IP가 강하지만 repeat content hit와 licensing/merchandise margin이 필요하다. NAVER/Dunamu와 Coupang/SKT는 플랫폼 규모보다 trust와 data governance가 먼저다. Krafton은 좋은 IP를 사도 studio governance가 깨지면 release execution이 흔들린다.

## 내릴 축

```text
IPO_pop_only -5
single_title_or_single_IP_concentration -5
M&A_deal_without_closing -4
China_reopening_optional_only -4
digital_asset_platform_without_trust -5
exchange_abnormal_withdrawal -5
data_breach -5
cybersecurity_revenue_cut -5
unlisted_or_non_KRX_reference_gap -3
event_rally_before_paid_usage -5
```

### 왜 내리나

Pinkfong의 +62%는 content IPO event premium이다. Shift Up은 valuation이 높고 Nikke/Stellar Blade concentration이 있다. SM/Tencent는 China reopening optionality지만 실제 공연 매출 전 Green이 아니다. NAVER/Dunamu는 deal과 동시에 trust incident가 나왔다. SKT는 data breach가 매출전망 하향과 보상·투자비로 내려왔다.

## Green gate 강화 조건

```text
R8 Stage 3-Green 필수:
1. paid user / active user retention 확인
2. ARPU / take-rate / ad-commerce monetization 확인
3. repeat content hit 또는 live-service durability 확인
4. IP licensing / merchandise / platform fee revenue 확인
5. operating leverage / FCF 확인
6. M&A는 closing + integration + revenue bridge 확인
7. platform trust / exchange trust 문제 없음
8. cybersecurity / data governance hard risk 없음
9. 가격경로가 evidence 이후 따라옴

금지:
IPO pop only
single-title hit only
single-IP legacy only
M&A announcement only
China reopening expectation only
crypto/platform deal without trust recovery
data breach unresolved
cybersecurity remediation 비용 불명
```

## 4B 조기감지 조건

```text
4B-watch:
IPO 첫날 +50~60% 이상 급등
single IP / single title valuation이 revenue보다 먼저 확장
M&A announcement로 +5~10% 이상 급등
China reopening headline로 K-content 주가 선반영
platform deal이 regulatory closing 전 가격화
digital-asset platform이 trust incident 전후로 급등락
content IP가 조회수만으로 고평가

4B-elevated:
repeat hit 미확인
licensing/merchandise margin 미확인
active user retention 약함
platform trust incident 동시 발생
data breach 조사 중
M&A legal dispute 존재
```

## 4C hard gate 조건

```text
major data breach
cybersecurity breach with revenue guidance cut
platform trust failure
exchange abnormal withdrawal / hack
M&A governance dispute that delays release
regulatory approval failure
content/IP single-hit fade
live-service retention collapse
large compensation / fine / remediation cost
```

이번 R8 Loop 12의 hard 4C는 **SK Telecom cybersecurity operational trust break**로 확정한다. Coupang은 non-KRX이므로 sector hard reference로 둔다. NAVER/Dunamu, Krafton, SM, Pinkfong, Shift Up은 각각 4C-watch 또는 4B-watch다.

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
```

---

# 9. patch-ready 출력

## docs/round/round_192.md 요약

```md
# R8 Loop 12. Platform / Content / Software / Security Price Validation

이번 라운드는 R8 Loop 12 price-validation 라운드다.

핵심 결론:
- Shift Up is game-IP Stage 2, not Green. IPO raise 435B won, implied market cap 3.5T won, 2023 revenue 169B won, OP 111B won, OP margin 65.7%. But live-service retention, next hit, OPM/FCF and single-title concentration must be checked.
- Pinkfong is kids-content IP IPO event premium. IPO raised 76B won; shares jumped as much as +62% and closed +9% at 41,550 won. Prior-year sales 97.4B won, OP 18.8B won. Repeat-hit and licensing margin required.
- SM Entertainment / Tencent is K-pop China optionality Stage 2. Tencent Music buys 9.7% from HYBE for 243B won, implied equity value about 2.51T won. Actual China concerts/ticket revenue needed.
- NAVER / Dunamu is platform M&A Stage 2 plus exchange-trust 4C-watch. Deal value 15.13T won, NAVER initially +7% but later -4.2% after Upbit abnormal withdrawal of 54B won.
- Coupang is non-KRX platform trust 4C reference. 33.7M accounts affected; stock down more than 4% at $26.86, later +9.2% after internal investigation said retained data involved only about 3,000 customers.
- Krafton / Unknown Worlds / Subnautica 2 is game M&A governance 4C-watch. Krafton acquired Unknown Worlds for $500M upfront with up to $250M earnout; Delaware court ordered reinstatement of CEO Ted Gill.
- SK Telecom is direct KRX hard 4C. Initial event -8.5% intraday and -6.7% close vs KOSPI +0.1%; 26.96M data pieces leaked, 700B won security investment, 800B won revenue forecast cut, potential all-victim compensation nearly 2.3T won.
```

## docs/checkpoints/checkpoint_28a_round192_r8_loop12.md 요약

```md
# Checkpoint 28A Round 192 R8 Loop 12 Platform Content SW Security Price Validation

## 반영 내용
- R8 Loop 12 price-validation 라운드를 추가했다.
- Game IPO, kids-content IPO, K-pop China optionality, digital-asset platform M&A, e-commerce data breach, game studio M&A governance, telecom cybersecurity hard 4C를 비교했다.
- Reuters / FT / Barron’s / IBD / Guardian anchors로 가능한 MFE/MAE 및 event metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- paid user retention, ARPU/take-rate, repeat-hit generation, IP licensing revenue, live-service retention, platform trust, cybersecurity control, data governance, operating leverage/FCF 가중치 강화
- IPO pop-only, single-title/IP concentration, M&A deal without closing, China reopening-only, digital-asset platform without trust, data breach, cybersecurity revenue cut 감점 강화
```

## data/e2r_case_library/cases_r8_loop12_round192.jsonl 초안

```jsonl
{"case_id":"r8_loop12_shift_up_game_ip_ipo_single_title_watch","symbol":"462870","company_name":"Shift Up","case_type":"success_candidate","primary_archetype":"GAME_IP_IPO_SINGLE_TITLE_RISK","stage2_date":"2024-06-27","stage4b_date":"IPO_valuation_watch","price_validation":{"price_data_source":"Reuters IPO / sales / earnings anchor","stage3_price":null,"ipo_raise_krw_bn":435,"ipo_raise_usd_mn":313,"implied_market_cap_krw_trn":3.5,"implied_market_cap_usd_bn":2.52,"nikke_sales_launch_to_1q2024_krw_bn":255,"revenue_2023_krw_bn":169,"op_2023_krw_bn":111,"op_margin_2023_pct":65.7,"ipo_valuation_to_revenue_2023":20.7,"ipo_valuation_to_op_2023":31.5,"tencent_post_ipo_stake_pct":35,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"game_IP_IPO_watch","notes":"Strong game-IP economics, but IPO and hit title are not Green until retention, repeat hit, pipeline and FCF confirm."}
{"case_id":"r8_loop12_pinkfong_kids_content_ip_ipo_event","symbol":"Pinkfong_newly_listed","company_name":"Pinkfong Company","case_type":"event_premium","primary_archetype":"KIDS_CONTENT_IP_IPO_EVENT_PREMIUM","stage2_date":"2025-11-18","stage4b_date":"2025-11-18","price_validation":{"price_data_source":"FT IPO / price / sales anchor","stage3_price":null,"ipo_raise_krw_bn":76,"intraday_mfe_pct":62,"close_price_krw":41550,"close_return_pct":9,"implied_ipo_price_krw":38119,"implied_intraday_high_krw":61552,"baby_shark_views_bn":16,"prior_year_sales_krw_bn":97.4,"prior_year_op_krw_bn":18.8,"op_margin_pct":19.3,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium","rerating_result":"kids_content_IP_IPO_watch","notes":"IPO pop is 4B/event premium; repeat hit, licensing, merchandise margin and platform retention required before Green."}
{"case_id":"r8_loop12_sm_tencent_kpop_china_optionality","symbol":"041510","company_name":"SM Entertainment / Tencent Music","case_type":"success_candidate","primary_archetype":"KPOP_IP_CHINA_OPTIONALITY","stage2_date":"2025-05-27/2025-05-30","price_validation":{"price_data_source":"Reuters SM / Tencent stake transaction anchor","stage3_price":null,"stake_sold_pct":9.7,"shares_sold_mn":2.2,"transaction_value_krw_bn":243,"transaction_value_usd_mn":177,"implied_sm_equity_value_krw_trn":2.51,"kakao_kakaoent_control_stake_pct":42,"china_ban_context":"unofficial K-pop performance restrictions since 2016","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"Kpop_China_optional_reopen_watch","notes":"Shareholder transaction and China thaw optionality are Stage 2; ticket revenue, artist schedule and regulatory durability required before Green."}
{"case_id":"r8_loop12_naver_dunamu_platform_merger_trust_gate","symbol":"035420","company_name":"NAVER / NAVER Financial / Dunamu","case_type":"success_candidate","primary_archetype":"DIGITAL_ASSET_PLATFORM_M_AND_A_TRUST_GATE","stage2_date":"2025-11-27","stage4b_date":"2025-11-27","stage4c_date":"2025-11-27_watch","price_validation":{"price_data_source":"Reuters deal/event-return/trust-risk anchor","stage3_price":null,"deal_value_krw_trn":15.13,"deal_value_usd_bn":10.27,"exchange_ratio_naver_financial_per_dunamu":2.54,"upbit_market_share_pct":70,"event_initial_mfe_pct":7,"event_later_mae_pct":-4.2,"event_swing_pp":-11.2,"abnormal_withdrawal_krw_bn":54,"loss_coverage":"Upbit to cover using own assets","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_trust_watch","rerating_result":"digital_asset_platform_merger_watch","notes":"Digital-asset platform M&A is Stage 2 but exchange abnormal withdrawal creates 4C-watch."}
{"case_id":"r8_loop12_coupang_platform_data_breach_reference","symbol":"CPNG_non_KRX","company_name":"Coupang","case_type":"4c_watch_reference","primary_archetype":"ECOMMERCE_PLATFORM_DATA_BREACH_4C","stage4c_date":"2025-12-01","stage2_date":"2025-12-26_relief","price_validation":{"price_data_source":"IBD / Barron's breach and event-return anchors","stage3_price":null,"breach_affected_accounts_mn":33.7,"event_mae_pct":-4,"event_price_anchor_usd":26.86,"retained_data_customers_after_investigation":3000,"retained_data_share_pct":0.0091,"relief_event_mfe_pct":9.2,"data_exposed":["names","phone numbers","email","shipping addresses","order information"],"not_compromised_company_context":["login credentials","credit card data"],"price_validation_status":"reported_event_anchor_not_full_ohlc_non_KRX"},"score_price_alignment":"thesis_break_watch_then_relief","rerating_result":"platform_data_trust_4C_reference","notes":"Non-KRX but important Korean platform trust reference; growth cannot override data-governance breach."}
{"case_id":"r8_loop12_krafton_unknown_worlds_subnautica_governance_watch","symbol":"259960","company_name":"Krafton / Unknown Worlds / Subnautica 2","case_type":"4c_watch","primary_archetype":"GAME_STUDIO_M_AND_A_GOVERNANCE_4C","stage4c_date":"2026-03-16","price_validation":{"price_data_source":"Reuters legal ruling / acquisition / earnout anchor","stage3_price":null,"unknown_worlds_acquisition_upfront_usd_mn":500,"earnout_at_issue_usd_mn":250,"court_event":"Krafton ordered to reinstate Unknown Worlds CEO Ted Gill","disputed_action":"studio leadership removal / operational control dispute","subnautica_2_status":"in development / early access preparation context","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"game_studio_M&A_governance_watch","notes":"Acquired IP is not Green until release, sales, retention and legal/governance overhang clear."}
{"case_id":"r8_loop12_skt_cybersecurity_operational_trust_hard_4c","symbol":"017670","company_name":"SK Telecom","case_type":"4c_thesis_break","primary_archetype":"TELECOM_CYBERSECURITY_OPERATIONAL_TRUST_HARD_4C","stage4c_date":"2025-04-28/2025-07-04/2025-12-21","price_validation":{"price_data_source":"Reuters breach / July investigation / compensation anchors","stage3_price":null,"initial_intraday_mae_pct":-8.5,"initial_close_mae_pct":-6.7,"kospi_same_context_pct":0.1,"relative_underperformance_initial_close_pp":-6.8,"affected_users_initial_mn":23,"protection_service_signups_mn":5.54,"protection_signup_share_pct":24.1,"july_event_mae_pct":-5.6,"leaked_data_pieces_mn":26.96,"data_protection_investment_krw_bn":700,"annualized_security_investment_krw_bn":140,"revenue_forecast_cut_2025_krw_bn":800,"customer_benefit_package_krw_bn":500,"individual_compensation_order_krw":100000,"applicant_count":58,"possible_all_victim_compensation_cost_krw_trn":2.3,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"cybersecurity_operational_trust_break","notes":"Direct KRX hard 4C: breach caused price drop, revenue-cut, security investment, compensation and possible broader liabilities."}
```

## data/sector_taxonomy/score_weight_profiles_round192_r8_loop12_v1.csv 초안

```csv
archetype,paid_user_retention,arpu_take_rate,repeat_hit_generation,ip_licensing_revenue,live_service_retention,platform_trust,cybersecurity_control,data_governance,regulatory_closing,operating_leverage_fcf,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
GAME_IP_IPO_SINGLE_TITLE_RISK,+5,+5,+5,+3,+5,+3,+2,+2,+1,+5,-5,+5,+4,Shift Up needs retention, repeat hit and pipeline beyond IPO valuation.
KIDS_CONTENT_IP_IPO_EVENT_PREMIUM,+4,+3,+5,+5,+2,+3,+2,+2,+1,+5,-5,+5,+3,Pinkfong IPO pop is event premium until repeat IP and licensing margin confirm.
KPOP_IP_CHINA_OPTIONALITY,+4,+4,+4,+5,+2,+3,+2,+2,+4,+4,-4,+5,+4,SM/Tencent China optionality requires concerts/ticket revenue and durable permission.
DIGITAL_ASSET_PLATFORM_M_AND_A_TRUST_GATE,+5,+5,+3,+2,+2,+5,+5,+5,+5,+5,-5,+5,+5,Naver/Dunamu needs closing, regulated revenue and exchange trust recovery.
ECOMMERCE_PLATFORM_DATA_BREACH_4C,+5,+5,+2,+1,+3,+5,+5,+5,+4,+5,0,+4,+5,Coupang shows platform scale is fragile when data governance breaks.
GAME_STUDIO_M_AND_A_GOVERNANCE_4C,+4,+4,+5,+5,+4,+4,+2,+2,+4,+5,-4,+5,+4,Krafton/Unknown Worlds shows acquired IP needs governance and release execution.
TELECOM_CYBERSECURITY_OPERATIONAL_TRUST_HARD_4C,+3,+3,+0,+0,+0,+5,+5,+5,+5,+5,0,+4,+5,SKT breach is hard 4C with revenue-cut, remediation and compensation liabilities.
```

---

# 이번 R8 Loop 12 결론

```text
1. Shift Up은 game IP Stage 2다.
   하지만 IPO valuation과 hit title만으로 Stage 3는 아니다. retention, repeat hit, FCF가 필요하다.

2. Pinkfong은 kids-content IP Stage 2와 IPO event premium이 동시에 붙는다.
   +62% IPO pop은 4B다. repeat IP와 licensing margin 전 Green 금지다.

3. SM/Tencent는 K-pop China optionality Stage 2다.
   지분거래와 중국 공연 재개 기대는 좋지만, 실제 ticket revenue 전 Stage 3는 아니다.

4. NAVER/Dunamu는 platform M&A Stage 2와 exchange-trust 4C-watch가 동시에 떴다.
   +7%에서 -4.2%로 뒤집힌 가격경로가 trust gate를 보여준다.

5. Coupang은 non-KRX지만 R8 platform data-trust reference다.
   33.7M account breach는 platform scale보다 data governance가 먼저라는 증거다.

6. Krafton/Unknown Worlds는 game M&A governance 4C-watch다.
   IP acquisition은 release execution과 earnout/governance를 통과해야 한다.

7. SK Telecom은 direct KRX hard 4C다.
   data breach가 주가, 매출전망, 보안투자, 보상비용으로 바로 내려왔다.
```

한 문장으로 압축하면:

> **R8에서 진짜 Stage 3는 “플랫폼·게임·K-content·M&A·IPO가 핫하다”가 아니라, paid retention·ARPU·repeat hit·IP monetization·platform trust·cybersecurity·FCF가 실제로 닫히는 순간이다.**

[1]: https://www.reuters.com/markets/deals/tencent-backed-shift-up-may-price-ipo-top-end-band-source-says-2024-06-27/?utm_source=chatgpt.com "Tencent-backed Shift Up may price IPO at top end of band, source says"
[2]: https://www.ft.com/content/d79a36bb-e985-43d5-843d-4a7199d2bafb?utm_source=chatgpt.com "'Baby Shark' creator Pinkfong pops in trading debut"
[3]: https://www.reuters.com/business/media-telecom/tencent-become-second-largest-shareholder-k-pop-agency-sm-entertainment-2025-05-27/?utm_source=chatgpt.com "Tencent to become second-largest shareholder in K-Pop agency SM Entertainment"
[4]: https://www.reuters.com/world/asia-pacific/navers-payment-arm-acquire-south-korean-crypto-exchange-operator-10-bln-deal-2025-11-27/?utm_source=chatgpt.com "Naver's payment arm to acquire South Korean crypto exchange operator in $10 bln deal"
[5]: https://www.investors.com/news/technology/coupang-stock-slide-data-breach-korea/?utm_source=chatgpt.com "Coupang Stock Slides After E-Commerce Company Reveals Data Breach"
[6]: https://www.reuters.com/legal/litigation/us-court-rules-against-s-korean-gaming-company-its-ai-hatched-takeover-plan-2026-03-16/?utm_source=chatgpt.com "US court rules against S Korean gaming company and its AI-hatched takeover plan"
[7]: https://www.reuters.com/sustainability/boards-policy-regulation/sk-telecom-shares-plunge-after-data-breach-due-cyberattack-2025-04-28/?utm_source=chatgpt.com "SK Telecom shares plunge after data breach due to cyberattack"
