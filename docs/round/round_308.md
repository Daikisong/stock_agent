순서상 이번은 **R13 Loop 15 — Cross-archetype RedTeam / 4B / 4C / 회계·지배구조·가격검증 라운드**다.

R13은 특정 산업 하나를 보는 라운드가 아니라, R1~R12에서 반복적으로 나온 **점수표의 착시**를 잡는 라운드다. 즉 “좋은 Stage2를 너무 늦게 잡는 문제”와 “headline만 보고 Green을 너무 빨리 주는 문제”를 동시에 교정한다.

```text
round = R13 Loop 15
round_id = round_236
large_sector = CROSS_ARCHETYPE_REDTEAM
method = trigger_level_backtest_v1_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R1 Loop 16
```

이번에도 full adjusted OHLC 30D/90D/180D/1Y/2Y window는 안정적으로 확보하지 못했다. 그래서 **event anchor / reported event return / event price / relative return**까지만 기록하고, full MFE/MAE는 `price_data_unavailable_after_deep_search`로 둔다. 다만 R13 목적상 이 자체가 중요한 결론이다. 지금까지 연구의 병목은 “Stage 판단”보다 **가격검증 자동화 layer가 아직 완전하지 않다**는 점이고, production으로 가려면 `trigger row`와 `OHLC row`를 분리 저장해야 한다.

---

# 1. 이번 라운드 대섹터

```text
R13 = Cross-archetype RedTeam / 4B / 4C / 회계신뢰도 / 가격검증
```

핵심 질문은 이거다.

```text
1. 좋은 Stage2를 Stage3로 너무 늦게 올리고 있나?
2. headline / policy / M&A / celebrity / AI / IPO를 Green으로 너무 빨리 올리고 있나?
3. 4B overlay를 peak 근처가 아니라 peak 뒤에 붙이고 있나?
4. 4C hard gate를 가격 하락 뒤에야 확인하고 있나?
5. 가격자료가 없을 때 Stage 자체를 과도하게 보수화하고 있나?
6. event anchor와 full OHLC backtest를 같은 row에 섞어서 시스템이 흐려지고 있나?
```

---

# 2. 대상 canonical archetype

```text
EARLY_EVIDENCE_MISSED_STRUCTURAL
DELIVERY_TO_REVENUE_STAGE2_YELLOW
STRATEGIC_CAPITAL_WITH_DILUTION_4B
CONTROL_BATTLE_GOVERNANCE_4B_4C
EVIDENCE_GOOD_BUT_PRICE_FAILED
PLATFORM_SECURITY_HARD_4C
OPERATIONAL_SAFETY_HARD_4C
PRICE_MOVED_WITHOUT_EVIDENCE
POLICY_THEME_OVERHEAT_4B
OHLC_BACKFILL_SEPARATION_REQUIRED
```

---

# 3. deep sub-archetype

```text
Missed structural:
- Samyang Foods / Buldak
- Hyundai Rotem / Poland K2

Stage2-Actionable but 4B overlay:
- Samsung SDS / KKR CB
- Hanwha Ocean / U.S. naval optionality
- Pinkfong IPO

Governance / control / dilution:
- Korea Zinc / MBK-Young Poong tender offer
- Korea Zinc post-buyback share sale plan and regulator revision order

Evidence-good but price-failed:
- LG CNS IPO
- Kakao / OpenAI partnership

Hard 4C:
- SK Telecom data breach
- Coupang data breach
- Jeju Air crash

Price moved without evidence:
- Kyochon / Cherrybro / Neuromeka Jensen Huang chicken rally
- stablecoin policy frenzy if license/revenue absent

Policy / regulatory 4B:
- Samsung / SK Hynix China export curbs
- stablecoin policy
- AI textbook rollback
```

---

# 4. 선정 case 요약

| bucket                            | case                               | 핵심 판정                                                                                                 |
| --------------------------------- | ---------------------------------- | ----------------------------------------------------------------------------------------------------- |
| missed_structural / Stage2→Yellow | Samyang Foods / Buldak             | ASP + U.S./Europe shipment + capacity + OP estimate +84%, shares +5.7%. 기존 Stage2로만 두면 너무 늦음          |
| Stage2-Actionable→Yellow          | Hyundai Rotem / Poland K2          | 18 K2 deliveries → revenue 270B won → OP estimate +85%, shares +9.3%, KOSPI -0.3%                     |
| Stage2 + 4B                       | Samsung SDS / KKR CB               | $820M CB, shares +20.8%, AI/M&A strategy. 단 CB dilution·order backlog gate                            |
| Governance 4B/4C                  | Korea Zinc / MBK-Young Poong       | tender offer +19.8%, Young Poong +30%; 이후 $1.8B share sale plan, regulator revision order, shares -8% |
| evidence_good_but_price_failed    | LG CNS IPO                         | cloud/AI 54% sales, IPO 1.2T won, but debut below 61,900 won issue price                              |
| hard 4C                           | SK Telecom / Coupang data breaches | SKT -5.6% after regulator finding; Coupang -4.4% premarket after 33.7M accounts affected              |
| hard 4C                           | Jeju Air crash                     | 179 deaths, Jeju Air -15.7% intraday to 6,920 won, 95.7B won market-cap loss                          |
| price_moved_without_evidence      | Kyochon / Cherrybro / Neuromeka    | Jensen Huang ate at non-listed Kkanbu; Kyochon/Cherrybro/Neuromeka surged without direct revenue link |

---

# 5. Case별 trigger grid

## Case A — Samyang Foods / Buldak: Stage2를 너무 늦게 본 missed structural

```text
symbol = 003230
case_type = missed_structural / Stage2_promote_candidate
archetype = EARLY_EVIDENCE_MISSED_STRUCTURAL
```

Samyang은 R13에서 가장 중요한 “Stage2를 너무 보수적으로 본 case”다. Kiwoom은 Samyang 2Q OP estimate를 81.2B won으로 올렸고, 이는 전년 대비 +84%였다. 근거가 단순 viral이 아니라 **Buldak ASP 상승, U.S./Europe shipment 증가, production capacity 확대**였고, shares는 +5.7%로 647,000 won에 마감했다. target price도 +26% 오른 830,000 won이었다. 이 조합은 plain Stage2가 아니라 최소 `Stage2-Actionable`, 더 정확히는 `Stage3-Yellow candidate`다. ([마켓워치][1])

```json
{
  "case_id": "r13_loop15_redteam_samyang_buldak_missed_structural",
  "symbol": "003230",
  "trigger_id": "r13_samyang_T1",
  "trigger_type": "Stage2-Actionable_to_Stage3-Yellow_candidate",
  "trigger_date": "2024-06-14",
  "evidence_available_at_that_date": [
    "2Q OP estimate KRW81.2B",
    "OP estimate +84% YoY",
    "Buldak ASP increase",
    "U.S./Europe shipment increase",
    "production capacity expansion"
  ],
  "entry_price_anchor_krw": 647000,
  "event_return_pct": 5.7,
  "target_price_krw": 830000,
  "target_price_raise_pct": 26,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "missed_structural_if_old_stage2_gate_used"
}
```

### R13 판정

```text
old_gate_problem = Stage3를 너무 늦게 주는 문제
corrective_rule = ASP + shipment + capacity + OP estimate revision + price reaction이면 Stage2-Actionable을 넘어 Yellow 후보
```

---

## Case B — Hyundai Rotem / Poland K2: delivery-to-revenue trigger는 headline보다 강하다

```text
symbol = 064350
case_type = Stage2-Actionable / Stage3-Yellow candidate
archetype = DELIVERY_TO_REVENUE_STAGE2_YELLOW
```

Hyundai Rotem은 “계약 announcement”보다 “납품 → 매출 → OP estimate”가 훨씬 강한 trigger라는 점을 보여준다. 2024년 4월 9일 Hyundai Rotem shares는 +9.3%로 41,300 won까지 올랐고, KOSPI는 -0.3%였다. KB Securities는 18대 K2 tanks가 Poland로 shipment되면서 약 270B won revenue contribution이 가능하고, Q1 OP가 +85% YoY인 59.1B won으로 consensus 44.4B won을 웃돌 수 있다고 봤다. ([월스트리트저널][2])

```json
{
  "case_id": "r13_loop15_redteam_hyundai_rotem_k2_delivery",
  "symbol": "064350",
  "trigger_id": "r13_rotem_T1",
  "trigger_type": "Stage2-Actionable_to_Stage3-Yellow_candidate",
  "trigger_date": "2024-04-09",
  "entry_price_anchor_krw": 41300,
  "event_return_pct": 9.3,
  "kospi_same_context_pct": -0.3,
  "market_relative_return_pp": 9.6,
  "k2_shipments_to_poland_count": 18,
  "k2_revenue_contribution_krw_bn": 270,
  "q1_op_estimate_krw_bn": 59.1,
  "q1_op_estimate_yoy_pct": 85,
  "q1_op_consensus_krw_bn": 44.4,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_delivery_to_revenue_entry"
}
```

### R13 판정

```text
old_gate_problem = signed contract와 delivery trigger를 같은 단계로 보는 문제
corrective_rule = delivery + revenue contribution + OP estimate beat + market-relative strength이면 Yellow 후보
```

---

## Case C — Samsung SDS / KKR CB: Stage2는 맞지만 4B를 병기해야 한다

```text
symbol = 018260
case_type = Stage2-Actionable with 4B overlay
archetype = STRATEGIC_CAPITAL_WITH_DILUTION_4B
```

Samsung SDS는 Stage2-Actionable이 맞다. KKR이 $820M의 newly issued convertible bonds를 매입한다고 발표했고, Samsung SDS shares는 장중 +20.8%까지 올랐다. KKR은 M&A, capital allocation, AI offerings에 대해 advisory role을 제공하고, Samsung SDS는 6.4T won cash와 함께 AI infrastructure, physical AI, stablecoins, M&A에 투자하겠다고 했다. 하지만 이건 CB다. 따라서 `strategic capital` 점수는 올리되, **dilution / conversion / backlog 미확인 4B**를 반드시 붙여야 한다. ([Reuters][3])

```json
{
  "case_id": "r13_loop15_redteam_samsung_sds_kkr_cb",
  "symbol": "018260",
  "trigger_id": "r13_sds_T1",
  "trigger_type": "Stage2-Actionable_plus_4B",
  "trigger_date": "2026-04-15",
  "convertible_bond_value_usd_mn": 820,
  "event_mfe_pct": 20.8,
  "morning_return_pct": 19.4,
  "kospi_same_context_pct": 3.0,
  "market_relative_return_pp": 17.8,
  "cash_and_equivalents_krw_trn": 6.4,
  "evidence_available_at_that_date": [
    "KKR strategic capital",
    "M&A advisory",
    "AI offerings expansion",
    "physical AI",
    "stablecoin ambition"
  ],
  "4B_overlay": [
    "CB dilution",
    "conversion risk",
    "no enterprise AI backlog yet",
    "strategy execution risk"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_Actionable_with_required_4B_overlay"
}
```

### R13 판정

```text
old_gate_problem = 전략투자/CB를 Green처럼 보는 문제
corrective_rule = strategic capital은 Stage2-Actionable 가능, 하지만 CB/dilution/order backlog 전에는 4B 병기
```

---

## Case D — Korea Zinc / control battle: control premium은 Green이 아니라 governance 4B/4C다

```text
symbol = 010130
case_type = control battle / governance / dilution red-team
archetype = CONTROL_BATTLE_GOVERNANCE_4B_4C
```

Korea Zinc는 R13에서 가장 중요한 governance red-team case다. 2024년 9월 MBK Partners와 Young Poong이 Korea Zinc shares를 660,000 won에 tender offer한다고 발표했을 때, Korea Zinc shares는 +19.8% 올랐고 Young Poong shares는 +30% daily limit까지 올랐다. 이 자체는 control premium event다. 하지만 이걸 Stage3로 보면 안 된다. control battle은 EPS/OP/FCF가 아니라 **지배권 프리미엄과 governance risk**다. ([Reuters][4])

이후 Korea Zinc가 약 $1.8B share sale plan을 발표하자 FSS가 revision order를 내렸고, plan의 목적·의사결정 과정·bookrunner due diligence 설명이 부족하다고 지적했다. Korea Zinc shares는 해당 filing 이후 최대 -8% 하락했다. 이 흐름은 `control premium → defensive capital raise → regulator intervention → dilution/governance 4B/4C`의 전형이다. ([Reuters][5])

```json
{
  "case_id": "r13_loop15_redteam_korea_zinc_control_battle",
  "symbol": "010130",
  "trigger_id": "r13_koreazinc_T1_T2",
  "trigger_type": "control_premium_then_governance_4B_4C",
  "t1_date": "2024-09-13",
  "tender_offer_price_krw": 660000,
  "pre_offer_close_krw": 556000,
  "korea_zinc_event_return_pct": 19.8,
  "young_poong_event_return_pct": 30,
  "tender_offer_value_krw_trn": 2.0,
  "tender_offer_value_usd_bn": 1.5,
  "t2_date": "2024-11-06",
  "share_sale_plan_usd_bn": 1.8,
  "fss_revision_order": true,
  "share_sale_event_mae_pct": -8,
  "4B_4C_overlay": [
    "control battle",
    "defensive share issuance",
    "dilution",
    "regulator revision order",
    "governance uncertainty"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "control_premium_not_stage3_green"
}
```

### R13 판정

```text
old_gate_problem = control premium을 실적 rerating으로 오해하는 문제
corrective_rule = tender/control battle은 Stage2 event 또는 4B, dilution/regulator 개입 시 4C-watch
```

---

## Case E — LG CNS IPO: evidence가 좋아도 price가 거부하면 Green 금지

```text
symbol = LG_CNS
case_type = evidence_good_but_price_failed
archetype = EVIDENCE_GOOD_BUT_PRICE_FAILED
```

LG CNS는 “좋은 narrative + 좋은 수치 + 나쁜 가격반응”의 표본이다. cloud/AI services가 2024년 첫 3개 분기 매출의 약 54%를 차지했고, IPO는 top range로 pricing되어 1.2T won을 조달했다. 하지만 상장일 issue price 61,900 won 아래인 59,700 won에 거래됐다. 이 경우 Stage2 evidence는 맞지만, price가 Green을 거부했다. ([Reuters][6])

```json
{
  "case_id": "r13_loop15_redteam_lg_cns_evidence_price_fail",
  "symbol": "LG_CNS",
  "trigger_id": "r13_lgcns_T1",
  "trigger_type": "evidence_good_but_price_failed",
  "trigger_date": "2025-02-05",
  "ipo_issue_price_krw": 61900,
  "debut_open_price_krw": 60500,
  "debut_last_reported_price_krw": 59700,
  "debut_return_vs_issue_pct": -3.55,
  "ipo_raise_krw_trn": 1.2,
  "cloud_ai_sales_share_3q2024_pct": 54,
  "revenue_3q2024_krw_trn": 4.0,
  "op_3q2024_krw_bn": 313,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "evidence_good_but_price_failed"
}
```

### R13 판정

```text
old_gate_problem = 좋은 사업 narrative만 보고 Stage3로 올리는 문제
corrective_rule = evidence가 좋아도 event close가 issue/entry 아래면 Green 금지, evidence_good_but_price_failed로 분리
```

---

## Case F — SK Telecom / Coupang data breach: 플랫폼 scale은 security 없으면 hard 4C다

```text
symbols = 017670 / CPNG_reference
case_type = platform security hard 4C
archetype = PLATFORM_SECURITY_HARD_4C
```

SK Telecom은 KRX-listed hard 4C template이다. 정부는 SKT가 data leak에서 negligent했다고 판단했고, 26.96M pieces of user data leak, CEO 직접 data governance, quarterly security measures, 700B won 5-year data protection investment, 50% August subscription discount, 2025 revenue forecast -800B won 조정을 발표했다. SKT shares는 그날 -5.6%로 마감했다. ([Reuters][7])

Coupang은 U.S.-listed이지만 한국 생활서비스 platform의 hard gate reference다. 33.7M customer accounts가 영향을 받았고, stock은 premarket -4.4%였다. 이후 CEO resignation, police/government probes가 뒤따랐다. platform scale은 보안이 닫혀 있지 않으면 moat가 아니라 피해 규모를 키운다. ([Barron's][8])

```json
{
  "case_id": "r13_loop15_redteam_platform_security_4c",
  "symbols": "017670/CPNG_reference",
  "trigger_id": "r13_security_T1",
  "trigger_type": "hard_4C_security",
  "skt_trigger_date": "2025-07-04",
  "skt_data_pieces_leaked_mn": 26.96,
  "skt_event_return_pct": -5.6,
  "skt_security_investment_5y_krw_bn": 700,
  "skt_revenue_forecast_cut_2025_krw_bn": 800,
  "skt_august_subscription_discount_pct": 50,
  "coupang_trigger_date": "2025-12-01",
  "coupang_affected_accounts_mn": 33.7,
  "coupang_premarket_event_return_pct": -4.4,
  "hard_4c_features": [
    "customer data leak",
    "regulator finding",
    "compensation cost",
    "revenue forecast cut",
    "CEO or governance response",
    "trust damage"
  ],
  "trigger_outcome_label": "hard_4C_success_platform_security"
}
```

### R13 판정

```text
old_gate_problem = platform scale / MAU / customer base를 security 없이 긍정점수로만 보는 문제
corrective_rule = 개인정보·USIM·payment·customer-data breach는 즉시 hard 4C, security capex는 growth capex가 아니라 trust-repair cost
```

---

## Case G — Jeju Air crash: safety 4C는 어떤 demand trigger보다 먼저다

```text
symbol = 089590
case_type = operational safety hard 4C
archetype = OPERATIONAL_SAFETY_HARD_4C
```

Jeju Air crash는 R13 hard 4C template이다. 179명이 사망했고, Jeju Air shares는 장중 최대 -15.7%로 6,920 won까지 하락했으며, 최대 95.7B won market cap이 사라졌다. AK Holdings는 장중 -12%까지 하락했고, 정부는 항공 운영 전반의 emergency safety inspection을 지시했다. 이건 demand/yield/여행회복보다 선행하는 hard gate다. ([Reuters][9])

```json
{
  "case_id": "r13_loop15_redteam_jeju_air_safety_4c",
  "symbol": "089590",
  "trigger_id": "r13_jejuair_T1",
  "trigger_type": "hard_4C_operational_safety",
  "trigger_date": "2024-12-30",
  "fatalities": 179,
  "intraday_mae_pct": -15.7,
  "intraday_low_krw": 6920,
  "reported_midday_return_pct": -8.5,
  "market_cap_loss_krw_bn": 95.7,
  "ak_holdings_intraday_mae_pct": -12,
  "safety_inspection_ordered": true,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "hard_4C_success_operational_safety"
}
```

### R13 판정

```text
old_gate_problem = 항공/여행 demand 회복만 보고 safety risk를 뒤늦게 반영하는 문제
corrective_rule = 사망사고·전국 안전점검·신뢰손상은 즉시 hard 4C, sector spread까지 감점
```

---

## Case H — Kyochon / Cherrybro / Neuromeka: price moved without evidence

```text
symbols = 339770 / 066360 / 348340
case_type = price_moved_without_evidence
archetype = PRICE_MOVED_WITHOUT_EVIDENCE
```

Kyochon/Cherrybro/Neuromeka는 R13에서 가장 깨끗한 “가격이 먼저 움직였지만 evidence가 없는” case다. Jensen Huang이 Samsung·Hyundai executives와 fried chicken을 먹은 restaurant은 상장사가 아닌 Kkanbu Chicken이었다. 그런데 Kyochon, Cherrybro, Neuromeka shares가 급등했다. MarketWatch는 Kkanbu가 public company가 아니었고, Nvidia가 한국에 260,000 AI chips를 판매하는 deals는 있었지만 해당 fried-chicken names에 equity purchase는 없었다고 보도했다. ([마켓워치][10])

```json
{
  "case_id": "r13_loop15_redteam_jensen_chicken_meme",
  "symbols": "339770/066360/348340",
  "trigger_id": "r13_chicken_T1",
  "trigger_type": "price_moved_without_evidence",
  "trigger_date": "2025-10-31",
  "event_context": "Jensen Huang dined at non-listed Kkanbu Chicken with Samsung and Hyundai executives",
  "listed_companies_moved": [
    "Kyochon F&B",
    "Cherrybro",
    "Neuromeka"
  ],
  "kkanbu_listed": false,
  "nvidia_korea_ai_chip_deals_units": 260000,
  "direct_revenue_link_confirmed": false,
  "equity_purchase_confirmed": false,
  "same_store_sales_confirmed": false,
  "franchise_fee_confirmed": false,
  "MFE_30D": "N/A_no_valid_stage3",
  "MAE_30D": "N/A_no_valid_stage3",
  "trigger_outcome_label": "price_moved_without_evidence"
}
```

### R13 판정

```text
old_gate_problem = 가격상승을 evidence로 착각하는 문제
corrective_rule = celebrity/event/meme rally는 direct revenue evidence 전에는 Stage3 금지, price_moved_without_evidence로 분리
```

---

# 6. Trigger별 가격검증 요약

| case                      | trigger                             |                      event anchor |                         event return | market-relative | full MFE/MAE | R13 판정                         |
| ------------------------- | ----------------------------------- | --------------------------------: | -----------------------------------: | --------------: | ------------ | ------------------------------ |
| Samyang Buldak            | OP estimate + ASP/shipment/capacity |                 647,000 won close |                                +5.7% |     unavailable | unavailable  | missed_structural              |
| Hyundai Rotem K2          | delivery → revenue → OP estimate    |                        41,300 won |                                +9.3% |          +9.6pp | unavailable  | excellent Stage2→Yellow        |
| Samsung SDS KKR CB        | strategic capital / AI / M&A        |                    no exact price |                               +20.8% |         +17.8pp | unavailable  | Stage2 + 4B                    |
| Korea Zinc control battle | tender offer / share sale           | 556,000 pre-offer / 660,000 offer | +19.8%, then -8% on share sale issue |     unavailable | unavailable  | control premium 4B/4C          |
| LG CNS IPO                | cloud/AI sales mix                  |       61,900 issue / 59,700 debut |                      -3.55% vs issue |     unavailable | unavailable  | evidence_good_but_price_failed |
| SKT/Coupang breach        | data breach                         |   SKT -5.6%, CPNG -4.4% premarket |                             negative |     unavailable | unavailable  | hard security 4C               |
| Jeju Air crash            | fatal safety accident               |                6,920 intraday low |                      -15.7% intraday |     unavailable | unavailable  | hard safety 4C                 |
| Jensen chicken meme       | celebrity dinner                    |                    no valid entry |           surged but no revenue link |             N/A | N/A          | price_moved_without_evidence   |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
좋은 Stage2:
- Samyang: ASP + shipment + capacity + OP estimate
- Hyundai Rotem: delivery + revenue + OP estimate
- Samsung SDS: strategic capital + AI/M&A + strong price reaction, but 4B

나쁜 Stage2:
- LG CNS: cloud/AI sales evidence was good, but price rejected IPO.
- Korea Zinc: control premium was real, but governance/dilution risk followed.
- Kyochon: price moved, but no direct evidence.
```

## Stage 2-Actionable entry 성과

```text
Actionable로 승격해야 하는 조합:
- event_return > +5%
- market_relative_return > +5pp
- evidence가 EPS/OP/FCF로 연결됨
- OP estimate / shipment / delivery / contract value / capacity가 같이 닫힘

Samyang과 Hyundai Rotem은 이 조건을 충족한다.
```

## Stage 3-Yellow 후보

```text
Yellow 후보:
- Samyang: 실제 분기 실적과 반복 수요 확인 시
- Hyundai Rotem: multi-quarter delivery/margin/cash collection 확인 시
- Hanwha Aerospace / Samsung E&A류: backlog-to-OP conversion 확인 시

Yellow가 아닌 것:
- Samsung SDS: CB와 order backlog gate가 남음
- Korea Zinc: control premium은 실적경로 아님
- LG CNS: price failed
- Kyochon: evidence 없음
```

## Stage3-Green

```text
이번 R13 Loop 15에서 확정 Green은 없음.

이유:
- R13은 red-team 라운드라 Green 확정보다 gate failure를 보는 목적이 크다.
- 대부분 case는 full OHLC MFE/MAE가 아직 unavailable이다.
- Green은 반드시 OHLC backfill + evidence-to-earnings conversion이 같이 닫혀야 한다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- Hyundai Rotem K2: evidence와 price reaction이 정렬됨
- Samyang Buldak: evidence와 price reaction이 정렬됨

Stage2_promote_candidate:
- Samyang
- Hyundai Rotem
- Samsung SDS, but 4B overlay
- Pinkfong/Samsung E&A/Hanwha Aerospace류는 같은 family

missed_structural:
- Samyang, if old Stage3 gate required actual reported earnings only
- Hyundai Rotem, if old gate ignored delivery-to-revenue estimate

evidence_good_but_price_failed:
- LG CNS
- Kakao/OpenAI도 같은 family

false_positive_score:
- Korea Zinc if control premium treated as operating rerating
- Samsung SDS if CB/AI strategy treated as Green without backlog
- stablecoin theme if policy treated as revenue

price_moved_without_evidence:
- Kyochon / Cherrybro / Neuromeka

thesis_break:
- SKT/Coupang breach
- Jeju Air crash
- Korea Zinc regulator/dilution event

hard_4c_success:
- Jeju Air crash
- SK Telecom data breach
- Coupang data breach
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
evidence_to_earnings_bridge,+5,"ASP/shipment/delivery/OP estimate가 같이 닫히면 Stage2를 Yellow 후보로 올린다","Samyang, Hyundai Rotem"
market_relative_event_strength,+4,"KOSPI 대비 +5pp 이상이면 Stage2-Actionable 승격 신호","Hyundai Rotem, Samsung SDS, Samsung E&A"
delivery_to_revenue_conversion,+5,"방산/수출/수주에서 납품이 매출과 OP estimate로 연결되면 강한 trigger","Hyundai Rotem"
actual_capacity_or_shipment,+4,"capacity/shipment가 실제 수요와 연결되면 단순 테마보다 강함","Samyang"
platform_security_trust,+5,"데이터 유출은 즉시 hard 4C","SKT, Coupang"
operational_safety_trust,+5,"사망사고·전국 안전점검은 hard 4C","Jeju Air"
governance_dilution_quality,+5,"control battle, defensive issuance, regulator order는 4B/4C","Korea Zinc"
price_evidence_disagreement,+5,"evidence가 좋아도 price가 거부하면 Green 금지","LG CNS"
```

## 내릴 축

```csv
axis,delta,reason,cases
headline_only_score,-5,"headline은 EPS/OP/FCF 연결 전에는 Stage3 금지","Kakao/OpenAI, LG CNS"
policy_theme_without_revenue,-5,"정책테마는 license/revenue/contract 전에는 4B","stablecoin, AI textbook"
control_premium_as_rerating,-5,"control premium은 실적 rerating이 아님","Korea Zinc"
CB_capital_without_backlog,-4,"CB 전략투자는 dilution/order backlog gate 필요","Samsung SDS"
celebrity_meme_event,-5,"유명인 이벤트는 revenue evidence 전에는 price_moved_without_evidence","Kyochon"
IPO_pop_without_durability,-4,"IPO pop은 recurring revenue 전에는 4B","LG CNS, Pinkfong"
platform_scale_without_security,-5,"scale은 breach 때 피해 규모를 키움","SKT, Coupang"
```

---

# 10. Stage 2-Actionable 승격 조건

R13 shadow rule:

```text
Stage2 evidence가 아래 중 3개 이상이면 Stage2-Actionable로 승격한다.

1. OP/EPS/FCF estimate revision이 있다.
2. shipment, delivery, ASP, capacity, contract value 중 2개 이상이 동시에 닫힌다.
3. event_return이 +5% 이상이다.
4. market_relative_return이 +5pp 이상이다.
5. evidence가 단순 narrative가 아니라 매출/마진 bridge를 갖는다.
6. 공개 evidence가 trigger date에 실제로 시장이 알 수 있었던 정보다.
7. hard 4C overlay가 없다.
```

적용:

```text
Samyang:
OP estimate +84%, ASP, shipment, capacity, +5.7% → Stage2-Actionable / Yellow candidate.

Hyundai Rotem:
delivery, revenue contribution, OP estimate beat, +9.3%, KOSPI -0.3% → Stage2-Actionable / Yellow candidate.

Samsung SDS:
+20.8%, strategic capital, AI/M&A → Stage2-Actionable.
하지만 CB/dilution/order backlog 미확인 → 4B 병기.
```

---

# 11. Stage 3-Yellow 조건

```text
Stage3-Yellow:
- Stage2-Actionable 조건을 충족하고,
- EPS/OP/FCF 경로가 바뀔 가능성이 크며,
- hard gate 하나만 남은 상태.
```

Yellow로 올릴 수 있는 family:

```text
1. Samyang-type:
ASP + shipment + capacity + OP estimate revision.

2. Hyundai Rotem-type:
delivery + revenue contribution + OP estimate beat.

3. Samsung E&A / Hanwha Aerospace-type:
large signed contract + backlog relevance + price reaction.

4. Pinkfong-type:
IPO pop + actual OP/sales + recurring IP evidence, 단 next-IP 확인 필요.
```

Yellow 금지 family:

```text
1. LG CNS-type:
evidence good but price failed.

2. Korea Zinc-type:
control premium / governance battle.

3. Samsung SDS-type:
strategic capital but CB/dilution/order backlog missing.

4. Kyochon-type:
price moved without evidence.

5. SKT/Coupang/Jeju-type:
hard 4C.
```

---

# 12. Stage 3-Green 조건

```text
Stage3-Green:
- Yellow 이후 full OHLC MFE/MAE가 우호적이어야 한다.
- 30D/90D에 entry_price 아래로 깊게 깨지면 안 된다.
- evidence-to-earnings bridge가 실제 실적/현금흐름으로 확인되어야 한다.
- 4B overlay가 해소되거나 관리 가능해야 한다.
- 4C hard gate가 없어야 한다.
```

R13 결론:

```text
stage3_green_confirmed = false
reason = full OHLC backfill unavailable + R13 is red-team calibration round
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- 전략투자/CB/유상증자/자사주/인수전이 있지만 dilution 또는 control risk가 있다.
- IPO pop이 있지만 post-listing durability가 없다.
- AI/정책/테마 headline이 있지만 revenue bridge가 없다.
- 주가가 +20~100% 급등했지만 evidence가 revenue로 연결되지 않는다.
- control premium이 operating rerating처럼 pricing된다.
```

적용:

```text
Samsung SDS:
+20.8% but CB/dilution/order backlog missing → 4B.

Korea Zinc:
tender offer + control premium, then share sale/regulator issue → 4B/4C.

LG CNS:
cloud/AI evidence but IPO failed → 4B/false-positive.

Kyochon:
celebrity meme → price_moved_without_evidence.
```

---

# 14. 4C hard gate 조건

```text
R13 hard 4C:
- 고객 데이터 유출 / 보안사고
- 사망사고 / 안전사고
- regulator intervention after governance/dilution event
- export-control license shock
- labor strike threatening output
- accounting/fraud/investigation risk
- platform trust collapse
```

확정 hard 4C:

```text
SK Telecom data breach
Coupang data breach
Jeju Air crash
```

4C-watch:

```text
Korea Zinc governance/dilution/regulator issue
Samsung/SK Hynix export curbs
Samsung labor strike
AI textbook rollback
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R13의 가장 중요한 production 설계 교정은 아래다.

```text
Stage 판정 row와 OHLC 검증 row를 분리해야 한다.
```

현재처럼 한 row에 `stage`, `trigger`, `MFE`, `MAE`, `evidence`를 다 넣으면, OHLC가 없을 때 Stage 자체를 과도하게 보수화하는 문제가 생긴다.

권장 구조:

```text
case_library row:
- 무엇이 일어났는가?
- 어떤 stage 후보인가?
- 어떤 evidence가 있었는가?

trigger_calibration row:
- trigger별 entry anchor는 무엇인가?
- reported event return은 얼마인가?
- full OHLC backfill 상태는 무엇인가?

ohlc_backfill row:
- entry_date
- adjusted OHLC
- MFE/MAE windows
- below_entry flag
- peak/drawdown
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_236.md 요약

```md
# R13 Loop 15. Cross-archetype RedTeam / 4B / 4C / Price Validation

이번 라운드는 R13 Loop 15 cross-archetype red-team 라운드다.

핵심 결론:
- Samyang Foods / Buldak shows old Stage3 gates can be too late. OP estimate +84%, ASP increase, U.S./Europe shipment growth, capacity expansion and +5.7% price reaction should promote Stage2 to Stage2-Actionable or Stage3-Yellow candidate.
- Hyundai Rotem / Poland K2 is the clean delivery-to-revenue template. 18 K2 deliveries, 270B won revenue contribution, Q1 OP estimate +85%, shares +9.3% while KOSPI -0.3%.
- Samsung SDS / KKR CB is Stage2-Actionable with 4B overlay. $820M CB, shares +20.8%, AI/M&A strategy, but CB dilution and order backlog are unresolved.
- Korea Zinc / MBK-Young Poong is control-premium red-team. Tender offer triggered +19.8% Korea Zinc and +30% Young Poong, but later $1.8B share-sale plan and FSS revision order caused -8% and governance/dilution 4B/4C.
- LG CNS is evidence_good_but_price_failed. Cloud/AI services were 54% of sales, IPO raised 1.2T won, but debut traded below the 61,900 won issue price.
- Platform security is hard 4C. SK Telecom data breach led to -5.6%, 26.96M data pieces leaked, 700B won security investment and 800B won revenue forecast cut. Coupang breach affected 33.7M customer accounts and shares fell 4.4% premarket.
- Jeju Air crash is hard operational safety 4C. 179 deaths, shares down as much as 15.7% to 6,920 won, 95.7B won market cap loss.
- Kyochon / Cherrybro / Neuromeka is price_moved_without_evidence. Jensen Huang ate at non-listed Kkanbu Chicken; listed peers surged without direct revenue evidence.

Main calibration:
- Raise evidence_to_earnings_bridge, market_relative_event_strength, delivery_to_revenue_conversion, actual_capacity_or_shipment, platform_security_trust, operational_safety_trust, governance_dilution_quality, price_evidence_disagreement.
- Lower headline_only_score, policy_theme_without_revenue, control_premium_as_rerating, CB_capital_without_backlog, celebrity_meme_event, IPO_pop_without_durability, platform_scale_without_security.

Structural production fix:
- Separate case_library rows from trigger_calibration rows from ohlc_backfill rows.
- Do not downgrade a valid Stage2/Yellow candidate only because OHLC backfill is missing.
```

## docs/checkpoints/checkpoint_28a_round236_r13_loop15.md 요약

```md
# Checkpoint 28A Round 236 R13 Loop 15 RedTeam Calibration

## 반영 내용
- R13 cross-archetype red-team validation을 수행했다.
- Samyang, Hyundai Rotem, Samsung SDS, Korea Zinc, LG CNS, SK Telecom/Coupang, Jeju Air, Kyochon/Cherrybro/Neuromeka를 비교했다.
- full adjusted OHLC window는 확보하지 못했으므로 reported event return과 event price anchor를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- Stage2-Actionable은 ASP/shipment/delivery/OP estimate/relative strength 조합으로 승격한다.
- CB/유상증자/control battle은 Stage2와 동시에 4B/4C overlay를 붙인다.
- evidence가 좋아도 price가 거부하면 evidence_good_but_price_failed로 둔다.
- security/safety/data breach는 hard 4C다.
- price moved without evidence는 separate label로 강제 분리한다.
- 다음 구현에서는 case_library, trigger_calibration, ohlc_backfill을 분리한다.
```

## data/e2r_case_library/cases_r13_loop15_round236.jsonl 초안

```jsonl
{"case_id":"r13_loop15_redteam_samyang_buldak_missed_structural","symbol":"003230","company_name":"Samyang Foods","case_type":"missed_structural","primary_archetype":"EARLY_EVIDENCE_MISSED_STRUCTURAL","best_trigger":"r13_samyang_T1","stage_candidate":"Stage2-Actionable_to_Stage3-Yellow_candidate","price_validation":{"entry_price_anchor_krw":647000,"event_return_pct":5.7,"target_price_krw":830000,"op_estimate_krw_bn":81.2,"op_estimate_yoy_pct":84,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"missed_structural_if_old_gate_used","notes":"ASP+shipment+capacity+OP estimate should promote Stage2 to Yellow candidate."}
{"case_id":"r13_loop15_redteam_hyundai_rotem_k2_delivery","symbol":"064350","company_name":"Hyundai Rotem","case_type":"Stage2_promote_candidate","primary_archetype":"DELIVERY_TO_REVENUE_STAGE2_YELLOW","best_trigger":"r13_rotem_T1","stage_candidate":"Stage2-Actionable_to_Stage3-Yellow_candidate","price_validation":{"entry_price_anchor_krw":41300,"event_return_pct":9.3,"kospi_same_context_pct":-0.3,"market_relative_return_pp":9.6,"k2_shipments_to_poland_count":18,"k2_revenue_contribution_krw_bn":270,"q1_op_estimate_krw_bn":59.1,"q1_op_estimate_yoy_pct":85,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_entry","notes":"Delivery-to-revenue and OP estimate beat are strong Yellow candidate triggers."}
{"case_id":"r13_loop15_redteam_samsung_sds_kkr_cb","symbol":"018260","company_name":"Samsung SDS","case_type":"Stage2_Actionable_with_4B","primary_archetype":"STRATEGIC_CAPITAL_WITH_DILUTION_4B","best_trigger":"r13_sds_T1","stage_candidate":"Stage2-Actionable + 4B-watch","price_validation":{"convertible_bond_value_usd_mn":820,"event_mfe_pct":20.8,"morning_return_pct":19.4,"kospi_same_context_pct":3.0,"market_relative_return_pp":17.8,"cash_and_equivalents_krw_trn":6.4,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate_with_4B_overlay","notes":"Strategic capital is actionable, but CB dilution and backlog gates remain."}
{"case_id":"r13_loop15_redteam_korea_zinc_control_battle","symbol":"010130","company_name":"Korea Zinc","case_type":"control_premium_4B_4C","primary_archetype":"CONTROL_BATTLE_GOVERNANCE_4B_4C","best_trigger":"r13_koreazinc_T1_T2","stage_candidate":"4B/4C-watch","price_validation":{"tender_offer_price_krw":660000,"pre_offer_close_krw":556000,"korea_zinc_event_return_pct":19.8,"young_poong_event_return_pct":30,"tender_offer_value_krw_trn":2.0,"share_sale_plan_usd_bn":1.8,"share_sale_event_mae_pct":-8,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"control_premium_not_stage3_green","notes":"Control premium is not operating rerating; dilution and regulator intervention are 4B/4C overlays."}
{"case_id":"r13_loop15_redteam_lg_cns_evidence_price_fail","symbol":"LG_CNS","company_name":"LG CNS","case_type":"evidence_good_but_price_failed","primary_archetype":"EVIDENCE_GOOD_BUT_PRICE_FAILED","best_trigger":"r13_lgcns_T1","stage_candidate":"Stage2_not_Green","price_validation":{"ipo_issue_price_krw":61900,"debut_open_price_krw":60500,"debut_last_reported_price_krw":59700,"debut_return_vs_issue_pct":-3.55,"ipo_raise_krw_trn":1.2,"cloud_ai_sales_share_3q2024_pct":54,"revenue_3q2024_krw_trn":4.0,"op_3q2024_krw_bn":313,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"evidence_good_but_price_failed","notes":"Good evidence but weak price action blocks Green."}
{"case_id":"r13_loop15_redteam_platform_security_4c","symbol":"017670/CPNG_reference","company_name":"SK Telecom / Coupang","case_type":"hard_4c_security","primary_archetype":"PLATFORM_SECURITY_HARD_4C","best_trigger":"r13_security_T1","stage_candidate":"4C","price_validation":{"skt_data_pieces_leaked_mn":26.96,"skt_event_return_pct":-5.6,"skt_security_investment_5y_krw_bn":700,"skt_revenue_forecast_cut_2025_krw_bn":800,"coupang_affected_accounts_mn":33.7,"coupang_premarket_event_return_pct":-4.4},"score_price_alignment":"hard_4c_success","notes":"Platform scale without security becomes hard 4C."}
{"case_id":"r13_loop15_redteam_jeju_air_safety_4c","symbol":"089590","company_name":"Jeju Air","case_type":"hard_4c_safety","primary_archetype":"OPERATIONAL_SAFETY_HARD_4C","best_trigger":"r13_jejuair_T1","stage_candidate":"4C","price_validation":{"fatalities":179,"intraday_mae_pct":-15.7,"intraday_low_krw":6920,"reported_midday_return_pct":-8.5,"market_cap_loss_krw_bn":95.7,"ak_holdings_intraday_mae_pct":-12,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"hard_4c_success","notes":"Fatal safety accident overrides demand/yield positives."}
{"case_id":"r13_loop15_redteam_jensen_chicken_meme","symbol":"339770/066360/348340","company_name":"Kyochon F&B / Cherrybro / Neuromeka","case_type":"price_moved_without_evidence","primary_archetype":"PRICE_MOVED_WITHOUT_EVIDENCE","best_trigger":"r13_chicken_T1","stage_candidate":"N/A_no_valid_stage3","price_validation":{"kkanbu_listed":false,"nvidia_korea_ai_chip_deals_units":260000,"direct_revenue_link_confirmed":false,"equity_purchase_confirmed":false,"same_store_sales_confirmed":false,"full_ohlc_status":"N/A_no_valid_stage3"},"score_price_alignment":"price_moved_without_evidence","notes":"Celebrity meme rally without direct revenue evidence must be separated from Stage scoring."}
```

## data/e2r_trigger_calibration/triggers_r13_loop15_round236.jsonl 초안

```jsonl
{"trigger_id":"r13_samyang_T1","case_id":"r13_loop15_redteam_samyang_buldak_missed_structural","trigger_type":"Stage2-Actionable_to_Stage3-Yellow_candidate","trigger_date":"2024-06-14","evidence_available":"OP estimate KRW81.2B +84% YoY, Buldak ASP increase, U.S./Europe shipment growth, capacity expansion, shares +5.7%","entry_price_krw":647000,"event_return_pct":5.7,"trigger_outcome_label":"missed_structural_if_old_gate_used","promote_to":"Stage3-Yellow_candidate"}
{"trigger_id":"r13_rotem_T1","case_id":"r13_loop15_redteam_hyundai_rotem_k2_delivery","trigger_type":"Stage2-Actionable_to_Stage3-Yellow_candidate","trigger_date":"2024-04-09","evidence_available":"18 K2 tanks shipped to Poland, KRW270B revenue contribution, Q1 OP estimate +85%, shares +9.3%, KOSPI -0.3%","entry_price_krw":41300,"event_return_pct":9.3,"market_relative_return_pp":9.6,"trigger_outcome_label":"excellent_delivery_to_revenue_entry","promote_to":"Stage3-Yellow_candidate"}
{"trigger_id":"r13_sds_T1","case_id":"r13_loop15_redteam_samsung_sds_kkr_cb","trigger_type":"Stage2-Actionable_plus_4B","trigger_date":"2026-04-15","evidence_available":"KKR buys $820M Samsung SDS CB, shares +20.8%, KKR to advise on M&A/capital allocation/AI offerings","event_return_pct":20.8,"market_relative_return_pp":17.8,"trigger_outcome_label":"Stage2_Actionable_with_required_4B_overlay","promote_to":"Stage2-Actionable+4B"}
{"trigger_id":"r13_koreazinc_T1","case_id":"r13_loop15_redteam_korea_zinc_control_battle","trigger_type":"control_premium_4B","trigger_date":"2024-09-13","evidence_available":"MBK/Young Poong tender offer at KRW660,000; Korea Zinc +19.8%, Young Poong +30%","event_return_pct":19.8,"trigger_outcome_label":"control_premium_not_operating_rerating","promote_to":"4B-watch"}
{"trigger_id":"r13_koreazinc_T2","case_id":"r13_loop15_redteam_korea_zinc_control_battle","trigger_type":"governance_dilution_4C_watch","trigger_date":"2024-11-06","evidence_available":"FSS revision order on Korea Zinc $1.8B share sale plan; shares fell as much as 8%","event_return_pct":-8,"trigger_outcome_label":"governance_dilution_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r13_lgcns_T1","case_id":"r13_loop15_redteam_lg_cns_evidence_price_fail","trigger_type":"evidence_good_but_price_failed","trigger_date":"2025-02-05","evidence_available":"Cloud/AI 54% sales, IPO raised 1.2T won, but debut traded at 59,700 below 61,900 issue price","event_return_pct":-3.55,"trigger_outcome_label":"evidence_good_but_price_failed","promote_to":"Stage2_only"}
{"trigger_id":"r13_security_T1","case_id":"r13_loop15_redteam_platform_security_4c","trigger_type":"hard_4C_security","trigger_date":"2025-07-04/2025-12-01","evidence_available":"SKT negligent data leak, -5.6%, 26.96M data pieces; Coupang 33.7M accounts, -4.4% premarket","event_return_pct":"SKT -5.6 / Coupang -4.4","trigger_outcome_label":"hard_4C_success","promote_to":"4C"}
{"trigger_id":"r13_jejuair_T1","case_id":"r13_loop15_redteam_jeju_air_safety_4c","trigger_type":"hard_4C_operational_safety","trigger_date":"2024-12-30","evidence_available":"Jeju Air crash killed 179; shares fell as much as 15.7% to KRW6,920; market cap loss 95.7B won","event_return_pct":-15.7,"trigger_outcome_label":"hard_4C_success","promote_to":"4C"}
{"trigger_id":"r13_chicken_T1","case_id":"r13_loop15_redteam_jensen_chicken_meme","trigger_type":"price_moved_without_evidence","trigger_date":"2025-10-31","evidence_available":"Jensen Huang dined at non-listed Kkanbu Chicken; listed chicken/robot names surged without direct revenue or equity purchase","event_return_pct":"no_valid_stage3_entry","trigger_outcome_label":"price_moved_without_evidence","promote_to":"N/A"}
```

## data/sector_taxonomy/score_weight_profiles_round236_r13_loop15_v1.csv 초안

```csv
archetype,evidence_to_earnings_bridge,market_relative_event_strength,delivery_to_revenue_conversion,actual_capacity_or_shipment,platform_security_trust,operational_safety_trust,governance_dilution_quality,price_evidence_disagreement,headline_only_penalty,control_premium_as_rerating_penalty,cb_capital_without_backlog_penalty,celebrity_meme_event_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
EARLY_EVIDENCE_MISSED_STRUCTURAL,+5,+4,+3,+5,+0,+0,+1,+2,-4,-1,-1,-2,ASP+shipment+capacity+OP estimate,reported earnings confirmation pending,actual earnings+favorable OHLC,Samyang template.
DELIVERY_TO_REVENUE_STAGE2_YELLOW,+5,+5,+5,+2,+0,+0,+1,+1,-3,-1,-1,-1,delivery+revenue+OP estimate,multi-quarter margin pending,cash collection+margin+OHLC,Hyundai Rotem template.
STRATEGIC_CAPITAL_WITH_DILUTION_4B,+3,+5,+1,+1,+1,+0,+5,+2,-3,-2,-5,-1,strategic capital+price strength,order backlog/dilution pending,backlog+margin+conversion clarity,Samsung SDS template.
CONTROL_BATTLE_GOVERNANCE_4B_4C,+1,+4,+0,+0,+0,+0,+5,+5,-2,-5,-3,-1,control premium,governance/dilution/regulator risk,clean governance+cashflow,Korea Zinc template.
EVIDENCE_GOOD_BUT_PRICE_FAILED,+3,+0,+1,+2,+1,+0,+1,+5,-3,-1,-1,-1,good evidence but weak price,price confirmation missing,price recovery+earnings proof,LG CNS template.
PLATFORM_SECURITY_HARD_4C,+0,+0,+0,+0,+5,+1,+3,+5,-1,-1,-1,-1,data breach,trust recovery pending,security restored+revenue stabilized,SKT/Coupang template.
OPERATIONAL_SAFETY_HARD_4C,+0,+0,+0,+0,+1,+5,+2,+5,-1,-1,-1,-1,fatal safety incident,investigation/remediation pending,safety trust recovered,Jeju Air template.
PRICE_MOVED_WITHOUT_EVIDENCE,+0,+3,+0,+0,+0,+0,+0,+5,-5,-1,-1,-5,price move without revenue evidence,no evidence,N/A,Kyochon/Jensen template.
OHLC_BACKFILL_SEPARATION_REQUIRED,+0,+0,+0,+0,+0,+0,+0,+5,0,0,0,0,stage row separate from OHLC row,backfill pending,full MFE/MAE calculated,Production architecture rule.
```

---

# 이번 R13 Loop 15 결론

```text
1. Samyang과 Hyundai Rotem은 old Stage3 gate가 너무 보수적이었다는 증거다.
   ASP/shipment/capacity/OP estimate 또는 delivery/revenue/OP estimate가 닫히면 Stage2-Actionable 또는 Yellow 후보로 올려야 한다.

2. Samsung SDS는 Stage2-Actionable이 맞지만, CB/dilution/order backlog가 남아 있으므로 4B 병기가 필수다.

3. Korea Zinc는 control premium을 operating rerating으로 착각하면 안 되는 case다.
   tender offer는 price event지만, share sale/regulator intervention은 governance 4B/4C다.

4. LG CNS는 evidence가 좋아도 price가 거부하면 Green을 주면 안 된다는 case다.

5. SK Telecom과 Coupang은 platform security hard 4C다.
   고객 데이터가 깨지면 scale은 moat가 아니라 damage multiplier가 된다.

6. Jeju Air는 operational safety hard 4C다.
   안전사고는 항공·레저 demand trigger보다 먼저 차감해야 한다.

7. Kyochon/Cherrybro/Neuromeka는 price_moved_without_evidence다.
   가격상승이 evidence를 대신할 수 없다.

8. production 구조상 case_library, trigger_calibration, ohlc_backfill을 분리해야 한다.
   OHLC 미확보 때문에 Stage 후보를 강등하면 연구가 너무 보수적으로 변한다.
```

한 문장으로 압축하면:

> **R13 Loop 15의 핵심은 “Stage를 더 보수적으로 하자”가 아니라, 좋은 early evidence는 더 빨리 Yellow 후보로 올리고, headline·control premium·CB·meme·security/safety risk는 더 빨리 4B/4C로 분리하자는 것이다. 다음 R1 Loop 16부터는 `case row`, `trigger row`, `OHLC backfill row`를 분리하는 방식으로 연구해야 한다.**

[1]: https://www.marketwatch.com/story/samyang-foods-set-to-post-strong-2q-earnings-market-talk-d654e045?utm_source=chatgpt.com "Samyang Foods Set to Post Strong 2Q Earnings -- Market Talk"
[2]: https://www.wsj.com/articles/hyundai-rotem-rallies-on-hopes-tank-exports-will-boost-earnings-9322d840?utm_source=chatgpt.com "Hyundai Rotem Rallies on Hopes Tank Exports Will Boost Earnings"
[3]: https://www.reuters.com/world/asia-pacific/kkr-buy-820-million-samsung-sds-convertible-bonds-shares-jump-20-2026-04-15/?utm_source=chatgpt.com "KKR to buy $820 million of Samsung SDS convertible bonds, shares jump 20%"
[4]: https://www.reuters.com/markets/deals/private-equity-mbk-young-poong-launch-15-bln-tender-offer-korea-zinc-shares-2024-09-13/?utm_source=chatgpt.com "Private equity MBK, Young Poong launch $1.5 bln tender offer for Korea Zinc shares"
[5]: https://www.reuters.com/markets/deals/korea-zincs-share-sale-plan-suspended-due-regulators-revision-request-filing-2024-11-06/?utm_source=chatgpt.com "Korea Zinc's $1.8 bln share sale plan suspended due to regulator's revision order"
[6]: https://www.reuters.com/technology/skorean-tech-services-firm-lg-cns-falls-stock-market-debut-2025-02-05/?utm_source=chatgpt.com "South Korean tech services firm LG CNS drops in market debut"
[7]: https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-orders-sk-telecom-strengthen-data-security-after-leak-2025-07-04/?utm_source=chatgpt.com "South Korea penalises 'negligent' SK Telecom over major data leak"
[8]: https://www.barrons.com/articles/coupang-stock-price-data-breach-aad847d8?utm_source=chatgpt.com "Online Retailer Coupang Owns Up to Big Blunder. The Stock Drops."
[9]: https://www.reuters.com/business/aerospace-defense/jeju-air-shares-plunge-record-low-after-deadly-plane-crash-2024-12-30/?utm_source=chatgpt.com "Jeju Air shares plummet to record low after deadly plane crash"
[10]: https://www.marketwatch.com/story/jensen-huang-spreads-nvidia-magic-to-fried-chicken-stocks-06b49648?utm_source=chatgpt.com "Jensen Huang spreads Nvidia magic to fried-chicken stocks"
