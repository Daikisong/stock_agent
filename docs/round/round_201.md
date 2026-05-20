좋아. 순서상 이번은 **R10 Loop 7 — 건설·부동산·건자재 가격경로 검증 라운드**로 진행한다.

이번 R10은 매우 보수적으로 봐야 한다. 건설·부동산은 “대형 수주”, “PF 정상화”, “데이터센터 부동산”, “재건”, “금리 인하” 같은 말이 주가를 먼저 밀 수 있지만, 실제 E2R Stage 3는 **현금흐름, PF 리스크 해소, 원가율, 안전·품질 신뢰, 임차인·NOI·AFFO, funding cost**가 확인되어야 한다.

---

# 1. 이번 라운드 대섹터

```text
R10 = 건설·부동산·건자재
large_sector = CONSTRUCTION_REAL_ESTATE_MATERIALS
round = R10 Loop 7 / price-path validation
목표 = Stage 3 / 4B / 4C가 실제 가격경로와 맞았는지 검증하고 shadow weight 보정
```

R10의 기본 영역은 건설 credit, REIT/development trust, 건자재, 데이터센터 REIT, 콜드체인 물류, 재건 정책, 재난복구 이벤트다. Round 40 기준 R10 validation focus는 `pf_credit`, `cash_flow`, `cost_ratio`, `occupancy`, `affo`, `funding_cost`, `tenant_contract`로 잡혀 있다. 

Round 119 기준으로 R10에서 부족한 증거는 `ai_data_center_theme`, `asset_headline`이고, 필요한 증거는 `tenant`, `noi_affo`, `power_water`, `funding_cost`, `capex_per_share`다. Green blocker는 `tenant_absent`, `affo_integrity_risk`, `capex_dilution`이다. 

---

# 2. 대상 canonical archetype

이번 R10 Loop 7에서는 새 archetype을 늘리는 게 아니라, 기존 R10 안에서 가격경로 검증이 필요한 축만 사용한다.

```text
CONSTRUCTION_REAL_ESTATE_CREDIT
CONSTRUCTION_REAL_ESTATE_CREDIT_KOREA
PF_RESTRUCTURING_RELIEF
PF_CREDIT_REDTEAM_OVERLAY
OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA
EPC_LOW_MARGIN_ORDER_OVERLAY
APARTMENT_QUALITY_SAFETY_OVERLAY
BUILDING_MATERIALS_PRICE_COST
DATA_CENTER_REIT_INFRASTRUCTURE
AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT
AI_DATA_CENTER_NO_REVENUE_NO_TENANT
DATA_CENTER_POWER_WATER_PERMITTING
REIT_AFFO_INTEGRITY_OVERLAY
AI_INFRA_REAL_ASSET_THEME_OVERLAY
DISASTER_REBUILD_EVENT
```

이번 R10의 핵심 질문은 이거다.

```text
이 회사는 건설·PF·데이터센터·재건 테마주인가?
아니면 수주가 실제 마진·현금흐름·임차계약·NOI/AFFO·주주가치로 내려오는 회사인가?
```

---

# 3. deep sub-archetype

```text
PF / 주택 건설:
- PF liquidity stress
- Taeyoung-style workout
- profitable project filtering
- syndicated loan / market stabilization fund
- high raw material cost
- housing downturn
- unsold inventory
- refinancing risk
- credit cost

품질 / 안전:
- apartment collapse
- construction defect
- fatal accident
- license suspension risk
- serious accident punishment
- site shutdown
- brand trust damage
- warranty / rebuild cost

해외 EPC / 인프라:
- Saudi Aramco gas expansion
- Fadhili / Jafurah gas project
- EPC backlog
- low-margin order risk
- cost overrun
- working capital burden
- completion / handover milestone

데이터센터 real asset:
- AI data center campus
- AWS / SK Ulsan data center
- OpenAI / Samsung SDS / SK Telecom data center JV
- tenant contract
- power availability
- water / permitting
- capex per share
- AFFO dilution
- listed exposure clarity

REIT / 부동산:
- dividend coverage
- occupancy
- funding cost
- AFFO integrity
- capex dilution
- logistics/cold-chain occupancy
```

---

# 4. 국장 신규 후보 case

## Case A — 삼성E&A `success_candidate / EPC backlog`

```text
symbol = 028050
archetype = OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA / EPC_LOW_MARGIN_ORDER_OVERLAY
case_type = success_candidate
```

삼성E&A는 R10에서 해외 EPC 수주가 Stage 3가 되려면 어떤 조건이 필요한지 보는 케이스다. 2024년 4월 Saudi Aramco는 Fadhili gas plant 확장에 총 77억 달러 계약을 발주했고, 이 중 삼성E&A와 GS건설 등이 EPC 계약자로 포함됐다. 해당 프로젝트는 Fadhili gas plant 처리능력을 하루 25억 scf에서 40억 scf로 키우는 구조이며, 2027년 11월 완공 예정으로 보도됐다. ([Reuters][1])

WSJ 보도 기준 삼성E&A는 Fadhili 확장 프로젝트에서 약 60억 달러 규모 계약을 따낸 것으로 보도됐고, 발표 직후 주가는 장중 최대 8.5% 상승해 26,750원까지 올랐다. 다만 대형 EPC 수주는 수주 자체보다 **마진·공정률·원가변동·working capital** 확인이 더 중요하다. ([월스트리트 저널][2])

### stage date 후보

```text
Stage 1:
2024-04-02
- Saudi Aramco Fadhili gas expansion 수주 기대
- 중동 gas EPC cycle

Stage 2:
2024-04-03
- 약 60억 달러 규모 삼성E&A Fadhili 계약 보도
- 주가 장중 +8.5%, 26,750원 anchor

Stage 3:
보류
- 수주 자체는 강하지만 EPC margin, cost overrun, progress revenue, working capital 확인 필요

Stage 4B:
수주 발표 직후 단기 급등은 event premium / 4B-watch 후보

Stage 4C:
공사 지연, 원가 초과, 저마진 수주, 발주처 변경, working capital 악화 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2024-04-03 26,750원 장중 anchor.
정확한 종가는 OHLC backfill 필요.

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
rerating_result = EPC_backlog_watch
stage_failure_type = stage2_watch_success 후보
```

### 교정 포인트

삼성E&A는 R10에서 `contract_size`보다 `EPC_margin_visibility`를 올려야 한다.

```text
수주 발표:
Stage 2

Stage 3 조건:
마진 가이던스
공정률 안정
원가 초과 없음
현금흐름 개선
수주잔고의 이익 전환
```

---

## Case B — 현대건설 `success_candidate / overseas gas infrastructure`

```text
symbol = 000720
archetype = OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA / INFRA_CONTRACT_BACKLOG
case_type = success_candidate
```

현대건설은 중동 gas infrastructure EPC 수주를 보는 케이스다. 2024년 6월 Aramco는 Jafurah gas field 2단계와 main gas network 3단계 확장에 250억 달러 이상 계약을 체결했고, Jafurah는 2030년까지 하루 20억 scf 판매가스를 생산할 계획이라고 보도됐다. 이 계약군에는 현대건설이 포함된 컨소시엄도 있었다. ([Reuters][3])

### stage date 후보

```text
Stage 1:
2024-06
- Saudi gas infrastructure capex cycle
- Jafurah / main gas network expansion

Stage 2:
2024-06-30
- Aramco $25B+ 계약군
- 현대건설 포함 컨소시엄 수주

Stage 3:
보류
- 대형 인프라 수주는 강하지만, project margin, cash collection, cost control 확인 전 Green 금지

Stage 4B:
중동 EPC 수주 기대만으로 주가가 먼저 과열되면 후보

Stage 4C:
project delay, cost overrun, 발주처 지급 지연, 저마진 수주 확인 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2024-06-30 또는 다음 거래일 OHLC backfill 필요.

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
rerating_result = overseas_EPC_watch
stage_failure_type = stage2_watch_success 후보
```

### 교정 포인트

현대건설은 `government/sovereign contract`, `project scale`, `backlog`를 올려주지만, `low_margin_EPC`, `working_capital_burden`, `cost_overrun` gate도 같이 붙여야 한다.

---

## Case C — 대우건설 `success_candidate / infrastructure handover`

```text
symbol = 047040
archetype = OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA / INFRA_RECONSTRUCTION_POLICY
case_type = success_candidate
```

대우건설은 R10에서 “수주 발표”보다 “완공·인도 milestone”을 Stage 2로 볼 수 있는 케이스다. Reuters는 2024년 11월 이라크 Grand Faw port가 2026년 운영을 시작하고 2028년에는 350만 컨테이너 처리능력까지 갈 것으로 보도했다. 또 한국의 대우건설이 건설한 5개 부두가 이라크 항만당국에 인도됐다고 설명했다. ([Reuters][4])

### stage date 후보

```text
Stage 1:
2023~2024
- Iraq Development Road / Grand Faw port 기대
- 중동 인프라 corridor

Stage 2:
2024-11-12
- 대우건설이 건설한 Grand Faw 5개 부두 인도
- 2026년 운영 시작, 2028년 350만 컨테이너 capacity 목표

Stage 3:
보류
- 완공 milestone은 강하지만, 대우건설 이익·현금흐름·추가수주 전환 확인 필요

Stage 4B:
이라크 개발도로 / 재건 기대가 주가에 과도하게 반영되면 후보

Stage 4C:
미수금, 정치 리스크, 추가 공정 지연, 대금 회수 지연 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2024-11-12 OHLC backfill 필요.

MFE_30D / 90D / 180D / 1Y / 2Y:
Stage 2 기준 backfill 필요.

MAE:
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
rerating_result = infrastructure_completion_watch
stage_failure_type = stage2_watch_success 후보
```

### 교정 포인트

대우건설은 `handover_milestone` 점수를 추가로 올려줄 수 있다. 다만 Stage 3는 “항구가 크다”가 아니라 대우건설의 **이익 인식·현금 회수·추가 수주**가 확인될 때다.

---

## Case D — 태영건설 `4C-thesis-break / PF credit`

```text
symbol = 009410
archetype = PF_RESTRUCTURING_RELIEF / PF_CREDIT_REDTEAM_OVERLAY
case_type = 4C-thesis-break
```

태영건설은 R10의 PF 4C 기준점이다. Reuters는 2024년 3월 한국 정부가 고금리와 부동산 침체로 어려움을 겪는 중소기업·건설사를 위해 40.6조 원 규모 금융지원을 준비했다고 보도했다. 기사에서는 2023년 12월 태영건설이 채무 재조정을 계획했다고 밝히면서 다른 건설사 유동성 우려가 커졌다고 설명했다. ([Reuters][5])

또 금융감독원은 2024년 5월 부동산 PF 부실을 빠르게 정리하기 위해 프로젝트 평가를 더 엄격히 하겠다고 밝혔다. 부동산 PF 연체율은 2021년 말 0.37%에서 2023년 말 2.70%까지 올라갔고, 1조 원 규모의 syndicated loan이 준비됐으며 필요 시 5조 원까지 확대 가능하다고 보도됐다. ([Reuters][6])

### stage date 후보

```text
Stage 1:
2023
- 부동산 PF 유동성 우려
- 고금리 / 미분양 / 중견 건설사 credit risk

Stage 2:
없음
- 태영건설은 정상적인 Stage 2 success case가 아니라 credit-stress case

Stage 3:
없음
- debt reschedule / workout은 Green 금지

Stage 4B:
과거 주택경기 회복 기대로 주가가 올랐다면 4B-watch 후보

Stage 4C:
2023-12
- 채무 재조정 계획
- PF liquidity stress
- sector-wide credit contagion
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage4c_price:
2023-12 debt reschedule 발표일 OHLC backfill 필요.

MFE / MAE:
PF 회복 narrative 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
PF stress 이후 drawdown backfill 필요
```

### score-price alignment

```text
alignment = thesis_break
rerating_result = credit_thesis_break
stage_failure_type = should_have_been_red_or_watch
```

### 교정 포인트

태영건설은 R10에서 `PF_credit`을 hard gate로 올리는 핵심 케이스다.

```text
PF 유동성 지원:
Stage 1~2 relief

Stage 3 금지:
채무 재조정
workout
PF 연체율 상승
자금시장 안정기금 의존
```

---

## Case E — HDC현대산업개발 `4C-thesis-break / apartment quality safety`

```text
symbol = 294870
archetype = APARTMENT_QUALITY_SAFETY_OVERLAY
case_type = 4C-thesis-break
```

HDC현대산업개발은 R10에서 품질·안전 hard gate를 보는 케이스다. 2022년 1월 광주 화정 아이파크 외벽 붕괴 사고로 6명이 사망했고, 정부 조사위원회는 잘못된 시공 방식과 부실한 건축자재를 원인으로 봤다. HDC는 2021년 광주 철거 건물 붕괴 사고에도 연루되어 있었고, 2022년 사고 이후 정부 조사와 회장 사임이 이어졌다. ([위키백과][7])

### stage date 후보

```text
Stage 1:
2021~2022
- 주택 브랜드 / 개발사업 기대

Stage 2:
없음
- 안전·품질 사고 발생 후 positive stage 부여 금지

Stage 3:
없음
- 품질·안전 신뢰 회복, 수주 재개, 비용 정리 전 Green 금지

Stage 4B:
과거 주택경기 기대로 주가가 올랐다면 후보

Stage 4C:
2022-01-11
- 광주 화정 아이파크 붕괴
- 6명 사망
- construction quality / operational trust break
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage4c_price:
2022-01-11 또는 다음 거래일 OHLC backfill 필요.

MFE / MAE:
사고 전 주택경기 narrative 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
사고 이후 drawdown backfill 필요
```

### score-price alignment

```text
alignment = thesis_break
rerating_result = operational_quality_break
stage_failure_type = hard_4C
```

### 교정 포인트

HDC현대산업개발은 R10에서 `construction_quality_safety`를 가장 강한 4C gate로 둬야 한다. 건설주는 수주잔고보다 **신뢰**가 무너지면 PBR·PER 프레임이 먼저 무너진다.

---

## Case F — POSCO E&C / DL건설 계열 `4C-watch / workplace safety`

```text
symbols = POSCO Holdings indirect / DL Construction exposure
archetype = APARTMENT_QUALITY_SAFETY_OVERLAY / OPERATIONAL_TRUST_HARD_4C
case_type = 4C-watch
```

2025년 한국 정부는 산업재해를 강하게 단속했고, Reuters는 한국의 건설 사망률이 OECD 회원국 중 두 번째로 높다고 보도했다. 기사에 따르면 POSCO E&C는 고속도로 공사 사망 사고 이후 CEO를 해임하고 103개 공사현장을 중단했고, DL Construction에서는 사망 사고 이후 약 80명의 임원이 사의를 냈다. ([Reuters][8])

또 한국 정부는 반복적인 사망 사고가 발생한 기업에 최대 영업이익 5% 벌금을 부과하고, 반복적으로 공사중지 명령을 받은 건설사의 면허를 취소할 수 있는 규제를 추진한다고 밝혔다. 2024년 한국에서 산업재해로 사망한 589명 중 거의 절반이 건설업에서 발생했다. ([Reuters][9])

### stage date 후보

```text
Stage 1:
2025
- 건설 안전규제 강화
- serious accident punishment 강화

Stage 2:
없음
- 안전사고는 positive stage가 아니라 RedTeam input

Stage 3:
없음
- 안전 신뢰 회복, 현장 정상화, 비용·벌금 영향 확인 전 Green 금지

Stage 4B:
건설주가 PF relief로 올랐지만 안전 리스크가 무시되는 구간이면 후보

Stage 4C:
2025년 사망사고 / 현장중단 / 경영진 사임
- hard 4C 후보라기보다 operational trust 4C-watch
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage4c_price:
사고·현장중단·경영진 사임 공시일별 OHLC backfill 필요.

MFE / MAE:
PF relief / 건설 회복 narrative 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = thesis_break_watch
rerating_result = operational_trust_risk
stage_failure_type = should_have_been_red_or_watch
```

### 교정 포인트

R10에서는 안전사고가 “뉴스 노이즈”가 아니라 **마진·공사중단·면허·평판·수주 경쟁력**을 훼손할 수 있는 RedTeam이다.

---

## Case G — SK/AWS Ulsan AI 데이터센터 `success_candidate / no-clean-listed-real-estate-exposure`

```text
listed exposure = SK그룹 관련 상장사 / SK텔레콤 / SK Inc. / 직접 REIT 노출은 불명확
archetype = AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT / AI_DATA_CENTER_NO_REVENUE_NO_TENANT
case_type = success_candidate + insufficient_evidence
```

R10에서 AI 데이터센터 real asset 테마는 매우 중요하지만, 국장 상장주에 바로 Stage 3를 주기는 어렵다. 2025년 6월 한국 정부는 SK그룹과 AWS가 약 7조 원, 약 51억 달러를 투자해 울산에 국내 최대 AI 데이터센터를 짓는다고 밝혔다. 시설은 2025년 9월 착공, 2029년 완전 가동, 초기 100MW 규모로 보도됐고, SK그룹은 1GW까지 확장 가능성을 언급했다. ([Reuters][10])

또 2026년 2월 과기정통부 장관은 OpenAI, Samsung SDS, SK Telecom이 한국 데이터센터 건설을 3월부터 시작할 예정이라고 밝혔다. 초기 용량은 20MW 규모로 보도됐다. ([Reuters][11])

### stage date 후보

```text
Stage 1:
2025-06-20
- SK/AWS 울산 AI 데이터센터 발표
- AI data center real asset theme

Stage 2:
2026-02-11
- OpenAI / Samsung SDS / SK Telecom 데이터센터 건설 예정
- 초기 20MW 규모

Stage 3:
보류
- R10 관점에서는 직접 상장 REIT/부동산 vehicle의 tenant, NOI/AFFO, power/water, capex per share가 필요
- SK텔레콤/삼성SDS는 R8/R2 성격도 강함

Stage 4B:
AI 데이터센터 테마로 관련 건설·전력·부동산주가 먼저 급등하면 후보

Stage 4C:
전력/물/인허가 지연, tenant 계약 불명확, capex dilution, 수익모델 부재 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage1_price:
2025-06-20 관련 상장사별 OHLC backfill 필요.

stage2_price:
2026-02-11 관련 상장사별 OHLC backfill 필요.

MFE / MAE:
theme basket 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = success_candidate + insufficient_evidence
rerating_result = AI_data_center_real_asset_watch
stage_failure_type = stage2_evidence_not_green
```

### 교정 포인트

AI 데이터센터는 R10에서 강한 구조 후보지만, “AI 데이터센터를 짓는다”와 “상장 부동산/건설주가 AFFO·NOI로 이익을 얻는다”는 다르다.

```text
Stage 1:
AI data center announcement

Stage 2:
tenant / capacity / construction start

Stage 3:
NOI/AFFO
power/water secured
tenant contract
capex per share controlled
funding cost manageable
```

---

# 5. 이번 R10 case별 요약표

| case             | 분류                               | Stage 3 판정 |                      4B/4C 판정 | 가격경로 1차 판단                            |
| ---------------- | -------------------------------- | ---------: | ----------------------------: | ------------------------------------- |
| 삼성E&A            | success_candidate                |         보류 |            수주 발표 급등은 4B-watch | EPC 수주는 Stage 2, 마진/현금흐름 전 Green 금지   |
| 현대건설             | success_candidate                |         보류 |          중동 EPC 과열 시 4B-watch | 대형 gas infra 수주는 강하지만 cost control 필요 |
| 대우건설             | success_candidate                |         보류 |       인프라 재건 기대 과열 시 4B-watch | Grand Faw 인도는 Stage 2, 현금회수 확인 필요     |
| 태영건설             | 4C-thesis-break                  |         없음 |           PF workout은 hard 4C | PF 유동성 위기 기준점                         |
| HDC현산            | 4C-thesis-break                  |         없음 |                 품질·안전 hard 4C | 붕괴사고는 Green 차단                        |
| POSCO E&C / DL건설 | 4C-watch                         |         없음 |               안전사고·현장중단 watch | 안전규제 강화로 operational trust 중요         |
| SK/AWS 데이터센터     | success_candidate / insufficient |         보류 | AI data center theme 4B-watch | tenant/NOI/AFFO 전 Green 금지            |

---

# 6. 각 case별 stage date 후보 요약

```text
삼성E&A:
Stage 1 = 2024-04-02 Fadhili gas expansion EPC 기대
Stage 2 = 2024-04-03 약 $6B 계약 보도 / 주가 장중 +8.5%
Stage 3 = 보류 / EPC margin·공정률·현금흐름 확인 필요
Stage 4B = 수주 발표 직후 event premium 후보
Stage 4C = cost overrun / 저마진 / working capital 악화 시 후보

현대건설:
Stage 1 = 2024-06 Saudi gas infra capex cycle
Stage 2 = 2024-06-30 Aramco $25B+ 계약군, Hyundai E&C consortium 포함
Stage 3 = 보류
Stage 4B = 중동 EPC 수주 기대 과열 시 후보
Stage 4C = delay / cost overrun / 지급 지연 시 후보

대우건설:
Stage 1 = Iraq Development Road / Grand Faw port 기대
Stage 2 = 2024-11-12 Grand Faw 5개 부두 인도
Stage 3 = 보류
Stage 4B = 이라크 재건·인프라 기대 과열 시 후보
Stage 4C = 미수금 / 정치 리스크 / 추가 공정 지연 시 후보

태영건설:
Stage 1 = 2023 PF liquidity stress
Stage 2 = 없음
Stage 3 = 없음
Stage 4B = 주택경기 회복 기대 과열 시 후보
Stage 4C = 2023-12 debt reschedule / workout

HDC현산:
Stage 1 = 주택 브랜드 / 개발사업 기대
Stage 2 = 없음
Stage 3 = 없음
Stage 4B = 주택경기 기대 과열 시 후보
Stage 4C = 2022-01-11 광주 화정 아이파크 붕괴

POSCO E&C / DL건설:
Stage 1 = 2025 안전규제 강화
Stage 2 = 없음
Stage 3 = 없음
Stage 4B = PF relief 속 안전 리스크 무시 구간
Stage 4C = 사망사고 / 현장중단 / 경영진 사임 watch

SK/AWS 데이터센터:
Stage 1 = 2025-06-20 SK/AWS 울산 AI 데이터센터 발표
Stage 2 = 2026-02-11 OpenAI/Samsung SDS/SK Telecom 데이터센터 건설 예정
Stage 3 = 보류 / tenant·NOI·AFFO·power/water 필요
Stage 4B = AI data center theme 급등 시 후보
Stage 4C = 인허가·전력·물·capex dilution 문제 시 후보
```

---

# 7. 가격경로 검증

R10은 정확한 OHLC backfill 없이 수익률을 확정하면 안 된다. 건설주는 수주 발표, PF 지원책, 구조조정, 안전사고, 데이터센터 테마가 서로 다른 속도로 주가를 움직인다.

| case             | stage3_price | MFE/MAE                        | below_stage3 | peak/drawdown                 |
| ---------------- | -----------: | ------------------------------ | ------------ | ----------------------------- |
| 삼성E&A            |   Stage 3 없음 | Fadhili Stage 2 기준 backfill    | N/A          | 수주 발표 후 event fade 필요         |
| 현대건설             |   Stage 3 없음 | Jafurah Stage 2 기준 backfill    | N/A          | 중동 EPC cycle peak 필요          |
| 대우건설             |   Stage 3 없음 | Grand Faw handover 기준 backfill | N/A          | 인프라 기대 drawdown 필요            |
| 태영건설             |   Stage 3 없음 | PF stress 기준 backfill          | N/A          | workout 이후 drawdown 필수        |
| HDC현산            |   Stage 3 없음 | 사고 전 narrative 기준 backfill     | N/A          | 붕괴사고 이후 drawdown 필수           |
| POSCO E&C / DL건설 |   Stage 3 없음 | 안전사고 event 기준 backfill         | N/A          | operational trust drawdown 필요 |
| SK/AWS 데이터센터     |   Stage 3 없음 | theme basket 기준 backfill       | N/A          | AI data center theme peak 필요  |

핵심은 이거다.

```text
R10에서 Stage 3는 수주나 자산 headline이 아니라,
현금흐름·마진·NOI/AFFO·임차계약·안전신뢰가 확인되는 날짜다.
```

---

# 8. score-price alignment 판정

```text
삼성E&A:
alignment = success_candidate
대형 EPC 수주는 Stage 2.
마진/현금흐름 전 Stage 3 금지.

현대건설:
alignment = success_candidate
중동 gas infra 수주는 강하지만 EPC low-margin risk 확인 필요.

대우건설:
alignment = success_candidate
Grand Faw handover는 Stage 2.
cash collection / 추가수주 전 Green 금지.

태영건설:
alignment = thesis_break
PF workout은 R10 hard 4C 기준점.

HDC현산:
alignment = thesis_break
품질·안전 사고는 construction trust hard 4C.

POSCO E&C / DL건설:
alignment = thesis_break_watch
반복 사망사고와 현장중단은 operational trust RedTeam.

SK/AWS 데이터센터:
alignment = success_candidate + insufficient_evidence
AI data center는 구조 후보지만, R10 상장 vehicle의 NOI/AFFO 전 Green 금지.
```

---

# 9. 점수비중 교정

## 올릴 축

```text
cash_flow_after_working_capital +5
EPC_margin_visibility +5
project_cost_control +4
handover_milestone +3
PF_credit_cleanup +5
funding_cost_control +4
tenant_contract_quality +5
NOI_AFFO_visibility +5
occupancy_or_utilization +4
power_water_permitting_secured +4
safety_quality_trust +5
```

R10에서 가장 강한 건 “수주”가 아니라 **수주가 현금흐름과 마진으로 닫히는 것**이다.

## 내릴 축

```text
contract_headline_only -4
PF_relief_policy_only -5
real_estate_rebound_theme_only -4
data_center_theme_without_tenant -5
asset_headline_without_NOI_AFFO -5
EPC_backlog_without_margin -4
low_margin_order_risk -4
capex_per_share_dilution -4
quality_safety_incident -5
workplace_fatality_repeated -5
```

태영건설·HDC현산·POSCO E&C/DL건설 때문에 `PF_credit`과 `safety_quality`는 R10의 가장 강한 RedTeam gate로 올려야 한다.

## Green gate 강화 조건

R10 Stage 3-Green은 앞으로 이렇게 줘야 한다.

```text
필수 gate:
1. 수주 또는 임차계약이 회사 단위로 확인됨
2. 마진 또는 NOI/AFFO가 확인됨
3. 현금흐름이 working capital에 먹히지 않음
4. PF / funding cost 리스크 통과
5. 공정률 / 원가율 안정
6. tenant / occupancy / utilization 확인
7. capex per share / dilution 통과
8. 안전·품질 hard risk 없음
9. 가격경로가 증거 이후 따라옴

금지:
수주 headline만 있음
PF 지원책만 있음
데이터센터 테마만 있음
자산 보유 headline만 있음
REIT 배당 headline만 있음
안전사고 발생
working capital 악화
저마진 EPC 수주
```

## 4B 조기감지 조건

```text
4B-watch:
대형 해외 EPC 수주 발표 직후 급등
PF 지원책으로 건설주 동반 급등
데이터센터 테마로 부동산/건설주 일괄 상승
REIT가 금리 인하 기대만으로 급등
재건/재난복구 테마로 가격이 먼저 감

4B-elevated:
수주는 늘지만 마진 가시성이 약함
PF 부실이 아직 정리되지 않음
공사비·인건비·금융비용 상승
데이터센터 tenant는 있지만 power/water/capex 문제가 남음
AFFO보다 배당 기대가 먼저 반영

4B-graduated:
좋은 수주에도 주가 반응 둔화
PF relief가 이미 가격에 반영
NOI/AFFO growth가 둔화
EPC margin surprise가 사라짐
```

## 4C hard gate 조건

```text
PF workout / 채무재조정
부동산 PF 연체율 급등
미분양 / 분양 실패
공사비 원가율 급등
working capital 악화
수주 취소 / 발주처 지급 지연
저마진 EPC 손실 인식
아파트 붕괴 / 품질사고
사망사고 반복 / 현장중단
면허 취소 리스크
tenant 부재
power/water/permitting failure
AFFO integrity 훼손
capex dilution
```

---

# 10. shadow-only 기록

이번 R10 Loop 7은 production scoring에 바로 반영하면 안 된다.

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
needs_ohlc_backfill = true
```

레포에 넣는다면 파일명은 이렇게 가는 게 자연스럽다.

```text
docs/round/round_129.md
docs/checkpoints/checkpoint_28a_round129_r10_loop7_construction_real_estate_materials_price_validation.md
src/e2r/sector/round129_r10_loop7_construction_real_estate_materials.py
data/e2r_case_library/cases_r10_loop7_round129.jsonl
data/sector_taxonomy/score_weight_profiles_round129_r10_loop7_v7.csv
output/e2r_round129_r10_loop7_construction_real_estate_materials/
```

---

# 이번 R10 Loop 7 결론

R10은 Stage 3 후보가 있긴 하지만, 굉장히 보수적으로 줘야 한다.

```text
1. 삼성E&A·현대건설·대우건설 같은 대형 EPC/인프라 수주는 Stage 2로는 강하다.
   하지만 Stage 3는 마진·공정률·현금흐름 확인 후에만 가능하다.

2. 태영건설은 PF credit hard 4C 기준점이다.
   PF 지원책은 relief이지 Green이 아니다.

3. HDC현산은 품질·안전 hard 4C 기준점이다.
   건설주는 브랜드 신뢰가 깨지면 수주잔고보다 RedTeam이 먼저다.

4. POSCO E&C/DL건설 사례는 반복 안전사고가 operational trust gate로 들어가야 함을 보여준다.

5. AI 데이터센터 real asset은 좋은 구조 후보지만,
   tenant·NOI/AFFO·power/water·capex per share 전에는 Stage 3가 아니다.

6. R10에서 가장 위험한 false Green은
   `수주 headline`, `PF relief`, `데이터센터 테마`, `금리 인하 REIT 기대`다.
```

한 문장으로 압축하면:

> **R10에서 진짜 Stage 3는 “수주가 있다”나 “부동산이 살아난다”가 아니라, 수주·자산·임차계약이 마진·현금흐름·NOI/AFFO로 닫히고 PF·안전·funding cost를 통과하는 순간이다.**
> **R10은 PF와 안전사고를 가장 강한 4C hard gate로 둬야 한다.**

[1]: https://www.reuters.com/markets/commodities/aramco-awards-77-bln-contracts-fadhili-gas-expansion-2024-04-02/?utm_source=chatgpt.com "Aramco awards $7.7 bln in contracts for Fadhili gas expansion"
[2]: https://www.wsj.com/articles/samsung-e-a-shares-rise-on-6-billion-saudi-contract-win-10a5b2f4?utm_source=chatgpt.com "Samsung E&A Shares Rise on $6 Billion Saudi Contract Win"
[3]: https://www.reuters.com/business/energy/aramco-signs-over-25-bln-deals-main-gas-network-jafurah-gas-field-2024-06-30/?utm_source=chatgpt.com "Aramco signs over $25 bln of deals for main gas network and Jafurah gas field"
[4]: https://www.reuters.com/world/middle-east/iraq-shortlists-11-firms-grand-faw-port-operation-decision-january-2025-2024-11-12/?utm_source=chatgpt.com "Iraq shortlists 11 firms for Grand Faw port operation, decision in January 2025"
[5]: https://www.reuters.com/markets/asia/south-korea-prepares-financial-support-small-businesses-builders-2024-03-27/?utm_source=chatgpt.com "South Korea prepares financial support for small businesses, builders"
[6]: https://www.reuters.com/markets/asia/south-korea-tightens-scrutiny-speed-up-real-estate-restructuring-2024-05-13/?utm_source=chatgpt.com "South Korea tightens scrutiny to speed up real estate restructuring"
[7]: https://en.wikipedia.org/wiki/Gwangju_Hwajeong_I-Park_exterior_wall_collapse?utm_source=chatgpt.com "Gwangju Hwajeong I-Park exterior wall collapse"
[8]: https://www.reuters.com/world/asia-pacific/south-koreas-new-president-injured-child-labourer-cracks-down-workplaces-death-2025-11-16/?utm_source=chatgpt.com "South Korea's new president, injured as a child labourer, cracks down on 'workplaces of death'"
[9]: https://www.reuters.com/sustainability/sustainable-finance-reporting/south-korea-fine-companies-up-5-profit-recurring-fatal-accidents-ministry-says-2025-09-15/?utm_source=chatgpt.com "South Korea to fine companies up to 5% of profit for recurring fatal accidents, ministry says"
[10]: https://www.reuters.com/business/retail-consumer/south-korea-says-sk-amazon-invest-5-bln-countrys-biggest-data-centre-2025-06-20/?utm_source=chatgpt.com "South Korea says SK and Amazon to invest $5 billion in country's biggest data centre"
[11]: https://www.reuters.com/world/asia-pacific/openai-samsung-sk-set-start-building-data-centres-korea-march-minister-says-2026-02-11/?utm_source=chatgpt.com "OpenAI, Samsung SDS and SK Telecom set to start building data centres in Korea in March, minister says"
