순서상 이번은 **R8 Loop 14 — 플랫폼·콘텐츠·SW·보안 가격경로 검증 라운드**다.

```text
round = R8 Loop 14
round_id = round_218
large_sector = PLATFORM_CONTENT_SOFTWARE_SECURITY
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
direct_KRX_hard_4c_confirmed = true_for_SK_Telecom_security_reference
next_round = R9 Loop 14
```

이번 R8은 **Naver/Webtoon, Kakao, HYBE/NewJeans, Shift Up, NCSoft, LG CNS, Douzone Bizon, SK Telecom 보안사고**를 본다. R8의 핵심은 “플랫폼 MAU”, “AI/cloud”, “K-content”, “IPO”, “게임 IP”, “보안 수혜” 같은 단어가 아니라, **트래픽·구독·IP 매출·신작 성과·aftermarket demand·규제/거버넌스·보안 신뢰가 실제 주가와 손익으로 닫혔는지**다.

이번에도 KRX/Naver/Yahoo/Stooq 기준의 **수정주가 일봉 OHLC 전체 window**는 안정적으로 확보하지 못했다. 따라서 30D/90D/180D/1Y full MFE·MAE는 임의 생성하지 않고, Reuters/WSJ/MarketWatch/FT가 보도한 **event return, event price, IPO price, 매출·영업이익, deal value, MAU, data-breach 비용**을 가격 anchor로 사용한다. full OHLC가 필요한 칸은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R8 = 플랫폼·콘텐츠·SW·보안
```

R8에서 진짜 Stage 3는 아래가 숫자로 닫힐 때다.

```text
플랫폼:
MAU/traffic → paid conversion → ARPU/take-rate → ad/commerce growth → margin → retention

콘텐츠:
IP hit → recurring revenue → global distribution → artist/creator contract stability → margin

게임:
hit title → live-service retention → monetization → global platform expansion → next title pipeline

SW/cloud:
AI/cloud keyword → recurring enterprise revenue → backlog → operating margin → customer retention

보안:
incident prevention / trust → contract win → ARR / managed service revenue → breach-risk avoidance
```

---

# 2. 대상 canonical archetype

```text
WEBTOON_PLATFORM_IPO_AFTERMARKET_GATE
KAKAO_PLATFORM_GOVERNANCE_4C_WATCH
KPOP_IP_CONTRACT_GOVERNANCE_4C
GAME_IP_IPO_STAGE2_QUALITY_GATE
LEGACY_GAME_TURNAROUND_BUYBACK_4B
AI_CLOUD_IT_SERVICE_IPO_FALSE_POSITIVE
ENTERPRISE_SOFTWARE_PE_CONTROL_STAGE2
CYBERSECURITY_TRUST_HARD_4C_REFERENCE
```

---

# 3. deep sub-archetype

```text
Naver / Webtoon:
- Webtoon IPO
- Naver parent holdco discount
- IPO pop vs post-IPO share decline
- Disney/IP partnership rebound
- IP-adaptation revenue volatility

Kakao:
- founder legal risk
- SM acquisition stock-manipulation charge
- platform governance and bank/control read-through
- AI/international expansion overhang

HYBE:
- ADOR/NewJeans dispute
- artist/IP concentration
- multi-label governance
- content-rights continuity and contract trust

Gaming:
- Shift Up IPO / Nikke / Stellar Blade
- Tencent/Sony exposure
- NCSoft earnings beat + buyback
- new-title pipeline vs legacy-game decline

SW/cloud:
- LG CNS IPO
- cloud/AI revenue mix
- weak debut despite good fundamentals
- M&A-use-of-proceeds gate

Enterprise software:
- Douzone Bizon / ERP / cloud software
- EQT 37.6% stake
- PE control premium vs regulatory approval and recurring revenue

Security:
- SK Telecom data breach
- USIM data leak
- revenue forecast cut / fine / customer compensation / data-protection capex
- security vendor read-through is not automatic Green
```

---

# 4. 국장 신규 후보 case

## Case A — Naver / Webtoon Entertainment IPO `platform IPO + aftermarket gate`

```text
symbol = 035420 / WBTN read-through
case_type = event_premium + evidence_good_but_aftermarket_failed
archetype = WEBTOON_PLATFORM_IPO_AFTERMARKET_GATE
```

### stage date

```text
Stage 1:
2024-05-31
- Webtoon files for U.S. IPO.
- Q1 2024 net income: $6.2M.
- Q1 2024 revenue: $326.7M.
- 170M monthly active users.
- Naver-backed global webtoon platform becomes public-market asset.

Stage 2:
2024-06-27
- Webtoon IPO prices at top of range.
- IPO price: $21.
- raised $315M.
- Nasdaq debut: shares jump 14.3%.
- opened at $21.30, hit high of $24.
- valuation around $2.71B.

Stage 4B / parent discount watch:
2024-06-19
- Nomura applied 50% holding-company discount to Naver’s Webtoon stake.
- Naver target cut 22% to 210,000 won.
- Naver shares -0.9% to 165,300 won.
- parent-platform valuation boost weaker than IPO headline.

Stage 4C-watch / aftermarket validation:
2025-08-13 and 2026-05-11
- Webtoon had fallen 55% from IPO before Disney/earnings rebound.
- then +62% to $15.16 after Disney deal and surprise profit.
- later Q1 2026 revenue slipped 1.5% to $320.9M.
- Q2 2026 revenue guide $332M~$342M below $348M consensus.
- shares -15% after hours to $11.24.
```

Webtoon은 “플랫폼 IPO가 떴다”만으로 Stage 3를 줄 수 없다는 좋은 R8 case다. IPO 당일에는 +14.3%로 강했지만, Naver parent 관점에서는 holding-company discount와 commerce GMV slowdown 때문에 target cut과 주가 -0.9%가 동시에 나왔다. 이후 Webtoon은 Disney deal과 surprise profit로 +62% 반등했지만, 2026년에는 IP adaptations business 둔화와 낮은 revenue guide로 after-hours -15%를 맞았다. 즉 Webtoon은 **Stage 2 platform asset**이고, Green은 MAU가 아니라 paid conversion, IP adaptation 매출 안정성, creator economics, parent value capture가 닫혀야 한다. ([Reuters][1])

### 실제 가격경로 검증

```json
{
  "case_id": "r8_loop14_naver_webtoon_ipo_aftermarket_gate",
  "symbol": "035420/WBTN",
  "stage1_date": "2024-05-31",
  "stage2_date": "2024-06-27",
  "stage4b_date": "2024-06-27",
  "stage4c_watch_date": "2025-08-13/2026-05-11",
  "stage3_price": null,
  "price_data_source": "Reuters / MarketWatch / Barron's / WSJ event anchors",
  "webtoon_ipo_price_usd": 21,
  "webtoon_open_price_usd": 21.30,
  "webtoon_debut_high_usd": 24.00,
  "webtoon_debut_mfe_pct": 14.3,
  "ipo_raise_usd_mn": 315,
  "ipo_valuation_usd_bn": 2.71,
  "q1_2024_revenue_usd_mn": 326.7,
  "q1_2024_net_income_usd_mn": 6.2,
  "monthly_active_users_mn": 170,
  "naver_event_price_krw": 165300,
  "naver_event_mae_pct": -0.9,
  "naver_target_price_krw": 210000,
  "naver_target_cut_pct": -22,
  "holding_company_discount_applied_pct": 50,
  "post_ipo_decline_before_disney_pct": -55,
  "disney_earnings_rebound_mfe_pct": 62,
  "disney_rebound_price_usd": 15.16,
  "q2_2025_revenue_usd_mn": 348.3,
  "q2_2025_revenue_growth_pct": 8.5,
  "q1_2026_revenue_usd_mn": 320.9,
  "q1_2026_revenue_decline_pct": -1.5,
  "q2_2026_guidance_usd_mn": "332-342",
  "q2_2026_consensus_usd_mn": 348,
  "q1_2026_after_hours_mae_pct": -15,
  "q1_2026_after_hours_price_usd": 11.24,
  "mfe_30d_90d_180d_1y": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_then_aftermarket_gate
rerating_result = WEBTOON_PLATFORM_IPO_STAGE2
stage_failure_type = IPO_pop_MAU_not_parent_value_capture_green
```

---

## Case B — Kakao / SM stock-manipulation case `platform governance 4C-watch`

```text
symbol = 035720 / 041510 read-through
case_type = thesis_break_watch_then_relief
archetype = KAKAO_PLATFORM_GOVERNANCE_4C_WATCH
```

### stage date

```text
Stage 1:
2023-02~2024-07
- Kakao’s SM Entertainment acquisition becomes platform/content governance issue.
- allegations of stock manipulation during bidding war with HYBE.

Stage 4C-watch:
2024-07-23
- Kakao founder Kim Beom-su arrested.
- allegation: manipulation of SM Entertainment stock price to block HYBE acquisition.
- Kakao shares -3.4%.
- Kakao had fallen 24% YTD.
- Kim/affiliates control 24% Kakao stake.
- Kakao group assets context: 86T won.
- case could hurt AI investment, international expansion, and KakaoBank control.

Stage 4C-watch 강화:
2025-08-29
- prosecutors seek 15-year jail term and 500M won fine.

Stage 2 relief:
2025-10-21
- later acquittal relief reported.
```

Kakao는 R8 platform에서 “MAU와 messenger moat”보다 governance가 먼저라는 case다. KakaoTalk 같은 국민 플랫폼도 창업자·인수전·금융규제 리스크가 붙으면 AI 투자, 해외 확장, KakaoBank control까지 같이 흔들린다. 체포 뉴스에 Kakao는 -3.4%였고, 이미 YTD -24%였다는 점이 가격경로의 힌트다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "case_id": "r8_loop14_kakao_platform_governance_sm_case",
  "symbol": "035720/041510_readthrough",
  "stage4c_watch_date": "2024-07-23",
  "stage2_relief_date": "2025-10-21",
  "stage3_price": null,
  "price_data_source": "Reuters Kakao founder arrest and prosecution anchors",
  "kakao_event_mae_pct": -3.4,
  "kakao_ytd_decline_context_pct": -24,
  "founder_affiliated_stake_pct": 24,
  "group_assets_krw_trn": 86,
  "prosecutor_sought_sentence_years": 15,
  "prosecutor_sought_fine_krw_mn": 500,
  "risk_channels": ["AI investment", "international expansion", "KakaoBank control", "SM content governance"],
  "sm_stock_manipulation_allegation": true,
  "direct_sm_event_price": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break_watch_then_relief
rerating_result = PLATFORM_GOVERNANCE_4C_WATCH
stage_failure_type = user_base_not_green_without_founder_legal_regulatory_clearance
```

---

## Case C — HYBE / ADOR / NewJeans `content IP governance 4C-watch`

```text
symbol = 352820
case_type = 4C-watch
archetype = KPOP_IP_CONTRACT_GOVERNANCE_4C
```

### stage date

```text
Stage 1:
2024-04-22
- HYBE audits ADOR and Min Hee-jin.
- suspicion: attempt to gain independence/control of label and artists.
- NewJeans IP becomes governance and artist-contract risk.

Stage 4C-watch:
2024-04-24
- HYBE shares drop nearly 8%.
- dispute exposes multi-label governance risk.
- NewJeans is a key growth artist/IP asset.
- analysts expect continued volatility.

Stage 4C-watch persistence:
2024-11~2025
- NewJeans contract dispute escalates into court battle and hiatus context.
- group/label dispute shows content-company revenue durability depends on artist-contract stability, not only fandom.
```

HYBE는 R8 콘텐츠 sector의 핵심 4C-watch다. K-pop company는 album sales나 streaming traffic만 보는 게 아니라, **artist contract, label governance, IP continuity**가 매출의 뿌리다. Reuters는 HYBE가 ADOR를 감사하며 분쟁이 재점화됐고, HYBE shares가 거의 8% 하락했다고 보도했다. ([Reuters][3])

### 실제 가격경로 검증

```json
{
  "case_id": "r8_loop14_hybe_ador_newjeans_ip_governance",
  "symbol": "352820",
  "stage4c_watch_date": "2024-04-24",
  "stage3_price": null,
  "price_data_source": "Reuters HYBE/ADOR audit and share reaction anchor",
  "event_mae_pct": -8.0,
  "dispute_parties": ["HYBE", "ADOR", "Min Hee-jin", "NewJeans"],
  "risk_type": ["artist_contract_continuity", "multi_label_governance", "content_IP_dependency"],
  "newjeans_contract_dispute_persistence": true,
  "direct_adjusted_ohlc": "price_data_unavailable_after_deep_search",
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = KPOP_IP_CONTRACT_GOVERNANCE_GATE
stage_failure_type = fandom_and_artist_IP_not_green_without_contract_stability
```

---

## Case D — Shift Up / Nikke·Stellar Blade IPO `game IP Stage 2 + IPO quality gate`

```text
symbol = 462870
case_type = success_candidate + IPO_quality_gate
archetype = GAME_IP_IPO_STAGE2_QUALITY_GATE
```

### stage date

```text
Stage 1:
2024-04~2024-06
- Stellar Blade launches successfully on PS5.
- Goddess of Victory: Nikke continues monetization.
- Korean game IP studio becomes KOSPI IPO candidate.

Stage 2:
2024-06-27 / 2024-07
- Shift Up expected to price IPO at top end.
- IPO raise: 435B won / $313M.
- valuation: 3.5T won / $2.52B.
- Tencent stake expected to fall from 40% to about 35%.
- Nikke booked 255B won sales between global launch and Q1 2024.
- 2023 revenue: 169B won.
- 2023 OP: 111B won.
- Stellar Blade hit No.1 Japan PS download ranking and No.2 North America.

Stage 3:
없음
- hit IP and IPO are Stage 2.
- Green requires live-service retention, PC/console sell-through, recurring monetization, next-title pipeline, post-IPO demand.
```

Shift Up은 R8의 좋은 game-IP Stage 2다. Reuters는 IPO가 top-end pricing으로 435B won을 조달할 수 있고, valuation은 3.5T won, Nikke sales는 255B won, 2023 OP는 111B won이라고 보도했다. 하지만 이 정도 수치도 곧바로 Stage 3는 아니다. 게임주는 **히트작 하나 → 반복 매출 → retention → 다음 작품 pipeline → post-IPO valuation**까지 확인해야 한다. ([Reuters][4])

### 실제 가격경로 검증

```json
{
  "case_id": "r8_loop14_shift_up_game_ip_ipo_quality_gate",
  "symbol": "462870",
  "stage2_date": "2024-06-27/2024-07",
  "stage3_price": null,
  "price_data_source": "Reuters Shift Up IPO and game-IP anchor",
  "ipo_raise_krw_bn": 435,
  "ipo_raise_usd_mn": 313,
  "valuation_krw_trn": 3.5,
  "valuation_usd_bn": 2.52,
  "tencent_stake_before_pct": 40,
  "tencent_stake_after_expected_pct": 35,
  "nikke_sales_krw_bn_to_q1_2024": 255,
  "revenue_2023_krw_bn": 169,
  "op_2023_krw_bn": 111,
  "op_margin_2023_pct": 65.7,
  "stellar_blade_download_ranking": {
    "Japan_PS": 1,
    "North_America_PS": 2
  },
  "post_ipo_adjusted_ohlc": "price_data_unavailable_after_deep_search",
  "stage3_conditions": ["live_service_retention", "global_sellthrough", "recurring_monetization", "next_title_pipeline", "post_ipo_demand"]
}
```

### alignment

```text
score_price_alignment = success_candidate_IPO_quality_gate
rerating_result = GAME_IP_IPO_STAGE2
stage_failure_type = hit_IP_and_IPO_not_recurring_revenue_green
```

---

## Case E — NCSoft / Q1 beat + buyback `legacy game turnaround 4B-watch`

```text
symbol = 036570
case_type = event_premium + 4B-watch
archetype = LEGACY_GAME_TURNAROUND_BUYBACK_4B
```

### stage date

```text
Stage 1:
2024-05
- NCSoft reports Q1 earnings beat.
- legacy-game publisher attempts turnaround through new titles and buyback.

Stage 2:
2024-05
- shares surge up to 14%.
- Q1 net profit: 57.12B won.
- net profit down about 50% YoY but far above analyst forecasts around 25B~26B won.
- company announces plan to repurchase 533,417 shares.
- treasury shares around 10% of total.
- new title pipeline: Battle Crush, Project BSS, LLL, Throne and Liberty global expansion.

Stage 4B:
- earnings beat + buyback can rerate stock before game pipeline retention and monetization are proven.
```

NCSoft는 R8의 turnaround event premium이다. WSJ는 Q1 net profit이 YoY로는 약 50% 줄었지만 consensus를 크게 웃돌고, 533,417 shares buyback plan까지 나오며 주가가 장중 +14% 올랐다고 보도했다. 이 case는 “buyback + earnings beat”가 Stage 2 catalyst지만, Green은 **신작 retention, 글로벌 흥행, monetization, legacy decline stabilization**이 필요하다는 row다. ([월스트리트저널][5])

### 실제 가격경로 검증

```json
{
  "case_id": "r8_loop14_ncsoft_earnings_buyback_turnaround",
  "symbol": "036570",
  "stage2_date": "2024-05",
  "stage4b_date": "2024-05",
  "stage3_price": null,
  "price_data_source": "WSJ NCSoft Q1 earnings beat / buyback event anchor",
  "event_mfe_pct": 14.0,
  "q1_net_profit_krw_bn": 57.12,
  "net_profit_yoy_change_pct": -50,
  "analyst_forecast_low_krw_bn": 24.99,
  "analyst_forecast_high_krw_bn": 26,
  "buyback_shares": 533417,
  "treasury_share_ratio_context_pct": 10,
  "new_title_pipeline": ["Battle Crush", "Project BSS", "LLL", "Throne and Liberty global expansion"],
  "new_title_retention_confirmed": false,
  "global_monetization_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_4B_watch
rerating_result = LEGACY_GAME_TURNAROUND_STAGE2
stage_failure_type = buyback_earnings_beat_not_new_title_retention_green
```

---

## Case F — LG CNS / AI·cloud IPO `AI/cloud false positive`

```text
symbol = 064400
case_type = evidence_good_but_price_failed
archetype = AI_CLOUD_IT_SERVICE_IPO_FALSE_POSITIVE
```

### stage date

```text
Stage 1:
2025-01~2025-02
- LG CNS IPO becomes Korea AI/cloud IT service listing test.
- AI/cloud services make up more than half of sales.

Stage 2:
2025-02-05
- IPO price: 61,900 won.
- opening price: 60,500 won.
- morning trading price: 59,700 won.
- IPO raised 1.2T won / $827.1M.
- retail oversubscription nearly 123x.
- institutional bids worth 76T won.
- cloud and AI services accounted for over half of sales in first three quarters of 2024.
- 9M 2024 revenue around 4T won.
- 9M OP: 313B won.

Stage 3:
없음
- AI/cloud mix was real, but aftermarket price failed.
```

LG CNS는 R8 software에서 가장 중요한 false-positive case다. Reuters는 LG CNS의 cloud/AI services가 2024년 1~3분기 매출의 절반 이상을 차지했고, IPO도 1.2T won 규모였으며 retail oversubscription이 123배였다고 보도했다. 그런데 상장 첫날 공모가 61,900원 아래인 59,700원에 거래됐다. 즉 **AI/cloud keyword와 oversubscription은 Stage 3가 아니다.** ([Reuters][6])

### 실제 가격경로 검증

```json
{
  "case_id": "r8_loop14_lg_cns_ai_cloud_ipo_false_positive",
  "symbol": "064400",
  "stage2_date": "2025-02-05",
  "stage3_price": null,
  "price_data_source": "Reuters LG CNS IPO/debut anchor",
  "ipo_price_krw": 61900,
  "open_price_krw": 60500,
  "morning_trading_price_krw": 59700,
  "debut_mae_vs_ipo_pct": -3.23,
  "ipo_raise_krw_trn": 1.2,
  "ipo_raise_usd_mn": 827.1,
  "retail_oversubscription_multiple": 123,
  "institutional_bids_krw_trn": 76,
  "cloud_ai_sales_share_9m2024_pct": 54,
  "revenue_9m2024_krw_trn": 4.0,
  "op_9m2024_krw_bn": 313,
  "op_margin_9m2024_pct": 7.8,
  "aftermarket_demand_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed
rerating_result = AI_CLOUD_IT_SERVICE_IPO_QUALITY_GATE
stage_failure_type = AI_cloud_sales_mix_not_aftermarket_green
```

---

## Case G — Douzone Bizon / EQT enterprise software stake `enterprise SW Stage 2`

```text
symbol = 012510
case_type = success_candidate + regulatory/control watch
archetype = ENTERPRISE_SOFTWARE_PE_CONTROL_STAGE2
```

### stage date

```text
Stage 1:
2025-11-07
- EQT enters South Korean enterprise software market through Douzone Bizon.
- ERP/cloud accounting/tax/compliance software becomes PE-control asset.

Stage 2:
2025-11-07
- EQT to invest about $930M.
- buys 37.6% stake in Douzone Bizon.
- stake includes 23.2% from chairman Young-woo Kim and 14.4% from Shinhan Financial affiliates.
- Douzone provides cloud ERP and business software for SMEs.
- deal subject to KFTC merger clearance and licensing authorization from Ministry of Trade, Industry and Resources.

Stage 3:
없음
- PE control premium is Stage 2.
- Green requires ARR/retention, cloud migration, margin expansion, cross-sell, regulatory approval, governance stability.
```

Douzone Bizon은 R8 enterprise software의 좋은 success_candidate다. Reuters는 EQT가 Douzone Bizon 지분 37.6%를 약 $930M에 인수한다고 보도했다. Douzone은 SME accounting, tax, compliance ERP/cloud software를 제공한다. 하지만 이것은 control premium Stage 2다. SaaS/ERP Green은 **ARR, retention, cloud migration, operating margin, regulatory approval**로 닫혀야 한다. ([Reuters][7])

### 실제 가격경로 검증

```json
{
  "case_id": "r8_loop14_douzone_bizon_eqt_enterprise_sw_stage2",
  "symbol": "012510",
  "stage2_date": "2025-11-07",
  "stage3_price": null,
  "price_data_source": "Reuters EQT-Douzone Bizon stake anchor",
  "eqt_investment_usd_mn": 930,
  "stake_acquired_pct": 37.6,
  "chairman_stake_sold_pct": 23.2,
  "shinhan_affiliate_stake_sold_pct": 14.4,
  "business_model": ["ERP", "accounting", "tax", "compliance", "cloud-based SME software"],
  "regulatory_approvals_required": ["KFTC merger clearance", "Ministry of Trade licensing authorization"],
  "arr_retention_confirmed": false,
  "cloud_margin_confirmed": false,
  "direct_event_return": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_but_price_data_unavailable
rerating_result = ENTERPRISE_SOFTWARE_PE_CONTROL_STAGE2
stage_failure_type = PE_control_premium_not_ARR_margin_green
```

---

## Case H — SK Telecom data breach `cybersecurity hard 4C reference`

```text
symbol = 017670
case_type = hard_4C_reference
archetype = CYBERSECURITY_TRUST_HARD_4C_REFERENCE
```

### stage date

```text
Stage 1:
2025-04-18
- SK Telecom detects malware-linked customer-data leak.
- USIM identity and telecom trust become explicit risk.

Stage 4C:
2025-04-28
- shares fall as much as -8.5%.
- close -6.7%.
- KOSPI +0.1%.
- 23M users offered free USIM replacement.
- more than 2,600 retail stores used.
- 5.54M users signed up for USIM Protection Service.

Stage 4C validation:
2025-07-04
- 26.96M pieces of data leaked.
- shares close -5.6%.
- data-protection investment: 700B won over five years.
- 50% August bill discount for 24M customers.
- 2025 revenue forecast cut by 800B won.
- customer benefit package cost about 500B won.

Stage 4C financial penalty:
2025-08-28
- PIPC fine about 134B won / $96.53M.
```

SK Telecom은 R8 보안 sector의 hard reference다. 보안사고는 단순 “보안주 수혜”가 아니라, 고객 신뢰·매출전망·보상비용·과징금을 한 번에 건드린다. Reuters는 첫 disclosure 이후 SKT가 장중 -8.5%, 종가 -6.7%였고 KOSPI는 +0.1%였다고 보도했다. 이후 정부조사에서는 26.96M pieces of data leak, 700B won security investment, 800B won revenue forecast cut, 500B won compensation package, 134B won fine이 붙었다. ([Reuters][8])

### 실제 가격경로 검증

```json
{
  "case_id": "r8_loop14_sk_telecom_cybersecurity_trust_hard_4c",
  "symbol": "017670",
  "stage4c_date": "2025-04-28/2025-07-04/2025-08-28",
  "stage3_price": null,
  "price_data_source": "Reuters SK Telecom data-breach event, investigation and fine anchors",
  "initial_intraday_mae_pct": -8.5,
  "initial_close_mae_pct": -6.7,
  "kospi_same_context_pct": 0.1,
  "relative_underperformance_initial_pp": -6.8,
  "free_usim_replacement_users_mn": 23,
  "retail_stores_involved": 2600,
  "usim_protection_service_signups_mn": 5.54,
  "leaked_data_pieces_mn": 26.96,
  "july_event_close_mae_pct": -5.6,
  "data_protection_investment_krw_bn": 700,
  "revenue_forecast_cut_krw_bn": 800,
  "customer_benefit_package_cost_krw_bn": 500,
  "pipc_fine_krw_bn": 134,
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = CYBERSECURITY_TRUST_HARD_4C_REFERENCE
stage_failure_type = data_trust_internal_control_break
```

---

# 5. 이번 R8 case별 stage date 요약

| case          | Stage 1               | Stage 2               | Stage 3 | Stage 4B            | Stage 4C                        |
| ------------- | --------------------- | --------------------- | ------- | ------------------- | ------------------------------- |
| Naver/Webtoon | 2024-05 IPO filing    | 2024-06 IPO           | N/A     | IPO pop             | 2026 weak guide / IP volatility |
| Kakao         | 2023~2024 SM case     | 2025 acquittal relief | N/A     | N/A                 | 2024 arrest/legal risk          |
| HYBE          | 2024-04 ADOR audit    | N/A                   | N/A     | N/A                 | NewJeans/IP governance watch    |
| Shift Up      | 2024-04~06 IP/IPO     | 2024-06~07 IPO        | N/A     | IPO valuation watch | pipeline/retention watch        |
| NCSoft        | 2024-05 earnings beat | buyback/new titles    | N/A     | +14% event          | legacy decline/new-title risk   |
| LG CNS        | 2025-02 IPO           | 2025-02 debut         | N/A     | AI/cloud IPO demand | weak debut                      |
| Douzone Bizon | 2025-11 EQT deal      | 37.6% PE stake        | N/A     | control premium     | regulatory/ARR gate             |
| SK Telecom    | 2025-04 breach        | remediation           | N/A     | N/A                 | hard security reference         |

---

# 6. 실제 가격경로 검증 총괄

| case          |                                      가격·사업 anchor | 해석                           | 판정                               |
| ------------- | ------------------------------------------------: | ---------------------------- | -------------------------------- |
| Naver/Webtoon | WBTN +14.3% debut, later -55%, +62%, then -15% AH | platform IPO volatility      | event_premium / aftermarket gate |
| Kakao         |                   -3.4%, YTD -24%, founder arrest | platform governance 4C-watch | thesis_break_watch               |
| HYBE          |                                        nearly -8% | artist/IP governance risk    | thesis_break_watch               |
| Shift Up      |         435B won IPO, 3.5T won value, OP 111B won | game-IP Stage 2              | success_candidate                |
| NCSoft        | +14%, buyback 533,417 shares, net profit -50% YoY | turnaround event, not Green  | 4B-watch                         |
| LG CNS        |                61,900 → 59,700 won, -3.23% vs IPO | AI/cloud false positive      | evidence_good_but_price_failed   |
| Douzone Bizon |                             $930M for 37.6% stake | enterprise SW Stage 2        | success_candidate                |
| SK Telecom    |                      -8.5% / -6.7%, 134B won fine | data-trust hard 4C           | thesis_break                     |

---

# 7. score-price alignment 판정

```text
aligned:
- 없음. R8은 대부분 platform/content/SW evidence가 Stage 2 또는 4B/4C gate에 머무름.

structural_success_candidate:
- Shift Up, if live-service retention and next-title pipeline confirm.
- Douzone Bizon, if ARR/retention/cloud margin improves after EQT investment.
- Webtoon, if paid conversion, IP adaptation revenue and parent value capture stabilize.

success_candidate:
- Naver/Webtoon.
- Shift Up.
- Douzone Bizon.
- NCSoft turnaround, but only if new-title retention confirms.

evidence_good_but_price_failed:
- LG CNS.
- Naver parent/Webtoon IPO valuation boost.
- Samsung Biologics-like pattern repeated in platform/SW: good asset but market demands monetization proof.

event_premium:
- Webtoon IPO debut +14.3%.
- NCSoft earnings beat/buyback +14%.
- Shift Up IPO pricing / game-IP premium.
- Douzone/EQT control premium.

price_moved_without_evidence:
- Webtoon IPO pop before post-IPO revenue/IP stability.
- NCSoft buyback rally before new-title retention.
- Shift Up IPO valuation before repeat monetization.
- Douzone PE stake before ARR/margin proof.

thesis_break_watch:
- Kakao founder legal/governance risk.
- HYBE ADOR/NewJeans artist-contract risk.
- Webtoon weak revenue guidance / IP adaptation decline.

thesis_break:
- SK Telecom data-breach hard reference.

hard_4C_confirmed:
- SK Telecom cybersecurity/data-trust break.
```

---

# 8. 점수비중 교정

## 올릴 축

```text
paid_conversion_ARPU +5
retention_and_repeat_usage +5
IP_revenue_stability +5
artist_contract_continuity +5
game_live_service_retention +5
new_title_pipeline_execution +5
cloud_AI_recurring_revenue +5
ARR_retention_enterprise_SW +5
data_trust_internal_control +5
regulatory_governance_clearance +5
```

### 왜 올리나

Webtoon은 170M MAU와 IPO pop이 있어도 post-IPO revenue guide가 약해지면 다시 깨진다. HYBE는 fandom이 강해도 artist-contract trust가 흔들리면 주가가 바로 맞는다. LG CNS는 cloud/AI 매출비중이 높아도 공모가를 지키지 못했다. SK Telecom은 데이터 신뢰가 매출전망, 보상비용, 과징금으로 직접 내려왔다. R8에서 플랫폼의 해자는 “사용자 수”가 아니라 **반복 사용 → 유료화 → 신뢰 → 마진**이다.

## 내릴 축

```text
MAU_headline_only -5
IPO_pop_only -5
AI_cloud_keyword_only -5
creator_IP_optional_value_only -5
artist_fandom_without_contract_stability -5
buyback_without_new_title_retention -5
PE_control_premium_without_ARR -5
cybersecurity_theme_readthrough_without_contract -5
governance_legal_risk_unresolved -5
```

### 왜 내리나

R8은 숫자가 그럴듯해 보여도 가장 빨리 무너지는 섹터다. 170M MAU, 123배 청약, +14% buyback rally, +14.3% IPO pop 같은 숫자는 모두 Stage 2다. Stage 3는 결제전환, 반복매출, retention, 신작 흥행, ARR, 보안 신뢰가 닫혀야 한다.

---

# 9. Green gate 강화 조건

```text
R8 Stage 3-Green 필수:
1. 플랫폼은 MAU보다 paid conversion, ARPU, retention 확인.
2. 콘텐츠는 artist/IP contract continuity와 global distribution revenue 확인.
3. 게임은 hit title이 아니라 live-service retention, monetization, next-title pipeline 확인.
4. SW/cloud는 cloud/AI 매출비중이 아니라 recurring revenue, margin, backlog 확인.
5. enterprise SW는 ARR, churn, cloud migration, operating margin 확인.
6. IPO는 첫날 pop이 아니라 aftermarket demand와 quarterly guide 확인.
7. 보안은 사고 수혜 테마가 아니라 실제 보안계약/ARR과 신뢰 회복 확인.
8. 창업자/거버넌스/규제 이슈가 있으면 Green 유예.
9. price path가 evidence 이후 따라옴.
```

---

# 10. 4B 조기감지 조건

```text
4B-watch:
- IPO debut +10~20% 이상 급등.
- AI/cloud keyword로 공모가가 높아짐.
- game-IP valuation이 hit title 하나에 집중.
- buyback + earnings beat로 신작 검증 전 급등.
- K-content artist fandom만으로 IP risk 무시.
- PE stake/control premium으로 ARR 전 valuation 확대.
- 플랫폼 MAU 숫자만으로 paid conversion 전 rerating.
```

---

# 11. 4C hard gate 조건

```text
Hard 4C:
- 대형 data breach / customer trust break.
- founder/legal risk that blocks platform expansion or financial subsidiary control.
- artist/IP contract termination or label governance breakdown.
- IPO weak debut after aggressive pricing.
- revenue guidance miss after platform IPO.
- game launch failure / retention collapse.
- enterprise software regulatory approval failure.
- cloud/AI revenue mix not translating into margin.
```

이번 R8 Loop 14의 hard 4C는 **SK Telecom data breach**다. Kakao, HYBE, Webtoon, LG CNS, NCSoft는 hard 4C가 아니라 **4C-watch / false-positive / 4B-watch**로 둔다.

---

# 12. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 13. 레포 반영용 patch-ready 출력

## docs/round/round_218.md 요약

```md
# R8 Loop 14. Platform / Content / Software / Security Price Validation

이번 라운드는 R8 Loop 14 price-validation 라운드다.

핵심 결론:
- Naver/Webtoon is platform IPO Stage 2 plus aftermarket gate. Webtoon IPO priced at $21, jumped 14.3% in Nasdaq debut and raised $315M, but Naver saw weaker valuation boost with a 50% holdco discount, target cut 22% to 210,000 won and shares -0.9% to 165,300 won. Webtoon later fell 55% post-IPO, rebounded +62% on Disney/earnings, then fell -15% after weak Q2 2026 guidance.
- Kakao is platform governance 4C-watch. Founder Kim Beom-su arrest over alleged SM stock manipulation drove Kakao -3.4%; Kakao had already fallen 24% YTD. Prosecutors later sought 15-year jail term and 500M won fine before later acquittal relief.
- HYBE is content/IP governance 4C-watch. HYBE audit of ADOR and Min Hee-jin triggered NewJeans IP governance concerns; HYBE shares fell nearly 8%.
- Shift Up is game-IP IPO Stage 2. IPO expected to raise 435B won at 3.5T won valuation; Nikke booked 255B won sales to Q1 2024 and 2023 OP was 111B won. Green requires retention, monetization, next-title pipeline and post-IPO demand.
- NCSoft is legacy-game turnaround event premium. Q1 beat and 533,417-share buyback plan drove shares up to +14%, but net profit was still down 50% YoY and new-title retention is unproven.
- LG CNS is AI/cloud IPO false positive. IPO price 61,900 won, morning trade 59,700 won despite cloud/AI over half of 9M 2024 sales and 313B won OP. Aftermarket demand failed.
- Douzone Bizon is enterprise software PE Stage 2. EQT invests $930M for 37.6% stake; ERP/cloud SME software is attractive, but ARR, retention, margin and regulatory approval are required.
- SK Telecom is cybersecurity/data-trust hard 4C. Data breach drove -8.5% intraday and -6.7% close vs KOSPI +0.1%; later 26.96M data pieces leaked, 700B won security investment, 800B won revenue forecast cut, 500B won customer package and 134B won fine.
```

## docs/checkpoints/checkpoint_28a_round218_r8_loop14.md 요약

```md
# Checkpoint 28A Round 218 R8 Loop 14 Platform Content Software Security Price Validation

## 반영 내용
- R8 Loop 14 price-validation 라운드를 추가했다.
- Naver/Webtoon, Kakao, HYBE/NewJeans, Shift Up, NCSoft, LG CNS, Douzone Bizon, SK Telecom security breach를 비교했다.
- Reuters / WSJ / MarketWatch / FT anchors로 가능한 event MFE/MAE, IPO price, event price, deal value, revenue/OP, MAU, data-breach cost/fine metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- paid conversion/ARPU, retention/repeat usage, IP revenue stability, artist-contract continuity, game live-service retention, new-title pipeline execution, cloud/AI recurring revenue, ARR retention, data trust/internal control, governance/regulatory clearance 가중치 강화.
- MAU headline-only, IPO pop-only, AI/cloud keyword-only, IP optional value-only, fandom without contract stability, buyback without new-title retention, PE control premium without ARR, cybersecurity theme read-through without contract 감점 강화.
```

## data/e2r_case_library/cases_r8_loop14_round218.jsonl 초안

```jsonl
{"case_id":"r8_loop14_naver_webtoon_ipo_aftermarket_gate","symbol":"035420/WBTN","company_name":"Naver / Webtoon Entertainment","case_type":"event_premium_aftermarket_gate","primary_archetype":"WEBTOON_PLATFORM_IPO_AFTERMARKET_GATE","stage1_date":"2024-05-31","stage2_date":"2024-06-27","stage4b_date":"2024-06-27","stage4c_date":"2025-08-13/2026-05-11_watch","price_validation":{"price_data_source":"Reuters / MarketWatch / Barron's / WSJ event anchors","stage3_price":null,"webtoon_ipo_price_usd":21,"webtoon_open_price_usd":21.30,"webtoon_debut_high_usd":24.00,"webtoon_debut_mfe_pct":14.3,"ipo_raise_usd_mn":315,"ipo_valuation_usd_bn":2.71,"q1_2024_revenue_usd_mn":326.7,"q1_2024_net_income_usd_mn":6.2,"monthly_active_users_mn":170,"naver_event_price_krw":165300,"naver_event_mae_pct":-0.9,"naver_target_price_krw":210000,"naver_target_cut_pct":-22,"holding_company_discount_applied_pct":50,"post_ipo_decline_before_disney_pct":-55,"disney_earnings_rebound_mfe_pct":62,"disney_rebound_price_usd":15.16,"q2_2025_revenue_usd_mn":348.3,"q2_2025_revenue_growth_pct":8.5,"q1_2026_revenue_usd_mn":320.9,"q1_2026_revenue_decline_pct":-1.5,"q2_2026_guidance_usd_mn":"332-342","q2_2026_consensus_usd_mn":348,"q1_2026_after_hours_mae_pct":-15,"q1_2026_after_hours_price_usd":11.24,"mfe_30d_90d_180d_1y":"price_data_unavailable_after_deep_search","mae_30d_90d_180d_1y":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_then_aftermarket_gate","rerating_result":"WEBTOON_PLATFORM_IPO_STAGE2","notes":"IPO pop and MAU are not Green; paid conversion, IP revenue stability and parent value capture required."}
{"case_id":"r8_loop14_kakao_platform_governance_sm_case","symbol":"035720/041510_readthrough","company_name":"Kakao / SM Entertainment read-through","case_type":"thesis_break_watch_then_relief","primary_archetype":"KAKAO_PLATFORM_GOVERNANCE_4C_WATCH","stage4c_date":"2024-07-23","stage2_date":"2025-10-21_relief","price_validation":{"price_data_source":"Reuters Kakao founder arrest and prosecution anchors","stage3_price":null,"kakao_event_mae_pct":-3.4,"kakao_ytd_decline_context_pct":-24,"founder_affiliated_stake_pct":24,"group_assets_krw_trn":86,"prosecutor_sought_sentence_years":15,"prosecutor_sought_fine_krw_mn":500,"risk_channels":["AI investment","international expansion","KakaoBank control","SM content governance"],"sm_stock_manipulation_allegation":true,"direct_sm_event_price":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch_then_relief","rerating_result":"PLATFORM_GOVERNANCE_4C_WATCH","notes":"Platform user base is not Green without founder/legal and regulatory clearance."}
{"case_id":"r8_loop14_hybe_ador_newjeans_ip_governance","symbol":"352820","company_name":"HYBE / ADOR / NewJeans","case_type":"4c_watch","primary_archetype":"KPOP_IP_CONTRACT_GOVERNANCE_4C","stage4c_date":"2024-04-24_watch","price_validation":{"price_data_source":"Reuters HYBE/ADOR audit and share reaction anchor","stage3_price":null,"event_mae_pct":-8.0,"dispute_parties":["HYBE","ADOR","Min Hee-jin","NewJeans"],"risk_type":["artist_contract_continuity","multi_label_governance","content_IP_dependency"],"newjeans_contract_dispute_persistence":true,"direct_adjusted_ohlc":"price_data_unavailable_after_deep_search","mfe_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"KPOP_IP_CONTRACT_GOVERNANCE_GATE","notes":"Fandom and artist IP require contract stability, label governance and revenue continuity."}
{"case_id":"r8_loop14_shift_up_game_ip_ipo_quality_gate","symbol":"462870","company_name":"Shift Up","case_type":"success_candidate_ipo_quality_gate","primary_archetype":"GAME_IP_IPO_STAGE2_QUALITY_GATE","stage2_date":"2024-06-27/2024-07","price_validation":{"price_data_source":"Reuters Shift Up IPO and game-IP anchor","stage3_price":null,"ipo_raise_krw_bn":435,"ipo_raise_usd_mn":313,"valuation_krw_trn":3.5,"valuation_usd_bn":2.52,"tencent_stake_before_pct":40,"tencent_stake_after_expected_pct":35,"nikke_sales_krw_bn_to_q1_2024":255,"revenue_2023_krw_bn":169,"op_2023_krw_bn":111,"op_margin_2023_pct":65.7,"stellar_blade_download_ranking":{"Japan_PS":1,"North_America_PS":2},"post_ipo_adjusted_ohlc":"price_data_unavailable_after_deep_search","stage3_conditions":["live_service_retention","global_sellthrough","recurring_monetization","next_title_pipeline","post_ipo_demand"]},"score_price_alignment":"success_candidate_IPO_quality_gate","rerating_result":"GAME_IP_IPO_STAGE2","notes":"Hit IP and IPO valuation need retention, monetization, next-title pipeline and aftermarket proof."}
{"case_id":"r8_loop14_ncsoft_earnings_buyback_turnaround","symbol":"036570","company_name":"NCSoft","case_type":"event_premium_4b_watch","primary_archetype":"LEGACY_GAME_TURNAROUND_BUYBACK_4B","stage2_date":"2024-05","stage4b_date":"2024-05","price_validation":{"price_data_source":"WSJ NCSoft Q1 earnings beat / buyback event anchor","stage3_price":null,"event_mfe_pct":14.0,"q1_net_profit_krw_bn":57.12,"net_profit_yoy_change_pct":-50,"analyst_forecast_low_krw_bn":24.99,"analyst_forecast_high_krw_bn":26,"buyback_shares":533417,"treasury_share_ratio_context_pct":10,"new_title_pipeline":["Battle Crush","Project BSS","LLL","Throne and Liberty global expansion"],"new_title_retention_confirmed":false,"global_monetization_confirmed":false,"mfe_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_4B_watch","rerating_result":"LEGACY_GAME_TURNAROUND_STAGE2","notes":"Earnings beat and buyback are Stage 2; new-title retention and monetization must close."}
{"case_id":"r8_loop14_lg_cns_ai_cloud_ipo_false_positive","symbol":"064400","company_name":"LG CNS","case_type":"evidence_good_but_price_failed","primary_archetype":"AI_CLOUD_IT_SERVICE_IPO_FALSE_POSITIVE","stage2_date":"2025-02-05","price_validation":{"price_data_source":"Reuters LG CNS IPO/debut anchor","stage3_price":null,"ipo_price_krw":61900,"open_price_krw":60500,"morning_trading_price_krw":59700,"debut_mae_vs_ipo_pct":-3.23,"ipo_raise_krw_trn":1.2,"ipo_raise_usd_mn":827.1,"retail_oversubscription_multiple":123,"institutional_bids_krw_trn":76,"cloud_ai_sales_share_9m2024_pct":54,"revenue_9m2024_krw_trn":4.0,"op_9m2024_krw_bn":313,"op_margin_9m2024_pct":7.8,"aftermarket_demand_confirmed":false,"mfe_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"AI_CLOUD_IT_SERVICE_IPO_QUALITY_GATE","notes":"AI/cloud sales mix and oversubscription failed aftermarket price test."}
{"case_id":"r8_loop14_douzone_bizon_eqt_enterprise_sw_stage2","symbol":"012510","company_name":"Douzone Bizon","case_type":"success_candidate_regulatory_watch","primary_archetype":"ENTERPRISE_SOFTWARE_PE_CONTROL_STAGE2","stage2_date":"2025-11-07","price_validation":{"price_data_source":"Reuters EQT-Douzone Bizon stake anchor","stage3_price":null,"eqt_investment_usd_mn":930,"stake_acquired_pct":37.6,"chairman_stake_sold_pct":23.2,"shinhan_affiliate_stake_sold_pct":14.4,"business_model":["ERP","accounting","tax","compliance","cloud-based SME software"],"regulatory_approvals_required":["KFTC merger clearance","Ministry of Trade licensing authorization"],"arr_retention_confirmed":false,"cloud_margin_confirmed":false,"direct_event_return":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_price_data_unavailable","rerating_result":"ENTERPRISE_SOFTWARE_PE_CONTROL_STAGE2","notes":"PE control premium is not ARR/margin Green until regulatory approval and recurring revenue quality confirm."}
{"case_id":"r8_loop14_sk_telecom_cybersecurity_trust_hard_4c","symbol":"017670","company_name":"SK Telecom","case_type":"hard_4c_reference","primary_archetype":"CYBERSECURITY_TRUST_HARD_4C_REFERENCE","stage4c_date":"2025-04-28/2025-07-04/2025-08-28","price_validation":{"price_data_source":"Reuters SK Telecom data-breach event, investigation and fine anchors","stage3_price":null,"initial_intraday_mae_pct":-8.5,"initial_close_mae_pct":-6.7,"kospi_same_context_pct":0.1,"relative_underperformance_initial_pp":-6.8,"free_usim_replacement_users_mn":23,"retail_stores_involved":2600,"usim_protection_service_signups_mn":5.54,"leaked_data_pieces_mn":26.96,"july_event_close_mae_pct":-5.6,"data_protection_investment_krw_bn":700,"revenue_forecast_cut_krw_bn":800,"customer_benefit_package_cost_krw_bn":500,"pipc_fine_krw_bn":134,"mae_30d_90d_180d_1y":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break","rerating_result":"CYBERSECURITY_TRUST_HARD_4C_REFERENCE","notes":"Data-trust/internal-control failure translated into stock drop, revenue cut, compensation package, security capex and fine."}
```

## data/sector_taxonomy/score_weight_profiles_round218_r8_loop14_v1.csv 초안

```csv
archetype,paid_conversion_arpu,retention_repeat_usage,ip_revenue_stability,artist_contract_continuity,game_live_service_retention,new_title_pipeline_execution,cloud_ai_recurring_revenue,arr_retention_enterprise_sw,data_trust_internal_control,regulatory_governance_clearance,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
WEBTOON_PLATFORM_IPO_AFTERMARKET_GATE,+5,+5,+5,+1,+0,+0,+2,+0,+3,+3,-5,+5,+4,Webtoon IPO pop/MAU failed to prove durable parent value capture and revenue guide stability.
KAKAO_PLATFORM_GOVERNANCE_4C_WATCH,+3,+4,+3,+2,+0,+0,+3,+2,+4,+5,0,+4,+5,Kakao shows platform moat must pass founder/legal/regulatory gate.
KPOP_IP_CONTRACT_GOVERNANCE_4C,+2,+5,+5,+5,+0,+0,+0,+0,+2,+5,0,+5,+4,HYBE/NewJeans shows artist contract continuity is core IP gate.
GAME_IP_IPO_STAGE2_QUALITY_GATE,+2,+5,+4,+0,+5,+5,+0,+0,+1,+3,-5,+5,+3,Shift Up hit IP/IPO needs live-service retention and next-title pipeline.
LEGACY_GAME_TURNAROUND_BUYBACK_4B,+1,+5,+3,+0,+5,+5,+0,+0,+1,+3,-5,+5,+3,NCSoft buyback/earnings beat needs new-title retention and monetization proof.
AI_CLOUD_IT_SERVICE_IPO_FALSE_POSITIVE,+2,+4,+0,+0,+0,+0,+5,+5,+2,+3,-5,+5,+4,LG CNS shows AI/cloud mix and oversubscription can still fail aftermarket demand.
ENTERPRISE_SOFTWARE_PE_CONTROL_STAGE2,+3,+5,+0,+0,+0,+0,+4,+5,+3,+5,-5,+4,+3,Douzone/EQT needs ARR, churn, cloud margin and regulatory approval.
CYBERSECURITY_TRUST_HARD_4C_REFERENCE,+0,+3,+0,+0,+0,+0,+2,+3,+5,+5,0,+5,+5,SK Telecom confirms data-trust/internal-control failure is hard 4C.
```

---

# 이번 R8 Loop 14 결론

```text
1. Naver/Webtoon은 platform IPO Stage 2다.
   IPO +14.3%는 좋았지만, Naver parent discount와 이후 revenue guide miss가 Green을 막았다.

2. Kakao는 platform governance 4C-watch다.
   국민 플랫폼도 founder/legal/regulatory risk가 있으면 AI·콘텐츠·은행 read-through가 같이 흔들린다.

3. HYBE는 content IP governance 4C-watch다.
   fandom보다 artist contract continuity와 multi-label governance가 먼저다.

4. Shift Up은 game-IP success_candidate다.
   Nikke와 Stellar Blade evidence는 강하지만 retention, recurring monetization, next-title pipeline 전에는 Stage 2다.

5. NCSoft는 legacy game turnaround event premium이다.
   +14% buyback/earnings beat는 4B-watch이고, 신작 retention이 Green 조건이다.

6. LG CNS는 AI/cloud false positive다.
   cloud/AI 매출비중과 청약경쟁률이 높아도 공모가를 못 지키면 Stage 3가 아니다.

7. Douzone Bizon은 enterprise SW Stage 2다.
   EQT $930M control premium은 좋지만 ARR, churn, cloud margin, regulatory approval이 필요하다.

8. SK Telecom은 R8 hard 4C다.
   data-trust failure가 주가, revenue forecast, compensation, security capex, fine으로 직접 내려왔다.
```

한 문장으로 압축하면:

> **R8에서 진짜 Stage 3는 “플랫폼·K-content·게임 IP·AI/cloud·보안이 좋다”가 아니라, paid conversion·retention·IP revenue stability·artist contract continuity·live-service monetization·ARR·aftermarket demand·data trust가 실제 숫자로 닫히는 순간이다.**

[1]: https://www.reuters.com/markets/deals/online-comics-platform-webtoon-reveals-revenue-growth-profitability-us-ipo-2024-05-31/?utm_source=chatgpt.com "Online comics platform Webtoon reveals revenue growth, profitability in US IPO filing"
[2]: https://www.reuters.com/technology/south-korean-court-approves-arrest-warrant-kakao-founder-2024-07-22/?utm_source=chatgpt.com "Founder of South Korea's Kakao arrested for suspected stock manipulation"
[3]: https://www.reuters.com/lifestyle/record-giant-hybe-audits-newjeans-label-infighting-returns-k-pop-2024-04-24/?utm_source=chatgpt.com "Record giant HYBE audits 'NewJeans' label as infighting returns to K-pop"
[4]: https://www.reuters.com/markets/deals/tencent-backed-shift-up-may-price-ipo-top-end-band-source-says-2024-06-27/?utm_source=chatgpt.com "Tencent-backed Shift Up may price IPO at top end of band, source says"
[5]: https://www.wsj.com/articles/ncsoft-climbs-on-first-quarter-earnings-beat-share-buyback-plan-bee824ea?utm_source=chatgpt.com "NCsoft Climbs on First-Quarter Earnings Beat, Share Buyback Plan"
[6]: https://www.reuters.com/technology/skorean-tech-services-firm-lg-cns-falls-stock-market-debut-2025-02-05/?utm_source=chatgpt.com "South Korean tech services firm LG CNS drops in market debut"
[7]: https://www.reuters.com/world/asia-pacific/swedish-firm-eqt-shells-out-930-million-slice-south-koreas-douzone-bizon-2025-11-07/?utm_source=chatgpt.com "Swedish firm EQT shells out $930 million for a slice of South Korea's Douzone Bizon"
[8]: https://www.reuters.com/sustainability/boards-policy-regulation/sk-telecom-shares-plunge-after-data-breach-due-cyberattack-2025-04-28/?utm_source=chatgpt.com "SK Telecom shares plunge after data breach due to cyberattack"
