순서상 이번은 **R2 Loop 12 — AI·반도체·전자부품 가격경로 검증 라운드**다.

```text
round = R2 Loop 12
round_id = round_186
large_sector = AI_SEMICONDUCTOR_ELECTRONICS
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = false
```

이번 R2 Loop 12는 SK하이닉스 HBM 성공을 benchmark로 두되, 반복을 줄이고 **Samsung HBM4/foundry catch-up, Hanmi HBM bonder, Gaonchips design house, LG Innotek AI-device/lidar component, LG Display LCD exit/OLED turnaround, CXMT 장비주 relief, China export-control RedTeam**까지 같이 본다.

원시 수정주가 일봉 OHLC는 이번 환경에서 안정적으로 확보하지 못했다. 대신 Reuters / WSJ / MarketWatch가 제공한 **가격 anchor, 이벤트 수익률, 계약금액, capex, 시장점유율, 정책·노동·수출통제 리스크 지표**만 계산했다. 30D/90D/180D full OHLC가 없는 항목은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R2 = AI·반도체·전자부품
```

R2의 Stage 3는 “AI 반도체 수혜”가 아니다.

**고객 주문, HBM 세대 전환, capacity bottleneck, 장비 발주, 패키징 capa, margin, EPS revision, 가격경로**가 같이 맞을 때다. 그리고 R2에서는 **labor disruption, China fab exposure, export-control, IP leakage, unconfirmed customer rumor**가 Green을 막는 RedTeam이다.

---

# 2. 대상 canonical archetype

```text
MEMORY_HBM4_CAPACITY_LEADER
HBM_CATCHUP_FOUNDRY_TURNAROUND
HBM_BONDER_EQUIPMENT_ORDER
SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER
AI_DEVICE_COMPONENT_OPTIONALITY
DISPLAY_LCD_EXIT_OLED_TURNAROUND
CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF
GEOPOLITICAL_EXPORT_CONTROL_OVERLAY
```

---

# 3. deep sub-archetype

```text
HBM leader:
- SK Hynix
- HBM sold-out / customer-specific HBM4
- ASML EUV order
- advanced packaging plant
- 4B-watch after massive MFE

Samsung catch-up:
- Samsung Electronics
- HBM4 Nvidia / AMD
- foundry turnaround
- Samsung $1T market-cap event
- union strike / labor disruption 4C-watch
- China fab export-control 4C-watch

HBM equipment:
- Hanmi Semiconductor
- TSV-TC bonder / HBM packaging equipment
- SK Hynix confirmed order
- Micron unconfirmed media report
- rumor-driven 4B

Design house:
- Gaonchips
- Samsung 2nm GAA / Preferred Networks AI chip
- design win vs tape-out / mass production / revenue

Electronic components:
- LG Innotek
- Apple AI replacement cycle
- Aeva lidar strategic collaboration
- camera-module dependence / single-customer risk

Display:
- LG Display
- LCD exit / Guangzhou plant sale
- OLED focus
- loss narrowing / financial-structure repair

China equipment relief:
- Jusung Engineering / Mirae Corp
- CXMT exclusion from entity list
- China-bound revenue relief
- export-control uncertainty

RedTeam:
- U.S. China-fab VEU revocation
- Samsung/SK China output exposure
- Hana Micron / Hanmi collateral selloff
- MATCH Act / CXMT / YMTC / SMIC pressure
```

---

# 4. 국장 신규 후보 case

## Case A — SK Hynix `structural_success + 4B-watch`

```text
symbol = 000660
case_type = structural_success + 4B-watch
archetype = MEMORY_HBM4_CAPACITY_LEADER
```

### stage date

```text
Stage 1:
2024-05-02
- HBM products sold out for 2024
- 2025 almost fully booked
- 12-stack HBM3E mass production planned
- AI-related chips expected to rise from 5% of memory revenue in 2023 to 61% by 2028

Stage 2:
2025-09-12
- HBM4 internal certification completed
- production system established for customers
- shares +7.3%
- KOSPI +1.2%

Stage 3:
2025-10-29 후보
- Q3 OP 11.4T won, +62% YoY
- all 2026 DRAM / HBM / NAND production sold out
- shares +6%
- KOSPI +1.5%

Stage 3 validation:
2026-03-24
- ASML EUV order 11.95T won / $7.97B
- shares +5.7%
- tools for HBM / advanced DRAM

Stage 4B:
2026-05-14
- shares +274% in 2025
- shares > +200% in 2026
- market cap about $942B
- valued under $100B 16 months earlier
```

SK Hynix는 R2에서 여전히 **Stage 3 성공 benchmark**다. HBM이 단순 테마가 아니라 sold-out capacity, customer-specific HBM4, record operating profit, EUV 장비 발주, advanced packaging capex로 이어졌다. 다만 2025년 +274%, 2026년 +200% 이상, 시총 약 $942B까지 온 상태라 지금은 신규 Green보다 **4B-watch**가 더 중요하다. ([월스트리트저널][1])

### 실제 가격경로 검증

```text
price_data_source:
WSJ / Reuters reported price and event anchors

stage3_price:
N/A

HBM_sold_out_2024:
true

HBM_almost_booked_2025:
true

AI_chip_revenue_share_2023:
5%

AI_chip_revenue_share_2028_expected:
61%

HBM4_internal_certification_event_MFE:
+7.3%

KOSPI_same_context:
+1.2%

relative_outperformance:
7.3 - 1.2
= +6.1pp

Q3_2025_OP:
11.4T won / $8.02B

Q3_2025_OP_growth:
+62% YoY

Q3_2025_event_MFE:
+6.0%

KOSPI_same_context_Q3:
+1.5%

relative_outperformance_Q3:
6.0 - 1.5
= +4.5pp

ASML_EUV_order:
11.95T won / $7.97B

ASML_event_MFE:
+5.7%

advanced_packaging_plant:
19T won / $12.9B

reported_2025_return:
+274%

reported_2026_return:
> +200%

market_cap:
about $942B

minimum_market_cap_MFE_from_under_100B:
942 / 100 - 1
= +842% 이상

MFE_30D / 90D / 180D / 1Y / 2Y:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = aligned
rerating_result = true_HBM_structural_rerating
current_state = 4B_watch
stage_failure_type = none
```

---

## Case B — Samsung Electronics `success_candidate + labor/export-control 4C-watch`

```text
symbol = 005930
case_type = success_candidate + 4C-watch
archetype = HBM_CATCHUP_FOUNDRY_TURNAROUND
```

### stage date

```text
Stage 1:
2025~2026
- HBM4 catch-up
- foundry turnaround
- Nvidia / AMD / Tesla / AI inference chip exposure

Stage 2:
2026-01-25
- Samsung to begin HBM4 production for Nvidia supply
- reportedly passed HBM4 qualification for Nvidia and AMD
- Samsung shares +2.2%
- SK Hynix -2.9%

Stage 2 추가:
2026-03-16
- Nvidia flags Samsung tie-up on new AI chips
- Samsung AI inference chip using 4nm process
- shares +5% to 196,800 won
- KOSPI +2.7%

Stage 2 추가:
2026-03-18
- Samsung / AMD MoU
- HBM4 for AMD Instinct MI455X
- DDR5 for EPYC
- possible foundry partnership

Stage 4B:
2026-05-06
- Samsung +14.4%
- reaches $1T market cap
- KOSPI closes +6.45%

Stage 4C-watch:
2025-09-01
- U.S. China-fab equipment authorization revoked
- Samsung -2.3%
- KOSPI -0.7%
- > one-third of Samsung DRAM output from China

Stage 4C-watch:
2026-05-12~18
- Samsung union strike risk
- May 21, 2026 strike threat
- more than 45,000 workers could join
- talks resume May 19, 2026
```

Samsung은 HBM4와 foundry catch-up에서 강한 Stage 2다. Nvidia·AMD 쪽 evidence가 계속 붙고, 2026년 5월 6일에는 $1T market cap까지 갔다. 하지만 아직 SK Hynix 같은 clean Stage 3는 아니다. 이유는 세 가지다. 첫째, HBM4 volume shipment와 margin이 완전히 닫히지 않았다. 둘째, China fab export-control이 남아 있다. 셋째, 2026년 5월 18일 현재 union strike risk가 아직 hard 4C는 아니지만 강한 4C-watch다. ([Reuters][2])

### 실제 가격경로 검증

```text
price_data_source:
Reuters HBM4 / Nvidia / AMD / KOSPI / labor / export-control anchors

stage3_price:
N/A

HBM4_Nvidia_event_MFE:
+2.2%

SK_Hynix_same_context:
-2.9%

Nvidia_AI_chip_tieup_event_MFE:
+5.0%

Nvidia_tieup_price_anchor:
196,800 won

KOSPI_same_context_Nvidia:
+2.7%

relative_outperformance_Nvidia_event:
5.0 - 2.7
= +2.3pp

KOSPI_7000_day_Samsung_MFE:
+14.4%

KOSPI_same_context:
+6.45%

relative_outperformance_KOSPI_7000_day:
14.4 - 6.45
= +7.95pp

Samsung_market_cap_milestone:
$1T

AMD_MoU:
HBM4 for Instinct MI455X
DDR5 for EPYC
possible foundry partnership

Samsung_HBM_share_context:
22%

SK_Hynix_HBM_share_context:
57%

China_fab_export_control_event_MAE:
-2.3%

KOSPI_export_control_context:
-0.7%

relative_underperformance_export_control:
-2.3 - (-0.7)
= -1.6pp

Samsung_China_DRAM_exposure:
> one-third

strike_risk_workers:
>45,000 in Reuters May 18 source
>50,000 in Reuters May 12 context

strike_start_target:
2026-05-21

hard_4C_status:
not confirmed as of 2026-05-18

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate + 4C_watch
rerating_result = HBM4_foundry_catchup_watch
stage_failure_type = stage2_not_green_until_volume_margin_labor_export_risk_clear
```

---

## Case C — Hanmi Semiconductor `success_candidate + rumor 4B-watch`

```text
symbol = 042700
case_type = success_candidate + 4B-watch
archetype = HBM_BONDER_EQUIPMENT_ORDER
```

### stage date

```text
Stage 1:
2024-03
- HBM packaging equipment demand
- TSV-TC bonder exposure
- SK Hynix / HBM supply-chain exposure

Stage 2:
2024-03
- confirmed SK Hynix supply deal 21.48B won
- recent contract wins around 200B won
- Hanmi supplies SK Hynix HBM packaging equipment

Stage 2 / 4B:
2024-03-26
- Hanmi +16%
- SK Hynix +4.3%
- KOSPI +0.7%

Stage 4B:
2024-03-28
- unconfirmed Micron media report
- Hanmi +22% to 139,100 won
- KOSPI -0.3%
- Hanmi / Micron did not confirm

Stage 4C-watch:
2025-09-01
- U.S. China-fab export-control event
- Hanmi -4.4%
```

Hanmi는 HBM equipment에서 좋은 Stage 2다. confirmed SK Hynix order와 HBM bonder exposure가 있다. 하지만 Micron 미확정 보도만으로 +22%를 기록한 구간은 Green이 아니라 4B다. R2 장비주는 고객 다변화 소식이 나올 때 반드시 **confirmed order vs rumor**를 분리해야 한다. ([월스트리트저널][3])

### 실제 가격경로 검증

```text
price_data_source:
WSJ / Reuters event and contract anchors

stage3_price:
N/A

SK_Hynix_contract:
21.48B won

recent_contract_wins:
about 200B won

2024-03-26_Hanmi_MFE:
+16%

2024-03-26_SK_Hynix_MFE:
+4.3%

KOSPI_same_context:
+0.7%

Hanmi_relative_outperformance_2024-03-26:
16 - 0.7
= +15.3pp

2024-03-28_Micron_rumor_MFE:
+22%

rumor_event_price:
139,100 won

implied_pre_rumor_reference_price:
139,100 / 1.22
= about 114,016 won

KOSPI_same_context_rumor:
-0.3%

relative_outperformance_rumor:
22 - (-0.3)
= +22.3pp

Micron_deal_status:
unconfirmed media report

China_export_control_event_MAE:
-4.4%

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate + 4B_watch
rerating_result = HBM_bonder_equipment_watch
stage_failure_type = confirmed_order_good_but_unconfirmed_customer_rumor_4B
```

---

## Case D — Gaonchips `success_candidate / design-win not revenue`

```text
symbol = 399720
case_type = success_candidate + insufficient_price_data
archetype = SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER
```

### stage date

```text
Stage 1:
2024-07-09
- Samsung 2nm GAA / advanced packaging
- AI chip design house exposure
- Japanese Preferred Networks AI chip

Stage 2:
2024-07-09
- Samsung wins Preferred Networks AI chip order
- Gaonchips designed the chips
- chips for generative AI / LLM high-performance computing hardware
- order size not disclosed

Stage 3:
없음
- design win alone is not Green
- tape-out, mass production, revenue recognition, gross margin 확인 필요

Stage 4B:
AI design-house theme으로 주가가 먼저 급등하면 후보

Stage 4C:
tape-out delay, yield issue, customer cancellation, no revenue conversion
```

Gaonchips는 시스템반도체 design-house Stage 2다. Samsung이 Preferred Networks AI chip을 2nm GAA와 advanced packaging으로 생산하는 첫 공개 수주를 확보했고, 그 칩 설계를 Gaonchips가 맡았다. 하지만 order size는 공개되지 않았고, design win은 revenue가 아니다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters design-win evidence

stage3_price:
N/A

order_size:
not disclosed

customer:
Preferred Networks

foundry:
Samsung Electronics

process:
2nm GAA

packaging:
advanced packaging

designer:
Gaonchips

end_use:
generative AI / LLM high-performance computing hardware

MFE / MAE:
price_data_unavailable_after_deep_search

reason:
- Reuters provides design-win evidence but no Gaonchips adjusted OHLC or event price anchor.
```

### alignment

```text
score_price_alignment = success_candidate_but_insufficient_price_data
rerating_result = AI_design_house_watch
stage_failure_type = design_win_not_revenue
```

---

## Case E — LG Innotek `success_candidate + Apple AI / lidar optionality`

```text
symbol = 011070
case_type = success_candidate + event_premium
archetype = AI_DEVICE_COMPONENT_OPTIONALITY
```

### stage date

```text
Stage 1:
2024-06-12
- Apple Intelligence / OpenAI iPhone cycle
- iPhone camera-module supplier replacement demand expectation

Stage 2:
2024-06-12
- LG Innotek shares up to +19%
- KOSPI +0.4%
- 2024 operating profit projected +33%

Stage 2 추가:
2025-07-29
- LG Innotek / Aeva strategic collaboration
- total deal $50M
- LG Innotek equity investment $32M
- single-digit stake
- lidar production capacity for robotics / consumer electronics / AR

Stage 3:
없음
- Apple AI replacement cycle / lidar partnership alone is not Green
- actual iPhone volumes, ASP, camera-module margin, Aeva volume ramp, FCF 확인 필요

Stage 4B:
Apple AI / lidar optionality로 price가 먼저 rerating되면 후보

Stage 4C:
Apple demand miss, camera-module ASP pressure, single-customer concentration, lidar adoption delay
```

LG Innotek은 R2 전자부품에서 “AI-device replacement cycle” 후보지만, Stage 3는 아니다. Apple/OpenAI 뉴스 이후 주가가 최대 19% 올랐고, 이후 Aeva와 $50M 전략협력, $32M 지분투자로 lidar optionality가 붙었다. 그러나 실제 Green은 iPhone 출하·부품 ASP·module margin·lidar volume ramp로 닫혀야 한다. ([월스트리트저널][5])

### 실제 가격경로 검증

```text
price_data_source:
WSJ Apple-AI event anchor / Reuters Aeva deal anchor

stage3_price:
N/A

Apple_AI_event_MFE:
+19%

KOSPI_same_context:
+0.4%

relative_outperformance:
19 - 0.4
= +18.6pp

2024_OP_growth_projection:
+33%

Aeva_total_deal:
$50M

LG_Innotek_equity_investment:
$32M

Aeva_stake:
single-digit percentage

remaining_deal_amount_for_capacity:
$50M - $32M
= $18M

target_applications:
vehicles
industrial equipment
robotics
consumer electronics
AR headsets

MFE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_event_premium
rerating_result = AI_device_component_optionality_watch
stage_failure_type = stage2_optionality_not_green
```

---

## Case F — LG Display `success_candidate / LCD exit + OLED turnaround watch`

```text
symbol = 034220
case_type = success_candidate + evidence_incomplete
archetype = DISPLAY_LCD_EXIT_OLED_TURNAROUND
```

### stage date

```text
Stage 1:
2024-04~07
- LCD oversupply exit
- OLED focus
- Apple OLED iPad / iPhone Pro Max panel demand
- financial structure repair

Stage 2:
2024-07-25
- Q2 operating loss narrowed to 94B won
- expected loss 308B won
- prior-year loss 881B won
- revenue +42% to 6.7T won

Stage 2 추가:
2024-09-26
- Guangzhou LCD plant sale to TCL CSOT
- 10.8B yuan / $1.54B
- includes 80% large LCD panel plant + 100% LCD module plant
- focus on higher-margin OLED

Stage 3:
없음
- restructuring and loss narrowing are Stage 2
- sustained OLED margin, FCF, customer mix, debt reduction 확인 전 Green 금지

Stage 4B:
LCD exit / OLED turnaround story로 price가 먼저 움직이면 후보

Stage 4C:
OLED demand miss, Apple concentration, panel-price decline, LCD sale delay, cash burn
```

LG Display는 구조조정 Stage 2다. Q2 loss가 크게 줄었고, Guangzhou LCD plant 매각으로 LCD exit와 OLED focus가 명확해졌다. 하지만 아직 Stage 3는 아니다. OLED mix, sustained profit, FCF, debt reduction이 확인되어야 한다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters earnings / LCD plant sale anchors

stage3_price:
N/A

Q2_operating_loss:
94B won

expected_Q2_loss:
308B won

loss_surprise_vs_expected:
1 - 94 / 308
= 69.5% smaller loss than expected

prior_year_Q2_loss:
881B won

loss_reduction_vs_prior_year:
1 - 94 / 881
= 89.3% smaller loss

Q2_revenue:
6.7T won

revenue_growth:
+42%

Q2_OP_margin:
-94B / 6.7T
= -1.4%

Guangzhou_LCD_sale:
10.8B yuan / $1.54B

stake_sold:
80% large LCD panel plant
100% LCD module plant

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate_but_evidence_incomplete
rerating_result = LCD_exit_OLED_turnaround_watch
stage_failure_type = restructuring_stage2_not_green
```

---

## Case G — Jusung Engineering / Mirae Corp `event_premium + China exposure watch`

```text
symbols = 036930 / 025560
case_type = event_premium + 4C-watch
archetype = CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF
```

### stage date

```text
Stage 1:
2024-11~12
- U.S. China chip export curbs
- CXMT entity-list exclusion possibility
- Korean China-bound equipment exposure

Stage 2:
2024-12-03
- CXMT excluded from U.S. entity list
- Korean equipment suppliers get short-term relief
- Jusung +7.7% after nearly -7% previous session
- Mirae +1.4%, after +7% previous session
- Mirae derived 15% of 1H revenue from CXMT
- Mirae signed about 9B won supply deals with CXMT

Stage 3:
없음
- relief is not Green
- non-China diversification, order book durability, margin, export-control durability 확인 필요

Stage 4B:
CXMT exclusion relief로 price가 먼저 움직이면 후보

Stage 4C:
MATCH Act, renewed CXMT restrictions, China capex cut, receivables risk
```

Jusung/Mirae는 장비주가 **China relief event**에 얼마나 민감한지 보여준다. CXMT가 entity list에서 빠지자 Jusung은 전일 약 -7% 뒤 +7.7%, Mirae는 +1.4% 올랐다. Mirae는 1H 매출의 약 15%가 CXMT였고, 그해 CXMT와 약 90억 원 공급계약을 체결했다. 하지만 이것은 Green이 아니라 **export-control relief**다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters CXMT exclusion / equipment supplier anchor

stage3_price:
N/A

Jusung_previous_session_MAE:
nearly -7%

Jusung_relief_MFE:
+7.7%

Mirae_relief_MFE:
+1.4%

Mirae_previous_session_MFE:
+7%

Mirae_CXMT_revenue_share_1H2024:
about 15%

Mirae_CXMT_supply_deals_2024:
about 9B won / $6.41M

China_equipment_imports_9M2024:
$24.12B

China_equipment_import_growth:
+33%

expected_China_chip_capex_drop_from_curbs:
about $10B / around -30% YoY to $35B

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium_4C_watch
rerating_result = China_equipment_relief_watch
stage_failure_type = relief_stage2_not_green
```

---

## Case H — Samsung / SK Hynix / Hana Micron / Hanmi export-control basket `4C-watch`

```text
symbols = 005930 / 000660 / 067310 / 042700
case_type = 4C-watch
archetype = GEOPOLITICAL_EXPORT_CONTROL_OVERLAY
```

### stage date

```text
Stage 1:
2025-08-29
- U.S. revokes VEU authorizations for Samsung and SK Hynix China fabs
- licenses required for U.S. equipment into China
- expansion / tech upgrade licenses not intended to be granted

Stage 4C-watch:
2025-09-01
- Samsung -2.3%
- SK Hynix -4.4%
- Hana Micron -1.7%
- Hanmi Semiconductor -4.4%
- KOSPI -0.7%

Stage 4C-watch 추가:
2026-04-22
- Micron pushes MATCH Act
- targets CXMT, YMTC, SMIC and DUV immersion equipment restrictions
- risk to China equipment servicing / export licensing

Stage 3:
없음
- export-control shock is RedTeam overlay, not positive evidence
```

R2에서 export-control은 단순 뉴스가 아니라 hard gate 후보의 전 단계다. 미국이 Samsung과 SK Hynix의 중국 fab 장비 반입 허가를 취소하자 Samsung, SK Hynix, Hana Micron, Hanmi가 함께 하락했다. Samsung DRAM의 3분의 1 이상, SK Hynix DRAM/NAND의 30~40%가 중국에 있다는 exposure도 확인됐다. 아직 hard 4C는 아니지만, license denial·upgrade restriction·China revenue impairment가 확인되면 hard 4C로 승격한다. ([Reuters][8])

### 실제 가격경로 검증

```text
price_data_source:
Reuters export-control / MATCH Act anchors

stage3_price:
N/A

Samsung_event_MAE:
-2.3%

SK_Hynix_event_MAE:
-4.4%

Hana_Micron_event_MAE:
-1.7%

Hanmi_event_MAE:
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

VEU_revocation_effective_delay:
120 days

license_policy:
existing operations likely allowed
capacity expansion / technology upgrade not intended

MATCH_Act_targets:
CXMT
YMTC
SMIC
DUV immersion machines
foreign equipment servicing alignment

hard_4C_status:
not confirmed

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = export_control_overlay_watch
stage_failure_type = 4C_watch_not_hard_4C
```

---

# 5. 이번 R2 case별 요약표

| case                  | 분류                               |                                                                           실제 가격검증 | alignment               |
| --------------------- | -------------------------------- | --------------------------------------------------------------------------------: | ----------------------- |
| SK Hynix              | structural_success + 4B          |                      HBM4 +7.3%, Q3 OP 11.4T, ASML +5.7%, 2025 +274%, 2026 +200%+ | aligned / now 4B        |
| Samsung Electronics   | success_candidate + 4C-watch     | HBM4 +2.2%, Nvidia +5%, KOSPI 7000 day +14.4%, export-control -2.3%, strike watch | Stage 2                 |
| Hanmi Semiconductor   | success_candidate + 4B           |                           confirmed SKH 21.48B won; Micron rumor +22% to 139,100원 | order + rumor 4B        |
| Gaonchips             | success_candidate / insufficient |               Samsung 2nm PFN AI chip, Gaonchips designed, order size undisclosed | design win              |
| LG Innotek            | success_candidate / event        |                                                     Apple AI +19%, Aeva $50M deal | AI-device optionality   |
| LG Display            | success_candidate / incomplete   |                               Q2 loss 94B vs expected 308B; Guangzhou sale $1.54B | OLED turnaround Stage 2 |
| Jusung / Mirae        | event premium + 4C-watch         |                                     Jusung -7% then +7.7%; Mirae CXMT 15% revenue | China relief            |
| Export-control basket | 4C-watch                         |                                  Samsung -2.3%, SK -4.4%, Hana -1.7%, Hanmi -4.4% | RedTeam                 |

---

# 6. score-price alignment 판정

```text
aligned:
- SK Hynix

aligned_but_now_4B:
- SK Hynix

success_candidate:
- Samsung Electronics
- Hanmi Semiconductor
- Gaonchips
- LG Innotek
- LG Display

event_premium:
- Hanmi Micron unconfirmed report
- LG Innotek Apple AI replacement-cycle event
- Jusung / Mirae CXMT relief

price_moved_without_evidence:
- Hanmi Micron rumor before confirmed order
- Apple AI component rally before iPhone volume / module margin proof
- design-house rally before tape-out / production / revenue

evidence_incomplete:
- Gaonchips
- LG Display
- LG Innotek

thesis_break_watch:
- Samsung labor strike risk
- Samsung/SK China export-control risk
- Hana Micron / Hanmi collateral export-control risk
- Jusung/Mirae China customer concentration

hard_4C_confirmed:
- false
```

---

# 7. 점수비중 교정

## 올릴 축

```text
confirmed_customer_order +5
HBM_generation_transition +5
capacity_bottleneck +5
advanced_packaging_capacity +5
EUV_order +5
delivery_or_mass_production_readiness +5
customer_specific_design_lockin +4
order_to_revenue_conversion +5
gross_margin_visibility +5
price_path_alignment +5
```

### 왜 올리나

SK Hynix는 HBM4 certification, Q3 record OP, ASML EUV order, advanced packaging investment, capacity sold-out이 모두 연결됐다. Hanmi는 confirmed SK Hynix order가 있고, Samsung은 HBM4/foundry catch-up Stage 2가 있다. 하지만 Samsung·Hanmi·Gaonchips·LG Innotek·LG Display는 아직 **revenue/margin/FCF bridge**가 완전히 닫히지 않았다.

## 내릴 축

```text
AI_keyword_only -5
unconfirmed_customer_rumor -5
design_win_without_revenue -5
Apple_AI_replacement_cycle_only -4
lidar_optionality_without_volume -4
LCD_exit_without_OLED_profit -4
China_customer_concentration -5
export_control_exposure -5
labor_disruption_risk -5
event_rally_before_revenue -5
```

### 왜 내리나

Hanmi의 Micron event는 미확정 보도만으로 +22%였다. Gaonchips는 design win은 있지만 order size와 revenue가 없다. LG Innotek은 Apple AI cycle 기대와 Aeva lidar optionality가 있지만, actual volume/margin이 필요하다. LG Display는 loss narrowing과 LCD exit는 좋지만 OLED profit/FCF가 필요하다. Export-control은 장비주와 memory maker 모두에 강한 RedTeam이다.

## Green gate 강화 조건

```text
R2 Stage 3-Green 필수:
1. confirmed customer order
2. product-specific exposure
3. delivery / mass production / shipment readiness
4. revenue recognition path
5. gross margin / OPM improvement
6. EPS / FCF revision
7. capacity bottleneck or allocation power
8. customer concentration / China exposure / labor / export-control risk 통과
9. 가격경로가 evidence 이후 따라옴

금지:
AI keyword only
미확정 고객 보도
design win only
Apple replacement-cycle 기대만 있음
capex / plant sale / partnership only
China customer relief만 있음
labor strike risk unresolved
export-control risk unresolved
```

## 4B 조기감지 조건

```text
4B-watch:
Stage 3 이후 3~5배 이상 상승
market-cap milestone headline화
HBM/customer rumor로 +20% 이상 급등
KOSPI 7000 / AI FOMO day에 대형주 +10% 이상 상승
Apple AI / lidar optionality로 component주 급등
China/CXMT relief로 장비주 급등
good news에도 price reaction 둔화

4B-elevated:
SK Hynix처럼 $1T 근접
Samsung처럼 $1T milestone + labor/export-risk 동시 존재
Hanmi처럼 unconfirmed customer report +22%
LG Innotek처럼 replacement-cycle 전 +19%
Jusung처럼 export-control relief만으로 +7.7%
```

## 4C hard gate 조건

```text
HBM qualification failure
volume shipment failure
customer order cancellation
order push-out
China fab license denial
China technology-upgrade block
labor strike / production halt
IP leakage / China competitive catch-up
gross margin collapse
customer concentration loss
cash burn / capex overrun
```

이번 R2 Loop 12에서는 hard 4C를 확정하지 않는다. 다만 **Samsung labor strike**, **Samsung/SK China fab export-control**, **Hanmi/Hana collateral selloff**, **Jusung/Mirae CXMT exposure**는 모두 강한 4C-watch다.

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
```

---

# 9. patch-ready 출력

## docs/round/round_186.md 요약

```md
# R2 Loop 12. AI Semiconductor Electronics Price Validation

이번 라운드는 R2 Loop 12 price-validation 라운드다.

핵심 결론:
- SK Hynix remains the structural success benchmark. HBM was sold out for 2024 and nearly fully booked for 2025. HBM4 certification event drove +7.3% vs KOSPI +1.2%. Q3 2025 OP was 11.4T won, +62% YoY, and 2026 output was sold out. ASML EUV order was 11.95T won / $7.97B. Current state is 4B-watch after 2025 +274% and 2026 >+200%.
- Samsung Electronics is HBM4/foundry catch-up Stage 2 plus 4C-watch. HBM4 Nvidia event +2.2%, Nvidia AI chip tie-up +5%, Samsung +14.4% on KOSPI 7000 day. But labor strike risk and China-fab export-control risk block Green.
- Hanmi Semiconductor is HBM bonder Stage 2 plus rumor 4B-watch. Confirmed SK Hynix contract was 21.48B won; unconfirmed Micron media report drove +22% to 139,100 won.
- Gaonchips is design-house Stage 2. Samsung won a Preferred Networks AI chip order using 2nm GAA and advanced packaging; Gaonchips designed the chips, but order size/revenue were not disclosed.
- LG Innotek is AI-device component optionality Stage 2. Apple AI event drove up to +19%; Aeva strategic collaboration was $50M including $32M equity investment. Actual volume/margin required.
- LG Display is LCD-exit/OLED-turnaround Stage 2. Q2 operating loss narrowed to 94B won versus expected 308B won; Guangzhou LCD plant sale was $1.54B. Sustained OLED profit and FCF required.
- Jusung/Mirae CXMT relief is event premium and China-exposure 4C-watch. Jusung +7.7% after nearly -7%; Mirae derived about 15% of 1H revenue from CXMT and signed about 9B won deals.
- Export-control basket is 4C-watch. Samsung -2.3%, SK Hynix -4.4%, Hana Micron -1.7%, Hanmi -4.4%; Samsung China DRAM exposure is over one-third, SK Hynix China DRAM/NAND exposure 30~40%.
```

## docs/checkpoints/checkpoint_28a_round186_r2_loop12.md 요약

```md
# Checkpoint 28A Round 186 R2 Loop 12 AI Semiconductor Electronics Price Validation

## 반영 내용
- R2 Loop 12 price-validation 라운드를 추가했다.
- HBM4 capacity leader, Samsung HBM4/foundry catch-up, HBM bonder equipment, AI design house, AI-device component, display LCD exit/OLED turnaround, CXMT equipment relief, China export-control overlay를 비교했다.
- Reuters / WSJ / MarketWatch anchors로 가능한 MFE/MAE 및 event metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- confirmed customer order, HBM generation transition, capacity bottleneck, advanced packaging capacity, EUV order, delivery/mass-production readiness, order-to-revenue conversion 가중치 강화
- AI keyword-only, unconfirmed customer rumor, design win without revenue, Apple AI cycle-only, lidar optionality without volume, LCD exit without OLED profit, China exposure, labor/export-control risk 감점 강화
```

## data/e2r_case_library/cases_r2_loop12_round186.jsonl 초안

```jsonl
{"case_id":"r2_loop12_sk_hynix_hbm4_structural_success_4b","symbol":"000660","company_name":"SK Hynix","case_type":"structural_success","primary_archetype":"MEMORY_HBM4_CAPACITY_LEADER","stage2_date":"2025-09-12","stage3_date":"2025-10-29_candidate","stage4b_date":"2026-05-14","price_validation":{"price_data_source":"WSJ/Reuters reported anchors","stage3_price":null,"hbm_sold_out_2024":true,"hbm_almost_booked_2025":true,"ai_chip_revenue_share_2023_pct":5,"ai_chip_revenue_share_2028_expected_pct":61,"hbm4_certification_event_mfe_pct":7.3,"kospi_same_context_pct":1.2,"relative_outperformance_pp":6.1,"q3_2025_op_krw_trn":11.4,"q3_2025_op_growth_pct":62,"q3_2025_event_mfe_pct":6.0,"asml_euv_order_krw_trn":11.95,"asml_euv_order_usd_bn":7.97,"asml_event_mfe_pct":5.7,"advanced_packaging_investment_krw_trn":19,"reported_return_2025_pct":274,"reported_return_2026_ytd_min_pct":200,"market_cap_usd_bn":942,"market_cap_mfe_from_under_100b_pct":842,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"aligned","rerating_result":"true_HBM_structural_rerating","notes":"Stage 3 worked; current state is 4B-watch due massive MFE and market-cap milestone."}
{"case_id":"r2_loop12_samsung_hbm4_foundry_labor_export_watch","symbol":"005930","company_name":"Samsung Electronics","case_type":"success_candidate","primary_archetype":"HBM_CATCHUP_FOUNDRY_TURNAROUND","stage2_date":"2026-01-25/2026-03-16/2026-03-18","stage4b_date":"2026-05-06","stage4c_date":"2025-09-01/2026-05_watch","price_validation":{"price_data_source":"Reuters HBM4/foundry/labor/export-control anchors","stage3_price":null,"hbm4_nvidia_event_mfe_pct":2.2,"sk_hynix_same_context_pct":-2.9,"nvidia_ai_chip_tieup_event_mfe_pct":5.0,"nvidia_tieup_price_anchor_krw":196800,"kospi_same_context_nvidia_pct":2.7,"relative_outperformance_nvidia_event_pp":2.3,"kospi_7000_day_samsung_mfe_pct":14.4,"kospi_7000_day_kospi_pct":6.45,"relative_outperformance_kospi7000_pp":7.95,"market_cap_milestone_usd_trn":1,"amd_mou":"HBM4 for Instinct MI455X, DDR5 for EPYC, possible foundry partnership","samsung_hbm_share_pct":22,"sk_hynix_hbm_share_pct":57,"china_export_control_mae_pct":-2.3,"china_dram_exposure":"more_than_one_third","strike_risk_workers":45000,"strike_start_target":"2026-05-21","hard_4c_status":"not_confirmed_as_of_2026-05-18","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_4C_watch","rerating_result":"HBM4_foundry_catchup_watch","notes":"Samsung has strong Stage 2, but volume/margin plus labor and China export-control risks block Green."}
{"case_id":"r2_loop12_hanmi_hbm_bonder_order_rumor_4b","symbol":"042700","company_name":"Hanmi Semiconductor","case_type":"success_candidate","primary_archetype":"HBM_BONDER_EQUIPMENT_ORDER","stage2_date":"2024-03","stage4b_date":"2024-03-28","stage4c_date":"2025-09-01_watch","price_validation":{"price_data_source":"WSJ/Reuters contract and event anchors","stage3_price":null,"sk_hynix_contract_krw_bn":21.48,"recent_contract_wins_krw_bn":200,"event_mfe_20240326_pct":16,"sk_hynix_event_mfe_20240326_pct":4.3,"kospi_same_context_pct":0.7,"relative_outperformance_pp":15.3,"micron_rumor_event_mfe_pct":22,"rumor_event_price_krw":139100,"implied_pre_rumor_reference_price_krw":114016,"kospi_rumor_context_pct":-0.3,"relative_outperformance_rumor_pp":22.3,"micron_deal_status":"unconfirmed_media_report","china_export_control_event_mae_pct":-4.4,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_4B_watch","rerating_result":"HBM_bonder_equipment_watch","notes":"Confirmed SK Hynix order is Stage 2; unconfirmed Micron rumor is 4B-watch."}
{"case_id":"r2_loop12_gaonchips_pfn_ai_design_house","symbol":"399720","company_name":"Gaonchips","case_type":"success_candidate","primary_archetype":"SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER","stage2_date":"2024-07-09","price_validation":{"price_data_source":"Reuters design-win evidence","stage3_price":null,"order_size":"not_disclosed","customer":"Preferred Networks","foundry":"Samsung Electronics","process":"2nm GAA","packaging":"advanced packaging","designer":"Gaonchips","end_use":"generative AI / LLM high-performance computing hardware","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_insufficient_price_data","rerating_result":"AI_design_house_watch","notes":"Design win is Stage 2; tape-out, mass production, revenue and margin required before Green."}
{"case_id":"r2_loop12_lg_innotek_apple_ai_aeva_lidar","symbol":"011070","company_name":"LG Innotek","case_type":"success_candidate","primary_archetype":"AI_DEVICE_COMPONENT_OPTIONALITY","stage2_date":"2024-06-12/2025-07-29","stage4b_date":"2024-06-12_watch","price_validation":{"price_data_source":"WSJ Apple-AI event / Reuters Aeva deal anchors","stage3_price":null,"apple_ai_event_mfe_pct":19,"kospi_same_context_pct":0.4,"relative_outperformance_pp":18.6,"op_growth_projection_2024_pct":33,"aeva_total_deal_usd_mn":50,"lg_innotek_equity_investment_usd_mn":32,"aeva_stake":"single_digit_percentage","remaining_capacity_amount_usd_mn":18,"target_applications":["vehicles","industrial equipment","robotics","consumer electronics","AR headsets"],"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_event_premium","rerating_result":"AI_device_component_optionality_watch","notes":"Apple AI and lidar optionality are Stage 2; actual volume, ASP, module margin and FCF required before Green."}
{"case_id":"r2_loop12_lg_display_lcd_exit_oled_turnaround","symbol":"034220","company_name":"LG Display","case_type":"success_candidate","primary_archetype":"DISPLAY_LCD_EXIT_OLED_TURNAROUND","stage2_date":"2024-07-25/2024-09-26","price_validation":{"price_data_source":"Reuters earnings and LCD sale anchors","stage3_price":null,"q2_operating_loss_krw_bn":94,"expected_q2_loss_krw_bn":308,"loss_surprise_vs_expected_pct":69.5,"prior_year_q2_loss_krw_bn":881,"loss_reduction_vs_prior_year_pct":89.3,"q2_revenue_krw_trn":6.7,"revenue_growth_pct":42,"q2_op_margin_pct":-1.4,"guangzhou_lcd_sale_yuan_bn":10.8,"guangzhou_lcd_sale_usd_bn":1.54,"stake_sold":["80% large LCD panel plant","100% LCD module plant"],"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_evidence_incomplete","rerating_result":"LCD_exit_OLED_turnaround_watch","notes":"Loss narrowing and LCD exit are Stage 2; sustained OLED profit and FCF required before Green."}
{"case_id":"r2_loop12_jusung_mirae_cxmt_relief_watch","symbol":"036930/025560","company_name":"Jusung Engineering / Mirae Corp","case_type":"event_premium","primary_archetype":"CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF","stage2_date":"2024-12-03","stage4c_date":"2024-12_watch","price_validation":{"price_data_source":"Reuters CXMT exclusion / Korean supplier anchor","stage3_price":null,"jusung_previous_session_mae_pct":-7,"jusung_relief_mfe_pct":7.7,"mirae_relief_mfe_pct":1.4,"mirae_previous_session_mfe_pct":7,"mirae_cxmt_revenue_share_1h2024_pct":15,"mirae_cxmt_supply_deals_krw_bn":9,"china_equipment_imports_9m2024_usd_bn":24.12,"china_equipment_import_growth_pct":33,"expected_china_chip_capex_drop_usd_bn":10,"expected_china_chip_capex_drop_pct":30,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_4C_watch","rerating_result":"China_equipment_relief_watch","notes":"CXMT exclusion is relief, not Green; customer concentration and export-control durability remain RedTeam."}
{"case_id":"r2_loop12_export_control_overlay_samsung_skh_hana_hanmi","symbol":"005930/000660/067310/042700","company_name":"Samsung / SK Hynix / Hana Micron / Hanmi export-control basket","case_type":"4c_watch","primary_archetype":"GEOPOLITICAL_EXPORT_CONTROL_OVERLAY","stage4c_date":"2025-09-01/2026-04-22_watch","price_validation":{"price_data_source":"Reuters export-control / MATCH Act anchors","stage3_price":null,"samsung_event_mae_pct":-2.3,"sk_hynix_event_mae_pct":-4.4,"hana_micron_event_mae_pct":-1.7,"hanmi_event_mae_pct":-4.4,"kospi_same_context_pct":-0.7,"samsung_relative_underperformance_pp":-1.6,"sk_hynix_relative_underperformance_pp":-3.7,"hanmi_relative_underperformance_pp":-3.7,"samsung_china_dram_exposure":"more_than_one_third","sk_hynix_china_dram_nand_exposure_pct":"30-40","veu_revocation_effective_delay_days":120,"license_policy":"existing operations likely allowed; expansion/upgrade not intended","match_act_targets":["CXMT","YMTC","SMIC","DUV immersion machines","foreign equipment servicing alignment"],"hard_4c_status":"not_confirmed","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"export_control_overlay_watch","notes":"China fab/export-control risk is 4C-watch; hard 4C if license denial or revenue/technology impairment confirms."}
```

## data/sector_taxonomy/score_weight_profiles_round186_r2_loop12_v1.csv 초안

```csv
archetype,confirmed_customer_order,hbm_transition,capacity_bottleneck,advanced_packaging,euv_order,production_readiness,design_lockin,order_to_revenue,gross_margin,price_path_alignment,event_penalty,china_labor_export_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
MEMORY_HBM4_CAPACITY_LEADER,+5,+5,+5,+5,+5,+5,+5,+5,+5,+5,-1,+4,+5,+4,SK Hynix is aligned Stage 3 but current state is 4B-watch.
HBM_CATCHUP_FOUNDRY_TURNAROUND,+5,+5,+4,+4,+3,+5,+4,+5,+5,+4,-3,+5,+5,+4,Samsung is Stage 2 until volume/margin and labor/export-control risk clear.
HBM_BONDER_EQUIPMENT_ORDER,+5,+5,+5,+4,+1,+4,+3,+5,+5,+5,-4,+4,+5,+4,Hanmi confirmed order is good, but unconfirmed customer rumor gets 4B penalty.
SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER,+3,+2,+2,+3,+0,+3,+5,+5,+4,+3,-5,+2,+4,+4,Gaonchips design win needs tape-out, mass production and revenue.
AI_DEVICE_COMPONENT_OPTIONALITY,+3,+2,+2,+2,+0,+3,+3,+5,+4,+4,-5,+2,+5,+3,LG Innotek Apple AI/lidar optionality needs actual volume and margin.
DISPLAY_LCD_EXIT_OLED_TURNAROUND,+2,+0,+1,+0,+0,+3,+1,+4,+5,+3,-4,+2,+4,+4,LG Display LCD exit/loss narrowing is Stage 2 until OLED profit/FCF confirm.
CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF,+3,+2,+3,+2,+0,+3,+2,+4,+4,+3,-5,+5,+5,+4,Jusung/Mirae relief is not Green due China concentration/export-control risk.
GEOPOLITICAL_EXPORT_CONTROL_OVERLAY,+0,+0,+0,+0,+0,+0,+0,+0,+0,+3,0,+5,+4,+5,China fab VEU revocation and MATCH Act are 4C-watch overlays.
```

---

# 이번 R2 Loop 12 결론

```text
1. SK Hynix는 R2 Stage 3 성공 benchmark다.
   하지만 지금은 신규 Green보다 4B-watch가 맞다.

2. Samsung은 HBM4/foundry catch-up Stage 2다.
   HBM4/Nvidia/AMD evidence는 좋지만, labor strike와 China fab export-control이 Green을 막는다.

3. Hanmi는 HBM bonder Stage 2다.
   confirmed SK Hynix order는 좋지만, Micron 미확정 보도 +22%는 4B다.

4. Gaonchips는 AI design-house Stage 2다.
   design win은 매출이 아니므로 tape-out, 양산, revenue 전 Green 금지다.

5. LG Innotek은 Apple AI / lidar optionality Stage 2다.
   실제 iPhone volume, camera-module ASP, lidar ramp 전에는 event premium이다.

6. LG Display는 LCD exit / OLED turnaround Stage 2다.
   적자 축소와 LCD 매각은 좋지만, 지속 OLED 이익과 FCF 전 Stage 3는 아니다.

7. Jusung/Mirae는 CXMT relief event다.
   China customer concentration과 export-control durability가 RedTeam이다.

8. export-control basket은 hard 4C는 아니지만 강한 4C-watch다.
   license denial, China fab upgrade block, revenue impairment가 확인되면 hard 4C로 승격한다.
```

한 문장으로 압축하면:

> **R2에서 진짜 Stage 3는 “AI·HBM·전자부품 수혜가 있다”가 아니라, 고객 주문·세대전환·capacity bottleneck·장비/패키징 발주·출하·마진·EPS revision이 실제 가격경로로 닫히고, labor·China fab·export-control·rumor 리스크를 통과하는 순간이다.**

* [Reuters](https://www.reuters.com/world/asia-pacific/ai-boom-puts-sk-hynix-cusp-1-trillion-market-value-2026-05-14/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/world-at-work/samsung-electronics-its-south-korean-union-resume-pay-talks-strike-risks-loom-2026-05-18/?utm_source=chatgpt.com)
* [월스트리트저널](https://www.wsj.com/articles/hanmi-semiconductor-climbs-after-media-reports-of-possible-deal-with-micron-e85398fb?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/technology/artificial-intelligence/samsung-electronics-wins-cutting-edge-ai-chip-order-japans-preferred-networks-2024-07-09/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/lg-innotek-take-stake-lidar-maker-aeva-part-50-million-deal-2025-07-29/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/markets/deals/lg-display-agrees-sale-chinese-lcd-plant-15-bln-2024-09-26/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/technology/chinese-chip-firms-say-they-can-withstand-new-us-export-curbs-2024-12-03/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/china/shares-samsung-sk-hynix-drop-after-us-makes-it-harder-make-chips-china-2025-09-01/?utm_source=chatgpt.com)

[1]: https://www.wsj.com/world/asia/sk-hynixs-ai-related-memory-chips-sold-out-for-year-aba56345?utm_source=chatgpt.com "SK Hynix's AI-Related Memory Chips Sold Out for Year"
[2]: https://www.reuters.com/world/asia-pacific/samsung-start-production-hbm4-chips-next-month-nvidia-supply-source-says-2026-01-25/?utm_source=chatgpt.com "Samsung to start production of HBM4 chips next month for Nvidia supply, source says"
[3]: https://www.wsj.com/articles/south-korean-chip-shares-rally-as-ai-frenzy-persists-260f9996?utm_source=chatgpt.com "South Korean Chip Shares Rally as AI Frenzy Persists"
[4]: https://www.reuters.com/technology/artificial-intelligence/samsung-electronics-wins-cutting-edge-ai-chip-order-japans-preferred-networks-2024-07-09/?utm_source=chatgpt.com "Samsung Electronics wins cutting-edge AI chip order from Japan's Preferred Networks"
[5]: https://www.wsj.com/articles/lg-innotek-shares-rally-tracking-apple-s-ai-driven-gains-6e193cc3?utm_source=chatgpt.com "LG Innotek Shares Rally, Tracking Apple's AI-Driven Gains"
[6]: https://www.reuters.com/technology/lg-display-reports-q2-loss-weak-demand-panels-2024-07-25/?utm_source=chatgpt.com "LG Display shrinks quarterly loss on Apple, Olympics demand"
[7]: https://www.reuters.com/technology/chinese-chip-firms-say-they-can-withstand-new-us-export-curbs-2024-12-03/?utm_source=chatgpt.com "Chinese chip firms say they can withstand new US export curbs"
[8]: https://www.reuters.com/world/china/shares-samsung-sk-hynix-drop-after-us-makes-it-harder-make-chips-china-2025-09-01/?utm_source=chatgpt.com "Shares in Samsung, SK Hynix drop after US makes it harder to make chips in China"
