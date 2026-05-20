순서상 이번은 **R10 Loop 14 — 건설·부동산·건자재 가격경로 검증 라운드**다.

```text
round = R10 Loop 14
round_id = round_220
large_sector = CONSTRUCTION_REAL_ESTATE_BUILDING_MATERIALS
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true_for_construction_safety_and_PF_liquidity_reference
next_round = R11 Loop 14
```

이번 R10은 건설주를 “수주”로만 보지 않는다. R10에서 진짜 Stage 3는 **분양률, PF 상환, 원가율, 미청구공사, 품질·안전, 인허가, 금리, 건자재 스프레드**가 같이 닫힐 때다. 이번에도 KRX/Naver/Yahoo/Stooq의 수정주가 일봉 OHLC window는 안정적으로 확보하지 못했다. 따라서 30D/90D/180D/1Y/2Y full MFE·MAE는 만들지 않고, Reuters/WSJ/MarketWatch/AP가 보도한 **event return, event price, PF delinquency, 지원 패키지, tariff, order value, target price, safety-event facts**를 가격 anchor로 사용한다.

---

# 1. 이번 라운드 대섹터

```text
R10 = 건설·부동산·건자재
```

R10의 핵심 gate는 아래다.

```text
주택건설:
분양률 → PF 상환 → 공사원가율 → 미청구공사 → 입주/하자 리스크 → 현금회수

부동산:
거래량 → LTV/DSR → 금리 → 실수요/투기수요 구분 → 공급정책 → 개발 인허가

EPC/해외건설:
수주 → advance payment → cost escalation → working capital → completion margin → claim risk

건자재:
수요 물량 → 판매단가 → 원재료/전력비 → 관세/덤핑 → 재고 → spread

건설안전:
사고 → 영업정지/보상/재시공 → 브랜드 신뢰 → 수주잔고 훼손 → financing cost
```

---

# 2. 대상 canonical archetype

```text
PF_LIQUIDITY_HARD_4C_WATCH
REAL_ESTATE_POLICY_STAGE2_NOT_GREEN
CONSTRUCTION_SAFETY_HARD_4C
OVERSEAS_EPC_ORDER_4B_WATCH
NUCLEAR_CONSTRUCTION_EXPORT_STAGE2
BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING
BUILDING_MATERIAL_TARIFF_RELIEF_EVENT_PREMIUM
US_LOCALIZATION_CAPEX_FALSE_POSITIVE
```

---

# 3. deep sub-archetype

```text
PF / 부동산 금융:
- Taeyoung E&C workout reference
- real-estate PF delinquency rate
- 40.6T won SME/builders support
- 1T~5T won syndicated loan
- profitable project vs non-viable project sorting

부동산 정책:
- Seoul LTV tightening
- land-transaction permit zones
- reconstruction easing / state land supply
- rate-cut vs housing-price overheating

건설 안전:
- HDC Hyundai Development / Gwangju Hwajeong I-Park
- fatal collapse, substandard materials, unauthorized slab change
- brand/safety trust hard gate

해외 EPC:
- Samsung E&A / Saudi Aramco Fadhili
- $6B order, +8.5% event move
- order headline vs EPC margin and working capital

원전 건설:
- KHNP Czech nuclear tender
- Doosan Enerbility / KEPCO E&C read-through
- preferred bidder success vs EDF/Westinghouse legal challenge

건자재 / 철강:
- Hyundai Steel weak construction demand
- rebar price decline, net-profit estimate cut
- Chinese steel-plate anti-dumping relief
- U.S. $6B plant capex backlash
```

---

# 4. 국장 신규 후보 case

## Case A — Taeyoung E&C / real-estate PF liquidity `PF hard 4C-watch`

```text
symbol = 009410
case_type = hard_4c_watch
archetype = PF_LIQUIDITY_HARD_4C_WATCH
```

### stage date

```text
Stage 1:
2023-12
- Taeyoung Engineering & Construction says it plans to reschedule debt.
- market begins to price Korean construction PF liquidity risk.

Stage 4C-watch:
2024-03-27
- Korean government prepares 40.6T won / $30.3B support package for SMEs and builders.
- builders get liquidity support through expanded guarantees, additional loans, and market-stabilising fund.
- Reuters explicitly links the concern to Taeyoung E&C’s December debt-rescheduling plan.

Stage 4C-watch validation:
2024-05-13
- FSS tightens real-estate PF project assessment.
- PF delinquency rate rises to 2.70% at end-2023 from 1.19% a year earlier and 0.37% at end-2021.
- syndicated loan prepared: 1T won, expandable to 5T won.
```

Taeyoung/PF는 R10의 핵심 hard watch다. 건설사는 수주잔고가 있어도 PF가 막히면 현금흐름이 끊긴다. Reuters는 Taeyoung E&C의 2023년 12월 debt rescheduling이 다른 건설사의 liquidity concern으로 확산됐고, 2024년 3월 정부가 40.6T won 지원 패키지를 준비했다고 보도했다. 2024년 5월에는 real-estate PF delinquency가 2021년 말 0.37%에서 2023년 말 2.70%까지 올라 FSS가 assessment를 강화했다. ([Reuters][1])

### 실제 가격경로 검증

```json
{
  "case_id": "r10_loop14_taeyoung_pf_liquidity_hard_watch",
  "symbol": "009410",
  "stage1_date": "2023-12",
  "stage4c_watch_date": "2024-03-27/2024-05-13",
  "stage3_price": null,
  "price_data_source": "Reuters PF liquidity and restructuring anchors",
  "government_support_package_krw_trn": 40.6,
  "government_support_package_usd_bn": 30.3,
  "pf_delinquency_end_2021_pct": 0.37,
  "pf_delinquency_end_2022_pct": 1.19,
  "pf_delinquency_end_2023_pct": 2.70,
  "syndicated_loan_initial_krw_trn": 1,
  "syndicated_loan_max_krw_trn": 5,
  "taeyoung_direct_event_price": "price_data_unavailable_after_deep_search",
  "unavailable_reason": "Reuters located PF/Taeyoung liquidity facts, but accessible sources did not expose an adjusted daily OHLC window for 009410 around the workout/rescheduling event."
}
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = PF_LIQUIDITY_HARD_4C_WATCH
stage_failure_type = backlog_not_green_if_PF_cashflow_fails
```

---

## Case B — Seoul housing curbs / supply policy `real-estate policy Stage 2, not Green`

```text
symbols = construction_developers / REITs / housing-supply basket
case_type = policy_stage2 + 4B-watch
archetype = REAL_ESTATE_POLICY_STAGE2_NOT_GREEN
```

### stage date

```text
Stage 1:
2025-03-19
- Seoul tightens apartment trading rules in wealthy districts.
- Gangnam, Seocho, Songpa, Yongsan transactions require prior local-council permits until 2025-09-30.
- council can deny if purchase is not for primary residence.

Stage 2:
2025-09-07
- Seoul LTV in wealthy districts cut from 50% to 40%.
- government also plans to boost supply using land owned by state-run firms, including Korea Land & Housing Corporation.
- reconstruction rules to be streamlined.

Stage 4B-watch:
2025-10~2025-11
- BOK keeps policy rate at 2.50%, balancing weak construction/economy against housing-price and FX risks.
- construction industry remains in downturn from rising labour/equipment costs and Seoul housing shortage.
```

이 case는 “부동산 규제 완화/공급확대 = 건설주 Green”이 아니라는 row다. 거래허가제, LTV, 재건축 규제, LH 토지 활용은 Stage 2 정책이다. 건설주 Stage 3는 실제 인허가, 착공, 분양률, PF 조건, 원가율, 현금회수로 닫혀야 한다. Reuters는 2025년 9월 Seoul LTV를 50%에서 40%로 낮추는 동시에 LH 등 공공토지를 활용해 공급을 늘리겠다고 보도했다. 이후 BOK는 주택가격·환율 리스크 때문에 금리인하 여지를 제한적으로 봤고, 건설업은 인건비·장비비 상승과 공급부족 사이에 끼어 있다고 설명했다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "case_id": "r10_loop14_seoul_property_policy_stage2_not_green",
  "symbols": "construction_developers_REITs_basket",
  "stage1_date": "2025-03-19",
  "stage2_date": "2025-09-07",
  "stage4b_watch_date": "2025-10-23",
  "stage3_price": null,
  "price_data_source": "Reuters Seoul property-curb and BOK housing-risk anchors",
  "permit_zone_districts": ["Gangnam", "Seocho", "Songpa", "Yongsan"],
  "permit_requirement_until": "2025-09-30",
  "ltv_before_pct": 50,
  "ltv_after_pct": 40,
  "state_land_supply_channel": "Korea Land & Housing Corporation and other state-run companies",
  "bok_policy_rate_context_pct": 2.50,
  "kospi_context_2025_ytd_pct": 62,
  "direct_construction_stock_anchor": "price_data_unavailable_after_deep_search",
  "stage3_conditions": ["building permits", "starts", "pre-sale absorption", "PF refinancing", "cost margin", "cash collection"]
}
```

### alignment

```text
score_price_alignment = policy_stage2_not_green
rerating_result = REAL_ESTATE_POLICY_STAGE2
stage_failure_type = policy_supply_headline_not_presale_cashflow_green
```

---

## Case C — HDC Hyundai Development / Gwangju collapse `construction safety hard 4C reference`

```text
symbol = 294870
case_type = hard_4c_reference
archetype = CONSTRUCTION_SAFETY_HARD_4C
```

### stage date

```text
Stage 1:
2022-01-11
- Gwangju Hwajeong I-Park apartment exterior wall collapses during construction.
- six workers die.
- HDC Hyundai Development is investigated.

Stage 4C:
2022-01~2022-03
- investigation finds faulty construction methods and substandard materials.
- unauthorized change: 39th floor slab thickness reportedly 35cm instead of planned 15cm.
- HDC chairman resigns amid criticism.
- same company had also been implicated in 2021 Gwangju demolition collapse.

Stage 3:
없음
- apartment-brand order backlog is not Green when safety/quality trust breaks.
```

HDC/Gwangju는 R10 safety hard reference다. 건설사는 “분양률이 좋다”보다 **무너질 수 없는 것을 무너뜨리지 않는 능력**이 먼저다. 이 사고는 6명 사망, 정부 조사, 부실시공·자재 문제, 브랜드 신뢰 훼손으로 이어졌고, 건설 safety gate가 valuation보다 선행해야 한다는 기준을 만든다. 공개 검색으로는 해당 event의 조정 OHLC window를 안정적으로 확보하지 못했기 때문에 가격경로 수치는 unavailable 처리한다. ([위키백과][3])

### 실제 가격경로 검증

```json
{
  "case_id": "r10_loop14_hdc_gwangju_construction_safety_hard_4c",
  "symbol": "294870",
  "stage4c_date": "2022-01-11/2022-03-14",
  "stage3_price": null,
  "price_data_source": "Gwangju Hwajeong I-Park collapse public reference; adjusted OHLC unavailable",
  "fatalities": 6,
  "investigation_findings": ["faulty construction methods", "substandard materials"],
  "unauthorized_slab_change_context": "39th floor slab reportedly 35cm vs planned 15cm",
  "chairman_resignation": true,
  "prior_2021_gwangju_collapse_association": true,
  "direct_adjusted_ohlc": "price_data_unavailable_after_deep_search",
  "unavailable_reason": "Reliable event facts found, but no accessible source exposed adjusted daily OHLC for 294870 around the event in this environment."
}
```

### alignment

```text
score_price_alignment = thesis_break_reference
rerating_result = CONSTRUCTION_SAFETY_HARD_4C
stage_failure_type = fatal_quality_safety_event_overrides_housing_backlog
```

---

## Case D — Samsung E&A / Saudi Aramco Fadhili order `overseas EPC Stage 2 + 4B-watch`

```text
symbol = 028050
case_type = success_candidate + event_premium
archetype = OVERSEAS_EPC_ORDER_4B_WATCH
```

### stage date

```text
Stage 1:
2024-04-02
- Saudi Aramco Fadhili gas expansion order is announced.
- Samsung E&A gets major overseas plant-construction order.

Stage 2:
2024-04-03
- Samsung E&A contract value: around $6B.
- Aramco total Fadhili expansion project: $7.7B.
- gas-processing capacity to rise 60% to 4B cubic feet/day.
- sulfur production to increase by 2,300 metric tons/day.
- completion expected by November 2027.

Stage 4B:
2024-04-03
- Samsung E&A shares rise as much as +8.5% to 26,750 won.
- KOSPI -1.4%.
- KB Securities target price: 35,000 won.

Stage 3:
없음
- mega-order is Stage 2.
- Green requires advance payment, cost estimate lock-in, working capital, variation orders, claim risk, completion margin.
```

Samsung E&A는 “해외수주 headline은 Stage 2”라는 R10 EPC 기준이다. $6B order와 +8.5% event move는 강하지만, EPC는 착공 이후 원가·설계변경·미청구공사·claim이 본체다. 주가는 KOSPI -1.4%에서 +8.5%로 반응했지만, 이는 order premium이지 completion-margin Green은 아니다. ([월스트리트저널][4])

### 실제 가격경로 검증

```json
{
  "case_id": "r10_loop14_samsung_ena_fadhili_epc_order_4b",
  "symbol": "028050",
  "stage2_date": "2024-04-03",
  "stage4b_date": "2024-04-03",
  "stage3_price": null,
  "price_data_source": "WSJ Samsung E&A Fadhili order event anchor",
  "contract_value_usd_bn": 6.0,
  "project_total_value_usd_bn": 7.7,
  "samsung_contract_share_of_project_pct": 77.9,
  "event_price_krw": 26750,
  "event_mfe_pct": 8.5,
  "kospi_same_context_pct": -1.4,
  "relative_outperformance_pp": 9.9,
  "target_price_krw": 35000,
  "target_upside_from_event_price_pct": 30.8,
  "gas_capacity_increase_pct": 60,
  "sulfur_production_increase_tpd": 2300,
  "completion_target": "2027-11",
  "mfe_30d_90d_180d_1y": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_success_candidate
rerating_result = OVERSEAS_EPC_ORDER_STAGE2
stage_failure_type = order_value_not_completion_margin_green
```

---

## Case E — Czech nuclear construction export / Doosan·KEPCO E&C read-through

```text
symbols = 034020 / 052690 / 051600 / KEPCO-KHNP read-through
case_type = success_candidate + legal_4C_watch
archetype = NUCLEAR_CONSTRUCTION_EXPORT_STAGE2
```

### stage date

```text
Stage 1:
2024-07-17
- Czech government picks KHNP as preferred bidder for two nuclear reactors.
- Korea wins first major overseas nuclear order since 2009.
- construction cost per unit estimated at around 200B Czech crowns / $8.65B.

Stage 2:
2024-07-17
- Reuters reports Doosan Enerbility shares had climbed 48% in three months partly on Czech hopes.
- KEPCO Plant S&E +14% and KEPCO E&C +41% over same period.
- final contract terms and value still to be negotiated.

Stage 4C-watch:
2024-10-31 / 2025-05-06
- Czech anti-monopoly office rejects appeals, but decisions not final.
- Czech court later temporarily blocks signing of at least $18B contract after EDF complaint.
- legal/tender execution risk remains.
```

Czech nuclear is R10의 “초대형 건설수출 Stage 2”다. Reuters는 KHNP가 preferred bidder로 선정됐고, Doosan Enerbility가 3개월간 +48%, KEPCO E&C가 +41% 올랐다고 보도했다. 하지만 final contract와 legal challenge가 남아 있다. 2025년에는 Czech court가 EDF complaint를 이유로 signing을 일시 차단했다. 즉 원전 수출은 강한 구조 후보지만 **preferred bidder ≠ booked margin**이다. ([Reuters][5])

### 실제 가격경로 검증

```json
{
  "case_id": "r10_loop14_czech_nuclear_construction_export_stage2",
  "symbols": "034020/052690/051600/KEPCO_KHNP_readthrough",
  "stage2_date": "2024-07-17",
  "stage4c_watch_date": "2024-10-31/2025-05-06",
  "stage3_price": null,
  "price_data_source": "Reuters Czech nuclear preferred-bidder and legal-challenge anchors",
  "reactors": 2,
  "estimated_cost_per_unit_czk_bn": 200,
  "estimated_cost_per_unit_usd_bn": 8.65,
  "khnp_status": "preferred_bidder",
  "first_major_overseas_nuclear_order_since": 2009,
  "doosan_enerbility_3m_gain_pct": 48,
  "kepco_plant_se_3m_gain_pct": 14,
  "kepco_ec_3m_gain_pct": 41,
  "court_blocked_contract_value_usd_bn_min": 18,
  "legal_challenge_party": "EDF",
  "final_contract_signed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_success_candidate
rerating_result = NUCLEAR_CONSTRUCTION_EXPORT_STAGE2
stage_failure_type = preferred_bidder_not_final_contract_margin_green
```

---

## Case F — Hyundai Steel / weak construction demand `building-material failed rerating`

```text
symbol = 004020
case_type = failed_rerating
archetype = BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING
```

### stage date

```text
Stage 1:
2024-06-21
- weak construction and shipbuilding demand hits Hyundai Steel estimates.
- reinforcing-bar demand/pricing becomes visible earnings risk.

Stage 4C-watch:
2024-06-21
- Nomura expects rebar price to decline 10% in 2024.
- 2024 net-profit estimate cut 73% to 215B won.
- target price cut 14% to 30,000 won.
- shares -1.2% to 29,000 won.

Stage 3:
없음
- 건자재 Green은 판매가격, 물량, 원가, 재고, construction starts가 같이 개선되어야 가능.
```

Hyundai Steel weak-demand case는 R10 건자재의 classic failed rerating이다. 철근 가격이 10% 하락할 수 있고 net profit estimate가 73% 깎였는데, 이건 건설경기 둔화가 건자재 P&L로 내려온 것이다. 건자재는 “중국 반덤핑”이나 “정책지원”보다 실제 착공·분양·원가·판매단가를 먼저 봐야 한다. ([마켓워치][6])

### 실제 가격경로 검증

```json
{
  "case_id": "r10_loop14_hyundai_steel_rebar_weak_construction_demand",
  "symbol": "004020",
  "stage4c_watch_date": "2024-06-21",
  "stage3_price": null,
  "price_data_source": "MarketWatch/Dow Jones Hyundai Steel weak-demand anchor",
  "event_price_krw": 29000,
  "event_mae_pct": -1.2,
  "rebar_price_decline_expected_pct": -10,
  "net_profit_estimate_after_cut_krw_bn": 215,
  "net_profit_estimate_cut_pct": -73,
  "implied_prior_net_profit_estimate_krw_bn": 796.3,
  "target_price_krw": 30000,
  "target_price_cut_pct": -14,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = failed_rerating
rerating_result = BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING
stage_failure_type = construction_demand_rebar_price_down
```

---

## Case G — Hyundai Steel / POSCO anti-dumping relief `building-material tariff event premium`

```text
symbols = 004020 / 005490
case_type = event_premium
archetype = BUILDING_MATERIAL_TARIFF_RELIEF_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2025-02-20
- South Korea provisionally decides to impose anti-dumping tariffs on Chinese steel plates.
- steel product used in shipbuilding and construction.
- concern: cheap Chinese steel imports hurting domestic producers.

Stage 2:
2025-02-20
- provisional tariff range: 27.91%~38.02%.
- 2024 Chinese steel imports to Korea: $10.4B.
- Chinese share of Korea steel imports: 49%.
- Hyundai Steel +5.8%.
- POSCO Holdings +3.9%.
- KOSPI -0.7%.

Stage 3:
없음
- tariff relief is Stage 2.
- Green requires ASP recovery, demand volume, raw-material cost, utilization, and margin.
```

이 case는 “정책 relief와 실제 spread를 분리하라”는 R10 building-material calibration이다. 반덤핑 관세로 현대제철 +5.8%, POSCO +3.9%가 나왔지만, 관세는 판매단가·물량·원가율로 내려와야 Green이다. construction demand가 약하면 tariff relief는 event premium에 그칠 수 있다. ([Reuters][7])

### 실제 가격경로 검증

```json
{
  "case_id": "r10_loop14_hyundai_posco_steel_plate_antidumping_event",
  "symbols": "004020/005490",
  "stage2_date": "2025-02-20",
  "stage3_price": null,
  "price_data_source": "Reuters steel-plate anti-dumping event anchor",
  "anti_dumping_tariff_pct": "27.91-38.02",
  "chinese_steel_imports_2024_usd_bn": 10.4,
  "chinese_share_of_korean_steel_imports_pct": 49,
  "hyundai_steel_event_mfe_pct": 5.8,
  "posco_event_mfe_pct": 3.9,
  "kospi_same_context_pct": -0.7,
  "hyundai_relative_outperformance_pp": 6.5,
  "posco_relative_outperformance_pp": 4.6,
  "steel_product_use": ["shipbuilding", "construction"],
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_policy_relief
rerating_result = BUILDING_MATERIAL_TARIFF_RELIEF_STAGE2
stage_failure_type = tariff_relief_not_ASP_volume_margin_green
```

---

## Case H — Hyundai Steel $6B U.S. plant `localization capex false positive`

```text
symbol = 004020
case_type = false_positive_score
archetype = US_LOCALIZATION_CAPEX_FALSE_POSITIVE
```

### stage date

```text
Stage 1:
2025-03-24
- Hyundai Motor Group announces broad U.S. investment package.
- Hyundai Steel included with $6B U.S. plant plan.
- rationale: fast-developing U.S. tariff situation.

Stage 4C-watch / false positive:
2025-04-22
- Hyundai Steel shares drop more than 21% after U.S. plant announcement.
- investors object to unclear funding and strategic details.
- project is part of $21B Hyundai Motor Group U.S. package.
- company says half of project may be funded by borrowing; POSCO equity input possible.
- weak domestic demand, cheap Chinese imports, labour disputes remain.
```

Hyundai Steel의 U.S. plant case는 “localization capex ≠ Green”의 정석이다. $6B U.S. plant는 tariff hedge처럼 보이지만, Reuters는 funding details가 불명확했고 투자자들이 반발해 주가가 21% 넘게 하락했다고 보도했다. 즉 R10에서 capex는 **수요·IRR·자금조달·원가·tariff saving**이 숫자로 닫혀야 Stage 3다. ([Reuters][8])

### 실제 가격경로 검증

```json
{
  "case_id": "r10_loop14_hyundai_steel_us_plant_capex_false_positive",
  "symbol": "004020",
  "stage4c_watch_date": "2025-04-22",
  "stage3_price": null,
  "price_data_source": "Reuters Hyundai Steel U.S. plant investor backlash anchor",
  "us_plant_investment_usd_bn": 6,
  "hyundai_group_us_package_usd_bn": 21,
  "stock_decline_after_announcement_pct": -21,
  "funding_plan_context": "half via borrowing; possible POSCO equity input",
  "risk_factors": ["unclear funding details", "tariff-policy uncertainty", "weak domestic demand", "cheap Chinese imports", "labour disputes"],
  "mfe_30d_90d": "N/A_no_valid_stage3",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = false_positive_score
rerating_result = US_LOCALIZATION_CAPEX_FALSE_POSITIVE
stage_failure_type = localization_capex_without_IRR_funding_clarity
```

---

# 5. 이번 R10 case별 stage date 요약

| case                      | Stage 1 | Stage 2               | Stage 3 | Stage 4B               | Stage 4C              |
| ------------------------- | ------- | --------------------- | ------- | ---------------------- | --------------------- |
| Taeyoung/PF               | 2023-12 | 2024 support          | N/A     | N/A                    | PF liquidity watch    |
| Seoul property policy     | 2025-03 | 2025-09 LTV/supply    | N/A     | policy rerating watch  | demand-credit watch   |
| HDC/Gwangju               | 2022-01 | N/A                   | N/A     | N/A                    | safety hard reference |
| Samsung E&A               | 2024-04 | $6B Fadhili order     | N/A     | +8.5%                  | EPC margin watch      |
| Czech nuclear             | 2024-07 | KHNP preferred bidder | N/A     | nuclear export premium | legal challenge watch |
| Hyundai Steel weak demand | 2024-06 | N/A                   | N/A     | N/A                    | rebar/demand failed   |
| Steel anti-dumping        | 2025-02 | tariff relief         | N/A     | +5.8/+3.9%             | demand/spread watch   |
| Hyundai Steel U.S. plant  | 2025-03 | capex plan            | N/A     | N/A                    | -21% capex backlash   |

---

# 6. 실제 가격경로 검증 총괄

| case                      |                                                   가격·사업 anchor | 해석                          | 판정                     |
| ------------------------- | -------------------------------------------------------------: | --------------------------- | ---------------------- |
| Taeyoung/PF               | PF delinquency 2.70%, support 40.6T won, syndicated loan 1T~5T | PF liquidity hard watch     | thesis_break_watch     |
| Seoul policy              |                         LTV 50%→40%, permit zones, supply push | policy Stage 2              | policy_stage2          |
| HDC/Gwangju               |          6 deaths, substandard materials, chairman resignation | safety hard reference       | thesis_break_reference |
| Samsung E&A               |                                   +8.5%, 26,750 won, $6B order | EPC order premium           | event_premium          |
| Czech nuclear             |          Doosan +48%, KEPCO E&C +41%, later $18B signing block | export construction Stage 2 | success_candidate      |
| Hyundai Steel weak demand |                            -1.2%, 29,000 won, NP estimate -73% | 건자재 failed rerating         | failed_rerating        |
| Steel anti-dumping        |                        Hyundai +5.8%, POSCO +3.9%, KOSPI -0.7% | tariff relief event         | event_premium          |
| Hyundai Steel U.S. plant  |                                stock -21% after $6B capex plan | capex false positive        | false_positive_score   |

---

# 7. score-price alignment 판정

```text
aligned:
- 없음. 이번 R10은 대부분 Stage 2 또는 4C-watch.

structural_success_candidate:
- Czech nuclear export, if final contract and EPC margin close.
- Samsung E&A Fadhili, if execution margin and working capital confirm.

success_candidate:
- Samsung E&A.
- Czech nuclear export.
- Seoul housing supply policy, if permits/starts/presales confirm.

failed_rerating:
- Hyundai Steel weak construction demand.
- Hyundai Steel U.S. plant capex backlash.

false_positive_score:
- Hyundai Steel $6B U.S. plant plan.
- Steel tariff relief if scored as final margin recovery.
- Seoul policy if scored as immediate builder Green.

event_premium:
- Samsung E&A +8.5% order move.
- Czech nuclear read-through gains.
- Steel anti-dumping relief.

price_moved_without_evidence:
- Policy support for builders before PF repayment/pre-sale absorption.
- Nuclear preferred-bidder rally before final contract.
- EPC mega-order rally before completion-margin proof.

thesis_break_watch:
- Taeyoung/PF liquidity.
- HDC/Gwangju construction safety.
- Hyundai Steel weak demand.
- Seoul property-credit tightening.

hard_4C_confirmed:
- construction safety hard reference: HDC/Gwangju.
- PF liquidity hard watch: Taeyoung/PF.
```

---

# 8. 점수비중 교정

## 올릴 축

```text
PF_repayment_visibility +5
presale_absorption +5
construction_cost_margin +5
unbilled_receivables_control +5
safety_quality_trust +5
completion_margin_visibility +5
working_capital_advance_payment +5
final_contract_signing +4
building_material_ASP_volume +5
capex_IRR_funding_clarity +5
```

### 왜 올리나

Taeyoung/PF는 건설사의 본체가 수주잔고가 아니라 PF 현금흐름이라는 점을 보여준다. HDC/Gwangju는 safety/quality가 hard gate임을 확인시킨다. Samsung E&A와 Czech nuclear는 수주와 preferred bidder가 Stage 2까지만 가능하다는 것을 보여준다. Hyundai Steel은 건자재 가격·수요·capex의 실제 경제성이 닫히지 않으면 정책 또는 투자 headline이 false positive가 될 수 있음을 보여준다.

## 내릴 축

```text
order_value_headline_only -5
policy_support_headline_only -5
property_supply_policy_only -5
preferred_bidder_without_final_contract -5
tariff_relief_without_ASP_margin -5
capex_localization_without_IRR -5
housing_price_rally_without_presales -5
backlog_without_PF_cashflow -5
safety_risk_unresolved -5
```

---

# 9. Green gate 강화 조건

```text
R10 Stage 3-Green 필수:
1. PF 상환 visibility와 refinancing cost 확인.
2. 분양률 / 입주율 / 미분양 재고 확인.
3. 공사원가율과 미청구공사 통제 확인.
4. 안전·품질 사고 / 하자충당금 / 영업정지 리스크 없음.
5. 해외 EPC는 final contract, advance payment, cost lock-in, claim risk 확인.
6. preferred bidder는 final contract 전 Stage 2까지만.
7. 건자재는 ASP, volume, raw-material/electricity cost, inventory 확인.
8. localization capex는 funding plan, IRR, tariff saving 확인.
9. price path가 evidence 이후 따라옴.
```

---

# 10. 4B 조기감지 조건

```text
4B-watch:
- 해외 EPC mega-order 발표 후 +5~10% 급등.
- 원전 preferred-bidder 뉴스로 관련주 30~50% 선반영.
- 반덤핑/관세 relief로 건자재주 급등.
- 정부 부동산 공급정책으로 건설주 선반영.
- 금리인하 기대만으로 REIT/건설주 rerating.
- capex/localization headline으로 IRR 전 상승.
```

---

# 11. 4C hard gate 조건

```text
Hard 4C:
- PF workout / debt rescheduling / liquidity support 의존.
- fatal construction safety event.
- major defect requiring reconstruction or compensation.
- business suspension / license risk after safety failure.
- pre-sale failure / unsold inventory spike.
- construction cost overrun and unbilled receivables surge.
- final contract blocked by legal/regulatory challenge.
- capex funding gap or dilution after localization plan.
```

이번 R10 Loop 14에서 직접 hard 4C는 **HDC/Gwangju construction safety reference**와 **Taeyoung/PF liquidity hard watch**다. Samsung E&A, Czech nuclear, steel anti-dumping은 hard 4C가 아니라 **Stage 2 / 4B-watch / event premium**이다.

---

# 12. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 13. 레포 반영용 patch-ready 출력

## docs/round/round_220.md 요약

```md
# R10 Loop 14. Construction / Real Estate / Building Materials Price Validation

이번 라운드는 R10 Loop 14 price-validation 라운드다.

핵심 결론:
- Taeyoung/PF liquidity is R10 hard 4C-watch. Korea prepared 40.6T won support for SMEs/builders and later tightened real-estate PF assessments as PF delinquency rose from 0.37% at end-2021 to 2.70% at end-2023. Backlog is not Green if PF repayment fails.
- Seoul property policy is Stage 2, not Green. Permit zones, LTV cut from 50% to 40%, state-land supply and reconstruction easing require actual permits, starts, pre-sale absorption, PF refinancing and cost-margin confirmation.
- HDC/Gwangju collapse is construction safety hard 4C reference. Six deaths, faulty construction methods, substandard materials, unauthorized slab-change context and chairman resignation make safety/quality trust a hard gate.
- Samsung E&A Fadhili is overseas EPC Stage 2 plus 4B-watch. $6B order, +8.5% move to 26,750 won vs KOSPI -1.4%, but Green requires advance payment, cost lock-in, working capital and completion margin.
- Czech nuclear construction export is success_candidate plus legal 4C-watch. KHNP preferred bidder; Doosan Enerbility +48%, KEPCO E&C +41% over three months, but final contract/legal challenge remains.
- Hyundai Steel weak construction demand is failed rerating. Rebar price expected -10%, net-profit estimate cut 73% to 215B won, target cut 14%, shares -1.2% at 29,000 won.
- Steel anti-dumping is building-material tariff event premium. Tariff range 27.91%~38.02%, Hyundai Steel +5.8%, POSCO +3.9%, KOSPI -0.7%. ASP, volume and spread required.
- Hyundai Steel $6B U.S. plant is localization capex false positive. Shares fell more than 21% after unclear funding/strategy; localization capex needs IRR, funding clarity and tariff-saving proof.
```

## docs/checkpoints/checkpoint_28a_round220_r10_loop14.md 요약

```md
# Checkpoint 28A Round 220 R10 Loop 14 Construction Real Estate Building Materials Price Validation

## 반영 내용
- R10 Loop 14 price-validation 라운드를 추가했다.
- Taeyoung/PF liquidity, Seoul property policy, HDC/Gwangju safety, Samsung E&A Fadhili EPC order, Czech nuclear construction export, Hyundai Steel weak demand, steel anti-dumping relief, Hyundai Steel U.S. plant capex를 비교했다.
- Reuters / WSJ / MarketWatch / AP anchors로 가능한 event MFE/MAE, event price, PF delinquency, support package, order value, tariff range, capex value, legal challenge metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- PF repayment visibility, pre-sale absorption, construction cost margin, unbilled receivables control, safety/quality trust, completion-margin visibility, working capital/advance payment, final contract signing, building-material ASP/volume, capex IRR/funding clarity 가중치 강화.
- order headline-only, policy support-only, property supply policy-only, preferred bidder without final contract, tariff relief without ASP/margin, localization capex without IRR, backlog without PF cashflow 감점 강화.
```

## data/e2r_case_library/cases_r10_loop14_round220.jsonl 초안

```jsonl
{"case_id":"r10_loop14_taeyoung_pf_liquidity_hard_watch","symbol":"009410","company_name":"Taeyoung Engineering & Construction / PF liquidity reference","case_type":"hard_4c_watch","primary_archetype":"PF_LIQUIDITY_HARD_4C_WATCH","stage1_date":"2023-12","stage4c_date":"2024-03-27/2024-05-13_watch","price_validation":{"price_data_source":"Reuters PF liquidity and restructuring anchors","stage3_price":null,"government_support_package_krw_trn":40.6,"government_support_package_usd_bn":30.3,"pf_delinquency_end_2021_pct":0.37,"pf_delinquency_end_2022_pct":1.19,"pf_delinquency_end_2023_pct":2.70,"syndicated_loan_initial_krw_trn":1,"syndicated_loan_max_krw_trn":5,"taeyoung_direct_event_price":"price_data_unavailable_after_deep_search","unavailable_reason":"Reuters located PF/Taeyoung liquidity facts, but accessible sources did not expose adjusted daily OHLC for 009410 around the event."},"score_price_alignment":"thesis_break_watch","rerating_result":"PF_LIQUIDITY_HARD_4C_WATCH","notes":"Backlog is not Green if PF repayment/refinancing cashflow fails."}
{"case_id":"r10_loop14_seoul_property_policy_stage2_not_green","symbol":"construction_developers_REITs_basket","company_name":"Seoul property policy / construction-developer basket","case_type":"policy_stage2_not_green","primary_archetype":"REAL_ESTATE_POLICY_STAGE2_NOT_GREEN","stage1_date":"2025-03-19","stage2_date":"2025-09-07","stage4b_date":"2025-10-23_watch","price_validation":{"price_data_source":"Reuters Seoul property-curb and BOK housing-risk anchors","stage3_price":null,"permit_zone_districts":["Gangnam","Seocho","Songpa","Yongsan"],"permit_requirement_until":"2025-09-30","ltv_before_pct":50,"ltv_after_pct":40,"state_land_supply_channel":"Korea Land & Housing Corporation and other state-run companies","bok_policy_rate_context_pct":2.50,"kospi_context_2025_ytd_pct":62,"direct_construction_stock_anchor":"price_data_unavailable_after_deep_search","stage3_conditions":["building permits","starts","pre-sale absorption","PF refinancing","cost margin","cash collection"]},"score_price_alignment":"policy_stage2_not_green","rerating_result":"REAL_ESTATE_POLICY_STAGE2","notes":"Policy supply/demand control is Stage 2; construction Green needs permits, starts, presales and PF cashflow."}
{"case_id":"r10_loop14_hdc_gwangju_construction_safety_hard_4c","symbol":"294870","company_name":"HDC Hyundai Development","case_type":"hard_4c_reference","primary_archetype":"CONSTRUCTION_SAFETY_HARD_4C","stage4c_date":"2022-01-11/2022-03-14","price_validation":{"price_data_source":"Gwangju Hwajeong I-Park collapse public reference; adjusted OHLC unavailable","stage3_price":null,"fatalities":6,"investigation_findings":["faulty construction methods","substandard materials"],"unauthorized_slab_change_context":"39th floor slab reportedly 35cm vs planned 15cm","chairman_resignation":true,"prior_2021_gwangju_collapse_association":true,"direct_adjusted_ohlc":"price_data_unavailable_after_deep_search","unavailable_reason":"Reliable event facts found, but no accessible source exposed adjusted daily OHLC for 294870 around the event in this environment."},"score_price_alignment":"thesis_break_reference","rerating_result":"CONSTRUCTION_SAFETY_HARD_4C","notes":"Fatal construction-quality event overrides housing backlog and brand premium."}
{"case_id":"r10_loop14_samsung_ena_fadhili_epc_order_4b","symbol":"028050","company_name":"Samsung E&A","case_type":"event_premium_success_candidate","primary_archetype":"OVERSEAS_EPC_ORDER_4B_WATCH","stage2_date":"2024-04-03","stage4b_date":"2024-04-03","price_validation":{"price_data_source":"WSJ Samsung E&A Fadhili order event anchor","stage3_price":null,"contract_value_usd_bn":6.0,"project_total_value_usd_bn":7.7,"samsung_contract_share_of_project_pct":77.9,"event_price_krw":26750,"event_mfe_pct":8.5,"kospi_same_context_pct":-1.4,"relative_outperformance_pp":9.9,"target_price_krw":35000,"target_upside_from_event_price_pct":30.8,"gas_capacity_increase_pct":60,"sulfur_production_increase_tpd":2300,"completion_target":"2027-11","mfe_30d_90d_180d_1y":"price_data_unavailable_after_deep_search","mae_30d_90d_180d_1y":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"OVERSEAS_EPC_ORDER_STAGE2","notes":"Mega-order is Stage 2; advance payment, cost lock-in, working capital and completion margin required."}
{"case_id":"r10_loop14_czech_nuclear_construction_export_stage2","symbol":"034020/052690/051600/KEPCO_KHNP_readthrough","company_name":"Doosan Enerbility / KEPCO E&C / KEPCO Plant S&E / KHNP","case_type":"success_candidate_legal_watch","primary_archetype":"NUCLEAR_CONSTRUCTION_EXPORT_STAGE2","stage2_date":"2024-07-17","stage4c_date":"2024-10-31/2025-05-06_watch","price_validation":{"price_data_source":"Reuters Czech nuclear preferred-bidder and legal-challenge anchors","stage3_price":null,"reactors":2,"estimated_cost_per_unit_czk_bn":200,"estimated_cost_per_unit_usd_bn":8.65,"khnp_status":"preferred_bidder","first_major_overseas_nuclear_order_since":2009,"doosan_enerbility_3m_gain_pct":48,"kepco_plant_se_3m_gain_pct":14,"kepco_ec_3m_gain_pct":41,"court_blocked_contract_value_usd_bn_min":18,"legal_challenge_party":"EDF","final_contract_signed":false,"mfe_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"NUCLEAR_CONSTRUCTION_EXPORT_STAGE2","notes":"Preferred bidder is not booked margin until final contract/legal challenge clears."}
{"case_id":"r10_loop14_hyundai_steel_rebar_weak_construction_demand","symbol":"004020","company_name":"Hyundai Steel","case_type":"failed_rerating","primary_archetype":"BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING","stage4c_date":"2024-06-21_watch","price_validation":{"price_data_source":"MarketWatch/Dow Jones Hyundai Steel weak-demand anchor","stage3_price":null,"event_price_krw":29000,"event_mae_pct":-1.2,"rebar_price_decline_expected_pct":-10,"net_profit_estimate_after_cut_krw_bn":215,"net_profit_estimate_cut_pct":-73,"implied_prior_net_profit_estimate_krw_bn":796.3,"target_price_krw":30000,"target_price_cut_pct":-14,"mfe_30d_90d":"price_data_unavailable_after_deep_search","mae_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"failed_rerating","rerating_result":"BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING","notes":"Weak construction demand and rebar-price decline damaged earnings estimates."}
{"case_id":"r10_loop14_hyundai_posco_steel_plate_antidumping_event","symbol":"004020/005490","company_name":"Hyundai Steel / POSCO Holdings","case_type":"event_premium_policy_relief","primary_archetype":"BUILDING_MATERIAL_TARIFF_RELIEF_EVENT_PREMIUM","stage2_date":"2025-02-20","price_validation":{"price_data_source":"Reuters steel-plate anti-dumping event anchor","stage3_price":null,"anti_dumping_tariff_pct":"27.91-38.02","chinese_steel_imports_2024_usd_bn":10.4,"chinese_share_of_korean_steel_imports_pct":49,"hyundai_steel_event_mfe_pct":5.8,"posco_event_mfe_pct":3.9,"kospi_same_context_pct":-0.7,"hyundai_relative_outperformance_pp":6.5,"posco_relative_outperformance_pp":4.6,"steel_product_use":["shipbuilding","construction"],"mfe_30d_90d":"price_data_unavailable_after_deep_search","mae_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_policy_relief","rerating_result":"BUILDING_MATERIAL_TARIFF_RELIEF_STAGE2","notes":"Tariff relief is not Green until ASP, volume, utilization and spread improve."}
{"case_id":"r10_loop14_hyundai_steel_us_plant_capex_false_positive","symbol":"004020","company_name":"Hyundai Steel","case_type":"false_positive_score","primary_archetype":"US_LOCALIZATION_CAPEX_FALSE_POSITIVE","stage4c_date":"2025-04-22_watch","price_validation":{"price_data_source":"Reuters Hyundai Steel U.S. plant investor backlash anchor","stage3_price":null,"us_plant_investment_usd_bn":6,"hyundai_group_us_package_usd_bn":21,"stock_decline_after_announcement_pct":-21,"funding_plan_context":"half via borrowing; possible POSCO equity input","risk_factors":["unclear funding details","tariff-policy uncertainty","weak domestic demand","cheap Chinese imports","labour disputes"],"mfe_30d_90d":"N/A_no_valid_stage3","mae_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"false_positive_score","rerating_result":"US_LOCALIZATION_CAPEX_FALSE_POSITIVE","notes":"Localization capex is not Green without funding clarity, IRR and tariff-saving proof."}
```

## data/sector_taxonomy/score_weight_profiles_round220_r10_loop14_v1.csv 초안

```csv
archetype,pf_repayment_visibility,presale_absorption,construction_cost_margin,unbilled_receivables_control,safety_quality_trust,completion_margin_visibility,working_capital_advance_payment,final_contract_signing,building_material_asp_volume,capex_irr_funding_clarity,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
PF_LIQUIDITY_HARD_4C_WATCH,+5,+5,+5,+5,+3,+2,+5,+1,+1,+4,0,+5,+5,Taeyoung/PF shows backlog is not Green if PF repayment/refinancing fails.
REAL_ESTATE_POLICY_STAGE2_NOT_GREEN,+4,+5,+5,+4,+2,+2,+3,+1,+2,+2,-5,+5,+4,Seoul property policy needs permits, starts, presales and PF cashflow.
CONSTRUCTION_SAFETY_HARD_4C,+3,+3,+4,+4,+5,+4,+3,+1,+1,+3,0,+4,+5,HDC/Gwangju confirms fatal quality/safety events override backlog.
OVERSEAS_EPC_ORDER_4B_WATCH,+2,+0,+5,+5,+3,+5,+5,+5,+1,+3,-5,+5,+4,Samsung E&A Fadhili order needs advance payment, working capital and completion margin.
NUCLEAR_CONSTRUCTION_EXPORT_STAGE2,+2,+0,+5,+5,+3,+5,+5,+5,+1,+4,-5,+5,+4,Czech nuclear preferred bidder needs final contract and legal clearance.
BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING,+1,+3,+4,+2,+1,+1,+1,+0,+5,+2,0,+4,+4,Hyundai Steel weak rebar demand shows ASP/volume must lead materials scoring.
BUILDING_MATERIAL_TARIFF_RELIEF_EVENT_PREMIUM,+1,+2,+4,+2,+1,+1,+1,+0,+5,+2,-5,+5,+3,Anti-dumping tariff relief needs ASP, volume and spread confirmation.
US_LOCALIZATION_CAPEX_FALSE_POSITIVE,+1,+1,+4,+3,+1,+2,+3,+2,+4,+5,0,+5,+4,Hyundai Steel U.S. plant shows capex headline needs funding clarity and IRR.
```

---

# 이번 R10 Loop 14 결론

```text
1. Taeyoung/PF는 R10 hard 4C-watch다.
   건설사는 수주잔고보다 PF 상환과 refinancing visibility가 먼저다.

2. Seoul property policy는 Stage 2다.
   LTV, 거래허가제, 공급확대는 실제 착공·분양률·PF cashflow 전에는 Green이 아니다.

3. HDC/Gwangju collapse는 construction safety hard reference다.
   safety/quality trust가 깨지면 backlog와 브랜드 premium을 즉시 덮는다.

4. Samsung E&A Fadhili는 해외 EPC success_candidate지만 4B-watch다.
   +8.5% event premium은 강하지만 completion margin과 working capital이 Stage 3 조건이다.

5. Czech nuclear는 원전 건설수출 Stage 2다.
   preferred bidder와 관련주 rerating은 강하지만 final contract와 legal risk가 남아 있다.

6. Hyundai Steel weak demand는 건자재 failed_rerating이다.
   rebar price -10%, net-profit estimate -73%는 건설경기 둔화가 소재 P&L로 내려온 증거다.

7. Steel anti-dumping은 event premium이다.
   tariff relief는 좋지만 ASP·volume·spread로 확인되어야 한다.

8. Hyundai Steel $6B U.S. plant는 false_positive_score다.
   localization capex가 funding clarity와 IRR 없이 발표되면 주가는 오히려 깨질 수 있다.
```

한 문장으로 압축하면:

> **R10에서 진짜 Stage 3는 “수주·정책·공급확대·원전·관세·미국공장 뉴스가 좋다”가 아니라, PF repayment·분양률·원가율·미청구공사·safety trust·advance payment·completion margin·건자재 ASP/volume·capex IRR이 실제 숫자로 닫히는 순간이다.**

[1]: https://www.reuters.com/markets/asia/south-korea-prepares-financial-support-small-businesses-builders-2024-03-27/?utm_source=chatgpt.com "South Korea prepares financial support for small businesses, builders"
[2]: https://www.reuters.com/markets/asia/south-korea-tighten-apartment-trading-rules-wealthy-seoul-districts-2025-03-19/?utm_source=chatgpt.com "South Korea to tighten apartment trading rules in wealthy Seoul districts"
[3]: https://en.wikipedia.org/wiki/Gwangju_Hwajeong_I-Park_exterior_wall_collapse?utm_source=chatgpt.com "Gwangju Hwajeong I-Park exterior wall collapse"
[4]: https://www.wsj.com/articles/samsung-e-a-shares-rise-on-6-billion-saudi-contract-win-10a5b2f4?utm_source=chatgpt.com "Samsung E&A Shares Rise on $6 Billion Saudi Contract Win"
[5]: https://www.reuters.com/business/energy/south-koreas-winning-bid-czech-nuclear-power-project-2024-07-17/?utm_source=chatgpt.com "South Korea's winning bid for Czech nuclear power project"
[6]: https://www.marketwatch.com/story/hyundai-steel-s-2024-earnings-could-be-hit-by-weak-demand-market-talk-bcbe77c8?utm_source=chatgpt.com "Hyundai Steel's 2024 Earnings Could Be Hit by Weak Demand -- Market Talk"
[7]: https://www.reuters.com/markets/asia/south-korea-provisionally-slaps-tariffs-chinese-steel-plates-dumping-2025-02-20/?utm_source=chatgpt.com "South Korea provisionally slaps tariffs on Chinese steel plates for dumping"
[8]: https://www.reuters.com/business/autos-transportation/hyundai-steels-6-bln-us-investment-draws-investor-ire-tests-seouls-tariff-2025-04-22/?utm_source=chatgpt.com "Hyundai Steel's $6 billion US investment draws investor ire, tests Seoul's tariff strategy"
