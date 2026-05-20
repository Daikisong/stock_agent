순서상 이번은 **R7 Loop 8 — 바이오·헬스케어·의료기기 가격경로 검증 라운드**다.

이번 라운드는 원시 수정주가 일봉 OHLC를 안정적으로 직접 추출하지 못한 종목에 대해 숫자를 지어내지 않고, **Reuters / Barron’s / WSJ / MarketWatch / Allure / arXiv**에 남은 가격 anchor, 이벤트 수익률, 매출·거래·임상·승인 수치로 계산 가능한 값만 계산했다.

```text
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

---

# 1. 이번 라운드 대섹터

```text
R7 = 바이오·헬스케어·의료기기
large_sector = BIOTECH_HEALTHCARE_DEVICE
round = R7 Loop 8 / price-path validation
```

R7의 기본 검증축은 `contract_backlog`, `capacity_utilization`, `approval`, `reimbursement`, `commercialization`, `dilution`, `privacy`다. R7은 CDMO, CRO, 바이오시밀러, GLP-1, 유전자치료, AI 신약, 의료AI, 원격의료, 의료기기, 진단, 동물헬스를 포함하지만, 핵심은 “승인·임상·논문이 좋다”가 아니라 **처방량·급여·매출·로열티·가동률·FCF가 확인되는가**다. 

Round 119 기준으로 R7에서 부족한 증거는 `approval_news`, `clinical_headline`이고, 필요한 증거는 `prescription_volume`, `reimbursement`, `commercial_revenue`, `cash_runway`, `royalty`다. Green blocker는 `commercialization_failure`, `dilution`, `approval_delay`다. 

---

# 2. 대상 canonical archetype

```text
BIOTECH_ROYALTY_COMMERCIALIZATION
SC_FORMULATION_ROYALTY_PLATFORM
KOREA_ONCOLOGY_DRUG_COMMERCIALIZATION
BIOSIMILAR_COMMERCIALIZATION
BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING
CDMO_HEALTHCARE_CONTRACT
CDMO_US_TARIFF_HEDGE_CAPACITY
VACCINE_CMO_RESTRUCTURING
BOTULINUM_US_MARKET_ENTRY
MEDICAL_DEVICE_HEALTHCARE_EXPORT
DIGITAL_HEALTHCARE_AI
MEDICAL_AI_EXTERNAL_VALIDATION
MEDICAL_AI_SUBGROUP_GENERALIZATION_RISK
APPROVAL_ONLY_NOT_COMMERCIALIZATION
MANUFACTURING_INSPECTION_CRL_OVERLAY
COMMERCIALIZATION_FAILURE_OVERLAY
```

이번 R7의 핵심 질문은 이거다.

```text
승인·논문·임상·M&A 테마인가?
아니면 처방·매출·로열티·가동률·마진·FCF가 실제로 이익 체급을 바꾸는가?
```

---

# 3. deep sub-archetype

```text
국산 신약 / 로열티:
- Yuhan lazertinib / Lazcluze
- J&J Rybrevant + Lazcluze
- EGFR NSCLC
- FDA approval
- prescription volume
- royalty recognition
- partner execution

SC formulation / royalty platform:
- Alteogen
- Merck Keytruda Qlex
- Keytruda patent cliff defense
- 30~40% patient conversion target
- enzyme IP / Halozyme dispute
- royalty visibility
- product sales ramp

CDMO / CMO:
- Samsung Biologics
- Celltrion
- SK Bioscience
- U.S. manufacturing site
- tariff hedge
- IDT Biologika acquisition
- GSK Rockville facility
- utilization / margin / capex

미용·보툴리눔:
- Hugel Letybo
- U.S. launch
- Botox competitor
- cheaper neuromodulator
- channel rollout
- pricing / competition

의료AI:
- Lunit INSIGHT DBT
- external validation
- AUC
- subgroup risk
- reimbursement / hospital adoption
```

---

# 4. 국장 신규 후보 case

## Case A — 알테오젠 `structural_success 후보 / SC royalty platform + 4B-watch`

```text
symbol = 196170
case_type = structural_success_candidate + 4B-watch
archetype = SC_FORMULATION_ROYALTY_PLATFORM / BIOTECH_ROYALTY_COMMERCIALIZATION
```

### evidence

2025년 3월 Reuters는 Merck가 Keytruda의 피하주사 제형을 2025년 10월 1일 미국에서 출시할 계획이며, FDA 승인 결정 목표일은 2025년 9월 23일이라고 보도했다. Merck는 피하주사 버전이 기존 30분 IV 주입 대비 훨씬 짧은 투여 시간을 제공하고, 출시 후 2년 안에 Keytruda 환자의 30~40%까지 전환될 수 있다고 기대했다. 이 제형에는 한국 알테오젠이 개발·제조하는 효소가 사용된다고 Reuters는 명시했다. ([Reuters][1])

2025년 9월 19일 Reuters는 FDA가 Merck의 피하주사 Keytruda 제형인 **Keytruda Qlex**를 승인했다고 보도했다. 기사에 따르면 Keytruda는 2024년 거의 300억 달러 매출을 올린 블록버스터이며, Qlex는 1~2분 내 피하 투여가 가능하고 Merck는 2년 내 30~40% adoption을 목표로 했다. ([Reuters][2])

MarketWatch는 Merck의 2025년 4분기 실적 보도에서 Keytruda Qlex가 2025년에 4,000만 달러 매출을 냈다고 정리했다. 이는 알테오젠 입장에서는 “승인 뉴스”에서 “초기 상업화 매출 발생”으로 올라가는 중요한 Stage 2→Stage 3 후보 evidence다. ([마켓워치][3])

반면 WSJ는 Keytruda Qlex에 사용되는 효소를 둘러싸고 Halozyme과 특허분쟁 가능성이 있다고 보도했고, 분석가들이 Qlex의 연매출 잠재력을 60억 달러 이상으로 봤다고 정리했다. 이는 알테오젠의 구조적 기회와 동시에 IP/legal 4C-watch를 만든다. ([월스트리트저널][4])

### stage date

```text
Stage 1:
2025-03-27
- Merck SC Keytruda launch plan
- Alteogen enzyme used in Keytruda SC formulation
- Keytruda patent cliff defense narrative

Stage 2:
2025-09-19
- FDA approves Keytruda Qlex
- Merck expects 30~40% adoption within two years
- Keytruda 2024 sales nearly $30B

Stage 3:
2026-02-xx 후보
- Keytruda Qlex 2025 sales $40M reported
- approval → launch → commercial revenue path begins
- 다만 알테오젠 royalty recognition / margin / cash receipt 확인 필요

Stage 4B:
Keytruda Qlex approval/launch 기대가 알테오젠 valuation에 과도 반영된 구간이면 후보
- 이번 pass에서는 한국 주가 OHLC anchor 확보 실패

Stage 4C-watch:
2025-03-05
- Halozyme patent dispute risk
- hard 4C 아님, legal/IP watch
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters / WSJ / MarketWatch evidence anchors

stage3_price:
price_data_unavailable_after_deep_search
- Reuters/WSJ/MarketWatch는 알테오젠 한국 주가 OHLC anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

Keytruda_2024_sales:
약 $30B

Keytruda_Qlex_2025_sales:
$40M

Qlex_sales_vs_Keytruda_2024_sales:
40M / 30B = 0.13%

Merck_target_conversion:
30~40% of Keytruda patients within two years

potential_Qlex_annual_sales_estimate_by_analysts:
>$6B per WSJ

potential_Qlex_sales_vs_Keytruda_2024_sales:
6B / 30B = 20%

MFE / MAE:
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

### 교정

알테오젠은 R7에서 `approval_news_only`가 아니라 **상업화 매출·로열티 인식**으로 Stage 3가 올라갈 수 있는 좋은 구조 후보다. 다만 한국 주가 OHLC가 이번 pass에서 직접 확보되지 않았기 때문에 `price_path_alignment`는 아직 partial이다.

---

## Case B — 유한양행 `success_candidate / FDA approval → royalty watch`

```text
symbol = 000100
case_type = success_candidate
archetype = KOREA_ONCOLOGY_DRUG_COMMERCIALIZATION / BIOTECH_ROYALTY_COMMERCIALIZATION
```

### evidence

2024년 8월 20일 Barron’s는 J&J가 FDA로부터 Rybrevant + Lazcluze 병용요법의 비소세포폐암 치료 승인을 받았다고 보도했다. 해당 병용요법은 AstraZeneca osimertinib 대비 질병 진행 또는 사망 위험을 30% 줄인 Phase 3 결과를 기반으로 했고, J&J 주가는 장전 0.4% 상승했다. ([Barron's][5])

Lazertinib은 유한양행이 개발한 EGFR TKI로, 2024년 8월 미국에서 Rybrevant와 병용요법으로 승인됐다. 공개 요약 기준 FDA 승인은 MARIPOSA 임상 858명 데이터를 기반으로 했고, 1차 치료 EGFR 변이 NSCLC 적응증에서 승인됐다. ([위키백과][6])

### stage date

```text
Stage 1:
2023~2024
- MARIPOSA data
- J&J partnership
- Lazertinib global commercialization 기대

Stage 2:
2024-08-20
- FDA approval for Rybrevant + Lazcluze
- Phase 3 data risk reduction 30%

Stage 3:
보류
- prescription volume
- J&J sales
- Yuhan royalty recognition
- EPS revision 확인 필요

Stage 4B:
FDA approval만으로 유한양행 주가가 과도하게 선반영된 구간이면 후보
- 한국 주가 OHLC anchor는 확보 실패

Stage 4C:
SC formulation CRL / launch delay / prescription underperformance / royalty shortfall 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Barron’s FDA approval / J&J event anchor + public drug approval summary

stage3_price:
N/A

stage2_price:
price_data_unavailable_after_deep_search
- Barron’s는 J&J premarket +0.4%만 제공하고 유한양행 한국 주가 anchor는 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

J&J_event_return:
+0.4% premarket

risk_reduction_vs_osimertinib:
30%

trial_size:
858 participants

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = FDA_approval_to_royalty_watch
stage_failure_type = stage2_watch_success
```

### 교정

유한양행은 R7에서 `approval` 점수는 올릴 수 있지만, Stage 3-Green은 늦게 줘야 한다.

```text
Stage 2:
FDA approval

Stage 3 조건:
prescription volume
partner product sales
royalty recognition
Yuhan EPS revision
```

---

## Case C — SK바이오사이언스 `success_candidate / CMO acquisition event premium`

```text
symbol = 302440
case_type = success_candidate + event_premium
archetype = CDMO_HEALTHCARE_CONTRACT / VACCINE_CMO_RESTRUCTURING
```

### evidence

2024년 6월 27일 Reuters는 SK바이오사이언스가 독일 CMO인 IDT Biologika 지분 60%를 3,390억 원, 약 2.44억 달러에 인수한다고 보도했다. 이 거래는 SK바이오사이언스의 2021년 IPO 이후 첫 대형 M&A였고, 발표 후 SK바이오사이언스 주가는 장중 11.7% 상승했다. ([Reuters][7])

같은 날 MarketWatch는 SK바이오사이언스 주가가 5.8% 상승해 52,200원에 도달했다고 별도 가격 anchor를 제공했다. ([마켓워치][8])

### stage date

```text
Stage 1:
2024년
- 코로나 이후 vaccine/CDMO 전환
- SK그룹 사업 포트폴리오 재편

Stage 2:
2024-06-27
- IDT Biologika 60% acquisition
- deal value 339B won
- global CMO production base

Stage 3:
없음
- M&A announcement만으로 Green 금지
- contract backlog, utilization, margin, integration cost, FCF 확인 필요

Stage 4B:
2024-06-27
- 발표 당일 +11.7% intraday / +5.8% to 52,200원
- event premium watch

Stage 4C:
integration failure, utilization underperformance, cash burn, new order failure 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters + MarketWatch reported event anchors

stage3_price:
N/A

stage2_event_price_anchor:
52,200원

MarketWatch_event_MFE_1D:
+5.8%

implied_prior_close:
52,200 / 1.058
= 약 49,338원

Reuters_intraday_event_MFE:
+11.7%

deal_value:
339B won

deal_value_usd:
$243.75M

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
partial_success
- M&A 발표일 가격 급등은 Stage 2 + 4B-watch로 처리해야 함.
```

### alignment

```text
score_price_alignment = success_candidate + event_premium
rerating_result = CMO_transition_watch
stage_failure_type = stage2_watch_success
```

### 교정

SK바이오사이언스는 R7에서 `M&A_for_CMO_transition`을 Stage 2로 인정하되, Stage 3는 **가동률·수주잔고·마진·FCF**로만 준다.

---

## Case D — 셀트리온 `success_candidate / U.S. tariff hedge manufacturing`

```text
symbol = 068270
case_type = success_candidate
archetype = BIOSIMILAR_COMMERCIALIZATION / BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING
```

### evidence

2025년 7월 29일 Reuters는 셀트리온이 미국 제약 관세 리스크를 줄이기 위해 미국 제조시설 인수 우선협상대상자로 선정됐다고 보도했다. 회사는 공장 인수와 운영에 7,000억 원, 약 5.04억 달러를 투자할 계획이라고 밝혔다. ([Reuters][9])

2025년 9월 23일 셀트리온 미국 자회사는 Eli Lilly로부터 ImClone Systems를 3.3억 달러에 인수한다고 공시했다. Reuters는 이 시설이 셀트리온의 미국 제품 라인과 향후 launch를 관세 노출로부터 보호하기 위한 목적이라고 정리했다. ([Reuters][10])

2025년 11월 19일 Reuters는 셀트리온이 미국 공장 증설에 최대 7,000억 원, 약 4.78억 달러를 투자할 계획이라고 보도했다. ([Reuters][11])

### stage date

```text
Stage 1:
2025-07-29
- U.S. pharma tariff hedge
- U.S. manufacturing site acquisition expectation

Stage 2:
2025-09-23
- ImClone Systems acquisition
- $330M transaction
- U.S. manufacturing base secured

Stage 3:
없음
- product transfer
- FDA/quality readiness
- utilization
- gross margin
- FCF 확인 필요

Stage 4B:
미국 현지화 기대로 주가가 먼저 과열된 구간이면 후보

Stage 4C:
integration delay, tariff policy reversal, capex burden, biosimilar pricing pressure 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters transaction / investment anchors

stage3_price:
N/A

stage2_price:
price_data_unavailable_after_deep_search
- Reuters는 셀트리온 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

initial_planned_investment:
700B won

ImClone_acquisition_value:
$330M

expansion_investment:
up to 700B won / $478.17M

USD_330M_KRW_equivalent_at_1463.9:
약 483.1B won

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = U.S._tariff_hedge_manufacturing_watch
stage_failure_type = stage2_watch_success
```

### 교정

셀트리온은 `U.S._manufacturing_tariff_hedge`를 Stage 2로 인정할 수 있지만, Stage 3는 **제품 이전·가동률·margin·FCF**가 확인된 뒤다.

---

## Case E — 삼성바이오로직스 `success_candidate / CDMO U.S. facility + valuation saturation watch`

```text
symbol = 207940
case_type = success_candidate + 4B-watch
archetype = CDMO_US_TARIFF_HEDGE_CAPACITY / CDMO_HEALTHCARE_CONTRACT
```

### evidence

2025년 12월 22일 Reuters는 삼성바이오로직스가 GSK로부터 미국 Rockville, Maryland의 Human Genome Sciences facility를 2.8억 달러에 인수한다고 보도했다. 이 시설은 60,000리터 drug substance capacity를 보유하고 있고, 삼성바이오로직스는 장기 미국 수요 대응과 기술 업그레이드를 위해 추가 투자를 계획했다. 발표 후 삼성바이오로직스 주가는 0.4% 하락해, 2% 오른 KOSPI를 언더퍼폼했다. ([Reuters][12])

### stage date

```text
Stage 1:
기존 CDMO success / 미국 생산 확대 기대

Stage 2:
2025-12-22
- GSK Rockville facility acquisition
- $280M deal
- 60,000L drug substance capacity

Stage 3:
보류
- 삼성바이오로직스는 기존 CDMO success benchmark지만,
  이 신규 facility 건은 utilization, contract transfer, margin 확인 전 Stage 3 아님

Stage 4B:
대형 CDMO 프리미엄이 이미 충분히 반영된 구간이면 후보

Stage 4C:
contract slowdown, utilization underperformance, capex overrun, tariff benefit reversal 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event return / capacity anchor

stage3_price:
N/A for new facility event

stage2_event_MAE_1D:
-0.4%

KOSPI_same_day_return:
+2.0%

relative_underperformance:
-0.4 - 2.0
= -2.4 percentage points

deal_value:
$280M

facility_capacity:
60,000L drug substance capacity

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate / evidence_good_but_price_failed
rerating_result = CDMO_US_capacity_watch
stage_failure_type = stage2_watch_success
```

### 교정

삼성바이오로직스는 CDMO가 structural E2R이 될 수 있음을 보여주는 대형 benchmark지만, 신규 미국 시설 인수 이벤트만으로 fresh Stage 3를 주면 안 된다. 이번 이벤트는 오히려 가격 반응이 약했다.

---

## Case F — 휴젤 `success_candidate / U.S. botulinum launch watch`

```text
symbol = 145020
case_type = success_candidate
archetype = BOTULINUM_US_MARKET_ENTRY / MEDICAL_DEVICE_HEALTHCARE_EXPORT
```

### evidence

2025년 3월 Allure는 Hugel의 Letybo가 미국에서 glabellar lines 치료용으로 FDA 승인을 받은 뒤 dermatologist office에 들어오기 시작했다고 보도했다. Letybo는 한국에서 Botulax로 널리 사용되어 왔고, Botox·Xeomin·Dysport·Daxxify·Jeuveau와 경쟁하는 새로운 neuromodulator로 설명됐다. ([Allure][13])

New York Post는 Letybo가 미국에서 Botox 대비 최대 30% 저렴할 수 있고, 단가가 Botox의 $12~18/unit 대비 $9~12/unit 수준일 수 있다고 보도했다. 이는 미국 시장 진입에서 pricing/distribution Stage 2 evidence가 될 수 있다. ([New York Post][14])

### stage date

```text
Stage 1:
2024
- Letybo FDA approval
- U.S. botulinum toxin market entry 기대

Stage 2:
2025-03-07
- Letybo U.S. dermatology office rollout
- Botox competitor narrative
- potential 30% cheaper pricing

Stage 3:
없음
- U.S. sales
- channel penetration
- ASP
- repeat order
- OPM 확인 전 Green 금지

Stage 4B:
승인·출시 뉴스만으로 휴젤 주가가 과열된 구간이면 후보

Stage 4C:
safety issue, pricing war, channel rollout failure, counterfeit/regulatory issue 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Allure / New York Post product launch evidence

stage3_price:
N/A

stage2_price:
price_data_unavailable_after_deep_search
- Allure/NYP는 휴젤 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

Letybo_pricing_estimate:
$9~12/unit

Botox_pricing_estimate:
$12~18/unit

potential_discount_range:
low-end comparison: 9/12 - 1 = -25%
high-end comparison: 12/18 - 1 = -33.3%

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

### 교정

휴젤은 `FDA approval + U.S. launch`가 Stage 2로는 강하지만 Stage 3는 매출·채널·가격·마진으로만 준다.

---

## Case G — 루닛 `insufficient_evidence / medical AI validation not commercialization`

```text
symbol = 328130
case_type = insufficient_evidence
archetype = DIGITAL_HEALTHCARE_AI / MEDICAL_AI_EXTERNAL_VALIDATION
```

### evidence

2025년 3월 arXiv 논문은 Lunit INSIGHT DBT 모델을 Emory EMBED 기반 163,449건 screening mammography exam에서 평가했고, 전체 AUC 0.91을 보였다고 보고했다. 다만 non-invasive cancer, calcification, dense breast tissue subgroup에서는 상대적으로 낮은 성능을 보였고, 연구진은 실제 임상 도입 시 세부 평가가 필요하다고 정리했다. ([arXiv][15])

### stage date

```text
Stage 1:
2023~2025
- 의료AI / 암진단 AI 테마

Stage 2:
2025-03-17
- external validation
- 163,449 DBT exams
- overall AUC 0.91
- subgroup risk identified

Stage 3:
없음
- external validation만으로 Green 금지
- reimbursement, hospital adoption, recurring revenue, cash runway 확인 필요

Stage 4B:
의료AI 테마로 주가가 먼저 급등하면 후보

Stage 4C:
reimbursement failure, subgroup performance issue, cash burn, adoption failure 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
arXiv clinical validation evidence

stage3_price:
N/A

stage2_price:
price_data_unavailable_after_deep_search
- arXiv 논문은 주가 anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

exam_count:
163,449

overall_AUC:
0.91

non_invasive_cancer_AUC:
0.85

calcification_AUC:
0.80

dense_breast_AUC:
0.90

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

### 교정

루닛은 R7에서 `external_validation`과 `commercialization`을 분리해야 한다. 논문 성능은 Stage 2 가능성이 있지만, Stage 3는 병원 도입·수가·반복매출·gross margin·cash runway가 필요하다.

---

# 5. 이번 R7 case별 요약표

| case      | 분류                                      |                                                               실제 가격검증 | alignment                      |
| --------- | --------------------------------------- | --------------------------------------------------------------------: | ------------------------------ |
| 알테오젠      | structural_success 후보                   |    Keytruda Qlex 2025 sales $40M, potential $6B+; 주가 OHLC unavailable | success_candidate              |
| 유한양행      | success_candidate                       |             FDA approval, J&J +0.4% premarket; Yuhan OHLC unavailable | success_candidate              |
| SK바이오사이언스 | success_candidate + event premium       |             +11.7% intraday / +5.8% to 52,200원; implied prior 49,338원 | event_premium + stage2         |
| 셀트리온      | success_candidate                       |          U.S. plant $330M, expansion up to 700B won; OHLC unavailable | success_candidate              |
| 삼성바이오로직스  | success_candidate / weak price response |     GSK facility $280M, 60,000L; 주가 -0.4%, KOSPI +2%, relative -2.4pp | evidence_good_but_price_failed |
| 휴젤        | success_candidate                       | Letybo U.S. launch, $9~12/unit vs Botox $12~18/unit; OHLC unavailable | success_candidate              |
| 루닛        | insufficient_evidence                   |                                163,449 exams, AUC 0.91, subgroup risk | stage2_evidence_not_green      |

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
  주가 -0.4%, KOSPI +2%

unknown_insufficient_evidence:
- 루닛
  external validation은 좋지만 reimbursement / revenue 전 Stage 3 아님

4B-watch:
- 알테오젠 Keytruda Qlex approval 기대가 주가에 과도 반영된 구간
- SK바이오사이언스 M&A 발표 당일 급등
- 바이오 approval / launch event 전반

4C-watch:
- 알테오젠 / Merck-Halozyme enzyme patent dispute
- 카테고리 공통: manufacturing inspection issue, commercialization delay, dilution, reimbursement failure

hard_4c_not_confirmed:
- 이번 pass에서 신뢰 가능한 한국 상장사 hard 4C를 확정할 enough source를 확보하지 못했다.
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

### 이유

알테오젠은 FDA approval에서 끝나지 않고 Keytruda Qlex 2025년 매출 $40M이라는 초기 상업화 evidence가 생겼다. 다만 알테오젠 로열티 인식과 cash receipt를 확인해야 Stage 3를 확정할 수 있다. ([마켓워치][3])

SK바이오사이언스는 IDT Biologika 인수 발표로 주가가 +11.7%까지 반응했지만, M&A만으로 Stage 3는 아니다. 가동률·수주잔고·마진이 필요하다. ([Reuters][7])

삼성바이오로직스는 미국 60,000L facility 인수에도 주가가 -0.4%로 KOSPI +2%를 언더퍼폼했다. 이건 “좋은 CDMO 뉴스도 이미 valuation에 반영되면 가격 반응이 약하다”는 4B/saturation 신호로 봐야 한다. ([Reuters][12])

## 내릴 축

```text
approval_news_only -5
clinical_headline_only -5
paper_validation_without_revenue -4
M&A_without_utilization -4
FDA_approval_without_commercial_sales -4
partner_peak_sales_without_royalty_visibility -3
pre_revenue_biotech_story -5
cash_burn_or_dilution_risk -5
manufacturing_inspection_issue -3
subgroup_performance_risk -3
```

### 이유

유한양행의 Lazcluze 승인과 휴젤의 Letybo 출시, 루닛의 외부검증은 모두 Stage 2로는 좋지만, 처방량·매출·로열티·급여·병원 도입 전 Stage 3는 아니다. ([Barron's][5])

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

이번 R7에서는 hard 4C를 억지로 확정하지 않았다. 특히 FDA CRL도 제조시설 이슈인지, 효능·안전성 이슈인지 분리해야 한다.

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

이번 세션에서 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉을 안정적으로 직접 확보하지 못했다. 대신 Reuters / Barron’s / WSJ / MarketWatch / Allure / arXiv의 evidence anchor와 이벤트 수익률을 사용해 계산 가능한 부분은 직접 계산했다.

---

# 9. patch-ready 출력

## docs/round/round_139.md 요약

```md
# R7 Loop 8. Biotech / Healthcare / Medical Device Price Validation

이번 라운드는 R7 price-validation 라운드다.

핵심 결론:
- 알테오젠은 Keytruda Qlex FDA approval과 2025년 $40M sales가 확인되어 SC royalty commercialization Stage 2→3 후보가 된다. 다만 알테오젠 로열티 인식과 cash receipt 확인 전 Stage 3 확정은 보류한다.
- 유한양행은 Rybrevant + Lazcluze FDA approval로 강한 Stage 2 후보지만, 처방량·J&J 매출·로열티 인식 전 Stage 3 금지다.
- SK바이오사이언스는 IDT Biologika 60% 인수 발표로 주가가 +11.7%까지 반응했지만, M&A 발표는 Stage 2 / event premium이다.
- 셀트리온은 미국 제조시설 인수와 증설로 tariff hedge Stage 2 후보지만, 제품 이전·가동률·margin·FCF 전 Stage 3 금지다.
- 삼성바이오로직스는 GSK Rockville facility 인수에도 주가 -0.4%, KOSPI +2%로 언더퍼폼했다. 좋은 CDMO 뉴스도 valuation saturation이 있으면 가격 반응이 약하다.
- 휴젤 Letybo는 U.S. launch Stage 2 후보지만, 미국 매출·채널·ASP·반복 주문 전 Green 금지다.
- 루닛은 외부검증 AUC 0.91이지만 reimbursement/hospital adoption/revenue 전 Stage 3가 아니다.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 139 R7 Loop 8 Biotech Healthcare Device Price Validation

## 반영 내용
- R7 Loop 8 price-validation 라운드를 추가했다.
- SC royalty platform, oncology drug commercialization, CDMO/CMO acquisition, U.S. botulinum launch, medical AI validation을 비교했다.
- Reuters/Barron's/WSJ/MarketWatch/Allure/arXiv reported anchors로 가능한 MFE/MAE 및 매출·거래 수치를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- commercial revenue, royalty recognition, prescription volume, reimbursement, utilization 가중치 강화
- approval-only, clinical-headline-only, M&A without utilization, paper validation without revenue 감점 강화
- patent/IP risk, manufacturing inspection, reimbursement failure 4C-watch 강화
```

## case row 초안

```jsonl
{"case_id":"r7_loop8_alteogen_keytruda_qlex_royalty_watch","symbol":"196170","company_name":"알테오젠","case_type":"success_candidate","primary_archetype":"SC_FORMULATION_ROYALTY_PLATFORM","stage1_date":"2025-03-27","stage2_date":"2025-09-19","stage3_date":"2026-02","stage4c_date":"2025-03-05","price_validation":{"price_data_source":"Reuters/WSJ/MarketWatch evidence anchors","stage3_price":null,"keytruda_2024_sales_usd_bn":30.0,"keytruda_qlex_2025_sales_usd_mn":40.0,"qlex_sales_vs_keytruda_2024_pct":0.13,"merck_target_conversion_pct":"30-40","potential_qlex_sales_usd_bn":6.0,"potential_qlex_sales_vs_keytruda_2024_pct":20.0,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"SC_royalty_commercialization_watch","notes":"Keytruda Qlex sales begin commercialization path; Alteogen royalty recognition and cash receipt required for Stage 3 confirmation."}
{"case_id":"r7_loop8_yuhan_lazcluze_approval_royalty_watch","symbol":"000100","company_name":"유한양행","case_type":"success_candidate","primary_archetype":"KOREA_ONCOLOGY_DRUG_COMMERCIALIZATION","stage2_date":"2024-08-20","price_validation":{"price_data_source":"Barron's / public drug approval summary","stage3_price":null,"jnj_event_return_premarket_pct":0.4,"risk_reduction_vs_osimertinib_pct":30,"trial_size":858,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"FDA_approval_to_royalty_watch","notes":"FDA approval is Stage 2; prescription volume, partner sales, Yuhan royalty and EPS revision required for Stage 3."}
{"case_id":"r7_loop8_sk_bioscience_idt_cmo_event","symbol":"302440","company_name":"SK바이오사이언스","case_type":"success_candidate","primary_archetype":"CDMO_HEALTHCARE_CONTRACT","stage2_date":"2024-06-27","stage4b_date":"2024-06-27","price_validation":{"price_data_source":"Reuters/MarketWatch reported event anchors","stage3_price":null,"stage2_event_price_anchor":52200,"marketwatch_event_mfe_1d_pct":5.8,"implied_prior_close":49338,"reuters_intraday_mfe_pct":11.7,"deal_value_krw_bn":339,"deal_value_usd_mn":243.75,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_event_premium","rerating_result":"CMO_transition_watch","notes":"IDT acquisition is Stage 2; utilization, backlog, margin and FCF required for Stage 3."}
{"case_id":"r7_loop8_celltrion_us_factory_tariff_hedge","symbol":"068270","company_name":"셀트리온","case_type":"success_candidate","primary_archetype":"BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING","stage1_date":"2025-07-29","stage2_date":"2025-09-23","price_validation":{"price_data_source":"Reuters transaction/investment anchors","stage3_price":null,"planned_investment_krw_bn":700,"imclone_acquisition_usd_mn":330,"imclone_acquisition_krw_bn":483.1,"expansion_investment_krw_bn":700,"expansion_investment_usd_mn":478.17,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"U.S._tariff_hedge_manufacturing_watch","notes":"U.S. facility is Stage 2; product transfer, utilization, margin and FCF required before Green."}
{"case_id":"r7_loop8_samsung_biologics_gsk_facility_saturation","symbol":"207940","company_name":"삼성바이오로직스","case_type":"success_candidate","primary_archetype":"CDMO_US_TARIFF_HEDGE_CAPACITY","stage2_date":"2025-12-22","price_validation":{"price_data_source":"Reuters reported event anchors","stage3_price":null,"stage2_event_mae_1d_pct":-0.4,"kospi_same_day_return_pct":2.0,"relative_underperformance_pp":-2.4,"deal_value_usd_mn":280,"facility_capacity_liters":60000,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"CDMO_US_capacity_watch","notes":"Good CDMO U.S. capacity event, but price reaction weak; utilization/contract transfer needed for fresh Stage 3."}
{"case_id":"r7_loop8_hugel_letybo_us_launch","symbol":"145020","company_name":"휴젤","case_type":"success_candidate","primary_archetype":"BOTULINUM_US_MARKET_ENTRY","stage2_date":"2025-03-07","price_validation":{"price_data_source":"Allure/New York Post product launch evidence","stage3_price":null,"letybo_unit_price_usd":"9-12","botox_unit_price_usd":"12-18","potential_discount_pct":"25-33.3","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"U.S._botulinum_launch_watch","notes":"U.S. Letybo rollout is Stage 2; U.S. sales, channel penetration, ASP and OPM required for Stage 3."}
{"case_id":"r7_loop8_lunit_medical_ai_validation_not_green","symbol":"328130","company_name":"루닛","case_type":"insufficient_evidence","primary_archetype":"MEDICAL_AI_EXTERNAL_VALIDATION","stage2_date":"2025-03-17","price_validation":{"price_data_source":"arXiv external validation evidence","stage3_price":null,"exam_count":163449,"overall_auc":0.91,"non_invasive_cancer_auc":0.85,"calcification_auc":0.80,"dense_breast_auc":0.90,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"unknown_insufficient_evidence","rerating_result":"medical_AI_validation_watch","notes":"External validation is Stage 2; reimbursement, hospital adoption, recurring revenue and cash runway required before Green."}
```

## shadow weight row 초안

```csv
archetype,commercial_revenue,royalty_recognition,prescription_volume,reimbursement,capacity_utilization,gross_margin,cash_runway,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
SC_FORMULATION_ROYALTY_PLATFORM,+5,+5,+3,+3,+0,+4,+3,-2,+5,+4,Alteogen needs royalty recognition/cash receipt after Keytruda Qlex sales begin.
KOREA_ONCOLOGY_DRUG_COMMERCIALIZATION,+5,+5,+5,+5,+0,+4,+4,-3,+4,+5,Yuhan FDA approval is Stage 2; prescription and royalty required for Stage 3.
CDMO_HEALTHCARE_CONTRACT,+4,+0,+0,+0,+5,+5,+4,-3,+4,+4,SK Bioscience M&A is Stage 2 until utilization/backlog/margin confirm.
BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING,+4,+0,+0,+1,+5,+5,+4,-2,+3,+4,Celltrion U.S. facility is Stage 2; product transfer/utilization/FCF required.
CDMO_US_TARIFF_HEDGE_CAPACITY,+4,+0,+0,+0,+5,+5,+4,-2,+4,+4,Samsung Biologics U.S. facility had weak price reaction; watch valuation saturation.
BOTULINUM_US_MARKET_ENTRY,+5,+0,+3,+3,+0,+5,+4,-3,+4,+4,Hugel U.S. launch is Stage 2 until channel sales and margin confirm.
MEDICAL_AI_EXTERNAL_VALIDATION,+2,+0,+0,+5,+0,+3,+5,-4,+5,+5,Lunit external validation is not Stage 3 without reimbursement/adoption/revenue.
```

---

# 이번 R7 Loop 8 결론

R7은 Stage 3를 가장 늦게 줘야 하는 섹터다.

```text
1. 알테오젠은 R7에서 가장 구조적인 후보 중 하나다.
   Keytruda Qlex가 FDA 승인 후 실제 2025년 매출 $40M을 냈기 때문이다.
   다만 알테오젠 로열티 인식과 cash receipt 확인 전 Stage 3 확정은 보류한다.

2. 유한양행은 FDA approval로 강한 Stage 2 후보지만,
   처방량·J&J 매출·로열티·EPS revision 전 Stage 3가 아니다.

3. SK바이오사이언스는 IDT 인수 발표로 +11.7%까지 반응했지만,
   M&A 발표는 Stage 2이자 event premium이다.

4. 셀트리온과 삼성바이오로직스의 미국 공장 인수는 tariff hedge Stage 2다.
   가동률·제품 이전·마진·FCF가 Stage 3 조건이다.

5. 휴젤 Letybo는 미국 출시가 Stage 2지만,
   미국 매출·채널 침투·ASP·반복 주문 전 Green 금지다.

6. 루닛은 외부검증 AUC 0.91이 있어도,
   수가·병원 도입·반복매출·cash runway 전에는 Stage 3가 아니다.

7. 이번 pass에서 신뢰 가능한 한국 상장사 hard 4C는 확정하지 않았다.
   R7 4C는 CRL, 임상 실패, 상업화 실패, 대규모 dilution, cash runway 붕괴처럼 원문과 날짜가 명확할 때만 확정해야 한다.
```

한 문장으로 압축하면:

> **R7에서 진짜 Stage 3는 “승인·임상·논문이 좋다”가 아니라, 처방·매출·로열티·수가·가동률·FCF로 돈이 실제로 들어오기 시작하는 순간이다.**
> **R7은 Stage 2 후보가 많지만, Stage 3-Green은 가장 보수적으로 줘야 한다.**

[1]: https://www.reuters.com/business/healthcare-pharmaceuticals/merck-plans-us-launch-subcutaneous-version-keytruda-october-1-2025-03-27/?utm_source=chatgpt.com "Merck plans to  launch US subcutaneous version of Keytruda on October 1"
[2]: https://www.reuters.com/business/healthcare-pharmaceuticals/us-fda-approves-mercks-new-injectable-version-keytruda-2025-09-19/?utm_source=chatgpt.com "US FDA approves Merck's injectable version of blockbuster cancer therapy Keytruda"
[3]: https://www.marketwatch.com/story/mercks-outlook-for-2026-comes-in-lower-than-expected-as-pipeline-faces-make-or-break-year-e797985f?utm_source=chatgpt.com "Merck's outlook for 2026 comes in below expectations as pipeline faces make-or-break year"
[4]: https://www.wsj.com/health/pharma/new-version-of-mercks-blockbuster-cancer-drug-threatened-by-patent-battle-b8509c95?utm_source=chatgpt.com "New Version of Merck's Blockbuster Cancer Drug Threatened by Patent Battle"
[5]: https://www.barrons.com/articles/johnson-johnson-fda-approval-acquisition-95d2ba8a?utm_source=chatgpt.com "Johnson & Johnson Gets FDA Approval for Treatment, Makes Acquisition of Up to $1.7 Billion"
[6]: https://en.wikipedia.org/wiki/Lazertinib?utm_source=chatgpt.com "Lazertinib"
[7]: https://www.reuters.com/markets/deals/south-koreas-sk-bioscience-buy-control-germanys-idt-biologika-244-mln-2024-06-27/?utm_source=chatgpt.com "South Korea's SK Bioscience to buy control of Germany's IDT Biologika for $244 mln"
[8]: https://www.marketwatch.com/story/sk-bioscience-shares-rise-5-8-to-krw52-200-ef6329cd?utm_source=chatgpt.com "SK Bioscience Shares Rise 5.8% to KRW52,200"
[9]: https://www.reuters.com/business/healthcare-pharmaceuticals/south-koreas-celltrion-says-tapped-buy-us-pharma-factory-offset-tariff-risk-2025-07-29/?utm_source=chatgpt.com "South Korea's Celltrion says tapped to buy US pharma factory to offset tariff risk"
[10]: https://www.reuters.com/business/healthcare-pharmaceuticals/celltrion-unit-pays-330-million-eli-lilly-production-facility-filing-shows-2025-09-23/?utm_source=chatgpt.com "Celltrion unit pays $330 million for Eli Lilly production facility, filing shows"
[11]: https://www.reuters.com/world/asia-pacific/celltrion-invest-up-478-mln-expand-us-factory-response-tariffs-2025-11-19/?utm_source=chatgpt.com "Celltrion to invest up to $478 mln to expand US factory in response to tariffs"
[12]: https://www.reuters.com/business/healthcare-pharmaceuticals/samsung-biologics-buy-us-drug-production-facility-gsk-280-mln-2025-12-21/?utm_source=chatgpt.com "Samsung Biologics to buy US drug production facility from GSK for $280 million"
[13]: https://www.allure.com/story/letybo-neuromodulator-injectable?utm_source=chatgpt.com "Everything You Need to Know About Letybo, the Newest Botox Competitor"
[14]: https://nypost.com/2025/03/12/lifestyle/botoxs-biggest-rival-lands-in-the-us-leytbo-said-to-be-faster-acting-and-up-to-30-cheaper/?utm_source=chatgpt.com "Botox's biggest rival lands in the US - Leytbo said to be faster-acting and up to 30% cheaper"
[15]: https://arxiv.org/abs/2503.13581?utm_source=chatgpt.com "Subgroup Performance of a Commercial Digital Breast Tomosynthesis Model for Breast Cancer Detection"
