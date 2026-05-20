순서상 이번은 **R8 Loop 16 — 플랫폼·콘텐츠·SW·보안 trigger-level price validation 라운드**다.

이번 R8은 “AI 플랫폼”, “웹툰”, “게임”, “K-pop”, “보안”을 하나로 섞으면 안 된다. 실제 가격은 전부 다른 문으로 반응했다. **AI 인프라 투자 → 클라우드/SI 매출**, **콘텐츠 IP → MAU/ARPU/광고·라이선스**, **게임 흥행 → 실제 sales/royalty/repeat title**, **플랫폼 거버넌스 → 규제 리스크**, **보안사고 → 고객신뢰·보상·매출가이던스**를 따로 분해해야 한다.

```text
round = R8 Loop 16
round_id = round_244
large_sector = PLATFORM_CONTENT_SW_SECURITY
method = trigger_level_backtest_v1_after_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R9 Loop 16
```

이번에도 KRX/Naver/Yahoo/Stooq의 수정주가 일봉 OHLC 30D/90D/180D/1Y/2Y window는 안정적으로 직접 확보하지 못했다. 그래서 full MFE/MAE는 만들지 않고 `price_data_unavailable_after_deep_search`로 분리한다. 대신 Reuters/FT/Barron’s/MarketWatch/Investopedia가 보도한 **event return, IPO price, issue price, close price, MAU, revenue, breach cost, fine, deal value**를 trigger anchor로 사용한다. Stage 판정과 가격검증 완료 여부는 분리한다.

---

# 1. 이번 라운드 대섹터

```text
R8 = 플랫폼·콘텐츠·SW·보안
```

R8의 core gate는 아래다.

```text
AI / cloud / SI:
AI data center investment → GPU/compute allocation → cloud/SI contract → recurring revenue → margin → capex/energy risk

Internet platform:
MAU/DAU → search/ad/e-commerce take-rate → AI compute cost → monetization → regulation/governance

Webtoon / content platform:
MAU → paid conversion → ad revenue → IP licensing → Disney/Netflix/studio partnerships → profit → creator payout risk

Gaming:
game hit / IP sales → platform expansion → retention → live-service monetization → sequel pipeline → one-title concentration

K-pop / entertainment:
artist IP → comeback/tour/album → platform revenue → label dispute → governance/regulatory risk → founder/key-person risk

Cybersecurity:
data breach → affected users → remediation cost → regulatory fine → compensation → churn → revenue guidance cut

M&A / JV:
deal announcement → approval → integration → GMV/ARPU/revenue/margin → governance/security overlay
```

---

# 2. 대상 canonical archetype

```text
AI_DATA_CENTER_CLOUD_SI_STAGE2_ACTIONABLE
AI_CLOUD_IPO_PRICE_MUTED
WEBTOON_IP_MONETIZATION_STAGE2_ACTIONABLE
GAME_IP_GLOBAL_EXPANSION_STAGE2
GAME_IP_IPO_STAGE2_WITH_CONCENTRATION_4B
CONTENT_LABEL_GOVERNANCE_4C_WATCH
PLATFORM_FOUNDER_REGULATORY_4C_RELIEF
CYBERSECURITY_DATA_BREACH_HARD_4C
```

---

# 3. deep sub-archetype

```text
Kakao / LG CNS / SK-AWS AI data center:
- SK Group + AWS 7T won / $5.11B Ulsan AI data center
- AWS contribution around $4B
- 100MW fully operational by 2029
- potential 1GW future expansion
- Kakao +11%, LG CNS +9%, SK Hynix +3%, KOSPI above 3,000
- Stage2-Actionable AI infrastructure trigger
- Green requires cloud/SI contract revenue and margin

LG CNS IPO:
- IPO raised 1.2T won / $827M
- issue price 61,900 won
- debut trading around 59,700 won, below issue price
- cloud and AI services were over half of first-three-quarter 2024 sales
- evidence good but price failed/muted

Webtoon / Naver:
- Webtoon IPO priced at $21, valuation $2.7B, raised $315M
- Naver retained about 63.4%
- 170M MAU, 150+ countries
- Nasdaq debut closed $23.00, +9.5% vs IPO price
- later Disney + earnings trigger: shares +62% to $15.16 after prior 55% post-IPO decline
- Stage2 platform/IP monetization; Green requires profitable growth and retention

Krafton / Naver / Mirae India tech fund:
- $666M Unicorn Growth Fund
- initial $333M, launch Jan 2026
- Krafton already invested over $200M in India
- BGMI 240M+ downloads
- Stage2 geographic/platform expansion
- price anchor unavailable

Shift Up:
- IPO expected to raise 435B won / $313M at top band
- market cap around 3.5T won / $2.52B
- Nikke booked 255B won sales from global launch to Q1 2024
- Stellar Blade ranked No.1 Japan PS download and No.2 North America
- 2023 OP 111B won on 169B won revenue
- Stage2 game-IP monetization, but title concentration 4B

HYBE:
- ADOR/NewJeans audit dispute caused HYBE shares to fall nearly 8%
- police sought detention warrant for Bang Si-hyuk in Apr 2026
- HYBE shares -2.4% despite market up
- content IP governance 4C-watch

Kakao:
- founder Kim Beom-su arrested over SM stock-manipulation suspicion
- Kakao shares -3.4%
- later court acquitted Kim in Oct 2025
- platform founder/regulatory 4C with relief trigger

SK Telecom security:
- cyberattack/data breach disclosed Apr 2025
- shares fell as much as -8.5%, closed -6.7%, KOSPI +0.1%
- all 23M users offered free USIM replacement
- later 26.96M pieces of user data confirmed leaked
- shares -5.6% on July probe result
- 134B won fine, 700B won five-year security investment, 800B won revenue forecast cut
- possible compensation cost near 2.3T won
```

---

# 4. 선정 case 요약

| bucket                         | case                                     | 핵심 판정                                                                     |
| ------------------------------ | ---------------------------------------- | ------------------------------------------------------------------------- |
| Stage2-Actionable              | Kakao / LG CNS / SK-AWS AI data center   | Kakao +11%, LG CNS +9%, SK Hynix +3%. AI 인프라 policy-to-price trigger      |
| evidence_good_but_price_failed | LG CNS IPO                               | AI/cloud 매출 비중은 좋지만 IPO debut이 공모가 하회                                     |
| Stage2-Actionable / Yellow 후보  | Webtoon / Naver IP monetization          | IPO +9.5%, later Disney/earnings +62%. MAU·IP monetization trigger        |
| Stage2 platform expansion      | Krafton/Naver/Mirae India fund           | $666M India tech fund, BGMI 240M+ downloads. 가격 anchor 없음                 |
| Stage2 game IP + 4B            | Shift Up                                 | Nikke sales, Stellar Blade ranking, IPO valuation. Title concentration 4B |
| 4C-watch                       | HYBE governance / ADOR / Bang legal risk | ADOR dispute -8%, Bang warrant -2.4%. IP governance risk                  |
| 4C + relief                    | Kakao founder regulatory case            | arrest -3.4%, later acquittal. 플랫폼 founder/regulatory overhang            |
| hard 4C                        | SK Telecom cybersecurity breach          | -8.5% intraday, -6.7% close, 134B won fine, revenue guidance cut          |

---

# 5. Case별 trigger grid

## Case A — Kakao / LG CNS / SK-AWS Ulsan AI data center

```text
symbols = 035720 / 064400 / SK_group_readthrough
case_type = Stage2-Actionable
archetype = AI_DATA_CENTER_CLOUD_SI_STAGE2_ACTIONABLE
```

| trigger |              type | date       | 당시 공개 evidence                                                                           | 가격 anchor                            | outcome          |
| ------- | ----------------: | ---------- | ---------------------------------------------------------------------------------------- | ------------------------------------ | ---------------- |
| T0      |         awareness | 2025-06    | South Korea AI policy optimism / AI data center buildout                                 | no direct price                      | Stage1           |
| T1      | Stage2-Actionable | 2025-06-20 | SK Group + AWS 7T won / $5.11B Ulsan AI data center, AWS $4B contribution                | Kakao +11%, LG CNS +9%, SK Hynix +3% | excellent event  |
| T2      |        validation | 2025-06-20 | 100MW full operation by 2029, possible 1GW expansion, KOSPI above 3,000                  | same                                 | infra validation |
| T3      |          4B-watch | 2025~2029  | power/cooling/capex, customer contracts, LG CNS SI margin, Kakao AI monetization missing | no OHLC                              | 4B               |
| T4      |     Stage3-Yellow | N/A        | cloud/SI backlog and recurring revenue not confirmed                                     | no Yellow                            | 보류               |

이 case는 R8의 가장 좋은 AI infrastructure Stage2-Actionable이다. SK Group과 AWS가 Ulsan에 한국 최대 AI data center를 만들기 위해 약 7T won, $5.11B를 투자하고, 이 중 AWS가 약 $4B를 부담한다는 정부 발표가 나왔다. 착공은 2025년 9월, 2029년 100MW full operation이 목표였고, Chey Tae-won은 1GW 확장 구상도 언급했다. 이 발표와 AI policy optimism 속에서 Kakao는 +11%, LG CNS는 +9%, SK Hynix는 +3% 올랐고, KOSPI는 3,000선을 넘었다. 다만 이건 아직 클라우드/SI 매출·AI 서비스 ARPU가 아니라 infrastructure event다. ([Reuters][1])

```json
{
  "case_id": "r8_loop16_kakao_lgcns_sk_aws_ai_datacenter",
  "symbols": "035720/064400/SK_group_readthrough",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable_AI_infra",
  "trigger_date": "2025-06-20",
  "investment_krw_trn": 7.0,
  "investment_usd_bn": 5.11,
  "aws_contribution_usd_bn": 4.0,
  "initial_capacity_mw": 100,
  "full_operation_year": 2029,
  "future_capacity_target_gw": 1.0,
  "kakao_event_return_pct": 11,
  "lg_cns_event_return_pct": 9,
  "sk_hynix_event_return_pct": 3,
  "stage3_gate_missing": [
    "cloud_contract_backlog",
    "LG_CNS_SI_margin",
    "Kakao_AI_service_monetization",
    "data_center_utilization",
    "power_and_cooling_cost",
    "recurring_revenue"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable_AI_infrastructure"
}
```

---

## Case B — LG CNS IPO / AI-cloud services but weak debut

```text
symbol = 064400
case_type = evidence_good_but_price_failed
archetype = AI_CLOUD_IPO_PRICE_MUTED
```

| trigger |             type | date       | 당시 공개 evidence                                                                                               | 가격 anchor              | outcome                        |
| ------- | ---------------: | ---------- | ------------------------------------------------------------------------------------------------------------ | ---------------------- | ------------------------------ |
| T0      |  Stage2 evidence | 2025-02-05 | LG CNS IPO raised 1.2T won / $827M; cloud and AI services over half of sales in first three quarters of 2024 | issue price 61,900 won | Stage2                         |
| T1      | price validation | 2025-02-05 | debut opened 60,500 won, later 59,700 won                                                                    | below IPO price        | evidence good but price failed |
| T2      |         4B-watch | 2025       | IPO overhang, valuation, AI/cloud growth-to-margin uncertainty                                               | no full OHLC           | 4B                             |
| T3      |    Stage3-Yellow | N/A        | external AI/cloud contract growth and margin not confirmed                                                   | no Yellow              | 보류                             |

LG CNS는 “AI/cloud business가 있어도 IPO 가격이 검증을 거부할 수 있다”는 case다. LG CNS는 1.2T won, $827.1M 규모 IPO를 진행했고, IT·cloud·AI services provider로 first-three-quarter 2024 sales의 절반 이상을 cloud and AI services가 차지했다. 그러나 공모가는 61,900 won이었고, 상장 첫날 주가는 60,500 won으로 시작해 59,700 won까지 내려 공모가를 하회했다. 즉 AI/cloud evidence는 있지만 price validation은 실패했다. ([Reuters][2])

```json
{
  "case_id": "r8_loop16_lg_cns_ipo_ai_cloud_price_muted",
  "symbol": "064400",
  "best_trigger": "T0/T1",
  "best_trigger_type": "Stage2_AI_cloud_but_price_failed",
  "trigger_date": "2025-02-05",
  "ipo_raise_krw_trn": 1.2,
  "ipo_raise_usd_mn": 827.1,
  "issue_price_krw": 61900,
  "debut_open_krw": 60500,
  "debut_later_price_krw": 59700,
  "ai_cloud_sales_share_context": ">50%_of_first_three_quarters_2024_sales",
  "stage3_gate_missing": [
    "external_AI_cloud_contract_growth",
    "cloud_margin",
    "M&A_execution",
    "recurring_revenue",
    "post_IPO_multiple_absorption"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "evidence_good_but_price_failed"
}
```

---

## Case C — Webtoon Entertainment / Naver IP monetization

```text
symbols = WBTN / 035420_readthrough
case_type = Stage2-Actionable / IP monetization
archetype = WEBTOON_IP_MONETIZATION_STAGE2_ACTIONABLE
```

| trigger |                                 type | date          | 당시 공개 evidence                                                                     | 가격 anchor          | outcome        |
| ------- | -----------------------------------: | ------------- | ---------------------------------------------------------------------------------- | ------------------ | -------------- |
| T0      |                      Stage2 evidence | 2024-05-31    | Webtoon IPO filing: 170M MAU, 150+ countries, Q1 net income $6.2M, revenue $326.7M | no IPO price yet   | Stage2         |
| T1      |                    Stage2-Actionable | 2024-06-27/28 | IPO priced $21, valuation $2.7B, raised $315M; debut close $23.00                  | debut +9.5% vs $21 | Actionable     |
| T2      | Stage2 validation / Yellow candidate | 2025-08-13    | Disney deal + surprise profit; shares +62% to $15.16 after prior 55% post-IPO fall | +62%               | strong trigger |
| T3      |                             4B-watch | 2024~2025     | post-IPO drawdown, monetization, creator payout, slowing growth concerns           | prior -55%         | 4B             |
| T4      |                         Stage3-Green | N/A           | sustained profitable growth and parent Naver value conversion not confirmed        | no Green           | 보류             |

Webtoon은 R8 content-platform에서 가장 좋은 Stage2-Actionable 후보 중 하나다. IPO filing 당시 Webtoon은 150개국 이상에서 170M monthly active users를 보유했고, 2024년 Q1 revenue는 $326.7M, net income은 $6.2M이었다. IPO는 $21에 priced, valuation $2.7B, proceeds $315M였고, debut close는 $23.00으로 IPO price 대비 +9.5%였다. 이후 2025년 Disney deal과 surprise profit 발표에서는 shares가 $15.16까지 +62% 뛰었지만, 그 직전까지 IPO 후 shares가 55% 하락했다는 점이 4B를 만든다. 즉 Webtoon은 IP monetization Stage2-Actionable이지만, Green은 sustained profitable growth와 IP licensing economics가 필요하다. ([Reuters][3])

```json
{
  "case_id": "r8_loop16_webtoon_naver_ip_monetization",
  "symbols": "WBTN/035420_readthrough",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable_IP_platform",
  "ipo_filing_date": "2024-05-31",
  "ipo_pricing_date": "2024-06-27",
  "ipo_price_usd": 21,
  "ipo_valuation_usd_bn": 2.7,
  "ipo_raise_usd_mn": 315,
  "debut_close_usd": 23.00,
  "debut_return_pct": 9.5,
  "monthly_active_users_mn": 170,
  "countries": ">150",
  "q1_2024_revenue_usd_mn": 326.7,
  "q1_2024_net_income_usd_mn": 6.2,
  "disney_earnings_event_return_pct": 62,
  "disney_event_price_usd": 15.16,
  "pre_disney_post_ipo_decline_pct": -55,
  "stage3_gate_missing": [
    "paid_conversion",
    "ad_ARPU",
    "IP_license_revenue",
    "creator_payout_ratio",
    "sustained_profitability",
    "Naver_parent_value_capture"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_Actionable_content_platform_with_4B_volatility"
}
```

---

## Case D — Krafton / Naver / Mirae India tech and gaming expansion

```text
symbols = 259960 / 035420 / 006800
case_type = Stage2 platform and game geography expansion
archetype = GAME_IP_GLOBAL_EXPANSION_STAGE2
```

| trigger |            type | date       | 당시 공개 evidence                                                                             | 가격 anchor       | outcome    |
| ------- | --------------: | ---------- | ------------------------------------------------------------------------------------------ | --------------- | ---------- |
| T0      |       awareness | 2025       | Krafton India gaming expansion, BGMI scale                                                 | no price        | Stage1     |
| T1      | Stage2 evidence | 2025-12-19 | Krafton, Naver, Mirae Asset launch $666M India tech fund                                   | no direct price | Stage2     |
| T2      |      validation | 2025-12-19 | initial $333M, launch Jan 2026; Krafton has invested $200M+ in India; BGMI 240M+ downloads | no price        | validation |
| T3      |        4B-watch | 2026       | India gaming regulation, monetization, price-sensitive user base, startup fund ROI         | no OHLC         | 4B         |
| T4      |   Stage3-Yellow | N/A        | fund returns, BGMI revenue, India platform monetization not confirmed                      | no Yellow       | 보류         |

Krafton/Naver/Mirae India fund는 R8에서 “콘텐츠 IP + 플랫폼 geographic expansion” Stage2다. 세 회사는 India-focused Unicorn Growth Fund를 만들고, 총 규모는 $666M, initial capital은 $333M이며 2026년 1월 launch 예정이다. Krafton은 이미 India에 $200M 이상을 투자했고, BGMI는 240M+ downloads를 보유하고 있다. 다만 India gaming regulation, monetization, fund IRR, startup investment return이 닫히지 않아 Stage2에 머문다. ([Reuters][4])

```json
{
  "case_id": "r8_loop16_krafton_naver_mirae_india_fund",
  "symbols": "259960/035420/006800",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2_platform_game_geographic_expansion",
  "trigger_date": "2025-12-19",
  "fund_total_usd_mn": 666,
  "initial_capital_usd_mn": 333,
  "fund_launch": "2026-01",
  "krafton_existing_india_investment_usd_mn": ">200",
  "bgmi_downloads_mn": ">240",
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "India_game_revenue",
    "BGMI_ARPU",
    "startup_fund_IRR",
    "regulatory_stability",
    "portfolio_exit_path",
    "Naver_platform_synergy"
  ],
  "trigger_outcome_label": "Stage2_geographic_expansion_not_Green"
}
```

---

## Case E — Shift Up / Nikke + Stellar Blade game IP monetization

```text
symbol = ShiftUp_KOSPI
case_type = Stage2 game-IP monetization with concentration 4B
archetype = GAME_IP_IPO_STAGE2_WITH_CONCENTRATION_4B
```

| trigger |                 type | date       | 당시 공개 evidence                                                                                                | 가격 anchor                             | outcome       |
| ------- | -------------------: | ---------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------- | ------------- |
| T0      |      Stage2 evidence | 2024-06-27 | Shift Up IPO expected at top band, raising 435B won / $313M, market cap 3.5T won                              | direct post-listing price unavailable | Stage2        |
| T1      |           validation | 2024-06-27 | Nikke booked 255B won sales from launch to Q1 2024; Stellar Blade No.1 Japan PS downloads, No.2 North America | no price                              | IP validation |
| T2      | financial validation | 2024       | 2023 OP 111B won on 169B won revenue, vs 18B OP in 2022                                                       | no price                              | validation    |
| T3      |             4B-watch | 2024~      | title concentration, console hit sustainability, Tencent stake, sequel pipeline                               | no OHLC                               | 4B            |
| T4      |        Stage3-Yellow | N/A        | repeat title sales, live-service retention, post-IPO price path unavailable                                   | no Yellow                             | 보류            |

Shift Up은 R8 gaming에서 좋은 Stage2지만, 아직 Green은 아니다. IPO pricing이 top band로 진행될 경우 435B won, $313M을 조달하고 market cap은 3.5T won, $2.52B로 예상됐다. Nikke는 global launch부터 2024년 Q1까지 255B won sales를 기록했고, Stellar Blade는 Japan PlayStation download ranking 1위, North America 2위였으며, 2023년 operating profit은 111B won으로 2022년 18B won보다 크게 늘었다. 다만 title concentration, post-IPO price path, sequel/live-service retention이 남아 있어 Stage2 + 4B다. ([Reuters][5])

```json
{
  "case_id": "r8_loop16_shiftup_game_ip_ipo",
  "symbol": "ShiftUp_KOSPI",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_game_IP_with_4B_concentration",
  "trigger_date": "2024-06-27",
  "ipo_raise_krw_bn": 435,
  "ipo_raise_usd_mn": 313,
  "expected_market_cap_krw_trn": 3.5,
  "expected_market_cap_usd_bn": 2.52,
  "nikke_sales_launch_to_q1_2024_krw_bn": 255,
  "stellar_blade_japan_ps_download_rank": 1,
  "stellar_blade_north_america_ps_download_rank": 2,
  "op_2023_krw_bn": 111,
  "revenue_2023_krw_bn": 169,
  "op_2022_krw_bn": 18,
  "direct_post_listing_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "post_IPO_price_path",
    "Stellar_Blade_repeat_sales",
    "Nikke_live_service_retention",
    "Project_pipeline",
    "title_concentration_risk",
    "Tencent_stake_overhang"
  ],
  "trigger_outcome_label": "Stage2_game_IP_not_Green"
}
```

---

## Case F — HYBE / ADOR-NewJeans dispute and Bang Si-hyuk legal risk

```text
symbol = 352820
case_type = content IP governance 4C-watch
archetype = CONTENT_LABEL_GOVERNANCE_4C_WATCH
```

| trigger |       type | date       | 당시 공개 evidence                                                                                   | 가격 anchor                        | outcome               |
| ------- | ---------: | ---------- | ------------------------------------------------------------------------------------------------ | -------------------------------- | --------------------- |
| T0      |   4C-watch | 2024-04-24 | HYBE audits ADOR / Min Hee-jin dispute, NewJeans label control issue                             | HYBE shares down nearly 8%       | label governance 4C   |
| T1      | validation | 2024~      | artist IP / label dispute creates share volatility                                               | same                             | validation            |
| T2      |   4C-watch | 2026-04-21 | police seek detention warrant for founder Bang Si-hyuk over alleged capital-market law violation | HYBE -2.4% despite market uptick | founder governance 4C |
| T3      |     relief | N/A        | legal resolution, artist activity normalization, BTS/IP monetization stability not confirmed     | no relief                        | 보류                    |

HYBE는 R8 content에서 **artist IP보다 governance가 먼저 가격을 때린** case다. ADOR/NewJeans dispute 당시 HYBE는 ADOR CEO Min Hee-jin에 대한 audit을 시작했고, NewJeans를 둘러싼 label-control dispute가 주가를 거의 -8% 밀었다. 2026년에는 police가 Bang Si-hyuk detention warrant를 요청했고, HYBE shares는 market이 오른 와중에도 -2.4% 하락했다. 이건 content IP의 가치가 사라졌다는 뜻이 아니라, label governance와 founder legal overhang이 Stage3를 막는 4C-watch라는 뜻이다. ([Reuters][6])

```json
{
  "case_id": "r8_loop16_hybe_content_label_governance",
  "symbol": "352820",
  "best_trigger": "T0/T2",
  "best_trigger_type": "4C_watch_content_governance",
  "ador_dispute_date": "2024-04-24",
  "ador_dispute_event_return_pct": "nearly_-8",
  "bang_warrant_date": "2026-04-21",
  "bang_warrant_event_return_pct": -2.4,
  "legal_issues": [
    "ADOR_label_control_dispute",
    "NewJeans_IP_disruption",
    "founder_capital_market_law_investigation"
  ],
  "stage3_gate_missing": [
    "artist_activity_normalization",
    "legal_resolution",
    "label_governance_stability",
    "tour_album_revenue_conversion",
    "founder_risk_resolution"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "content_IP_governance_4C_watch"
}
```

---

## Case G — Kakao founder regulatory case / SM Entertainment stock-manipulation charge

```text
symbol = 035720
case_type = platform founder regulatory 4C with relief trigger
archetype = PLATFORM_FOUNDER_REGULATORY_4C_RELIEF
```

| trigger |          type | date          | 당시 공개 evidence                                                                        | 가격 anchor                 | outcome               |
| ------- | ------------: | ------------- | ------------------------------------------------------------------------------------- | ------------------------- | --------------------- |
| T0      |      4C-watch | 2024-07-22/23 | Kakao founder Kim Beom-su arrested over suspected SM Entertainment stock manipulation | Kakao shares -3.4%        | founder/regulatory 4C |
| T1      |    validation | 2024          | possible impact on Kakao AI/global expansion and KakaoBank ownership rules            | same                      | governance validation |
| T2      |        relief | 2025-10-21    | court clears Kim of stock manipulation charges                                        | no direct price in source | relief                |
| T3      | Stage3-Yellow | N/A           | platform monetization and regulatory cleanup not confirmed                            | no Yellow                 | 보류                    |

Kakao는 R8 platform governance case다. Founder Kim Beom-su가 SM Entertainment takeover 과정에서 stock manipulation 혐의로 arrest되자 Kakao shares는 -3.4% 하락했다. 보도는 이 사건이 Kakao의 AI investment/global expansion뿐 아니라 KakaoBank control에도 영향을 줄 수 있다고 설명했다. 이후 2025년 10월 court가 Kim을 무죄로 판단했다는 relief trigger가 나왔지만, 직접 price anchor는 확보하지 못했다. 따라서 이 case는 `founder regulatory 4C → legal relief`로 기록한다. ([Reuters][7])

```json
{
  "case_id": "r8_loop16_kakao_founder_regulatory_relief",
  "symbol": "035720",
  "best_trigger": "T0/T2",
  "best_trigger_type": "4C_watch_with_relief",
  "arrest_date": "2024-07-22/2024-07-23",
  "arrest_event_return_pct": -3.4,
  "charge_context": "SM_Entertainment_stock_manipulation_suspicion",
  "relief_date": "2025-10-21",
  "relief_event": "court_clears_Kim_Beom_su_of_stock_manipulation_charges",
  "direct_relief_price_anchor": "price_data_unavailable_after_deep_search",
  "risk_channels": [
    "AI_investment_delay",
    "global_expansion_delay",
    "KakaoBank_control_rule",
    "platform_governance_overhang"
  ],
  "trigger_outcome_label": "platform_founder_regulatory_4C_with_relief"
}
```

---

## Case H — SK Telecom cybersecurity breach

```text
symbol = 017670
case_type = hard 4C cybersecurity
archetype = CYBERSECURITY_DATA_BREACH_HARD_4C
```

| trigger |               type | date       | 당시 공개 evidence                                                                                                            | 가격 anchor                                         | outcome           |
| ------- | -----------------: | ---------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ----------------- |
| T0      |            hard 4C | 2025-04-28 | malware-driven customer data breach, all 23M users offered free USIM replacement                                          | shares as much as -8.5%, close -6.7%, KOSPI +0.1% | hard 4C           |
| T1      |      4C validation | 2025-07-04 | 26.96M user-data pieces leaked, negligence finding, 700B won five-year security investment, 800B won revenue forecast cut | shares -5.6%                                      | validated         |
| T2      | penalty validation | 2025-08-28 | PIPC fine about 134B won / $96.5M; weak internal security controls                                                        | no direct same price in snippet                   | hard validation   |
| T3      |  compensation risk | 2025-12-21 | consumer agency order for 100,000 won compensation per applicant; possible all-victim cost near 2.3T won                  | no direct price                                   | compensation tail |
| T4      |             relief | N/A        | churn control, customer trust recovery, security remediation not confirmed                                                | no relief                                         | 보류                |

SK Telecom은 R8 security hard 4C의 교과서다. 2025년 4월 malware-driven data breach 공시 후 shares는 장중 -8.5%, 종가 -6.7%를 기록했고, 같은 날 KOSPI는 +0.1%였다. 회사는 23M subscribers 전원에게 free USIM replacement를 제공한다고 했다. 이후 정부 조사에서 26.96M pieces of user data leak가 확인됐고, SK Telecom은 700B won 규모 5년 security investment와 800B won revenue forecast cut을 발표했다. 8월에는 134B won fine이 부과됐고, 12월에는 피해자 전체 보상 시 비용이 nearly 2.3T won에 이를 수 있다는 consumer-agency context가 나왔다. 이건 단순 보안비용이 아니라 customer trust, regulatory penalty, revenue guidance가 동시에 깨지는 hard 4C다. ([Reuters][8])

```json
{
  "case_id": "r8_loop16_sk_telecom_cyber_breach",
  "symbol": "017670",
  "best_trigger": "T0/T3",
  "best_trigger_type": "hard_4C_cybersecurity",
  "breach_price_event_date": "2025-04-28",
  "intraday_event_return_pct": -8.5,
  "close_event_return_pct": -6.7,
  "kospi_same_context_pct": 0.1,
  "affected_subscribers_mn": 23,
  "user_data_pieces_leaked_mn": 26.96,
  "july_probe_event_return_pct": -5.6,
  "security_investment_5y_krw_bn": 700,
  "revenue_forecast_cut_krw_bn": 800,
  "fine_krw_bn": 134,
  "possible_all_victim_compensation_krw_trn": 2.3,
  "stage3_gate_missing": [
    "customer_churn_stabilization",
    "USIM_replacement_completion",
    "security_remediation",
    "compensation_final_amount",
    "revenue_guidance_recovery",
    "trust_rebuild"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "hard_4C_success_cybersecurity"
}
```

---

# 6. Trigger별 가격경로 검증 요약

| case                        | best trigger |                      entry anchor |                                   event MFE/MAE |                      market-relative | full MFE/MAE | outcome                        |
| --------------------------- | ------------ | --------------------------------: | ----------------------------------------------: | -----------------------------------: | ------------ | ------------------------------ |
| Kakao/LG CNS AI data center | T1/T2        |                             event |            Kakao +11%, LG CNS +9%, SK Hynix +3% |              KOSPI milestone context | unavailable  | Stage2-Actionable              |
| LG CNS IPO                  | T0/T1        |             issue 61,900 → 59,700 |                                 below IPO price |                                  N/A | unavailable  | evidence good but price failed |
| Webtoon/Naver               | T1/T2        | $21 IPO → $23 debut; later $15.16 |               +9.5% debut, +62% Disney/earnings |            S&P +0.4% on Disney event | unavailable  | Stage2-Actionable + 4B         |
| Krafton/Naver/Mirae India   | T1/T2        |                       unavailable |                                        no price |                                  N/A | unavailable  | Stage2 expansion               |
| Shift Up                    | T0/T2        |                       unavailable | no direct post-listing price in sourced trigger |                                  N/A | unavailable  | Stage2 game IP                 |
| HYBE                        | T0/T2        |                             event |                         nearly -8%, later -2.4% |        market up on Bang warrant day | unavailable  | 4C-watch                       |
| Kakao founder case          | T0/T2        |                             event |              -3.4%, later legal relief no price |                                  N/A | unavailable  | 4C + relief                    |
| SK Telecom breach           | T0/T3        |                             event |        -8.5% intraday, -6.7% close, later -5.6% | -6.8pp vs KOSPI +0.1% on first event | unavailable  | hard 4C                        |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
좋은 Stage2:
- Kakao/LG CNS AI data center
- Webtoon IPO / Disney IP monetization
- Krafton/Naver/Mirae India fund
- Shift Up game IP IPO

약한 Stage2:
- LG CNS IPO: AI/cloud evidence는 좋지만 price가 공모가를 하회.
- Krafton/Naver/Mirae India: fund와 BGMI scale은 좋지만 주가 anchor와 수익화가 없음.
- Shift Up: IP evidence는 좋지만 post-listing price path와 title concentration gate.
```

## Stage2-Actionable entry 성과

```text
Actionable:
- Kakao/LG CNS AI data center: Kakao +11%, LG CNS +9%.
- Webtoon: IPO +9.5%, Disney/earnings +62%.
- SK Telecom breach는 반대 방향의 Actionable 4C: -8.5% / -6.7%.

Actionable 보류:
- Krafton/Naver/Mirae India fund: price anchor 없음.
- Shift Up: direct event return 없음.
```

## Stage3-Yellow 후보

```text
Yellow 후보:
- Kakao/LG CNS: AI data center가 cloud/SI backlog and margin으로 연결되면.
- Webtoon/Naver: IP licensing, ad ARPU, paid conversion, profit이 반복되면.
- Krafton: India/BGMI revenue and fund-return visibility가 확인되면.
- Shift Up: Stellar Blade/Nikke repeat monetization and new-title pipeline이 확인되면.
```

## Stage3-Green

```text
이번 R8 Loop 16에서 확정 Green 없음.

이유:
- AI data center는 아직 infrastructure investment이지 recurring software revenue가 아니다.
- Webtoon은 좋은 trigger가 있지만 IPO 후 -55% drawdown도 있었다.
- game IP는 hit validation은 있으나 title concentration과 repeatability가 남아 있다.
- HYBE/Kakao/SK Telecom은 governance/security hard overlay가 강하다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- Kakao/LG CNS AI data center Stage2 rally
- LG CNS IPO evidence-good-price-failed
- Webtoon IPO and Disney/earnings rally
- HYBE governance drawdown
- Kakao founder regulatory drawdown
- SK Telecom cyber hard 4C

Stage2_promote_candidate:
- Kakao/LG CNS AI data center
- Webtoon/Naver IP monetization
- Krafton India expansion, if monetization confirms
- Shift Up, if repeat sales and pipeline confirm

Stage3-Yellow candidate:
- Webtoon if IP licensing and profitable growth sustain
- LG CNS/Kakao if AI infrastructure converts to cloud/SI recurring revenue
- Shift Up if Stellar Blade/Nikke revenue durability and next-title visibility improve

evidence_good_but_price_failed:
- LG CNS IPO
- Samsung-like AI/SW IPO theme without price validation
- Krafton/Naver fund due no price anchor

event_premium:
- Webtoon Disney deal
- Kakao/LG CNS AI data center policy rally
- Shift Up IPO/gaming-IP premium

thesis_break_watch:
- HYBE ADOR/NewJeans and Bang legal risk
- Kakao founder regulatory overhang
- SK Telecom cybersecurity breach

hard_4C_success:
- SK Telecom cybersecurity breach
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
AI_compute_to_cloud_revenue,+5,"AI data center가 실제 cloud/SI recurring revenue로 연결되어야 Yellow","Kakao/LG CNS"
SI_contract_backlog,+5,"LG CNS 같은 SI는 data center headline보다 backlog와 margin이 핵심","LG CNS"
IP_platform_MAU_monetization,+5,"Webtoon은 MAU보다 paid conversion/ad ARPU/IP licensing이 핵심","Webtoon/Naver"
content_IP_license_revenue,+5,"Disney/Webtoon 같은 IP deal은 revenue/profit 검증 시 승격","Webtoon"
game_IP_repeat_sales,+5,"게임주는 hit보다 repeat sales/live-service retention이 중요","Shift Up/Krafton"
India_platform_monetization,+4,"India expansion은 downloads보다 ARPU/regulation/ROI가 필요","Krafton"
label_governance_stability,+5,"엔터는 artist IP보다 label governance가 먼저 깨질 수 있음","HYBE"
founder_regulatory_clearance,+4,"플랫폼 창업자 legal overhang은 valuation discount 요인","Kakao"
cybersecurity_trust_cost,+5,"보안사고는 고객신뢰·보상·매출가이던스 hard gate","SK Telecom"
```

## 내릴 축

```csv
axis,delta,reason,cases
AI_infra_headline_without_revenue,-5,"AI data center headline만으로 Green 금지","Kakao/LG CNS"
IPO_valuation_without_post_listing_strength,-5,"AI/SW IPO가 공모가 하회하면 Actionable 금지","LG CNS"
MAU_without_ARPU_profit,-5,"플랫폼 MAU만으로 Green 금지","Webtoon"
game_hit_without_pipeline,-5,"한 게임 흥행만으로 Green 금지","Shift Up"
geographic_fund_without_ROI,-4,"India fund headline은 monetization/exit 전에는 Stage2","Krafton/Naver/Mirae"
artist_IP_without_governance,-5,"IP가 좋아도 label/legal dispute가 있으면 4B/4C","HYBE"
platform_founder_risk_ignored,-4,"founder/regulatory risk 무시 금지","Kakao"
security_incident_treated_as_one_off,-5,"data breach를 일회성 비용으로만 보면 false positive","SK Telecom"
```

---

# 10. Stage2-Actionable 승격 조건

R8 Loop 16 shadow rule:

```text
R8에서 Stage2 evidence가 아래 중 3개 이상이면 Stage2-Actionable로 승격한다.

1. event return이 +5% 이상이다.
2. market-relative return이 +5pp 이상이다.
3. AI/cloud/data center trigger가 실제 cloud/SI backlog or recurring revenue로 연결된다.
4. content platform은 MAU + revenue/profit + IP licensing 중 2개 이상이 확인된다.
5. game company는 hit sales + retention/live service + sequel/pipeline 중 2개 이상이 확인된다.
6. platform expansion은 geography/user scale뿐 아니라 ARPU/GMV/ROI가 확인된다.
7. governance, founder legal risk, cybersecurity breach 4B/4C overlay가 없다.
```

적용:

```text
Kakao/LG CNS:
조건 1은 강함. 3이 아직 부족 → Stage2-Actionable, Yellow 보류.

Webtoon:
조건 1,4 일부 충족 → Stage2-Actionable / Yellow candidate.

LG CNS IPO:
AI/cloud evidence는 있으나 price가 공모가 하회 → Actionable 금지.

SK Telecom:
반대 방향 hard 4C. security trust cost를 즉시 차감.

HYBE/Kakao:
IP/platform 사업이 있어도 governance/founder legal overhang 때문에 4C-watch.
```

---

# 11. Stage3-Yellow 조건

```text
Stage3-Yellow:
- Stage2-Actionable 이후 EPS/OP/FCF 경로 변화 가능성이 높아짐.
- 하지만 monetization, margin, retention, legal/security gate 중 하나가 남은 상태.
```

Yellow 후보:

```text
Webtoon:
Disney/IP licensing + surprise profit이 반복되면 Yellow.

Kakao/LG CNS:
AI data center가 cloud/SI backlog and margin으로 전환되면 Yellow.

Shift Up:
Stellar Blade/Nikke revenue durability and next-title pipeline이 확인되면 Yellow.

Krafton:
BGMI India monetization and fund portfolio ROI가 확인되면 Yellow.

Naver:
Webtoon value capture and AI compute monetization이 동시에 확인되면 Yellow.
```

---

# 12. Stage3-Green 조건

```text
Stage3-Green:
- AI infrastructure converts into recurring software/cloud/SI revenue.
- MAU converts into ARPU, ad revenue, paid conversion and profit.
- IP licensing converts into durable revenue and margin.
- game hits convert into repeat sales, live-service retention and sequel pipeline.
- governance/founder/legal disputes are resolved.
- cybersecurity remediation is completed and churn/revenue guidance recovers.
- full-window MFE/MAE is favorable.
```

이번 R8 Loop 16에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + revenue/margin/retention/security/governance gates not fully closed
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- AI infra headline rallies before cloud/SI revenue.
- IPO priced high but stock trades below issue price.
- Webtoon/content platform rallies on IP deal after prior large drawdown.
- game IPO rallies on one or two hit titles before repeatability.
- K-pop/content IP suffers label or founder governance dispute.
- platform founder is hit by regulatory/legal investigation.
- security breach creates compensation and revenue-guidance tail risk.
```

적용:

```text
Kakao/LG CNS:
AI data center rally → 4B if contract revenue/margin not visible.

LG CNS:
IPO debut below issue price → price-failed 4B.

Webtoon:
Disney + earnings rally is good, but prior -55% drawdown → 4B volatility.

Shift Up:
Nikke/Stellar Blade success good, but title concentration → 4B.

HYBE/Kakao:
governance/legal overhang → 4C-watch.

SK Telecom:
security breach → hard 4C.
```

---

# 14. 4C hard gate 조건

```text
R8 4C:
- large-scale customer data breach
- regulatory fine or compensation that changes revenue guidance
- platform founder arrest / capital-market law investigation
- content-label control dispute disrupting artist IP
- cyber incident with user churn and remediation cost
- IPO below issue price with no follow-through demand
- game pipeline cancellation after one-title concentration
```

이번 R8 Loop 16 hard 4C:

```text
SK Telecom cybersecurity breach = hard_4C_success
```

Strong 4C-watch:

```text
- HYBE ADOR/NewJeans and Bang Si-hyuk legal risk
- Kakao founder regulatory overhang
- LG CNS IPO price-failed evidence
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R8 production 설계 원칙:

```text
1. AI infrastructure와 AI software revenue를 분리한다.
2. MAU와 ARPU/profit을 분리한다.
3. IPO valuation과 post-listing price validation을 분리한다.
4. game hit와 repeatable pipeline을 분리한다.
5. content IP와 label/founder governance를 분리한다.
6. cybersecurity incident는 remediation cost, fine, compensation, revenue guidance를 별도 hard gate로 둔다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_244.md 요약

```md
# R8 Loop 16. Platform / Content / Software / Security Trigger-level Price Validation

이번 라운드는 R8 Loop 16 trigger-level validation 라운드다.

핵심 결론:
- Kakao / LG CNS / SK-AWS AI data center is the cleanest Stage2-Actionable AI infrastructure trigger. SK Group and AWS plan a 7T won / $5.11B Ulsan AI data center, with AWS contributing around $4B. Kakao rose 11%, LG CNS 9%, SK Hynix more than 3%, and KOSPI moved above 3,000. Green requires cloud/SI backlog and recurring revenue.
- LG CNS IPO is evidence-good but price failed. IPO raised 1.2T won / $827M and cloud/AI services were over half of sales, but shares traded at 59,700 won below the 61,900 won issue price on debut.
- Webtoon / Naver is Stage2-Actionable content-platform monetization. Webtoon had 170M MAU and 150+ countries, priced IPO at $21, closed debut at $23, then later surged 62% on Disney deal and surprise profit after a prior 55% post-IPO drawdown.
- Krafton / Naver / Mirae India fund is Stage2 geographic/platform expansion. $666M fund, $333M initial capital, BGMI over 240M downloads. Price anchor and monetization are missing.
- Shift Up is Stage2 game-IP monetization with 4B concentration. IPO expected to raise 435B won / $313M; Nikke booked 255B won sales, Stellar Blade ranked No.1 Japan PS downloads and No.2 North America, and 2023 OP was 111B won. Repeatability and post-listing price path are missing.
- HYBE is content-IP governance 4C-watch. ADOR/NewJeans dispute caused shares to fall nearly 8%; police detention-warrant request for Bang Si-hyuk later pushed shares down 2.4%.
- Kakao founder regulatory case is 4C with relief. Kim Beom-su arrest sent Kakao -3.4%; later court acquittal is a relief trigger, but price anchor is unavailable.
- SK Telecom cybersecurity breach is hard 4C. Shares fell as much as 8.5%, closed -6.7% vs KOSPI +0.1%, later probe confirmed 26.96M data pieces leaked, 134B won fine, 700B won security investment, 800B won revenue forecast cut, and possible compensation cost near 2.3T won.

Main calibration:
- Raise AI_compute_to_cloud_revenue, SI_contract_backlog, IP_platform_MAU_monetization, content_IP_license_revenue, game_IP_repeat_sales, India_platform_monetization, label_governance_stability, founder_regulatory_clearance, cybersecurity_trust_cost.
- Lower AI_infra_headline_without_revenue, IPO_valuation_without_post_listing_strength, MAU_without_ARPU_profit, game_hit_without_pipeline, geographic_fund_without_ROI, artist_IP_without_governance, platform_founder_risk_ignored, security_incident_treated_as_one_off.
```

## docs/checkpoints/checkpoint_28a_round244_r8_loop16.md 요약

```md
# Checkpoint 28A Round 244 R8 Loop 16 Trigger-level Calibration

## 반영 내용
- R8 Loop 16 trigger-level validation을 수행했다.
- Kakao/LG CNS AI data center, LG CNS IPO, Webtoon/Naver, Krafton/Naver/Mirae India fund, Shift Up, HYBE governance, Kakao founder regulatory case, SK Telecom cybersecurity breach를 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 Reuters / FT / Barron’s / MarketWatch / Investopedia의 reported event return과 event price anchor를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- AI infrastructure는 cloud/SI recurring revenue 전에는 Stage2다.
- AI/cloud IPO는 post-listing price validation이 필요하다.
- Webtoon/content platform은 MAU보다 ARPU, paid conversion, IP licensing, profit이 중요하다.
- Game IP는 hit sales보다 repeat sales, retention, sequel pipeline이 Green gate다.
- Entertainment는 artist IP와 label/founder governance를 분리한다.
- Cybersecurity breach is hard 4C when it triggers fines, compensation and revenue guidance cuts.
```

## data/e2r_case_library/cases_r8_loop16_round244.jsonl 초안

```jsonl
{"case_id":"r8_loop16_kakao_lgcns_sk_aws_ai_datacenter","symbol":"035720/064400/SK_group_readthrough","company_name":"Kakao / LG CNS / SK-AWS AI data center read-through","case_type":"Stage2_Actionable_AI_infra","primary_archetype":"AI_DATA_CENTER_CLOUD_SI_STAGE2_ACTIONABLE","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2025-06-20","investment_krw_trn":7.0,"investment_usd_bn":5.11,"aws_contribution_usd_bn":4.0,"initial_capacity_mw":100,"full_operation_year":2029,"future_capacity_target_gw":1.0,"kakao_event_return_pct":11,"lg_cns_event_return_pct":9,"sk_hynix_event_return_pct":3,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_AI_infrastructure","notes":"AI infra trigger was strongly price-aligned, but cloud/SI backlog and recurring revenue are Green gates."}
{"case_id":"r8_loop16_lg_cns_ipo_ai_cloud_price_muted","symbol":"064400","company_name":"LG CNS","case_type":"evidence_good_but_price_failed","primary_archetype":"AI_CLOUD_IPO_PRICE_MUTED","best_trigger":"T0/T1","stage_candidate":"Stage2_but_not_Actionable","price_validation":{"trigger_date":"2025-02-05","ipo_raise_krw_trn":1.2,"ipo_raise_usd_mn":827.1,"issue_price_krw":61900,"debut_open_krw":60500,"debut_later_price_krw":59700,"ai_cloud_sales_share_context":">50%_of_first_three_quarters_2024_sales","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"evidence_good_but_price_failed","notes":"AI/cloud exposure was real, but IPO traded below issue price; no Actionable promotion."}
{"case_id":"r8_loop16_webtoon_naver_ip_monetization","symbol":"WBTN/035420_readthrough","company_name":"Webtoon Entertainment / Naver","case_type":"Stage2_Actionable_content_platform","primary_archetype":"WEBTOON_IP_MONETIZATION_STAGE2_ACTIONABLE","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable_to_Yellow_candidate","price_validation":{"ipo_price_usd":21,"ipo_valuation_usd_bn":2.7,"ipo_raise_usd_mn":315,"debut_close_usd":23.0,"debut_return_pct":9.5,"monthly_active_users_mn":170,"countries":">150","q1_2024_revenue_usd_mn":326.7,"q1_2024_net_income_usd_mn":6.2,"disney_earnings_event_return_pct":62,"disney_event_price_usd":15.16,"pre_disney_post_ipo_decline_pct":-55,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_Actionable_content_platform_with_4B_volatility","notes":"IPO and Disney/earnings trigger were strong, but prior drawdown and sustained profitability are gates."}
{"case_id":"r8_loop16_krafton_naver_mirae_india_fund","symbol":"259960/035420/006800","company_name":"Krafton / Naver / Mirae Asset","case_type":"Stage2_platform_game_geographic_expansion","primary_archetype":"GAME_IP_GLOBAL_EXPANSION_STAGE2","best_trigger":"T1/T2","stage_candidate":"Stage2","price_validation":{"trigger_date":"2025-12-19","fund_total_usd_mn":666,"initial_capital_usd_mn":333,"fund_launch":"2026-01","krafton_existing_india_investment_usd_mn":">200","bgmi_downloads_mn":">240","direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_stage2","notes":"India platform expansion is strategic, but monetization and fund ROI are not yet verified."}
{"case_id":"r8_loop16_shiftup_game_ip_ipo","symbol":"ShiftUp_KOSPI","company_name":"Shift Up","case_type":"Stage2_game_IP_with_4B_concentration","primary_archetype":"GAME_IP_IPO_STAGE2_WITH_CONCENTRATION_4B","best_trigger":"T0/T2","stage_candidate":"Stage2 + 4B-watch","price_validation":{"trigger_date":"2024-06-27","ipo_raise_krw_bn":435,"ipo_raise_usd_mn":313,"expected_market_cap_krw_trn":3.5,"expected_market_cap_usd_bn":2.52,"nikke_sales_launch_to_q1_2024_krw_bn":255,"stellar_blade_japan_ps_download_rank":1,"stellar_blade_north_america_ps_download_rank":2,"op_2023_krw_bn":111,"revenue_2023_krw_bn":169,"op_2022_krw_bn":18,"direct_post_listing_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_game_IP_not_Green","notes":"Game IP evidence is strong, but post-listing price path, repeat sales and title concentration are gates."}
{"case_id":"r8_loop16_hybe_content_label_governance","symbol":"352820","company_name":"HYBE","case_type":"4C_watch_content_governance","primary_archetype":"CONTENT_LABEL_GOVERNANCE_4C_WATCH","best_trigger":"T0/T2","stage_candidate":"4C-watch","price_validation":{"ador_dispute_date":"2024-04-24","ador_dispute_event_return_pct":"nearly_-8","bang_warrant_date":"2026-04-21","bang_warrant_event_return_pct":-2.4,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","notes":"Artist IP value is offset by label governance and founder legal overhang."}
{"case_id":"r8_loop16_kakao_founder_regulatory_relief","symbol":"035720","company_name":"Kakao","case_type":"4C_watch_with_relief","primary_archetype":"PLATFORM_FOUNDER_REGULATORY_4C_RELIEF","best_trigger":"T0/T2","stage_candidate":"4C-watch_to_relief","price_validation":{"arrest_date":"2024-07-22/2024-07-23","arrest_event_return_pct":-3.4,"charge_context":"SM_Entertainment_stock_manipulation_suspicion","relief_date":"2025-10-21","relief_event":"court_clears_Kim_Beom_su_of_stock_manipulation_charges","direct_relief_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"platform_founder_regulatory_4C_with_relief","notes":"Founder regulatory overhang hit shares; acquittal is relief but direct relief price anchor unavailable."}
{"case_id":"r8_loop16_sk_telecom_cyber_breach","symbol":"017670","company_name":"SK Telecom","case_type":"hard_4C_cybersecurity","primary_archetype":"CYBERSECURITY_DATA_BREACH_HARD_4C","best_trigger":"T0/T3","stage_candidate":"4C","price_validation":{"breach_price_event_date":"2025-04-28","intraday_event_return_pct":-8.5,"close_event_return_pct":-6.7,"kospi_same_context_pct":0.1,"affected_subscribers_mn":23,"user_data_pieces_leaked_mn":26.96,"july_probe_event_return_pct":-5.6,"security_investment_5y_krw_bn":700,"revenue_forecast_cut_krw_bn":800,"fine_krw_bn":134,"possible_all_victim_compensation_krw_trn":2.3,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"hard_4C_success","notes":"Cyber breach triggered price collapse, fine, remediation cost, revenue guidance cut and compensation tail risk."}
```

## data/e2r_trigger_calibration/triggers_r8_loop16_round244.jsonl 초안

```jsonl
{"trigger_id":"r8l16_kakao_lgcns_ai_dc_T1","case_id":"r8_loop16_kakao_lgcns_sk_aws_ai_datacenter","trigger_type":"Stage2-Actionable_AI_infra","trigger_date":"2025-06-20","evidence_available":"SK Group and AWS announce 7T won / $5.11B Ulsan AI data center; Kakao +11%, LG CNS +9%, SK Hynix +3%, KOSPI above 3,000","event_return_pct":"Kakao +11 / LG CNS +9","trigger_outcome_label":"excellent_stage2_actionable_AI_infrastructure","promote_to":"Stage2-Actionable"}
{"trigger_id":"r8l16_lgcns_ipo_T1","case_id":"r8_loop16_lg_cns_ipo_ai_cloud_price_muted","trigger_type":"evidence_good_but_price_failed","trigger_date":"2025-02-05","evidence_available":"LG CNS IPO raised 1.2T won / $827M; cloud and AI services over half of sales, but shares traded at 59,700 won below 61,900 won issue price","event_return_pct":"below_issue_price","trigger_outcome_label":"evidence_good_but_price_failed","promote_to":"Stage2_only"}
{"trigger_id":"r8l16_webtoon_ipo_T1","case_id":"r8_loop16_webtoon_naver_ip_monetization","trigger_type":"Stage2-Actionable_IP_platform","trigger_date":"2024-06-27/2024-06-28","evidence_available":"Webtoon IPO priced at $21, valuation $2.7B, raised $315M, debut close $23.00; 170M MAU and 150+ countries","event_return_pct":9.5,"trigger_outcome_label":"Stage2_Actionable_content_platform","promote_to":"Stage2-Actionable"}
{"trigger_id":"r8l16_webtoon_disney_T2","case_id":"r8_loop16_webtoon_naver_ip_monetization","trigger_type":"Stage2_validation_Yellow_candidate","trigger_date":"2025-08-13","evidence_available":"Webtoon shares +62% to $15.16 after Disney IP deal and surprise profit, after prior 55% post-IPO decline","event_return_pct":62,"trigger_outcome_label":"IP_monetization_validation_with_4B_volatility","promote_to":"Stage2-Actionable_to_Yellow_candidate"}
{"trigger_id":"r8l16_krafton_india_T1","case_id":"r8_loop16_krafton_naver_mirae_india_fund","trigger_type":"Stage2_geographic_expansion","trigger_date":"2025-12-19","evidence_available":"Krafton, Naver and Mirae Asset launch $666M India tech fund; initial $333M; Krafton has invested over $200M in India and BGMI has over 240M downloads","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_geographic_expansion_not_Green","promote_to":"Stage2"}
{"trigger_id":"r8l16_shiftup_ipo_T0","case_id":"r8_loop16_shiftup_game_ip_ipo","trigger_type":"Stage2_game_IP","trigger_date":"2024-06-27","evidence_available":"Shift Up IPO expected to raise 435B won / $313M, market cap 3.5T won; Nikke 255B won sales, Stellar Blade top PS download rankings, 2023 OP 111B won","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_game_IP_with_concentration_4B","promote_to":"Stage2+4B"}
{"trigger_id":"r8l16_hybe_ador_T0","case_id":"r8_loop16_hybe_content_label_governance","trigger_type":"4C-watch_content_governance","trigger_date":"2024-04-24","evidence_available":"HYBE audits ADOR amid Min Hee-jin/NewJeans label dispute; shares fall nearly 8%","event_return_pct":"nearly_-8","trigger_outcome_label":"content_label_governance_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r8l16_hybe_bang_T2","case_id":"r8_loop16_hybe_content_label_governance","trigger_type":"4C-watch_founder_legal","trigger_date":"2026-04-21","evidence_available":"Police seek detention warrant for Bang Si-hyuk over alleged capital-market law violation; HYBE shares -2.4% despite market uptick","event_return_pct":-2.4,"trigger_outcome_label":"founder_governance_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r8l16_kakao_founder_T0","case_id":"r8_loop16_kakao_founder_regulatory_relief","trigger_type":"4C-watch_founder_regulatory","trigger_date":"2024-07-22/2024-07-23","evidence_available":"Kakao founder Kim Beom-su arrested over suspected SM Entertainment stock manipulation; Kakao shares -3.4%","event_return_pct":-3.4,"trigger_outcome_label":"platform_founder_regulatory_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r8l16_skt_breach_T0","case_id":"r8_loop16_sk_telecom_cyber_breach","trigger_type":"hard_4C_cybersecurity","trigger_date":"2025-04-28","evidence_available":"SK Telecom discloses customer data leak from malware; shares as much as -8.5%, close -6.7%, KOSPI +0.1%; free USIM replacement for 23M users","event_return_pct":-6.7,"trigger_outcome_label":"hard_4C_success_cybersecurity","promote_to":"4C"}
{"trigger_id":"r8l16_skt_breach_penalty_T2","case_id":"r8_loop16_sk_telecom_cyber_breach","trigger_type":"4C_validation_penalty","trigger_date":"2025-07-04/2025-08-28/2025-12-21","evidence_available":"Probe confirms 26.96M data pieces leaked, shares -5.6%, 700B won security investment, 800B won revenue forecast cut, 134B won fine, possible compensation near 2.3T won","event_return_pct":-5.6,"trigger_outcome_label":"cybersecurity_4C_validation","promote_to":"4C"}
```

## data/sector_taxonomy/score_weight_profiles_round244_r8_loop16_v1.csv 초안

```csv
archetype,ai_compute_to_cloud_revenue,si_contract_backlog,ip_platform_mau_monetization,content_ip_license_revenue,game_ip_repeat_sales,india_platform_monetization,label_governance_stability,founder_regulatory_clearance,cybersecurity_trust_cost,ai_infra_headline_without_revenue_penalty,ipo_valuation_without_post_listing_strength_penalty,mau_without_arpu_profit_penalty,game_hit_without_pipeline_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
AI_DATA_CENTER_CLOUD_SI_STAGE2_ACTIONABLE,+5,+5,+1,+0,+0,+0,+1,+1,+2,-5,-2,-1,-1,AI data center+price reaction,cloud/SI revenue missing,recurring revenue+margin,Kakao/LG CNS.
AI_CLOUD_IPO_PRICE_MUTED,+4,+4,+0,+0,+0,+0,+0,+0,+1,-4,-5,-1,-1,AI/cloud sales but IPO price failed,post-listing strength missing,contract growth+margin,LG CNS IPO.
WEBTOON_IP_MONETIZATION_STAGE2_ACTIONABLE,+1,+0,+5,+5,+0,+1,+1,+1,+0,-1,-3,-5,-1,MAU+IPO+Disney/IP deal,profit durability missing,paid conversion+IP revenue+profit,Webtoon/Naver.
GAME_IP_GLOBAL_EXPANSION_STAGE2,+0,+0,+1,+1,+5,+5,+0,+0,+1,-1,-2,-1,-4,India expansion+BGMI scale,ARPU/fund ROI missing,India monetization+fund exits,Krafton/Naver/Mirae.
GAME_IP_IPO_STAGE2_WITH_CONCENTRATION_4B,+0,+0,+0,+1,+5,+0,+0,+0,+0,-1,-4,-1,-5,game IP sales/profit,repeat sales/pipeline missing,retention+new title pipeline,Shift Up.
CONTENT_LABEL_GOVERNANCE_4C_WATCH,+0,+0,+2,+5,+0,+0,+5,+4,+1,-1,-1,-1,-1,artist IP disrupted by governance,legal resolution missing,N/A,HYBE.
PLATFORM_FOUNDER_REGULATORY_4C_RELIEF,+2,+0,+2,+0,+0,+0,+3,+5,+1,-1,-1,-1,-1,founder regulatory overhang,platform monetization/relief price missing,regulatory clearance+business normalization,Kakao.
CYBERSECURITY_DATA_BREACH_HARD_4C,+0,+0,+0,+0,+0,+0,+1,+1,+5,-1,-1,-1,-1,data breach/fine/compensation,remediation and trust recovery missing,N/A,SK Telecom.
```

---

# 이번 R8 Loop 16 결론

```text
1. Kakao/LG CNS AI data center trigger는 R8의 가장 좋은 Stage2-Actionable이다.
   Kakao +11%, LG CNS +9%로 price reaction이 강했다. 다만 cloud/SI recurring revenue 전에는 Green이 아니다.

2. LG CNS IPO는 evidence_good_but_price_failed다.
   AI/cloud sales share는 좋았지만 공모가 61,900 won 아래인 59,700 won에 거래됐다.

3. Webtoon/Naver는 Stage2-Actionable content platform이다.
   IPO +9.5%, Disney/earnings +62%는 강하지만 prior -55% drawdown과 profit durability가 4B다.

4. Krafton/Naver/Mirae India fund는 Stage2 geographic expansion이다.
   $666M fund와 BGMI 240M+ downloads는 좋지만 ARPU/fund ROI가 필요하다.

5. Shift Up은 Stage2 game IP + 4B다.
   Nikke, Stellar Blade, OP growth는 강하지만 title concentration and post-listing price path가 필요하다.

6. HYBE는 content IP governance 4C-watch다.
   ADOR/NewJeans dispute와 Bang legal risk가 artist IP rerating을 막았다.

7. Kakao founder case는 platform regulatory 4C with relief다.
   arrest -3.4%, later acquittal은 relief지만 business normalization이 필요하다.

8. SK Telecom breach는 hard 4C다.
   -8.5% intraday, -6.7% close, 134B won fine, 700B won security investment, 800B won revenue forecast cut, compensation tail risk가 모두 닫혔다.
```

한 문장으로 압축하면:

> **R8 Loop 16에서 배운 핵심은 “AI·웹툰·게임·K-pop·보안 headline”이 아니라, cloud/SI recurring revenue, ARPU/profit, IP licensing, repeat game sales, label governance, founder regulatory clearance, cybersecurity trust cost가 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 AI data center headline, IPO valuation, MAU, one-hit game, artist IP, founder story만으로는 4B/false positive가 되기 쉽다.**

[1]: https://www.reuters.com/business/retail-consumer/south-korea-says-sk-amazon-invest-5-bln-countrys-biggest-data-centre-2025-06-20/?utm_source=chatgpt.com "South Korea says SK and Amazon to invest $5 billion in country's biggest data centre"
[2]: https://www.reuters.com/technology/skorean-tech-services-firm-lg-cns-falls-stock-market-debut-2025-02-05/?utm_source=chatgpt.com "South Korean tech services firm LG CNS drops in market debut"
[3]: https://www.reuters.com/markets/deals/online-comics-platform-webtoon-reveals-revenue-growth-profitability-us-ipo-2024-05-31/?utm_source=chatgpt.com "Online comics platform Webtoon reveals revenue growth, profitability in US IPO filing"
[4]: https://www.reuters.com/world/asia-pacific/pubg-maker-krafton-leads-south-korean-trio-666-million-india-tech-bet-2025-12-19/?utm_source=chatgpt.com "PUBG maker Krafton leads South Korean trio in $666 million India tech bet"
[5]: https://www.reuters.com/markets/deals/tencent-backed-shift-up-may-price-ipo-top-end-band-source-says-2024-06-27/?utm_source=chatgpt.com "Tencent-backed Shift Up may price IPO at top end of band, source says"
[6]: https://www.reuters.com/lifestyle/record-giant-hybe-audits-newjeans-label-infighting-returns-k-pop-2024-04-24/?utm_source=chatgpt.com "Record giant HYBE audits 'NewJeans' label as infighting returns to K-pop"
[7]: https://www.reuters.com/technology/south-korean-court-approves-arrest-warrant-kakao-founder-2024-07-22/?utm_source=chatgpt.com "Founder of South Korea's Kakao arrested for suspected stock manipulation"
[8]: https://www.reuters.com/sustainability/boards-policy-regulation/sk-telecom-shares-plunge-after-data-breach-due-cyberattack-2025-04-28/?utm_source=chatgpt.com "SK Telecom shares plunge after data breach due to cyberattack"
