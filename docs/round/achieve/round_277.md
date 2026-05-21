순서상 이번은 **R8 Loop 13 — 플랫폼·콘텐츠·SW·보안 가격경로 검증 라운드**다.

```text
round = R8 Loop 13
round_id = round_205
large_sector = PLATFORM_CONTENT_SW_SECURITY
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true_for_security_trust
next_round = R9 Loop 13
```

이번 R8 Loop 13은 **NAVER/Line Yahoo data-sovereignty, Webtoon Entertainment IPO, Kakao/SM governance, HYBE/ADOR·IPO legal risk, Shift Up game-IP IPO, LG CNS AI/cloud IPO, Krafton India expansion, SK Telecom cybersecurity breach**를 본다.

이번에도 KRX/Naver/Yahoo/Stooq 기준 **수정주가 일봉 전체 구간**은 안정적으로 확보하지 못했다. 그래서 30D/90D/180D full OHLC는 만들지 않고, Reuters / FT / AP / MarketWatch 등에서 확인된 **event return, IPO price, issue price, valuation, MAU, 매출·영업이익, breach cost, fine, 고객수, 규제 anchor**만 계산했다. full OHLC가 필요한 칸은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R8 = 플랫폼·콘텐츠·SW·보안
```

R8에서 진짜 Stage 3는 “MAU가 많다”, “IPO가 됐다”, “웹툰 글로벌화”, “K-pop IP”, “게임 신작”, “AI/cloud”, “데이터센터”, “보안주 수혜”라는 말이 아니다.

진짜 Stage 3는 **유료 전환, ARPU, take-rate, creator economics, IP 재투자, cloud/AI recurring revenue, churn 방어, data-governance, cybersecurity trust, regulatory clearance, 실제 OP/FCF**가 같이 닫히는 순간이다.

---

# 2. 대상 canonical archetype

```text
DATA_SOVEREIGNTY_PLATFORM_4C_WATCH
GLOBAL_CONTENT_PLATFORM_IPO_NOT_PARENT_GREEN
PLATFORM_GOVERNANCE_LEGAL_4C_WATCH
KPOP_IP_GOVERNANCE_4C_WATCH
GAME_IP_MONETIZATION_IPO_STAGE2
AI_CLOUD_IT_SERVICE_IPO_QUALITY_GATE
EMERGING_MARKET_GAME_PLATFORM_OPTION
CYBERSECURITY_TRUST_HARD_4C
```

---

# 3. deep sub-archetype

```text
플랫폼 / 데이터 주권:
- NAVER / LY Corp / Line Yahoo
- Japan administrative guidance
- Naver Cloud-linked data leak
- SoftBank control discussion
- data sovereignty vs platform governance

웹툰 / 글로벌 콘텐츠:
- Webtoon Entertainment / NAVER
- Nasdaq IPO
- 170M MAU, 150+ countries
- Line Manga, Wattpad, Naver Webtoon
- net loss vs platform growth
- parent NAVER value bridge

플랫폼 governance / 콘텐츠 M&A:
- Kakao / SM Entertainment
- founder arrest / later acquittal
- KakaoBank control risk
- AI investments / IPO pipeline risk

K-pop IP governance:
- HYBE / ADOR / NewJeans
- Bang Si-hyuk IPO-fraud investigation
- artist IP concentration
- shareholder trust / legal overhang

게임:
- Shift Up / Goddess of Victory: Nikke / Stellar Blade
- Tencent stake
- IPO pop / game-IP concentration
- sequel / PC port / China launch / review backlash

AI/cloud SW:
- LG CNS
- IPO weak debut
- cloud and AI 54% of sales
- M&A use of proceeds
- AI/cloud recurring revenue vs IPO valuation

India platform option:
- Krafton / BGMI / Naver / Mirae Asset India fund
- BGMI 240M+ downloads
- regulatory volatility / data-security history
- gaming platform optionality vs another-hit risk

보안 hard gate:
- SK Telecom data breach
- USIM replacement
- 26.96M data pieces leaked
- 700B won security investment
- revenue forecast cut 800B won
- 134B won fine
```

---

# 4. 국장 신규 후보 case

## Case A — NAVER / Line Yahoo `data-sovereignty 4C-watch`

```text
symbol = 035420
case_type = 4C-watch
archetype = DATA_SOVEREIGNTY_PLATFORM_4C_WATCH
```

### stage date

```text
Stage 1:
2023-11 ~ 2024-04
- Line Yahoo data leak
- unauthorized access through Naver Cloud-linked system
- Japan administrative guidance
- data sovereignty / capital-control debate

Stage 4C-watch:
2024-04-27 / 2024-05-10
- South Korea says it will consult Naver after report of Japan pressure to divest stake
- SoftBank in talks with Naver over control of LY Corp
- data leak involved more than 300,000 Line users and others in Reuters source
- Japan guidance asks LY Corp to review capital-control relationship with Naver as major subcontractor
- LY Corp to stop outsourcing to Naver

Stage 2 relief:
2024-08-02
- LY Corp 150B yen / $1.01B buyback
- A Holdings voting rights to fall from 64.42% to as low as 62.50%
- buyback price 388 yen, roughly 11% premium to prior close

Stage 3:
없음
- 플랫폼 이용자 기반은 크지만, data-governance / Japan regulatory clearance / capital structure clarity 전 Green 금지
```

NAVER/Line Yahoo는 R8에서 “플랫폼은 MAU보다 data sovereignty가 먼저”라는 표본이다. Reuters는 Line Yahoo data leak 이후 일본 정부가 LY Corp의 Naver 의존과 자본관계를 재검토하라고 요구했고, SoftBank가 NAVER와 control 논의를 하고 있다고 보도했다. LY Corp의 1500억 엔 buyback은 유동성 요건 완화와 지분권 희석 relief지만, 플랫폼 Green은 아니다. 데이터 보안과 규제 신뢰가 깨지면 해외 플랫폼 control 자체가 흔들린다. ([Reuters][1])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters data leak / SoftBank talks / LY buyback anchors",
  "stage3_price": null,
  "data_leak_records_context": "more_than_300000_Line_users_and_others_in_Reuters_source",
  "ly_corp_market_value_may2024_jpy_trn": 2.77,
  "ly_corp_market_value_may2024_usd_bn": 17.77,
  "a_holdings_pre_buyback_voting_rights_pct": 64.42,
  "a_holdings_post_buyback_low_voting_rights_pct": 62.50,
  "voting_rights_decline_pp": -1.92,
  "buyback_value_jpy_bn": 150,
  "buyback_value_usd_bn": 1.01,
  "buyback_price_jpy": 388,
  "buyback_premium_pct": 11,
  "naver_ohlc": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = data_sovereignty_platform_4C_watch
stage_failure_type = overseas_platform_control_not_green_without_data_governance
```

---

## Case B — NAVER / Webtoon Entertainment IPO `success_candidate + parent value bridge gap`

```text
symbol = 035420 / WBTN
case_type = success_candidate + event_premium
archetype = GLOBAL_CONTENT_PLATFORM_IPO_NOT_PARENT_GREEN
```

### stage date

```text
Stage 1:
2024-06-26
- Webtoon Entertainment prices U.S. IPO at top of range
- NAVER-backed global webtoon platform
- Korean digital-content export / IP adaptation narrative

Stage 2:
2024-06-27
- Webtoon sells 15M shares at $21
- IPO raises $315M
- valuation about $2.67B
- about 170M MAU in 150+ countries
- Naver U.Hub buys $50M private placement
- BlackRock interest up to $50M

Stage 4B:
2024-06-27
- Webtoon shares rise as much as +14.3% to $24 in Nasdaq debut

Stage 4C-watch / quality gate:
2024 filing context
- 2023 revenue $1.28B
- 2023 net loss $145M
- FT says difficult for IPO to boost parent NAVER shares amid Line Yahoo data-sovereignty spat

Stage 3:
없음
- Webtoon IPO는 Stage 2
- NAVER Green은 Webtoon monetization, paid conversion, creator economics, ad/take-rate, parent value bridge 필요
```

Webtoon IPO는 R8 content-platform success_candidate지만, NAVER 주주에게는 곧바로 Green이 아니다. Reuters는 Webtoon이 15M shares를 $21에 팔아 $315M을 조달했고, valuation은 $2.67B라고 보도했다. 플랫폼은 170M MAU를 갖고 있지만, FT는 2023년 Webtoon이 $1.28B 매출에 $145M 순손실을 냈고, Line Yahoo data-sovereignty 논란 때문에 IPO가 NAVER 주가에 직접 boost를 주기 어렵다고 평가했다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters / FT Webtoon IPO anchors",
  "stage3_price": null,
  "ipo_price_usd": 21,
  "shares_sold_mn": 15,
  "ipo_raise_usd_mn": 315,
  "valuation_usd_bn": 2.67,
  "debut_high_usd": 24,
  "debut_mfe_pct": 14.3,
  "opened_at_usd": 21.30,
  "naver_private_placement_usd_mn": 50,
  "blackrock_indicated_interest_usd_mn": 50,
  "monthly_active_users_mn": 170,
  "countries": 150,
  "webtoon_2023_revenue_usd_bn": 1.28,
  "webtoon_2023_net_loss_usd_mn": 145,
  "naver_parent_value_bridge_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_event_premium
rerating_result = global_content_platform_IPO_stage2
stage_failure_type = IPO_MAU_not_parent_EPS_green
```

---

## Case C — Kakao / SM Entertainment legal overhang `platform governance 4C-watch`

```text
symbol = 035720
case_type = 4C-watch
archetype = PLATFORM_GOVERNANCE_LEGAL_4C_WATCH
```

### stage date

```text
Stage 1:
2023-03
- Kakao enters SM Entertainment control battle
- platform + K-pop IP expansion
- Kakao’s content strategy tied to SM acquisition

Stage 4C-watch:
2024-07-22 / 2024-07-23
- Kakao founder Kim Beom-su arrested on suspected stock manipulation during SM acquisition
- Kakao shares fall -3.4%
- risk: AI investment, overseas expansion, IPO pipeline, KakaoBank control if convicted of financial crime

Stage 2 relief:
2025-10-21
- South Korean court clears Kakao founder of stock manipulation charges, Yonhap reported via Reuters
- prosecutors had sought 15-year prison sentence and 500M won fine
- legal overhang eased but governance-risk history remains

Stage 3:
없음
- SM ownership and platform content strategy need earnings/IP monetization proof, not just acquisition
```

Kakao/SM은 R8 platform governance calibration이다. Kakao의 SM 인수는 content IP 확장 Stage 2였지만, founder arrest가 나오자 Kakao shares는 -3.4% 하락했다. Reuters는 이 사건이 Kakao의 AI investments, 해외 expansion, IPO pipeline, KakaoBank control risk까지 건드릴 수 있다고 설명했다. 2025년 무죄 판결은 relief지만, 이 case는 `founder/legal overhang`을 R8 hard gate 후보로 남긴다. ([Reuters][3])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters Kakao arrest/acquittal anchors",
  "stage3_price": null,
  "arrest_event_date": "2024-07-23",
  "kakao_event_mae_pct": -3.4,
  "kim_beom_su_kakao_stake_pct": 24,
  "kakao_group_value_context_krw_trn": 86,
  "kakao_group_value_context_usd_bn": 62,
  "prosecutor_sought_sentence_years": 15,
  "prosecutor_sought_fine_krw_mn": 500,
  "acquittal_date": "2025-10-21",
  "sm_content_monetization_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break_watch_then_relief
rerating_result = platform_content_MA_governance_gate
stage_failure_type = founder_legal_overhang_not_content_green
```

---

## Case D — HYBE / ADOR / Bang Si-hyuk legal risk `content IP governance 4C-watch`

```text
symbol = 352820
case_type = 4C-watch
archetype = KPOP_IP_GOVERNANCE_4C_WATCH
```

### stage date

```text
Stage 1:
2024-04-22
- HYBE audits ADOR management
- NewJeans IP / label independence dispute
- multi-label governance risk

Stage 4C-watch:
2024-04-24
- Reuters: HYBE shares drop nearly -8%
- dispute with Min Hee-jin / ADOR returns K-pop infighting to market focus

Stage 4C-watch 강화:
2025-07-24
- police raid HYBE offices over founder Bang Si-hyuk share probe
- investigation linked to alleged unfair share trading around 2020 IPO

Stage 4C-watch 추가:
2026-04-21
- police seek detention warrant for Bang Si-hyuk
- allegation: deceiving early IPO investors, profit arrangement about 190B won / $129.1M
- HYBE shares fall -2.4% despite general market uptick

Stage 2 relief:
2026-04-24
- prosecutors deny police request for arrest warrant, saying detention grounds insufficient, but investigation continues

Stage 3:
없음
- BTS/NewJeans/IP strength is not Green if label governance and founder legal risk remain unresolved
```

HYBE는 R8 content IP governance의 대표 case다. NewJeans/ADOR dispute에서 HYBE shares는 nearly -8% 하락했고, 이후 Bang Si-hyuk IPO-related investigation까지 겹치면서 2026년 detention warrant request 때 -2.4%가 나왔다. BTS comeback이나 global tour가 있어도, R8 scoring에서는 IP strength와 governance/legal gate를 분리해야 한다. ([Reuters][4])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters / AP HYBE governance and legal-risk anchors",
  "stage3_price": null,
  "ador_dispute_event_mae_pct": -8,
  "bang_detention_request_event_mae_pct": -2.4,
  "alleged_profit_arrangement_krw_bn": 190,
  "alleged_profit_arrangement_usd_mn": 129.1,
  "police_raid_date": "2025-07-24",
  "prosecutors_rejected_warrant_request_date": "2026-04-24",
  "artist_ip_strength_confirmed": true,
  "governance_legal_clearance_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = Kpop_IP_governance_4C_watch
stage_failure_type = artist_IP_not_green_without_label_governance_clearance
```

---

## Case E — Shift Up `game-IP monetization + IPO overheat`

```text
symbol = 462870
case_type = success_candidate + overheat
archetype = GAME_IP_MONETIZATION_IPO_STAGE2
```

### stage date

```text
Stage 1:
2024-04~06
- Stellar Blade launch success
- Goddess of Victory: Nikke mobile revenue
- Tencent-backed Korean game developer IPO

Stage 2:
2024-06-27 / 2024-07
- Reuters: Shift Up may price IPO at top of range
- IPO raise 435B won / $313M
- valuation 3.5T won / $2.52B
- Tencent stake about 40% pre-offering, around 35% after IPO
- Nikke generated 255B won from late 2022 through Q1 2024
- 2023 revenue 169B won
- 2023 operating profit 111B won

Stage 4B:
IPO pricing at top of range / game-IP concentration before multi-title durability proof

Stage 3:
없음
- actual Stage 3 needs post-IPO sales retention, new-title pipeline, PC/console conversion, China/global service quality, margin durability
```

Shift Up은 R8 게임-IP monetization의 좋은 Stage 2다. Reuters는 Shift Up이 IPO를 top of range로 pricing해 4350억 원을 조달하고, valuation이 3.5조 원이 될 수 있다고 보도했다. Nikke는 late 2022~Q1 2024 기간 2550억 원 revenue를 냈고, Shift Up의 2023 operating profit은 1110억 원이었다. 하지만 IPO overheat와 single-IP concentration을 같이 봐야 한다. ([reuters.com](https://www.reuters.com/markets/deals/tencent-backed-shift-up-may-price-ipo-top-end-band-source-says-2024-06-27/))

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters Shift Up IPO anchor",
  "stage3_price": null,
  "ipo_raise_krw_bn": 435,
  "ipo_raise_usd_mn": 313,
  "valuation_krw_trn": 3.5,
  "valuation_usd_bn": 2.52,
  "tencent_stake_pre_ipo_pct": 40,
  "tencent_stake_post_ipo_pct": 35,
  "nikke_revenue_late2022_to_q1_2024_krw_bn": 255,
  "revenue_2023_krw_bn": 169,
  "op_2023_krw_bn": 111,
  "op_margin_2023_pct": 65.7,
  "post_ipo_multititle_durability_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_but_ipo_overheat
rerating_result = game_IP_monetization_stage2
stage_failure_type = IPO_top_range_not_multititle_green
```

---

## Case F — LG CNS `AI/cloud IT-service IPO quality gate`

```text
symbol = 064400
case_type = evidence_good_but_price_failed
archetype = AI_CLOUD_IT_SERVICE_IPO_QUALITY_GATE
```

### stage date

```text
Stage 1:
2025-01-06
- LG CNS IPO bookbuilding
- AI/cloud IT services
- Korean software/platform infra listing test

Stage 2:
2025-02-05
- IPO price 61,900 won
- debut opens 60,500 won
- trades at 59,700 won in morning, below IPO price
- IPO raises 1.2T won / $827.1M
- market valuation about 5.79T won
- retail portion oversubscribed nearly 123x
- institutional bids 76T won
- cloud and AI 54% of sales in first three quarters 2024
- 9M 2024 revenue about 4T won
- 9M 2024 OP 313B won

Stage 3:
없음
- AI/cloud mix is good, but IPO price failed
- recurring revenue, margin durability, M&A ROI, debt use, customer concentration needed
```

LG CNS는 R8 SW/AI/cloud의 좋은 quality gate case다. Cloud/AI가 매출의 54%이고 9M 2024 OP가 3130억 원인 것은 좋은 evidence다. 그러나 IPO 가격 61,900원 대비 debut trading price는 59,700원으로 낮았다. 즉 “AI/cloud 비중이 높다”는 Stage 2일 뿐, IPO valuation을 바로 정당화하지는 못했다. ([Reuters][5])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters LG CNS IPO and debut anchors",
  "stage3_price": null,
  "ipo_price_krw": 61900,
  "open_price_krw": 60500,
  "morning_trading_price_krw": 59700,
  "debut_mae_vs_ipo_pct": -3.23,
  "ipo_raise_krw_trn": 1.2,
  "ipo_raise_usd_mn": 827.1,
  "market_valuation_morning_krw_trn": 5.79,
  "retail_oversubscription_multiple": 123,
  "institutional_bids_krw_trn": 76,
  "cloud_ai_sales_share_9m2024_pct": 54,
  "revenue_9m2024_krw_trn": 4.0,
  "op_9m2024_krw_bn": 313,
  "op_margin_9m2024_pct": 7.8,
  "new_issuance_use_for_ma_krw_bn": 390,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed
rerating_result = AI_cloud_IT_service_IPO_quality_gate
stage_failure_type = AI_cloud_mix_not_IPO_green
```

---

## Case G — Krafton / India platform option `success_candidate + regulatory watch`

```text
symbol = 259960
case_type = success_candidate + 4C-watch
archetype = EMERGING_MARKET_GAME_PLATFORM_OPTION
```

### stage date

```text
Stage 1:
2025-08~2025-12
- Krafton expands India exposure
- BGMI / PUBG India platform
- Korea digital-content diversification away from China

Stage 2:
2025-12-19
- Krafton, NAVER, Mirae Asset create $666M India tech fund
- initial pool over $333M, launch January 2026
- Krafton has invested over $200M in India
- BGMI has more than 240M downloads
- fund focuses on Asia tech startups, especially India

Stage 2 business validation:
2025-08 FT
- Krafton plans at least $50M annual India investment
- India among top five Krafton markets
- India accounts for about 10% of record 1H sales of 1.5T won
- Indian gaming market player count +12% to 444M
- nearly one-third of Indian gamers spend money

Stage 4C-watch:
- BGMI/PUBG history includes India data-security ban / regulatory volatility
- Krafton still needs another hit beyond Battlegrounds

Stage 3:
없음
- India option is Stage 2
- paid conversion, ARPU, regulatory clearance, second-IP success, fund ROI needed
```

Krafton은 R8에서 game-platform emerging-market optionality다. Reuters는 Krafton이 NAVER·Mirae Asset과 $666M India tech fund를 만들고, BGMI가 240M+ downloads를 갖고 있다고 보도했다. FT는 India가 Krafton top-five market이고 1H record sales 1.5조 원의 약 10%를 차지했다고 설명했다. 다만 BGMI/PUBG는 과거 India data-security ban 경험이 있고, Krafton은 Battlegrounds 이후 또 다른 hit를 증명해야 한다. ([Reuters][6])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters / FT Krafton India platform anchors",
  "stage3_price": null,
  "india_tech_fund_total_usd_mn": 666,
  "initial_pool_usd_mn": 333,
  "fund_launch": "2026-01",
  "krafton_prior_india_investment_usd_mn": 200,
  "bgmi_downloads_mn": 240,
  "annual_india_investment_plan_usd_mn": 50,
  "india_share_of_1h_record_sales_pct": 10,
  "krafton_1h_sales_krw_trn": 1.5,
  "implied_india_sales_1h_krw_bn": 150,
  "india_gamers_mn": 444,
  "india_gamer_growth_pct": 12,
  "spending_gamer_share_pct": 33,
  "regulatory_data_security_watch": true,
  "second_hit_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_regulatory_watch
rerating_result = emerging_market_game_platform_option
stage_failure_type = downloads_and_market_option_not_ARPU_green
```

---

## Case H — SK Telecom `cybersecurity trust hard 4C`

```text
symbol = 017670
case_type = 4C-thesis-break
archetype = CYBERSECURITY_TRUST_HARD_4C
```

### stage date

```text
Stage 1:
2025-04-18
- SK Telecom detects large customer-data leak caused by malware
- USIM / subscriber identity security issue

Stage 4C:
2025-04-28
- shares fall as much as -8.5%
- shares close -6.7%
- KOSPI +0.1%
- all 23M users offered free USIM replacement
- more than 2,600 retail stores involved
- 5.54M customers signed up for USIM Protection Service by Sunday

Stage 4C validation:
2025-07-04
- 26.96M pieces of user data leaked
- shares close -5.6%
- 700B won five-year data protection investment
- 50% August bill discount for all 24M customers
- 2025 revenue forecast cut by 800B won
- customer benefit package cost about 500B won

Stage 4C legal/financial validation:
2025-08-28 / 2025-12-21
- Personal Information Protection Commission fines SKT about 134B won
- consumer agency may push compensation to all affected victims
- total compensation could reach nearly 2.3T won
```

SK Telecom은 R8의 hard 4C다. 플랫폼·통신·보안에서 data trust가 깨지면 단순 비용이 아니라 revenue forecast, compensation, regulator fine, customer churn risk로 내려온다. Reuters는 SKT가 breach disclosure 후 장중 -8.5%, 종가 -6.7% 하락했고, KOSPI는 +0.1%였다고 보도했다. 이후 26.96M data pieces leak, 7000억 원 보안투자, 8000억 원 매출전망 하향, 1340억 원 과징금, 잠재 보상 2.3조 원까지 이어졌다. ([Reuters][7])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters SK Telecom breach / investigation / fine / compensation anchors",
  "stage3_price": null,
  "initial_intraday_mae_pct": -8.5,
  "initial_close_mae_pct": -6.7,
  "kospi_same_context_pct": 0.1,
  "relative_underperformance_initial_pp": -6.8,
  "usim_replacement_users_mn": 23,
  "retail_stores_involved": 2600,
  "usim_protection_service_signups_mn": 5.54,
  "leaked_data_pieces_mn": 26.96,
  "july_event_close_mae_pct": -5.6,
  "data_protection_investment_krw_bn": 700,
  "august_bill_discount_pct": 50,
  "customers_for_discount_mn": 24,
  "revenue_forecast_cut_krw_bn": 800,
  "customer_benefit_package_cost_krw_bn": 500,
  "pipc_fine_krw_bn": 134,
  "possible_total_compensation_krw_trn": 2.3,
  "mfe": "N/A",
  "mae_30d_90d_180d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = cybersecurity_trust_hard_4C
stage_failure_type = data_breach_cost_revenue_trust_break
```

---

# 5. 이번 R8 case별 stage date 요약

| case                | Stage 1         | Stage 2             | Stage 3 | Stage 4B            | Stage 4C                   |
| ------------------- | --------------- | ------------------- | ------- | ------------------- | -------------------------- |
| NAVER / Line Yahoo  | 2023-11~2024-04 | 2024-08-02 relief   | N/A     | N/A                 | 2024-04~05 watch           |
| NAVER / Webtoon IPO | 2024-06-26      | 2024-06-27          | N/A     | 2024-06-27          | loss / parent bridge watch |
| Kakao / SM          | 2023-03         | acquisition context | N/A     | N/A                 | 2024-07 watch, 2025 relief |
| HYBE / ADOR / Bang  | 2024-04-22      | content IP context  | N/A     | N/A                 | 2024-04 / 2026-04 watch    |
| Shift Up            | 2024-04~06      | 2024-06/07          | N/A     | IPO top-range watch | IP concentration watch     |
| LG CNS              | 2025-01         | 2025-02-05          | N/A     | IPO demand watch    | IPO price failure          |
| Krafton India       | 2025-08~12      | 2025-12-19          | N/A     | India option watch  | regulatory/data watch      |
| SK Telecom          | 2025-04-18      | N/A                 | N/A     | N/A                 | 2025-04~12 hard            |

---

# 6. 실제 가격경로 검증 총괄

| case               |                                                   anchor | MFE / MAE 해석                               | 판정                             |
| ------------------ | -------------------------------------------------------: | ------------------------------------------ | ------------------------------ |
| NAVER / Line Yahoo |         LY 150B yen buyback, voting rights 64.42%→62.50% | data sovereignty relief, not Green         | 4C-watch                       |
| NAVER / Webtoon    |          IPO $21, high $24, +14.3%, 170M MAU, $145M loss | IPO event premium, parent bridge gap       | success_candidate              |
| Kakao              |             founder arrest, Kakao -3.4%, later acquittal | governance 4C-watch then relief            | 4C-watch                       |
| HYBE               |              ADOR dispute nearly -8%, Bang warrant -2.4% | IP governance and founder legal risk       | 4C-watch                       |
| Shift Up           |        435B won IPO, 3.5T won valuation, OP margin 65.7% | game-IP success but IPO overheat           | success_candidate              |
| LG CNS             |                                IPO 61,900→59,700, -3.23% | AI/cloud evidence good but price failed    | evidence_good_but_price_failed |
| Krafton            |                    BGMI 240M downloads, India fund $666M | platform option, ARPU/regulatory not Green | success_candidate              |
| SKT                | -8.5% intraday, -6.7% close, 134B fine, 800B revenue cut | cybersecurity hard 4C                      | thesis_break                   |

---

# 7. score-price alignment 판정

```text
success_candidate:
- NAVER / Webtoon Entertainment
- Shift Up
- Krafton India platform option
- LG CNS, but only after IPO valuation and recurring AI/cloud revenue prove out

event_premium:
- Webtoon IPO +14.3%
- Shift Up IPO top-range pricing
- Krafton India fund / BGMI option if price moves before ARPU

evidence_good_but_price_failed:
- LG CNS AI/cloud IPO

price_moved_without_evidence:
- Webtoon MAU if treated as NAVER EPS Green
- Shift Up IPO if treated as multi-title durability
- Krafton India downloads if treated as ARPU/FCF Green

thesis_break_watch:
- NAVER / Line Yahoo data sovereignty
- Kakao founder legal overhang
- HYBE ADOR / founder legal risk

thesis_break:
- SK Telecom cybersecurity breach

hard_4C_confirmed:
- SK Telecom data breach / cybersecurity trust break
```

---

# 8. 점수비중 교정

## 올릴 축

```text
paid_conversion +5
ARPU_take_rate +5
recurring_cloud_AI_revenue +5
creator_economics +4
content_IP_retention +5
platform_data_governance +5
cybersecurity_internal_control +5
regulatory_clearance +5
parent_value_bridge +4
customer_trust_repair_cost +5
```

### 왜 올리나

SKT는 data breach가 매출전망 하향·과징금·보안투자·잠재보상으로 내려간 hard 4C다. NAVER/Line Yahoo는 data sovereignty가 해외 플랫폼 control까지 건드렸다. Webtoon은 MAU가 많지만 순손실과 parent value bridge가 남았다. LG CNS는 cloud/AI 매출비중이 높아도 IPO price가 실패했다. Shift Up·Krafton은 IP/download가 좋지만 ARPU·multi-title durability가 필요하다.

## 내릴 축

```text
MAU_only -5
IPO_pop_only -5
creator_platform_loss_ignored -5
unlisted_subsidiary_or_US_listed_parent_bridge_missing -4
founder_legal_overhang -5
label_or_artist_governance_dispute -5
game_single_IP_concentration -4
downloads_without_ARPU -5
cloud_AI_keyword_without_margin -5
data_breach_or_internal_control_failure -5
```

### 왜 내리나

Webtoon의 170M MAU는 monetization이 아니고, LG CNS의 AI/cloud mix는 IPO price를 방어하지 못했다. Kakao와 HYBE는 founder/legal/governance가 platform premium을 누른다. Shift Up과 Krafton은 game IP가 강하지만 single-IP concentration과 second-hit risk가 크다. SKT는 data trust failure가 곧 hard 4C다.

## Green gate 강화 조건

```text
R8 Stage 3-Green 필수:
1. MAU가 paid conversion / ARPU / take-rate로 전환
2. platform unit economics와 OP/FCF 확인
3. creator / developer economics 지속 가능
4. parent value bridge 확인
5. game은 multi-title durability / live-ops retention 확인
6. cloud/AI는 recurring revenue와 margin 확인
7. data governance / cybersecurity 통과
8. regulatory / founder legal overhang 해소
9. price path가 evidence 이후 따라옴

금지:
MAU only
IPO pop only
downloads only
AI/cloud keyword only
content IP headline only
founder legal risk unresolved
data breach unresolved
```

## 4B 조기감지 조건

```text
4B-watch:
IPO debut +10~15% 이상
게임 IPO top-range pricing / single-IP valuation premium
MAU 100M+ headline로 parent rally
AI/cloud 매출비중 headline로 valuation 확장
India / emerging market downloads로 ARPU 전 rerating
K-pop IP governance resolution 없이 rebound
data-breach relief news만으로 quick rebound

4B-elevated:
loss-making platform
parent value bridge 없음
single-IP concentration
legal/founder overhang
data-sovereignty dispute
cybersecurity remediation cost large
```

## 4C hard gate 조건

```text
large data breach
USIM / identity / authentication leakage
regulatory fine
revenue forecast cut from trust event
platform forced selldown / data-sovereignty dispute
founder arrest / capital-market law risk
artist IP contract rupture
cloud/AI recurring revenue miss
IPO valuation break
game regulatory ban / data-security ban
```

이번 R8 Loop 13의 hard 4C는 **SK Telecom data breach**로 확정한다. NAVER/Line Yahoo, Kakao, HYBE는 hard 4C가 아니라 4C-watch다.

---

# 9. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 10. 레포 반영용 patch-ready 출력

## docs/round/round_205.md 요약

```md
# R8 Loop 13. Platform / Content / Software / Security Price Validation

이번 라운드는 R8 Loop 13 price-validation 라운드다.

핵심 결론:
- NAVER / Line Yahoo is data-sovereignty 4C-watch. Japan’s administrative guidance after data leak pressured LY Corp’s Naver dependence and capital relationship. LY Corp later announced a 150B yen buyback that lowers A Holdings voting rights from 64.42% to as low as 62.50%. Green requires data-governance and regulatory clearance.
- NAVER / Webtoon Entertainment IPO is global-content Stage 2, not parent Green. Webtoon sold 15M shares at $21, raised $315M, valuation $2.67B, 170M MAU, debut high $24 (+14.3%). But 2023 revenue $1.28B and net loss $145M mean monetization and parent value bridge are required.
- Kakao / SM Entertainment is platform-governance 4C-watch. Kakao founder Kim Beom-su’s arrest caused Kakao -3.4%; later acquittal eased the overhang, but founder/legal risk remains a scoring gate.
- HYBE / ADOR / Bang Si-hyuk is content-IP governance 4C-watch. HYBE shares dropped nearly -8% on ADOR dispute; later founder detention-warrant request drove -2.4% despite market uptick. Artist IP is not Green without governance clarity.
- Shift Up is game-IP monetization Stage 2 plus IPO overheat. IPO raised 435B won at 3.5T won valuation; Nikke generated 255B won from late 2022 through Q1 2024; 2023 OP 111B won on 169B won revenue. Multi-title durability required.
- LG CNS is AI/cloud IT-service IPO quality gate. IPO price 61,900 won, trading at 59,700 won on debut morning (-3.23%). Cloud and AI were 54% of 9M 2024 sales, but IPO valuation failed.
- Krafton India is emerging-market game-platform option. $666M India fund with NAVER/Mirae, BGMI 240M+ downloads, India about 10% of 1H record sales. ARPU, paid conversion and regulatory clearance required.
- SK Telecom is cybersecurity trust hard 4C. Shares -8.5% intraday and -6.7% close after breach; later 26.96M data pieces leaked, 700B won security investment, 800B won revenue forecast cut, 134B won fine and potential 2.3T won compensation.
```

## docs/checkpoints/checkpoint_28a_round205_r8_loop13.md 요약

```md
# Checkpoint 28A Round 205 R8 Loop 13 Platform Content Software Security Price Validation

## 반영 내용
- R8 Loop 13 price-validation 라운드를 추가했다.
- NAVER/Line Yahoo data-sovereignty, Webtoon IPO, Kakao/SM legal overhang, HYBE/ADOR and founder legal risk, Shift Up IPO, LG CNS AI/cloud IPO, Krafton India option, SK Telecom breach를 비교했다.
- Reuters / FT / AP / MarketWatch anchors로 가능한 event MFE/MAE 및 business metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- paid conversion, ARPU/take-rate, recurring cloud/AI revenue, content-IP retention, platform data governance, cybersecurity internal control, regulatory clearance, parent value bridge, trust repair cost 가중치 강화
- MAU-only, IPO pop-only, downloads without ARPU, AI/cloud keyword without margin, founder legal overhang, label governance dispute, data breach/internal-control failure 감점 강화
```

## data/e2r_case_library/cases_r8_loop13_round205.jsonl 초안

```jsonl
{"case_id":"r8_loop13_naver_line_yahoo_data_sovereignty_watch","symbol":"035420","company_name":"NAVER / Line Yahoo / LY Corp","case_type":"4c_watch","primary_archetype":"DATA_SOVEREIGNTY_PLATFORM_4C_WATCH","stage4c_date":"2024-04-27/2024-05-10_watch","stage2_date":"2024-08-02_relief","price_validation":{"price_data_source":"Reuters data leak / SoftBank talks / LY buyback anchors","stage3_price":null,"data_leak_records_context":"more_than_300000_Line_users_and_others_in_Reuters_source","ly_corp_market_value_may2024_jpy_trn":2.77,"ly_corp_market_value_may2024_usd_bn":17.77,"a_holdings_pre_buyback_voting_rights_pct":64.42,"a_holdings_post_buyback_low_voting_rights_pct":62.50,"voting_rights_decline_pp":-1.92,"buyback_value_jpy_bn":150,"buyback_value_usd_bn":1.01,"buyback_price_jpy":388,"buyback_premium_pct":11,"price_validation_status":"naver_ohlc_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"data_sovereignty_platform_4C_watch","notes":"Line Yahoo data governance and capital-control pressure block overseas platform Green."}
{"case_id":"r8_loop13_naver_webtoon_entertainment_ipo","symbol":"035420/WBTN","company_name":"NAVER / Webtoon Entertainment","case_type":"success_candidate_event_premium","primary_archetype":"GLOBAL_CONTENT_PLATFORM_IPO_NOT_PARENT_GREEN","stage2_date":"2024-06-27","stage4b_date":"2024-06-27","price_validation":{"price_data_source":"Reuters / FT Webtoon IPO anchors","stage3_price":null,"ipo_price_usd":21,"shares_sold_mn":15,"ipo_raise_usd_mn":315,"valuation_usd_bn":2.67,"debut_high_usd":24,"debut_mfe_pct":14.3,"opened_at_usd":21.30,"naver_private_placement_usd_mn":50,"blackrock_indicated_interest_usd_mn":50,"monthly_active_users_mn":170,"countries":150,"webtoon_2023_revenue_usd_bn":1.28,"webtoon_2023_net_loss_usd_mn":145,"naver_parent_value_bridge_confirmed":false,"price_validation_status":"reported_ipo_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_event_premium","rerating_result":"global_content_platform_IPO_stage2","notes":"MAU and IPO pop are not parent NAVER Green without paid conversion, take-rate, OP and parent value bridge."}
{"case_id":"r8_loop13_kakao_sm_founder_legal_governance","symbol":"035720","company_name":"Kakao / SM Entertainment legal overhang","case_type":"4c_watch","primary_archetype":"PLATFORM_GOVERNANCE_LEGAL_4C_WATCH","stage4c_date":"2024-07-23_watch","stage2_date":"2025-10-21_relief","price_validation":{"price_data_source":"Reuters Kakao arrest/acquittal anchors","stage3_price":null,"arrest_event_date":"2024-07-23","kakao_event_mae_pct":-3.4,"kim_beom_su_kakao_stake_pct":24,"kakao_group_value_context_krw_trn":86,"kakao_group_value_context_usd_bn":62,"prosecutor_sought_sentence_years":15,"prosecutor_sought_fine_krw_mn":500,"acquittal_date":"2025-10-21","sm_content_monetization_confirmed":false,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch_then_relief","rerating_result":"platform_content_MA_governance_gate","notes":"Founder/legal overhang blocks content-platform Green until governance and IP monetization prove out."}
{"case_id":"r8_loop13_hybe_ador_bang_legal_ip_governance","symbol":"352820","company_name":"HYBE / ADOR / Bang Si-hyuk legal risk","case_type":"4c_watch","primary_archetype":"KPOP_IP_GOVERNANCE_4C_WATCH","stage4c_date":"2024-04-24/2026-04-21_watch","price_validation":{"price_data_source":"Reuters / AP HYBE governance and legal-risk anchors","stage3_price":null,"ador_dispute_event_mae_pct":-8,"bang_detention_request_event_mae_pct":-2.4,"alleged_profit_arrangement_krw_bn":190,"alleged_profit_arrangement_usd_mn":129.1,"police_raid_date":"2025-07-24","prosecutors_rejected_warrant_request_date":"2026-04-24","artist_ip_strength_confirmed":true,"governance_legal_clearance_confirmed":false,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"Kpop_IP_governance_4C_watch","notes":"Artist IP strength is not Green when label governance and founder legal risk remain unresolved."}
{"case_id":"r8_loop13_shiftup_game_ip_ipo_overheat","symbol":"462870","company_name":"Shift Up","case_type":"success_candidate_overheat","primary_archetype":"GAME_IP_MONETIZATION_IPO_STAGE2","stage2_date":"2024-06-27/2024-07","stage4b_date":"2024-07_IPO_watch","price_validation":{"price_data_source":"Reuters Shift Up IPO anchor","stage3_price":null,"ipo_raise_krw_bn":435,"ipo_raise_usd_mn":313,"valuation_krw_trn":3.5,"valuation_usd_bn":2.52,"tencent_stake_pre_ipo_pct":40,"tencent_stake_post_ipo_pct":35,"nikke_revenue_late2022_to_q1_2024_krw_bn":255,"revenue_2023_krw_bn":169,"op_2023_krw_bn":111,"op_margin_2023_pct":65.7,"post_ipo_multititle_durability_confirmed":false,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_ipo_overheat","rerating_result":"game_IP_monetization_stage2","notes":"Game-IP economics are strong, but top-range IPO is not Green until multi-title durability and live-ops retention prove out."}
{"case_id":"r8_loop13_lg_cns_ai_cloud_ipo_quality_gate","symbol":"064400","company_name":"LG CNS","case_type":"evidence_good_but_price_failed","primary_archetype":"AI_CLOUD_IT_SERVICE_IPO_QUALITY_GATE","stage2_date":"2025-02-05","price_validation":{"price_data_source":"Reuters LG CNS IPO and debut anchors","stage3_price":null,"ipo_price_krw":61900,"open_price_krw":60500,"morning_trading_price_krw":59700,"debut_mae_vs_ipo_pct":-3.23,"ipo_raise_krw_trn":1.2,"ipo_raise_usd_mn":827.1,"market_valuation_morning_krw_trn":5.79,"retail_oversubscription_multiple":123,"institutional_bids_krw_trn":76,"cloud_ai_sales_share_9m2024_pct":54,"revenue_9m2024_krw_trn":4.0,"op_9m2024_krw_bn":313,"op_margin_9m2024_pct":7.8,"new_issuance_use_for_ma_krw_bn":390,"price_validation_status":"reported_ipo_anchor_not_full_ohlc"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"AI_cloud_IT_service_IPO_quality_gate","notes":"AI/cloud revenue mix is good evidence, but IPO price failed; recurring revenue and margin durability required."}
{"case_id":"r8_loop13_krafton_india_game_platform_option","symbol":"259960","company_name":"Krafton / BGMI / India platform option","case_type":"success_candidate_4c_watch","primary_archetype":"EMERGING_MARKET_GAME_PLATFORM_OPTION","stage2_date":"2025-12-19","stage4c_date":"regulatory_data_security_watch","price_validation":{"price_data_source":"Reuters / FT Krafton India platform anchors","stage3_price":null,"india_tech_fund_total_usd_mn":666,"initial_pool_usd_mn":333,"fund_launch":"2026-01","krafton_prior_india_investment_usd_mn":200,"bgmi_downloads_mn":240,"annual_india_investment_plan_usd_mn":50,"india_share_of_1h_record_sales_pct":10,"krafton_1h_sales_krw_trn":1.5,"implied_india_sales_1h_krw_bn":150,"india_gamers_mn":444,"india_gamer_growth_pct":12,"spending_gamer_share_pct":33,"regulatory_data_security_watch":true,"second_hit_confirmed":false,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_regulatory_watch","rerating_result":"emerging_market_game_platform_option","notes":"Downloads and India option are Stage 2; ARPU, paid conversion, regulatory clearance and second-hit proof required."}
{"case_id":"r8_loop13_skt_data_breach_cybersecurity_hard_4c","symbol":"017670","company_name":"SK Telecom","case_type":"4c_thesis_break","primary_archetype":"CYBERSECURITY_TRUST_HARD_4C","stage4c_date":"2025-04-28/2025-07-04/2025-08-28","price_validation":{"price_data_source":"Reuters SK Telecom breach / investigation / fine / compensation anchors","stage3_price":null,"initial_intraday_mae_pct":-8.5,"initial_close_mae_pct":-6.7,"kospi_same_context_pct":0.1,"relative_underperformance_initial_pp":-6.8,"usim_replacement_users_mn":23,"retail_stores_involved":2600,"usim_protection_service_signups_mn":5.54,"leaked_data_pieces_mn":26.96,"july_event_close_mae_pct":-5.6,"data_protection_investment_krw_bn":700,"august_bill_discount_pct":50,"customers_for_discount_mn":24,"revenue_forecast_cut_krw_bn":800,"customer_benefit_package_cost_krw_bn":500,"pipc_fine_krw_bn":134,"possible_total_compensation_krw_trn":2.3,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"cybersecurity_trust_hard_4C","notes":"Data breach turned into revenue cut, security capex, fine and potential compensation; hard 4C."}
```

## data/sector_taxonomy/score_weight_profiles_round205_r8_loop13_v1.csv 초안

```csv
archetype,paid_conversion,arpu_take_rate,recurring_cloud_ai_revenue,creator_economics,content_ip_retention,platform_data_governance,cybersecurity_internal_control,regulatory_clearance,parent_value_bridge,customer_trust_repair_cost,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
DATA_SOVEREIGNTY_PLATFORM_4C_WATCH,+3,+3,+2,+2,+3,+5,+5,+5,+4,+5,0,+4,+5,NAVER/Line Yahoo shows data sovereignty can override platform scale.
GLOBAL_CONTENT_PLATFORM_IPO_NOT_PARENT_GREEN,+5,+5,+1,+5,+5,+4,+3,+3,+5,+3,-5,+5,+4,Webtoon IPO/MAU needs monetization and parent NAVER value bridge.
PLATFORM_GOVERNANCE_LEGAL_4C_WATCH,+3,+4,+2,+3,+5,+4,+4,+5,+4,+4,0,+4,+5,Kakao/SM shows founder legal risk blocks platform content premium.
KPOP_IP_GOVERNANCE_4C_WATCH,+4,+5,+1,+3,+5,+4,+3,+5,+3,+4,0,+4,+5,HYBE/ADOR shows artist IP is not enough without label governance.
GAME_IP_MONETIZATION_IPO_STAGE2,+5,+5,+1,+2,+5,+2,+2,+3,+2,+2,-5,+5,+4,Shift Up needs multi-title durability beyond IPO and single-IP economics.
AI_CLOUD_IT_SERVICE_IPO_QUALITY_GATE,+3,+4,+5,+0,+1,+3,+4,+3,+3,+2,-5,+5,+3,LG CNS needs recurring AI/cloud revenue and margin durability, not IPO demand.
EMERGING_MARKET_GAME_PLATFORM_OPTION,+5,+5,+1,+1,+4,+4,+3,+5,+2,+3,-4,+5,+4,Krafton India needs ARPU, paid conversion, regulatory clearance and second-hit proof.
CYBERSECURITY_TRUST_HARD_4C,+0,+0,+0,+0,+0,+5,+5,+5,+0,+5,0,+4,+5,SKT breach confirms data/security trust hard gate.
```

---

# 이번 R8 Loop 13 결론

```text
1. NAVER/Line Yahoo는 data-sovereignty 4C-watch다.
   해외 플랫폼은 MAU보다 data governance와 capital-control risk가 먼저다.

2. Webtoon Entertainment IPO는 글로벌 콘텐츠 Stage 2다.
   170M MAU와 +14.3% debut pop은 좋지만, $145M 손실과 parent NAVER value bridge가 남아 있다.

3. Kakao/SM은 platform governance 4C-watch다.
   founder arrest 때 -3.4%가 나왔고, 무죄 relief 이후에도 governance gate로 남긴다.

4. HYBE는 artist IP가 강해도 label governance와 founder legal risk가 4C-watch다.
   ADOR dispute nearly -8%, Bang warrant request -2.4%가 가격경로로 확인됐다.

5. Shift Up은 game-IP monetization Stage 2다.
   OP margin은 강하지만 IPO top-range와 single-IP concentration 때문에 4B-watch다.

6. LG CNS는 AI/cloud evidence가 좋아도 IPO price가 실패했다.
   AI/cloud 매출비중만으로는 Stage 3가 아니다.

7. Krafton India는 emerging-market platform option이다.
   BGMI 240M downloads와 India fund는 Stage 2지만 ARPU와 regulatory clearance가 필요하다.

8. SK Telecom은 R8 hard 4C다.
   data breach가 주가, 매출전망, 과징금, 보안투자, 보상비용으로 직접 내려왔다.
```

한 문장으로 압축하면:

> **R8에서 진짜 Stage 3는 “MAU·IPO·K-pop IP·게임 IP·AI/cloud·인도 다운로드가 많다”가 아니라, 유료전환·ARPU·반복매출·data governance·cybersecurity trust·규제통과·OP/FCF가 실제 숫자로 닫히는 순간이다.**

[1]: https://www.reuters.com/world/asia-pacific/south-korea-consult-naver-after-report-firm-faces-japan-pressure-divest-stake-2024-04-27/?utm_source=chatgpt.com "South Korea to consult Naver, after report firm faces Japan pressure to divest stake"
[2]: https://www.reuters.com/markets/deals/webtoon-entertainment-prices-us-ipo-21-per-share-2024-06-26/?utm_source=chatgpt.com "Webtoon Entertainment prices US IPO at top of range to raise about $315 mln"
[3]: https://www.reuters.com/technology/south-korean-court-approves-arrest-warrant-kakao-founder-2024-07-22/?utm_source=chatgpt.com "Founder of South Korea's Kakao arrested for suspected stock manipulation"
[4]: https://www.reuters.com/lifestyle/record-giant-hybe-audits-newjeans-label-infighting-returns-k-pop-2024-04-24/?utm_source=chatgpt.com "Record giant HYBE audits 'NewJeans' label as infighting returns to K-pop"
[5]: https://www.reuters.com/markets/deals/south-koreas-lg-cns-launches-ipo-up-817-mln-term-sheet-says-2025-01-06/?utm_source=chatgpt.com "South Korea's LG CNS launches IPO for up to $817 mln, term sheet says"
[6]: https://www.reuters.com/world/asia-pacific/pubg-maker-krafton-leads-south-korean-trio-666-million-india-tech-bet-2025-12-19/?utm_source=chatgpt.com "PUBG maker Krafton leads South Korean trio in $666 million India tech bet"
[7]: https://www.reuters.com/sustainability/boards-policy-regulation/sk-telecom-shares-plunge-after-data-breach-due-cyberattack-2025-04-28/?utm_source=chatgpt.com "SK Telecom shares plunge after data breach due to cyberattack"
