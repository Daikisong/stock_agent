순서상 이번은 **R7 Loop 9 — 바이오·헬스케어·의료기기 가격경로 검증 라운드**다.

이번 R7 Loop 9는 지난번의 “승인·논문·M&A는 Stage 2까지만”이라는 원칙을 더 강하게 검증한다. 이번에는 **SC 제형 로열티, 국산 항암제 상업화, 백신 CMO M&A, 바이오시밀러 미국 생산, CDMO 미국 시설, 보툴리눔 미국 출시, 의료AI 외부검증**을 섞어서 봤다.

```text
round = R7 Loop 9
round_id = round_152
large_sector = BIOTECH_HEALTHCARE_DEVICE
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = false
```

원시 수정주가 일봉 OHLC는 이번 환경에서 안정적으로 직접 확보하지 못했다. 대신 Reuters / Barron’s / MarketWatch / WSJ / Allure / New York Post / arXiv가 제공한 **가격 anchor, 이벤트 수익률, 승인·매출·계약·임상 지표**로 계산 가능한 값만 계산했다.

---

# 1. 이번 라운드 대섹터

```text
R7 = 바이오·헬스케어·의료기기
```

R7의 핵심은 “승인됐다”, “임상이 좋다”, “논문 성능이 좋다”가 아니라, **처방량·보험/수가·상업매출·로열티·가동률·마진·FCF가 실제로 들어오는가**다.

---

# 2. 대상 canonical archetype

```text
SC_FORMULATION_ROYALTY_PLATFORM
KOREA_ONCOLOGY_DRUG_COMMERCIALIZATION
BIOTECH_ROYALTY_COMMERCIALIZATION
CDMO_HEALTHCARE_CONTRACT
CDMO_US_TARIFF_HEDGE_CAPACITY
BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING
BOTULINUM_US_MARKET_ENTRY
MEDICAL_AI_EXTERNAL_VALIDATION
MEDICAL_AI_COMMERCIALIZATION_GATE
MANUFACTURING_INSPECTION_CRL_OVERLAY
M&A_WITHOUT_UTILIZATION
APPROVAL_ONLY_NOT_COMMERCIALIZATION
EVENT_PREMIUM
```

---

# 3. deep sub-archetype

```text
로열티 / SC 제형:
- Alteogen
- Merck Keytruda Qlex
- Keytruda 2024 sales nearly $30B
- Qlex 30~40% conversion target
- Qlex 2025 sales $40M
- Qlex Q1 2026 sales $128M
- Halozyme patent challenge risk
- royalty recognition / cash receipt before Green

국산 항암제:
- Yuhan lazertinib / Lazcluze
- J&J Rybrevant + Lazcluze
- FDA approval
- Rybrevant SC CRL as manufacturing inspection watch
- prescription volume / partner sales / royalty before Green

CMO / CDMO:
- SK Bioscience IDT Biologika
- Samsung Biologics GSK facility
- Celltrion ImClone facility
- U.S. tariff hedge
- acquisition announcement vs utilization / backlog / margin

미용·보툴리눔:
- Hugel Letybo
- U.S. launch
- price discount vs Botox
- channel penetration / ASP / repeat order before Green

의료AI:
- Lunit INSIGHT DBT
- external validation
- AUC / subgroup risk
- reimbursement / hospital adoption / recurring revenue before Green
```

---

# 4. 국장 신규 후보 case

## Case A — 알테오젠 `structural_success_candidate / SC royalty commercialization watch`

```text
symbol = 196170
case_type = structural_success_candidate + 4B-watch
archetype = SC_FORMULATION_ROYALTY_PLATFORM
```

### stage date

```text
Stage 1:
2024-11-19
- Merck injectable Keytruda late-stage data non-inferior vs IV
- Alteogen enzyme used with Keytruda SC formulation

Stage 2:
2025-09-19
- FDA approves Keytruda Qlex
- 1~2분 SC injection
- Keytruda 2024 sales nearly $30B
- Merck targets 30~40% adoption within two years

Stage 3:
2026 Q1 후보
- Keytruda Qlex 2025 sales $40M
- Q1 2026 Qlex sales $128M
- 상업화 매출이 발생하기 시작함
- 단, Alteogen royalty recognition / cash receipt 확인 전 Stage 3 확정은 보류

Stage 4B:
Keytruda Qlex approval / patent-cliff defense 기대가 알테오젠 valuation에 과도 반영된 구간

Stage 4C-watch:
Halozyme enzyme patent challenge / IP dispute
```

Merck의 Keytruda Qlex는 2025년 9월 FDA 승인을 받았고, 기존 IV 투여가 약 30분 걸리는 것과 달리 SC 제형은 용량에 따라 1~2분 투여가 가능하다. Keytruda는 2024년 거의 300억 달러 매출을 낸 블록버스터이고, Merck는 SC 제형이 2년 내 Keytruda 사용 환자의 30~40%까지 전환될 수 있다고 봤다. Alteogen은 Keytruda SC 제형에 쓰이는 효소 개발·제조사로 명시되어 있다. ([Reuters][1])

2025년 Keytruda Qlex 매출은 4,000만 달러였고, 2026년 1분기에는 1.28억 달러로 늘었다. 이건 R7에서 승인 뉴스가 실제 상업화 매출로 내려가기 시작한 드문 Stage 2→3 후보 evidence다. 다만 알테오젠 자체의 로열티 인식·현금 수취·마진 반영을 확인하기 전에는 Stage 3 확정이 아니라 `success_candidate`로 둔다. ([마켓워치][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / MarketWatch / Investors.com reported commercial anchors

stage3_price:
price_data_unavailable_after_deep_search

reason:
- Reuters / MarketWatch / Investors.com은 Keytruda Qlex approval, Merck sales, Alteogen enzyme evidence를 제공하지만,
  알테오젠 한국 주가 OHLC anchor는 제공하지 않음.
- KRX / Naver / Yahoo / Stooq 원시 일봉 OHLC 직접 확보 실패.

Keytruda_2024_sales:
nearly $30B

Keytruda_Qlex_2025_sales:
$40M

Qlex_2025_sales_vs_Keytruda_2024_sales:
40M / 30B = 0.13%

Qlex_Q1_2026_sales:
$128M

Qlex_Q1_2026_vs_2025_full_year:
128M / 40M = 3.2x

Merck_target_conversion:
30~40% of Keytruda patients within two years

MFE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
price_data_unavailable_after_deep_search

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = SC_royalty_commercialization_watch
stage_failure_type = stage2_to_stage3_candidate
```

---

## Case B — 유한양행 `success_candidate / oncology approval-to-royalty watch`

```text
symbol = 000100
case_type = success_candidate + manufacturing_inspection_watch
archetype = KOREA_ONCOLOGY_DRUG_COMMERCIALIZATION
```

### stage date

```text
Stage 1:
2024년
- lazertinib / Lazcluze global commercialization 기대
- J&J Rybrevant + Lazcluze partnership

Stage 2:
2024-08-20
- FDA approves Rybrevant + Lazcluze for EGFR-mutated NSCLC
- Phase 3 data showed 30% reduction in risk of progression or death vs osimertinib
- J&J expects Rybrevant peak sales >$5B

Stage 3:
보류
- prescription volume
- J&J product sales
- Yuhan royalty recognition
- Yuhan EPS revision 확인 필요

Stage 4B:
FDA approval만으로 유한양행 주가가 과도하게 선반영된 구간이면 후보

Stage 4C-watch:
2024-12-16
- FDA declines approval of SC Rybrevant version
- CRL related to manufacturing-facility inspection observations
- not efficacy/safety/formulation issue
```

J&J의 Rybrevant + Lazcluze 조합은 2024년 8월 EGFR 변이 비소세포폐암 1차 치료제로 FDA 승인을 받았다. Reuters는 이 승인이 late-stage study에서 AstraZeneca Tagrisso 대비 질병 진행까지의 시간을 늘린 데이터를 기반으로 했고, J&J가 Rybrevant peak sales를 50억 달러 이상으로 기대한다고 보도했다. Barron’s와 MarketWatch도 Phase 3에서 질병 진행 또는 사망 위험을 30% 줄였다고 정리했다. ([Reuters][3])

다만 2024년 12월 FDA는 Rybrevant SC 버전 승인을 거절했다. Reuters는 CRL이 제조시설 사전검사 관찰사항과 관련된 것이고, 제형·효능·안전성 데이터와는 무관하며 추가 임상을 요구하지 않았다고 보도했다. 따라서 이건 hard 4C가 아니라 `manufacturing_inspection_CRL_watch`다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / Barron's / MarketWatch FDA approval and CRL anchors

stage3_price:
N/A

Yuhan_stock_OHLC:
price_data_unavailable_after_deep_search

reason:
- Reuters / Barron's / MarketWatch는 J&J approval 및 SC CRL anchor는 제공하지만,
  유한양행 event-day 한국 주가 OHLC anchor는 제공하지 않음.
- KRX / Naver / Yahoo / Stooq 원시 일봉 OHLC 직접 확보 실패.

FDA_approval_date:
2024-08-20

risk_reduction_vs_osimertinib:
30%

J&J_Rybrevant_peak_sales_expectation:
>$5B

SC_Rybrevant_CRL_date:
2024-12-16

CRL_type:
manufacturing inspection observation

additional_clinical_studies_requested:
false

J&J_premarket_reaction:
+0.4% in Barron's approval report

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = FDA_approval_to_royalty_watch
stage_failure_type = stage2_watch_success
```

---

## Case C — SK바이오사이언스 `success_candidate + event_premium / CMO M&A`

```text
symbol = 302440
case_type = success_candidate + event_premium
archetype = CDMO_HEALTHCARE_CONTRACT / M&A_WITHOUT_UTILIZATION
```

### stage date

```text
Stage 1:
2024년
- vaccine/CDMO transition
- post-COVID business repositioning
- SK Group portfolio rebalancing

Stage 2:
2024-06-27
- SK Bioscience acquires 60% of IDT Biologika
- deal value 3,390억 원 / $243.75M
- first major M&A since 2021 IPO
- shares +11.7% morning trade
- separate price anchor: +5.8% to 52,200원

Stage 3:
없음
- M&A announcement만으로 Green 금지
- contract backlog, utilization, integration cost, margin, FCF 확인 필요

Stage 4B:
2024-06-27
- M&A announcement day rally

Stage 4C:
integration failure, utilization underperformance, CMO order failure, cash burn, goodwill impairment 시 후보
```

SK바이오사이언스는 독일 CMO IDT Biologika 지분 60%를 3,390억 원, 약 2.44억 달러에 인수한다고 발표했고, Reuters는 이것이 2021년 IPO 이후 첫 대형 M&A라고 보도했다. 발표 후 SK바이오사이언스 주가는 오전장에 11.7% 상승했다. MarketWatch는 같은 날 주가가 5.8% 올라 52,200원을 기록했다고 별도 가격 anchor를 제공했다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / MarketWatch reported event anchors

entry_date:
2024-06-27

stage3_price:
N/A

stage2_event_price_anchor:
52,200원

MarketWatch_event_MFE_1D:
+5.8%

implied_prior_close:
52,200 / 1.058
= 약 49,338원

Reuters_morning_MFE:
+11.7%

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

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

Stage 4B peak-before 여부:
partial_success
- M&A 발표 당일 급등은 Stage 2와 4B-watch를 동시에 기록.
```

### alignment

```text
score_price_alignment = success_candidate + event_premium
rerating_result = CMO_transition_watch
stage_failure_type = stage2_watch_success
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
2025-07-29
- U.S. pharma tariff risk
- Celltrion selected as preferred bidder for U.S. pharma factory
- planned investment 7,000억 원

Stage 2:
2025-09-23
- Celltrion U.S. subsidiary acquires ImClone Systems from Eli Lilly
- acquisition value $330M
- U.S. manufacturing base secured

추가 Stage 2:
2025-11-19
- Celltrion plans up to 7,000억 원 / $478M expansion at U.S. factory

Stage 3:
없음
- plant acquisition / expansion만으로 Green 금지
- product transfer, FDA/quality readiness, utilization, gross margin, FCF 확인 필요

Stage 4B:
tariff hedge narrative로 주가가 먼저 과열되면 후보

Stage 4C:
integration delay, tariff policy reversal, biosimilar pricing pressure, capex burden 시 후보
```

셀트리온은 미국 제약 관세 리스크를 줄이기 위해 미국 제조시설 인수 우선협상대상자가 됐고, 이후 Eli Lilly로부터 ImClone Systems를 3.3억 달러에 인수했다. Reuters는 셀트리온이 해당 시설을 업그레이드·확장해 미국 판매 제품과 향후 출시 제품을 관세 노출로부터 보호하려 한다고 보도했다. 이후 셀트리온은 미국 공장 증설에 최대 7,000억 원, 약 4.78억 달러를 투자할 계획도 밝혔다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters transaction / investment anchors

stage3_price:
N/A

Celltrion_stock_OHLC:
price_data_unavailable_after_deep_search

reason:
- Reuters는 transaction / investment anchor는 제공하지만 셀트리온 event-day 주가 reaction anchor는 제공하지 않음.
- KRX / Naver / Yahoo / Stooq 원시 일봉 OHLC 직접 확보 실패.

initial_planned_investment:
700B won / $503.78M

ImClone_acquisition_value:
$330M

expansion_investment:
up to 700B won / $478.17M

additional_possible_investment_range:
300B~700B won depending on tariff policy

USD_330M_KRW_equivalent_at_1463.9:
330M * 1,463.9
= 약 483.1B won

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = U.S._tariff_hedge_manufacturing_watch
stage_failure_type = stage2_watch_success
```

---

## Case E — 삼성바이오로직스 `success_candidate / evidence_good_but_price_failed`

```text
symbol = 207940
case_type = success_candidate + evidence_good_but_price_failed
archetype = CDMO_US_TARIFF_HEDGE_CAPACITY
```

### stage date

```text
Stage 1:
2025년
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

삼성바이오로직스는 GSK로부터 미국 Rockville 소재 Human Genome Sciences 시설을 2.8억 달러에 인수하기로 했다. Reuters는 이 시설이 60,000L drug substance capacity를 보유하며, 삼성바이오로직스가 장기 미국 수요에 대응하고 capacity·기술 업그레이드를 계획한다고 보도했다. 그러나 발표일 주가는 0.4% 하락해 KOSPI 2% 상승을 언더퍼폼했다. ([Reuters][7])

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

below_stage3_price_flag:
N/A

score-price read:
좋은 CDMO/U.S. facility evidence에도 가격은 즉시 실패.
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed
rerating_result = CDMO_US_capacity_watch
stage_failure_type = stage2_watch_success_but_price_failed
```

---

## Case F — 휴젤 `success_candidate / U.S. botulinum launch`

```text
symbol = 145020
case_type = success_candidate
archetype = BOTULINUM_US_MARKET_ENTRY
```

### stage date

```text
Stage 1:
2024~2025
- Letybo FDA approval
- K-aesthetics U.S. entry
- Botox competitor narrative

Stage 2:
2025-03
- Letybo arrives in U.S. dermatology offices
- potential 25~33% lower unit price than Botox
- 31M global treatments / 65-country approval footprint

Stage 3:
없음
- U.S. sales, channel penetration, ASP, repeat order, OPM 확인 전 Green 금지

Stage 4B:
FDA approval / U.S. launch news만으로 주가가 과열되면 후보

Stage 4C:
price war, safety issue, channel rollout failure, competition from Botox/Daxxify/Dysport/Xeomin/Jeuveau 시 후보
```

Letybo는 미국에 진입한 Hugel 제조 botulinum toxin neuromodulator로, New York Post는 Letybo가 Botox의 단위당 12~18달러 대비 9~12달러로 최대 30% 저렴할 수 있다고 보도했다. Vogue는 Letybo가 미국에는 2025년 3월 데뷔했지만 이미 65개국 이상에서 승인됐고 3,100만 건 이상의 치료 경험이 있다고 정리했다. ([New York Post][8])

### 실제 가격경로 검증

```text
price_data_source:
New York Post / Vogue product launch anchors

stage3_price:
N/A

Hugel_stock_OHLC:
price_data_unavailable_after_deep_search

reason:
- New York Post / Vogue는 product launch / pricing anchor는 제공하지만 휴젤 한국 주가 reaction anchor는 제공하지 않음.
- KRX / Naver / Yahoo / Stooq 원시 일봉 OHLC 직접 확보 실패.

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

global_treatments:
31M+

approved_countries:
65+

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = U.S._botulinum_launch_watch
stage_failure_type = stage2_watch_success
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

Stage 2:
2025-03-17
- Lunit INSIGHT DBT external validation
- 163,449 screening mammography exams
- overall AUC 0.91
- subgroup risks identified

Stage 3:
없음
- 외부검증만으로 Green 금지
- reimbursement, hospital adoption, recurring revenue, gross margin, cash runway 확인 필요

Stage 4B:
의료AI 논문/검증 뉴스로 주가가 먼저 급등하면 후보

Stage 4C:
subgroup performance issue, reimbursement failure, adoption failure, cash burn/dilution 시 후보
```

arXiv 연구는 Lunit INSIGHT DBT 모델을 163,449건의 screening mammography exam에 대해 평가했고, 전체 AUC는 0.91이었다. 다만 non-invasive cancer, calcification, dense breast tissue subgroup에서는 성능이 낮아졌고, 연구진은 실제 clinical deployment에서 세부 평가와 주의가 필요하다고 결론냈다. ([arXiv][9])

### 실제 가격경로 검증

```text
price_data_source:
arXiv external validation evidence

stage3_price:
N/A

Lunit_stock_OHLC:
price_data_unavailable_after_deep_search

reason:
- arXiv 논문은 주가 anchor를 제공하지 않음.
- Reuters / WSJ / MarketWatch / FT에서 이 event의 루닛 주가 reaction anchor를 찾지 못함.
- KRX / Naver / Yahoo / Stooq 원시 일봉 OHLC 직접 확보 실패.

exam_count:
163,449

positive_cases:
1,368 screen-detected cancers

negative_exams:
162,081

overall_AUC:
0.91

non_invasive_cancer_AUC:
0.85

calcification_AUC:
0.80

dense_breast_AUC:
0.90

precision:
0.08

recall:
0.73

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = unknown_insufficient_evidence
rerating_result = medical_AI_validation_watch
stage_failure_type = stage2_evidence_not_green
```

---

# 5. 이번 R7 case별 요약표

| case      | 분류                                |                                                                실제 가격검증 | alignment                   |
| --------- | --------------------------------- | ---------------------------------------------------------------------: | --------------------------- |
| 알테오젠      | structural_success 후보             |      Keytruda Qlex 2025 $40M, Q1 2026 $128M, Keytruda 2024 nearly $30B | success_candidate           |
| 유한양행      | success_candidate                 | Rybrevant+Lazcluze FDA approval, 30% risk reduction, SC CRL 제조검사 watch | success_candidate           |
| SK바이오사이언스 | success_candidate + event premium |                          52,200원, +5.8%; morning +11.7%; deal 339B won | stage2 event                |
| 셀트리온      | success_candidate                 |                           U.S. ImClone $330M, expansion up to 700B won | stage2 watch                |
| 삼성바이오로직스  | evidence_good_but_price_failed    |                     GSK facility $280M, 60,000L; 주가 -0.4% vs KOSPI +2% | evidence good, price failed |
| 휴젤        | success_candidate                 |                 Letybo $9~12/unit vs Botox $12~18/unit; 31M treatments | stage2 watch                |
| 루닛        | insufficient_evidence             |                                163,449 exams, AUC 0.91, subgroup risks | stage2 evidence, not Green  |

---

# 6. score-price alignment 판정

```text
success_candidate:
- 알테오젠
- 유한양행
- 셀트리온
- 휴젤

event_premium:
- SK바이오사이언스 IDT Biologika acquisition event

evidence_good_but_price_failed:
- 삼성바이오로직스 GSK facility acquisition event

unknown_insufficient_evidence:
- 루닛 medical AI external validation

4B-watch:
- SK바이오사이언스 M&A announcement rally
- 알테오젠 Keytruda Qlex approval/commercialization 기대가 valuation에 과도 반영된 구간
- 휴젤 U.S. launch news가 sales보다 먼저 가격에 반영되는 구간

4C-watch:
- 유한양행 / J&J Rybrevant SC manufacturing-inspection CRL
- 알테오젠 / Halozyme patent challenge
- 루닛 subgroup performance and reimbursement risk

hard_4c_confirmed:
- false
```

---

# 7. 점수비중 교정

## 올릴 축

```text
commercial_revenue +5
royalty_recognition +5
prescription_volume +5
reimbursement_access +5
capacity_utilization +5
contract_backlog +4
gross_margin_visibility +4
cash_runway +4
U.S._commercial_launch_with_sales +4
external_validation_with_adoption +3
```

### 왜 올리나

알테오젠은 R7에서 가장 구조적인 후보 중 하나다. Keytruda Qlex가 FDA 승인 후 2025년 4,000만 달러, 2026년 1분기 1.28억 달러 매출을 냈기 때문이다. 하지만 알테오젠의 royalty recognition과 cash receipt 확인 전 Stage 3 확정은 보류한다. ([마켓워치][2])

셀트리온과 삼성바이오로직스의 미국 생산시설 확보는 tariff hedge Stage 2로 볼 수 있다. 하지만 R7에서는 시설을 샀다는 것보다 **제품 이전, 가동률, 계약 이전, margin, FCF**가 Stage 3의 문이다. ([Reuters][10])

## 내릴 축

```text
approval_news_only -5
clinical_headline_only -5
paper_validation_without_revenue -4
M&A_without_utilization -5
FDA_approval_without_commercial_sales -4
partner_peak_sales_without_royalty_visibility -3
pre_revenue_biotech_story -5
cash_burn_or_dilution_risk -5
manufacturing_inspection_issue -4
subgroup_performance_risk -3
```

### 왜 내리나

유한양행의 Lazcluze approval, 휴젤 Letybo launch, 루닛 external validation은 모두 Stage 2 evidence로는 의미가 있다. 그러나 prescription volume, partner sales, royalty, reimbursement, hospital adoption, recurring revenue가 확인되기 전에는 Stage 3-Green이 아니다. ([Reuters][3])

## Green gate 강화 조건

```text
R7 Stage 3-Green 필수:
1. approval 또는 regulatory clearance
2. commercial launch
3. prescription volume 또는 hospital adoption
4. reimbursement / insurance / payer access
5. revenue recognition
6. royalty 또는 gross margin 확인
7. cash runway / dilution risk 통과
8. partner execution risk 통과
9. price path가 evidence 이후 따라옴

금지:
승인 뉴스만 있음
임상 헤드라인만 있음
논문 성능만 있음
파트너 peak sales만 있음
M&A 발표만 있음
FDA clearance 있지만 매출 없음
현금 runway 부족
대규모 유상증자/CB 위험
```

## 4B 조기감지 조건

```text
4B-watch:
FDA 승인 직후 주가 급등
파트너 peak sales 숫자만 반복
CDMO capacity premium이 가동률보다 먼저 확장
M&A 발표 당일 급등
의료AI 논문/외부검증으로 주가만 급등
commercial revenue보다 valuation이 먼저 감

4B-elevated:
launch가 시작됐지만 처방 증가가 느림
보험/급여 접근 제한
CDMO capex가 계약보다 빠름
경쟁약 출시
가격경쟁 심화
cash burn 지속
```

## 4C hard gate 조건

```text
FDA CRL / 허가 거절
효능·안전성 임상 실패
상업화 실패
처방량 부진
보험/급여 실패
로열티 미발생
대규모 dilution
cash runway 붕괴
manufacturing inspection failure
product safety issue
subgroup clinical performance failure
partner launch failure
patent/IP legal loss
```

이번 R7 Loop 9에서는 hard 4C를 억지로 확정하지 않는다. J&J의 Rybrevant SC CRL은 효능·안전성 문제가 아니라 제조시설 inspection issue였고 추가 임상도 요구되지 않았으므로 `4C-watch`다. ([Reuters][4])

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
hard_4c_confirmed = false
```

---

# 9. patch-ready 출력

## docs/round/round_152.md 요약

```md
# R7 Loop 9. Biotech / Healthcare / Medical Device Price Validation

이번 라운드는 R7 Loop 9 price-validation 라운드다.

핵심 결론:
- Alteogen은 Keytruda Qlex FDA approval과 commercial revenue 발생으로 R7의 구조적 success_candidate다. Keytruda Qlex는 2025년 $40M, Q1 2026 $128M sales를 기록했다. 다만 Alteogen royalty recognition / cash receipt 확인 전 Stage 3 확정은 보류한다.
- Yuhan은 Rybrevant + Lazcluze FDA approval로 Stage 2 후보지만, prescription volume, J&J sales, royalty recognition 전 Stage 3 금지다. Rybrevant SC CRL은 manufacturing-inspection watch이지 hard 4C는 아니다.
- SK Bioscience는 IDT Biologika 60% acquisition으로 Stage 2 후보이고, 주가는 52,200원, +5.8%, morning +11.7% 반응했다. 하지만 M&A announcement는 Stage 2 / event premium이다.
- Celltrion은 ImClone acquisition과 U.S. plant expansion으로 tariff-hedge Stage 2 후보지만, product transfer / utilization / margin / FCF 전 Green 금지다.
- Samsung Biologics는 GSK Rockville facility acquisition에도 주가 -0.4%, KOSPI +2%로 언더퍼폼했다. 좋은 CDMO 뉴스도 valuation saturation이면 price failed다.
- Hugel Letybo는 U.S. botulinum launch Stage 2 후보지만, U.S. sales / channel penetration / ASP / OPM 전 Green 금지다.
- Lunit은 external validation AUC 0.91이지만 reimbursement / hospital adoption / recurring revenue 전 Stage 3가 아니다.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 152 R7 Loop 9 Biotech Healthcare Device Price Validation

## 반영 내용
- R7 Loop 9 price-validation 라운드를 추가했다.
- SC royalty platform, Korean oncology commercialization, vaccine CMO M&A, biosimilar tariff-hedge manufacturing, CDMO U.S. facility, botulinum U.S. launch, medical AI external validation을 비교했다.
- Reuters/Barron’s/MarketWatch/WSJ/Allure/New York Post/arXiv reported anchors로 가능한 MFE/MAE 및 commercial/clinical/transaction metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- commercial revenue, royalty recognition, prescription volume, reimbursement, utilization, gross margin 가중치 강화
- approval-only, clinical-headline-only, paper validation without revenue, M&A without utilization 감점 강화
- manufacturing-inspection CRL, patent/IP risk, reimbursement failure 4C-watch 강화
```

## case row 초안

```jsonl
{"case_id":"r7_loop9_alteogen_keytruda_qlex_commercialization","symbol":"196170","company_name":"알테오젠","case_type":"success_candidate","primary_archetype":"SC_FORMULATION_ROYALTY_PLATFORM","stage1_date":"2024-11-19","stage2_date":"2025-09-19","stage3_date":"2026-Q1_candidate","stage4c_date":"IP_patent_watch","price_validation":{"price_data_source":"Reuters/MarketWatch/Investors.com reported commercial anchors","stage3_price":null,"keytruda_2024_sales_usd_bn":30.0,"keytruda_qlex_2025_sales_usd_mn":40.0,"qlex_2025_sales_vs_keytruda_2024_pct":0.13,"qlex_q1_2026_sales_usd_mn":128.0,"qlex_q1_2026_vs_2025_full_year_multiple":3.2,"merck_target_conversion_pct":"30-40","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"SC_royalty_commercialization_watch","notes":"Qlex commercial sales validate Stage 2-to-3 path, but Alteogen royalty recognition and cash receipt required for Stage 3 confirmation."}
{"case_id":"r7_loop9_yuhan_lazcluze_approval_royalty_watch","symbol":"000100","company_name":"유한양행","case_type":"success_candidate","primary_archetype":"KOREA_ONCOLOGY_DRUG_COMMERCIALIZATION","stage2_date":"2024-08-20","stage4c_date":"2024-12-16","price_validation":{"price_data_source":"Reuters/Barron's/MarketWatch FDA approval and CRL anchors","stage3_price":null,"risk_reduction_vs_osimertinib_pct":30,"jnj_rybrevant_peak_sales_expectation_usd_bn":5.0,"sc_rybrevant_crl_type":"manufacturing inspection observation","additional_clinical_studies_requested":false,"jnj_premarket_reaction_pct":0.4,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"FDA_approval_to_royalty_watch","notes":"Approval is Stage 2; prescription volume, J&J product sales, Yuhan royalty recognition and EPS revision required for Stage 3. SC CRL is manufacturing watch, not hard 4C."}
{"case_id":"r7_loop9_sk_bioscience_idt_cmo_mna","symbol":"302440","company_name":"SK바이오사이언스","case_type":"success_candidate","primary_archetype":"CDMO_HEALTHCARE_CONTRACT","stage2_date":"2024-06-27","stage4b_date":"2024-06-27","price_validation":{"price_data_source":"Reuters/MarketWatch reported event anchors","stage3_price":null,"stage2_event_price_anchor":52200,"marketwatch_event_mfe_1d_pct":5.8,"implied_prior_close":49338,"reuters_morning_mfe_pct":11.7,"deal_value_krw_bn":339,"deal_value_usd_mn":243.75,"stake_acquired_pct":60,"implied_idt_equity_value_krw_bn":565,"remaining_klocke_stake_pct":40,"sk_bioscience_ipo_proceeds_usd_bn":1.33,"deal_value_vs_ipo_proceeds_pct":18.3,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_event_premium","rerating_result":"CMO_transition_watch","notes":"IDT acquisition is Stage 2; utilization, backlog, margin and FCF required before Green."}
{"case_id":"r7_loop9_celltrion_us_factory_tariff_hedge","symbol":"068270","company_name":"셀트리온","case_type":"success_candidate","primary_archetype":"BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING","stage1_date":"2025-07-29","stage2_date":"2025-09-23","price_validation":{"price_data_source":"Reuters transaction/investment anchors","stage3_price":null,"initial_planned_investment_krw_bn":700,"initial_planned_investment_usd_mn":503.78,"imclone_acquisition_usd_mn":330,"imclone_acquisition_krw_bn":483.1,"expansion_investment_krw_bn":700,"expansion_investment_usd_mn":478.17,"additional_possible_investment_krw_bn":"300-700","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"U.S._tariff_hedge_manufacturing_watch","notes":"U.S. facility is Stage 2; product transfer, FDA readiness, utilization, gross margin and FCF required before Green."}
{"case_id":"r7_loop9_samsung_biologics_gsk_facility_price_failed","symbol":"207940","company_name":"삼성바이오로직스","case_type":"evidence_good_but_price_failed","primary_archetype":"CDMO_US_TARIFF_HEDGE_CAPACITY","stage2_date":"2025-12-22","price_validation":{"price_data_source":"Reuters reported event return/facility capacity anchor","stage3_price":null,"stage2_event_mae_1d_pct":-0.4,"kospi_same_day_return_pct":2.0,"relative_underperformance_pp":-2.4,"deal_value_usd_mn":280,"facility_capacity_liters":60000,"expected_close":"around end-Q1 2026","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"CDMO_US_capacity_watch","notes":"Good U.S. CDMO capacity event but immediate price reaction failed; utilization/contract transfer needed for fresh Stage 3."}
{"case_id":"r7_loop9_hugel_letybo_us_launch","symbol":"145020","company_name":"휴젤","case_type":"success_candidate","primary_archetype":"BOTULINUM_US_MARKET_ENTRY","stage2_date":"2025-03","price_validation":{"price_data_source":"New York Post/Vogue product launch anchors","stage3_price":null,"letybo_unit_price_usd":"9-12","botox_unit_price_usd":"12-18","low_end_discount_pct":-25.0,"high_end_discount_pct":-33.3,"global_treatments_mn":31,"approved_countries":65,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"U.S._botulinum_launch_watch","notes":"U.S. launch is Stage 2; U.S. sales, channel penetration, ASP, repeat order and OPM required before Green."}
{"case_id":"r7_loop9_lunit_medical_ai_external_validation","symbol":"328130","company_name":"루닛","case_type":"insufficient_evidence","primary_archetype":"MEDICAL_AI_EXTERNAL_VALIDATION","stage2_date":"2025-03-17","price_validation":{"price_data_source":"arXiv external validation evidence","stage3_price":null,"exam_count":163449,"positive_cases":1368,"negative_exams":162081,"overall_auc":0.91,"non_invasive_cancer_auc":0.85,"calcification_auc":0.80,"dense_breast_auc":0.90,"precision":0.08,"recall":0.73,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"unknown_insufficient_evidence","rerating_result":"medical_AI_validation_watch","notes":"External validation is Stage 2; reimbursement, hospital adoption, recurring revenue, gross margin and cash runway required before Green."}
```

## shadow weight row 초안

```csv
archetype,commercial_revenue,royalty_recognition,prescription_volume,reimbursement,capacity_utilization,gross_margin,cash_runway,event_penalty,manufacturing_ip_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
SC_FORMULATION_ROYALTY_PLATFORM,+5,+5,+3,+3,+0,+4,+3,-2,+4,+5,+4,Alteogen needs royalty recognition/cash receipt after Qlex commercial sales.
KOREA_ONCOLOGY_DRUG_COMMERCIALIZATION,+5,+5,+5,+5,+0,+4,+4,-3,+4,+4,+5,Yuhan approval is Stage 2; prescription, J&J sales and Yuhan royalty required.
CDMO_HEALTHCARE_CONTRACT,+4,+0,+0,+0,+5,+5,+4,-4,+3,+4,+4,SK Bioscience M&A is Stage 2 until utilization/backlog/margin/FCF confirm.
BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING,+4,+0,+0,+1,+5,+5,+4,-2,+3,+3,+4,Celltrion U.S. facility is tariff hedge Stage 2, not Green before transfer/utilization/FCF.
CDMO_US_TARIFF_HEDGE_CAPACITY,+4,+0,+0,+0,+5,+5,+4,-3,+3,+4,+4,Samsung Biologics U.S. facility had weak price reaction; watch valuation saturation.
BOTULINUM_US_MARKET_ENTRY,+5,+0,+3,+3,+0,+5,+4,-3,+3,+4,+4,Hugel U.S. launch requires channel sales, ASP and OPM before Green.
MEDICAL_AI_EXTERNAL_VALIDATION,+2,+0,+0,+5,+0,+3,+5,-4,+3,+5,+5,Lunit external validation is not Green without reimbursement/adoption/revenue.
M&A_WITHOUT_UTILIZATION,+0,+0,+0,+0,+5,+4,+4,-5,+2,+5,+4,M&A announcement should not become Green until utilization and cashflow confirm.
```

---

# 이번 R7 Loop 9 결론

R7은 Stage 3를 가장 늦게 줘야 하는 섹터다.

```text
1. 알테오젠은 이번 라운드에서 가장 구조적인 후보다.
   Keytruda Qlex가 실제 매출을 내기 시작했기 때문이다.
   그래도 알테오젠 로열티 인식과 현금수취 전 Stage 3 확정은 보류한다.

2. 유한양행은 FDA approval로 강한 Stage 2 후보다.
   하지만 처방량, J&J 매출, 로열티, EPS revision 전 Stage 3는 아니다.

3. SK바이오사이언스는 IDT 인수 발표로 가격이 반응했지만,
   M&A 발표는 Stage 2이자 event premium이다.

4. 셀트리온과 삼성바이오로직스의 미국 공장 확보는 tariff hedge Stage 2다.
   제품 이전, 가동률, 마진, FCF가 Stage 3 조건이다.

5. 삼성바이오로직스는 좋은 CDMO 뉴스에도 주가가 KOSPI를 언더퍼폼했다.
   valuation saturation이면 evidence_good_but_price_failed로 처리해야 한다.

6. 휴젤 Letybo는 미국 출시가 Stage 2지만,
   미국 매출, 채널 침투, ASP, 반복 주문 전 Green 금지다.

7. 루닛은 외부검증 AUC 0.91이 있어도,
   수가, 병원 도입, 반복매출, cash runway 전에는 Stage 3가 아니다.

8. 이번 R7 Loop 9에서 hard 4C는 억지로 만들지 않았다.
   제조시설 CRL, IP dispute, subgroup risk는 4C-watch다.
```

한 문장으로 압축하면:

> **R7에서 진짜 Stage 3는 “승인·임상·논문이 좋다”가 아니라, 처방·매출·로열티·수가·가동률·FCF로 돈이 실제로 들어오기 시작하는 순간이다.**
> **R7은 Stage 2 후보가 많지만, Stage 3-Green은 가장 보수적으로 줘야 한다.**

[1]: https://www.reuters.com/business/healthcare-pharmaceuticals/us-fda-approves-mercks-new-injectable-version-keytruda-2025-09-19/?utm_source=chatgpt.com "US FDA approves Merck's injectable version of blockbuster cancer therapy Keytruda"
[2]: https://www.marketwatch.com/story/mercks-outlook-for-2026-comes-in-lower-than-expected-as-pipeline-faces-make-or-break-year-e797985f?utm_source=chatgpt.com "Merck's outlook for 2026 comes in below expectations as pipeline faces make-or-break year"
[3]: https://www.reuters.com/business/healthcare-pharmaceuticals/us-fda-approves-jjs-combination-therapy-type-lung-cancer-2024-08-20/?utm_source=chatgpt.com "US FDA approves J&J's chemotherapy-free treatment for lung cancer"
[4]: https://www.reuters.com/business/healthcare-pharmaceuticals/us-fda-declines-approve-injection-form-jjs-lung-cancer-drug-2024-12-16/?utm_source=chatgpt.com "US FDA declines to approve injection form of J&J's lung cancer drug"
[5]: https://www.reuters.com/markets/deals/south-koreas-sk-bioscience-buy-control-germanys-idt-biologika-244-mln-2024-06-27/?utm_source=chatgpt.com "South Korea's SK Bioscience to buy control of Germany's IDT Biologika for $244 mln"
[6]: https://www.reuters.com/business/healthcare-pharmaceuticals/south-koreas-celltrion-says-tapped-buy-us-pharma-factory-offset-tariff-risk-2025-07-29/?utm_source=chatgpt.com "South Korea's Celltrion says tapped to buy US pharma factory to offset tariff risk"
[7]: https://www.reuters.com/business/healthcare-pharmaceuticals/samsung-biologics-buy-us-drug-production-facility-gsk-280-mln-2025-12-21/?utm_source=chatgpt.com "Samsung Biologics to buy US drug production facility from GSK for $280 million"
[8]: https://nypost.com/2025/03/12/lifestyle/botoxs-biggest-rival-lands-in-the-us-leytbo-said-to-be-faster-acting-and-up-to-30-cheaper/?utm_source=chatgpt.com "Botox's biggest rival lands in the US - Leytbo said to be faster-acting and up to 30% cheaper"
[9]: https://arxiv.org/abs/2503.13581?utm_source=chatgpt.com "Subgroup Performance of a Commercial Digital Breast Tomosynthesis Model for Breast Cancer Detection"
[10]: https://www.reuters.com/business/healthcare-pharmaceuticals/celltrion-unit-pays-330-million-eli-lilly-production-facility-filing-shows-2025-09-23/?utm_source=chatgpt.com "Celltrion unit pays $330 million for Eli Lilly production facility, filing shows"
