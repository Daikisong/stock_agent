순서상 이번은 **R2 Loop 13 — AI·반도체·전자부품 가격경로 검증 라운드**다.

```text
round = R2 Loop 13
round_id = round_199
large_sector = AI_SEMICONDUCTOR_ELECTRONICS
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = false
next_round = R3 Loop 13
```

이번 R2 Loop 13은 SK하이닉스·삼성전자 HBM 대표축을 완전히 버리지는 않되, 반복을 줄이기 위해 **HBM 장비 분사, AI칩 설계 스타트업 합병, KOSDAQ 반도체 검사장비 IPO, 국가 foundry 정책, Nvidia Blackwell 국내 공급, 삼성 노사·HBM lag risk**까지 같이 본다.

이번에도 30D/90D/180D 수정주가 일봉 전체는 안정적으로 확보하지 못했다. 그래서 **보도에서 확인된 event price / event return / 계약·투자·정책 금액 / OP·매출 anchor**만 계산했고, full OHLC가 필요한 칸은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R2 = AI·반도체·전자부품
```

R2에서 진짜 Stage 3는 “HBM”, “AI칩”, “검사장비”, “foundry 정책”, “Nvidia supply chain”이라는 단어가 아니다.

진짜 Stage 3는 **고객 확정 → 양산·인증 → 장비/소재 반복 주문 → 매출 인식 → gross margin / OP / FCF → 중국·노동·수출통제·검증 실패 리스크 통과**까지 닫히는 순간이다.

---

# 2. 대상 canonical archetype

```text
HBM_MEMORY_STRUCTURAL_RERATING_NOW_4B
SAMSUNG_HBM_CATCHUP_LAG_AND_LABOR_4C
HBM_EQUIPMENT_CARVEOUT_NOT_GREEN
AI_CHIP_DESIGN_UNLISTED_MERGER_STAGE2
SEMICONDUCTOR_INSPECTION_KOSDAQ_IPO_OVERHEAT
STATE_FOUNDRY_POLICY_RELIEF_NOT_GREEN
NVIDIA_BLACKWELL_DOMESTIC_AI_INFRA_STAGE2
CHINA_FAB_EXPORT_CONTROL_4C_WATCH
```

---

# 3. deep sub-archetype

```text
HBM memory:
- SK Hynix
- AI memory supply squeeze
- HBM / conventional DRAM 가격 구조 변화
- massive MFE 이후 4B-watch

Samsung catch-up:
- memory price recovery
- HBM qualification / China curb / Tesla foundry relief
- Q2 2025 profit drop
- labor strike / bonus dispute / emergency arbitration

HBM equipment:
- Hanwha Precision Machinery
- Hanwha Vision cash-flow backing
- HBM equipment development
- spin-off / governance / value unlock vs parent-share profit taking

AI chip design:
- Rebellions + Sapeon
- SK Telecom / SK Hynix shareholder exposure
- NPU / data-center LLM chip
- unlisted merger, not listed Green

Inspection IPO:
- TeraView KOSDAQ
- terahertz semiconductor inspection
- Samsung 10% stake
- 600x oversubscription
- IPO valuation / high-margin promise vs order book execution

Policy / fabless:
- 4.5T won foundry proposal
- 12-inch 40nm legacy foundry
- domestic fabless / defense chip self-sufficiency
- policy relief, not company Stage 3

AI infra:
- Nvidia Blackwell 260,000+ chips to Korea
- Samsung / SK / Hyundai / Naver smart factory / AI infra
- chip consumption vs supplier revenue bridge

Export-control:
- Samsung/SK China fab exposure
- U.S. authorisation revocation
- China-fab upgrade risk
```

---

# 4. 국장 신규 후보 case

## Case A — SK Hynix `structural_success + now 4B-watch`

```text
symbol = 000660
case_type = structural_success + 4B-watch
archetype = HBM_MEMORY_STRUCTURAL_RERATING_NOW_4B
```

### stage date

```text
Stage 1:
2024-03~06
- AI memory demand
- HBM supply scarcity
- hedge funds start buying Korea AI memory exposure

Stage 2:
2024-07-11
- global hedge funds target SK Hynix / Samsung for AI memory exposure
- SK Hynix seen as key HBM supplier to Nvidia
- SK Hynix up more than 70% YTD at that point

Stage 3:
2024-07-24 candidate
- Q2 OP 5.47T won, highest since 2018
- HBM shipments expected to more than double next year
- AI chip demand exceeds expectation

Stage 4B:
2026-05-14
- SK Hynix shares +274% in 2025
- shares > +200% in 2026
- market cap about $942B
- under $100B about 16 months earlier
```

SK Hynix는 여전히 R2의 가장 깨끗한 structural success benchmark다. 2024년에는 hedge fund들이 HBM scarcity와 Nvidia supply-chain exposure를 보고 한국 메모리 대형주를 사기 시작했고, SK Hynix는 이미 2024년 7월 기준 YTD 70% 이상 상승했다. 같은 달 Q2 OP 5.47조 원, 2018년 이후 최고 이익, HBM shipment next-year doubling 전망이 붙었다. 2026년에는 2025년 +274%, 2026년 +200% 이상 상승해 시총 약 $942B까지 갔기 때문에, 지금은 신규 Green보다 **4B-watch**가 맞다. ([Reuters][1])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters reported return / earnings anchors",
  "entry_date": "2024-07-24_candidate",
  "stage3_price": null,
  "q2_2024_op_krw_trn": 5.47,
  "q2_2024_op_status": "highest since 2018",
  "hbm_shipments_next_year": "expected_to_more_than_double",
  "reported_ytd_return_2024_july_pct": 70,
  "reported_return_2025_pct": 274,
  "reported_return_2026_min_pct": 200,
  "market_cap_2026_may_usd_bn": 942,
  "market_cap_mfe_from_under_100b_pct": 842,
  "mfe_30d_90d_180d_1y_2y": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = aligned
rerating_result = true_HBM_memory_structural_rerating
current_state = 4B_watch
```

---

## Case B — Samsung Electronics `success_candidate + HBM lag / labor 4C-watch`

```text
symbol = 005930
case_type = success_candidate + thesis_break_watch
archetype = SAMSUNG_HBM_CATCHUP_LAG_AND_LABOR_4C
```

### stage date

```text
Stage 1:
2024-07-05
- Samsung flags more than 15-fold Q2 OP rise
- memory price recovery
- AI demand lifts chip prices

Stage 2:
2024-07-05
- Q2 OP estimated 10.4T won vs 670B won YoY
- revenue estimated +23% to 74T won
- profit beat LSEG SmartEstimate 8.8T won

Stage 4C-watch:
2025-07-30
- Q2 2025 OP drops 55% to 4.7T won
- chip division profit only 400B won vs 6.5T won one year earlier
- weak AI chip sales, HBM shipment delay, China curbs
- stock only +0.7%, matching KOSPI, because Tesla $16.5B chip-sourcing deal gave relief

Stage 4C-watch 강화:
2026-05-12~19
- union demands removal of bonus cap and 15% OP bonus pool
- possible 18-day strike from 2026-05-21
- court partly limits strike but government warns emergency intervention possible
- one-day halt could cost up to 1T won
```

Samsung은 R2에서 “좋은 메모리 회복 story와 HBM lag risk가 동시에 존재하는” case다. 2024년 7월에는 Q2 OP가 10.4조 원으로 전년 6,700억 원 대비 15배 이상 늘었고, revenue도 23% 증가한 74조 원으로 예상됐다. 하지만 2025년 7월에는 Q2 OP가 55% 줄어 4.7조 원이 됐고, chip division profit은 6.5조 원에서 4,000억 원으로 급감했다. 원인은 weak AI chip sales, HBM shipment delay, China curbs였고, Tesla deal이 없었다면 가격 반응은 더 나빴을 수 있다. 2026년 5월에는 strike risk까지 붙어 operational 4C-watch가 강화됐다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters earnings / labor anchors",
  "stage3_price": null,
  "q2_2024_op_estimate_krw_trn": 10.4,
  "q2_2024_prior_year_op_krw_trn": 0.67,
  "q2_2024_op_growth_multiple": 15.52,
  "q2_2024_revenue_estimate_krw_trn": 74,
  "q2_2024_revenue_growth_pct": 23,
  "lseg_smartestimate_krw_trn": 8.8,
  "q2_2025_op_krw_trn": 4.7,
  "q2_2025_op_decline_pct": -55,
  "chip_division_profit_q2_2025_krw_trn": 0.4,
  "chip_division_profit_prior_year_krw_trn": 6.5,
  "chip_division_profit_decline_pct": -93.8,
  "stock_reaction_q2_2025_pct": 0.7,
  "kospi_same_context_pct": 0.7,
  "tesla_chip_sourcing_deal_usd_bn": 16.5,
  "strike_possible_workers": 50000,
  "strike_duration_days": 18,
  "one_day_direct_loss_estimate_krw_trn": 1,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_plus_thesis_break_watch
rerating_result = Samsung_memory_recovery_but_HBM_lag_and_labor_gate
stage_failure_type = recovery_not_green_until_HBM_volume_margin_and_labor_risk_clear
```

---

## Case C — Hanwha Precision Machinery carve-out `failed_rerating / HBM equipment not Green`

```text
listed_parent = 012450
case_type = failed_rerating + success_candidate
archetype = HBM_EQUIPMENT_CARVEOUT_NOT_GREEN
```

### stage date

```text
Stage 1:
2024-04-02
- media reports Hanwha Aerospace spin-off plan
- stock jumped more than +15% on spin-off speculation

Stage 2:
2024-04-05
- Hanwha Aerospace confirms spin-off of Hanwha Precision Machinery and Hanwha Vision
- semiconductor equipment and video-surveillance businesses contributed about 16% of revenue
- Hanwha Precision develops HBM equipment
- new industrial-solutions company estimated around 2T won
- defense business estimated around 10T won

Stage 4B / failed_rerating:
2024-04-05
- stock falls -8% in morning trade on profit taking
- value-unlock story was partially priced before official confirmation

Stage 3:
없음
- HBM equipment business carve-out is not Green
- actual HBM equipment orders, margin, listed vehicle, governance, cash-flow bridge needed
```

Hanwha Precision Machinery는 R2의 좋은 HBM equipment 후보지만, parent-stock 기준으로는 clean Green이 아니다. Hanwha Aerospace는 반도체 장비와 video-surveillance 사업을 분사한다고 밝혔고, 이 두 사업은 매출의 약 16%를 차지했다. Hanwha Precision은 HBM 장비를 개발 중이라는 설명도 나왔지만, 공식 발표일에는 parent 주가가 -8% 하락했다. 즉 “HBM equipment carve-out”은 Stage 2이고, price path는 이미 speculation → confirmation sell-the-news로 움직였다. ([Reuters][3])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters spin-off/event-return anchor",
  "stage3_price": null,
  "media_report_pre_event_mfe_pct": 15,
  "confirmation_event_mae_pct": -8,
  "spin_off_business_revenue_share_pct": 16,
  "new_industrial_solutions_estimated_value_krw_trn": 2,
  "defense_business_estimated_value_krw_trn": 10,
  "parent_market_cap_context_krw_trn": 11,
  "hbm_equipment_development_confirmed": true,
  "actual_hbm_equipment_order_revenue_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = failed_rerating_stage2
rerating_result = HBM_equipment_carveout_watch
stage_failure_type = carveout_value_unlock_not_order_revenue_green
```

---

## Case D — Rebellions / Sapeon `success_candidate / unlisted AI chip design`

```text
listed_readthrough = SK Telecom / SK Hynix / KT / AI-chip ecosystem
case_type = success_candidate + insufficient_price_data
archetype = AI_CHIP_DESIGN_UNLISTED_MERGER_STAGE2
```

### stage date

```text
Stage 1:
2024-06-12
- Rebellions and Sapeon plan merger
- South Korea tries to create Nvidia challenger in AI NPU

Stage 2:
2024-08-18
- Rebellions and Sapeon agree to merge
- Sapeon shareholders include SK Telecom and SK Hynix
- Rebellions has over $225M total funding after $15M Wa'ed Ventures investment
- merged entity targets global AI semiconductor market in 2~3 years

Stage 3:
없음
- unlisted merger is not listed-stock Green
- tape-out, mass production, customer order, inference deployment, revenue/margin needed

Stage 4B:
AI chip “Korea Nvidia challenger” narrative로 SKT / SK Hynix / ecosystem stocks가 먼저 움직이면 watch
```

Rebellions/Sapeon은 한국 AI chip design의 중요한 Stage 2다. Reuters는 두 AI chip developers가 Nvidia와 경쟁하기 위해 합병한다고 보도했고, Sapeon 주주에는 SK Telecom과 SK Hynix가 포함된다. 하지만 비상장 합병이고, 아직 상장사 revenue bridge가 확인되지 않았다. 그래서 이 case는 **unlisted AI chip optionality**로만 기록한다. ([Reuters][4])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters AI-chip merger anchors",
  "stage3_price": null,
  "merged_companies": "Rebellions + Sapeon Korea",
  "listed_shareholder_readthrough": ["SK Telecom", "SK Hynix"],
  "total_funding_rebellions_usd_mn": 225,
  "waed_ventures_investment_usd_mn": 15,
  "target_market_share_timeline": "2-3 years",
  "npu_focus": true,
  "listed_stock_ohlc": "price_data_unavailable_after_deep_search",
  "reason": "direct company unlisted; listed shareholder earnings bridge not confirmed"
}
```

### alignment

```text
score_price_alignment = success_candidate_but_insufficient_price_data
rerating_result = Korean_AI_chip_design_unlisted_stage2
stage_failure_type = merger_not_mass_production_revenue_green
```

---

## Case E — TeraView KOSDAQ IPO `overheat / inspection equipment Stage 2`

```text
symbol = newly listed KOSDAQ foreign semiconductor equipment company
case_type = overheat + success_candidate
archetype = SEMICONDUCTOR_INSPECTION_KOSDAQ_IPO_OVERHEAT
```

### stage date

```text
Stage 1:
2025-12-08
- British semiconductor inspection firm chooses KOSDAQ
- terahertz ultra-precision inspection for advanced semiconductor manufacturing
- Samsung Electronics customer and 10% shareholder

Stage 2:
2025-12-08
- IPO offering 40B won / about $27M
- implied valuation about $240M
- oversubscribed 600x
- listing price 8,000 won
- implied P/E about 40x
- 60% revenue generated from regional clients, many Korean semiconductor companies
- product margins 60~70% forecast depending on product
- order book growth forecast at least 100% this year and next

Stage 4B:
2025-12 IPO
- 600x oversubscription / 40x P/E before listed track record

Stage 3:
없음
- order book, delivered inspection systems, recurring service, customer concentration, margin durability needed
```

TeraView는 R2에서 흥미로운 KOSDAQ semiconductor inspection IPO다. Samsung이 10% stake를 가진 고객이고, 테라헤르츠 기술은 AI chip 제조의 ultra-precision inspection에 쓰인다. 하지만 600배 청약, P/E 40배, 60~70% margin promise는 IPO overheat도 같이 의미한다. Stage 3는 실제 order book delivery와 margin durability가 확인되어야 한다. ([마켓워치][5])

### 실제 가격경로 검증

```json
{
  "price_data_source": "MarketWatch IPO anchor",
  "stage3_price": null,
  "ipo_offering_krw_bn": 40,
  "ipo_offering_usd_mn": 27,
  "implied_valuation_usd_mn": 240,
  "oversubscription_multiple": 600,
  "listing_price_krw": 8000,
  "implied_pe": 40,
  "samsung_stake_pct": 10,
  "regional_revenue_share_pct": 60,
  "margin_forecast_pct": "60-70",
  "order_book_growth_forecast_pct": 100,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = overheat_success_candidate
rerating_result = semiconductor_inspection_IPO_watch
stage_failure_type = IPO_demand_not_delivery_margin_green
```

---

## Case F — Korea 4.5T foundry plan `policy relief, not Green`

```text
symbol = Samsung / SK Hynix / DB HiTek / fabless ecosystem basket
case_type = success_candidate_policy_relief
archetype = STATE_FOUNDRY_POLICY_RELIEF_NOT_GREEN
```

### stage date

```text
Stage 1:
2025-12-10
- Korea considers state-private foundry plan
- memory leadership vs logic/foundry weakness
- domestic fabless and defense-chip supply security

Stage 2:
2025-12-10
- 4.5T won / $3.06B foundry proposal
- 12-inch, 40nm facility
- intended to support essential chips / fabless companies
- defense chip import dependence around 99%
- possible law changes to prioritize domestic chips for national-security infrastructure

Stage 3:
없음
- policy proposal is not listed-stock Green
- final budget, operator, utilization, customer contracts, margin needed
```

Korea foundry plan은 R2 정책 relief다. 4.5조 원 규모의 12-inch 40nm foundry는 domestic fabless와 방산 chip self-sufficiency를 돕는 구조지만, 아직 기업별 Stage 3는 아니다. operator, budget finalization, 고객 계약, utilization, margin이 확인되어야 한다. ([Reuters][6])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters foundry-policy anchor",
  "stage3_price": null,
  "proposed_foundry_investment_krw_trn": 4.5,
  "proposed_foundry_investment_usd_bn": 3.06,
  "wafer_size": "12-inch",
  "process_node": "40nm",
  "target_users": "domestic fabless / essential chips",
  "defense_chip_import_dependence_pct": 99,
  "operator_confirmed": false,
  "customer_contract_confirmed": false,
  "listed_price_path": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_policy_relief
rerating_result = state_foundry_policy_stage2
stage_failure_type = policy_proposal_not_utilization_margin_green
```

---

## Case G — Nvidia Blackwell supply to Korea `success_candidate / AI infra demand not supplier revenue`

```text
symbols = Samsung / SK Group / Hyundai Motor / Naver / Kakao ecosystem
case_type = success_candidate + event_premium
archetype = NVIDIA_BLACKWELL_DOMESTIC_AI_INFRA_STAGE2
```

### stage date

```text
Stage 1:
2025-10-31
- Nvidia plans large Blackwell supply to Korea
- Korea wants to become AI hub
- AI chips for government, Samsung, SK, Hyundai, Naver

Stage 2:
2025-10-31
- Nvidia to supply more than 260,000 Blackwell AI chips to South Korea
- government to use 50,000 chips for AI infrastructure
- Samsung, SK, Hyundai each to deploy up to 50,000 chips
- Naver to buy 60,000 chips
- Hyundai to use chips in autonomous driving / robotics / smart manufacturing supercomputer

Stage 3:
없음
- Blackwell consumption is not automatic Korean listed-stock Green
- need AI factory productivity, Naver cloud revenue, Samsung/SK manufacturing efficiency, capex ROI
```

Nvidia Blackwell 공급은 R2와 R8/R11 사이의 AI infra Stage 2다. 한국 기업들이 AI chip을 대규모로 들여오는 건 수요와 정책 의지는 강하지만, Nvidia chips를 산다고 한국 상장사 이익이 자동으로 늘지는 않는다. 실제 Stage 3는 smart factory 생산성, Naver cloud revenue, Samsung/SK process efficiency, capex ROI가 확인될 때다. ([Reuters][7])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters Nvidia Blackwell supply anchor",
  "stage3_price": null,
  "total_blackwell_chips_to_korea": 260000,
  "government_ai_infra_chips": 50000,
  "samsung_chips_up_to": 50000,
  "sk_chips_up_to": 50000,
  "hyundai_chips_up_to": 50000,
  "naver_chips": 60000,
  "direct_supplier_revenue_to_korean_listed_companies": false,
  "capex_roi_confirmed": false,
  "price_validation_status": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_event_premium
rerating_result = AI_infra_chip_consumption_stage2
stage_failure_type = capex_consumption_not_eps_green
```

---

## Case H — China fab export-control basket `4C-watch`

```text
symbols = 005930 / 000660 / 067310 / 042700
case_type = 4C-watch
archetype = CHINA_FAB_EXPORT_CONTROL_4C_WATCH
```

### stage date

```text
Stage 1:
2025-08-29
- U.S. revokes authorisations for Samsung / SK Hynix China fabs
- China fab U.S. equipment access risk

Stage 4C-watch:
2025-09-01
- Samsung -2.3%
- SK Hynix -4.4%
- Hana Micron -1.7%
- Hanmi Semiconductor -4.4%
- KOSPI -0.7%
- Samsung has more than one-third DRAM output from China
- SK Hynix has 30~40% of DRAM/NAND output from China

Stage 3:
N/A
```

China fab export control은 R2의 persistent RedTeam이다. 미국이 장비 반입 authorisation을 취소하자 Samsung, SK Hynix, Hana Micron, Hanmi가 모두 하락했고, 이는 HBM/AI boom 속에서도 China fab exposure가 hard gate로 남아 있음을 보여준다. 다만 이 case는 hard 4C 확정이 아니라 4C-watch다. ([Reuters][8])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters export-control event-return anchor",
  "stage3_price": null,
  "samsung_event_mae_pct": -2.3,
  "sk_hynix_event_mae_pct": -4.4,
  "hana_micron_event_mae_pct": -1.7,
  "hanmi_semiconductor_event_mae_pct": -4.4,
  "kospi_same_context_pct": -0.7,
  "samsung_relative_underperformance_pp": -1.6,
  "sk_hynix_relative_underperformance_pp": -3.7,
  "hanmi_relative_underperformance_pp": -3.7,
  "samsung_china_dram_exposure": "more_than_one_third",
  "sk_hynix_china_dram_nand_exposure_pct": "30-40",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = China_fab_export_control_overlay
stage_failure_type = 4C_watch_not_hard_4C
```

---

# 5. 이번 R2 case별 stage date 요약

| case                     | Stage 1    | Stage 2    | Stage 3              | Stage 4B                         | Stage 4C                   |
| ------------------------ | ---------- | ---------- | -------------------- | -------------------------------- | -------------------------- |
| SK Hynix                 | 2024-03~06 | 2024-07-11 | 2024-07-24 candidate | 2026-05-14                       | N/A                        |
| Samsung Electronics      | 2024-07-05 | 2024-07-05 | N/A                  | $1T / labor-profit-sharing watch | 2025-07-30 / 2026-05 watch |
| Hanwha Precision         | 2024-04-02 | 2024-04-05 | N/A                  | 2024-04-05                       | N/A                        |
| Rebellions/Sapeon        | 2024-06-12 | 2024-08-18 | N/A                  | watch                            | N/A                        |
| TeraView                 | 2025-12-08 | 2025-12-08 | N/A                  | IPO overheat                     | N/A                        |
| Korea foundry            | 2025-12-10 | 2025-12-10 | N/A                  | policy basket watch              | N/A                        |
| Nvidia Blackwell Korea   | 2025-10-31 | 2025-10-31 | N/A                  | AI infra event watch             | N/A                        |
| China fab export-control | 2025-08-29 | N/A        | N/A                  | N/A                              | 2025-09-01 watch           |

---

# 6. 실제 가격경로 검증 총괄

| case                 |                            price / return anchor | MFE / MAE 해석                                        | 판정                     |
| -------------------- | -----------------------------------------------: | --------------------------------------------------- | ---------------------- |
| SK Hynix             |    2024 YTD +70%, 2025 +274%, 2026 +200%+, $942B | Stage 3 성공, 현재 4B                                   | aligned                |
| Samsung              | Q2 2025 OP -55%, chip profit -93.8%, stock +0.7% | Tesla relief로 bad news absorb, but HBM lag 4C-watch | thesis_break_watch     |
| Hanwha Precision     |                     rumor +15%, confirmation -8% | value-unlock speculation → sell-the-news            | failed_rerating_stage2 |
| Rebellions/Sapeon    |                         unlisted, funding >$225M | AI chip design Stage 2, no listed revenue           | insufficient           |
| TeraView             |               600x IPO, valuation $240M, P/E 40x | inspection equipment Stage 2 + IPO overheat         | overheat               |
| Korea foundry        |                                  4.5T won policy | policy relief, no operator/utilization              | policy_not_green       |
| Nvidia Blackwell     |                          260,000+ chips to Korea | AI infra consumption, not EPS proof                 | event_premium          |
| China export-control |             Samsung -2.3%, SK -4.4%, Hanmi -4.4% | direct 4C-watch                                     | thesis_break_watch     |

---

# 7. score-price alignment 판정

```text
aligned:
- SK Hynix

aligned_but_now_4B:
- SK Hynix

success_candidate:
- Samsung Electronics, but only after HBM volume / margin / labor risk clear
- Hanwha Precision Machinery carve-out
- Rebellions/Sapeon
- Korea state foundry policy
- Nvidia Blackwell Korea AI infra

failed_rerating:
- Hanwha Aerospace / Hanwha Precision spin-off confirmation sell-the-news

overheat:
- TeraView KOSDAQ IPO
- SK Hynix $1T approach / memory supercycle milestone

price_moved_without_evidence:
- TeraView if treated as Green before delivered order book
- Rebellions/Sapeon if listed parents move before revenue bridge
- Nvidia Blackwell AI infra if capex consumption treated as EPS

evidence_good_but_price_failed:
- Samsung Q2 2025: Tesla relief muted reaction, but HBM lag and China curbs were negative
- SK Hynix Q2 2024 result day: strong OP but investor expectations already high

thesis_break_watch:
- Samsung HBM lag / China curbs / labor strike
- China fab export-control basket

hard_4C_confirmed:
- false
```

---

# 8. 점수비중 교정

## 올릴 축

```text
HBM_volume_certification +5
customer_qualification +5
mass_production_readiness +5
equipment_order_backlog +5
delivered_order_book +5
gross_margin_visibility +5
OP_revision_quality +4
labor_operational_resilience +5
China_fab_export_control_clearance +5
capex_ROI_bridge +4
```

### 왜 올리나

SK Hynix는 HBM volume, customer demand, OP revision, supply squeeze가 모두 가격경로와 맞았다. 반면 Samsung은 2024년 회복은 좋았지만 2025년 HBM lag / China curbs가 곧바로 thesis-break watch로 바뀌었다. Hanwha Precision, TeraView, Rebellions는 모두 Stage 2지만 실제 order / delivery / revenue bridge가 필요하다.

## 내릴 축

```text
AI_chip_keyword_only -5
policy_foundry_headline_only -5
IPO_oversubscription_only -5
strategic_equity_or_unlisted_merger_only -5
equipment_carveout_without_orders -4
capex_consumption_without_EPS -4
HBM_rumor_without_customer_qualification -5
China_fab_exposure -5
labor_strike_unresolved -5
```

### 왜 내리나

TeraView의 600x 청약은 Green이 아니다. Rebellions/Sapeon은 unlisted AI chip design option이다. Korea foundry plan은 operator와 utilization이 없다. Nvidia Blackwell 국내 공급은 AI chip을 “사는” 이벤트이지 한국 상장사 이익 증가가 아니다. Samsung strike와 China fab exposure는 R2 hard gate 후보로 남는다.

## Green gate 강화 조건

```text
R2 Stage 3-Green 필수:
1. customer qualification / 인증 확인
2. mass production / shipment 시작
3. equipment / material order backlog 확인
4. delivered order book 또는 recurring order 확인
5. OP / gross margin / FCF 개선 확인
6. capex ROI 또는 utilization 확인
7. China fab / export-control risk 통과
8. labor / production disruption risk 통과
9. price path가 evidence 이후 따라옴

금지:
AI keyword only
HBM rumor only
foundry policy only
IPO oversubscription only
unlisted merger only
strategic stake only
Blackwell chip consumption only
equipment carve-out only
```

## 4B 조기감지 조건

```text
4B-watch:
HBM/AI memory로 1년 3~5배 상승
market-cap $1T milestone headline
IPO oversubscription 100x~600x
P/E 40x+ before listed delivery record
spin-off rumor로 +15% 후 confirmation sell-the-news
AI chip merger / Nvidia infra headline로 revenue 전 basket rally
policy foundry headline로 fabless/equipment주 선반영

4B-elevated:
actual customer qualification 없음
delivered order book 없음
operator / utilization 없음
capex ROI 없음
China fab exposure 남음
labor strike unresolved
```

## 4C hard gate 조건

```text
HBM qualification failure
customer shipment delay
AI chip order cancellation
mass production failure
China fab equipment license denial
export-control escalation
labor strike causing production halt
equipment order cancellation
IPO lockup / delivery failure
foundry utilization failure
```

이번 R2 Loop 13에서는 hard 4C를 확정하지 않는다. 다만 **Samsung HBM lag / labor strike**, **China fab export-control**, **TeraView IPO overheat**, **unlisted AI chip merger revenue gap**은 모두 강한 shadow gate로 둔다.

---

# 9. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 10. 레포 반영용 patch-ready 출력

## docs/round/round_199.md 요약

```md
# R2 Loop 13. AI Semiconductor Electronics Price Validation

이번 라운드는 R2 Loop 13 price-validation 라운드다.

핵심 결론:
- SK Hynix remains the clean structural success benchmark. It was already up more than 70% YTD in July 2024, later reported Q2 2024 OP of 5.47T won, and by May 2026 had risen +274% in 2025 and >+200% in 2026 with market cap around $942B. Current state is 4B-watch.
- Samsung Electronics is success_candidate plus HBM lag/labor 4C-watch. Q2 2024 OP estimate was 10.4T won, more than 15x YoY, but Q2 2025 OP fell 55% to 4.7T won and chip-division profit fell to 400B won from 6.5T won. Labor strike risk remains a hard gate candidate.
- Hanwha Precision Machinery carve-out is HBM equipment Stage 2 but failed_rerating on confirmation. Hanwha Aerospace stock jumped >15% on reports but fell -8% on confirmation. Equipment orders and revenue bridge required.
- Rebellions/Sapeon is AI chip design Stage 2. The unlisted merger has SK Telecom/SK Hynix read-through and >$225M funding, but no listed revenue bridge.
- TeraView is semiconductor-inspection KOSDAQ IPO overheat. Offering 40B won, valuation $240M, 600x oversubscription, Samsung 10% stake, P/E about 40x. Delivery/margin proof required.
- Korea 4.5T won foundry plan is policy relief, not Green. It proposes a 12-inch 40nm facility for essential chips/fabless companies, but operator, utilization and customer contracts are unconfirmed.
- Nvidia Blackwell Korea supply is AI infra Stage 2. More than 260,000 chips to Korea, including 50,000 each for government, Samsung, SK and Hyundai and 60,000 for Naver. Capex consumption is not EPS proof.
- China fab export-control remains 4C-watch. Samsung -2.3%, SK Hynix -4.4%, Hana Micron -1.7%, Hanmi -4.4%, KOSPI -0.7% on the September 2025 authorisation revocation event.
```

## docs/checkpoints/checkpoint_28a_round199_r2_loop13.md 요약

```md
# Checkpoint 28A Round 199 R2 Loop 13 AI Semiconductor Electronics Price Validation

## 반영 내용
- R2 Loop 13 price-validation 라운드를 추가했다.
- HBM memory success, Samsung HBM lag/labor risk, Hanwha Precision carve-out, Rebellions/Sapeon AI chip merger, TeraView KOSDAQ IPO, state foundry policy, Nvidia Blackwell Korea infra, China fab export-control overlay를 비교했다.
- Reuters / FT / WSJ / MarketWatch anchors로 가능한 event MFE/MAE 및 price/valuation anchors를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- HBM volume certification, customer qualification, mass-production readiness, equipment order backlog, delivered order book, gross margin visibility, labor resilience, China export-control clearance 가중치 강화
- AI keyword-only, foundry policy headline-only, IPO oversubscription-only, strategic equity/unlisted merger-only, equipment carve-out without orders, capex consumption without EPS 감점 강화
```

## data/e2r_case_library/cases_r2_loop13_round199.jsonl 초안

```jsonl
{"case_id":"r2_loop13_sk_hynix_hbm_success_now_4b","symbol":"000660","company_name":"SK Hynix","case_type":"structural_success","primary_archetype":"HBM_MEMORY_STRUCTURAL_RERATING_NOW_4B","stage2_date":"2024-07-11","stage3_date":"2024-07-24_candidate","stage4b_date":"2026-05-14","price_validation":{"price_data_source":"Reuters reported return / earnings anchors","stage3_price":null,"q2_2024_op_krw_trn":5.47,"q2_2024_op_status":"highest_since_2018","hbm_shipments_next_year":"expected_to_more_than_double","reported_ytd_return_2024_july_pct":70,"reported_return_2025_pct":274,"reported_return_2026_min_pct":200,"market_cap_2026_may_usd_bn":942,"market_cap_mfe_from_under_100b_pct":842,"price_validation_status":"reported_anchor_not_full_ohlc"},"score_price_alignment":"aligned","rerating_result":"true_HBM_memory_structural_rerating","notes":"Stage 3 worked; current state is 4B-watch after massive MFE and market-cap milestone."}
{"case_id":"r2_loop13_samsung_hbm_lag_labor_4c_watch","symbol":"005930","company_name":"Samsung Electronics","case_type":"success_candidate","primary_archetype":"SAMSUNG_HBM_CATCHUP_LAG_AND_LABOR_4C","stage2_date":"2024-07-05","stage4c_date":"2025-07-30/2026-05_watch","price_validation":{"price_data_source":"Reuters earnings/labor anchors","stage3_price":null,"q2_2024_op_estimate_krw_trn":10.4,"q2_2024_prior_year_op_krw_trn":0.67,"q2_2024_op_growth_multiple":15.52,"q2_2024_revenue_estimate_krw_trn":74,"q2_2024_revenue_growth_pct":23,"lseg_smartestimate_krw_trn":8.8,"q2_2025_op_krw_trn":4.7,"q2_2025_op_decline_pct":-55,"chip_division_profit_q2_2025_krw_trn":0.4,"chip_division_profit_prior_year_krw_trn":6.5,"chip_division_profit_decline_pct":-93.8,"stock_reaction_q2_2025_pct":0.7,"kospi_same_context_pct":0.7,"tesla_chip_sourcing_deal_usd_bn":16.5,"strike_possible_workers":50000,"strike_duration_days":18,"one_day_direct_loss_estimate_krw_trn":1,"price_validation_status":"reported_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_plus_thesis_break_watch","rerating_result":"Samsung_memory_recovery_but_HBM_lag_and_labor_gate","notes":"Memory recovery is Stage 2; HBM shipment lag, China curbs and labor risk block Green."}
{"case_id":"r2_loop13_hanwha_precision_hbm_equipment_carveout","symbol":"012450_parent","company_name":"Hanwha Precision Machinery / Hanwha Aerospace parent","case_type":"failed_rerating","primary_archetype":"HBM_EQUIPMENT_CARVEOUT_NOT_GREEN","stage2_date":"2024-04-05","stage4b_date":"2024-04-05","price_validation":{"price_data_source":"Reuters spin-off/event-return anchor","stage3_price":null,"media_report_pre_event_mfe_pct":15,"confirmation_event_mae_pct":-8,"spin_off_business_revenue_share_pct":16,"new_industrial_solutions_estimated_value_krw_trn":2,"defense_business_estimated_value_krw_trn":10,"parent_market_cap_context_krw_trn":11,"hbm_equipment_development_confirmed":true,"actual_hbm_equipment_order_revenue_confirmed":false,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"failed_rerating_stage2","rerating_result":"HBM_equipment_carveout_watch","notes":"Carve-out and HBM equipment development are Stage 2; actual orders/revenue needed before Green."}
{"case_id":"r2_loop13_rebellions_sapeon_ai_chip_merger","symbol":"SKT/SK_Hynix_readthrough_unlisted","company_name":"Rebellions / Sapeon Korea","case_type":"success_candidate","primary_archetype":"AI_CHIP_DESIGN_UNLISTED_MERGER_STAGE2","stage2_date":"2024-08-18","price_validation":{"price_data_source":"Reuters AI-chip merger anchors","stage3_price":null,"merged_companies":"Rebellions + Sapeon Korea","listed_shareholder_readthrough":["SK Telecom","SK Hynix"],"total_funding_rebellions_usd_mn":225,"waed_ventures_investment_usd_mn":15,"target_market_share_timeline":"2-3 years","npu_focus":true,"price_validation_status":"unlisted_company_no_direct_ohlc"},"score_price_alignment":"success_candidate_but_insufficient_price_data","rerating_result":"Korean_AI_chip_design_unlisted_stage2","notes":"AI chip merger is Stage 2; tape-out, mass production, customer order, deployment revenue and margin needed."}
{"case_id":"r2_loop13_teraview_kosdaq_semiconductor_inspection_ipo","symbol":"new_KOSDAQ_foreign_listing","company_name":"TeraView","case_type":"overheat","primary_archetype":"SEMICONDUCTOR_INSPECTION_KOSDAQ_IPO_OVERHEAT","stage2_date":"2025-12-08","stage4b_date":"2025-12-08","price_validation":{"price_data_source":"MarketWatch IPO anchor","stage3_price":null,"ipo_offering_krw_bn":40,"ipo_offering_usd_mn":27,"implied_valuation_usd_mn":240,"oversubscription_multiple":600,"listing_price_krw":8000,"implied_pe":40,"samsung_stake_pct":10,"regional_revenue_share_pct":60,"margin_forecast_pct":"60-70","order_book_growth_forecast_pct":100,"price_validation_status":"reported_ipo_anchor_not_full_ohlc"},"score_price_alignment":"overheat_success_candidate","rerating_result":"semiconductor_inspection_IPO_watch","notes":"Terahertz inspection is Stage 2, but 600x subscription and P/E 40x are 4B unless delivered order book/margin prove out."}
{"case_id":"r2_loop13_korea_state_foundry_policy","symbol":"foundry_fabless_basket","company_name":"Korea state-private foundry policy basket","case_type":"success_candidate_policy_relief","primary_archetype":"STATE_FOUNDRY_POLICY_RELIEF_NOT_GREEN","stage2_date":"2025-12-10","price_validation":{"price_data_source":"Reuters foundry-policy anchor","stage3_price":null,"proposed_foundry_investment_krw_trn":4.5,"proposed_foundry_investment_usd_bn":3.06,"wafer_size":"12-inch","process_node":"40nm","target_users":"domestic fabless / essential chips","defense_chip_import_dependence_pct":99,"operator_confirmed":false,"customer_contract_confirmed":false,"price_validation_status":"policy_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_policy_relief","rerating_result":"state_foundry_policy_stage2","notes":"Policy proposal is not Green until operator, budget, utilization, customer contracts and margin are confirmed."}
{"case_id":"r2_loop13_nvidia_blackwell_korea_ai_infra","symbol":"Samsung/SK/Hyundai/Naver/Kakao_ecosystem","company_name":"Nvidia Blackwell Korea AI infrastructure buyers","case_type":"success_candidate_event_premium","primary_archetype":"NVIDIA_BLACKWELL_DOMESTIC_AI_INFRA_STAGE2","stage2_date":"2025-10-31","price_validation":{"price_data_source":"Reuters Nvidia Blackwell supply anchor","stage3_price":null,"total_blackwell_chips_to_korea":260000,"government_ai_infra_chips":50000,"samsung_chips_up_to":50000,"sk_chips_up_to":50000,"hyundai_chips_up_to":50000,"naver_chips":60000,"direct_supplier_revenue_to_korean_listed_companies":false,"capex_roi_confirmed":false,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_event_premium","rerating_result":"AI_infra_chip_consumption_stage2","notes":"Blackwell consumption is Stage 2; smart-factory productivity, cloud revenue, process efficiency and capex ROI required."}
{"case_id":"r2_loop13_china_fab_export_control_basket","symbol":"005930/000660/067310/042700","company_name":"Samsung / SK Hynix / Hana Micron / Hanmi China-fab export-control basket","case_type":"4c_watch","primary_archetype":"CHINA_FAB_EXPORT_CONTROL_4C_WATCH","stage4c_date":"2025-09-01_watch","price_validation":{"price_data_source":"Reuters export-control event-return anchor","stage3_price":null,"samsung_event_mae_pct":-2.3,"sk_hynix_event_mae_pct":-4.4,"hana_micron_event_mae_pct":-1.7,"hanmi_semiconductor_event_mae_pct":-4.4,"kospi_same_context_pct":-0.7,"samsung_relative_underperformance_pp":-1.6,"sk_hynix_relative_underperformance_pp":-3.7,"hanmi_relative_underperformance_pp":-3.7,"samsung_china_dram_exposure":"more_than_one_third","sk_hynix_china_dram_nand_exposure_pct":"30-40","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"China_fab_export_control_overlay","notes":"China fab exposure remains 4C-watch, not hard 4C unless license denial/revenue impairment confirms."}
```

## data/sector_taxonomy/score_weight_profiles_round199_r2_loop13_v1.csv 초안

```csv
archetype,hbm_volume_certification,customer_qualification,mass_production_readiness,equipment_order_backlog,delivered_order_book,gross_margin_visibility,op_revision_quality,labor_operational_resilience,china_fab_export_control_clearance,capex_roi_bridge,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
HBM_MEMORY_STRUCTURAL_RERATING_NOW_4B,+5,+5,+5,+3,+4,+5,+5,+4,+4,+3,-1,+5,+4,SK Hynix remains aligned but is now 4B after massive MFE.
SAMSUNG_HBM_CATCHUP_LAG_AND_LABOR_4C,+5,+5,+5,+3,+4,+5,+4,+5,+5,+4,-3,+5,+5,Samsung recovery needs HBM volume/margin and labor risk clearance.
HBM_EQUIPMENT_CARVEOUT_NOT_GREEN,+3,+4,+4,+5,+5,+5,+3,+2,+3,+3,-4,+5,+4,Hanwha Precision carve-out requires actual HBM equipment orders and revenue.
AI_CHIP_DESIGN_UNLISTED_MERGER_STAGE2,+2,+4,+5,+1,+4,+5,+2,+2,+3,+4,-5,+5,+4,Rebellions/Sapeon needs customer deployment and listed revenue bridge.
SEMICONDUCTOR_INSPECTION_KOSDAQ_IPO_OVERHEAT,+2,+4,+4,+5,+5,+5,+3,+2,+3,+4,-5,+5,+4,TeraView IPO is Stage 2 but oversubscription/P-E overheat requires delivery proof.
STATE_FOUNDRY_POLICY_RELIEF_NOT_GREEN,+1,+2,+3,+2,+2,+4,+2,+2,+4,+5,-5,+4,+4,Foundry policy needs operator/utilization/customer contracts.
NVIDIA_BLACKWELL_DOMESTIC_AI_INFRA_STAGE2,+1,+2,+3,+0,+0,+3,+2,+2,+2,+5,-4,+4,+3,Blackwell consumption is not EPS without productivity/cloud revenue bridge.
CHINA_FAB_EXPORT_CONTROL_4C_WATCH,+0,+0,+0,+0,+0,+2,+0,+2,+5,+0,0,+4,+5,China fab exposure remains R2 hard-gate candidate.
```

---

# 이번 R2 Loop 13 결론

```text
1. SK Hynix는 여전히 R2 structural success benchmark다.
   다만 지금은 Stage 3 추가가 아니라 4B-watch다.

2. Samsung은 memory recovery는 강하지만 HBM lag, China curbs, labor risk가 동시에 붙는다.
   Green은 HBM volume/margin과 operational risk clearance 뒤다.

3. Hanwha Precision Machinery carve-out은 HBM equipment Stage 2다.
   하지만 confirmation day -8%는 value-unlock rumor가 이미 선반영됐다는 뜻이다.

4. Rebellions/Sapeon은 Korea AI chip design Stage 2다.
   unlisted merger라서 상장사 Green은 customer deployment와 revenue bridge가 필요하다.

5. TeraView는 semiconductor inspection Stage 2지만 IPO overheat다.
   600x 청약과 P/E 40x는 4B-watch다.

6. Korea 4.5T foundry plan은 policy relief다.
   operator, utilization, customer contracts 전에는 Green이 아니다.

7. Nvidia Blackwell Korea supply는 AI infra Stage 2다.
   chip을 사는 이벤트와 EPS가 늘어나는 이벤트를 분리해야 한다.

8. China fab export-control은 R2 persistent 4C-watch다.
   Samsung/SK의 China production exposure는 HBM supercycle 속에서도 hard gate 후보로 남는다.
```

한 문장으로 압축하면:

> **R2에서 진짜 Stage 3는 “AI·HBM·foundry·장비·IPO·정책이 좋다”가 아니라, 고객 인증·양산·반복 주문·마진·FCF가 실제 가격경로로 닫히고, 중국 fab·노동·수출통제·IPO 과열을 통과하는 순간이다.**

* [Reuters](https://www.reuters.com/world/asia-pacific/ai-boom-puts-sk-hynix-cusp-1-trillion-market-value-2026-05-14/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/technology/nvidia-supplier-sk-hynixs-q2-profit-soars-ai-boom-2024-07-24/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/technology/samsung-flags-15-fold-rise-second-quarter-profit-chip-prices-climb-2024-07-04/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/china/samsung-q2-profit-drops-55-weak-ai-chip-sales-china-curbs-2025-07-30/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/markets/asia/hanwha-aerospace-spin-off-semiconductor-equipment-unit-2024-04-05/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/technology/artificial-intelligence/south-korean-ai-chip-developers-rebellions-sapeon-merge-2024-06-12/?utm_source=chatgpt.com)
* [마켓워치](https://www.marketwatch.com/story/a-british-tech-company-is-going-public-in-south-korea-the-ceo-explains-why-5bf0c593?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/south-korea-consider-setting-up-31-bln-foundry-grow-local-chip-sector-2025-12-10/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/media-telecom/nvidia-supply-more-than-260000-blackwell-ai-chips-south-korea-2025-10-31/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/china/shares-samsung-sk-hynix-drop-after-us-makes-it-harder-make-chips-china-2025-09-01/?utm_source=chatgpt.com)

[1]: https://www.reuters.com/markets/hedge-funds-turn-south-korea-next-wave-ai-2024-07-11/?utm_source=chatgpt.com "Hedge funds turn to South Korea for next wave in AI"
[2]: https://www.reuters.com/technology/samsung-flags-15-fold-rise-second-quarter-profit-chip-prices-climb-2024-07-04/?utm_source=chatgpt.com "Samsung flags better-than-expected profit rise as AI boom lifts chip prices"
[3]: https://www.reuters.com/markets/asia/hanwha-aerospace-spin-off-semiconductor-equipment-unit-2024-04-05/?utm_source=chatgpt.com "South Korea's Hanwha Aerospace to spin off industrial solutions businesses from defence"
[4]: https://www.reuters.com/technology/artificial-intelligence/south-korean-ai-chip-developers-rebellions-sapeon-merge-2024-06-12/?utm_source=chatgpt.com "South Korean AI chip developers Rebellions and Sapeon to merge"
[5]: https://www.marketwatch.com/story/a-british-tech-company-is-going-public-in-south-korea-the-ceo-explains-why-5bf0c593?utm_source=chatgpt.com "A British tech company is going public - in South Korea. The CEO explains why."
[6]: https://www.reuters.com/world/asia-pacific/south-korea-consider-setting-up-31-bln-foundry-grow-local-chip-sector-2025-12-10/?utm_source=chatgpt.com "South Korea to consider setting up $3.1 bln foundry to grow local chip sector"
[7]: https://www.reuters.com/business/media-telecom/nvidia-supply-more-than-260000-blackwell-ai-chips-south-korea-2025-10-31/?utm_source=chatgpt.com "Nvidia to supply more than 260,000 Blackwell AI chips to South Korea"
[8]: https://www.reuters.com/world/china/shares-samsung-sk-hynix-drop-after-us-makes-it-harder-make-chips-china-2025-09-01/?utm_source=chatgpt.com "Shares in Samsung, SK Hynix drop after US makes it harder to make chips in China"
