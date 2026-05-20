좋아. 순서상 이번은 **R3 Loop 7 — 2차전지·전기차·친환경 가격경로 검증 라운드**로 진행한다.

이번 R3는 일부러 결론을 세게 잡아야 해. **현 시점 R3는 “Stage 3-Green을 많이 찾는 라운드”가 아니라, false Green을 막는 라운드**에 가깝다. EV 배터리·소재는 2023년식 기대가 아직 남아 있지만, 2024~2026 가격경로와 공시 흐름을 보면 계약 취소, EV 수요 둔화, CAPEX 축소, 고객 주문 축소가 너무 많이 나왔다. 그래서 이번 라운드는 “좋은 구조 후보”보다 **Stage 2까지만 허용하고 Stage 3를 막아야 하는 케이스**가 많다.

---

# 1. 이번 라운드 대섹터

```text
R3 = 2차전지·전기차·친환경
large_sector = BATTERY_EV_GREEN
round = R3 Loop 7 / price-path validation
목표 = Stage 3 / 4B / 4C가 실제 가격경로와 맞았는지 검증하고 shadow weight 보정
```

R3의 기본 영역은 배터리 소재, 배터리 장비, 재활용, ESS, 수소, 재생에너지, CBAM, 폐기물, 데이터센터 물 재활용까지다. Round 40 지도에서도 R3 validation focus는 `contract_quality`, `utilization`, `fcf`, `ev_demand`, `capa_overbuild`, `commodity_price`로 잡혀 있다. 

Round 119 기준으로 R3에서 부족한 증거는 `ev_theme`, `ess_theme`, `capa_announcement`이고, 필요한 증거는 `contract_amount`, `gwh_volume`, `opm`, `fcf`, `customer_quality`다. Green blocker는 `overcapacity`, `mineral_price_down`, `negative_fcf`다. 

---

# 2. 대상 canonical archetype

이번 R3 Loop 7에서 새 archetype을 늘리지 않고, 기존 R3 안에서 가격경로 검증이 필요한 축만 사용한다.

```text
BATTERY_MATERIALS_CAPEX_OVERHEAT
CATHODE_LONG_CONTRACT_VISIBILITY
LITHIUM_RESOURCE_SECURITY_KOREA
BATTERY_EQUIPMENT_CAPEX_CYCLE
BATTERY_RECYCLING_ESS_SHIFT
ESS_LFP_GRID_STORAGE
EV_TO_ESS_CAPACITY_REDEPLOYMENT
EV_BATTERY_JV_RESTRUCTURING
BATTERY_CONTRACT_CANCELLATION_4C
BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE
BATTERY_TAX_CREDIT_QUALITY_OVERLAY
BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY
SEPARATOR_EV_DEMAND_CYCLE
COPPER_FOIL_EV_DEMAND_CYCLE
LITHIUM_CYCLE_OVERLAY
EVENT_LITHIUM_PRICE_RALLY
```

이번 R3의 핵심 질문은 이거다.

```text
이 회사는 EV/ESS/배터리 수혜주인가?
아니면 실제 고객 주문, GWh 물량, 마진, FCF, EPS revision으로 체급이 바뀌는 회사인가?
```

---

# 3. deep sub-archetype

```text
셀 메이커:
- LG Energy Solution
- Samsung SDI
- SK On via SK Innovation
- EV battery slowdown
- ESS pivot
- LFP ESS
- IRA / AMPC tax credit
- US plant utilization
- customer cancellation
- capex cut

양극재 / 전구체:
- L&F high-nickel cathode
- POSCO Future M cathode/anode
- EcoPro Materials precursor
- Tesla 4680 exposure
- Ford / GM / Tesla order risk
- lithium price event
- long-term supply contract
- contract value revision

분리막 / 동박 / 소재:
- SK IE Technology separator
- copper foil
- separator utilization
- EV demand slowdown
- customer concentration
- sale / restructuring risk

ESS / 재활용 / 친환경:
- LFP ESS contract
- EV-to-ESS line conversion
- recycling feedstock visibility
- second-life battery
- renewable policy
- hydrogen/fuel cell
- waste/recycling
```

---

# 4. 국장 신규 후보 case

## Case A — LG에너지솔루션 `success_candidate + 4C-watch`

```text
symbol = 373220
archetype = ESS_LFP_GRID_STORAGE / EV_TO_ESS_CAPACITY_REDEPLOYMENT / BATTERY_CONTRACT_CANCELLATION_4C
case_type = success_candidate + 4C-watch
```

LG에너지솔루션은 R3에서 가장 중요한 “ESS 전환은 Stage 2로 인정하되, EV thesis 훼손은 4C-watch로 동시에 기록해야 하는” 케이스다.

2025년 1월 LG에너지솔루션은 EV 수요 둔화 때문에 CAPEX를 최대 30% 줄이겠다고 했고, 2024년 4분기에는 2,260억 원 영업손실을 기록했다. 회사는 기존/계획된 설비 활용에 집중하겠다고 했고, 미국 EV 보조금 변화가 단기 수요를 누를 수 있다고 봤다. 이 시점에서 R3 Stage 3-Green은 막아야 한다. ([Reuters][1])

그런데 2025년 7월에는 Tesla향으로 추정되는 43억 달러 LFP 배터리 공급계약을 체결했다. 계약 기간은 2027년 8월부터 2030년 7월까지이고, ESS용 LFP 배터리를 미국 공장에서 공급하는 구조로 보도됐다. 이건 EV에서 ESS로 수요축을 옮기는 Stage 2 증거다. ([Reuters][2])

하지만 2025년 12월에는 Ford와 Freudenberg 관련 계약 종료/취소로 약 13.5조 원의 기대 매출 손실이 발생할 수 있다는 보도가 나왔다. 이는 2024년 매출의 절반을 넘는 규모로 언급됐고, EV 수요 둔화와 정책 변화가 실제 계약가시성을 훼손한 케이스다. ([Reuters][3])

### stage date 후보

```text
Stage 1:
2024~2025
- EV 배터리 둔화
- ESS 전환 기대
- 미국 LFP/ESS supply chain 기대

Stage 2:
2025-07-30
- 43억 달러 LFP battery supply contract
- Tesla ESS customer 추정
- 미국 공장 기반 ESS 공급

Stage 3:
보류
- 매출 인식이 2027년 이후
- OPM / FCF / EPS revision 아직 확인 필요
- EV 계약 취소 리스크가 동시에 존재

Stage 4B:
없음
- ESS 전환 기대가 주가를 과도하게 먼저 밀면 4B-watch 후보

Stage 4C:
2025-12-26 후보
- Ford / Freudenberg 계약 종료·취소
- EV battery expected revenue 대규모 훼손
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2025-07-30 OHLC backfill 필요.

MFE_30D / 90D / 180D / 1Y / 2Y:
Stage 2 기준으로 backfill 가능.
Stage 3 기준으로는 N/A.

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
alignment = success_candidate + thesis_break_watch
rerating_result = unknown
stage_failure_type = stage2_watch_success 후보
```

### 교정 포인트

LG에너지솔루션은 “ESS 전환이 있다”는 이유만으로 Stage 3를 주면 안 된다.

```text
ESS 계약:
Stage 2 가능

Stage 3 조건:
GWh 물량
매출 인식
OPM
FCF
AMPC 제외 이익
EV 계약 취소 리스크 통과
```

---

## Case B — L&F `4C-thesis-break`

```text
symbol = 066970
archetype = CATHODE_LONG_CONTRACT_VISIBILITY / BATTERY_CONTRACT_CANCELLATION_4C
case_type = 4C-thesis-break
```

L&F는 이번 R3에서 가장 선명한 4C 케이스다.

L&F는 2023년에 Tesla향 high-nickel cathode 공급계약을 발표했지만, 2025년 12월 그 계약의 예상 가치가 29억 달러에서 단 7,386달러로 줄었다고 밝혔다. Reuters는 Tesla 4680 생산 차질, EV 수요 둔화, Cybertruck 부진 등이 원인으로 거론됐다고 보도했다. ([Reuters][4])

이건 E2R에서 거의 교과서적인 thesis break다. 처음엔 `고객 = Tesla`, `소재 = high-nickel cathode`, `계약 = 장기 공급`으로 Stage 2~3 후보처럼 보였지만, 실제 고객 수요와 4680 양산이 깨지면 계약가시성이 사라진다.

### stage date 후보

```text
Stage 1:
2023
- Tesla 4680 / high-nickel cathode 기대

Stage 2:
2023 계약 발표 시점
- Tesla향 cathode supply deal
- 단, 가격/물량/실제 call-off 구조 확인 필요

Stage 3:
보류했어야 함
- Tesla 4680 양산, 실제 발주량, 매출 인식, 마진 확인 전 Green 금지

Stage 4B:
2023~2024 배터리 소재 과열 구간
- 정확한 가격경로 backfill 필요

Stage 4C:
2025-12-29
- 계약 예상가치 $2.9B → $7,386
- 고객 수요 / 4680 / EV thesis break
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여가 맞음.

Stage2_price:
2023 계약 발표일 OHLC backfill 필요.

MFE_30D / 90D / 180D / 1Y / 2Y:
Stage 2 기준 backfill 필요.
Stage 3 기준 N/A.

MAE:
Stage 2 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
2023~2024 과열 peak backfill 필요

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = thesis_break
rerating_result = no_rerating / thesis_break
stage_failure_type = false_green 방지용 핵심 case
```

### 교정 포인트

L&F는 R3 점수표에서 `contract_amount`보다 `binding volume`, `take-or-pay`, `customer production ramp`, `order call-off`, `chemistry adoption`을 더 강하게 봐야 한다는 증거다.

```text
계약 headline
≠ Stage 3

Tesla 고객명
≠ Stage 3

Stage 3 조건:
실제 발주량
4680 양산 안정
매출 인식
마진
EPS revision
```

---

## Case C — SK이노베이션 / SK온 `failed_rerating + ESS pivot watch`

```text
symbol = 096770
archetype = EV_BATTERY_JV_RESTRUCTURING / EV_TO_ESS_CAPACITY_REDEPLOYMENT
case_type = failed_rerating + success_candidate
```

SK이노베이션은 상장사이고, SK온은 비상장 자회사이므로 R3에서는 SK이노베이션을 통해 SK온 battery thesis를 본다.

2024년 7월 FT는 SK온이 10개 분기 연속 손실을 기록했고, 순부채가 2.9조 원에서 15.6조 원으로 5배 이상 증가했다고 보도했다. CEO는 “비상경영”을 선언했고, SK그룹 내에서는 SK이노베이션과 SK E&S 합병 같은 재무 보강 방안이 논의됐다. ([Financial Times][5])

2024년 8월 SK이노베이션 주주들은 SK E&S와의 합병을 승인했다. Reuters는 이 합병이 EV 수요 둔화로 어려움을 겪는 손실 배터리 자회사 SK온의 재무를 보강하기 위한 구조라고 설명했다. 이때 주가는 장중 최대 5% 상승했다. ([Reuters][6])

이후 2025년 9월 SK온은 미국 Flatiron Energy에 2026~2030년 최대 7.2GWh ESS용 LFP 배터리를 공급하기로 했다. 금액은 공개되지 않았고, 일부 EV 생산라인을 ESS용으로 전환할 계획도 밝혔다. ([Reuters][7])

### stage date 후보

```text
Stage 1:
2021~2023
- SK온 글로벌 EV 배터리 성장 기대

Stage 2:
2025-09-03
- Flatiron ESS LFP 7.2GWh 공급계약
- EV line → ESS conversion 가능성

Stage 3:
보류
- 계약금액 미공개
- SK온 누적 손실 / 부채 부담 / FCF 확인 필요
- ESS 양산은 2026년 하반기 예정

Stage 4B:
없음
- 합병 승인에 따른 주가 반등은 event premium에 가까움

Stage 4C:
2024-07
- 비상경영, 10개 분기 손실, 순부채 급증
- 기존 EV battery growth thesis 훼손
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

Stage2_price:
2025-09-03 OHLC backfill 필요.

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
alignment = thesis_break_then_success_candidate
rerating_result = failed_rerating / restructuring_relief
stage_failure_type = should_have_been_red_or_watch
```

### 교정 포인트

SK온은 R3에서 `ESS pivot`을 긍정적으로 볼 수 있지만, SK온의 과거 EV thesis는 이미 4C에 가까운 훼손을 겪었다.

```text
올릴 축:
ESS GWh
line conversion
production start date
customer contract

내릴 축:
negative FCF
high debt
unlisted subsidiary opacity
contract value undisclosed
loss-making battery unit
```

---

## Case D — 삼성SDI `success_candidate / insufficient_evidence`

```text
symbol = 006400
archetype = ESS_LFP_GRID_STORAGE / BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE
case_type = success_candidate / insufficient_evidence
```

삼성SDI는 ESS 전환 기대는 있지만, 이번 라운드에서는 Stage 3를 주면 안 된다.

2025년 3월 삼성SDI CEO는 EV 수요가 2026년 상반기까지 부진할 것으로 봤고, 회사의 2024년 4분기 영업손실은 2,570억 원이었다. 이 자체가 R3 Green을 막는 강한 근거다. ([Reuters][8])

2025년 11월에는 Tesla가 삼성SDI로부터 3년간 3조 원 이상 ESS 배터리를 구매하기로 했다는 보도가 나왔지만, 삼성SDI는 “아직 결정된 것이 없다”고 밝혔다. 이건 Stage 1~2 attention으로는 의미가 있지만, 미확정 보도만으로 Stage 3를 줄 수 없다. ([Reuters][9])

### stage date 후보

```text
Stage 1:
2025-11-03
- Tesla ESS battery purchase 보도

Stage 2:
보류
- 회사가 확정되지 않았다고 밝힘
- 계약금액/고객/기간이 보도에는 있지만 company confirmation 부족

Stage 3:
없음
- 확정 계약, 매출 인식, margin, EPS revision 전 Green 금지

Stage 4B:
없음
- 미확정 보도에 주가 급등했다면 price-only watch

Stage 4C:
2025-03-05 watch
- EV 수요 부진, 4Q 영업손실
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

Stage1_price:
2025-11-03 OHLC backfill 필요.

MFE / MAE:
Stage 1 기준 backfill 가능.

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
rerating_result = event_premium 후보
stage_failure_type = stage1_attention_only
```

### 교정 포인트

삼성SDI는 R3에서 `media_report_without_company_confirmation` 감점을 강화해야 하는 케이스다.

```text
Tesla ESS 보도
≠ Stage 3

회사 확인 없음
= disclosure confidence cap

EV 수요 부진 + 영업손실
= Green block
```

---

## Case E — SK아이이테크놀로지 `failed_rerating / 4C-watch`

```text
symbol = 361610
archetype = SEPARATOR_EV_DEMAND_CYCLE / EV_BATTERY_JV_RESTRUCTURING
case_type = failed_rerating / 4C-watch
```

SK아이이테크놀로지는 R3의 분리막/부품 쪽 false Green 방지에 좋은 케이스다.

2024년 5월 Reuters는 SK이노베이션이 EV 수요 약화와 SK온의 재무난 때문에 분리막 자회사 SK아이이테크놀로지 매각을 검토하고 있다고 보도했다. 당시 SKIET는 EV 배터리 분리막 업체이고, Panasonic 등 EV 배터리 제조사에 공급하는 기업으로 설명됐다. SKIET 시가총액은 약 4.09조 원이었다. ([Reuters][10])

또 같은 기사에서 SK온은 2024년 1분기 영업손실이 전 분기 186억 원에서 3,320억 원으로 확대됐고, EV 배터리 출하가 줄었다고 되어 있다. 이건 분리막/소재 업체가 최종 EV 수요 둔화와 고객 재무 문제에서 자유롭지 않다는 뜻이다. ([Reuters][10])

### stage date 후보

```text
Stage 1:
2021~2023
- EV separator growth 기대

Stage 2:
보류
- 실제 고객 수요/가동률/마진 개선 증거 필요

Stage 3:
없음
- EV 수요 둔화, SK온 손실 확대, 매각 검토 보도

Stage 4B:
과거 EV 소재 과열 구간
- 가격 backfill 필요

Stage 4C:
2024-05-15
- SKIET 매각 검토 보도
- EV demand weakening
- SK온 재무난
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

MFE / MAE:
과거 Stage 1 narrative 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = thesis_break
rerating_result = failed_rerating
stage_failure_type = should_have_been_red_or_watch
```

### 교정 포인트

SKIET는 `separator` 같은 필수 소재도 EV 수요 둔화와 고객 CAPEX 축소를 이기지 못하면 Stage 3가 될 수 없다는 반례다.

```text
분리막 필수소재
≠ 구조적 Green

필수 확인:
가동률
고객 출하
OPM
FCF
고객 다변화
```

---

## Case F — 포스코퓨처엠 `overheat / cyclical_event`

```text
symbol = 003670
archetype = CATHODE_LONG_CONTRACT_VISIBILITY / LITHIUM_CYCLE_OVERLAY
case_type = overheat / cyclical_event
```

포스코퓨처엠은 장기 양극재/음극재 공급계약과 포스코그룹 원료 내재화 스토리 때문에 Stage 2~3 후보처럼 보였던 기업이다. 하지만 이번 R3에서는 Green 확정이 아니라 **가격 이벤트와 수요둔화 리스크를 분리하는 케이스**로 쓰는 게 맞다.

2025년 12월 Ford가 여러 EV 모델을 중단한다는 소식에 LG에너지솔루션이 6% 하락했고, 삼성SDI는 3.5%, 양극재 업체 포스코퓨처엠은 8.2% 급락했다. 이건 고객사 EV 계획 축소가 양극재 valuation에 직접 충격을 주는 사례다. ([Reuters][11])

반대로 2025년 8월 CATL이 리튬 광산 프로젝트를 중단하자 리튬 가격 상승 기대가 커졌고, 한국 배터리 소재주 중 포스코퓨처엠은 8.3%, L&F는 10% 올랐다. 하지만 이건 상품가격 이벤트에 가까워서 Stage 3-Green 증거가 아니다. ([월스트리트저널][12])

### stage date 후보

```text
Stage 1:
2023~2024
- 양극재 장기계약 / 포스코그룹 원료 내재화 / EV 성장 기대

Stage 2:
계약별 backfill 필요
- 장기계약은 Stage 2 가능

Stage 3:
보류
- OPM, FCF, 고객 실제 주문, EV 수요 확인 필요

Stage 4B:
2023~2024 배터리 소재 과열 구간 후보

Stage 4C:
2025-12-16 watch
- Ford EV 모델 중단 → 포스코퓨처엠 -8.2%
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

Stage2_price:
계약 발표일별 backfill 필요.

MFE / MAE:
Stage 2 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
2023~2024 과열 peak backfill 필요

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = cyclical_success / event_premium 후보
rerating_result = unknown
stage_failure_type = false_green 방지용
```

### 교정 포인트

포스코퓨처엠은 `lithium price rally`, `CATL supply disruption`, `long-term contract headline`을 Stage 3로 직접 올리면 안 된다는 케이스다.

```text
상품가격 이벤트:
Stage 1~2 attention

Stage 3 조건:
고객 주문 지속
OPM 개선
FCF 개선
계약 물량 실제 인식
EV 수요 둔화 통과
```

---

## Case G — 에코프로머티리얼즈 `overheat / price_moved_without_evidence 후보`

```text
symbol = 450080
archetype = BATTERY_MATERIALS_CAPEX_OVERHEAT / PRECURSOR_SUPPLY_CHAIN
case_type = overheat / insufficient_evidence
```

에코프로머티리얼즈는 전구체/수직계열화 스토리로 R3 attention은 강하지만, 이번 루프에서는 Stage 3-Green을 주면 안 되는 케이스로 본다.

회사는 2023년 11월 KOSPI에 상장했고, 약한 EV 수요 환경 때문에 공모 구조를 조정해 4,190억 원가량을 조달한 것으로 정리되어 있다. 주요 생산물은 양극재 전구체이고, 그룹 내부 EcoPro BM에 공급하는 수직계열화 구조가 핵심이다. ([위키백과][13])

2024년 6월에는 주가가 11% 하락해 119,200원으로 떨어졌다는 MarketWatch 보도가 있다. 2025년 12월 Ford의 EV 후퇴 보도 때도 MarketWatch는 한국 배터리 supply chain 하락 종목으로 SK이노베이션, LG에너지솔루션, SK아이이테크놀로지, 에코프로머티리얼즈를 언급했고, 에코프로머티리얼즈가 5% 하락했다고 전했다. ([마켓워치][14]) ([마켓워치][15])

### stage date 후보

```text
Stage 1:
2023-11 IPO / EcoPro group precursor story

Stage 2:
보류
- 고객 다변화, 외부 매출, OPM, FCF 확인 필요

Stage 3:
없음
- 수직계열화 스토리와 IPO 수급만으로 Green 금지

Stage 4B:
IPO 이후 가격 과열 구간 후보
- OHLC backfill 필요

Stage 4C:
2025-12-16 watch
- Ford EV 후퇴에 supply chain 동반 하락
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

MFE / MAE:
IPO 이후 price path backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = price_moved_without_evidence 후보
rerating_result = theme_overheat 후보
stage_failure_type = insufficient_evidence
```

### 교정 포인트

에코프로머티리얼즈는 전구체/수직계열화가 테마로는 강하지만, E2R Green은 별도다.

```text
필수:
외부 고객
가동률
OPM
FCF
원료 조달 안정성
전구체 가격/스프레드
```

---

# 5. 이번 R3 case별 요약표

| case        | 분류                               | Stage 3 판정 |                      4B/4C 판정 | 가격경로 1차 판단                  |
| ----------- | -------------------------------- | ---------: | ----------------------------: | --------------------------- |
| LG에너지솔루션    | success_candidate + 4C-watch     |         보류 |        2025-12 계약취소는 4C-watch | ESS는 Stage 2, EV thesis는 훼손 |
| L&F         | 4C-thesis-break                  |    보류했어야 함 |         2025-12-29 hard 4C 후보 | Tesla 계약가치 붕괴               |
| SK이노베이션/SK온 | failed_rerating + ESS pivot      |         보류 |           2024 비상경영은 4C-watch | ESS는 Stage 2, EV는 실패        |
| 삼성SDI       | success_candidate / insufficient |         없음 |     미확정 Tesla ESS 보도는 Stage 1 | 회사 확인 전 Green 금지            |
| SK아이이테크놀로지  | failed_rerating                  |         없음 |       2024-05 매각 검토는 4C-watch | 분리막도 EV 수요 둔화에 취약           |
| 포스코퓨처엠      | overheat / cyclical_event        |         보류 | Ford shock / lithium event 분리 | 상품가격 이벤트는 Stage 3 아님        |
| 에코프로머티리얼즈   | overheat / insufficient          |         없음 |  IPO/EV supply chain 과열 watch | 전구체 스토리만으로 Green 금지         |

---

# 6. 각 case별 stage date 후보 요약

```text
LG에너지솔루션:
Stage 1 = 2024~2025 EV 둔화 + ESS 전환 기대
Stage 2 = 2025-07-30 Tesla 추정 LFP ESS 43억 달러 계약
Stage 3 = 보류
Stage 4B = 없음 / ESS 기대 과열 시 후보
Stage 4C = 2025-12-26 Ford/Freudenberg 계약취소 watch

L&F:
Stage 1 = 2023 Tesla 4680 high-nickel cathode 기대
Stage 2 = 2023 Tesla supply deal
Stage 3 = 보류했어야 함
Stage 4B = 2023~2024 소재 과열 구간 후보
Stage 4C = 2025-12-29 계약가치 $2.9B → $7,386

SK이노베이션/SK온:
Stage 1 = EV battery global growth 기대
Stage 2 = 2025-09-03 Flatiron ESS LFP 7.2GWh 계약
Stage 3 = 보류
Stage 4B = 없음 / 합병 반등은 event premium
Stage 4C = 2024-07 SK온 비상경영, 누적손실, 순부채 증가

삼성SDI:
Stage 1 = 2025-11-03 Tesla ESS 보도
Stage 2 = 보류
Stage 3 = 없음
Stage 4B = 미확정 보도 급등 시 price-only 후보
Stage 4C = 2025-03-05 EV 수요 부진 + 4Q 영업손실 watch

SK아이이테크놀로지:
Stage 1 = EV separator growth 기대
Stage 2 = 보류
Stage 3 = 없음
Stage 4B = 과거 EV 소재 과열 구간 후보
Stage 4C = 2024-05-15 매각 검토 / EV 수요 약화

포스코퓨처엠:
Stage 1 = 장기계약 / 양극재 성장 기대
Stage 2 = 계약별 backfill 필요
Stage 3 = 보류
Stage 4B = 2023~2024 소재 과열 구간 후보
Stage 4C = 2025-12-16 Ford EV 후퇴 충격 watch

에코프로머티리얼즈:
Stage 1 = 2023-11 IPO / 전구체 수직계열화 기대
Stage 2 = 보류
Stage 3 = 없음
Stage 4B = IPO 이후 과열 구간 후보
Stage 4C = 2025-12-16 EV supply chain shock watch
```

---

# 7. 가격경로 검증

이번 R3는 정확한 OHLC backfill 없이 수익률을 확정하면 위험하다. 특히 배터리주는 2023년 peak, 2024~2025 drawdown, 2025 리튬 이벤트 반등, 2025 Ford shock이 섞여 있어서 일봉 기준으로 분해해야 한다.

| case        | stage3_price | MFE/MAE                            | below_stage3 | peak/drawdown                    |
| ----------- | -----------: | ---------------------------------- | ------------ | -------------------------------- |
| LG에너지솔루션    |   Stage 3 없음 | Stage 2 기준 backfill                | N/A          | 2025 계약취소 후 drawdown backfill    |
| L&F         |   Stage 3 없음 | 2023 Stage 2 기준 backfill           | N/A          | 2023~2025 peak/drawdown 필수       |
| SK이노베이션/SK온 |   Stage 3 없음 | ESS Stage 2 기준 backfill            | N/A          | battery thesis drawdown backfill |
| 삼성SDI       |   Stage 3 없음 | Stage 1 ESS 보도 기준 backfill         | N/A          | EV slowdown drawdown backfill    |
| SK아이이테크놀로지  |   Stage 3 없음 | EV separator narrative 기준 backfill | N/A          | 매각 검토 전후 drawdown backfill       |
| 포스코퓨처엠      |   Stage 3 없음 | 계약/리튬 이벤트 기준 backfill              | N/A          | Ford shock, lithium rally 구간 분리  |
| 에코프로머티리얼즈   |   Stage 3 없음 | IPO 이후 backfill                    | N/A          | IPO overheat/drawdown backfill   |

핵심은 이거다.

```text
R3는 현재 Stage 3-Green을 많이 줄 구간이 아니다.
Stage 2 후보는 많지만,
Stage 3는 GWh / OPM / FCF / EPS revision / 고객 주문 지속성이 확인될 때까지 막아야 한다.
```

---

# 8. score-price alignment 판정

```text
LG에너지솔루션:
alignment = success_candidate + thesis_break_watch
ESS 전환은 Stage 2.
EV 계약취소는 4C-watch.

L&F:
alignment = thesis_break
Tesla 계약가치 붕괴는 hard 4C 후보.

SK이노베이션/SK온:
alignment = failed_rerating_then_success_candidate
EV battery thesis는 실패.
ESS LFP는 Stage 2 후보.

삼성SDI:
alignment = unknown_insufficient_evidence
Tesla ESS 미확정 보도는 Stage 1.
EV 수요 부진과 손실 때문에 Green 금지.

SK아이이테크놀로지:
alignment = thesis_break
분리막 성장 thesis가 EV 수요 둔화와 SK온 재무난에 훼손.

포스코퓨처엠:
alignment = cyclical_success / event_premium 후보
리튬 이벤트 상승과 Ford shock 하락을 구조적 Green과 분리해야 함.

에코프로머티리얼즈:
alignment = price_moved_without_evidence 후보
IPO / 전구체 / 그룹 스토리는 Stage 3 증거가 아님.
```

---

# 9. 점수비중 교정

## 올릴 축

```text
contract_binding_quality +4
gwh_volume_visibility +4
customer_order_calloff +4
opm_margin_visibility +4
fcf_after_capex +4
ess_revenue_conversion +3
utilization_rate +3
customer_quality +3
tax_credit_quality +2
```

R3에서 가장 중요한 건 계약명이나 고객명이 아니라 **계약이 실제 GWh, 가동률, 매출, 마진, FCF로 내려오는지**다.

## 내릴 축

```text
ev_theme -5
capa_announcement -4
customer_name_only -4
non_binding_supply_mou -4
policy_subsidy_expectation -3
lithium_price_event -3
ipo_theme_premium -4
group_vertical_integration_story -3
ess_media_report_unconfirmed -3
tax_credit_without_operating_profit -3
```

R3는 특히 `capa_announcement`가 위험하다. 공장을 짓는다는 말은 비용이 먼저 나간다는 뜻일 수도 있다. 매출·마진·FCF가 같이 오지 않으면 Stage 3가 아니라 오히려 RedTeam이다.

## Green gate 강화 조건

R3 Stage 3-Green은 앞으로 이렇게 줘야 한다.

```text
필수 gate:
1. binding contract
2. GWh or tonnage volume
3. customer call-off / shipment evidence
4. utilization rate
5. OPM or gross margin improvement
6. FCF after CAPEX
7. EPS/FCF revision
8. EV demand / ESS demand durability
9. tax credit quality separated from underlying profit

금지:
EV theme
ESS theme
CAPA announcement
customer name only
unconfirmed media report
lithium price spike
IPO premium
contract value without actual order
AMPC 제외 시 적자
```

## 4B 조기감지 조건

```text
4B-watch:
배터리 소재주가 EPS보다 먼저 3~5배 이상 상승
장기계약 headline만 반복
CAPA 증설이 수요보다 앞섬
리튬 가격 이벤트로 소재주 동반 급등
목표주가가 EV TAM만으로 확장
수주잔고는 큰데 OPM/FCF가 안 나옴

4B-elevated:
고객 주문 축소 조짐
공장 가동률 하락
재고 증가
수익성이 AMPC/보조금에 의존
소재 가격 하락으로 ASP pressure
```

## 4C hard gate 조건

```text
계약 취소
계약가치 대폭 축소
고객 모델 폐기
고객 EV 전략 후퇴
take-or-pay 부재 확인
GWh call-off 감소
CAPEX 축소 / 공장 지연
가동률 급락
OPM 붕괴
FCF 악화
재고/매출채권 증가
AMPC 제외 영업적자
EV 수요 회복 지연
```

L&F의 Tesla 계약가치 붕괴는 `contract_value_reduction_hard_4c`로 따로 둬야 한다. LG에너지솔루션의 EV 계약 취소는 `customer_strategy_contract_loss_4c_watch`로 둬야 하고, ESS LFP 전환은 별도 Stage 2로 분리해야 한다.

---

# 10. shadow-only 기록

이번 R3 Loop 7은 production scoring에 바로 반영하면 안 된다.

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
needs_ohlc_backfill = true
```

레포에 넣는다면 파일명은 이렇게 가는 게 자연스럽다.

```text
docs/round/round_122.md
docs/checkpoints/checkpoint_28a_round122_r3_loop7_battery_ev_green_price_validation.md
src/e2r/sector/round122_r3_loop7_battery_ev_green.py
data/e2r_case_library/cases_r3_loop7_round122.jsonl
data/sector_taxonomy/score_weight_profiles_round122_r3_loop7_v7.csv
output/e2r_round122_r3_loop7_battery_ev_green/
```

---

# 이번 R3 Loop 7 결론

R3 점수표는 방향이 맞지만, **Stage 3-Green을 훨씬 더 보수적으로 줘야 한다.**

이번 라운드의 핵심 교정은 이거야.

```text
1. EV/ESS/배터리 테마는 Stage 1 attention일 뿐이다.

2. ESS 전환은 좋은 Stage 2 후보지만,
   매출·OPM·FCF가 나오기 전 Stage 3가 아니다.

3. 양극재/전구체 장기계약은 계약명보다 실제 call-off가 중요하다.

4. Tesla, Ford, GM 같은 고객명은 점수가 아니다.
   고객의 모델 폐기, 주문축소, 4680 실패, EV 전략 후퇴가 나오면 바로 4C-watch다.

5. AMPC/세액공제는 이익의 질을 따로 봐야 한다.
   보조금 제외 시 적자면 Green을 막아야 한다.

6. R3의 가장 중요한 RedTeam은 CAPA 과잉, 가동률 하락, 계약가치 축소, FCF 악화다.
```

한 문장으로 압축하면:

> **R3에서 진짜 Stage 3는 “배터리 수혜”가 아니라, 계약이 실제 GWh·가동률·마진·FCF로 내려오는 순간이다.**
> **지금 R3는 대체로 Green 발굴보다 false Green 차단이 더 중요한 구간이다.**

[1]: https://www.reuters.com/technology/lg-energy-solution-posts-quarterly-loss-first-time-three-years-2025-01-24/?utm_source=chatgpt.com "LG Energy Solution cuts capex on slowing EV demand after Q4 loss"
[2]: https://www.reuters.com/business/energy/lg-energy-solution-tesla-sign-43-billion-battery-supply-deal-source-says-2025-07-30/?utm_source=chatgpt.com "LG Energy Solution, Tesla sign $4.3 billion battery supply deal, source says"
[3]: https://www.reuters.com/business/energy/lg-energy-solution-cancels-39-trillion-won-battery-order-with-freudenberg-2025-12-26/?utm_source=chatgpt.com "LG Energy Solution cancels 3.9 trillion won battery order with Freudenberg"
[4]: https://www.reuters.com/world/asia-pacific/south-koreas-lf-says-value-battery-material-supply-deal-with-tesla-cut-7386-2025-12-29/?utm_source=chatgpt.com "South Korea's L&F slashes value of battery material supply deal with Tesla"
[5]: https://www.ft.com/content/5affede6-1f1d-458e-b4d0-e2e7e902dcca?utm_source=chatgpt.com "Battery maker SK On declares 'emergency' as EV sales disappoint"
[6]: https://www.reuters.com/markets/deals/sk-innovation-shareholders-approve-merger-plan-with-sk-es-yonhap-reports-2024-08-27/?utm_source=chatgpt.com "SK Innovation shareholders approve merger seen shoring up loss-making battery unit"
[7]: https://www.reuters.com/business/energy/south-koreas-sk-signs-energy-storage-battery-supply-deal-with-flatiron-energy-2025-09-03/?utm_source=chatgpt.com "South Korea's SK On signs energy storage battery supply deal with Flatiron Energy"
[8]: https://www.reuters.com/business/autos-transportation/samsung-sdi-ceo-says-ev-demand-remain-sluggish-until-h1-2026-2025-03-05/?utm_source=chatgpt.com "Samsung SDI CEO says EV demand to remain sluggish until H1 of 2026"
[9]: https://www.reuters.com/business/autos-transportation/tesla-buy-2-bln-ess-batteries-samsung-sdi-over-3-years-newspaper-says-2025-11-03/?utm_source=chatgpt.com "Tesla to buy $2 bln of ESS batteries from Samsung SDI over 3 years, newspaper says"
[10]: https://www.reuters.com/technology/sk-innovation-considering-sale-battery-materials-unit-skiet-paper-reports-2024-05-15/?utm_source=chatgpt.com "SK Innovation considering sale of battery materials unit SKIET, paper reports"
[11]: https://www.reuters.com/world/asia-pacific/shares-lg-energy-solution-fall-6-after-ford-retreats-ev-push-2025-12-16/?utm_source=chatgpt.com "Shares of LG Energy Solution fall 6% after Ford retreats from EV push"
[12]: https://www.wsj.com/finance/commodities-futures/ev-battery-giant-catl-suspends-mining-project-67693725?utm_source=chatgpt.com "EV Battery Giant CATL Suspends Mining Project"
[13]: https://en.wikipedia.org/wiki/Ecopro_Materials?utm_source=chatgpt.com "Ecopro Materials"
[14]: https://www.marketwatch.com/story/ecopro-materials-shares-fall-11-to-krw119-200-103f38d7?utm_source=chatgpt.com "Ecopro Materials Shares Fall 11% to KRW119,200"
[15]: https://www.marketwatch.com/story/while-ford-shares-are-remarkably-steady-after-20-billion-charge-these-stocks-are-getting-battered-bbbcfa04?utm_source=chatgpt.com "While Ford shares are remarkably steady after $20 billion charge, these stocks are getting battered"
