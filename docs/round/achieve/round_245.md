순서상 이번은 **R2 Loop 11 — AI·반도체·전자부품 가격경로 검증 라운드**다.

이번 R2 Loop 11은 HBM 대장 반복을 줄이되, benchmark는 남기고, **HBM capacity winner, Samsung catch-up, HBM bonder 장비, China/CXMT 노출 장비주, 디자인하우스, 정책 foundry, 장비 spin-off, export-control/IP leak RedTeam**을 같이 본다.

```text
round = R2 Loop 11
round_id = round_173
large_sector = AI_SEMICONDUCTOR_ELECTRONICS
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = false
```

이번에도 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉 OHLC 전체 구간은 안정적으로 확보하지 못했다. 대신 Reuters / WSJ / MarketWatch가 제공한 **가격 anchor, 이벤트 수익률, 계약금액, CAPEX, 정책금액, 시장점유율, 리스크 지표**로 계산 가능한 값만 계산했다. 30D/90D/180D full OHLC가 없는 항목은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R2 = AI·반도체·전자부품
```

R2의 Stage 3는 “AI 반도체 수혜”가 아니다. **고객 주문·HBM 세대 전환·CAPA 병목·장비 발주·마진·EPS revision·가격경로**가 같이 맞는 순간이다.

---

# 2. 대상 canonical archetype

```text
MEMORY_HBM_CAPACITY_LEADER
HBM_EUV_ADVANCED_PACKAGING_CAPEX
HBM_CATCHUP_EXECUTION
FOUNDRY_TURNAROUND_CONTRACT
HBM_BONDER_EQUIPMENT
CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF
SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER
POLICY_FOUNDRY_EVENT
SEMICONDUCTOR_EQUIPMENT_SPINOFF_OPTIONALITY
GEOPOLITICAL_EXPORT_CONTROL_OVERLAY
SEMICONDUCTOR_IP_LEAK_REDTEAM
PRICE_ONLY_RALLY
```

---

# 3. deep sub-archetype

```text
HBM leader:
- SK Hynix
- HBM / advanced DRAM
- ASML EUV 11.95T won order
- advanced packaging 19T won plant
- AI memory capacity bottleneck
- market-cap milestone / 4B crowding

Samsung catch-up:
- Samsung Electronics
- $16.5B foundry contract
- AMD HBM4 / DDR5 MoU
- HBM share gap vs SK Hynix
- strike / labor disruption
- China fab export-control / IP leak RedTeam

HBM equipment:
- Hanmi Semiconductor
- TSV-TC bonder / HBM packaging equipment
- SK Hynix confirmed contract
- Micron unconfirmed media report
- 4B rumor risk

China/CXMT equipment suppliers:
- Jusung Engineering
- Mirae Corp
- CXMT exclusion relief
- China-bound revenue
- export-control uncertainty

Design house:
- Gaonchips
- Preferred Networks AI chip
- Samsung 2nm GAA / advanced packaging
- design win vs tape-out / production / revenue

Policy foundry:
- DB HiTek
- public-private 40nm 12-inch foundry
- automotive / data-center legacy chips
- defense semiconductor localization

Equipment spin-off:
- Hanwha Precision Machinery exposure via Hanwha Aerospace
- HBM equipment optionality
- spin-off / valuation unlock vs order/revenue

RedTeam:
- U.S. China-fab equipment authorization revocation
- Samsung/SK China output exposure
- Hana Micron / Hanmi collateral selloff
- Samsung DRAM IP leak to CXMT
```

---

# 4. 국장 신규 후보 case

## Case A — SK하이닉스 `structural_success + 4B-watch`

```text
symbol = 000660
case_type = structural_success + 4B-watch
archetype = MEMORY_HBM_CAPACITY_LEADER / HBM_EUV_ADVANCED_PACKAGING_CAPEX
```

SK하이닉스는 R2에서 여전히 가장 깨끗한 Stage 3 benchmark다. 다만 이번 Loop 11에서는 “또 SK하이닉스 좋다”가 아니라, **Stage 3 성공 후 4B로 어떻게 넘어가는지**를 보는 기준점으로 둔다. SK하이닉스는 2026년 3월 ASML EUV 장비 11.95조 원, 약 79.7억 달러 주문을 공시했고, Reuters는 이 주문이 HBM과 advanced DRAM 생산에 쓰일 것으로 보도했다. 같은 기사에서 SK하이닉스 주가는 5.7% 상승했다. 이후 2026년 4월에는 AI memory 수요 대응을 위해 19조 원, 약 128.5억 달러 규모 advanced packaging 공장 투자를 발표했다. ([Reuters][1])

### stage date

```text
Stage 1:
2024년 상반기
- AI server / HBM demand
- old commodity memory frame break

Stage 2:
2024-06-25
- HBM dominance
- DRAM price upcycle
- EPS revision
- stage3 candidate anchor = 222,000원

Stage 3:
2024-06-25 후보
- HBM 지배력 + EPS revision + 가격경로 반응

추가 Stage 3 validation:
2026-03-24
- ASML EUV tools 11.95T won / $7.97B order
- by 2027-12-31
- shares +5.7%

추가 Stage 3 validation:
2026-04-22
- advanced packaging plant 19T won / $12.85B
- HBM / AI memory packaging capacity

Stage 4B:
2026-05-14
- 2025년 +274%
- 2026년 +200% 이상
- market cap 약 $942B
- 1조 달러 근접
```

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch / Reuters reported price and return anchors

stage3_price:
222,000원

ASML_EUV_order:
11.95T won / $7.97B

ASML_EUV_event_MFE:
+5.7%

estimated_EUV_tools:
about 30 machines

advanced_packaging_plant_investment:
19T won / $12.85B

reported_return_2025:
+274%

reported_return_2026_to_2026-05-14:
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
```

### alignment

```text
score_price_alignment = aligned
rerating_result = true_rerating
stage_failure_type = green_success_now_4B_watch
```

---

## Case B — 삼성전자 `success_candidate + labor/export/IP 4C-watch`

```text
symbol = 005930
case_type = success_candidate + 4C-watch
archetype = HBM_CATCHUP_EXECUTION / FOUNDRY_TURNAROUND_CONTRACT
```

삼성전자는 R2에서 가장 큰 “좋은 Stage 2지만 아직 Green은 아닌” 케이스다. 2025년 7월 삼성전자는 165억 달러 규모 foundry 계약을 체결했고, 주가는 3.5% 상승했다. Reuters는 고객과 세부 조건이 2033년 말 계약 완료 전까지 비공개라고 보도했으며, 이후 Tesla 관련 보도가 시장에 붙었다. 2026년 3월에는 AMD와 AI memory 공급 및 foundry 협력 가능성을 포함한 MoU를 체결했고, Samsung HBM4가 AMD Instinct MI455X에 들어갈 수 있다는 구조가 제시됐다. ([Reuters][2])

하지만 동시에 삼성전자에는 강한 4C-watch가 붙는다. 2026년 5월 삼성 노조가 45,000명 이상 참여 가능한 18일 파업을 위협하자 삼성전자 주가는 5월 15일 최대 9.3% 하락했고, 이후 법원 결정으로 일부 우려가 완화되자 5월 18일 3.88% 반등했다. 또 미국의 중국 fab 장비허가 취소로 Samsung은 2025년 9월 2.3% 하락했고, Reuters는 Samsung DRAM 생산의 3분의 1 이상이 중국에서 나온다고 보도했다. ([Reuters][3])

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
- shares +3.5%
- contract through end-2033

Stage 2 추가:
2026-03-18
- AMD MoU on AI memory
- Samsung HBM4 for AMD Instinct MI455X
- possible foundry partnership

Stage 3:
보류
- HBM4 volume shipment
- Nvidia/AMD/Tesla revenue recognition
- foundry yield / margin / EPS revision 확인 전 Green 금지

Stage 4B:
HBM/foundry catch-up narrative로 valuation이 먼저 확장되면 후보

Stage 4C-watch:
2025-09-01
- U.S. revokes China equipment authorizations
- Samsung -2.3%

Stage 4C-watch:
2026-05-15
- strike risk
- Samsung shares down as much as -9.3%

4C relief:
2026-05-18
- court ruling relief
- shares +3.88%
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported contract / event-return / strike-risk anchors

stage3_price:
N/A

foundry_contract_value:
$16.5B

foundry_contract_event_return:
+3.5%

foundry_contract_duration:
through end-2033

AMD_MoU:
HBM4 for Instinct MI455X
DDR5 for EPYC
possible foundry partnership

Samsung_HBM_market_share_context:
22%

SK_Hynix_HBM_market_share_context:
57%

export_control_event_MAE:
-2.3%

Samsung_China_DRAM_exposure:
> one-third

strike_event_MAE:
-9.3%

court_ruling_relief_return:
+3.88%

KOSPI_same_context_May_18:
+0.31%

relative_outperformance_May_18:
3.88 - 0.31
= +3.57pp

possible_strike_workers:
45,000+

possible_direct_loss_per_day:
up to 1T won

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate + 4C_watch
rerating_result = HBM_catchup_foundry_turnaround_watch
stage_failure_type = stage2_watch_until_volume_margin_confirm
```

---

## Case C — 한미반도체 `success_candidate + rumor 4B-watch`

```text
symbol = 042700
case_type = success_candidate + 4B-watch
archetype = HBM_BONDER_EQUIPMENT
```

한미반도체는 HBM equipment Stage 2 후보로 남길 수 있다. WSJ는 한미반도체가 SK하이닉스로부터 214.8억 원 계약을 확보했고, 최근 deal 총액이 약 2,000억 원이라고 보도했다. 하지만 같은 기사에서 Micron 공급 가능성 보도만으로 한미반도체 주가가 장중 최대 22% 상승해 139,100원을 기록했다고 보도했다. Micron과 한미반도체 모두 당시 보도를 확인하지 않았다. 즉 confirmed SK Hynix order와 unconfirmed Micron rumor를 분리해야 한다. ([월스트리트저널][4])

### stage date

```text
Stage 1:
2023~2024
- HBM packaging equipment
- TSV-TC bonder
- SK Hynix supply-chain exposure

Stage 2:
2024-03
- SK Hynix contract 21.48B won
- recent deals total around 200B won
- confirmed customer order

Stage 3:
조건부 후보
- confirmed customer order
- HBM equipment exposure
- order-to-revenue, margin, EPS 확인 필요

Stage 4B:
2024-03-28
- Micron 미확정 보도만으로 장중 +22%
- 139,100원
- KOSPI -0.3%

Stage 4C:
Micron deal not confirmed, customer concentration, HBM capex pause, export-control risk
```

### 실제 가격경로 검증

```text
price_data_source:
WSJ reported price and contract anchors

stage3_price:
price_data_unavailable_after_deep_search

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

export_control_event_MAE:
-4.4% on 2025-09-01

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = aligned_candidate + 4B_watch
rerating_result = HBM_equipment_rerating_candidate
stage_failure_type = confirmed_order_good_but_unconfirmed_customer_rumor_4B
```

---

## Case D — 주성엔지니어링 / 미래산업 `China-CXMT supplier relief / export-control watch`

```text
symbols = 036930 / 025560
case_type = event_premium + 4C-watch
archetype = CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF
```

주성엔지니어링과 미래산업은 R2에서 “중국향 장비 exposure”를 볼 때 좋은 RedTeam 케이스다. 2024년 12월 미국의 새 중국 반도체 수출규제에서 CXMT가 entity list에서 제외되자, Reuters는 주성엔지니어링이 전일 거의 7% 하락한 뒤 오전장 7.7% 상승했다고 보도했다. 미래산업은 2024년 상반기 매출의 약 15%가 CXMT에서 나왔고, 그해 CXMT와 약 90억 원 공급계약을 체결했으며, 주가는 오전장 1.4% 상승했다. 이건 구조적 Stage 3가 아니라 **export-control relief event**다. ([Reuters][5])

### stage date

```text
Stage 1:
2024
- 중국 memory capex
- CXMT equipment demand
- Korean equipment supplier exposure

Stage 2:
2024-12-03
- CXMT excluded from U.S. entity list
- short-term relief for Korean equipment suppliers

Stage 3:
없음
- China-bound relief만으로 Green 금지
- non-China customer diversification, revenue conversion, margin, export-control durability 필요

Stage 4B:
CXMT exclusion relief로 장비주가 먼저 반등하면 후보

Stage 4C:
next export-control wave, CXMT restriction, China capex cut, receivables risk, margin pressure
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters China export-control / CXMT relief anchor

stage3_price:
N/A

Jusung_previous_session_MAE:
nearly -7%

Jusung_relief_MFE:
+7.7%

Mirae_Corp_relief_MFE:
+1.4%

Mirae_previous_session_gain:
+7%

Mirae_CXMT_revenue_share_1H2024:
about 15%

Mirae_CXMT_supply_deals_2024:
about 9B won / $6.41M

China_equipment_imports_9M2024:
$24.12B

China_equipment_import_growth:
+33% approximately

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium / 4C_watch
rerating_result = China_equipment_relief_watch
stage_failure_type = stage2_relief_not_green
```

---

## Case E — 가온칩스 `success_candidate / design-win Stage 2`

```text
symbol = 399720
case_type = success_candidate / insufficient_price_data
archetype = SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER
```

가온칩스는 R2 디자인하우스 Stage 2 후보로 유지한다. Samsung은 일본 Preferred Networks의 AI chip을 2nm GAA와 advanced packaging으로 생산하는 첫 공개 수주를 확보했고, 이 칩 설계는 가온칩스가 맡았다. Reuters는 이 칩이 generative AI와 large language model용 high-performance computing hardware에 쓰일 것이라고 보도했다. 하지만 주문 규모는 공개되지 않았고, 가온칩스 매출·마진·양산 전환은 확인되지 않았다. ([Reuters][6])

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

Stage 3:
없음
- design win만으로 Green 금지
- tape-out, mass production, revenue recognition, gross margin 확인 필요

Stage 4B:
AI chip design house theme으로 주가가 먼저 급등하면 후보

Stage 4C:
tape-out delay, yield issue, customer cancellation, no revenue conversion
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters evidence source

stage3_price:
N/A

stage2_price:
price_data_unavailable_after_deep_search

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

reason:
- Reuters는 가온칩스 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq raw OHLC unavailable in this pass.
```

### alignment

```text
score_price_alignment = unknown_insufficient_evidence
rerating_result = design_win_watch
stage_failure_type = stage2_evidence_not_green
```

---

## Case F — DB하이텍 / 정책 foundry `event_premium / policy Stage 1~2`

```text
symbol = 000990
case_type = event_premium / policy_watch
archetype = POLICY_FOUNDRY_EVENT
```

DB하이텍은 R2 정책 foundry 후보로 볼 수 있지만, Green은 아니다. 2025년 12월 한국 정부는 4.5조 원, 약 30.6억 달러 규모의 12인치 40nm public-private foundry 설립을 검토한다고 밝혔다. Reuters는 자동차·데이터센터용 legacy chip 개발과 방산 반도체 국산화가 목적이고, 방산 반도체는 수입 의존도가 99%라고 보도했다. 정부는 Samsung과 DB HiTek 같은 foundry 업체와 협의할 예정이라고 밝혔다. ([Reuters][7])

### stage date

```text
Stage 1:
2025-12-10
- 4.5T won public-private foundry 검토
- 12-inch / 40nm facility
- automotive / data-center legacy chip
- defense semiconductor localization

Stage 2:
약한 Stage 2
- Samsung / SK Hynix / DB HiTek consultation
- domestic foundry policy beneficiary candidate

Stage 3:
없음
- government consultation만으로 Green 금지
- funded capex, company-level order, utilization, customer commitment, margin 확인 필요

Stage 4B:
정책 foundry 테마로 DB HiTek / fabless basket이 먼저 급등하면 후보

Stage 4C:
예산 미반영, 민간 부담 과다, customer 부재, utilization failure
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters policy evidence source

stage3_price:
N/A

stage1_price:
price_data_unavailable_after_deep_search

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

reason:
- Reuters는 DB HiTek 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq raw OHLC unavailable in this pass.
```

### alignment

```text
score_price_alignment = event_premium / policy_watch
rerating_result = policy_foundry_watch
stage_failure_type = stage1_attention_only
```

---

## Case G — Hanwha Precision Machinery spin-off `event_premium / HBM equipment optionality`

```text
symbol = 012450 parent exposure
case_type = event_premium / corporate_action_watch
archetype = SEMICONDUCTOR_EQUIPMENT_SPINOFF_OPTIONALITY
```

Hanwha Aerospace의 Hanwha Precision Machinery spin-off는 R2 반도체 장비 optionality를 보여주지만 Green은 아니다. Reuters는 Hanwha Aerospace가 Hanwha Precision Machinery와 Hanwha Vision을 분리해 industrial solutions company로 묶겠다고 발표했고, Hanwha Precision의 HBM 장비 개발 가능성을 언급했다고 보도했다. 하지만 발표 전 media report로 주가가 15% 이상 오른 뒤, 공식 발표 당일에는 profit-taking으로 8% 하락했다. ([Reuters][8])

### stage date

```text
Stage 1:
2024-04-02
- Hanwha Precision Machinery spin-off media report
- HBM equipment optionality
- valuation unlock 기대

Stage 2:
2024-04-05
- Hanwha Aerospace announces spin-off
- Hanwha Precision Machinery + Hanwha Vision into industrial solutions company
- industrial solutions value about 2T won
- defence business value about 10T won

Stage 3:
없음
- spin-off / valuation-unlock만으로 Green 금지
- HBM equipment order, revenue, margin, listed vehicle economics 확인 필요

Stage 4B:
2024-04-02~05
- media report +15% 이상
- formal announcement -8%
```

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

defence_business_estimated_value:
10T won

revenue_contribution_from_spun_units:
about 16%

parent_market_cap_context:
about 11T won

industrial_plus_defence_estimate:
12T won

estimated_sum_vs_parent_market_cap:
12T / 11T - 1
= +9.1%

MFE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium
rerating_result = HBM_equipment_corporate_action_watch
stage_failure_type = corporate_action_not_green
```

---

## Case H — export-control / IP-leak RedTeam basket `4C-watch`

```text
symbols = 005930 / 000660 / 067310 / 042700 / equipment-supplier basket
case_type = 4C-watch
archetype = GEOPOLITICAL_EXPORT_CONTROL_OVERLAY / SEMICONDUCTOR_IP_LEAK_REDTEAM
```

이번 R2 Loop 11의 RedTeam 핵심은 export-control과 IP leakage다. 2025년 9월 미국이 Samsung과 SK Hynix 중국 fab에 대한 장비 반입 authorization을 취소하자 Samsung은 2.3%, SK Hynix는 4.4%, Hana Micron은 1.7%, Hanmi Semiconductor는 4.4% 하락했다. Reuters는 Samsung DRAM의 3분의 1 이상, SK Hynix DRAM/NAND의 30~40%가 중국에 있다고 보도했다. ([Reuters][9])

또 2025년 12월에는 한국 검찰이 Samsung의 10나노 DRAM 공정 기술이 CXMT로 유출된 혐의로 10명을 기소했다. Reuters는 이 기술 개발에 Samsung이 1.6조 원을 투입했고, 손실 추정이 수십조 원에 이를 수 있다고 보도했다. 이는 R2에서 hard 4C까지는 아니더라도, **기술 경쟁력·중국 추격·IP 신뢰 gate**를 강하게 올려야 하는 이유다. ([Reuters][10])

### stage date

```text
Stage 1:
2025년
- U.S.-China chip export control
- China fab exposure
- China memory catch-up / CXMT

Stage 2:
없음
- negative RedTeam event

Stage 3:
없음

Stage 4C-watch:
2025-09-01
- U.S. revokes China equipment authorizations
- Samsung -2.3%
- SK Hynix -4.4%
- Hana Micron -1.7%
- Hanmi Semiconductor -4.4%

추가 4C-watch:
2025-12-26
- Samsung DRAM process leak charges
- CXMT alleged recipient
- 1.6T won development cost
- tens of trillions won loss estimate
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters export-control and IP-leak anchors

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

IP_leak_development_cost:
1.6T won

estimated_losses:
at least tens of trillions of won

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = export_control_and_IP_leak_4C_watch
stage_failure_type = 4C_watch_not_hard_4C
```

---

# 5. 이번 R2 case별 요약표

| case                          | 분류                           |                                                                          실제 가격검증 | alignment                  |
| ----------------------------- | ---------------------------- | -------------------------------------------------------------------------------: | -------------------------- |
| SK Hynix                      | structural_success + 4B      | EUV order +5.7%, 11.95T won; advanced packaging 19T won; 2025 +274%, 2026 +200%+ | aligned / now 4B           |
| Samsung Electronics           | success_candidate + 4C-watch |    $16.5B foundry +3.5%; strike -9.3%; court relief +3.88%; export control -2.3% | Stage 2 + watch            |
| Hanmi Semiconductor           | success_candidate + 4B       |     SKH contract 21.48B won; Micron rumor +22% to 139,100원; export control -4.4% | confirmed order + rumor 4B |
| Jusung / Mirae                | event premium + 4C-watch     |                  Jusung -7% then +7.7%; Mirae CXMT revenue 15%, contracts 9B won | China relief               |
| Gaonchips                     | success_candidate            |              Preferred Networks AI chip, Samsung 2nm GAA, order size undisclosed | design win Stage 2         |
| DB HiTek / policy foundry     | event premium                |                     4.5T won 40nm 12-inch foundry, defense import dependency 99% | policy Stage 1~2           |
| Hanwha Precision spin-off     | event premium                |                            media +15%, announcement -8%, industrial value 2T won | corporate action           |
| Export-control/IP leak basket | 4C-watch                     |         Samsung -2.3%, SKH -4.4%, Hana -1.7%, Hanmi -4.4%; IP leak 1.6T won tech | RedTeam                    |

---

# 6. score-price alignment 판정

```text
aligned:
- SK Hynix

success_candidate:
- Samsung Electronics
- Hanmi Semiconductor
- Gaonchips

event_premium:
- Jusung / Mirae CXMT exclusion relief
- DB HiTek / policy foundry
- Hanwha Precision Machinery spin-off

price_moved_without_evidence:
- Hanmi Micron unconfirmed report
- Hanwha Precision spin-off media rally
- policy foundry rally if company order/utilization absent

evidence_good_but_price_failed:
- LS Electric-style grid case는 R1에 있었고, 이번 R2에서는 Samsung / Hanmi는 price failed보다 watch 성격
- Samsung strike shock은 negative price evidence

thesis_break_watch:
- export-control basket
- Samsung strike / labor disruption
- Samsung-CXMT IP leak
- China/CXMT supplier dependency

4B-watch:
- SK Hynix trillion-dollar proximity
- Hanmi Micron rumor +22%
- Hanwha Precision spin-off media +15%
- Samsung foundry/HBM catch-up if revenue보다 price 먼저 감

4C-watch:
- Samsung labor strike
- China fab export-control
- CXMT IP leakage
- China customer concentration in equipment suppliers

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
EUV_or_advanced_packaging_capacity +5
product_specificity +4
order_to_revenue_conversion +5
gross_margin_visibility +5
customer_diversification +4
price_path_alignment +5
```

### 왜 올리나

SK Hynix는 HBM·EUV·advanced packaging이 실제 capacity bottleneck과 가격경로로 연결됐다. Hanmi도 confirmed SK Hynix order가 있는 구간은 Stage 2~3 후보가 될 수 있다. Samsung도 foundry/HBM catch-up evidence가 있지만, volume shipment와 margin confirmation 전에는 Stage 2다.

## 내릴 축

```text
AI_keyword_only -5
MOU_or_policy_only -5
unconfirmed_media_report -5
design_win_without_revenue -4
policy_foundry_without_order -5
corporate_action_without_order -4
China_customer_dependency -5
export_control_exposure -5
IP_leak_risk -5
labor_disruption_risk -5
price_rally_before_confirmation -5
```

### 왜 내리나

Hanmi의 Micron news는 미확정 보도였고, Hanwha Precision spin-off는 HBM equipment optionality지만 corporate action이다. DB HiTek 정책 foundry는 회사 단위 order가 아니다. Samsung은 좋은 계약과 MoU가 있어도 strike, China fab, IP leak risk가 동시에 붙는다.

## Green gate 강화 조건

```text
R2 Stage 3-Green 필수:
1. company-level customer evidence
2. product-specific exposure
3. order / shipment / contract / revenue path 확인
4. gross margin 또는 OPM 개선
5. EPS/FCF revision
6. capacity bottleneck 또는 supply allocation
7. customer diversification
8. export-control / China fab / labor / IP leakage / accounting trust 통과
9. 가격경로가 evidence 이후 따라옴

금지:
AI 이름만 있음
HBM rumor만 있음
미확정 고객 보도
design win만 있음
정책 foundry만 있음
spin-off / corporate action만 있음
China customer concentration만 있음
```

## 4B 조기감지 조건

```text
4B-watch:
Stage 3 이후 3배 이상 상승
시총 milestone이 headline화
미확정 고객 다변화 보도에 +20% 이상 급등
spin-off / corporate-action event가 실적보다 먼저 가격화
AI capex consensus가 한쪽으로 몰림
좋은 뉴스에도 주가 반응이 둔화되거나 악재에 민감해짐

4B-elevated:
SK Hynix처럼 1조 달러 근접
Hanmi처럼 미확정 고객 보도만으로 +22%
Hanwha Precision처럼 media report +15% 후 announcement -8%
Samsung처럼 contract/MoU는 있으나 labor/export/IP risk가 동시에 커짐
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

이번 R2 Loop 11에서는 hard 4C를 억지로 확정하지 않는다. 다만 **Samsung strike**, **China fab export-control**, **Samsung/CXMT IP leak**, **China customer concentration**은 모두 강한 4C-watch다.

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

## docs/round/round_173.md 요약

```md
# R2 Loop 11. AI Semiconductor Electronics Price Validation

이번 라운드는 R2 Loop 11 price-validation 라운드다.

핵심 결론:
- SK Hynix remains the R2 structural success benchmark but now requires 4B-watch. ASML EUV order was 11.95T won / $7.97B and shares rose +5.7%; advanced packaging plant investment was 19T won / $12.85B. 2025 return +274%, 2026 >+200%, market cap around $942B.
- Samsung Electronics is Stage 2 success_candidate, not Green. $16.5B foundry deal drove +3.5%; AMD HBM4/DDR5 MoU validates catch-up. But strike risk, China-fab export-control and IP-leak RedTeam require 4C-watch.
- Hanmi Semiconductor is HBM equipment Stage 2 candidate. Confirmed SK Hynix contract was 21.48B won, but unconfirmed Micron media report drove +22% to 139,100 won, making it 4B-watch.
- Jusung Engineering / Mirae Corp are China-CXMT supplier relief cases. CXMT exclusion from entity list drove Jusung +7.7% after nearly -7%; Mirae had about 15% 1H 2024 revenue from CXMT and about 9B won supply deals. This is relief, not Green.
- Gaonchips is system-semi design-win Stage 2. Preferred Networks AI chip uses Samsung 2nm GAA and advanced packaging, but order size, mass production, revenue and margin are unconfirmed.
- DB HiTek / public-private foundry is policy Stage 1~2. Proposed foundry is 4.5T won, 12-inch, 40nm, but company-level orders and utilization are not confirmed.
- Hanwha Precision Machinery spin-off is HBM equipment optionality but event premium. Media report drove parent +15%+, announcement day -8%; order/revenue/margin not confirmed.
- Export-control/IP-leak basket is 4C-watch. Samsung -2.3%, SK Hynix -4.4%, Hana Micron -1.7%, Hanmi -4.4% on China equipment authorization revocation; Samsung 1.6T won DRAM technology leak case raises IP RedTeam.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 173 R2 Loop 11 AI Semiconductor Price Validation

## 반영 내용
- R2 Loop 11 price-validation 라운드를 추가했다.
- HBM leader, Samsung catch-up/foundry, HBM bonder equipment, China-CXMT equipment supplier relief, system-semi design house, policy foundry, HBM equipment spin-off, export-control/IP-leak RedTeam을 비교했다.
- Reuters/WSJ/MarketWatch anchors로 가능한 MFE/MAE 및 contract/capex/policy/risk metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- confirmed customer order, HBM generation transition, EUV/advanced packaging capacity, product specificity, customer diversification, price-path alignment 가중치 강화
- AI keyword-only, unconfirmed media report, design win without revenue, policy foundry without order, corporate action without order, China customer dependency, export-control/IP-leak risk 감점 강화
- R2 4B-watch와 4C-watch 민감도 강화
```

## case row 초안

```jsonl
{"case_id":"r2_loop11_sk_hynix_euv_packaging_4b","symbol":"000660","company_name":"SK Hynix","case_type":"structural_success","primary_archetype":"MEMORY_HBM_CAPACITY_LEADER","stage3_date":"2024-06-25","stage4b_date":"2026-05-14","price_validation":{"price_data_source":"MarketWatch/Reuters reported anchors","stage3_price":222000,"asml_euv_order_krw_trn":11.95,"asml_euv_order_usd_bn":7.97,"asml_euv_event_mfe_pct":5.7,"estimated_euv_tools":30,"advanced_packaging_investment_krw_trn":19,"advanced_packaging_investment_usd_bn":12.85,"reported_return_2025_pct":274,"reported_return_2026_ytd_pct":200,"minimum_compounded_return_from_2025_start_pct":1022,"market_cap_mfe_minimum_pct":842,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"aligned","rerating_result":"true_rerating","notes":"HBM/EUV/advanced packaging confirms structural success; current state is 4B-watch after massive MFE."}
{"case_id":"r2_loop11_samsung_hbm_foundry_strike_export_ip_watch","symbol":"005930","company_name":"Samsung Electronics","case_type":"success_candidate","primary_archetype":"HBM_CATCHUP_EXECUTION","stage2_date":"2025-07-28/2026-03-18","stage4c_date":"2025-09-01/2026-05/2025-12-26","price_validation":{"price_data_source":"Reuters contract/event/strike/export/IP anchors","stage3_price":null,"foundry_contract_usd_bn":16.5,"foundry_contract_event_return_pct":3.5,"foundry_contract_duration":"through_end_2033","amd_mou":"HBM4 for Instinct MI455X, DDR5 for EPYC, possible foundry partnership","samsung_hbm_market_share_pct":22,"sk_hynix_hbm_market_share_pct":57,"export_control_event_mae_pct":-2.3,"china_dram_exposure":"more_than_one_third","strike_event_mae_pct":-9.3,"court_ruling_relief_return_pct":3.88,"kospi_same_context_pct":0.31,"relative_outperformance_may18_pp":3.57,"possible_strike_workers":45000,"possible_direct_loss_per_day_krw_trn":1,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_4c_watch","rerating_result":"HBM_catchup_foundry_turnaround_watch","notes":"Samsung has Stage 2 foundry/HBM evidence, but volume/margin/EPS plus labor/export/IP risks must clear before Green."}
{"case_id":"r2_loop11_hanmi_hbm_bonder_confirmed_order_rumor_4b","symbol":"042700","company_name":"Hanmi Semiconductor","case_type":"success_candidate","primary_archetype":"HBM_BONDER_EQUIPMENT","stage2_date":"2024-03","stage4b_date":"2024-03-28","price_validation":{"price_data_source":"WSJ/Reuters reported anchors","stage3_price":null,"confirmed_sk_hynix_contract_krw_bn":21.48,"recent_deals_total_krw_bn":200,"stage4b_peak_price_krw":139100,"stage4b_event_mfe_pct":22,"implied_pre_4b_reference_price_krw":114016,"kospi_same_context_pct":-0.3,"relative_outperformance_pp":22.3,"micron_deal_status":"unconfirmed_media_report","export_control_event_mae_pct":-4.4,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"aligned_candidate_4b_watch","rerating_result":"HBM_equipment_rerating_candidate","notes":"Confirmed SK Hynix order is good Stage 2 evidence; unconfirmed Micron media report is 4B-watch."}
{"case_id":"r2_loop11_jusung_mirae_cxmt_supplier_relief","symbol":"036930/025560","company_name":"Jusung Engineering / Mirae Corp","case_type":"event_premium","primary_archetype":"CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF","stage2_date":"2024-12-03","stage4c_date":"2024-12_watch","price_validation":{"price_data_source":"Reuters China export-control / CXMT relief anchor","stage3_price":null,"jusung_previous_session_mae_pct":-7,"jusung_relief_mfe_pct":7.7,"mirae_relief_mfe_pct":1.4,"mirae_previous_session_gain_pct":7,"mirae_cxmt_revenue_share_1h2024_pct":15,"mirae_cxmt_supply_deals_krw_bn":9,"china_equipment_imports_9m2024_usd_bn":24.12,"china_equipment_import_growth_pct":33,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_4c_watch","rerating_result":"China_equipment_relief_watch","notes":"CXMT exclusion relief is Stage 2 event, not Green; export-control durability and customer diversification required."}
{"case_id":"r2_loop11_gaonchips_pfn_design_win","symbol":"399720","company_name":"Gaonchips","case_type":"success_candidate","primary_archetype":"SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER","stage2_date":"2024-07-09","price_validation":{"price_data_source":"Reuters evidence source","stage3_price":null,"order_size":"not_disclosed","technology":"Samsung 2nm GAA + advanced packaging","customer":"Preferred Networks","end_use":"generative AI / LLM HPC hardware","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"unknown_insufficient_evidence","rerating_result":"design_win_watch","notes":"Design win is Stage 2; tape-out, mass production, revenue and margin required for Stage 3."}
{"case_id":"r2_loop11_db_hitek_policy_foundry","symbol":"000990","company_name":"DB HiTek / policy foundry exposure","case_type":"event_premium","primary_archetype":"POLICY_FOUNDRY_EVENT","stage1_date":"2025-12-10","price_validation":{"price_data_source":"Reuters policy evidence","stage3_price":null,"foundry_project_size_krw_trn":4.5,"foundry_project_size_usd_bn":3.06,"process_node_nm":40,"wafer_size_inch":12,"defense_semiconductor_import_dependency_pct":99,"company_status":"policy_beneficiary_candidate_not_confirmed_order","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_policy_watch","rerating_result":"policy_foundry_watch","notes":"Government foundry consultation is Stage 1/2, not company Green."}
{"case_id":"r2_loop11_hanwha_precision_hbm_equipment_spinoff","symbol":"012450_parent_exposure","company_name":"Hanwha Precision Machinery / Hanwha Aerospace spin-off exposure","case_type":"event_premium","primary_archetype":"SEMICONDUCTOR_EQUIPMENT_SPINOFF_OPTIONALITY","stage2_date":"2024-04-05","stage4b_date":"2024-04-02/2024-04-05","price_validation":{"price_data_source":"Reuters corporate-action/event-return anchor","stage3_price":null,"media_report_event_mfe_pct":15,"formal_announcement_event_mae_pct":-8,"industrial_solutions_estimated_value_krw_trn":2,"industrial_solutions_estimated_value_usd_bn":1.48,"defence_business_estimated_value_krw_trn":10,"revenue_contribution_from_spun_units_pct":16,"parent_market_cap_context_krw_trn":11,"industrial_plus_defence_estimate_krw_trn":12,"estimated_sum_vs_parent_market_cap_pct":9.1,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium","rerating_result":"HBM_equipment_corporate_action_watch","notes":"HBM equipment optionality via spin-off is Stage 2/corporate-action event; order/revenue/margin required before Green."}
{"case_id":"r2_loop11_export_control_ip_leak_redteam","symbol":"005930/000660/067310/042700","company_name":"Samsung/SK Hynix/Hana Micron/Hanmi export-control and IP-leak basket","case_type":"4c_watch","primary_archetype":"GEOPOLITICAL_EXPORT_CONTROL_OVERLAY","stage4c_date":"2025-09-01/2025-12-26","price_validation":{"price_data_source":"Reuters export-control and IP-leak anchors","stage3_price":null,"samsung_mae_1d_pct":-2.3,"sk_hynix_mae_1d_pct":-4.4,"hana_micron_mae_1d_pct":-1.7,"hanmi_mae_1d_pct":-4.4,"kospi_same_context_pct":-0.7,"samsung_relative_underperformance_pp":-1.6,"sk_hynix_relative_underperformance_pp":-3.7,"hanmi_relative_underperformance_pp":-3.7,"samsung_china_dram_exposure":"more_than_one_third","sk_hynix_china_dram_nand_exposure_pct":"30-40","authorization_effective_delay_days":120,"ip_leak_development_cost_krw_trn":1.6,"estimated_losses":"at_least_tens_of_trillions_of_won","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"export_control_and_IP_leak_4C_watch","notes":"Export-control and IP leakage are R2 4C-watch; hard 4C requires production/revenue/competitive impairment confirmation."}
```

## shadow weight row 초안

```csv
archetype,confirmed_order,hbm_transition,capacity_bottleneck,euv_packaging,product_specificity,order_to_revenue,margin_visibility,customer_diversification,price_path_alignment,event_penalty,china_export_ip_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
MEMORY_HBM_CAPACITY_LEADER,+5,+5,+5,+5,+5,+5,+5,+4,+5,-1,+4,+5,+4,SK Hynix is aligned Stage 3 but now requires 4B-watch.
HBM_CATCHUP_EXECUTION,+4,+4,+4,+3,+4,+4,+5,+3,+3,-2,+5,+4,+4,Samsung is Stage 2 until HBM/foundry volume, margin and labor/export risks clear.
FOUNDRY_TURNAROUND_CONTRACT,+5,+2,+3,+3,+4,+4,+5,+3,+3,-3,+4,+4,+4,$16.5B contract helps Samsung but yield/margin/revenue bridge must confirm.
HBM_BONDER_EQUIPMENT,+5,+5,+5,+3,+5,+5,+5,+4,+4,-3,+3,+5,+3,Hanmi confirmed order is good; unconfirmed Micron rumor is 4B risk.
CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF,+3,+2,+3,+2,+4,+4,+4,+2,+2,-4,+5,+5,+4,Jusung/Mirae CXMT relief is event, not Green; customer concentration matters.
SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER,+2,+1,+2,+2,+5,+4,+4,+3,+2,-4,+2,+3,+3,Gaonchips design win needs tape-out, production and revenue.
POLICY_FOUNDRY_EVENT,+1,+0,+2,+1,+2,+1,+2,+1,+1,-5,+2,+4,+3,Policy foundry consultation is not company Green.
SEMICONDUCTOR_EQUIPMENT_SPINOFF_OPTIONALITY,+2,+2,+2,+2,+3,+2,+3,+2,+2,-5,+2,+5,+3,Spin-off optionality requires order book and revenue conversion.
GEOPOLITICAL_EXPORT_CONTROL_OVERLAY,+0,+0,+0,+0,+0,+0,+0,+0,+2,0,+5,+3,+5,China fab authorization loss and IP leak are 4C-watch until production/revenue impact confirms.
```

---

# 이번 R2 Loop 11 결론

R2는 Stage 3를 제대로 잡으면 대형 MFE가 나오지만, **AI라는 말 하나로는 가장 쉽게 오염되는 섹터**다.

```text
1. SK Hynix는 여전히 R2 Stage 3 성공 benchmark다.
   EUV, advanced packaging, HBM capacity가 모두 맞물린다.
   그러나 지금은 신규 Green보다 4B-watch가 중요하다.

2. Samsung Electronics는 HBM/foundry catch-up Stage 2 후보다.
   $16.5B foundry contract와 AMD MoU는 좋지만,
   volume shipment, margin, EPS 전 Green은 아니다.
   strike, China fab, IP leak은 4C-watch다.

3. Hanmi Semiconductor는 confirmed SK Hynix order가 있는 구간은 좋다.
   하지만 Micron 미확정 보도 +22%는 4B-watch다.

4. Jusung / Mirae는 CXMT exclusion relief로 반등했지만,
   China customer concentration과 export-control risk가 남는다.

5. Gaonchips는 design win Stage 2다.
   tape-out, 양산, revenue, margin 전 Stage 3 금지다.

6. DB HiTek policy foundry는 정부정책 Stage 1~2다.
   회사 단위 order / utilization / EPS 전 Green 금지다.

7. Hanwha Precision spin-off는 HBM equipment optionality지만,
   corporate action만으로 Stage 3가 아니다.

8. export-control / IP leak basket은 R2의 핵심 4C-watch다.
   실제 생산·매출·경쟁력 훼손으로 이어지면 hard 4C로 승격한다.
```

한 문장으로 압축하면:

> **R2에서 진짜 Stage 3는 “AI 반도체 수혜”가 아니라, 고객 주문·HBM 세대 전환·CAPA 병목·장비 발주·마진·EPS revision이 실제 가격경로로 이어지는 순간이다.**
> **이번 R2 Loop 11은 SK Hynix 같은 winner는 4B로 관리하고, Samsung·Hanmi·Gaonchips·DB HiTek·Jusung/Mirae 같은 후보는 confirmed order와 rumor/policy/China-risk를 분리하는 라운드다.**

[1]: https://www.reuters.com/world/asia-pacific/sk-hynix-buy-euv-scanners-8-billion-asml-korea-2026-03-24/?utm_source=chatgpt.com "SK Hynix to buy $8 billion in ASML chipmaking tools in largest disclosed order"
[2]: https://www.reuters.com/business/samsung-elec-signs-165-billion-deal-make-chips-global-firm-2025-07-28/?utm_source=chatgpt.com "Samsung Elec signs $16.5 billion deal to make chips for global firm"
[3]: https://www.reuters.com/business/world-at-work/samsung-elecs-union-says-samsung-proposed-unconditional-talks-strike-plan-holds-2026-05-15/?utm_source=chatgpt.com "Samsung's South Korean union sticks to strike plan after talks offer; shares slide"
[4]: https://www.wsj.com/articles/hanmi-semiconductor-climbs-after-media-reports-of-possible-deal-with-micron-e85398fb?utm_source=chatgpt.com "Hanmi Semiconductor Climbs After Media Reports of Possible Deal With Micron"
[5]: https://www.reuters.com/technology/chinese-chip-firms-say-they-can-withstand-new-us-export-curbs-2024-12-03/?utm_source=chatgpt.com "Chinese chip firms say they can withstand new US export curbs"
[6]: https://www.reuters.com/technology/artificial-intelligence/samsung-electronics-wins-cutting-edge-ai-chip-order-japans-preferred-networks-2024-07-09/?utm_source=chatgpt.com "Samsung Electronics wins cutting-edge AI chip order from Japan's Preferred Networks"
[7]: https://www.reuters.com/world/asia-pacific/south-korea-consider-setting-up-31-bln-foundry-grow-local-chip-sector-2025-12-10/?utm_source=chatgpt.com "South Korea to consider setting up $3.1 bln foundry to grow local chip sector"
[8]: https://www.reuters.com/markets/asia/hanwha-aerospace-spin-off-semiconductor-equipment-unit-2024-04-05/?utm_source=chatgpt.com "South Korea's Hanwha Aerospace to spin off industrial solutions businesses from defence"
[9]: https://www.reuters.com/world/china/shares-samsung-sk-hynix-drop-after-us-makes-it-harder-make-chips-china-2025-09-01/?utm_source=chatgpt.com "Shares in Samsung, SK Hynix drop after US makes it harder to make chips in China"
[10]: https://www.reuters.com/world/asia-pacific/south-korea-charges-10-over-alleged-chip-technology-leak-chinas-cxmt-2025-12-26/?utm_source=chatgpt.com "South Korea charges 10 over alleged chip technology leak to China's CXMT"
