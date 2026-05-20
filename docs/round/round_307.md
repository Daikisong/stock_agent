순서상 이번은 **R12 Loop 15 — 농업·생활서비스·기타 trigger-level price validation 라운드**다.

이번 R12는 범위가 넓다. 그래서 핵심은 “잡테마”를 많이 늘리는 게 아니라, **농업 투입재·비료·에듀테크·사교육·생활 플랫폼·배달·아동 콘텐츠·폐기물/재활용·가격규제**가 실제로 EPS/OP/FCF로 연결됐는지, 아니면 정책/사회 이벤트/규제/보안 리스크였는지를 분리하는 것이다.

```text
round = R12 Loop 15
round_id = round_235
large_sector = AGRICULTURE_LIFE_SERVICES_MISC
method = trigger_level_backtest_v1
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R13 Loop 15
```

이번에도 KRX/Naver/Yahoo/Stooq의 수정주가 일봉 OHLC 30D/90D/180D/1Y window를 안정적으로 직접 추출하지 못했다. 그래서 full MFE/MAE는 만들지 않고 `price_data_unavailable_after_deep_search`로 둔다. 대신 Reuters/FT/AP/Barron’s/Times가 보도한 **reported event return, IPO price, debut return, policy trigger, affected users, market share, demand/price data, regulatory reversal**를 trigger anchor로 쓴다. 계산 불가능한 MFE/MAE는 만들지 않는다.

---

# 1. 이번 라운드 대섹터

```text
R12 = 농업·생활서비스·기타
```

R12의 core gate는 아래다.

```text
농업·비료:
공급차질 → 국제가격 → 국내 원가/ASP → 수입대체/재고 → 농가 수요 → 실제 매출/마진

농기계·스마트팜:
정책/로봇/자율주행 → 북미·국내 판매 → dealer inventory → ASP/margin → 반복수요

교육·에듀테크:
정책 도입 → 교재/디바이스 채택 → 학교·학원 계약 → 유료 이용률 → 교사/학부모 반발 → rollback risk

사교육·생활서비스:
구조적 수요 → 이용자 수/ARPU → 규제/정치 반발 → 출생률·가계부담 → 지속성

배달·이커머스:
M&A/시장점유율 → 수수료/take-rate → 규제·데이터보안 → 고객 이탈 → 보상비용

아동 콘텐츠·에듀테인먼트:
IP hit → recurring licensing/merchandise → 후속 IP → 글로벌 확장 → one-hit-wonder valuation risk

폐기물·재활용:
정책/플라스틱 규제 → 처리단가 → 원가/탄소비용 → 실제 재활용률 → 정부 위탁/cleanup liability
```

---

# 2. 대상 canonical archetype

```text
FERTILIZER_EXPORT_CONTROL_STAGE2_EVENT
AGRI_FEED_PRICE_INPUT_COST_4C_WATCH
AI_TEXTBOOK_POLICY_STAGE2_WITH_ROLLBACK_4C
HAGWON_PRIVATE_EDUCATION_STRUCTURAL_STAGE2
FOOD_DELIVERY_MA_STAGE2_WITH_REGULATORY_4B
ECOMMERCE_DATA_BREACH_HARD_4C
CHILDREN_IP_EDUTAINMENT_IPO_STAGE2_WITH_4B
PLASTIC_RECYCLING_POLICY_FALSE_POSITIVE
SHRINKFLATION_PRICE_REGULATION_4C_WATCH
```

---

# 3. deep sub-archetype

```text
비료 / 식량안보:
- China fertilizer export restrictions
- urea / phosphate / nitrogen-potassium blends
- China exported more than $13B fertilizer
- 40% urea price rise from pre-war levels
- only ammonium sulphate still broadly exportable
- Korea urea supply-chain memory from 2021
- Namhae Chemical / KG Chemical / Chobi / fertilizer basket는 직접 가격자료 미확보

사료 / 곡물:
- Korea Feed Leaders Committee 65,000t feed wheat tender no purchase
- Cargill lowest offer $298.50/t C&F
- high price offers due wheat futures / U.S. harvest concerns
- feed and livestock input-cost 4C-watch

에듀테크 / AI textbook:
- AI digital textbooks planned for 2025
- backlash from parents and academics
- 50,000+ parents petition against
- 2025 National Assembly rollback: official textbook → supplementary materials
- school phone/digital-device ban effective March 2026

사교육 / hagwon:
- 47.6% under-six children in cram schools
- 25% under-two children
- preschool hagwon monthly average Won332k
- English kindergarten monthly average Won1.5m
- structural demand but political/social/regulatory pressure

음식배달:
- Uber/Naver consortium reportedly bids up to 8T won for Baemin
- Uber 80%, Naver 20%
- Delivery Hero shares +5.6% after Uber stake increase
- Naver says teaser letter received, no decision
- M&A optionality, not Green

이커머스 / 보안:
- Coupang 33.7M customer accounts / more than 33M personal info
- stock -4.4% premarket after breach
- CEO resignation
- later +9% relief after limited-data update
- Korean e-commerce/life-service hard security reference

아동 콘텐츠 / 에듀테인먼트:
- Pinkfong IPO
- IPO price 38,000 won
- shares +62% intraday to 61,500 won, close +9% at 41,550 won
- 76B won raised
- Baby Shark 16B+ YouTube views
- operating profit 18.8B won on 97.4B won sales
- one-hit-wonder / valuation 4B

폐기물·재활용:
- Korea claims 73% plastic recycling rate but Greenpeace estimate true recycling 27%
- plastic waste +31% from 2019 to 2022
- Asan site 19,000 tonnes untreated plastic waste
- cleanup cost 2~3B won
- policy theme but economics poor
```

---

# 4. 선정 case 요약

| bucket                        | case                           | 핵심 판정                                                                                                              |
| ----------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| Stage2 event / 4B             | Fertilizer export controls     | China fertilizer export restrictions, urea/fertilizer price shock. 국내 비료 basket은 price unavailable, Stage2 event로만 |
| 4C-watch                      | Feed wheat tender / input cost | Korea FLC 65,000t tender no purchase due high offers. 축산·사료 input-cost 4C                                          |
| Stage2 + hard rollback 4C     | AI digital textbook / edtech   | 2025 도입 계획 → 학부모 반발 → official textbook 지위 박탈. 에듀테크 Green 금지                                                       |
| Stage2 structural / 4B-social | Hagwon preschool demand        | under-six 47.6% hagwon, average Won332k. 구조적 수요지만 규제/저출산 부담                                                        |
| Stage2 M&A / 4B               | Naver-Uber / Baemin            | 8T won possible bid, Naver 20% consortium. final decision·take-rate·KFTC 전에는 Green 아님                              |
| hard 4C                       | Coupang data breach            | 33M+ customers, -4.4% premarket, CEO resignation, special audit. 생활플랫폼 보안 hard gate                                |
| Stage2-Actionable + 4B        | Pinkfong IPO                   | +62% intraday, close +9%, Baby Shark IP. 후속 IP/라이선싱 전에는 one-hit-wonder 4B                                          |
| false-positive watch          | Plastic recycling / waste      | recycling policy theme but true recycling and cleanup economics weak. 폐기물주는 처리단가/계약 전 Green 금지                     |

---

# 5. Case별 trigger grid

## Case A — Fertilizer export controls / Korean fertilizer basket

```text
symbols = 025860 / 001390 / 001550 / fertilizer_basket
company_scope = Namhae Chemical / KG Chemical / Chobi / fertilizer-input basket
case_type = Stage2 event / 4B supply-shock watch
archetype = FERTILIZER_EXPORT_CONTROL_STAGE2_EVENT
```

| trigger | type                        |       date | 당시 공개 evidence                                                                                                                          | 가격 anchor                    | outcome                  |
| ------- | --------------------------- | ---------: | --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | ------------------------ |
| T0      | awareness                   |  2021~2024 | Korea suffered urea supply crunch from China export restrictions; urea is both fertilizer and diesel-emission raw material              | no KRX price                 | Stage1                   |
| T1      | Stage2 evidence             | 2026-03-19 | China restricts nitrogen-potassium blends and some phosphate fertilizers; only limited products like ammonium sulphate still exportable | KRX basket price unavailable | Stage2 event             |
| T2      | Stage2-Actionable candidate | 2026-03-19 | China exported >$13B fertilizer; restrictions may affect half to three-quarters of exports, up to 40M tons                              | no KRX price                 | candidate, price missing |
| T3      | 4B-watch                    | 2026-04-28 | China tightens border inspections even on ammonium sulphate; false declarations of urea/potash suspected                                | no KRX price                 | supply-chain 4B          |
| T4      | Stage3-Yellow               |        N/A | domestic ASP, inventory, margin, actual Korean company sales not confirmed                                                              | N/A                          | no Yellow                |

Fertilizer export-control trigger는 R12 agriculture-input Stage2다. Reuters는 China가 domestic market을 보호하기 위해 nitrogen-potassium blends와 phosphate varieties export를 제한했고, China가 전년 $13B 이상 fertilizer를 수출한 주요 supplier라고 보도했다. restrictions는 China fertilizer exports의 절반~3/4, 최대 40M tons에 영향을 줄 수 있고, international urea prices는 pre-war levels 대비 약 40% 올랐다고 설명했다. 이건 Korean fertilizer basket에 event premium을 줄 수 있는 trigger지만, domestic ASP·inventory·margin·listed-company sales가 없으면 Stage3가 아니다. ([Reuters][1])

4월 Reuters는 China가 ammonium sulphate까지 customs inspection을 강화했다고 보도했다. 이유는 restricted urea/potash가 ammonium sulphate로 false declaration 되는 사례가 발견됐기 때문이다. 따라서 이 case는 공급차질 event로는 강하지만, 국내 listed fertilizer companies에 대한 직접 가격/실적 연결이 확인되지 않아 `Stage2 event + 4B supply-chain watch`로 둔다. ([Reuters][2])

```json
{
  "case_id": "r12_loop15_fertilizer_export_control_korea_basket",
  "symbols": "025860/001390/001550/fertilizer_basket",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2_event_with_4B_supply_watch",
  "trigger_date": "2026-03-19/2026-04-28",
  "china_fertilizer_exports_usd_bn": 13,
  "potential_export_restriction_volume_mn_tons": 40,
  "restricted_export_share_range_pct": "50-75",
  "international_urea_price_rise_from_prewar_pct": 40,
  "ammonium_sulphate_inspection_tightening": true,
  "korea_urea_supply_crunch_memory_2021": true,
  "direct_krx_price_anchor": "price_data_unavailable_after_deep_search",
  "sources_checked": [
    "Reuters China fertilizer export restrictions 2026-03-19",
    "Reuters China customs fertilizer inspection 2026-04-28",
    "KRX/Naver keyword searches for Namhae Chemical/KG Chemical/Chobi event prices"
  ],
  "stage3_gate_missing": [
    "domestic_fertilizer_ASP",
    "inventory_available_for_sale",
    "Korean_company_import_mix",
    "margin_pass_through",
    "actual_sales_volume"
  ],
  "trigger_outcome_label": "Stage2_event_not_Green"
}
```

---

## Case B — Korea feed wheat tender failure / agriculture input-cost 4C

```text
symbols = feed_livestock_food_cost_basket
company_scope = feed makers / livestock processors / food-service input-cost read-through
case_type = 4C-watch
archetype = AGRI_FEED_PRICE_INPUT_COST_4C_WATCH
```

| trigger | type          |       date | 당시 공개 evidence                                                                                         | 가격 anchor              | outcome       |
| ------- | ------------- | ---------: | ------------------------------------------------------------------------------------------------------ | ---------------------- | ------------- |
| T0      | awareness     |    2026-05 | wheat futures and crop-supply risk raise import-cost pressure                                          | no stock price         | watch         |
| T1      | 4C-watch      | 2026-05-13 | Korea Feed Leaders Committee believed to make no purchase in 65,000t feed wheat tender due high offers | no listed basket price | input-cost 4C |
| T2      | validation    | 2026-05-13 | lowest offer Cargill $298.50/t C&F, plus $2/t extra unloading surcharge                                | no stock price         | validated     |
| T3      | Stage2 relief |        N/A | lower import price / successful tender not confirmed                                                   | N/A                    | no relief     |

Reuters reported that South Korea’s Feed Leaders Committee was believed to have made no purchase in a tender for up to 65,000 metric tons of animal feed wheat because of high price offers. The lowest offer, from Cargill, was $298.50/t cost-and-freight plus a $2/t surcharge for extra port unloading. This is not a growth trigger; it is an input-cost 4C-watch for feed/livestock/food-service chains. ([Reuters][3])

```json
{
  "case_id": "r12_loop15_feed_wheat_tender_input_cost",
  "symbols": "feed_livestock_food_cost_basket",
  "best_trigger": "T1/T2",
  "best_trigger_type": "4C_watch_input_cost",
  "trigger_date": "2026-05-13",
  "feed_wheat_tender_volume_tons": 65000,
  "purchase_result": "believed_no_purchase",
  "lowest_offer_cargill_usd_per_ton_cnf": 298.5,
  "extra_unloading_surcharge_usd_per_ton": 2.0,
  "reason": "high_price_offers_due_wheat_futures_and_harvest_concerns",
  "direct_krx_price_anchor": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "agri_input_cost_4C_watch"
}
```

---

## Case C — AI digital textbooks / Korean edtech policy rollback

```text
symbols = 095720 / 133750 / 289010 / 095720_readthrough / edtech_basket
company_scope = Woongjin ThinkBig / MegaStudy Education / Icecream Edu / YBM Net / education-content basket
case_type = Stage2 policy with hard rollback 4C
archetype = AI_TEXTBOOK_POLICY_STAGE2_WITH_ROLLBACK_4C
```

| trigger | type             |       date | 당시 공개 evidence                                                                                                     | 가격 anchor             | outcome               |
| ------- | ---------------- | ---------: | ------------------------------------------------------------------------------------------------------------------ | --------------------- | --------------------- |
| T0      | Stage2 awareness | 2024-08-18 | Korea planned AI-powered digital textbooks from 2025 for children as young as 8; Samsung/LG-linked tools mentioned | no direct stock price | Stage2 policy         |
| T1      | 4B/social watch  | 2024-08-18 | 50,000+ parents petition; concerns over screen time, misinformation, hallucination, privacy                        | no price              | backlash watch        |
| T2      | hard rollback 4C | 2025-08-04 | National Assembly reclassifies AI textbooks from official textbooks to supplementary materials                     | no direct stock price | policy rollback       |
| T3      | 4C validation    | 2025-08-27 | Korea passes classroom mobile/digital-device ban effective March 2026, with educational exceptions                 | no price              | digital education cap |
| T4      | Stage3-Yellow    |        N/A | actual school contracts / paid adoption / teacher acceptance not confirmed                                         | N/A                   | no Yellow             |

AI digital textbook은 R12 education-policy에서 “정책 발표만으로 Green을 주면 안 된다”는 case다. FT는 South Korea가 2025년부터 AI-powered digital textbooks를 도입하려 했고, 아이들이 8세부터 tablet-loaded AI features를 쓸 예정이었다고 보도했다. 하지만 부모와 academics의 반발이 컸고, 50,000명 넘는 부모가 petition을 냈으며, misinformation, hallucination, privacy, screen exposure 우려가 제기됐다. ([Financial Times][4])

이후 Business Insider는 2025년 8월 4일 National Assembly가 AI textbooks의 법적 지위를 official classroom textbooks에서 supplementary materials로 낮추는 amendment를 통과시켰다고 보도했다. 이는 policy rollback hard 4C다. Reuters도 한국이 2026년 3월부터 교실 내 mobile phones and digital devices 사용을 금지하는 법을 통과시켰다고 보도했다. 교육목적 예외는 있지만, edtech adoption에는 분명한 4C overlay다. ([Business Insider][5])

```json
{
  "case_id": "r12_loop15_ai_digital_textbook_policy_rollback",
  "symbols": "095720/133750/289010/edtech_basket",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_policy_with_rollback_4C",
  "t0_date": "2024-08-18",
  "planned_rollout_year": 2025,
  "target_age_context": "as_young_as_8",
  "parent_petition_count": ">50000",
  "risks": [
    "screen_overexposure",
    "misinformation",
    "AI_hallucination",
    "privacy",
    "teacher_workload"
  ],
  "t2_date": "2025-08-04",
  "rollback": "official_textbook_to_supplementary_material",
  "t3_date": "2025-08-27",
  "classroom_mobile_digital_device_ban_effective": "2026-03",
  "direct_krx_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "school_contracts",
    "paid_adoption",
    "teacher_acceptance",
    "learning_outcome_data",
    "privacy_safety_certification"
  ],
  "trigger_outcome_label": "policy_rollback_4C_watch"
}
```

---

## Case D — Hagwon / preschool private-education structural demand

```text
symbols = 215200 / 019680 / 095720 / 133750 / private_education_basket
company_scope = MegaStudy Education / Daekyo / Woongjin ThinkBig / Creverse / hagwon basket
case_type = structural Stage2 with social/regulatory 4B
archetype = HAGWON_PRIVATE_EDUCATION_STRUCTURAL_STAGE2
```

| trigger | type              |       date | 당시 공개 evidence                                                                         | 가격 anchor             | outcome                |
| ------- | ----------------- | ---------: | -------------------------------------------------------------------------------------- | --------------------- | ---------------------- |
| T0      | Stage2 structural | 2025-03-16 | 47.6% of under-six children in hagwon; 25% of under-two children also attend           | no direct stock price | structural demand      |
| T1      | Stage2 validation | 2025-03-16 | preschool monthly tuition average Won332k; English kindergartens average Won1.5m/month | no price              | ARPU evidence          |
| T2      | 4B/social watch   | 2025-03-16 | record private education spending worsens family burden, household debt, low birthrate | no price              | social/regulatory risk |
| T3      | Stage3-Yellow     |        N/A | listed-company enrollment/ARPU/OP margin not confirmed                                 | N/A                   | no Yellow              |

Hagwon/private education is structurally strong but politically fragile. FT reported that 47.6% of South Korean children under six attend cram schools, and even 25% of children under two attend. Average monthly tuition for preschoolers was Won332,000, while English-specialized kindergartens averaged Won1.5mn per month. This is real structural demand and ARPU evidence. ([Financial Times][6])

But the same facts are also a 4B/social risk. The burden feeds household-debt and birthrate concerns, so listed education companies need enrollment growth, ARPU, margin and policy tolerance before Stage3. ([Financial Times][6])

```json
{
  "case_id": "r12_loop15_hagwon_preschool_private_education",
  "symbols": "215200/019680/095720/133750/private_education_basket",
  "best_trigger": "T0/T1",
  "best_trigger_type": "Stage2_structural_with_4B_social_overlay",
  "trigger_date": "2025-03-16",
  "under_six_hagwon_enrollment_pct": 47.6,
  "under_two_hagwon_enrollment_pct": 25,
  "preschool_monthly_tuition_avg_krw": 332000,
  "english_kindergarten_monthly_tuition_avg_krw": 1500000,
  "direct_krx_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "listed_company_enrollment_growth",
    "ARPU_growth",
    "teacher_cost_control",
    "operating_margin",
    "policy_tolerance"
  ],
  "trigger_outcome_label": "structural_stage2_with_social_4B"
}
```

---

## Case E — Naver / Uber / Baemin food-delivery M&A

```text
symbols = 035420 / Baemin_private / Delivery_Hero_readthrough
company_scope = Naver / Uber / Baedal Minjok / Delivery Hero
case_type = Stage2 M&A optionality with regulatory 4B
archetype = FOOD_DELIVERY_MA_STAGE2_WITH_REGULATORY_4B
```

| trigger | type                 |       date | 당시 공개 evidence                                                                                 | 가격 anchor               | outcome             |
| ------- | -------------------- | ---------: | ---------------------------------------------------------------------------------------------- | ----------------------- | ------------------- |
| T0      | awareness            | 2026-05-18 | Uber and Naver consortium reportedly bids up to 8T won for Baemin                              | Naver price unavailable | Stage2 M&A          |
| T1      | Stage2 validation    | 2026-05-18 | Uber 80%, Naver 20% consortium; target is 100% stake in Korea’s largest food delivery platform | no Naver price          | candidate           |
| T2      | 4B-watch             | 2026-05-18 | Naver says teaser letter received but no decision; KFTC/take-rate/fee regulation gate          | no Naver price          | 4B                  |
| T3      | related price anchor | 2026-05-18 | Delivery Hero shares +5.6% after Uber raises stake to 19.5%                                    | DHER +5.6%              | global read-through |
| T4      | Stage3-Yellow        |        N/A | final acquisition / regulatory approval / monetization not confirmed                           | N/A                     | no Yellow           |

Baemin case는 R12 생활서비스 M&A Stage2다. Reuters는 Uber와 Naver가 8T won, 약 $5.34B까지 제안하는 consortium을 만들어 Baedal Minjok 100% stake를 인수하려 한다고 보도했다. Uber와 Naver의 지분 구조는 80:20으로 언급됐고, Naver는 teaser letter를 받았지만 결정된 것은 없다고 밝혔다. 이건 food-delivery consolidation optionality지, Green이 아니다. ([Reuters][7])

같은 날 Reuters는 Uber가 Delivery Hero 지분을 7%에서 19.5%로 늘려 최대주주가 됐고, Delivery Hero shares가 5.6% 올랐다고 보도했다. FT도 Uber의 Delivery Hero 지분이 19.5%와 5.6% options로 늘어나면서 blocking minority 성격을 갖는다고 설명했다. 다만 Korea Baemin deal은 아직 final bid/approval/take-rate economics가 없다. ([Reuters][8])

```json
{
  "case_id": "r12_loop15_naver_uber_baemin_food_delivery_ma",
  "symbols": "035420/Baemin_private/Delivery_Hero_readthrough",
  "best_trigger": "T0/T3",
  "best_trigger_type": "Stage2_MA_optionality_with_4B_regulatory_overlay",
  "trigger_date": "2026-05-18",
  "reported_baemin_bid_krw_trn": 8.0,
  "reported_baemin_bid_usd_bn": 5.34,
  "consortium_split": {
    "Uber_pct": 80,
    "Naver_pct": 20
  },
  "target": "100%_Baedal_Minjok",
  "naver_decision_status": "teaser_letter_received_no_final_decision",
  "delivery_hero_uber_stake_after_pct": 19.5,
  "delivery_hero_event_return_pct": 5.6,
  "direct_naver_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "final_binding_bid",
    "KFTC_approval",
    "funding_structure",
    "commission_take_rate",
    "merchant_fee_regulation",
    "customer_retention",
    "delivery_cost_synergy"
  ],
  "trigger_outcome_label": "Stage2_MA_not_Green"
}
```

---

## Case F — Coupang data breach / life-service security hard 4C

```text
symbol = CPNG / Korea e-commerce read-through
company_scope = Coupang / Korean e-commerce and life-service platform reference
case_type = hard 4C with relief bounce
archetype = ECOMMERCE_DATA_BREACH_HARD_4C
```

| trigger | type                     |       date | 당시 공개 evidence                                                                       | 가격 anchor                         | outcome          |
| ------- | ------------------------ | ---------: | ------------------------------------------------------------------------------------ | --------------------------------- | ---------------- |
| T0      | hard 4C                  | 2025-12-01 | data breach disclosed; 33.7M customer accounts exposed                               | CPNG -4.4% premarket              | hard 4C          |
| T1      | 4C validation            | 2025-12-10 | CEO resigns; more than 33M customers’ personal info; police raid / government probe  | CPNG down >4% since Nov 30 per FT | validation       |
| T2      | further regulatory watch | 2025-12-22 | tax agency special audit after data leak, regulators/police probing                  | no new price                      | governance watch |
| T3      | false-break relief       | 2025-12-26 | stock +9% after company says limited retained data and no payment/login/customs data | +9%                               | relief           |
| T4      | Stage3                   |        N/A | not growth trigger                                                                   | N/A                               | N/A              |

Coupang is not KRX-listed, but it is Korea’s dominant life-service platform and a useful R12 hard-gate reference. Barron’s reported Coupang stock was down 4.4% in premarket trading after the company confirmed a data breach affecting about 33.7M Korean customer accounts. The compromised data included names, emails, phone numbers and certain order information, while payment/login information was not accessed. ([Barron's][9])

FT later reported the CEO resigned after a breach exposing personal information of more than 33M customers, causing backlash, customer exodus, police raids and government probe. Reuters then reported the National Tax Service conducted a special audit related to the breach and Coupang’s transactions with its U.S.-listed parent. A later update triggered a relief bounce, with Investopedia reporting the shares rose about 9% after Coupang said the retained data was limited and no payment/login/customs data had been compromised. ([Financial Times][10])

```json
{
  "case_id": "r12_loop15_coupang_data_breach_life_service_4c",
  "symbols": "CPNG/Korea_ecommerce_readthrough",
  "best_trigger": "T0/T3",
  "best_trigger_type": "hard_4C_with_false_break_relief",
  "t0_date": "2025-12-01",
  "affected_customer_accounts_mn": 33.7,
  "premarket_event_return_pct": -4.4,
  "stock_performance_before_breach_ytd_pct": 28,
  "t1_date": "2025-12-10",
  "ceo_resignation": true,
  "government_probe": true,
  "police_raid": true,
  "t2_date": "2025-12-22",
  "tax_agency_special_audit": true,
  "t3_date": "2025-12-26",
  "relief_event_return_pct": 9,
  "limited_data_update": true,
  "payment_login_customs_data_compromised": false,
  "trigger_outcome_label": "hard_4C_security_with_false_break_relief"
}
```

---

## Case G — Pinkfong / Baby Shark edutainment IPO

```text
symbol = Pinkfong / Samsung Publishing read-through
company_scope = Pinkfong / Samsung Publishing read-through
case_type = Stage2-Actionable with 4B one-hit-wonder overlay
archetype = CHILDREN_IP_EDUTAINMENT_IPO_STAGE2_WITH_4B
```

| trigger | type                    |       date | 당시 공개 evidence                                                                                                        | 가격 anchor                             | outcome    |
| ------- | ----------------------- | ---------: | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------- | ---------- |
| T0      | awareness               |  2018~2025 | Baby Shark global IP, 16B+ YouTube views, Samsung Publishing read-through                                             | old Samsung Publishing +76% reference | Stage1     |
| T1      | Stage2 evidence         | 2025-11-05 | Pinkfong IPO priced at top of range, 38,000 won, 76B won raised                                                       | pre-listing                           | Stage2     |
| T2      | Stage2-Actionable       | 2025-11-18 | Pinkfong debut: +62% intraday to 61,500 won, close +9% at 41,550 won                                                  | +62% / +9%                            | Actionable |
| T3      | Stage3-Yellow candidate |    2025-11 | 2024 OP 18.8B won on 97.4B won sales; Bebefinn surpasses Baby Shark in some metrics                                   | no forward OHLC                       | candidate  |
| T4      | 4B-watch                |    2025-11 | one-hit-wonder concern, shares later slipped about one-tenth from opening-day pop, valuation around 25x 2025 earnings | no full OHLC                          | 4B         |
| T5      | Stage3-Green            |        N/A | recurring licensing/merchandise and next-IP durability not confirmed                                                  | N/A                                   | no Green   |

Pinkfong은 R12 아동 콘텐츠·에듀테인먼트에서 가장 명확한 Stage2-Actionable이다. FT는 Pinkfong shares가 IPO debut에서 intraday +62%로 61,500 won까지 오른 뒤, 종가는 +9%인 41,550 won이었다고 보도했다. IPO로 76B won을 조달했고, Baby Shark video는 16B+ views를 기록했다. ([Financial Times][11])

다만 이건 곧바로 Green이 아니다. FT는 “Baby Shark still has teeth” analysis에서 shares가 opening-day pop 이후 약 10% 밀렸고, 2025 earnings 약 25x valuation과 one-hit-wonder 우려를 언급했다. The Times는 Pinkfong이 38,000 won IPO price, 76B won raise, 270M combined subscribers, 2025 H1 operating margin 20%를 제시했지만, Baby Shark에 맞먹는 후속 hit는 아직 어렵다고 설명했다. 즉 Stage2-Actionable + 4B valuation/one-hit overlay다. ([Financial Times][12])

```json
{
  "case_id": "r12_loop15_pinkfong_babyshark_ipo",
  "symbols": "Pinkfong/Samsung_Publishing_readthrough",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable_with_4B_one_hit_overlay",
  "ipo_price_krw": 38000,
  "ipo_raise_krw_bn": 76,
  "debut_intraday_high_krw": 61500,
  "debut_intraday_mfe_pct": 62,
  "debut_close_krw": 41550,
  "debut_close_return_pct": 9,
  "baby_shark_youtube_views_bn": 16,
  "sales_2024_krw_bn": 97.4,
  "op_2024_krw_bn": 18.8,
  "combined_subscribers_mn_context": 270,
  "h1_2025_op_margin_pct_context": 20,
  "valuation_context_2025e_pe": 25,
  "stage3_gate_missing": [
    "next_IP_revenue",
    "licensing_merchandise_growth",
    "global_distribution_contracts",
    "recurring_subscription_revenue",
    "post_IPO_margin_durability"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_Actionable_IPO_with_4B_one_hit_risk"
}
```

---

## Case H — Plastic recycling / waste-management policy false-positive watch

```text
symbols = waste_recycling_basket / KG_ETS_readthrough / SK_ecoplant_private_readthrough
case_type = false_positive watch
archetype = PLASTIC_RECYCLING_POLICY_FALSE_POSITIVE
```

| trigger | type                 |       date | 당시 공개 evidence                                                                       | 가격 anchor       | outcome           |
| ------- | -------------------- | ---------: | ------------------------------------------------------------------------------------ | --------------- | ----------------- |
| T0      | Stage2 policy        | 2024-11-22 | Korea hosts/plans global plastic agreement talks; recycling narrative strong         | no stock price  | policy            |
| T1      | false-positive watch | 2024-11-22 | Korea claims 73% plastic recycling rate, but Greenpeace estimates true recycling 27% | no stock price  | economics problem |
| T2      | 4C/liability watch   | 2024-11-22 | Asan site has 19,000t untreated plastic waste; cleanup cost 2~3B won                 | no listed price | cleanup liability |
| T3      | Stage3-Yellow        |        N/A | treatment contracts / tipping fees / margin / pyrolysis economics not confirmed      | N/A             | no Yellow         |

Plastic recycling은 R12 폐기물 theme의 false-positive watch다. Reuters는 Korea가 plastic recycling efforts로 73% recycling rate를 주장하지만, Greenpeace는 실제 재활용률을 27%로 추정한다고 보도했다. 2019~2022년 plastic waste는 31% 증가했고, Asan의 shuttered recycling site에는 약 19,000 tonnes untreated plastic waste가 쌓여 있으며 cleanup cost는 2~3B won으로 추정됐다. ([Reuters][13])

따라서 “재활용 정책 = 폐기물주 Green”은 너무 빠르다. listed waste/recycling companies에는 treatment contracts, tipping fees, public cleanup budget, pyrolysis economics, carbon cost pass-through가 필요하다.

```json
{
  "case_id": "r12_loop15_plastic_recycling_policy_false_positive",
  "symbols": "waste_recycling_basket/KG_ETS_readthrough/SK_ecoplant_private_readthrough",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_policy_false_positive_watch",
  "trigger_date": "2024-11-22",
  "claimed_plastic_recycling_rate_pct": 73,
  "greenpeace_estimated_real_recycling_rate_pct": 27,
  "plastic_waste_growth_2019_2022_pct": 31,
  "asan_untreated_plastic_waste_tons": 19000,
  "estimated_cleanup_cost_krw_bn": "2-3",
  "direct_krx_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "government_cleanup_contract",
    "tipping_fee_visibility",
    "pyrolysis_margin",
    "carbon_cost_pass_through",
    "facility_utilization",
    "regulatory_enforcement_durability"
  ],
  "trigger_outcome_label": "policy_theme_false_positive_watch"
}
```

---

# 6. Trigger별 가격경로 검증 요약

| case                      | best trigger |                            entry anchor |                        event MFE/MAE | market-relative | full MFE/MAE | outcome                      |
| ------------------------- | ------------ | --------------------------------------: | -----------------------------------: | --------------: | ------------ | ---------------------------- |
| Fertilizer export control | T1/T3        |                  KRX basket unavailable | urea +40% vs pre-war, no stock price |             N/A | unavailable  | Stage2 event / 4B            |
| Feed wheat tender         | T1/T2        |                             unavailable |  no purchase, lowest offer $298.50/t |             N/A | unavailable  | input-cost 4C                |
| AI textbooks              | T0/T2        |                             unavailable |                       no stock price |             N/A | unavailable  | Stage2 policy → rollback 4C  |
| Hagwon demand             | T0/T1        |                             unavailable |      structural ARPU/enrollment data |             N/A | unavailable  | Stage2 structural / 4B       |
| Naver/Uber/Baemin         | T0/T3        |           Naver unavailable, DHER +5.6% |                  Delivery Hero +5.6% |       Naver N/A | unavailable  | Stage2 M&A / 4B              |
| Coupang breach            | T0/T3        |  CPNG premarket -4.4%, later +9% relief |                    -4.4%, +9% relief |             N/A | N/A          | hard 4C / false-break relief |
| Pinkfong IPO              | T1/T2        | 38,000 IPO / 61,500 high / 41,550 close |             +62% intraday, +9% close |             N/A | unavailable  | Stage2-Actionable + 4B       |
| Plastic recycling         | T0/T2        |                             unavailable |                       no stock price |             N/A | unavailable  | policy false-positive watch  |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
Fertilizer:
China export controls are Stage2 event, but Korean company ASP/margin not confirmed.

AI textbooks:
policy introduction was Stage2, but rollback made it 4C-watch.

Hagwon:
structural demand and ARPU are strong Stage2 evidence, but listed-company conversion missing.

Baemin/Naver:
M&A optionality is Stage2. Final bid, funding, KFTC approval and take-rate economics missing.
```

## Stage 2-Actionable entry 성과

```text
Pinkfong:
IPO +62% intraday / +9% close with global IP evidence.
Actionable, but one-hit-wonder and valuation 4B overlay.

Baemin/Naver:
Delivery Hero +5.6% on Uber stake-building is relevant global read-through, but Naver direct price missing.
```

## Stage3-Yellow 후보

```text
Pinkfong:
could become Yellow if Bebefinn/next IP, licensing, merchandise and margin durability confirm.

Hagwon:
could become Yellow if listed companies show enrollment/ARPU/OP margin growth despite regulation.

Fertilizer:
could become Yellow only if domestic ASP and margin pass-through appear in listed company results.

Baemin/Naver:
could become Yellow if binding acquisition, approval, take-rate and synergy close.
```

## Stage3-Green

```text
이번 R12 Loop 15에서 확정 Green 없음.

이유:
- fertilizer는 commodity event but company margin missing.
- edtech has policy rollback.
- hagwon has demand but social/regulatory risk.
- Baemin/Naver is not binding and no Naver price anchor.
- Coupang is hard security 4C.
- Pinkfong is strong IPO/IP event but post-IPO recurring revenue missing.
- recycling policy lacks economics.
```

---

# 8. score-price alignment 판정

```text
Stage2_promote_candidate:
- Pinkfong IPO
- Baemin/Naver M&A optionality, weaker due direct Naver price missing
- Fertilizer export-control basket, weaker due company price/margin missing
- Hagwon structural demand, if listed-company ARPU confirms

Stage3-Yellow candidate:
- Pinkfong, if post-IPO next-IP revenue and licensing confirm
- Baemin/Naver, if binding acquisition and take-rate economics confirm
- Fertilizer basket, if ASP/margin pass-through confirms

evidence_good_but_price_failed:
- AI textbook policy, because adoption plan was later rolled back
- Plastic recycling policy, because headline recycling rate hides weak true recycling economics

false_positive_score:
- AI textbook policy if treated as guaranteed edtech revenue
- Recycling policy if treated as immediate waste-company margin
- Baemin/Naver if teaser letter is treated as signed deal
- Fertilizer restrictions if domestic pass-through fails

price_moved_without_evidence:
- Any listed education/fertilizer stock that rises before contracts, ASP, or margin evidence

thesis_break_watch:
- AI textbook rollback
- classroom device ban
- Coupang data breach
- plastic recycling cleanup liability
- social pressure on hagwon spending

hard_4C_success:
- Coupang data breach, life-service platform security reference
```

---

# 9. 점수비중 교정

## 올릴 축

```text
domestic_ASP_margin_pass_through +5
inventory_and_import_mix_visibility +4
school_contract_paid_adoption +5
policy_rollback_risk +5
listed_company_enrollment_ARPU +4
platform_data_security_trust +5
binding_MA_approval_take_rate +5
recurring_IP_revenue +5
cleanup_contract_tipping_fee_visibility +5
```

### 근거

Fertilizer trigger는 global supply shock만으로는 부족하고 국내 ASP/margin이 필요하다. AI textbooks는 정책 발표보다 rollback risk가 더 중요했다. Hagwon은 structural demand가 있지만 listed-company ARPU가 필요하다. Baemin/Naver는 teaser letter와 reported bid가 아니라 binding acquisition/KFTC/take-rate가 gate다. Coupang은 customer data security가 생활서비스 platform의 hard gate임을 보여줬다. Pinkfong은 IPO pop보다 recurring IP revenue가 중요하다. Plastic recycling은 cleanup contract와 tipping fee가 없으면 정책 테마에 머문다.

## 내릴 축

```text
commodity_supply_shock_without_company_margin -5
edtech_policy_headline_without_school_contract -5
AI_textbook_without_teacher_parent_acceptance -5
hagwon_structural_demand_without_margin -3
M&A_teaser_without_binding_offer -5
platform_scale_without_security -5
viral_IP_without_next_franchise -4
recycling_rate_headline_without_economics -5
```

### 근거

AI textbook은 정책 headline이 있었지만 official textbook 지위를 잃었다. Coupang은 platform scale이 오히려 breach 피해 규모를 키웠다. Pinkfong은 +62% pop이 있었지만 one-hit-wonder risk가 남았다. Recycling은 official rate와 true economics가 크게 달랐다.

---

# 10. Stage 2-Actionable 승격 조건

R12 Loop 15 shadow rule:

```text
R12에서 Stage 2 evidence가 아래 중 3개 이상이면 Stage2-Actionable로 승격한다.

1. 정책/공급 shock이 국내 listed company의 ASP, margin, contract로 연결된다.
2. 학교/교육 정책은 actual contract, paid adoption, teacher acceptance가 확인된다.
3. 생활서비스 M&A는 binding offer, financing, approval path, take-rate economics가 확인된다.
4. platform/life service는 data-security trust가 훼손되지 않는다.
5. IP/edutainment는 IPO pop뿐 아니라 recurring licensing, merchandise, next-IP evidence가 있다.
6. waste/recycling은 cleanup contract, tipping fee, facility utilization, carbon-cost pass-through가 확인된다.
7. event 당일 market-relative +5pp 이상 가격반응이 있고, 그 반응이 공개 evidence와 연결된다.
```

적용:

```text
Pinkfong:
IPO pop + global IP + OP/sales evidence → Stage2-Actionable.
하지만 next-IP/revenue durability 전에는 Green 금지.

Baemin/Naver:
reported bid is Stage2, but binding offer / KFTC / economics before Actionable.

Fertilizer:
global supply shock is Stage2, but company margin/price unavailable → Actionable 보류.

AI textbook:
policy headline was Stage2 but rollback makes 4C-watch.
```

---

# 11. Stage 3-Yellow 조건

```text
Stage3-Yellow:
- R12 trigger가 EPS/OP/FCF 경로를 바꿀 가능성이 숫자로 보임
- 하지만 핵심 gate 하나가 남음
```

후보:

```text
Pinkfong:
recurring IP revenue and post-IPO margin confirm → Yellow.

Hagwon:
listed-company enrollment/ARPU and margin confirm despite regulation → Yellow.

Baemin/Naver:
binding acquisition and take-rate synergy confirm → Yellow.

Fertilizer:
domestic ASP/margin pass-through and inventory mix confirm → Yellow.
```

---

# 12. Stage 3-Green 조건

```text
Stage3-Green:
- 농업/비료는 supply shock이 실제 ASP/margin/volume으로 연결됨
- 에듀테크는 paid adoption, school contracts, teacher/parent acceptance가 닫힘
- 사교육은 enrollment, ARPU, margin이 지속되고 규제 리스크가 낮음
- 생활플랫폼은 M&A approval, take-rate, data-security trust가 닫힘
- IP는 one-hit이 아니라 recurring franchise revenue가 확인됨
- waste/recycling은 cleanup contracts and treatment economics가 확인됨
- full-window MFE/MAE가 우호적
```

이번 R12 Loop 15에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- commodity supply shock으로 비료주가 오르지만 domestic margin evidence 없음
- edtech policy announcement가 school adoption 전에 과열
- M&A teaser가 binding offer처럼 가격에 반영됨
- platform scale이 data-security risk를 무시하고 rerating
- viral IP IPO가 next-IP revenue 없이 급등
- recycling headline이 cleanup economics 없이 rerating
```

적용:

```text
Pinkfong:
+62% intraday IPO pop → 4B one-hit/valuation overlay.

Baemin/Naver:
reported 8T won bid but no final decision → 4B M&A teaser.

Fertilizer:
China export restriction but KRX margin missing → 4B supply-shock watch.

AI textbook:
policy backlash → rollback 4C, headline-only scoring 금지.
```

---

# 14. 4C hard gate 조건

```text
R12 4C:
- data breach / 개인정보 유출 / 플랫폼 신뢰 훼손
- policy rollback / official status downgrade
- school device ban reducing edtech adoption
- input-cost shock that cannot pass through
- cleanup liability without profitable treatment contract
- social backlash against education/childcare burden
- M&A blocked by regulator or merchant-fee politics
```

이번 R12 Loop 15 hard 4C:

```text
Coupang data breach = hard_4C_success
```

Strong 4C-watch:

```text
- AI textbook rollback
- classroom phone/digital-device ban
- feed wheat high-price tender failure
- plastic recycling cleanup liability
- platform data/security risk
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_235.md 요약

```md
# R12 Loop 15. Agriculture / Life Services / Misc Trigger-level Price Validation

이번 라운드는 R12 Loop 15 trigger-level validation 라운드다.

핵심 결론:
- Fertilizer export controls are Stage2 event, not Green. China restricted nitrogen-potassium blends and phosphate fertilizers; China exported more than $13B of fertilizer last year; restrictions may hit 50~75% of exports, potentially up to 40M tons. Urea prices are up around 40% from pre-war levels. Korean listed-company ASP/margin evidence was not found.
- Feed wheat tender failure is agri input-cost 4C-watch. Korea FLC made no purchase in a 65,000t feed wheat tender because offers were high; lowest offer was $298.50/t C&F plus $2/t unloading surcharge.
- AI digital textbook policy is Stage2 policy with rollback 4C. Korea planned AI textbooks from 2025 but faced 50k+ parent petition/backlash; in 2025, National Assembly downgraded AI textbooks from official textbooks to supplementary materials. Classroom mobile/digital-device ban effective March 2026 adds 4C overlay.
- Hagwon preschool demand is structural Stage2 with social/regulatory 4B. 47.6% of under-six children and 25% of under-two children attend cram schools; average preschool hagwon tuition is Won332k/month and English kindergartens average Won1.5mn/month.
- Naver/Uber/Baemin is Stage2 M&A optionality. Reported 8T won bid for 100% of Baemin via Uber 80% / Naver 20% consortium; Naver says no decision. Delivery Hero shares rose 5.6% after Uber increased its stake to 19.5%.
- Coupang data breach is hard life-service platform 4C. 33.7M customer accounts were affected; stock fell 4.4% premarket; CEO resigned; regulators, police and tax agency probes followed. Later +9% relief was false-break relief, not growth.
- Pinkfong IPO is Stage2-Actionable with 4B one-hit overlay. IPO price 38,000 won, intraday +62% to 61,500 won, close +9% at 41,550 won. Baby Shark has 16B+ views, but next-IP and recurring revenue are required for Yellow.
- Plastic recycling policy is false-positive watch. Korea claims 73% recycling rate, but Greenpeace estimates true recycling at 27%; plastic waste rose 31% from 2019 to 2022; Asan site holds 19,000t untreated plastic with 2~3B won cleanup cost.

Main calibration:
- Raise domestic_ASP_margin_pass_through, inventory_and_import_mix_visibility, school_contract_paid_adoption, policy_rollback_risk, listed_company_enrollment_ARPU, platform_data_security_trust, binding_MA_approval_take_rate, recurring_IP_revenue, cleanup_contract_tipping_fee_visibility.
- Lower commodity_supply_shock_without_company_margin, edtech_policy_headline_without_school_contract, AI_textbook_without_teacher_parent_acceptance, M&A_teaser_without_binding_offer, platform_scale_without_security, viral_IP_without_next_franchise, recycling_rate_headline_without_economics.
```

## docs/checkpoints/checkpoint_28a_round235_r12_loop15.md 요약

```md
# Checkpoint 28A Round 235 R12 Loop 15 Trigger-level Calibration

## 반영 내용
- R12 Loop 15 trigger-level validation을 수행했다.
- Fertilizer export controls, feed wheat tender failure, AI digital textbook rollback, hagwon structural demand, Naver/Uber/Baemin M&A, Coupang data breach, Pinkfong IPO, plastic recycling policy false-positive를 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 Reuters / FT / AP / Barron’s / Times의 reported event return과 event price anchor를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- 농업 input shock은 domestic ASP/margin pass-through 없으면 Stage2 event다.
- 에듀테크 policy는 school contract, paid adoption, parent/teacher acceptance가 없으면 Green 금지다.
- 생활플랫폼은 data security가 hard gate다.
- M&A teaser는 binding offer and approval 전에는 4B-watch다.
- IP/edutainment IPO는 recurring franchise revenue 전에는 one-hit-wonder 4B overlay를 붙인다.
- recycling policy는 true recycling economics and cleanup contracts가 없으면 false-positive watch다.
```

## data/e2r_case_library/cases_r12_loop15_round235.jsonl 초안

```jsonl
{"case_id":"r12_loop15_fertilizer_export_control_korea_basket","symbol":"025860/001390/001550/fertilizer_basket","company_name":"Namhae Chemical / KG Chemical / Chobi / fertilizer basket","case_type":"Stage2_event_with_4B_supply_watch","primary_archetype":"FERTILIZER_EXPORT_CONTROL_STAGE2_EVENT","best_trigger":"T1/T3","stage_candidate":"Stage2_event","price_validation":{"trigger_date":"2026-03-19/2026-04-28","china_fertilizer_exports_usd_bn":13,"potential_export_restriction_volume_mn_tons":40,"restricted_export_share_range_pct":"50-75","international_urea_price_rise_from_prewar_pct":40,"ammonium_sulphate_inspection_tightening":true,"korea_urea_supply_crunch_memory_2021":true,"direct_krx_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_event_not_Green","notes":"Global fertilizer supply shock is Stage2; domestic ASP/margin/sales evidence required for Yellow."}
{"case_id":"r12_loop15_feed_wheat_tender_input_cost","symbol":"feed_livestock_food_cost_basket","company_name":"Feed / livestock / food-cost read-through","case_type":"4c_watch","primary_archetype":"AGRI_FEED_PRICE_INPUT_COST_4C_WATCH","best_trigger":"T1/T2","stage_candidate":"4C-watch","price_validation":{"trigger_date":"2026-05-13","feed_wheat_tender_volume_tons":65000,"purchase_result":"believed_no_purchase","lowest_offer_cargill_usd_per_ton_cnf":298.5,"extra_unloading_surcharge_usd_per_ton":2.0,"reason":"high_price_offers_due_wheat_futures_and_harvest_concerns","direct_krx_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","notes":"Failed feed wheat tender is input-cost pressure, not growth."}
{"case_id":"r12_loop15_ai_digital_textbook_policy_rollback","symbol":"095720/133750/289010/edtech_basket","company_name":"Woongjin ThinkBig / MegaStudy / Icecream Edu / edtech basket","case_type":"Stage2_policy_with_rollback_4C","primary_archetype":"AI_TEXTBOOK_POLICY_STAGE2_WITH_ROLLBACK_4C","best_trigger":"T0/T2","stage_candidate":"Stage2_policy_to_4C_watch","price_validation":{"planned_rollout_year":2025,"target_age_context":"as_young_as_8","parent_petition_count":">50000","risks":["screen_overexposure","misinformation","AI_hallucination","privacy","teacher_workload"],"rollback":"official_textbook_to_supplementary_material","classroom_mobile_digital_device_ban_effective":"2026-03","direct_krx_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"policy_rollback_4C_watch","notes":"AI textbook policy was real Stage2, but rollback and device restrictions create 4C overlay."}
{"case_id":"r12_loop15_hagwon_preschool_private_education","symbol":"215200/019680/095720/133750/private_education_basket","company_name":"MegaStudy / Daekyo / Woongjin ThinkBig / Creverse / hagwon basket","case_type":"structural_stage2_with_social_4B","primary_archetype":"HAGWON_PRIVATE_EDUCATION_STRUCTURAL_STAGE2","best_trigger":"T0/T1","stage_candidate":"Stage2_structural","price_validation":{"trigger_date":"2025-03-16","under_six_hagwon_enrollment_pct":47.6,"under_two_hagwon_enrollment_pct":25,"preschool_monthly_tuition_avg_krw":332000,"english_kindergarten_monthly_tuition_avg_krw":1500000,"direct_krx_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_stage2","notes":"Hagwon demand and ARPU are structural, but social/regulatory pressure and listed-company margin are gates."}
{"case_id":"r12_loop15_naver_uber_baemin_food_delivery_ma","symbol":"035420/Baemin_private/Delivery_Hero_readthrough","company_name":"Naver / Uber / Baedal Minjok / Delivery Hero","case_type":"Stage2_MA_optionality_with_4B","primary_archetype":"FOOD_DELIVERY_MA_STAGE2_WITH_REGULATORY_4B","best_trigger":"T0/T3","stage_candidate":"Stage2_MA","price_validation":{"trigger_date":"2026-05-18","reported_baemin_bid_krw_trn":8.0,"reported_baemin_bid_usd_bn":5.34,"consortium_split":{"Uber_pct":80,"Naver_pct":20},"target":"100%_Baedal_Minjok","naver_decision_status":"teaser_letter_received_no_final_decision","delivery_hero_uber_stake_after_pct":19.5,"delivery_hero_event_return_pct":5.6,"direct_naver_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_MA_not_Green","notes":"Food-delivery M&A teaser is Stage2; binding bid, approval and take-rate economics required."}
{"case_id":"r12_loop15_coupang_data_breach_life_service_4c","symbol":"CPNG/Korea_ecommerce_readthrough","company_name":"Coupang / Korea e-commerce life-service reference","case_type":"hard_4c_with_false_break_relief","primary_archetype":"ECOMMERCE_DATA_BREACH_HARD_4C","best_trigger":"T0/T3","stage_candidate":"4C","price_validation":{"affected_customer_accounts_mn":33.7,"premarket_event_return_pct":-4.4,"stock_performance_before_breach_ytd_pct":28,"ceo_resignation":true,"government_probe":true,"police_raid":true,"tax_agency_special_audit":true,"relief_event_return_pct":9,"payment_login_customs_data_compromised":false},"score_price_alignment":"hard_4c_success","notes":"Platform scale without security becomes hard 4C; later relief is false-break relief."}
{"case_id":"r12_loop15_pinkfong_babyshark_ipo","symbol":"Pinkfong/Samsung_Publishing_readthrough","company_name":"Pinkfong / Baby Shark / Samsung Publishing read-through","case_type":"Stage2_Actionable_with_4B_one_hit_overlay","primary_archetype":"CHILDREN_IP_EDUTAINMENT_IPO_STAGE2_WITH_4B","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable","price_validation":{"ipo_price_krw":38000,"ipo_raise_krw_bn":76,"debut_intraday_high_krw":61500,"debut_intraday_mfe_pct":62,"debut_close_krw":41550,"debut_close_return_pct":9,"baby_shark_youtube_views_bn":16,"sales_2024_krw_bn":97.4,"op_2024_krw_bn":18.8,"combined_subscribers_mn_context":270,"h1_2025_op_margin_pct_context":20,"valuation_context_2025e_pe":25,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate_with_4B","notes":"IPO pop and global IP are Actionable; recurring next-IP revenue needed for Yellow/Green."}
{"case_id":"r12_loop15_plastic_recycling_policy_false_positive","symbol":"waste_recycling_basket/KG_ETS_readthrough/SK_ecoplant_private_readthrough","company_name":"Waste / recycling policy basket","case_type":"policy_false_positive_watch","primary_archetype":"PLASTIC_RECYCLING_POLICY_FALSE_POSITIVE","best_trigger":"T0/T2","stage_candidate":"Stage2_policy","price_validation":{"trigger_date":"2024-11-22","claimed_plastic_recycling_rate_pct":73,"greenpeace_estimated_real_recycling_rate_pct":27,"plastic_waste_growth_2019_2022_pct":31,"asan_untreated_plastic_waste_tons":19000,"estimated_cleanup_cost_krw_bn":"2-3","direct_krx_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"false_positive_watch","notes":"Recycling policy headline is not Green without cleanup contracts, tipping fees and treatment economics."}
```

## data/e2r_trigger_calibration/triggers_r12_loop15_round235.jsonl 초안

```jsonl
{"trigger_id":"r12l15_fertilizer_china_T1","case_id":"r12_loop15_fertilizer_export_control_korea_basket","trigger_type":"Stage2_event","trigger_date":"2026-03-19","evidence_available":"China restricts fertilizer exports; China exported more than $13B fertilizer; restrictions may affect 50-75% of exports, up to 40M tons; urea +40% from pre-war levels","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_event_not_Green","promote_to":"Stage2"}
{"trigger_id":"r12l15_feed_wheat_T1","case_id":"r12_loop15_feed_wheat_tender_input_cost","trigger_type":"4C-watch","trigger_date":"2026-05-13","evidence_available":"Korea FLC believed no purchase in 65,000t feed wheat tender due high offers; lowest offer $298.50/t C&F plus $2 surcharge","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"agri_input_cost_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r12l15_ai_textbook_T0","case_id":"r12_loop15_ai_digital_textbook_policy_rollback","trigger_type":"Stage2_policy","trigger_date":"2024-08-18","evidence_available":"Korea planned AI digital textbooks from 2025 for children as young as 8; 50k+ parents petitioned against over screen/misinformation/privacy concerns","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_policy_with_4B_social_backlash","promote_to":"Stage2"}
{"trigger_id":"r12l15_ai_textbook_T2","case_id":"r12_loop15_ai_digital_textbook_policy_rollback","trigger_type":"4C-watch","trigger_date":"2025-08-04","evidence_available":"National Assembly stripped AI textbooks of official textbook status and reclassified them as supplementary materials","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"policy_rollback_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r12l15_hagwon_preschool_T0","case_id":"r12_loop15_hagwon_preschool_private_education","trigger_type":"Stage2_structural","trigger_date":"2025-03-16","evidence_available":"47.6% of under-six children and 25% of under-two children attend hagwon; preschool average tuition Won332k/month; English kindergartens Won1.5mn/month","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"structural_stage2_with_social_4B","promote_to":"Stage2"}
{"trigger_id":"r12l15_baemin_naver_T0","case_id":"r12_loop15_naver_uber_baemin_food_delivery_ma","trigger_type":"Stage2_MA","trigger_date":"2026-05-18","evidence_available":"Uber/Naver consortium reportedly bids up to 8T won for Baemin; Uber 80%, Naver 20%; Naver received teaser letter but no decision","event_return_pct":"Naver price unavailable / Delivery Hero +5.6 related","trigger_outcome_label":"Stage2_MA_not_Green","promote_to":"Stage2"}
{"trigger_id":"r12l15_coupang_breach_T0","case_id":"r12_loop15_coupang_data_breach_life_service_4c","trigger_type":"hard_4C","trigger_date":"2025-12-01","evidence_available":"Coupang data breach affects 33.7M customer accounts; stock -4.4% premarket","event_return_pct":-4.4,"trigger_outcome_label":"hard_4c_security","promote_to":"4C"}
{"trigger_id":"r12l15_coupang_breach_T3","case_id":"r12_loop15_coupang_data_breach_life_service_4c","trigger_type":"false_break_relief","trigger_date":"2025-12-26","evidence_available":"Coupang shares +9% after update says limited retained data and no payment/login/customs data compromised","event_return_pct":9,"trigger_outcome_label":"false_break_relief","promote_to":"4C_watch_relief"}
{"trigger_id":"r12l15_pinkfong_ipo_T2","case_id":"r12_loop15_pinkfong_babyshark_ipo","trigger_type":"Stage2-Actionable+4B-watch","trigger_date":"2025-11-18","evidence_available":"Pinkfong IPO debut: +62% intraday to 61,500 won, close +9% at 41,550 won; Baby Shark 16B+ YouTube views; IPO raised 76B won","event_return_pct":62,"trigger_outcome_label":"Stage2_Actionable_with_4B_one_hit_overlay","promote_to":"Stage2-Actionable"}
{"trigger_id":"r12l15_plastic_recycling_T1","case_id":"r12_loop15_plastic_recycling_policy_false_positive","trigger_type":"false_positive_watch","trigger_date":"2024-11-22","evidence_available":"Korea claims 73% plastic recycling but Greenpeace estimates true rate 27%; plastic waste +31% 2019-2022; Asan site has 19,000t untreated waste","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"policy_theme_false_positive_watch","promote_to":"Stage2_policy_only"}
```

## data/sector_taxonomy/score_weight_profiles_round235_r12_loop15_v1.csv 초안

```csv
archetype,domestic_asp_margin_pass_through,inventory_import_mix_visibility,school_contract_paid_adoption,policy_rollback_risk,listed_company_enrollment_arpu,platform_data_security_trust,binding_ma_approval_take_rate,recurring_ip_revenue,cleanup_contract_tipping_fee_visibility,commodity_supply_shock_without_company_margin_penalty,edtech_policy_without_school_contract_penalty,ai_textbook_without_teacher_parent_acceptance_penalty,ma_teaser_without_binding_offer_penalty,platform_scale_without_security_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
FERTILIZER_EXPORT_CONTROL_STAGE2_EVENT,+5,+4,+0,+1,+0,+0,+0,+0,+0,-5,-1,-1,-1,-1,global supply shock,domestic ASP/margin missing,ASP+inventory+margin pass-through,Fertilizer event Stage2 only.
AGRI_FEED_PRICE_INPUT_COST_4C_WATCH,+4,+3,+0,+1,+0,+0,+0,+0,+0,-4,-1,-1,-1,-1,input cost shock,pass-through missing,feed cost stabilization,Feed wheat tender 4C-watch.
AI_TEXTBOOK_POLICY_STAGE2_WITH_ROLLBACK_4C,+0,+0,+5,+5,+2,+4,+0,+1,+0,-1,-5,-5,-1,-1,policy rollout,school contracts/acceptance missing,paid adoption+acceptance+learning outcomes,AI textbook rollback.
HAGWON_PRIVATE_EDUCATION_STRUCTURAL_STAGE2,+0,+0,+1,+4,+5,+1,+0,+0,+0,-1,-2,-2,-1,-1,enrollment+tuition ARPU,listed-company margin missing,enrollment+ARPU+margin,Hagwon structural Stage2.
FOOD_DELIVERY_MA_STAGE2_WITH_REGULATORY_4B,+0,+0,+0,+2,+0,+4,+5,+0,+0,-1,-1,-1,-5,-4,reported M&A bid,binding offer/KFTC/take-rate missing,approval+take-rate+synergy,Baemin/Naver Stage2 M&A.
ECOMMERCE_DATA_BREACH_HARD_4C,+0,+0,+0,+2,+0,+5,+1,+0,+0,-1,-1,-1,-1,-5,data breach,trust recovery pending,security restored+churn controlled,Coupang hard 4C.
CHILDREN_IP_EDUTAINMENT_IPO_STAGE2_WITH_4B,+0,+0,+0,+1,+0,+1,+0,+5,+0,-1,-1,-1,-1,-1,IPO pop+global IP,next-IP revenue missing,recurring licensing+next franchise,Pinkfong Stage2-Actionable.
PLASTIC_RECYCLING_POLICY_FALSE_POSITIVE,+0,+0,+0,+3,+0,+0,+0,+0,+5,-1,-1,-1,-1,-1,recycling policy,cleanup contract/tipping fee missing,contracted treatment economics,Plastic recycling false-positive watch.
SHRINKFLATION_PRICE_REGULATION_4C_WATCH,+3,+1,+0,+4,+0,+0,+0,+0,+0,-2,-1,-1,-1,-1,price regulation,margin/label compliance missing,compliance+pricing power,Consumer-life price regulation watch.
```

---

# 이번 R12 Loop 15 결론

```text
1. Fertilizer export controls는 Stage2 event다.
   global supply shock은 강하지만 국내 fertilizer company ASP/margin 확인 전에는 Yellow/Green 금지다.

2. Feed wheat tender failure는 input-cost 4C-watch다.
   high offer 때문에 구매가 안 된 것은 feed/livestock/food-service margin에 부정적이다.

3. AI digital textbook은 Stage2 policy였지만 rollback 4C가 나왔다.
   official textbook 지위 박탈과 classroom device ban 때문에 edtech Green은 금지다.

4. Hagwon preschool demand는 structural Stage2다.
   under-six 47.6%, under-two 25%, tuition ARPU는 강하지만 사회·규제 리스크가 크다.

5. Naver/Uber/Baemin은 food-delivery M&A Stage2다.
   8T won teaser는 크지만 final binding bid, KFTC, take-rate economics 전에는 Green이 아니다.

6. Coupang data breach는 R12 hard 4C다.
   생활서비스 platform은 scale보다 data-security trust가 먼저다.

7. Pinkfong IPO는 Stage2-Actionable + 4B다.
   +62% IPO pop과 Baby Shark IP는 강하지만, next franchise와 recurring licensing revenue가 필요하다.

8. Plastic recycling policy는 false-positive watch다.
   recycling rate headline보다 true recycling economics, cleanup contract, tipping fee가 중요하다.
```

한 문장으로 압축하면:

> **R12 Loop 15에서 배운 핵심은 “정책·공급차질·생활서비스 headline”이 아니라, 국내 ASP/margin, paid adoption, enrollment/ARPU, binding M&A approval, platform data security, recurring IP revenue, cleanup economics가 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 commodity shock, edtech policy, M&A teaser, viral IP, recycling headline만으로는 4B/false positive가 되기 쉽다.**

[1]: https://www.reuters.com/world/asia-pacific/china-restricts-fertiliser-exports-further-crimping-war-tightened-supply-2026-03-19/?utm_source=chatgpt.com "China restricts fertiliser exports, further crimping war-tightened supply"
[2]: https://www.reuters.com/world/asia-pacific/china-tightens-border-inspections-fertilizer-exports-sources-say-2026-04-28/?utm_source=chatgpt.com "China tightens border inspections for fertilizer exports, sources say"
[3]: https://www.reuters.com/world/asia-pacific/south-koreas-flc-believed-make-no-purchase-65000-ton-feed-wheat-tender-traders-2026-05-13/?utm_source=chatgpt.com "South Korea's FLC believed to make no purchase in 65,000 ton feed wheat tender, traders say"
[4]: https://www.ft.com/content/1f5c5377-5e85-4174-a54f-adc8f19fa5cb?utm_source=chatgpt.com "South Korea's plan for AI textbooks hit by backlash from parents"
[5]: https://www.businessinsider.com/ai-in-school-south-korea-textbook-rollback-jobs-education-2025-8?utm_source=chatgpt.com "Why South Korea's AI rollback in classrooms is a cautionary tale for the US"
[6]: https://www.ft.com/content/4babaa33-5ad8-4290-b7d3-835165ed8091?utm_source=chatgpt.com "South Korea's academic race pushes half of under-6s into 'cram' schools"
[7]: https://www.reuters.com/world/asia-pacific/uber-naver-team-up-baemin-takeover-seoul-economic-daily-2026-05-18/?utm_source=chatgpt.com "Uber, Naver team up on Baemin takeover -Seoul Economic Daily"
[8]: https://www.reuters.com/business/uber-raises-stake-germanys-delivery-hero-2026-05-18/?utm_source=chatgpt.com "Uber adds to stake in Germany's Delivery Hero, becomes biggest shareholder"
[9]: https://www.barrons.com/articles/coupang-stock-price-data-breach-aad847d8?utm_source=chatgpt.com "Online Retailer Coupang Owns Up to Big Blunder. The Stock Drops."
[10]: https://www.ft.com/content/5629623b-afb4-4ecd-9015-0177310e6d1c?utm_source=chatgpt.com "South Korean CEO quits after huge online data breach"
[11]: https://www.ft.com/content/d79a36bb-e985-43d5-843d-4a7199d2bafb?utm_source=chatgpt.com "'Baby Shark' creator Pinkfong pops in trading debut"
[12]: https://www.ft.com/content/218223d4-e04b-4fe3-9398-52ce7558a38d?utm_source=chatgpt.com "'Baby Shark' still has teeth"
[13]: https://www.reuters.com/business/environment/south-koreas-mountain-plastic-waste-shows-limits-recycling-2024-11-22/?utm_source=chatgpt.com "South Korea's mountain of plastic waste shows limits of recycling"
