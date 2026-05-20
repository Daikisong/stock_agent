순서상 이번은 **R8 Loop 15 — 플랫폼·콘텐츠·SW·보안 trigger-level price validation 라운드**다.

이번 R8의 핵심은 “AI 플랫폼 / 콘텐츠 IP / 게임 / 클라우드 / 보안이 좋다”가 아니라, **MAU·AI 사용량·클라우드 매출·IP 매출·게임 sell-through·M&A integration·보안 사고·아티스트 governance 중 어느 trigger가 실제 entry였고, 어느 trigger는 4B/4C였는지**를 분리하는 것이다.

```text
round = R8 Loop 15
round_id = round_231
large_sector = PLATFORM_CONTENT_SW_SECURITY
method = trigger_level_backtest_v1
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R9 Loop 15
```

이번에도 KRX/Naver/Yahoo/Stooq의 수정주가 일봉 OHLC 30D/90D/180D/1Y window를 안정적으로 직접 추출하지 못했다. 그래서 full MFE/MAE는 `price_data_unavailable_after_deep_search`로 두고, Reuters/FT/WSJ/MarketWatch/AP의 **reported event return, IPO/debut price, deal value, cloud/AI sales ratio, subscriber/user count, data-breach cost, litigation/security event**를 trigger anchor로 쓴다. 단, **OHLC 미확보를 이유로 Stage 후보 자체를 강등하지 않는다.**

---

# 1. 이번 라운드 대섹터

```text
R8 = 플랫폼·콘텐츠·SW·보안
```

R8의 core gate는 아래다.

```text
AI 플랫폼:
AI partnership → product integration → paid usage / retention → cloud/API cost → margin → regulatory/data rights

인터넷·포털:
search/chat/social MAU → ad revenue → AI infra capex → monetization → competitive share

콘텐츠 IP:
IP hit → recurring revenue → game/OTT/webtoon expansion → global licensing → margin → creator/artist governance

게임:
new title hit → concurrent users / downloads / sales → paid conversion → live-service retention → publisher/developer economics

SW/cloud:
IPO/M&A/capital injection → AI/cloud revenue share → enterprise order backlog → margin → dilution/CB risk

보안:
data breach → direct compensation → revenue cut → regulatory fine → security capex → customer churn / trust recovery
```

---

# 2. 대상 canonical archetype

```text
AI_MESSAGING_PARTNERSHIP_STAGE2_WITH_MONETIZATION_GATE
AI_INFRA_PORTAL_STAGE2_ACTIONABLE
WEBTOON_IPO_CONTENT_PLATFORM_STAGE2
CLOUD_AI_IT_SERVICES_EVIDENCE_GOOD_PRICE_FAILED
AI_SOFTWARE_CB_STRATEGIC_CAPITAL_STAGE2_WITH_4B
GAME_IP_GLOBALIZATION_STAGE2_ACTIONABLE
KPOP_ARTIST_GOVERNANCE_4C_WATCH
CYBERSECURITY_DATA_BREACH_HARD_4C
CONTENT_MA_IP_EXPANSION_STAGE2
```

---

# 3. deep sub-archetype

```text
Kakao:
- OpenAI partnership
- KakaoTalk 97% domestic messaging share
- initial +9% surge then -2% close
- AI product integration vs monetization gate

Naver:
- Webtoon Entertainment U.S. IPO
- 170M MAU, $315M IPO, $2.67B valuation, +14.3% debut pop
- Nvidia Blackwell 60,000-chip purchase
- AI infra capex vs monetization

LG CNS:
- cloud/AI services 54% of sales in first 3Q 2024
- IPO at top range, 1.2T won raised
- weak debut below 61,900 won issue price
- evidence good but price failed

Samsung SDS:
- KKR $820M convertible bonds
- stock +20.8%
- AI infrastructure / M&A / physical AI / stablecoin ambition
- CB/dilution and strategy execution 4B overlay

Krafton:
- ADK acquisition $516M
- India Unicorn Growth Fund $666M with Naver/Mirae
- BGMI 240M downloads but India data-security/regulatory history
- IP diversification vs regulatory volatility

Shift Up:
- IPO top-end pricing, 435B won raise, 3.5T won valuation
- Nikke 255B won sales from global launch to Q1 2024
- Stellar Blade PS5 top rankings
- IP concentration and Tencent ownership overlay

HYBE / SM / NewJeans:
- HYBE audit of ADOR; shares nearly -8%
- court blocks NewJeans independent activities
- Tencent becomes SM second-largest shareholder, China thaw optionality
- artist IP governance 4C-watch vs China reopening Stage2

SK Telecom / data-breach security reference:
- 26.96M pieces of user data leaked
- shares -6.7% in April, -5.6% after probe result
- 700B won five-year security investment
- 800B won 2025 revenue forecast cut
```

---

# 4. 선정 case 요약

| bucket                         | case                              | 핵심 판정                                                                                                         |
| ------------------------------ | --------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Stage2-Actionable              | Kakao / OpenAI                    | OpenAI partnership + KakaoTalk 97% share, initial +9% 후 -2% close. AI product trigger는 좋지만 monetization gate  |
| Stage2-Actionable              | Naver / Webtoon + Nvidia AI infra | Webtoon IPO +14.3%, 170M MAU, Naver 60k Blackwell chips. Content/IP와 AI infra 모두 Stage2                       |
| evidence_good_but_price_failed | LG CNS IPO                        | cloud/AI 54% sales, IPO 1.2T won, debut below issue price. AI/cloud story만으론 Green 불가                         |
| Stage2 + 4B                    | Samsung SDS / KKR CB              | KKR $820M CB, shares +20.8%, AI/M&A/stablecoin. CB/dilution and strategy overlay                              |
| Stage2-Actionable              | Krafton / ADK + India fund        | ADK $516M, India fund $666M, BGMI 240M downloads. IP expansion but regulatory/data risk                       |
| Stage2-Actionable              | Shift Up / IPO + Stellar Blade    | 435B won IPO, 3.5T valuation, Nikke 255B sales, Stellar Blade rankings. IP concentration gate                 |
| 4C-watch                       | HYBE / NewJeans governance        | HYBE -8% on audit; court injunction blocks NewJeans independent activities. Artist IP governance hard overlay |
| hard 4C reference              | SK Telecom data breach            | shares -6.7% then -5.6%; 26.96M data pieces, 700B security capex, 800B revenue forecast cut                   |

---

# 5. Case별 trigger grid

## Case A — Kakao / OpenAI AI messaging partnership

```text
symbol = 035720
case_type = Stage2-Actionable with monetization gate
archetype = AI_MESSAGING_PARTNERSHIP_STAGE2_WITH_MONETIZATION_GATE
```

| trigger | type              |                                             date | 당시 공개 evidence                                                                | 가격 anchor                                           | outcome                        |
| ------- | ----------------- | -----------------------------------------------: | ----------------------------------------------------------------------------- | --------------------------------------------------- | ------------------------------ |
| T0      | awareness         |                                        2024~2025 | Kakao AI lag vs Naver, KakaoTalk dominant messaging base                      | N/A                                                 | Stage1                         |
| T1      | Stage2 evidence   |                                       2025-02-04 | OpenAI-Kakao AI product partnership, KakaoTalk 97% domestic messaging share   | Kakao initial +9% prior/around news, then -2% close | Stage2-Actionable              |
| T2      | Stage2-Actionable |                                       2025-02-04 | OpenAI tech to be used in Kakao products; AI/messaging focus stated           | same                                                | Actionable                     |
| T3      | 4B-watch          |                                       2025-02-04 | monetization unclear, Kakao lagging Naver in AI, no immediate paid usage data | -2% close after +9% surge                           | evidence good but price failed |
| T4      | Stage3-Yellow     |                                              N/A | paid AI usage / retention / ad uplift / KakaoTalk integration missing         | N/A                                                 | no Yellow                      |
| T5      | 4C-watch          | governance/legal risk from broader Kakao complex | from R6                                                                       | overlay                                             |                                |

Kakao/OpenAI는 R8에서 Stage2-Actionable이지만, price action이 “좋은 headline인데 바로 식는” 구조를 보여준다. Reuters는 OpenAI와 Kakao가 한국 AI products를 공동 개발한다고 보도했고, KakaoTalk의 국내 messaging share가 97%라고 설명했다. 그러나 Kakao는 전날/초기 +9% 급등 후 당일 -2%로 마감했고, Reuters는 Kakao가 AI를 성장 엔진으로 내세우지만 Naver보다 뒤처졌다는 analyst context도 같이 전했다. 즉 이건 Green이 아니라 **AI messaging Stage2-Actionable + monetization gate**다. ([Reuters][1])

```json
{
  "case_id": "r8_loop15_kakao_openai_ai_messaging",
  "symbol": "035720",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable_with_monetization_gate",
  "trigger_date": "2025-02-04",
  "kakaotalk_domestic_share_pct": 97,
  "initial_event_mfe_pct": 9,
  "close_event_return_pct": -2,
  "partner": "OpenAI",
  "product_focus": ["AI products", "messaging"],
  "stage3_gate_missing": [
    "paid_AI_usage",
    "KakaoTalk_AI_retention",
    "ad_revenue_uplift",
    "API/cloud_cost_margin",
    "data_privacy_clearance"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_Actionable_but_evidence_good_price_failed"
}
```

---

## Case B — Naver / Webtoon IPO + Nvidia AI infrastructure

```text
symbol = 035420
case_type = Stage2-Actionable
archetype = AI_INFRA_PORTAL_STAGE2_ACTIONABLE / WEBTOON_IPO_CONTENT_PLATFORM_STAGE2
```

| trigger | type              |       date | 당시 공개 evidence                                                                               | 가격 anchor                      | outcome                                  |
| ------- | ----------------- | ---------: | -------------------------------------------------------------------------------------------- | ------------------------------ | ---------------------------------------- |
| T0      | awareness         | 2024-05-31 | Webtoon IPO filing: 170M MAU, Q1 revenue +5% to $326.7M, net income $6.2M vs loss prior year | WBTN not yet traded            | Stage2                                   |
| T1      | Stage2 evidence   | 2024-06-26 | Webtoon IPO priced at $21, top of range, raised $315M, valuation $2.67B                      | Naver direct price unavailable | Stage2                                   |
| T2      | Stage2-Actionable | 2024-06-27 | Webtoon Nasdaq debut +14.3%, high $24, valuation $2.71B                                      | WBTN +14.3%                    | Actionable content-platform value unlock |
| T3      | Stage2 AI infra   | 2025-10-31 | Nvidia to supply Korea 260k Blackwell chips; Naver to buy 60k chips                          | no Naver price anchor          | AI infra Stage2                          |
| T4      | Stage3-Yellow     |        N/A | Webtoon profitability durability / AI monetization / Naver search-ad uplift missing          | N/A                            | no Yellow                                |
| T5      | 4B-watch          |        N/A | IPO pop and AI chip capex without monetization                                               | N/A                            | watch                                    |

Naver has two R8 triggers: content-platform value unlock and AI infra. Reuters reported Webtoon had 170M monthly active users, Q1 revenue of $326.7M, and a swing to $6.2M net income in its IPO filing; the IPO later priced at $21 at the top of range, raising about $315M at a $2.67B valuation. On debut, Webtoon shares rose as much as 14.3%, reaching $24 and implying a $2.71B valuation. ([Reuters][2])

The AI infra trigger is separate: Reuters reported Nvidia would supply more than 260,000 Blackwell chips to Korea and that Naver would buy 60,000 chips to increase compute capacity; Korea’s government would work with Naver and Kakao around the National AI Computing Center. This is Stage2 AI-infra evidence, not Stage3, because Naver still needs to show paid AI product usage, search/ad uplift, cloud/API margin and capex ROI. ([Reuters][3])

```json
{
  "case_id": "r8_loop15_naver_webtoon_nvidia_ai_infra",
  "symbol": "035420",
  "best_trigger": "T2/T3",
  "best_trigger_type": "Stage2-Actionable",
  "webtoon_maus_mn": 170,
  "webtoon_q1_revenue_usd_mn": 326.7,
  "webtoon_q1_revenue_growth_pct": 5,
  "webtoon_q1_net_income_usd_mn": 6.2,
  "webtoon_ipo_price_usd": 21,
  "webtoon_ipo_raise_usd_mn": 315,
  "webtoon_ipo_valuation_usd_bn": 2.67,
  "webtoon_debut_mfe_pct": 14.3,
  "webtoon_debut_high_usd": 24,
  "naver_blackwell_chip_purchase_units": 60000,
  "korea_total_blackwell_chips_units": 260000,
  "naver_direct_ohlc_status": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "Webtoon_profit_durability",
    "IP_adaptation_revenue",
    "AI_search_ad_uplift",
    "AI_cloud_margin",
    "Blackwell_capex_ROI"
  ],
  "trigger_outcome_label": "Stage2_Actionable_content_and_AI_infra"
}
```

---

## Case C — LG CNS / cloud-AI IPO

```text
symbol = LG_CNS
case_type = evidence_good_but_price_failed
archetype = CLOUD_AI_IT_SERVICES_EVIDENCE_GOOD_PRICE_FAILED
```

| trigger | type                        |       date | 당시 공개 evidence                                                       | 가격 anchor                                    | outcome                        |
| ------- | --------------------------- | ---------: | -------------------------------------------------------------------- | -------------------------------------------- | ------------------------------ |
| T0      | Stage2 evidence             | 2025-01-06 | IPO bookbuilding, price range 53,700~61,900 won, valuation $3.5~4.1B | no listing price yet                         | Stage2                         |
| T1      | Stage2 evidence             | 2025-02-05 | IPO at top range, 1.2T won raised, largest since LGES                | opened 60,500, traded 59,700 vs issue 61,900 | evidence good but price failed |
| T2      | Stage2-Actionable candidate | 2025-02-05 | cloud/AI 54% of sales in first 3Q 2024; 4T won revenue, 313B won OP  | same                                         | candidate                      |
| T3      | 4B/false-positive watch     | 2025-02-05 | weak IPO debut despite cloud/AI story; M&A plan vague                | below IPO price                              | false positive risk            |
| T4      | Stage3-Yellow               |        N/A | enterprise AI backlog / margin / M&A execution missing               | N/A                                          | no Yellow                      |

LG CNS는 R8의 전형적인 `evidence_good_but_price_failed`다. Reuters에 따르면 LG CNS는 IPO를 top range로 pricing해 1.2T won을 조달했지만, 상장일 주가는 issue price 61,900 won 아래인 59,700 won까지 내려갔다. 동시에 회사의 cloud/AI services가 2024년 첫 3개 분기 매출의 약 54%를 차지했고, 해당 기간 revenue는 약 4T won, operating profit은 313B won이었다. 즉 AI/cloud evidence는 분명하지만, **IPO price action은 Green을 거부했다.** ([Reuters][4])

```json
{
  "case_id": "r8_loop15_lg_cns_cloud_ai_ipo",
  "symbol": "LG_CNS",
  "best_trigger": "T1/T2",
  "best_trigger_type": "evidence_good_but_price_failed",
  "trigger_date": "2025-02-05",
  "ipo_issue_price_krw": 61900,
  "debut_open_price_krw": 60500,
  "debut_last_reported_price_krw": 59700,
  "debut_return_vs_issue_pct": -3.55,
  "ipo_raise_krw_trn": 1.2,
  "cloud_ai_sales_share_3q2024_pct": 54,
  "revenue_3q2024_krw_trn": 4.0,
  "op_3q2024_krw_bn": 313,
  "mna_use_of_proceeds_krw_bn": 390,
  "stage3_gate_missing": [
    "enterprise_AI_order_backlog",
    "cloud_AI_margin_expansion",
    "M&A_target_execution",
    "post_IPO_free_float_absorption",
    "recurring_revenue_visibility"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "evidence_good_but_price_failed"
}
```

---

## Case D — Samsung SDS / KKR convertible bond AI strategy

```text
symbol = 018260
case_type = Stage2-Actionable with 4B overlay
archetype = AI_SOFTWARE_CB_STRATEGIC_CAPITAL_STAGE2_WITH_4B
```

| trigger | type              |       date | 당시 공개 evidence                                                                           | 가격 anchor                                             | outcome           |
| ------- | ----------------- | ---------: | ---------------------------------------------------------------------------------------- | ----------------------------------------------------- | ----------------- |
| T0      | awareness         |  2025~2026 | AI transformation / enterprise IT services / physical AI theme                           | N/A                                                   | Stage1            |
| T1      | Stage2 evidence   | 2026-04-15 | KKR buys $820M newly issued Samsung SDS convertible bonds                                | shares as much as +20.8%, morning +19.4%, KOSPI +3.0% | Stage2-Actionable |
| T2      | Stage2-Actionable | 2026-04-15 | KKR strategic advice on M&A, capital allocation, AI offerings; Samsung SDS cash 6.4T won | same                                                  | Actionable        |
| T3      | 4B-watch          | 2026-04-15 | CB dilution, strategy includes physical AI/stablecoins, no immediate order backlog       | +20.8% event                                          | 4B overlay        |
| T4      | Stage3-Yellow     |        N/A | AI order backlog / M&A closure / margin expansion missing                                | N/A                                                   | no Yellow         |

Samsung SDS is one of the strongest R8 Stage2-Actionable cases. Reuters reported KKR would buy $820M of newly issued convertible bonds, sending Samsung SDS shares up as much as 20.8% while KOSPI rose 3.0%. KKR would advise on M&A, capital allocation and AI offerings; Samsung SDS said it had 6.4T won in cash and would invest in AI infra, physical AI, stablecoins and M&A. This is **Stage2-Actionable**, but CB dilution and lack of immediate enterprise backlog require a 4B overlay. ([Reuters][5])

```json
{
  "case_id": "r8_loop15_samsung_sds_kkr_cb_ai",
  "symbol": "018260",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable_with_4B_overlay",
  "trigger_date": "2026-04-15",
  "convertible_bond_value_usd_mn": 820,
  "event_mfe_pct": 20.8,
  "morning_return_pct": 19.4,
  "kospi_same_context_pct": 3.0,
  "market_relative_return_pp": 17.8,
  "cash_and_equivalents_krw_trn": 6.4,
  "strategic_focus": [
    "AI infrastructure",
    "AI transformation",
    "M&A",
    "physical AI",
    "stablecoins"
  ],
  "stage3_gate_missing": [
    "AI_order_backlog",
    "M&A_closure",
    "margin_expansion",
    "CB_dilution_absorption",
    "enterprise_customer_wins"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_Actionable_with_CB_4B_overlay"
}
```

---

## Case E — Krafton / ADK acquisition + India tech fund

```text
symbol = 259960
case_type = Stage2-Actionable
archetype = CONTENT_MA_IP_EXPANSION_STAGE2 / GAME_IP_GLOBALIZATION_STAGE2_ACTIONABLE
```

| trigger | type              |                                     date | 당시 공개 evidence                                                                  | 가격 anchor          | outcome             |
| ------- | ----------------- | ---------------------------------------: | ------------------------------------------------------------------------------- | ------------------ | ------------------- |
| T0      | awareness         |                                2024~2025 | PUBG/BGMI global IP, India gaming exposure                                      | no direct price    | Stage1              |
| T1      | Stage2 evidence   |                               2025-06-24 | Krafton agrees to buy Japan ADK for ¥75B / $516M                                | no KRX event price | Stage2              |
| T2      | Stage2-Actionable |                               2025-06-24 | ADK participated in 300+ animations incl. Doraemon, Yu-Gi-Oh!, Crayon Shin-chan | no price           | IP expansion        |
| T3      | Stage2 evidence   |                               2025-12-19 | Krafton/Naver/Mirae $666M India fund; Krafton invested >$200M in India          | no price           | geography expansion |
| T4      | 4C-watch          | India BGMI regulatory/data-security risk | BGMI 240M downloads but previous temporary ban                                  | regulatory overlay |                     |
| T5      | Stage3-Yellow     |                                      N/A | ADK integration / new IP revenue / fund return missing                          | N/A                | no Yellow           |

Krafton is a Stage2-Actionable platform/content IP expansion case. Reuters reported Krafton agreed to buy ADK Holdings’ parent for ¥75B, about $516M; ADK had participated in more than 300 animation productions including IPs such as Doraemon, Yu-Gi-Oh! and Crayon Shin-chan. This is not just a financial investment but an IP pipeline expansion trigger. ([Reuters][6])

The India trigger is separate. Reuters reported Krafton would lead a $666M India-focused tech fund with Naver and Mirae Asset, while Krafton had already invested more than $200M in India; BGMI had more than 240M downloads but had previously faced data-security-linked regulatory bans. That makes Krafton `Stage2-Actionable` with a regulatory/data overlay, not Green. ([Reuters][7])

```json
{
  "case_id": "r8_loop15_krafton_adk_india_ip_expansion",
  "symbol": "259960",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2-Actionable",
  "adk_acquisition_value_jpy_bn": 75,
  "adk_acquisition_value_usd_mn": 516.21,
  "adk_animation_productions_count": 300,
  "example_ips": ["Doraemon", "Yu-Gi-Oh!", "Crayon Shin-chan"],
  "india_fund_target_usd_mn": 666,
  "india_fund_initial_pool_usd_mn": 333,
  "krafton_india_prior_investment_usd_mn": 200,
  "bgmi_downloads_mn": 240,
  "regulatory_history": "temporary ban / data security concerns",
  "direct_krafton_event_price": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "ADK_integration",
    "new_IP_revenue",
    "India_fund_return",
    "BGMI_regulatory_stability",
    "non_PUBG_revenue_share"
  ],
  "trigger_outcome_label": "Stage2_Actionable_IP_and_geography_expansion"
}
```

---

## Case F — Shift Up / IPO + Stellar Blade + Nikke IP

```text
symbol = 462870
case_type = Stage2-Actionable / IP concentration watch
archetype = GAME_IP_GLOBALIZATION_STAGE2_ACTIONABLE
```

| trigger | type              |        date | 당시 공개 evidence                                                                   | 가격 anchor          | outcome    |
| ------- | ----------------- | ----------: | -------------------------------------------------------------------------------- | ------------------ | ---------- |
| T0      | awareness         |     2024-04 | Stellar Blade PS5 launched; strong Japan/North America rankings                  | no KRX listing yet | Stage1     |
| T1      | Stage2 evidence   |  2024-06-27 | IPO expected at top range, 435B won raise, 3.5T won valuation                    | pre-listing        | Stage2     |
| T2      | Stage2-Actionable |  2024-06-27 | Nikke sales 255B won from global launch to Q1 2024, 2023 OP 111B on 169B revenue | no debut OHLC      | Actionable |
| T3      | 4B-watch          | IPO/listing | Tencent 40% pre-IPO, expected 35% post; high valuation and IP concentration      | no full price      | 4B         |
| T4      | Stage3-Yellow     |         N/A | post-IPO recurring revenue / PC port / sequel / new title monetization missing   | N/A                | no Yellow  |

Shift Up’s pre-IPO evidence was strong enough for Stage2-Actionable. Reuters reported the company was likely to price at the top of the band, raising 435B won at a 3.5T won valuation; Tencent had a 40% stake pre-IPO and would fall to about 35%. Importantly, this was not just an IPO hype story: Nikke had generated 255B won in sales from global launch to Q1 2024, Stellar Blade ranked No. 1 in Japan’s PlayStation downloads and No. 2 in North America, and 2023 OP was 111B won on 169B won revenue. ([Reuters][8])

The missing gate is post-IPO durability: recurrent Nikke revenue, Stellar Blade PC/sequel economics, new-title pipeline and Tencent/customer concentration. Therefore this is `Stage2-Actionable`, not Green.

```json
{
  "case_id": "r8_loop15_shiftup_ipo_stellarblade_nikke",
  "symbol": "462870",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable",
  "trigger_date": "2024-06-27",
  "ipo_raise_krw_bn": 435,
  "ipo_raise_usd_mn": 313,
  "expected_market_cap_krw_trn": 3.5,
  "expected_market_cap_usd_bn": 2.52,
  "tencent_pre_ipo_stake_pct": 40,
  "tencent_expected_post_ipo_stake_pct": 35,
  "nikke_sales_krw_bn": 255,
  "op_2023_krw_bn": 111,
  "revenue_2023_krw_bn": 169,
  "stellar_blade_japan_ps_download_rank": 1,
  "stellar_blade_north_america_ps_download_rank": 2,
  "direct_shiftup_debut_price": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "post_IPO_revenue_growth",
    "Nikke_retention",
    "Stellar_Blade_PC_or_sequel_revenue",
    "new_project_pipeline",
    "IP_concentration_risk_control"
  ],
  "trigger_outcome_label": "Stage2_Actionable_game_IP"
}
```

---

## Case G — HYBE / NewJeans governance and SM/Tencent China optionality

```text
symbols = 352820 / 041510 / 035720
case_type = artist governance 4C-watch + China reopening Stage2 reference
archetype = KPOP_ARTIST_GOVERNANCE_4C_WATCH
```

| trigger | type                     |                                                         date | 당시 공개 evidence                                                                                    | 가격 anchor                   | outcome                 |
| ------- | ------------------------ | -----------------------------------------------------------: | ------------------------------------------------------------------------------------------------- | --------------------------- | ----------------------- |
| T0      | 4C-watch                 |                                                   2024-04-24 | HYBE audits ADOR over alleged independence plot; NewJeans IP governance dispute                   | HYBE shares fell nearly -8% | artist IP governance 4C |
| T1      | 4C-watch                 |                                                   2025-03-21 | court blocks NewJeans from independent activities, upholds ADOR role                              | HYBE price unavailable      | legal overhang          |
| T2      | Stage2 China optionality |                                                   2025-05-27 | Tencent becomes SM second-largest shareholder via 9.7% stake from HYBE, signs of China K-pop thaw | no SM event return          | Stage2                  |
| T3      | Stage3-Yellow            |                                                          N/A | China concerts / ticket revenue / artist schedule not confirmed                                   | N/A                         | no Yellow               |
| T4      | hard 4C                  | if artist contract collapse / injunction causes revenue loss | not confirmed                                                                                     | watch                       |                         |

HYBE/NewJeans is a clear R8 4C-watch. Reuters reported HYBE launched an audit against ADOR leadership over suspected plans to become independent, and HYBE shares fell nearly 8% amid the dispute. A year later, a Seoul court blocked NewJeans members from pursuing independent activities and affirmed ADOR’s management role, keeping artist IP governance as a live overhang. ([Reuters][9])

SM/Tencent is a different trigger: Tencent Music bought HYBE’s 9.7% SM stake for 243B won, making it the second-largest shareholder after Kakao/Kakao Entertainment’s 42% controlling stake; Reuters noted signs of a potential thaw in China’s unofficial K-pop performance ban. This is `Stage2 China optionality`, not Stage3, until concerts, ticket revenue and artist schedules are actually confirmed. ([Reuters][10])

```json
{
  "case_id": "r8_loop15_hybe_newjeans_sm_tencent_kpop_governance",
  "symbols": "352820/041510/035720",
  "best_trigger": "T0/T1/T2",
  "best_trigger_type": "4C_artist_governance_watch_plus_Stage2_China_optionality",
  "hybe_audit_date": "2024-04-24",
  "hybe_audit_event_mae_pct": -8,
  "court_injunction_date": "2025-03-21",
  "newjeans_independent_activity_blocked": true,
  "sm_tencent_transaction_date": "2025-05-27",
  "sm_stake_sold_pct": 9.7,
  "sm_stake_sale_value_krw_bn": 243,
  "kakao_sm_control_stake_pct": 42,
  "china_kpop_thaw_optionality": true,
  "stage3_gate_missing": [
    "artist_contract_resolution",
    "China_concert_approval",
    "ticket_revenue",
    "album_or_tour_schedule",
    "management_fee_stability"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "artist_governance_4C_watch_and_China_optional_Stage2"
}
```

---

## Case H — SK Telecom data breach / cybersecurity hard gate reference

```text
symbol = 017670
case_type = hard 4C reference
archetype = CYBERSECURITY_DATA_BREACH_HARD_4C
```

| trigger | type            |       date | 당시 공개 evidence                                                                                                 | 가격 anchor                                | outcome           |
| ------- | --------------- | ---------: | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ----------------- |
| T0      | 4C              | 2025-04-28 | malware-driven customer data leak disclosed; 23M subscribers offered USIM replacement                          | intraday -8.5%, close -6.7%, KOSPI +0.1% | hard security 4C  |
| T1      | 4C validation   | 2025-07-04 | government says negligent; 26.96M data pieces leaked; fine/order to strengthen security                        | SKT -5.6%                                | hard validation   |
| T2      | cost validation | 2025-07-04 | 700B won five-year data-protection investment; 50% August subscription discount; 800B won revenue forecast cut | same                                     | cost-confirmed 4C |
| T3      | relief          |        N/A | trust recovery / churn control / security investment execution not confirmed                                   | N/A                                      | no relief yet     |

SK Telecom is the R8 security hard-gate template. Reuters reported SKT shares fell as much as 8.5% and closed -6.7% after a customer data leak caused by a cyberattack; the company offered free USIM replacement to all 23M users and urged signups for its USIM Protection Service. Later, regulators said SKT was negligent after 26.96M pieces of user data were leaked; shares closed -5.6%, the company announced 700B won of security investment over five years, a 50% August subscription discount for 24M customers, and cut its 2025 revenue forecast by 800B won to reflect breach-related costs. ([Reuters][11])

```json
{
  "case_id": "r8_loop15_skt_data_breach_security_4c",
  "symbol": "017670",
  "best_trigger": "T0/T1/T2",
  "best_trigger_type": "hard_4C_security",
  "t0_date": "2025-04-28",
  "t0_intraday_mae_pct": -8.5,
  "t0_close_return_pct": -6.7,
  "t0_kospi_return_pct": 0.1,
  "subscribers_affected_context_mn": 23,
  "t1_date": "2025-07-04",
  "data_pieces_leaked_mn": 26.96,
  "t1_close_return_pct": -5.6,
  "security_investment_5y_krw_bn": 700,
  "revenue_forecast_cut_2025_krw_bn": 800,
  "customer_benefit_package_cost_krw_bn": 500,
  "august_subscription_discount_pct": 50,
  "usim_replacements_by_late_june_mn": 9.39,
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "hard_4c_success_security_trust"
}
```

---

# 6. Trigger별 가격경로 검증 요약

| case                 | best trigger |           entry anchor |                         event MFE/MAE |             market-relative | full MFE/MAE | outcome                        |
| -------------------- | ------------ | ---------------------: | ------------------------------------: | --------------------------: | ------------ | ------------------------------ |
| Kakao/OpenAI         | T1/T2        |                  event |               +9% initial → -2% close |                 unavailable | unavailable  | Stage2, monetization gate      |
| Naver/Webtoon/Nvidia | T2/T3        | Webtoon IPO / AI chips |          WBTN +14.3%, Naver 60k chips |           Naver unavailable | unavailable  | Stage2 content + AI infra      |
| LG CNS IPO           | T1/T2        |           61,900 issue | 59,700 last reported, -3.55% vs issue |                 unavailable | unavailable  | evidence good but price failed |
| Samsung SDS/KKR      | T1/T2        |                  event |                   +20.8%, KOSPI +3.0% |                     +17.8pp | unavailable  | Stage2 + 4B                    |
| Krafton/ADK/India    | T1/T3        |               no price |                     deal anchors only |                 unavailable | unavailable  | Stage2 IP/geography            |
| Shift Up IPO         | T1/T2        |         no debut price |     IPO 435B won / valuation 3.5T won |                 unavailable | unavailable  | Stage2 game IP                 |
| HYBE/NewJeans        | T0/T1        |                  event |              HYBE nearly -8% on audit |                 unavailable | unavailable  | artist governance 4C           |
| SK Telecom breach    | T0/T1/T2     |                  event |                     -6.7%, then -5.6% | -6.8pp first event vs KOSPI | unavailable  | hard security 4C               |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
Kakao/OpenAI:
AI messaging partnership is Stage2, but -2% close after +9% initial says monetization is not yet priced as Green.

Naver/Webtoon:
Webtoon IPO is a clean content-platform value-unlock Stage2; Nvidia 60k Blackwell chip purchase is AI infra Stage2.

Krafton/ADK:
ADK acquisition and India fund are Stage2 IP/geography expansion, but new-IP revenue and regulatory stability are missing.

Shift Up:
IPO and IP revenue evidence are strong, but post-IPO revenue durability and IP concentration are unresolved.
```

## Stage 2-Actionable entry 성과

```text
Samsung SDS:
KKR CB +20.8% is one of the strongest R8 Stage2-Actionable triggers.
But CB dilution and execution risk mean Stage3 cannot be given yet.

Naver/Webtoon:
Webtoon +14.3% debut pop is Actionable content-platform value unlock, but Naver direct MFE is unavailable.

Kakao:
initial +9% was Actionable, but close -2% weakens it to evidence_good_but_price_failed.
```

## Stage3-Yellow 후보

```text
Samsung SDS:
If AI order backlog / M&A execution / margin expansion follows, Stage3-Yellow possible.

Naver:
If AI infra converts into paid AI search/cloud usage, Yellow possible.

Krafton:
If ADK integration creates measurable new IP revenue or India fund creates strategic monetization, Yellow possible.

Shift Up:
If Stellar Blade PC/sequel and Nikke retention confirm recurrent revenue, Yellow possible.
```

## Stage3-Green

```text
이번 R8 Loop 15에서 확정 Green 없음.

이유:
- AI partnerships lack paid usage / margin data.
- Content IPOs lack durable post-listing profitability in KRX parent price.
- Game IP lacks post-launch retention / live-service conversion evidence.
- Cloud/SW lacks enterprise order backlog and margin.
- Security cases are 4C, not growth.
```

## 기존 점수표가 놓쳤을 가능성

```text
Stage2_promote_candidate:
- Samsung SDS / KKR CB
- Naver / Webtoon IPO
- Krafton / ADK + India
- Shift Up / IP-IPO
- Kakao/OpenAI, weaker due close -2%

missed_structural 가능성:
- Samsung SDS if subsequent AI/M&A orders validate the +20.8% trigger.
- Shift Up if post-IPO IP revenue/PC port/sequel created strong MFE.
- Naver if AI infra and Webtoon value unlock translate to parent rerating.

false_positive risk:
- LG CNS AI/cloud IPO
- Kakao OpenAI if no paid usage
- Samsung SDS if CB rally was only financial-engineering hype
```

---

# 8. score-price alignment 판정

```text
Stage2_promote_candidate:
- Samsung SDS / KKR CB
- Naver / Webtoon IPO + Nvidia AI infra
- Krafton / ADK + India fund
- Shift Up / IPO + IP revenue

evidence_good_but_price_failed:
- LG CNS IPO
- Kakao/OpenAI, because initial +9% faded to -2% close

event_premium:
- Webtoon IPO pop if not followed by profitability
- Tencent/SM China-thaw optionality
- Krafton ADK if treated as immediate earnings

false_positive_score:
- LG CNS if AI/cloud IPO is treated as Green despite weak debut
- Kakao if OpenAI headline is treated as monetized AI revenue
- Samsung SDS if CB/dilution ignored

thesis_break_watch:
- HYBE/NewJeans artist governance
- SK Telecom data breach
- Coupang-style platform breach reference, not included as KRX main row

hard_4c_success:
- SK Telecom data breach
```

---

# 9. 점수비중 교정

## 올릴 축

```text
paid_AI_usage_conversion +5
AI_cloud_margin_visibility +5
enterprise_order_backlog +5
content_IP_monetization +5
game_sellthrough_and_retention +5
global_IP_licensing +4
platform_user_data_security +5
artist_contract_governance +5
M&A_integration_revenue +4
AI_infra_capex_ROI +5
```

### 근거

Samsung SDS는 KKR/AI/M&A trigger가 강했지만, 실제 기업고객 order backlog와 margin이 닫혀야 Yellow로 올라간다. Kakao는 OpenAI partner라는 이름보다 KakaoTalk 내 유료 usage와 retention이 중요하다. Naver는 Webtoon MAU와 IPO pop, Nvidia chip purchase가 강하지만, parent-level AI/search/cloud monetization이 닫혀야 한다. SKT breach는 platform/user-data security가 R8 hard gate임을 보여준다.

## 내릴 축

```text
AI_partnership_headline_only -5
IPO_pop_without_parent_monetization -4
cloud_AI_sales_mix_without_price_confirmation -4
CB_capital_injection_without_order_backlog -4
IP_acquisition_without_revenue_synergy -4
game_IP_hype_without_retention -5
artist_name_without_contract_control -5
security_capex_after_breach_as_positive -5
```

### 근거

LG CNS는 cloud/AI sales mix가 있어도 weak debut가 나왔다. Kakao는 OpenAI headline 후 +9% initial move가 -2% close로 식었다. Samsung SDS는 +20.8%였지만 CB/dilution과 backlog gate가 남아 있다. HYBE/NewJeans는 artist IP가 revenue source인 동시에 governance hard gate가 될 수 있다. SKT의 700B won security investment는 성장 capex가 아니라 breach cost recovery다.

---

# 10. Stage 2-Actionable 승격 조건

R8 Loop 15 shadow rule:

```text
R8에서 Stage 2 evidence가 아래 중 3개 이상이면 Stage2-Actionable로 승격한다.

1. AI partnership이 실제 product integration 또는 infra purchase로 연결된다.
2. cloud/AI revenue share가 숫자로 확인된다.
3. IPO/M&A가 MAU, revenue, profit, IP library, user base를 동반한다.
4. event 당일 market-relative +5pp 이상 가격 반응이 있다.
5. game/content IP가 실제 sales, downloads, MAU, retention, licensing으로 연결된다.
6. enterprise SW는 backlog, recurring revenue, margin, customer wins 중 하나가 확인된다.
7. 보안/데이터 리스크가 없거나 통제 가능하다.
```

적용:

```text
Samsung SDS:
KKR CB + AI/M&A + +20.8% → Stage2-Actionable.

Naver/Webtoon:
170M MAU + IPO top pricing + +14.3% debut → Stage2-Actionable.

Krafton:
ADK IP assets + India fund + BGMI downloads → Stage2-Actionable.

Shift Up:
Nikke sales + Stellar Blade ranking + IPO valuation → Stage2-Actionable.
```

---

# 11. Stage 3-Yellow 조건

```text
Stage3-Yellow:
- AI/product/content trigger가 EPS/OP/FCF 경로를 바꿀 가능성이 숫자로 보임
- 하지만 monetization, margin, retention, integration, governance 중 하나가 남음
```

후보:

```text
Samsung SDS:
AI order backlog / M&A execution / margin 확인 시 Yellow.

Naver:
AI infra usage / Webtoon profitability / parent-level monetization 확인 시 Yellow.

Krafton:
ADK integration and India monetization 확인 시 Yellow.

Shift Up:
Stellar Blade PC/sequel and Nikke retention 확인 시 Yellow.

Kakao:
KakaoTalk AI paid usage and ad uplift 확인 시 Yellow.
```

---

# 12. Stage 3-Green 조건

```text
Stage3-Green:
- AI partnership이 paid usage / API revenue / ad uplift / margin으로 전환됨
- 콘텐츠 IP가 recurring revenue / licensing / sequel pipeline으로 확인됨
- 게임 IP가 launch 이후 retention과 live-service revenue를 유지함
- SW/cloud가 enterprise backlog와 recurring margin을 보여줌
- 보안/규제/데이터 리스크가 hard gate를 통과함
- full-window MFE/MAE가 우호적
```

이번 R8 Loop 15에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- AI partnership headline으로 급등하지만 유료 사용량 없음
- IPO pop이 parent EPS/FCF로 연결되지 않음
- CB/전략투자 발표로 +20% 급등하지만 order backlog 없음
- 게임/IP M&A가 즉시 earnings로 과대평가됨
- K-pop artist dispute가 revenue보다 sentiment로만 가격을 흔듦
- security capex를 growth capex처럼 해석함
```

적용:

```text
Samsung SDS:
+20.8%는 Actionable이지만 CB/dilution 4B overlay.

LG CNS:
AI/cloud IPO story에도 weak debut → false positive watch.

Kakao:
OpenAI headline +9% initial → -2% close → monetization 없는 4B/false-positive watch.

Naver/Webtoon:
IPO pop은 good trigger but parent monetization gate.
```

---

# 14. 4C hard gate 조건

```text
R8 4C:
- data breach / customer-data leak
- regulatory finding of negligence
- revenue forecast cut due breach compensation
- artist contract collapse / injunction blocking activities
- IP rights dispute affecting release schedule
- AI/data privacy violation
- cloud/security failure causing enterprise churn
- crypto/platform custody or customer-data incident
```

이번 R8 Loop 15 hard 4C:

```text
SK Telecom data breach = hard_4c_success
```

Strong 4C-watch:

```text
- HYBE/NewJeans artist governance
- Kakao broader governance/legal overlay from R6
- LG CNS weak IPO if AI/cloud backlog fails
- Krafton India data-security regulatory history
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_231.md 요약

```md
# R8 Loop 15. Platform / Content / SW / Security Trigger-level Price Validation

이번 라운드는 R8 Loop 15 trigger-level validation 라운드다.

핵심 결론:
- Kakao / OpenAI is Stage2-Actionable with monetization gate. OpenAI partnership and KakaoTalk 97% domestic messaging share are real evidence, but Kakao shares fell 2% after an initial 9% surge. Green requires paid AI usage, retention, ad uplift and margin.
- Naver / Webtoon / Nvidia AI infra is Stage2-Actionable. Webtoon had 170M MAU, Q1 revenue $326.7M and $6.2M net income; IPO raised $315M at $2.67B valuation; debut rose 14.3%. Naver also plans to buy 60,000 Nvidia Blackwell chips. Green requires parent-level monetization.
- LG CNS is evidence_good_but_price_failed. Cloud/AI services were 54% of sales in first 3Q 2024, but IPO shares traded below the 61,900 won issue price on debut.
- Samsung SDS / KKR CB is Stage2-Actionable with 4B overlay. KKR will buy $820M of convertible bonds; shares jumped as much as 20.8%. AI/M&A strategy is strong, but CB dilution and order backlog remain gates.
- Krafton / ADK / India fund is Stage2-Actionable. ADK acquisition worth $516M adds animation IP; India fund target is $666M; BGMI has 240M downloads but regulatory/data-security risk remains.
- Shift Up is Stage2-Actionable game IP. 435B won IPO, 3.5T won valuation, Nikke 255B won sales, Stellar Blade PS ranking; Green requires post-IPO revenue durability and IP concentration control.
- HYBE / NewJeans is artist governance 4C-watch. HYBE shares fell nearly 8% on ADOR audit; court blocked NewJeans independent activities. SM/Tencent is separate Stage2 China optionality.
- SK Telecom data breach is hard R8 4C. Shares closed -6.7% after breach disclosure and -5.6% after government negligence finding. 26.96M pieces of data leaked, 700B won security investment and 800B won 2025 revenue forecast cut.

Main calibration:
- Raise paid AI usage conversion, AI cloud margin visibility, enterprise order backlog, content IP monetization, game sell-through/retention, global IP licensing, user-data security, artist-contract governance, M&A integration revenue, AI infra capex ROI.
- Lower AI partnership headline-only, IPO pop without parent monetization, cloud/AI sales mix without price confirmation, CB capital injection without backlog, IP acquisition without synergy, game IP hype without retention, artist name without contract control, security capex after breach as positive.
```

## docs/checkpoints/checkpoint_28a_round231_r8_loop15.md 요약

```md
# Checkpoint 28A Round 231 R8 Loop 15 Trigger-level Calibration

## 반영 내용
- R8 Loop 15 trigger-level validation을 수행했다.
- Kakao/OpenAI, Naver/Webtoon/Nvidia, LG CNS, Samsung SDS/KKR, Krafton/ADK/India, Shift Up, HYBE/NewJeans/SM-Tencent, SK Telecom data breach를 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 Reuters / FT / WSJ / MarketWatch / AP의 reported event return과 event price anchor를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- AI partnership은 paid usage, retention, ad uplift, cloud/API margin 전에는 Green 금지.
- 콘텐츠/게임 IP는 launch ranking이나 IPO가 아니라 sales, retention, recurring revenue, licensing으로 승격한다.
- SW/cloud는 sales mix보다 enterprise order backlog와 margin 확인이 중요하다.
- security/data breach는 R8 hard gate이며, 보안투자는 성장 capex가 아니라 trust-repair cost로 분리한다.
```

## data/e2r_case_library/cases_r8_loop15_round231.jsonl 초안

```jsonl
{"case_id":"r8_loop15_kakao_openai_ai_messaging","symbol":"035720","company_name":"Kakao","case_type":"Stage2_Actionable_but_evidence_good_price_failed","primary_archetype":"AI_MESSAGING_PARTNERSHIP_STAGE2_WITH_MONETIZATION_GATE","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2025-02-04","kakaotalk_domestic_share_pct":97,"initial_event_mfe_pct":9,"close_event_return_pct":-2,"partner":"OpenAI","product_focus":["AI products","messaging"],"stage3_gate_missing":["paid_AI_usage","KakaoTalk_AI_retention","ad_revenue_uplift","API_cloud_cost_margin","data_privacy_clearance"],"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"evidence_good_but_price_failed","notes":"OpenAI headline and KakaoTalk base are Stage2-Actionable, but monetization was not confirmed."}
{"case_id":"r8_loop15_naver_webtoon_nvidia_ai_infra","symbol":"035420","company_name":"Naver / Webtoon Entertainment","case_type":"Stage2_promote_candidate","primary_archetype":"AI_INFRA_PORTAL_STAGE2_ACTIONABLE/WEBTOON_IPO_CONTENT_PLATFORM_STAGE2","best_trigger":"T2/T3","stage_candidate":"Stage2-Actionable","price_validation":{"webtoon_maus_mn":170,"webtoon_q1_revenue_usd_mn":326.7,"webtoon_q1_revenue_growth_pct":5,"webtoon_q1_net_income_usd_mn":6.2,"webtoon_ipo_price_usd":21,"webtoon_ipo_raise_usd_mn":315,"webtoon_ipo_valuation_usd_bn":2.67,"webtoon_debut_mfe_pct":14.3,"webtoon_debut_high_usd":24,"naver_blackwell_chip_purchase_units":60000,"korea_total_blackwell_chips_units":260000,"naver_direct_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate","notes":"Webtoon IPO and Naver AI infra are Stage2-Actionable; parent-level AI/content monetization still needed."}
{"case_id":"r8_loop15_lg_cns_cloud_ai_ipo","symbol":"LG_CNS","company_name":"LG CNS","case_type":"evidence_good_but_price_failed","primary_archetype":"CLOUD_AI_IT_SERVICES_EVIDENCE_GOOD_PRICE_FAILED","best_trigger":"T1/T2","stage_candidate":"Stage2","price_validation":{"trigger_date":"2025-02-05","ipo_issue_price_krw":61900,"debut_open_price_krw":60500,"debut_last_reported_price_krw":59700,"debut_return_vs_issue_pct":-3.55,"ipo_raise_krw_trn":1.2,"cloud_ai_sales_share_3q2024_pct":54,"revenue_3q2024_krw_trn":4.0,"op_3q2024_krw_bn":313,"mna_use_of_proceeds_krw_bn":390,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"evidence_good_but_price_failed","notes":"Cloud/AI sales mix was real but weak IPO debut blocks Green."}
{"case_id":"r8_loop15_samsung_sds_kkr_cb_ai","symbol":"018260","company_name":"Samsung SDS","case_type":"Stage2_Actionable_with_4B_overlay","primary_archetype":"AI_SOFTWARE_CB_STRATEGIC_CAPITAL_STAGE2_WITH_4B","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable + 4B-watch","price_validation":{"trigger_date":"2026-04-15","convertible_bond_value_usd_mn":820,"event_mfe_pct":20.8,"morning_return_pct":19.4,"kospi_same_context_pct":3.0,"market_relative_return_pp":17.8,"cash_and_equivalents_krw_trn":6.4,"strategic_focus":["AI infrastructure","AI transformation","M&A","physical AI","stablecoins"],"stage3_gate_missing":["AI_order_backlog","M&A_closure","margin_expansion","CB_dilution_absorption","enterprise_customer_wins"],"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate_with_4B_overlay","notes":"KKR strategic capital is actionable, but CB/dilution and backlog gates remain."}
{"case_id":"r8_loop15_krafton_adk_india_ip_expansion","symbol":"259960","company_name":"Krafton","case_type":"Stage2_promote_candidate","primary_archetype":"CONTENT_MA_IP_EXPANSION_STAGE2/GAME_IP_GLOBALIZATION_STAGE2_ACTIONABLE","best_trigger":"T1/T3","stage_candidate":"Stage2-Actionable","price_validation":{"adk_acquisition_value_jpy_bn":75,"adk_acquisition_value_usd_mn":516.21,"adk_animation_productions_count":300,"example_ips":["Doraemon","Yu-Gi-Oh!","Crayon Shin-chan"],"india_fund_target_usd_mn":666,"india_fund_initial_pool_usd_mn":333,"krafton_india_prior_investment_usd_mn":200,"bgmi_downloads_mn":240,"regulatory_history":"temporary ban / data security concerns","direct_krafton_event_price":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate","notes":"ADK and India fund expand IP/geography, but integration, new-IP revenue and regulatory stability remain gates."}
{"case_id":"r8_loop15_shiftup_ipo_stellarblade_nikke","symbol":"462870","company_name":"Shift Up","case_type":"Stage2_promote_candidate","primary_archetype":"GAME_IP_GLOBALIZATION_STAGE2_ACTIONABLE","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2024-06-27","ipo_raise_krw_bn":435,"ipo_raise_usd_mn":313,"expected_market_cap_krw_trn":3.5,"expected_market_cap_usd_bn":2.52,"tencent_pre_ipo_stake_pct":40,"tencent_expected_post_ipo_stake_pct":35,"nikke_sales_krw_bn":255,"op_2023_krw_bn":111,"revenue_2023_krw_bn":169,"stellar_blade_japan_ps_download_rank":1,"stellar_blade_north_america_ps_download_rank":2,"direct_shiftup_debut_price":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate","notes":"Nikke sales, Stellar Blade ranking and IPO valuation support Stage2-Actionable; Green needs post-IPO durability."}
{"case_id":"r8_loop15_hybe_newjeans_sm_tencent_kpop_governance","symbol":"352820/041510/035720","company_name":"HYBE / NewJeans / SM / Tencent / Kakao","case_type":"4C_artist_governance_watch_plus_Stage2_China_optionality","primary_archetype":"KPOP_ARTIST_GOVERNANCE_4C_WATCH","best_trigger":"T0/T1/T2","stage_candidate":"4C-watch / Stage2 China optionality","price_validation":{"hybe_audit_date":"2024-04-24","hybe_audit_event_mae_pct":-8,"court_injunction_date":"2025-03-21","newjeans_independent_activity_blocked":true,"sm_tencent_transaction_date":"2025-05-27","sm_stake_sold_pct":9.7,"sm_stake_sale_value_krw_bn":243,"kakao_sm_control_stake_pct":42,"china_kpop_thaw_optionality":true,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","notes":"Artist IP governance is 4C-watch; China reopening is Stage2 until concerts and ticket revenue confirm."}
{"case_id":"r8_loop15_skt_data_breach_security_4c","symbol":"017670","company_name":"SK Telecom","case_type":"hard_4c_reference","primary_archetype":"CYBERSECURITY_DATA_BREACH_HARD_4C","best_trigger":"T0/T1/T2","stage_candidate":"4C","price_validation":{"t0_date":"2025-04-28","t0_intraday_mae_pct":-8.5,"t0_close_return_pct":-6.7,"t0_kospi_return_pct":0.1,"subscribers_affected_context_mn":23,"t1_date":"2025-07-04","data_pieces_leaked_mn":26.96,"t1_close_return_pct":-5.6,"security_investment_5y_krw_bn":700,"revenue_forecast_cut_2025_krw_bn":800,"customer_benefit_package_cost_krw_bn":500,"august_subscription_discount_pct":50,"usim_replacements_by_late_june_mn":9.39,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"hard_4c_success","notes":"Data breach is R8 hard 4C; security investment after breach is trust-repair cost, not growth capex."}
```

## data/e2r_trigger_calibration/triggers_r8_loop15_round231.jsonl 초안

```jsonl
{"trigger_id":"r8l15_kakao_openai_T1","case_id":"r8_loop15_kakao_openai_ai_messaging","trigger_type":"Stage2-Actionable","trigger_date":"2025-02-04","evidence_available":"OpenAI-Kakao AI product partnership, KakaoTalk 97% domestic messaging share, initial +9% then -2% close","event_return_pct":"initial +9 / close -2","trigger_outcome_label":"evidence_good_but_price_failed","promote_to":"Stage2-Actionable_only"}
{"trigger_id":"r8l15_naver_webtoon_T2","case_id":"r8_loop15_naver_webtoon_nvidia_ai_infra","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-27","evidence_available":"Webtoon IPO priced at $21, raised $315M, 170M MAU, debut +14.3%","event_return_pct":14.3,"trigger_outcome_label":"Stage2_promote_candidate","promote_to":"Stage2-Actionable"}
{"trigger_id":"r8l15_naver_blackwell_T3","case_id":"r8_loop15_naver_webtoon_nvidia_ai_infra","trigger_type":"Stage2_AI_infra","trigger_date":"2025-10-31","evidence_available":"Naver to buy 60,000 Nvidia Blackwell chips; Korea total 260,000 chips; National AI Computing Center context","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_AI_infra","promote_to":"Stage2"}
{"trigger_id":"r8l15_lgcns_ipo_T1","case_id":"r8_loop15_lg_cns_cloud_ai_ipo","trigger_type":"evidence_good_but_price_failed","trigger_date":"2025-02-05","evidence_available":"Cloud/AI 54% of sales, IPO raised 1.2T won, but debut traded below 61,900 won issue price at 59,700 won","event_return_pct":-3.55,"trigger_outcome_label":"evidence_good_but_price_failed","promote_to":"Stage2_only"}
{"trigger_id":"r8l15_samsungsds_kkr_T1","case_id":"r8_loop15_samsung_sds_kkr_cb_ai","trigger_type":"Stage2-Actionable+4B-watch","trigger_date":"2026-04-15","evidence_available":"KKR buys $820M Samsung SDS CB, shares +20.8%, KKR to advise on M&A/capital allocation/AI offerings","event_return_pct":20.8,"market_relative_return_pp":17.8,"trigger_outcome_label":"Stage2_promote_candidate_with_4B_overlay","promote_to":"Stage2-Actionable"}
{"trigger_id":"r8l15_krafton_adk_T1","case_id":"r8_loop15_krafton_adk_india_ip_expansion","trigger_type":"Stage2-Actionable","trigger_date":"2025-06-24","evidence_available":"Krafton to buy ADK for ¥75B/$516M; ADK involved in 300+ animations including Doraemon/Yu-Gi-Oh!/Crayon Shin-chan","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_IP_expansion","promote_to":"Stage2-Actionable"}
{"trigger_id":"r8l15_shiftup_ipo_T1","case_id":"r8_loop15_shiftup_ipo_stellarblade_nikke","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-27","evidence_available":"Shift Up IPO expected top range, 435B won raise, 3.5T won valuation, Nikke 255B won sales, Stellar Blade PS rankings","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_game_IP","promote_to":"Stage2-Actionable"}
{"trigger_id":"r8l15_hybe_newjeans_T0","case_id":"r8_loop15_hybe_newjeans_sm_tencent_kpop_governance","trigger_type":"4C-watch","trigger_date":"2024-04-24","evidence_available":"HYBE audits ADOR over independence/control allegations; shares fell nearly 8%","event_return_pct":-8,"trigger_outcome_label":"artist_governance_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r8l15_skt_breach_T0","case_id":"r8_loop15_skt_data_breach_security_4c","trigger_type":"hard_4C","trigger_date":"2025-04-28","evidence_available":"SK Telecom malware data leak; free USIM replacement for 23M users; shares closed -6.7% vs KOSPI +0.1%","event_return_pct":-6.7,"market_relative_return_pp":-6.8,"trigger_outcome_label":"hard_4c_success","promote_to":"4C"}
{"trigger_id":"r8l15_skt_breach_T1","case_id":"r8_loop15_skt_data_breach_security_4c","trigger_type":"hard_4C_validation","trigger_date":"2025-07-04","evidence_available":"Regulator found SKT negligent; 26.96M data pieces leaked; shares -5.6%; 700B won security investment; 800B won revenue forecast cut","event_return_pct":-5.6,"trigger_outcome_label":"hard_4c_validated","promote_to":"4C"}
```

## data/sector_taxonomy/score_weight_profiles_round231_r8_loop15_v1.csv 초안

```csv
archetype,paid_ai_usage_conversion,ai_cloud_margin_visibility,enterprise_order_backlog,content_ip_monetization,game_sellthrough_retention,global_ip_licensing,platform_user_data_security,artist_contract_governance,ma_integration_revenue,ai_infra_capex_roi,ai_partnership_headline_only_penalty,ipo_pop_without_parent_monetization_penalty,cloud_ai_mix_without_price_confirmation_penalty,cb_capital_without_backlog_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
AI_MESSAGING_PARTNERSHIP_STAGE2_WITH_MONETIZATION_GATE,+5,+4,+2,+1,+0,+0,+4,+2,+1,+3,-5,-2,-2,-2,AI partnership+dominant MAU,paid usage/ad uplift missing,paid usage+margin,Kakao OpenAI is Stage2 not Green.
AI_INFRA_PORTAL_STAGE2_ACTIONABLE,+5,+5,+4,+3,+0,+0,+4,+1,+2,+5,-4,-3,-2,-2,AI infra purchase+portal base,capex ROI missing,AI revenue+margin+retention,Naver Blackwell trigger Stage2.
WEBTOON_IPO_CONTENT_PLATFORM_STAGE2,+1,+1,+1,+5,+0,+5,+2,+2,+2,+0,-2,-4,-1,-1,MAU+IPO+profitability,post-listing durability missing,parent monetization+IP revenue,Naver/Webtoon Stage2.
CLOUD_AI_IT_SERVICES_EVIDENCE_GOOD_PRICE_FAILED,+2,+5,+5,+0,+0,+0,+4,+1,+3,+4,-3,-2,-4,-2,cloud/AI sales mix,weak price/enterprise backlog missing,backlog+margin expansion,LG CNS evidence good price failed.
AI_SOFTWARE_CB_STRATEGIC_CAPITAL_STAGE2_WITH_4B,+3,+5,+5,+0,+0,+0,+4,+1,+4,+4,-3,-2,-2,-4,strategic capital+AI/M&A,CB/backlog missing,order backlog+margin+M&A execution,Samsung SDS Stage2+4B.
GAME_IP_GLOBALIZATION_STAGE2_ACTIONABLE,+0,+0,+0,+4,+5,+4,+2,+2,+4,+0,-2,-2,-1,-1,game IP sales/ranking,retention/new title missing,recurring revenue+retention,Krafton/Shift Up game IP Stage2.
KPOP_ARTIST_GOVERNANCE_4C_WATCH,+0,+0,+0,+5,+0,+5,+1,+5,+1,+0,-2,-2,-1,-1,artist IP governance dispute,contract resolution pending,artist schedule+revenue stability,HYBE/NewJeans 4C-watch.
CYBERSECURITY_DATA_BREACH_HARD_4C,+0,+2,+2,+0,+0,+0,+5,+2,+0,+1,-1,-1,-1,-1,data breach/customer trust,trust recovery pending,security proven+churn controlled,SKT breach hard 4C.
CONTENT_MA_IP_EXPANSION_STAGE2,+0,+0,+1,+5,+3,+5,+2,+2,+5,+0,-2,-2,-1,-2,IP acquisition/library,synergy revenue missing,new IP revenue+licensing,Krafton ADK Stage2.
```

---

# 이번 R8 Loop 15 결론

```text
1. Kakao/OpenAI는 Stage2-Actionable이지만 Green은 아니다.
   KakaoTalk 97% 점유율과 OpenAI partnership은 강하지만, +9% initial move가 -2% close로 식었다. paid usage와 ad uplift가 필요하다.

2. Naver/Webtoon/Nvidia AI infra는 Stage2-Actionable이다.
   Webtoon IPO +14.3%, 170M MAU, Naver 60k Blackwell chip purchase는 강하지만 parent-level monetization이 필요하다.

3. LG CNS는 evidence_good_but_price_failed다.
   cloud/AI sales mix 54%에도 IPO debut가 issue price 아래였다.

4. Samsung SDS/KKR CB는 Stage2-Actionable + 4B overlay다.
   +20.8% trigger는 강하지만 CB dilution과 AI order backlog gate가 남아 있다.

5. Krafton은 IP/geography expansion Stage2-Actionable이다.
   ADK $516M과 India fund $666M은 좋지만 integration과 regulatory/data risk가 남는다.

6. Shift Up은 game IP Stage2-Actionable이다.
   Nikke sales, Stellar Blade ranking, IPO valuation은 강하지만 post-IPO recurring revenue와 IP concentration 확인이 필요하다.

7. HYBE/NewJeans는 artist governance 4C-watch다.
   콘텐츠 IP는 곡/앨범보다 계약·소속·활동권이 먼저 깨질 수 있다.

8. SK Telecom data breach는 R8 hard 4C다.
   데이터 유출은 보안비용이 아니라 revenue forecast cut, 고객보상, trust loss로 바로 이어졌다.
```

한 문장으로 압축하면:

> **R8 Loop 15에서 배운 핵심은 “AI/콘텐츠/IP headline”이 아니라, paid AI usage·cloud margin·enterprise backlog·IP monetization·game retention·artist governance·data security가 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 AI partnership, IPO pop, CB 투자, celebrity/IP name, 보안투자 headline만으로는 4B/false positive가 되기 쉽다.**

[1]: https://www.reuters.com/technology/artificial-intelligence/openai-kakao-jointly-develop-ai-products-south-korea-2025-02-04/?utm_source=chatgpt.com "OpenAI clinches deal with Kakao, talks with SoftBank and Samsung about Stargate"
[2]: https://www.reuters.com/markets/deals/online-comics-platform-webtoon-reveals-revenue-growth-profitability-us-ipo-2024-05-31/?utm_source=chatgpt.com "Online comics platform Webtoon reveals revenue growth, profitability in US IPO filing"
[3]: https://www.reuters.com/business/media-telecom/nvidia-supply-more-than-260000-blackwell-ai-chips-south-korea-2025-10-31/?utm_source=chatgpt.com "Nvidia to supply more than 260,000 Blackwell AI chips to South Korea"
[4]: https://www.reuters.com/technology/skorean-tech-services-firm-lg-cns-falls-stock-market-debut-2025-02-05/?utm_source=chatgpt.com "South Korean tech services firm LG CNS drops in market debut"
[5]: https://www.reuters.com/world/asia-pacific/kkr-buy-820-million-samsung-sds-convertible-bonds-shares-jump-20-2026-04-15/?utm_source=chatgpt.com "KKR to buy $820 million of Samsung SDS convertible bonds, shares jump 20%"
[6]: https://www.reuters.com/en/south-korean-game-company-krafton-acquire-japans-adk-516-mln-2025-06-24/?utm_source=chatgpt.com "South Korean game company Krafton to acquire Japan's ADK for $516 mln"
[7]: https://www.reuters.com/world/asia-pacific/pubg-maker-krafton-leads-south-korean-trio-666-million-india-tech-bet-2025-12-19/?utm_source=chatgpt.com "PUBG maker Krafton leads South Korean trio in $666 million India tech bet"
[8]: https://www.reuters.com/markets/deals/tencent-backed-shift-up-may-price-ipo-top-end-band-source-says-2024-06-27/?utm_source=chatgpt.com "Tencent-backed Shift Up may price IPO at top end of band, source says"
[9]: https://www.reuters.com/lifestyle/record-giant-hybe-audits-newjeans-label-infighting-returns-k-pop-2024-04-24/?utm_source=chatgpt.com "Record giant HYBE audits 'NewJeans' label as infighting returns to K-pop"
[10]: https://www.reuters.com/business/media-telecom/tencent-become-second-largest-shareholder-k-pop-agency-sm-entertainment-2025-05-27/?utm_source=chatgpt.com "Tencent to become second-largest shareholder in K-Pop agency SM Entertainment"
[11]: https://www.reuters.com/sustainability/boards-policy-regulation/sk-telecom-shares-plunge-after-data-breach-due-cyberattack-2025-04-28/?utm_source=chatgpt.com "SK Telecom shares plunge after data breach due to cyberattack"
