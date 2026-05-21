좋아. 순서상 이번은 **R4 Loop 7 — 소재·스프레드·전략자원 가격경로 검증 라운드**로 진행한다.

이번 R4는 R3와 비슷하게 **Stage 3-Green을 많이 발굴하는 라운드가 아니라, commodity/spread/event premium을 구조적 리레이팅으로 착각하지 않게 만드는 라운드**에 가깝다. 소재 섹터는 가격이 먼저 튀고, 나중에 스프레드·재고·중국 공급·CAPEX가 따라와서 무너지는 경우가 많다. 그래서 이번 라운드는 “스프레드가 좋아졌다”와 “EPS/FCF 체급이 구조적으로 바뀌었다”를 강하게 분리해야 한다.

---

# 1. 이번 라운드 대섹터

```text
R4 = 소재·스프레드·전략자원
large_sector = MATERIALS_SPREAD_STRATEGIC
round = R4 Loop 7 / price-path validation
목표 = Stage 3 / 4B / 4C가 실제 가격경로와 맞았는지 검증하고 shadow weight 보정
```

R4의 기본 영역은 정유, 화학, 철강, 비철금속, 전략자원, 리튬, 귀금속, 제지, 농산물 input, LNG, 종합상사, 가스 유틸리티다. Round 40 지도에서도 R4 validation focus는 `product_spread`, `cost_curve`, `capacity_discipline`, `commodity_peak`, `eps_normalization`으로 잡혀 있다. 

Round 119 기준으로 R4에서 부족한 증거는 단순 `commodity_price_up`이고, 필요한 증거는 `price_floor`, `offtake`, `cost_curve`, `fcf`, `supply_discipline`다. Green blocker는 `spread_reversal`, `china_oversupply`, `inventory_build`다. 

---

# 2. 대상 canonical archetype

이번 R4 Loop 7에서는 새 archetype을 늘리지 않고, 기존 R4 안에서 가격경로 검증이 필요한 축을 사용한다.

```text
REFINING_OIL_SPREAD
CHEMICAL_SPREAD
PETROCHEMICAL_RESTRUCTURING_KOREA
COMMODITY_SPREAD_CYCLE_NOT_STRUCTURAL
NONFERROUS_STRATEGIC_METALS
RARE_METALS_STRATEGIC_MATERIALS
RARE_METALS_PRICE_FLOOR_OFFTAKE
LITHIUM_BATTERY_RAW_MATERIAL
LITHIUM_CYCLE_OVERLAY
POLYSILICON_NON_CHINA_SUPPLY_OPTION
COPPER_PROCESSING_PLUS_DEFENSE
EVENT_PREMIUM_GOVERNANCE_OVERLAY
COMMODITY_PRICE_4C_OVERLAY
```

이번 라운드의 핵심 질문은 이거다.

```text
이 회사는 원자재 가격/스프레드 이벤트로 오른 것인가?
아니면 price floor, offtake, cost curve, supply discipline, FCF가 잠겨서
시장 프레임 자체가 바뀌는가?
```

---

# 3. deep sub-archetype

```text
정유 / 에너지 스프레드:
- refining margin
- 3-2-1 crack spread
- geopolitical refinery outage
- diesel / jet fuel shortage
- crude input cost
- inventory gain/loss
- refining turnaround
- not structural unless capital return / FCF durability appears

석유화학:
- naphtha cracker
- ethylene / PE / PP spread
- China/Middle East overcapacity
- Korea NCC restructuring
- capacity shutdown
- government-backed restructuring
- loss reduction vs true rerating

비철 / 전략자원:
- zinc / copper / lead / precious metals
- antimony / gallium / germanium
- non-China strategic metals
- U.S. critical minerals plant
- governance battle / tender offer event premium
- capex burden / dilution risk

리튬 / 배터리 원료:
- spodumene
- lithium hydroxide
- POSCO lithium JV
- lithium price rally
- commodity price floor
- low-price countercyclical acquisition
- battery demand link

폴리실리콘 / 태양광 소재:
- non-China polysilicon
- SpaceX / AI data center solar power narrative
- IRA qualification
- China polysilicon overcapacity
- unconfirmed media report risk

구리 / 방산 복합:
- copper products
- ammunition
- defense unit sale rumor
- copper + defense premium
- denied transaction
- event premium vs recurring FCF
```

---

# 4. 국장 신규 후보 case

## Case A — 롯데케미칼 `4C-thesis-break / restructuring watch`

```text
symbol = 011170
archetype = PETROCHEMICAL_RESTRUCTURING_KOREA / CHEMICAL_SPREAD
case_type = 4C-thesis-break + restructuring_watch
```

롯데케미칼은 R4에서 “석유화학 스프레드 회복 기대”를 Stage 3로 올리면 안 되는 대표 케이스다. 2024년 롯데케미칼은 영업손실이 전년 대비 157% 확대된 8,950억 원을 기록했고, 이는 2011년 이후 가장 큰 영업손실이었다. Reuters는 한국 석유화학 기업들이 중국·중동 증설과 수요 둔화로 구조적 공급과잉에 눌렸다고 설명했다. ([Reuters][1])

이후 2025년 11월 롯데케미칼과 HD현대 측은 대산 석유화학 사업 구조조정 계획을 정부에 제출했고, 2026년 2월 정부는 첫 석유화학 구조조정 프로젝트를 승인했다. 계획에는 롯데케미칼 대산 NCC의 3년 가동 중단, HD현대케미칼과의 통합, 2조 원 이상 지원 패키지가 포함됐다. ([Reuters][2])

### stage date 후보

```text
Stage 1:
2024~2025
- 석유화학 바닥론 / 중국 부양 기대 / 구조조정 기대

Stage 2:
2025-11-26
- 롯데케미칼·HD현대 구조조정 계획 제출
- 공급과잉 해소를 위한 capacity cut 방향성

Stage 3:
보류
- 구조조정은 Stage 2 가능
- 그러나 spread 회복, OPM 개선, FCF 전환, EPS revision 전 Green 금지

Stage 4B:
없음
- 구조조정 기대만으로 급등했다면 event premium watch

Stage 4C:
2025-02-07 또는 그 이전
- 2024 영업손실 확대
- 중국/중동 과잉공급 지속
- 기존 petrochemical cycle thesis 훼손
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2025-11-26 OHLC backfill 필요.

MFE_30D / 90D / 180D / 1Y / 2Y:
Stage 2 기준 backfill 가능.
Stage 3 기준 N/A.

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
alignment = thesis_break_then_restructuring_watch
rerating_result = no_rerating / restructuring_relief_candidate
stage_failure_type = should_have_been_red_or_watch
```

### 교정 포인트

롯데케미칼은 R4에서 `capacity_cut`이 나오기 전까지는 Stage 3를 막아야 하는 케이스다. 구조조정은 좋은 신호일 수 있지만, 손실 축소와 FCF 전환이 확인되기 전에는 **구조적 리레이팅이 아니라 구조조정 relief**다.

---

## Case B — LG화학 `failed_rerating / petrochemical 4C-watch`

```text
symbol = 051910
archetype = CHEMICAL_SPREAD / PETROCHEMICAL_RESTRUCTURING_KOREA
case_type = failed_rerating + 4C-watch
```

LG화학은 배터리 소재와 석유화학이 섞여 있어 R3/R4 교차 케이스지만, 이번에는 석유화학 기준으로 본다. Reuters는 2024년 LG화학 영업이익이 63.75% 감소해 2019년 이후 최저였고, 석유화학 부문은 2024년 4분기 990억 원 영업손실을 냈다고 보도했다. 공급과잉은 중국과 중동 증설 때문에 수년간 지속될 수 있다고 설명됐다. ([Reuters][1])

2025년 12월 LG화학은 석유화학 구조조정 계획을 정부에 제출했고, 2026년 3월에는 이란전쟁에 따른 나프타 원료 조달 차질로 여수 2번 NCC를 일시 중단했다. 즉, 이 회사는 “스프레드 회복 기대”보다 원료 조달, 공급과잉, 구조조정, 설비 가동 리스크를 먼저 봐야 한다. ([Reuters][3])

### stage date 후보

```text
Stage 1:
2024~2025
- 석유화학 업황 바닥 기대
- 중국 부양 기대

Stage 2:
2025-12-19
- 정부에 석유화학 구조조정 계획 제출

Stage 3:
보류
- 구조조정 계획만으로는 부족
- NCC 가동률, spread, OPM, FCF 전환 확인 필요

Stage 4B:
없음

Stage 4C:
2025-02-07
- 2024 영업이익 급감, petrochemical loss
- 공급과잉 장기화
추가 4C-watch:
2026-03-23
- 여수 NCC 원료 조달 차질로 일시 중단
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2025-12-19 OHLC backfill 필요.

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
alignment = thesis_break / evidence_good_but_price_failed 후보
rerating_result = failed_rerating
stage_failure_type = false_green 방지용
```

### 교정 포인트

LG화학은 R4에서 `spread_recovery_hope`를 낮추고, `actual_spread`, `operating_rate`, `feedstock_security`, `FCF_after_restructuring`을 높여야 한다.

---

## Case C — SK이노베이션 `cyclical_success / not_structural`

```text
symbol = 096770
archetype = REFINING_OIL_SPREAD / LNG_ENERGY_TRADING_DISTRIBUTION
case_type = cyclical_success
```

SK이노베이션은 R4 정유 스프레드 판정에 좋은 케이스다. 2025년 1분기에는 예상 밖 영업손실 450억 원을 냈고, 정유·석유개발·윤활유 이익이 감소했으며, 석유화학과 배터리 손실도 이어졌다. 당시 회사는 2분기 정제마진이 점진적으로 개선될 수 있다고 봤다. ([Reuters][4])

반면 2026년 1분기에는 2.2조 원 영업이익을 기록하며 전년 동기 300억 원 손실에서 크게 반전했고, LSEG SmartEstimate 1.4조 원을 웃돌았다. 다만 회사는 정유사업 회복이 느릴 수 있다고 경고했다. ([Reuters][5])

### stage date 후보

```text
Stage 1:
2025-04-30
- 정제마진 개선 기대
- 1Q 손실에도 2Q margin 회복 언급

Stage 2:
2026-05-13
- 1Q 2026 영업이익 2.2조 원
- 실적 반전 확인

Stage 3:
보류
- 정유마진은 cyclical
- 전쟁/공급차질성 margin improvement는 구조적 Green 아님
- FCF, 배당/자사주, 장기 margin floor 확인 필요

Stage 4B:
2026년 geopolitical refining squeeze로 정유주 급등했다면 4B-watch

Stage 4C:
정제마진 정상화 / 공급 복구 / crude cost shock 발생 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2026-05-13 OHLC backfill 필요.

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
alignment = cyclical_success
rerating_result = cyclical_rerating
stage_failure_type = stage2_watch_success
```

### 교정 포인트

정유는 R4에서 Stage 3를 매우 조심해야 한다.

```text
정제마진 개선
= Stage 2 가능

Stage 3 조건:
multi-quarter margin floor
FCF
deleveraging
shareholder return
non-refining mix 개선
```

전쟁이나 일시적 공급차질로 생긴 spread는 구조적 E2R이 아니라 `cyclical_success`다.

---

## Case D — 고려아연 `event_premium + strategic_material_success_candidate`

```text
symbol = 010130
archetype = NONFERROUS_STRATEGIC_METALS / EVENT_PREMIUM_GOVERNANCE_OVERLAY
case_type = event_premium + success_candidate
```

고려아연은 R4에서 가장 복잡한 케이스다. 한쪽은 세계 1위급 비철금속·전략광물 플랫폼이고, 다른 한쪽은 경영권 분쟁·자사주·유상증자·규제 개입이 섞인 event premium이다.

2024년 9월 MBK파트너스와 영풍은 고려아연 지분 공개매수를 시작했고, 공개매수가 660,000원 대비 직전 종가 556,000원에서 고려아연 주가는 당일 약 19.8% 상승했다. 이 구간은 구조적 Stage 3가 아니라 경영권 event premium으로 분류해야 한다. ([Reuters][6])

2024년 10월 고려아연은 MBK 측에 맞서 2.663조 원 규모 자사주 매입·소각 계획과 Bain Capital의 별도 지분 매입을 발표했다. 이후 2024년 11월에는 1.8B달러 규모 신주발행 계획이 금융감독당국의 정정 요구로 중단됐고, 주가는 최대 8% 하락했다. ([월스트리트저널][7])

다만 2025년 12월에는 미국 정부가 중국 의존도를 줄이기 위해 고려아연의 74억 달러 규모 critical minerals processing plant를 지원한다는 보도가 나왔다. 해당 시설은 안티모니, 게르마늄, 갈륨, 아연, 납, 구리, 귀금속 등을 생산하고 2027~2029년 단계적으로 가동될 예정이며, 주가는 보도 후 최대 27% 상승했다. 이것은 R4에서 Stage 2 strategic-material evidence로 볼 수 있다. ([Financial Times][8])

### stage date 후보

```text
Stage 1:
2024-09-13
- MBK/영풍 공개매수
- 경영권 분쟁 / governance event

Stage 2:
2025-12-15
- 미국 critical minerals plant 지원
- non-China strategic metals supply chain evidence

Stage 3:
보류
- 공장 가동은 2027~2029년
- capex, financing, JV 구조, FCF, dilution risk 확인 필요

Stage 4B:
2024-09~10
- 공개매수 / 자사주 / Bain 참여로 가격이 먼저 급등
- event premium 4B-watch

Stage 4C:
2024-11-06 watch
- 대규모 신주발행 계획에 규제 정정 요구
- 자본배분·공시 신뢰도 watch
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage1_price_anchor:
2024-09-12 종가 556,000원
2024-09-13 공개매수가 660,000원 / 주가 +19.8%

stage2_price:
2025-12-15 OHLC backfill 필요.

MFE / MAE:
Event 기준과 strategic-material Stage2 기준을 분리해 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = event_premium + success_candidate
rerating_result = event_premium / strategic_material_watch
stage_failure_type = should_not_be_green_until_project_fcf
```

### 교정 포인트

고려아연은 R4에서 `strategic metals` 점수를 올릴 수 있지만, governance event premium과 섞으면 안 된다.

```text
공개매수 / 자사주 / 경영권 분쟁:
event premium

미국 critical minerals plant:
Stage 2 strategic visibility

Stage 3 조건:
financing clarity
capex burden
commercial operation
offtake
margin
FCF
dilution risk 통과
```

---

## Case E — POSCO홀딩스 `success_candidate / lithium cycle watch`

```text
symbol = 005490
archetype = LITHIUM_BATTERY_RAW_MATERIAL / RARE_METALS_PRICE_FLOOR_OFFTAKE
case_type = success_candidate + cyclical_watch
```

POSCO홀딩스는 R4에서 리튬 원료 확보와 commodity cycle을 분리하는 케이스다. 2025년 11월 호주 Mineral Resources는 리튬 사업 일부 지분 30%를 POSCO에 7.65억 달러에 매각한다고 발표했다. 이 거래는 POSCO가 Wodgina와 Mt Marion 리튬 광산에 간접 15% 지분을 갖고, 지분만큼 spodumene concentrate를 받는 구조다. ([Reuters][9])

하지만 같은 보도는 리튬 가격이 2022년 톤당 6,000달러 이상에서 2025년 6월 약 610달러까지 떨어졌고, 8월 약 880달러로 반등했지만 여전히 2022년 고점에는 크게 못 미쳤다고 설명했다. 즉 POSCO의 리튬 투자는 장기 원료 확보로 Stage 2는 가능하지만, 리튬 가격 반등만으로 Stage 3를 주면 안 된다. ([Reuters][9])

### stage date 후보

```text
Stage 1:
2023~2025
- 포스코 리튬 / 배터리 원료 내재화 기대

Stage 2:
2025-11-11
- MinRes lithium JV stake deal
- Wodgina / Mt Marion 간접 지분
- spodumene concentrate 확보

Stage 3:
보류
- 리튬 가격 저점 매수는 장기 옵션
- 실제 lithium hydroxide margin, offtake, FCF 확인 필요

Stage 4B:
리튬 가격 이벤트로 주가가 급등한 구간이 있으면 4B-watch

Stage 4C:
리튬 가격 재하락 / 프로젝트 write-down / 수요 부진 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2025-11-11 OHLC backfill 필요.

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
alignment = success_candidate / cyclical_watch
rerating_result = unknown
stage_failure_type = stage2_watch_success 후보
```

### 교정 포인트

POSCO홀딩스는 R4에서 `resource_security`와 `commodity_price_event`를 분리해야 한다.

```text
원료 지분 확보:
Stage 2 가능

Stage 3 조건:
cost-competitive supply
downstream margin
offtake
FCF
lithium price floor
project execution
```

---

## Case F — OCI홀딩스 `event_premium / insufficient_evidence`

```text
symbol = 010060
archetype = POLYSILICON_NON_CHINA_SUPPLY_OPTION
case_type = event_premium / insufficient_evidence
```

OCI홀딩스는 R4에서 “비중국 폴리실리콘”과 “미확정 AI/SpaceX 테마”를 분리하는 케이스다. 2026년 4월 Reuters는 OCI홀딩스의 말레이시아 자회사 OCI TerraSus가 SpaceX와 다년 폴리실리콘 공급계약을 논의 중이라는 한국 매체 보도를 전했다. 하지만 SpaceX는 확인하지 않았고, OCI홀딩스 대변인도 보도를 확인할 수 없다고 밝혔다. ([Reuters][10])

이와 별개로 중국 폴리실리콘 업계는 과잉공급을 줄이기 위해 약 1/3 생산능력 폐쇄와 OPEC식 quota를 논의했고, 해당 기대만으로 폴리실리콘 가격이 급등했다. 이건 R4의 supply discipline 후보지만, OCI홀딩스 Stage 3로 직접 연결하려면 실제 계약, 가격, 물량, 마진이 필요하다. ([Reuters][11])

### stage date 후보

```text
Stage 1:
2026-04-14
- OCI TerraSus / SpaceX supply talk media report
- non-China polysilicon / IRA / AI data center solar narrative

Stage 2:
보류
- 회사 확인 없음
- 계약금액, 물량, 기간, 가격 없음

Stage 3:
없음
- 미확정 media report로 Green 금지

Stage 4B:
보도에 주가가 급등했다면 price-only / event premium watch

Stage 4C:
없음
- 단, 중국 공급 재확대 / 폴리실리콘 가격 재하락 / 계약 불발 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage1_price:
2026-04-14 OHLC backfill 필요.

MFE / MAE:
Stage 1 이벤트 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = event_premium / unknown_insufficient_evidence
rerating_result = event_premium 후보
stage_failure_type = stage1_attention_only
```

### 교정 포인트

OCI홀딩스는 `SpaceX`, `AI data center`, `non-China polysilicon` 같은 단어만으로 Stage 3를 주면 안 된다.

```text
필수:
confirmed contract
volume
price
duration
customer confirmation
margin
FCF
```

---

## Case G — 풍산 `event_premium / price_moved_without_evidence`

```text
symbol = 103140
archetype = COPPER_PROCESSING_PLUS_DEFENSE / EVENT_PREMIUM_GOVERNANCE_OVERLAY
case_type = event_premium / price_moved_without_evidence
```

풍산은 R4/R1 교차 케이스다. 구리 가공과 방산 탄약이 같이 있어서 전략금속 + 방산 프리미엄으로 보기 쉽다. 2026년 4월 Reuters는 한화에어로스페이스가 풍산 방산사업부 인수를 검토했고, 거래 규모가 1.5조 원가량일 수 있다는 보도를 전했다. 하지만 며칠 뒤 한화에어로스페이스는 검토를 중단했고, 풍산도 방산사업부 매각 계획이 없다고 공시했다. ([Reuters][12])

이건 R4에서 아주 좋은 event premium 반례다. 구리·탄약이라는 테마는 강하지만, 매각·재평가 이벤트가 부정되면 가격경로는 꺾일 수 있다.

### stage date 후보

```text
Stage 1:
2026-04-03
- 한화에어로스페이스 풍산 방산부문 인수 검토 보도
- copper + defense premium

Stage 2:
없음
- 회사는 다양한 구조개편 방안을 검토한다고 했지만 확정 없음

Stage 3:
없음
- 매각 부인
- copper/defense earnings, FCF, margin 확인 전 Green 금지

Stage 4B:
2026-04-03 보도 직후 가격 급등 시 event premium watch

Stage 4C:
2026-04-09
- 한화 인수 검토 중단
- 풍산 매각 계획 부인
- event thesis break
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage1_price:
2026-04-03 OHLC backfill 필요.

MFE_5D / 20D:
event premium 검증용으로 필요.

MAE_30D / 90D:
event fade 검증 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = price_moved_without_evidence / thesis_break_event
rerating_result = event_premium
stage_failure_type = should_have_been_stage1_only
```

### 교정 포인트

풍산은 `copper + defense`가 좋아 보여도, 거래/재평가 이벤트가 확정되지 않으면 Stage 3가 아니라는 케이스다.

```text
올릴 축:
actual copper spread
ammunition order
margin
export contract
FCF

내릴 축:
sale rumor
management premium rumor
unconfirmed restructuring
```

---

# 5. 이번 R4 case별 요약표

| case     | 분류                                          | Stage 3 판정 |                             4B/4C 판정 | 가격경로 1차 판단                       |
| -------- | ------------------------------------------- | ---------: | -----------------------------------: | -------------------------------- |
| 롯데케미칼    | 4C-thesis-break / restructuring watch       |         없음 | 2024 손실·공급과잉은 4C, 2026 구조조정은 Stage 2 | 구조조정 relief이지 Green 아님           |
| LG화학     | failed_rerating / petrochemical 4C-watch    |         없음 |                      손실·NCC 중단 watch | spread 회복 기대만으로 Green 금지         |
| SK이노베이션  | cyclical_success                            |         보류 |               정유마진 공급차질성 4B-watch 가능 | 정유 반전은 Stage 2, 구조적 Stage 3 아님   |
| 고려아연     | event_premium + strategic success_candidate |         보류 |       공개매수/자사주/증자는 event/4B/4C-watch | critical minerals plant는 Stage 2 |
| POSCO홀딩스 | success_candidate / lithium cycle watch     |         보류 |                  리튬 가격 이벤트는 4B-watch | 원료확보는 Stage 2, FCF 전 Green 금지    |
| OCI홀딩스   | event_premium / insufficient                |         없음 |         미확정 SpaceX 보도는 price-only 후보 | 회사 확인 전 Stage 3 금지               |
| 풍산       | event_premium / event-thesis-break          |         없음 |                매각 루머 후 부인 = event 4C | copper/defense 테마만으로 Green 금지    |

---

# 6. 각 case별 stage date 후보 요약

```text
롯데케미칼:
Stage 1 = 2024~2025 석유화학 바닥론 / 구조조정 기대
Stage 2 = 2025-11-26 구조조정 계획 제출
Stage 3 = 보류
Stage 4B = 구조조정 기대 과열 시 후보
Stage 4C = 2025-02-07 2024 영업손실 확대 / 공급과잉

LG화학:
Stage 1 = 2024~2025 석유화학 회복 기대
Stage 2 = 2025-12-19 구조조정 계획 제출
Stage 3 = 보류
Stage 4B = 없음
Stage 4C = 2025-02-07 petrochemical loss / 2026-03-23 NCC 원료차질 watch

SK이노베이션:
Stage 1 = 2025-04-30 정제마진 개선 기대
Stage 2 = 2026-05-13 1Q 2026 영업이익 2.2조 원
Stage 3 = 보류
Stage 4B = geopolitical refining squeeze 급등 시 후보
Stage 4C = 정제마진 정상화 / 공급 복구 시 후보

고려아연:
Stage 1 = 2024-09-13 MBK/영풍 공개매수
Stage 2 = 2025-12-15 미국 critical minerals plant
Stage 3 = 보류
Stage 4B = 2024-09~10 공개매수/자사주 event premium
Stage 4C = 2024-11-06 신주발행 정정 요구 watch

POSCO홀딩스:
Stage 1 = 2023~2025 리튬 원료 내재화 기대
Stage 2 = 2025-11-11 MinRes lithium JV stake deal
Stage 3 = 보류
Stage 4B = lithium price rally 과열 시 후보
Stage 4C = lithium price 재하락 / project write-down 시 후보

OCI홀딩스:
Stage 1 = 2026-04-14 SpaceX polysilicon talks media report
Stage 2 = 보류
Stage 3 = 없음
Stage 4B = 미확정 보도 급등 시 price-only
Stage 4C = 계약 불발 / polysilicon price 재하락 시 후보

풍산:
Stage 1 = 2026-04-03 한화 방산부문 인수 검토 보도
Stage 2 = 없음
Stage 3 = 없음
Stage 4B = 보도 직후 가격 급등 시 event premium
Stage 4C = 2026-04-09 인수 검토 중단 / 매각계획 부인
```

---

# 7. 가격경로 검증

R4는 정확한 OHLC backfill 없이 수익률을 확정하면 안 된다. 특히 소재주는 commodity price, event premium, 구조조정 relief, policy shock이 섞여 있어서 stage별 가격을 분리해야 한다.

| case     | stage3_price | MFE/MAE                                | below_stage3 | peak/drawdown                             |
| -------- | -----------: | -------------------------------------- | ------------ | ----------------------------------------- |
| 롯데케미칼    |   Stage 3 없음 | Stage 2 구조조정 기준 backfill               | N/A          | 2024~2026 drawdown/relief backfill        |
| LG화학     |   Stage 3 없음 | Stage 2 구조조정 기준 backfill               | N/A          | NCC halt / petrochemical loss 구간 backfill |
| SK이노베이션  |   Stage 3 없음 | Stage 2 실적반전 기준 backfill               | N/A          | refining margin peak/drawdown backfill    |
| 고려아연     |   Stage 3 없음 | event / strategic plant 기준 분리 backfill | N/A          | 공개매수 peak / 증자 shock backfill             |
| POSCO홀딩스 |   Stage 3 없음 | lithium JV 기준 backfill                 | N/A          | lithium cycle peak/drawdown backfill      |
| OCI홀딩스   |   Stage 3 없음 | SpaceX media report 기준 backfill        | N/A          | event fade backfill                       |
| 풍산       |   Stage 3 없음 | 인수 루머 기준 MFE_5D/20D 필요                 | N/A          | 부인 이후 drawdown backfill                   |

핵심은 이거다.

```text
R4는 commodity/event 가격경로를 Stage 3로 오인하면 망가진다.
Stage 3는 price floor / offtake / cost curve / FCF / supply discipline이 확인될 때만 준다.
```

---

# 8. score-price alignment 판정

```text
롯데케미칼:
alignment = thesis_break_then_restructuring_watch
rerating_result = no_rerating / restructuring_relief_candidate

LG화학:
alignment = thesis_break / evidence_good_but_price_failed 후보
rerating_result = failed_rerating

SK이노베이션:
alignment = cyclical_success
rerating_result = cyclical_rerating
Stage 3가 아니라 Stage 2 watch

고려아연:
alignment = event_premium + success_candidate
경영권 이벤트와 strategic metals project를 분리해야 함

POSCO홀딩스:
alignment = success_candidate / cyclical_watch
리튬 원료확보는 Stage 2, lithium price event는 Green 아님

OCI홀딩스:
alignment = event_premium / unknown_insufficient_evidence
미확정 SpaceX 보도는 Stage 1 attention

풍산:
alignment = price_moved_without_evidence / thesis_break_event
인수 루머는 Stage 3 증거가 아님
```

---

# 9. 점수비중 교정

## 올릴 축

```text
actual_product_spread +4
fcf_after_working_capital +4
supply_discipline_confirmed +4
capacity_shutdown_confirmed +3
price_floor_or_offtake +4
cost_curve_advantage +3
strategic_customer_or_government_offtake +3
inventory_normalization +3
capital_return_from_cashflow +2
```

R4에서 가장 중요한 건 “가격이 올랐다”가 아니라 **그 가격이 지속될 수 있는 구조가 있는가**다.

## 내릴 축

```text
commodity_price_up_only -5
restructuring_plan_without_margin -3
policy_support_without_fcf -3
tender_offer_or_governance_premium -4
unconfirmed_media_report -4
capacity_cut_expectation_only -3
lithium_price_event -4
refining_margin_geopolitical_shock -3
customer_or_contract_unconfirmed -3
capex_heavy_project_pre_revenue -3
```

고려아연, OCI홀딩스, 풍산 때문에 `event premium` 감점축은 강해야 한다. 롯데케미칼·LG화학 때문에 `restructuring_plan_without_margin`도 Stage 3를 막아야 한다.

## Green gate 강화 조건

R4 Stage 3-Green은 앞으로 이렇게 줘야 한다.

```text
필수 gate:
1. product spread 개선이 실제 확인됨
2. cost curve advantage 있음
3. supply discipline 또는 capacity shutdown이 확인됨
4. inventory build가 아님
5. FCF 전환 또는 현금흐름 개선
6. price floor / offtake / long-term contract 존재
7. EPS revision이 1개 분기 이벤트가 아니라 중기 경로로 연결
8. capex 부담과 dilution risk 통과

금지:
commodity price spike
tender offer premium
governance battle
정책 지원 기대
미확정 media report
구조조정 계획만 있음
리튬/폴리실리콘 가격 이벤트
전쟁성 refining margin
```

## 4B 조기감지 조건

```text
4B-watch:
원자재 가격 급등 후 관련주 동반 급등
구조조정 기대만으로 multiple 확장
공개매수 / 자사주 / governance battle로 주가 급등
리튬/폴리실리콘 supply discipline 뉴스로 소재주 동반 급등
정제마진 공급차질성 spike

4B-elevated:
실적보다 가격이 먼저 감
보고서가 commodity upside만 반복
신규 CAPEX 발표로 dilution/FCF 부담 커짐
계약보다 정책/루머가 주가를 끌고 감

4B-graduated:
spread peak 후 이익 normalize
재고 이익이 사라짐
증설 재개 / 공급 복구
좋은 실적에도 주가 반응 둔화
```

## 4C hard gate 조건

```text
spread reversal
china_oversupply
middle_east_capacity_overhang
inventory_build
NCC 가동 중단
계약/매각/공개매수 이벤트 불발
regulator revision order
대규모 신주발행 / dilution
commodity price 재하락
project capex overrun
offtake 부재
FCF 악화
```

풍산의 매각 루머 부인, 고려아연의 신주발행 정정 요구, 롯데케미칼/LG화학의 손실과 공급과잉은 전부 R4 RedTeam에서 강하게 반영해야 한다.

---

# 10. shadow-only 기록

이번 R4 Loop 7은 production scoring에 바로 반영하면 안 된다.

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
needs_ohlc_backfill = true
```

레포에 넣는다면 파일명은 이렇게 가는 게 자연스럽다.

```text
docs/round/round_123.md
docs/checkpoints/checkpoint_28a_round123_r4_loop7_materials_spread_strategic_price_validation.md
src/e2r/sector/round123_r4_loop7_materials_spread_strategic.py
data/e2r_case_library/cases_r4_loop7_round123.jsonl
data/sector_taxonomy/score_weight_profiles_round123_r4_loop7_v7.csv
output/e2r_round123_r4_loop7_materials_spread_strategic/
```

---

# 이번 R4 Loop 7 결론

R4 점수표는 방향이 맞지만, **Stage 3-Green은 더 보수적으로 줘야 한다.**
R4의 가장 큰 적은 “가격 이벤트를 구조 변화로 착각하는 것”이다.

이번 라운드의 핵심 교정은 이거다.

```text
1. 석유화학 구조조정은 Stage 2 가능하지만,
   spread / OPM / FCF 확인 전 Stage 3가 아니다.

2. 정유마진 개선은 cyclical_success일 수 있지만,
   전쟁·공급차질성 margin spike는 구조적 Green이 아니다.

3. 전략광물은 좋은 테마지만,
   offtake / price floor / capex / FCF / dilution을 확인해야 한다.

4. 리튬·폴리실리콘 가격 이벤트는 Stage 1~2 attention이다.
   가격 반등 자체로 Green을 주면 false_positive가 커진다.

5. 경영권 분쟁, 공개매수, 자사주, 매각 루머는 event premium이다.
   실제 EPS/FCF 체급 변화와 분리해야 한다.

6. R4의 4C는 spread reversal, 중국/중동 공급과잉, 재고 증가,
   구조조정 실패, dilution, 미확정 계약 불발에서 온다.
```

한 문장으로 압축하면:

> **R4에서 진짜 Stage 3는 “원자재 가격이 올랐다”가 아니라, 가격·원가·공급규율·offtake·FCF가 잠겨서 이익 체급이 구조적으로 바뀌는 순간이다.**
> **지금 R4는 Green 발굴보다 commodity/event false Green 차단이 더 중요한 구간이다.**

[1]: https://www.reuters.com/markets/commodities/south-korean-petrochemical-firms-profits-plunge-2024-oversupply-persists-2025-02-07/?utm_source=chatgpt.com "South Korean petrochemical firms' profits plunge in 2024 as oversupply persists"
[2]: https://www.reuters.com/world/asia-pacific/south-koreas-hd-hyundai-lotte-chemical-submit-plan-restructure-petrochemical-2025-11-26/?utm_source=chatgpt.com "South Korea's HD Hyundai, Lotte Chemical submit plan to restructure petrochemical businesses"
[3]: https://www.reuters.com/world/asia-pacific/lg-chem-submits-petrochem-restructuring-plan-government-2025-12-19/?utm_source=chatgpt.com "LG Chem submits petrochem restructuring plan to government"
[4]: https://www.reuters.com/business/energy/sk-innovation-expects-refining-margins-gradually-improve-q2-2025-04-30/?utm_source=chatgpt.com "SK Innovation sinks to Q1 operating loss, sees refining margins improving"
[5]: https://www.reuters.com/world/asia-pacific/sk-innovation-warns-refining-recovery-take-time-beats-q1-profit-estimates-2026-05-13/?utm_source=chatgpt.com "SK Innovation warns refining recovery to take time, beats Q1 profit estimates"
[6]: https://www.reuters.com/markets/deals/private-equity-mbk-young-poong-launch-15-bln-tender-offer-korea-zinc-shares-2024-09-13/?utm_source=chatgpt.com "Private equity MBK, Young Poong launch $1.5 bln tender offer for Korea Zinc shares"
[7]: https://www.wsj.com/business/korea-zinc-teams-up-with-bain-capital-to-thwart-takeover-bid-e58c98a8?utm_source=chatgpt.com "Korea Zinc Teams Up With Bain Capital to Thwart Takeover Bid"
[8]: https://www.ft.com/content/d885ab55-b4f8-4c8f-a213-94f2778863ac?utm_source=chatgpt.com "US backs $7.4bn critical minerals smelter to counter China"
[9]: https://www.reuters.com/business/energy/australias-minres-sell-30-lithium-jv-stake-posco-765-mln-2025-11-11/?utm_source=chatgpt.com "Australia's MinRes inks $765 million deal with POSCO for lithium JV stake, shares surge"
[10]: https://www.reuters.com/world/asia-pacific/unit-south-koreas-oci-talks-with-spacex-supply-polysilicon-media-says-2026-04-14/?utm_source=chatgpt.com "Unit of South Korea's OCI in talks with SpaceX to supply polysilicon, media says"
[11]: https://www.reuters.com/sustainability/climate-energy/top-china-polysilicon-firms-plan-shut-third-production-capacity-set-opec-style-2025-07-31/?utm_source=chatgpt.com "Top China polysilicon firms plan to shut a third of production capacity, set OPEC-style output quotas, GCL says"
[12]: https://www.reuters.com/world/asia-pacific/hanwha-seeks-buy-poongsans-ammunition-business-about-11-billion-newspaper-says-2026-04-03/?utm_source=chatgpt.com "Hanwha seeks to buy Poongsan's ammunition business for about $1.1 billion, newspaper says"
