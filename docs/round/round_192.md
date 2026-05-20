좋아. 이 프롬프트 기준으로 **R1 다음 라운드 = R1 Loop 7 가격경로 검증 라운드**로 진행하면 된다.

이번 답변은 “완성 패치”라기보다 **다음 레포 패치에 넣을 수 있는 R1 calibration draft**로 봐줘. 정확한 MFE/MAE는 KRX/KIS/Yahoo/Kiwoom OHLC로 backfill해야 하고, 여기서는 공개 기사에 남은 stage-price anchor와 이벤트 가격 반응을 기준으로 1차 판정한다. 억지로 수치를 채우지 않고, 모르는 값은 `needs_price_backfill`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R1 = 산업재·수주·인프라
large_sector = INDUSTRIAL_ORDERS_INFRA
목표 = R1의 Stage 3 / 4B / 4C가 실제 가격경로와 맞았는지 검증
```

R1의 기본 영역은 계약, 수주잔고, 전력망, 방산, 조선, 철도, 원전, 데이터센터 전력설비다. Round 40 지도에서도 R1 validation focus는 `contract_amount_to_sales`, `contract_duration`, `backlog`, `delivery_schedule`, `op_eps_revision`, `margin`으로 잡혀 있다. 

Round 119 기준으로 R1에서 부족한 증거는 단순 `order_headline`이나 `power_grid_theme`이고, 진짜 필요한 증거는 `contract_quality`, `margin`, `eps_fcf_revision`, `price_path`다. Green blocker는 `contract_cancelled`, `margin_unknown`, `capacity_relief`다. 

---

# 2. 대상 canonical archetype

이번 R1 Loop 7에서 볼 archetype은 새로 늘리는 게 아니라, 기존 R1 구조 중 가격경로 검증이 필요한 축 위주로 잡는다.

```text
DEFENSE_GOVERNMENT_BACKLOG
DEFENSE_LOCAL_PRODUCTION_PLATFORM
DEFENSE_INTERCEPTOR_COMBAT_VALIDATION
CONTRACT_BACKLOG_INDUSTRIAL
SHIPBUILDING_OFFSHORE_BACKLOG
SHIP_MRO_RECURRING_PLATFORM
AI_DATA_CENTER_POWER_EQUIPMENT
POWER_EQUIPMENT_BACKLOG_TO_FCF
PRICE_ONLY_RALLY
CROWDING_4B_WATCH
THESIS_BREAK_4C
```

이번 라운드에서 핵심은 **“수주 뉴스”와 “실제 리레이팅 가능한 계약/실적 경로”를 분리하는 것**이다.

---

# 3. deep sub-archetype

```text
방산 수출:
- K2 tank export
- K9 / Chunmoo export
- M-SAM / Cheongung-II export
- FA-50 / KF-21 export
- European rearmament
- Middle East air-defense demand
- local production / technology transfer
- export credit / financing
- production slot / delivery schedule

조선 / 해양:
- LNG carrier / offshore backlog
- naval shipbuilding
- ship MRO
- KRW trillion shipbuilding contract
- margin visibility
- delivery slot quality
- sanction / geopolitical shock

전력망 / 전력설비:
- transformer shortage
- switchgear
- power cable
- data-center power equipment
- target-price rerating
- capacity bottleneck
- margin and EPS revision

가격검증 overlay:
- price-only IPO rally
- contract headline without margin
- 4B crowded defense rally
- capital raise / dilution shock
- sanction / contract delay / financing failure
```

---

# 4. 국장 신규 후보 case

이번에는 대표 전력기기 성공사례인 HD현대일렉트릭, 효성중공업, 일진전기 같은 기존 case-library 중심축은 의도적으로 뒤로 뺐다. 대신 R1 안에서 **방산·조선·MRO·전력장비의 덜 검증된 가격경로**를 본다.

## Case A — 현대로템 `structural_success`

```text
symbol = 064350
archetype = DEFENSE_GOVERNMENT_BACKLOG / DEFENSE_LOCAL_PRODUCTION_PLATFORM
case_type = structural_success
```

현대로템은 R1에서 가장 좋은 가격검증 후보 중 하나다. 2024년 4월 이미 폴란드 K2 전차 납품이 1분기 실적을 밀어올릴 가능성이 보였고, 당시 KB증권은 1분기 영업이익이 전년 대비 85% 증가해 컨센서스를 웃돌 수 있다고 봤다. 기사에 나온 당시 주가는 41,300원이었다. ([월스트리트 저널][1])

이후 2025년 6월에는 폴란드에 K2 전차 180대를 공급하는 약 60억 달러 규모 계약이 임박했다는 보도가 나왔고, 2025년 8월에는 폴란드가 현대로템과 180대 추가 계약을 체결했다. 해당 계약은 2022년 180대 계약에 이은 두 번째 대형 계약이고, 일부 물량은 폴란드 현지 생산이 포함됐다. ([Reuters][2])

### stage date 후보

```text
Stage 1:
2022년 폴란드 1차 K2 계약 이후
- 테마 / 산업 변화 포착

Stage 2:
2024-04-09
- 폴란드 K2 납품이 실적에 반영될 수 있다는 기대
- 영업이익 YoY +85% 예상
- stage2_price_anchor = 41,300원

Stage 3:
2024-04-09 ~ 2024년 2Q 실적 확인 구간
- 단순 방산 테마가 아니라 납품 → 매출 → 영업이익으로 연결
- 다만 정확한 Stage 3 확정일은 실적 발표일 OHLC backfill 필요

Stage 4B:
2025-08-01 이후
- 2차 폴란드 계약 확정
- 유럽 방산 리레이팅이 대중적으로 확인된 구간

Stage 4C:
없음
```

### 가격경로 검증

```text
stage3_price:
41,300원 anchor 사용 가능

MFE_30D:
needs_ohlc_backfill

MFE_90D:
needs_ohlc_backfill

MFE_180D:
needs_ohlc_backfill

MFE_1Y / 2Y:
수백 % 이상 가능성이 매우 높음.
다만 정확한 값은 OHLC backfill 필요.

MAE:
needs_ohlc_backfill

below_stage3_price_flag:
needs_ohlc_backfill

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

FT는 2026년 방산 랠리 기사에서 현대로템 주가가 같은 기간 6배 이상 올랐다고 보도했다. 이건 Stage 3가 2024년 실적 전환 구간에서 잡혔다면, E2R 원칙상 “리레이팅 전 매수 → 대형 MFE”가 실제로 있었을 가능성이 높다는 뜻이다. ([Financial Times][3])

### score-price alignment

```text
alignment = aligned
rerating_result = true_rerating
stage_failure_type = green_success 후보
```

현대로템은 R1 점수표에서 `contract_quality`, `delivery_schedule`, `government_backlog`, `op_eps_revision`, `price_path_alignment` 가중치를 올려주는 성공사례로 쓸 수 있다.

---

## Case B — LIG넥스원 `success_candidate / 4B-watch 후보`

```text
symbol = 079550
archetype = DEFENSE_INTERCEPTOR_COMBAT_VALIDATION
case_type = success_candidate
```

LIG넥스원은 천궁-II / M-SAM II 수출 구조다. 2024년 9월 LIG넥스원은 이라크에 중거리 지대공 미사일 방어체계를 수출하는 3.71조 원, 약 28억 달러 규모 계약을 따냈다. 이 계약은 앞서 사우디아라비아의 32억 달러 M-SAM II 계약에 이은 것이고, 발표 당일 주가는 장 초반 3.6% 상승했다. ([Reuters][4])

2026년에는 이란전쟁/중동 미사일 방어 수요와 맞물려 Cheongung-II가 저가 Patriot 대안으로 주목받았고, FT는 LIG넥스원이 전쟁 시작 이후 거의 47% 상승했다고 보도했다. ([Financial Times][3])

### stage date 후보

```text
Stage 1:
2024-02
- 사우디 M-SAM II 계약 이후 방공 수출 테마 강화

Stage 2:
2024-09-20
- 이라크 3.71조 원 계약
- 중동 수출 레퍼런스 추가

Stage 3:
2024-09-20 이후 실적/수주잔고 반영 확인 구간
- 계약 자체는 강하지만, 매출 인식·마진·EPS revision 확인 필요
- 정확한 Stage 3 확정은 실적자료 backfill 필요

Stage 4B:
2026년 이란전쟁 이후
- 전투검증 / 미사일방어 수요가 시장에 넓게 알려진 구간

Stage 4C:
없음
```

### 가격경로 검증

```text
stage3_price:
needs_price_backfill
기사에는 발표일 +3.6% 반응만 있음.

MFE_30D / 90D / 180D:
needs_ohlc_backfill

MFE_1Y:
2026년 전쟁 이후 +47% 구간 확인.
단, Stage 3 기준 정확한 MFE는 backfill 필요.

MAE:
needs_ohlc_backfill

below_stage3_price_flag:
needs_ohlc_backfill

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = aligned 후보
rerating_result = true_rerating 후보
stage_failure_type = yellow_success 또는 green_success 후보
```

LIG넥스원은 현대로템보다 Stage 3-Green을 더 조심해야 한다. 계약 규모는 강하지만, interceptor 체계는 납기, 생산능력, 수출국별 정치 리스크, 매출 인식 시차가 크다. 그래서 `contract_signed`만으로 Green을 주기보다 `contract_signed + backlog + margin + EPS revision + delivery visibility`가 같이 나와야 한다.

---

## Case C — 한화에어로스페이스 `structural_success_but_4B_timing_test`

```text
symbol = 012450
archetype = DEFENSE_GOVERNMENT_BACKLOG / CROWDED_RERATING_4B_WATCH
case_type = structural_success + 4B-watch
```

한화에어로스페이스는 R1에서 아주 좋은 4B timing test다. 2024년 3월 이미 KSLV-III 우주발사체 사업 기대와 방산 수출 확대 기대가 같이 붙었고, 당시 주가는 장중 217,000원까지 올랐다. 기사에서는 방산 수출이 2024년에 46% 증가할 수 있고, 영업이익률도 2023년 7.5%에서 2024년 9.0%로 개선될 수 있다는 전망이 나왔다. ([월스트리트 저널][5])

2024년 4월에는 폴란드에 72대 천무를 공급하는 16.4억 달러 계약이 발표됐다. 이 계약은 2022년 한국-폴란드 220억 달러 방산 패키지의 일부였고, 별도 금융계약 체결 후 효력이 발생하는 구조였다. ([Reuters][6])

2025년 3월에는 3.6조 원 규모 유상증자 발표로 주가가 하루 13% 급락했고, 감독당국은 이후 증권신고서 정정을 요구했다. 이건 E2R상 4B-watch 또는 capital allocation shock으로 잡아야 하는 이벤트였다. ([Reuters][7])

그런데 이게 곧바로 4C는 아니었다. 2025년 4월 회사는 증자 규모를 2.3조 원으로 줄였고, 동시에 2025년 매출 30조 원, 영업이익 3조 원을 제시했다. 이후 2026년 1월에는 노르웨이가 한화에어로스페이스 천무 체계를 20억 달러에 도입하기로 했다. ([Reuters][8])

### stage date 후보

```text
Stage 1:
2023~2024
- 유럽 재무장 / 폴란드 방산 수출 / 우주발사체 기대

Stage 2:
2024-03-22
- 방산 수출 증가, OPM 개선 기대, KSLV-III 기대
- stage2_price_anchor = 217,000원 장중

Stage 3:
2024-04-25
- 폴란드 천무 16.4억 달러 계약
- 단, financing 조건 확인 필요
- stage3 확정은 실적/EPS revision backfill 필요

Stage 4B:
2025-03-21
- 주가가 이미 크게 오른 뒤 대형 유상증자 발표
- 13% 급락
- capital allocation / dilution shock

Stage 4C:
없음
- 증자 충격은 있었지만 계약·수요·이익 thesis가 바로 훼손되지는 않음
```

### 가격경로 검증

```text
stage3_price:
217,000원 ~ 243,500원 anchor 사용 가능
- 2024-03-22 장중 217,000원
- 2024-06-28 243,500원 보도

MFE_30D / 90D:
needs_ohlc_backfill

MFE_180D / 1Y / 2Y:
큰 폭의 MFE 가능성이 높음.
FT 보도 기준 한화에어로스페이스는 187,500원에서 1,435,000원까지 오른 구간이 확인됨.

MAE:
2025-03-21 유상증자 발표 후 -13% 이벤트 확인

below_stage3_price_flag:
아마 false 가능성이 높지만 OHLC backfill 필요

peak_price:
1,435,000원 anchor 확인

drawdown_after_peak:
needs_ohlc_backfill
```

FT는 2026년 기사에서 한화에어로스페이스 주가가 187,500원에서 1,435,000원까지 올랐다고 보도했다. ([Financial Times][3])

### score-price alignment

```text
alignment = aligned
rerating_result = true_rerating
stage_failure_type = green_success
4B_result = early_4B_watch_not_hard_exit
```

여기서 중요한 교정점이 나온다.

**한화에어로스페이스는 4B를 너무 빨리 “종료 신호”로 쓰면 안 된다.**
2025년 3월 유상증자 충격은 분명 4B-watch였지만, 이후 계약과 실적 가이던스가 살아 있었다. 그러니까 R1 방산에서는 4B를 이렇게 나눠야 한다.

```text
4B-watch:
주가 과열, 증자, crowding, valuation 부담

4B-elevated:
증자/대규모 투자로 dilution 우려가 커졌지만 backlog와 EPS가 살아 있음

4C:
계약 취소, financing 실패, 수요 붕괴, EPS 하향, 회계/공시 신뢰 훼손
```

한화에어로스페이스는 `4B-watch/elevated`이지, `4C`가 아니었다.

---

## Case D — 삼성중공업 `success_candidate / Stage2_not_Green`

```text
symbol = 010140
archetype = SHIPBUILDING_OFFSHORE_BACKLOG
case_type = success_candidate
```

삼성중공업은 2024년 7월 1.438조 원 규모의 선박 건조 계약을 확보했다. 계약 규모만 보면 R1의 `SHIPBUILDING_OFFSHORE_BACKLOG`에 들어갈 수 있다. ([마켓워치][9])

하지만 E2R 기준으로는 **계약금액만으로 Stage 3-Green을 주면 안 된다.** 조선은 계약 headline보다 선가, 원가, 환율, 납기, 슬롯, 원자재, 인건비, 저가수주 여부, 영업이익률 개선이 더 중요하다.

### stage date 후보

```text
Stage 1:
2024년 조선 수주 사이클

Stage 2:
2024-07-01
- 1.438조 원 선박계약 공시/보도

Stage 3:
보류
- 계약금액은 있으나 margin / EPS revision / FCF visibility 확인 필요

Stage 4B:
없음

Stage 4C:
없음
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

MFE / MAE:
Stage 2 기준 backfill 가능하지만, Stage 3 기준으로는 보류.

below_stage3_price_flag:
N/A

peak_price:
needs_price_backfill

drawdown_after_peak:
needs_price_backfill
```

### score-price alignment

```text
alignment = unknown_insufficient_evidence
rerating_result = unknown
stage_failure_type = stage2_strong_not_green
```

삼성중공업 케이스는 R1 점수표에서 `contract_amount`는 Stage 2 점수까지만 주고, Stage 3-Green에는 `margin`, `op_eps_revision`, `delivery_slot_quality`, `cost_control`을 요구해야 한다는 교정에 유용하다.

---

## Case E — HD현대마린솔루션 `event_premium / price_moved_without_evidence`

```text
symbol = 443060
archetype = SHIP_MRO_RECURRING_PLATFORM / PRICE_ONLY_RALLY
case_type = event_premium 또는 overheat
```

HD현대마린솔루션은 선박 수리/MRO 플랫폼 성격이 있어 R1로 라우팅할 수 있지만, 2024년 5월 IPO 첫날 주가가 공모가 83,400원 대비 97% 상승해 163,900원에 마감한 것은 E2R Stage 3라기보다 **IPO event premium / price-only rally**에 가깝다. 기사에 따르면 2023년 매출은 1.43조 원으로 7.2% 증가했고 영업·순이익이 크게 늘었지만, 첫날 가격 반응은 IPO 수급과 희소성 프리미엄이 강했다. ([월스트리트 저널][10])

### stage date 후보

```text
Stage 1:
2024-05 IPO 수요예측 / 상장 흥행

Stage 2:
2024-05-08 상장
- 사업모델과 실적 존재
- MRO recurring platform 가능성은 있음

Stage 3:
보류
- 상장 첫날 가격 급등을 Stage 3로 주면 안 됨
- 상장 후 반복매출, OPM, 수주, FCF 추적 필요

Stage 4B:
2024-05-08
- IPO 첫날 +97%
- event premium / price-only rally

Stage 4C:
없음
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

MFE / MAE:
IPO event 기준으로 별도 측정 가능.
E2R Stage 3 기준으로는 N/A.

below_stage3_price_flag:
N/A

peak_price:
needs_price_backfill

drawdown_after_peak:
needs_price_backfill
```

### score-price alignment

```text
alignment = price_moved_without_evidence
rerating_result = event_premium
stage_failure_type = should_have_been_watch_not_green
```

이 케이스는 R1에서 `IPO`, `상장 첫날 급등`, `희소성 프리미엄`을 Stage 3로 오인하지 말라는 반례다.

---

## Case F — KAI 한국항공우주 `success_candidate / insufficient_evidence`

```text
symbol = 047810
archetype = DEFENSE_AIRCRAFT_EXPORT_BACKLOG
case_type = success_candidate
```

KAI는 2025년 6월 필리핀 국방부와 약 9,753억 원, 7.13억 달러 규모 FA-50 12대 공급계약을 체결했다. 2030년까지 납품되는 계약이고, 필리핀 군 현대화와 연결된다. ([Reuters][11])

이건 R1 방산 수출 archetype으로 볼 수 있지만, Stage 3-Green을 주기엔 아직 부족하다. 계약 규모는 의미 있지만, 한화에어로스페이스나 현대로템처럼 중장기 EPS/FCF 체급 변화를 명확히 보여주는 수준인지 검증이 필요하다.

### stage date 후보

```text
Stage 1:
FA-50 수출 기대

Stage 2:
2025-06-04
- 필리핀 12대 FA-50 계약

Stage 3:
보류
- 수주잔고, 마진, EPS revision, 추가 수출 파이프라인 확인 필요

Stage 4B:
없음

Stage 4C:
없음
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

MFE / MAE:
Stage 2 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_price_backfill

drawdown_after_peak:
needs_price_backfill
```

### score-price alignment

```text
alignment = unknown_insufficient_evidence
rerating_result = unknown
stage_failure_type = stage2_watch_success 후보
```

KAI는 `계약 있음 → Stage 2`, `체급 변화 확인 전 → Watch`가 맞다.

---

## Case G — 한화오션 `4C-thesis-break 후보 / insufficient_evidence`

```text
symbol = 042660
archetype = SHIPBUILDING_OFFSHORE_BACKLOG / GEOPOLITICAL_SHIPBUILDING_SANCTION_OVERLAY
case_type = 4C-thesis-break 후보
```

한화오션은 2025년 10월 중국이 미국 관련 자회사에 제재를 부과했고, 2025년 11월 중국 상무부가 그 제재를 1년간 중단한다고 밝혔다. ([Reuters][12])

이건 조선·방산·미중 지정학이 섞인 R1/R11 교차 이벤트다. 다만 제재가 중단됐기 때문에 `hard 4C`로 확정하면 안 된다. 대신 `policy/geopolitical sanction watch`로 기록하고, 실제 계약 지연, 고객 취소, 매출 차질, 영업이익 하향이 나왔는지 봐야 한다.

### stage date 후보

```text
Stage 1:
미국 조선/방산 협력 기대

Stage 2:
조선·방산 수주 및 MRO 기대 구간

Stage 3:
보류
- 수주잔고와 마진 확인 필요

Stage 4B:
미국 조선협력 theme crowding 구간 가능
- 가격경로 backfill 필요

Stage 4C:
2025-10 제재 부과 시점 후보
- 하지만 2025-11 제재 중단으로 hard 4C 확정 불가
```

### 가격경로 검증

```text
stage3_price:
needs_backfill

MFE / MAE:
needs_backfill

below_stage3_price_flag:
needs_backfill

peak_price:
needs_backfill

drawdown_after_peak:
needs_backfill
```

### score-price alignment

```text
alignment = unknown
rerating_result = unknown
stage_failure_type = insufficient_evidence
```

한화오션은 `4C 후보`는 맞지만, `4C 확정`은 아니다. R13에서 `policy_shock_review`로 넘겨야 한다.

---

# 5. 이번 R1 case별 요약표

| case      | 분류                                  | Stage 3 판정 |                    4B/4C 판정 | 가격경로 1차 판단                 |
| --------- | ----------------------------------- | ---------: | --------------------------: | -------------------------- |
| 현대로템      | structural_success                  |         가능 |          2025~2026 4B-watch | Stage 3 이후 대형 MFE 가능성 높음   |
| LIG넥스원    | success_candidate                   |     조건부 가능 |     2026 전투검증 후 4B-watch 후보 | MFE 확인 필요, 방향성은 aligned    |
| 한화에어로스페이스 | structural_success + 4B timing test |         가능 | 2025 증자 충격은 4B-watch, 4C 아님 | 4B를 hard exit로 쓰면 너무 이른 신호 |
| 삼성중공업     | success_candidate                   |         보류 |                          없음 | 계약금액만으로 Green 금지           |
| HD현대마린솔루션 | event_premium / overheat            |         금지 |        IPO 첫날 4B/price-only | Stage 3 오인 방지 case         |
| KAI       | success_candidate                   |         보류 |                          없음 | 계약은 Stage 2, 체급 변화는 미확인    |
| 한화오션      | 4C 후보 / insufficient                |         보류 |  sanction watch, hard 4C 아님 | 제재 중단으로 thesis-break 확정 불가 |

---

# 6. Stage 3 / 4B / 4C 검증 결론

## Stage 3는 R1 방산에서 꽤 잘 작동한다

현대로템과 한화에어로스페이스는 E2R 원칙에 잘 맞는다.

```text
단순 테마:
유럽 방산 / 폴란드 수출 / 우주 / 재무장

진짜 Stage 3 증거:
납품
계약
영업이익률 개선
EPS/OP revision
추가 수주
가격경로 대형 MFE
```

특히 현대로템은 `Stage 3 서생원 원칙으로 들어갔다면 큰 수익률이 있었어야 한다`는 네 기준에 잘 맞는 후보야. 기사상 stage anchor가 41,300원이고, 이후 수백 % 단위 가격경로가 확인되는 쪽이라, exact OHLC backfill만 들어오면 R1 성공 calibration에 강하게 들어갈 수 있다. ([월스트리트 저널][1])

## 4B는 “종료”가 아니라 “상승 후반부 위험 상태”로 나눠야 한다

한화에어로스페이스가 핵심이다. 2025년 3월 유상증자 충격은 4B-watch가 맞다. 하지만 이후 2025년 가이던스와 2026년 노르웨이 계약까지 보면, 이걸 4C나 hard exit로 처리하면 너무 이르다. ([Reuters][8])

따라서 R1 방산에서는 4B를 이렇게 세분화해야 한다.

```text
4B-watch:
많이 올랐다. valuation/crowding 감시.

4B-elevated:
증자, 대형 capex, dilution, supply-chain 투자 부담이 생겼다.
하지만 backlog/EPS thesis가 살아 있으면 hard exit 아님.

4B-graduated:
valuation이 이미 포화되고, 신규 계약이 주가를 더 못 밀며,
실적이 좋아도 가격 반응이 둔해진다.

4C:
계약 취소, financing 실패, 예산 삭감, 납기 차질, 회계/공시 문제, EPS 하향.
```

## 4C는 이번 R1에서 억지로 만들면 안 된다

한화오션 sanction watch는 4C 후보지만, 제재가 중단됐으니 hard 4C로 확정하면 안 된다. R1에서 4C는 정말 무겁게 써야 한다.

```text
4C 확정 조건:
계약 취소
financing 실패
고객 예산 취소
납품 지연이 실적 훼손으로 연결
수주잔고 품질 훼손
회계/공시 신뢰 훼손
EPS/FCF 하향
```

---

# 7. score-price alignment 판정

```text
현대로템:
aligned
true_rerating
Stage 3 성공 후보

한화에어로스페이스:
aligned
true_rerating
다만 4B timing은 hard exit가 아니라 elevated watch

LIG넥스원:
aligned 후보
수출계약 + 전투검증 + 중동/유럽 수요
가격 backfill 필요

삼성중공업:
unknown_insufficient_evidence
Stage 2 strong, not Green

HD현대마린솔루션:
price_moved_without_evidence
event_premium
IPO price-only rally

KAI:
unknown_insufficient_evidence
계약은 Stage 2, Stage 3는 보류

한화오션:
unknown / policy_shock_watch
4C 후보지만 hard 4C 미확정
```

---

# 8. 점수비중 교정

## 올릴 축

R1 Loop 7에서 shadow weight를 올려야 하는 축은 이거야.

```text
contract_quality +2
delivery_schedule +2
order_to_revenue_conversion +2
op_eps_revision +3
margin_visibility +3
government_financing_or_budget +2
price_path_alignment +2
```

특히 방산에서는 `계약 체결`보다 `납품 일정`, `정부 financing`, `현지 생산 구조`, `실제 매출 인식`, `OPM 개선`이 더 중요하다.

## 내릴 축

```text
order_headline -3
theme_keyword -3
broker_target_only -2
ipo_first_day_price_move -4
contract_amount_without_margin -2
policy_or_mou_without_budget -3
```

삼성중공업, KAI, HD현대마린솔루션 케이스 때문에 이 감점축은 반드시 필요하다.

## Green gate 강화 조건

R1 Stage 3-Green은 앞으로 이렇게 줘야 한다.

```text
필수:
계약금액 / 매출비율
계약기간
납기
고객 또는 정부 예산/financing
수주잔고 증가
OPM 또는 EPS revision
가격경로가 증거 이후 따라오는지

금지:
계약 headline만 있음
마진 불명
납기 불명
financing 조건 불명
IPO/수급성 급등
증거보다 가격이 먼저 감
```

## 4B 조기감지 조건

```text
4B-watch:
Stage 3 이후 3배 이상 상승
target multiple 재평가 완료
보고서/뉴스가 모두 같은 논리를 반복
대형 증자 또는 capex 발표
신규 계약에도 주가 반응 둔화

4B-elevated:
dilution shock
대규모 투자 부담
valuation saturation
하지만 EPS/backlog thesis는 아직 살아 있음

4B-graduated:
실적 beat에도 주가가 못 감
forward multiple 포화
추가 수주가 surprise가 아님
```

## 4C hard gate 조건

```text
계약 취소
financing 실패
정부 예산 삭감
고객사 발주 취소
납품 지연이 실적 하향으로 연결
수주잔고 품질 악화
마진 붕괴
회계/공시 신뢰 훼손
제재/수출통제 장기화
```

---

# 9. shadow-only 기록

이번 R1 Loop 7은 production scoring에 바로 반영하면 안 된다.

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
needs_ohlc_backfill = true
```

레포에 넣는다면 이런 파일 형태가 맞다.

```text
docs/round/round_120.md
docs/checkpoints/checkpoint_28a_round120_r1_loop7_industrial_infra_price_validation.md
src/e2r/sector/round120_r1_loop7_industrial_infra.py
data/e2r_case_library/cases_r1_loop7_round120.jsonl
data/sector_taxonomy/score_weight_profiles_round120_r1_loop7_v7.csv
output/e2r_round120_r1_loop7_industrial_infra/
```

---

# 10. 이번 R1 라운드 결론

R1은 방향이 맞다. 특히 **방산 수출형 R1**은 E2R Stage 3가 실제 대형 상승을 잡을 수 있다는 증거가 꽤 강하다.

하지만 보정이 필요하다.

```text
1. Stage 3는 계약 headline이 아니라 납품·마진·EPS revision까지 봐야 한다.
2. 방산은 4B가 너무 빨리 뜰 수 있다. 4B-watch와 4C를 분리해야 한다.
3. 조선은 계약금액만으로 Green을 주면 안 된다.
4. IPO/상장 첫날 급등은 Stage 3가 아니라 event premium이다.
5. 4C는 억지로 만들지 말고, 실제 thesis break가 있을 때만 준다.
```

이번 R1 Loop 7의 핵심 교정은 이거야.

> **R1에서 가장 강한 Stage 3 증거는 “수주”가 아니라 “수주가 납품·마진·EPS/FCF 체급 변화로 넘어가는 순간”이다.**
> **4B는 상승 종료 신호가 아니라, 먼저 watch/elevated/graduated로 나눠야 한다.**

[1]: https://www.wsj.com/articles/hyundai-rotem-rallies-on-hopes-tank-exports-will-boost-earnings-9322d840?utm_source=chatgpt.com "Hyundai Rotem Rallies on Hopes Tank Exports Will Boost Earnings"
[2]: https://www.reuters.com/business/aerospace-defense/south-korea-close-6-billion-tank-deal-with-poland-june-yonhap-reports-2025-06-09/?utm_source=chatgpt.com "South Korea close to $6 billion tank deal with Poland in June, Yonhap reports"
[3]: https://www.ft.com/content/658c8411-df02-4b5e-a69d-2029114e4ca1?utm_source=chatgpt.com "Iran war lifts K-defence company offering cheap Patriot rival"
[4]: https://www.reuters.com/business/aerospace-defense/south-koreas-lig-nex1-wins-28-bln-deal-with-iraq-export-missile-systems-2024-09-19/?utm_source=chatgpt.com "South Korea's LIG Nex1 wins $2.8 bln Iraq deal to export missile systems"
[5]: https://www.wsj.com/articles/hanwha-aerospace-shares-extend-gains-on-bid-for-space-rocket-project-bb8a5805?utm_source=chatgpt.com "Hanwha Aerospace Shares Extend Gains on Bid for Space Rocket Project"
[6]: https://www.reuters.com/business/aerospace-defense/skoreas-hanwha-aerospace-deal-supply-more-rocket-launchers-poland-2024-04-25/?utm_source=chatgpt.com "South Korea's Hanwha to supply more rocket launchers to Poland for $1.64 bln"
[7]: https://www.reuters.com/business/aerospace-defense/south-korea-market-watchdog-orders-hanwha-aerospace-revise-share-issuance-plan-2025-03-27/?utm_source=chatgpt.com "S. Korea watchdog blocks Hanwha Aerospace $2.5 billion capital raising plan"
[8]: https://www.reuters.com/business/aerospace-defense/south-koreas-hanwha-aerospace-trims-capital-increase-plan-16-bln-2025-04-07/?utm_source=chatgpt.com "South Korea's Hanwha Aerospace trims capital increase plan to $1.6 bln"
[9]: https://www.marketwatch.com/story/samsung-heavy-industries-secures-krw1-438t-shipbuilding-contract-8a19cc30?utm_source=chatgpt.com "Samsung Heavy Industries Secures KRW1.438T Shipbuilding Contract"
[10]: https://www.wsj.com/business/hd-hyundai-marine-solution-makes-strong-debut-in-south-korea-e5e63451?utm_source=chatgpt.com "KKR-Backed HD Hyundai Marine Makes Strong Debut in South Korea"
[11]: https://www.reuters.com/en/south-koreas-kai-signs-700-mln-aircraft-deal-with-philippines-2025-06-04/?utm_source=chatgpt.com "South Korea's KAI signs $700 mln aircraft deal with Philippines"
[12]: https://www.reuters.com/world/china/china-suspends-sanctions-us-linked-units-skoreas-hanwha-ocean-2025-11-10/?utm_source=chatgpt.com "China suspends sanctions on US-linked units of S.Korea's Hanwha Ocean"
