순서상 이번은 **R1 Loop 8 — 산업재·수주·인프라 가격경로 검증 라운드**다.

이번 답변은 이전처럼 `needs_ohlc_backfill`로 끝내지 않고, **딥서치로 확인 가능한 가격 anchor와 수익률은 직접 계산**했다. 다만 KRX/Naver/Yahoo/Stooq의 원시 수정주가 일봉 OHLC를 이 세션에서 안정적으로 직접 추출하지 못한 종목은 숫자를 지어내지 않고 `price_data_unavailable_after_deep_search`로 명시했다. 그래서 이번 라운드는 **full OHLC complete**가 아니라 **reported price-anchor 기반 price validation 완료본**이다.

---

# 1. 이번 라운드 대섹터

```text
R1 = 산업재·수주·인프라
large_sector = INDUSTRIAL_ORDERS_INFRA
round = R1 Loop 8 / price-path validation
```

R1의 기본 검증축은 `contract_amount_to_sales`, `contract_duration`, `backlog`, `delivery_schedule`, `op_eps_revision`, `margin`이다. R1은 전력설비·방산·조선·철도·원전·데이터센터 전력설비처럼 “수주가 이익 체급으로 내려오는지”를 보는 섹터다. 

---

# 2. 대상 canonical archetype

```text
DEFENSE_GOVERNMENT_BACKLOG
DEFENSE_LOCAL_PRODUCTION_PLATFORM
DEFENSE_INTERCEPTOR_COMBAT_VALIDATION
DEFENSE_AIRCRAFT_EXPORT_BACKLOG
SHIPBUILDING_OFFSHORE_BACKLOG
SHIP_MRO_RECURRING_PLATFORM
GEOPOLITICAL_SHIPBUILDING_SANCTION_OVERLAY
CONTRACT_BACKLOG_INDUSTRIAL
PRICE_ONLY_RALLY
CROWDING_4B_WATCH
THESIS_BREAK_4C
```

이번 R1의 핵심 질문은 이거다.

```text
수주 뉴스인가?
아니면 계약금액·기간·납기·마진·EPS revision·가격경로가 같이 맞은 구조적 리레이팅인가?
```

---

# 3. deep sub-archetype

```text
방산 수출:
- K2 tank export
- Poland second K2 contract
- Chunmoo / K9 export ecosystem
- Cheongung-II air-defense export
- FA-50 export
- European rearmament
- local production / technology transfer
- delivery schedule

조선 / 해양:
- ship MRO recurring platform
- HD Hyundai Marine Solution IPO
- U.S. shipbuilding policy
- Hanwha Ocean China sanction
- HD Hyundai Heavy / Mipo merger
- MASGA / U.S. shipbuilding cooperation

가격검증 overlay:
- IPO first-day rally
- MOU / preliminary deal
- sanction shock
- capital raise / dilution
- confirmed contract vs rumor
```

---

# 4. 국장 신규 후보 case

## Case A — 현대로템 `structural_success / Stage 3 aligned 후보`

```text
symbol = 064350
case_type = structural_success
archetype = DEFENSE_GOVERNMENT_BACKLOG / DEFENSE_LOCAL_PRODUCTION_PLATFORM
```

### evidence

2024년 4월 9일 현대로템은 폴란드 K2 전차 납품이 1분기 실적을 끌어올릴 것이라는 기대에 9.3% 상승해 41,300원에 거래됐다. KB증권은 당시 1분기 영업이익이 전년 대비 85% 증가할 수 있고, K2 18대 납품이 분기 매출의 약 3분의 1을 차지할 수 있다고 봤다. 이건 단순 방산 테마가 아니라 **납품 → 매출 → 영업이익**으로 내려오는 Stage 2~3 후보 evidence다. ([월스트리트저널][1])

2025년 8월 1일에는 폴란드가 현대로템과 K2 전차 180대를 추가 구매하는 계약을 체결했고, 이 계약은 약 65억 달러 규모로 보도됐다. 이 계약에는 폴란드 현지 생산과 기술이전 성격이 포함됐다. ([Reuters][2])

2026년 3월 FT는 현대로템 주가가 지난 1년 동안 6배 이상 올랐다고 보도했다. 같은 기사에서 한국 방산 수출 ecosystem이 폴란드·중동·유럽 재무장 수요를 타고 확대됐다고 설명했다. ([Financial Times][3])

### stage date

```text
Stage 1:
2022-2024
- 폴란드 K2 1차 계약
- 유럽 재무장 / K-defense 수출 기대

Stage 2:
2024-04-09
- K2 납품이 1Q 실적에 반영될 수 있다는 증권사 추정
- 영업이익 YoY +85% 기대
- price anchor = 41,300원

Stage 3:
2024-04-09 후보
- 납품·매출·OP revision이 함께 나온 구간
- 다만 official close OHLC 미확보로 reported anchor 기준

Stage 4B:
2025-08-01 이후 후보
- 2차 폴란드 계약 체결
- 이미 시장이 K2 export rerating을 넓게 인식한 구간

Stage 4C:
없음
```

### 실제 가격경로 검증

```text
price_data_source:
WSJ reported intraday/trading price anchor + FT reported 1Y return

entry_date:
2024-04-09

stage3_price:
41,300원 reported price anchor
official close OHLC = price_data_unavailable_after_deep_search

reported_MFE_subperiod:
FT 기준 2025-03~2026-03 약 1년 동안 6배 이상
=> reported 1Y subperiod MFE >= +500%

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MFE_1Y / 2Y:
reported anchor로는 2025-03~2026-03 subperiod +500% 이상 확인
Stage3 entry 기준 exact MFE는 full OHLC unavailable

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
price_data_unavailable_after_deep_search

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
partial_success
- 2026년 3월 이미 6배 이상 상승 보도.
- 2025년 8월 2차 K2 계약 이후부터는 fresh Stage 3가 아니라 4B-watch로 보는 게 안전.
```

### alignment

```text
score_price_alignment = aligned
rerating_result = true_rerating
stage_failure_type = green_success 후보
```

### 교정

현대로템은 R1에서 `delivery_schedule`, `order_to_revenue_conversion`, `op_eps_revision`, `government_backlog` 가중치를 올려준다.

---

## Case B — 한화에어로스페이스 `structural_success + 4B-watch`

```text
symbol = 012450
case_type = structural_success + 4B-watch
archetype = DEFENSE_GOVERNMENT_BACKLOG / CROWDED_RERATING_4B_WATCH
```

### evidence

FT는 2026년 3월 기사에서 한화에어로스페이스 주가가 지난 1년 동안 187,500원에서 1,435,000원으로 상승했다고 보도했다. 이는 방산 수요와 한국 방산 ecosystem 재평가가 가격에 크게 반영된 케이스다. ([Financial Times][3])

하지만 2025년 3월 한화에어로스페이스는 3.6조 원 규모 유상증자를 발표했고, 주가는 하루 13% 급락했다. FT와 Reuters 모두 이 사건을 투자자들이 희석과 자금조달 목적을 우려한 이벤트로 보도했다. ([Financial Times][4])

### stage date

```text
Stage 1:
2022-2024
- 폴란드 / 유럽 재무장 / K9·Chunmoo 수출 확대

Stage 2:
2024-2025
- 수주잔고 확대
- 유럽·중동·노르웨이 등 방산 수요 확대

Stage 3:
2024-2025 중 수주잔고와 EPS 체급 변화 확인 구간
- reported price anchor 기준 187,500원

Stage 4B:
2025-03-21
- 주가가 이미 크게 오른 뒤 대형 증자 발표
- 하루 -13%

Stage 4C:
없음
- 증자는 dilution shock이지만 수요·수주 thesis break는 아님
```

### 실제 가격경로 검증

```text
price_data_source:
FT reported price path + Reuters/FT capital raise reaction

entry_price_anchor:
187,500원

peak_price_anchor:
1,435,000원

reported_MFE:
(1,435,000 / 187,500) - 1
= +665.3%

stage4b_event_MAE_1D:
-13%

MFE_30D / 90D / 180D:
full OHLC unavailable

MFE_1Y:
reported 1Y MFE = +665.3%

MAE_30D / 90D / 180D / 1Y:
full OHLC unavailable

below_stage3_price_flag:
full OHLC unavailable, but reported path implies large positive trend

drawdown_after_peak:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
success
- 대시세 이후 capital raise shock을 4B-watch로 잡아야 함.
```

### alignment

```text
score_price_alignment = aligned
rerating_result = true_rerating
4B_result = 4B_watch_success_not_exit
```

### 교정

한화에어로스페이스는 R1에서 `4B-watch`와 `4C`를 분리해야 한다는 기준점이다.

```text
dilution shock after large rally:
4B-watch / 4B-elevated

contract cancellation or EPS thesis break:
4C
```

---

## Case C — LIG넥스원 `success_candidate + 4B-watch`

```text
symbol = 079550
case_type = success_candidate + 4B-watch
archetype = DEFENSE_INTERCEPTOR_COMBAT_VALIDATION
```

### evidence

2024년 9월 LIG넥스원은 이라크에 약 28억 달러 규모 중거리 지대공 미사일 체계를 수출하는 계약을 체결했다. 해당 계약은 사우디아라비아의 32억 달러 M-SAM II 계약에 이은 것으로, 발표 직후 주가는 3.6% 상승했다. ([Reuters][5])

2026년 3월 FT는 Cheongung-II가 이란전쟁에서 전투 검증을 받으며 중동·유럽 수요가 커질 수 있다고 보도했고, LIG넥스원 주가가 전쟁 시작 이후 약 47% 올랐다고 정리했다. ([Financial Times][3])

### stage date

```text
Stage 1:
2024-02
- Saudi M-SAM II 계약
- 중동 방공 수요 확대

Stage 2:
2024-09-19
- Iraq $2.8B M-SAM II export contract
- 발표 직후 +3.6%

Stage 3:
보류
- 계약은 강하지만 납기, 마진, EPS revision, 생산능력 확인 필요

Stage 4B:
2026-03-11 후보
- Cheongung-II 전투검증 이후 수요 narrative 확산
- 전쟁 시작 이후 주가 +47%

Stage 4C:
없음
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters Iraq deal return anchor + FT war-period return anchor

stage3_price:
N/A, Stage 3 미부여

stage2_event_MFE_1D:
+3.6%

reported_4B_period_MFE:
+47% since Iran war began

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
partial_success
- 전투검증 후 +47%는 4B-watch가 필요한 구간.
```

### alignment

```text
score_price_alignment = success_candidate / aligned_partial
rerating_result = defense_interceptor_rerating_candidate
stage_failure_type = stage2_watch_success
```

### 교정

LIG넥스원은 R1에서 `combat_validation`, `export_contract`, `delivery_capacity`, `margin_visibility`를 올려준다. 다만 전투검증으로 가격이 빨리 확장되면 4B-watch를 붙여야 한다.

---

## Case D — KAI 한국항공우주 `success_candidate / Stage 2 watch`

```text
symbol = 047810
case_type = success_candidate
archetype = DEFENSE_AIRCRAFT_EXPORT_BACKLOG
```

### evidence

2025년 6월 KAI는 필리핀 국방부와 약 9,753억 원, 7.13억 달러 규모 FA-50 12대 공급계약을 체결했다. 납품은 2030년까지 진행될 예정이며, 필리핀 군 현대화와 연결된다. ([Reuters][6])

FT는 2026년 3월 기사에서 Korea Aerospace Industries 주가가 지난 1년 동안 세 배가량 올랐다고 보도했다. 다만 이 상승은 KAI 자체 FA-50 계약뿐 아니라 한국 방산주 전반의 재평가와 함께 나타난 것이므로, Stage 3는 마진·EPS revision 확인 전 보류한다. ([Financial Times][3])

### stage date

```text
Stage 1:
2024-2025
- FA-50 export / KF-21 / K-defense 기대

Stage 2:
2025-06-04
- Philippines FA-50 12대, 약 9,753억 원 계약

Stage 3:
보류
- 납기, 마진, 추가 수출, EPS revision 확인 필요

Stage 4B:
2026-03 후보
- 방산주 전반 재평가 속 KAI가 지난 1년 3배 상승

Stage 4C:
없음
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters contract evidence + FT reported return anchor

stage3_price:
N/A

stage2_price:
price_data_unavailable_after_deep_search

reported_1Y_MFE:
주가 약 3배
=> +200% 수준

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
partial_success
- 3배 상승 후에는 fresh Stage 3보다 4B-watch.
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = defense_aircraft_export_watch
stage_failure_type = stage2_watch_success
```

### 교정

KAI는 `export_contract`만으로 Green 금지다. `order_to_revenue`, `margin`, `production_schedule`, `EPS revision`이 Stage 3 조건이다.

---

## Case E — HD현대마린솔루션 `event_premium / price_moved_without_evidence`

```text
symbol = 443060
case_type = event_premium / overheat
archetype = SHIP_MRO_RECURRING_PLATFORM / PRICE_ONLY_RALLY
```

### evidence

2024년 5월 HD현대마린솔루션은 공모가 83,400원 대비 97% 오른 163,900원에 상장 첫날 마감했다. WSJ는 이 회사의 2023년 매출이 1.43조 원으로 7.2% 증가했고 영업이익과 순이익도 크게 늘었다고 보도했지만, 첫날 가격경로는 IPO 수급과 희소성 프리미엄이 크게 작용한 이벤트였다. ([월스트리트저널][7])

### stage date

```text
Stage 1:
2024-04~05
- IPO 수요예측
- ship MRO recurring platform 기대

Stage 2:
2024-05-08
- 상장
- 2023년 매출 +7.2%, 영업이익 +42%, 순이익 +44%
- 사업모델은 Stage 2 후보

Stage 3:
없음
- 상장 첫날 주가 급등은 Stage 3 아님
- 반복매출·OPM·FCF·수주 확인 필요

Stage 4B:
2024-05-08
- IPO 첫날 +97%

Stage 4C:
없음
```

### 실제 가격경로 검증

```text
price_data_source:
WSJ IPO price and first-day close anchor

IPO_price:
83,400원

first_day_close:
163,900원

event_MFE_1D:
(163,900 / 83,400) - 1
= +96.5%

stage3_price:
N/A

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

peak_price:
163,900원 first-day close anchor, later peak unavailable

drawdown_after_peak:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
yes_for_event
- 상장 첫날부터 4B / event premium.
```

### alignment

```text
score_price_alignment = price_moved_without_evidence
rerating_result = IPO_event_premium
stage_failure_type = should_have_been_4B_watch_not_green
```

### 교정

HD현대마린솔루션은 R1에서 `IPO_first_day_rally`를 강하게 감점한다. 사업모델은 좋을 수 있지만, IPO 첫날 +96.5%는 Stage 3가 아니라 4B/event premium이다.

---

## Case F — 한화오션 `4C-watch / geopolitical shipbuilding sanction`

```text
symbol = 042660
case_type = 4C-watch
archetype = GEOPOLITICAL_SHIPBUILDING_SANCTION_OVERLAY
```

### evidence

2025년 10월 14일 중국은 한화오션의 미국 관련 자회사 5곳에 제재를 부과했다. Reuters는 이 제재가 미중 해운·조선 갈등과 연결돼 있으며, 한화오션 주가가 제재 발표 후 5.8% 하락 마감했다고 보도했다. AP도 한화오션이 미국 Philly Shipyard 인수와 미국 조선 재건 협력에 노출돼 있고, 제재 후 주가가 크게 하락했다고 설명했다. ([Reuters][8])

### stage date

```text
Stage 1:
2025
- 미국 조선 재건
- Philly Shipyard
- U.S.-Korea shipbuilding cooperation

Stage 2:
보류
- MRO·미국 조선 협력은 Stage 2 후보지만 회사 단위 매출·마진 확인 필요

Stage 3:
없음

Stage 4B:
미국 조선 재건 테마로 가격이 먼저 확장된 구간이 있으면 후보

Stage 4C:
2025-10-14
- 중국 제재
- 주가 -5.8%
- geopolitical shipbuilding sanction watch
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event return

stage3_price:
N/A

stage4c_event_MAE_1D:
-5.8%

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search

Stage 4C 큰 하락 이전 포착 여부:
partial_success
- 제재 당일 4C-watch 가능.
- hard 4C는 실제 계약·매출 차질 확인 필요.
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = geopolitical_sanction_watch
stage_failure_type = 4C_watch_not_hard_4C
```

### 교정

한화오션은 R1/R11 cross-over로 `geopolitical_sanction`, `China_exposure`, `U.S._shipbuilding_policy_risk`를 RedTeam에 넣어야 한다.

---

## Case G — HD현대중공업 / HD현대미포 합병 `success_candidate + 4B-watch`

```text
symbols = 329180 / 010620
case_type = success_candidate + 4B-watch
archetype = SHIPBUILDING_OFFSHORE_BACKLOG / U.S._SHIPBUILDING_POLICY
```

### evidence

2025년 8월 HD현대중공업은 HD현대미포와 합병해 미국 조선 시장에서 더 큰 점유율을 노리겠다고 발표했다. Reuters는 이 합병이 한미 정상회담 이후 언급된 “Make American Shipbuilding Great Again” 협력 프로젝트와 연결돼 있다고 보도했다. 발표 전후 HD현대중공업은 11.3%, HD현대미포는 14.6% 상승해 각각 종가 기준 사상 최고가를 기록했다. ([Reuters][9])

### stage date

```text
Stage 1:
2025-08
- U.S.-Korea shipbuilding cooperation
- MASGA project

Stage 2:
2025-08-27
- HD현대중공업·HD현대미포 합병 발표
- 미국 조선시장 확대 목표

Stage 3:
보류
- 합병 시너지, 미국 수주, 마진, FCF 확인 필요

Stage 4B:
2025-08-27
- 발표 전후 양사 record high
- HD현대중공업 +11.3%, HD현대미포 +14.6%

Stage 4C:
합병 실패, 미국 수주 지연, 저마진 수주, integration cost 증가 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters event return anchor

HD_Hyundai_Heavy_event_MFE_1D:
+11.3%

HD_Hyundai_Mipo_event_MFE_1D:
+14.6%

stage3_price:
N/A

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

peak_price:
record high reported, exact price unavailable

drawdown_after_peak:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
event-day 4B-watch
- record high는 가격 선반영 신호.
```

### alignment

```text
score_price_alignment = success_candidate / event_premium_watch
rerating_result = shipbuilding_policy_rerating_candidate
stage_failure_type = stage2_watch_success
```

### 교정

합병 자체는 Stage 2다. Stage 3는 미국 조선 수주·마진·FCF로 내려와야 한다. record high + 이벤트 급등은 4B-watch다.

---

# 5. 이번 R1 case별 요약표

| case       | 분류                      |                                  실제 가격검증 | alignment                    |
| ---------- | ----------------------- | ---------------------------------------: | ---------------------------- |
| 현대로템       | structural_success      | 41,300원 anchor, 이후 1Y subperiod 6배 이상 보도 | aligned                      |
| 한화에어로스페이스  | structural_success + 4B | 187,500원 → 1,435,000원, +665.3%; 증자일 -13% | aligned / 4B-watch           |
| LIG넥스원     | success_candidate + 4B  |              Iraq 계약일 +3.6%; 전투검증 후 +47% | success_candidate            |
| KAI        | success_candidate       |                  FA-50 계약, 이후 1Y 약 3배 보도 | success_candidate            |
| HD현대마린솔루션  | overheat / IPO premium  |               83,400원 → 163,900원, +96.5% | price_moved_without_evidence |
| 한화오션       | 4C-watch                |                             중국 제재일 -5.8% | thesis_break_watch           |
| HD현대중공업/미포 | success_candidate + 4B  |      합병 이벤트 +11.3% / +14.6%, record high | event_premium_watch          |

---

# 6. score-price alignment 판정

```text
aligned:
- 현대로템
- 한화에어로스페이스

success_candidate:
- LIG넥스원
- KAI
- HD현대중공업 / HD현대미포

price_moved_without_evidence:
- HD현대마린솔루션 IPO 첫날 +96.5%

event_premium:
- HD현대마린솔루션
- HD현대중공업 / HD현대미포 합병 이벤트 일부

thesis_break_watch:
- 한화오션 중국 제재

4B-watch:
- 한화에어로스페이스 대형 증자
- 현대로템 2차 폴란드 계약 이후
- LIG넥스원 전투검증 이후
- HD현대마린솔루션 IPO 첫날
- HD현대중공업/미포 record high 이벤트
```

---

# 7. 점수비중 교정

## 올릴 축

```text
contract_amount_to_sales +4
delivery_schedule +4
order_to_revenue_conversion +5
op_eps_revision +5
government_backlog +4
combat_validation +3
local_production_or_technology_transfer +3
price_path_alignment +5
```

**현대로템**은 납품과 영업이익 전망이 주가 경로와 맞았다. **한화에어로스페이스**는 대형 MFE가 확인됐다. 이 둘은 R1 Stage 3의 성공 기준을 강화한다.

## 내릴 축

```text
order_headline_only -4
ipo_first_day_rally -5
mou_or_preliminary_policy_event -4
record_high_on_policy_event -3
contract_without_margin_visibility -3
geopolitical_exposure_unpriced -3
```

**HD현대마린솔루션**은 IPO 첫날 +96.5%이므로 Stage 3가 아니라 4B/event premium이다. **HD현대중공업/미포**도 합병 이벤트로 record high를 찍었으므로 Stage 2와 4B-watch를 동시에 기록해야 한다.

## Green gate 강화 조건

```text
R1 Stage 3-Green 필수:
1. 계약금액 확인
2. 계약기간 / 납기 확인
3. 실제 납품 또는 매출 인식 확인
4. OPM / EPS revision 확인
5. 수주잔고 품질 확인
6. 가격경로가 evidence 이후 따라왔는지 확인
7. sanction / financing / dilution / margin risk 통과

금지:
수주 headline만 있음
IPO 첫날 급등
MOU / preliminary deal
record high event rally
마진 불명
정책 테마만 있음
```

## 4B 조기감지 조건

```text
4B-watch:
Stage 3 이후 2~5배 이상 상승
신규 계약이 surprise가 아니라 consensus가 됨
market cap / record high가 headline화
대형 증자 또는 CB 발표
IPO 첫날 50~100% 급등
정책/합병/MOU 이벤트로 record high

4B-elevated:
증자·CAPEX·현지공장 투자 부담
계약은 많지만 마진 가시성 둔화
중국/미국 sanction exposure
기존 수주가 이미 valuation에 반영
```

## 4C hard gate 조건

```text
계약 취소
financing 실패
납기 지연이 실적 하향으로 연결
중국/미국 제재가 실제 매출 차질로 연결
마진 붕괴
회계/공시 신뢰 훼손
치명적 안전/품질 문제
```

한화오션 중국 제재는 현 단계에서 **4C-watch**이지 hard 4C는 아니다. 실제 계약 차질·매출 차질·고객 이탈이 확인되면 hard 4C로 승격한다.

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

`full_ohlc_complete = false`는 숨기면 안 된다. 이번 세션에서 KRX/Naver/Yahoo/Stooq의 원시 수정주가 일봉을 안정적으로 직접 추출하지 못했다. 대신 Reuters/FT/WSJ의 **검증 가능한 가격 anchor와 이벤트 수익률**로 계산 가능한 항목은 직접 계산했다.

---

# 9. patch-ready 출력

## docs/round/round_133.md 요약

```md
# R1 Loop 8. Industrial Orders / Infra Price Validation

이번 라운드는 R13 이후 다시 R1로 돌아온 가격검증 라운드다.

핵심 결론:
- 현대로템은 K2 납품이 매출·OP revision으로 연결되며 Stage 3 aligned 후보로 분류된다.
- 한화에어로스페이스는 187,500원에서 1,435,000원까지 올라 +665.3% MFE anchor가 확인된다. 대형 증자는 4B-watch이지 hard 4C가 아니다.
- LIG넥스원은 Iraq M-SAM 계약과 Cheongung-II 전투검증 이후 rerating 후보지만, 납기·마진·EPS revision 전에는 Stage 3 보류다.
- KAI는 FA-50 필리핀 계약으로 Stage 2 후보지만, Stage 3는 생산·마진·EPS 확인 후다.
- HD현대마린솔루션은 IPO 첫날 +96.5%로 price_moved_without_evidence / event premium이다.
- 한화오션 중국 제재는 geopolitical shipbuilding 4C-watch다.
- HD현대중공업/미포 합병 이벤트는 Stage 2이자 4B-watch다.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 133 R1 Loop 8 Industrial Infra Price Validation

## 반영 내용
- R1 price-validation 라운드를 추가했다.
- 방산 수출, 조선/MRO, IPO event premium, sanction risk를 비교했다.
- Reuters/FT/WSJ reported price anchors로 가능한 MFE/MAE를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- order_to_revenue_conversion 강화
- op_eps_revision 강화
- IPO/event premium 감점 강화
- 4B-watch와 4C 구분 강화
- geopolitical sanction watch 추가
```

## case row 초안

```jsonl
{"case_id":"r1_loop8_hyundai_rotem_k2_aligned","symbol":"064350","company_name":"현대로템","case_type":"structural_success","primary_archetype":"DEFENSE_GOVERNMENT_BACKLOG","stage2_date":"2024-04-09","stage3_date":"2024-04-09","stage4b_date":"2025-08-01","price_validation":{"price_data_source":"WSJ/FT reported anchors","stage3_price":41300,"mfe_1y":500.0,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"aligned","rerating_result":"true_rerating","notes":"K2 delivery to Poland connected to revenue and OP revision; later FT reports Hyundai Rotem up more than sixfold over one-year subperiod."}
{"case_id":"r1_loop8_hanwha_aerospace_mfe_4b","symbol":"012450","company_name":"한화에어로스페이스","case_type":"structural_success","primary_archetype":"STRUCTURAL_SUCCESS_BUT_4B_WATCH","stage4b_date":"2025-03-21","price_validation":{"price_data_source":"FT/Reuters reported anchors","stage3_price":187500,"peak_price":1435000,"peak_return_from_stage3":665.3,"mae_1d":-13.0,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"aligned","rerating_result":"true_rerating","notes":"Capital raise is 4B-watch/elevated, not hard 4C."}
{"case_id":"r1_loop8_lig_nex1_cheongung_watch","symbol":"079550","company_name":"LIG넥스원","case_type":"success_candidate","primary_archetype":"DEFENSE_INTERCEPTOR_COMBAT_VALIDATION","stage2_date":"2024-09-19","stage4b_date":"2026-03-11","price_validation":{"price_data_source":"Reuters/FT reported anchors","mfe_1d":3.6,"mfe_subperiod":47.0,"price_validation_status":"reported_return_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"defense_interceptor_rerating_candidate","notes":"Iraq contract and combat validation are strong, but margin/delivery/EPS revision required for Stage 3."}
{"case_id":"r1_loop8_kai_fa50_stage2","symbol":"047810","company_name":"한국항공우주","case_type":"success_candidate","primary_archetype":"DEFENSE_AIRCRAFT_EXPORT_BACKLOG","stage2_date":"2025-06-04","price_validation":{"price_data_source":"Reuters/FT reported anchors","mfe_1y":200.0,"price_validation_status":"reported_return_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"aircraft_export_watch","notes":"FA-50 Philippines contract is Stage 2; Stage 3 requires production, margin and EPS revision."}
{"case_id":"r1_loop8_hd_hyundai_marine_ipo_premium","symbol":"443060","company_name":"HD현대마린솔루션","case_type":"overheat","primary_archetype":"PRICE_ONLY_RALLY","stage2_date":"2024-05-08","stage4b_date":"2024-05-08","price_validation":{"price_data_source":"WSJ IPO anchor","ipo_price":83400,"first_day_close":163900,"mfe_1d":96.5,"price_validation_status":"reported_price_anchor_not_stage3"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"IPO_event_premium","notes":"Good MRO business model, but IPO first-day rally is not Stage 3."}
{"case_id":"r1_loop8_hanwha_ocean_china_sanction","symbol":"042660","company_name":"한화오션","case_type":"4c_watch","primary_archetype":"GEOPOLITICAL_SHIPBUILDING_SANCTION_OVERLAY","stage4c_date":"2025-10-14","price_validation":{"price_data_source":"Reuters reported return anchor","mae_1d":-5.8,"price_validation_status":"reported_event_return_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"geopolitical_sanction_watch","notes":"China sanctions are 4C-watch; hard 4C requires actual revenue/contract disruption."}
{"case_id":"r1_loop8_hd_hyundai_heavy_mipo_merger_4b","symbol":"329180/010620","company_name":"HD현대중공업/HD현대미포","case_type":"success_candidate","primary_archetype":"SHIPBUILDING_OFFSHORE_BACKLOG","stage2_date":"2025-08-27","stage4b_date":"2025-08-27","price_validation":{"price_data_source":"Reuters reported return anchor","mfe_1d_heavy":11.3,"mfe_1d_mipo":14.6,"price_validation_status":"reported_event_return_not_full_ohlc"},"score_price_alignment":"event_premium_watch","rerating_result":"shipbuilding_policy_rerating_candidate","notes":"Merger is Stage 2; record-high event move is 4B-watch until US orders/margins/FCF confirm."}
```

## shadow weight row 초안

```csv
archetype,contract_quality,delivery_schedule,order_to_revenue,op_eps_revision,price_path_alignment,event_premium_penalty,geopolitical_redteam,4b_watch_sensitivity,notes
DEFENSE_GOVERNMENT_BACKLOG,+4,+4,+5,+5,+5,0,+1,+3,Hyundai Rotem and Hanwha Aerospace confirm large MFE when delivery and OP revision align.
DEFENSE_INTERCEPTOR_COMBAT_VALIDATION,+4,+3,+3,+3,+3,0,+1,+4,LIG Nex1 needs combat validation plus delivery/margin/EPS before Green.
DEFENSE_AIRCRAFT_EXPORT_BACKLOG,+3,+3,+3,+3,+2,0,+1,+3,KAI FA-50 export is Stage 2 until margin and production schedule confirm.
SHIP_MRO_RECURRING_PLATFORM,+2,+2,+2,+2,+1,-5,0,+5,HD Hyundai Marine IPO rally is 4B/event premium, not Stage 3.
GEOPOLITICAL_SHIPBUILDING_SANCTION_OVERLAY,0,0,0,0,+2,0,+5,+3,Hanwha Ocean China sanctions require 4C-watch.
SHIPBUILDING_OFFSHORE_BACKLOG,+3,+3,+3,+3,+3,-3,+2,+4,HD Hyundai Heavy/Mipo merger is Stage 2 and 4B-watch until margin/FCF confirm.
```

---

# 이번 R1 Loop 8 결론

R1은 Stage 3가 실제로 대시세를 잡을 수 있는 섹터다. 하지만 조건은 빡세다.

```text
1. 현대로템과 한화에어로스페이스는 Stage 3가 잘 잡히면 대형 MFE가 나온다는 증거다.

2. LIG넥스원과 KAI는 강한 Stage 2 후보지만,
   납기·마진·EPS revision 전에는 Stage 3를 보류해야 한다.

3. HD현대마린솔루션은 좋은 사업일 수 있지만,
   IPO 첫날 +96.5%는 Stage 3가 아니라 4B/event premium이다.

4. 한화오션 중국 제재는 hard 4C는 아니지만,
   R1 조선·방산의 geopolitical RedTeam으로 반드시 넣어야 한다.

5. HD현대중공업/미포 합병은 Stage 2와 4B-watch가 동시에 뜨는 case다.
   미국 조선정책 기대가 실제 수주·마진·FCF로 내려오기 전에는 Green 금지다.
```

한 문장으로 압축하면:

> **R1에서 진짜 Stage 3는 “수주가 있다”가 아니라, 수주가 납품·매출·마진·EPS revision으로 내려오고 가격경로가 그 뒤를 따라오는 순간이다.**
> **R1의 4B는 대형 수익률 이후 capital raise·IPO premium·record high·정책 이벤트에서 빨리 붙여야 하고, 4C는 계약·제재·마진·신뢰 훼손이 실제 실적을 찌를 때만 hard gate로 승격해야 한다.**

[1]: https://www.wsj.com/articles/hyundai-rotem-rallies-on-hopes-tank-exports-will-boost-earnings-9322d840?utm_source=chatgpt.com "Hyundai Rotem Rallies on Hopes Tank Exports Will Boost Earnings"
[2]: https://www.reuters.com/markets/emerging/poland-signs-contract-buy-more-south-korean-battle-tanks-2025-08-01/?utm_source=chatgpt.com "Poland signs contract to buy more South Korean battle tanks"
[3]: https://www.ft.com/content/658c8411-df02-4b5e-a69d-2029114e4ca1?utm_source=chatgpt.com "Iran war lifts K-defence company offering cheap Patriot rival"
[4]: https://www.ft.com/content/994a0a80-414f-442f-bf41-f2dbde5a04ca?utm_source=chatgpt.com "South Korea's biggest defence group plans $2.5bn share sale to expand overseas"
[5]: https://www.reuters.com/business/aerospace-defense/south-koreas-lig-nex1-wins-28-bln-deal-with-iraq-export-missile-systems-2024-09-19/?utm_source=chatgpt.com "South Korea's LIG Nex1 wins $2.8 bln Iraq deal to export missile systems"
[6]: https://www.reuters.com/en/south-koreas-kai-signs-700-mln-aircraft-deal-with-philippines-2025-06-04/?utm_source=chatgpt.com "South Korea's KAI signs $700 mln aircraft deal with Philippines"
[7]: https://www.wsj.com/business/hd-hyundai-marine-solution-makes-strong-debut-in-south-korea-e5e63451?utm_source=chatgpt.com "KKR-Backed HD Hyundai Marine Makes Strong Debut in South Korea"
[8]: https://www.reuters.com/world/asia-pacific/china-takes-steps-against-us-linked-units-skorea-shipbuilder-hanwha-2025-10-14/?utm_source=chatgpt.com "China takes steps against US-linked units of S.Korea shipbuilder Hanwha"
[9]: https://www.reuters.com/markets/emerging/south-korean-shipbuilder-hd-hyundai-heavy-merge-with-affiliate-hd-hyundai-mipo-2025-08-27/?utm_source=chatgpt.com "South Korean shipbuilder HD Hyundai Heavy to merge with affiliate HD Hyundai Mipo"
