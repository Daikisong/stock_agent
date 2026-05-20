순서상 이번은 **R7 Loop 15 — 바이오·헬스케어·의료기기 trigger-level price validation 라운드**다.

이번 R7의 핵심은 “FDA 승인 / CDMO 수주 / 신약 LO / 의료기기 M&A”를 한 덩어리로 보지 않는 것이다. **임상 성공, 허가, 출시, 실제 매출, 로열티, 특허소송, 공장 현지화, 보험·리임버스먼트, 고객사 call-off**가 각각 다른 trigger다.

```text
round = R7 Loop 15
round_id = round_230
large_sector = BIO_HEALTHCARE_MEDICAL_DEVICE
method = trigger_level_backtest_v1
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R8 Loop 15
```

이번에도 KRX/Naver/Yahoo/Stooq의 수정주가 일봉 OHLC 30D/90D/180D/1Y window를 안정적으로 직접 추출하지 못했다. 그래서 full MFE/MAE는 `price_data_unavailable_after_deep_search`로 두고, Reuters/WSJ/FT/MarketWatch가 보도한 **reported event return, product launch timing, approval, deal value, factory value, policy-support sector return, litigation event**를 trigger anchor로 쓴다. 단, **OHLC 미확보를 이유로 Stage 후보 자체를 강등하지 않는다.**

---

# 1. 이번 라운드 대섹터

```text
R7 = 바이오·헬스케어·의료기기
```

R7의 핵심 gate는 아래다.

```text
신약 / 플랫폼:
임상 결과 → 허가 신청 → FDA approval → launch → adoption → royalty / sales → patent litigation

CDMO:
수주 / 공장 인수 → capacity → 고객사 pipeline → batch order → utilization → margin → tariff risk

바이오시밀러:
FDA approval → patent litigation / settlement → launch date → price erosion → market share → margin

백신 / CDMO M&A:
M&A signing → capacity / technology fit → integration → order backlog → utilization → cashflow

의료기기 / aesthetic:
approval / tender / acquisition → actual hospital or clinic adoption → consumable/repeat sales → margin

AI healthcare:
regulatory clearance / acquisition → revenue integration → hospital workflow adoption → reimbursement

정책 / tariff:
정부지원 / U.S. tariff hedge → local manufacturing → funding / capex → margin / approval speed
```

---

# 2. 대상 canonical archetype

```text
SC_FORMULATION_ROYALTY_STAGE2_TO_GREEN
BIOPHARMA_TARIFF_LOCALIZATION_STAGE2
CDMO_LOCALIZATION_EVIDENCE_GOOD_PRICE_FAILED
VACCINE_CDMO_MA_STAGE2_ACTIONABLE
AESTHETIC_TOXIN_US_LAUNCH_STAGE2
AESTHETIC_DEVICE_MA_CONTROL_PREMIUM
BIOSIMILAR_PATENT_LITIGATION_4C_WATCH
PRIVATE_BIOTECH_LO_REFERENCE
```

---

# 3. deep sub-archetype

```text
Alteogen:
- ALT-B4 / berahyaluronidase alfa
- Merck Keytruda Qlex
- non-inferiority trial
- FDA approval
- launch / adoption 30~40%
- Qlex early sales
- Halozyme patent challenge

Samsung Biologics:
- CDMO order flow
- Kiniksa $152.2M contract
- Korea pharma tariff-policy support
- GSK U.S. facility $280M
- first U.S. facility / 60,000L
- Amgen vs Samsung Bioepis patent litigation

Celltrion:
- U.S. factory preferred bidder
- Eli Lilly / ImClone Systems $330M acquisition
- U.S. tariff hedge
- 700B won expansion plan

SK Bioscience:
- IDT Biologika 60% stake
- 339B won / $243.75M
- first major M&A since IPO
- shares +11.7%

Hugel:
- Letybo / Botulax
- U.S. FDA approval / launch
- Botox competitor, lower-price positioning
- actual U.S. adoption and price erosion gate

Jeisys Medical:
- ArchiMed $742M acquisition
- energy-based aesthetic devices
- revenue +44% annually / EBITDA +45% annually
- M&A/control premium vs operating Stage3

Samsung Bioepis:
- Amgen patent lawsuit over Prolia/Xgeva biosimilars
- 34 patent claims
- launch-delay / litigation 4C-watch

ADEL / Sanofi:
- unlisted Korean biotech reference
- $1.04B Alzheimer’s partnership
- $80M upfront
- LO does not equal public-market Stage3 without listed price / trial progress
```

---

# 4. 선정 case 요약

| bucket                                             | case                                              | 핵심 판정                                                                                                                             |
| -------------------------------------------------- | ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| structural_success / Stage3-Yellow→Green candidate | Alteogen / Keytruda Qlex                          | non-inferiority → FDA approval → launch → Q1 2026 Qlex sales. 다만 Alteogen royalty visibility와 Halozyme patent risk 때문에 Green은 조건부 |
| Stage2 policy / localization                       | Samsung Biologics / Celltrion tariff localization | 정부지원에 Samsung Bio +6.23%, 이후 GSK U.S. facility $280M / Celltrion U.S. plant. 가격반응은 혼재                                             |
| Stage2-Actionable                                  | SK Bioscience / IDT Biologika                     | 60% stake, 339B won, shares +11.7%. CDMO/vaccine M&A trigger                                                                      |
| Stage2 product launch                              | Hugel / Letybo                                    | FDA-approved neuromodulator U.S. launch. U.S. adoption / price / market share 필요                                                  |
| 4B/control premium                                 | Jeisys Medical / ArchiMed                         | $742M acquisition, aesthetic EBD structural market. delisting/control premium이지 operating Green 아님                                |
| 4C-watch                                           | Samsung Bioepis / Amgen lawsuit                   | Prolia/Xgeva biosimilar patent litigation, 34 patents. launch-delay hard gate                                                     |
| Stage2 private reference                           | ADEL / Sanofi                                     | $1.04B Alzheimer’s deal, $80M upfront. listed price trigger 부재라 reference만                                                        |
| 4C/patent watch                                    | Alteogen / Halozyme risk                          | Keytruda Qlex는 강하지만 enzyme patent battle이 4C overlay                                                                              |

---

# 5. Case별 trigger grid

## Case A — Alteogen / Merck Keytruda Qlex

```text
symbol = 196170
case_type = structural_success / Stage3-Yellow→Green candidate
archetype = SC_FORMULATION_ROYALTY_STAGE2_TO_GREEN
```

### Trigger grid

| trigger | type                   |       date | 당시 공개 evidence                                                                                       | 가격 anchor                  | outcome               |
| ------- | ---------------------- | ---------: | ---------------------------------------------------------------------------------------------------- | -------------------------- | --------------------- |
| T0      | awareness              |    2024 이전 | Merck가 Keytruda SC formulation 개발, Alteogen enzyme 사용                                                | OHLC unavailable           | Stage1                |
| T1      | Stage2 evidence        | 2024-11-19 | Merck says SC Keytruda trial non-inferior vs IV; injection 2~3분 vs IV 30분                            | Merck +1.8% premarket      | Stage2-Actionable     |
| T2      | Stage3-Yellow          | 2025-03-27 | Merck plans U.S. launch Oct 1, expects 30~40% adoption within two years, FDA decision target Sept 23 | Alteogen price unavailable | Yellow                |
| T3      | Stage3-Green candidate | 2025-09-19 | FDA approves Keytruda Qlex; 1~2분 injection; late-Sept availability                                   | Alteogen price unavailable | Green candidate       |
| T4      | Green validation       |    2026-Q1 | Qlex sales $128M in Q1 2026, Merck reports Keytruda +12%                                             | Merck -1.6% separate mix   | revenue validation    |
| T5      | 4C-watch               |   2025-03~ | Halozyme patent challenge risk over enzyme; Merck says no launch delay                               | no direct KRX              | patent overlay        |
| T6      | hard 4C                |        N/A | launch block / injunction not confirmed                                                              | N/A                        | hard_4c_not_confirmed |

Alteogen은 R7에서 가장 중요한 Stage ladder case다. 2024년 11월 Merck는 injectable Keytruda가 IV formulation 대비 non-inferior였다고 발표했고, injection 시간이 2~3분으로 IV infusion 약 30분보다 훨씬 짧다고 밝혔다. 이때는 아직 approval 전이라 `Stage2-Actionable`이다. ([Reuters][1])

2025년 3월에는 Merck가 U.S. launch를 2025년 10월 1일로 계획하고, FDA decision target을 2025년 9월 23일로 제시했으며, Keytruda 환자의 30~40%가 2년 안에 SC formulation으로 전환될 수 있다고 밝혔다. 여기서부터는 단순 임상 결과가 아니라 launch/adoption plan이 붙었기 때문에 `Stage3-Yellow`로 올릴 수 있다. ([Reuters][2])

2025년 9월 FDA approval이 나오면서 Keytruda Qlex는 실제 제품으로 바뀌었다. Reuters는 Qlex가 1~2분 injection으로 투여될 수 있고, Merck가 2025년 9월 말부터 U.S. availability를 목표로 한다고 보도했다. 2026년 1분기에는 Qlex sales가 $128M로 잡혔다는 WSJ 보도까지 나왔다. 이 지점은 `Stage3-Green candidate`지만, Alteogen 입장에서는 royalty formula와 patent dispute exposure가 남아 있어 완전 Green 확정은 보류한다. ([Reuters][3])

### Trigger price validation row

```json
{
  "case_id": "r7_loop15_alteogen_keytruda_qlex",
  "symbol": "196170",
  "best_trigger": "T2/T3",
  "best_trigger_type": "Stage3-Yellow_to_Green_candidate",
  "t1_date": "2024-11-19",
  "t1_trigger": "SC Keytruda non-inferiority trial",
  "t1_merck_event_return_pct": 1.8,
  "injection_time_minutes": "2-3",
  "iv_infusion_time_minutes": 30,
  "t2_date": "2025-03-27",
  "t2_launch_plan_date": "2025-10-01",
  "expected_peak_adoption_pct": "30-40",
  "keytruda_2024_sales_usd_bn": 30,
  "t3_date": "2025-09-19",
  "t3_fda_approval": true,
  "t3_brand_name": "Keytruda Qlex",
  "qlex_q1_2026_sales_usd_mn": 128,
  "patent_challenge_counterparty": "Halozyme",
  "alteogen_direct_ohlc_status": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "Alteogen_royalty_rate_visibility",
    "commercial_royalty_recognition",
    "patent_dispute_outcome",
    "regional_launch_timing",
    "Merck_switch_rate_actual"
  ],
  "trigger_outcome_label": "Stage3_Yellow_to_Green_candidate"
}
```

### 판정

```text
score_price_alignment = Stage3-Yellow_to_Green_candidate
new_rule = 임상 non-inferiority만으로는 Stage2, launch/adoption plan부터 Yellow, FDA approval + sales부터 Green candidate
```

---

## Case B — Alteogen / Halozyme patent challenge overlay

```text
symbol = 196170
case_type = 4C-watch overlay
archetype = SC_FORMULATION_PATENT_4C_WATCH
```

### Trigger grid

| trigger | type           |       date | 당시 공개 evidence                                                                     | 가격 anchor    | outcome      |
| ------- | -------------- | ---------: | ---------------------------------------------------------------------------------- | ------------ | ------------ |
| T0      | 4C-watch       | 2025-03-05 | WSJ reports Halozyme patent challenge risk over enzyme used in injectable Keytruda | no KRX price | patent watch |
| T1      | partial relief | 2025-03-27 | Merck says it will not delay launch, believes position strong vs Halozyme claims   | no KRX price | relief       |
| T2      | hard 4C        |        N/A | injunction / launch delay not confirmed                                            | N/A          | no hard 4C   |

Alteogen은 좋은 Stage3 후보지만, R7에서는 patent overlay를 별도 row로 둬야 한다. WSJ는 Halozyme이 enzyme patent issue를 제기했고, Merck가 Halozyme patents 재검토를 요청했다고 보도했다. 다만 Reuters는 이후 Merck가 launch를 지연하지 않겠다고 밝혔고, Halozyme claim에 대해 강한 입장을 갖고 있다고 전했다. 따라서 현재는 hard 4C가 아니라 `4C-watch / false-break watch`다. ([월스트리트저널][4])

```json
{
  "case_id": "r7_loop15_alteogen_halozyme_patent_watch",
  "symbol": "196170",
  "best_trigger": "T0/T1",
  "best_trigger_type": "4C-watch_overlay",
  "trigger_date": "2025-03-05/2025-03-27",
  "patent_counterparty": "Halozyme",
  "merck_patent_petitions": true,
  "launch_delay_confirmed": false,
  "merck_no_delay_statement": true,
  "hard_4c_confirmed": false,
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "4C_watch_not_hard"
}
```

---

## Case C — Samsung Biologics / CDMO localization and tariff policy

```text
symbol = 207940
case_type = Stage2 policy + localization / evidence_good_but_price_failed
archetype = BIOPHARMA_TARIFF_LOCALIZATION_STAGE2
```

### Trigger grid

| trigger | type              |       date | 당시 공개 evidence                                                                        | 가격 anchor                                | outcome                     |
| ------- | ----------------- | ---------: | ------------------------------------------------------------------------------------- | ---------------------------------------- | --------------------------- |
| T0      | Stage2 policy     | 2025-05-21 | Korea pledges more support for biopharma/export industries under U.S. tariff pressure | pharma sector +3.97%, Samsung Bio +6.23% | Stage2-Actionable policy    |
| T1      | Stage2 evidence   | 2025-12-22 | Samsung Bio buys first U.S. drug-production facility from GSK for $280M               | Samsung Bio -0.4%, KOSPI +2%             | evidence good, price failed |
| T2      | Stage2-Actionable | 2025-12-22 | Human Genome Sciences 100% stake, Rockville Maryland, 60,000L drug-substance capacity | same                                     | localization candidate      |
| T3      | Stage3-Yellow     |        N/A | utilization/customer transfer/order backlog not confirmed                             | N/A                                      | no Yellow                   |
| T4      | 4C-watch          | 2024-08-13 | Amgen sues Samsung Bioepis over Prolia/Xgeva biosimilars                              | no direct Samsung Bio price              | litigation watch            |

Samsung Biologics는 R7에서 “정책지원/현지화”가 Stage2까지만 가능하다는 case다. 2025년 5월에는 정부가 biopharma sector에 추가 지원을 약속하며 pharmaceutical sector가 +3.97%, Samsung Biologics가 +6.23% 올랐다. 이는 tariff policy support trigger로 `Stage2-Actionable`이 가능하다. ([Reuters][5])

그러나 2025년 12월 GSK U.S. facility 인수는 evidence는 좋았지만 가격반응은 좋지 않았다. Reuters는 Samsung Biologics가 Rockville, Maryland의 Human Genome Sciences를 $280M에 인수한다고 보도했고, 해당 facility는 60,000L drug-substance capacity를 갖고 있지만, 당일 Samsung Biologics shares는 -0.4%로 KOSPI +2%를 밑돌았다. 그래서 이 trigger는 `evidence_good_but_price_failed`다. ([Reuters][6])

### Trigger price validation row

```json
{
  "case_id": "r7_loop15_samsung_biologics_tariff_localization",
  "symbol": "207940",
  "best_trigger": "T0/T1",
  "best_trigger_type": "Stage2_policy_to_evidence_good_but_price_failed",
  "t0_date": "2025-05-21",
  "pharma_sector_event_return_pct": 3.97,
  "samsung_biologics_event_return_pct": 6.23,
  "t1_date": "2025-12-22",
  "us_facility_acquisition_value_usd_mn": 280,
  "facility_location": "Rockville, Maryland",
  "facility_capacity_liters": 60000,
  "t1_samsung_biologics_return_pct": -0.4,
  "t1_kospi_return_pct": 2.0,
  "market_relative_return_pp": -2.4,
  "stage3_gate_missing": [
    "customer_transfer",
    "facility_utilization",
    "incremental_CDMO_order",
    "margin_visibility",
    "tariff_saving_quantification"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "evidence_good_but_price_failed"
}
```

### 판정

```text
score_price_alignment = evidence_good_but_price_failed
new_rule = biopharma localization은 Stage2, utilization/order/margin 확인 전 Green 금지
```

---

## Case D — Celltrion / U.S. factory tariff hedge

```text
symbol = 068270
case_type = Stage2 localization / success candidate
archetype = BIOPHARMA_TARIFF_LOCALIZATION_STAGE2
```

### Trigger grid

| trigger | type                        |       date | 당시 공개 evidence                                                                          | 가격 anchor           | outcome   |
| ------- | --------------------------- | ---------: | --------------------------------------------------------------------------------------- | ------------------- | --------- |
| T0      | Stage2 policy               |    2025-05 | U.S. pharma tariff risk; Korean pharma exports $9.59B in 2024, 16% to U.S.              | no Celltrion direct | Stage2    |
| T1      | Stage2 evidence             | 2025-07-29 | Celltrion becomes preferred bidder for U.S. pharma factory; planned investment 700B won | no price            | Stage2    |
| T2      | Stage2 validation           | 2025-09-23 | Celltrion U.S. unit acquires ImClone Systems from Eli Lilly for $330M                   | price unavailable   | Stage2    |
| T3      | Stage2-Actionable candidate | 2025-11-19 | plans up to 700B won / $478M expansion in U.S. facility                                 | no price            | candidate |
| T4      | Stage3-Yellow               |        N/A | commercial production / product transfer / margin not confirmed                         | N/A                 | no Yellow |

Celltrion도 Samsung Biologics와 같은 localization theme지만, price anchor가 부족해 Stage2에 둔다. Reuters는 2025년 7월 Celltrion이 U.S. manufacturing factory 인수 preferred bidder가 됐고, 인수·운영에 700B won을 투자할 계획이라고 보도했다. 이후 9월에는 Celltrion U.S. subsidiary가 Eli Lilly로부터 ImClone Systems를 $330M에 인수한다고 공시했다. ([Reuters][7])

11월에는 U.S. factory expansion에 최대 700B won, 약 $478M을 추가 투자하겠다고 밝혔다. 이건 tariff hedge와 U.S. demand 대응으로는 Stage2지만, product transfer, utilization, tariff saving, margin 전에는 Yellow/Green으로 올리기 어렵다. ([Reuters][8])

```json
{
  "case_id": "r7_loop15_celltrion_us_factory_tariff_hedge",
  "symbol": "068270",
  "best_trigger": "T1/T2/T3",
  "best_trigger_type": "Stage2_localization",
  "preferred_bidder_date": "2025-07-29",
  "planned_acquisition_operation_investment_krw_bn": 700,
  "imclone_acquisition_value_usd_mn": 330,
  "us_expansion_investment_krw_bn": 700,
  "us_expansion_investment_usd_mn": 478,
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "commercial_production_transfer",
    "U.S._facility_utilization",
    "tariff_saving",
    "gross_margin",
    "product_launch_timing"
  ],
  "trigger_outcome_label": "Stage2_localization_success_candidate"
}
```

---

## Case E — SK Bioscience / IDT Biologika acquisition

```text
symbol = 302440
case_type = Stage2-Actionable
archetype = VACCINE_CDMO_MA_STAGE2_ACTIONABLE
```

### Trigger grid

| trigger | type              |       date | 당시 공개 evidence                                                                                 | 가격 anchor     | outcome           |
| ------- | ----------------- | ---------: | ---------------------------------------------------------------------------------------------- | ------------- | ----------------- |
| T0      | awareness         | post-COVID | vaccine maker seeks business model beyond pandemic demand                                      | no price      | Stage1            |
| T1      | Stage2 evidence   | 2024-06-27 | SK Bioscience acquires 60% of Germany’s IDT Biologika for 339B won / $243.75M                  | shares +11.7% | Stage2-Actionable |
| T2      | Stage2-Actionable | 2024-06-27 | first major M&A since 2021 IPO, European CDMO/vaccine footprint                                | same          | Actionable        |
| T3      | Stage3-Yellow     |        N/A | order backlog / utilization / integration economics not confirmed                              | N/A           | no Yellow         |
| T4      | 4B-watch          |    2024-06 | SK Group rebalancing context; M&A may be portfolio optimisation rather than immediate earnings | no full OHLC  | watch             |

SK Bioscience는 R7의 명확한 `Stage2-Actionable`이다. Reuters는 SK Bioscience가 German pharmaceutical contract manufacturer IDT Biologika의 60% stake를 339B won, 약 $243.75M에 인수한다고 보도했고, 발표 후 shares가 +11.7% 올랐다고 전했다. 이건 단순 정책이 아니라 **M&A + European CDMO footprint + 가격반응**이 붙은 trigger다. ([Reuters][9])

다만 IDT integration, backlog, utilization, margin이 확인되기 전에는 Stage3-Yellow로 올리기 어렵다.

```json
{
  "case_id": "r7_loop15_sk_bioscience_idt_biologika",
  "symbol": "302440",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable",
  "trigger_date": "2024-06-27",
  "stake_acquired_pct": 60,
  "deal_value_krw_bn": 339,
  "deal_value_usd_mn": 243.75,
  "event_return_pct": 11.7,
  "first_major_ma_since_ipo": true,
  "idt_remaining_stake_holder": "Klocke Gruppe 40%",
  "stage3_gate_missing": [
    "integration_plan",
    "CDMO_order_backlog",
    "facility_utilization",
    "margin_contribution",
    "new_customer_wins"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_Actionable_CDMO_MA"
}
```

### 판정

```text
score_price_alignment = Stage2_promote_candidate
new_rule = vaccine/CDMO M&A + price reaction은 Stage2-Actionable
but = backlog/utilization/margin 전에는 Green 금지
```

---

## Case F — Hugel / Letybo U.S. launch

```text
symbol = 145020
case_type = Stage2 product launch
archetype = AESTHETIC_TOXIN_US_LAUNCH_STAGE2
```

### Trigger grid

| trigger | type                        |                                                    date | 당시 공개 evidence                                                               | 가격 anchor    | outcome   |
| ------- | --------------------------- | ------------------------------------------------------: | ---------------------------------------------------------------------------- | ------------ | --------- |
| T0      | Stage2 evidence             |                                                 2024-02 | Letybo FDA approval for moderate-to-severe glabellar lines                   | no KRX price | Stage2    |
| T1      | Stage2 launch               |                                                 2025-03 | Letybo starts arriving in U.S. market; lower-cost Botox competitor narrative | no KRX price | Stage2    |
| T2      | Stage2-Actionable candidate |                                                 2025-03 | estimated U.S. price $9~12/unit vs Botox $12~18/unit; possible 30% cheaper   | no price     | candidate |
| T3      | Stage3-Yellow               |                                                     N/A | U.S. clinic adoption / revenue / market share not confirmed                  | N/A          | no Yellow |
| T4      | 4B-watch                    | if price discount erodes margin or adoption disappoints | not confirmed                                                                | pending      | watch     |

Hugel/Letybo는 R7 의료미용 product launch case다. U.S. 시장에서 Letybo는 glabellar lines 치료용 neuromodulator로 FDA approval을 받은 제품이고, 2025년에는 U.S. dermatology market에 본격 등장하는 Botox competitor로 보도됐다. 가격은 Botox보다 낮은 $9~12/unit 수준으로 언급됐지만, 실제 U.S. clinic adoption, Hugel revenue contribution, margin이 없으면 Stage3가 아니다. ([Allure][10])

```json
{
  "case_id": "r7_loop15_hugel_letybo_us_launch",
  "symbol": "145020",
  "best_trigger": "T0/T1",
  "best_trigger_type": "Stage2_product_launch",
  "fda_approval_context": "moderate-to-severe_glabellar_lines",
  "us_launch_context_date": "2025-03",
  "estimated_letybo_price_usd_per_unit": "9-12",
  "botox_price_usd_per_unit_context": "12-18",
  "claimed_discount_pct_context": 30,
  "direct_hugel_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "U.S._clinic_adoption",
    "distributor_sell-through",
    "market_share",
    "price_realization",
    "margin_after_discount"
  ],
  "trigger_outcome_label": "Stage2_product_launch_not_Yellow"
}
```

---

## Case G — Jeisys Medical / ArchiMed aesthetic-device acquisition

```text
symbol = 287410
case_type = event_premium / control premium
archetype = AESTHETIC_DEVICE_MA_CONTROL_PREMIUM
```

### Trigger grid

| trigger | type              |       date | 당시 공개 evidence                                                                                                   | 가격 anchor                                             | outcome              |
| ------- | ----------------- | ---------: | ---------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | -------------------- |
| T0      | awareness         |       2024 | global aesthetic EBD growth                                                                                      | no price                                              | Stage1               |
| T1      | Stage2 evidence   | 2024-09-11 | ArchiMed finalizes roughly $742M acquisition of Jeisys Medical                                                   | shares closed 12,860 won previous day, little changed | control premium      |
| T2      | Stage2-Actionable | 2024-09-11 | EBD market expected >$16B by 2032 vs $4.5B prior year; Jeisys revenue +44% CAGR, EBITDA +45% CAGR through FY2023 | no MFE                                                | structural candidate |
| T3      | 4B                |    2024-09 | tender/delisting process rather than organic operating rerating                                                  | no full OHLC                                          | 4B                   |
| T4      | Stage3-Green      |        N/A | public-market trading after delisting not applicable                                                             | N/A                                                   | N/A                  |

Jeisys는 R7에서 “의료기기 structural growth”와 “M&A control premium”을 분리해야 하는 case다. WSJ는 healthcare PE firm ArchiMed가 Korean aesthetic device maker Jeisys Medical을 약 $742M에 인수한다고 보도했고, Jeisys revenue가 FY2023까지 3년간 연평균 44%, adjusted pretax earnings가 45% 성장했다고 전했다. EBD market도 $4.5B에서 2032년 $16B 이상으로 커질 것으로 제시됐다. ([월스트리트저널][11])

하지만 public-market trigger로는 tender/delisting이 중심이기 때문에, operating Stage3라기보다 `control premium / M&A event`로 둔다.

```json
{
  "case_id": "r7_loop15_jeisys_archimed_aesthetic_device_ma",
  "symbol": "287410",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2_structural_but_4B_control_premium",
  "trigger_date": "2024-09-11",
  "acquisition_value_usd_mn": 742,
  "prior_close_price_krw": 12860,
  "global_ebd_market_prior_year_usd_bn": 4.5,
  "global_ebd_market_2032e_usd_bn": 16,
  "revenue_cagr_through_fy2023_pct": 44,
  "adjusted_pretax_earnings_cagr_pct": 45,
  "delisting_process": true,
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "event_premium_control_premium_not_operating_Green"
}
```

---

## Case H — Samsung Bioepis / Amgen Prolia·Xgeva patent litigation

```text
symbol = Samsung Bioepis / 207940 read-through
case_type = 4C-watch
archetype = BIOSIMILAR_PATENT_LITIGATION_4C_WATCH
```

### Trigger grid

| trigger | type     |                                                         date | 당시 공개 evidence                                                              | 가격 anchor       | outcome          |
| ------- | -------- | -----------------------------------------------------------: | --------------------------------------------------------------------------- | --------------- | ---------------- |
| T0      | Stage2   | Samsung Bioepis applies for U.S. biosimilars of Prolia/Xgeva | no price                                                                    | Stage2          |                  |
| T1      | 4C-watch |                                                   2024-08-13 | Amgen sues Samsung Bioepis over 34 patents, seeks to block sale/manufacture | no direct price | litigation watch |
| T2      | hard 4C  |    if injunction blocks launch / settlement delays economics | not confirmed                                                               | pending         | no hard 4C       |

Samsung Bioepis litigation은 R7 biosimilar 4C-watch다. Reuters는 Amgen이 Samsung Bioepis를 상대로 Prolia/Xgeva biosimilar가 34개 patents를 침해한다고 주장하며 production/sale block을 요청했다고 보도했다. Prolia와 Xgeva의 U.S. sales는 전년 기준 각각 $2.7B, $1.5B였고, biosimilar entry timing에 따라 upside/downside가 크게 갈릴 수 있다. ([Reuters][12])

```json
{
  "case_id": "r7_loop15_samsung_bioepis_amgen_patent_litigation",
  "symbol": "207940_readthrough/Samsung_Bioepis",
  "best_trigger": "T1",
  "best_trigger_type": "4C-watch",
  "trigger_date": "2024-08-13",
  "litigation_counterparty": "Amgen",
  "patents_asserted_count": 34,
  "products": [
    "Prolia biosimilar",
    "Xgeva biosimilar"
  ],
  "prolia_us_sales_usd_bn": 2.7,
  "xgeva_us_sales_usd_bn": 1.5,
  "requested_relief": [
    "block_making",
    "block_selling",
    "monetary_damages"
  ],
  "hard_4c_confirmed": false,
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "biosimilar_patent_litigation_4C_watch"
}
```

---

## Case I — ADEL / Sanofi Alzheimer’s LO reference

```text
symbol = private / unlisted reference
case_type = private_reference
archetype = PRIVATE_BIOTECH_LO_REFERENCE
```

ADEL은 상장사가 아니므로 R7 case library의 KRX row로는 넣지 않는 게 맞다. 다만 한국 biotech LO의 calibration reference로는 유용하다. Reuters는 ADEL이 Sanofi와 Alzheimer’s drug ADEL-Y01 공동개발·상업화 계약을 맺었고, 총 deal value는 $1.04B, upfront는 $80M라고 보도했다. 이 구조는 listed biotech에서 “총 계약금액 headline”과 “upfront/cash-recognition”을 분리해야 한다는 reference다. ([Reuters][13])

```json
{
  "case_id": "r7_loop15_adel_sanofi_private_reference",
  "symbol": "private_reference",
  "best_trigger": "T1",
  "trigger_type": "LO_reference_not_KRX_case",
  "deal_value_usd_bn": 1.04,
  "upfront_payment_usd_mn": 80,
  "drug_candidate": "ADEL-Y01",
  "trial_stage": "early-stage human trials in U.S.",
  "listed_price_anchor": "N/A_private_company",
  "trigger_outcome_label": "private_reference_for_LO_total_value_vs_upfront"
}
```

---

# 6. Trigger별 가격경로 검증 요약

| case                     | best trigger |               entry anchor |                                                          event MFE/MAE | market-relative | full MFE/MAE | outcome                                 |
| ------------------------ | ------------ | -------------------------: | ---------------------------------------------------------------------: | --------------: | ------------ | --------------------------------------- |
| Alteogen / Keytruda Qlex | T2/T3        | Alteogen price unavailable |                 Merck +1.8% at trial trigger; Qlex sales $128M Q1 2026 |     unavailable | unavailable  | Stage3-Yellow→Green candidate           |
| Samsung Biologics        | T0/T1        |                      event | Samsung Bio +6.23% on policy; later -0.4% vs KOSPI +2 on U.S. facility |     +? / -2.4pp | unavailable  | Stage2 / evidence_good_but_price_failed |
| Celltrion                | T1/T2/T3     |                unavailable |                                                        no direct price |             N/A | unavailable  | Stage2 localization                     |
| SK Bioscience            | T1/T2        |                      event |                                                                 +11.7% |     unavailable | unavailable  | Stage2-Actionable                       |
| Hugel / Letybo           | T0/T1        |                unavailable |                                                        no direct price |             N/A | unavailable  | Stage2 product launch                   |
| Jeisys / ArchiMed        | T1/T2        | 12,860 prior close context |                                                      acquisition $742M |             N/A | unavailable  | control-premium event                   |
| Samsung Bioepis / Amgen  | T1           |                unavailable |                                                        no direct price |             N/A | unavailable  | 4C-watch                                |
| ADEL / Sanofi            | reference    |                        N/A |                                                                private |             N/A | N/A          | LO reference                            |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
Celltrion:
U.S. plant acquisition and expansion are Stage2 localization.
Price anchor 부족으로 Actionable 승격 보류.

Hugel:
FDA-approved product launch is Stage2.
U.S. adoption and revenue data 없으면 Yellow 보류.

ADEL:
private reference only.
Total deal value와 upfront를 분리하는 calibration에 사용.
```

## Stage 2-Actionable entry 성과

```text
Alteogen:
non-inferiority trial and launch plan은 Stage2-Actionable에서 Stage3-Yellow로 올라갈 수 있음.

SK Bioscience:
IDT acquisition + +11.7% is Stage2-Actionable.

Samsung Biologics:
policy support +6.23%는 Stage2-Actionable.
GSK facility acquisition은 evidence는 좋았지만 -0.4% / KOSPI +2%라 evidence_good_but_price_failed.
```

## Stage 3-Yellow entry 성과

```text
Alteogen:
launch plan + adoption estimate 30~40% + FDA approval.
Yellow 이상 가능.

Hugel:
U.S. product launch는 Stage2지만 adoption/revenue가 없어 Yellow 보류.

Samsung Bio / Celltrion:
factory localization은 utilization/margin/order 없으면 Yellow 보류.
```

## Stage3-Green 후보

```text
Alteogen:
Qlex approval + launch + Q1 2026 $128M sales는 Green candidate.
하지만 Alteogen royalty recognition / patent dispute / switch-rate actual이 확인되어야 확정 Green.
```

## 기존 점수표가 놓쳤을 가능성

```text
missed_structural:
- Alteogen: launch/adoption/FDA approval trigger를 Stage2로만 두면 너무 늦음.
- SK Bioscience: CDMO/vaccine M&A + +11.7%는 plain Stage2보다 강함.

Stage2_promote_candidate:
- Alteogen
- SK Bioscience
- Samsung Biologics policy support
```

---

# 8. score-price alignment 판정

```text
Stage2_promote_candidate:
- Alteogen
- SK Bioscience
- Samsung Biologics policy support
- possibly Jeisys structural aesthetic-device M&A, but public-market control premium dominates

Stage3-Yellow candidate:
- Alteogen / Keytruda Qlex
- Hugel / Letybo only after adoption data
- Samsung Bio / Celltrion only after utilization/order-margin data

Stage3-Green candidate:
- Alteogen, if royalty recognition and patent risk clear

event_premium:
- Jeisys / ArchiMed M&A
- Samsung Bio policy support first move
- CDMO localization headlines without utilization

evidence_good_but_price_failed:
- Samsung Biologics GSK facility acquisition

thesis_break_watch:
- Alteogen/Halozyme patent risk
- Samsung Bioepis/Amgen patent lawsuit
- U.S. pharma tariff/localization capex if margin benefit fails

hard_4C:
- 이번 R7 Loop 15에서는 confirmed hard 4C 없음
```

---

# 9. 점수비중 교정

## 올릴 축

```text
FDA_approval_to_launch_conversion +5
actual_product_sales_after_approval +5
royalty_recognition_visibility +5
adoption_rate_guidance +4
patent_litigation_clearance +5
CDMO_order_backlog_utilization +5
tariff_localization_margin_benefit +4
M&A_integration_and_utilization +4
biosimilar_launch_settlement +5
clinic_adoption_sellthrough +4
```

### 근거

Alteogen은 non-inferiority → launch plan → FDA approval → Qlex sales로 trigger가 단계적으로 닫혔다. 이것은 Stage2를 Yellow/Green으로 올리는 좋은 template다. 반대로 Samsung Biologics와 Celltrion의 U.S. factory trigger는 현지화와 tariff hedge는 좋지만 utilization/order/margin 없이는 Green이 아니다. SK Bioscience는 M&A + +11.7%로 Actionable하되 integration과 backlog가 필요하다.

## 내릴 축

```text
FDA_trial_result_only -4
product_approval_without_revenue -3
CDMO_capacity_headline_only -5
factory_acquisition_without_utilization -4
total_LO_value_without_upfront -5
biosimilar_approval_without_patent_clearance -5
aesthetic_launch_without_sellthrough -4
policy_support_without_company_order -4
```

### 근거

Hugel Letybo는 approval/launch만으로는 Stage3가 아니다. ADEL/Sanofi 같은 LO는 total deal value보다 upfront와 milestone probability를 봐야 한다. Samsung Bioepis는 biosimilar filing/approval path가 있어도 patent litigation이 launch를 막을 수 있다. Samsung Biologics GSK facility는 evidence는 좋았지만 당일 가격은 시장보다 약했다.

---

# 10. Stage 2-Actionable 승격 조건

R7 Loop 15 shadow rule:

```text
R7에서 Stage 2 evidence가 아래 중 3개 이상이면 Stage2-Actionable로 승격한다.

1. FDA approval 또는 pivotal non-inferiority/superiority result가 확인된다.
2. launch timing 또는 adoption-rate guidance가 구체적이다.
3. 실제 early sales 또는 royalty trigger가 보인다.
4. CDMO/M&A trigger가 capacity뿐 아니라 customer/order/utilization으로 연결된다.
5. event 당일 또는 직후 market-relative 가격반응이 강하다.
6. patent/litigation overhang이 없거나 launch delay 가능성이 낮다.
7. product launch가 clinic/hospital adoption 또는 reimbursement path와 연결된다.
```

적용:

```text
Alteogen:
T1~T4 ladder는 Stage2-Actionable → Stage3-Yellow → Green candidate.

SK Bioscience:
IDT acquisition + +11.7%는 Stage2-Actionable.

Samsung Biologics:
policy support +6.23%는 Stage2-Actionable.
GSK facility는 evidence_good_but_price_failed라 full OHLC retest 필요.
```

---

# 11. Stage 3-Yellow 조건

```text
Stage3-Yellow:
- approval / launch / adoption guidance / early sales 중 2~3개가 닫힘
- 하지만 royalty recognition, reimbursement, patent, utilization, margin 중 하나가 남아 있음
```

후보:

```text
Alteogen:
approval + launch + adoption guidance + Qlex early sales.
남은 gate: royalty recognition, patent dispute.

SK Bioscience:
M&A + price reaction.
남은 gate: integration, backlog, utilization.

Samsung Bio / Celltrion:
U.S. facility.
남은 gate: utilization, customer transfer, margin.
```

---

# 12. Stage 3-Green 조건

```text
Stage3-Green:
- approval 이후 실제 product sales / royalty가 확인됨
- adoption rate가 guidance대로 진행됨
- patent/litigation risk가 해소됨
- CDMO는 utilization과 backlog가 확인됨
- U.S. factory/localization은 tariff saving과 margin이 확인됨
- full-window MFE/MAE가 우호적
```

이번 R7 Loop 15에서 Green candidate는 하나다.

```text
Alteogen / Keytruda Qlex:
Green candidate, but royalty and patent gate remain.
```

확정 Green은 보류한다.

```text
stage3_green_confirmed = false
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- FDA approval headline으로 주가가 크게 올랐지만 actual sales/royalty가 없음
- CDMO capacity/factory headline만 있고 utilization이 없음
- M&A 발표 후 integration/backlog가 불명확함
- aesthetic product launch 후 clinic sell-through가 없음
- LO total value가 크지만 upfront가 작고 milestone probability가 낮음
```

적용:

```text
Samsung Biologics GSK facility:
evidence는 좋지만 price failed, utilization 전 Green 금지.

Jeisys:
aesthetic-device structural story는 좋지만 tender/delisting control premium.

Hugel:
product launch만으로 Stage3 금지.

ADEL:
$1.04B total value보다 $80M upfront와 trial progress를 봐야 함.
```

---

# 14. 4C hard gate 조건

```text
R7 4C:
- FDA CRL / approval rejection
- launch delay / patent injunction
- biosimilar patent litigation blocking launch
- product safety issue / recall
- CDMO customer cancellation
- facility utilization collapse
- clinical trial failure
- reimbursement failure
```

이번 R7 Loop 15에서 hard 4C 확정은 없다.

```text
hard_4c_not_confirmed = true
```

Strong 4C-watch:

```text
- Alteogen / Halozyme patent challenge
- Samsung Bioepis / Amgen patent lawsuit
- Samsung Biologics GSK facility evidence-good-price-failed
- U.S. pharma tariff / localization margin uncertainty
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_230.md 요약

```md
# R7 Loop 15. Bio / Healthcare / Medical Device Trigger-level Price Validation

이번 라운드는 R7 Loop 15 trigger-level validation 라운드다.

핵심 결론:
- Alteogen / Keytruda Qlex is the key Stage3-Yellow to Green candidate. Merck reported non-inferiority for SC Keytruda in 2024; planned U.S. launch around October 2025 with expected 30~40% adoption; FDA approved Keytruda Qlex in September 2025; Qlex recorded $128M sales in Q1 2026. Green still requires Alteogen royalty recognition and patent-risk clearance.
- Alteogen/Halozyme is 4C-watch, not hard 4C. WSJ reported enzyme patent dispute risk; Merck later said it would not delay launch and believed it had a strong position.
- Samsung Biologics is Stage2 policy/localization with evidence_good_but_price_failed. Korean pharma policy support lifted Samsung Bio +6.23%, but the later $280M GSK U.S. facility acquisition saw Samsung Bio -0.4% vs KOSPI +2%. Utilization and order conversion are required.
- Celltrion U.S. factory is Stage2 localization. Preferred-bidder trigger, $330M ImClone acquisition, and up to 700B won expansion support tariff hedge, but product transfer, utilization and margin are missing.
- SK Bioscience / IDT Biologika is Stage2-Actionable. 60% stake acquisition for 339B won / $243.75M, shares +11.7%, first major M&A since IPO. Green requires integration, backlog and utilization.
- Hugel / Letybo is Stage2 product launch. FDA-approved neuromodulator launch in the U.S., lower-price Botox competitor narrative. Green requires clinic adoption, U.S. revenue and margin.
- Jeisys Medical / ArchiMed is control-premium M&A, not operating Green. $742M acquisition, revenue +44% CAGR and EBITDA +45% CAGR through FY2023, but tender/delisting dominates the public-market trigger.
- Samsung Bioepis / Amgen is biosimilar patent litigation 4C-watch. Amgen sued over Prolia/Xgeva biosimilars, asserting 34 patents and seeking to block manufacturing/sales.
- ADEL / Sanofi is private reference only. $1.04B total value and $80M upfront show why total LO value must be separated from upfront and milestone probability.

Main calibration:
- Raise FDA approval-to-launch conversion, actual product sales after approval, royalty recognition visibility, adoption-rate guidance, patent litigation clearance, CDMO backlog/utilization, tariff-localization margin benefit, M&A integration/utilization, biosimilar launch settlement, clinic adoption/sell-through.
- Lower trial-result only, approval without revenue, CDMO capacity headline only, factory acquisition without utilization, LO total value without upfront, biosimilar approval without patent clearance, aesthetic launch without sell-through, policy support without company order.
```

## docs/checkpoints/checkpoint_28a_round230_r7_loop15.md 요약

```md
# Checkpoint 28A Round 230 R7 Loop 15 Trigger-level Calibration

## 반영 내용
- R7 Loop 15 trigger-level validation을 수행했다.
- Alteogen/Keytruda Qlex, Samsung Biologics, Celltrion, SK Bioscience, Hugel, Jeisys Medical, Samsung Bioepis, ADEL reference를 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 Reuters / WSJ / FT / MarketWatch의 reported event return과 event price anchor를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- R7 Stage3는 FDA approval만이 아니라 launch, adoption, early sales, royalty recognition으로 올라간다.
- CDMO/factory/localization trigger는 utilization, customer transfer, order backlog, margin 전에는 Stage2다.
- Biosimilar approval path는 patent litigation clearance가 없으면 4C-watch다.
- LO total value는 upfront와 milestone probability를 분리한다.
```

## data/e2r_case_library/cases_r7_loop15_round230.jsonl 초안

```jsonl
{"case_id":"r7_loop15_alteogen_keytruda_qlex","symbol":"196170","company_name":"Alteogen","case_type":"Stage3_Yellow_to_Green_candidate","primary_archetype":"SC_FORMULATION_ROYALTY_STAGE2_TO_GREEN","best_trigger":"T2/T3/T4","stage_candidate":"Stage3-Yellow_to_Green_candidate","price_validation":{"t1_date":"2024-11-19","t1_trigger":"SC Keytruda non-inferiority trial","t1_merck_event_return_pct":1.8,"injection_time_minutes":"2-3","iv_infusion_time_minutes":30,"t2_date":"2025-03-27","t2_launch_plan_date":"2025-10-01","expected_peak_adoption_pct":"30-40","keytruda_2024_sales_usd_bn":30,"t3_date":"2025-09-19","t3_fda_approval":true,"t3_brand_name":"Keytruda Qlex","qlex_q1_2026_sales_usd_mn":128,"alteogen_direct_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage3-Yellow_to_Green_candidate","notes":"Non-inferiority is Stage2; launch/adoption plan is Yellow; FDA approval plus early sales is Green candidate, pending royalty and patent risk."}
{"case_id":"r7_loop15_alteogen_halozyme_patent_watch","symbol":"196170","company_name":"Alteogen / Merck / Halozyme","case_type":"4c_watch","primary_archetype":"SC_FORMULATION_PATENT_4C_WATCH","best_trigger":"T0/T1","stage_candidate":"4C-watch","price_validation":{"trigger_date":"2025-03-05/2025-03-27","patent_counterparty":"Halozyme","merck_patent_petitions":true,"launch_delay_confirmed":false,"merck_no_delay_statement":true,"hard_4c_confirmed":false,"direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","notes":"Patent challenge is 4C-watch, but no hard 4C while launch delay/injunction is absent."}
{"case_id":"r7_loop15_samsung_biologics_tariff_localization","symbol":"207940","company_name":"Samsung Biologics","case_type":"Stage2_policy_evidence_good_but_price_failed","primary_archetype":"BIOPHARMA_TARIFF_LOCALIZATION_STAGE2","best_trigger":"T0/T1","stage_candidate":"Stage2","price_validation":{"pharma_sector_event_return_pct":3.97,"samsung_biologics_event_return_pct":6.23,"us_facility_acquisition_value_usd_mn":280,"facility_location":"Rockville, Maryland","facility_capacity_liters":60000,"us_facility_event_return_pct":-0.4,"kospi_same_context_pct":2.0,"market_relative_return_pp":-2.4,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"evidence_good_but_price_failed","notes":"Biopharma policy support is actionable; U.S. facility acquisition needs utilization/order conversion."}
{"case_id":"r7_loop15_celltrion_us_factory_tariff_hedge","symbol":"068270","company_name":"Celltrion","case_type":"success_candidate_stage2","primary_archetype":"BIOPHARMA_TARIFF_LOCALIZATION_STAGE2","best_trigger":"T1/T2/T3","stage_candidate":"Stage2_localization","price_validation":{"preferred_bidder_date":"2025-07-29","planned_acquisition_operation_investment_krw_bn":700,"imclone_acquisition_value_usd_mn":330,"us_expansion_investment_krw_bn":700,"us_expansion_investment_usd_mn":478,"direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_stage2","notes":"U.S. factory tariff hedge is Stage2; Green requires product transfer, utilization and margin."}
{"case_id":"r7_loop15_sk_bioscience_idt_biologika","symbol":"302440","company_name":"SK Bioscience","case_type":"Stage2_promote_candidate","primary_archetype":"VACCINE_CDMO_MA_STAGE2_ACTIONABLE","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2024-06-27","stake_acquired_pct":60,"deal_value_krw_bn":339,"deal_value_usd_mn":243.75,"event_return_pct":11.7,"first_major_ma_since_ipo":true,"idt_remaining_stake_holder":"Klocke Gruppe 40%","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate","notes":"Vaccine/CDMO M&A with +11.7% price response is Stage2-Actionable; Green requires backlog, utilization and margin."}
{"case_id":"r7_loop15_hugel_letybo_us_launch","symbol":"145020","company_name":"Hugel","case_type":"success_candidate_stage2","primary_archetype":"AESTHETIC_TOXIN_US_LAUNCH_STAGE2","best_trigger":"T0/T1","stage_candidate":"Stage2_product_launch","price_validation":{"fda_approval_context":"moderate-to-severe_glabellar_lines","us_launch_context_date":"2025-03","estimated_letybo_price_usd_per_unit":"9-12","botox_price_usd_per_unit_context":"12-18","claimed_discount_pct_context":30,"direct_hugel_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_stage2","notes":"Aesthetic toxin approval/launch is Stage2; clinic adoption, sell-through and margin are needed for Yellow."}
{"case_id":"r7_loop15_jeisys_archimed_aesthetic_device_ma","symbol":"287410","company_name":"Jeisys Medical","case_type":"event_premium_control_premium","primary_archetype":"AESTHETIC_DEVICE_MA_CONTROL_PREMIUM","best_trigger":"T1/T2","stage_candidate":"Stage2_structural_but_4B_control_premium","price_validation":{"trigger_date":"2024-09-11","acquisition_value_usd_mn":742,"prior_close_price_krw":12860,"global_ebd_market_prior_year_usd_bn":4.5,"global_ebd_market_2032e_usd_bn":16,"revenue_cagr_through_fy2023_pct":44,"adjusted_pretax_earnings_cagr_pct":45,"delisting_process":true,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_4B_watch","notes":"Aesthetic-device market is structural, but tender/delisting control premium dominates public trigger."}
{"case_id":"r7_loop15_samsung_bioepis_amgen_patent_litigation","symbol":"207940_readthrough/Samsung_Bioepis","company_name":"Samsung Bioepis / Amgen","case_type":"4c_watch","primary_archetype":"BIOSIMILAR_PATENT_LITIGATION_4C_WATCH","best_trigger":"T1","stage_candidate":"4C-watch","price_validation":{"trigger_date":"2024-08-13","litigation_counterparty":"Amgen","patents_asserted_count":34,"products":["Prolia biosimilar","Xgeva biosimilar"],"prolia_us_sales_usd_bn":2.7,"xgeva_us_sales_usd_bn":1.5,"requested_relief":["block_making","block_selling","monetary_damages"],"hard_4c_confirmed":false,"direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","notes":"Biosimilar approval/filing is not Green without patent clearance or settlement."}
{"case_id":"r7_loop15_adel_sanofi_private_reference","symbol":"private_reference","company_name":"ADEL / Sanofi","case_type":"private_reference","primary_archetype":"PRIVATE_BIOTECH_LO_REFERENCE","best_trigger":"T1","stage_candidate":"N/A_private","price_validation":{"deal_value_usd_bn":1.04,"upfront_payment_usd_mn":80,"drug_candidate":"ADEL-Y01","trial_stage":"early-stage human trials in U.S.","listed_price_anchor":"N/A_private_company"},"score_price_alignment":"reference_only","notes":"Use as LO calibration reference: total deal value must be separated from upfront and milestone probability."}
```

## data/e2r_trigger_calibration/triggers_r7_loop15_round230.jsonl 초안

```jsonl
{"trigger_id":"r7l15_alteogen_T1","case_id":"r7_loop15_alteogen_keytruda_qlex","trigger_type":"Stage2-Actionable","trigger_date":"2024-11-19","evidence_available":"Merck SC Keytruda non-inferior to IV; injection 2-3 minutes vs IV about 30 minutes; Alteogen enzyme used","event_return_pct":"Merck +1.8 premarket / Alteogen OHLC unavailable","trigger_outcome_label":"Stage2_Actionable","promote_to":"Stage2-Actionable"}
{"trigger_id":"r7l15_alteogen_T2","case_id":"r7_loop15_alteogen_keytruda_qlex","trigger_type":"Stage3-Yellow","trigger_date":"2025-03-27","evidence_available":"Merck launch plan, FDA decision date, expected 30-40% Keytruda adoption within two years","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage3_Yellow_candidate","promote_to":"Stage3-Yellow"}
{"trigger_id":"r7l15_alteogen_T3","case_id":"r7_loop15_alteogen_keytruda_qlex","trigger_type":"Stage3-Green_candidate","trigger_date":"2025-09-19","evidence_available":"FDA approves Keytruda Qlex; 1-2 minute injection; U.S. availability late September","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage3_Green_candidate","promote_to":"Stage3-Green_candidate"}
{"trigger_id":"r7l15_alteogen_T5","case_id":"r7_loop15_alteogen_halozyme_patent_watch","trigger_type":"4C-watch","trigger_date":"2025-03-05","evidence_available":"Halozyme patent challenge risk over enzyme used in injectable Keytruda","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"patent_4C_watch_not_hard","promote_to":"4C-watch"}
{"trigger_id":"r7l15_samsungbio_T0","case_id":"r7_loop15_samsung_biologics_tariff_localization","trigger_type":"Stage2-Actionable","trigger_date":"2025-05-21","evidence_available":"Korea pledges biopharma support under U.S. tariff pressure; pharma sector +3.97%; Samsung Biologics +6.23%","event_return_pct":6.23,"trigger_outcome_label":"Stage2_policy_actionable","promote_to":"Stage2-Actionable"}
{"trigger_id":"r7l15_samsungbio_T1","case_id":"r7_loop15_samsung_biologics_tariff_localization","trigger_type":"evidence_good_but_price_failed","trigger_date":"2025-12-22","evidence_available":"Samsung Biologics buys first U.S. drug production facility from GSK for $280M; shares -0.4% vs KOSPI +2%","event_return_pct":-0.4,"market_relative_return_pp":-2.4,"trigger_outcome_label":"evidence_good_but_price_failed","promote_to":"Stage2_only"}
{"trigger_id":"r7l15_celltrion_T2","case_id":"r7_loop15_celltrion_us_factory_tariff_hedge","trigger_type":"Stage2_localization","trigger_date":"2025-09-23","evidence_available":"Celltrion U.S. subsidiary acquires ImClone Systems from Eli Lilly for $330M to hedge U.S. tariff risk","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"success_candidate_stage2","promote_to":"Stage2"}
{"trigger_id":"r7l15_skbio_T1","case_id":"r7_loop15_sk_bioscience_idt_biologika","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-27","evidence_available":"SK Bioscience buys 60% of Germany's IDT Biologika for 339B won / $243.75M; shares +11.7%","event_return_pct":11.7,"trigger_outcome_label":"Stage2_promote_candidate","promote_to":"Stage2-Actionable"}
{"trigger_id":"r7l15_hugel_T1","case_id":"r7_loop15_hugel_letybo_us_launch","trigger_type":"Stage2_product_launch","trigger_date":"2025-03","evidence_available":"Letybo launched/arriving in U.S. market as FDA-approved neuromodulator and lower-cost Botox competitor","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"success_candidate_stage2","promote_to":"Stage2"}
{"trigger_id":"r7l15_jeisys_T1","case_id":"r7_loop15_jeisys_archimed_aesthetic_device_ma","trigger_type":"event_premium_control_premium","trigger_date":"2024-09-11","evidence_available":"ArchiMed acquires Jeisys Medical for roughly $742M; revenue +44% CAGR and adjusted pretax earnings +45% CAGR through FY2023","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"control_premium_not_operating_Green","promote_to":"4B-watch"}
{"trigger_id":"r7l15_samsungbioepis_T1","case_id":"r7_loop15_samsung_bioepis_amgen_patent_litigation","trigger_type":"4C-watch","trigger_date":"2024-08-13","evidence_available":"Amgen sues Samsung Bioepis over 34 Prolia/Xgeva biosimilar patents, seeks to block manufacturing/sales","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"biosimilar_patent_litigation_4C_watch","promote_to":"4C-watch"}
```

## data/sector_taxonomy/score_weight_profiles_round230_r7_loop15_v1.csv 초안

```csv
archetype,fda_approval_to_launch_conversion,actual_product_sales_after_approval,royalty_recognition_visibility,adoption_rate_guidance,patent_litigation_clearance,cdmo_order_backlog_utilization,tariff_localization_margin_benefit,ma_integration_utilization,biosimilar_launch_settlement,clinic_adoption_sellthrough,trial_result_only_penalty,approval_without_revenue_penalty,cdmo_capacity_headline_only_penalty,total_lo_value_without_upfront_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
SC_FORMULATION_ROYALTY_STAGE2_TO_GREEN,+5,+5,+5,+4,+5,+1,+1,+1,+1,+1,-4,-3,-2,-2,trial+launch+adoption guidance,royalty/patent pending,approval+sales+royalty,Alteogen Qlex ladder template.
SC_FORMULATION_PATENT_4C_WATCH,+2,+2,+4,+2,+5,+0,+0,+0,+0,+0,-2,-2,-1,-1,patent challenge,injunction/launch delay pending,litigation cleared,Alteogen/Halozyme overlay.
BIOPHARMA_TARIFF_LOCALIZATION_STAGE2,+2,+2,+1,+1,+2,+5,+5,+4,+1,+0,-2,-2,-5,-2,policy support/factory acquisition,utilization/order/margin pending,utilization+tariff saving+orders,Samsung Bio/Celltrion localization template.
CDMO_LOCALIZATION_EVIDENCE_GOOD_PRICE_FAILED,+1,+1,+0,+0,+2,+5,+5,+4,+1,+0,-2,-2,-5,-2,factory acquisition with weak price reaction,utilization pending,order conversion,Samsung Bio GSK facility case.
VACCINE_CDMO_MA_STAGE2_ACTIONABLE,+1,+1,+0,+0,+2,+5,+3,+5,+1,+0,-2,-2,-4,-2,M&A+price response,integration/backlog pending,utilization+margin,SK Bioscience IDT template.
AESTHETIC_TOXIN_US_LAUNCH_STAGE2,+4,+3,+1,+2,+3,+0,+0,+1,+1,+5,-3,-4,-1,-1,FDA approval+launch,clinic adoption/revenue pending,sell-through+market share+margin,Hugel Letybo Stage2.
AESTHETIC_DEVICE_MA_CONTROL_PREMIUM,+1,+2,+0,+0,+1,+1,+0,+5,+0,+4,-2,-2,-2,-2,M&A/control premium,public operating data unavailable,post-acquisition growth not public,Jeisys control premium separation.
BIOSIMILAR_PATENT_LITIGATION_4C_WATCH,+2,+2,+1,+1,+5,+0,+0,+1,+5,+0,-2,-3,-1,-1,patent lawsuit,settlement/launch date pending,launch after clearance,Samsung Bioepis/Amgen 4C-watch.
PRIVATE_BIOTECH_LO_REFERENCE,+1,+1,+1,+0,+2,+0,+0,+1,+0,+0,-2,-2,-1,-5,LO total value/upfront split,trial progress pending,N/A,ADEL/Sanofi reference only.
```

---

# 이번 R7 Loop 15 결론

```text
1. Alteogen은 R7의 핵심 Stage3-Yellow→Green 후보다.
   non-inferiority는 Stage2, launch/adoption guidance는 Yellow, FDA approval + Qlex sales는 Green candidate다.

2. Alteogen/Halozyme patent issue는 4C-watch다.
   아직 launch delay나 injunction이 없으므로 hard 4C는 아니다.

3. Samsung Biologics는 policy support와 localization Stage2다.
   정부지원 trigger는 +6.23%였지만, GSK U.S. facility 인수는 -0.4%로 가격반응이 약했다.

4. Celltrion U.S. factory는 Stage2 localization이다.
   tariff hedge는 좋지만 product transfer, utilization, margin이 확인되어야 한다.

5. SK Bioscience / IDT Biologika는 Stage2-Actionable이다.
   60% stake, 339B won, +11.7% price reaction은 plain Stage2보다 강하다.

6. Hugel / Letybo는 Stage2 product launch다.
   U.S. FDA-approved neuromodulator지만 clinic adoption, revenue, margin 전에는 Yellow가 아니다.

7. Jeisys / ArchiMed는 control-premium M&A다.
   aesthetic EBD market은 구조적이지만 public trigger는 tender/delisting event다.

8. Samsung Bioepis / Amgen lawsuit는 biosimilar patent 4C-watch다.
   biosimilar는 approval보다 patent clearance / settlement / launch date가 중요하다.

9. ADEL / Sanofi는 private reference다.
   total LO value와 upfront를 분리해야 한다는 calibration에만 사용한다.
```

한 문장으로 압축하면:

> **R7 Loop 15에서 배운 핵심은 “FDA 승인/공장 인수/LO”가 아니라, approval→launch→adoption→sales/royalty, CDMO capacity→utilization/order, biosimilar approval→patent clearance가 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 product approval만 있거나 factory headline만 있으면 Stage2, patent/litigation은 즉시 4C overlay다.**

[1]: https://www.reuters.com/business/healthcare-pharmaceuticals/merck-says-keytruda-injection-par-with-approved-iv-version-trial-2024-11-19/ "https://www.reuters.com/business/healthcare-pharmaceuticals/merck-says-keytruda-injection-par-with-approved-iv-version-trial-2024-11-19/"
[2]: https://www.reuters.com/business/healthcare-pharmaceuticals/merck-plans-us-launch-subcutaneous-version-keytruda-october-1-2025-03-27/ "https://www.reuters.com/business/healthcare-pharmaceuticals/merck-plans-us-launch-subcutaneous-version-keytruda-october-1-2025-03-27/"
[3]: https://www.reuters.com/business/healthcare-pharmaceuticals/us-fda-approves-mercks-new-injectable-version-keytruda-2025-09-19/ "https://www.reuters.com/business/healthcare-pharmaceuticals/us-fda-approves-mercks-new-injectable-version-keytruda-2025-09-19/"
[4]: https://www.wsj.com/health/pharma/new-version-of-mercks-blockbuster-cancer-drug-threatened-by-patent-battle-b8509c95 "https://www.wsj.com/health/pharma/new-version-of-mercks-blockbuster-cancer-drug-threatened-by-patent-battle-b8509c95"
[5]: https://www.reuters.com/business/healthcare-pharmaceuticals/south-korean-shares-rise-1-pharmaceutical-stocks-jump-2025-05-21/ "https://www.reuters.com/business/healthcare-pharmaceuticals/south-korean-shares-rise-1-pharmaceutical-stocks-jump-2025-05-21/"
[6]: https://www.reuters.com/business/healthcare-pharmaceuticals/samsung-biologics-buy-us-drug-production-facility-gsk-280-mln-2025-12-21/ "https://www.reuters.com/business/healthcare-pharmaceuticals/samsung-biologics-buy-us-drug-production-facility-gsk-280-mln-2025-12-21/"
[7]: https://www.reuters.com/business/healthcare-pharmaceuticals/south-koreas-celltrion-says-tapped-buy-us-pharma-factory-offset-tariff-risk-2025-07-29/ "https://www.reuters.com/business/healthcare-pharmaceuticals/south-koreas-celltrion-says-tapped-buy-us-pharma-factory-offset-tariff-risk-2025-07-29/"
[8]: https://www.reuters.com/world/asia-pacific/celltrion-invest-up-478-mln-expand-us-factory-response-tariffs-2025-11-19/ "https://www.reuters.com/world/asia-pacific/celltrion-invest-up-478-mln-expand-us-factory-response-tariffs-2025-11-19/"
[9]: https://www.reuters.com/markets/deals/south-koreas-sk-bioscience-buy-control-germanys-idt-biologika-244-mln-2024-06-27/ "https://www.reuters.com/markets/deals/south-koreas-sk-bioscience-buy-control-germanys-idt-biologika-244-mln-2024-06-27/"
[10]: https://www.allure.com/story/letybo-neuromodulator-injectable "https://www.allure.com/story/letybo-neuromodulator-injectable"
[11]: https://www.wsj.com/articles/europes-archimed-bets-on-anti-aging-trend-in-first-asia-deal-cbe16f5e "https://www.wsj.com/articles/europes-archimed-bets-on-anti-aging-trend-in-first-asia-deal-cbe16f5e"
[12]: https://www.reuters.com/legal/litigation/amgen-sues-samsung-biotech-unit-over-bone-drug-copies-2024-08-13/ "https://www.reuters.com/legal/litigation/amgen-sues-samsung-biotech-unit-over-bone-drug-copies-2024-08-13/"
[13]: https://www.reuters.com/business/healthcare-pharmaceuticals/south-koreas-adel-signs-up-104-billion-alzheimers-drug-development-deal-with-2025-12-15/ "https://www.reuters.com/business/healthcare-pharmaceuticals/south-koreas-adel-signs-up-104-billion-alzheimers-drug-development-deal-with-2025-12-15/"
