좋아. 순서상 이번은 **R7 Loop 7 — 바이오·헬스케어·의료기기 가격경로 검증 라운드**로 진행한다.

이번 R7은 특히 조심해야 한다. 바이오는 **승인 뉴스, 임상 결과, FDA 이벤트, 기술수출, 로열티 기대**가 가격을 먼저 밀기 쉽다. 하지만 E2R Stage 3는 “승인받았다”가 아니라 **상업화 매출, 처방량, 보험·급여, 로열티, CMO 가동률, cash runway, dilution 통과**까지 내려와야 한다.

---

# 1. 이번 라운드 대섹터

```text
R7 = 바이오·헬스케어·의료기기
large_sector = BIOTECH_HEALTHCARE_DEVICE
round = R7 Loop 7 / price-path validation
목표 = Stage 3 / 4B / 4C가 실제 가격경로와 맞았는지 검증하고 shadow weight 보정
```

R7의 기본 영역은 CDMO, CRO, 바이오시밀러, GLP-1, 유전자치료제, AI 신약개발, 디지털헬스, 원격의료, 의료기기, 진단, 동물헬스다. Round 40 기준 R7 validation focus는 `contract_backlog`, `capacity_utilization`, `approval`, `reimbursement`, `commercialization`, `dilution`, `privacy`로 잡혀 있다. 

Round 119 기준으로 R7에서 부족한 증거는 `approval_news`, `clinical_headline`이고, 필요한 증거는 `prescription_volume`, `reimbursement`, `commercial_revenue`, `cash_runway`, `royalty`다. Green blocker는 `commercialization_failure`, `dilution`, `approval_delay`다. 

---

# 2. 대상 canonical archetype

```text
BIOTECH_ROYALTY_COMMERCIALIZATION
KOREA_ONCOLOGY_DRUG_COMMERCIALIZATION
BIOSIMILAR_COMMERCIALIZATION
BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING
CDMO_HEALTHCARE_CONTRACT
CDMO_US_TARIFF_HEDGE_CAPACITY
MEDICAL_DEVICE_HEALTHCARE_EXPORT
BOTULINUM_US_MARKET_ENTRY
DIGITAL_HEALTHCARE_AI
MEDICAL_AI_EXTERNAL_VALIDATION
MEDICAL_AI_SUBGROUP_GENERALIZATION_RISK
APPROVAL_ONLY_NOT_COMMERCIALIZATION
REIMBURSEMENT_ACCESS_OVERLAY
COMMERCIALIZATION_FAILURE_OVERLAY
MANUFACTURING_INSPECTION_CRL_OVERLAY
```

이번 R7의 핵심 질문은 이거다.

```text
이 회사는 승인·임상·기술수출 테마주인가?
아니면 처방·보험·매출·로열티·CMO 가동률·FCF로 실제 이익 체급이 바뀌는 회사인가?
```

---

# 3. deep sub-archetype

```text
국산 신약 / 로열티:
- lazertinib / Leclaza / Lazcluze
- J&J Rybrevant combo
- EGFR-mutated NSCLC
- FDA approval
- commercial launch
- prescription volume
- royalty stream
- partner execution risk

바이오시밀러 / 미국 현지화:
- Celltrion biosimilar portfolio
- U.S. manufacturing facility
- tariff hedge
- product launch protection
- capacity expansion
- margin / FCF
- biosimilar competition

CDMO / CMO:
- Samsung Biologics
- SK Bioscience / IDT Biologika
- U.S. facility acquisition
- German vaccine CMO
- contract backlog
- utilization
- capex burden
- tariff hedge

미용·의료기기:
- Hugel Letybo
- Botulax / botulinum toxin
- U.S. FDA approval
- U.S. launch
- Botox competitor
- channel rollout
- price competition
- counterfeit / safety risk

의료AI:
- Lunit INSIGHT
- breast / chest AI
- external validation
- reimbursement
- hospital adoption
- revenue conversion
- subgroup performance risk
```

---

# 4. 국장 신규 후보 case

## Case A — 유한양행 `success_candidate / royalty-commercialization watch`

```text
symbol = 000100
archetype = BIOTECH_ROYALTY_COMMERCIALIZATION / KOREA_ONCOLOGY_DRUG_COMMERCIALIZATION
case_type = success_candidate
```

유한양행은 R7에서 “승인 뉴스는 강하지만 Stage 3는 처방·로열티까지 기다려야 하는” 케이스다. 2024년 8월 FDA는 J&J의 Rybrevant와 lazertinib 병용요법을 EGFR 변이 비소세포폐암 1차 치료로 승인했다. Reuters는 이 조합이 AstraZeneca의 Tagrisso 대비 질병 진행 없이 사는 기간을 늘린 late-stage study 데이터에 기반했고, J&J가 Rybrevant peak sales를 50억 달러 이상으로 기대한다고 보도했다. ([Reuters][1])

다만 2024년 12월 FDA는 Rybrevant 피하주사 제형을 승인하지 않았고, 그 사유는 임상 효능·안전성 문제가 아니라 제조시설 사전점검 관련 이슈였다. 기존 IV 제형은 영향을 받지 않았고 추가 임상시험도 요구되지 않았다고 Reuters는 보도했다. 그래서 이건 hard 4C가 아니라 `commercial convenience delay / manufacturing-inspection watch` 정도로 처리해야 한다. ([Reuters][2])

### stage date 후보

```text
Stage 1:
2023~2024
- MARIPOSA 데이터 / EGFR NSCLC 신약 기대
- J&J 파트너십 / 글로벌 상업화 기대

Stage 2:
2024-08-20
- FDA 승인
- Rybrevant + lazertinib 1차 치료 승인
- J&J launch 준비

Stage 3:
보류
- 실제 처방량, 매출, 유한양행 로열티 인식, EPS revision 확인 필요

Stage 4B:
승인 이후 주가가 대형 rerating을 받았고 로열티 기대가 과도하게 선반영되면 후보

Stage 4C:
2024-12-16은 hard 4C 아님
- SC 제형 제조시설 CRL watch
- IV 제형 승인과 효능 데이터는 유지
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2024-08-20 OHLC backfill 필요.

MFE_30D / 90D / 180D / 1Y / 2Y:
Stage 2 기준 backfill 필요.

MAE_30D / 90D / 180D / 1Y:
Stage 2 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = success_candidate
rerating_result = commercialization_watch
stage_failure_type = stage2_watch_success 후보
```

### 교정 포인트

유한양행은 R7에서 `approval` 점수를 올려줄 수 있지만, Stage 3-Green은 늦게 줘야 한다.

```text
FDA approval:
Stage 2 강한 증거

Stage 3 조건:
처방량
J&J 매출
로열티 인식
유한양행 EPS revision
SC 제형/편의성 확장 리스크 통과
```

---

## Case B — 휴젤 `success_candidate / U.S. launch watch`

```text
symbol = 145020
archetype = BOTULINUM_US_MARKET_ENTRY / MEDICAL_DEVICE_HEALTHCARE_EXPORT
case_type = success_candidate
```

휴젤은 R7 미용의료/보툴리눔 쪽에서 좋은 Stage 2 후보야. Hugel의 Letybo는 미국 FDA 승인을 받은 뒤 2025년 미국 피부과 시장에 본격 등장했고, 미국 매체들은 Letybo가 Botox, Xeomin, Dysport, Daxxify, Jeuveau와 경쟁하는 신규 neuromodulator라고 설명했다. Allure는 Letybo가 한국에서 Botulax로 널리 쓰여온 제품이고, 미국에서는 glabellar lines 치료용으로 승인되어 의사 오피스에 들어오기 시작했다고 보도했다. ([Allure][3])

다만 이건 아직 Stage 3 확정이 아니다. 미국 출시 자체는 Stage 2지만, 실제 Stage 3는 미국 유통망, 시술 채널 penetration, ASP, 마진, 소송·안전 리스크, 반복 주문이 확인되어야 한다.

### stage date 후보

```text
Stage 1:
2024
- Letybo FDA approval / U.S. Botox competitor narrative

Stage 2:
2025-03
- Letybo 미국 시장 진입 / 피부과 오피스 도입 시작
- Botox competitor로 언급

Stage 3:
보류
- 미국 매출, ASP, channel penetration, OPM, repeat order 확인 필요

Stage 4B:
미국 승인·출시 뉴스만으로 주가가 먼저 과열됐다면 후보

Stage 4C:
없음
- 단, 안전성 이슈, counterfeit confusion, 가격경쟁 심화, 소송 리스크 발생 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2025-03 출시/보도 구간 OHLC backfill 필요.

MFE / MAE:
Stage 2 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = success_candidate
rerating_result = U.S._commercialization_watch
stage_failure_type = stage2_watch_success 후보
```

### 교정 포인트

휴젤은 R7에서 `approval + U.S. launch`가 Stage 2로는 강하지만, Stage 3는 매출로 내려와야 한다.

```text
올릴 축:
FDA approval
U.S. launch
channel rollout
repeat treatment demand

내릴 축:
approval_only
price_competition
safety_or_counterfeit_risk
U.S._sales_absent
```

---

## Case C — 셀트리온 `success_candidate / U.S. tariff hedge manufacturing`

```text
symbol = 068270
archetype = BIOSIMILAR_COMMERCIALIZATION / BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING
case_type = success_candidate
```

셀트리온은 R7에서 바이오시밀러 상업화와 미국 현지 생산 hedge를 보는 케이스다. 2025년 7월 셀트리온은 미국 제약 관세 리스크를 줄이기 위해 미국 내 제조시설 인수 우선협상대상자로 선정됐다고 밝혔다. 당시 회사는 인수·운영에 약 7,000억 원을 투자할 계획이라고 했고, 관세 정책 변화에 따라 추가 투자 가능성도 열어뒀다. ([Reuters][4])

이후 2025년 9월 셀트리온 미국 자회사는 Eli Lilly의 ImClone Systems를 3.3억 달러에 인수한다고 공시했고, Reuters는 이 시설이 미국 제품 라인과 향후 launch를 관세 노출로부터 보호하기 위한 목적이라고 설명했다. 2025년 11월에는 미국 공장 확장에 최대 7,000억 원을 투자하겠다고 발표했다. ([Reuters][5])

### stage date 후보

```text
Stage 1:
2025-07-29
- 미국 의약품 관세 리스크
- 미국 생산기지 확보 기대

Stage 2:
2025-09-23
- ImClone Systems 인수 공시
- 미국 제조시설 확보

Stage 3:
보류
- 실제 제품 이전, 가동률, 원가 절감, tariff hedge 효과, FCF 확인 필요

Stage 4B:
미국 현지화 기대가 가격에 과도하게 선반영되면 후보

Stage 4C:
없음
- 단, 인수 후 capex burden, 통합 지연, tariff policy reversal, biosimilar 가격경쟁 심화 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2025-09-23 OHLC backfill 필요.

MFE / MAE:
Stage 2 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = success_candidate
rerating_result = tariff_hedge_watch
stage_failure_type = stage2_watch_success 후보
```

### 교정 포인트

셀트리온은 `U.S. facility acquisition`이 좋은 Stage 2지만, Stage 3는 아직 아니다.

```text
Stage 3 조건:
제품 이전
FDA/quality readiness
가동률
관세 절감 효과
gross margin
FCF
바이오시밀러 가격경쟁 통과
```

---

## Case D — SK바이오사이언스 `success_candidate / CMO acquisition watch`

```text
symbol = 302440
archetype = CDMO_HEALTHCARE_CONTRACT / VACCINE_CMO_RESTRUCTURING
case_type = success_candidate
```

SK바이오사이언스는 코로나 백신 일회성 이후 CMO/글로벌 생산기지 전환을 보는 케이스다. 2024년 6월 회사는 독일 제약 CMO인 IDT Biologika의 지분 60%를 3,390억 원, 약 2.44억 달러에 인수한다고 밝혔다. Reuters는 이 거래가 SK바이오사이언스의 2021년 IPO 이후 첫 대형 M&A이며, 발표 당일 주가가 장중 11.7% 올랐다고 보도했다. ([Reuters][6])

다만 이 역시 Stage 3가 아니다. 코로나 백신 일회성 매출 이후 CMO 전환이 실제로 성공하려면 IDT의 수주잔고, 가동률, 고객, margin, integration cost, FCF가 확인되어야 한다.

### stage date 후보

```text
Stage 1:
2024
- 코로나 이후 백신/CMO 사업 재편 기대

Stage 2:
2024-06-27
- IDT Biologika 60% 인수
- 글로벌 CMO 생산기지 확보

Stage 3:
보류
- contract backlog, utilization, margin, integration cost 확인 필요

Stage 4B:
M&A 발표 직후 +11.7%는 event premium 성격
- 단기 4B-watch 후보

Stage 4C:
없음
- 단, 인수 후 실적 기여 부진, 통합 비용, cash burn, 신규 수주 실패 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2024-06-27 OHLC backfill 필요.

MFE / MAE:
Stage 2 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = success_candidate / event_premium_watch
rerating_result = unknown
stage_failure_type = stage2_watch_success 후보
```

### 교정 포인트

SK바이오사이언스는 R7에서 `M&A for CMO transition`을 Stage 2로 인정하되, Stage 3는 가동률과 계약으로만 준다.

---

## Case E — 삼성바이오로직스 `4B-benchmark / U.S. capacity watch`

```text
symbol = 207940
archetype = CDMO_US_TARIFF_HEDGE_CAPACITY / CDMO_HEALTHCARE_CONTRACT
case_type = 4B-benchmark / success_candidate
```

삼성바이오로직스는 기존 대표 CDMO 성공사례라 이번 신규 success case로 반복하지는 않는다. 대신 **R7 CDMO 4B benchmark**로 둔다. 2025년 12월 삼성바이오로직스는 GSK로부터 미국 Rockville, Maryland의 Human Genome Sciences 시설을 2.8억 달러에 인수한다고 밝혔다. Reuters는 이 시설의 drug substance capacity가 60,000리터이고, 삼성바이오로직스가 미국 장기 수요 대응과 생산능력 확대를 위해 추가 투자를 계획한다고 보도했다. ([Reuters][7])

이건 좋은 Stage 2~3 증거가 될 수 있지만, 삼성바이오로직스는 이미 시장이 CDMO 프리미엄을 잘 알고 있는 대형주다. 따라서 신규 Stage 3보다 4B-watch 기준점으로 쓰는 게 더 맞다.

### stage date 후보

```text
Stage 1:
이미 과거 CDMO structural success 구간

Stage 2:
2025-12-22
- 미국 생산시설 인수
- 60,000L drug substance capacity
- 미국 수요 대응 / tariff hedge

Stage 3:
기존 success anchor
- 이번 라운드에서는 신규 Stage 3로 쓰지 않음

Stage 4B:
대형 CDMO 프리미엄이 이미 충분히 반영된 구간이면 4B-watch

Stage 4C:
없음
- 단, 대형 계약 둔화, 가동률 하락, capex 과잉, tariff benefit reversal 시 후보
```

### 가격경로 검증

```text
stage3_price:
기존 CDMO case-library backfill 대상.

stage2_price:
2025-12-22 OHLC backfill 필요.

MFE / MAE:
기존 Stage 3와 신규 U.S. facility Stage 2를 분리해 backfill 필요.

below_stage3_price_flag:
기존 case backfill 필요.

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = aligned benchmark
rerating_result = true_rerating / 4B-watch
stage_failure_type = green_success benchmark
```

### 교정 포인트

삼성바이오로직스는 R7에서 CDMO가 진짜 structural E2R이 될 수 있음을 보여주지만, 지금은 신규 Stage 3보다 **valuation saturation / capex return / utilization**을 봐야 한다.

---

## Case F — 루닛 `insufficient_evidence / medical-AI external-validation watch`

```text
symbol = 328130
archetype = DIGITAL_HEALTHCARE_AI / MEDICAL_AI_EXTERNAL_VALIDATION / MEDICAL_AI_SUBGROUP_GENERALIZATION_RISK
case_type = insufficient_evidence / evidence_good_but_price_unproven
```

루닛은 R7에서 의료AI를 Stage 3로 너무 쉽게 올리지 말라는 케이스다. 2025년 arXiv에 공개된 Emory EMBED 기반 연구는 Lunit INSIGHT DBT 모델을 163,449건의 screening mammography exam에 대해 평가했고, 전체 AUC 0.91을 보였지만, non-invasive cancer, calcification, dense breast tissue에서는 상대적으로 낮은 성능을 보였다고 보고했다. 즉 외부검증 자체는 의미 있지만, subgroup risk도 동시에 존재한다. ([arXiv][8])

이건 Stage 2 evidence로는 좋다. 하지만 Stage 3는 병원 도입, 보험/수가, 반복매출, ARR, gross margin, cash burn 안정이 확인되어야 한다.

### stage date 후보

```text
Stage 1:
2023~2025
- 의료AI / 암진단 AI 테마

Stage 2:
2025-03-17
- 외부 데이터셋 기반 Lunit INSIGHT DBT 성능 평가
- 전체 AUC 0.91
- subgroup 성능 리스크도 확인

Stage 3:
없음
- 임상 성능 검증만으로는 매출 체급 변화 아님
- reimbursement / hospital adoption / recurring revenue 필요

Stage 4B:
의료AI 테마로 주가가 먼저 급등하면 후보

Stage 4C:
subgroup performance issue, reimbursement failure, regulatory/clinical adoption failure, cash burn 증가 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2025-03-17 기준 OHLC backfill 필요.

MFE / MAE:
Stage 2 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = unknown_insufficient_evidence
rerating_result = medical_AI_watch
stage_failure_type = stage2_evidence_not_green
```

### 교정 포인트

루닛은 R7에서 `external_validation`과 `commercialization`을 분리해야 한다.

```text
외부검증:
Stage 2 가능

Stage 3 조건:
병원 도입
수가 / 보험
반복매출
ARR
gross margin
cash runway
subgroup risk 관리
```

---

## Case G — hard 4C 후보: 이번 pass에서는 확정 보류

```text
case_type = 4C-thesis-break
status = insufficient_reliable_source_in_this_pass
```

R7에는 원래 HLB류 FDA CRL, 임상 실패, 상업화 실패, 허가 지연 같은 hard 4C가 매우 중요하다. 다만 이번 pass에서 신뢰할 만한 1차·주요 외신 source를 충분히 묶지 못했기 때문에, 억지로 특정 종목을 hard 4C로 확정하지 않는다.

이번 라운드에서 확인 가능한 4C 성격의 리스크는 다음처럼 “watch”로만 둔다.

```text
유한양행 / J&J combo:
SC 제형 CRL은 manufacturing inspection issue.
효능·안전성 thesis break 아님.
=> hard 4C 아님, commercialization delay watch.

루닛:
subgroup performance risk.
=> hard 4C 아님, adoption/reimbursement watch.

SK바이오사이언스:
M&A 후 integration / utilization 실패 가능성.
=> 아직 hard 4C 아님.

휴젤:
U.S. Botox competitor launch는 Stage 2.
=> 안전성·가격경쟁·유통 실패가 나오기 전 hard 4C 아님.
```

이렇게 보류하는 게 R7에서는 맞다. 바이오는 “실패했다”는 말을 너무 쉽게 붙이면 안 된다. FDA CRL, 임상 실패, cash runway 붕괴, 대규모 dilution, 상업화 실패가 날짜와 원문으로 확인될 때만 4C로 확정해야 한다.

---

# 5. 이번 R7 case별 요약표

| case      | 분류                              |        Stage 3 판정 |                       4B/4C 판정 | 가격경로 1차 판단                          |
| --------- | ------------------------------- | ----------------: | -----------------------------: | ----------------------------------- |
| 유한양행      | success_candidate               |                보류 |          SC 제형 CRL은 hard 4C 아님 | FDA 승인은 Stage 2, 로열티 전 Stage 3 금지   |
| 휴젤        | success_candidate               |                보류 |      U.S. launch 과열 시 4B-watch | FDA 승인·출시는 Stage 2, 미국 매출 확인 필요     |
| 셀트리온      | success_candidate               |                보류 | U.S. facility 기대 과열 시 4B-watch | 관세 hedge는 Stage 2, margin/FCF 확인 필요 |
| SK바이오사이언스 | success_candidate / event watch |                보류 |   M&A 발표 +11.7%는 event premium | IDT 인수는 Stage 2, 가동률 전 Green 금지     |
| 삼성바이오로직스  | 4B-benchmark                    | 기존 success anchor |        CDMO valuation 4B-watch | 신규 Stage 3보다 saturation 감시          |
| 루닛        | insufficient_evidence           |                없음 |          의료AI 테마 과열 시 4B-watch | 외부검증은 Stage 2, 상업화 전 Green 금지       |
| hard 4C   | 보류                              |               N/A |                          확정 보류 | reliable source 부족 시 억지 4C 금지       |

---

# 6. 각 case별 stage date 후보 요약

```text
유한양행:
Stage 1 = 2023~2024 MARIPOSA / J&J combo 기대
Stage 2 = 2024-08-20 FDA 승인
Stage 3 = 보류 / 처방량·로열티·EPS revision 필요
Stage 4B = 승인 후 로열티 기대 과열 시 후보
Stage 4C = 2024-12-16 SC 제형 CRL watch, hard 4C 아님

휴젤:
Stage 1 = 2024 Letybo FDA approval
Stage 2 = 2025-03 U.S. launch / Botox competitor narrative
Stage 3 = 보류 / 미국 매출·ASP·채널 penetration 필요
Stage 4B = 승인·출시 뉴스 과열 시 후보
Stage 4C = 안전성·소송·가격경쟁 심화 시 후보

셀트리온:
Stage 1 = 2025-07 U.S. tariff hedge facility 기대
Stage 2 = 2025-09-23 ImClone Systems 인수
Stage 3 = 보류 / 제품 이전·가동률·margin·FCF 필요
Stage 4B = 미국 현지화 기대 과열 시 후보
Stage 4C = integration delay / capex burden / tariff reversal 시 후보

SK바이오사이언스:
Stage 1 = 코로나 이후 CMO 전환 기대
Stage 2 = 2024-06-27 IDT Biologika 60% 인수
Stage 3 = 보류 / 수주잔고·가동률·margin 필요
Stage 4B = M&A 발표 직후 event premium 후보
Stage 4C = 통합 실패·cash burn·수주 실패 시 후보

삼성바이오로직스:
Stage 1 = 기존 CDMO success
Stage 2 = 2025-12-22 미국 GSK facility 인수
Stage 3 = 기존 success anchor, 신규 Stage 3 아님
Stage 4B = CDMO valuation saturation 후보
Stage 4C = 계약 둔화·가동률 하락·capex 과잉 시 후보

루닛:
Stage 1 = 의료AI 테마
Stage 2 = 2025-03-17 외부검증 논문
Stage 3 = 없음 / 상업화·수가·반복매출 필요
Stage 4B = 의료AI 테마 급등 시 후보
Stage 4C = reimbursement failure / subgroup risk / cash burn 시 후보
```

---

# 7. 가격경로 검증

R7은 정확한 OHLC backfill 없이 수익률을 확정하면 안 된다. 특히 바이오는 FDA 승인일, CRL일, 논문 공개일, M&A 발표일, 실적발표일을 분리해야 한다.

| case      |         stage3_price | MFE/MAE                           | below_stage3   | peak/drawdown                |
| --------- | -------------------: | --------------------------------- | -------------- | ---------------------------- |
| 유한양행      |           Stage 3 없음 | FDA 승인 Stage 2 기준 backfill        | N/A            | 승인 후 royalty 기대 peak 필요      |
| 휴젤        |           Stage 3 없음 | U.S. launch Stage 2 기준 backfill   | N/A            | Letybo launch 이후 drawdown 필요 |
| 셀트리온      |           Stage 3 없음 | U.S. facility Stage 2 기준 backfill | N/A            | tariff hedge 기대 peak 필요      |
| SK바이오사이언스 |           Stage 3 없음 | IDT 인수 기준 backfill                | N/A            | M&A event fade 확인 필요         |
| 삼성바이오로직스  | 기존 Stage 3 benchmark | 기존 case backfill 필요               | needs backfill | CDMO 4B peak 필요              |
| 루닛        |           Stage 3 없음 | 외부검증 논문 기준 backfill               | N/A            | 의료AI 테마 peak/drawdown 필요     |

핵심은 이거다.

```text
R7에서 Stage 3는 승인일이 아니라 상업화 숫자가 확인되는 날이다.
승인·논문·M&A는 대부분 Stage 2까지만 준다.
```

---

# 8. score-price alignment 판정

```text
유한양행:
alignment = success_candidate
FDA approval은 강하지만 prescription/royalty 전 Stage 3 금지.

휴젤:
alignment = success_candidate
U.S. launch는 강한 Stage 2.
매출·채널·ASP 확인 전 Green 금지.

셀트리온:
alignment = success_candidate
U.S. facility acquisition은 tariff hedge Stage 2.
가동률·margin·FCF 전 Green 금지.

SK바이오사이언스:
alignment = event_premium_watch
IDT 인수는 CMO 전환 후보지만 발표 당일 +11.7%는 event premium 성격.

삼성바이오로직스:
alignment = aligned benchmark
단, 신규 Stage 3보다 4B/saturation 감시.

루닛:
alignment = unknown_insufficient_evidence
external validation은 좋지만 reimbursement/revenue 전 Stage 3 아님.
```

---

# 9. 점수비중 교정

## 올릴 축

```text
commercial_revenue +5
prescription_volume +5
royalty_recognition +5
reimbursement_access +4
contract_backlog +4
capacity_utilization +4
gross_margin_visibility +4
cash_runway +4
U.S._commercial_launch_with_sales +3
external_validation_with_adoption +3
```

R7에서 제일 중요한 건 “과학적으로 가능하다”가 아니라 **돈으로 바뀌었는가**다. 임상·승인·논문은 문을 여는 열쇠고, Stage 3는 그 문을 지나 실제 매출이 복도로 이어질 때다.

## 내릴 축

```text
approval_news_only -5
clinical_headline_only -5
paper_validation_without_revenue -4
M&A_without_utilization -3
FDA_approval_without_reimbursement -4
partner_peak_sales_without_royalty_visibility -3
pre_revenue_biotech_story -5
cash_burn_or_dilution_risk -5
manufacturing_inspection_issue -3
subgroup_performance_risk -3
```

유한양행, 휴젤, 루닛, SK바이오사이언스가 이 감점축을 요구한다.

## Green gate 강화 조건

R7 Stage 3-Green은 앞으로 이렇게 줘야 한다.

```text
필수 gate:
1. approval 또는 regulatory clearance
2. commercial launch
3. prescription volume 또는 hospital adoption
4. reimbursement / insurance / payer access
5. revenue recognition
6. royalty 또는 gross margin 확인
7. cash runway / dilution risk 통과
8. partner execution risk 통과
9. price path가 증거 이후 따라왔는지 확인

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
로열티 기대가 처방량보다 먼저 가격에 반영
CDMO capacity premium이 가동률보다 먼저 확장
의료AI 논문/인허가로 주가만 급등
M&A 발표 당일 급등
파트너 peak sales 숫자만 반복

4B-elevated:
launch가 시작됐지만 처방 증가가 느림
보험/급여 접근이 제한적
CDMO capex가 계약보다 빠름
경쟁약 출시
가격경쟁 심화
cash burn이 계속됨

4B-graduated:
승인 이후 매출 ramp가 기대보다 느림
로열티가 컨센서스를 못 따라감
좋은 뉴스에도 주가 반응 둔화
```

## 4C hard gate 조건

```text
FDA CRL / 허가 거절
단, 제조시설 issue와 efficacy/safety issue는 분리
임상 실패
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
```

특히 R7에서는 CRL을 무조건 hard 4C로 처리하면 안 된다.

```text
efficacy/safety CRL:
hard 4C 가능

manufacturing inspection CRL:
commercialization delay watch
추가 임상 요구 없음이면 hard 4C 아님
```

유한양행/J&J SC 제형 이슈가 이 구분의 좋은 예다.

---

# 10. shadow-only 기록

이번 R7 Loop 7은 production scoring에 바로 반영하면 안 된다.

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
needs_ohlc_backfill = true
hard_4c_confirmed = false in this pass
```

레포에 넣는다면 파일명은 이렇게 가는 게 자연스럽다.

```text
docs/round/round_126.md
docs/checkpoints/checkpoint_28a_round126_r7_loop7_biotech_healthcare_device_price_validation.md
src/e2r/sector/round126_r7_loop7_biotech_healthcare_device.py
data/e2r_case_library/cases_r7_loop7_round126.jsonl
data/sector_taxonomy/score_weight_profiles_round126_r7_loop7_v7.csv
output/e2r_round126_r7_loop7_biotech_healthcare_device/
```

---

# 이번 R7 Loop 7 결론

R7은 Stage 3를 매우 늦게 줘야 한다.
이 섹터에서 가격은 승인 뉴스에 민감하게 먼저 움직이지만, 진짜 E2R은 **상업화 숫자**가 나온 뒤에야 확인된다.

이번 라운드의 핵심 교정은 이거다.

```text
1. FDA 승인은 강한 Stage 2지만 Stage 3가 아니다.
   처방량·매출·로열티·EPS revision이 필요하다.

2. 보툴리눔·의료기기 미국 진출은 Stage 2 후보지만,
   미국 채널 침투와 매출 확인 전 Green 금지다.

3. 바이오시밀러와 CDMO의 미국 공장 인수는 좋은 구조 후보지만,
   가동률·margin·FCF가 확인되어야 Stage 3다.

4. 의료AI는 외부검증만으로 Green 금지다.
   병원 도입·수가·반복매출·cash runway가 필요하다.

5. R7의 4C는 신중하게 확정해야 한다.
   FDA CRL도 제조시설 이슈인지, 효능·안전성 이슈인지 분리해야 한다.
```

한 문장으로 압축하면:

> **R7에서 진짜 Stage 3는 “승인·임상·논문이 좋다”가 아니라, 처방·보험·매출·로열티·가동률·FCF로 이익 체급이 바뀌는 순간이다.**
> **R7은 Stage 2 후보가 많지만, Stage 3-Green은 가장 엄격하게 줘야 한다.**

[1]: https://www.reuters.com/business/healthcare-pharmaceuticals/us-fda-approves-jjs-combination-therapy-type-lung-cancer-2024-08-20/?utm_source=chatgpt.com "US FDA approves J&J's chemotherapy-free treatment for lung cancer"
[2]: https://www.reuters.com/business/healthcare-pharmaceuticals/us-fda-declines-approve-injection-form-jjs-lung-cancer-drug-2024-12-16/?utm_source=chatgpt.com "US FDA declines to approve injection form of J&J's lung cancer drug"
[3]: https://www.allure.com/story/letybo-neuromodulator-injectable?utm_source=chatgpt.com "Everything You Need to Know About Letybo, the Newest Botox Competitor"
[4]: https://www.reuters.com/business/healthcare-pharmaceuticals/south-koreas-celltrion-says-tapped-buy-us-pharma-factory-offset-tariff-risk-2025-07-29/?utm_source=chatgpt.com "South Korea's Celltrion says tapped to buy US pharma factory to offset tariff risk"
[5]: https://www.reuters.com/business/healthcare-pharmaceuticals/celltrion-unit-pays-330-million-eli-lilly-production-facility-filing-shows-2025-09-23/?utm_source=chatgpt.com "Celltrion unit pays $330 million for Eli Lilly production facility, filing shows"
[6]: https://www.reuters.com/markets/deals/south-koreas-sk-bioscience-buy-control-germanys-idt-biologika-244-mln-2024-06-27/?utm_source=chatgpt.com "South Korea's SK Bioscience to buy control of Germany's IDT Biologika for $244 mln"
[7]: https://www.reuters.com/business/healthcare-pharmaceuticals/samsung-biologics-buy-us-drug-production-facility-gsk-280-mln-2025-12-21/?utm_source=chatgpt.com "Samsung Biologics to buy US drug production facility from GSK for $280 million"
[8]: https://arxiv.org/abs/2503.13581?utm_source=chatgpt.com "Subgroup Performance of a Commercial Digital Breast Tomosynthesis Model for Breast Cancer Detection"
