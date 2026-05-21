순서상 이번은 **R2 Loop 8 — AI·반도체·전자부품 가격경로 검증 라운드**다.

이번 라운드는 원시 일봉 OHLC를 안정적으로 직접 추출하지 못한 종목에 대해 숫자를 지어내지 않고, **Reuters / WSJ / FT / MarketWatch / Tom’s Hardware 등에 남은 가격 anchor와 이벤트 수익률을 기준으로 계산 가능한 값만 계산**했다. 그래서 결과 상태는 `price_validation_completed = partial_with_reported_price_anchors`, `full_ohlc_complete = false`다.

---

# 1. 이번 라운드 대섹터

```text
R2 = AI·반도체·전자부품
large_sector = AI_SEMICONDUCTOR_ELECTRONICS
round = R2 Loop 8 / price-path validation
```

R2의 기본 검증축은 `eps_revision`, `capacity_bottleneck`, `customer_order`, `gross_margin`, `inventory`, `accounting_trust`다. R2는 HBM, 범용 메모리, 반도체 장비, 패키징, AI 서버 공급망, neocloud, 광통신, 냉각, 회계신뢰도 overlay를 보는 섹터다. 

Round 119 기준으로 R2에서 부족한 증거는 `ai_name`, `server_theme`이고, 필요한 증거는 `hbm_lta`, `prepayment`, `capacity_constraint`, `consensus_revision`, `rerating_room`이다. Green blocker는 `capex_cut`, `supply_glut`, `circular_financing`이다. 

---

# 2. 대상 canonical archetype

```text
MEMORY_HBM_CAPACITY
MEMORY_HBM_LTA_PREPAYMENT
HBM_CATCHUP_EXECUTION
COMMODITY_MEMORY_GENERAL_SEMI
SEMI_EQUIPMENT_AI_CAPEX
HBM_BONDER_EQUIPMENT_KOREA
ADVANCED_PACKAGING_EQUIPMENT_KOREA
SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER
AI_CHIP_FABRIC_INFRA
AI_DATA_CENTER_INFRASTRUCTURE
REDTEAM_ACCOUNTING_TRUST_OVERLAY
AI_CAPEX_CROWDING_OVERLAY
DISCLOSURE_CONFIDENCE_CAP
PRICE_ONLY_RALLY
```

이번 R2의 핵심 질문은 이거다.

```text
AI 반도체 수혜주인가?
아니면 고객 주문·CAPA 병목·마진·EPS revision·가격경로가 같이 맞은 구조적 리레이팅인가?
```

---

# 3. deep sub-archetype

```text
HBM leader:
- SK Hynix HBM leadership
- HBM demand from Nvidia / OpenAI / AI server
- DRAM and HBM price upcycle
- capacity sold out
- market-cap rerating
- 4B crowding / valuation saturation

HBM equipment:
- Hanmi Semiconductor TSV-TC bonder
- SK Hynix customer visibility
- Micron customer expansion rumor
- confirmed contract vs unconfirmed media report
- order-to-revenue conversion

HBM catch-up:
- Samsung Electronics HBM lag
- commodity DRAM/NAND recovery
- OpenAI Stargate LOI
- Nvidia qualification gap
- labor/production disruption watch

AI chip design house:
- Gaonchips
- Preferred Networks AI chip
- Samsung 2nm GAA
- design win vs volume shipment
- tape-out / mass production / revenue conversion

policy foundry:
- DB HiTek
- 40nm public-private foundry
- AI/fabless policy support
- government consultation vs actual order

export-control RedTeam:
- U.S. China chip equipment authorization revocation
- Samsung / SK Hynix China exposure
- Hana Micron / Hanmi Semiconductor supplier risk
```

---

# 4. 국장 신규 후보 case

## Case A — SK하이닉스 `structural_success + 4B-watch benchmark`

```text
symbol = 000660
case_type = structural_success + 4B-watch
archetype = MEMORY_HBM_CAPACITY / MEMORY_HBM_LTA_PREPAYMENT
```

### evidence

2024년 6월 25일 MarketWatch는 Nomura가 SK하이닉스의 HBM 지배력과 강한 메모리 가격을 이유로 2024년 영업이익 추정치를 30조 원, 2025년을 53조 원으로 상향했고, 당시 주가가 222,000원이라고 보도했다. 이 날짜는 `HBM dominance + earnings revision + old memory-cycle frame break`가 같이 나온 강한 Stage 3 후보 anchor다. ([마켓워치][1])

2026년 5월 14일 Reuters는 SK하이닉스가 2025년에 274% 상승했고 2026년에도 200% 넘게 올랐으며, 16개월 전 1,000억 달러 미만이던 시가총액이 약 9,420억 달러가 됐다고 보도했다. 이는 R2 Stage 3가 진짜 대형 MFE를 잡을 수 있음을 보여주는 강한 benchmark다. ([Reuters][2])

또 2026년 5월 11일 Tom’s Hardware는 SK하이닉스가 Intel EMIB 협업 보도 후 장중 1,946,000원까지 올라 사상 최고가를 찍었다고 보도했다. 이건 Stage 3 이후 4B-watch / price-ahead-of-confirmed-partnership을 붙여야 하는 구간이다. ([Tom's Hardware][3])

### stage date

```text
Stage 1:
2024년 상반기
- HBM3E / Nvidia / AI server memory demand

Stage 2:
2024-06-25
- Nomura 영업이익 추정치 상향
- HBM dominance + DRAM price upcycle
- price anchor = 222,000원

Stage 3:
2024-06-25 후보
- HBM 구조적 수요
- 메모리 가격 상승
- 영업이익 추정치 상향
- old commodity memory frame break

Stage 4B:
2026-05-14
- 2025년 +274%, 2026년 +200% 이상
- 시총 약 $942B
- 1조 달러 근접

추가 4B-watch:
2026-05-11
- Intel EMIB 협업 보도
- 장중 1,946,000원 사상 최고가

Stage 4C:
없음
- 단, HBM 가격하락, capex 과잉, 고객 가격저항, AI capex cut은 4C 후보
```

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch stage3 price anchor + Reuters cumulative return + Tom’s Hardware peak anchor

entry_date:
2024-06-25

stage3_price:
222,000원

peak_price:
1,946,000원 reported intraday high

MFE_from_stage3_to_reported_peak:
(1,946,000 / 222,000) - 1
= +776.6%

reported_market_cap_MFE:
<$100B → $942B
minimum market-cap rerating = +842% 이상

reported_return_2025:
+274%

reported_return_2026_to_2026-05-14:
> +200%

minimum_compounded_return_from_2025_start_to_2026-05-14:
(1 + 2.74) * (1 + 2.00) - 1
= +1,022% 이상

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
price_data_unavailable_after_deep_search

drawdown_after_peak:
관측 필요
```

### alignment

```text
score_price_alignment = aligned
rerating_result = true_rerating
stage_failure_type = green_success
4B_status = 4B-watch / 4B-elevated
```

### 교정

SK하이닉스는 R2에서 다음 축을 올린다.

```text
eps_revision +5
capacity_bottleneck +5
customer_visibility +4
memory_price_upcycle +3
old_frame_mispricing +5
price_path_alignment +5
```

다만 2026년 5월 이후 신규 Stage 3가 아니라 4B-watch다.

---

## Case B — 한미반도체 `structural_success + 4B-watch`

```text
symbol = 042700
case_type = structural_success + 4B-watch
archetype = HBM_BONDER_EQUIPMENT_KOREA / SEMI_EQUIPMENT_AI_CAPEX
```

### evidence

2024년 3월 26일 WSJ는 한미반도체가 SK하이닉스에 HBM 패키징 장비인 TSV-TC bonder를 공급하며, 최근 SK하이닉스와 214.8억 원 계약을 포함해 누적 약 2,000억 원 규모의 최근 계약을 확보했다고 보도했다. 당일 한미반도체 주가는 16% 상승했다. ([월스트리트저널][4])

2024년 3월 28일 WSJ는 한미반도체가 Micron에 HBM 패키징 장비를 공급할 수 있다는 미확정 보도만으로 장중 22% 상승해 139,100원을 기록했다고 보도했다. 양사 모두 당시 해당 media report에 대해 확인하지 않았다. 이 구간은 Stage 3 성공 후보이면서 동시에 빠른 4B-watch가 붙어야 하는 구간이다. ([월스트리트저널][5])

### stage date

```text
Stage 1:
2023~2024
- HBM equipment / TSV-TC bonder / SK Hynix supply chain

Stage 2:
2024-03-26
- SK하이닉스향 TSV-TC bonder 계약
- 최근 계약 누적 약 2,000억 원
- 주가 +16%

Stage 3:
2024-03-26 후보
- 고객사 확인
- 제품 확인
- HBM CAPA 병목과 직접 연결
- 단, 매출 인식·마진·EPS revision은 추가 확인 필요

Stage 4B:
2024-03-28
- Micron 미확정 보도만으로 장중 +22%
- 장중 139,100원
- price ahead of confirmed customer

Stage 4C:
없음
```

### 실제 가격경로 검증

```text
price_data_source:
WSJ reported event return and intraday price anchor

entry_date:
2024-03-26

stage3_price:
price_data_unavailable_after_deep_search
- WSJ는 당일 +16%를 보도했지만 종가 절대값은 제공하지 않음.

stage2_event_MFE_1D:
+16%

stage4b_peak_price:
139,100원

stage4b_event_MFE_1D:
+22%

implied_pre_4B_reference_price:
139,100 / 1.22
= 약 114,016원

MFE_30D / 90D / 180D / 1Y / 2Y:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
success
- 2024-03-28 미확정 Micron 보도 급등은 명확한 4B-watch.
```

### alignment

```text
score_price_alignment = aligned + 4B-watch
rerating_result = HBM_equipment_rerating_candidate
stage_failure_type = green_success_candidate
```

### 교정

한미반도체는 `confirmed_customer_order`와 `unconfirmed_customer_report`를 분리해야 한다.

```text
올릴 축:
confirmed_customer
product_specific_order
HBM_bonder_exposure
order_to_revenue_conversion

내릴 축:
unconfirmed_media_report
customer_diversification_rumor
price_ahead_of_confirmed_order
```

---

## Case C — 삼성전자 `success_candidate / HBM catch-up 보류 + commodity memory rerating`

```text
symbol = 005930
case_type = success_candidate / HBM_CATCHUP_EXECUTION 보류
archetype = HBM_CATCHUP_EXECUTION / COMMODITY_MEMORY_GENERAL_SEMI
```

### evidence

2025년 10월 14일 Reuters는 삼성전자가 2025년 3분기 영업이익을 12.1조 원으로 예상하며 13개 분기 만의 최고 이익을 예고했다고 보도했다. 이는 범용 DRAM/NAND 가격 상승과 데이터센터 서버 수요가 이끈 결과였지만, 동시에 Reuters는 삼성전자가 Nvidia향 HBM 공급에서 SK하이닉스에 뒤처져 있고 HBM 진척은 느렸다고 설명했다. 삼성전자 주가는 장중 2.9% 올라 2021년 1월 이후 최고 수준까지 갔다가 차익실현으로 0.5% 하락 마감했다. ([Reuters][6])

2025년 10월 2일 OpenAI Stargate LOI 이후 Samsung Electronics는 3.5% 상승해 89,000원에 마감했고, SK하이닉스는 9.9% 오른 395,500원에 마감했다. 이 이벤트는 HBM과 AI 데이터센터 수요의 강도를 보여주지만, 삼성전자의 HBM catch-up Stage 3를 자동으로 보장하지는 않는다. ([월스트리트저널][7])

### stage date

```text
Stage 1:
2024~2025
- Samsung HBM catch-up 기대
- AI memory cycle 회복

Stage 2:
2025-10-14
- Q3 2025 영업이익 12.1조 원 예상
- commodity DRAM/NAND 가격 상승
- 데이터센터 서버 수요 확인

Stage 3:
보류
- commodity memory recovery는 Stage 2~Watch
- HBM Green은 Nvidia qualification, HBM sales growth, volume shipment, margin 확인 필요

Stage 4B:
2025-10-02 / 2025-10-14
- OpenAI LOI / earnings surprise로 가격이 먼저 확장
- 삼성전자 89,000원 close anchor

Stage 4C:
없음
- 단, HBM qualification 지연, 파업/생산차질, 중국 규제, 고객 주문 차질은 4C-watch
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters / WSJ reported event return and close anchor

stage3_price:
N/A, Stage 3 미부여

stage2_event_2025-10-14:
intraday MFE = +2.9%
close MAE relative to previous close = -0.5%

OpenAI_event_close_price:
89,000원

OpenAI_event_return:
+3.5%

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
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
score_price_alignment = success_candidate / evidence_good_but_price_failed 후보
rerating_result = commodity_memory_rerating_watch
stage_failure_type = should_have_been_yellow_or_watch
```

### 교정

삼성전자는 R2에서 `commodity_memory_recovery`와 `HBM_leadership`을 분리해야 한다.

```text
Stage 2 가능:
commodity DRAM/NAND price up
earnings surprise
OpenAI LOI

Stage 3 조건:
HBM customer qualification
HBM sales growth
volume shipment
HBM margin
EPS/FCF revision from AI memory
```

---

## Case D — 가온칩스 `success_candidate / design-win Stage 2`

```text
symbol = 399720
case_type = success_candidate
archetype = SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER / AI_CHIP_FABRIC_INFRA
```

### evidence

2024년 7월 9일 Reuters는 삼성전자가 일본 Preferred Networks의 AI chip을 2nm GAA 공정과 advanced packaging으로 생산하는 첫 공개 수주를 확보했고, 해당 AI chip 설계를 가온칩스가 맡았다고 보도했다. 이 칩은 생성AI와 대형언어모델용 high-performance computing hardware에 들어가는 구조다. ([Reuters][8])

### stage date

```text
Stage 1:
2024년
- AI chip / system semiconductor / Samsung 2nm GAA 기대

Stage 2:
2024-07-09
- Preferred Networks AI chip design
- Samsung 2nm GAA + advanced packaging
- company-level design-win evidence

Stage 3:
없음
- design win만으로는 Green 금지
- tape-out, 양산, 매출 인식, margin 확인 필요

Stage 4B:
AI chip design house 테마로 가격이 먼저 급등한 구간이 있으면 후보

Stage 4C:
tape-out delay, yield failure, 고객 취소, no revenue 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters evidence source only

stage3_price:
N/A

stage2_price:
price_data_unavailable_after_deep_search
- Reuters 기사에는 가격반응 anchor가 없음.
- KRX/Naver/Yahoo/Stooq에서 원시 OHLC 직접 확보 실패.

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
```

### alignment

```text
score_price_alignment = unknown_insufficient_evidence
rerating_result = design_win_watch
stage_failure_type = stage2_evidence_not_green
```

### 교정

가온칩스는 `design_win`을 Stage 2로 강하게 인정하되, Stage 3는 늦게 줘야 한다.

```text
Stage 3 조건:
tape-out
mass production
revenue conversion
gross margin
repeat customer
```

---

## Case E — DB하이텍 `event_premium / policy-foundry Stage 1~2`

```text
symbol = 000990
case_type = event_premium / insufficient_evidence
archetype = AI_CHIP_FABRIC_INFRA / POLICY_FOUNDRY_EVENT
```

### evidence

2025년 12월 10일 Reuters는 한국 정부가 4.5조 원 규모 12인치 40nm foundry를 검토하며, 삼성전자와 DB하이텍 같은 국내 foundry 기업과 협의할 것이라고 보도했다. 이 시설은 자동차·데이터센터 등에 쓰이는 legacy chip 개발·테스트를 돕기 위한 공공·민간 공동 투자 구조다. ([Reuters][9])

### stage date

```text
Stage 1:
2025-12-10
- 4.5조 원 public-private foundry 검토
- DB하이텍 협의 대상 언급

Stage 2:
보류 또는 약한 Stage 2
- 정책 방향은 강하지만 회사 단위 계약/투자확정/고객 확보 전

Stage 3:
없음
- government consultation만으로 Green 금지

Stage 4B:
정책 테마로 주가가 먼저 급등하면 4B-watch

Stage 4C:
정책 후퇴, 예산 미반영, 민간 부담 과다, 실질 고객 부재 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters evidence source only

stage3_price:
N/A

stage1_price:
price_data_unavailable_after_deep_search
- Reuters 기사에는 DB하이텍 주가 반응 anchor 없음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

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
score_price_alignment = event_premium / unknown_insufficient_evidence
rerating_result = policy_foundry_watch
stage_failure_type = stage1_attention_only
```

### 교정

DB하이텍은 R2에서 `policy_foundry`를 Stage 3로 올리면 안 되는 반례다.

```text
정책 발표:
Stage 1

협의 대상:
약한 Stage 2

Stage 3 조건:
funded capex
customer order
utilization
gross margin
EPS/FCF revision
```

---

## Case F — 하나마이크론 / 한미반도체 공급망 `4C-watch / export-control shock`

```text
symbols = 067310 / 042700
case_type = 4C-watch
archetype = REDTEAM_ACCOUNTING_TRUST_OVERLAY / GEOPOLITICAL_EXPORT_CONTROL_OVERLAY
```

### evidence

2025년 9월 1일 Reuters는 미국이 삼성전자와 SK하이닉스의 중국 공장에 대한 미국 반도체 장비 반입 허가를 취소하면서, 삼성전자 주가는 2.3%, SK하이닉스는 4.4% 하락했다고 보도했다. 같은 기사에서 하나마이크론은 1.7%, 한미반도체는 4.4% 하락했다. 이 이벤트는 HBM/AI supply chain이 구조적으로 좋아도 지정학·중국 공장·장비 규제가 R2 4C-watch가 될 수 있음을 보여준다. ([Reuters][10])

### stage date

```text
Stage 1:
2025년
- U.S.-China chip export control
- Korean memory makers' China fab exposure

Stage 2:
없음
- negative RedTeam event

Stage 3:
없음

Stage 4B:
AI 반도체 공급망이 과열된 구간에서 규제충격 발생

Stage 4C:
2025-09-01
- U.S. revokes China chip-equipment authorizations
- Samsung -2.3%
- SK Hynix -4.4%
- Hana Micron -1.7%
- Hanmi Semiconductor -4.4%
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event return

stage3_price:
N/A

event_MAE_1D:
Samsung Electronics = -2.3%
SK Hynix = -4.4%
Hana Micron = -1.7%
Hanmi Semiconductor = -4.4%

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
- export-control shock 당일 4C-watch 가능.
- hard 4C는 실제 생산/매출/고객 차질 확인 필요.
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = export_control_4C_watch
stage_failure_type = 4C_watch_not_hard_4C
```

### 교정

R2에는 `export_control`, `China_fab_exposure`, `equipment_access_risk`를 4C-watch로 넣어야 한다.

---

## Case G — SK하이닉스·삼성전자 OpenAI Stargate event `4B-watch / policy-demand validation`

```text
symbols = 000660 / 005930
case_type = 4B-watch
archetype = AI_CAPEX_CROWDING_OVERLAY / MEMORY_HBM_CAPACITY
```

### evidence

2025년 10월 2일 SK하이닉스와 삼성전자는 OpenAI Stargate 프로젝트 관련 LOI 이후 급등했다. Reuters는 삼성전자가 4.7%, SK하이닉스가 12% 상승했고, KOSPI가 3% 넘게 올라 record high를 기록했다고 보도했다. FT는 SK하이닉스가 장중 12%까지 오른 뒤 10% 상승 마감했고, 삼성전자는 장중 약 5% 후 3.5% 상승 마감했다고 보도했다. WSJ는 SK하이닉스가 395,500원에 마감했고 삼성전자가 89,000원에 마감했다고 보도했다. ([Reuters][11])

### stage date

```text
Stage 1:
2025-10-01
- OpenAI Stargate / Korea AI data center / HBM demand expectation

Stage 2:
2025-10-02
- OpenAI LOI
- SK Hynix HBM demand up to 900,000 DRAM wafers/month discussion
- Samsung affiliates data-center cooperation

Stage 3:
SK Hynix는 기존 Stage 3 success anchor 이후 추가 4B evidence
Samsung은 Stage 2~Watch, HBM catch-up 확정 전 Green 보류

Stage 4B:
2025-10-02
- SK Hynix 장중 +12%, 종가 +10% 또는 Reuters 기준 +12%
- Samsung 종가 +3.5~4.7%
- KOSPI record high
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters / FT / WSJ reported return and close price anchors

SK_Hynix_event_MFE_1D:
+12% intraday / +10% close

SK_Hynix_event_close_price:
395,500원

Samsung_event_return:
+3.5% close, Reuters intraday/report +4.7%

Samsung_event_close_price:
89,000원

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A for event row

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = aligned_for_SK_Hynix / event_premium_for_Samsung
rerating_result = AI_memory_demand_validation + 4B_watch
stage_failure_type = 4B_watch
```

### 교정

OpenAI event는 R2에서 **수요 검증이자 4B-watch**다.

```text
SK Hynix:
기존 Stage 3 success가 OpenAI demand로 추가 검증됨.
하지만 이미 4B-watch.

Samsung:
OpenAI LOI는 positive지만 HBM execution이 확인되기 전 Stage 3 보류.
```

---

# 5. 이번 R2 case별 요약표

| case                     | 분류                                |                                                        실제 가격검증 | alignment             |
| ------------------------ | --------------------------------- | -------------------------------------------------------------: | --------------------- |
| SK하이닉스                   | structural_success + 4B           |                    222,000원 → 1,946,000원, +776.6%; 시총 최소 +842% | aligned               |
| 한미반도체                    | structural_success + 4B           |                 SK하이닉스 계약일 +16%; Micron 미확정 보도일 +22%, 139,100원 | aligned + 4B-watch    |
| 삼성전자                     | success_candidate / Stage 2 watch |  OpenAI event 89,000원, +3.5%; Q3 profit event 장중 +2.9% 후 -0.5% | success_candidate     |
| 가온칩스                     | success_candidate                 |                    Preferred Networks design win, 가격 anchor 없음 | insufficient_evidence |
| DB하이텍                    | event_premium                     |                              4.5조 foundry policy, 가격 anchor 없음 | event_premium         |
| 하나마이크론/한미 export-control | 4C-watch                          |                                 Hana Micron -1.7%, Hanmi -4.4% | thesis_break_watch    |
| SK하이닉스/삼성 OpenAI         | 4B-watch                          | SK Hynix +12% intraday / 395,500원 close, Samsung 89,000원 close | 4B-watch              |

---

# 6. score-price alignment 판정

```text
aligned:
- SK하이닉스
- 한미반도체, 단 Micron 미확정 보도 구간은 4B-watch

success_candidate:
- 삼성전자
- 가온칩스

event_premium:
- DB하이텍 policy foundry
- 삼성전자 OpenAI LOI 일부

price_moved_without_evidence:
- 한미반도체 Micron 미확정 보도 구간
- DB하이텍 정책 이벤트 구간

thesis_break_watch:
- 하나마이크론 / 한미반도체 export-control shock
- Samsung / SK Hynix China authorization revocation

4B-watch:
- SK하이닉스 2026 1조 달러 근접
- 한미반도체 Micron 미확정 보도 급등
- OpenAI Stargate event
```

---

# 7. 점수비중 교정

## 올릴 축

```text
eps_revision +5
capacity_bottleneck +5
customer_visibility +5
confirmed_customer_order +5
HBM_product_specificity +4
order_to_revenue_conversion +4
gross_margin_visibility +4
price_path_alignment +5
```

### 왜 올리나

SK하이닉스는 222,000원 Stage 3 anchor에서 1,946,000원 reported high까지 +776.6% MFE가 계산된다. 이건 R2의 `capacity_bottleneck + EPS revision + HBM customer visibility`가 실제 대시세와 맞는다는 강한 증거다. ([마켓워치][1])

한미반도체는 SK하이닉스향 HBM bonder 계약과 최근 누적 2,000억 원 수주가 확인되었고, 당일 주가가 +16% 반응했다. 이건 장비주에서도 고객·제품·계약이 특정될 때 Stage 3 후보가 될 수 있음을 보여준다. ([월스트리트저널][4])

## 내릴 축

```text
ai_keyword_only -5
server_theme_only -4
design_win_without_revenue -4
policy_foundry_without_order -4
unconfirmed_media_report -5
OpenAI_or_Nvidia_event_without_company_revenue -3
customer_name_without_margin -3
price_rally_before_confirmation -5
```

### 왜 내리나

한미반도체의 Micron 보도 급등은 미확정 media report였고, DB하이텍은 정부 foundry 협의 대상일 뿐 회사 단위 계약·매출·마진이 확인되지 않았다. 가온칩스도 design win은 강하지만 tape-out·양산·매출 전 Stage 3가 아니다. ([월스트리트저널][5])

## Green gate 강화 조건

```text
R2 Stage 3-Green 필수:
1. company-level customer evidence
2. product-specific exposure
3. order / shipment / contract / revenue path 확인
4. gross margin 또는 OPM 개선
5. EPS/FCF revision
6. capacity bottleneck 또는 supply allocation
7. 가격경로가 evidence 이후 따라옴
8. export-control / China fab / accounting trust 통과

금지:
AI 이름만 있음
서버 테마만 있음
미확정 고객 보도
design win만 있음
정책 foundry만 있음
OpenAI/Nvidia partnership headline만 있음
```

## 4B 조기감지 조건

```text
4B-watch:
Stage 3 이후 3배 이상 상승
시총 milestone이 headline화
미확정 고객 다변화 보도에 급등
OpenAI / Nvidia / Stargate 이벤트로 지수와 함께 급등
AI CAPEX consensus가 한쪽으로 몰림
신규 수주에도 주가가 valuation으로 먼저 움직임

4B-elevated:
SK Hynix처럼 1조 달러 시총 근접
한미반도체처럼 고객 rumor만으로 +20%대 급등
Samsung처럼 commodity memory는 좋아도 HBM execution lag가 남음
```

## 4C hard gate 조건

```text
HBM qualification failure
order push-out
customer capex cut
memory price decline
HBM supply normalization
China fab export-control disruption
equipment authorization loss
accounting or disclosure trust break
production strike / labor disruption
customer concentration failure
```

이번 라운드에서는 export-control shock을 hard 4C로 확정하지 않고 **4C-watch**로 둔다. 실제 생산 차질, 매출 차질, 고객 주문 취소가 확인될 때 hard 4C로 승격한다.

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

이번 세션에서 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉을 안정적으로 직접 확보하지 못했다. 대신 Reuters / WSJ / FT / MarketWatch / Tom’s Hardware의 가격 anchor와 이벤트 수익률을 사용해 계산 가능한 부분은 직접 계산했다.

---

# 9. patch-ready 출력

## docs/round/round_134.md 요약

```md
# R2 Loop 8. AI / Semiconductor / Electronics Price Validation

이번 라운드는 R13 이후 다시 R2로 온 price-validation 라운드다.

핵심 결론:
- SK하이닉스는 2024-06-25 222,000원 Stage 3 anchor에서 2026년 reported high 1,946,000원까지 +776.6% MFE가 확인된다. 현재는 신규 Stage 3가 아니라 4B-watch다.
- 한미반도체는 SK하이닉스향 TSV-TC bonder 계약과 누적 약 2,000억 원 계약으로 Stage 3 후보가 가능하지만, Micron 미확정 보도 +22% 급등은 4B-watch다.
- 삼성전자는 범용 메모리 회복과 OpenAI event로 Stage 2 후보지만, HBM catch-up 실행 전 Stage 3-Green은 보류한다.
- 가온칩스는 Preferred Networks AI chip design win으로 Stage 2 후보지만, tape-out·양산·매출 전 Green 금지다.
- DB하이텍은 policy foundry event로 Stage 1~2 attention이지만, 회사 단위 계약·매출 전 Green 금지다.
- 하나마이크론·한미반도체 export-control shock은 R2 4C-watch다.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 134 R2 Loop 8 AI Semiconductor Price Validation

## 반영 내용
- R2 price-validation 라운드를 추가했다.
- HBM leader, HBM equipment, HBM catch-up, design house, policy foundry, export-control shock을 비교했다.
- Reuters/WSJ/FT/MarketWatch/Tom's Hardware reported price anchors로 가능한 MFE/MAE를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- EPS revision, capacity bottleneck, customer visibility, confirmed customer order 강화
- 미확정 media report, policy foundry, design win without revenue 감점 강화
- 4B-watch 민감도 강화
- export-control 4C-watch 추가
```

## case row 초안

```jsonl
{"case_id":"r2_loop8_sk_hynix_hbm_aligned_4b","symbol":"000660","company_name":"SK하이닉스","case_type":"structural_success","primary_archetype":"MEMORY_HBM_CAPACITY","stage2_date":"2024-06-25","stage3_date":"2024-06-25","stage4b_date":"2026-05-14","price_validation":{"price_data_source":"MarketWatch/Reuters/Tom's Hardware reported anchors","stage3_price":222000,"peak_price":1946000,"peak_return_from_stage3":776.6,"market_cap_mfe_minimum":842.0,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"aligned","rerating_result":"true_rerating","notes":"HBM dominance and EPS revision produced large MFE; now 4B-watch."}
{"case_id":"r2_loop8_hanmi_semiconductor_hbm_bonder_4b","symbol":"042700","company_name":"한미반도체","case_type":"structural_success","primary_archetype":"HBM_BONDER_EQUIPMENT_KOREA","stage2_date":"2024-03-26","stage3_date":"2024-03-26","stage4b_date":"2024-03-28","price_validation":{"price_data_source":"WSJ reported event anchors","mfe_1d_stage2":16.0,"stage4b_peak_price":139100,"mfe_1d_stage4b":22.0,"implied_pre_4b_reference_price":114016,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"aligned","rerating_result":"HBM_equipment_rerating_candidate","notes":"Confirmed SK Hynix orders support Stage 3 candidate; unconfirmed Micron media report is 4B-watch."}
{"case_id":"r2_loop8_samsung_memory_recovery_hbm_watch","symbol":"005930","company_name":"삼성전자","case_type":"success_candidate","primary_archetype":"HBM_CATCHUP_EXECUTION","stage2_date":"2025-10-14","price_validation":{"price_data_source":"Reuters/WSJ reported anchors","stage3_price":null,"event_intraday_mfe":2.9,"event_close_return":-0.5,"openai_event_close_price":89000,"openai_event_return":3.5,"price_validation_status":"stage2_watch_not_stage3"},"score_price_alignment":"success_candidate","rerating_result":"commodity_memory_rerating_watch","notes":"Commodity memory recovery is Stage 2; HBM execution needed for Stage 3."}
{"case_id":"r2_loop8_gaonchips_pfn_design_win","symbol":"399720","company_name":"가온칩스","case_type":"success_candidate","primary_archetype":"SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER","stage2_date":"2024-07-09","price_validation":{"price_data_source":"Reuters evidence only","stage3_price":null,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"unknown_insufficient_evidence","rerating_result":"design_win_watch","notes":"Preferred Networks AI chip design win is Stage 2; tape-out, volume production and revenue required for Stage 3."}
{"case_id":"r2_loop8_db_hitek_policy_foundry","symbol":"000990","company_name":"DB하이텍","case_type":"event_premium","primary_archetype":"AI_CHIP_FABRIC_INFRA","stage1_date":"2025-12-10","price_validation":{"price_data_source":"Reuters evidence only","stage3_price":null,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium","rerating_result":"policy_foundry_watch","notes":"Government foundry consultation is not revenue evidence."}
{"case_id":"r2_loop8_hana_micron_hanmi_export_control_watch","symbol":"067310/042700","company_name":"하나마이크론/한미반도체","case_type":"4c_watch","primary_archetype":"GEOPOLITICAL_EXPORT_CONTROL_OVERLAY","stage4c_date":"2025-09-01","price_validation":{"price_data_source":"Reuters reported event returns","hana_micron_mae_1d":-1.7,"hanmi_mae_1d":-4.4,"samsung_mae_1d":-2.3,"sk_hynix_mae_1d":-4.4,"price_validation_status":"reported_event_return_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"export_control_4C_watch","notes":"Export-control shock is 4C-watch; hard 4C requires actual production/revenue disruption."}
{"case_id":"r2_loop8_openai_stargate_memory_4b","symbol":"000660/005930","company_name":"SK하이닉스/삼성전자","case_type":"4b_watch","primary_archetype":"AI_CAPEX_CROWDING_OVERLAY","stage2_date":"2025-10-02","stage4b_date":"2025-10-02","price_validation":{"price_data_source":"Reuters/FT/WSJ reported anchors","sk_hynix_mfe_1d_intraday":12.0,"sk_hynix_close_return":10.0,"sk_hynix_close_price":395500,"samsung_close_return":3.5,"samsung_close_price":89000,"price_validation_status":"reported_event_return_not_full_ohlc"},"score_price_alignment":"aligned_for_sk_hynix_event_premium_for_samsung","rerating_result":"AI_memory_demand_validation_4B_watch","notes":"OpenAI LOI validates demand but also marks 4B-watch after large rerating."}
```

## shadow weight row 초안

```csv
archetype,eps_revision,capacity_bottleneck,customer_visibility,confirmed_order,margin_visibility,price_path_alignment,event_premium_penalty,export_control_redteam,4b_watch_sensitivity,notes
MEMORY_HBM_CAPACITY,+5,+5,+5,+4,+4,+5,0,+2,+5,SK Hynix confirms large MFE from HBM and EPS revision but now requires 4B-watch.
HBM_BONDER_EQUIPMENT_KOREA,+3,+5,+5,+5,+3,+4,-2,+2,+5,Hanmi confirmed SK Hynix order supports Stage 3 candidate; Micron rumor is 4B-watch.
HBM_CATCHUP_EXECUTION,+3,+3,+3,+2,+3,+3,-2,+3,+4,Samsung commodity memory recovery is Stage 2; HBM execution needed before Green.
SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER,+2,+2,+3,+2,+2,+2,-3,+1,+3,Gaonchips design win is Stage 2 until tape-out/revenue/margin.
AI_CHIP_FABRIC_INFRA,+1,+2,+1,+1,+1,+1,-4,+1,+3,DB HiTek policy foundry consultation is not Stage 3 evidence.
GEOPOLITICAL_EXPORT_CONTROL_OVERLAY,0,0,0,0,0,+2,0,+5,+3,Export-control shock becomes 4C-watch until actual production or revenue disruption is proven.
AI_CAPEX_CROWDING_OVERLAY,+2,+3,+3,+2,+1,+3,-3,+2,+5,OpenAI/Stargate validates demand but also accelerates 4B-watch.
```

---

# 이번 R2 Loop 8 결론

R2는 Stage 3가 실제로 대형 수익률을 만들 수 있는 섹터다. 하지만 가장 쉽게 false positive가 생기는 섹터이기도 하다.

```text
1. SK하이닉스는 Stage 3가 잘 잡히면 대형 MFE가 나온다는 강한 증거다.
   222,000원 anchor에서 1,946,000원 reported high까지 +776.6% MFE가 계산된다.

2. 한미반도체는 HBM 장비주도 Stage 3 후보가 될 수 있음을 보여준다.
   단, confirmed SK Hynix order와 unconfirmed Micron rumor를 반드시 분리해야 한다.

3. 삼성전자는 범용 메모리 회복으로 Stage 2 후보지만,
   HBM catch-up execution 전 Stage 3-Green은 보류해야 한다.

4. 가온칩스는 design win만으로 Green 금지다.
   tape-out, 양산, 매출, margin이 필요하다.

5. DB하이텍은 정책 foundry event일 뿐이다.
   회사 단위 order / utilization / EPS 전 Green 금지다.

6. R2 4C는 export-control, China fab exposure, HBM qualification failure, customer capex cut에서 온다.

7. OpenAI/Stargate 같은 대형 수요 이벤트는 positive evidence이지만,
   이미 크게 오른 HBM winner에게는 동시에 4B-watch다.
```

한 문장으로 압축하면:

> **R2에서 진짜 Stage 3는 “AI 반도체 수혜”가 아니라, HBM·장비·패키징·메모리 가격이 고객 주문·CAPA 병목·마진·EPS revision으로 내려오고 가격경로가 뒤따르는 순간이다.**
> **그리고 R2는 HBM winner가 맞아도 4B가 빨리 붙어야 한다. AI 수요가 사실이어도 가격은 더 빨리 달릴 수 있다.**

[1]: https://www.marketwatch.com/story/sk-hynix-s-hbm-dominance-higher-chip-prices-could-lift-earnings-market-talk-6508cbf8?utm_source=chatgpt.com "SK Hynix's HBM Dominance, Higher Chip Prices Could Lift Earnings -- Market Talk"
[2]: https://www.reuters.com/world/asia-pacific/ai-boom-puts-sk-hynix-cusp-1-trillion-market-value-2026-05-14/?utm_source=chatgpt.com "AI boom puts SK Hynix on cusp of $1 trillion market value"
[3]: https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-shares-surge-to-all-time-high-on-reports-of-intel-emib-partnership?utm_source=chatgpt.com "Intel, SK hynix shares surge following reports of chip packaging partnership - SK is said to be testing Intel's 2.5D EMIB for HBM integration"
[4]: https://www.wsj.com/articles/south-korean-chip-shares-rally-as-ai-frenzy-persists-260f9996?utm_source=chatgpt.com "South Korean Chip Shares Rally as AI Frenzy Persists"
[5]: https://www.wsj.com/articles/hanmi-semiconductor-climbs-after-media-reports-of-possible-deal-with-micron-e85398fb?utm_source=chatgpt.com "Hanmi Semiconductor Climbs After Media Reports of Possible Deal With Micron"
[6]: https://www.reuters.com/world/asia-pacific/samsung-elec-estimates-32-rise-q3-operating-profit-beating-expectations-2025-10-13/?utm_source=chatgpt.com "Samsung expects best profit since 2022, as AI boom squeezes commodity chip supply"
[7]: https://www.wsj.com/finance/samsung-sk-hynix-rally-on-partnership-with-openai-for-stargate-project-54937adf?utm_source=chatgpt.com "Samsung, SK Hynix Rally on Partnership With OpenAI for Stargate Project"
[8]: https://www.reuters.com/technology/artificial-intelligence/samsung-electronics-wins-cutting-edge-ai-chip-order-japans-preferred-networks-2024-07-09/?utm_source=chatgpt.com "Samsung Electronics wins cutting-edge AI chip order from Japan's Preferred Networks"
[9]: https://www.reuters.com/world/asia-pacific/south-korea-consider-setting-up-31-bln-foundry-grow-local-chip-sector-2025-12-10/?utm_source=chatgpt.com "South Korea to consider setting up $3.1 bln foundry to grow local chip sector"
[10]: https://www.reuters.com/world/china/shares-samsung-sk-hynix-drop-after-us-makes-it-harder-make-chips-china-2025-09-01/?utm_source=chatgpt.com "Shares in Samsung, SK Hynix drop after US makes it harder to make chips in China"
[11]: https://www.reuters.com/world/asia-pacific/samsung-sk-hynix-shares-rally-openai-partnerships-2025-10-02/?utm_source=chatgpt.com "Samsung, SK Hynix shares leap after OpenAI chip deal"
