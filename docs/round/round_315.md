순서상 이번은 **R7 Loop 16 — 바이오·헬스케어·의료기기 trigger-level price validation 라운드**다.

이번 R7의 핵심은 **임상 성공·FDA 승인·기술수출·CDMO 수주·공장 인수·의료기기 M&A**를 한 덩어리로 보지 않는 것이다. 바이오는 사진으로 보면 한 장면 같지만, 실제 가격은 완전히 다른 문으로 들어간다. **임상 데이터 → 규제승인 → launch timing → royalty / milestone → 생산능력 → 특허·소송·제조검사 → 실제 매출**이 순서대로 닫혀야 한다.

```text
round = R7 Loop 16
round_id = round_243
large_sector = BIO_HEALTHCARE_MEDICAL_DEVICE
method = trigger_level_backtest_v1_after_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R8 Loop 16
```

이번에도 KRX/Naver/Yahoo/Stooq의 수정주가 일봉 OHLC 30D/90D/180D/1Y/2Y window는 안정적으로 직접 확보하지 못했다. 그래서 full MFE/MAE는 만들지 않고 `price_data_unavailable_after_deep_search`로 분리한다. 대신 Reuters/WSJ/FT/MarketWatch/Barron’s의 **reported event return, approval date, contract value, facility capacity, lawsuit/fine/CRL trigger**를 price anchor로 쓴다. OHLC 미확보 때문에 Stage 후보 자체를 강등하지 않는다.

---

# 1. 이번 라운드 대섹터

```text
R7 = 바이오·헬스케어·의료기기
```

R7의 core gate는 아래다.

```text
신약 / 기술수출:
preclinical / phase data → pivotal trial → FDA/EMA approval → launch → royalty/milestone → partner sales

바이오 플랫폼:
enzyme / ADC linker / bispecific platform → partner product approval → adoption rate → royalty rate → IP/litigation risk

CDMO:
contract / facility acquisition → capacity → client quality audit → utilization → tariff hedge → margin

바이오시밀러:
FDA filing / approval → patent lawsuit → settlement → launch timing → price erosion → market share

백신 / 감염병:
M&A / supply partnership → capacity utilization → demand durability → inventory risk → public procurement

의료기기 / aesthetic:
tender offer / M&A → installed base → consumables → global channel → delisting/control premium risk

4B / 4C:
CRL, FDA inspection observation, patent lawsuit, manufacturing defect, tariff, labor strike, clinical failure, data integrity issue
```

---

# 2. 대상 canonical archetype

```text
SC_FORMULATION_PLATFORM_STAGE3_YELLOW
BIOPHARMA_TARIFF_POLICY_SUPPORT_STAGE2
CDMO_US_FACILITY_EXPANSION_STAGE2_PRICE_MUTED
VACCINE_CDMO_MA_STAGE2_ACTIONABLE
BIOPHARMA_US_LOCALIZATION_STAGE2_WITH_CAPEX_GATE
ONCOLOGY_APPROVAL_STAGE2_WITH_MANUFACTURING_4B
BIOSIMILAR_PATENT_LITIGATION_4C_WATCH
AESTHETIC_MEDICAL_DEVICE_PE_BUYOUT_STAGE2
PHARMA_TARIFF_4B_4C_WATCH
```

---

# 3. deep sub-archetype

```text
Alteogen / Merck Keytruda Qlex:
- Merck Keytruda SC version uses Alteogen enzyme.
- FDA approved Keytruda Qlex in Sep 2025.
- Keytruda had nearly $30B 2024 sales.
- Merck expects SC version to reach 30~40% adoption within two years.
- Qlex generated $128M Q1 2026 sales.
- Direct Alteogen KRX price anchor unavailable in this session.
- Stage3-Yellow candidate; Green requires royalty rate, sales conversion, patent risk clarity.

Samsung Biologics / policy support and U.S. facility:
- Korea pharma sector +3.97% after government support pledge.
- Samsung Biologics +6.23%, Celltrion +0.35%.
- Later Samsung Biologics bought GSK/Human Genome Sciences U.S. facility for $280M.
- Facility has 60,000L drug substance capacity.
- Shares -0.4% while market +2%.
- Stage2 policy support; U.S. facility evidence good but price muted.

SK Bioscience / IDT Biologika:
- 60% stake in German CDMO IDT Biologika.
- Deal value 339B won / $243.75M.
- First major M&A since 2021 IPO.
- SK Bioscience shares +11.7% morning trade.
- Stage2-Actionable; Green requires utilization, contract backlog, vaccine demand.

Celltrion / U.S. factory localization:
- Preferred bidder for U.S. pharma manufacturing facility.
- Planned 700B won investment; possible additional 300B~700B depending on tariffs.
- Later U.S. subsidiary acquired ImClone Systems from Eli Lilly for $330M.
- Another plan to invest up to 700B won / $478M to expand U.S. factory.
- Stage2 localization; price anchor unavailable.

Yuhan / Lazertinib / J&J Rybrevant:
- FDA approved Rybrevant + lazertinib combination in Aug 2024.
- J&J expects over $5B peak sales from Rybrevant.
- FDA later declined SC Rybrevant approval due to manufacturing inspection observations, not efficacy/safety.
- Stage2 approval + manufacturing 4B.

Samsung Bioepis / Amgen lawsuit:
- Amgen sued Samsung Bioepis over proposed Prolia/Xgeva biosimilars.
- 34 patents alleged.
- Prolia/Xgeva U.S. sales exceeded $4.2B in prior year.
- Biosimilar launch timing is legal gate.
- 4C-watch patent/litigation.

Jeisys Medical / ArchiMed:
- ArchiMed acquired Korean aesthetic medical-device maker Jeisys for about $742M.
- Jeisys shares closed at 12,860 won around deal process.
- EBD devices target wrinkles, scars, body contouring, hair removal.
- Stage2 medical-device M&A, but buyout/delisting/control premium is not operating Green.

Asian pharma tariff shock:
- Trump announced 100% tariffs on branded drug imports unless producers have U.S. manufacturing.
- Asian pharma stocks fell; branded-drug exporters with U.S. exposure hit.
- Korean drugmakers’ U.S. manufacturing localization becomes Stage2 hedge; tariff uncertainty remains 4B/4C.
```

---

# 4. 선정 case 요약

| bucket                        | case                                  | 핵심 판정                                                                                                                   |
| ----------------------------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Stage3-Yellow candidate       | Alteogen / Merck Keytruda SC          | FDA approval + Keytruda $30B franchise + 30~40% adoption target + Qlex Q1 2026 sales. Direct Alteogen price unavailable |
| Stage2 policy support         | Samsung Biologics / pharma support    | Bio sector +3.97%, Samsung Biologics +6.23%. 정책 support는 Stage2, business conversion 필요                                 |
| evidence_good_but_price_muted | Samsung Biologics / GSK U.S. facility | $280M U.S. facility, 60,000L capacity, but stock -0.4% vs market +2%                                                    |
| Stage2-Actionable             | SK Bioscience / IDT Biologika         | 339B won / $244M acquisition, +11.7%. M&A trigger strong                                                                |
| Stage2 localization           | Celltrion / U.S. factory              | U.S. factory acquisition and expansion to offset tariff risk. Price anchor unavailable                                  |
| Stage2 + 4B                   | Yuhan / lazertinib / J&J              | FDA approval is positive, SC Rybrevant CRL due manufacturing inspection is 4B                                           |
| 4C-watch                      | Samsung Bioepis / Amgen lawsuit       | Patent litigation over Prolia/Xgeva biosimilars. Launch timing legal gate                                               |
| Stage2 medical-device M&A     | Jeisys / ArchiMed                     | $742M aesthetic-device buyout, but control premium/delisting, not Green                                                 |
| 4B/4C-watch                   | Pharma tariff shock                   | U.S. manufacturing becomes strategic, but tariff/policy uncertainty persists                                            |

---

# 5. Case별 trigger grid

## Case A — Alteogen / Merck Keytruda subcutaneous formulation

```text
symbol = 196170
case_type = Stage3-Yellow candidate
archetype = SC_FORMULATION_PLATFORM_STAGE3_YELLOW
```

| trigger |                    type | date       | 당시 공개 evidence                                                                                               | 가격 anchor                         | outcome          |
| ------- | ----------------------: | ---------- | ------------------------------------------------------------------------------------------------------------ | --------------------------------- | ---------------- |
| T0      |         Stage2 evidence | 2024-11-19 | Merck says SC Keytruda trial was non-inferior to IV version; Alteogen manufactures enzyme used with Keytruda | direct Alteogen price unavailable | Stage2           |
| T1      |       Stage2 validation | 2025-03-27 | Merck plans U.S. launch Oct 1; expects 30~40% Keytruda patient adoption within 2 years                       | unavailable                       | validation       |
| T2      | Stage3-Yellow candidate | 2025-09-19 | FDA approves Keytruda Qlex SC formulation                                                                    | unavailable                       | Yellow candidate |
| T3      |       Stage3 validation | 2026-04-30 | Merck reports $128M Qlex sales in Q1 2026                                                                    | unavailable                       | validation       |
| T4      |                4B-watch | 2025~      | Halozyme patent challenge risk / royalty economics not disclosed                                             | unavailable                       | 4B               |
| T5      |            Stage3-Green | N/A        | Alteogen royalty rate, full OHLC, sustained sales conversion unavailable                                     | no Green                          | 보류               |

Alteogen은 이번 R7에서 가장 좋은 platform-to-product validation case다. Merck의 SC Keytruda는 Alteogen enzyme을 사용하고, 기존 IV infusion 대비 투여시간을 30분 안팎에서 1~2분 또는 2분 수준으로 줄이는 제품이다. Keytruda는 2024년 거의 $30B 매출을 낸 blockbuster이고, Merck는 SC version adoption이 2년 안에 Keytruda 환자의 30~40%까지 갈 수 있다고 봤다. FDA는 2025년 9월 Keytruda Qlex를 승인했고, Merck는 2026년 Q1에 Qlex sales $128M을 기록했다. 다만 Alteogen 직접 KRX price anchor와 royalty rate가 확보되지 않았으므로 Green은 보류하고 `Stage3-Yellow candidate`로 둔다. ([Reuters][1])

```json
{
  "case_id": "r7_loop16_alteogen_keytruda_sc",
  "symbol": "196170",
  "best_trigger": "T2/T3",
  "best_trigger_type": "Stage3-Yellow_candidate",
  "t0_trial_date": "2024-11-19",
  "t1_launch_plan_date": "2025-03-27",
  "t2_fda_approval_date": "2025-09-19",
  "t3_sales_validation_date": "2026-04-30",
  "keytruda_2024_sales_usd_bn": 30,
  "expected_sc_adoption_pct": "30-40",
  "qlex_q1_2026_sales_usd_mn": 128,
  "administration_time_improvement": "about_30_minutes_IV_to_1-2_minutes_SC",
  "direct_alteogen_price_anchor": "price_data_unavailable_after_deep_search",
  "4B_overlay": [
    "royalty_rate_not_disclosed",
    "Halozyme_patent_challenge_risk",
    "Merck_sales_conversion_dependency",
    "full_OHLC_unavailable"
  ],
  "trigger_outcome_label": "Stage3_Yellow_candidate_platform_to_product"
}
```

---

## Case B — Samsung Biologics / Korea pharma policy support and U.S. tariff hedge

```text
symbol = 207940
case_type = Stage2 policy support
archetype = BIOPHARMA_TARIFF_POLICY_SUPPORT_STAGE2
```

| trigger |          type | date       | 당시 공개 evidence                                                             | 가격 anchor                                                                      | outcome    |
| ------- | ------------: | ---------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ---------- |
| T0      | Stage2 policy | 2025-05-21 | Korea pledges biopharma support amid U.S. tariff pressure                  | pharma sector +3.97%, Samsung Biologics +6.23%, Celltrion +0.35%, KOSPI +0.99% | Stage2     |
| T1      |    validation | 2025-05-21 | Korean pharma exports $9.59B in 2024, U.S. 16% of pharma exports           | same                                                                           | validation |
| T2      |      4B-watch | 2025       | tariff details, FDA inspection, U.S. production strategy not yet closed    | no full OHLC                                                                   | 4B         |
| T3      | Stage3-Yellow | N/A        | actual order backlog / U.S. manufacturing / tariff exemption not confirmed | no Yellow                                                                      | 보류         |

Samsung Biologics의 2025년 5월 21일 움직임은 “정책 support가 가격을 밀어준 Stage2”다. 한국 정부가 biopharmaceutical sector 지원을 약속하자 KOSPI pharma sector는 +3.97%, Samsung Biologics는 +6.23%, Celltrion은 +0.35% 올랐다. 같은 맥락에서 한국 pharma exports는 2024년 $9.59B였고, 그중 U.S.향이 16%였다는 점도 확인된다. 하지만 정책 support는 곧바로 Stage3가 아니다. tariff details, FDA inspection, U.S. manufacturing strategy, 실제 order backlog가 닫혀야 Yellow다. ([Reuters][2])

```json
{
  "case_id": "r7_loop16_samsung_biologics_policy_support",
  "symbol": "207940",
  "best_trigger": "T0/T1",
  "best_trigger_type": "Stage2_policy_support",
  "trigger_date": "2025-05-21",
  "pharma_sector_event_return_pct": 3.97,
  "samsung_biologics_event_return_pct": 6.23,
  "celltrion_event_return_pct": 0.35,
  "kospi_event_return_pct": 0.99,
  "korea_pharma_exports_2024_usd_bn": 9.59,
  "us_share_of_korea_pharma_exports_pct": 16,
  "stage3_gate_missing": [
    "tariff_details",
    "US_manufacturing_plan",
    "FDA_inspection_outcome",
    "new_CDMO_order_backlog",
    "margin_guidance"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_policy_support_not_Green"
}
```

---

## Case C — Samsung Biologics / GSK U.S. facility acquisition

```text
symbol = 207940
case_type = evidence good but price muted
archetype = CDMO_US_FACILITY_EXPANSION_STAGE2_PRICE_MUTED
```

| trigger |            type | date       | 당시 공개 evidence                                                                | 가격 anchor                | outcome                    |
| ------- | --------------: | ---------- | ----------------------------------------------------------------------------- | ------------------------ | -------------------------- |
| T0      | Stage2 evidence | 2025-12-22 | Samsung Biologics buys first U.S. drug production facility from GSK for $280M | shares -0.4%, market +2% | evidence good, price muted |
| T1      |      validation | 2025-12-22 | Rockville facility has 60,000L drug substance capacity                        | same                     | capacity validation        |
| T2      |        4B-watch | 2025~2026  | closing, upgrade capex, utilization, client transfer not confirmed            | no full OHLC             | 4B                         |
| T3      |   Stage3-Yellow | N/A        | customer contracts / utilization / margin not confirmed                       | no Yellow                | 보류                         |

GSK facility acquisition은 전략적으로 좋지만 price가 Green을 거부한 case다. Samsung Biologics는 GSK로부터 Rockville, Maryland의 Human Genome Sciences facility를 $280M에 인수해 첫 U.S. drug production site를 확보한다. 해당 시설은 60,000L drug substance capacity를 갖고 있고, 회사는 추가 투자와 technology upgrade를 계획했다. 그런데 발표일 shares는 -0.4%였고 broader market은 +2%였다. 이건 `evidence_good_but_price_muted`다. ([Reuters][3])

```json
{
  "case_id": "r7_loop16_samsung_biologics_gsk_us_facility",
  "symbol": "207940",
  "best_trigger": "T0/T1",
  "best_trigger_type": "Stage2_facility_expansion_price_muted",
  "trigger_date": "2025-12-22",
  "acquisition_value_usd_mn": 280,
  "facility_location": "Rockville_Maryland",
  "facility_capacity_liters": 60000,
  "event_return_pct": -0.4,
  "market_context_pct": 2.0,
  "market_relative_return_pp": -2.4,
  "stage3_gate_missing": [
    "deal_closing",
    "capacity_upgrade_plan",
    "client_transfer",
    "utilization",
    "US_tariff_hedge_effect",
    "margin_accretion"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "evidence_good_but_price_muted"
}
```

---

## Case D — SK Bioscience / IDT Biologika acquisition

```text
symbol = 302440
case_type = Stage2-Actionable
archetype = VACCINE_CDMO_MA_STAGE2_ACTIONABLE
```

| trigger |            type | date       | 당시 공개 evidence                                                 | 가격 anchor                   | outcome          |
| ------- | --------------: | ---------- | -------------------------------------------------------------- | --------------------------- | ---------------- |
| T0      | Stage2 evidence | 2024-06-27 | SK Bioscience to acquire 60% stake in Germany’s IDT Biologika  | shares +11.7% morning trade | excellent Stage2 |
| T1      |      validation | 2024-06-27 | deal value 339B won / $243.75M; first major M&A since 2021 IPO | same                        | validation       |
| T2      |        4B-watch | 2024~      | integration, vaccine demand, CMO utilization, acquisition ROI  | no full OHLC                | 4B               |
| T3      |   Stage3-Yellow | N/A        | utilization/backlog/margin not confirmed                       | no Yellow                   | 보류               |

SK Bioscience는 이번 R7의 가장 좋은 Stage2-Actionable M&A case다. 회사는 Germany CDMO IDT Biologika의 60% stake를 339B won, 약 $243.75M에 인수한다고 발표했고, SK Bioscience shares는 발표 후 morning trade에서 +11.7% 올랐다. 이는 2021년 IPO 이후 첫 major M&A였다. 다만 vaccine demand, CDMO utilization, integration margin이 닫히기 전에는 Green이 아니다. ([Reuters][4])

```json
{
  "case_id": "r7_loop16_sk_bioscience_idt_biologika",
  "symbol": "302440",
  "best_trigger": "T0/T1",
  "best_trigger_type": "Stage2-Actionable_MA",
  "trigger_date": "2024-06-27",
  "stake_acquired_pct": 60,
  "deal_value_krw_bn": 339,
  "deal_value_usd_mn": 243.75,
  "event_return_pct": 11.7,
  "first_major_ma_since_ipo": true,
  "stage3_gate_missing": [
    "IDT_utilization",
    "contract_backlog",
    "vaccine_demand_durability",
    "integration_margin",
    "post_acquisition_ROIC"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable_MA"
}
```

---

## Case E — Celltrion / U.S. manufacturing localization

```text
symbol = 068270
case_type = Stage2 localization with capex gate
archetype = BIOPHARMA_US_LOCALIZATION_STAGE2_WITH_CAPEX_GATE
```

| trigger |            type | date       | 당시 공개 evidence                                                    | 가격 anchor                          | outcome             |
| ------- | --------------: | ---------- | ----------------------------------------------------------------- | ---------------------------------- | ------------------- |
| T0      | Stage2 evidence | 2025-07-29 | Celltrion selected as preferred bidder for U.S. pharma factory    | direct Celltrion price unavailable | Stage2              |
| T1      |      validation | 2025-09-23 | Celltrion U.S. unit buys ImClone Systems from Eli Lilly for $330M | unavailable                        | validation          |
| T2      |      validation | 2025-11-19 | Celltrion to invest up to 700B won / $478M to expand U.S. factory | unavailable                        | capacity validation |
| T3      |        4B-watch | 2025~      | high U.S. cost, tariff policy, utilization, capex ROI             | no OHLC                            | 4B                  |
| T4      |   Stage3-Yellow | N/A        | U.S. production margin and tariff shield not confirmed            | no Yellow                          | 보류                  |

Celltrion은 R7에서 U.S. localization Stage2다. 회사는 U.S. tariff risk를 줄이기 위해 U.S. manufacturing facility 인수의 preferred bidder가 됐고, 700B won 규모 투자를 계획했다. 이후 U.S. subsidiary가 Eli Lilly로부터 ImClone Systems를 $330M에 인수했고, 2025년 11월에는 U.S. factory capacity expansion에 최대 700B won, 약 $478M을 투자하겠다고 했다. 다만 U.S. cost, utilization, tariff shield, biosimilar margin이 닫히지 않았기 때문에 Green이 아니라 Stage2다. ([Reuters][5])

```json
{
  "case_id": "r7_loop16_celltrion_us_factory_localization",
  "symbol": "068270",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_US_localization_with_capex_gate",
  "preferred_bidder_date": "2025-07-29",
  "planned_initial_investment_krw_bn": 700,
  "possible_additional_investment_krw_bn": "300-700",
  "imclone_acquisition_date": "2025-09-23",
  "imclone_acquisition_value_usd_mn": 330,
  "expansion_investment_date": "2025-11-19",
  "expansion_investment_krw_bn": 700,
  "expansion_investment_usd_mn": 478,
  "direct_celltrion_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "US_factory_utilization",
    "tariff_avoidance_effect",
    "biosimilar_margin",
    "customer_pipeline_transfer",
    "capex_ROI"
  ],
  "trigger_outcome_label": "Stage2_US_localization_not_Green"
}
```

---

## Case F — Yuhan / lazertinib / J&J Rybrevant approval and SC manufacturing gate

```text
symbol = 000100
case_type = Stage2 approval with manufacturing 4B
archetype = ONCOLOGY_APPROVAL_STAGE2_WITH_MANUFACTURING_4B
```

| trigger |            type | date       | 당시 공개 evidence                                                                           | 가격 anchor                      | outcome          |
| ------- | --------------: | ---------- | ---------------------------------------------------------------------------------------- | ------------------------------ | ---------------- |
| T0      | Stage2 approval | 2024-08-20 | FDA approves J&J Rybrevant + lazertinib chemotherapy-free first-line NSCLC treatment     | direct Yuhan price unavailable | Stage2           |
| T1      |      validation | 2024-08-20 | EGFR mutation occurs in 10~15% of U.S. NSCLC; J&J expects over $5B peak Rybrevant sales  | unavailable                    | validation       |
| T2      |        4B-watch | 2024-12-16 | FDA declines SC Rybrevant approval due to manufacturing facility inspection observations | unavailable                    | manufacturing 4B |
| T3      |   Stage3-Yellow | N/A        | Yuhan royalty/milestone/sales share and SC approval path not confirmed                   | no Yellow                      | 보류               |

Yuhan의 lazertinib은 승인 evidence 자체는 강하다. FDA는 J&J의 Rybrevant + lazertinib combination을 EGFR-mutated advanced NSCLC 1차 치료제로 승인했고, J&J는 Rybrevant peak sales가 $5B를 넘을 수 있다고 봤다. 하지만 2024년 12월 FDA가 SC Rybrevant approval을 manufacturing facility inspection observations 때문에 거절했다. 이 rejection은 efficacy/safety가 아니라 manufacturing issue였고 추가 임상은 요구되지 않았지만, R7 scoring상 launch convenience와 uptake를 지연시킬 수 있는 4B다. ([Reuters][6])

```json
{
  "case_id": "r7_loop16_yuhan_lazertinib_jnj_rybrevant",
  "symbol": "000100",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_approval_with_manufacturing_4B",
  "approval_date": "2024-08-20",
  "approved_combo": "Rybrevant_plus_lazertinib",
  "indication": "first_line_EGFR_mutated_advanced_NSCLC",
  "egfr_mutation_us_nsclc_pct": "10-15",
  "rybrevant_peak_sales_expectation_usd_bn": ">5",
  "sc_crl_date": "2024-12-16",
  "crl_reason": "manufacturing_facility_inspection_observations",
  "crl_not_related_to": [
    "formulation",
    "efficacy",
    "safety"
  ],
  "direct_yuhan_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "Yuhan_royalty_rate",
    "lazertinib_milestone_revenue",
    "commercial_launch_sales",
    "SC_Rybrevant_resolution",
    "partner_sales_conversion"
  ],
  "trigger_outcome_label": "approval_stage2_with_manufacturing_4B"
}
```

---

## Case G — Samsung Bioepis / Amgen Prolia-Xgeva biosimilar patent lawsuit

```text
symbol = 207940_readthrough
case_type = patent litigation 4C-watch
archetype = BIOSIMILAR_PATENT_LITIGATION_4C_WATCH
```

| trigger |            type | date       | 당시 공개 evidence                                                        | 가격 anchor            | outcome           |
| ------- | --------------: | ---------- | --------------------------------------------------------------------- | -------------------- | ----------------- |
| T0      | Stage2 evidence | 2024       | Samsung Bioepis applied for U.S. approval of Prolia/Xgeva biosimilars | no price             | Stage2            |
| T1      |        4C-watch | 2024-08-13 | Amgen sues Samsung Bioepis, alleging infringement of 34 patents       | no Samsung Bio price | litigation 4C     |
| T2      |      validation | 2024-08-13 | Prolia U.S. sales >$2.7B, Xgeva >$1.5B previous year                  | no price             | market validation |
| T3      |          relief | N/A        | settlement / launch timing / patent resolution not confirmed          | no relief            | 보류                |

Samsung Bioepis biosimilar case는 R7에서 “승인 신청이 있어도 patent litigation이 launch를 막는” 4C-watch다. Amgen은 Samsung Bioepis의 Prolia/Xgeva biosimilar가 34개 patents를 침해한다고 New Jersey federal court에 소송을 제기했고, Prolia U.S. sales는 전년 $2.7B 이상, Xgeva는 $1.5B 이상이었다. 이 시장은 크지만, patent litigation과 launch timing이 닫히기 전에는 Stage3가 아니다. ([Reuters][7])

```json
{
  "case_id": "r7_loop16_samsung_bioepis_amgen_litigation",
  "symbol": "207940_readthrough",
  "best_trigger": "T1/T2",
  "best_trigger_type": "4C_watch_patent_litigation",
  "trigger_date": "2024-08-13",
  "originator": "Amgen",
  "products": [
    "Prolia",
    "Xgeva"
  ],
  "alleged_patents": 34,
  "prolia_us_sales_prior_year_usd_bn": 2.7,
  "xgeva_us_sales_prior_year_usd_bn": 1.5,
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "settlement",
    "launch_date",
    "patent_resolution",
    "price_erosion",
    "market_share_capture"
  ],
  "trigger_outcome_label": "biosimilar_patent_litigation_4C_watch"
}
```

---

## Case H — Jeisys Medical / ArchiMed aesthetic medical-device buyout

```text
symbol = 287410
case_type = Stage2 medical-device M&A / control premium
archetype = AESTHETIC_MEDICAL_DEVICE_PE_BUYOUT_STAGE2
```

| trigger |          type | date       | 당시 공개 evidence                                                                                | 가격 anchor                      | outcome                   |
| ------- | ------------: | ---------- | --------------------------------------------------------------------------------------------- | ------------------------------ | ------------------------- |
| T0      |    Stage2 M&A | 2024-09-11 | ArchiMed finalizes about $742M acquisition of Jeisys Medical                                  | shares closed 12,860 won       | Stage2                    |
| T1      |    validation | 2024-09-11 | Jeisys makes energy-based devices for wrinkle reduction, scars, body contouring, hair removal | same                           | medical-device validation |
| T2      |      4B-watch | 2024       | delisting process, control premium, PE ownership, public-market exit                          | no public OHLC after delisting | 4B                        |
| T3      | Stage3-Yellow | N/A        | public-shareholder return after delisting not applicable; operating growth private            | no Yellow                      | 보류                        |

Jeisys는 R7 의료기기 M&A template다. ArchiMed는 Korean aesthetic medical-device company Jeisys Medical을 약 $742M에 인수했고, Jeisys shares는 deal process 당시 Seoul에서 12,860 won에 마감했다. Jeisys는 radio waves, ultrasound, lasers 등을 활용한 energy-based devices를 만들며 wrinkle reduction, acne/scar treatment, body contouring, hair removal에 쓰인다. 하지만 이건 public-company operating rerating이 아니라 PE buyout/control premium이며 delisting process가 붙어 있다. 그래서 Stage2 M&A로만 두고 Green은 금지한다. ([월스트리트저널][8])

```json
{
  "case_id": "r7_loop16_jeisys_archimed_medical_device_buyout",
  "symbol": "287410",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_medical_device_MA_with_control_premium_4B",
  "trigger_date": "2024-09-11",
  "acquisition_value_usd_mn": 742,
  "reported_share_close_krw": 12860,
  "device_type": "energy_based_devices",
  "applications": [
    "wrinkle_reduction",
    "acne_scar_treatment",
    "body_contouring",
    "permanent_hair_removal"
  ],
  "4B_overlay": [
    "delisting_process",
    "control_premium",
    "private_equity_ownership",
    "public_market_exit"
  ],
  "full_mfe_mae_status": "not_applicable_after_buyout",
  "trigger_outcome_label": "Stage2_MA_not_operating_Green"
}
```

---

## Case I — Pharma tariff shock / localization hedge

```text
symbols = 207940 / 068270 / 302440 / pharma_basket
case_type = 4B/4C-watch policy shock
archetype = PHARMA_TARIFF_4B_4C_WATCH
```

| trigger |          type | date       | 당시 공개 evidence                                                                         | 가격 anchor                | outcome |
| ------- | ------------: | ---------- | -------------------------------------------------------------------------------------- | ------------------------ | ------- |
| T0      |   4B/4C-watch | 2025-09-26 | Trump announces 100% tariffs on branded drug imports unless U.S. manufacturing begun   | Asian pharma stocks fell | 4B/4C   |
| T1      |  Stage2 hedge | 2025       | Samsung Biologics, Celltrion, SK Bioscience pursue U.S./EU manufacturing / CDMO assets | mixed                    | hedge   |
| T2      |      4B-watch | 2025~      | final tariff rate, branded vs generic, plant certification timeline uncertain          | no OHLC                  | 4B      |
| T3      | Stage3-Yellow | N/A        | actual tariff avoidance and margin protection not confirmed                            | no Yellow                | 보류      |

Pharma tariff는 R7의 policy hard overlay다. Trump는 branded drug imports에 100% tariff를 부과하겠다고 했고, U.S. manufacturing을 이미 착공한 기업은 예외로 두겠다는 구조였다. Reuters는 Asian pharma shares가 떨어졌고, branded-drug exposure가 있는 회사가 타격을 받았다고 보도했다. 이 trigger 때문에 Samsung Biologics, Celltrion, SK Bioscience 같은 names의 U.S./EU facility 확보는 Stage2 hedge가 되지만, final tariff rate, plant certification timeline, 실제 margin protection이 없으면 Green이 아니다. ([Reuters][9])

```json
{
  "case_id": "r7_loop16_pharma_tariff_localization",
  "symbols": "207940/068270/302440/pharma_basket",
  "best_trigger": "T0/T2",
  "best_trigger_type": "4B_4C_policy_shock_with_Stage2_localization_hedge",
  "trigger_date": "2025-09-26",
  "tariff_rate_context_pct": 100,
  "tariff_scope": "branded_drug_imports_unless_US_manufacturing_started",
  "localization_hedge_examples": [
    "Samsung_Biologics_US_facility",
    "Celltrion_US_factory",
    "SK_Bioscience_IDT_Biologika"
  ],
  "direct_korea_basket_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "final_tariff_rate",
    "US_plant_certification",
    "product_transfer",
    "margin_protection",
    "regulatory_approval"
  ],
  "trigger_outcome_label": "pharma_tariff_4B_4C_with_localization_hedge"
}
```

---

# 6. Trigger별 가격경로 검증 요약

| case                           | best trigger |        entry anchor |                                          event MFE/MAE |  market-relative | full MFE/MAE   | outcome                       |
| ------------------------------ | ------------ | ------------------: | -----------------------------------------------------: | ---------------: | -------------- | ----------------------------- |
| Alteogen / Keytruda SC         | T2/T3        |   no Alteogen price |           Qlex approval/sales validation, no KRX price |              N/A | unavailable    | Stage3-Yellow candidate       |
| Samsung Biologics policy       | T0/T1        |        sector event | Samsung Bio +6.23%, pharma sector +3.97%, KOSPI +0.99% | +5.24pp vs KOSPI | unavailable    | Stage2 policy                 |
| Samsung Biologics GSK facility | T0/T1        |               event |                                    -0.4% vs market +2% |           -2.4pp | unavailable    | evidence good but price muted |
| SK Bioscience IDT              | T0/T1        |               event |                                   +11.7% morning trade |      unavailable | unavailable    | Stage2-Actionable             |
| Celltrion U.S. factory         | T0/T2        |            no price |                                        no direct price |              N/A | unavailable    | Stage2 localization           |
| Yuhan / lazertinib             | T0/T2        |      no Yuhan price |                                        no direct price |              N/A | unavailable    | Stage2 approval + 4B          |
| Samsung Bioepis litigation     | T1/T2        |     no direct price |                                        no direct price |              N/A | unavailable    | 4C-watch                      |
| Jeisys / ArchiMed              | T0/T2        |    12,860 won close |                         buyout/control premium context |              N/A | not applicable | Stage2 M&A                    |
| Pharma tariff                  | T0/T2        | Asian pharma basket |                                  no Korean basket OHLC |              N/A | unavailable    | 4B/4C-watch                   |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
좋은 Stage2:
- Samsung Biologics policy support
- Celltrion U.S. factory localization
- Yuhan/J&J lazertinib approval
- Jeisys medical-device M&A
- Pharma tariff localization hedge

약한 Stage2:
- Samsung Biologics GSK facility: evidence good but price muted.
- Celltrion localization: strong strategy but direct price unavailable.
- Yuhan: approval is strong but Yuhan royalty/sales economics unavailable.
```

## Stage2-Actionable entry 성과

```text
Actionable:
- SK Bioscience / IDT Biologika: +11.7% price reaction and clear deal value.
- Samsung Biologics policy support: +6.23% with sector tailwind.
- Alteogen / Keytruda SC: product-level validation strong, but direct KRX price unavailable.

Actionable 보류:
- Celltrion U.S. factory: capex and localization clear, but price unavailable.
- Jeisys: buyout/control premium, not operating rerating.
```

## Stage3-Yellow 후보

```text
Yellow 후보:
- Alteogen: Qlex approval and sales validation; royalty/sales conversion needed.
- Samsung Biologics: CDMO backlog/utilization and U.S. site utilization if confirmed.
- SK Bioscience: IDT utilization and vaccine/CDMO order backlog if confirmed.
- Yuhan: lazertinib royalties/milestones and partner sales conversion if confirmed.
```

## Stage3-Green

```text
이번 R7 Loop 16에서 확정 Green 없음.

이유:
- Alteogen은 product validation은 강하지만 royalty economics and direct OHLC가 없다.
- Samsung Biologics/Celltrion은 U.S. facility localization이 tariff hedge지만 utilization/margin이 없다.
- SK Bioscience는 M&A가 강하지만 post-acquisition utilization이 필요하다.
- Yuhan은 approval이 있지만 SC Rybrevant manufacturing CRL overlay가 있다.
- Samsung Bioepis는 patent litigation gate가 있다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- SK Bioscience / IDT Biologika
- Samsung Biologics policy support
- Samsung Biologics GSK facility price-muted reaction
- Alteogen / Keytruda SC as product-validation Yellow candidate

Stage2_promote_candidate:
- SK Bioscience
- Samsung Biologics policy support
- Alteogen, if direct price and royalty data confirm
- Celltrion localization, if utilization/margin confirm

Stage3-Yellow candidate:
- Alteogen
- SK Bioscience, after IDT utilization
- Samsung Biologics, after U.S. facility utilization and CDMO backlog
- Yuhan, after royalty/milestone conversion

evidence_good_but_price_failed_or_muted:
- Samsung Biologics GSK facility
- Celltrion U.S. factory due no price anchor
- Yuhan lazertinib due no Yuhan price anchor

event_premium:
- Jeisys buyout/control premium
- pharma tariff localization hedge

thesis_break_watch:
- Samsung Bioepis / Amgen patent lawsuit
- J&J SC Rybrevant CRL manufacturing observations
- pharma tariff shock

hard_4C_success:
- 이번 R7에서는 confirmed hard 4C 없음
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
regulatory_approval_to_sales_bridge,+5,"FDA approval이 실제 partner sales로 연결되면 Yellow 이상","Alteogen, Yuhan"
royalty_milestone_visibility,+5,"기술수출/플랫폼은 royalty/milestone disclosure가 핵심","Alteogen, Yuhan"
CDMO_capacity_utilization,+5,"CDMO는 capacity보다 utilization and signed backlog가 Green gate","Samsung Biologics, SK Bioscience, Celltrion"
US_localization_tariff_hedge,+4,"U.S. facility는 tariff hedge로 Stage2","Samsung Biologics, Celltrion"
M&A_price_reaction,+4,"M&A 발표 후 +5% 이상이면 Stage2-Actionable 후보","SK Bioscience"
partner_product_adoption,+5,"Keytruda Qlex처럼 partner adoption target/sales가 있으면 승격","Alteogen"
patent_litigation_resolution,+5,"biosimilar는 patent gate가 launch timing을 결정","Samsung Bioepis"
manufacturing_inspection_cleanliness,+5,"FDA inspection observation은 launch 4B/4C","Yuhan/J&J"
```

## 내릴 축

```csv
axis,delta,reason,cases
approval_without_economics,-5,"승인만 있고 royalty/sales economics 없으면 Green 금지","Yuhan, Alteogen"
facility_acquisition_without_utilization,-5,"공장 인수만으로 CDMO Green 금지","Samsung Biologics, Celltrion"
policy_support_without_backlog,-4,"정부 지원은 order backlog 전에는 Stage2","Samsung Biologics"
biotech_MA_without_ROIC,-4,"M&A는 integration/utilization 전에는 4B","SK Bioscience"
biosimilar_filing_without_patent_clearance,-5,"바이오시밀러 신청은 patent 해결 전 Green 금지","Samsung Bioepis"
control_premium_delisting_without_public_forward_return,-5,"PE buyout은 operating rerating과 분리","Jeisys"
tariff_headline_without_margin_protection,-4,"tariff hedge는 실제 margin 보호 전에는 4B","pharma basket"
```

---

# 10. Stage2-Actionable 승격 조건

R7 Loop 16 shadow rule:

```text
R7에서 Stage2 evidence가 아래 중 3개 이상이면 Stage2-Actionable로 승격한다.

1. FDA/EMA/MFDS approval or pivotal trial success가 있다.
2. partner product가 실제 launch 또는 sales를 시작했다.
3. royalty/milestone economics가 확인된다.
4. event return이 +5% 이상이다.
5. CDMO/M&A deal value와 capacity가 명확하다.
6. U.S./EU facility가 tariff hedge or customer proximity로 연결된다.
7. patent lawsuit, CRL, FDA inspection, manufacturing defect 4B/4C overlay가 없다.
```

적용:

```text
SK Bioscience:
deal value + clear M&A + +11.7% reaction → Stage2-Actionable.

Samsung Biologics policy:
+6.23% and sector support → Stage2, but backlog missing.

Alteogen:
approval + partner sales validation → Yellow candidate, but direct price/royalty missing.

Yuhan:
approval is strong, but SC Rybrevant manufacturing CRL and economics missing → Stage2 + 4B.

Samsung Bioepis:
biosimilar opportunity exists, but Amgen lawsuit → 4C-watch.
```

---

# 11. Stage3-Yellow 조건

```text
Stage3-Yellow:
- Stage2-Actionable 이후 EPS/OP/FCF 경로 변화 가능성이 높아짐.
- 하지만 royalty, utilization, manufacturing, patent, launch timing 중 하나가 남은 상태.
```

Yellow 후보:

```text
Alteogen:
Qlex sales and adoption target are real. Royalty rate and direct KRX price confirmation needed.

Samsung Biologics:
policy support and U.S. capacity are real. CDMO backlog and utilization needed.

SK Bioscience:
IDT M&A reaction is strong. Utilization and vaccine/CDMO demand needed.

Celltrion:
U.S. factory localization is real. Tariff hedge and biosimilar margin needed.

Yuhan:
FDA approval is real. Royalty/milestone and SC formulation manufacturing resolution needed.
```

---

# 12. Stage3-Green 조건

```text
Stage3-Green:
- regulatory approval converts to revenue, royalty or milestone.
- partner launch and adoption are visible.
- CDMO facility utilization and margin are visible.
- FDA inspection/manufacturing observations are resolved.
- patent litigation is settled or launch timing is clear.
- tariff hedge translates into protected gross margin.
- full-window MFE/MAE is favorable.
```

이번 R7 Loop 16에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + royalty/utilization/patent/manufacturing gates not fully closed
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- approval headline appears before royalty/sales economics.
- CDMO facility is acquired before utilization and client transfer are known.
- M&A rally appears before post-deal backlog and ROIC.
- biosimilar filing appears before patent clearance.
- FDA CRL appears due manufacturing or inspection issue.
- tariff policy drives localization before actual margin protection.
```

적용:

```text
Alteogen:
approval positive, but royalty/patent risk → 4B watch.

Samsung Biologics:
GSK facility positive, but price muted and utilization gate → 4B.

Celltrion:
U.S. factory positive, but capex/ROIC gate → 4B.

Yuhan/J&J:
approval positive, but SC CRL manufacturing issue → 4B.

Samsung Bioepis:
biosimilar filing positive, but patent lawsuit → 4C-watch.

Jeisys:
M&A positive, but delisting/control premium → 4B.
```

---

# 14. 4C hard gate 조건

```text
R7 4C:
- FDA Complete Response Letter caused by efficacy/safety/data-integrity issue
- manufacturing inspection observations blocking approval
- patent lawsuit blocking biosimilar launch
- trial failure or endpoint miss
- product recall / safety event
- CDMO FDA warning letter / batch failure
- tariff shock not offset by U.S. facility
```

이번 R7 Loop 16 hard 4C 확정은 없다.

```text
hard_4c_not_confirmed = true
```

Strong 4C-watch:

```text
- Samsung Bioepis / Amgen patent lawsuit
- J&J SC Rybrevant CRL manufacturing inspection issue
- pharma tariff shock
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R7 production 설계 원칙:

```text
1. FDA approval과 partner sales를 분리한다.
2. technology platform과 royalty/milestone economics를 분리한다.
3. CDMO facility capacity와 utilization/backlog를 분리한다.
4. biosimilar filing과 patent clearance를 분리한다.
5. M&A/control premium과 operating rerating을 분리한다.
6. CRL은 efficacy/safety/data-integrity vs manufacturing-inspection issue를 구분한다.
7. tariff hedge는 actual margin protection 전까지 4B다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_243.md 요약

```md
# R7 Loop 16. Bio / Healthcare / Medical Device Trigger-level Price Validation

이번 라운드는 R7 Loop 16 trigger-level validation 라운드다.

핵심 결론:
- Alteogen / Merck Keytruda SC is the strongest Stage3-Yellow candidate. Merck’s SC Keytruda uses Alteogen’s enzyme; FDA approved Keytruda Qlex in Sep 2025; Merck expects 30~40% Keytruda patient adoption within two years; Qlex generated $128M in Q1 2026. Direct Alteogen KRX price and royalty economics remain unavailable.
- Samsung Biologics policy support is Stage2. Korean pharma sector rose 3.97%, Samsung Biologics +6.23%, Celltrion +0.35% after government biopharma support pledge. Backlog/utilization and tariff details are not yet closed.
- Samsung Biologics / GSK U.S. facility is evidence-good but price-muted. Samsung Biologics bought a $280M U.S. facility with 60,000L capacity, but shares fell 0.4% while the broader market rose 2%.
- SK Bioscience / IDT Biologika is Stage2-Actionable. SK Bioscience acquired a 60% stake in German CDMO IDT Biologika for 339B won / $243.75M, and shares rose 11.7% in morning trade.
- Celltrion U.S. factory localization is Stage2. Celltrion became preferred bidder for a U.S. factory, then acquired ImClone Systems from Eli Lilly for $330M and planned up to 700B won / $478M expansion. Price anchor and utilization are unavailable.
- Yuhan / lazertinib / J&J Rybrevant is Stage2 approval with manufacturing 4B. FDA approved Rybrevant + lazertinib in Aug 2024, but FDA later declined SC Rybrevant approval due manufacturing inspection observations.
- Samsung Bioepis / Amgen Prolia-Xgeva biosimilar litigation is 4C-watch. Amgen sued over 34 patents; Prolia and Xgeva U.S. sales exceeded $4.2B in the prior year.
- Jeisys / ArchiMed aesthetic medical-device buyout is Stage2 M&A, not operating Green. ArchiMed acquired Jeisys for about $742M; Jeisys shares closed at 12,860 won, and delisting/control premium must be separated from operating rerating.
- Pharma tariff shock is 4B/4C-watch. 100% branded-drug tariff threat makes U.S. localization valuable, but final tariff, certification and margin protection are unresolved.

Main calibration:
- Raise regulatory_approval_to_sales_bridge, royalty_milestone_visibility, CDMO_capacity_utilization, US_localization_tariff_hedge, M&A_price_reaction, partner_product_adoption, patent_litigation_resolution, manufacturing_inspection_cleanliness.
- Lower approval_without_economics, facility_acquisition_without_utilization, policy_support_without_backlog, biotech_MA_without_ROIC, biosimilar_filing_without_patent_clearance, control_premium_delisting_without_public_forward_return, tariff_headline_without_margin_protection.
```

## docs/checkpoints/checkpoint_28a_round243_r7_loop16.md 요약

```md
# Checkpoint 28A Round 243 R7 Loop 16 Trigger-level Calibration

## 반영 내용
- R7 Loop 16 trigger-level validation을 수행했다.
- Alteogen/Keytruda SC, Samsung Biologics policy support and GSK facility, SK Bioscience/IDT Biologika, Celltrion U.S. factory, Yuhan/lazertinib, Samsung Bioepis/Amgen litigation, Jeisys/ArchiMed buyout, pharma tariff shock를 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 Reuters / WSJ / FT / MarketWatch / Barron’s의 reported event return과 event price anchor를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- FDA approval은 partner sales and royalty/milestone economics 전에는 Green이 아니다.
- SC formulation platform은 approval, adoption, royalty, patent risk를 분리한다.
- CDMO facility acquisition은 utilization and signed backlog 전까지 Stage2다.
- U.S. localization은 tariff hedge지만 capex ROIC and certification gate가 필요하다.
- Biosimilar filing은 patent clearance 전에는 4C-watch다.
- Medical-device PE buyout은 control premium and delisting을 operating rerating과 분리한다.
```

## data/e2r_case_library/cases_r7_loop16_round243.jsonl 초안

```jsonl
{"case_id":"r7_loop16_alteogen_keytruda_sc","symbol":"196170","company_name":"Alteogen","case_type":"Stage3_Yellow_candidate","primary_archetype":"SC_FORMULATION_PLATFORM_STAGE3_YELLOW","best_trigger":"T2/T3","stage_candidate":"Stage3-Yellow_candidate","price_validation":{"t0_trial_date":"2024-11-19","t1_launch_plan_date":"2025-03-27","t2_fda_approval_date":"2025-09-19","t3_sales_validation_date":"2026-04-30","keytruda_2024_sales_usd_bn":30,"expected_sc_adoption_pct":"30-40","qlex_q1_2026_sales_usd_mn":128,"direct_alteogen_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage3_Yellow_candidate","notes":"Strong platform-to-product validation, but royalty rate and direct KRX price are missing."}
{"case_id":"r7_loop16_samsung_biologics_policy_support","symbol":"207940","company_name":"Samsung Biologics","case_type":"Stage2_policy_support","primary_archetype":"BIOPHARMA_TARIFF_POLICY_SUPPORT_STAGE2","best_trigger":"T0/T1","stage_candidate":"Stage2","price_validation":{"trigger_date":"2025-05-21","pharma_sector_event_return_pct":3.97,"samsung_biologics_event_return_pct":6.23,"celltrion_event_return_pct":0.35,"kospi_event_return_pct":0.99,"korea_pharma_exports_2024_usd_bn":9.59,"us_share_of_korea_pharma_exports_pct":16,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_policy_support_not_Green","notes":"Policy support moved the sector, but backlog/utilization and tariff details are not closed."}
{"case_id":"r7_loop16_samsung_biologics_gsk_us_facility","symbol":"207940","company_name":"Samsung Biologics","case_type":"evidence_good_but_price_muted","primary_archetype":"CDMO_US_FACILITY_EXPANSION_STAGE2_PRICE_MUTED","best_trigger":"T0/T1","stage_candidate":"Stage2","price_validation":{"trigger_date":"2025-12-22","acquisition_value_usd_mn":280,"facility_location":"Rockville_Maryland","facility_capacity_liters":60000,"event_return_pct":-0.4,"market_context_pct":2.0,"market_relative_return_pp":-2.4,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"evidence_good_but_price_muted","notes":"U.S. capacity is strategic, but price reaction was negative relative to market."}
{"case_id":"r7_loop16_sk_bioscience_idt_biologika","symbol":"302440","company_name":"SK Bioscience","case_type":"Stage2_Actionable_MA","primary_archetype":"VACCINE_CDMO_MA_STAGE2_ACTIONABLE","best_trigger":"T0/T1","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2024-06-27","stake_acquired_pct":60,"deal_value_krw_bn":339,"deal_value_usd_mn":243.75,"event_return_pct":11.7,"first_major_ma_since_ipo":true,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_MA","notes":"Clear M&A trigger and strong price reaction; utilization/backlog needed for Yellow."}
{"case_id":"r7_loop16_celltrion_us_factory_localization","symbol":"068270","company_name":"Celltrion","case_type":"Stage2_US_localization_with_capex_gate","primary_archetype":"BIOPHARMA_US_LOCALIZATION_STAGE2_WITH_CAPEX_GATE","best_trigger":"T0/T2","stage_candidate":"Stage2","price_validation":{"preferred_bidder_date":"2025-07-29","planned_initial_investment_krw_bn":700,"possible_additional_investment_krw_bn":"300-700","imclone_acquisition_date":"2025-09-23","imclone_acquisition_value_usd_mn":330,"expansion_investment_date":"2025-11-19","expansion_investment_krw_bn":700,"expansion_investment_usd_mn":478,"direct_celltrion_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_US_localization_not_Green","notes":"U.S. localization is a tariff hedge, but utilization, margin and ROIC are missing."}
{"case_id":"r7_loop16_yuhan_lazertinib_jnj_rybrevant","symbol":"000100","company_name":"Yuhan / Johnson & Johnson read-through","case_type":"Stage2_approval_with_manufacturing_4B","primary_archetype":"ONCOLOGY_APPROVAL_STAGE2_WITH_MANUFACTURING_4B","best_trigger":"T0/T2","stage_candidate":"Stage2 + 4B-watch","price_validation":{"approval_date":"2024-08-20","approved_combo":"Rybrevant_plus_lazertinib","indication":"first_line_EGFR_mutated_advanced_NSCLC","egfr_mutation_us_nsclc_pct":"10-15","rybrevant_peak_sales_expectation_usd_bn":">5","sc_crl_date":"2024-12-16","crl_reason":"manufacturing_facility_inspection_observations","direct_yuhan_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"approval_stage2_with_manufacturing_4B","notes":"Approval is strong but royalty economics and SC manufacturing resolution are gates."}
{"case_id":"r7_loop16_samsung_bioepis_amgen_litigation","symbol":"207940_readthrough","company_name":"Samsung Bioepis / Samsung Biologics read-through","case_type":"4C_watch_patent_litigation","primary_archetype":"BIOSIMILAR_PATENT_LITIGATION_4C_WATCH","best_trigger":"T1/T2","stage_candidate":"4C-watch","price_validation":{"trigger_date":"2024-08-13","originator":"Amgen","products":["Prolia","Xgeva"],"alleged_patents":34,"prolia_us_sales_prior_year_usd_bn":2.7,"xgeva_us_sales_prior_year_usd_bn":1.5,"direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","notes":"Biosimilar opportunity is blocked by patent/litigation launch-timing gate."}
{"case_id":"r7_loop16_jeisys_archimed_medical_device_buyout","symbol":"287410","company_name":"Jeisys Medical","case_type":"Stage2_medical_device_MA_with_control_premium_4B","primary_archetype":"AESTHETIC_MEDICAL_DEVICE_PE_BUYOUT_STAGE2","best_trigger":"T0/T2","stage_candidate":"Stage2_MA","price_validation":{"trigger_date":"2024-09-11","acquisition_value_usd_mn":742,"reported_share_close_krw":12860,"device_type":"energy_based_devices","full_ohlc_status":"not_applicable_after_buyout"},"score_price_alignment":"Stage2_MA_not_operating_Green","notes":"PE buyout/control premium is not equivalent to operating Stage3."}
{"case_id":"r7_loop16_pharma_tariff_localization","symbol":"207940/068270/302440/pharma_basket","company_name":"Samsung Biologics / Celltrion / SK Bioscience pharma basket","case_type":"4B_4C_policy_shock_with_Stage2_localization_hedge","primary_archetype":"PHARMA_TARIFF_4B_4C_WATCH","best_trigger":"T0/T2","stage_candidate":"4B/4C-watch + Stage2_hedge","price_validation":{"trigger_date":"2025-09-26","tariff_rate_context_pct":100,"tariff_scope":"branded_drug_imports_unless_US_manufacturing_started","direct_korea_basket_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"policy_4B_4C_watch","notes":"Tariff shock makes localization valuable but final tariff, certification and margin protection are unresolved."}
```

## data/e2r_trigger_calibration/triggers_r7_loop16_round243.jsonl 초안

```jsonl
{"trigger_id":"r7l16_alteogen_keytruda_T2","case_id":"r7_loop16_alteogen_keytruda_sc","trigger_type":"Stage3-Yellow_candidate","trigger_date":"2025-09-19/2026-04-30","evidence_available":"FDA approved Merck Keytruda Qlex; Merck expects 30-40% adoption within two years; Qlex generated $128M sales in Q1 2026; Alteogen enzyme used with Keytruda SC","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage3_Yellow_candidate_platform_to_product","promote_to":"Stage3-Yellow_candidate"}
{"trigger_id":"r7l16_samsungbio_policy_T0","case_id":"r7_loop16_samsung_biologics_policy_support","trigger_type":"Stage2_policy_support","trigger_date":"2025-05-21","evidence_available":"Korea pledges biopharma support; pharma sector +3.97%, Samsung Biologics +6.23%, Celltrion +0.35%, KOSPI +0.99%","event_return_pct":6.23,"trigger_outcome_label":"Stage2_policy_support_not_Green","promote_to":"Stage2"}
{"trigger_id":"r7l16_samsungbio_gsk_T0","case_id":"r7_loop16_samsung_biologics_gsk_us_facility","trigger_type":"Stage2_facility_price_muted","trigger_date":"2025-12-22","evidence_available":"Samsung Biologics buys first U.S. facility from GSK for $280M; 60,000L drug substance capacity; shares -0.4% vs market +2%","event_return_pct":-0.4,"trigger_outcome_label":"evidence_good_but_price_muted","promote_to":"Stage2"}
{"trigger_id":"r7l16_skbioscience_idt_T0","case_id":"r7_loop16_sk_bioscience_idt_biologika","trigger_type":"Stage2-Actionable_MA","trigger_date":"2024-06-27","evidence_available":"SK Bioscience acquires 60% of IDT Biologika for 339B won / $243.75M; first major M&A since IPO; shares +11.7% morning trade","event_return_pct":11.7,"trigger_outcome_label":"excellent_stage2_actionable_MA","promote_to":"Stage2-Actionable"}
{"trigger_id":"r7l16_celltrion_us_factory_T0","case_id":"r7_loop16_celltrion_us_factory_localization","trigger_type":"Stage2_US_localization","trigger_date":"2025-07-29/2025-11-19","evidence_available":"Celltrion selected as preferred bidder for U.S. facility, acquired ImClone from Eli Lilly for $330M, and planned up to 700B won / $478M U.S. factory expansion","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_US_localization_not_Green","promote_to":"Stage2"}
{"trigger_id":"r7l16_yuhan_lazertinib_T0","case_id":"r7_loop16_yuhan_lazertinib_jnj_rybrevant","trigger_type":"Stage2_approval_with_4B","trigger_date":"2024-08-20/2024-12-16","evidence_available":"FDA approved Rybrevant + lazertinib for first-line EGFR-mutated NSCLC; later FDA declined SC Rybrevant due manufacturing inspection observations","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"approval_stage2_with_manufacturing_4B","promote_to":"Stage2+4B"}
{"trigger_id":"r7l16_samsung_bioepis_amgen_T1","case_id":"r7_loop16_samsung_bioepis_amgen_litigation","trigger_type":"4C-watch_patent_litigation","trigger_date":"2024-08-13","evidence_available":"Amgen sues Samsung Bioepis over proposed Prolia/Xgeva biosimilars, alleging infringement of 34 patents; Prolia/Xgeva U.S. sales exceeded $4.2B prior year","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"biosimilar_patent_litigation_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r7l16_jeisys_archimed_T0","case_id":"r7_loop16_jeisys_archimed_medical_device_buyout","trigger_type":"Stage2_MA_control_premium","trigger_date":"2024-09-11","evidence_available":"ArchiMed acquires Jeisys Medical for about $742M; shares closed at 12,860 won; EBD aesthetic devices but delisting/control premium overlay","event_return_pct":"control_premium_not_forward_OHLC","trigger_outcome_label":"Stage2_MA_not_operating_Green","promote_to":"Stage2+4B"}
{"trigger_id":"r7l16_pharma_tariff_T0","case_id":"r7_loop16_pharma_tariff_localization","trigger_type":"4B_4C_policy_shock","trigger_date":"2025-09-26","evidence_available":"Trump announces 100% tariffs on branded drug imports unless companies have started U.S. manufacturing; Asian pharma stocks fall; Korean localization becomes hedge","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"pharma_tariff_4B_4C_with_localization_hedge","promote_to":"4B/4C-watch"}
```

## data/sector_taxonomy/score_weight_profiles_round243_r7_loop16_v1.csv 초안

```csv
archetype,regulatory_approval_to_sales_bridge,royalty_milestone_visibility,cdmo_capacity_utilization,us_localization_tariff_hedge,ma_price_reaction,partner_product_adoption,patent_litigation_resolution,manufacturing_inspection_cleanliness,approval_without_economics_penalty,facility_acquisition_without_utilization_penalty,policy_support_without_backlog_penalty,biotech_ma_without_roic_penalty,biosimilar_filing_without_patent_clearance_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
SC_FORMULATION_PLATFORM_STAGE3_YELLOW,+5,+5,+1,+0,+0,+5,+4,+3,-5,-1,-1,-1,-1,partner approval+sales validation,royalty/direct price missing,royalty+sales+OHLC,Alteogen/Keytruda Qlex.
BIOPHARMA_TARIFF_POLICY_SUPPORT_STAGE2,+1,+0,+3,+5,+2,+0,+1,+2,-2,-2,-4,-1,-1,policy support+sector rally,backlog/utilization missing,tariff hedge+backlog+margin,Samsung Biologics policy.
CDMO_US_FACILITY_EXPANSION_STAGE2_PRICE_MUTED,+1,+0,+5,+5,+0,+0,+1,+4,-2,-5,-1,-2,-1,U.S. facility/capacity,utilization and price support missing,client transfer+utilization+margin,Samsung Biologics GSK facility.
VACCINE_CDMO_MA_STAGE2_ACTIONABLE,+1,+0,+5,+2,+5,+1,+1,+3,-1,-3,-1,-4,-1,M&A+price reaction,utilization/backlog missing,post-deal utilization+margin,SK Bioscience IDT.
BIOPHARMA_US_LOCALIZATION_STAGE2_WITH_CAPEX_GATE,+1,+0,+4,+5,+1,+1,+1,+4,-1,-5,-1,-4,-1,U.S. localization,capex ROI/utilization missing,tariff shield+facility margin,Celltrion.
ONCOLOGY_APPROVAL_STAGE2_WITH_MANUFACTURING_4B,+5,+5,+0,+0,+1,+4,+1,+5,-5,-1,-1,-1,-1,FDA approval+partner launch,royalty/SC manufacturing missing,royalty+sales+manufacturing resolution,Yuhan/lazertinib.
BIOSIMILAR_PATENT_LITIGATION_4C_WATCH,+2,+2,+0,+0,+0,+0,+5,+2,-3,-1,-1,-1,-5,biosimilar opportunity,patent settlement missing,N/A,Samsung Bioepis/Amgen.
AESTHETIC_MEDICAL_DEVICE_PE_BUYOUT_STAGE2,+1,+0,+1,+0,+4,+1,+0,+1,-1,-1,-1,-3,-1,medical-device M&A,delisting/control premium,installed base+consumables if public,Jeisys/ArchiMed.
PHARMA_TARIFF_4B_4C_WATCH,+0,+0,+3,+5,+1,+0,+1,+4,-1,-4,-3,-2,-1,tariff shock/localization hedge,final tariff and margin protection missing,certified U.S. production+margin,pharma tariff basket.
```

---

# 이번 R7 Loop 16 결론

```text
1. Alteogen / Keytruda SC는 R7의 가장 좋은 Stage3-Yellow 후보다.
   FDA approval, adoption target, Qlex Q1 2026 sales까지 닫혔다. 다만 royalty와 direct KRX price anchor가 없다.

2. Samsung Biologics policy support는 Stage2다.
   sector와 stock reaction은 좋지만 backlog/utilization and tariff details가 필요하다.

3. Samsung Biologics GSK facility는 evidence good but price muted다.
   60,000L U.S. capacity는 좋지만, 발표일 주가는 market을 underperform했다.

4. SK Bioscience / IDT Biologika는 Stage2-Actionable이다.
   deal value와 +11.7% price reaction이 닫혔다. utilization/backlog가 Yellow gate다.

5. Celltrion U.S. factory localization은 Stage2다.
   U.S. tariff hedge는 맞지만 utilization, ROIC, margin이 필요하다.

6. Yuhan / lazertinib은 Stage2 approval + 4B다.
   FDA approval은 강하지만 SC Rybrevant manufacturing CRL이 launch convenience를 늦출 수 있다.

7. Samsung Bioepis / Amgen lawsuit는 biosimilar 4C-watch다.
   biosimilar filing만으로는 안 되고 patent clearance가 launch를 결정한다.

8. Jeisys / ArchiMed는 medical-device M&A Stage2다.
   control premium and delisting은 operating Stage3와 분리해야 한다.

9. Pharma tariff shock는 4B/4C-watch다.
   U.S. localization은 hedge지만 final tariff, plant certification, margin protection 전에는 Green이 아니다.
```

한 문장으로 압축하면:

> **R7 Loop 16에서 배운 핵심은 “FDA 승인·CDMO 공장·기술수출·M&A headline”이 아니라, partner sales, royalty/milestone economics, CDMO utilization, patent clearance, manufacturing inspection cleanliness, U.S. tariff hedge가 실제 margin으로 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 승인만, 공장 인수만, biosimilar filing만, PE buyout만으로는 4B/false positive가 되기 쉽다.**

[1]: https://www.reuters.com/business/healthcare-pharmaceuticals/merck-says-keytruda-injection-par-with-approved-iv-version-trial-2024-11-19/ "https://www.reuters.com/business/healthcare-pharmaceuticals/merck-says-keytruda-injection-par-with-approved-iv-version-trial-2024-11-19/"
[2]: https://www.reuters.com/business/healthcare-pharmaceuticals/south-korean-shares-rise-1-pharmaceutical-stocks-jump-2025-05-21/ "https://www.reuters.com/business/healthcare-pharmaceuticals/south-korean-shares-rise-1-pharmaceutical-stocks-jump-2025-05-21/"
[3]: https://www.reuters.com/business/healthcare-pharmaceuticals/samsung-biologics-buy-us-drug-production-facility-gsk-280-mln-2025-12-21/ "https://www.reuters.com/business/healthcare-pharmaceuticals/samsung-biologics-buy-us-drug-production-facility-gsk-280-mln-2025-12-21/"
[4]: https://www.reuters.com/markets/deals/south-koreas-sk-bioscience-buy-control-germanys-idt-biologika-244-mln-2024-06-27/ "https://www.reuters.com/markets/deals/south-koreas-sk-bioscience-buy-control-germanys-idt-biologika-244-mln-2024-06-27/"
[5]: https://www.reuters.com/business/healthcare-pharmaceuticals/south-koreas-celltrion-says-tapped-buy-us-pharma-factory-offset-tariff-risk-2025-07-29/ "https://www.reuters.com/business/healthcare-pharmaceuticals/south-koreas-celltrion-says-tapped-buy-us-pharma-factory-offset-tariff-risk-2025-07-29/"
[6]: https://www.reuters.com/business/healthcare-pharmaceuticals/us-fda-approves-jjs-combination-therapy-type-lung-cancer-2024-08-20/ "https://www.reuters.com/business/healthcare-pharmaceuticals/us-fda-approves-jjs-combination-therapy-type-lung-cancer-2024-08-20/"
[7]: https://www.reuters.com/legal/litigation/amgen-sues-samsung-biotech-unit-over-bone-drug-copies-2024-08-13/ "https://www.reuters.com/legal/litigation/amgen-sues-samsung-biotech-unit-over-bone-drug-copies-2024-08-13/"
[8]: https://www.wsj.com/articles/europes-archimed-bets-on-anti-aging-trend-in-first-asia-deal-cbe16f5e "https://www.wsj.com/articles/europes-archimed-bets-on-anti-aging-trend-in-first-asia-deal-cbe16f5e"
[9]: https://www.reuters.com/business/healthcare-pharmaceuticals/shares-asian-drugmakers-drop-after-trump-threatens-tariffs-2025-09-26/ "https://www.reuters.com/business/healthcare-pharmaceuticals/shares-asian-drugmakers-drop-after-trump-threatens-tariffs-2025-09-26/"
