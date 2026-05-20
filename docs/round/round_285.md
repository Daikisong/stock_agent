순서상 이번은 **R3 Loop 14 — 2차전지·전기차·친환경 가격경로 검증 라운드**다.

```text
round = R3 Loop 14
round_id = round_213
large_sector = SECONDARY_BATTERY_EV_GREEN_ENERGY
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true
next_round = R4 Loop 14
```

이번 R3는 “배터리 장기성장”을 부정하는 라운드가 아니다. 오히려 반대로, 장기 성장 산업일수록 **계약 취소, EV 수요 둔화, 고객사의 하이브리드 전환, 보조금 종료, 공장 utilization, ESS pivot, tariff/customs, 원재료·공급망 gate**를 더 세게 봐야 한다는 라운드다.

이번에도 KRX/Naver/Yahoo/Stooq 기준의 수정주가 일봉 OHLC 전체 구간은 안정적으로 확보하지 못했다. 따라서 30D/90D/180D/1Y full MFE·MAE는 만들지 않고, Reuters/AP/MarketWatch가 보도한 **event return, 계약금액, 영업손실, 공장투자, JV 해체, 감산·해고, 정책자금, 공급망 지연**을 가격 anchor로 사용했다.

---

# 1. 이번 라운드 대섹터

```text
R3 = 2차전지·전기차·친환경
```

R3에서 진짜 Stage 3는 “배터리”, “IRA”, “미국 공장”, “ESS”, “친환경”, “수소”, “태양광”, “실리콘 음극재”, “전기차 장기성장”이라는 단어가 아니다.

진짜 Stage 3는 아래가 같이 닫히는 순간이다.

```text
배터리:
고객 계약 → 실제 call-off → 공장 utilization → AMPC/보조금 지속성 → ASP/mix → gross margin → FCF

소재:
고객사 EV 생산계획 → 실제 물량 → 원재료 가격 → 판가연동 → 재고손실 → cash conversion

ESS:
EV 라인 전환 → ESS PO → LFP 생산 → 설치/납품 → margin → recurring order

태양광:
정책자금 → 부품 통관 → 공장 가동률 → 모듈 ASP → 세액공제 → 현금흐름

수소:
공장 착공 → 수요처 → 설비 utilization → 보조금/전력단가 → 전해조·연료전지 매출
```

---

# 2. 대상 canonical archetype

```text
EV_BATTERY_CONTRACT_CANCELLATION_HARD_4C
BATTERY_JV_STAGE2_WITH_EV_DEMAND_WATCH
SK_ON_RESTRUCTURING_ESS_PIVOT_STAGE2
BATTERY_MATERIAL_SUPPLY_CHAIN_BETA_4C
SOLAR_US_MANUFACTURING_POLICY_STAGE2_CUSTOMS_4C
HYDROGEN_FUEL_CELL_CAPEX_STAGE2
SILICON_ANODE_SCALEUP_STAGE2
BATTERY_DEMAND_POLICY_OVERHANG_CROSS_REFERENCE
```

---

# 3. deep sub-archetype

```text
EV battery contract:
- LG Energy Solution / Ford / Freudenberg
- 계약취소, 예상매출 손실, 유럽공장 utilization delay
- Ford EV model cancellation and policy-demand reset

Battery JV:
- Samsung SDI / GM Indiana plant
- $3.5B JV, 27GWh → 36GWh potential
- but EV demand sluggish, Q4 operating loss

SK On:
- SK Innovation / SK E&S merger
- SK On never profitable since spin-off
- Ford JV dissolution
- ESS LFP pivot, Georgia line conversion

Battery materials:
- SK IE Technology / EcoPro Materials / LGES / SK Innovation
- Ford F-150 Lightning cancellation / hybrid pivot
- battery content per vehicle sharply lower
- material supplier beta

Solar:
- Hanwha Solutions / Qcells
- U.S. $1.45B loan guarantee, $2.5B Georgia facility
- customs detentions / UFLPA supply-chain gate
- furloughs and contractor cuts

Hydrogen:
- Hyundai Motor hydrogen fuel-cell plant
- 930B won capex
- fuel cells and electrolyzers for cars, trucks, construction machinery, marine vessels
- hydrogen demand and utilization gate

Silicon anode:
- SK Inc / Group14
- $463M Series D led by SK
- full ownership of Korea BAM plant
- silicon-carbon anode as graphite substitute
- unlisted technology read-through

Policy overhang:
- U.S. tax-credit expiry, tariffs, Trump policy, EV adoption slowdown
- Korean battery makers pivoting from EV to ESS
```

---

# 4. 국장 신규 후보 case

## Case A — LG Energy Solution / Ford·Freudenberg `hard 4C`

```text
symbol = 373220
case_type = 4C-thesis-break
archetype = EV_BATTERY_CONTRACT_CANCELLATION_HARD_4C
```

### stage date

```text
Stage 1:
2024-10
- LGES signs EV battery supply contracts with Ford for Europe, scheduled to start 2026~2027.
- market frames contract as global EV battery demand visibility.

Stage 4C:
2025-12-17 / 2025-12-18
- Ford terminates EV battery supply deal worth about 9.6T won / $6.5B.
- LGES shares fall as much as -7.6%.
- KOSPI -1.4% in same early-trading context.
- analysts say replacement orders are hard to secure immediately and European plant utilization recovery could be delayed.

Stage 4C 강화:
2025-12-26
- LGES also cancels 3.9T won / $2.7B Freudenberg Battery Power Systems contract.
- combined expected revenue loss: 13.5T won.
- that is more than half of LGES 2024 revenue of 25.62T won.
```

LGES는 이번 R3의 hard 4C다. Ford 계약 취소 하나가 아니라, 일주일 안에 Ford 9.6T won과 Freudenberg 3.9T won 계약이 같이 날아가며 expected revenue loss가 13.5T won까지 커졌다. Reuters는 Ford 취소 직후 LGES가 장중 -7.6% 하락했고, 취소된 계약이 2027년 유럽공장 utilization 회복을 지연시킬 수 있다고 보도했다. 이건 “장기 EV 성장”이 아니라 **고객 call-off와 공장 utilization이 Stage 3의 본체**라는 hard reference다. ([Reuters][1])

### 실제 가격경로 검증

```json
{
  "case_id": "r3_loop14_lges_ford_freudenberg_contract_cancellation_hard_4c",
  "symbol": "373220",
  "stage3_price": null,
  "stage4c_date": "2025-12-18/2025-12-26",
  "price_data_source": "Reuters contract-cancellation and event-return anchors",
  "ford_contract_cancelled_krw_trn": 9.6,
  "ford_contract_cancelled_usd_bn": 6.5,
  "freudenberg_contract_cancelled_krw_trn": 3.9,
  "freudenberg_contract_cancelled_usd_bn": 2.7,
  "combined_cancelled_expected_revenue_krw_trn": 13.5,
  "lges_2024_revenue_krw_trn": 25.62,
  "cancelled_revenue_as_share_of_2024_revenue_pct": 52.7,
  "ford_cancellation_event_mae_pct": -7.6,
  "kospi_same_context_pct": -1.4,
  "relative_underperformance_pp": -6.2,
  "european_plant_utilization_delay_risk": true,
  "mfe_30d_90d_180d_1y": "N/A_after_4C",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = EV_battery_contract_cancellation_hard_4C
stage_failure_type = customer_calloff_and_utilization_break
```

---

## Case B — Samsung SDI / GM JV `success_candidate + EV-demand 4C-watch`

```text
symbol = 006400
case_type = success_candidate + 4C-watch
archetype = BATTERY_JV_STAGE2_WITH_EV_DEMAND_WATCH
```

### stage date

```text
Stage 1:
2024-08-27
- Samsung SDI finalizes U.S. EV battery JV with GM.
- North America localization and IRA/AMPC optionality become visible.

Stage 2:
2024-08-28
- Samsung SDI and GM complete $3.5B agreement.
- Indiana plant initial capacity 27GWh.
- potential expansion to 36GWh.
- mass production aimed for 2027.
- shares +3.2%, KOSPI -0.3%.

Stage 4C-watch:
2025-03-05
- Samsung SDI CEO says EV demand likely sluggish until H1 2026.
- Samsung SDI posted Q4 2024 operating loss of 257B won / $176.54M.
```

Samsung SDI는 Stage 2는 명확하다. GM JV는 $3.5B 규모이고, 27GWh 초기 capacity에 36GWh 확장 가능성이 있다. 발표 직후 주가도 +3.2%로 KOSPI -0.3% 대비 강했다. 하지만 2025년 3월 CEO가 EV demand가 2026년 상반기까지 부진할 수 있다고 말했고, Q4 2024에는 257B won 영업손실을 냈다. 따라서 Green은 JV 자체가 아니라 2027년 mass production, GM call-off, capacity utilization, AMPC, margin으로 확인해야 한다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "case_id": "r3_loop14_samsung_sdi_gm_jv_stage2_ev_demand_watch",
  "symbol": "006400",
  "stage2_date": "2024-08-28",
  "stage4c_watch_date": "2025-03-05",
  "stage3_price": null,
  "price_data_source": "Reuters GM JV and EV-demand anchors",
  "gm_jv_investment_usd_bn": 3.5,
  "initial_capacity_gwh": 27,
  "potential_expansion_capacity_gwh": 36,
  "capacity_expansion_pct": 33.3,
  "mass_production_target": 2027,
  "stage2_event_mfe_pct": 3.2,
  "kospi_same_context_pct": -0.3,
  "relative_outperformance_pp": 3.5,
  "q4_2024_operating_loss_krw_bn": 257,
  "q4_2024_operating_loss_usd_mn": 176.54,
  "ev_demand_sluggish_until": "H1_2026",
  "mfe_30d_90d_180d_1y": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_4C_watch
rerating_result = battery_JV_stage2
stage_failure_type = JV_capacity_not_utilization_margin_green
```

---

## Case C — SK Innovation / SK On `restructuring + ESS pivot`

```text
symbol = 096770
case_type = success_candidate_policy_restructuring + 4C-watch
archetype = SK_ON_RESTRUCTURING_ESS_PIVOT_STAGE2
```

### stage date

```text
Stage 1:
2024-07
- SK On declares emergency management amid slow EV demand.
- battery unit losses and debt burden become group-level issue.

Stage 2:
2024-08-27
- SK Innovation shareholders approve merger with SK E&S.
- merged company to have assets worth 100T won.
- goal: strengthen finances of loss-making SK On.
- SK Innovation shares +5%.
- KOSPI -0.5%.
- SK E&S 2023 OP: 1.3T won.
- SK On has not turned a profit since 2021 spin-off.

Stage 4C-watch:
2025-12-11
- SK On and Ford end U.S. battery JV.
- original joint investment: $11.4B.
- Ford takes Kentucky plants; SK On takes Tennessee facility.
- SK On Q3 2025 operating loss 124.8B won, nearly double previous quarter’s 66.4B won loss.
- Tennessee production start schedule flexible.

Stage 2 pivot:
2025-09-03
- SK On signs Flatiron ESS LFP deal.
- up to 7.2GWh from 2026 to 2030.
- plans to convert some Georgia EV battery lines for ESS.
```

SK Innovation/SK On은 R3에서 “EV slowdown → group restructuring → ESS pivot” case다. SK E&S merger approval로 SK Innovation은 +5%였고, 이건 balance-sheet relief Stage 2다. 하지만 SK On은 Ford JV까지 해체했고, Q3 2025 operating loss가 124.8B won으로 전분기 66.4B won의 거의 두 배였다. ESS 7.2GWh Flatiron deal은 좋은 pivot이지만, financial terms가 없고 실제 margin이 확인돼야 한다. ([Reuters][3])

### 실제 가격경로 검증

```json
{
  "case_id": "r3_loop14_sk_innovation_skon_restructuring_ess_pivot",
  "symbol": "096770",
  "stage2_date": "2024-08-27/2025-09-03",
  "stage4c_watch_date": "2025-12-11",
  "stage3_price": null,
  "price_data_source": "Reuters merger, JV dissolution and ESS anchors",
  "sk_innovation_merger_event_mfe_pct": 5.0,
  "kospi_merger_context_pct": -0.5,
  "merged_company_assets_krw_trn": 100,
  "sk_es_2023_op_krw_trn": 1.3,
  "sk_es_2023_sales_krw_trn": 11.2,
  "sk_on_profit_history": "not_profitable_since_2021_spin_off",
  "blueoval_sk_original_investment_usd_bn": 11.4,
  "sk_on_q3_2025_op_loss_krw_bn": 124.8,
  "sk_on_q2_2025_op_loss_krw_bn": 66.4,
  "q3_loss_vs_q2_loss_increase_pct": 88.0,
  "flatiron_ess_supply_gwh": 7.2,
  "flatiron_ess_supply_period": "2026-2030",
  "ess_contract_value_disclosed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_restructuring_but_4C_watch
rerating_result = SK_On_ESS_pivot_stage2
stage_failure_type = EV_capacity_reset_not_ESS_margin_green
```

---

## Case D — EcoPro Materials / SK IE Technology / battery-material beta `price_moved_without_evidence + 4C-watch`

```text
symbols = 450080 / 361610 / 096770 / 373220
case_type = 4C-watch
archetype = BATTERY_MATERIAL_SUPPLY_CHAIN_BETA_4C
```

### stage date

```text
Stage 1:
2025-12-16
- Ford announces large EV-related charge and pivots from full EVs to hybrids.
- F-150 Lightning EV production direction changes.
- Korean battery supply chain reprices.

Stage 4C-watch:
2025-12-16
- SK Innovation -3%.
- LG Energy Solution -6%.
- SK IE Technology -5%.
- EcoPro Materials -5%.
- Citi says Ford shift is negative for Korean battery supply chain.
- lower-battery-content hybrid replacement means less battery content per vehicle.
```

이 case는 R3 소재주 scoring의 핵심이다. Battery-material supplier는 “EV 장기성장”보다 고객의 모델 mix와 battery content per vehicle에 더 민감하다. MarketWatch는 Ford가 full EV에서 hybrid/EREV 쪽으로 방향을 바꾸자 SK Innovation, LGES, SK IE Technology, EcoPro Materials가 3~6% 하락했다고 보도했다. 특히 “hybrid로 가면 배터리 함량이 줄어든다”는 점이 소재주에는 직접 4C다. ([마켓워치][4])

### 실제 가격경로 검증

```json
{
  "case_id": "r3_loop14_battery_material_supply_chain_ford_beta",
  "symbols": "450080/361610/096770/373220",
  "stage4c_watch_date": "2025-12-16",
  "stage3_price": null,
  "price_data_source": "MarketWatch Ford EV pivot / Korea battery supply-chain anchor",
  "ford_charge_context_usd_bn": 20,
  "sk_innovation_event_mae_pct": -3,
  "lg_energy_solution_event_mae_pct": -6,
  "sk_ie_technology_event_mae_pct": -5,
  "ecopro_materials_event_mae_pct": -5,
  "battery_content_risk": "lower_battery_content_in_hybrid_or_EREV_replacement",
  "stage3_mfe_mae": "N/A_no_valid_stage3",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = battery_material_customer_mix_beta
stage_failure_type = EV_model_mix_lower_battery_content
```

---

## Case E — Hanwha Solutions / Qcells `solar policy success + customs 4C-watch`

```text
symbol = 009830 / 000880 read-through
case_type = success_candidate + 4C-watch
archetype = SOLAR_US_MANUFACTURING_POLICY_STAGE2_CUSTOMS_4C
```

### stage date

```text
Stage 1:
2024-08-08
- U.S. DOE offers conditional loan guarantee for Qcells.
- U.S. solar manufacturing and IRA/localization theme.

Stage 2:
2024-08-08
- conditional loan guarantee up to $1.45B.
- supports $2.5B Cartersville, Georgia facility.
- plant to produce solar panels and inputs including cells, ingots and wafers.
- enough annual solar panels to power about 500,000 households.
- nearly 2,000 jobs once fully operational.
- loan conditional on financial/legal/other requirements.

Stage 4C-watch:
2025-11-08
- Qcells furloughs around 1,000 workers at Georgia factories.
- about 300 contract workers cut.
- overseas components detained by U.S. customs under forced-labor import law.
- production temporarily curtailed.
```

Qcells는 친환경 policy success와 supply-chain 4C가 동시에 있는 case다. $1.45B DOE loan guarantee와 $2.5B Georgia plant는 강한 Stage 2다. 하지만 2025년에는 U.S. customs가 부품을 억류하며 Georgia factory workers 1,000명을 furlough하고 300 contract workers를 줄였다. 태양광에서 Green은 “미국 공장”이 아니라 **부품 통관, full supply-chain localization, factory utilization, module ASP, tax credit monetization**이다. ([Reuters][5])

### 실제 가격경로 검증

```json
{
  "case_id": "r3_loop14_hanwha_qcells_solar_policy_customs_gate",
  "symbol": "009830",
  "stage2_date": "2024-08-08",
  "stage4c_watch_date": "2025-11-08",
  "stage3_price": null,
  "price_data_source": "Reuters DOE loan guarantee and Qcells furlough anchors",
  "doe_conditional_loan_guarantee_usd_bn": 1.45,
  "cartersville_facility_investment_usd_bn": 2.5,
  "households_powered_per_year_context": 500000,
  "jobs_when_operational": 2000,
  "furloughed_workers": 1000,
  "contract_workers_cut": 300,
  "customs_issue": "component_shipments_detained_under_forced_labor_import_law",
  "full_production_resumption_confirmed": false,
  "parent_stock_ohlc": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_4C_watch
rerating_result = solar_US_manufacturing_policy_stage2
stage_failure_type = policy_loan_not_factory_utilization_green
```

---

## Case F — Hyundai Motor hydrogen fuel-cell plant `green capex Stage 2`

```text
symbol = 005380
case_type = success_candidate
archetype = HYDROGEN_FUEL_CELL_CAPEX_STAGE2
```

### stage date

```text
Stage 1:
2025-10-30
- Hyundai breaks ground on hydrogen fuel-cell plant in Ulsan.
- hydrogen mobility and electrolyzer strategy becomes visible.

Stage 2:
2025-10-30
- 930B won / $654M facility.
- 43,000 square metres.
- construction completion expected in 2027.
- products: fuel cells and electrolyzers.
- applications: passenger cars, commercial trucks, buses, construction machinery, marine vessels.
- site is former internal-combustion transmission plant.

Stage 3:
없음
- hydrogen capex is not Green.
- Green requires customer demand, utilization, cost/kW, subsidy, power price, unit margin.
```

Hyundai hydrogen plant는 R3 친환경 Stage 2다. Reuters는 현대차가 930B won 규모 Ulsan hydrogen fuel-cell facility 착공을 발표했고, fuel cells와 electrolyzers를 승용차·상용트럭·버스·건설장비·선박용으로 만들 계획이라고 보도했다. 다만 hydrogen은 capex가 먼저고 demand가 뒤따르기 쉬운 영역이다. Stage 3는 공장 완공이 아니라 고객 수요와 unit economics다. ([Reuters][6])

### 실제 가격경로 검증

```json
{
  "case_id": "r3_loop14_hyundai_hydrogen_fuel_cell_capex_stage2",
  "symbol": "005380",
  "stage2_date": "2025-10-30",
  "stage3_price": null,
  "price_data_source": "Reuters Hyundai hydrogen fuel-cell plant anchor",
  "facility_investment_krw_bn": 930,
  "facility_investment_usd_mn": 654,
  "site_area_sqm": 43000,
  "completion_expected": 2027,
  "products": ["fuel_cells", "electrolyzers"],
  "applications": ["passenger_cars", "commercial_trucks", "buses", "construction_equipment", "marine_vessels"],
  "former_site": "internal_combustion_transmission_plant",
  "customer_demand_confirmed": false,
  "unit_economics_confirmed": false,
  "mfe_mae": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_but_capex_gate
rerating_result = hydrogen_fuel_cell_capex_stage2
stage_failure_type = hydrogen_capex_not_utilization_margin_green
```

---

## Case G — SK Inc / Group14 silicon anode `success_candidate + unlisted read-through`

```text
symbol = 034730 read-through
case_type = success_candidate + insufficient_evidence
archetype = SILICON_ANODE_SCALEUP_STAGE2
```

### stage date

```text
Stage 1:
2025-08-20
- SK-led financing for Group14 Technologies.
- silicon-carbon anode material replaces graphite and improves charge speed / energy density.
- Korea battery material plant becomes part of regional supply-chain strategy.

Stage 2:
2025-08-20
- Group14 raises $463M Series D led by SK.
- total equity raised exceeds $1B.
- Group14 acquires remaining 75% stake in JV with SK.
- gains full ownership of South Korea BAM factory.
- SCC55 silicon-carbon material can replace graphite anodes.
- now owns three BAM factories, two in Washington and one in Korea.

Stage 3:
없음
- unlisted tech scale-up is not SK Inc Green.
- Green requires customer contracts, production ramp, yield, ASP, margin and SK listed value bridge.
```

Group14/SK는 좋은 battery-material technology Stage 2다. Reuters는 Group14가 SK 주도로 $463M Series D를 조달했고, SK와의 JV 잔여 75%를 인수해 한국의 BAM factory 전체 소유권을 확보했다고 보도했다. 하지만 이것은 비상장 material scale-up이고, SK Inc 주가 Green은 아니다. 실제 고객계약, yield, 생산 ramp, margin, listed value bridge가 필요하다. ([Reuters][7])

### 실제 가격경로 검증

```json
{
  "case_id": "r3_loop14_sk_group14_silicon_anode_stage2",
  "symbol": "034730_readthrough",
  "stage2_date": "2025-08-20",
  "stage3_price": null,
  "price_data_source": "Reuters Group14 financing and JV-control anchor",
  "series_d_funding_usd_mn": 463,
  "total_equity_raised_usd_bn": 1.0,
  "remaining_jv_stake_acquired_pct": 75,
  "bam_factories_total": 3,
  "bam_factories_locations": ["Washington_1", "Washington_2", "South_Korea"],
  "material": "SCC55_silicon_carbon_composite",
  "graphite_replacement_potential": true,
  "customer_contracts_confirmed": false,
  "listed_sk_value_bridge_confirmed": false,
  "mfe_mae": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_but_insufficient_evidence
rerating_result = silicon_anode_scaleup_stage2
stage_failure_type = unlisted_material_scaleup_not_listed_EPS_green
```

---

## Case H — LGES / Samsung SDI / SK On ESS pivot basket `success_candidate + policy overhang`

```text
symbols = 373220 / 006400 / 096770
case_type = success_candidate + 4B-watch
archetype = BATTERY_DEMAND_POLICY_OVERHANG_CROSS_REFERENCE
```

### stage date

```text
Stage 1:
2025-07~09
- U.S. tariffs and federal EV purchase subsidy expiry threaten EV battery demand.
- Korean battery makers begin shifting capacity toward ESS.

Stage 2:
2025-09-03 / 2025-12-11
- SK On signs up to 7.2GWh LFP ESS supply deal with Flatiron for 2026~2030.
- SK On plans to convert Georgia EV lines for ESS.
- LGES and Samsung SDI also repurpose EV production lines toward ESS due subsidy phase-out and slower EV demand.
- ESS batteries can use similar chemistry and serve data centers / energy-storage facilities.

Stage 3:
없음
- ESS pivot is not Green until actual PO value, shipment, installation, margin and repeat order confirm.
```

ESS pivot는 R3의 다음 cycle 후보지만, 아직 Stage 2다. Reuters는 SK On이 Flatiron에 2026~2030년 최대 7.2GWh LFP ESS batteries를 공급하기로 했고, Georgia EV battery lines 일부를 ESS로 전환할 계획이라고 보도했다. 또한 LGES와 Samsung SDI도 EV 수요 둔화와 subsidy phase-out에 대응해 ESS 생산으로 전환 중이라고 설명했다. 다만 contract value가 공개되지 않았고, 실제 installation과 margin이 확인되어야 한다. ([Reuters][8])

### 실제 가격경로 검증

```json
{
  "case_id": "r3_loop14_korean_battery_ess_pivot_cross_reference",
  "symbols": "373220/006400/096770",
  "stage2_date": "2025-09-03/2025-12-11",
  "stage3_price": null,
  "price_data_source": "Reuters SK On ESS and battery-sector pivot anchors",
  "flatiron_ess_supply_gwh": 7.2,
  "supply_period": "2026-2030",
  "lFP_ESS_first_order": true,
  "ev_line_conversion_for_ess": "Georgia_EV_lines_some_conversion_planned",
  "contract_value_disclosed": false,
  "lges_samsung_sdi_ess_repurposing_context": true,
  "data_center_energy_storage_demand_context": true,
  "actual_installation_margin_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_4B_watch
rerating_result = ESS_pivot_stage2
stage_failure_type = ESS_pivot_not_PO_value_margin_green
```

---

# 5. 이번 R3 case별 stage date 요약

| case                     | Stage 1    | Stage 2                          | Stage 3 | Stage 4B                   | Stage 4C                |
| ------------------------ | ---------- | -------------------------------- | ------- | -------------------------- | ----------------------- |
| LGES / Ford·Freudenberg  | 2024-10    | N/A                              | N/A     | N/A                        | 2025-12 hard            |
| Samsung SDI / GM JV      | 2024-08    | 2024-08-28                       | N/A     | JV premium watch           | 2025 EV-demand watch    |
| SK Innovation / SK On    | 2024-07    | 2024-08 / 2025-09 ESS            | N/A     | ESS pivot watch            | 2025-12 Ford JV reset   |
| EcoPro Materials / SK IE | 2025-12    | N/A                              | N/A     | N/A                        | Ford hybrid pivot watch |
| Hanwha/Qcells            | 2024-08    | DOE loan / U.S. factory          | N/A     | policy premium watch       | 2025 customs/furlough   |
| Hyundai hydrogen         | 2025-10    | 930B won plant                   | N/A     | hydrogen capex watch       | utilization risk        |
| SK/Group14               | 2025-08    | $463M funding / Korean BAM plant | N/A     | silicon-anode tech premium | unlisted bridge risk    |
| ESS pivot basket         | 2025-07~09 | 7.2GWh Flatiron deal             | N/A     | ESS demand watch           | EV line-conversion risk |

---

# 6. 실제 가격경로 검증 총괄

| case                |                                            가격·계약 anchor | 해석                                     | 판정                |
| ------------------- | ------------------------------------------------------: | -------------------------------------- | ----------------- |
| LGES                |                  -7.6%, 13.5T won expected revenue loss | contract/call-off hard break           | thesis_break      |
| Samsung SDI         |                 +3.2%, $3.5B JV, later 257B won OP loss | JV Stage 2 + EV demand gate            | success_candidate |
| SK Innovation/SK On | +5% merger relief, later Ford JV split, 124.8B won loss | restructuring and ESS pivot, not Green | 4C-watch          |
| EcoPro/SK IE beta   |      SKI -3%, LGES -6%, SK IE -5%, EcoPro Materials -5% | Ford model mix lowers battery content  | 4C-watch          |
| Hanwha/Qcells       |                  $1.45B DOE loan, later 1,000 furloughs | solar policy success + customs gate    | success_candidate |
| Hyundai hydrogen    |                                          930B won plant | capex Stage 2, utilization absent      | success_candidate |
| SK/Group14          |               $463M funding, full Korea plant ownership | unlisted tech scale-up                 | insufficient      |
| ESS pivot           |                          7.2GWh deal, value undisclosed | next-cycle Stage 2                     | success_candidate |

---

# 7. score-price alignment 판정

```text
aligned:
- none as full Stage 3 this round.

structural_success_candidate:
- ESS pivot basket, if actual contract value / shipment / margin later confirms.
- Hanwha/Qcells, if full supply-chain localization and utilization confirm.
- Samsung SDI GM JV, if 2027 call-off and margin confirm.

success_candidate:
- Samsung SDI / GM JV.
- SK On / ESS pivot.
- Hyundai hydrogen fuel-cell capex.
- SK/Group14 silicon anode.
- Qcells U.S. manufacturing.

evidence_good_but_price_failed:
- Samsung SDI, if JV is scored as Green while later EV-demand loss dominates.
- Hanwha/Qcells, if policy loan is scored before customs/factory utilization.

event_premium:
- ESS pivot headlines.
- hydrogen capex.
- silicon-anode funding.
- solar policy loan.

price_moved_without_evidence:
- battery-material stocks if traded on “EV long-term growth” without customer model/call-off.
- ESS pivot before disclosed contract value and installation.
- hydrogen plant before demand/utilization.
- silicon anode before customer contracts and listed EPS bridge.

thesis_break:
- LGES Ford/Freudenberg cancellation.

thesis_break_watch:
- SK On Ford JV dissolution.
- EcoPro Materials / SK IE Technology supply-chain beta.
- Hanwha/Qcells customs detention.
- Samsung SDI EV-demand slump.

hard_4C_confirmed:
- LG Energy Solution contract-cancellation hard 4C.
```

---

# 8. 점수비중 교정

## 올릴 축

```text
customer_calloff_visibility +5
contract_cancellation_risk +5
plant_utilization +5
EV_model_mix_battery_content +5
subsidy_tariff_policy_stability +5
ESS_PO_value_and_margin +5
supply_chain_customs_clearance +5
localization_execution +4
raw_material_cost_pass_through +4
listed_value_bridge_for_unlisted_tech +4
```

### 왜 올리나

LGES는 계약 취소가 expected revenue의 절반 이상을 날릴 수 있다는 걸 보여줬다. Samsung SDI는 $3.5B JV가 좋아도 EV demand가 2026년 상반기까지 부진하면 Green이 아니다. SK On은 EV battery lines를 ESS로 바꾸는 pivot이 Stage 2로는 좋지만, 계약가와 margin이 없다. Hanwha/Qcells는 정책자금이 있어도 부품 통관이 막히면 공장이 멈춘다. EcoPro/SK IE는 Ford model mix 하나로 battery content가 줄면 소재주도 같이 맞는다.

## 내릴 축

```text
EV_growth_headline_only -5
signed_contract_without_calloff -5
capacity_capex_without_utilization -5
IRA_or_policy_loan_only -5
ESS_pivot_without_contract_value -5
hybrid_shift_ignored -5
unlisted_material_tech_readthrough -4
solar_factory_without_customs_clearance -5
hydrogen_capex_without_demand -4
```

### 왜 내리나

R3에서 가장 큰 함정은 “배터리 산업은 장기 성장하니까 계약·공장·정책자금은 다 Green”이라고 보는 것이다. 실제로는 Ford가 EV 모델을 취소하면 LGES 계약도, SK On JV도, EcoPro/SK IE 같은 소재 chain도 동시에 흔들린다. 배터리 산업은 성장산업이지만, Stage 3는 고객의 실제 생산계획과 call-off에 붙어 있다.

---

# 9. Green gate 강화 조건

```text
R3 Stage 3-Green 필수:
1. 계약이 실제 call-off / shipment / revenue recognition으로 전환.
2. 공장 utilization이 확인됨.
3. AMPC / IRA / tariff / subsidy 지속성이 확인됨.
4. EV 모델 mix가 BEV에서 hybrid/EREV로 바뀌어 battery content가 줄지 확인.
5. ESS pivot은 contract value, shipment, installation, margin 확인.
6. 소재주는 raw material cost pass-through와 customer production schedule 확인.
7. 태양광은 customs clearance, full supply-chain localization, module ASP 확인.
8. 수소는 고객 수요, cost/kW, utilization, subsidy 확인.
9. 비상장 기술은 listed EPS/value bridge 확인.
10. price path가 evidence 이후 따라옴.
```

---

# 10. 4B 조기감지 조건

```text
4B-watch:
- EV battery plant / JV headline로 주가 선반영.
- ESS pivot headline로 margin 확인 전 rerating.
- hydrogen capex announcement로 demand 확인 전 rerating.
- silicon anode / recycling / next-gen battery tech funding만으로 상장사 read-through.
- solar U.S. manufacturing policy loan으로 통관/utilization 전 선반영.
- Ford/GM/Hyundai customer-name 계약이 actual call-off 없이 가격화.
```

---

# 11. 4C hard gate 조건

```text
Hard 4C:
- major customer contract cancellation.
- automaker EV model cancellation / BEV-to-hybrid shift lowering battery content.
- plant utilization delay.
- subsidy / tax-credit expiry damaging demand.
- customs detention blocking solar/battery component shipments.
- JV dissolution or capacity transfer.
- repeated operating losses with no utilization recovery.
- raw material price collapse causing inventory loss.
```

이번 R3 Loop 14의 hard 4C는 **LGES Ford/Freudenberg contract cancellation**이다. SK On, Samsung SDI, Qcells, EcoPro/SK IE는 hard 4C가 아니라 **4C-watch / policy-relief / pivot-stage2**로 둔다.

---

# 12. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 13. 레포 반영용 patch-ready 출력

## docs/round/round_213.md 요약

```md
# R3 Loop 14. Secondary Battery / EV / Green Energy Price Validation

이번 라운드는 R3 Loop 14 price-validation 라운드다.

핵심 결론:
- LG Energy Solution is hard 4C. Ford terminated a 9.6T won / $6.5B EV battery deal, LGES shares fell as much as -7.6%, and Freudenberg later cancelled another 3.9T won / $2.7B contract. Combined lost expected revenue was 13.5T won, more than half of 2024 revenue.
- Samsung SDI / GM JV is Stage 2 plus EV-demand 4C-watch. $3.5B Indiana JV, 27GWh initial capacity, 36GWh potential, mass production target 2027, shares +3.2%. But EV demand expected sluggish until H1 2026 and Q4 2024 OP loss was 257B won.
- SK Innovation / SK On is restructuring plus ESS pivot Stage 2. SK Innovation shares +5% after SK E&S merger approval; merged company assets 100T won. SK On later ended Ford JV and posted Q3 2025 OP loss 124.8B won. ESS Flatiron deal offers up to 7.2GWh from 2026 to 2030, but value and margin undisclosed.
- EcoPro Materials / SK IE Technology supply-chain beta is 4C-watch. Ford’s EV-to-hybrid pivot drove SK Innovation -3%, LGES -6%, SK IE -5%, EcoPro Materials -5%; lower-battery-content vehicles hurt the Korean battery supply chain.
- Hanwha/Qcells is solar policy success_candidate plus customs 4C-watch. U.S. DOE loan guarantee up to $1.45B for $2.5B Cartersville facility; later Qcells furloughed 1,000 workers and cut 300 contractors due customs detentions of components.
- Hyundai hydrogen fuel-cell plant is green-capex Stage 2. 930B won / $654M Ulsan facility, completion expected 2027, fuel cells and electrolyzers for vehicles, construction equipment and marine uses. Utilization and unit economics required.
- SK / Group14 is silicon-anode Stage 2. Group14 raised $463M led by SK, total equity raised over $1B, and acquired remaining 75% of JV to fully own Korea BAM factory. Listed SK value bridge unconfirmed.
- Battery ESS pivot basket is Stage 2. Korean battery makers are repurposing EV battery lines toward ESS; actual PO value, installation, margin and repeat orders required.
```

## docs/checkpoints/checkpoint_28a_round213_r3_loop14.md 요약

```md
# Checkpoint 28A Round 213 R3 Loop 14 Secondary Battery EV Green Energy Price Validation

## 반영 내용
- R3 Loop 14 price-validation 라운드를 추가했다.
- LGES contract cancellation, Samsung SDI/GM JV, SK On restructuring/ESS pivot, EcoPro/SK IE battery-material beta, Hanwha/Qcells solar factory/customs, Hyundai hydrogen plant, SK/Group14 silicon anode, Korean ESS pivot basket을 비교했다.
- Reuters / AP / MarketWatch anchors로 가능한 event MFE/MAE, contract value, operating loss, plant investment, JV reset, furlough and funding metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- customer call-off visibility, contract cancellation risk, plant utilization, EV model mix/battery content, subsidy/tariff stability, ESS PO value and margin, supply-chain customs clearance, localization execution, raw-material pass-through, listed value bridge 가중치 강화.
- EV growth headline-only, signed contract without call-off, capacity capex without utilization, IRA/policy loan-only, ESS pivot without contract value, hybrid shift ignored, unlisted technology read-through 감점 강화.
```

## data/e2r_case_library/cases_r3_loop14_round213.jsonl 초안

```jsonl
{"case_id":"r3_loop14_lges_ford_freudenberg_contract_cancellation_hard_4c","symbol":"373220","company_name":"LG Energy Solution","case_type":"4c_thesis_break","primary_archetype":"EV_BATTERY_CONTRACT_CANCELLATION_HARD_4C","stage4c_date":"2025-12-18/2025-12-26","price_validation":{"price_data_source":"Reuters contract-cancellation and event-return anchors","stage3_price":null,"ford_contract_cancelled_krw_trn":9.6,"ford_contract_cancelled_usd_bn":6.5,"freudenberg_contract_cancelled_krw_trn":3.9,"freudenberg_contract_cancelled_usd_bn":2.7,"combined_cancelled_expected_revenue_krw_trn":13.5,"lges_2024_revenue_krw_trn":25.62,"cancelled_revenue_as_share_of_2024_revenue_pct":52.7,"ford_cancellation_event_mae_pct":-7.6,"kospi_same_context_pct":-1.4,"relative_underperformance_pp":-6.2,"european_plant_utilization_delay_risk":true,"mae_30d_90d_180d_1y":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break","rerating_result":"EV_battery_contract_cancellation_hard_4C","notes":"Major customer call-off broke expected revenue and utilization thesis."}
{"case_id":"r3_loop14_samsung_sdi_gm_jv_stage2_ev_demand_watch","symbol":"006400","company_name":"Samsung SDI","case_type":"success_candidate_4c_watch","primary_archetype":"BATTERY_JV_STAGE2_WITH_EV_DEMAND_WATCH","stage2_date":"2024-08-28","stage4c_date":"2025-03-05_watch","price_validation":{"price_data_source":"Reuters GM JV and EV-demand anchors","stage3_price":null,"gm_jv_investment_usd_bn":3.5,"initial_capacity_gwh":27,"potential_expansion_capacity_gwh":36,"capacity_expansion_pct":33.3,"mass_production_target":2027,"stage2_event_mfe_pct":3.2,"kospi_same_context_pct":-0.3,"relative_outperformance_pp":3.5,"q4_2024_operating_loss_krw_bn":257,"q4_2024_operating_loss_usd_mn":176.54,"ev_demand_sluggish_until":"H1_2026","mfe_30d_90d_180d_1y":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_4C_watch","rerating_result":"battery_JV_stage2","notes":"JV capacity is Stage 2; actual call-off, utilization, AMPC and margin required."}
{"case_id":"r3_loop14_sk_innovation_skon_restructuring_ess_pivot","symbol":"096770","company_name":"SK Innovation / SK On","case_type":"success_candidate_restructuring_4c_watch","primary_archetype":"SK_ON_RESTRUCTURING_ESS_PIVOT_STAGE2","stage2_date":"2024-08-27/2025-09-03","stage4c_date":"2025-12-11_watch","price_validation":{"price_data_source":"Reuters merger, JV dissolution and ESS anchors","stage3_price":null,"sk_innovation_merger_event_mfe_pct":5.0,"kospi_merger_context_pct":-0.5,"merged_company_assets_krw_trn":100,"sk_es_2023_op_krw_trn":1.3,"sk_es_2023_sales_krw_trn":11.2,"sk_on_profit_history":"not_profitable_since_2021_spin_off","blueoval_sk_original_investment_usd_bn":11.4,"sk_on_q3_2025_op_loss_krw_bn":124.8,"sk_on_q2_2025_op_loss_krw_bn":66.4,"q3_loss_vs_q2_loss_increase_pct":88.0,"flatiron_ess_supply_gwh":7.2,"flatiron_ess_supply_period":"2026-2030","ess_contract_value_disclosed":false,"mfe_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_restructuring_but_4C_watch","rerating_result":"SK_On_ESS_pivot_stage2","notes":"ESS pivot is promising but EV capacity reset and losses remain."}
{"case_id":"r3_loop14_battery_material_supply_chain_ford_beta","symbol":"450080/361610/096770/373220","company_name":"EcoPro Materials / SK IE Technology / SK Innovation / LGES","case_type":"4c_watch","primary_archetype":"BATTERY_MATERIAL_SUPPLY_CHAIN_BETA_4C","stage4c_date":"2025-12-16_watch","price_validation":{"price_data_source":"MarketWatch Ford EV pivot / Korea battery supply-chain anchor","stage3_price":null,"ford_charge_context_usd_bn":20,"sk_innovation_event_mae_pct":-3,"lg_energy_solution_event_mae_pct":-6,"sk_ie_technology_event_mae_pct":-5,"ecopro_materials_event_mae_pct":-5,"battery_content_risk":"lower_battery_content_in_hybrid_or_EREV_replacement","mae_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"battery_material_customer_mix_beta","notes":"EV-to-hybrid model mix can reduce battery content and hit material suppliers."}
{"case_id":"r3_loop14_hanwha_qcells_solar_policy_customs_gate","symbol":"009830","company_name":"Hanwha Solutions / Qcells","case_type":"success_candidate_4c_watch","primary_archetype":"SOLAR_US_MANUFACTURING_POLICY_STAGE2_CUSTOMS_4C","stage2_date":"2024-08-08","stage4c_date":"2025-11-08_watch","price_validation":{"price_data_source":"Reuters DOE loan guarantee and Qcells furlough anchors","stage3_price":null,"doe_conditional_loan_guarantee_usd_bn":1.45,"cartersville_facility_investment_usd_bn":2.5,"households_powered_per_year_context":500000,"jobs_when_operational":2000,"furloughed_workers":1000,"contract_workers_cut":300,"customs_issue":"component_shipments_detained_under_forced_labor_import_law","full_production_resumption_confirmed":false,"parent_stock_ohlc":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_4C_watch","rerating_result":"solar_US_manufacturing_policy_stage2","notes":"Policy loan and U.S. factory are Stage 2; customs clearance and utilization required."}
{"case_id":"r3_loop14_hyundai_hydrogen_fuel_cell_capex_stage2","symbol":"005380","company_name":"Hyundai Motor","case_type":"success_candidate_capex_gate","primary_archetype":"HYDROGEN_FUEL_CELL_CAPEX_STAGE2","stage2_date":"2025-10-30","price_validation":{"price_data_source":"Reuters Hyundai hydrogen fuel-cell plant anchor","stage3_price":null,"facility_investment_krw_bn":930,"facility_investment_usd_mn":654,"site_area_sqm":43000,"completion_expected":2027,"products":["fuel_cells","electrolyzers"],"applications":["passenger_cars","commercial_trucks","buses","construction_equipment","marine_vessels"],"former_site":"internal_combustion_transmission_plant","customer_demand_confirmed":false,"unit_economics_confirmed":false,"mfe_mae":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_capex_gate","rerating_result":"hydrogen_fuel_cell_capex_stage2","notes":"Hydrogen plant capex is not Green until demand, utilization and unit economics confirm."}
{"case_id":"r3_loop14_sk_group14_silicon_anode_stage2","symbol":"034730_readthrough","company_name":"SK / Group14 Technologies","case_type":"success_candidate_insufficient_evidence","primary_archetype":"SILICON_ANODE_SCALEUP_STAGE2","stage2_date":"2025-08-20","price_validation":{"price_data_source":"Reuters Group14 financing and JV-control anchor","stage3_price":null,"series_d_funding_usd_mn":463,"total_equity_raised_usd_bn":1.0,"remaining_jv_stake_acquired_pct":75,"bam_factories_total":3,"bam_factories_locations":["Washington_1","Washington_2","South_Korea"],"material":"SCC55_silicon_carbon_composite","graphite_replacement_potential":true,"customer_contracts_confirmed":false,"listed_sk_value_bridge_confirmed":false,"mfe_mae":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_insufficient_evidence","rerating_result":"silicon_anode_scaleup_stage2","notes":"Unlisted battery-material technology needs customer contracts, yield, margin and listed value bridge."}
{"case_id":"r3_loop14_korean_battery_ess_pivot_cross_reference","symbol":"373220/006400/096770","company_name":"LGES / Samsung SDI / SK On ESS pivot basket","case_type":"success_candidate_4b_watch","primary_archetype":"BATTERY_DEMAND_POLICY_OVERHANG_CROSS_REFERENCE","stage2_date":"2025-09-03/2025-12-11","price_validation":{"price_data_source":"Reuters SK On ESS and battery-sector pivot anchors","stage3_price":null,"flatiron_ess_supply_gwh":7.2,"supply_period":"2026-2030","lfp_ess_first_order":true,"ev_line_conversion_for_ess":"Georgia_EV_lines_some_conversion_planned","contract_value_disclosed":false,"lges_samsung_sdi_ess_repurposing_context":true,"data_center_energy_storage_demand_context":true,"actual_installation_margin_confirmed":false,"mfe_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_4B_watch","rerating_result":"ESS_pivot_stage2","notes":"ESS pivot is Stage 2; PO value, installation, margin and repeat orders required."}
```

## data/sector_taxonomy/score_weight_profiles_round213_r3_loop14_v1.csv 초안

```csv
archetype,customer_calloff_visibility,contract_cancellation_risk,plant_utilization,ev_model_mix_battery_content,subsidy_tariff_policy_stability,ess_po_value_margin,supply_chain_customs_clearance,localization_execution,raw_material_cost_pass_through,listed_value_bridge,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
EV_BATTERY_CONTRACT_CANCELLATION_HARD_4C,+5,+5,+5,+5,+5,+2,+3,+4,+3,+2,0,+4,+5,LGES cancellation shows call-off and utilization are hard gates.
BATTERY_JV_STAGE2_WITH_EV_DEMAND_WATCH,+5,+4,+5,+5,+5,+2,+2,+5,+3,+2,-4,+4,+4,Samsung SDI GM JV needs 2027 production, call-off, AMPC and margin.
SK_ON_RESTRUCTURING_ESS_PIVOT_STAGE2,+5,+5,+5,+5,+5,+5,+2,+4,+3,+3,-4,+5,+4,SK On restructuring/ESS pivot needs disclosed PO value and profitability.
BATTERY_MATERIAL_SUPPLY_CHAIN_BETA_4C,+5,+5,+4,+5,+5,+1,+3,+3,+5,+2,0,+5,+4,Ford hybrid pivot shows lower battery content can hit materials.
SOLAR_US_MANUFACTURING_POLICY_STAGE2_CUSTOMS_4C,+3,+3,+5,+0,+5,+0,+5,+5,+4,+2,-5,+5,+4,Qcells needs customs clearance and factory utilization after policy loan.
HYDROGEN_FUEL_CELL_CAPEX_STAGE2,+3,+3,+5,+0,+5,+1,+2,+4,+3,+2,-5,+5,+3,Hyundai hydrogen capex requires demand, utilization and unit economics.
SILICON_ANODE_SCALEUP_STAGE2,+5,+4,+5,+4,+4,+2,+3,+4,+5,+5,-5,+5,+4,Group14/SK needs customer contracts, yield, margin and listed value bridge.
BATTERY_DEMAND_POLICY_OVERHANG_CROSS_REFERENCE,+5,+5,+5,+5,+5,+5,+3,+4,+4,+3,-5,+5,+4,ESS pivot is not Green until PO value, shipment, installation and margin confirm.
```

---

# 이번 R3 Loop 14 결론

```text
1. LG Energy Solution은 R3 hard 4C다.
   Ford/Freudenberg 계약취소로 13.5T won expected revenue가 사라졌고, 이는 2024 revenue의 52.7% 수준이다.

2. Samsung SDI는 GM JV Stage 2다.
   $3.5B, 27GWh~36GWh capacity는 좋지만 EV demand와 Q4 operating loss가 4C-watch다.

3. SK Innovation/SK On은 restructuring + ESS pivot Stage 2다.
   SK E&S merger와 Flatiron ESS deal은 좋지만 Ford JV 해체와 SK On 손실이 남아 있다.

4. EcoPro Materials / SK IE Technology는 고객 model mix beta다.
   Ford가 EV에서 hybrid/EREV로 옮기면 battery content가 줄고 소재주도 바로 맞는다.

5. Hanwha/Qcells는 solar policy success_candidate지만 customs gate가 있다.
   $1.45B loan guarantee보다 부품 통관과 공장 utilization이 Stage 3 조건이다.

6. Hyundai hydrogen plant는 green capex Stage 2다.
   공장 착공은 수요가 아니고, utilization과 unit economics가 필요하다.

7. SK/Group14는 silicon-anode technology Stage 2다.
   비상장 기술 scale-up은 listed EPS/value bridge 없이는 Green이 아니다.

8. ESS pivot은 다음 cycle 후보지만 아직 Stage 2다.
   EV 라인 전환과 7.2GWh headline보다 PO value, installation, margin이 중요하다.
```

한 문장으로 압축하면:

> **R3에서 진짜 Stage 3는 “배터리·EV·IRA·태양광·수소·ESS가 좋다”가 아니라, 고객 call-off·공장 utilization·battery content·보조금 지속성·customs clearance·ESS PO value·margin·FCF가 실제 숫자로 닫히는 순간이다.**

* [Reuters](https://www.reuters.com/business/energy/shares-south-koreas-lges-drop-more-than-7-after-ford-cancels-ev-battery-deal-2025-12-18/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/energy/lg-energy-solution-cancels-39-trillion-won-battery-order-with-freudenberg-2025-12-26/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/markets/deals/samsung-sdi-signs-deal-with-gm-its-joint-ev-battery-factory-us-2024-08-27/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/autos-transportation/samsung-sdi-ceo-says-ev-demand-remain-sluggish-until-h1-2026-2025-03-05/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/markets/deals/sk-innovation-shareholders-approve-merger-plan-with-sk-es-yonhap-reports-2024-08-27/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/autos-transportation/south-koreas-sk-ford-motor-end-us-battery-joint-venture-2025-12-11/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/energy/south-koreas-sk-signs-energy-storage-battery-supply-deal-with-flatiron-energy-2025-09-03/?utm_source=chatgpt.com)
* [마켓워치](https://www.marketwatch.com/story/while-ford-shares-are-remarkably-steady-after-20-billion-charge-these-stocks-are-getting-battered-bbbcfa04?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/energy/us-offers-15-bln-conditional-loan-guarantee-qcells-solar-facility-georgia-2024-08-08/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/sustainability/climate-energy/qcells-furloughs-1000-workers-us-solar-factories-due-stalled-shipments-2025-11-08/?utm_source=chatgpt.com)

[1]: https://www.reuters.com/business/energy/shares-south-koreas-lges-drop-more-than-7-after-ford-cancels-ev-battery-deal-2025-12-18/?utm_source=chatgpt.com "Shares in South Korea's LGES drop more than 7% after Ford cancels EV battery deal"
[2]: https://www.reuters.com/markets/deals/samsung-sdi-signs-deal-with-gm-its-joint-ev-battery-factory-us-2024-08-27/?utm_source=chatgpt.com "Samsung SDI finalizes deal with GM to build $3.5 bln joint EV battery factory in US"
[3]: https://www.reuters.com/markets/deals/sk-innovation-shareholders-approve-merger-plan-with-sk-es-yonhap-reports-2024-08-27/?utm_source=chatgpt.com "SK Innovation shareholders approve merger seen shoring up loss-making battery unit"
[4]: https://www.marketwatch.com/story/while-ford-shares-are-remarkably-steady-after-20-billion-charge-these-stocks-are-getting-battered-bbbcfa04?utm_source=chatgpt.com "While Ford shares are remarkably steady after $20 billion charge, these stocks are getting battered"
[5]: https://www.reuters.com/business/energy/us-offers-15-bln-conditional-loan-guarantee-qcells-solar-facility-georgia-2024-08-08/?utm_source=chatgpt.com "US offers $1.5 bln conditional loan guarantee to Qcells for solar facility in Georgia"
[6]: https://www.reuters.com/world/asia-pacific/hyundai-motor-breaks-ground-680-million-hydrogen-fuel-cell-plant-south-korea-2025-10-30/?utm_source=chatgpt.com "Hyundai Motor breaks ground on $680 million hydrogen fuel cell plant in South Korea"
[7]: https://www.reuters.com/business/finance/porsche-backed-group14-closes-new-funding-takes-control-jvs-battery-material-2025-08-20/?utm_source=chatgpt.com "Porsche-backed Group14 closes new funding, takes control of JV's battery material plant"
[8]: https://www.reuters.com/business/energy/south-koreas-sk-signs-energy-storage-battery-supply-deal-with-flatiron-energy-2025-09-03/?utm_source=chatgpt.com "South Korea's SK On signs energy storage battery supply deal with Flatiron Energy"
