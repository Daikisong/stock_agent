순서상 이번은 **R4 Loop 14 — 소재·스프레드·전략자원 가격경로 검증 라운드**다.

```text
round = R4 Loop 14
round_id = round_214
large_sector = MATERIALS_SPREADS_STRATEGIC_RESOURCES
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true
next_round = R5 Loop 14
```

이번 R4는 **석유화학 oversupply, NCC 구조조정, 철강 spread, 중국 steel dumping, Korea Zinc control premium, lithium resource integration, lithium-price squeeze rally, L&F/Tesla 계약 붕괴, 희토류 export-control, cathode supply-chain rebalancing**을 본다.

이번에도 수정주가 일봉 OHLC 전체 window는 안정적으로 확보하지 못했다. 그래서 30D/90D/180D/1Y full MFE·MAE는 만들지 않고, Reuters / WSJ / MarketWatch가 제공한 **event return, event price, 영업손실, 계약금액, 지분율, tariff rate, 생산능력, export-control 수치**를 가격 anchor로 사용한다. full OHLC가 필요한 칸은 `price_data_unavailable_after_deep_search`로 명시한다.

---

# 1. 이번 라운드 대섹터

```text
R4 = 소재·스프레드·전략자원
```

R4에서 진짜 Stage 3는 “중국 경기부양”, “리튬 반등”, “철강 관세”, “석유화학 구조조정”, “전략광물”, “2차전지 소재”, “경영권 분쟁”이라는 단어가 아니다.

진짜 Stage 3는 아래가 닫히는 순간이다.

```text
석유화학:
NCC 가동률 → ethylene/propylene spread → 재고평가손 → 구조조정 후 supply cut → cash margin

철강:
중국산 dumping relief → 실제 판매단가 → 원재료/전력비 → 건설·조선 실수요 → spread

전략금속:
control premium → governance / dilution / capex / smelter safety / regulatory clearance

리튬:
광산 지분 → spodumene offtake → hydroxide plant utilization → lithium price → customer call-off

배터리 소재:
계약금액 → 실제 call-off → 고객 EV 생산계획 → ASP / inventory → margin

희토류:
export license → 실제 선적 → 대체 sourcing → defence/semiconductor/EV supply-chain continuity
```

---

# 2. 대상 canonical archetype

```text
PETROCHEMICAL_SPREAD_COLLAPSE_4C
PETROCHEMICAL_RESTRUCTURING_STAGE2_NOT_GREEN
STEEL_ANTI_DUMPING_EVENT_PREMIUM
STRATEGIC_METAL_CONTROL_PREMIUM_4B
LITHIUM_RESOURCE_INTEGRATION_STAGE2
LITHIUM_PRICE_SQUEEZE_EVENT_PREMIUM
BATTERY_MATERIAL_CONTRACT_COLLAPSE_HARD_4C
RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C
CATHODE_SUPPLY_CHAIN_REBALANCING_STAGE2
```

---

# 3. deep sub-archetype

```text
석유화학:
- Lotte Chemical / LG Chem
- Northeast Asia oversupply
- China and Middle East capacity expansion
- NCC shutdown / Daesan restructuring
- 2T won policy support
- capacity cut vs real spread recovery

철강:
- Hyundai Steel / POSCO Holdings
- rebar price decline
- Chinese steel-plate dumping
- anti-dumping tariff relief
- U.S. steel tariff export risk

전략금속:
- Korea Zinc / Young Poong / MBK
- zinc/non-ferrous smelter control premium
- tender offer / buyback / governance / safety dispute
- strategic metal premium vs operating cashflow

리튬:
- POSCO Holdings / Mineral Resources
- Wodgina / Mt Marion lithium mine exposure
- low lithium-price countercyclical acquisition
- spodumene offtake and processing utilization gate

리튬 squeeze:
- POSCO Future M / L&F / Samsung SDI / LGES
- CATL Yichun suspension
- lithium-price sentiment rally
- inventory valuation vs actual EV call-off

계약붕괴:
- L&F / Tesla 4680 cathode
- $2.9B expected contract value → $7,386
- customer-name headline vs actual material requirement

희토류:
- China export controls
- processed rare earths and magnets >90% China share
- defence users denied, advanced semiconductor case-by-case
- heavy rare-earth exports down ~50%

Cathode supply-chain:
- LG Chem cathode plant ownership rebalancing
- Toyota Tsusho 25% stake
- Huayou share diluted from 49% to 24%
- Exxon non-binding lithium supply up to 100,000t
```

---

# 4. 국장 신규 후보 case

## Case A — Lotte Chemical / LG Chem petrochemical spread collapse

```text
symbols = 011170 / 051910
case_type = failed_rerating + 4C-watch
archetype = PETROCHEMICAL_SPREAD_COLLAPSE_4C
```

### stage date

```text
Stage 1:
2024 full-year
- China / Middle East capacity expansion creates Northeast Asia petrochemical oversupply.
- weak China demand prevents spread recovery.

Stage 4C-watch:
2025-02-07
- Lotte Chemical 2024 operating loss: 895B won.
- loss widened about 157% YoY.
- largest operating loss since 2011.
- LG Chem 2024 OP: 916.8B won, down 63.75% YoY.
- LG Chem petrochemical division Q4 OP loss: 99B won.
- both companies cite global glut and oversupply.

Stage 3:
없음
- stimulus / restructuring 기대만으로 Green 금지.
- ethylene spread, utilization, cash margin 확인 필요.
```

석유화학은 이번 R4의 대표 failed rerating이다. Lotte Chemical은 2024년 895B won 영업손실을 냈고 손실폭이 전년 대비 약 157% 확대됐다. LG Chem도 2024년 영업이익이 916.8B won으로 63.75% 감소했으며, 석유화학 부문은 Q4에 99B won 영업손실을 냈다. 핵심 원인은 중국·중동 증설과 중국 수요 부진이 만든 구조적 oversupply다. ([Reuters][1])

### 실제 가격경로 검증

```json
{
  "case_id": "r4_loop14_lotte_lgchem_petrochemical_spread_collapse",
  "symbols": "011170/051910",
  "stage3_price": null,
  "stage4c_watch_date": "2025-02-07",
  "price_data_source": "Reuters earnings/spread-collapse anchor",
  "lotte_chemical_2024_op_loss_krw_bn": 895,
  "lotte_chemical_op_loss_yoy_widening_pct": 157,
  "lg_chem_2024_op_krw_bn": 916.8,
  "lg_chem_2024_op_decline_pct": -63.75,
  "lg_chem_petrochemical_q4_op_loss_krw_bn": 99,
  "driver": "Northeast Asia oversupply from China/Middle East capacity and weak China demand",
  "full_ohlc_status": "price_data_unavailable_after_deep_search",
  "unavailable_reason": "event-return and earnings anchors located, but adjusted daily OHLC window not retrievable from accessible KRX/Naver/Yahoo/Stooq paths in this environment"
}
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = petrochemical_spread_collapse
stage_failure_type = oversupply_spread_not_policy_story
```

---

## Case B — Lotte Chemical / HD Hyundai Chemical Daesan restructuring

```text
symbols = 011170 / HD Hyundai Oilbank read-through
case_type = success_candidate_policy_restructuring
archetype = PETROCHEMICAL_RESTRUCTURING_STAGE2_NOT_GREEN
```

### stage date

```text
Stage 1:
2025-08
- Korean government pushes petrochemical industry to reduce naphtha-cracking capacity.
- goal: cut 2.7M~3.7M tpy, about 25% of capacity.

Stage 2:
2025-11-26
- HD Hyundai and Lotte submit Daesan restructuring plan.
- Lotte to spin off Daesan business and merge it into HD Hyundai Chemical.
- Lotte Daesan NCC capacity: 1.1M tpy.
- HD Hyundai capacity: 850,000 tpy.

Stage 2 강화:
2026-02-24
- government approves first restructuring deal.
- support package: more than 2T won / $1.39B.
- Lotte and HD Hyundai Oilbank each inject 600B won.
- combined capital increase: 1.2T won.
- ownership adjusted to 50-50.
- Lotte Daesan NCC to halt operations for three years.
- lower utility costs up to 115B won and R&D funding 26B won included.

Stage 3:
없음
- 구조조정은 Stage 2.
- 실제 spread, cash margin, 가동률, debt reduction 확인 전 Green 금지.
```

이 case는 석유화학 구조조정이 “좋은 뉴스”이긴 하지만 Stage 3가 아니라는 기준이다. 정부는 최대 25% capacity reduction을 요구했고, Lotte Daesan 1.1M tpy NCC와 HD Hyundai 850,000 tpy capacity를 묶는 restructuring이 제출됐다. 이후 승인된 패키지는 2T won 이상 지원, 양사 600B won씩 출자, Lotte Daesan NCC 3년 가동중단을 포함한다. 하지만 실제 Green은 구조조정 발표가 아니라 **spread 회복과 cash margin**이다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "case_id": "r4_loop14_lotte_hdhyundai_petrochemical_restructuring",
  "symbols": "011170/HD_Hyundai_Oilbank_readthrough",
  "stage2_date": "2025-11-26/2026-02-24",
  "stage3_price": null,
  "price_data_source": "Reuters petrochemical restructuring anchors",
  "national_capacity_cut_target_tpy_mn": "2.7-3.7",
  "national_capacity_cut_target_pct": 25,
  "lotte_daesan_ncc_capacity_tpy_mn": 1.1,
  "hd_hyundai_capacity_tpy_mn": 0.85,
  "government_support_krw_trn": 2.0,
  "combined_capital_increase_krw_trn": 1.2,
  "lotte_contribution_krw_bn": 600,
  "hd_hyundai_oilbank_contribution_krw_bn": 600,
  "post_restructuring_ownership": "50-50",
  "lotte_daesan_shutdown_years": 3,
  "lower_utility_cost_support_krw_bn": 115,
  "r_and_d_funding_krw_bn": 26,
  "full_ohlc_status": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_policy_restructuring
rerating_result = petrochemical_capacity_rationalisation_stage2
stage_failure_type = capacity_cut_plan_not_spread_cash_margin_green
```

---

## Case C — Hyundai Steel / POSCO steel anti-dumping and weak-demand spread

```text
symbols = 004020 / 005490
case_type = event_premium + evidence_good_but_price_failed
archetype = STEEL_ANTI_DUMPING_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2024-06-21
- weak demand in construction and shipbuilding pressures Hyundai Steel.
- rebar price expected to fall 10%.
- competition from Japanese and Chinese steelmakers in shipbuilding steel plates.

Stage 4C-watch:
2024-06-21
- Hyundai Steel shares -1.2% to 29,000 won.
- 2024 net-profit estimate cut 73% to 215B won.
- target price cut 14% to 30,000 won.

Stage 2 relief:
2025-02-20
- Korea provisionally imposes 27.91%~38.02% anti-dumping tariff on Chinese steel plates.
- Chinese steel imports in 2024: $10.4B.
- Chinese share of total Korean steel imports: 49%.
- Hyundai Steel +5.8%.
- POSCO Holdings +3.9%.
- KOSPI -0.7%.

Stage 4C-watch:
2025 tariff context
- U.S. steel/aluminium tariff risk can erode exporter profitability.
```

철강은 R4에서 “tariff relief = Green”이 아니다. Hyundai Steel은 2024년 weak demand로 net-profit estimate가 73% 삭감되고 주가가 -1.2%였다. 이후 중국산 steel plate anti-dumping tariff로 Hyundai Steel +5.8%, POSCO +3.9%가 나왔지만, 이것은 event premium이다. 실제 Stage 3는 건설·조선 실수요, 판매단가, 원재료비, 전력비, spread가 닫혀야 한다. ([마켓워치][3])

### 실제 가격경로 검증

```json
{
  "case_id": "r4_loop14_hyundai_posco_steel_spread_antidumping",
  "symbols": "004020/005490",
  "stage2_date": "2025-02-20",
  "stage4c_watch_date": "2024-06-21",
  "stage3_price": null,
  "price_data_source": "MarketWatch Hyundai Steel weak-demand anchor + Reuters anti-dumping anchor",
  "hyundai_steel_weak_demand_event_price_krw": 29000,
  "hyundai_steel_weak_demand_event_mae_pct": -1.2,
  "rebar_price_decline_expected_pct": -10,
  "net_profit_estimate_after_cut_krw_bn": 215,
  "net_profit_estimate_cut_pct": -73,
  "implied_prior_net_profit_estimate_krw_bn": 796.3,
  "target_price_krw": 30000,
  "target_price_cut_pct": -14,
  "anti_dumping_tariff_pct": "27.91-38.02",
  "chinese_steel_imports_2024_usd_bn": 10.4,
  "chinese_share_of_korean_steel_imports_pct": 49,
  "hyundai_steel_antidumping_event_mfe_pct": 5.8,
  "posco_antidumping_event_mfe_pct": 3.9,
  "kospi_same_context_pct": -0.7,
  "hyundai_relative_outperformance_pp": 6.5,
  "posco_relative_outperformance_pp": 4.6,
  "full_ohlc_status": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_policy_relief
rerating_result = steel_spread_relief_stage2
stage_failure_type = tariff_relief_not_physical_demand_spread_green
```

---

## Case D — Korea Zinc / Young Poong / MBK strategic metal control premium

```text
symbol = 010130 / 000670
case_type = 4B-watch + governance_watch
archetype = STRATEGIC_METAL_CONTROL_PREMIUM_4B
```

### stage date

```text
Stage 1:
2024-09-13
- MBK Partners and Young Poong launch tender offer for Korea Zinc.
- Korea Zinc frames it as hostile takeover.
- strategic non-ferrous metal and smelter control premium enters market.

Stage 2:
2024-09-13
- tender offer size: 2T won / $1.5B.
- offer price: 660,000 won/share.
- target stake: 6.98%~14.61%.
- prior close: 556,000 won.
- Korea Zinc +19.8%.
- Young Poong daily limit +30%.

Stage 4B:
2024-09~10
- control premium prices faster than operating improvement.
- Korea Zinc later pairs with Bain Capital and announces 2.663T won buyback at 830,000 won/share context in WSJ source.
- governance / dilution / safety / accounting-quality gate remains.

Stage 3:
없음
- control premium is not operating Green.
```

Korea Zinc는 전략금속 case지만, Stage 3가 아니라 4B-watch다. 경영권 premium은 가격을 빠르게 밀어 올릴 수 있지만, zinc spread·TC/RC·capex·governance·safety·dilution risk와 분리해야 한다. Reuters는 2T won tender offer와 660,000 won offer price, Korea Zinc +19.8%, Young Poong +30%를 보도했다. WSJ는 이후 Korea Zinc가 Bain과 손잡고 2.663T won buyback을 추진했다고 보도했다. ([Reuters][4])

### 실제 가격경로 검증

```json
{
  "case_id": "r4_loop14_korea_zinc_strategic_metal_control_premium",
  "symbol": "010130/000670",
  "stage2_date": "2024-09-13",
  "stage4b_date": "2024-09-13",
  "stage3_price": null,
  "price_data_source": "Reuters tender-offer anchor + WSJ Bain/buyback anchor",
  "tender_offer_value_krw_trn": 2.0,
  "tender_offer_value_usd_bn": 1.5,
  "offer_price_krw": 660000,
  "prior_close_krw": 556000,
  "tender_premium_to_prior_close_pct": 18.7,
  "korea_zinc_event_mfe_pct": 19.8,
  "young_poong_event_mfe_pct": 30.0,
  "target_stake_min_pct": 6.98,
  "target_stake_max_pct": 14.61,
  "young_poong_existing_stake_pct": 25.4,
  "mbk_young_poong_combined_stake_if_success_pct": 40.0,
  "buyback_context_krw_trn": 2.663,
  "buyback_context_price_krw": 830000,
  "full_ohlc_status": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_4B_watch
rerating_result = strategic_metal_control_premium
stage_failure_type = control_premium_not_smelt_margin_green
```

---

## Case E — POSCO Holdings / Mineral Resources lithium mine integration

```text
symbol = 005490
case_type = success_candidate + lithium_price_4C-watch
archetype = LITHIUM_RESOURCE_INTEGRATION_STAGE2
```

### stage date

```text
Stage 1:
2025-11-11
- POSCO enters Australian lithium mine exposure through MinRes deal.
- countercyclical lithium resource acquisition during low lithium price environment.

Stage 2:
2025-11-11
- MinRes sells 30% stake in part of lithium business to POSCO for $765M.
- POSCO gains effective 15% interest in Wodgina and Mt Marion lithium mines.
- MinRes remains operator.
- POSCO already has lithium hydroxide JV in Korea with Pilbara Minerals.
- MinRes shares +10.8% on deal.
- Reuters notes lithium prices had collapsed, hitting miners and forcing asset sales.

Stage 3:
없음
- POSCO Green requires spodumene offtake, hydroxide plant utilization, lithium-price recovery, customer call-off and margin.
```

POSCO의 lithium integration은 R4 소재 전략자원 Stage 2다. POSCO가 MinRes의 Wodgina/Mt Marion exposure를 확보한 것은 장기 공급망 관점에서 좋다. 하지만 Reuters는 이 deal이 lithium price collapse와 MinRes balance-sheet repair라는 배경에서 나왔다고 설명했다. 즉 countercyclical resource acquisition은 좋은 Stage 2지만, POSCO Green은 hydroxide plant utilization과 고객 call-off로 닫혀야 한다. ([Reuters][5])

### 실제 가격경로 검증

```json
{
  "case_id": "r4_loop14_posco_minres_lithium_resource_integration",
  "symbol": "005490",
  "stage2_date": "2025-11-11",
  "stage3_price": null,
  "price_data_source": "Reuters MinRes-POSCO lithium JV anchor",
  "deal_value_usd_mn": 765,
  "stake_sold_in_part_lithium_business_pct": 30,
  "posco_effective_interest_wodgina_mt_marion_pct": 15,
  "assets": ["Wodgina", "Mt Marion"],
  "operator": "Mineral Resources",
  "minres_event_mfe_pct": 10.8,
  "context": "low lithium prices and MinRes balance-sheet repair",
  "posco_direct_event_return": "price_data_unavailable_after_deep_search",
  "green_conditions": ["spodumene_offtake", "hydroxide_plant_utilization", "lithium_price", "customer_calloff", "margin"]
}
```

### alignment

```text
score_price_alignment = success_candidate_but_price_data_unavailable
rerating_result = lithium_resource_integration_stage2
stage_failure_type = mine_stake_not_hydroxide_margin_green
```

---

## Case F — POSCO Future M / L&F lithium squeeze rally from CATL suspension

```text
symbols = 003670 / 066970 / 006400 / 373220
case_type = event_premium + price_moved_without_evidence
archetype = LITHIUM_PRICE_SQUEEZE_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2025-08-11
- CATL suspends Yichun lithium mining project after license expiry.
- market expects tighter lithium supply and lithium-price rebound.

Stage 4B:
2025-08-11
- Ganfeng Lithium +21%.
- Tianqi Lithium +18%.
- POSCO Future M +8.3%.
- L&F +10%.
- Samsung SDI +3.2%.
- LGES +2.8%.
- KOSPI -0.1%.
- lithium prices had fallen as much as 90% since 2022 peak.

Stage 3:
없음
- CATL said it could resume if licence renewed and no material operational impact.
- Korean material rally is inventory-valuation / sentiment premium unless customer volume and margin improve.
```

이 case는 R4의 전형적인 price_moved_without_evidence다. CATL mine suspension으로 lithium squeeze 기대가 생기자 POSCO Future M +8.3%, L&F +10%가 나왔지만, CATL은 license가 갱신되면 생산을 재개할 수 있고 material impact는 없다고 했다. 따라서 이것은 lithium price sentiment rally이지 Stage 3가 아니다. ([월스트리트저널][6])

### 실제 가격경로 검증

```json
{
  "case_id": "r4_loop14_posco_future_m_lnf_lithium_squeeze_rally",
  "symbols": "003670/066970/006400/373220",
  "stage4b_date": "2025-08-11",
  "stage3_price": null,
  "price_data_source": "WSJ CATL lithium suspension and Korean material rally anchor",
  "ganfeng_lithium_event_mfe_pct": 21.0,
  "tianqi_lithium_event_mfe_pct": 18.0,
  "posco_future_m_event_mfe_pct": 8.3,
  "lnf_event_mfe_pct": 10.0,
  "samsung_sdi_event_mfe_pct": 3.2,
  "lges_event_mfe_pct": 2.8,
  "kospi_same_context_pct": -0.1,
  "lithium_price_decline_since_2022_peak_pct": -90,
  "catl_material_operational_impact_confirmed": false,
  "catl_resume_if_license_renewed": true,
  "customer_volume_margin_confirmed": false,
  "full_ohlc_status": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = price_moved_without_evidence
rerating_result = lithium_price_squeeze_event_premium
stage_failure_type = lithium_sentiment_not_customer_volume_margin_green
```

---

## Case G — L&F / Tesla 4680 cathode contract collapse

```text
symbol = 066970
case_type = hard_4C
archetype = BATTERY_MATERIAL_CONTRACT_COLLAPSE_HARD_4C
```

### stage date

```text
Stage 1:
2023
- L&F signs high-nickel cathode material supply deal with Tesla and affiliates.
- market links contract to Tesla 4680 cells.

Stage 2:
2023
- initial expected deal value: $2.9B.
- supply period: January 2024 to December 2025.

Stage 4C:
2025-12-29
- contract value cut to $7,386.
- Reuters cites EV demand slowdown and Tesla 4680 production/ramp difficulties as likely reasons.
- L&F’s customer-name contract did not convert into material requirement.

Stage 3:
없음
- customer-name contract was never valid Stage 3 without actual call-off.
```

L&F는 R4 battery-material hard 4C다. $2.9B Tesla 계약이 $7,386로 줄어든 것은 “고객명·계약금액 headline”이 실제 call-off와 다르다는 가장 강한 반례다. Reuters는 EV demand slowdown, Tesla 4680 ramp 문제, Cybertruck 부진이 material requirement 감소 배경이라고 설명했다. ([Reuters][7])

### 실제 가격경로 검증

```json
{
  "case_id": "r4_loop14_lnf_tesla_4680_cathode_contract_collapse",
  "symbol": "066970",
  "stage4c_date": "2025-12-29",
  "stage3_price": null,
  "price_data_source": "Reuters L&F/Tesla contract-collapse anchor",
  "initial_contract_projection_usd_bn": 2.9,
  "revised_contract_value_usd": 7386,
  "contract_value_collapse_pct": -99.9997,
  "supply_period": "2024-01_to_2025-12",
  "customer": "Tesla and affiliates",
  "material": "high_nickel_cathode_materials",
  "application_context": "Tesla 4680 cells",
  "reported_likely_drivers": ["EV demand slowdown", "4680 production/ramp difficulty", "Cybertruck underperformance"],
  "full_ohlc_status": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = battery_material_contract_collapse_hard_4C
stage_failure_type = signed_contract_without_actual_calloff
```

---

## Case H — China rare-earth export controls / strategic resource supply-chain

```text
symbols = 005930 / 000660 / 042660 / EV-defense-semiconductor-materials basket
case_type = 4C-watch
archetype = RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C
```

### stage date

```text
Stage 1:
2025-04
- China introduces rare-earth export controls in retaliation for U.S. tariffs.
- heavy rare earths become geopolitical leverage.

Stage 4C-watch:
2025-10-09
- China tightens rare-earth export controls.
- overseas defence users will not receive licences.
- advanced semiconductor applications reviewed case-by-case.
- China produces over 90% of processed rare earths and rare-earth magnets.
- foreign users of Chinese components/equipment may need export licences.

Stage 4C-watch Korea validation:
2025-10-22
- Korean trade envoy asks China to lift sanctions on Hanwha Ocean U.S. subsidiaries.
- Korea also raises rare-earth export curbs.
- curbs expected to affect Samsung and SK Hynix.

Stage 4C persistence:
2026-05
- exports of yttrium, dysprosium and terbium still down around 50% since April 2025 controls.
- latest White House statement acknowledges China export-control regime remains.
```

희토류는 R4 전략자원 hard watch다. 중국은 processed rare earths와 rare-earth magnets의 90% 이상을 생산하고, defence users에는 license를 주지 않으며 advanced semiconductor applications는 case-by-case로 처리한다고 밝혔다. 2026년 5월에도 yttrium·dysprosium·terbium exports가 controls 이후 약 50% 낮은 수준으로 남아 있었다. 한국 측은 이 curbs가 Samsung, SK Hynix, Hanwha Ocean에도 영향을 줄 수 있다고 봤다. ([Reuters][8])

### 실제 가격경로 검증

```json
{
  "case_id": "r4_loop14_rare_earth_export_control_supply_chain",
  "symbols": "005930/000660/042660/strategic_materials_basket",
  "stage4c_watch_date": "2025-10-09/2025-10-22/2026-05",
  "stage3_price": null,
  "price_data_source": "Reuters rare-earth export-control and Korean trade-envoy anchors",
  "processed_rare_earths_china_share_pct": 90,
  "rare_earth_magnets_china_share_pct": 90,
  "heavy_rare_earth_exports_decline_since_controls_pct": -50,
  "affected_elements": ["yttrium", "dysprosium", "terbium", "scandium", "indium"],
  "defence_user_license_policy": "not_granted",
  "advanced_semiconductor_license_policy": "case_by_case",
  "korea_affected_companies_context": ["Samsung Electronics", "SK Hynix", "Hanwha Ocean"],
  "direct_korean_stock_price_anchor": "price_data_unavailable_after_deep_search",
  "mfe_mae": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = rare_earth_export_control_supply_chain_gate
stage_failure_type = export_license_not_theme_green
```

---

## Case I — LG Chem cathode supply-chain ownership rebalancing

```text
symbol = 051910
case_type = success_candidate + nonbinding_watch
archetype = CATHODE_SUPPLY_CHAIN_REBALANCING_STAGE2
```

### stage date

```text
Stage 1:
2024-11-20
- Exxon signs non-binding lithium supply deal with LG Chem.
- up to 100,000 metric tons of lithium from Arkansas project.
- LG Chem to use lithium at Tennessee cathode facility.
- financial terms and final contract still to be negotiated.

Stage 2:
2025-09-08
- Toyota Tsusho acquires 25% stake in LG Chem’s South Korea cathode material plant.
- Toyota Tsusho becomes second-largest shareholder of the plant.
- Zhejiang Huayou Cobalt stake falls from 49% to 24%.

Stage 3:
없음
- ownership rebalancing and non-binding lithium supply are Stage 2.
- Green requires binding lithium contract, Tennessee cathode ramp, customer call-off, margin, geopolitics-risk reduction.
```

LG Chem cathode case는 R4에서 좋은 supply-chain rebalancing 후보지만, Stage 3는 아니다. Toyota Tsusho의 25% stake는 China exposure를 낮추는 방향의 Stage 2이고, Exxon의 up-to-100,000t lithium deal은 North America supply-chain 방향성으로 좋다. 그러나 Exxon deal은 non-binding이고 가격·최종조건이 미확정이다. ([Reuters][9])

### 실제 가격경로 검증

```json
{
  "case_id": "r4_loop14_lg_chem_cathode_supply_chain_rebalancing",
  "symbol": "051910",
  "stage1_date": "2024-11-20",
  "stage2_date": "2025-09-08",
  "stage3_price": null,
  "price_data_source": "Reuters Toyota Tsusho cathode plant stake + Exxon non-binding lithium deal anchors",
  "toyota_tsusho_cathode_plant_stake_pct": 25,
  "huayou_cobalt_stake_before_pct": 49,
  "huayou_cobalt_stake_after_pct": 24,
  "huayou_stake_decline_pp": -25,
  "exxon_nonbinding_lithium_supply_tonnes": 100000,
  "exxon_project_location": "Arkansas Smackover",
  "lg_chem_tennessee_cathode_use": true,
  "financial_terms_finalized": false,
  "binding_contract_confirmed": false,
  "direct_event_return": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_nonbinding_watch
rerating_result = cathode_supply_chain_rebalancing_stage2
stage_failure_type = ownership_rebalancing_nonbinding_supply_not_margin_green
```

---

# 5. 이번 R4 case별 stage date 요약

| case                               | Stage 1             | Stage 2                     | Stage 3 | Stage 4B                     | Stage 4C                             |
| ---------------------------------- | ------------------- | --------------------------- | ------- | ---------------------------- | ------------------------------------ |
| Lotte/LG Chem petrochem            | 2024 FY             | N/A                         | N/A     | N/A                          | 2025-02 loss/spread watch            |
| Lotte/HD Hyundai restructuring     | 2025-08             | 2025-11 / 2026-02           | N/A     | policy restructuring premium | spread/cash-margin watch             |
| Hyundai Steel/POSCO                | 2024-06 weak demand | 2025-02 anti-dumping relief | N/A     | tariff event                 | weak demand/export tariff watch      |
| Korea Zinc                         | 2024-09             | tender / buyback            | N/A     | control premium              | governance/dilution/safety watch     |
| POSCO lithium                      | 2025-11             | MinRes mine stake           | N/A     | lithium resource premium     | lithium price/utilization watch      |
| POSCO Future M/L&F lithium squeeze | 2025-08             | CATL suspension event       | N/A     | lithium squeeze rally        | license renewal / no material impact |
| L&F/Tesla                          | 2023 contract       | 2023 headline               | N/A     | N/A                          | 2025-12 hard                         |
| Rare earth controls                | 2025-04             | limited licensing relief    | N/A     | N/A                          | 2025-10 / 2026-05 watch              |
| LG Chem cathode                    | 2024-11             | 2025-09 ownership shift     | N/A     | supply-chain premium         | non-binding/final terms watch        |

---

# 6. 실제 가격경로 검증 총괄

| case                           |                                           가격·계약 anchor | 해석                               | 판정                           |
| ------------------------------ | -----------------------------------------------------: | -------------------------------- | ---------------------------- |
| Lotte/LG Chem petrochem        |             Lotte OP loss 895B won, LG Chem OP -63.75% | spread collapse                  | thesis_break_watch           |
| Lotte/HD Hyundai restructuring |               2T won support, 1.1M tpy NCC 3년 shutdown | capacity rationalization Stage 2 | success_candidate            |
| Hyundai Steel/POSCO            |                Hyundai -1.2%, later +5.8%; POSCO +3.9% | weak demand + tariff event       | event_premium                |
| Korea Zinc                     |                +19.8%, Young Poong +30%, tender 2T won | control premium 4B               | 4B-watch                     |
| POSCO lithium                  |           MinRes +10.8%, POSCO direct OHLC unavailable | resource integration Stage 2     | success_candidate            |
| POSCO Future M/L&F             |                              +8.3% / +10%, KOSPI -0.1% | lithium squeeze sentiment        | price_moved_without_evidence |
| L&F/Tesla                      |                                         $2.9B → $7,386 | contract hard break              | thesis_break                 |
| Rare earth controls            |            exports of key heavy rare earths still -50% | supply-chain hard watch          | thesis_break_watch           |
| LG Chem cathode                | Toyota 25%, Huayou 49%→24%, Exxon 100,000t non-binding | supply-chain Stage 2             | success_candidate            |

---

# 7. score-price alignment 판정

```text
aligned:
- 없음. R4는 대부분 spread/contract/control/policy gate가 아직 닫히지 않음.

structural_success_candidate:
- Lotte/HD Hyundai petrochemical restructuring, if spread/cash margin later improves.
- POSCO lithium mine integration, if hydroxide utilization and offtake margin confirm.
- LG Chem cathode ownership rebalancing, if binding lithium and cathode ramp confirm.

success_candidate:
- Korea Zinc as strategic metal control premium, but only Stage 2/4B.
- POSCO lithium resource integration.
- LG Chem cathode supply-chain rebalancing.

failed_rerating:
- Lotte Chemical / LG Chem petrochemical spread collapse.
- Hyundai Steel weak-demand estimate cut.

overheat / 4B:
- Korea Zinc control premium.
- POSCO Future M/L&F CATL lithium squeeze rally.
- Steel anti-dumping rally if treated as spread recovery.

price_moved_without_evidence:
- POSCO Future M / L&F lithium rally from CATL mine suspension.
- Korea Zinc control premium if treated as operating Green.
- anti-dumping steel rally if treated as final demand recovery.

evidence_good_but_price_failed:
- Hyundai Steel weak demand case.
- Petrochemical restructuring if stock rerates before spread.

thesis_break:
- L&F / Tesla contract-value collapse.

thesis_break_watch:
- petrochemical oversupply.
- rare-earth export controls.
- steel weak demand and U.S. tariff risk.
- lithium price and utilization risk.
```

---

# 8. 점수비중 교정

## 올릴 축

```text
spread_margin_realization +5
capacity_cut_actual_execution +5
plant_shutdown_discipline +4
commodity_price_sensitivity +5
customer_calloff_visibility +5
contract_value_durability +5
resource_offtake_utilization +5
export_license_continuity +5
governance_dilution_control +5
inventory_valuation_risk +4
```

### 왜 올리나

Lotte/LG Chem은 oversupply와 spread collapse가 직접 손익을 깎았다. Lotte/HD Hyundai restructuring은 capacity cut이 실제 shutdown으로 이어져야 한다. Hyundai Steel/POSCO는 tariff relief가 있어도 실수요와 spread가 필요하다. POSCO Future M/L&F는 lithium squeeze가 가격을 밀었지만, customer call-off와 margin이 없다. L&F는 signed contract가 실제 call-off와 다르면 0에 가까워질 수 있음을 보여줬다. Rare earth는 실제 export license continuity가 핵심이다.

## 내릴 축

```text
commodity_rebound_headline_only -5
tariff_relief_only -5
control_premium_only -5
capacity_restructuring_policy_only -5
mine_stake_without_processing_margin -5
CATL_license_suspension_sentiment -5
nonbinding_supply_agreement -5
signed_contract_without_calloff -5
rare_earth_truce_without_actual_exports -5
```

### 왜 내리나

R4는 headline이 가장 위험한 섹터다. 리튬이 오른다고 모든 소재주가 Stage 3는 아니고, anti-dumping tariff가 붙었다고 철강 spread가 복구된 것도 아니다. 경영권 premium도 operating cashflow와 다르다. 석유화학 구조조정도 cash margin이 나오기 전에는 Stage 2다.

---

# 9. Green gate 강화 조건

```text
R4 Stage 3-Green 필수:
1. 소재 spread가 실제 gross/operating margin으로 확인.
2. 구조조정은 capacity shutdown이 실제 실행되고 utilization / cash margin 개선.
3. 리튬·전략자원은 offtake, processing utilization, customer call-off 확인.
4. 배터리 소재 계약은 실제 shipment / revenue recognition 확인.
5. steel tariff relief는 판매단가, 실수요, 원재료비, export tariff 영향 확인.
6. rare earth는 actual export license and shipment 확인.
7. control premium은 governance, dilution, accounting/safety risk와 분리.
8. non-binding agreement는 Stage 2까지만.
9. price path가 evidence 이후 따라옴.
```

---

# 10. 4B 조기감지 조건

```text
4B-watch:
- control premium으로 +20% 이상 급등.
- CATL / lithium license headline으로 소재주 +8~10% 급등.
- anti-dumping tariff로 철강주 +5% 이상 급등.
- restructuring policy support로 spread 확인 전 rerating.
- strategic mineral / rare earth headline로 실제 license 전 가격화.
- mine stake acquisition으로 processing utilization 전 rerating.
```

---

# 11. 4C hard gate 조건

```text
Hard 4C:
- signed contract value collapse.
- customer call-off failure.
- petrochemical spread collapse with deep operating loss.
- rare-earth export licence denial / shipment failure.
- tariff reversal or export tariff shock.
- forced plant shutdown from oversupply without balance-sheet relief.
- mine/offtake economics broken by commodity price collapse.
- governance/dilution/accounting risk after control-premium rally.
```

이번 R4 Loop 14의 hard 4C는 **L&F / Tesla cathode contract collapse**다. Petrochemical oversupply, rare earth controls, Korea Zinc governance, steel spread, lithium price squeeze는 hard 4C가 아니라 **4C-watch / 4B-watch / event premium**으로 둔다.

---

# 12. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 13. 레포 반영용 patch-ready 출력

## docs/round/round_214.md 요약

```md
# R4 Loop 14. Materials / Spreads / Strategic Resources Price Validation

이번 라운드는 R4 Loop 14 price-validation 라운드다.

핵심 결론:
- Lotte Chemical / LG Chem petrochemical spread collapse is 4C-watch. Lotte Chemical 2024 OP loss widened 157% YoY to 895B won; LG Chem OP fell 63.75% to 916.8B won and petrochemical division posted Q4 OP loss of 99B won. Oversupply from China/Middle East and weak China demand drove spread collapse.
- Lotte Chemical / HD Hyundai Chemical Daesan restructuring is Stage 2, not Green. Government approved first restructuring deal with more than 2T won support, 1.2T won combined capital increase, 50-50 ownership, and Lotte Daesan NCC shutdown for three years. Spread/cash margin required.
- Hyundai Steel / POSCO steel anti-dumping is event premium. Hyundai Steel weak-demand case saw shares -1.2% at 29,000 won and net-profit estimate cut 73%; later anti-dumping tariffs of 27.91%~38.02% drove Hyundai Steel +5.8%, POSCO +3.9%, KOSPI -0.7%.
- Korea Zinc is strategic-metal control premium 4B-watch. MBK/Young Poong tender offer of 2T won at 660,000 won/share drove Korea Zinc +19.8% and Young Poong +30%. Control premium is not smelting margin Green.
- POSCO / MinRes lithium deal is resource-integration Stage 2. POSCO pays $765M for 30% stake in part of MinRes lithium business, gaining effective 15% interest in Wodgina and Mt Marion. MinRes +10.8%; POSCO direct OHLC unavailable.
- POSCO Future M / L&F lithium squeeze rally is price_moved_without_evidence. CATL Yichun mine suspension drove POSCO Future M +8.3%, L&F +10%, Samsung SDI +3.2%, LGES +2.8%, while KOSPI -0.1%. CATL said no material impact and possible restart if license renewed.
- L&F / Tesla 4680 cathode is hard 4C. Initial $2.9B expected supply value was cut to $7,386, showing customer-name contract without actual call-off is not Stage 3.
- China rare-earth export controls are strategic-resource 4C-watch. China produces over 90% of processed rare earths and magnets, denies licences to defence users, reviews advanced semiconductor applications case-by-case, and heavy rare-earth exports remain down around 50%.
- LG Chem cathode supply-chain rebalancing is Stage 2. Toyota Tsusho takes 25% stake in LG Chem cathode plant, Huayou stake falls from 49% to 24%; Exxon non-binding lithium supply deal up to 100,000t remains non-binding.
```

## docs/checkpoints/checkpoint_28a_round214_r4_loop14.md 요약

```md
# Checkpoint 28A Round 214 R4 Loop 14 Materials Spreads Strategic Resources Price Validation

## 반영 내용
- R4 Loop 14 price-validation 라운드를 추가했다.
- Lotte/LG Chem petrochemical spread collapse, Lotte/HD Hyundai restructuring, Hyundai Steel/POSCO anti-dumping, Korea Zinc control premium, POSCO/MinRes lithium, POSCO Future M/L&F lithium squeeze, L&F/Tesla contract collapse, China rare-earth controls, LG Chem cathode ownership rebalancing을 비교했다.
- Reuters / WSJ / MarketWatch anchors로 가능한 event MFE/MAE, event price, OP loss, contract value, tariff rate, capacity and ownership metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- spread margin realization, capacity-cut execution, plant-shutdown discipline, commodity-price sensitivity, customer call-off visibility, contract-value durability, resource offtake/utilization, export-license continuity, governance/dilution control, inventory-valuation risk 가중치 강화.
- commodity rebound headline-only, tariff relief-only, control premium-only, restructuring policy-only, mine stake without processing margin, CATL license suspension sentiment, non-binding supply agreement, signed contract without call-off 감점 강화.
```

## data/e2r_case_library/cases_r4_loop14_round214.jsonl 초안

```jsonl
{"case_id":"r4_loop14_lotte_lgchem_petrochemical_spread_collapse","symbol":"011170/051910","company_name":"Lotte Chemical / LG Chem","case_type":"failed_rerating_4c_watch","primary_archetype":"PETROCHEMICAL_SPREAD_COLLAPSE_4C","stage4c_date":"2025-02-07","price_validation":{"price_data_source":"Reuters earnings/spread-collapse anchor","stage3_price":null,"lotte_chemical_2024_op_loss_krw_bn":895,"lotte_chemical_op_loss_yoy_widening_pct":157,"lg_chem_2024_op_krw_bn":916.8,"lg_chem_2024_op_decline_pct":-63.75,"lg_chem_petrochemical_q4_op_loss_krw_bn":99,"driver":"Northeast Asia oversupply from China/Middle East capacity and weak China demand","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"petrochemical_spread_collapse","notes":"Oversupply and spread collapse directly hit earnings; China stimulus/restructuring headline is not Green."}
{"case_id":"r4_loop14_lotte_hdhyundai_petrochemical_restructuring","symbol":"011170/HD_Hyundai_Oilbank_readthrough","company_name":"Lotte Chemical / HD Hyundai Chemical","case_type":"success_candidate_policy_restructuring","primary_archetype":"PETROCHEMICAL_RESTRUCTURING_STAGE2_NOT_GREEN","stage2_date":"2025-11-26/2026-02-24","price_validation":{"price_data_source":"Reuters petrochemical restructuring anchors","stage3_price":null,"national_capacity_cut_target_tpy_mn":"2.7-3.7","national_capacity_cut_target_pct":25,"lotte_daesan_ncc_capacity_tpy_mn":1.1,"hd_hyundai_capacity_tpy_mn":0.85,"government_support_krw_trn":2.0,"combined_capital_increase_krw_trn":1.2,"lotte_contribution_krw_bn":600,"hd_hyundai_oilbank_contribution_krw_bn":600,"post_restructuring_ownership":"50-50","lotte_daesan_shutdown_years":3,"lower_utility_cost_support_krw_bn":115,"r_and_d_funding_krw_bn":26,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_policy_restructuring","rerating_result":"petrochemical_capacity_rationalisation_stage2","notes":"Capacity cut and support package are Stage 2; spread and cash margin recovery required."}
{"case_id":"r4_loop14_hyundai_posco_steel_spread_antidumping","symbol":"004020/005490","company_name":"Hyundai Steel / POSCO Holdings","case_type":"event_premium_policy_relief","primary_archetype":"STEEL_ANTI_DUMPING_EVENT_PREMIUM","stage2_date":"2025-02-20","stage4c_date":"2024-06-21_watch","price_validation":{"price_data_source":"MarketWatch Hyundai Steel weak-demand anchor + Reuters anti-dumping anchor","stage3_price":null,"hyundai_steel_weak_demand_event_price_krw":29000,"hyundai_steel_weak_demand_event_mae_pct":-1.2,"rebar_price_decline_expected_pct":-10,"net_profit_estimate_after_cut_krw_bn":215,"net_profit_estimate_cut_pct":-73,"implied_prior_net_profit_estimate_krw_bn":796.3,"target_price_krw":30000,"target_price_cut_pct":-14,"anti_dumping_tariff_pct":"27.91-38.02","chinese_steel_imports_2024_usd_bn":10.4,"chinese_share_of_korean_steel_imports_pct":49,"hyundai_steel_antidumping_event_mfe_pct":5.8,"posco_antidumping_event_mfe_pct":3.9,"kospi_same_context_pct":-0.7,"hyundai_relative_outperformance_pp":6.5,"posco_relative_outperformance_pp":4.6,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_policy_relief","rerating_result":"steel_spread_relief_stage2","notes":"Anti-dumping relief is not Green until physical demand, ASP and spread recover."}
{"case_id":"r4_loop14_korea_zinc_strategic_metal_control_premium","symbol":"010130/000670","company_name":"Korea Zinc / Young Poong / MBK","case_type":"event_premium_4b_watch","primary_archetype":"STRATEGIC_METAL_CONTROL_PREMIUM_4B","stage2_date":"2024-09-13","stage4b_date":"2024-09-13","price_validation":{"price_data_source":"Reuters tender-offer anchor + WSJ Bain/buyback anchor","stage3_price":null,"tender_offer_value_krw_trn":2.0,"tender_offer_value_usd_bn":1.5,"offer_price_krw":660000,"prior_close_krw":556000,"tender_premium_to_prior_close_pct":18.7,"korea_zinc_event_mfe_pct":19.8,"young_poong_event_mfe_pct":30.0,"target_stake_min_pct":6.98,"target_stake_max_pct":14.61,"young_poong_existing_stake_pct":25.4,"mbk_young_poong_combined_stake_if_success_pct":40.0,"buyback_context_krw_trn":2.663,"buyback_context_price_krw":830000,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_4B_watch","rerating_result":"strategic_metal_control_premium","notes":"Control premium must be separated from zinc spread, smelter margin, governance, dilution and safety risk."}
{"case_id":"r4_loop14_posco_minres_lithium_resource_integration","symbol":"005490","company_name":"POSCO Holdings / Mineral Resources","case_type":"success_candidate_price_unavailable","primary_archetype":"LITHIUM_RESOURCE_INTEGRATION_STAGE2","stage2_date":"2025-11-11","price_validation":{"price_data_source":"Reuters MinRes-POSCO lithium JV anchor","stage3_price":null,"deal_value_usd_mn":765,"stake_sold_in_part_lithium_business_pct":30,"posco_effective_interest_wodgina_mt_marion_pct":15,"assets":["Wodgina","Mt Marion"],"operator":"Mineral Resources","minres_event_mfe_pct":10.8,"context":"low lithium prices and MinRes balance-sheet repair","posco_direct_event_return":"price_data_unavailable_after_deep_search","green_conditions":["spodumene_offtake","hydroxide_plant_utilization","lithium_price","customer_calloff","margin"]},"score_price_alignment":"success_candidate_but_price_data_unavailable","rerating_result":"lithium_resource_integration_stage2","notes":"Mine stake is Stage 2; processing utilization, offtake and margin required."}
{"case_id":"r4_loop14_posco_future_m_lnf_lithium_squeeze_rally","symbol":"003670/066970/006400/373220","company_name":"POSCO Future M / L&F / Samsung SDI / LGES","case_type":"price_moved_without_evidence","primary_archetype":"LITHIUM_PRICE_SQUEEZE_EVENT_PREMIUM","stage4b_date":"2025-08-11","price_validation":{"price_data_source":"WSJ CATL lithium suspension and Korean material rally anchor","stage3_price":null,"ganfeng_lithium_event_mfe_pct":21.0,"tianqi_lithium_event_mfe_pct":18.0,"posco_future_m_event_mfe_pct":8.3,"lnf_event_mfe_pct":10.0,"samsung_sdi_event_mfe_pct":3.2,"lges_event_mfe_pct":2.8,"kospi_same_context_pct":-0.1,"lithium_price_decline_since_2022_peak_pct":-90,"catl_material_operational_impact_confirmed":false,"catl_resume_if_license_renewed":true,"customer_volume_margin_confirmed":false,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"lithium_price_squeeze_event_premium","notes":"Lithium sentiment rally is not Green without customer volume, ASP, inventory and margin confirmation."}
{"case_id":"r4_loop14_lnf_tesla_4680_cathode_contract_collapse","symbol":"066970","company_name":"L&F","case_type":"hard_4c","primary_archetype":"BATTERY_MATERIAL_CONTRACT_COLLAPSE_HARD_4C","stage4c_date":"2025-12-29","price_validation":{"price_data_source":"Reuters L&F/Tesla contract-collapse anchor","stage3_price":null,"initial_contract_projection_usd_bn":2.9,"revised_contract_value_usd":7386,"contract_value_collapse_pct":-99.9997,"supply_period":"2024-01_to_2025-12","customer":"Tesla and affiliates","material":"high_nickel_cathode_materials","application_context":"Tesla 4680 cells","reported_likely_drivers":["EV demand slowdown","4680 production/ramp difficulty","Cybertruck underperformance"],"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break","rerating_result":"battery_material_contract_collapse_hard_4C","notes":"Signed customer-name contract failed actual call-off; hard 4C."}
{"case_id":"r4_loop14_rare_earth_export_control_supply_chain","symbol":"005930/000660/042660/strategic_materials_basket","company_name":"Samsung / SK Hynix / Hanwha Ocean rare-earth supply-chain read-through","case_type":"4c_watch","primary_archetype":"RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C","stage4c_date":"2025-10-09/2025-10-22/2026-05_watch","price_validation":{"price_data_source":"Reuters rare-earth export-control and Korean trade-envoy anchors","stage3_price":null,"processed_rare_earths_china_share_pct":90,"rare_earth_magnets_china_share_pct":90,"heavy_rare_earth_exports_decline_since_controls_pct":-50,"affected_elements":["yttrium","dysprosium","terbium","scandium","indium"],"defence_user_license_policy":"not_granted","advanced_semiconductor_license_policy":"case_by_case","korea_affected_companies_context":["Samsung Electronics","SK Hynix","Hanwha Ocean"],"direct_korean_stock_price_anchor":"price_data_unavailable_after_deep_search","mfe_mae":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"rare_earth_export_control_supply_chain_gate","notes":"Strategic-resource headline needs actual licences, shipments, inventory and alternative sourcing."}
{"case_id":"r4_loop14_lg_chem_cathode_supply_chain_rebalancing","symbol":"051910","company_name":"LG Chem","case_type":"success_candidate_nonbinding_watch","primary_archetype":"CATHODE_SUPPLY_CHAIN_REBALANCING_STAGE2","stage1_date":"2024-11-20","stage2_date":"2025-09-08","price_validation":{"price_data_source":"Reuters Toyota Tsusho cathode plant stake + Exxon non-binding lithium deal anchors","stage3_price":null,"toyota_tsusho_cathode_plant_stake_pct":25,"huayou_cobalt_stake_before_pct":49,"huayou_cobalt_stake_after_pct":24,"huayou_stake_decline_pp":-25,"exxon_nonbinding_lithium_supply_tonnes":100000,"exxon_project_location":"Arkansas Smackover","lg_chem_tennessee_cathode_use":true,"financial_terms_finalized":false,"binding_contract_confirmed":false,"direct_event_return":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_nonbinding_watch","rerating_result":"cathode_supply_chain_rebalancing_stage2","notes":"Ownership rebalancing and non-binding lithium supply are Stage 2; binding contract and cathode ramp required."}
```

## data/sector_taxonomy/score_weight_profiles_round214_r4_loop14_v1.csv 초안

```csv
archetype,spread_margin_realization,capacity_cut_actual_execution,plant_shutdown_discipline,commodity_price_sensitivity,customer_calloff_visibility,contract_value_durability,resource_offtake_utilization,export_license_continuity,governance_dilution_control,inventory_valuation_risk,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
PETROCHEMICAL_SPREAD_COLLAPSE_4C,+5,+3,+3,+5,+1,+1,+0,+0,+2,+5,0,+4,+5,Lotte/LG Chem show oversupply spread collapse hits earnings directly.
PETROCHEMICAL_RESTRUCTURING_STAGE2_NOT_GREEN,+5,+5,+5,+4,+1,+1,+0,+0,+2,+4,-5,+4,+4,Daesan restructuring is Stage 2 until spread/cash margin improves.
STEEL_ANTI_DUMPING_EVENT_PREMIUM,+5,+3,+2,+5,+1,+1,+0,+0,+2,+4,-5,+5,+4,Steel tariff relief needs physical demand, ASP and spread confirmation.
STRATEGIC_METAL_CONTROL_PREMIUM_4B,+4,+1,+1,+5,+1,+2,+2,+3,+5,+3,-5,+5,+4,Korea Zinc control premium needs governance/dilution and smelting-margin separation.
LITHIUM_RESOURCE_INTEGRATION_STAGE2,+4,+2,+2,+5,+4,+4,+5,+2,+3,+5,-5,+5,+4,POSCO mine stake needs offtake, processing utilization and lithium-price margin.
LITHIUM_PRICE_SQUEEZE_EVENT_PREMIUM,+4,+1,+1,+5,+4,+4,+3,+1,+2,+5,-5,+5,+3,CATL license suspension sentiment is not customer-volume/margin Green.
BATTERY_MATERIAL_CONTRACT_COLLAPSE_HARD_4C,+3,+1,+1,+5,+5,+5,+3,+1,+2,+5,0,+4,+5,L&F/Tesla proves customer-name contract requires actual call-off.
RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C,+2,+0,+0,+5,+3,+3,+3,+5,+2,+5,0,+5,+5,Rare-earth controls require actual export licences and shipments.
CATHODE_SUPPLY_CHAIN_REBALANCING_STAGE2,+4,+2,+2,+5,+4,+4,+4,+3,+3,+4,-5,+4,+3,LG Chem ownership shift/nonbinding supply needs binding contract and cathode ramp.
```

---

# 이번 R4 Loop 14 결론

```text
1. Lotte Chemical / LG Chem은 petrochemical spread collapse다.
   oversupply가 손익으로 내려왔고, 중국 부양책 기대만으로 Stage 3를 주면 false positive다.

2. Lotte / HD Hyundai restructuring은 Stage 2다.
   2T won 지원과 3년 NCC shutdown은 좋지만, 실제 spread와 cash margin 전에는 Green이 아니다.

3. Hyundai Steel / POSCO anti-dumping은 event premium이다.
   tariff relief는 주가를 움직였지만, 물량·ASP·spread가 Stage 3 조건이다.

4. Korea Zinc는 strategic metal control premium 4B다.
   +19.8%, Young Poong +30%는 control premium이지 smelting cashflow가 아니다.

5. POSCO lithium resource deal은 success_candidate다.
   하지만 mine stake와 processing margin 사이에는 offtake, utilization, lithium price gate가 있다.

6. POSCO Future M / L&F lithium squeeze는 price_moved_without_evidence다.
   CATL license suspension은 sentiment rally를 만들었지만, 고객 물량과 margin은 확인되지 않았다.

7. L&F / Tesla는 R4 hard 4C다.
   $2.9B 계약이 $7,386로 줄어든 것은 signed contract headline이 실제 call-off가 아니라는 결정적 반례다.

8. Rare earth controls는 전략자원 4C-watch다.
   China export license와 실제 선적이 없으면 semis/EV/defense supply-chain Green을 주면 안 된다.

9. LG Chem cathode rebalancing은 Stage 2다.
   Toyota Tsusho stake와 Exxon non-binding supply는 좋지만, binding contract와 cathode ramp가 필요하다.
```

한 문장으로 압축하면:

> **R4에서 진짜 Stage 3는 “리튬·철강·석화·희토류·전략금속 뉴스가 좋다”가 아니라, spread margin·capacity shutdown·actual call-off·offtake utilization·export license·inventory valuation·cash conversion이 실제 숫자로 닫히는 순간이다.**

[1]: https://www.reuters.com/markets/commodities/south-korean-petrochemical-firms-profits-plunge-2024-oversupply-persists-2025-02-07/?utm_source=chatgpt.com "South Korean petrochemical firms' profits plunge in 2024 as oversupply persists"
[2]: https://www.reuters.com/world/asia-pacific/south-koreas-hd-hyundai-lotte-chemical-submit-plan-restructure-petrochemical-2025-11-26/?utm_source=chatgpt.com "South Korea's HD Hyundai, Lotte Chemical submit plan to restructure petrochemical businesses"
[3]: https://www.marketwatch.com/story/hyundai-steel-s-2024-earnings-could-be-hit-by-weak-demand-market-talk-bcbe77c8?utm_source=chatgpt.com "Hyundai Steel's 2024 Earnings Could Be Hit by Weak Demand -- Market Talk"
[4]: https://www.reuters.com/markets/deals/private-equity-mbk-young-poong-launch-15-bln-tender-offer-korea-zinc-shares-2024-09-13/?utm_source=chatgpt.com "Private equity MBK, Young Poong launch $1.5 bln tender offer for Korea Zinc shares"
[5]: https://www.reuters.com/business/energy/australias-minres-sell-30-lithium-jv-stake-posco-765-mln-2025-11-11/?utm_source=chatgpt.com "Australia's MinRes inks $765 million deal with POSCO for lithium JV stake, shares surge"
[6]: https://www.wsj.com/finance/commodities-futures/ev-battery-giant-catl-suspends-mining-project-67693725?utm_source=chatgpt.com "EV Battery Giant CATL Suspends Mining Project"
[7]: https://www.reuters.com/world/asia-pacific/south-koreas-lf-says-value-battery-material-supply-deal-with-tesla-cut-7386-2025-12-29/?utm_source=chatgpt.com "South Korea's L&F slashes value of battery material supply deal with Tesla"
[8]: https://www.reuters.com/world/china/china-tightens-rare-earth-export-controls-2025-10-09/?utm_source=chatgpt.com "China tightens rare earth export controls, targets defence, semiconductor users"
[9]: https://www.reuters.com/markets/emerging/lg-chem-says-japans-toyota-tsusho-acquires-25-stake-its-south-korea-cathode-2025-09-08/?utm_source=chatgpt.com "LG Chem says Japan's Toyota Tsusho acquires 25% stake in its South Korea cathode material plant"
