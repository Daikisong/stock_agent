순서상 이번은 **R7 Loop 11 — 바이오·헬스케어·의료기기 가격경로 검증 라운드**다.

이번 R7 Loop 11은 지난 R7의 미용기기·CDMO 일부 반복을 줄이고, **플랫폼 기술 royalty, 국산 신약 FDA 승인, CDMO 미국 현지화, vaccine/CMO M&A, 파트너 임상 실패, 의료AI 외부검증, 정책수혜 과열**을 같이 본다.

```text
round = R7 Loop 11
round_id = round_178
large_sector = BIOTECH_HEALTHCARE_DEVICE
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = false
```

이번에도 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉 OHLC 전체 구간은 안정적으로 확보하지 못했다. 대신 Reuters / WSJ / arXiv가 제공한 **가격 anchor, 이벤트 수익률, 계약금액, 임상·허가·시설·정책 지표**로 계산 가능한 값만 계산했다. 30D/90D/180D full OHLC가 없는 항목은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R7 = 바이오·헬스케어·의료기기
```

R7의 Stage 3는 “FDA 승인”, “임상 성공”, “대형 파트너”, “CDMO 공장”, “AI 성능”이 아니다. **처방·시술·병원 도입·수가·상업매출·로열티·가동률·마진·FCF가 실제로 들어오는 순간**이다.

---

# 2. 대상 canonical archetype

```text
BIO_PLATFORM_ROYALTY_CONVERSION
KOREAN_NEW_DRUG_GLOBAL_APPROVAL
CDMO_US_TARIFF_HEDGE_CAPACITY
CMO_M_AND_A_TRANSITION
BIOPHARMA_POLICY_TARIFF_RELIEF
AUTOIMMUNE_PARTNER_TRIAL_FAILURE
MEDICAL_AI_EXTERNAL_VALIDATION
APPROVAL_OR_VALIDATION_ONLY_NOT_GREEN
EVENT_PREMIUM
EVIDENCE_GOOD_BUT_PRICE_FAILED
```

---

# 3. deep sub-archetype

```text
플랫폼 기술 / royalty:
- Alteogen / hyaluronidase enzyme
- Merck Keytruda SC
- 30~40% adoption target
- Keytruda $30B product base
- Halozyme patent challenge
- royalty / supply / patent durability before Green

국산 신약 글로벌 승인:
- Yuhan / Lazcluze / lazertinib
- J&J Rybrevant + Lazcluze approval
- EGFR-mutated NSCLC
- approval vs actual royalty / milestone / launch revenue

CDMO / CMO:
- Samsung Biologics GSK U.S. facility
- Celltrion ImClone acquisition / U.S. tariff hedge
- SK Bioscience IDT Biologika acquisition
- policy support vs utilization / backlog / margin / FCF

파트너 임상 리스크:
- HanAll / Immunovant batoclimab
- thyroid eye disease late-stage trial failure
- partner-program 4C-watch

의료AI:
- Lunit INSIGHT DBT
- AUC 0.91 external validation
- subgroup weakness
- reimbursement / hospital adoption / recurring revenue before Green

정책 이벤트:
- pharmaceutical sector support against U.S. tariffs
- pharma sub-index +3.97%
- Samsung Biologics +6.23%
- policy relief, not Green
```

---

# 4. 국장 신규 후보 case

## Case A — Alteogen `success_candidate + patent/royalty 4B-watch`

```text
symbol = 196170
case_type = success_candidate + 4B-watch
archetype = BIO_PLATFORM_ROYALTY_CONVERSION
```

### stage date

```text
Stage 1:
2024-11-19
- Merck Keytruda subcutaneous version non-inferior in late-stage trial
- Alteogen enzyme used in formulation
- administration time reduced from about 30 minutes to 2~3 minutes

Stage 2:
2025-03-27
- Merck plans U.S. launch of Keytruda SC on Oct 1 after FDA decision target Sept 23
- expected peak adoption 30~40% of Keytruda patients within two years
- Keytruda 2024 sales nearly $30B
- Alteogen develops/manufactures enzyme used with Keytruda SC

Stage 3:
보류
- FDA approval / launch / royalty recognition / supply revenue / patent durability 확인 전 Green 금지

Stage 4B:
Keytruda SC / Merck partner / $30B product-base narrative로 주가가 먼저 valuation화되면 후보

Stage 4C-watch:
Halozyme patent challenge / litigation risk
```

Alteogen은 이번 R7 Loop 11에서 가장 중요한 “플랫폼 기술이 royalty로 전환될 수 있는가” case다. Merck는 Keytruda SC가 기존 IV 제형 대비 비열등성을 보였다고 발표했고, SC 투여 시간은 기존 약 30분 infusion에서 약 2~3분 injection으로 줄어든다. 이후 Merck는 FDA 결정 목표일을 2025년 9월 23일로 보고, 승인 후 2025년 10월 1일 미국 출시를 계획한다고 밝혔다. Keytruda는 2024년 매출이 거의 300억 달러였고, Merck는 SC 제형이 2년 안에 Keytruda 환자의 30~40%까지 채택될 수 있다고 봤다. 다만 WSJ는 Halozyme patent dispute 가능성을 제기했으므로, Alteogen은 Stage 2가 강하지만 Green은 royalty/supply revenue와 patent durability 확인 뒤다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / WSJ clinical-launch-patent anchors

stage3_price:
N/A

Alteogen_stock_OHLC:
price_data_unavailable_after_deep_search

Keytruda_2024_sales:
nearly $30B

expected_SC_adoption:
30~40% of Keytruda patients within two years

administration_time:
2~3 minutes vs about 30 minutes IV infusion

FDA_decision_target:
2025-09-23

planned_US_launch:
2025-10-01

patent_risk:
Halozyme patent challenge possible

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = platform_royalty_conversion_watch
stage_failure_type = stage2_strong_but_not_green_until_royalty_and_patent_confirm
```

---

## Case B — Yuhan / Oscotec / Lazertinib `success_candidate + launch-revenue gate`

```text
symbols = 000100 / 039200 exposure
case_type = success_candidate
archetype = KOREAN_NEW_DRUG_GLOBAL_APPROVAL
```

### stage date

```text
Stage 1:
2024-08
- J&J Rybrevant + Lazcluze FDA approval
- EGFR-mutated NSCLC first-line chemotherapy-free therapy
- Yuhan-origin lazertinib global validation

Stage 2:
2024-08-20
- FDA approves J&J combination therapy using Rybrevant + lazertinib
- J&J expects more than $5B peak sales from Rybrevant
- approval based on late-stage study showing longer progression-free survival

Stage 3:
보류
- royalty / milestone / Yuhan revenue recognition / prescription uptake 확인 전 Green 금지

Stage 4B:
approval headline로 price가 royalty evidence보다 먼저 움직이면 후보

Stage 4C-watch:
2024-12-16
- FDA declines to approve SC version of Rybrevant due to manufacturing inspection observations
- efficacy/safety data not affected
```

Yuhan/Oscotec Lazertinib은 한국 신약의 글로벌 승인 Stage 2다. FDA는 J&J의 Rybrevant와 Lazcluze, 즉 lazertinib 병용요법을 EGFR-mutated NSCLC 1차 치료로 승인했고, J&J는 Rybrevant peak sales를 50억 달러 이상으로 기대한다고 밝혔다. 그러나 Yuhan 주주 관점의 Stage 3는 approval headline이 아니라 실제 royalty, milestone, prescription uptake, revenue recognition이다. 이후 FDA가 Rybrevant SC 제형 승인을 제조시설 inspection 문제로 거절한 건 formulation·efficacy·safety 문제는 아니지만, launch-timing 4C-watch로 둔다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters approval / CRL anchors

stage3_price:
N/A

Yuhan_stock_OHLC:
price_data_unavailable_after_deep_search

Oscotec_stock_OHLC:
price_data_unavailable_after_deep_search

approval:
Rybrevant + lazertinib for first-line EGFR-mutated NSCLC

J&J_peak_sales_expectation_for_Rybrevant:
> $5B

SC_Rybrevant_CRL:
manufacturing inspection observations

CRL_not_related_to:
formulation / efficacy / safety data

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = Korean_new_drug_global_approval_watch
stage_failure_type = approval_not_green_until_royalty_revenue_confirm
```

---

## Case C — Samsung Biologics `evidence_good_but_price_failed + U.S. CDMO capacity`

```text
symbol = 207940
case_type = evidence_good_but_price_failed
archetype = CDMO_US_TARIFF_HEDGE_CAPACITY
```

### stage date

```text
Stage 1:
2025
- U.S. tariff hedge
- global CDMO capacity expansion
- U.S. client proximity

Stage 2:
2025-05-21
- pharmaceutical sector +3.97% on policy support
- Samsung Biologics +6.23%

Stage 2 추가:
2025-12-22
- Samsung Biologics buys GSK Rockville facility
- $280M acquisition
- 60,000L drug substance capacity
- first U.S. drug production facility

Stage 3:
없음
- policy support / facility acquisition만으로 Green 금지
- contract transfer, utilization, margin, FCF 확인 필요

Stage 4B:
정책지원·미국 현지화 headline이 먼저 가격화되면 후보

Stage 4C-watch:
good news에도 price reaction이 약하거나 underperform하면 valuation saturation 후보
```

Samsung Biologics는 R7에서 좋은 CDMO 구조를 갖지만, 이번 라운드에서는 `evidence_good_but_price_failed`로 본다. 2025년 5월 한국 정부의 바이오·제약 지원 기대에 pharmaceutical sector는 3.97%, Samsung Biologics는 6.23% 상승했다. 그러나 2025년 12월 GSK의 Rockville facility를 2.8억 달러에 인수한다고 발표했을 때, 시설은 60,000L drug substance capacity를 갖는 첫 미국 생산시설이었음에도 주가는 0.4% 하락했고 KOSPI는 2% 상승했다. 즉 policy와 capacity evidence는 좋지만, Stage 3는 utilization·contract transfer·margin·FCF 확인 뒤다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters policy / facility-acquisition / event-return anchors

stage3_price:
N/A

pharmaceutical_sector_event_MFE:
+3.97%

Samsung_Biologics_policy_event_MFE:
+6.23%

GSK_facility_deal_value:
$280M

facility_capacity:
60,000L drug substance capacity

GSK_facility_event_MAE:
-0.4%

KOSPI_same_day_return:
+2.0%

relative_underperformance:
-0.4 - 2.0
= -2.4pp

MFE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed
rerating_result = CDMO_US_capacity_watch
stage_failure_type = stage2_good_evidence_but_price_failed
```

---

## Case D — Celltrion `success_candidate + U.S. tariff-hedge manufacturing`

```text
symbol = 068270
case_type = success_candidate
archetype = CDMO_US_TARIFF_HEDGE_CAPACITY
```

### stage date

```text
Stage 1:
2025
- U.S. pharmaceutical tariff risk
- biosimilar U.S. localization need
- tariff hedge / supply-chain resilience

Stage 2:
2025-07-29
- Celltrion preferred bidder for U.S. manufacturing facility
- planned investment 700B won
- possible additional 300B~700B won depending on U.S. tariff policy

Stage 2 강화:
2025-09-23
- Celltrion U.S. subsidiary acquires ImClone Systems from Eli Lilly
- acquisition value $330M
- U.S. manufacturing base secured

Stage 2 추가:
2025-11-19
- up to 700B won / $478M expansion at U.S. factory

Stage 3:
없음
- facility acquisition / expansion만으로 Green 금지
- product transfer, FDA/quality readiness, utilization, gross margin, FCF 확인 필요
```

Celltrion은 U.S. tariff hedge와 biosimilar localization의 좋은 Stage 2다. 2025년 7월 Celltrion은 미국 제조공장 인수 우선협상대상자가 됐고, 7,000억 원 투자와 추가 3,000억~7,000억 원 투자를 검토한다고 밝혔다. 이후 9월에는 Eli Lilly로부터 ImClone Systems를 3.3억 달러에 인수했고, 11월에는 미국 공장에 최대 7,000억 원을 추가 투자해 capacity를 확대한다고 밝혔다. 그러나 이건 아직 시설과 capex의 Stage 2다. Stage 3는 제품 이전, 품질·규제 readiness, 가동률, gross margin, FCF가 확인될 때다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters acquisition / expansion anchors

stage3_price:
N/A

preferred_bidder_investment_plan:
700B won

possible_additional_investment:
300B~700B won

ImClone_acquisition_value:
$330M

expansion_investment:
up to 700B won / $478.17M

USD_330M_KRW_equivalent_at_1463.9:
330M * 1,463.9
= 약 483.1B won

combined_acquisition_plus_expansion:
483.1B + 700B
= 약 1.183T won

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = U.S._tariff_hedge_manufacturing_watch
stage_failure_type = stage2_watch_success_not_green
```

---

## Case E — SK Bioscience `success_candidate + CMO M&A event premium`

```text
symbol = 302440
case_type = success_candidate + event_premium
archetype = CMO_M_AND_A_TRANSITION
```

### stage date

```text
Stage 1:
2024
- vaccine/CDMO transition
- post-COVID business repositioning
- SK Group portfolio optimization

Stage 2:
2024-06-27
- SK Bioscience acquires 60% of IDT Biologika
- deal value 339B won / $243.75M
- first major M&A since 2021 IPO
- 2021 IPO proceeds $1.33B
- shares +11.7% in morning trade

Stage 3:
없음
- M&A announcement만으로 Green 금지
- contract backlog, utilization, integration cost, margin, FCF 확인 필요

Stage 4B:
2024-06-27
- +11.7% announcement rally
- utilization/backlog 전 event premium
```

SK Bioscience는 vaccine business에서 CMO/CDMO 전환을 시도하는 Stage 2다. 회사는 독일 IDT Biologika 지분 60%를 3,390억 원에 인수했고, Reuters는 이 거래가 2021년 IPO 이후 첫 대형 M&A이며 발표 후 주가가 오전장 11.7% 상승했다고 보도했다. 하지만 M&A는 실적이 아니라 그릇이다. Stage 3는 인수한 시설이 실제 backlog, utilization, margin, FCF로 바뀌는지다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters acquisition / event-return anchor

stage3_price:
N/A

deal_value:
339B won / $243.75M

stake_acquired:
60%

implied_IDT_equity_value:
339B / 0.60
= 565B won

remaining_Klocke_stake:
40%

SK_Bioscience_2021_IPO_proceeds:
$1.33B

deal_value_vs_IPO_proceeds:
243.75M / 1.33B
= 18.3%

event_MFE_morning:
+11.7%

MFE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_event_premium
rerating_result = vaccine_CMO_transition_watch
stage_failure_type = M&A_stage2_not_green
```

---

## Case F — HanAll Biopharma / Immunovant `4C-watch / partner trial failure`

```text
symbol = 009420
case_type = 4C-watch
archetype = AUTOIMMUNE_PARTNER_TRIAL_FAILURE
```

### stage date

```text
Stage 1:
2024~2025
- FcRn autoimmune pipeline
- Immunovant / Roivant partner value
- batoclimab / IMVT-1402 expectation

Stage 2:
보류
- partner pipeline value는 Stage 2 후보이나, indication별 data 필요

Stage 3:
없음
- partner pipeline expectation만으로 Green 금지

Stage 4C-watch:
2026-04-02
- Immunovant batoclimab fails two late-stage thyroid eye disease trials
- primary endpoint not met
- Immunovant shares -4.8% to $23.89
- Roivant says results do not support further TED development
- future batoclimab plans to be reviewed with HanAll Biopharma
```

HanAll Biopharma는 partner-program risk를 봐야 한다. Immunovant의 batoclimab은 thyroid eye disease late-stage trial 2건에서 24주 후 2mm 이상 안구돌출 감소라는 primary endpoint를 달성하지 못했다. Immunovant 주가는 4.8% 하락해 23.89달러였고, Roivant CEO는 thyroid eye disease에서 추가 개발을 뒷받침하지 않는 결과라고 밝혔다. Immunovant는 HanAll과 향후 batoclimab 개발 계획을 검토하겠다고 했다. 한국 상장사 OHLC는 확보하지 못했지만, 이건 강한 partner-program 4C-watch다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters partner trial-failure anchor

stage3_price:
N/A

HanAll_stock_OHLC:
price_data_unavailable_after_deep_search

partner:
Immunovant / Roivant

trial:
two late-stage thyroid eye disease trials

primary_endpoint:
at least 2mm reduction in eye bulging after 24 weeks

result:
failed to meet primary goal

Immunovant_event_MAE:
-4.8%

Immunovant_event_price:
$23.89

future_plan:
review future batoclimab development with HanAll Biopharma

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = partner_trial_failure_watch
stage_failure_type = 4C_watch_not_hard_4C
```

---

## Case G — Lunit `insufficient_evidence / medical AI external validation`

```text
symbol = 328130
case_type = insufficient_evidence
archetype = MEDICAL_AI_EXTERNAL_VALIDATION
```

### stage date

```text
Stage 1:
2023~2025
- medical AI / cancer screening AI narrative
- breast imaging AI adoption expectation

Stage 2:
2025-03-17
- Lunit INSIGHT DBT external validation
- 163,449 screening mammography exams
- 1,368 screen-detected cancers
- overall AUC 0.91
- subgroup weakness identified

Stage 3:
없음
- 외부검증만으로 Green 금지
- reimbursement, hospital adoption, recurring revenue, gross margin, cash runway 확인 필요

Stage 4B:
의료AI 논문/검증 뉴스로 주가가 먼저 급등하면 후보

Stage 4C:
subgroup performance issue, reimbursement failure, adoption failure, cash burn/dilution
```

Lunit은 “성능은 좋지만 아직 Green은 아니다”를 보여주는 의료AI case다. arXiv 연구는 Lunit INSIGHT DBT를 163,449건의 screening mammography exam에서 평가했고, 전체 AUC 0.91을 기록했다. 그러나 non-invasive cancer, calcification, dense breast tissue subgroup에서는 성능이 낮아졌고, 연구진은 실제 임상 도입에서 subgroup별 평가와 주의가 필요하다고 결론냈다. 따라서 Stage 2 evidence는 맞지만, Stage 3는 수가·병원 도입·반복매출·gross margin·cash runway가 확인되어야 한다. ([arXiv][7])

### 실제 가격경로 검증

```text
price_data_source:
arXiv external validation evidence

stage3_price:
N/A

Lunit_stock_OHLC:
price_data_unavailable_after_deep_search

exam_count:
163,449

positive_cases:
1,368 screen-detected cancers

negative_exams:
162,081

overall_AUC:
0.91

precision:
0.08

recall:
0.73

non_invasive_cancer_AUC:
0.85

calcification_AUC:
0.80

dense_breast_AUC:
0.90

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = unknown_insufficient_evidence
rerating_result = medical_AI_validation_watch
stage_failure_type = validation_not_revenue
```

---

## Case H — Biopharma tariff-policy basket `event_premium / policy relief`

```text
symbols = 207940 / 068270 / biopharma basket
case_type = event_premium / policy_relief
archetype = BIOPHARMA_POLICY_TARIFF_RELIEF
```

### stage date

```text
Stage 1:
2025-05-20~21
- U.S. tariff pressure on pharmaceuticals
- Korea government vows support for biopharma and auto sectors
- reshoring / export-market support policy

Stage 2:
2025-05-21
- pharmaceutical sector +3.97%
- Samsung Biologics +6.23%
- Celltrion +0.35%
- foreign net buy 113.7B won
- won strengthens 0.56%

Stage 3:
없음
- policy support만으로 Green 금지
- company-level order, tariff pass-through, margin, U.S. localization, FCF 확인 필요

Stage 4B:
정책지원 기대만으로 biotech/pharma basket이 먼저 급등하면 후보

Stage 4C:
tariff details worsen, U.S. plant cost burden, FDA inspection issue, policy support not enough
```

Biopharma tariff-policy basket은 R7에서 “좋은 정책 relief지만 Green이 아닌” case다. 한국 정부는 미국 관세 압력에 대응해 biopharmaceuticals와 autos에 추가 지원책을 준비하겠다고 했고, 당일 pharmaceutical sector는 3.97%, Samsung Biologics는 6.23%, Celltrion은 0.35% 상승했다. 그러나 정책지원은 Stage 2 relief다. 실제 Green은 회사별 수주·마진·U.S. localization·tariff pass-through·FCF로 확인해야 한다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters policy / sector-return anchor

stage3_price:
N/A

pharmaceutical_sector_event_MFE:
+3.97%

Samsung_Biologics_event_MFE:
+6.23%

Celltrion_event_MFE:
+0.35%

KOSPI_same_context:
+0.99%

foreign_net_buy:
113.7B won / $82.05M

won_strengthening:
+0.56%

policy_package_context:
additional support for biopharma / auto sectors against U.S. tariffs

MFE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium_policy_relief
rerating_result = biopharma_tariff_policy_watch
stage_failure_type = policy_relief_not_green
```

---

# 5. 이번 R7 case별 요약표

| case                    | 분류                             |                                               실제 가격검증 | alignment                |
| ----------------------- | ------------------------------ | ----------------------------------------------------: | ------------------------ |
| Alteogen / Keytruda SC  | success_candidate + 4B-watch   |        Keytruda $30B, SC adoption 30~40%, patent risk | platform royalty Stage 2 |
| Yuhan / Lazertinib      | success_candidate              |       J&J approval, Rybrevant peak >$5B, SC CRL watch | approval Stage 2         |
| Samsung Biologics       | evidence_good_but_price_failed | policy +6.23%, GSK facility $280M, -0.4% vs KOSPI +2% | price failed             |
| Celltrion               | success_candidate              |              ImClone $330M + expansion up to 700B won | tariff hedge Stage 2     |
| SK Bioscience           | success_candidate + event      |                          IDT 60% for 339B won, +11.7% | M&A Stage 2              |
| HanAll / Immunovant     | 4C-watch                       |              batoclimab TED failure, Immunovant -4.8% | partner trial risk       |
| Lunit                   | insufficient_evidence          |            163,449 exams, AUC 0.91, subgroup weakness | validation not revenue   |
| Biopharma policy basket | event premium                  |    sector +3.97%, SamsungBio +6.23%, Celltrion +0.35% | policy relief            |

---

# 6. score-price alignment 판정

```text
success_candidate:
- Alteogen
- Yuhan / lazertinib
- Celltrion
- SK Bioscience

event_premium:
- SK Bioscience IDT M&A +11.7%
- biopharma tariff-policy basket
- Alteogen / Keytruda SC narrative if price outruns royalty recognition

evidence_good_but_price_failed:
- Samsung Biologics GSK U.S. facility

thesis_break_watch:
- HanAll / Immunovant batoclimab failure
- Yuhan/J&J Rybrevant SC manufacturing CRL watch
- Lunit subgroup-performance / reimbursement failure risk

unknown_insufficient_evidence:
- Lunit
- Alteogen stock OHLC / royalty revenue
- Yuhan stock OHLC / royalty revenue

4B-watch:
- platform royalty expectation before revenue
- FDA approval before prescription/royalty
- M&A announcement before utilization
- policy rally before company-level earnings bridge

hard_4C_confirmed:
- false
```

---

# 7. 점수비중 교정

## 올릴 축

```text
commercial_revenue +5
royalty_revenue_visibility +5
prescription_volume +5
reimbursement_access +5
hospital_adoption +4
capacity_utilization +5
contract_backlog +4
gross_margin_visibility +4
cash_runway +4
partner_execution_quality +5
```

### 왜 올리나

Alteogen, Yuhan, Celltrion, SK Bioscience 모두 Stage 2 증거는 강하다. 하지만 R7에서 Stage 3는 **approval headline이 아니라 royalty·prescription·utilization·gross margin·FCF**가 들어올 때다. Samsung Biologics는 좋은 U.S. facility evidence에도 주가가 KOSPI를 언더퍼폼했으므로, “좋은 뉴스”와 “fresh rerating”을 분리해야 한다.

## 내릴 축

```text
approval_news_only -5
clinical_headline_only -5
external_validation_without_revenue -5
M&A_without_utilization -5
policy_support_without_order -4
facility_acquisition_without_backlog -4
partner_program_without_indication_success -5
patent_litigation_risk -4
cash_burn_or_dilution_risk -5
subgroup_performance_risk -3
```

### 왜 내리나

Lunit은 AUC가 높아도 수가와 병원 도입 전에는 매출이 아니다. HanAll은 partner program 실패가 곧 4C-watch다. Alteogen은 Keytruda SC 구조가 좋아도 patent challenge와 royalty recognition을 봐야 한다. SK Bioscience와 Celltrion은 시설·M&A가 utilization 전에는 Stage 2다.

## Green gate 강화 조건

```text
R7 Stage 3-Green 필수:
1. approval / clearance / launch 중 최소 하나 확인
2. commercial launch 이후 매출 확인
3. prescription volume / procedure volume / hospital adoption 확인
4. reimbursement / payer / ASP 확인
5. royalty / milestone / supply revenue 확인
6. gross margin 또는 royalty margin 확인
7. capacity utilization / backlog 확인
8. cash runway / dilution risk 통과
9. partner execution risk 통과
10. price path가 evidence 이후 따라옴

금지:
FDA approval만 있음
임상 headline만 있음
논문 성능만 있음
정책지원만 있음
M&A 발표만 있음
미국 공장 인수만 있음
파트너 pipeline 기대만 있음
royalty 확인 전 platform story
```

## 4B 조기감지 조건

```text
4B-watch:
FDA 승인 직후 주가 급등
Keytruda / Merck / J&J 같은 대형 파트너명으로 valuation 급등
royalty 인식 전 platform stock rerating
M&A 발표 당일 급등
policy-support day sector rally
의료AI 외부검증으로 주가만 급등
CDMO capacity premium이 가동률보다 먼저 확장

4B-elevated:
launch가 시작됐지만 처방·시술 증가가 느림
보험/수가 접근 제한
CDMO capex가 계약보다 빠름
partner patent/litigation risk
cash burn 지속
```

## 4C hard gate 조건

```text
FDA CRL / 허가 거절
효능·안전성 임상 실패
partner trial failure
commercial launch failure
royalty non-recognition
prescription volume failure
reimbursement failure
manufacturing inspection failure
product safety issue
subgroup clinical performance failure
capacity utilization failure
large dilution / cash runway break
```

이번 R7 Loop 11에서는 hard 4C를 확정하지 않는다. 다만 **HanAll/Immunovant trial failure**, **Yuhan/J&J SC Rybrevant CRL**, **Lunit subgroup weakness**, **Alteogen patent challenge**는 모두 강한 4C-watch다.

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

---

# 9. patch-ready 출력

## docs/round/round_178.md 요약

```md
# R7 Loop 11. Biotech / Healthcare / Medical Device Price Validation

이번 라운드는 R7 Loop 11 price-validation 라운드다.

핵심 결론:
- Alteogen is platform-royalty Stage 2. Merck plans Keytruda SC launch after FDA decision target Sept 23, with U.S. launch planned Oct 1, expected 30~40% adoption, and Keytruda 2024 sales nearly $30B. Patent challenge risk remains.
- Yuhan / lazertinib is global new-drug approval Stage 2. J&J Rybrevant + Lazcluze FDA approval validates the drug, but Yuhan royalty/revenue recognition and prescription uptake are required. Rybrevant SC CRL is manufacturing-inspection watch.
- Samsung Biologics is evidence_good_but_price_failed. Policy-support day +6.23%, but GSK U.S. facility acquisition $280M caused -0.4% vs KOSPI +2%, so utilization and contract transfer are needed.
- Celltrion is U.S. tariff-hedge manufacturing Stage 2. ImClone acquisition $330M plus expansion up to 700B won, but product transfer, utilization, margin and FCF are required.
- SK Bioscience is CMO M&A Stage 2. IDT Biologika 60% acquisition for 339B won, shares +11.7%, but backlog/utilization/margin/FCF are required.
- HanAll / Immunovant is partner trial 4C-watch. Batoclimab failed two late-stage thyroid eye disease trials; Immunovant -4.8%.
- Lunit is medical AI validation Stage 2 but insufficient evidence. 163,449 exams, AUC 0.91, but subgroup weakness and reimbursement/adoption risk block Green.
- Biopharma tariff-policy basket is event premium. Pharmaceutical sector +3.97%, SamsungBio +6.23%, Celltrion +0.35%, but policy relief is not company-level Green.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 178 R7 Loop 11 Biotech Healthcare Device Price Validation

## 반영 내용
- R7 Loop 11 price-validation 라운드를 추가했다.
- Platform royalty conversion, Korean new-drug global approval, CDMO U.S. tariff hedge, CMO M&A transition, biopharma policy relief, partner trial failure, medical AI external validation을 비교했다.
- Reuters/WSJ/arXiv anchors로 가능한 MFE/MAE 및 clinical/commercial/transaction metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- commercial revenue, royalty visibility, prescription volume, reimbursement, hospital adoption, utilization, gross margin, partner execution quality 가중치 강화
- approval-only, clinical headline-only, external validation without revenue, M&A without utilization, policy support without order, facility without backlog, patent litigation risk 감점 강화
- R7 4B-watch와 partner/manufacturing/reimbursement 4C-watch 민감도 강화
```

## case row 초안

```jsonl
{"case_id":"r7_loop11_alteogen_keytruda_sc_platform_royalty","symbol":"196170","company_name":"Alteogen","case_type":"success_candidate","primary_archetype":"BIO_PLATFORM_ROYALTY_CONVERSION","stage1_date":"2024-11-19","stage2_date":"2025-03-27","stage4c_date":"2025_patent_watch","price_validation":{"price_data_source":"Reuters/WSJ clinical-launch-patent anchors","stage3_price":null,"keytruda_2024_sales_usd_bn":30,"expected_sc_adoption_pct":"30-40","administration_time":"2-3_minutes_vs_about_30_minutes_IV","fda_decision_target":"2025-09-23","planned_us_launch":"2025-10-01","patent_risk":"Halozyme challenge possible","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"platform_royalty_conversion_watch","notes":"Strong Stage 2 platform story; royalty/supply revenue and patent durability required before Green."}
{"case_id":"r7_loop11_yuhan_lazertinib_global_approval","symbol":"000100/039200","company_name":"Yuhan / Oscotec / Lazertinib","case_type":"success_candidate","primary_archetype":"KOREAN_NEW_DRUG_GLOBAL_APPROVAL","stage2_date":"2024-08-20","stage4c_date":"2024-12-16_watch","price_validation":{"price_data_source":"Reuters approval/CRL anchors","stage3_price":null,"approval":"Rybrevant + lazertinib for first-line EGFR-mutated NSCLC","jj_peak_sales_expectation_for_rybrevant_usd_bn":5,"sc_rybrevant_crl_reason":"manufacturing inspection observations","crl_not_related_to":["formulation","efficacy","safety data"],"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"Korean_new_drug_global_approval_watch","notes":"FDA approval is Stage 2; royalty, milestone, prescription uptake and revenue recognition required before Green."}
{"case_id":"r7_loop11_samsung_biologics_gsk_facility_price_failed","symbol":"207940","company_name":"Samsung Biologics","case_type":"evidence_good_but_price_failed","primary_archetype":"CDMO_US_TARIFF_HEDGE_CAPACITY","stage2_date":"2025-05-21/2025-12-22","price_validation":{"price_data_source":"Reuters policy/facility/event-return anchors","stage3_price":null,"pharmaceutical_sector_event_mfe_pct":3.97,"samsung_biologics_policy_event_mfe_pct":6.23,"gsk_facility_deal_value_usd_mn":280,"facility_capacity_liters":60000,"gsk_facility_event_mae_pct":-0.4,"kospi_same_day_return_pct":2.0,"relative_underperformance_pp":-2.4,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"CDMO_US_capacity_watch","notes":"Good U.S. CDMO facility evidence but weak price reaction; utilization/contract transfer/margin required."}
{"case_id":"r7_loop11_celltrion_us_tariff_hedge_factory","symbol":"068270","company_name":"Celltrion","case_type":"success_candidate","primary_archetype":"CDMO_US_TARIFF_HEDGE_CAPACITY","stage2_date":"2025-07-29/2025-09-23/2025-11-19","price_validation":{"price_data_source":"Reuters acquisition/expansion anchors","stage3_price":null,"preferred_bidder_investment_plan_krw_bn":700,"possible_additional_investment_krw_bn":"300-700","imclone_acquisition_value_usd_mn":330,"expansion_investment_krw_bn":700,"expansion_investment_usd_mn":478.17,"imclone_acquisition_krw_bn_at_1463_9":483.1,"combined_acquisition_plus_expansion_krw_trn":1.183,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"U.S._tariff_hedge_manufacturing_watch","notes":"Facility acquisition/expansion is Stage 2; product transfer, utilization, gross margin and FCF required before Green."}
{"case_id":"r7_loop11_sk_bioscience_idt_cmo_mna","symbol":"302440","company_name":"SK Bioscience","case_type":"success_candidate","primary_archetype":"CMO_M_AND_A_TRANSITION","stage2_date":"2024-06-27","stage4b_date":"2024-06-27","price_validation":{"price_data_source":"Reuters acquisition/event-return anchor","stage3_price":null,"deal_value_krw_bn":339,"deal_value_usd_mn":243.75,"stake_acquired_pct":60,"implied_idt_equity_value_krw_bn":565,"remaining_klocke_stake_pct":40,"sk_bioscience_ipo_proceeds_usd_bn":1.33,"deal_value_vs_ipo_proceeds_pct":18.3,"event_mfe_morning_pct":11.7,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_event_premium","rerating_result":"vaccine_CMO_transition_watch","notes":"IDT acquisition is Stage 2; utilization, backlog, margin and FCF required before Green."}
{"case_id":"r7_loop11_hanall_immunovant_batoclimab_ted_failure","symbol":"009420","company_name":"HanAll Biopharma / Immunovant","case_type":"4c_watch","primary_archetype":"AUTOIMMUNE_PARTNER_TRIAL_FAILURE","stage4c_date":"2026-04-02","price_validation":{"price_data_source":"Reuters partner trial-failure anchor","stage3_price":null,"partner":"Immunovant/Roivant","trial":"two late-stage thyroid eye disease trials","primary_endpoint":"at least 2mm reduction in eye bulging after 24 weeks","result":"failed_to_meet_primary_goal","immunovant_event_mae_pct":-4.8,"immunovant_event_price_usd":23.89,"future_plan":"review future batoclimab development with HanAll Biopharma","price_validation_status":"hanall_stock_price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"partner_trial_failure_watch","notes":"Partner trial failure is 4C-watch; hard 4C requires broader pipeline/cashflow impairment confirmation."}
{"case_id":"r7_loop11_lunit_medical_ai_external_validation","symbol":"328130","company_name":"Lunit","case_type":"insufficient_evidence","primary_archetype":"MEDICAL_AI_EXTERNAL_VALIDATION","stage2_date":"2025-03-17","price_validation":{"price_data_source":"arXiv external validation evidence","stage3_price":null,"exam_count":163449,"positive_cases":1368,"negative_exams":162081,"overall_auc":0.91,"precision":0.08,"recall":0.73,"non_invasive_cancer_auc":0.85,"calcification_auc":0.80,"dense_breast_auc":0.90,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"unknown_insufficient_evidence","rerating_result":"medical_AI_validation_watch","notes":"External validation is Stage 2; reimbursement, hospital adoption, recurring revenue, gross margin and cash runway required before Green."}
{"case_id":"r7_loop11_biopharma_tariff_policy_relief_basket","symbol":"207940/068270/biopharma_basket","company_name":"Biopharma tariff-policy basket","case_type":"event_premium","primary_archetype":"BIOPHARMA_POLICY_TARIFF_RELIEF","stage2_date":"2025-05-21","price_validation":{"price_data_source":"Reuters policy/sector-return anchor","stage3_price":null,"pharmaceutical_sector_event_mfe_pct":3.97,"samsung_biologics_event_mfe_pct":6.23,"celltrion_event_mfe_pct":0.35,"kospi_same_context_pct":0.99,"foreign_net_buy_krw_bn":113.7,"foreign_net_buy_usd_mn":82.05,"won_strengthening_pct":0.56,"policy_package_context":"additional support for biopharma and auto sectors against U.S. tariffs","price_validation_status":"reported_sector_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_policy_relief","rerating_result":"biopharma_tariff_policy_watch","notes":"Policy relief is Stage 2, not Green; company-level revenue, margin and FCF required."}
```

## shadow weight row 초안

```csv
archetype,commercial_revenue,royalty_visibility,prescription_volume,reimbursement,hospital_adoption,utilization,gross_margin,cash_runway,partner_execution,event_penalty,clinical_regulatory_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
BIO_PLATFORM_ROYALTY_CONVERSION,+5,+5,+3,+3,+3,+0,+5,+4,+5,-3,+5,+5,+4,Alteogen/Keytruda SC needs royalty/supply revenue and patent durability.
KOREAN_NEW_DRUG_GLOBAL_APPROVAL,+5,+5,+5,+5,+4,+0,+5,+4,+5,-4,+4,+5,+4,Yuhan/lazertinib approval is Stage 2 until prescription/royalty revenue confirms.
CDMO_US_TARIFF_HEDGE_CAPACITY,+4,+0,+0,+0,+0,+5,+5,+4,+3,-4,+2,+4,+4,SamsungBio/Celltrion facilities need utilization/backlog/margin/FCF.
CMO_M_AND_A_TRANSITION,+4,+0,+0,+0,+0,+5,+5,+4,+4,-5,+2,+5,+4,SK Bioscience IDT acquisition is Stage 2 until integration and utilization confirm.
BIOPHARMA_POLICY_TARIFF_RELIEF,+2,+0,+0,+0,+0,+2,+3,+3,+2,-5,+3,+5,+3,Policy support is relief, not Green.
AUTOIMMUNE_PARTNER_TRIAL_FAILURE,+0,+0,+0,+0,+0,+0,+0,+5,+5,0,+5,+3,+5,HanAll/Immunovant trial failure is partner-program 4C-watch.
MEDICAL_AI_EXTERNAL_VALIDATION,+2,+0,+0,+5,+5,+0,+3,+5,+3,-4,+4,+5,+5,Lunit external validation is not Green without reimbursement/adoption/revenue.
APPROVAL_OR_VALIDATION_ONLY_NOT_GREEN,+0,+0,+0,+0,+0,+0,+0,+4,+3,-5,+4,+5,+4,Approval/validation headlines remain Stage 2 until commercial conversion.
```

---

# 이번 R7 Loop 11 결론

R7은 **가장 늦게 Green을 줘야 하는 섹터**다. 좋은 뉴스가 많지만, 뉴스와 돈 사이에 가장 긴 복도가 있다.

```text
1. Alteogen은 platform royalty Stage 2가 강하다.
   하지만 FDA approval, launch, royalty/supply revenue, patent durability 전 Green은 아니다.

2. Yuhan / Lazertinib은 한국 신약 글로벌 승인 Stage 2다.
   그러나 royalty, milestone, prescription uptake 전 Stage 3는 아니다.

3. Samsung Biologics는 좋은 U.S. facility evidence에도 price reaction이 실패했다.
   이건 evidence_good_but_price_failed로 둔다.

4. Celltrion은 U.S. tariff hedge manufacturing Stage 2다.
   제품 이전, utilization, gross margin, FCF가 Stage 3 조건이다.

5. SK Bioscience의 IDT 인수는 CMO 전환 Stage 2다.
   M&A 발표 +11.7%는 backlog/utilization 전 4B-watch다.

6. HanAll / Immunovant는 partner trial failure 4C-watch다.
   파트너 pipeline은 한국 회사 가격경로가 없어도 RedTeam에 들어가야 한다.

7. Lunit은 의료AI 외부검증 Stage 2다.
   AUC 0.91이어도 reimbursement, hospital adoption, recurring revenue 전 Green 금지다.

8. Biopharma tariff-policy basket은 event premium이다.
   정책지원은 회사별 매출·마진·FCF로 닫히기 전에는 Green이 아니다.
```

한 문장으로 압축하면:

> **R7에서 진짜 Stage 3는 “승인·임상·대형 파트너·CDMO 공장·AI 성능이 좋다”가 아니라, 처방·수가·병원도입·로열티·가동률·마진·FCF가 실제로 들어오기 시작하는 순간이다.**

[1]: https://www.reuters.com/business/healthcare-pharmaceuticals/merck-says-keytruda-injection-par-with-approved-iv-version-trial-2024-11-19/?utm_source=chatgpt.com "Merck says Keytruda injection on par with approved IV version in trial"
[2]: https://www.reuters.com/business/healthcare-pharmaceuticals/us-fda-approves-jjs-combination-therapy-type-lung-cancer-2024-08-20/?utm_source=chatgpt.com "US FDA approves J&J's chemotherapy-free treatment for lung cancer"
[3]: https://www.reuters.com/business/healthcare-pharmaceuticals/south-korean-shares-rise-1-pharmaceutical-stocks-jump-2025-05-21/?utm_source=chatgpt.com "South Korean shares rise 1% as pharmaceutical stocks jump"
[4]: https://www.reuters.com/business/healthcare-pharmaceuticals/south-koreas-celltrion-says-tapped-buy-us-pharma-factory-offset-tariff-risk-2025-07-29/?utm_source=chatgpt.com "South Korea's Celltrion says tapped to buy US pharma factory to offset tariff risk"
[5]: https://www.reuters.com/markets/deals/south-koreas-sk-bioscience-buy-control-germanys-idt-biologika-244-mln-2024-06-27/?utm_source=chatgpt.com "South Korea's SK Bioscience to buy control of Germany's IDT Biologika for $244 mln"
[6]: https://www.reuters.com/business/healthcare-pharmaceuticals/immunovants-treatment-eye-disease-fails-late-stage-trial-2026-04-02/?utm_source=chatgpt.com "Immunovant's treatment for eye disease fails in late-stage trials"
[7]: https://arxiv.org/abs/2503.13581?utm_source=chatgpt.com "Subgroup Performance of a Commercial Digital Breast Tomosynthesis Model for Breast Cancer Detection"
