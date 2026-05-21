순서상 이번은 **R7 Loop 10 — 바이오·헬스케어·의료기기 가격경로 검증 라운드**다.

이번 R7은 지난번의 알테오젠·유한양행 중심을 줄이고, **미용 의료기기, 보툴리눔 미국 진입, 바이오 CMO M&A, 미국 생산시설 tariff hedge, 의료AI 외부검증, 파트너 임상 실패**를 섞어서 본다.

```text
round = R7 Loop 10
round_id = round_165
large_sector = BIOTECH_HEALTHCARE_DEVICE
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = false
```

이번 환경에서는 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉 OHLC를 안정적으로 직접 확보하지 못했다. 대신 Reuters / WSJ / Allure / New York Post / arXiv가 제공한 **가격 anchor, 이벤트 수익률, 인수금액, 매출·EBITDA 성장률, 임상·규제 지표**로 계산 가능한 값만 계산했다. 원시 OHLC가 없는 구간은 `price_data_unavailable_after_deep_search`로 표시했다.

---

# 1. 이번 라운드 대섹터

```text
R7 = 바이오·헬스케어·의료기기
```

R7의 Stage 3는 “FDA 승인”, “임상 성공”, “논문 성능”, “M&A”가 아니다. **처방량·병원 채택·보험/수가·상업매출·로열티·가동률·마진·FCF가 실제로 들어오는 순간**이다.

---

# 2. 대상 canonical archetype

```text
MEDICAL_AESTHETIC_DEVICE_GLOBALIZATION
AESTHETIC_DEVICE_TAKE_PRIVATE
BOTULINUM_US_MARKET_ENTRY
BIOPHARMA_CMO_M_AND_A
BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING
CDMO_US_TARIFF_HEDGE_CAPACITY
AUTOIMMUNE_PARTNER_TRIAL_FAILURE
MEDICAL_AI_EXTERNAL_VALIDATION
MEDICAL_AI_COMMERCIALIZATION_GATE
APPROVAL_OR_VALIDATION_ONLY_NOT_GREEN
EVENT_PREMIUM
EVIDENCE_GOOD_BUT_PRICE_FAILED
```

---

# 3. deep sub-archetype

```text
미용 의료기기:
- Jeisys Medical
- Classys peer read-through
- energy-based devices
- anti-aging / aesthetic healthcare
- global expansion
- take-private premium vs listed rerating

보툴리눔:
- Hugel Letybo
- FDA-approved neuromodulator
- U.S. launch
- price discount vs Botox
- channel penetration / ASP / repeat treatment before Green

CMO/CDMO:
- SK Bioscience / IDT Biologika
- Celltrion / ImClone Systems
- Samsung Biologics / GSK Rockville facility
- U.S. manufacturing / tariff hedge
- facility acquisition vs utilization / contract transfer / FCF

임상 파트너 리스크:
- HanAll Biopharma / Immunovant
- batoclimab thyroid eye disease trial failure
- partner pipeline value reset
- Korean licensor price path unavailable

의료AI:
- Lunit INSIGHT DBT
- external validation AUC
- subgroup weakness
- reimbursement / hospital adoption / recurring revenue before Green
```

---

# 4. 국장 신규 후보 case

## Case A — Jeisys Medical `success_candidate / aesthetic-device take-private`

```text
symbol = 287410
case_type = success_candidate + event_premium
archetype = MEDICAL_AESTHETIC_DEVICE_GLOBALIZATION / AESTHETIC_DEVICE_TAKE_PRIVATE
```

### stage date

```text
Stage 1:
2023~2024
- energy-based aesthetic device demand
- anti-aging / non-invasive procedure market growth
- Korea aesthetic-device exporter rerating

Stage 2:
2024-09-11
- ArchiMed acquires publicly traded Jeisys Medical
- deal value about $742M
- shares closed at 12,860원 before/around report
- FY2023 revenue about $107M
- adjusted pretax earnings about $31M
- revenue CAGR 44%, adjusted pretax earnings CAGR 45% over three years through FY2023

Stage 3:
없음
- take-private / PE acquisition은 Stage 2 event
- 상장사 Stage 3는 recurring device sales, consumables, margin, FCF 확인 필요

Stage 4B:
take-private premium / anti-aging theme만으로 동종 미용의료기기주가 급등하면 후보

Stage 4C:
device demand normalization, distributor inventory, regulatory recall, consumable attach-rate failure 시 후보
```

Jeisys Medical은 R7에서 “미용 의료기기 수요가 진짜로 해외 PE에게 평가받은” Stage 2 사례다. WSJ는 ArchiMed가 한국의 energy-based aesthetic device 기업 Jeisys를 약 7.42억 달러에 인수하고 delisting 절차를 시작했다고 보도했다. Jeisys는 2023년까지 3년간 매출이 연 44% 성장해 약 1.07억 달러, 조정 세전이익이 연 45% 성장해 약 3,100만 달러에 이르렀다. 다만 이것은 take-private valuation event이지, 남은 상장 peer의 Green 조건은 아니다. ([월스트리트저널][1])

### 실제 가격경로 검증

```text
price_data_source:
WSJ reported acquisition / price / financial anchors

entry_date:
2024-09-11

stage3_price:
N/A

reported_close_price:
12,860원

deal_value:
$742M

FY2023_revenue:
$107M

FY2023_adjusted_pretax_earnings:
$31M

adjusted_pretax_margin:
31 / 107
= 29.0%

revenue_CAGR_3Y:
+44% annually

adjusted_pretax_earnings_CAGR_3Y:
+45% annually

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_event_premium
rerating_result = aesthetic_device_take_private_watch
stage_failure_type = stage2_event_not_green
```

---

## Case B — 휴젤 `success_candidate / Letybo U.S. launch`

```text
symbol = 145020
case_type = success_candidate
archetype = BOTULINUM_US_MARKET_ENTRY
```

### stage date

```text
Stage 1:
2024
- Letybo FDA approval
- K-aesthetics / botulinum toxin U.S. entry
- Botox competitor narrative

Stage 2:
2025-03
- Letybo arrives in U.S. dermatology offices
- FDA-approved for glabellar lines
- possible unit price $9~12 vs Botox $12~18
- potential 25~33% discount

Stage 3:
없음
- U.S. launch만으로 Green 금지
- U.S. sales, channel penetration, ASP, repeat treatment, OPM 확인 필요

Stage 4B:
FDA approval / U.S. launch news만으로 valuation이 먼저 확장되면 후보

Stage 4C:
price war, safety issue, channel rollout failure, Botox/Daxxify/Dysport/Xeomin/Jeuveau competition 시 후보
```

Hugel의 Letybo는 미국 미용 보툴리눔 시장 진입이라는 Stage 2 evidence를 갖는다. Allure와 New York Post는 Letybo가 FDA 승인을 받은 neuromodulator로, 미국에서 glabellar lines 치료용으로 쓰이며, unit price가 약 9~12달러로 Botox 12~18달러보다 낮을 수 있다고 정리했다. 하지만 R7에서 launch와 가격경쟁력은 Green이 아니다. Green은 미국 매출, 병·의원 채널 침투, ASP, 반복시술, OPM으로 확인해야 한다. ([Allure][2])

### 실제 가격경로 검증

```text
price_data_source:
Allure / New York Post product launch and price anchors

stage3_price:
N/A

Hugel_stock_OHLC:
price_data_unavailable_after_deep_search

Letybo_unit_price_estimate:
$9~12 per unit

Botox_unit_price_estimate:
$12~18 per unit

low-end_discount:
9 / 12 - 1
= -25.0%

high-end_discount:
12 / 18 - 1
= -33.3%

FDA_approval_status:
approved neuromodulator for glabellar lines

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = U.S._botulinum_launch_watch
stage_failure_type = stage2_watch_success
```

---

## Case C — SK바이오사이언스 `success_candidate + M&A event premium`

```text
symbol = 302440
case_type = success_candidate + event_premium
archetype = BIOPHARMA_CMO_M_AND_A
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
M&A announcement day rally
- +11.7% is event premium unless utilization/backlog confirms

Stage 4C:
integration failure, utilization underperformance, CMO order failure, cash burn, goodwill impairment 시 후보
```

SK바이오사이언스는 IDT Biologika 지분 60%를 3,390억 원에 인수해 CMO/CDMO 전환을 시도했다. Reuters는 이 거래가 2021년 IPO 이후 첫 대형 M&A이며, 발표 후 주가가 오전장 11.7% 상승했다고 보도했다. 하지만 R7에서 M&A는 Stage 2다. Stage 3는 인수한 설비가 실제 backlog, utilization, margin, FCF로 연결될 때다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters acquisition / event-return anchors

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

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_event_premium
rerating_result = vaccine_CMO_transition_watch
stage_failure_type = stage2_M&A_not_green
```

---

## Case D — 셀트리온 `success_candidate / U.S. tariff-hedge manufacturing`

```text
symbol = 068270
case_type = success_candidate
archetype = BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING
```

### stage date

```text
Stage 1:
2025
- U.S. pharma tariff risk
- biosimilar U.S. localization need
- tariff hedge / supply-chain resilience

Stage 2:
2025-09-23
- Celltrion U.S. subsidiary acquires ImClone Systems from Eli Lilly
- acquisition value $330M
- U.S. manufacturing base secured

추가 Stage 2:
2025-11-19
- Celltrion plans up to 700B won / $478M expansion at U.S. factory

Stage 3:
없음
- plant acquisition / expansion만으로 Green 금지
- product transfer, FDA/quality readiness, utilization, gross margin, FCF 확인 필요

Stage 4B:
tariff hedge narrative로 주가가 먼저 과열되면 후보

Stage 4C:
integration delay, tariff policy reversal, biosimilar pricing pressure, capex burden 시 후보
```

셀트리온은 Eli Lilly로부터 ImClone Systems를 3.3억 달러에 인수했고, 이후 미국 공장에 최대 7,000억 원을 투자해 생산능력을 확대하겠다고 밝혔다. Reuters는 셀트리온이 미국 판매 제품과 향후 출시 제품을 tariff exposure에서 보호하기 위한 목적이라고 설명했다. 하지만 plant acquisition은 Stage 2다. Stage 3는 제품 이전, 가동률, 품질승인, gross margin, FCF가 확인될 때다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters transaction / investment anchors

stage3_price:
N/A

Celltrion_stock_OHLC:
price_data_unavailable_after_deep_search

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
stage_failure_type = stage2_watch_success
```

---

## Case E — 삼성바이오로직스 `evidence_good_but_price_failed`

```text
symbol = 207940
case_type = success_candidate + evidence_good_but_price_failed
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
2025-12-22
- Samsung Biologics buys GSK Rockville facility
- $280M acquisition
- 60,000L drug substance capacity
- first U.S. drug production facility

Stage 3:
없음
- facility acquisition만으로 Green 금지
- contract transfer, utilization, margin, FCF 확인 필요

Stage 4B:
대형 CDMO valuation이 이미 충분히 반영된 구간이면 후보

Stage 4C:
utilization underperformance, capex overrun, tariff benefit reversal, contract slowdown 시 후보
```

삼성바이오로직스는 GSK로부터 미국 Rockville 소재 Human Genome Sciences 시설을 2.8억 달러에 인수하기로 했다. 시설은 60,000L drug substance capacity를 갖고 있고, 삼성바이오로직스의 첫 미국 생산시설이다. 그런데 발표일 주가는 0.4% 하락했고, KOSPI는 2% 상승했다. 좋은 CDMO evidence라도 valuation이 이미 반영되어 있거나 revenue bridge가 약하면 `evidence_good_but_price_failed`로 처리해야 한다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event return / facility capacity anchor

stage3_price:
N/A

stage2_event_MAE_1D:
-0.4%

KOSPI_same_day_return:
+2.0%

relative_underperformance:
-0.4 - 2.0
= -2.4pp

deal_value:
$280M

facility_capacity:
60,000L drug substance capacity

expected_close:
around end-Q1 2026

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed
rerating_result = CDMO_US_capacity_watch
stage_failure_type = stage2_watch_success_but_price_failed
```

---

## Case F — 한올바이오파마 / Immunovant `4C-watch / partner trial failure`

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

한올바이오파마는 partner pipeline 리스크를 봐야 한다. Reuters는 Immunovant의 batoclimab이 thyroid eye disease late-stage trial 2건에서 24주 후 2mm 이상 안구돌출 감소라는 primary goal을 달성하지 못했다고 보도했다. Immunovant 주가는 4.8% 하락했고, Roivant는 TED에서 추가 개발을 지지하지 않는 결과라고 밝혔다. Immunovant는 HanAll Biopharma와 batoclimab의 향후 개발 계획을 검토하겠다고 했다. 한국 상장사 원시 OHLC는 확인하지 못했지만, 이는 분명한 partner-program 4C-watch다. ([Reuters][6])

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

## Case G — 루닛 `insufficient_evidence / medical AI external validation`

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
subgroup performance issue, reimbursement failure, adoption failure, cash burn/dilution 시 후보
```

Lunit INSIGHT DBT는 외부검증상 좋은 성능을 보였지만, 바로 Green은 아니다. arXiv 연구는 163,449건의 screening mammography exam에서 Lunit INSIGHT DBT를 평가했고, 전체 AUC 0.91을 기록했다. 그러나 non-invasive cancer, calcification, dense breast tissue subgroup에서는 성능이 낮아졌고, 연구진은 실제 임상 도입에서 세부 subgroup 평가와 주의가 필요하다고 결론냈다. 즉 R7 Stage 2 evidence는 맞지만, 수가·병원 도입·반복매출 전 Stage 3는 아니다. ([arXiv][7])

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
stage_failure_type = stage2_evidence_not_green
```

---

# 5. 이번 R7 case별 요약표

| case              | 분류                             |                                                      실제 가격검증 | alignment              |
| ----------------- | ------------------------------ | -----------------------------------------------------------: | ---------------------- |
| Jeisys Medical    | success_candidate + event      | take-private $742M, 12,860원, revenue $107M, adj. pretax $31M | Stage 2                |
| Hugel / Letybo    | success_candidate              |                      U.S. launch, $9~12/unit vs Botox $12~18 | Stage 2                |
| SK Bioscience     | success_candidate + event      |                          IDT 60% for 339B won, shares +11.7% | M&A Stage 2            |
| Celltrion         | success_candidate              |                ImClone $330M + U.S. expansion up to 700B won | Stage 2                |
| Samsung Biologics | evidence_good_but_price_failed |       GSK facility $280M, 60,000L, shares -0.4% vs KOSPI +2% | price failed           |
| HanAll Biopharma  | 4C-watch                       | Immunovant batoclimab TED trial failure, partner stock -4.8% | partner trial risk     |
| Lunit             | insufficient_evidence          |                   163,449 exams, AUC 0.91, subgroup weakness | validation not revenue |

---

# 6. score-price alignment 판정

```text
success_candidate:
- Jeisys Medical
- Hugel
- SK Bioscience
- Celltrion

event_premium:
- Jeisys take-private
- SK Bioscience IDT M&A

evidence_good_but_price_failed:
- Samsung Biologics GSK U.S. facility acquisition

thesis_break_watch:
- HanAll Biopharma / Immunovant batoclimab trial failure

unknown_insufficient_evidence:
- Lunit medical AI external validation

4B-watch:
- Jeisys/medical aesthetic device take-private premium이 peer valuation으로 번질 때
- Hugel U.S. launch news가 U.S. sales보다 먼저 가격화될 때
- SK Bioscience M&A announcement rally
- medical AI validation news로 주가가 먼저 급등할 때

4C-watch:
- HanAll partner clinical failure
- Lunit subgroup performance / reimbursement failure
- CDMO utilization underperformance
- botulinum price war / safety / channel rollout failure

hard_4C_confirmed:
- false
```

---

# 7. 점수비중 교정

## 올릴 축

```text
commercial_revenue +5
prescription_or_procedure_volume +5
channel_penetration +5
reimbursement_access +5
capacity_utilization +5
contract_backlog +4
gross_margin_visibility +4
cash_runway +4
repeat_treatment_or_consumables +4
hospital_adoption +4
```

### 왜 올리나

R7에서 Jeisys, Hugel, SK Bioscience, Celltrion 모두 좋은 Stage 2 후보가 될 수 있다. 하지만 이들은 각각 take-private, U.S. launch, M&A, facility acquisition이다. Stage 3는 **시술량·처방량·가동률·계약 이전·마진·FCF**로 확인되어야 한다.

## 내릴 축

```text
approval_news_only -5
clinical_headline_only -5
external_validation_without_revenue -4
M&A_without_utilization -5
take_private_premium_only -4
FDA_approval_without_commercial_sales -4
partner_pipeline_without_indication_success -4
pre_revenue_medical_AI_story -5
cash_burn_or_dilution_risk -5
subgroup_performance_risk -3
```

### 왜 내리나

Hugel Letybo는 미국 출시가 의미 있지만, launch만으로는 매출이 아니다. Lunit은 AUC 0.91이 좋아도 수가와 병원 도입 전에는 매출이 아니다. HanAll은 partner pipeline이 실패하면 한국 회사의 원시 가격경로가 없더라도 4C-watch를 붙여야 한다.

## Green gate 강화 조건

```text
R7 Stage 3-Green 필수:
1. approval / clearance / launch 중 최소 하나 확인
2. commercial launch 이후 매출 확인
3. prescription volume / procedure volume / hospital adoption 확인
4. reimbursement / payer / ASP 확인
5. revenue recognition
6. gross margin 또는 royalty 확인
7. cash runway / dilution risk 통과
8. partner execution risk 통과
9. price path가 evidence 이후 따라옴

금지:
FDA approval만 있음
임상 headline만 있음
논문 성능만 있음
M&A 발표만 있음
take-private premium만 있음
미국 공장 인수만 있음
파트너 pipeline 기대만 있음
현금 runway 부족
대규모 dilution 가능성
```

## 4B 조기감지 조건

```text
4B-watch:
FDA 승인 직후 주가 급등
U.S. launch 전후 매출 없이 valuation 확장
M&A 발표 당일 급등
take-private premium이 peer group으로 번짐
의료AI 논문/외부검증으로 주가만 급등
CDMO capacity premium이 가동률보다 먼저 확장
commercial revenue보다 valuation이 먼저 감

4B-elevated:
launch가 시작됐지만 처방·시술 증가가 느림
보험/수가 접근 제한
CDMO capex가 계약보다 빠름
경쟁 제품 출시
가격경쟁 심화
cash burn 지속
```

## 4C hard gate 조건

```text
FDA CRL / 허가 거절
효능·안전성 임상 실패
partner trial failure
상업화 실패
처방량 / 시술량 부진
보험/수가 실패
로열티 미발생
대규모 dilution
cash runway 붕괴
manufacturing inspection failure
product safety issue
subgroup clinical performance failure
partner launch failure
patent/IP legal loss
```

이번 R7 Loop 10에서는 hard 4C를 억지로 확정하지 않는다. HanAll/Immunovant는 partner trial failure라 강한 4C-watch지만, HanAll 자체 프로그램 전체 붕괴나 현금흐름 훼손이 확인된 것은 아니므로 hard 4C로 승격하지 않는다.

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

## docs/round/round_165.md 요약

```md
# R7 Loop 10. Biotech / Healthcare / Medical Device Price Validation

이번 라운드는 R7 Loop 10 price-validation 라운드다.

핵심 결론:
- Jeisys Medical is a medical aesthetic device Stage 2 case. ArchiMed acquired it for about $742M; shares closed around 12,860 won; FY2023 revenue was about $107M and adjusted pretax earnings about $31M. This is take-private validation, not listed Stage 3.
- Hugel Letybo is U.S. botulinum launch Stage 2. Letybo is FDA-approved for glabellar lines and may be priced at $9~12/unit vs Botox $12~18/unit. U.S. sales, channel penetration, ASP and OPM are required before Green.
- SK Bioscience IDT Biologika acquisition is CMO transition Stage 2. It bought 60% for 339B won and shares rose 11.7% in morning trade. Utilization, backlog, margin and FCF are required before Green.
- Celltrion U.S. manufacturing is Stage 2. ImClone acquisition was $330M, and expansion may be up to 700B won. Product transfer, quality readiness, utilization and FCF are required before Green.
- Samsung Biologics GSK facility is evidence_good_but_price_failed. It acquired a $280M U.S. facility with 60,000L capacity, but shares fell 0.4% while KOSPI rose 2%.
- HanAll Biopharma / Immunovant is partner trial 4C-watch. Batoclimab failed two late-stage thyroid eye disease trials; Immunovant shares fell 4.8%.
- Lunit is medical AI external-validation Stage 2. Lunit INSIGHT DBT was tested on 163,449 exams with AUC 0.91, but subgroup weaknesses and reimbursement/adoption risk block Green.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 165 R7 Loop 10 Biotech Healthcare Device Price Validation

## 반영 내용
- R7 Loop 10 price-validation 라운드를 추가했다.
- Medical aesthetic device take-private, U.S. botulinum launch, vaccine CMO M&A, biosimilar U.S. manufacturing, CDMO U.S. facility, autoimmune partner trial failure, medical AI external validation을 비교했다.
- Reuters/WSJ/Allure/New York Post/arXiv reported anchors로 가능한 MFE/MAE 및 clinical/commercial/transaction metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- commercial revenue, prescription/procedure volume, reimbursement, utilization, gross margin, repeat treatment/consumables 가중치 강화
- approval-only, M&A-without-utilization, take-private-premium-only, external-validation-without-revenue, partner-pipeline-without-indication-success 감점 강화
- partner trial failure / reimbursement failure / medical AI subgroup risk 4C-watch 강화
```

## case row 초안

```jsonl
{"case_id":"r7_loop10_jeisys_aesthetic_device_take_private","symbol":"287410","company_name":"Jeisys Medical","case_type":"success_candidate","primary_archetype":"MEDICAL_AESTHETIC_DEVICE_GLOBALIZATION","stage2_date":"2024-09-11","price_validation":{"price_data_source":"WSJ acquisition/price/financial anchors","stage3_price":null,"reported_close_price_krw":12860,"deal_value_usd_mn":742,"fy2023_revenue_usd_mn":107,"fy2023_adjusted_pretax_earnings_usd_mn":31,"adjusted_pretax_margin_pct":29.0,"revenue_cagr_3y_pct":44,"adjusted_pretax_earnings_cagr_3y_pct":45,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_event_premium","rerating_result":"aesthetic_device_take_private_watch","notes":"Take-private validates aesthetic-device demand but is Stage 2; recurring device sales, consumables, margin and FCF required for Green."}
{"case_id":"r7_loop10_hugel_letybo_us_launch","symbol":"145020","company_name":"Hugel","case_type":"success_candidate","primary_archetype":"BOTULINUM_US_MARKET_ENTRY","stage2_date":"2025-03","price_validation":{"price_data_source":"Allure/New York Post product launch and price anchors","stage3_price":null,"letybo_unit_price_usd":"9-12","botox_unit_price_usd":"12-18","low_end_discount_pct":-25.0,"high_end_discount_pct":-33.3,"fda_approval_status":"approved_neuromodulator_for_glabellar_lines","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"U.S._botulinum_launch_watch","notes":"U.S. launch is Stage 2; U.S. sales, channel penetration, ASP, repeat treatment and OPM required before Green."}
{"case_id":"r7_loop10_sk_bioscience_idt_cmo_mna","symbol":"302440","company_name":"SK Bioscience","case_type":"success_candidate","primary_archetype":"BIOPHARMA_CMO_M_AND_A","stage2_date":"2024-06-27","stage4b_date":"2024-06-27","price_validation":{"price_data_source":"Reuters acquisition/event-return anchors","stage3_price":null,"deal_value_krw_bn":339,"deal_value_usd_mn":243.75,"stake_acquired_pct":60,"implied_idt_equity_value_krw_bn":565,"remaining_klocke_stake_pct":40,"sk_bioscience_ipo_proceeds_usd_bn":1.33,"deal_value_vs_ipo_proceeds_pct":18.3,"event_mfe_morning_pct":11.7,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_event_premium","rerating_result":"vaccine_CMO_transition_watch","notes":"IDT acquisition is Stage 2; utilization, backlog, margin and FCF required before Green."}
{"case_id":"r7_loop10_celltrion_us_manufacturing_tariff_hedge","symbol":"068270","company_name":"Celltrion","case_type":"success_candidate","primary_archetype":"BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING","stage2_date":"2025-09-23/2025-11-19","price_validation":{"price_data_source":"Reuters transaction/investment anchors","stage3_price":null,"imclone_acquisition_usd_mn":330,"expansion_investment_krw_bn":700,"expansion_investment_usd_mn":478.17,"imclone_acquisition_krw_bn_at_1463_9":483.1,"combined_acquisition_plus_expansion_krw_trn":1.183,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"U.S._tariff_hedge_manufacturing_watch","notes":"U.S. facility is Stage 2; product transfer, quality readiness, utilization, gross margin and FCF required before Green."}
{"case_id":"r7_loop10_samsung_biologics_gsk_facility_price_failed","symbol":"207940","company_name":"Samsung Biologics","case_type":"evidence_good_but_price_failed","primary_archetype":"CDMO_US_TARIFF_HEDGE_CAPACITY","stage2_date":"2025-12-22","price_validation":{"price_data_source":"Reuters event return/facility capacity anchor","stage3_price":null,"stage2_event_mae_1d_pct":-0.4,"kospi_same_day_return_pct":2.0,"relative_underperformance_pp":-2.4,"deal_value_usd_mn":280,"facility_capacity_liters":60000,"expected_close":"around_end_Q1_2026","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"CDMO_US_capacity_watch","notes":"Good U.S. CDMO capacity event but immediate price reaction failed; utilization/contract transfer needed for fresh Stage 3."}
{"case_id":"r7_loop10_hanall_immunovant_batoclimab_ted_failure","symbol":"009420","company_name":"HanAll Biopharma / Immunovant","case_type":"4c_watch","primary_archetype":"AUTOIMMUNE_PARTNER_TRIAL_FAILURE","stage4c_date":"2026-04-02","price_validation":{"price_data_source":"Reuters partner trial-failure anchor","stage3_price":null,"partner":"Immunovant/Roivant","trial":"two late-stage thyroid eye disease trials","primary_endpoint":"at least 2mm reduction in eye bulging after 24 weeks","result":"failed_to_meet_primary_goal","immunovant_event_mae_pct":-4.8,"immunovant_event_price_usd":23.89,"future_plan":"review future batoclimab development with HanAll Biopharma","price_validation_status":"hanall_stock_price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"partner_trial_failure_watch","notes":"Partner trial failure is 4C-watch; hard 4C requires broader pipeline/cashflow impairment confirmation."}
{"case_id":"r7_loop10_lunit_medical_ai_external_validation","symbol":"328130","company_name":"Lunit","case_type":"insufficient_evidence","primary_archetype":"MEDICAL_AI_EXTERNAL_VALIDATION","stage2_date":"2025-03-17","price_validation":{"price_data_source":"arXiv external validation evidence","stage3_price":null,"exam_count":163449,"positive_cases":1368,"negative_exams":162081,"overall_auc":0.91,"precision":0.08,"recall":0.73,"non_invasive_cancer_auc":0.85,"calcification_auc":0.80,"dense_breast_auc":0.90,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"unknown_insufficient_evidence","rerating_result":"medical_AI_validation_watch","notes":"External validation is Stage 2; reimbursement, hospital adoption, recurring revenue, gross margin and cash runway required before Green."}
```

## shadow weight row 초안

```csv
archetype,commercial_revenue,procedure_or_prescription_volume,channel_penetration,reimbursement,capacity_utilization,gross_margin,cash_runway,event_penalty,clinical_partner_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
MEDICAL_AESTHETIC_DEVICE_GLOBALIZATION,+5,+5,+5,+1,+3,+5,+4,-3,+2,+4,+3,Jeisys take-private validates demand but listed Green requires recurring sales/consumables/margin/FCF.
BOTULINUM_US_MARKET_ENTRY,+5,+5,+5,+3,+0,+5,+4,-3,+3,+4,+4,Hugel Letybo U.S. launch needs sales/channel/ASP/repeat treatment before Green.
BIOPHARMA_CMO_M_AND_A,+4,+0,+0,+0,+5,+5,+4,-5,+2,+5,+4,SK Bioscience IDT M&A is Stage 2 until utilization/backlog/margin/FCF confirm.
BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING,+4,+0,+0,+1,+5,+5,+4,-3,+2,+4,+4,Celltrion U.S. facility is tariff hedge Stage 2, not Green before transfer/utilization/FCF.
CDMO_US_TARIFF_HEDGE_CAPACITY,+4,+0,+0,+0,+5,+5,+4,-4,+2,+4,+4,Samsung Biologics U.S. facility had weak price reaction; watch valuation saturation.
AUTOIMMUNE_PARTNER_TRIAL_FAILURE,+0,+0,+0,+0,+0,+0,+5,0,+5,+3,+5,HanAll/Immunovant trial failure is 4C-watch for partner-pipeline value.
MEDICAL_AI_EXTERNAL_VALIDATION,+2,+0,+0,+5,+0,+3,+5,-4,+3,+5,+5,Lunit external validation is not Green without reimbursement/adoption/revenue.
APPROVAL_OR_VALIDATION_ONLY_NOT_GREEN,+0,+0,+0,+0,+0,+0,+4,-5,+3,+5,+4,Approval/validation headlines should remain Stage 2 until commercial conversion.
```

---

# 이번 R7 Loop 10 결론

R7은 Stage 3를 가장 늦게 줘야 하는 섹터다.

```text
1. Jeisys Medical은 미용 의료기기 수요가 실제 PE valuation을 받은 Stage 2 사례다.
   그러나 take-private premium은 Green이 아니다.

2. Hugel Letybo는 미국 보툴리눔 시장 진입 Stage 2다.
   U.S. 매출, 채널침투, ASP, 반복시술 전 Stage 3는 아니다.

3. SK Bioscience의 IDT Biologika 인수는 CMO 전환 Stage 2다.
   M&A 발표는 +11.7% event premium이지만, 가동률·backlog·margin·FCF 전 Green 금지다.

4. Celltrion은 미국 생산시설 확보로 tariff hedge Stage 2다.
   제품 이전, 품질 readiness, 가동률, gross margin, FCF가 Stage 3 조건이다.

5. Samsung Biologics는 좋은 CDMO 뉴스에도 주가가 KOSPI를 언더퍼폼했다.
   이건 evidence_good_but_price_failed로 처리해야 한다.

6. HanAll Biopharma는 partner trial failure 4C-watch다.
   partner pipeline은 한국 회사 가격경로가 없어도 RedTeam에 들어가야 한다.

7. Lunit은 외부검증 AUC 0.91이 있어도,
   수가, 병원 도입, 반복매출, cash runway 전에는 Stage 3가 아니다.
```

한 문장으로 압축하면:

> **R7에서 진짜 Stage 3는 “승인·임상·논문·M&A가 좋다”가 아니라, 처방·시술·병원도입·수가·매출·가동률·마진·FCF로 돈이 실제로 들어오기 시작하는 순간이다.**
> **이번 R7 Loop 10은 미용의료기기·보툴리눔·CDMO·의료AI의 Stage 2 후보를 인정하되, M&A premium·external validation·partner trial failure·price failed를 4B/4C로 분리하는 라운드다.**

[1]: https://www.wsj.com/articles/europes-archimed-bets-on-anti-aging-trend-in-first-asia-deal-cbe16f5e?utm_source=chatgpt.com "Europe's ArchiMed Bets on Anti-Aging Trend in First Asia Deal"
[2]: https://www.allure.com/story/letybo-neuromodulator-injectable?utm_source=chatgpt.com "Everything You Need to Know About Letybo, the Newest Botox Competitor"
[3]: https://www.reuters.com/markets/deals/south-koreas-sk-bioscience-buy-control-germanys-idt-biologika-244-mln-2024-06-27/?utm_source=chatgpt.com "South Korea's SK Bioscience to buy control of Germany's IDT Biologika for $244 mln"
[4]: https://www.reuters.com/business/healthcare-pharmaceuticals/celltrion-unit-pays-330-million-eli-lilly-production-facility-filing-shows-2025-09-23/?utm_source=chatgpt.com "Celltrion unit pays $330 million for Eli Lilly production facility, filing shows"
[5]: https://www.reuters.com/business/healthcare-pharmaceuticals/samsung-biologics-buy-us-drug-production-facility-gsk-280-mln-2025-12-21/?utm_source=chatgpt.com "Samsung Biologics to buy US drug production facility from GSK for $280 million"
[6]: https://www.reuters.com/business/healthcare-pharmaceuticals/immunovants-treatment-eye-disease-fails-late-stage-trial-2026-04-02/?utm_source=chatgpt.com "Immunovant's treatment for eye disease fails in late-stage trials"
[7]: https://arxiv.org/abs/2503.13581?utm_source=chatgpt.com "Subgroup Performance of a Commercial Digital Breast Tomosynthesis Model for Breast Cancer Detection"
