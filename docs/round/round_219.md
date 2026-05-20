순서상 이번은 **R2 Loop 9 — AI·반도체·전자부품 가격경로 검증 라운드**다.

이번 라운드는 HBM 리더만 반복하지 않고, **HBM4 리더십, 삼성전자 catch-up/노동 리스크, HBM 장비주, AI 디자인하우스, 정책 foundry, OpenAI/Stargate event, 미중 export-control 4C-watch**를 같이 봤다.

```text
round = R2 Loop 9
round_id = round_147
large_sector = AI_SEMICONDUCTOR_ELECTRONICS
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
```

원시 수정주가 일봉 OHLC는 이번 환경에서 안정적으로 직접 확보하지 못했다. 대신 Reuters / MarketWatch / WSJ / AP / Tom’s Hardware가 제공한 **가격 anchor, 이벤트 수익률, 시총, 계약·정책 지표**로 계산 가능한 값만 계산했다.

---

# 1. 이번 라운드 대섹터

```text
R2 = AI·반도체·전자부품
```

R2의 핵심은 “AI 반도체 수혜”가 아니라, **고객 주문·CAPA 병목·HBM 세대 전환·마진·EPS revision·가격경로가 같이 맞는가**다.

---

# 2. 대상 canonical archetype

```text
MEMORY_HBM_CAPACITY
MEMORY_HBM4_FIRST_MOVER
MEMORY_SUPERCYCLE_AI_CAPEX
HBM_CATCHUP_EXECUTION
HBM_BONDER_EQUIPMENT_KOREA
SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER
AI_CHIP_FABRIC_INFRA
POLICY_FOUNDRY_EVENT
OPENAI_STARGATE_AI_CAPEX_EVENT
GEOPOLITICAL_EXPORT_CONTROL_OVERLAY
LABOR_SUPPLY_CHAIN_4C_WATCH
PRICE_ONLY_RALLY
```

---

# 3. deep sub-archetype

```text
HBM leader:
- SK Hynix
- HBM dominance
- HBM4 internal certification
- Nvidia customer visibility
- AI capex demand
- memory supercycle
- market-cap milestone
- 4B crowding

Samsung catch-up:
- Samsung Electronics
- HBM3E / HBM4 catch-up
- OpenAI Stargate demand
- Q3 operating profit recovery
- labor strike risk
- foundry/logic division weakness
- production disruption risk

HBM equipment:
- Hanmi Semiconductor
- TSV-TC bonder
- SK Hynix confirmed order
- Micron unconfirmed media report
- customer diversification rumor vs confirmed contract

AI design house:
- Gaonchips
- Preferred Networks AI chip
- Samsung 2nm GAA foundry
- design win vs mass production

Policy foundry:
- DB HiTek
- 40nm public-private foundry
- government consultation vs funded order
- defense semiconductor localization

RedTeam:
- U.S. China equipment authorization revocation
- Samsung/SK Hynix China fab exposure
- Hana Micron / Hanmi supplier selloff
- labor strike and production halt
```

---

# 4. 국장 신규 후보 case

## Case A — SK하이닉스 `structural_success + 4B-watch`

```text
symbol = 000660
case_type = structural_success + 4B-watch
archetype = MEMORY_HBM_CAPACITY / MEMORY_HBM4_FIRST_MOVER
```

### stage date

```text
Stage 1:
2024년 상반기
- HBM3E / Nvidia / AI server demand
- old commodity memory frame break

Stage 2:
2024-06-25
- Nomura가 2024 OP 30조 원, 2025 OP 53조 원으로 추정치 상향
- HBM dominance + DRAM price upcycle + EPS revision
- price anchor = 222,000원

Stage 3:
2024-06-25 후보
- HBM 지배력
- 메모리 가격 상승
- EPS revision
- AI server capacity bottleneck

추가 Stage 3 validation:
2025-09-12
- HBM4 internal certification 완료
- mass production preparation
- 주가 장중 +7.3%, KOSPI +1.2%
- HBM share 2026년 low-60% 전망

Stage 4B:
2026-05-04
- AI capex 상향 기대에 종가 +12.52%, 1,447,000원 record high

추가 Stage 4B:
2026-05-14
- 2025년 +274%, 2026년 +200% 이상
- 시총 약 $942B, 1조 달러 근접

Stage 4C:
없음
- 단, AI capex cut, HBM 가격 하락, 고객 가격저항, supply normalization은 4C 후보
```

Nomura는 2024년 6월 25일 SK하이닉스의 HBM 지배력과 메모리 가격 상승을 이유로 2024년 영업이익 추정치를 30조 원, 2025년을 53조 원으로 상향했고, 당시 주가는 222,000원이었다. 2025년 9월에는 SK하이닉스가 HBM4 내부 인증을 완료하고 양산 준비에 들어갔으며, 주가는 장중 7.3% 올라 KOSPI 1.2% 상승을 크게 웃돌았다. 2026년 5월 4일에는 미국 빅테크 AI capex 상향 기대에 종가 기준 12.52% 올라 1,447,000원 record high를 찍었다. ([마켓워치][1])

2026년 5월 14일 Reuters는 SK하이닉스가 2025년에 274%, 2026년에 200% 넘게 올랐고, 시가총액이 16개월 전 1,000억 달러 미만에서 약 9,420억 달러까지 커졌다고 보도했다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch / Reuters reported price and return anchors

entry_date:
2024-06-25

stage3_price:
222,000원

2025-09-12 HBM4 event:
MFE_1D_intraday = +7.3%
KOSPI same context = +1.2%
relative_outperformance = +6.1pp

2026-05-04 record close:
1,447,000원

MFE_from_stage3_to_2026-05-04_record_close:
(1,447,000 / 222,000) - 1
= +551.8%

reported_return_2025:
+274%

reported_return_2026_to_2026-05-14:
> +200%

minimum_compounded_return_from_2025_start_to_2026-05-14:
(1 + 2.74) * (1 + 2.00) - 1
= +1,022% 이상

market_cap_path:
< $100B → 약 $942B

minimum_market_cap_MFE:
(942 / 100) - 1
= +842% 이상

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
price_data_unavailable_after_deep_search

peak_price:
1,447,000원 reported close anchor, later peak unavailable in this pass

drawdown_after_peak:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = aligned
rerating_result = true_rerating
stage_failure_type = green_success
4B_status = 4B-watch / 4B-elevated
```

### 교정

```text
올릴 축:
eps_revision +5
capacity_bottleneck +5
HBM4_first_mover +5
customer_visibility +5
memory_price_upcycle +4
price_path_alignment +5

4B 강화:
market_cap_milestone
AI_capex_consensus_crowding
reported_1Y_multi_bagger
```

---

## Case B — 삼성전자 `success_candidate + labor/production 4C-watch`

```text
symbol = 005930
case_type = success_candidate + 4C-watch
archetype = HBM_CATCHUP_EXECUTION / LABOR_SUPPLY_CHAIN_4C_WATCH
```

### stage date

```text
Stage 1:
2024~2025
- Samsung HBM catch-up
- AI memory cycle recovery
- one-stop semiconductor provider narrative

Stage 2:
2025-10-02
- OpenAI Stargate partnership
- Samsung +4.7%
- highest in more than four years

추가 Stage 2:
2025 Q3
- operating profit 12.2조 원, +32.5%
- revenue 86조 원
- semiconductor division OP 7조 원
- HBM3E mass production / HBM4 sample shipment

Stage 3:
보류
- HBM catch-up은 고객 인증, volume shipment, Nvidia/AI accelerator sales, margin 확인 전 Green 금지

Stage 4B:
2026-05-06
- Samsung +14.4%, $1T market cap milestone
- KOSPI +6.45%

Stage 4C-watch:
2026-05-15
- strike plan 유지 보도 후 Samsung -9.3%
- 45,000~50,000명 이상 strike risk
- JPMorgan OP loss estimate 21~31조 원
```

OpenAI Stargate 협력 보도 후 삼성전자는 4.7% 올랐고, 2025년 3분기에는 영업이익 12.2조 원, 매출 86조 원을 기록하며 AI memory 회복을 보였다. 다만 삼성은 HBM catch-up이 진행 중인 상태이고, HBM volume shipment와 고객별 margin이 Stage 3 조건이다. 2026년 5월에는 노동 리스크가 커졌고, 노조가 18일 파업 계획을 유지한다는 보도 후 주가가 9.3% 하락했다. JPMorgan은 파업 시 영업이익 손실을 21~31조 원으로 추정했다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / AP reported event anchors

stage3_price:
N/A

OpenAI_event_return:
+4.7%

Q3_2025_operating_profit:
12.2T won

Q3_2025_OP_growth:
+32.5%

Q3_2025_revenue:
86T won

semiconductor_division_OP:
7T won

2026-05-06_AI_rally_event:
Samsung +14.4%
KOSPI +6.45%
relative_outperformance = +7.95pp

2026-05-15_strike_event_MAE:
-9.3%

JPMorgan_estimated_OP_loss:
21T~31T won

sales_opportunity_loss:
about 4.5T won

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

Stage 4C 큰 하락 이전 포착 여부:
partial_success
- strike risk는 4C-watch로 선제 반영 가능.
```

### alignment

```text
score_price_alignment = success_candidate + 4C-watch
rerating_result = HBM_catchup_plus_labor_risk
stage_failure_type = should_have_been_yellow_or_watch_until_volume_HBM_sales
```

### 교정

```text
올릴 축:
Q3_OP_recovery
HBM_sample_shipment
OpenAI_demand_validation

내릴 축:
HBM_catchup_not_leadership
labor_strike_risk
foundry_logic_losses
production_disruption_risk
```

---

## Case C — 한미반도체 `structural_success_candidate + 4B-watch`

```text
symbol = 042700
case_type = structural_success_candidate + 4B-watch
archetype = HBM_BONDER_EQUIPMENT_KOREA
```

### stage date

```text
Stage 1:
2023~2024
- HBM packaging equipment
- TSV-TC bonder
- SK Hynix supply chain

Stage 2:
2024-03-26 전후
- SK하이닉스향 214.8억 원 contract
- 최근 계약 누적 약 2,000억 원

Stage 3:
조건부 후보
- confirmed customer order
- product-specific HBM equipment exposure
- 단, 매출 인식·마진·EPS revision 확인 필요

Stage 4B:
2024-03-28
- Micron 미확정 보도만으로 장중 +22%
- 139,100원
- KOSPI -0.3%
```

한미반도체는 SK하이닉스향 HBM 패키징 장비 계약과 최근 누적 약 2,000억 원 계약이 확인되어 Stage 2~3 후보가 될 수 있다. 그러나 2024년 3월 28일 Micron 공급 가능성에 대한 미확정 보도만으로 주가가 장중 22% 올라 139,100원을 기록한 구간은 명확한 4B-watch다. 양사는 당시 보도에 대해 확인하지 않았다. ([월스트리트저널][4])

### 실제 가격경로 검증

```text
price_data_source:
WSJ reported price and contract anchors

stage3_price:
price_data_unavailable_after_deep_search
- WSJ는 confirmed SK Hynix order와 Micron rumor event는 제공하지만 2024-03-26 종가 절대값은 제공하지 않음.

confirmed_SK_Hynix_contract:
21.48B won

recent_deals_total:
about 200B won

stage4b_peak_price:
139,100원

stage4b_event_MFE_1D:
+22%

implied_pre_4B_reference_price:
139,100 / 1.22
= 약 114,016원

KOSPI_same_context:
-0.3%

relative_outperformance:
22 - (-0.3)
= +22.3pp

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
success
- unconfirmed Micron media report 급등은 4B-watch.
```

### alignment

```text
score_price_alignment = aligned_candidate + 4B_watch
rerating_result = HBM_equipment_rerating_candidate
stage_failure_type = confirmed_order_good_but_unconfirmed_customer_rumor_4B
```

### 교정

```text
올릴 축:
confirmed_customer_order +5
product_specific_HBM_equipment +5
order_to_revenue_conversion +4

내릴 축:
unconfirmed_media_report -5
customer_diversification_rumor -4
price_rally_before_confirmation -5
```

---

## Case D — 가온칩스 `success_candidate / design-win Stage 2`

```text
symbol = 399720
case_type = success_candidate / insufficient_price_data
archetype = SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER
```

### stage date

```text
Stage 1:
2024년
- AI chip design house
- Samsung advanced foundry ecosystem

Stage 2:
2024-07-09
- Preferred Networks AI chip design
- Samsung 2nm GAA + advanced packaging
- generative AI / LLM high-performance computing hardware

Stage 3:
없음
- design win만으로 Green 금지
- tape-out, mass production, revenue recognition, gross margin 확인 필요

Stage 4B:
AI chip design house theme으로 주가가 먼저 급등하면 후보

Stage 4C:
tape-out delay, yield issue, customer cancellation, no revenue conversion 시 후보
```

Samsung은 일본 Preferred Networks의 AI chip을 2nm GAA 공정과 advanced packaging으로 생산하는 첫 공개 수주를 확보했고, 이 칩 설계는 한국의 가온칩스가 맡았다. 이 칩은 생성AI와 대형언어모델용 high-performance computing hardware에 사용될 예정이다. 다만 Samsung은 주문 규모를 공개하지 않았고, 가온칩스의 매출 전환도 확인되지 않았다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters evidence source

stage3_price:
N/A

stage2_price:
price_data_unavailable_after_deep_search
- Reuters는 가온칩스 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

order_size:
not disclosed

technology:
Samsung 2nm GAA + advanced packaging

customer:
Preferred Networks

end_use:
generative AI / LLM high-performance computing hardware

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = unknown_insufficient_evidence
rerating_result = design_win_watch
stage_failure_type = stage2_evidence_not_green
```

### 교정

```text
Stage 2:
design win

Stage 3 조건:
tape-out
mass production
revenue recognition
gross margin
repeat customer
```

---

## Case E — DB하이텍 `event_premium / policy foundry Stage 1~2`

```text
symbol = 000990
case_type = event_premium / policy_watch
archetype = AI_CHIP_FABRIC_INFRA / POLICY_FOUNDRY_EVENT
```

### stage date

```text
Stage 1:
2025-12-10
- 4.5조 원 public-private foundry 검토
- 12-inch / 40nm facility
- 자동차·데이터센터 legacy chip
- Samsung / DB HiTek consultation

Stage 2:
보류 또는 약한 Stage 2
- 정책 방향은 강하지만 회사 단위 계약·투자확정·고객 확보 전

Stage 3:
없음
- government consultation만으로 Green 금지

Stage 4B:
정책 foundry 테마로 주가가 먼저 급등하면 후보

Stage 4C:
예산 미반영, 민간 부담 과다, 고객 부재, utilization failure 시 후보
```

한국 정부는 AI 시대 반도체 경쟁력 강화를 위해 4.5조 원 규모 12인치 40nm foundry 설립을 검토하고 있으며, Samsung과 DB HiTek 같은 foundry 기업들과 협의할 것이라고 밝혔다. 이 시설은 자동차·데이터센터용 legacy chip 개발·테스트를 지원하고, 방산용 반도체 국산화를 목표로 한다. 그러나 이는 **정책·협의 단계**이지 DB하이텍 회사 단위 수주나 매출 evidence가 아니다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters policy evidence source

stage3_price:
N/A

stage1_price:
price_data_unavailable_after_deep_search
- Reuters는 DB하이텍 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

foundry_project_size:
4.5T won / $3.06B

process_node:
40nm

wafer_size:
12-inch

defense_semiconductor_import_dependency:
99%

company_status:
consultation target, not confirmed order

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = event_premium / policy_watch
rerating_result = policy_foundry_watch
stage_failure_type = stage1_attention_only
```

### 교정

```text
정책 발표:
Stage 1

협의 대상:
약한 Stage 2

Stage 3 조건:
funded capex
company-level order
customer commitment
utilization
gross margin
EPS/FCF revision
```

---

## Case F — OpenAI/Stargate memory event `4B-watch / demand validation`

```text
symbols = 000660 / 005930
case_type = 4B-watch
archetype = OPENAI_STARGATE_AI_CAPEX_EVENT / MEMORY_HBM_CAPACITY
```

### stage date

```text
Stage 1:
2025-10-01
- OpenAI Stargate
- Samsung / SK partnership

Stage 2:
2025-10-02
- semiconductor procurement agreement
- two Korean data centers, initial 20MW
- demand up to 900,000 DRAM wafers/month

Stage 3:
SK Hynix는 기존 Stage 3 success의 demand validation
Samsung은 HBM catch-up 확인 전 Stage 2~Watch

Stage 4B:
2025-10-02
- SK Hynix +12%
- Samsung +4.7%
- combined market cap +$37B
- KOSPI +3% record
```

OpenAI는 Samsung과 SK와 Stargate 관련 반도체 조달과 한국 데이터센터 협력을 발표했고, Reuters는 Samsung이 4.7%, SK Hynix가 12% 상승했으며 두 회사 시가총액이 합산 370억 달러 증가했다고 보도했다. Tom’s Hardware는 Stargate 수요가 월 900,000개 DRAM wafer까지 커질 수 있으며, 이는 전체 DRAM output의 약 40%에 해당할 수 있다고 정리했다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / Tom’s Hardware reported anchors

stage3_price:
N/A for event row

SK_Hynix_event_MFE_1D:
+12%

Samsung_event_MFE_1D:
+4.7%

combined_market_cap_added:
$37B

KOSPI_event_return:
> +3%

OpenAI_expected_DRAM_wafers_monthly:
900,000 wafers/month

share_of_global_DRAM_output:
about 40%

implied_global_DRAM_output:
900,000 / 0.40
= 2.25M wafers/month

AI_project_scale:
$500B Stargate initiative

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
success
- demand validation이지만, 이미 오른 winners에는 4B-watch.
```

### alignment

```text
score_price_alignment = aligned_for_SK_Hynix / event_premium_for_Samsung
rerating_result = AI_memory_demand_validation_4B_watch
stage_failure_type = 4B_watch
```

### 교정

```text
SK Hynix:
demand validation + 4B

Samsung:
positive Stage 2, but HBM execution before Green

공통:
OpenAI headline만으로 후발주 Green 금지
```

---

## Case G — export-control shock `4C-watch / China fab exposure`

```text
symbols = 005930 / 000660 / 067310 / 042700
case_type = 4C-watch
archetype = GEOPOLITICAL_EXPORT_CONTROL_OVERLAY
```

### stage date

```text
Stage 1:
2025년
- U.S.-China chip export control
- China fab exposure

Stage 2:
없음
- negative RedTeam event

Stage 3:
없음

Stage 4B:
AI semiconductor supply chain이 과열된 구간에서 규제충격 발생

Stage 4C-watch:
2025-09-01
- U.S. revokes China equipment authorizations
- Samsung -2.3%
- SK Hynix -4.4%
- Hana Micron -1.7%
- Hanmi Semiconductor -4.4%
```

미국은 Samsung과 SK Hynix의 중국 공장에 미국산 반도체 제조장비를 들여올 수 있게 했던 authorization을 취소했다. Samsung DRAM 생산의 3분의 1 이상, SK Hynix DRAM/NAND의 30~40%가 중국에 기반하고 있다는 분석이 보도됐고, 같은 날 Samsung -2.3%, SK Hynix -4.4%, Hana Micron -1.7%, Hanmi Semiconductor -4.4%가 하락했다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event return anchor

stage3_price:
N/A

Samsung_event_MAE_1D:
-2.3%

SK_Hynix_event_MAE_1D:
-4.4%

Hana_Micron_event_MAE_1D:
-1.7%

Hanmi_Semiconductor_event_MAE_1D:
-4.4%

KOSPI_same_context:
-0.7%

Samsung_China_DRAM_exposure:
> one-third

SK_Hynix_China_DRAM_NAND_exposure:
30~40%

authorization_effective_delay:
120 days

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4C 큰 하락 이전 포착 여부:
partial_success
- 정책 변경 당일 4C-watch 가능.
- hard 4C는 실제 생산/매출 차질 확인 후.
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = export_control_4C_watch
stage_failure_type = 4C_watch_not_hard_4C
```

### 교정

```text
4C-watch:
China fab exposure
equipment authorization loss
U.S.-China policy reversal

hard 4C 승격 조건:
production disruption
customer shipment delay
revenue impact
capex plan cancellation
```

---

# 5. 이번 R2 case별 요약표

| case                  | 분류                           |                                                   실제 가격검증 | alignment              |
| --------------------- | ---------------------------- | --------------------------------------------------------: | ---------------------- |
| SK하이닉스                | structural_success + 4B      | 222,000원 → 1,447,000원, +551.8%; 2025 +274%, 2026 +200% 이상 | aligned                |
| 삼성전자                  | success_candidate + 4C-watch |             OpenAI +4.7%; Q3 OP 12.2조; strike event -9.3% | watch                  |
| 한미반도체                 | success_candidate + 4B       |         Micron 미확정 보도 +22%, 139,100원; SKH contract 214.8억 | aligned_candidate + 4B |
| 가온칩스                  | success_candidate            |                      PFN AI chip design win, 가격 anchor 없음 | insufficient_evidence  |
| DB하이텍                 | event/policy watch           |           4.5조 public-private foundry, 40nm, 가격 anchor 없음 | event_premium          |
| OpenAI/Stargate       | 4B-watch                     |      SKH +12%, Samsung +4.7%, 시총 +$37B, 900k wafers/month | demand validation + 4B |
| export-control basket | 4C-watch                     |         Samsung -2.3%, SKH -4.4%, Hana -1.7%, Hanmi -4.4% | thesis_break_watch     |

---

# 6. score-price alignment 판정

```text
aligned:
- SK하이닉스

aligned_candidate:
- 한미반도체, confirmed SK Hynix order 구간

success_candidate:
- 삼성전자
- 가온칩스

event_premium / policy_watch:
- DB하이텍 public-private foundry
- OpenAI/Stargate 후발주 일부

price_moved_without_evidence:
- 한미반도체 Micron 미확정 보도 구간
- OpenAI headline으로 개별 후발주가 매출 없이 급등하는 구간

thesis_break_watch:
- export-control basket
- 삼성전자 labor/strike risk

4B-watch:
- SK하이닉스 market-cap milestone
- 한미반도체 Micron rumor +22%
- OpenAI/Stargate memory event
- Samsung $1T / AI memory crowding

4C-watch:
- 삼성전자 strike / production disruption risk
- China fab export-control shock
```

---

# 7. 점수비중 교정

## 올릴 축

```text
eps_revision +5
HBM4_first_mover +5
capacity_bottleneck +5
confirmed_customer_order +5
product_specificity +4
order_to_revenue_conversion +4
gross_margin_visibility +4
price_path_alignment +5
```

### 이유

SK하이닉스는 HBM 지배력과 EPS revision 이후 대형 MFE가 나왔다. 2024년 6월 25일 222,000원 anchor에서 2026년 5월 4일 1,447,000원까지 +551.8%가 계산된다. 한미반도체는 SK하이닉스향 HBM 장비 계약이 확인된 구간은 Stage 2~3 후보가 될 수 있다.

## 내릴 축

```text
ai_keyword_only -5
server_theme_only -4
design_win_without_revenue -4
policy_foundry_without_order -5
unconfirmed_media_report -5
OpenAI_or_Nvidia_event_without_company_revenue -4
customer_name_without_margin -3
price_rally_before_confirmation -5
labor_disruption_risk -4
China_fab_export_control_risk -4
```

### 이유

한미반도체의 Micron 보도 급등은 미확정 media report였고, DB하이텍은 정부 foundry 협의 대상일 뿐 회사 단위 매출·마진 evidence가 없다. 삼성전자는 AI memory recovery가 강하지만 strike risk와 foundry/logic division weakness가 4C-watch로 붙는다.

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
8. export-control / China fab / labor / accounting trust 통과

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
OpenAI / Stargate / Nvidia event로 지수와 함께 급등
미확정 고객 다변화 보도에 +20% 이상 급등
AI capex consensus가 한쪽으로 몰림
좋은 뉴스에도 가격이 이미 record high 부근

4B-elevated:
SK Hynix처럼 1조 달러 근접
Samsung처럼 $1T milestone + strike/labor tension 동시 발생
Hanmi처럼 미확정 고객 보도로 급등
OpenAI wafer-demand headline 후 후발주까지 동반 급등
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
labor strike / production halt
accounting or disclosure trust break
customer concentration failure
```

이번 라운드에서는 export-control과 삼성전자 strike risk를 hard 4C가 아니라 **4C-watch**로 둔다. 실제 생산 차질, shipment delay, 매출 차질이 확인되면 hard 4C로 승격한다.

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

## docs/round/round_147.md 요약

```md
# R2 Loop 9. AI Semiconductor Electronics Price Validation

이번 라운드는 R2 Loop 9 price-validation 라운드다.

핵심 결론:
- SK하이닉스는 2024-06-25 222,000원 Stage 3 anchor에서 2026-05-04 1,447,000원 record close까지 +551.8% MFE가 확인된다. 현재는 신규 Stage 3가 아니라 4B-watch다.
- 삼성전자는 OpenAI event +4.7%, Q3 OP 12.2조 원으로 Stage 2 후보지만, HBM volume/margin 확인 전 Stage 3는 보류한다. strike risk로 -9.3% 하락한 event는 4C-watch다.
- 한미반도체는 SK하이닉스향 HBM 장비 계약이 Stage 2~3 후보지만, Micron 미확정 보도 +22%는 4B-watch다.
- 가온칩스는 Preferred Networks AI chip design win으로 Stage 2 후보지만, tape-out·양산·매출 전 Green 금지다.
- DB하이텍은 4.5조 원 public-private foundry policy event로 Stage 1~2 후보지만 회사 단위 order/revenue 전 Green 금지다.
- OpenAI/Stargate event는 SK하이닉스와 삼성전자 demand validation이지만, 이미 오른 HBM winners에게는 4B-watch다.
- U.S. China fab equipment authorization revocation은 Samsung/SK/Hana/Hanmi에 4C-watch를 만든다.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 147 R2 Loop 9 AI Semiconductor Price Validation

## 반영 내용
- R2 Loop 9 price-validation 라운드를 추가했다.
- HBM4 leader, Samsung catch-up/labor risk, HBM equipment, AI design house, policy foundry, OpenAI/Stargate demand event, export-control shock을 비교했다.
- Reuters/MarketWatch/WSJ/AP/Tom’s Hardware reported anchors로 가능한 MFE/MAE와 policy/order metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- EPS revision, HBM4 first mover, confirmed customer order, capacity bottleneck, price path alignment 가중치 강화
- unconfirmed media report, policy foundry without order, design win without revenue, labor/export-control risk 감점 강화
- R2 4B-watch와 4C-watch 민감도 강화
```

## case row 초안

```jsonl
{"case_id":"r2_loop9_sk_hynix_hbm4_stage3_4b","symbol":"000660","company_name":"SK하이닉스","case_type":"structural_success","primary_archetype":"MEMORY_HBM4_FIRST_MOVER","stage2_date":"2024-06-25","stage3_date":"2024-06-25","stage4b_date":"2026-05-04","price_validation":{"price_data_source":"MarketWatch/Reuters reported anchors","stage3_price":222000,"hbm4_event_mfe_intraday_pct":7.3,"hbm4_relative_outperformance_pp":6.1,"record_close_2026_05_04":1447000,"peak_return_from_stage3_pct":551.8,"reported_return_2025_pct":274,"reported_return_2026_ytd_pct":200,"minimum_compounded_return_from_2025_start_pct":1022,"market_cap_mfe_minimum_pct":842,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"aligned","rerating_result":"true_rerating","notes":"HBM dominance, HBM4 first mover and EPS revision produced large MFE; now 4B-watch."}
{"case_id":"r2_loop9_samsung_hbm_catchup_labor_watch","symbol":"005930","company_name":"삼성전자","case_type":"success_candidate","primary_archetype":"HBM_CATCHUP_EXECUTION","stage2_date":"2025-10-02","stage4c_date":"2026-05-15","price_validation":{"price_data_source":"Reuters/AP reported anchors","stage3_price":null,"openai_event_return_pct":4.7,"q3_2025_op_krw_trn":12.2,"q3_2025_op_growth_pct":32.5,"q3_2025_revenue_krw_trn":86,"semiconductor_division_op_krw_trn":7,"ai_rally_2026_05_06_return_pct":14.4,"strike_event_mae_pct":-9.3,"jpmorgan_op_loss_estimate_krw_trn":"21-31","sales_opportunity_loss_krw_trn":4.5,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_4c_watch","rerating_result":"HBM_catchup_plus_labor_risk","notes":"HBM catch-up is Stage 2 until volume/margin confirm; strike risk is 4C-watch."}
{"case_id":"r2_loop9_hanmi_hbm_bonder_confirmed_vs_rumor","symbol":"042700","company_name":"한미반도체","case_type":"success_candidate","primary_archetype":"HBM_BONDER_EQUIPMENT_KOREA","stage2_date":"2024-03-26","stage4b_date":"2024-03-28","price_validation":{"price_data_source":"WSJ reported price and contract anchors","stage3_price":null,"confirmed_sk_hynix_contract_krw_bn":21.48,"recent_deals_total_krw_bn":200,"stage4b_peak_price":139100,"stage4b_event_mfe_pct":22,"implied_pre_4b_reference_price":114016,"kospi_same_context_pct":-0.3,"relative_outperformance_pp":22.3,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"aligned_candidate_4B_watch","rerating_result":"HBM_equipment_rerating_candidate","notes":"Confirmed SK Hynix order is Stage 2/3 candidate; unconfirmed Micron report is 4B-watch."}
{"case_id":"r2_loop9_gaonchips_pfn_design_win","symbol":"399720","company_name":"가온칩스","case_type":"success_candidate","primary_archetype":"SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER","stage2_date":"2024-07-09","price_validation":{"price_data_source":"Reuters evidence source","stage3_price":null,"order_size":"not_disclosed","technology":"Samsung 2nm GAA + advanced packaging","customer":"Preferred Networks","end_use":"generative AI / LLM HPC hardware","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"unknown_insufficient_evidence","rerating_result":"design_win_watch","notes":"Design win is Stage 2; tape-out, mass production, revenue and margin required for Stage 3."}
{"case_id":"r2_loop9_db_hitek_policy_foundry","symbol":"000990","company_name":"DB하이텍","case_type":"event_premium","primary_archetype":"POLICY_FOUNDRY_EVENT","stage1_date":"2025-12-10","price_validation":{"price_data_source":"Reuters policy evidence","stage3_price":null,"foundry_project_size_krw_trn":4.5,"foundry_project_size_usd_bn":3.06,"process_node_nm":40,"wafer_size_inch":12,"defense_semiconductor_import_dependency_pct":99,"company_status":"consultation_target_not_confirmed_order","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_policy_watch","rerating_result":"policy_foundry_watch","notes":"Government foundry consultation is Stage 1/2, not company Green."}
{"case_id":"r2_loop9_openai_stargate_memory_4b","symbol":"000660/005930","company_name":"SK하이닉스/삼성전자","case_type":"4b_watch","primary_archetype":"OPENAI_STARGATE_AI_CAPEX_EVENT","stage2_date":"2025-10-02","stage4b_date":"2025-10-02","price_validation":{"price_data_source":"Reuters/Tom's Hardware reported anchors","stage3_price":null,"sk_hynix_event_mfe_pct":12,"samsung_event_mfe_pct":4.7,"combined_market_cap_added_usd_bn":37,"kospi_event_return_pct":3,"openai_expected_dram_wafers_monthly":900000,"share_of_global_dram_output_pct":40,"implied_global_dram_output_wafers_monthly":2250000,"stargate_project_scale_usd_bn":500,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"aligned_for_sk_hynix_event_premium_for_samsung","rerating_result":"AI_memory_demand_validation_4B_watch","notes":"Demand validation for leaders, but 4B-watch after large rerating; 후발주 Green 금지."}
{"case_id":"r2_loop9_export_control_china_fab_watch","symbol":"005930/000660/067310/042700","company_name":"Samsung/SK Hynix/Hana Micron/Hanmi","case_type":"4c_watch","primary_archetype":"GEOPOLITICAL_EXPORT_CONTROL_OVERLAY","stage4c_date":"2025-09-01","price_validation":{"price_data_source":"Reuters reported event returns","stage3_price":null,"samsung_mae_1d_pct":-2.3,"sk_hynix_mae_1d_pct":-4.4,"hana_micron_mae_1d_pct":-1.7,"hanmi_mae_1d_pct":-4.4,"kospi_same_context_pct":-0.7,"samsung_china_dram_exposure":"more_than_one_third","sk_hynix_china_dram_nand_exposure_pct":"30-40","authorization_effective_delay_days":120,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"export_control_4C_watch","notes":"Export-control shock is 4C-watch; hard 4C requires production/revenue disruption."}
```

## shadow weight row 초안

```csv
archetype,eps_revision,hbm4_first_mover,capacity_bottleneck,confirmed_order,product_specificity,order_to_revenue,margin_visibility,price_path_alignment,event_penalty,labor_export_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
MEMORY_HBM4_FIRST_MOVER,+5,+5,+5,+4,+5,+4,+4,+5,-1,+3,+5,+4,SK Hynix confirms large MFE and 4B-watch after HBM4/market-cap milestone.
HBM_CATCHUP_EXECUTION,+4,+3,+4,+3,+4,+3,+4,+3,-2,+5,+4,+4,Samsung is Stage 2 until volume HBM sales/margins; labor risk creates 4C-watch.
HBM_BONDER_EQUIPMENT_KOREA,+3,+0,+5,+5,+5,+4,+4,+4,-3,+2,+5,+3,Hanmi confirmed order is good; unconfirmed customer rumor is 4B/event risk.
SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER,+2,+0,+2,+2,+4,+3,+3,+2,-4,+1,+3,+3,Gaonchips design win needs tape-out/mass production/revenue.
POLICY_FOUNDRY_EVENT,+1,+0,+2,+1,+2,+1,+2,+1,-5,+2,+4,+3,DB HiTek policy foundry consultation is not Green.
OPENAI_STARGATE_AI_CAPEX_EVENT,+3,+2,+5,+3,+3,+2,+2,+4,-4,+2,+5,+3,OpenAI demand validates leaders but causes 4B/event premium for 후발주.
GEOPOLITICAL_EXPORT_CONTROL_OVERLAY,+0,+0,+0,+0,+0,+0,+0,+2,0,+5,+3,+5,China fab authorization loss is 4C-watch until production/revenue disruption confirmed.
```

---

# 이번 R2 Loop 9 결론

R2는 Stage 3가 실제로 대형 수익률을 만들 수 있는 섹터지만, 동시에 **가장 빨리 4B가 붙는 섹터**다.

```text
1. SK하이닉스는 R2 Stage 3 성공 benchmark다.
   222,000원 anchor에서 1,447,000원까지 +551.8% MFE가 계산된다.
   하지만 현재는 신규 Stage 3가 아니라 4B-watch다.

2. 삼성전자는 AI memory 회복과 OpenAI demand validation이 있지만,
   HBM catch-up의 volume/margin 확인 전 Stage 3는 보류해야 한다.
   strike risk는 4C-watch다.

3. 한미반도체는 confirmed SK Hynix order가 있는 구간은 좋지만,
   Micron 미확정 보도 +22%는 4B-watch다.

4. 가온칩스는 design win만으로 Green 금지다.
   tape-out, 양산, 매출, margin이 필요하다.

5. DB하이텍은 정책 foundry event일 뿐이다.
   회사 단위 order / utilization / EPS 전 Green 금지다.

6. OpenAI/Stargate는 수요 검증이지만,
   이미 오른 HBM winner에게는 동시에 4B-watch다.

7. export-control과 삼성전자 노동 리스크는 hard 4C는 아니지만,
   생산·매출 차질로 이어질 수 있는 4C-watch다.
```

한 문장으로 압축하면:

> **R2에서 진짜 Stage 3는 “AI 반도체 수혜”가 아니라, HBM·장비·디자인·메모리 가격이 고객 주문·CAPA 병목·마진·EPS revision으로 내려오고 가격경로가 뒤따르는 순간이다.**
> **그리고 R2는 AI 수요가 진짜여도 가격이 더 빨리 달리기 때문에, winner에는 4B-watch를 아주 빨리 붙여야 한다.**

[1]: https://www.marketwatch.com/story/sk-hynix-s-hbm-dominance-higher-chip-prices-could-lift-earnings-market-talk-6508cbf8?utm_source=chatgpt.com "SK Hynix's HBM Dominance, Higher Chip Prices Could Lift Earnings -- Market Talk"
[2]: https://www.reuters.com/world/asia-pacific/ai-boom-puts-sk-hynix-cusp-1-trillion-market-value-2026-05-14/?utm_source=chatgpt.com "AI boom puts SK Hynix on cusp of $1 trillion market value"
[3]: https://www.reuters.com/world/asia-pacific/samsung-sk-hynix-shares-rally-openai-partnerships-2025-10-02/?utm_source=chatgpt.com "Samsung, SK Hynix shares leap after OpenAI chip deal"
[4]: https://www.wsj.com/articles/hanmi-semiconductor-climbs-after-media-reports-of-possible-deal-with-micron-e85398fb?utm_source=chatgpt.com "Hanmi Semiconductor Climbs After Media Reports of Possible Deal With Micron"
[5]: https://www.reuters.com/technology/artificial-intelligence/samsung-electronics-wins-cutting-edge-ai-chip-order-japans-preferred-networks-2024-07-09/?utm_source=chatgpt.com "Samsung Electronics wins cutting-edge AI chip order from Japan's Preferred Networks"
[6]: https://www.reuters.com/world/asia-pacific/south-korea-consider-setting-up-31-bln-foundry-grow-local-chip-sector-2025-12-10/?utm_source=chatgpt.com "South Korea to consider setting up $3.1 bln foundry to grow local chip sector"
[7]: https://www.reuters.com/world/china/shares-samsung-sk-hynix-drop-after-us-makes-it-harder-make-chips-china-2025-09-01/?utm_source=chatgpt.com "Shares in Samsung, SK Hynix drop after US makes it harder to make chips in China"
