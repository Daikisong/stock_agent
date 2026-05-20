순서상 이번은 **R8 Loop 17 — 플랫폼·콘텐츠·SW·보안 trigger-level price validation 라운드**다.

```text
round = R8 Loop 17
round_id = round_257
large_sector = PLATFORM_CONTENT_SW_SECURITY
method = trigger_level_backtest_v1_after_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R9 Loop 17
```

이번 R8도 KRX/Naver/Yahoo/Stooq 수정주가 일봉 OHLC window를 안정적으로 확보하지 못했다. 그래서 MFE/MAE/peak/drawdown 숫자는 만들지 않고 `price_data_unavailable_after_deep_search`로 둔다. 대신 Reuters/FT/WSJ/Barron’s 등에서 확인된 **reported event return, IPO price, deal value, abnormal-withdrawal amount, breach 규모, MAU/매출/AI infrastructure data**를 trigger anchor로 쓴다.

---

# 1. 이번 라운드 대섹터

```text
R8 = 플랫폼·콘텐츠·SW·보안
```

R8의 core gate는 아래다.

```text
AI platform:
AI partnership → product integration → MAU / ARPU / ad conversion → cloud/inference cost → margin → security/data sovereignty 4B

Sovereign AI / cloud:
GPU procurement → sovereign AI export → government/enterprise contract → cloud utilization → capex ROI → global scale risk

Content platform:
IPO / Disney·Marvel IP deal → MAU → paid conversion → ad/subscription revenue → creator payout → parent holding discount

Gaming:
IPO / major title launch → concurrent users / sales → live-service retention → DLC/sequel pipeline → legal/IP/control risk

K-pop / content IP:
artist comeback → album/tour/IP monetization → platform/community revenue → label governance → artist contract dispute 4B

Cybersecurity / platform trust:
breach → user churn / compensation / regulatory fine → security capex → revenue guidance cut → hard 4C or 4B

IT services / SW:
cloud+AI sales mix → IPO / M&A → order backlog → margin → weak debut / valuation overhang
```

---

# 2. 대상 canonical archetype

```text
AI_CHAT_PLATFORM_PARTNERSHIP_STAGE2_PRICE_FAILED
SOVEREIGN_AI_CLOUD_INFRA_STAGE2_CAPEX_4B
WEBTOON_CONTENT_PLATFORM_STAGE2_HOLDCO_DISCOUNT
GAMING_IP_SUCCESS_STAGE2_WITH_LEGAL_4B
IT_SERVICES_AI_CLOUD_IPO_PRICE_FAILED
CYBER_BREACH_HARD_4C_SECURITY_CAPEX
KPOP_LABEL_GOVERNANCE_4B
PLATFORM_GOVERNANCE_REGULATORY_4B
```

---

# 3. deep sub-archetype

```text
Kakao / OpenAI:
- OpenAI and Kakao agreed to jointly develop AI products for South Korea.
- Kakao shares initially surged about 9% but later ended down 2%.
- Stage2 AI partnership, but price-failed / execution-overhang.
- 4B: founder legal risk, regulatory scrutiny, AI capex, product monetization.

Naver / sovereign AI / Nvidia Blackwell:
- Nvidia to supply more than 260,000 Blackwell AI chips to South Korea.
- Naver to purchase 60,000 chips to boost computing capacity.
- FT reported Naver plans $690M 2026 AI/cloud investment and stock +20% YTD.
- Stage2 sovereign AI/cloud infra, not Green until enterprise contracts and cloud utilization.

Webtoon Entertainment / Naver:
- Webtoon Nasdaq debut rose as much as 14.3%; IPO raised $315M at top of range.
- Later stock jumped 62% after Disney/Marvel/Star Wars deal and surprise Q2 profit.
- But Naver got weaker valuation boost; Nomura applied 50% holding-company discount and cut Naver target by 22%.
- Stage2 content platform, parent holdco discount 4B.

Shift Up:
- IPO priced at top of range, raising 435B won / about $313M, valuation 3.5T won.
- Goddess of Victory: Nikke generated 255B won from late 2022 through Q1 2024; Stellar Blade success supported listing.
- Stage2 gaming IP, but post-listing OHLC unavailable in this source set.

Krafton / Subnautica:
- Delaware court ruled against Krafton in Unknown Worlds/Subnautica dispute.
- Court found improper removal of CEO and extended earnout timeline tied to $250M bonus.
- This is gaming IP governance/legal 4B, not hard 4C unless financial or release impact becomes stock-price confirmed.

LG CNS:
- IT/cloud/AI services provider raised 1.2T won / $827.1M IPO.
- Shares opened below 61,900 won IPO price and traded at 59,700 won.
- Cloud and AI services were 54% of first-three-quarter 2024 sales.
- Stage2 SW/cloud, but IPO price failed.

SK Telecom:
- cyberattack/data breach; shares fell as much as 8.5%, closed -6.7%, KOSPI +0.1%.
- later 26.96M pieces of user data identified, 700B won 5-year security investment, 50% August fee discount, 800B won 2025 revenue forecast cut.
- Strong hard 4C / security-trust break.

HYBE:
- ADOR/NewJeans dispute caused shares to drop nearly 8%.
- 2026 police sought detention warrant for Bang Si-hyuk; HYBE stock fell 2.4%.
- Content IP remains strong, but label governance/founder legal 4B is material.

Kakao founder legal/regulatory:
- Kakao founder Kim Beom-su arrested in 2024 on stock manipulation allegations; Kakao shares -3.4%.
- A conviction could jeopardize KakaoBank control; later 2025 court cleared Kim.
- Platform governance 4B, relief trigger exists but not Green.
```

---

# 4. 선정 case 요약

| bucket                  | case                                    | 핵심 판정                                                                                   |
| ----------------------- | --------------------------------------- | --------------------------------------------------------------------------------------- |
| Stage2 price-failed     | **Kakao / OpenAI AI partnership**       | initial +9% → later -2%, AI product integration but monetization/regulatory 4B          |
| Stage2 capex            | **Naver sovereign AI / Blackwell GPUs** | Naver 60,000 Blackwell chips, $690M AI/cloud investment, stock +20% YTD                 |
| Stage2 content platform | **Webtoon / Naver**                     | IPO +14.3%, Disney deal +62%, but Naver holdco discount                                 |
| Stage2 gaming IP        | **Shift Up IPO / Stellar Blade**        | 435B won IPO, 3.5T won valuation, Nikke 255B won revenue context                        |
| legal 4B                | **Krafton / Subnautica dispute**        | Delaware ruling against Krafton, $250M earnout/control issue                            |
| price-failed SW IPO     | **LG CNS IPO**                          | 1.2T won IPO, 61,900 won issue → 59,700 won debut trading                               |
| hard 4C security        | **SK Telecom cyber breach**             | -6.7% close, 26.96M data pieces, 700B won security capex, 800B won revenue forecast cut |
| content-governance 4B   | **HYBE / ADOR + founder investigation** | shares nearly -8% on ADOR, -2.4% on Bang detention warrant                              |
| platform-governance 4B  | **Kakao founder legal risk**            | shares -3.4%, AI/overseas/KakaoBank control risk; later acquittal relief                |

---

# 5. 각 case별 trigger grid

## Case A — Kakao / OpenAI AI partnership

```text
symbol = 035720
case_type = Stage2 AI platform partnership, price failed
archetype = AI_CHAT_PLATFORM_PARTNERSHIP_STAGE2_PRICE_FAILED
```

| trigger |             type | date       | 당시 공개 evidence                                                         | 가격 anchor         | outcome |
| ------- | ---------------: | ---------- | ---------------------------------------------------------------------- | ----------------- | ------- |
| T0      |           Stage1 | 2024~2025  | Kakao AI service rollout need, platform monetization pressure          | no entry          |         |
| T1      |  Stage2 evidence | 2025-02-04 | OpenAI and Kakao to jointly develop AI products in South Korea         | initial Kakao +9% |         |
| T2      | price validation | 2025-02-04 | KakaoTalk integration 기대에도 stock later -2%                             | price failed      |         |
| T3      |         4B-watch | 2025       | execution, AI capex, product monetization, founder/regulatory overhang | 4B                |         |
| T4      |    Stage3-Yellow | N/A        | MAU/ARPU/ad conversion or paid AI revenue needed                       | 보류                |         |

Kakao/OpenAI는 headline만 보면 강한 Stage2다. OpenAI가 Kakao와 한국용 AI product를 공동 개발하기로 했고, KakaoTalk 같은 dominant messaging app에 OpenAI technology를 붙일 수 있다는 기대가 있었다. 그런데 Kakao 주가는 처음 약 +9% 급등했다가 이후 -2%로 끝났다. 이건 “AI partnership = Green”이 아니라, **AI product integration은 Stage2, 가격검증은 failed**로 분리해야 한다는 case다. Reuters는 같은 기사에서 OpenAI가 Stargate 관련 논의를 Samsung·SoftBank·Arm과도 진행했다고 보도했다. ([Reuters][1])

```json
{
  "case_id": "r8_loop17_kakao_openai_ai_partnership",
  "symbol": "035720",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2_AI_platform_partnership_price_failed",
  "trigger_date": "2025-02-04",
  "initial_event_return_pct": 9,
  "later_event_return_pct": -2,
  "strategic_logic": [
    "KakaoTalk_AI_product_integration",
    "OpenAI_technology_partnership",
    "Korean_AI_service_localization",
    "Stargate_adjacent_AI_infra_context"
  ],
  "4B_overlay": [
    "product_monetization_uncertain",
    "AI_inference_cost",
    "founder_legal_overhang",
    "regulatory_scrutiny",
    "execution_risk"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_AI_partnership_but_price_failed"
}
```

---

## Case B — Naver sovereign AI / Blackwell GPU infrastructure

```text
symbol = 035420
case_type = Stage2 sovereign AI/cloud infrastructure
archetype = SOVEREIGN_AI_CLOUD_INFRA_STAGE2_CAPEX_4B
```

| trigger |                  type | date         | 당시 공개 evidence                                                                                    | 가격 anchor                    | outcome |
| ------- | --------------------: | ------------ | ------------------------------------------------------------------------------------------------- | ---------------------------- | ------- |
| T0      |                Stage1 | 2025         | sovereign AI / data-sovereignty theme                                                             | no entry                     |         |
| T1      | Stage2 infrastructure | 2025-10-31   | Nvidia to supply South Korea with 260,000+ Blackwell chips; Naver to buy 60,000                   | no event return              |         |
| T2      |            validation | 2026 context | Naver promoting sovereign AI/cloud to Middle East, SE Asia, Japan; $690M 2026 AI/cloud investment | Naver stock +20% YTD context |         |
| T3      |              4B-watch | 2026         | capex ROI, international scaling, U.S./China cloud competition, data-sovereignty execution        | 4B                           |         |
| T4      |         Stage3-Yellow | N/A          | enterprise/government contracts and cloud utilization needed                                      | 보류                           |         |

Naver sovereign AI는 R8에서 가장 구조적인 Stage2 후보 중 하나다. Reuters는 Nvidia가 한국에 260,000개 이상의 Blackwell AI chips를 공급하고, 그중 Naver가 computing capacity 강화를 위해 60,000개를 구매한다고 보도했다. FT는 Naver가 U.S./China hyperscaler의 대안으로 sovereign AI/cloud를 밀고 있으며, 2026년에 $690M 규모의 AI/cloud 투자와 60,000 Blackwell GPUs 조달을 계획하고 있고, 주가는 AI 기대감으로 연중 약 +20% 올랐다고 설명했다. 다만 Green은 cloud utilization, enterprise contract, AI service margin이 닫혀야 한다. ([Reuters][2])

```json
{
  "case_id": "r8_loop17_naver_sovereign_ai_blackwell",
  "symbol": "035420",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2_sovereign_AI_cloud_capex",
  "blackwell_trigger_date": "2025-10-31",
  "south_korea_blackwell_chip_supply_count": ">260000",
  "naver_blackwell_chip_count": 60000,
  "naver_ai_cloud_investment_2026_usd_mn": 690,
  "reported_stock_return_ytd_context_pct": 20,
  "strategic_logic": [
    "sovereign_AI",
    "data_sovereignty",
    "cloud_and_AI_services_export",
    "Middle_East_SE_Asia_Japan_expansion"
  ],
  "4B_overlay": [
    "capex_ROI",
    "global_cloud_scale_risk",
    "enterprise_contract_visibility",
    "GPU_depreciation",
    "AI_margin_uncertainty"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_sovereign_AI_cloud_not_Green"
}
```

---

## Case C — Webtoon Entertainment / Naver content platform

```text
symbols = WBTN / 035420
case_type = Stage2 content platform with parent holding discount
archetype = WEBTOON_CONTENT_PLATFORM_STAGE2_HOLDCO_DISCOUNT
```

| trigger |              type | date       | 당시 공개 evidence                                                                            | 가격 anchor                       | outcome |
| ------- | ----------------: | ---------- | ----------------------------------------------------------------------------------------- | ------------------------------- | ------- |
| T0      |        Stage2 IPO | 2024-06-27 | Naver-backed Webtoon Nasdaq debut                                                         | WBTN +14.3% intraday; IPO $315M |         |
| T1      |         parent 4B | 2024-06-19 | Nomura says Naver valuation boost weaker; 50% holdco discount; Naver -0.9% to 165,300 won | parent price weak               |         |
| T2      | Stage2 validation | 2025-08-13 | Webtoon Disney/Marvel/Star Wars deal + surprise profit                                    | WBTN +62% early trading         |         |
| T3      |          4B-watch | 2024~2025  | post-IPO stock -55% before rebound, creator payout, monetization, parent discount         | 4B                              |         |
| T4      |     Stage3-Yellow | N/A        | MAU→paid/revenue/margin and parent Naver readthrough needed                               | 보류                              |         |

Webtoon은 콘텐츠 플랫폼 Stage2로는 매우 좋지만, Naver parent readthrough는 약했다. Reuters는 Naver-backed Webtoon의 Nasdaq debut에서 Webtoon shares가 IPO price 대비 최대 +14.3% 올랐고, IPO가 $315M를 raised했다고 보도했다. 하지만 MarketWatch/WSJ market talk는 Nomura가 Webtoon IPO의 Naver valuation boost가 약할 수 있다며 50% holding-company discount를 적용하고 Naver target을 22% 낮췄으며, Naver shares가 -0.9%, 165,300원이었다고 보도했다. 이후 Barron’s는 Webtoon이 Disney/Marvel/Star Wars comics deal과 surprise Q2 profit을 발표하자 주가가 +62% 급등했다고 보도했다. 즉 Webtoon 자체는 Stage2 content platform이지만, Naver는 holdco discount 4B다. ([Reuters][3])

```json
{
  "case_id": "r8_loop17_webtoon_naver_content_platform",
  "symbols": "WBTN/035420",
  "best_trigger": "T0/T3",
  "best_trigger_type": "Stage2_content_platform_with_parent_holdco_4B",
  "ipo_date": "2024-06-27",
  "webtoon_ipo_intraday_return_pct": 14.3,
  "webtoon_ipo_raise_usd_mn": 315,
  "webtoon_ipo_valuation_usd_bn": 2.71,
  "naver_private_placement_usd_mn": 50,
  "naver_market_talk_price_krw": 165300,
  "naver_market_talk_return_pct": -0.9,
  "nomura_target_cut_pct": 22,
  "holdco_discount_pct": 50,
  "disney_deal_event_return_pct": 62,
  "q2_revenue_usd_mn": 348.3,
  "q2_revenue_yoy_pct": 8.5,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Webtoon_stage2_but_Naver_holdco_discount_4B"
}
```

---

## Case D — Shift Up / gaming IP IPO

```text
symbol = 462870
case_type = Stage2 gaming IP / IPO
archetype = GAMING_IP_SUCCESS_STAGE2_WITH_LEGAL_4B
```

| trigger |          type | date       | 당시 공개 evidence                                                         | 가격 anchor                                   | outcome |
| ------- | ------------: | ---------- | ---------------------------------------------------------------------- | ------------------------------------------- | ------- |
| T0      |        Stage1 | 2024       | Stellar Blade PS5 success, Nikke mobile revenue                        | no entry                                    |         |
| T1      |    Stage2 IPO | 2024-06-27 | Shift Up IPO likely priced top of range                                | raises 435B won / $313M, valuation 3.5T won |         |
| T2      |    validation | 2024       | Goddess of Victory: Nikke generated 255B won from late 2022 to Q1 2024 | no listing-day OHLC                         |         |
| T3      |      4B-watch | 2024~2026  | Tencent ownership, title concentration, PC/sequel execution            | 4B                                          |         |
| T4      | Stage3-Yellow | N/A        | title sales, retention, royalties, new pipeline needed                 | 보류                                          |         |

Shift Up은 R8 gaming IP Stage2다. Reuters는 Tencent-backed Shift Up이 IPO를 price-band 상단에서 정할 가능성이 있고, 435B won, 약 $313M를 조달하며 valuation은 3.5T won, 약 $2.52B가 될 것이라고 보도했다. 또 Goddess of Victory: Nikke가 2022년 말부터 2024년 1분기까지 255B won revenue를 냈고, Stellar Blade의 download ranking success도 IPO를 뒷받침했다. 다만 이 source set에서 listing-day adjusted OHLC와 post-launch MFE/MAE는 확보하지 못했다. 따라서 Stage2 gaming IP로 두되, Green은 PC sales/royalty, live-service retention, sequel pipeline 확인 후다. ([Reuters][4])

```json
{
  "case_id": "r8_loop17_shift_up_gaming_ip_ipo",
  "symbol": "462870",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2_gaming_IP_IPO_no_full_price",
  "trigger_date": "2024-06-27",
  "ipo_raise_krw_bn": 435,
  "ipo_raise_usd_mn": 313,
  "ipo_valuation_krw_trn": 3.5,
  "ipo_valuation_usd_bn": 2.52,
  "nikke_revenue_late_2022_to_q1_2024_krw_bn": 255,
  "major_titles": [
    "Goddess_of_Victory_Nikke",
    "Stellar_Blade"
  ],
  "4B_overlay": [
    "title_concentration",
    "Tencent_ownership",
    "PC_port_sales_execution",
    "sequel_pipeline",
    "live_service_retention"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_gaming_IP_no_OHLC"
}
```

---

## Case E — Krafton / Subnautica legal-governance dispute

```text
symbol = 259960
case_type = gaming IP governance/legal 4B
archetype = GAMING_IP_SUCCESS_STAGE2_WITH_LEGAL_4B
```

| trigger |              type | date       | 당시 공개 evidence                                                                             | 가격 anchor             | outcome |
| ------- | ----------------: | ---------- | ------------------------------------------------------------------------------------------ | --------------------- | ------- |
| T0      | Stage2 background | 2021~2025  | Krafton acquired Unknown Worlds, Subnautica 2 earnout structure                            | no price              |         |
| T1      |          4B legal | 2026-03-16 | Delaware court ruled against Krafton in Unknown Worlds case                                | no KRX price          |         |
| T2      |        validation | 2026-03-16 | court found improper removal of CEO; operational control returned; earnout period extended | $250M earnout         |         |
| T3      |          4B-watch | 2026       | release timing, reputation, earnout liability, appeal risk                                 | 4B                    |         |
| T4      |           hard 4C | N/A        | stock-price confirmed financial impairment not available                                   | hard 4C not confirmed |         |

Krafton/Subnautica는 R8에서 “gaming IP 성공”과 “studio governance/legal risk”를 분리하는 case다. Reuters는 Delaware court가 Krafton의 Unknown Worlds takeover plan에 반대 판결을 냈고, Krafton이 CEO Ted Gill을 부당하게 해임했다고 보도했다. 이 dispute는 2021년 Unknown Worlds 인수와 연결된 $250M earnout을 둘러싼 문제였고, court는 operational control을 Gill에게 돌려주고 earnout timeline을 연장했다. 주가 anchor는 없으므로 hard 4C는 아니지만, acquired studio/IP pipeline에는 강한 4B다. ([Reuters][5])

```json
{
  "case_id": "r8_loop17_krafton_subnautica_legal_4b",
  "symbol": "259960",
  "best_trigger": "T1/T3",
  "best_trigger_type": "4B_gaming_IP_governance_legal_dispute",
  "trigger_date": "2026-03-16",
  "earnout_value_usd_mn": 250,
  "court_outcome": "Delaware_court_ruled_against_Krafton",
  "operational_control_returned_to": "Ted_Gill",
  "risk_items": [
    "release_timing",
    "studio_governance",
    "earnout_liability",
    "reputation_damage",
    "appeal_risk"
  ],
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "hard_4C_status": "not_confirmed",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "gaming_IP_legal_4B_not_4C"
}
```

---

## Case F — LG CNS IT/cloud/AI services IPO

```text
symbol = 064400
case_type = IT services / AI-cloud IPO price failed
archetype = IT_SERVICES_AI_CLOUD_IPO_PRICE_FAILED
```

| trigger |             type | date       | 당시 공개 evidence                                                                       | 가격 anchor                  | outcome |
| ------- | ---------------: | ---------- | ------------------------------------------------------------------------------------ | -------------------------- | ------- |
| T0      |       Stage2 IPO | 2025-01-06 | LG CNS IPO to raise up to $817M, price range 53,700~61,900 won                       | no trading yet             |         |
| T1      | price validation | 2025-02-05 | IPO priced at 61,900 won, raised 1.2T won / $827.1M                                  | opened 60,500, last 59,700 |         |
| T2      |       validation | 2025-02-05 | cloud+AI services 54% of first-three-quarter 2024 sales; 4T won revenue, 313B won OP | same                       |         |
| T3      |         4B-watch | 2025       | weak IPO debut, valuation, M&A execution, captive sales mix                          | 4B                         |         |
| T4      |    Stage3-Yellow | N/A        | external AI/cloud order backlog and margin expansion needed                          | 보류                         |         |

LG CNS는 R8 SW/cloud IPO의 price-failed case다. Reuters는 LG CNS가 1.2T won, $827.1M 규모 IPO를 했고, issue price는 61,900원이었다고 보도했다. 그런데 listing debut에서 shares는 60,500원으로 열리고 59,700원에 거래되어 issue price를 밑돌았다. cloud and AI services가 2024년 첫 3개 분기 매출의 54%를 차지한다는 점은 좋지만, IPO 가격검증은 실패다. 따라서 Stage2 SW/cloud로만 두고 Green은 external order backlog와 margin 확인 후다. ([Reuters][6])

```json
{
  "case_id": "r8_loop17_lg_cns_ai_cloud_ipo_price_failed",
  "symbol": "064400",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2_IT_services_AI_cloud_IPO_price_failed",
  "ipo_launch_date": "2025-01-06",
  "ipo_price_range_krw": "53700-61900",
  "ipo_raise_krw_trn": 1.2,
  "ipo_raise_usd_mn": 827.1,
  "issue_price_krw": 61900,
  "debut_open_price_krw": 60500,
  "debut_last_price_krw": 59700,
  "cloud_ai_sales_share_first_3q_2024_pct": 54,
  "first_3q_2024_revenue_krw_trn": 4.0,
  "first_3q_2024_operating_profit_krw_bn": 313,
  "4B_overlay": [
    "weak_IPO_debut",
    "valuation_overhang",
    "AI_MA_execution",
    "captive_sales_mix",
    "external_order_backlog_unknown"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "AI_cloud_SW_evidence_good_but_IPO_price_failed"
}
```

---

## Case G — SK Telecom cyberattack / data breach

```text
symbol = 017670
case_type = hard 4C platform/security trust break
archetype = CYBER_BREACH_HARD_4C_SECURITY_CAPEX
```

| trigger |                    type | date       | 당시 공개 evidence                                                                                  | 가격 anchor                                | outcome |
| ------- | ----------------------: | ---------- | ----------------------------------------------------------------------------------------------- | ---------------------------------------- | ------- |
| T0      |              4C trigger | 2025-04-28 | cyberattack/data breach, USIM replacement, all 23M subscribers affected by remediation          | intraday -8.5%, close -6.7%, KOSPI +0.1% |         |
| T1      |              validation | 2025-07-04 | 26.96M pieces of user data leaked; 700B won 5-year security investment; 50% August fee discount | no new stock price                       |         |
| T2      |        financial impact | 2025-07-04 | 2025 revenue forecast cut by 800B won due compensation/remediation cost                         | 4C                                       |         |
| T3      | compensation escalation | 2025-12-21 | consumer agency orders compensation; broader compensation could approach 2.3T won               | 4C-watch                                 |         |
| T4      |                recovery | N/A        | churn, ARPU, trust, security audit completion needed                                            | 보류                                       |         |

SK Telecom은 이번 R8의 가장 강한 hard 4C다. Reuters는 cyberattack/data breach 후 SK Telecom shares가 장중 최대 -8.5% 하락했고 종가는 -6.7%였으며 KOSPI는 +0.1%였다고 보도했다. 이후 정부는 26.96M pieces of user data leak를 확인했고, SKT는 5년간 700B won security investment, August subscription fee 50% discount, 2025 revenue forecast 800B won 하향을 발표했다. 또 consumer agency compensation 이슈가 이어졌고 broader compensation이 최대 2.3T won까지 거론됐다. 이건 단순 4B가 아니라 **trust/security thesis break**다. ([Reuters][7])

```json
{
  "case_id": "r8_loop17_sk_telecom_cyber_breach",
  "symbol": "017670",
  "best_trigger": "T0/T3",
  "best_trigger_type": "hard_4C_cybersecurity_trust_break",
  "trigger_date": "2025-04-28",
  "intraday_event_return_pct": -8.5,
  "close_event_return_pct": -6.7,
  "kospi_same_context_pct": 0.1,
  "affected_subscribers_context_mn": 23,
  "leaked_data_pieces_mn": 26.96,
  "security_investment_5yr_krw_bn": 700,
  "august_subscription_discount_pct": 50,
  "revenue_forecast_cut_2025_krw_bn": 800,
  "potential_broader_compensation_krw_trn": 2.3,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "recovery_gate_missing": [
    "churn_stabilization",
    "ARPU_recovery",
    "security_audit_completion",
    "compensation_finality",
    "regulator_closure"
  ],
  "trigger_outcome_label": "hard_4C_success_cyber_breach"
}
```

---

## Case H — HYBE / ADOR-NewJeans dispute and founder legal risk

```text
symbol = 352820
case_type = content IP governance 4B
archetype = KPOP_LABEL_GOVERNANCE_4B
```

| trigger |                type | date       | 당시 공개 evidence                                                                             | 가격 anchor                        | outcome |
| ------- | ------------------: | ---------- | ------------------------------------------------------------------------------------------ | -------------------------------- | ------- |
| T0      | 4B label governance | 2024-04-24 | HYBE audits ADOR / Min Hee-jin amid NewJeans control dispute                               | HYBE nearly -8%                  |         |
| T1      |          validation | 2024       | analysts expect volatility; dispute threatens K-pop IP governance                          | 4B                               |         |
| T2      |    founder legal 4B | 2026-04-21 | police seek detention warrant for Bang Si-hyuk over IPO-related capital-market allegations | HYBE -2.4% despite market uptick |         |
| T3      |             hard 4C | N/A        | BTS/NewJeans revenue collapse not confirmed                                                | hard 4C not confirmed            |         |
| T4      |       Stage3-Yellow | N/A        | artist schedule/tour/IP monetization and governance stabilization needed                   | 보류                               |         |

HYBE는 R8에서 “content IP가 강해도 label governance가 4B가 된다”는 case다. Reuters는 HYBE가 ADOR CEO Min Hee-jin 측을 audit하면서 NewJeans label control dispute가 재점화됐고, HYBE shares가 거의 -8% 하락했다고 보도했다. 2026년에는 police가 HYBE founder Bang Si-hyuk에 대한 detention warrant를 요청했고, HYBE stock은 시장 상승에도 -2.4%였다. 다만 이건 아직 BTS/NewJeans revenue collapse가 확인된 hard 4C가 아니라, content IP governance/founder legal 4B다. ([Reuters][8])

```json
{
  "case_id": "r8_loop17_hybe_ador_bang_governance_4b",
  "symbol": "352820",
  "best_trigger": "T0/T3",
  "best_trigger_type": "4B_content_IP_label_governance_founder_legal",
  "ador_trigger_date": "2024-04-24",
  "ador_event_return_pct": "nearly_-8",
  "bang_warrant_trigger_date": "2026-04-21",
  "bang_warrant_event_return_pct": -2.4,
  "risk_items": [
    "ADOR_NewJeans_label_control",
    "artist_contract_uncertainty",
    "founder_capital_market_law_investigation",
    "IPO_related_legal_risk",
    "brand_reputation"
  ],
  "hard_4C_status": "not_confirmed",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "content_IP_governance_4B_not_4C"
}
```

---

## Case I — Kakao founder legal/regulatory risk

```text
symbol = 035720
case_type = platform governance / regulatory 4B
archetype = PLATFORM_GOVERNANCE_REGULATORY_4B
```

| trigger |          type | date       | 당시 공개 evidence                                                                         | 가격 anchor                               | outcome |
| ------- | ------------: | ---------- | -------------------------------------------------------------------------------------- | --------------------------------------- | ------- |
| T0      |      4B legal | 2024-07-23 | Kakao founder Kim Beom-su arrested over SM Entertainment stock-manipulation allegation | Kakao -3.4%, lowest since Nov, YTD -24% |         |
| T1      |    validation | 2024-07    | potential impact on AI investments, overseas expansion, KakaoBank control              | 4B                                      |         |
| T2      |        relief | 2025-10-21 | court cleared Kim of stock-manipulation charges                                        | no relief price anchor                  |         |
| T3      | Stage3-Yellow | N/A        | regulatory closure and AI/product investment recovery needed                           | 보류                                      |         |

Kakao founder legal risk는 R8 platform governance 4B다. Reuters는 Kakao founder Kim Beom-su가 SM Entertainment acquisition 과정의 stock manipulation allegation으로 체포됐고, Kakao shares가 morning trade에서 -3.4%, 11월 이후 최저였으며 YTD -24%였다고 보도했다. 또 유죄가 되면 KakaoBank control에도 영향을 줄 수 있다고 했다. 2025년 court acquittal은 relief trigger지만, price anchor가 없고 AI/product execution 회복이 필요하다. ([Reuters][9])

```json
{
  "case_id": "r8_loop17_kakao_founder_legal_governance",
  "symbol": "035720",
  "best_trigger": "T0/T2",
  "best_trigger_type": "4B_platform_governance_regulatory_risk_with_relief",
  "arrest_trigger_date": "2024-07-23",
  "event_return_pct": -3.4,
  "ytd_return_context_pct": -24,
  "risk_items": [
    "SM_Entertainment_stock_manipulation_allegation",
    "AI_investment_delay",
    "overseas_expansion_delay",
    "KakaoBank_control_risk",
    "regulatory_scrutiny"
  ],
  "relief_trigger_date": "2025-10-21",
  "relief_event": "court_cleared_Kim_Beom_su",
  "relief_price_anchor": "price_data_unavailable_after_deep_search",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "platform_governance_4B_with_relief_not_Green"
}
```

---

# 6. Trigger별 실제 가격경로 검증 요약

이번 R8 Loop 17은 full OHLC가 없으므로, 아래 표는 **reported event anchor 기준**이다.

| case                 | best trigger |                                              event return / price |      market-relative | full MFE/MAE | outcome                              |
| -------------------- | -----------: | ----------------------------------------------------------------: | -------------------: | ------------ | ------------------------------------ |
| Kakao / OpenAI       |        T1/T2 |                                            initial +9%, later -2% |         price failed | unavailable  | Stage2 AI partnership, price failed  |
| Naver sovereign AI   |        T1/T2 |                                            stock +20% YTD context | no event-window OHLC | unavailable  | Stage2 AI/cloud capex                |
| Webtoon / Naver      |        T0/T2 | Webtoon +14.3% IPO, +62% Disney/earnings; Naver -0.9% market talk |          parent weak | unavailable  | content Stage2 + holdco 4B           |
| Shift Up             |           T1 |                                  435B won IPO, 3.5T won valuation | no post-listing OHLC | unavailable  | gaming IP Stage2                     |
| Krafton / Subnautica |           T1 |                                                 price unavailable |                  N/A | unavailable  | gaming IP legal 4B                   |
| LG CNS               |           T1 |                                 61,900 issue → 59,700 debut trade |         price failed | unavailable  | SW/cloud IPO price failed            |
| SK Telecom           |        T0/T3 |                          -8.5% intraday, -6.7% close, KOSPI +0.1% |         -6.8pp close | unavailable  | hard 4C cyber breach                 |
| HYBE                 |        T0/T2 |                           nearly -8%; later -2.4% on Bang warrant |             negative | unavailable  | content governance 4B                |
| Kakao founder        |        T0/T2 |                                           -3.4%, YTD -24% context |             negative | unavailable  | platform governance 4B, relief watch |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
가장 좋은 Stage2:
1. Naver sovereign AI / Blackwell infrastructure.
2. Webtoon Entertainment content platform, especially Disney/earnings trigger.
3. Shift Up gaming IP IPO.
4. Kakao/OpenAI AI partnership, but price failed.
5. LG CNS AI/cloud IPO, but price failed.
```

## Stage2-Actionable entry 성과

```text
Stage2-Actionable 후보:
- Naver sovereign AI: GPU/capex/data-sovereignty infrastructure is concrete, but no event-window OHLC.
- Webtoon: IPO and Disney/earnings trigger showed clear WBTN price reaction.
- Shift Up: IP revenue and IPO valuation are concrete, but no post-listing price anchor.

Actionable 보류:
- Kakao/OpenAI: initial +9% but later -2% → price failed.
- LG CNS: cloud/AI sales mix good, but IPO traded below issue price.
- Krafton/Subnautica: legal risk, not positive action.
- HYBE: label/founder governance 4B.
- SK Telecom: hard 4C.
```

## Stage3-Yellow 후보

```text
Yellow 후보:
- Naver sovereign AI if enterprise/government cloud contracts and utilization are confirmed.
- Webtoon if Disney/IP partnerships convert into MAU, paid conversion, ad/revenue growth and margin.
- Shift Up if PC sales/live-service retention/sequel pipeline prove repeatability.
- Kakao/OpenAI only if KakaoTalk AI monetization and MAU/ARPU conversion appear.
- LG CNS only if external AI/cloud order backlog and margin expand after IPO.
```

## Stage3-Green

```text
이번 R8 Loop 17에서 확정 Green 없음.

이유:
- AI partnership은 product monetization 전까지 Stage2다.
- sovereign AI는 capex-heavy라 cloud utilization / contract visibility가 필요하다.
- content platform은 MAU→paid/revenue/margin conversion이 필요하다.
- gaming IP는 title concentration and legal risk가 크다.
- cybersecurity breach and governance risk가 platform valuation에 직접 4B/4C로 작동한다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- SK Telecom cyber breach as hard 4C.
- Kakao/OpenAI as Stage2 but price failed.
- Naver sovereign AI as Stage2 capex/infrastructure.
- Webtoon as content platform Stage2 with parent holdco discount.
- LG CNS as AI/cloud SW IPO price failed.
- HYBE as content IP governance 4B.
- Kakao founder legal risk as platform governance 4B.
- Krafton/Subnautica as gaming IP legal 4B.

Stage2_promote_candidate:
- Naver sovereign AI / Blackwell.
- Webtoon / Disney IP platform.
- Shift Up gaming IP.
- Kakao/OpenAI only after monetization proof.
- LG CNS only after external backlog/margin proof.

false_positive_score:
- Kakao/OpenAI promoted to Green despite later -2% price.
- LG CNS promoted to Green despite IPO price failure.
- Naver AI capex promoted without utilization/contracts.
- Webtoon IPO read through to Naver without holdco discount.
- Shift Up promoted without post-listing sales retention.
- HYBE promoted without governance risk adjustment.

evidence_good_but_price_failed:
- Kakao/OpenAI.
- LG CNS IPO.
- Samsung Bio GSK from R7 was analogous, but R8 primary case is LG CNS.

event_premium:
- Webtoon IPO / Disney deal.
- Kakao/OpenAI initial spike.
- Shift Up IPO.
- Naver AI capex/sovereign AI narrative.

thesis_break:
- SK Telecom cyber breach.

4B-watch:
- HYBE label/founder governance.
- Kakao founder/legal/regulatory risk.
- Krafton/Subnautica legal/control risk.
- Naver AI capex ROI.
- Webtoon parent holding-company discount.
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
AI_product_integration,+4,"AI partnership is Stage2 if product surface is concrete","Kakao/OpenAI"
sovereign_AI_infra,+5,"GPU procurement and sovereign AI/export cloud can become structural Stage2","Naver"
cloud_AI_capex_to_contract,+5,"AI capex must convert to government/enterprise contracts","Naver, LG CNS"
content_IP_partnership,+5,"Disney/Marvel/Star Wars-style IP partnership can accelerate platform monetization","Webtoon"
MAU_paid_conversion,+5,"content/platform Green requires MAU to revenue/margin conversion","Webtoon, Kakao"
gaming_IP_sales_retention,+5,"gaming Green requires title sales plus retention/repeat pipeline","Shift Up, Krafton"
cyber_trust_security,+5,"major breach with user/financial impact is hard 4C","SK Telecom"
governance_legal_risk,+5,"founder/legal/label disputes materially hit platform/content valuations","Kakao, HYBE, Krafton"
```

## 내릴 축

```csv
axis,delta,reason,cases
AI_partnership_without_monetization,-5,"AI partnership headline만으로 Green 금지","Kakao/OpenAI"
AI_capex_without_utilization,-5,"GPU/capex가 계약·utilization으로 안 닫히면 Green 금지","Naver"
IPO_without_aftermarket_strength,-5,"AI/cloud IPO가 issue price 아래면 Actionable 금지","LG CNS"
content_IP_without_margin,-4,"IP partnership도 margin/revenue 전에는 Green 금지","Webtoon"
parent_readthrough_without_holdco_discount,-5,"Webtoon success를 Naver로 과대 반영 금지","Naver/Webtoon"
gaming_title_without_retention,-4,"single title success만으로 Green 금지","Shift Up"
cyber_incident_ignored,-5,"breach·compensation·revenue cut 무시 금지","SK Telecom"
governance_dispute_ignored,-5,"founder/label/legal dispute 무시 금지","Kakao, HYBE, Krafton"
```

---

# 10. Stage2-Actionable 승격 조건

R8 Loop 17 shadow rule:

```text
R8에서 Stage2 evidence가 아래 중 4개 이상이면 Stage2-Actionable로 승격한다.

1. event return +5% 이상 또는 strong reported price reaction
2. AI/product/IP/launch/IPO/deal value가 명확하다
3. MAU, revenue, paid conversion, cloud utilization, game sales 중 하나가 확인된다
4. parent readthrough discount or holdco discount가 식별된다
5. legal/governance/cybersecurity 4B가 식별 가능하고 통제 가능하다
6. capex가 enterprise/government contract로 연결될 수 있다
7. price reaction이 final close 기준으로 evidence와 같은 방향이다
```

적용:

```text
Naver sovereign AI:
2,4,5,6 충족. event-window return 부족 → Stage2, Yellow 보류.

Webtoon:
1,2,3,4,5 충족 → Webtoon 자체 Stage2-Actionable. Naver readthrough는 4B.

Shift Up:
2,3 일부,5 충족. post-listing price 부족 → Stage2.

Kakao/OpenAI:
1 initial, 2 충족 but 7 실패 → price-failed Stage2.

LG CNS:
2,3 충족 but 7 실패 → Actionable 금지.

SK Telecom:
negative 4C → 승격 금지.

HYBE/Kakao governance/Krafton:
4B negative triggers → positive Stage2 승격 금지.
```

---

# 11. Stage3-Yellow 조건

```text
Stage3-Yellow:
Stage2 이후 아래 중 2개 이상이 추가로 닫히면 Yellow.

1. AI product monetization / ARPU / ad conversion
2. cloud/GPU utilization and external contract backlog
3. IP partnership converts into revenue and margin
4. game launch sales plus retention/DLC/sequel pipeline
5. cyber/governance risk contained
6. parent holding discount narrows
7. paid conversion or subscriber/user growth is recurring
```

Yellow 후보:

```text
Naver:
sovereign AI contracts + cloud utilization + capex ROI 확인 시 Yellow.

Webtoon:
Disney/IP deal revenue + paid conversion + margin 확인 시 Yellow.

Shift Up:
PC sales + live-service retention + new IP pipeline 확인 시 Yellow.

Kakao/OpenAI:
AI product MAU/ARPU/ad conversion 확인 시 Yellow.

LG CNS:
external AI/cloud order backlog + margin expansion 확인 시 Yellow.
```

---

# 12. Stage3-Green 조건

```text
Stage3-Green:
- AI partnership produces measurable monetization.
- sovereign AI capex converts into high-utilization cloud revenue.
- content platform shows MAU, paid conversion, ad/subscription revenue and margin.
- gaming IP shows title sales, retention and recurring pipeline.
- cyber/security/governance 4B is resolved.
- full-window MFE/MAE is favorable.
```

이번 R8 Loop 17에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + monetization/utilization/retention/governance/cyber gates not fully closed
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- AI partnership after initial spike closes negative.
- GPU/capex without enterprise contract.
- content IPO readthrough blocked by parent holdco discount.
- gaming studio legal/control dispute.
- IT services IPO weak debut.
- founder/legal investigation.
- label/artist governance dispute.
- cyber breach with compensation and revenue cut.
```

적용:

```text
Kakao:
OpenAI price failed + founder legal 4B.

Naver:
AI capex and Webtoon holdco discount 4B.

Webtoon:
platform success but parent readthrough 4B.

Shift Up:
title concentration 4B.

Krafton:
Subnautica legal dispute 4B.

LG CNS:
IPO price failed 4B.

SK Telecom:
cyber breach hard 4C.

HYBE:
ADOR/NewJeans and Bang legal 4B.
```

---

# 14. 4C hard gate 조건

```text
R8 4C:
- major data breach with stock drawdown, user/remediation cost and revenue guidance cut
- prolonged platform outage causing regulatory intervention and user churn
- cybersecurity failure forcing massive compensation
- content IP contract termination causing revenue collapse
- legal ruling causing material earnout/liability/release impairment with price collapse
```

이번 R8 Loop 17 hard/strong 4C:

```text
SK Telecom cyber breach = hard_4C_success
```

Hard 4C not yet confirmed:

```text
Kakao founder legal risk = 4B with relief trigger, not hard 4C.
HYBE governance = 4B, not hard 4C.
Krafton Subnautica = 4B legal, not hard 4C without stock-price/financial impairment.
Kakao/OpenAI = price-failed Stage2, not 4C.
LG CNS = IPO price failed, not 4C.
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R8 production 설계 원칙:

```text
1. AI partnership와 AI monetization을 분리한다.
2. GPU/capex와 contract/utilization을 분리한다.
3. content platform IPO와 parent-company readthrough를 분리한다.
4. game IPO/IP success와 retention/pipeline을 분리한다.
5. cyber breach는 user impact + compensation + guidance cut이 있으면 hard 4C다.
6. founder/label/studio governance risk는 platform/content score에서 선차감한다.
7. weak IPO debut은 Actionable 금지 신호다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_257.md 요약

```md
# R8 Loop 17. Platform / Content / SW / Security Trigger-level Price Validation

이번 라운드는 R8 Loop 17 trigger-level validation 라운드다.

핵심 결론:
- Kakao / OpenAI is Stage2 AI partnership but price failed. Kakao initially surged about 9% after OpenAI partnership news but later ended down 2%. Product integration is real, but monetization and regulatory overhang remain 4B.
- Naver sovereign AI / Blackwell is Stage2 cloud-infra capex. Nvidia will supply 260,000+ Blackwell chips to South Korea, Naver will buy 60,000, and FT reported Naver's 2026 AI/cloud investment at $690M with stock +20% YTD. Green requires enterprise contracts and utilization.
- Webtoon / Naver is Stage2 content platform with parent holdco discount. Webtoon rose as much as 14.3% on Nasdaq debut and later 62% after Disney/Marvel/Star Wars deal and surprise profit. Naver readthrough is weakened by holding-company discount.
- Shift Up is Stage2 gaming IP. IPO raised 435B won / $313M at a 3.5T won valuation, supported by Nikke revenue and Stellar Blade success. Full post-listing OHLC unavailable.
- Krafton / Subnautica is gaming IP governance/legal 4B. Delaware court ruled against Krafton, returned operational control to Unknown Worlds CEO and extended the $250M earnout timeline.
- LG CNS is AI/cloud SW IPO price failed. IPO raised 1.2T won / $827.1M at 61,900 won, but shares opened at 60,500 and traded at 59,700.
- SK Telecom cyber breach is hard 4C. Shares closed -6.7% after cyberattack/data breach while KOSPI rose 0.1%; later 26.96M data pieces, 700B won security investment and 800B won 2025 revenue forecast cut were disclosed.
- HYBE / ADOR and founder legal risk is content governance 4B. HYBE shares fell nearly 8% on ADOR audit dispute and later 2.4% after police sought a detention warrant for Bang Si-hyuk.
- Kakao founder legal risk is platform governance 4B. Kakao fell 3.4% after Kim Beom-su's arrest; later acquittal is relief but not Green without AI/product execution recovery.

Main calibration:
- Raise AI_product_integration, sovereign_AI_infra, cloud_AI_capex_to_contract, content_IP_partnership, MAU_paid_conversion, gaming_IP_sales_retention, cyber_trust_security, governance_legal_risk.
- Lower AI_partnership_without_monetization, AI_capex_without_utilization, IPO_without_aftermarket_strength, content_IP_without_margin, parent_readthrough_without_holdco_discount, gaming_title_without_retention, cyber_incident_ignored, governance_dispute_ignored.
```

## docs/checkpoints/checkpoint_28a_round257_r8_loop17.md 요약

```md
# Checkpoint 28A Round 257 R8 Loop 17 Trigger-level Calibration

## 반영 내용
- R8 Loop 17 trigger-level validation을 수행했다.
- Kakao/OpenAI, Naver sovereign AI/Blackwell, Webtoon/Naver, Shift Up, Krafton/Subnautica, LG CNS, SK Telecom cyber breach, HYBE governance, Kakao founder legal risk를 검토했다.
- full adjusted OHLC는 확보하지 못했으므로 Reuters / FT / WSJ / Barron’s reported event return과 event price anchor를 사용했다.
- MFE/MAE는 조작하지 않고 price_data_unavailable_after_deep_search로 분리했다.

## 핵심 보정
- AI partnership is Stage2 only until product monetization appears.
- Sovereign AI capex requires contract and utilization evidence.
- Content-platform success must be separated from parent holding-company discount.
- Game IP success needs sales retention and repeat pipeline.
- Weak IPO debut blocks Actionable classification.
- Cyber breach with user impact, compensation and guidance cut is hard 4C.
- Founder, label and studio governance risks are R8 4B overlays.
```

## data/e2r_case_library/cases_r8_loop17_round257.jsonl 초안

```jsonl
{"case_id":"r8_loop17_kakao_openai_ai_partnership","symbol":"035720","company_name":"Kakao","case_type":"Stage2_AI_platform_partnership_price_failed","primary_archetype":"AI_CHAT_PLATFORM_PARTNERSHIP_STAGE2_PRICE_FAILED","best_trigger":"T1/T3","stage_candidate":"Stage2 price-failed","price_validation":{"trigger_date":"2025-02-04","initial_event_return_pct":9,"later_event_return_pct":-2,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_AI_partnership_but_price_failed","notes":"OpenAI partnership is real, but final price reaction failed and monetization/regulatory overhang remains."}
{"case_id":"r8_loop17_naver_sovereign_ai_blackwell","symbol":"035420","company_name":"Naver","case_type":"Stage2_sovereign_AI_cloud_capex","primary_archetype":"SOVEREIGN_AI_CLOUD_INFRA_STAGE2_CAPEX_4B","best_trigger":"T1/T3","stage_candidate":"Stage2","price_validation":{"blackwell_trigger_date":"2025-10-31","south_korea_blackwell_chip_supply_count":">260000","naver_blackwell_chip_count":60000,"naver_ai_cloud_investment_2026_usd_mn":690,"reported_stock_return_ytd_context_pct":20,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_sovereign_AI_cloud_not_Green","notes":"GPU procurement and sovereign AI are structural, but contracts, utilization and capex ROI are missing."}
{"case_id":"r8_loop17_webtoon_naver_content_platform","symbol":"WBTN/035420","company_name":"Webtoon Entertainment / Naver","case_type":"Stage2_content_platform_with_parent_holdco_4B","primary_archetype":"WEBTOON_CONTENT_PLATFORM_STAGE2_HOLDCO_DISCOUNT","best_trigger":"T0/T3","stage_candidate":"Stage2 + 4B-watch","price_validation":{"ipo_date":"2024-06-27","webtoon_ipo_intraday_return_pct":14.3,"webtoon_ipo_raise_usd_mn":315,"webtoon_ipo_valuation_usd_bn":2.71,"naver_market_talk_price_krw":165300,"naver_market_talk_return_pct":-0.9,"nomura_target_cut_pct":22,"holdco_discount_pct":50,"disney_deal_event_return_pct":62,"q2_revenue_usd_mn":348.3,"q2_revenue_yoy_pct":8.5,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Webtoon_stage2_but_Naver_holdco_discount_4B","notes":"Webtoon platform has strong price triggers, but parent Naver readthrough is weakened by holdco discount."}
{"case_id":"r8_loop17_shift_up_gaming_ip_ipo","symbol":"462870","company_name":"Shift Up","case_type":"Stage2_gaming_IP_IPO_no_full_price","primary_archetype":"GAMING_IP_SUCCESS_STAGE2_WITH_LEGAL_4B","best_trigger":"T1/T3","stage_candidate":"Stage2","price_validation":{"trigger_date":"2024-06-27","ipo_raise_krw_bn":435,"ipo_raise_usd_mn":313,"ipo_valuation_krw_trn":3.5,"ipo_valuation_usd_bn":2.52,"nikke_revenue_late_2022_to_q1_2024_krw_bn":255,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_gaming_IP_no_OHLC","notes":"Gaming IP and IPO valuation are concrete, but post-listing OHLC and retention/pipeline evidence are missing."}
{"case_id":"r8_loop17_krafton_subnautica_legal_4b","symbol":"259960","company_name":"Krafton / Unknown Worlds","case_type":"4B_gaming_IP_governance_legal_dispute","primary_archetype":"GAMING_IP_SUCCESS_STAGE2_WITH_LEGAL_4B","best_trigger":"T1/T3","stage_candidate":"4B-watch","price_validation":{"trigger_date":"2026-03-16","earnout_value_usd_mn":250,"court_outcome":"Delaware_court_ruled_against_Krafton","operational_control_returned_to":"Ted_Gill","direct_price_anchor":"price_data_unavailable_after_deep_search","hard_4C_status":"not_confirmed"},"score_price_alignment":"gaming_IP_legal_4B_not_4C","notes":"Legal ruling creates studio/IP governance risk, but hard 4C requires stock-price or financial impairment confirmation."}
{"case_id":"r8_loop17_lg_cns_ai_cloud_ipo_price_failed","symbol":"064400","company_name":"LG CNS","case_type":"Stage2_IT_services_AI_cloud_IPO_price_failed","primary_archetype":"IT_SERVICES_AI_CLOUD_IPO_PRICE_FAILED","best_trigger":"T1/T3","stage_candidate":"Stage2 price-failed","price_validation":{"ipo_launch_date":"2025-01-06","ipo_price_range_krw":"53700-61900","ipo_raise_krw_trn":1.2,"ipo_raise_usd_mn":827.1,"issue_price_krw":61900,"debut_open_price_krw":60500,"debut_last_price_krw":59700,"cloud_ai_sales_share_first_3q_2024_pct":54,"first_3q_2024_revenue_krw_trn":4.0,"first_3q_2024_operating_profit_krw_bn":313,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"AI_cloud_SW_evidence_good_but_IPO_price_failed","notes":"Cloud/AI sales mix is strong, but debut below issue price blocks Actionable status."}
{"case_id":"r8_loop17_sk_telecom_cyber_breach","symbol":"017670","company_name":"SK Telecom","case_type":"hard_4C_cybersecurity_trust_break","primary_archetype":"CYBER_BREACH_HARD_4C_SECURITY_CAPEX","best_trigger":"T0/T3","stage_candidate":"4C","price_validation":{"trigger_date":"2025-04-28","intraday_event_return_pct":-8.5,"close_event_return_pct":-6.7,"kospi_same_context_pct":0.1,"affected_subscribers_context_mn":23,"leaked_data_pieces_mn":26.96,"security_investment_5yr_krw_bn":700,"august_subscription_discount_pct":50,"revenue_forecast_cut_2025_krw_bn":800,"potential_broader_compensation_krw_trn":2.3,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"hard_4C_success_cyber_breach","notes":"Cyber breach caused stock drawdown, remediation, security capex, compensation and guidance cut."}
{"case_id":"r8_loop17_hybe_ador_bang_governance_4b","symbol":"352820","company_name":"HYBE","case_type":"4B_content_IP_label_governance_founder_legal","primary_archetype":"KPOP_LABEL_GOVERNANCE_4B","best_trigger":"T0/T3","stage_candidate":"4B-watch","price_validation":{"ador_trigger_date":"2024-04-24","ador_event_return_pct":"nearly_-8","bang_warrant_trigger_date":"2026-04-21","bang_warrant_event_return_pct":-2.4,"hard_4C_status":"not_confirmed","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"content_IP_governance_4B_not_4C","notes":"Content IP remains strong, but label/founder governance risk is a material overlay."}
{"case_id":"r8_loop17_kakao_founder_legal_governance","symbol":"035720","company_name":"Kakao","case_type":"4B_platform_governance_regulatory_risk_with_relief","primary_archetype":"PLATFORM_GOVERNANCE_REGULATORY_4B","best_trigger":"T0/T2","stage_candidate":"4B-watch with relief","price_validation":{"arrest_trigger_date":"2024-07-23","event_return_pct":-3.4,"ytd_return_context_pct":-24,"relief_trigger_date":"2025-10-21","relief_event":"court_cleared_Kim_Beom_su","relief_price_anchor":"price_data_unavailable_after_deep_search","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"platform_governance_4B_with_relief_not_Green","notes":"Founder legal risk hit Kakao, but later acquittal is only relief until AI/product execution recovers."}
```

## data/e2r_trigger_calibration/triggers_r8_loop17_round257.jsonl 초안

```jsonl
{"trigger_id":"r8l17_kakao_openai_T1","case_id":"r8_loop17_kakao_openai_ai_partnership","trigger_type":"Stage2_AI_partnership","trigger_date":"2025-02-04","event_return_pct":"initial_+9_later_-2","trigger_outcome_label":"Stage2_AI_partnership_price_failed","promote_to":"Stage2_price_failed"}
{"trigger_id":"r8l17_naver_blackwell_T1","case_id":"r8_loop17_naver_sovereign_ai_blackwell","trigger_type":"Stage2_sovereign_AI_infra","trigger_date":"2025-10-31","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_sovereign_AI_cloud_capex","promote_to":"Stage2"}
{"trigger_id":"r8l17_webtoon_ipo_T0","case_id":"r8_loop17_webtoon_naver_content_platform","trigger_type":"Stage2_content_platform_IPO","trigger_date":"2024-06-27","event_return_pct":14.3,"trigger_outcome_label":"Webtoon_platform_stage2","promote_to":"Stage2"}
{"trigger_id":"r8l17_webtoon_disney_T2","case_id":"r8_loop17_webtoon_naver_content_platform","trigger_type":"Stage2_content_IP_partnership","trigger_date":"2025-08-13","event_return_pct":62,"trigger_outcome_label":"content_IP_partnership_stage2","promote_to":"Stage2-Actionable_candidate"}
{"trigger_id":"r8l17_naver_webtoon_holdco_T1","case_id":"r8_loop17_webtoon_naver_content_platform","trigger_type":"4B_parent_holdco_discount","trigger_date":"2024-06-19","event_return_pct":-0.9,"trigger_outcome_label":"parent_readthrough_holdco_4B","promote_to":"4B-watch"}
{"trigger_id":"r8l17_shiftup_ipo_T1","case_id":"r8_loop17_shift_up_gaming_ip_ipo","trigger_type":"Stage2_gaming_IP_IPO","trigger_date":"2024-06-27","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"gaming_IP_IPO_no_OHLC","promote_to":"Stage2"}
{"trigger_id":"r8l17_krafton_subnautica_T1","case_id":"r8_loop17_krafton_subnautica_legal_4b","trigger_type":"4B_gaming_IP_legal_dispute","trigger_date":"2026-03-16","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"gaming_IP_legal_4B_not_4C","promote_to":"4B-watch"}
{"trigger_id":"r8l17_lg_cns_ipo_T1","case_id":"r8_loop17_lg_cns_ai_cloud_ipo_price_failed","trigger_type":"evidence_good_but_price_failed_AI_cloud_IPO","trigger_date":"2025-02-05","event_return_pct":"issue_61900_last_59700","trigger_outcome_label":"AI_cloud_IPO_price_failed","promote_to":"no_actionable"}
{"trigger_id":"r8l17_skt_breach_T0","case_id":"r8_loop17_sk_telecom_cyber_breach","trigger_type":"hard_4C_cyber_breach","trigger_date":"2025-04-28","event_return_pct":-6.7,"market_relative_pp":-6.8,"trigger_outcome_label":"hard_4C_success_cyber_breach","promote_to":"4C"}
{"trigger_id":"r8l17_hybe_ador_T0","case_id":"r8_loop17_hybe_ador_bang_governance_4b","trigger_type":"4B_content_label_governance","trigger_date":"2024-04-24","event_return_pct":"nearly_-8","trigger_outcome_label":"content_IP_governance_4B","promote_to":"4B-watch"}
{"trigger_id":"r8l17_hybe_bang_T2","case_id":"r8_loop17_hybe_ador_bang_governance_4b","trigger_type":"4B_founder_legal_risk","trigger_date":"2026-04-21","event_return_pct":-2.4,"trigger_outcome_label":"founder_legal_4B","promote_to":"4B-watch"}
{"trigger_id":"r8l17_kakao_founder_T0","case_id":"r8_loop17_kakao_founder_legal_governance","trigger_type":"4B_platform_governance_legal","trigger_date":"2024-07-23","event_return_pct":-3.4,"trigger_outcome_label":"platform_governance_4B","promote_to":"4B-watch"}
```

## data/sector_taxonomy/score_weight_profiles_round257_r8_loop17_v1.csv 초안

```csv
archetype,AI_product_integration,sovereign_AI_infra,cloud_AI_capex_to_contract,content_IP_partnership,MAU_paid_conversion,gaming_IP_sales_retention,cyber_trust_security,governance_legal_risk,AI_partnership_without_monetization_penalty,AI_capex_without_utilization_penalty,IPO_without_aftermarket_strength_penalty,content_IP_without_margin_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
AI_CHAT_PLATFORM_PARTNERSHIP_STAGE2_PRICE_FAILED,+5,+1,+2,+0,+4,+0,+2,+4,-5,-2,-1,-1,Kakao/OpenAI initial spike then -2,monetization missing,MAU/ARPU/ad conversion,Kakao.
SOVEREIGN_AI_CLOUD_INFRA_STAGE2_CAPEX_4B,+2,+5,+5,+0,+2,+0,+2,+1,-1,-5,-1,-1,Naver 60000 Blackwell chips,contract/utilization missing,enterprise contracts+cloud utilization,Naver.
WEBTOON_CONTENT_PLATFORM_STAGE2_HOLDCO_DISCOUNT,+0,+0,+1,+5,+5,+0,+1,+1,-1,-1,-2,-4,Webtoon IPO+Disney deal strong,Naver holdco discount,paid conversion+margin+parent readthrough,Webtoon/Naver.
GAMING_IP_SUCCESS_STAGE2_WITH_LEGAL_4B,+0,+0,+0,+1,+1,+5,+1,+5,-1,-1,-2,-1,Shift Up/Krafton IP triggers,title retention/legal risk,repeat sales+pipeline+legal containment,Shift Up/Krafton.
IT_SERVICES_AI_CLOUD_IPO_PRICE_FAILED,+2,+2,+5,+0,+0,+0,+2,+1,-2,-4,-5,-1,LG CNS cloud/AI sales but IPO failed,aftermarket weak,external backlog+margin,LG CNS.
CYBER_BREACH_HARD_4C_SECURITY_CAPEX,+0,+0,+0,+0,+5,+0,+5,+3,-1,-1,-1,-1,SKT breach hard 4C,user/security/compensation impact,churn/ARPU/regulator closure,SK Telecom.
KPOP_LABEL_GOVERNANCE_4B,+0,+0,+0,+5,+2,+0,+1,+5,-1,-1,-1,-3,HYBE ADOR/founder risk,content IP governance 4B,artist schedule+governance stabilization,HYBE.
PLATFORM_GOVERNANCE_REGULATORY_4B,+3,+1,+2,+2,+3,+0,+2,+5,-3,-1,-1,-2,Kakao founder legal risk,regulatory overhang,legal closure+product execution,Kakao.
```

---

# 이번 R8 Loop 17 결론

```text
1. Kakao/OpenAI는 Stage2 AI partnership이지만 price failed다.
   +9% initial spike 후 -2%로 끝났기 때문에 Green 금지다.

2. Naver sovereign AI는 Stage2 cloud/AI infra다.
   60,000 Blackwell chips, $690M AI/cloud 투자, stock +20% YTD context는 좋지만, contract/utilization이 필요하다.

3. Webtoon은 content platform Stage2다.
   IPO +14.3%, Disney/earnings +62%는 강하지만 Naver parent readthrough는 holdco discount 4B다.

4. Shift Up은 gaming IP Stage2다.
   435B won IPO와 Nikke/Stellar Blade IP는 좋지만 post-listing OHLC와 retention data가 없다.

5. Krafton/Subnautica는 gaming IP legal 4B다.
   $250M earnout/control dispute는 pipeline risk지만 hard 4C price anchor는 없다.

6. LG CNS는 AI/cloud SW evidence good but IPO price failed다.
   61,900원 issue price 대비 59,700원 거래는 Actionable 금지 신호다.

7. SK Telecom cyber breach는 hard 4C다.
   -6.7% close, KOSPI +0.1%, 26.96M data pieces, 700B won security capex, 800B won revenue forecast cut이 같이 닫혔다.

8. HYBE는 content IP governance 4B다.
   ADOR dispute -8%, Bang warrant -2.4%로 content valuation에 governance discount가 붙는다.

9. Kakao founder legal risk는 platform governance 4B다.
   -3.4% trigger 후 2025 acquittal relief는 있지만, AI/product monetization 회복 전에는 Green이 아니다.
```

한 문장으로 압축하면:

> **R8 Loop 17에서 배운 핵심은 “AI·콘텐츠·게임·보안 headline”이 아니라, MAU/ARPU, paid conversion, cloud utilization, IP revenue, game retention, cybersecurity trust, governance/legal overhang이 닫혀야 Stage3로 올릴 수 있다는 것이다. AI partnership이나 IPO가 있어도 가격이 실패하면 Actionable 금지이고, breach가 user·보상·매출가이던스까지 깨면 hard 4C다.**

다음 순서는 **R9 Loop 17 — 모빌리티·운송·레저**다.

[1]: https://www.reuters.com/technology/artificial-intelligence/openai-kakao-jointly-develop-ai-products-south-korea-2025-02-04/ "https://www.reuters.com/technology/artificial-intelligence/openai-kakao-jointly-develop-ai-products-south-korea-2025-02-04/"
[2]: https://www.reuters.com/business/media-telecom/nvidia-supply-more-than-260000-blackwell-ai-chips-south-korea-2025-10-31/ "https://www.reuters.com/business/media-telecom/nvidia-supply-more-than-260000-blackwell-ai-chips-south-korea-2025-10-31/"
[3]: https://www.reuters.com/markets/us/webtoons-nasdaq-debut-sees-shares-jump-14-2024-06-27/ "https://www.reuters.com/markets/us/webtoons-nasdaq-debut-sees-shares-jump-14-2024-06-27/"
[4]: https://www.reuters.com/markets/deals/tencent-backed-shift-up-may-price-ipo-top-end-band-source-says-2024-06-27/ "https://www.reuters.com/markets/deals/tencent-backed-shift-up-may-price-ipo-top-end-band-source-says-2024-06-27/"
[5]: https://www.reuters.com/legal/litigation/us-court-rules-against-s-korean-gaming-company-its-ai-hatched-takeover-plan-2026-03-16/ "https://www.reuters.com/legal/litigation/us-court-rules-against-s-korean-gaming-company-its-ai-hatched-takeover-plan-2026-03-16/"
[6]: https://www.reuters.com/technology/skorean-tech-services-firm-lg-cns-falls-stock-market-debut-2025-02-05/ "https://www.reuters.com/technology/skorean-tech-services-firm-lg-cns-falls-stock-market-debut-2025-02-05/"
[7]: https://www.reuters.com/sustainability/boards-policy-regulation/sk-telecom-shares-plunge-after-data-breach-due-cyberattack-2025-04-28/ "https://www.reuters.com/sustainability/boards-policy-regulation/sk-telecom-shares-plunge-after-data-breach-due-cyberattack-2025-04-28/"
[8]: https://www.reuters.com/lifestyle/record-giant-hybe-audits-newjeans-label-infighting-returns-k-pop-2024-04-24/ "https://www.reuters.com/lifestyle/record-giant-hybe-audits-newjeans-label-infighting-returns-k-pop-2024-04-24/"
[9]: https://www.reuters.com/technology/south-korean-court-approves-arrest-warrant-kakao-founder-2024-07-22/ "https://www.reuters.com/technology/south-korean-court-approves-arrest-warrant-kakao-founder-2024-07-22/"
