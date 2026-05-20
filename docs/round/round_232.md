순서상 이번은 **R2 Loop 10 — AI·반도체·전자부품 가격경로 검증 라운드**다.

이번 라운드는 HBM 대장만 반복하지 않고, **HBM leader, 삼성전자 catch-up/foundry, HBM 장비, 시스템반도체 디자인하우스, 정책 foundry, AI chip infra event, export-control shock, 반도체 장비 spin-off**를 같이 봤다.

```text
round = R2 Loop 10
round_id = round_160
large_sector = AI_SEMICONDUCTOR_ELECTRONICS
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
```

이번 환경에서는 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉 OHLC를 안정적으로 직접 확보하지 못했다. 대신 Reuters / WSJ / MarketWatch가 제공한 **가격 anchor, 이벤트 수익률, 계약금액, 시총, 정책·공장·CAPEX 지표**로 계산 가능한 값만 계산했다. 원시 OHLC가 없는 구간은 `price_data_unavailable_after_deep_search`로 표시했다.

---

# 1. 이번 라운드 대섹터

```text
R2 = AI·반도체·전자부품
```

R2의 핵심은 “AI 반도체 수혜”가 아니라, **고객 주문·CAPA 병목·HBM 세대 전환·마진·EPS revision·가격경로가 같이 맞는가**다. R2는 Stage 3가 대형 MFE를 만들 수 있지만, 동시에 4B가 가장 빨리 붙는 섹터다.

---

# 2. 대상 canonical archetype

```text
MEMORY_HBM_CAPACITY
MEMORY_HBM4_FIRST_MOVER
HBM_CAPEX_CAPACITY_BUILDOUT
HBM_EUV_AND_ADVANCED_PACKAGING_CAPEX
HBM_CATCHUP_EXECUTION
FOUNDRY_TURNAROUND_CONTRACT
HBM_BONDER_EQUIPMENT_KOREA
SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER
POLICY_FOUNDRY_EVENT
AI_CHIP_INFRASTRUCTURE_EVENT
GEOPOLITICAL_EXPORT_CONTROL_OVERLAY
SEMICONDUCTOR_IP_LEAK_REDTEAM
CORPORATE_ACTION_SPINOFF_EVENT
PRICE_ONLY_RALLY
```

---

# 3. deep sub-archetype

```text
HBM leader:
- SK Hynix
- HBM4 internal certification
- Nvidia customer visibility
- EUV order / advanced packaging plant
- AI capex demand
- market-cap milestone
- 4B crowding

Samsung catch-up:
- Samsung Electronics
- HBM3E / HBM4 catch-up
- Nvidia / AMD / OpenAI demand validation
- Tesla / foundry contract
- Texas fab / yield / foundry loss
- labor strike risk

HBM equipment:
- Hanmi Semiconductor
- TSV-TC bonder
- confirmed SK Hynix order
- unconfirmed Micron media report
- customer diversification rumor vs confirmed contract

System semiconductor:
- Gaonchips
- Preferred Networks AI chip design
- Samsung 2nm GAA foundry
- design win vs mass production / revenue

Policy foundry:
- DB HiTek / Samsung / SK ecosystem
- 4.5T won public-private 40nm foundry
- defense semiconductor import dependence
- policy support vs company revenue

AI infrastructure event:
- Nvidia Blackwell Korea supply
- OpenAI Stargate memory demand
- Samsung / SK / Naver / Kakao AI infrastructure
- event premium vs revenue bridge

RedTeam:
- U.S. China equipment authorization revocation
- China-fab exposure
- Samsung strike / labor disruption
- chip technology leak to CXMT
- IP loss / China competitive catch-up
```

---

# 4. 국장 신규 후보 case

## Case A — SK하이닉스 `structural_success + 4B-watch`

```text
symbol = 000660
case_type = structural_success + 4B-watch
archetype = MEMORY_HBM_CAPACITY / MEMORY_HBM4_FIRST_MOVER / HBM_CAPEX_CAPACITY_BUILDOUT
```

### stage date

```text
Stage 1:
2024년 상반기
- AI server / HBM demand
- old commodity memory frame break

Stage 2:
2024-06-25
- HBM dominance + DRAM price upcycle + EPS revision
- stage3 candidate anchor = 222,000원

Stage 3:
2024-06-25 후보
- HBM 지배력
- 메모리 가격 상승
- EPS revision
- AI server capacity bottleneck

추가 Stage 3 validation:
2025-09-12
- HBM4 internal certification 완료
- production system established for customers
- shares +7.3%, KOSPI +1.2%

추가 Stage 3 validation:
2026-03-24
- ASML EUV tools 11.95T won / $7.97B purchase
- by 2027-12-31
- shares +5.7%

추가 Stage 2/3 capacity validation:
2026-04-22
- 19T won / $12.85B advanced packaging plant
- construction starts April 2026
- HBM / advanced DRAM capacity support

Stage 4B:
2026-05-14
- 2025년 +274%
- 2026년 +200% 이상
- market cap 약 $942B
- 1조 달러 근접
```

SK하이닉스는 R2에서 여전히 가장 깨끗한 structural_success benchmark다. 2025년 9월 HBM4 내부 인증과 고객용 생산체계 구축을 발표했을 때 주가는 장중 7.3% 올랐고, KOSPI 1.2%를 크게 웃돌았다. 2026년에는 ASML EUV 장비 11.95조 원, 약 79.7억 달러 구매를 공시했고, 주가는 5.7% 상승했다. 또 2026년 4월에는 19조 원 규모 advanced packaging 공장 투자를 발표했다. 다만 2026년 5월 기준 시총이 약 9,420억 달러에 도달했고, 2025년 +274%, 2026년 +200% 이상 상승했으므로 지금은 신규 Stage 3가 아니라 4B-watch다. ([Reuters][1])

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch / Reuters reported price and return anchors

entry_date:
2024-06-25

stage3_price:
222,000원

HBM4_event_return:
+7.3%

HBM4_event_KOSPI:
+1.2%

HBM4_relative_outperformance:
7.3 - 1.2
= +6.1pp

ASML_EUV_order:
11.95T won / $7.97B

ASML_EUV_event_return:
+5.7%

estimated_EUV_tools:
about 30 machines

advanced_packaging_plant_investment:
19T won / $12.85B

reported_2025_return:
+274%

reported_2026_return_to_2026-05-14:
> +200%

minimum_compounded_return_from_start_2025_to_2026-05-14:
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
price_data_unavailable_after_deep_search beyond reported anchors

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

---

## Case B — 삼성전자 `success_candidate + labor/export-control 4C-watch`

```text
symbol = 005930
case_type = success_candidate + 4C-watch
archetype = HBM_CATCHUP_EXECUTION / FOUNDRY_TURNAROUND_CONTRACT / LABOR_SUPPLY_CHAIN_4C_WATCH
```

### stage date

```text
Stage 1:
2025년
- Samsung HBM catch-up
- foundry turnaround
- AI memory / AI chip supply-chain recovery 기대

Stage 2:
2025-07-28
- $16.5B foundry contract
- client later reported by sources as Tesla
- shares +3.5%
- contract through end-2033

Stage 2 추가:
2025-10-31
- Nvidia HBM3E / HBM4 supply collaboration
- Samsung says close discussion to supply HBM4 to Nvidia
- shares +4.32%

Stage 2 추가:
2026-03-18
- AMD MoU on AI memory and possible foundry partnership
- Samsung HBM4 for future AMD Instinct MI455X discussed

Stage 3:
보류
- HBM4 volume shipment
- Nvidia/AMD/Tesla revenue recognition
- foundry margin / yield / EPS revision 확인 전 Green 금지

Stage 4B:
AI/foundry/HBM catch-up narrative로 valuation이 먼저 확장되면 후보

Stage 4C-watch:
2025-09-01
- U.S. revokes China chip-equipment authorization
- Samsung -2.3%

Stage 4C-watch:
2026-05-15~18
- Samsung union strike risk
- 45,000~50,000+ workers
- 18-day strike threat
- May 15 shares -9.3%
- May 18 court-ruling relief shares +3.88%, but strike risk remains
```

삼성전자는 R2에서 가장 애매한 success_candidate다. 2025년 7월 165억 달러 foundry 계약으로 주가가 3.5% 올랐고, Reuters는 이 계약의 고객이 Tesla라고 보도했다. 2025년 10월에는 Nvidia와 HBM3E/HBM4 supply collaboration을 발표했고 주가는 4.32% 상승했다. 2026년 3월에는 AMD와 AI memory 및 foundry 협력을 논의하는 MoU도 나왔다. 하지만 HBM4 volume shipment, foundry yield, margin, EPS revision이 확인되기 전에는 Green이 아니다. 동시에 중국 fab 장비허가 취소와 2026년 5월 대규모 파업 리스크가 4C-watch다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported contract / event-return / strike-risk anchors

stage3_price:
N/A

foundry_contract_value:
$16.5B

foundry_contract_duration:
through end-2033

foundry_contract_event_return:
+3.5%

Tesla_client_report:
sources said client is Tesla

foundry_loss_context:
estimated >5T won loss in H1, according to Kiwoom analyst cited by Reuters

Nvidia_HBM4_event_return:
+4.32%

Samsung_China_DRAM_exposure:
> one-third

export_control_event_MAE:
-2.3%

Samsung_strike_event_MAE:
-9.3% on May 15, 2026

court_ruling_relief_event_return:
+3.88% on May 18, 2026

KOSPI_same_context_May_18:
+0.31%

relative_outperformance_May_18:
3.88 - 0.31
= +3.57pp

workers_in_possible_strike:
45,000~50,000+

possible_direct_loss_per_day:
up to 1T won, according to PM warning

prolonged_disruption_damage:
up to 100T won, according to PM warning

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = success_candidate + 4C_watch
rerating_result = HBM_catchup_foundry_turnaround_watch
stage_failure_type = stage2_watch_until_volume_margin_confirm
```

---

## Case C — 한미반도체 `success_candidate + unconfirmed-customer 4B-watch`

```text
symbol = 042700
case_type = success_candidate + 4B-watch
archetype = HBM_BONDER_EQUIPMENT_KOREA
```

### stage date

```text
Stage 1:
2023~2024
- HBM packaging equipment
- TSV-TC bonder
- SK Hynix supply-chain exposure

Stage 2:
2024-03
- SK Hynix contract 214.8억 원
- recent deals total around 2,000억 원
- confirmed customer order

Stage 3:
조건부 후보
- confirmed customer order
- product-specific HBM equipment exposure
- order-to-revenue, margin, EPS 확인 필요

Stage 4B:
2024-03-28
- Micron 미확정 보도만으로 장중 +22%
- 139,100원
- KOSPI -0.3%

Stage 4C:
Micron deal not confirmed, customer concentration, HBM capex pause, equipment order delay 시 후보
```

한미반도체는 HBM 장비주 중 Stage 2~3 후보가 될 수 있다. SK하이닉스향 214.8억 원 계약과 최근 약 2,000억 원 규모의 deal들이 확인됐기 때문이다. 하지만 2024년 3월 Micron 공급 가능성 보도만으로 장중 22% 급등해 139,100원을 기록했고, 당시 Micron과 한미반도체 모두 보도를 확인하지 않았다. 이건 R2에서 **confirmed order와 unconfirmed customer-rumor를 분리해야 하는 대표 case**다. ([월스트리트저널][3])

### 실제 가격경로 검증

```text
price_data_source:
WSJ reported price and contract anchors

stage3_price:
price_data_unavailable_after_deep_search

reason:
- WSJ는 confirmed SK Hynix order와 Micron-rumor event는 제공하지만,
  confirmed-order date의 종가 OHLC는 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉 OHLC 직접 확보 실패.

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

Micron_deal_status:
unconfirmed media report

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
- system semiconductor catch-up narrative

Stage 2:
2024-07-09
- Preferred Networks AI chip order
- Samsung 2nm GAA + advanced packaging
- Gaonchips designed the chips
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

삼성전자는 일본 Preferred Networks의 AI chip을 2nm GAA 공정과 advanced packaging으로 생산하는 첫 공개 수주를 확보했고, 이 칩 설계는 한국의 가온칩스가 맡았다. 이 칩은 생성AI와 대형언어모델용 high-performance computing hardware에 쓰일 예정이다. 하지만 주문 규모는 공개되지 않았고, 가온칩스의 매출 인식과 gross margin은 아직 확인되지 않았다. 따라서 Stage 2 design win이지 Stage 3가 아니다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters evidence source

stage3_price:
N/A

stage2_price:
price_data_unavailable_after_deep_search

reason:
- Reuters는 가온칩스 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉 OHLC 직접 확보 실패.

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

---

## Case E — DB하이텍 / 공공-민간 foundry 정책 `event_premium / policy Stage 1~2`

```text
symbol = 000990
case_type = event_premium / policy_watch
archetype = POLICY_FOUNDRY_EVENT
```

### stage date

```text
Stage 1:
2025-12-10
- 4.5조 원 public-private foundry 검토
- 12-inch / 40nm facility
- automotive / data-center legacy chip
- defense semiconductor localization

Stage 2:
약한 Stage 2
- Samsung / SK Hynix / industry consultation
- DB HiTek 같은 legacy foundry candidate 가능

Stage 3:
없음
- government consultation만으로 Green 금지
- funded capex, company-level order, utilization, customer commitment, margin 확인 필요

Stage 4B:
정책 foundry 테마로 주가가 먼저 급등하면 후보

Stage 4C:
예산 미반영, 민간 부담 과다, 고객 부재, utilization failure 시 후보
```

한국 정부는 AI 시대 반도체 경쟁력 강화를 위해 4.5조 원 규모의 12인치 40nm 공공-민간 foundry 설립을 검토하고 있다. 이 facility는 자동차·데이터센터용 legacy chip 개발과 defense semiconductor localization을 지원하는 구조이며, defense semiconductor import dependence는 99%로 언급됐다. 하지만 DB하이텍 회사 단위 수주나 매출이 아니라 정책·협의 단계다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters policy evidence source

stage3_price:
N/A

stage1_price:
price_data_unavailable_after_deep_search

reason:
- Reuters는 DB하이텍 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉 OHLC 직접 확보 실패.

foundry_project_size:
4.5T won / $3.06B

process_node:
40nm

wafer_size:
12-inch

defense_semiconductor_import_dependency:
99%

company_status:
consultation target / policy beneficiary candidate, not confirmed order

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

---

## Case F — Nvidia Blackwell / OpenAI Stargate Korea event `4B-watch / demand validation`

```text
symbols = 000660 / 005930 / 035420 / 035720 / Samsung SDS / related AI infra basket
case_type = 4B-watch
archetype = AI_CHIP_INFRASTRUCTURE_EVENT
```

### stage date

```text
Stage 1:
2025-10-02
- OpenAI Stargate partnership
- Samsung / SK Hynix semiconductor procurement
- two Korea data centers, 20MW initial capacity

Stage 2:
2025-10-31
- Nvidia to supply >260,000 Blackwell AI chips to Korea
- government 50,000
- Samsung / SK / Hyundai up to 50,000 each
- Naver 60,000

Stage 3:
SK Hynix에는 existing Stage 3 demand validation
Samsung에는 Stage 2 catch-up validation
Naver/Kakao/SDS 등 후발주에는 revenue bridge 전 Green 금지

Stage 4B:
OpenAI event:
- SK Hynix +12%
- Samsung +4.7%
- combined market cap +$37B
- KOSPI >3%

Nvidia Korea event:
- chip allocation headline can create AI infra basket premium
```

OpenAI Stargate 협력은 SK하이닉스와 삼성전자에 강한 demand validation이 됐다. 발표 후 SK하이닉스는 12%, 삼성전자는 4.7% 상승했고, 두 회사 시총은 합산 370억 달러 증가했다. 뒤이어 Nvidia는 한국 정부와 대기업에 Blackwell AI chip 26만 개 이상을 공급한다고 발표했다. 정부는 5만 개, Samsung/SK/Hyundai는 각각 최대 5만 개, Naver는 6만 개를 배정받는 구조다. 이 이벤트는 leader에는 수요검증, 후발 AI infra basket에는 event premium이다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event return and AI-chip allocation anchors

stage3_price:
N/A for event row

OpenAI_event:
SK_Hynix_event_MFE_1D = +12%
Samsung_event_MFE_1D = +4.7%
combined_market_cap_added = $37B
KOSPI_event_return = > +3%

OpenAI_Korea_data_center_initial_capacity:
20MW

Nvidia_Blackwell_Korea_total:
>260,000 chips

government_allocation:
50,000 chips

Samsung_allocation:
up to 50,000 chips

SK_Group_allocation:
up to 50,000 chips

Hyundai_allocation:
up to 50,000 chips

Naver_allocation:
60,000 chips

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
success
- demand validation이지만, 후발주 Green은 금지.
```

### alignment

```text
score_price_alignment = aligned_for_SK_Hynix / event_premium_for_followers
rerating_result = AI_memory_and_AI_infra_demand_validation_4B_watch
stage_failure_type = 4B_watch
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
- KOSPI -0.7%
```

미국은 Samsung과 SK Hynix의 중국 공장에 미국산 반도체 제조장비를 들여올 수 있게 했던 authorization을 취소했다. Samsung DRAM 생산의 3분의 1 이상, SK Hynix DRAM/NAND의 30~40%가 중국에 기반한다는 분석이 보도됐고, 같은 날 Samsung -2.3%, SK Hynix -4.4%, Hana Micron -1.7%, Hanmi Semiconductor -4.4%가 하락했다. 이건 hard 4C는 아니지만, R2에서 반드시 붙여야 하는 4C-watch다. ([Reuters][7])

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

Samsung_relative_underperformance:
-2.3 - (-0.7)
= -1.6pp

SK_Hynix_relative_underperformance:
-4.4 - (-0.7)
= -3.7pp

Hanmi_relative_underperformance:
-4.4 - (-0.7)
= -3.7pp

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

---

## Case H — Hanwha Precision Machinery / 반도체 장비 spin-off `event_premium / corporate-action watch`

```text
parent_symbol = 012450
case_type = event_premium / corporate_action_watch
archetype = CORPORATE_ACTION_SPINOFF_EVENT / HBM_EQUIPMENT_OPTIONALITY
```

### stage date

```text
Stage 1:
2024-04-02~05
- Hanwha Aerospace semiconductor-equipment spin-off media report
- HBM equipment optionality
- industrial-solutions carve-out

Stage 2:
2024-04-05
- Hanwha Aerospace announces spin-off of Hanwha Precision Machinery and Hanwha Vision
- chip-equipment unit includes HBM equipment development angle
- industrial solutions entity estimated 2T won
- defense business estimated 10T won

Stage 3:
없음
- spin-off / valuation-unlock만으로 Green 금지
- listed vehicle, order book, HBM equipment revenue, margin, cashflow 확인 필요

Stage 4B:
2024-04-02
- media report 후 parent stock +15% 이상
- formal announcement 후 profit-taking -8%

Stage 4C:
spin-off delay, governance discount, HBM equipment order failure, listing/valuation disappointment 시 후보
```

Hanwha Aerospace는 chip equipment maker Hanwha Precision Machinery와 surveillance camera maker Hanwha Vision을 분리해 industrial-solutions company로 묶기로 했다. 회사는 Hanwha Precision의 chip-equipment business가 HBM equipment 개발을 포함해 성장할 수 있다고 설명했다. 그러나 모회사 주가는 media report 후 15% 이상 올랐다가 공식 발표 후 오전장 8% 하락했다. 이는 R2에서 **HBM equipment optionality가 있어도 corporate action만으로 Green을 주면 안 되는 케이스**다. ([Reuters][8])

### 실제 가격경로 검증

```text
price_data_source:
Reuters corporate-action / event-return anchor

stage3_price:
N/A

media_report_event_MFE:
> +15%

formal_announcement_event_MAE:
-8%

industrial_solutions_estimated_value:
2T won / $1.48B

defense_business_estimated_value:
10T won

revenue_contribution_from_spun_units:
about 16%

parent_market_cap_context:
about 11T won

industrial_plus_defense_estimate:
12T won

estimated_sum_vs_parent_market_cap:
12T / 11T - 1
= +9.1%

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium
rerating_result = HBM_equipment_corporate_action_watch
stage_failure_type = stage2_evidence_not_green
```

---

# 5. 이번 R2 case별 요약표

| case                      | 분류                           |                                                             실제 가격검증 | alignment                 |
| ------------------------- | ---------------------------- | ------------------------------------------------------------------: | ------------------------- |
| SK하이닉스                    | structural_success + 4B      |              HBM4 +7.3%, EUV order +5.7%, 2025 +274%, 2026 +200% 이상 | aligned                   |
| 삼성전자                      | success_candidate + 4C-watch |     foundry deal +3.5%, Nvidia HBM event +4.32%, strike event -9.3% | watch                     |
| 한미반도체                     | success_candidate + 4B       |                   SKH contract 214.8억, Micron 미확정 보도 +22%, 139,100원 | aligned_candidate + 4B    |
| 가온칩스                      | success_candidate            |    PFN AI chip design win, order size undisclosed, OHLC unavailable | Stage 2                   |
| DB하이텍 / policy foundry    | event/policy watch           | 4.5T won 40nm public-private foundry, defense import dependence 99% | policy Stage 1~2          |
| OpenAI/Nvidia Korea event | 4B-watch                     |                         SKH +12%, Samsung +4.7%, Nvidia chips >260k | demand validation + event |
| export-control basket     | 4C-watch                     |            Samsung -2.3%, SKH -4.4%, Hanmi -4.4%, Hana Micron -1.7% | thesis_break_watch        |
| Hanwha Precision spin-off | event premium                |              media +15%, announcement -8%, industrial entity 2T won | corporate-action watch    |

---

# 6. score-price alignment 판정

```text
aligned:
- SK하이닉스

aligned_candidate:
- 한미반도체 confirmed SK Hynix order 구간

success_candidate:
- 삼성전자
- 가온칩스

event_premium / policy_watch:
- DB하이텍 public-private foundry
- OpenAI/Nvidia Korea AI-infra event 후발 basket
- Hanwha Precision spin-off

price_moved_without_evidence:
- 한미반도체 Micron 미확정 보도 구간
- AI chip infra headline으로 후발주가 매출 없이 급등하는 구간
- corporate-action valuation unlock만으로 급등하는 구간

thesis_break_watch:
- export-control basket
- 삼성전자 labor/strike risk
- semiconductor IP leak / China HBM catch-up risk

4B-watch:
- SK하이닉스 market-cap milestone
- 한미반도체 Micron rumor +22%
- OpenAI/Nvidia memory/infra event
- Hanwha Precision spin-off media-rally
- Samsung catch-up narrative가 volume shipment보다 먼저 가격에 반영되는 구간

4C-watch:
- 삼성전자 strike / production disruption risk
- China fab export-control shock
- chip technology leak to CXMT / China competitive catch-up
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
advanced_packaging_capacity +4
price_path_alignment +5
```

### 이유

SK하이닉스는 HBM4, EUV, advanced packaging, AI demand가 한 줄로 연결되며 구조적 Stage 3가 실제 가격경로로 이어진다. 한미반도체도 confirmed SK Hynix order가 있는 구간은 Stage 2~3 후보가 될 수 있다. 다만 confirmed order와 rumor를 분리해야 한다.

## 내릴 축

```text
ai_keyword_only -5
server_theme_only -4
design_win_without_revenue -4
policy_foundry_without_order -5
unconfirmed_media_report -5
OpenAI_or_Nvidia_event_without_company_revenue -4
customer_name_without_margin -3
corporate_action_without_order -4
price_rally_before_confirmation -5
labor_disruption_risk -4
China_fab_export_control_risk -4
IP_leak_to_China_risk -4
```

### 이유

한미반도체의 Micron 보도 급등은 미확정 media report였고, DB하이텍/policy foundry는 회사 단위 order가 아니다. 삼성전자는 AI/foundry catch-up story가 있지만, labor strike와 China-fab export-control이 4C-watch로 붙는다. Hanwha Precision spin-off는 HBM 장비 optionality가 있지만, corporate action만으로 Green이 아니다.

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
8. export-control / China fab / labor / IP leakage / accounting trust 통과

금지:
AI 이름만 있음
서버 테마만 있음
미확정 고객 보도
design win만 있음
정책 foundry만 있음
OpenAI/Nvidia partnership headline만 있음
spin-off / corporate action만 있음
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
spin-off / corporate-action event가 실적보다 먼저 가격에 반영

4B-elevated:
SK Hynix처럼 1조 달러 근접
Samsung처럼 foundry/HBM catch-up 전에 labor risk 동시 발생
Hanmi처럼 미확정 고객 보도로 급등
OpenAI/Nvidia chip allocation 후 후발 AI infra basket 급등
corporate-action valuation unlock이 order/revenue보다 먼저 가격화
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
IP leakage / China competitive catch-up
accounting or disclosure trust break
customer concentration failure
```

이번 R2 Loop 10에서는 export-control, Samsung strike risk, IP leak risk를 hard 4C가 아니라 **4C-watch**로 둔다. 실제 생산 차질, shipment delay, 매출 차질, 기술경쟁력 훼손이 확인되면 hard 4C로 승격한다.

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

## docs/round/round_160.md 요약

```md
# R2 Loop 10. AI Semiconductor Electronics Price Validation

이번 라운드는 R2 Loop 10 price-validation 라운드다.

핵심 결론:
- SK Hynix remains the R2 structural success benchmark. HBM4 certification drove +7.3%, ASML EUV order drove +5.7%, and the stock is near a $1T market cap after +274% in 2025 and >+200% in 2026. Current state is 4B-watch, not fresh Stage 3.
- Samsung Electronics is a success_candidate but not Green. $16.5B foundry deal, Nvidia HBM3E/HBM4 collaboration, AMD MoU are Stage 2; HBM/foundry volume, margin, EPS and labor risk must clear first. Strike risk and China-fab export-control are 4C-watch.
- Hanmi Semiconductor is a HBM bonder candidate. Confirmed SK Hynix order and KRW200B recent deals support Stage 2, but unconfirmed Micron reports drove +22% to 139,100 won, making it 4B-watch.
- Gaonchips is Stage 2 design-win watch. Preferred Networks AI chip design with Samsung 2nm GAA is meaningful, but tape-out, mass production, revenue and margin are required before Green.
- DB HiTek/public-private foundry is policy Stage 1~2. A 4.5T won 40nm foundry and 99% defense semiconductor import dependence are policy evidence, not company Green.
- OpenAI/Nvidia Korea AI-chip event validates memory demand for leaders but creates 4B/event premium for followers. SK Hynix +12%, Samsung +4.7%, Nvidia Blackwell allocation >260k chips.
- U.S. export-control shock is R2 4C-watch. Samsung -2.3%, SK Hynix -4.4%, Hana Micron -1.7%, Hanmi -4.4%.
- Hanwha Precision Machinery spin-off is HBM-equipment optionality but not Green. Parent rose >15% on media report and fell -8% on formal announcement; corporate action needs order/revenue conversion.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 160 R2 Loop 10 AI Semiconductor Price Validation

## 반영 내용
- R2 Loop 10 price-validation 라운드를 추가했다.
- HBM leader, Samsung HBM/foundry catch-up, HBM bonder equipment, system-semi design house, policy foundry, AI infrastructure event, export-control shock, chip-equipment spin-off를 비교했다.
- Reuters/WSJ/MarketWatch reported anchors로 가능한 MFE/MAE 및 contract/capex/policy metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- EPS revision, HBM4 first mover, confirmed customer order, capacity bottleneck, advanced packaging capacity, price path alignment 가중치 강화
- unconfirmed media report, policy foundry without order, design win without revenue, AI infra event without revenue, labor/export-control/IP leak risk 감점 강화
- R2 4B-watch와 4C-watch 민감도 강화
```

## case row 초안

```jsonl
{"case_id":"r2_loop10_sk_hynix_hbm4_euv_packaging_4b","symbol":"000660","company_name":"SK하이닉스","case_type":"structural_success","primary_archetype":"MEMORY_HBM4_FIRST_MOVER","stage3_date":"2024-06-25","stage4b_date":"2026-05-14","price_validation":{"price_data_source":"Reuters/MarketWatch reported anchors","stage3_price":222000,"hbm4_event_mfe_pct":7.3,"hbm4_kospi_pct":1.2,"hbm4_relative_outperformance_pp":6.1,"asml_euv_order_krw_trn":11.95,"asml_euv_order_usd_bn":7.97,"asml_euv_event_return_pct":5.7,"estimated_euv_tools":30,"advanced_packaging_investment_krw_trn":19,"advanced_packaging_investment_usd_bn":12.85,"reported_return_2025_pct":274,"reported_return_2026_ytd_pct":200,"minimum_compounded_return_from_2025_start_pct":1022,"market_cap_mfe_minimum_pct":842,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"aligned","rerating_result":"true_rerating","notes":"HBM4, EUV and advanced packaging capacity confirm structural success; current state is 4B-watch after massive MFE."}
{"case_id":"r2_loop10_samsung_hbm_foundry_labor_export_watch","symbol":"005930","company_name":"삼성전자","case_type":"success_candidate","primary_archetype":"HBM_CATCHUP_EXECUTION","stage2_date":"2025-07-28/2025-10-31/2026-03-18","stage4c_date":"2025-09-01/2026-05","price_validation":{"price_data_source":"Reuters contract/event/strike anchors","stage3_price":null,"foundry_contract_usd_bn":16.5,"foundry_contract_event_return_pct":3.5,"foundry_contract_duration":"through_end_2033","tesla_client_reported":true,"estimated_foundry_loss_h1_krw_trn":5.0,"nvidia_hbm_event_return_pct":4.32,"export_control_event_mae_pct":-2.3,"china_dram_exposure":"more_than_one_third","strike_event_mae_pct":-9.3,"court_ruling_relief_return_pct":3.88,"kospi_same_context_pct":0.31,"relative_outperformance_may18_pp":3.57,"possible_strike_workers":"45000-50000+","possible_direct_loss_per_day_krw_trn":1,"prolonged_disruption_damage_krw_trn":100,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_4c_watch","rerating_result":"HBM_catchup_foundry_turnaround_watch","notes":"Samsung has Stage 2 HBM/foundry evidence, but volume/margin/EPS and labor/export-control risks must clear before Green."}
{"case_id":"r2_loop10_hanmi_hbm_bonder_confirmed_vs_rumor","symbol":"042700","company_name":"한미반도체","case_type":"success_candidate","primary_archetype":"HBM_BONDER_EQUIPMENT_KOREA","stage2_date":"2024-03","stage4b_date":"2024-03-28","price_validation":{"price_data_source":"WSJ reported price and contract anchors","stage3_price":null,"confirmed_sk_hynix_contract_krw_bn":21.48,"recent_deals_total_krw_bn":200,"stage4b_peak_price":139100,"stage4b_event_mfe_pct":22,"implied_pre_4b_reference_price":114016,"kospi_same_context_pct":-0.3,"relative_outperformance_pp":22.3,"micron_deal_status":"unconfirmed_media_report","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"aligned_candidate_4B_watch","rerating_result":"HBM_equipment_rerating_candidate","notes":"Confirmed SK Hynix order is Stage 2/3 candidate; unconfirmed Micron report is 4B-watch."}
{"case_id":"r2_loop10_gaonchips_pfn_design_win","symbol":"399720","company_name":"가온칩스","case_type":"success_candidate","primary_archetype":"SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER","stage2_date":"2024-07-09","price_validation":{"price_data_source":"Reuters evidence source","stage3_price":null,"order_size":"not_disclosed","technology":"Samsung 2nm GAA + advanced packaging","customer":"Preferred Networks","end_use":"generative AI / LLM HPC hardware","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"unknown_insufficient_evidence","rerating_result":"design_win_watch","notes":"Design win is Stage 2; tape-out, mass production, revenue and margin required for Stage 3."}
{"case_id":"r2_loop10_db_hitek_policy_foundry","symbol":"000990","company_name":"DB하이텍 / policy foundry exposure","case_type":"event_premium","primary_archetype":"POLICY_FOUNDRY_EVENT","stage1_date":"2025-12-10","price_validation":{"price_data_source":"Reuters policy evidence","stage3_price":null,"foundry_project_size_krw_trn":4.5,"foundry_project_size_usd_bn":3.06,"process_node_nm":40,"wafer_size_inch":12,"defense_semiconductor_import_dependency_pct":99,"company_status":"policy_beneficiary_candidate_not_confirmed_order","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_policy_watch","rerating_result":"policy_foundry_watch","notes":"Government foundry consultation is Stage 1/2, not company Green."}
{"case_id":"r2_loop10_openai_nvidia_korea_ai_infra_event","symbol":"000660/005930/035420/035720/AI_infra_basket","company_name":"OpenAI/Nvidia Korea AI infrastructure event","case_type":"4b_watch","primary_archetype":"AI_CHIP_INFRASTRUCTURE_EVENT","stage2_date":"2025-10-02/2025-10-31","stage4b_date":"2025-10-02","price_validation":{"price_data_source":"Reuters reported event return and allocation anchors","stage3_price":null,"sk_hynix_openai_event_mfe_pct":12,"samsung_openai_event_mfe_pct":4.7,"combined_market_cap_added_usd_bn":37,"kospi_event_return_pct":3,"openai_korea_data_center_initial_capacity_mw":20,"nvidia_blackwell_korea_total_chips":260000,"government_allocation_chips":50000,"samsung_allocation_chips":50000,"sk_group_allocation_chips":50000,"hyundai_allocation_chips":50000,"naver_allocation_chips":60000,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"aligned_for_sk_hynix_event_premium_for_followers","rerating_result":"AI_memory_and_AI_infra_demand_validation_4B_watch","notes":"Demand validation for leaders, but followers need company revenue bridge before Green."}
{"case_id":"r2_loop10_export_control_china_fab_watch","symbol":"005930/000660/067310/042700","company_name":"Samsung/SK Hynix/Hana Micron/Hanmi","case_type":"4c_watch","primary_archetype":"GEOPOLITICAL_EXPORT_CONTROL_OVERLAY","stage4c_date":"2025-09-01","price_validation":{"price_data_source":"Reuters reported event returns","stage3_price":null,"samsung_mae_1d_pct":-2.3,"sk_hynix_mae_1d_pct":-4.4,"hana_micron_mae_1d_pct":-1.7,"hanmi_mae_1d_pct":-4.4,"kospi_same_context_pct":-0.7,"samsung_relative_underperformance_pp":-1.6,"sk_hynix_relative_underperformance_pp":-3.7,"hanmi_relative_underperformance_pp":-3.7,"samsung_china_dram_exposure":"more_than_one_third","sk_hynix_china_dram_nand_exposure_pct":"30-40","authorization_effective_delay_days":120,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"export_control_4C_watch","notes":"Export-control shock is 4C-watch; hard 4C requires production/revenue disruption."}
{"case_id":"r2_loop10_hanwha_precision_hbm_equipment_spinoff","symbol":"012450_parent_exposure","company_name":"Hanwha Precision Machinery / Hanwha Aerospace spin-off exposure","case_type":"event_premium","primary_archetype":"CORPORATE_ACTION_SPINOFF_EVENT","stage2_date":"2024-04-05","stage4b_date":"2024-04-02/2024-04-05","price_validation":{"price_data_source":"Reuters corporate-action/event-return anchor","stage3_price":null,"media_report_event_mfe_pct":15,"formal_announcement_event_mae_pct":-8,"industrial_solutions_estimated_value_krw_trn":2,"industrial_solutions_estimated_value_usd_bn":1.48,"defense_business_estimated_value_krw_trn":10,"revenue_contribution_from_spun_units_pct":16,"parent_market_cap_context_krw_trn":11,"industrial_plus_defense_estimate_krw_trn":12,"estimated_sum_vs_parent_market_cap_pct":9.1,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium","rerating_result":"HBM_equipment_corporate_action_watch","notes":"HBM equipment optionality via spin-off is Stage 2/corporate-action event; order/revenue/margin required before Green."}
```

## shadow weight row 초안

```csv
archetype,eps_revision,hbm4_first_mover,capacity_bottleneck,confirmed_order,product_specificity,order_to_revenue,margin_visibility,advanced_packaging_capacity,price_path_alignment,event_penalty,labor_export_ip_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
MEMORY_HBM4_FIRST_MOVER,+5,+5,+5,+4,+5,+4,+4,+5,+5,-1,+3,+5,+4,SK Hynix confirms structural success but now requires 4B-watch.
HBM_CATCHUP_EXECUTION,+4,+3,+4,+3,+4,+3,+4,+3,+3,-2,+5,+4,+4,Samsung is Stage 2 until HBM/foundry volume sales and margins confirm.
FOUNDRY_TURNAROUND_CONTRACT,+4,+1,+2,+5,+3,+4,+5,+2,+3,-3,+4,+4,+4,Samsung Tesla/foundry deal helps but yield/margin and labor risks remain.
HBM_BONDER_EQUIPMENT_KOREA,+3,+0,+5,+5,+5,+4,+4,+3,+4,-3,+2,+5,+3,Hanmi confirmed order is good; unconfirmed customer rumor is 4B risk.
SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER,+2,+0,+2,+2,+4,+3,+3,+1,+2,-4,+1,+3,+3,Gaonchips design win needs tape-out, production and revenue.
POLICY_FOUNDRY_EVENT,+1,+0,+2,+1,+2,+1,+2,+1,+1,-5,+2,+4,+3,Policy foundry consultation is not company Green.
AI_CHIP_INFRASTRUCTURE_EVENT,+3,+2,+5,+3,+3,+2,+2,+2,+4,-4,+2,+5,+3,OpenAI/Nvidia events validate leaders but create event premium for followers.
GEOPOLITICAL_EXPORT_CONTROL_OVERLAY,+0,+0,+0,+0,+0,+0,+0,+0,+2,0,+5,+3,+5,China fab authorization loss is 4C-watch until production/revenue impact confirmed.
CORPORATE_ACTION_SPINOFF_EVENT,+1,+0,+2,+1,+2,+2,+3,+1,+2,-5,+2,+5,+3,Spin-off optionality requires listed vehicle, order book and revenue conversion.
```

---

# 이번 R2 Loop 10 결론

R2는 Stage 3가 실제로 대형 수익률을 만들 수 있는 섹터지만, 동시에 **가장 빨리 4B가 붙는 섹터**다.

```text
1. SK하이닉스는 R2 Stage 3 성공 benchmark다.
   HBM4, EUV, advanced packaging capacity가 모두 맞물린다.
   하지만 지금은 신규 Stage 3가 아니라 4B-watch다.

2. 삼성전자는 HBM/foundry catch-up 후보지만,
   HBM4 volume shipment, foundry margin, EPS revision 전 Green 금지다.
   노동 리스크와 China fab export-control은 4C-watch다.

3. 한미반도체는 confirmed SK Hynix order가 있는 구간은 좋지만,
   Micron 미확정 보도 +22%는 4B-watch다.

4. 가온칩스는 design win만으로 Green 금지다.
   tape-out, 양산, 매출, margin이 필요하다.

5. DB하이텍/policy foundry는 정책 event일 뿐이다.
   회사 단위 order / utilization / EPS 전 Green 금지다.

6. OpenAI/Nvidia Korea event는 수요 검증이지만,
   후발 AI infra basket에는 4B/event premium이다.

7. export-control shock은 R2의 핵심 4C-watch다.
   실제 생산·매출 차질로 이어지면 hard 4C로 승격한다.

8. Hanwha Precision spin-off는 HBM equipment optionality지만,
   corporate action만으로 Stage 3가 아니다.
```

한 문장으로 압축하면:

> **R2에서 진짜 Stage 3는 “AI 반도체 수혜”가 아니라, HBM·장비·디자인·메모리 가격이 고객 주문·CAPA 병목·마진·EPS revision으로 내려오고 가격경로가 뒤따르는 순간이다.**
> **그리고 R2는 AI 수요가 진짜여도 가격이 더 빨리 달리기 때문에, winner와 후발주 모두 4B-watch를 아주 빨리 붙여야 한다.**

[1]: https://www.reuters.com/world/sk-hynix-says-readying-hbm4-production-after-completing-internal-certification-2025-09-12/?utm_source=chatgpt.com "SK Hynix says readying HBM4 production after completing internal certification"
[2]: https://www.reuters.com/business/samsung-elec-signs-165-billion-deal-make-chips-global-firm-2025-07-28/?utm_source=chatgpt.com "Samsung Elec signs $16.5 billion deal to make chips for global firm"
[3]: https://www.wsj.com/articles/hanmi-semiconductor-climbs-after-media-reports-of-possible-deal-with-micron-e85398fb?utm_source=chatgpt.com "Hanmi Semiconductor Climbs After Media Reports of Possible Deal With Micron"
[4]: https://www.reuters.com/technology/artificial-intelligence/samsung-electronics-wins-cutting-edge-ai-chip-order-japans-preferred-networks-2024-07-09/?utm_source=chatgpt.com "Samsung Electronics wins cutting-edge AI chip order from Japan's Preferred Networks"
[5]: https://www.reuters.com/world/asia-pacific/south-korea-consider-setting-up-31-bln-foundry-grow-local-chip-sector-2025-12-10/?utm_source=chatgpt.com "South Korea to consider setting up $3.1 bln foundry to grow local chip sector"
[6]: https://www.reuters.com/world/asia-pacific/samsung-sk-hynix-shares-rally-openai-partnerships-2025-10-02/?utm_source=chatgpt.com "Samsung, SK Hynix shares leap after OpenAI chip deal"
[7]: https://www.reuters.com/world/china/shares-samsung-sk-hynix-drop-after-us-makes-it-harder-make-chips-china-2025-09-01/?utm_source=chatgpt.com "Shares in Samsung, SK Hynix drop after US makes it harder to make chips in China"
[8]: https://www.reuters.com/markets/asia/hanwha-aerospace-spin-off-semiconductor-equipment-unit-2024-04-05/?utm_source=chatgpt.com "South Korea's Hanwha Aerospace to spin off industrial solutions businesses from defence"
