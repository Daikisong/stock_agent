순서상 이번은 **R2 Loop 14 — AI·반도체·전자부품 가격경로 검증 라운드**다.

```text
round = R2 Loop 14
round_id = round_212
large_sector = AI_SEMICONDUCTOR_ELECTRONIC_COMPONENTS
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = false
hard_4c_watch_confirmed = true
next_round = R3 Loop 14
```

이번 R2는 **SK하이닉스 HBM, 삼성전자 HBM·파업·중국규제, 한미반도체 TC bonder, LG이노텍 Apple AI iPhone, LG디스플레이 OLED 전환, Rebellions/Sapeon AI chip, Samsung/SK OpenAI Stargate, LG전자 소비가전·부품비용**을 본다.

이번 환경에서도 KRX/Naver/Yahoo/Stooq 기준의 **수정주가 일봉 OHLC 전체 구간**은 안정적으로 확보하지 못했다. 그래서 30D/90D/180D/1Y full MFE·MAE는 임의로 만들지 않고, Reuters / WSJ / MarketWatch / FT가 제공한 **event return, event price, target price, 영업이익, 계약·투자·valuation, 시장점유율, strike·export-control risk**를 가격 anchor로 사용한다. full OHLC가 필요한 칸은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R2 = AI·반도체·전자부품
```

R2에서 진짜 Stage 3는 “AI”, “HBM”, “Nvidia”, “OpenAI”, “on-device AI”, “Apple”, “OLED”, “AI chip startup”, “반도체 장비”라는 단어가 아니다.

진짜 Stage 3는 아래가 같이 닫히는 순간이다.

```text
메모리:
HBM allocation → 실제 고객 납품 → ASP → DRAM mix → OP margin → capex/wafer trade-off → 공급계약 지속성

장비:
고객사 capex → 실제 PO → 납품 → revenue recognition → gross margin → 고객 다변화

부품:
AI device narrative → 실제 출하량 → ASP / mix → 부품 탑재량 → 마진 → 재고 리스크

디스플레이:
LCD exit / OLED 전환 → 고객 수요 → capex → utilization → 흑자 전환 → 현금흐름

fabless / AI chip:
MOU / merger / valuation → tape-out → 양산 → 실제 고객 inference workload → 매출 / margin
```

---

# 2. 대상 canonical archetype

```text
HBM_DOMINANCE_STAGE3_AND_4B
SAMSUNG_HBM_CATCHUP_AND_LABOR_4C_WATCH
TC_BONDER_HBM_EQUIPMENT_EVENT_PREMIUM
ON_DEVICE_AI_IPHONE_COMPONENT_STAGE2
OLED_PORTFOLIO_RESTRUCTURING_STAGE2
KOREAN_AI_CHIP_FABLESS_STAGE2
AI_INFRA_MEMORY_SUPPLY_MOU_4B
CONSUMER_ELECTRONICS_COMPONENT_COST_4C_WATCH
```

---

# 3. deep sub-archetype

```text
HBM memory:
- SK Hynix
- Nvidia HBM3E supplier position
- HBM sold out / almost sold out
- record OP
- HBM market share / $1T market-cap approach
- 4B risk from valuation and crowding

Samsung:
- HBM lag / Nvidia qualification
- China HBM export restrictions
- Samsung $1T market cap rally
- strike / bonus dispute / supply disruption risk
- foundry / logic-chip loss drag

HBM equipment:
- Hanmi Semiconductor
- TSV-TC bonder
- SK Hynix contracts
- Micron rumor
- customer diversification vs unconfirmed deal risk

Apple AI components:
- LG Innotek
- iPhone 16 / Apple Intelligence / replacement cycle
- camera module and component demand
- evidence good but price failed

OLED/display:
- LG Display
- Guangzhou LCD sale
- OLED infrastructure investment
- LCD exit / OLED focus
- balance-sheet repair vs capex and utilization

Korean AI chip:
- Rebellions / Sapeon
- SK Telecom / SK Hynix / KT read-through
- NPU for LLM data centers
- merger and funding are Stage 2, not Green

AI infra MOU:
- Samsung / SK Hynix / OpenAI Stargate
- wafer demand / DRAM output absorption
- MOU vs binding take-or-pay order

Consumer electronics:
- LG Electronics
- weak TV / consumer demand
- component-cost inflation from memory shortage
- B2B/data-center cooling optionality not enough
```

---

# 4. 국장 신규 후보 case

## Case A — SK하이닉스 / HBM `structural_success + 4B-watch`

```text
symbol = 000660
case_type = structural_success + 4B-watch
archetype = HBM_DOMINANCE_STAGE3_AND_4B
```

### stage date

```text
Stage 1:
2024-03-26
- AI chip demand and HBM3E price/mix optimism appear clearly in market.
- SK Hynix and Hanmi Semiconductor rally together.
- SK Hynix is framed as a leading HBM supplier to Nvidia.

Stage 2:
2024-07-25
- SK Hynix reports Q2 OP 5.47T won, highest since Q3 2018.
- HBM demand expected to grow stronger.
- management says next-year HBM shipments could more than double.
- HBM chips were sold out for 2024 and almost sold out for 2025, per prior management comment cited by Reuters.
- SK Hynix shares had risen 47% YTD as of the day before report.

Stage 3 candidate:
2024-03~2024-07
- HBM demand, ASP/mix, Nvidia exposure and OP recovery align.
- 다만 Q2 실적 발표일에는 high expectation 때문에 주가가 장중 -8.4% 하락.

Stage 4B:
2026-01-28 / 2026-05-14
- Q4 2025 OP 19.2T won, +137% YoY, HBM sales more than doubled, HBM share 61%.
- shares +9% after hours, about +30% YTD after Q4 report.
- 2026년에는 SK Hynix shares +200% after +274% in 2025, market cap near $942B.
- 구조 성공은 맞지만 valuation/crowding 4B-watch 필요.
```

SK하이닉스는 R2의 구조 성공 case다. HBM은 단순 테마가 아니라 OP와 ASP/mix로 내려왔다. Reuters는 2024년 Q2 OP가 5.47T won으로 2018년 이후 최고였고, HBM 수요가 예상보다 강하며 다음 해 HBM shipment가 두 배 이상 늘 수 있다고 보도했다. 그러나 같은 실적 발표일 주가는 장중 -8.4% 하락했다. 즉 **Stage 3 gate는 작동했지만, 기대가 너무 높아지는 순간 4B가 같이 떠야 한다.** ([Reuters][1])

2026년에는 이 논리가 더 강해졌다. Reuters는 SK하이닉스가 Q4 2025 OP 19.2T won, +137% YoY를 기록했고, HBM 매출이 전년 대비 두 배 이상 늘었으며 HBM 시장점유율 61%를 기록했다고 보도했다. 동시에 2026년 주가가 이미 +200%, 2025년 +274% 뒤에 market cap 약 $942B까지 커졌다는 점은 4B-watch를 강화한다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "case_id": "r2_loop14_sk_hynix_hbm_dominance_stage3_4b",
  "symbol": "000660",
  "stage3_date_candidate": "2024-03-26_to_2024-07-25",
  "stage3_price": null,
  "price_data_source": "WSJ chip-rally anchor + Reuters earnings/market-cap anchors",
  "stage1_event_mfe_pct_2024_03_26": 4.3,
  "kospi_same_context_pct_2024_03_26": 0.7,
  "relative_outperformance_pp_2024_03_26": 3.6,
  "q2_2024_op_krw_trn": 5.47,
  "q2_2024_op_usd_bn": 3.96,
  "q2_2024_earnings_event_mae_pct": -8.4,
  "ytd_gain_before_q2_report_pct": 47,
  "q4_2025_op_krw_trn": 19.2,
  "q4_2025_op_growth_pct": 137,
  "q4_2025_analyst_expectation_krw_trn": 17.7,
  "hbm_market_share_q4_2025_pct": 61,
  "q4_2025_after_hours_mfe_pct": 9,
  "share_cancellation_krw_trn": 12.2,
  "treasury_share_cancellation_shares_mn": 15.3,
  "treasury_share_cancellation_outstanding_pct": 2.1,
  "share_gain_2025_pct": 274,
  "share_gain_2026_to_may_pct": 200,
  "market_cap_may_2026_usd_bn": 942,
  "mfe_30d_90d_180d_1y_2y": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = aligned_structural_but_4B_watch
rerating_result = HBM_dominance_stage3_candidate
stage_failure_type = expectations_and_valuation_overshoot_after_success
```

---

## Case B — 삼성전자 / HBM catch-up + strike risk `success_candidate + 4C-watch`

```text
symbol = 005930
case_type = success_candidate + 4C-watch
archetype = SAMSUNG_HBM_CATCHUP_AND_LABOR_4C_WATCH
```

### stage date

```text
Stage 1:
2024-10~2025-01
- Samsung falls behind SK Hynix in HBM / Nvidia qualification.
- investor concern rises over high-end AI memory competitiveness.

Stage 4C-watch:
2025-01-31
- Samsung warns Q1 AI-chip sales will be sluggish.
- U.S. export restrictions to China hurt HBM demand.
- Samsung relied on Chinese customers for about 20% of HBM sales, per analysts cited by Reuters.
- Samsung shares -2.8%.
- SK Hynix shares -9.6% in same broad chip selloff.

Stage 2 relief / catch-up:
2026-05-06
- Samsung market cap exceeds $1T.
- Samsung shares +12% in early trade and +14.4% in KOSPI 7,000 session.
- AI memory rally broadens beyond SK Hynix.

Stage 4C-watch 강화:
2026-05-12~19
- 50,000-worker strike risk / 18-day strike threat.
- semiconductors accounted for 37% of Korea exports in April.
- Samsung shares initially -6%, later +1.8% after ministerial meeting.
- SK Hynix +7.7% as possible beneficiary.
```

삼성전자는 R2에서 단순 success가 아니다. 2025년에는 HBM lag와 China export restriction이 명확한 4C-watch였다. Reuters는 Samsung이 Q1 AI chip sales 부진을 경고했고, 중국 고객이 HBM 매출의 약 20%였기 때문에 미국 수출규제 충격이 더 컸다고 보도했다. 그날 Samsung은 -2.8% 하락했다. ([Reuters][3])

2026년에는 AI rally 덕분에 Samsung이 $1T market cap을 넘었고, KOSPI 7,000 session에서 Samsung +14.4%, SK Hynix +10.6%가 나왔다. 하지만 곧바로 노조 파업 risk가 붙었다. Reuters는 semiconductors가 2026년 4월 한국 수출의 37%였고, Samsung strike threat 때문에 Samsung이 장중 -6%까지 밀렸다가 ministerial meeting 이후 +1.8%로 마감했으며, SK Hynix는 +7.7% 올랐다고 보도했다. ([Reuters][4])

### 실제 가격경로 검증

```json
{
  "case_id": "r2_loop14_samsung_hbm_catchup_labor_4c_watch",
  "symbol": "005930",
  "stage2_date": "2026-05-06",
  "stage4c_watch_date": "2025-01-31/2026-05-12",
  "stage3_price": null,
  "price_data_source": "Reuters Samsung HBM/export restriction, KOSPI 7000 and strike anchors",
  "hbm_china_customer_share_context_pct": 20,
  "q1_2025_ai_chip_warning_event_mae_pct": -2.8,
  "sk_hynix_same_context_mae_pct": -9.6,
  "samsung_1t_marketcap_event_mfe_pct": 12.0,
  "kospi_7000_session_samsung_mfe_pct": 14.4,
  "kospi_7000_session_sk_hynix_mfe_pct": 10.6,
  "samsung_market_cap_may_2026_usd_trn": 1.0,
  "semiconductor_export_share_apr_2026_pct": 37,
  "strike_threat_workers": 50000,
  "strike_duration_days": 18,
  "strike_news_intraday_mae_pct": -6.0,
  "strike_news_close_mfe_pct": 1.8,
  "sk_hynix_same_strike_context_mfe_pct": 7.7,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_with_hard_gate
rerating_result = Samsung_HBM_catchup_stage2
stage_failure_type = HBM_lag_China_restriction_labor_continuity_gate
```

---

## Case C — 한미반도체 / TC bonder `structural_success_candidate + rumor 4B`

```text
symbol = 042700
case_type = structural_success_candidate + 4B-watch
archetype = TC_BONDER_HBM_EQUIPMENT_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2024-03-26
- Hanmi rallies with SK Hynix on AI HBM demand.
- Hanmi supplies TSV-TC bonders and HBM packaging equipment to SK Hynix.

Stage 2:
2024-03-26
- Hanmi +16%, KOSPI +0.7%.
- Hanmi recently signed 21.48B won supply deal with SK Hynix.
- recent contract wins total around 200B won.

Stage 4B:
2024-03-28
- Hanmi rises as much as +22% to 139,100 won.
- rally triggered by media reports of possible Micron supply deal.
- Hanmi/Micron not confirmed.
- Kospi -0.3%.
```

한미반도체는 R2 장비주의 좋은 success_candidate지만, 루머와 실제 계약을 분리해야 한다. WSJ는 Hanmi가 SK Hynix와 21.48B won 공급계약을 맺었고 최근 계약들이 약 200B won 규모였다고 보도했다. 이는 Stage 2로 강하다. 다만 이틀 뒤 Micron deal 보도만으로 주가가 장중 +22%까지 오른 것은 4B-watch다. 실제 PO와 납품, revenue recognition, gross margin이 확인되어야 Stage 3다. ([월스트리트저널][5])

### 실제 가격경로 검증

```json
{
  "case_id": "r2_loop14_hanmi_tc_bonder_hbm_equipment_4b",
  "symbol": "042700",
  "stage2_date": "2024-03-26",
  "stage4b_date": "2024-03-28",
  "stage3_price": null,
  "price_data_source": "WSJ Hanmi HBM equipment and Micron-rumor event anchors",
  "stage2_event_mfe_pct": 16.0,
  "kospi_stage2_context_pct": 0.7,
  "sk_hynix_supply_deal_krw_bn": 21.48,
  "recent_contract_wins_total_krw_bn": 200,
  "micron_rumor_event_high_price_krw": 139100,
  "micron_rumor_event_mfe_pct": 22.0,
  "kospi_micron_rumor_context_pct": -0.3,
  "relative_outperformance_micron_rumor_pp": 22.3,
  "micron_deal_confirmed_at_source_date": false,
  "shipment_revenue_confirmed": false,
  "mfe_30d_90d_180d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_but_4B_watch
rerating_result = HBM_equipment_TC_bonder_stage2
stage_failure_type = Micron_rumor_not_customer_PO_green
```

---

## Case D — LG이노텍 / Apple Intelligence iPhone cycle `evidence_good_but_price_failed`

```text
symbol = 011070
case_type = evidence_good_but_price_failed
archetype = ON_DEVICE_AI_IPHONE_COMPONENT_STAGE2
```

### stage date

```text
Stage 1:
2024-06-27
- Apple Intelligence and iPhone 16 replacement cycle expected to lift component demand.
- LG Innotek camera/module exposure becomes Stage 2 candidate.

Stage 2:
2024-06-27
- Mirae expects 2Q OP 106.4B won.
- consensus was 81.1B won.
- estimate is 31% above consensus.
- target price raised 18% to 330,000 won.

Stage 3:
없음
- shares were -0.4% at 272,000 won on the same report.
- AI iPhone narrative did not get price confirmation.
```

LG이노텍은 R2 부품주에서 좋은 `evidence_good_but_price_failed`다. Apple Intelligence와 iPhone 교체주기 기대가 있었고, OP estimate는 consensus보다 31% 높았다. 그런데 주가는 272,000원에서 -0.4%였다. 즉 on-device AI narrative는 Stage 2지만, 실제 iPhone sell-through, component mix, inventory, margin 확인 전에는 Green이 아니다. ([마켓워치][6])

### 실제 가격경로 검증

```json
{
  "case_id": "r2_loop14_lg_innotek_ai_iphone_component_price_failed",
  "symbol": "011070",
  "stage2_date": "2024-06-27",
  "stage3_price": null,
  "price_data_source": "MarketWatch/Dow Jones LG Innotek event anchor",
  "event_price_krw": 272000,
  "event_mae_pct": -0.4,
  "q2_op_estimate_krw_bn": 106.4,
  "q2_op_consensus_krw_bn": 81.1,
  "op_estimate_above_consensus_pct": 31.2,
  "target_price_krw": 330000,
  "target_price_raise_pct": 18,
  "target_upside_from_event_price_pct": 21.3,
  "ai_iphone_sellthrough_confirmed": false,
  "component_mix_margin_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed
rerating_result = on_device_AI_iPhone_component_stage2
stage_failure_type = AI_iPhone_expectation_not_component_margin_green
```

---

## Case E — LG디스플레이 / OLED 전환 `success_candidate + capex/utilization gate`

```text
symbol = 034220
case_type = success_candidate
archetype = OLED_PORTFOLIO_RESTRUCTURING_STAGE2
```

### stage date

```text
Stage 1:
2024-09-26
- LG Display exits large LCD production in China.
- strategic shift toward higher-margin OLED.

Stage 2:
2024-09-26
- sells Guangzhou LCD plant to TCL CSOT for 10.8B yuan / $1.54B.
- sale includes 80% stake in large LCD panel plant and 100% of LCD module plant.
- expected completion March 2025.
- proceeds intended to improve financial stability.
- OLED focus becomes clearer.

Stage 2 추가:
2026-04-22
- announces 1.1T won / $744.94M OLED infrastructure investment.
- investment period: April 2026 to June 2028.

Stage 3:
없음
- LCD exit / OLED capex is Stage 2.
- Green requires OLED utilization, customer demand, panel ASP, margin and FCF.
```

LG디스플레이는 R2 전자부품/디스플레이의 구조조정 후보지만, 아직 Stage 3가 아니다. Reuters는 Guangzhou LCD plant sale이 $1.54B 규모이고, LGD가 OLED 중심으로 경쟁력과 재무안정성을 높이려 한다고 보도했다. 이후 2026년에는 1.1T won OLED infrastructure investment가 나왔다. 그러나 OLED capex는 utilization과 고객 수요가 없으면 비용이다. ([Reuters][7])

### 실제 가격경로 검증

```json
{
  "case_id": "r2_loop14_lg_display_oled_restructuring_stage2",
  "symbol": "034220",
  "stage2_date": "2024-09-26/2026-04-22",
  "stage3_price": null,
  "price_data_source": "Reuters LCD sale and OLED capex anchors",
  "guangzhou_lcd_sale_cny_bn": 10.8,
  "guangzhou_lcd_sale_usd_bn": 1.54,
  "large_lcd_panel_stake_sold_pct": 80,
  "lcd_module_plant_stake_sold_pct": 100,
  "expected_completion": "2025-03",
  "oled_infrastructure_investment_krw_trn": 1.1,
  "oled_infrastructure_investment_usd_mn": 744.94,
  "investment_period": "2026-04_to_2028-06",
  "oled_utilization_confirmed": false,
  "oled_margin_confirmed": false,
  "direct_event_return": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_but_capex_gate
rerating_result = OLED_portfolio_restructuring_stage2
stage_failure_type = LCD_exit_OLED_capex_not_utilization_green
```

---

## Case F — Rebellions / Sapeon `Korean AI chip Stage 2, listed read-through insufficient`

```text
symbols = 017670 / 030200 / 000660 read-through
case_type = success_candidate + insufficient_evidence
archetype = KOREAN_AI_CHIP_FABLESS_STAGE2
```

### stage date

```text
Stage 1:
2024-06-12
- Rebellions and Sapeon pursue merger.
- South Korea attempts to build domestic AI chip champion.
- SK Telecom is Sapeon parent; SK Hynix is among Sapeon shareholders.

Stage 2:
2024-08-18
- definitive merger agreement signed.
- merged company targets NPU market.
- Rebellions received $15M from Saudi Aramco VC arm.
- total funding exceeds $225M.
- Rebellions' ATOM was first South Korean NPU used in data center for LLM and entered mass production.

Stage 3:
없음
- unlisted AI-chip merger is not listed-stock Green.
- Green requires tape-out, volume production, customer workloads, inference revenue, gross margin.
```

Rebellions/Sapeon은 R2에서 중요한 국내 AI chip Stage 2다. 하지만 국장 상장주 scoring에서는 조심해야 한다. Reuters는 SK Telecom의 Sapeon과 Rebellions가 Nvidia에 도전하기 위해 merger를 추진했고, Rebellions가 LLM data center에 사용된 국내 NPU를 양산했다고 보도했다. 이후 definitive merger도 체결됐다. 그러나 SKT/KT/SK Hynix read-through로 바로 Green을 주면 안 된다. 실제 AI chip 매출, 고객 workload, gross margin이 필요하다. ([Reuters][8])

### 실제 가격경로 검증

```json
{
  "case_id": "r2_loop14_rebellions_sapeon_korean_ai_chip_stage2",
  "symbols": "017670/030200/000660_readthrough",
  "stage2_date": "2024-06-12/2024-08-18",
  "stage3_price": null,
  "price_data_source": "Reuters Rebellions-Sapeon merger anchors",
  "sapeon_parent": "SK Telecom",
  "sapeon_shareholders_include": ["SK Telecom", "SK Hynix"],
  "merger_definitive_agreement_date": "2024-08-18",
  "waed_ventures_investment_usd_mn": 15,
  "total_funding_usd_mn": 225,
  "atom_chip_status": "first South Korean NPU used in data center for LLM; entered mass production",
  "listed_stock_direct_revenue_confirmed": false,
  "customer_workload_revenue_confirmed": false,
  "direct_event_price_anchor": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_but_insufficient_evidence
rerating_result = Korean_AI_chip_fabless_stage2
stage_failure_type = unlisted_AI_chip_merger_not_listed_EPS_green
```

---

## Case G — Samsung/SK Hynix / OpenAI Stargate `AI infra MOU 4B-watch`

```text
symbols = 005930 / 000660
case_type = event_premium + 4B-watch
archetype = AI_INFRA_MEMORY_SUPPLY_MOU_4B
```

### stage date

```text
Stage 1:
2025-10
- Samsung and SK Hynix sign LOI with OpenAI.
- Stargate AI data-center project becomes Korean memory demand catalyst.

Stage 2:
2025-10
- SK Hynix shares rise as much as +12%, finish +10%.
- Samsung gains +3.5%.
- OpenAI demand mentioned: up to 900,000 DRAM wafers/month.
- more than twice current HBM industry capacity in FT summary.
- Samsung to contribute through memory and floating data-center-related subsidiaries.

Stage 4B:
2025-10
- LOI/MOU and wafer-demand headline move price before binding take-or-pay contract and margin terms.
```

OpenAI Stargate는 R2에서 매우 강한 demand signal이지만, 아직 4B-watch다. FT는 OpenAI와의 LOI 이후 SK Hynix가 장중 +12%, 종가 +10%, Samsung이 +3.5% 올랐다고 보도했다. 또한 OpenAI가 월 900,000 DRAM wafer 수요를 만들 수 있다고 설명했다. 하지만 LOI와 실제 take-or-pay supply contract, ASP, capacity allocation, margin은 다르다. ([Financial Times][9])

### 실제 가격경로 검증

```json
{
  "case_id": "r2_loop14_samsung_sk_openai_stargate_memory_mou_4b",
  "symbols": "005930/000660",
  "stage2_date": "2025-10",
  "stage4b_date": "2025-10",
  "stage3_price": null,
  "price_data_source": "FT OpenAI Stargate LOI price-reaction anchor",
  "sk_hynix_intraday_mfe_pct": 12.0,
  "sk_hynix_close_mfe_pct": 10.0,
  "samsung_event_mfe_pct": 3.5,
  "openai_dram_wafer_demand_per_month": 900000,
  "demand_context": "more_than_twice_current_HBM_industry_capacity_in_source_summary",
  "binding_take_or_pay_contract_confirmed": false,
  "asp_margin_terms_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_4B_watch
rerating_result = AI_infra_memory_supply_MOU_stage2
stage_failure_type = LOI_wafer_demand_headline_not_binding_margin_green
```

---

## Case H — LG전자 / consumer electronics cost pressure `4C-watch`

```text
symbol = 066570
case_type = 4C-watch
archetype = CONSUMER_ELECTRONICS_COMPONENT_COST_4C_WATCH
```

### stage date

```text
Stage 1:
2025-2026
- AI memory shortage raises component costs across electronics.
- consumer electronics demand remains weak.
- LG Electronics attempts to shift toward B2B, subscriptions, platforms, data-center cooling.

Stage 4C-watch:
2026-01-30
- Q4 2025 net loss 725.90B won.
- revenue 23.852T won, +4.8% YoY.
- operating loss 109.00B won.
- first operating loss in nine years.
- media entertainment division annual operating loss 750.90B won.
- management flags semiconductor shortages and rising component costs.

Stage 3:
없음
- B2B/data-center cooling optionality is Stage 2.
- Green requires profitable mix shift, recurring platform revenue, component-cost pass-through, TV loss control.
```

LG전자는 R2의 반대편이다. AI memory shortage는 Samsung/SK Hynix에는 수혜지만, 전자제품 OEM에는 component-cost 4C가 된다. WSJ는 LG전자가 Q4 2025에 725.90B won 순손실과 109.00B won 영업손실을 냈고, 9년 만의 영업손실이라고 보도했다. 반도체 shortage와 부품비 상승도 불확실성으로 제시됐다. 즉 R2는 memory supplier와 device maker를 반대로 scoring해야 한다. ([월스트리트저널][10])

### 실제 가격경로 검증

```json
{
  "case_id": "r2_loop14_lg_electronics_component_cost_4c_watch",
  "symbol": "066570",
  "stage4c_watch_date": "2026-01-30",
  "stage3_price": null,
  "price_data_source": "WSJ LG Electronics earnings anchor",
  "q4_2025_net_loss_krw_bn": 725.90,
  "q4_2025_revenue_krw_trn": 23.852,
  "q4_2025_revenue_growth_pct": 4.8,
  "q4_2025_operating_loss_krw_bn": 109.00,
  "first_operating_loss_in_years": 9,
  "media_entertainment_annual_operating_loss_krw_bn": 750.90,
  "flagged_risks": ["semiconductor shortages", "rising component costs", "weak consumer demand"],
  "b2b_data_center_cooling_optional": true,
  "direct_event_return": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = consumer_electronics_component_cost_gate
stage_failure_type = AI_memory_shortage_benefits_suppliers_but_pressures_OEM_margin
```

---

# 5. 이번 R2 case별 stage date 요약

| case                | Stage 1           | Stage 2                  | Stage 3              | Stage 4B                  | Stage 4C                           |
| ------------------- | ----------------- | ------------------------ | -------------------- | ------------------------- | ---------------------------------- |
| SK Hynix HBM        | 2024-03-26        | 2024-07-25 / 2026-01     | 2024-03~07 candidate | 2026 valuation/crowding   | tariff/demand volatility watch     |
| Samsung Electronics | 2024-10~2025-01   | 2026-05-06               | N/A                  | AI rally                  | HBM lag / China / strike watch     |
| Hanmi Semiconductor | 2024-03-26        | SK Hynix contracts       | N/A                  | Micron rumor +22%         | customer concentration watch       |
| LG Innotek          | 2024-06-27        | Apple AI iPhone estimate | N/A                  | iPhone AI theme           | price failed                       |
| LG Display          | 2024-09 / 2026-04 | LCD sale / OLED capex    | N/A                  | OLED capex theme          | utilization/cashflow watch         |
| Rebellions/Sapeon   | 2024-06~08        | AI chip merger           | N/A                  | AI fabless theme          | listed EPS absent                  |
| Samsung/SK OpenAI   | 2025-10           | LOI / Stargate           | N/A                  | wafer-demand headline     | binding contract absent            |
| LG Electronics      | 2026-01-30        | B2B optionality          | N/A                  | data-center cooling theme | component-cost / weak demand watch |

---

# 6. 실제 가격경로 검증 총괄

| case              |                                    가격 anchor | 해석                             | 판정                             |
| ----------------- | -------------------------------------------: | ------------------------------ | ------------------------------ |
| SK Hynix          |            +4.3%, later Q2 -8.4%, 2026 +200% | 구조 성공 + 과열 4B                  | aligned_structural_but_4B      |
| Samsung           | 2025 -2.8%, 2026 +14.4%, strike -6% intraday | catch-up 가능하나 hard gate 많음     | success_candidate_4C_watch     |
| Hanmi             |                        +16%, then +22% rumor | 실제 계약은 Stage 2, 루머는 4B         | event_premium                  |
| LG Innotek        |              272,000원, -0.4%, target 330,000 | evidence good but price failed | evidence_good_but_price_failed |
| LG Display        |         $1.54B LCD sale, 1.1T won OLED capex | restructuring Stage 2          | success_candidate              |
| Rebellions/Sapeon |                       $225M+ funding, merger | unlisted AI chip Stage 2       | insufficient                   |
| OpenAI Stargate   |                       SK +10%, Samsung +3.5% | LOI 4B-watch                   | event_premium                  |
| LG Electronics    |     109B won operating loss, 725.9B net loss | AI memory shortage hurts OEM   | thesis_break_watch             |

---

# 7. score-price alignment 판정

```text
aligned:
- SK Hynix, structural but with 4B-watch.

structural_success_candidate:
- SK Hynix
- Hanmi Semiconductor, if actual PO / shipment / margin confirm.
- LG Display, if OLED utilization and cashflow confirm.

success_candidate:
- Samsung Electronics HBM catch-up
- Rebellions/Sapeon Korean AI chip
- LG Innotek Apple AI iPhone component cycle

evidence_good_but_price_failed:
- LG Innotek
- LS Electric-like pattern repeated in R2: estimate/target upgrade without price confirmation.
- SK Hynix Q2 2024 earnings day, because good earnings met overextended expectations.

event_premium:
- Hanmi Micron rumor
- Samsung/SK OpenAI Stargate LOI
- Samsung $1T/KOSPI 7,000 AI rally

price_moved_without_evidence:
- OpenAI wafer demand if treated as binding supply contract.
- Rebellions/Sapeon if treated as listed SKT/SK Hynix EPS.
- Hanmi Micron rumor before confirmed PO.
- Apple AI iPhone expectation before LG Innotek component margin.

thesis_break_watch:
- Samsung HBM China exposure / Nvidia qualification lag / strike risk.
- LG Electronics component-cost pressure.
- LG Display OLED capex without utilization.

hard_4C_confirmed:
- 없음.
```

---

# 8. 점수비중 교정

## 올릴 축

```text
actual_hbm_allocation +5
customer_delivery_and_calloff +5
HBM_ASP_mix_margin +5
capacity_utilization +5
equipment_PO_to_revenue +5
customer_diversification +4
device_sellthrough +5
component_mix_margin +5
OLED_utilization +5
labor_supply_continuity +5
```

### 왜 올리나

SK하이닉스는 HBM이 실제 OP와 점유율로 내려오며 Stage 3에 가까워졌다. 반면 한미반도체는 SK Hynix 계약은 강하지만 Micron rumor는 4B다. LG이노텍은 AI iPhone 기대와 목표가 상향에도 주가가 -0.4%였으므로 device sell-through와 component margin이 필요하다. Samsung은 HBM catch-up이 좋아도 China restriction과 strike가 hard gate다. LG전자는 AI memory shortage가 부품비용으로 역풍이 될 수 있음을 보여준다.

## 내릴 축

```text
AI_keyword_only -5
HBM_theme_without_customer_delivery -5
LOI_or_MOU_without_binding_contract -5
rumored_customer_PO -5
on_device_AI_expectation_only -5
capacity_capex_without_utilization -5
unlisted_AI_chip_readthrough -5
consumer_OEM_exposed_to_memory_cost -4
labor_disruption_risk -5
```

### 왜 내리나

R2에서 가장 큰 함정은 “AI라는 단어가 공급망 전체에 같은 방향으로 작동한다”고 보는 것이다. SK하이닉스에는 HBM shortage가 마진 수혜지만, LG전자 같은 OEM에는 부품비용 압박이다. OpenAI LOI는 수요 signal이지만, take-or-pay 계약이 아니다. Apple AI iPhone 기대도 부품사 margin으로 닫혀야 한다.

---

# 9. Green gate 강화 조건

```text
R2 Stage 3-Green 필수:
1. HBM은 고객 allocation / shipment / ASP / mix margin 확인.
2. 장비주는 actual PO / 납품 / revenue recognition 확인.
3. 고객 루머는 Green 금지.
4. MOU/LOI는 binding contract 전 Stage 2까지만.
5. on-device AI는 실제 device sell-through와 component content 확인.
6. OLED는 capex가 아니라 utilization과 cashflow 확인.
7. AI chip fabless는 tape-out, 양산, 고객 workload, inference revenue 확인.
8. OEM은 memory/component cost pass-through 확인.
9. strike / export restriction / China exposure를 hard gate로 반영.
```

---

# 10. 4B 조기감지 조건

```text
4B-watch:
- HBM leader가 1년 +200% 이상 상승.
- AI memory MOU/LOI로 +10% 이상 급등.
- 장비주가 unconfirmed customer rumor로 +20% 이상 급등.
- on-device AI iPhone expectation으로 부품주가 먼저 rerating.
- OLED capex / LCD exit만으로 흑자 전환 가정.
- unlisted AI chip merger를 상장사 EPS로 바로 연결.
- Samsung catch-up rally 뒤 strike/export-control risk 무시.
```

---

# 11. 4C hard gate 조건

```text
Hard 4C / strong watch:
- HBM qualification failure.
- export-control ban on HBM / AI chips.
- major customer call-off cancellation.
- strike or shutdown disrupting memory supply.
- capex without utilization causing cash burn.
- component-cost spike crushing OEM margins.
- foundry / logic-chip loss widening despite AI rally.
```

이번 R2 Loop 14에서는 직접 hard 4C는 확정하지 않는다. 대신 **Samsung HBM lag/China restriction/strike**, **LG Electronics component-cost pressure**, **Hanmi unconfirmed customer rumor**, **OpenAI LOI non-binding risk**를 strong 4C/4B watch로 둔다.

---

# 12. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 13. 레포 반영용 patch-ready 출력

## docs/round/round_212.md 요약

```md
# R2 Loop 14. AI / Semiconductor / Electronic Components Price Validation

이번 라운드는 R2 Loop 14 price-validation 라운드다.

핵심 결론:
- SK Hynix is structural HBM success but 4B-watch. Q2 2024 OP 5.47T won, highest since Q3 2018, HBM shipments expected to more than double, but shares dropped as much as -8.4% on the earnings day due to high expectations. Q4 2025 OP reached 19.2T won, HBM market share 61%, and shares were +200% in 2026 after +274% in 2025.
- Samsung Electronics is HBM catch-up success_candidate plus 4C-watch. In Jan 2025, Samsung warned of sluggish AI-chip sales due China restrictions and HBM qualification lag; shares -2.8%. In May 2026, Samsung reached $1T market cap and rose +14.4% during KOSPI 7,000 session, but strike risk and China exposure remain hard gates.
- Hanmi Semiconductor is HBM equipment success_candidate plus rumor 4B. Hanmi +16% on AI HBM rally and SK Hynix contract context, then +22% to 139,100 won on unconfirmed Micron deal reports.
- LG Innotek is evidence_good_but_price_failed. Apple AI iPhone cycle and 2Q OP estimate 106.4B won, 31% above consensus, but shares were -0.4% at 272,000 won.
- LG Display is OLED restructuring Stage 2. Guangzhou LCD sale $1.54B and later 1.1T won OLED capex support shift to OLED, but utilization and cashflow are not confirmed.
- Rebellions/Sapeon is Korean AI chip Stage 2, but listed read-through is insufficient. Merger and $225M+ funding are positive; tape-out, mass production, customer workload revenue and margin required.
- Samsung/SK Hynix OpenAI Stargate LOI is AI infrastructure 4B-watch. SK Hynix +10%, Samsung +3.5% after LOI; up to 900,000 DRAM wafers/month demand is not yet binding take-or-pay revenue.
- LG Electronics is consumer-electronics component-cost 4C-watch. Q4 2025 operating loss 109B won, net loss 725.9B won, first operating loss in nine years, with semiconductor shortages and component-cost risks flagged.
```

## docs/checkpoints/checkpoint_28a_round212_r2_loop14.md 요약

```md
# Checkpoint 28A Round 212 R2 Loop 14 AI Semiconductor Electronic Components Price Validation

## 반영 내용
- R2 Loop 14 price-validation 라운드를 추가했다.
- SK Hynix, Samsung Electronics, Hanmi Semiconductor, LG Innotek, LG Display, Rebellions/Sapeon, Samsung/SK OpenAI Stargate, LG Electronics를 비교했다.
- Reuters / WSJ / MarketWatch / FT anchors로 가능한 event MFE/MAE, stage price, OP, target price, deal/funding/capex metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- actual HBM allocation, customer delivery/call-off, HBM ASP/mix margin, capacity utilization, equipment PO-to-revenue, customer diversification, device sell-through, component mix margin, OLED utilization, labor supply continuity 가중치 강화.
- AI keyword-only, HBM theme without delivery, LOI/MOU without binding contract, rumored customer PO, on-device AI expectation-only, capacity capex without utilization, unlisted AI chip read-through 감점 강화.
```

## data/e2r_case_library/cases_r2_loop14_round212.jsonl 초안

```jsonl
{"case_id":"r2_loop14_sk_hynix_hbm_dominance_stage3_4b","symbol":"000660","company_name":"SK Hynix","case_type":"structural_success_4b_watch","primary_archetype":"HBM_DOMINANCE_STAGE3_AND_4B","stage3_date":"2024-03-26_to_2024-07-25_candidate","stage4b_date":"2026-01-28/2026-05-14","price_validation":{"price_data_source":"WSJ chip-rally anchor + Reuters earnings/market-cap anchors","stage3_price":null,"stage1_event_mfe_pct_2024_03_26":4.3,"kospi_same_context_pct_2024_03_26":0.7,"relative_outperformance_pp_2024_03_26":3.6,"q2_2024_op_krw_trn":5.47,"q2_2024_op_usd_bn":3.96,"q2_2024_earnings_event_mae_pct":-8.4,"ytd_gain_before_q2_report_pct":47,"q4_2025_op_krw_trn":19.2,"q4_2025_op_growth_pct":137,"q4_2025_analyst_expectation_krw_trn":17.7,"hbm_market_share_q4_2025_pct":61,"q4_2025_after_hours_mfe_pct":9,"share_cancellation_krw_trn":12.2,"treasury_share_cancellation_shares_mn":15.3,"share_gain_2025_pct":274,"share_gain_2026_to_may_pct":200,"market_cap_may_2026_usd_bn":942,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"aligned_structural_but_4B_watch","rerating_result":"HBM_dominance_stage3_candidate","notes":"HBM success is real, but valuation/crowding 4B must trigger after extreme rerating."}
{"case_id":"r2_loop14_samsung_hbm_catchup_labor_4c_watch","symbol":"005930","company_name":"Samsung Electronics","case_type":"success_candidate_4c_watch","primary_archetype":"SAMSUNG_HBM_CATCHUP_AND_LABOR_4C_WATCH","stage2_date":"2026-05-06","stage4c_date":"2025-01-31/2026-05-12_watch","price_validation":{"price_data_source":"Reuters Samsung HBM/export restriction, KOSPI 7000 and strike anchors","stage3_price":null,"hbm_china_customer_share_context_pct":20,"q1_2025_ai_chip_warning_event_mae_pct":-2.8,"sk_hynix_same_context_mae_pct":-9.6,"samsung_1t_marketcap_event_mfe_pct":12.0,"kospi_7000_session_samsung_mfe_pct":14.4,"kospi_7000_session_sk_hynix_mfe_pct":10.6,"samsung_market_cap_may_2026_usd_trn":1.0,"semiconductor_export_share_apr_2026_pct":37,"strike_threat_workers":50000,"strike_duration_days":18,"strike_news_intraday_mae_pct":-6.0,"strike_news_close_mfe_pct":1.8,"sk_hynix_same_strike_context_mfe_pct":7.7,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_with_hard_gate","rerating_result":"Samsung_HBM_catchup_stage2","notes":"Samsung AI memory catch-up needs qualification, export-control and labor-continuity gates."}
{"case_id":"r2_loop14_hanmi_tc_bonder_hbm_equipment_4b","symbol":"042700","company_name":"Hanmi Semiconductor","case_type":"success_candidate_4b_watch","primary_archetype":"TC_BONDER_HBM_EQUIPMENT_EVENT_PREMIUM","stage2_date":"2024-03-26","stage4b_date":"2024-03-28","price_validation":{"price_data_source":"WSJ Hanmi HBM equipment and Micron-rumor event anchors","stage3_price":null,"stage2_event_mfe_pct":16.0,"kospi_stage2_context_pct":0.7,"sk_hynix_supply_deal_krw_bn":21.48,"recent_contract_wins_total_krw_bn":200,"micron_rumor_event_high_price_krw":139100,"micron_rumor_event_mfe_pct":22.0,"kospi_micron_rumor_context_pct":-0.3,"relative_outperformance_micron_rumor_pp":22.3,"micron_deal_confirmed_at_source_date":false,"shipment_revenue_confirmed":false,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_but_4B_watch","rerating_result":"HBM_equipment_TC_bonder_stage2","notes":"Actual SK Hynix contracts are Stage 2; Micron rumor is not PO/revenue Green."}
{"case_id":"r2_loop14_lg_innotek_ai_iphone_component_price_failed","symbol":"011070","company_name":"LG Innotek","case_type":"evidence_good_but_price_failed","primary_archetype":"ON_DEVICE_AI_IPHONE_COMPONENT_STAGE2","stage2_date":"2024-06-27","price_validation":{"price_data_source":"MarketWatch/Dow Jones LG Innotek event anchor","stage3_price":null,"event_price_krw":272000,"event_mae_pct":-0.4,"q2_op_estimate_krw_bn":106.4,"q2_op_consensus_krw_bn":81.1,"op_estimate_above_consensus_pct":31.2,"target_price_krw":330000,"target_price_raise_pct":18,"target_upside_from_event_price_pct":21.3,"ai_iphone_sellthrough_confirmed":false,"component_mix_margin_confirmed":false,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"on_device_AI_iPhone_component_stage2","notes":"AI iPhone expectation and target raise did not get price confirmation; sell-through and margin required."}
{"case_id":"r2_loop14_lg_display_oled_restructuring_stage2","symbol":"034220","company_name":"LG Display","case_type":"success_candidate_capex_gate","primary_archetype":"OLED_PORTFOLIO_RESTRUCTURING_STAGE2","stage2_date":"2024-09-26/2026-04-22","price_validation":{"price_data_source":"Reuters LCD sale and OLED capex anchors","stage3_price":null,"guangzhou_lcd_sale_cny_bn":10.8,"guangzhou_lcd_sale_usd_bn":1.54,"large_lcd_panel_stake_sold_pct":80,"lcd_module_plant_stake_sold_pct":100,"expected_completion":"2025-03","oled_infrastructure_investment_krw_trn":1.1,"oled_infrastructure_investment_usd_mn":744.94,"investment_period":"2026-04_to_2028-06","oled_utilization_confirmed":false,"oled_margin_confirmed":false,"price_validation_status":"direct_event_return_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_capex_gate","rerating_result":"OLED_portfolio_restructuring_stage2","notes":"LCD exit and OLED capex are Stage 2; OLED utilization and FCF required."}
{"case_id":"r2_loop14_rebellions_sapeon_korean_ai_chip_stage2","symbol":"017670/030200/000660_readthrough","company_name":"Rebellions / Sapeon / SK Telecom-SK Hynix read-through","case_type":"success_candidate_insufficient_evidence","primary_archetype":"KOREAN_AI_CHIP_FABLESS_STAGE2","stage2_date":"2024-06-12/2024-08-18","price_validation":{"price_data_source":"Reuters Rebellions-Sapeon merger anchors","stage3_price":null,"sapeon_parent":"SK Telecom","sapeon_shareholders_include":["SK Telecom","SK Hynix"],"merger_definitive_agreement_date":"2024-08-18","waed_ventures_investment_usd_mn":15,"total_funding_usd_mn":225,"atom_chip_status":"first South Korean NPU used in data center for LLM; entered mass production","listed_stock_direct_revenue_confirmed":false,"customer_workload_revenue_confirmed":false,"direct_event_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_insufficient_evidence","rerating_result":"Korean_AI_chip_fabless_stage2","notes":"AI chip merger/funding is Stage 2; listed EPS and customer workload revenue absent."}
{"case_id":"r2_loop14_samsung_sk_openai_stargate_memory_mou_4b","symbol":"005930/000660","company_name":"Samsung Electronics / SK Hynix / OpenAI Stargate","case_type":"event_premium_4b_watch","primary_archetype":"AI_INFRA_MEMORY_SUPPLY_MOU_4B","stage2_date":"2025-10","stage4b_date":"2025-10","price_validation":{"price_data_source":"FT OpenAI Stargate LOI price-reaction anchor","stage3_price":null,"sk_hynix_intraday_mfe_pct":12.0,"sk_hynix_close_mfe_pct":10.0,"samsung_event_mfe_pct":3.5,"openai_dram_wafer_demand_per_month":900000,"demand_context":"more_than_twice_current_HBM_industry_capacity_in_source_summary","binding_take_or_pay_contract_confirmed":false,"asp_margin_terms_confirmed":false,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_4B_watch","rerating_result":"AI_infra_memory_supply_MOU_stage2","notes":"OpenAI LOI is powerful demand signal but not binding margin/call-off Green."}
{"case_id":"r2_loop14_lg_electronics_component_cost_4c_watch","symbol":"066570","company_name":"LG Electronics","case_type":"4c_watch","primary_archetype":"CONSUMER_ELECTRONICS_COMPONENT_COST_4C_WATCH","stage4c_date":"2026-01-30_watch","price_validation":{"price_data_source":"WSJ LG Electronics earnings anchor","stage3_price":null,"q4_2025_net_loss_krw_bn":725.90,"q4_2025_revenue_krw_trn":23.852,"q4_2025_revenue_growth_pct":4.8,"q4_2025_operating_loss_krw_bn":109.00,"first_operating_loss_in_years":9,"media_entertainment_annual_operating_loss_krw_bn":750.90,"flagged_risks":["semiconductor shortages","rising component costs","weak consumer demand"],"b2b_data_center_cooling_optional":true,"direct_event_return":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"consumer_electronics_component_cost_gate","notes":"AI memory shortage helps memory suppliers but can pressure OEM component costs and margins."}
```

## data/sector_taxonomy/score_weight_profiles_round212_r2_loop14_v1.csv 초안

```csv
archetype,actual_hbm_allocation,customer_delivery_calloff,hbm_asp_mix_margin,capacity_utilization,equipment_po_to_revenue,customer_diversification,device_sellthrough,component_mix_margin,oled_utilization,labor_supply_continuity,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
HBM_DOMINANCE_STAGE3_AND_4B,+5,+5,+5,+5,+0,+4,+0,+0,+0,+4,-2,+5,+4,SK Hynix HBM success is real but valuation/crowding 4B must trigger.
SAMSUNG_HBM_CATCHUP_AND_LABOR_4C_WATCH,+5,+5,+5,+5,+0,+4,+0,+0,+0,+5,-4,+5,+5,Samsung needs HBM qualification, China exposure and labor continuity gates.
TC_BONDER_HBM_EQUIPMENT_EVENT_PREMIUM,+3,+5,+4,+4,+5,+5,+0,+0,+0,+2,-5,+5,+4,Hanmi needs confirmed customer PO/shipment/revenue, not rumor.
ON_DEVICE_AI_IPHONE_COMPONENT_STAGE2,+0,+3,+0,+4,+0,+4,+5,+5,+0,+1,-5,+5,+3,LG Innotek needs actual iPhone sell-through and component margin.
OLED_PORTFOLIO_RESTRUCTURING_STAGE2,+0,+3,+0,+5,+0,+3,+4,+4,+5,+1,-4,+4,+3,LG Display LCD exit/OLED capex needs utilization and FCF.
KOREAN_AI_CHIP_FABLESS_STAGE2,+0,+5,+3,+4,+0,+5,+0,+0,+0,+2,-5,+5,+4,Rebellions/Sapeon needs tape-out, production, workload revenue and listed EPS bridge.
AI_INFRA_MEMORY_SUPPLY_MOU_4B,+5,+5,+5,+5,+0,+4,+0,+0,+0,+2,-5,+5,+4,OpenAI/Stargate LOI is demand signal, not binding take-or-pay Green.
CONSUMER_ELECTRONICS_COMPONENT_COST_4C_WATCH,+0,+2,+0,+3,+0,+2,+5,+5,+0,+1,0,+4,+4,LG Electronics shows memory shortage can hurt OEM margins.
```

---

# 이번 R2 Loop 14 결론

```text
1. SK하이닉스는 R2의 structural_success다.
   HBM demand, OP, market share, share cancellation까지 맞지만 2026년 과열 4B-watch가 필수다.

2. 삼성전자는 success_candidate이지만 gate가 더 많다.
   HBM catch-up, $1T rally는 좋지만 HBM China exposure, Nvidia qualification, strike risk가 남아 있다.

3. 한미반도체는 HBM equipment success_candidate다.
   실제 SK Hynix 계약은 Stage 2지만, Micron rumor +22%는 4B다.

4. LG이노텍은 evidence_good_but_price_failed다.
   Apple AI iPhone 기대와 OP estimate beat에도 주가가 -0.4%였다.

5. LG디스플레이는 OLED restructuring Stage 2다.
   LCD exit와 OLED capex는 좋지만 utilization과 FCF 전에는 Green이 아니다.

6. Rebellions/Sapeon은 Korean AI chip Stage 2다.
   merger와 funding은 좋지만 상장사 EPS로 바로 연결하면 안 된다.

7. OpenAI Stargate LOI는 demand signal이지만 4B-watch다.
   월 900,000 wafer headline은 binding take-or-pay 계약이 아니다.

8. LG전자는 AI memory shortage의 반대편이다.
   메모리 supplier에는 수혜지만 OEM에는 component-cost 4C가 될 수 있다.
```

한 문장으로 압축하면:

> **R2에서 진짜 Stage 3는 “AI·HBM·Nvidia·OpenAI·Apple AI·OLED·로봇칩이 좋다”가 아니라, 실제 고객 납품·ASP/mix·PO·revenue recognition·device sell-through·capacity utilization·component margin·labor continuity가 숫자로 닫히는 순간이다.**

[1]: https://www.reuters.com/technology/nvidia-supplier-sk-hynixs-q2-profit-soars-ai-boom-2024-07-24/ "https://www.reuters.com/technology/nvidia-supplier-sk-hynixs-q2-profit-soars-ai-boom-2024-07-24/"
[2]: https://www.reuters.com/world/asia-pacific/sk-hynix-posts-forecast-beating-q4-profit-huge-ai-demand-2026-01-28/ "https://www.reuters.com/world/asia-pacific/sk-hynix-posts-forecast-beating-q4-profit-huge-ai-demand-2026-01-28/"
[3]: https://www.reuters.com/technology/samsung-q4-profit-growth-slows-chip-issues-weigh-2025-01-31/ "https://www.reuters.com/technology/samsung-q4-profit-growth-slows-chip-issues-weigh-2025-01-31/"
[4]: https://www.reuters.com/world/asia-pacific/south-koreas-kospi-share-index-tops-7000-first-time-2026-05-06/ "https://www.reuters.com/world/asia-pacific/south-koreas-kospi-share-index-tops-7000-first-time-2026-05-06/"
[5]: https://www.wsj.com/articles/south-korean-chip-shares-rally-as-ai-frenzy-persists-260f9996 "https://www.wsj.com/articles/south-korean-chip-shares-rally-as-ai-frenzy-persists-260f9996"
[6]: https://www.marketwatch.com/story/lg-innotek-could-post-2q-earnings-beat-market-talk-534689b2 "https://www.marketwatch.com/story/lg-innotek-could-post-2q-earnings-beat-market-talk-534689b2"
[7]: https://www.reuters.com/markets/deals/lg-display-agrees-sale-chinese-lcd-plant-15-bln-2024-09-26/ "https://www.reuters.com/markets/deals/lg-display-agrees-sale-chinese-lcd-plant-15-bln-2024-09-26/"
[8]: https://www.reuters.com/technology/artificial-intelligence/south-korean-ai-chip-developers-rebellions-sapeon-merge-2024-06-12/ "https://www.reuters.com/technology/artificial-intelligence/south-korean-ai-chip-developers-rebellions-sapeon-merge-2024-06-12/"
[9]: https://www.ft.com/content/52193ddd-bb37-427a-94b2-197af50d1ee4 "https://www.ft.com/content/52193ddd-bb37-427a-94b2-197af50d1ee4"
[10]: https://www.wsj.com/business/earnings/lg-electronics-reports-first-quarterly-net-loss-in-a-year-784ddcc8 "https://www.wsj.com/business/earnings/lg-electronics-reports-first-quarterly-net-loss-in-a-year-784ddcc8"
