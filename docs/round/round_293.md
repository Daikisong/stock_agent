순서상 이번은 **R11 Loop 14 — 정책·지정학·재난·이벤트 가격경로 검증 라운드**다.

```text
round = R11 Loop 14
round_id = round_221
large_sector = POLICY_GEOPOLITICS_DISASTER_EVENT
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true_for_political_liquidity_and_disaster_references
next_round = R12 Loop 14
```

이번 R11은 정책·지정학·재난·이벤트 자체가 아니라, **정책 headline이 실제 가격·손익·현금흐름·공급망·신뢰로 닫혔는지**를 검증하는 라운드다. 앞 라운드의 섹터 case를 반복하지 않고, R11 전용으로 **동해 가스전 이벤트, 한화오션 중국 제재, 계엄/정치 리스크, 주식세제·AI windfall tax, 공매도/시장접근성 개혁, 의대증원·의료파업, 대형 산불, 방산 지정학 order**를 뽑았다.

수정주가 일봉 OHLC 전체 window는 이번 환경에서도 안정적으로 확보하지 못했다. `finance` tool은 KRX ticker를 지원하지 않았고, 공개 검색으로 KRX/Naver/Yahoo/Stooq의 조정 OHLC 30D/90D/180D window를 일괄 추출할 수 없었다. 그래서 30D/90D/180D/1Y/2Y MFE·MAE는 임의 생성하지 않고, Reuters / WSJ / FT / MarketWatch / AP가 보도한 **event return, event price, policy amount, liquidity facility, deal value, casualty/disaster data, index reaction**을 가격 anchor로 사용했다.

---

# 1. 이번 라운드 대섹터

```text
R11 = 정책·지정학·재난·이벤트
```

R11에서 진짜 Stage 3는 “정부 발표”, “대통령 발언”, “전쟁”, “제재”, “재난”, “정책 수혜”, “테마 급등”이 아니다. 진짜 Stage 3는 아래가 숫자로 닫힐 때다.

```text
정책:
발표 → 시행령/입법 → 예산/세제 → 기업 손익 반영 → 가격경로 확인

지정학:
긴장 고조 → 실제 제재/통관/항로/조달 차질 → 비용/매출 영향 → 대응 가능성

재난:
사고/재난 → 피해 규모 → 보상/복구비/영업중단 → 신뢰 훼손 → 재무 영향

시장제도:
제도개편 → 외국인 접근성 → 유동성/거래대금 → 증권·거래소·금융사 수익 → 지속성

선거/정치:
공약 → 실제 법안/예산 → 수혜·피해 업종 분리 → 시장 신뢰
```

---

# 2. 대상 canonical archetype

```text
RESOURCE_DISCOVERY_POLICY_EVENT_PREMIUM
GEOPOLITICAL_SANCTIONS_SUPPLY_CHAIN_4C
POLITICAL_LIQUIDITY_SHOCK_HARD_REFERENCE
TAX_POLICY_MARKET_CONFIDENCE_4C
MARKET_ACCESS_REFORM_STAGE2
MEDICAL_REFORM_SERVICE_DISRUPTION_4C_REFERENCE
NATURAL_DISASTER_RECOVERY_POLICY_REFERENCE
GEOPOLITICAL_DEFENSE_ORDER_STAGE2
LABOR_POLICY_SYSTEMIC_EXPORT_RISK_4C
```

---

# 3. deep sub-archetype

```text
정책 resource discovery:
- Korea Gas / SK Innovation / Daesung Energy / SK Gas
- 동해 가스전 / Blue Whale
- 대통령 발표, 14B barrels, success probability 20%
- event premium vs economic viability

중국 제재:
- Hanwha Ocean / HD Hyundai Heavy
- U.S.-linked subsidiaries sanctions
- China port-fee / U.S.-China maritime conflict
- shipbuilding geopolitics vs order backlog

정치/계엄 shock:
- KOSPI / won / 금융지주 / 소비·관광 / 방산·원전
- unlimited liquidity, 10T stock stabilization fund, 40T bond stabilization fund
- political legitimacy and foreign-capital confidence

세제 / AI windfall tax:
- KOSPI / securities / Samsung / SK Hynix / AI basket
- capital-gains threshold, transaction tax, corporate/dividend tax
- AI national dividend / windfall tax comment
- policy credibility vs market rerating

시장접근성:
- short-selling ban removal
- MSCI accessibility review
- unfair trading one-strike-out policy
- developed-market upgrade hope vs actual foreign access

의료개혁:
- 의대정원 확대, 전공의 walkout
- hospital operation disruption, military/public doctors deployment
- policy objective good, service disruption hard gate

자연재난:
- 2025 wildfires
- disaster zone, deaths/evacuations, recovery spending
- insurer/construction/materials read-through only after claims/rebuild orders

방산 지정학:
- Hanwha Aerospace / Romania K9
- Russia-Ukraine-driven rearmament
- order backlog expansion
- order headline vs delivery/margin/dilution

노동정책:
- Samsung strike risk
- emergency arbitration possible
- 1-day halt loss up to 1T won, extended damage up to 100T won
- systemic export risk vs single-company labor dispute
```

---

# 4. 국장 신규 후보 case

## Case A — Korea Gas / 동해 가스전 `event premium + price_moved_without_evidence`

```text
symbols = 036460 / 096770 / 117580 / 018670
company_scope = Korea Gas / SK Innovation / Daesung Energy / SK Gas
case_type = price_moved_without_evidence
archetype = RESOURCE_DISCOVERY_POLICY_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2024-06-03
- 대통령이 동해 심해 가스·석유 탐사 시추를 승인.
- 최대 14B barrels oil/gas 가능성 발표.
- 국가 에너지 안보·자원개발 테마 급등.

Stage 2:
2024-06-03
- Korea Gas +30%, 17-month high.
- Daesung Energy +30%, daily limit.
- SK Innovation +6%.
- SK Gas +7%.
- project estimated cost >500B won.
- per-well drilling cost about 100B won.
- success probability about 20%.
- commercial production target 2035.
- Reuters explicitly notes that only drilling can reveal how much oil/gas is actually present.

Stage 4B:
2024-06-03
- price moved before reserve confirmation, economic feasibility, drilling result, CAPEX/IRR.

Stage 3:
없음
- resource discovery headline is not Green.
```

이 case는 R11 정책 이벤트의 정석이다. 대통령 발표와 “최대 14B barrels” 숫자만으로 Korea Gas는 +30%, Daesung Energy도 +30% 상한가였지만, Reuters는 success probability가 약 20%이고, 실제 매장량은 시추해야만 알 수 있다고 보도했다. 즉 R11에서 **정책 발표 + 숫자 큰 자원 테마**는 Stage 2/4B까지만 가능하다. 경제성, drilling result, CAPEX, 생산권, 판매계약이 닫히기 전에는 Stage 3가 아니다. ([Reuters][1])

### 실제 가격경로 검증

```json
{
  "case_id": "r11_loop14_kogas_blue_whale_resource_event_premium",
  "symbols": "036460/096770/117580/018670",
  "stage2_date": "2024-06-03",
  "stage4b_date": "2024-06-03",
  "stage3_price": null,
  "price_data_source": "Reuters / WSJ resource-discovery event anchors",
  "korea_gas_event_mfe_pct": 30,
  "korea_gas_event_price_krw": 38700,
  "daesung_energy_event_mfe_pct": 30,
  "sk_innovation_event_mfe_pct": 6,
  "sk_gas_event_mfe_pct": 7,
  "kospi_same_context_pct": 1.9,
  "potential_resource_boe_bn": 14,
  "project_cost_krw_bn_min": 500,
  "per_well_cost_krw_bn": 100,
  "success_probability_pct": 20,
  "commercial_production_target": 2035,
  "economic_viability_confirmed": false,
  "drilling_result_confirmed": false,
  "stage3_mfe_mae": "N/A_no_valid_stage3",
  "mfe_30d_90d_180d_1y_2y": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = price_moved_without_evidence
rerating_result = RESOURCE_DISCOVERY_POLICY_EVENT_PREMIUM
stage_failure_type = policy_resource_headline_without_drilling_IRR
```

---

## Case B — Hanwha Ocean / 중국 제재 `geopolitical 4C-watch`

```text
symbol = 042660
case_type = thesis_break_watch
archetype = GEOPOLITICAL_SANCTIONS_SUPPLY_CHAIN_4C
```

### stage date

```text
Stage 1:
2025-10-14
- China sanctions five U.S.-linked Hanwha Ocean subsidiaries.
- background: U.S.-China shipbuilding/port-fee conflict and U.S. efforts to rebuild shipbuilding.

Stage 4C-watch:
2025-10-14
- China bans Chinese organizations and individuals from transactions/cooperation with sanctioned Hanwha units.
- Hanwha Ocean -5.8%.
- HD Hyundai Heavy -4.1%.
- sanctions target U.S. affiliates including Philly Shipyard-related entities.
- Hanwha had pledged $5B in 2025 to expand Philly Shipyard.
- U.S. State Department later called the sanctions an attempt to coerce South Korea and undermine U.S.-ROK cooperation.

Stage 2 relief / policy response:
2025-10-22
- Korean trade envoy asks China to remove sanctions and discusses rare-earth curbs.
```

Hanwha Ocean은 R11 geopolitics에서 가장 좋은 국장 case다. 중국 제재는 “방산·조선 수주 좋다”를 바로 꺾는 이벤트다. Reuters는 Hanwha Ocean이 -5.8%, HD Hyundai Heavy가 -4.1% 하락했다고 보도했고, 제재는 중국 기업·개인이 해당 Hanwha units와 거래/협력하는 것을 금지했다. 이 case는 **U.S.-ROK shipbuilding cooperation이 수혜이면서 동시에 중국 sanction risk를 만든다**는 row다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "case_id": "r11_loop14_hanwha_ocean_china_sanctions_4c_watch",
  "symbol": "042660",
  "stage4c_watch_date": "2025-10-14",
  "stage2_relief_date": "2025-10-22",
  "stage3_price": null,
  "price_data_source": "Reuters / AP China sanctions anchors",
  "hanwha_ocean_event_mae_pct": -5.8,
  "hd_hyundai_heavy_event_mae_pct": -4.1,
  "sanctioned_units_count": 5,
  "sanction_scope": "Chinese organizations and individuals prohibited from transactions/cooperation with sanctioned units",
  "philly_shipyard_investment_pledge_usd_bn": 5,
  "us_rok_shipbuilding_cooperation_context": true,
  "korea_trade_envoy_requested_removal": true,
  "stage3_mfe_mae": "N/A_no_valid_stage3",
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = GEOPOLITICAL_SANCTIONS_SUPPLY_CHAIN_4C
stage_failure_type = geopolitical_sanction_overrides_order_theme
```

---

## Case C — 2024 계엄·정치 리스크 `political liquidity hard reference`

```text
symbols = KOSPI / EWY / financial-market basket
case_type = hard_4C_reference
archetype = POLITICAL_LIQUIDITY_SHOCK_HARD_REFERENCE
```

### stage date

```text
Stage 1:
2024-12-03 night
- President Yoon declares martial law.
- National Assembly votes to lift it; government later rescinds.

Stage 4C-reference:
2024-12-04
- Reuters: won plunges after declaration; authorities pledge unlimited liquidity.
- finance ministry and BOK hold emergency meetings.
- regulator ready to deploy up to 10T won stock-market stabilization fund.
- FT: 10T won stock fund and 40T won bond stabilization fund can be activated.
- KOSPI closed -1.4% in FT source; Reuters global market wrap says KOSPI fell nearly 2%.
- won near two-year low.
- MSCI Korea ETF / Korea ETFs also hit in overseas trading.

Stage 3:
N/A
- political liquidity shock is not investable Green; it is a cross-sector hard gate.
```

계엄 shock는 R11에서 가장 중요한 hard reference다. 어떤 섹터든 정치·헌정 리스크가 터지면 valuation보다 먼저 유동성·환율·외국인 신뢰가 흔들린다. Reuters는 정부가 “unlimited liquidity”를 약속했고, 금융당국이 10T won stock stabilization fund를 준비했다고 보도했다. FT는 10T won 주식시장 안정기금과 40T won 채권시장 안정기금을 언급했고, KOSPI가 -1.4%로 마감했다고 보도했다. ([Reuters][3])

### 실제 가격경로 검증

```json
{
  "case_id": "r11_loop14_martial_law_political_liquidity_shock",
  "symbols": "KOSPI/EWY/market_basket",
  "stage4c_date": "2024-12-04_reference",
  "stage3_price": null,
  "price_data_source": "Reuters / FT martial-law market-stabilization anchors",
  "kospi_close_mae_pct_ft": -1.4,
  "kospi_intraday_or_session_context_reuters_pct": "nearly_-2",
  "stock_stabilization_fund_krw_trn": 10,
  "bond_market_stabilization_fund_krw_trn": 40,
  "liquidity_commitment": "unlimited_liquidity",
  "won_context": "near_two_year_low",
  "political_risk_channel": ["FX", "foreign capital confidence", "credit spread", "consumption", "policy execution"],
  "company_level_stage3_mfe_mae": "N/A_macro_hard_reference"
}
```

### alignment

```text
score_price_alignment = thesis_break_reference
rerating_result = POLITICAL_LIQUIDITY_SHOCK_HARD_REFERENCE
stage_failure_type = political_legitimacy_and_liquidity_risk
```

---

## Case D — 주식 세제 / AI windfall tax `tax policy market-confidence 4C`

```text
symbols = KOSPI / 005930 / 000660 / securities basket
case_type = 4C-watch + relief
archetype = TAX_POLICY_MARKET_CONFIDENCE_4C
```

### stage date

```text
Stage 1:
2025-08-01
- new tax proposals hit Korean equity-market confidence.
- proposals include lowering capital-gains tax threshold, raising corporate/dividend taxes, and raising transaction tax.

Stage 4C-watch:
2025-08-01
- KOSPI -3.9%, steepest decline since April in MarketWatch source.
- proposal conflicts with KOSPI 5000 / Korea Discount reform narrative.

Stage 2 relief:
2025-09-11
- President Lee says he will not pursue lowering the capital-gains tax threshold from 5B won to 1B won.
- Reuters: plan had caused backlash and risked damaging the stock market.
- transaction tax hike to 0.2% from 0.15% remains in broader package.

Stage 4C-watch recurrence:
2026-05-12
- AI windfall-tax / national dividend comment spooks market.
- KOSPI falls 5% intraday before closing -2.3%.
- presidential office later says it was a personal view.
```

이 case는 R11 policy의 핵심이다. 같은 정부가 “KOSPI 5000”과 shareholder reform을 밀어도, 세제 불확실성이 들어오면 market confidence가 즉시 깨진다. 2025년 8월 세제 proposal에는 KOSPI -3.9%가 나왔고, 2025년 9월 대통령이 threshold 인하를 밀지 않겠다고 하자 relief가 왔다. 2026년에는 AI windfall tax성 발언만으로 KOSPI가 장중 -5%, 종가 -2.3%였다. ([마켓워치][4])

### 실제 가격경로 검증

```json
{
  "case_id": "r11_loop14_tax_policy_market_confidence_4c",
  "symbols": "KOSPI/005930/000660/securities_basket",
  "stage4c_watch_date": "2025-08-01/2026-05-12",
  "stage2_relief_date": "2025-09-11",
  "stage3_price": null,
  "price_data_source": "MarketWatch / Reuters / Barron's tax-policy anchors",
  "kospi_tax_proposal_mae_pct": -3.9,
  "capital_gains_threshold_before_krw_bn": 5,
  "capital_gains_threshold_proposed_krw_bn": 1,
  "transaction_tax_before_pct": 0.15,
  "transaction_tax_proposed_pct": 0.20,
  "ai_tax_intraday_mae_pct": -5.0,
  "ai_tax_close_mae_pct": -2.3,
  "ai_tax_comment_later_clarified_as_personal_view": true,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break_watch_then_policy_relief
rerating_result = TAX_POLICY_MARKET_CONFIDENCE_4C
stage_failure_type = reform_narrative_breaks_if_tax_policy_hits_equity_returns
```

---

## Case E — 공매도 재개·불공정거래 단속 `market-access reform Stage 2`

```text
symbols = securities_basket / KRX_market_reference
case_type = success_candidate_policy_stage2
archetype = MARKET_ACCESS_REFORM_STAGE2
```

### stage date

```text
Stage 1:
2025-03
- Korea lifts market-wide short-selling ban for first time in five years after building detection systems.

Stage 2:
2025-06-20
- MSCI says short-selling accessibility improved from “improvements needed” to “no major issues, improvements possible”.
- Korea still has other hurdles: foreign-exchange market access, lack of offshore market, onshore limitations.
- developed-market upgrade remains uncertain.

Stage 2 추가:
2025-07-09
- FSC/FSS/KRX announce unfair-trading measures.
- serious short-sale violations can face fines equal to 100% of short-sale orders.
- business suspension and trading restrictions possible.
- one-strike-out policy after President Lee’s directive.

Stage 3:
없음
- market access reform is Stage 2.
- Green requires foreign flow, trading value, securities-firm earnings, index upgrade trajectory.
```

공매도/불공정거래 reform은 R11 market-structure Stage 2다. MSCI는 short-selling accessibility가 개선됐다고 평가했지만, 동시에 FX market access와 offshore market 부재 같은 문제가 남아 있다고 봤다. 또 FSC는 불법 공매도에 최고 수준의 과징금과 영업정지·거래제한을 예고했다. 다만 증권주/시장 제도 Green은 실제 외국인 flow, 거래대금, 수수료 수익, MSCI upgrade path로 확인해야 한다. ([Reuters][5])

### 실제 가격경로 검증

```json
{
  "case_id": "r11_loop14_short_selling_market_access_reform_stage2",
  "symbols": "securities_basket/KRX_market_reference",
  "stage1_date": "2025-03",
  "stage2_date": "2025-06-20/2025-07-09",
  "stage3_price": null,
  "price_data_source": "Reuters MSCI accessibility and unfair-trading reform anchors",
  "short_selling_ban_lifted_after_years": 5,
  "msci_short_selling_accessibility_rating_change": "improvements_needed_to_no_major_issues_improvements_possible",
  "serious_short_sale_violation_fine_pct_of_order": 100,
  "possible_penalties": ["business_suspension", "trading_restrictions"],
  "remaining_hurdles": ["FX market access", "lack of offshore market", "onshore limitations"],
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_conditions": ["foreign inflow", "trading value", "brokerage earnings", "MSCI watchlist/upgrade progress"]
}
```

### alignment

```text
score_price_alignment = success_candidate_policy_stage2
rerating_result = MARKET_ACCESS_REFORM_STAGE2
stage_failure_type = accessibility_reform_not_foreign_flow_brokerage_profit_green
```

---

## Case F — 의대증원·전공의 파업 `medical reform service-disruption reference`

```text
symbols = healthcare_service_basket / telemedicine_readthrough
case_type = 4C-reference
archetype = MEDICAL_REFORM_SERVICE_DISRUPTION_4C_REFERENCE
```

### stage date

```text
Stage 1:
2024-02-20
- trainee doctors begin walkout against medical-school quota expansion.
- policy aim: address doctor shortage and aging-population healthcare demand.

Stage 4C-reference:
2024-02-28
- about 9,000 trainee doctors participate.
- hospitals face surgery cancellations and service disruption.
- government sends military and community doctors to hospitals.
- authorities warn of licence suspensions.
- later reports mention about 12,000 doctors from 100 teaching hospitals and possible suspension notices to thousands.

Stage 3:
N/A
- medical reform policy is socially important, but investable Green requires service capacity, reimbursement, hospital earnings, and implementation stability.
```

의대증원 case는 R11에서 “정책 목적이 옳아도 실행 충격이 있으면 4C reference”라는 기준이다. Reuters는 약 9,000명의 전공의가 walkout에 참여했고, 병원 수술 취소와 서비스 차질이 발생해 정부가 군의관·공보의를 투입한다고 보도했다. 정책 beneficiary를 찾더라도, 의료서비스 disruption과 규제/여론 리스크가 먼저다. ([Reuters][6])

### 실제 가격경로 검증

```json
{
  "case_id": "r11_loop14_medical_reform_doctors_strike_service_disruption",
  "symbols": "healthcare_service_basket/telemedicine_readthrough",
  "stage4c_watch_date": "2024-02-28",
  "stage3_price": null,
  "price_data_source": "Reuters / Guardian doctors strike anchors",
  "trainee_doctors_walkout_count_reuters": 9000,
  "reported_doctors_in_teaching_hospitals_context": 12000,
  "teaching_hospitals_context_count": 100,
  "service_disruptions": ["surgery_cancellations", "hospital_service_delay"],
  "government_response": ["military_doctors", "community_doctors", "license_suspension_warning"],
  "direct_listed_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_conditions": ["service capacity recovery", "reimbursement economics", "hospital earnings", "implementation stability"]
}
```

### alignment

```text
score_price_alignment = thesis_break_reference
rerating_result = MEDICAL_REFORM_SERVICE_DISRUPTION_4C_REFERENCE
stage_failure_type = policy_goal_not_green_if_service_capacity_breaks
```

---

## Case G — 2025 South Korea wildfires `natural-disaster recovery reference`

```text
symbols = insurers / construction / building-materials / ESG-disaster-response basket
case_type = disaster_4C_reference
archetype = NATURAL_DISASTER_RECOVERY_POLICY_REFERENCE
```

### stage date

```text
Stage 1:
2025-03-21
- large wildfires break out across central and southern South Korea.

Stage 4C-reference:
2025-03-22~2025-03-28
- Reuters: death toll rises to at least 16 during active phase; thousands evacuated; more than 15,000 hectares destroyed at that point.
- AP: later containment report says 28 deaths, 37 injuries, 118,265 acres burned, over 30,000 displaced.
- government designates disaster zones.
- worst wildfire event / record-scale disaster language appears in major media.

Stage 3:
N/A
- disaster recovery read-through to construction/materials/insurers requires actual claims, reconstruction orders, government budget and margin.
```

산불 case는 R11 자연재난 reference다. 재난은 “복구 수혜” headline보다 먼저 피해·보상·보험·복구예산·자재수급을 봐야 한다. AP는 28명 사망, 37명 부상, 118,265 acres 소실, 30,000명 이상 이재민을 보도했고, Reuters는 재난구역 지정과 대규모 피해를 보도했다. 이런 사건은 건설·건자재·보험에 무조건 Green이 아니라, claims와 actual reconstruction orders가 확인되어야 한다. ([Reuters][7])

### 실제 가격경로 검증

```json
{
  "case_id": "r11_loop14_2025_wildfire_disaster_recovery_reference",
  "symbols": "insurers/construction/materials_basket",
  "stage4c_watch_date": "2025-03-22_to_2025-03-28",
  "stage3_price": null,
  "price_data_source": "Reuters / AP wildfire-disaster anchors",
  "reuters_active_phase_deaths": 16,
  "ap_later_deaths": 28,
  "ap_injuries": 37,
  "ap_acres_burned": 118265,
  "ap_displaced_people": 30000,
  "reuters_hectares_destroyed_active_phase_min": 15000,
  "disaster_zone_designation": true,
  "direct_listed_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_conditions": ["insurance claims", "government recovery budget", "reconstruction orders", "material margin", "contract awards"]
}
```

### alignment

```text
score_price_alignment = disaster_reference
rerating_result = NATURAL_DISASTER_RECOVERY_POLICY_REFERENCE
stage_failure_type = disaster_damage_not_reconstruction_margin_green
```

---

## Case H — Hanwha Aerospace / Romania K9 order `geopolitical defense order Stage 2`

```text
symbol = 012450
case_type = structural_success_candidate + 4B/dilution watch
archetype = GEOPOLITICAL_DEFENSE_ORDER_STAGE2
```

### stage date

```text
Stage 1:
2022~2024
- Russia-Ukraine war drives European rearmament.
- South Korean defense exporters gain order pipeline.

Stage 2:
2024-07-09
- Hanwha Aerospace wins $1B Romania order.
- 54 K9 self-propelled howitzers, ammunition, and 36 K10 resupply vehicles.
- Romania’s largest arms acquisition in seven years.
- contract runs until July 2029.
- Hanwha defense backlog rises from 5.1T won at end-2021 to around 30T won by March 2024.
- shares rise more than 5% to record high in early trading.

Stage 4B-watch:
2025-03
- later 3.6T won share sale / dilution shock from prior R1 reference shows order backlog alone is not Green.
```

Hanwha Aerospace는 R11 지정학 defense-order success_candidate다. Reuters는 Romania $1B K9 order와 주가 +5% record-high reaction을 보도했다. 하지만 이 case는 R1의 Hanwha dilution 반례와 연결해야 한다. 방산 order는 Stage 2로 강하지만, Stage 3는 delivery, margin, cash collection, local-production, dilution-adjusted EPS가 닫혀야 한다. ([Reuters][8])

### 실제 가격경로 검증

```json
{
  "case_id": "r11_loop14_hanwha_aerospace_romania_k9_geopolitical_order",
  "symbol": "012450",
  "stage2_date": "2024-07-09",
  "stage4b_watch_date": "2025-03_dilution_reference",
  "stage3_price": null,
  "price_data_source": "Reuters Romania K9 order and later dilution-watch anchors",
  "order_value_usd_bn": 1.0,
  "k9_howitzers": 54,
  "k10_resupply_vehicles": 36,
  "contract_end": "2029-07",
  "backlog_end_2021_krw_trn": 5.1,
  "backlog_march_2024_krw_trn": 30,
  "backlog_growth_multiple": 5.88,
  "event_mfe_pct": 5.0,
  "later_share_sale_krw_trn": 3.6,
  "later_dilution_event_mae_pct": -13,
  "stage3_conditions": ["delivery", "margin", "cash collection", "local production", "dilution-adjusted EPS"],
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_but_4B_watch
rerating_result = GEOPOLITICAL_DEFENSE_ORDER_STAGE2
stage_failure_type = order_backlog_not_delivery_margin_dilution_adjusted_green
```

---

## Case I — Samsung strike risk / 정부 중재 `labor-policy systemic export 4C-watch`

```text
symbols = 005930 / 000660 / KOSPI_export_chain
case_type = 4C-watch
archetype = LABOR_POLICY_SYSTEMIC_EXPORT_RISK_4C
```

### stage date

```text
Stage 1:
2026-05-17
- Samsung union threatens 18-day strike.
- semiconductor supply and export-chain continuity become national policy issue.

Stage 4C-watch:
2026-05-17
- Korean government says it will pursue all options to avoid strike.
- rarely used emergency arbitration could bar industrial action for 30 days.
- Prime Minister estimates a single day halt at Samsung semiconductor facilities could cause direct losses up to 1T won.
- prolonged disruption could cause economic damage as high as 100T won.
- Samsung accounts for 22.8% of Korea exports and employs over 120,000 workers.

Stage 3:
N/A
- labor resolution is not Green unless production continuity, yield, delivery schedule and customer allocation remain intact.
```

삼성 strike risk는 R11 labor-policy hard watch다. Reuters는 정부가 emergency arbitration까지 검토한다고 보도했고, 하루 생산 중단 손실이 최대 1T won, 장기 disruption 피해가 100T won까지 가능하다는 정부 추산을 전했다. 이건 단순 노사 이슈가 아니라 국가 수출·AI 반도체 supply chain issue다. ([Reuters][9])

### 실제 가격경로 검증

```json
{
  "case_id": "r11_loop14_samsung_strike_labor_policy_systemic_export_risk",
  "symbols": "005930/000660/KOSPI_export_chain",
  "stage4c_watch_date": "2026-05-17",
  "stage3_price": null,
  "price_data_source": "Reuters Samsung strike / government emergency arbitration anchor",
  "strike_threat_days": 18,
  "emergency_arbitration_possible": true,
  "industrial_action_bar_period_days": 30,
  "single_day_halt_loss_krw_trn_max": 1,
  "prolonged_disruption_damage_krw_trn_max": 100,
  "samsung_export_share_pct": 22.8,
  "samsung_employee_count": 120000,
  "direct_event_return": "price_data_unavailable_after_deep_search",
  "stage3_conditions": ["production continuity", "yield", "delivery schedule", "customer allocation", "labor settlement durability"]
}
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = LABOR_POLICY_SYSTEMIC_EXPORT_RISK_4C
stage_failure_type = labor_supply_continuity_is_semiconductor_export_gate
```

---

# 5. 이번 R11 case별 stage date 요약

| case                          | Stage 1           | Stage 2                    | Stage 3 | Stage 4B                    | Stage 4C                           |
| ----------------------------- | ----------------- | -------------------------- | ------- | --------------------------- | ---------------------------------- |
| Korea Gas / Blue Whale        | 2024-06-03        | 대통령 시추 승인                  | N/A     | +30% resource event         | economic viability unconfirmed     |
| Hanwha Ocean sanctions        | 2025-10-14        | 2025-10-22 policy response | N/A     | U.S.-ROK shipbuilding theme | China sanctions                    |
| Martial law shock             | 2024-12-03        | liquidity response         | N/A     | N/A                         | political liquidity hard reference |
| Tax policy / AI tax           | 2025-08 / 2026-05 | 2025-09 relief             | N/A     | reform-policy rally risk    | tax-confidence shock               |
| Short-selling / market access | 2025-03           | 2025-06/07 reform          | N/A     | developed-market hope       | unfair trading / access gap        |
| Medical reform                | 2024-02           | N/A                        | N/A     | N/A                         | service disruption reference       |
| Wildfires                     | 2025-03           | disaster-zone response     | N/A     | recovery theme watch        | disaster reference                 |
| Hanwha Aerospace K9           | 2024-07           | Romania order              | N/A     | order backlog premium       | dilution/delivery watch            |
| Samsung strike                | 2026-05           | government mediation       | N/A     | AI supply-chain spillover   | labor continuity risk              |

---

# 6. 실제 가격경로 검증 총괄

| case                   |                                                 가격·정책 anchor | 해석                                 | 판정                           |
| ---------------------- | -----------------------------------------------------------: | ---------------------------------- | ---------------------------- |
| Korea Gas / Blue Whale |                KOGAS +30%, Daesung +30%, SKI +6%, SK Gas +7% | resource headline 4B               | price_moved_without_evidence |
| Hanwha Ocean sanctions |                             Hanwha Ocean -5.8%, HD HHI -4.1% | geopolitics 4C-watch               | thesis_break_watch           |
| Martial law shock      |        KOSPI -1.4%~nearly -2%, 10T stock fund, 40T bond fund | political liquidity hard reference | thesis_break_reference       |
| Tax policy / AI tax    |                KOSPI -3.9%; AI tax intraday -5%, close -2.3% | policy-confidence 4C               | thesis_break_watch           |
| Short-selling reform   | MSCI accessibility upgrade; 100% fine for serious violations | market access Stage 2              | success_candidate            |
| Medical reform         |    9,000 trainee doctors walkout, military/community doctors | service-disruption reference       | thesis_break_reference       |
| Wildfires              |              28 deaths, 118,265 acres burned, 30k+ displaced | disaster reference                 | disaster_4C_reference        |
| Hanwha Aerospace K9    |                             +5%, $1B order, backlog 5.1T→30T | defense order Stage 2              | success_candidate            |
| Samsung strike         |     1-day halt up to 1T won, prolonged damage up to 100T won | labor-policy export risk           | thesis_break_watch           |

---

# 7. score-price alignment 판정

```text
aligned:
- 없음. R11은 대부분 policy/event Stage 2 또는 4C reference.

structural_success_candidate:
- Hanwha Aerospace Romania K9, if delivery/margin/cash collection confirm.
- Market-access reform, if foreign flow and brokerage earnings confirm.

success_candidate:
- Hanwha Aerospace order.
- Short-selling / market-access reform.
- Blue Whale only as resource option, not Stage 3.

failed_rerating:
- 세제 proposal / AI tax shock when reform narrative is contradicted.
- Resource theme if drilling/economic feasibility fails.
- Hanwha Ocean if China sanctions impair project execution.

overheat / 4B:
- Korea Gas / Daesung Energy resource-event +30%.
- Hanwha Aerospace order premium if treated as EPS before delivery.
- KOSPI AI rally vulnerable to AI windfall-tax comment.

price_moved_without_evidence:
- Blue Whale gas/oil resource rally.
- Disaster recovery trades before actual claims/rebuild orders.
- Defense order headline before delivery/margin.

evidence_good_but_price_failed:
- Tax reform credibility: good Value-Up policy can fail if tax package undermines investor returns.
- Short-selling reform can still fail if FX/offshore-market access remains unresolved.

thesis_break:
- Martial-law political liquidity shock as cross-sector hard reference.
- Hanwha Ocean China sanctions as geopolitical 4C-watch.
- Medical reform service-disruption reference.
- Wildfire disaster reference.
- Samsung strike/labor continuity risk.
```

---

# 8. 점수비중 교정

## 올릴 축

```text
policy_implementation_certainty +5
legal_regulatory_finality +5
geopolitical_counterparty_risk +5
sanction_export_control_exposure +5
political_liquidity_risk +5
tax_policy_consistency +5
market_access_foreign_flow +4
service_continuity_under_policy +4
disaster_damage_to_cashflow +4
labor_continuity_systemic_risk +5
```

### 왜 올리나

Blue Whale은 resource headline만으로 +30%를 만들었지만, success probability와 drilling economics가 없었다. Hanwha Ocean은 U.S. cooperation이 오히려 중국 제재 리스크가 되는 구조를 보여줬다. Martial law shock은 유동성·환율·외국인 신뢰를 한 번에 건드렸다. 세제 proposal과 AI windfall tax 발언은 주가가 정책 신뢰를 얼마나 민감하게 가격화하는지 보여준다. Samsung strike risk는 노사 이슈가 아니라 수출 시스템 리스크다.

## 내릴 축

```text
government_announcement_only -5
presidential_headline_only -5
resource_estimate_without_drilling -5
policy_beneficiary_theme_only -5
sanction_ignored_order_backlog -5
tax_reform_without_market_consistency -5
market_access_reform_without_foreign_flow -4
disaster_recovery_without_budget_contract -4
defense_order_without_delivery_margin -4
```

---

# 9. Green gate 강화 조건

```text
R11 Stage 3-Green 필수:
1. 정책은 발표가 아니라 법안/시행령/예산/집행 확인.
2. 자원개발은 drilling result, economic viability, CAPEX/IRR 확인.
3. 지정학 event는 sanction/export-control/항로/통관의 실제 매출·비용 영향 확인.
4. 세제정책은 investor-return consistency 확인.
5. 시장제도는 foreign flow, 거래대금, broker earnings, MSCI upgrade path 확인.
6. 재난 복구는 claims, government budget, reconstruction contracts 확인.
7. 의료·노동 정책은 service/production continuity 확인.
8. 방산 order는 delivery, margin, cash collection, dilution-adjusted EPS 확인.
9. price path가 evidence 이후 따라옴.
```

---

# 10. 4B 조기감지 조건

```text
4B-watch:
- 대통령 resource 발표로 +20~30% 급등.
- 방산 order headline로 record high.
- 세제 완화/철회 기대만으로 broad rally.
- 시장제도/공매도 reform headline로 증권주 선반영.
- 재난 복구 theme가 actual contract 전 급등.
- 정책 beneficiary basket이 실제 예산/법안 전 rerating.
```

---

# 11. 4C hard gate 조건

```text
Hard 4C:
- martial law / constitutional crisis / political liquidity shock.
- foreign sanctions that block transactions/cooperation.
- tax policy that directly damages investor-return expectation.
- resource exploration failure after speculative rally.
- nationwide medical/service disruption after policy conflict.
- major natural disaster with claims/recovery uncertainty.
- prolonged strike threat at systemically important exporter.
- export-control or rare-earth/shipbuilding sanctions hitting supply chain.
```

이번 R11 Loop 14의 hard reference는 **martial-law political liquidity shock**, **Hanwha Ocean China sanctions**, **medical-reform service disruption**, **2025 wildfires**, **Samsung strike systemic export risk**다. 직접 기업 hard 4C로는 Hanwha Ocean의 sanctions case가 가장 뚜렷하고, Blue Whale은 `price_moved_without_evidence`, tax-policy는 `market-confidence 4C-watch`, Hanwha Aerospace Romania order는 `success_candidate_4B_watch`로 둔다.

---

# 12. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 13. 레포 반영용 patch-ready 출력

## docs/round/round_221.md 요약

```md
# R11 Loop 14. Policy / Geopolitics / Disaster / Event Price Validation

이번 라운드는 R11 Loop 14 price-validation 라운드다.

핵심 결론:
- Korea Gas / Blue Whale is resource-discovery event premium and price_moved_without_evidence. KOGAS +30%, Daesung Energy +30%, SK Innovation +6%, SK Gas +7% after presidential drilling approval for up to 14B barrels oil/gas prospects. Success probability about 20%, project cost >500B won, per-well cost about 100B won, economic viability unconfirmed.
- Hanwha Ocean China sanctions are geopolitical 4C-watch. China sanctioned five U.S.-linked Hanwha subsidiaries, banning Chinese organizations/individuals from transactions/cooperation. Hanwha Ocean -5.8%, HD Hyundai Heavy -4.1%. Korea later sought removal of the sanctions.
- Martial-law shock is political liquidity hard reference. Korea pledged unlimited liquidity, with up to 10T won stock stabilization fund and 40T won bond stabilization fund available. KOSPI fell -1.4% to nearly -2%, won near two-year low.
- Tax policy is market-confidence 4C-watch. 2025 tax package triggered KOSPI -3.9%; Lee later backed away from lowering capital-gains threshold from 5B won to 1B won. In 2026, an AI windfall-tax/national-dividend comment sent KOSPI down 5% intraday and -2.3% at close.
- Short-selling / unfair-trading reform is market-access Stage 2. Korea lifted short-selling ban after five years; MSCI improved short-selling accessibility assessment; FSC announced fines up to 100% of short-sale orders for serious violations. Foreign flow and brokerage earnings required.
- Medical-school quota / doctors strike is service-disruption reference. About 9,000 trainee doctors walked out; hospitals faced surgery cancellations; government deployed military/community doctors and warned of license suspensions.
- 2025 wildfires are disaster reference. AP later reported 28 deaths, 37 injuries, 118,265 acres burned and more than 30,000 displaced. Recovery trades require claims, budgets and contracts.
- Hanwha Aerospace Romania K9 is geopolitical defense order Stage 2. $1B order for 54 K9 howitzers, ammunition and 36 K10 vehicles; shares +5% to record high; backlog rose from 5.1T won to around 30T won. Delivery/margin/dilution-adjusted EPS required.
- Samsung strike risk is labor-policy systemic export 4C-watch. Government may use emergency arbitration; one-day halt at Samsung semiconductor facilities could cost up to 1T won, prolonged disruption up to 100T won. Samsung accounts for 22.8% of Korea exports.
```

## docs/checkpoints/checkpoint_28a_round221_r11_loop14.md 요약

```md
# Checkpoint 28A Round 221 R11 Loop 14 Policy Geopolitics Disaster Event Price Validation

## 반영 내용
- R11 Loop 14 price-validation 라운드를 추가했다.
- Korea Gas/Blue Whale, Hanwha Ocean China sanctions, martial-law liquidity shock, tax-policy confidence shock, short-selling market-access reform, medical-reform strike, 2025 wildfires, Hanwha Aerospace Romania K9, Samsung strike risk를 비교했다.
- Reuters / WSJ / FT / MarketWatch / AP anchors로 가능한 event MFE/MAE, event price, liquidity package, policy amount, order value, disaster facts, strike-loss estimate를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- policy implementation certainty, legal/regulatory finality, geopolitical counterparty risk, sanction/export-control exposure, political liquidity risk, tax-policy consistency, market-access foreign flow, service continuity under policy, disaster damage-to-cashflow, labor-continuity systemic risk 가중치 강화.
- government announcement-only, presidential headline-only, resource estimate without drilling, policy beneficiary theme-only, sanction ignored order backlog, tax reform without market consistency, market-access reform without foreign flow, disaster recovery without budget/contract 감점 강화.
```

## data/e2r_case_library/cases_r11_loop14_round221.jsonl 초안

```jsonl
{"case_id":"r11_loop14_kogas_blue_whale_resource_event_premium","symbol":"036460/096770/117580/018670","company_name":"Korea Gas / SK Innovation / Daesung Energy / SK Gas","case_type":"price_moved_without_evidence","primary_archetype":"RESOURCE_DISCOVERY_POLICY_EVENT_PREMIUM","stage2_date":"2024-06-03","stage4b_date":"2024-06-03","price_validation":{"price_data_source":"Reuters / WSJ resource-discovery event anchors","stage3_price":null,"korea_gas_event_mfe_pct":30,"korea_gas_event_price_krw":38700,"daesung_energy_event_mfe_pct":30,"sk_innovation_event_mfe_pct":6,"sk_gas_event_mfe_pct":7,"kospi_same_context_pct":1.9,"potential_resource_boe_bn":14,"project_cost_krw_bn_min":500,"per_well_cost_krw_bn":100,"success_probability_pct":20,"commercial_production_target":2035,"economic_viability_confirmed":false,"drilling_result_confirmed":false,"stage3_mfe_mae":"N/A_no_valid_stage3","mfe_30d_90d_180d_1y_2y":"price_data_unavailable_after_deep_search"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"RESOURCE_DISCOVERY_POLICY_EVENT_PREMIUM","notes":"Presidential resource estimate moved stocks before drilling/economic viability."}
{"case_id":"r11_loop14_hanwha_ocean_china_sanctions_4c_watch","symbol":"042660","company_name":"Hanwha Ocean","case_type":"thesis_break_watch","primary_archetype":"GEOPOLITICAL_SANCTIONS_SUPPLY_CHAIN_4C","stage4c_date":"2025-10-14","stage2_date":"2025-10-22_relief_attempt","price_validation":{"price_data_source":"Reuters / AP China sanctions anchors","stage3_price":null,"hanwha_ocean_event_mae_pct":-5.8,"hd_hyundai_heavy_event_mae_pct":-4.1,"sanctioned_units_count":5,"sanction_scope":"Chinese organizations and individuals prohibited from transactions/cooperation with sanctioned units","philly_shipyard_investment_pledge_usd_bn":5,"us_rok_shipbuilding_cooperation_context":true,"korea_trade_envoy_requested_removal":true,"stage3_mfe_mae":"N/A_no_valid_stage3","mae_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"GEOPOLITICAL_SANCTIONS_SUPPLY_CHAIN_4C","notes":"Geopolitical sanctions can override shipbuilding order/backlog narrative."}
{"case_id":"r11_loop14_martial_law_political_liquidity_shock","symbol":"KOSPI/EWY/market_basket","company_name":"South Korea market political-liquidity reference","case_type":"hard_4c_reference","primary_archetype":"POLITICAL_LIQUIDITY_SHOCK_HARD_REFERENCE","stage4c_date":"2024-12-04_reference","price_validation":{"price_data_source":"Reuters / FT martial-law market-stabilization anchors","stage3_price":null,"kospi_close_mae_pct_ft":-1.4,"kospi_session_context_reuters_pct":"nearly_-2","stock_stabilization_fund_krw_trn":10,"bond_market_stabilization_fund_krw_trn":40,"liquidity_commitment":"unlimited_liquidity","won_context":"near_two_year_low","political_risk_channel":["FX","foreign capital confidence","credit spread","consumption","policy execution"],"company_level_stage3_mfe_mae":"N/A_macro_hard_reference"},"score_price_alignment":"thesis_break_reference","rerating_result":"POLITICAL_LIQUIDITY_SHOCK_HARD_REFERENCE","notes":"Constitutional/political shock requires liquidity, FX and foreign-capital confidence hard gate."}
{"case_id":"r11_loop14_tax_policy_market_confidence_4c","symbol":"KOSPI/005930/000660/securities_basket","company_name":"Korea tax-policy market-confidence basket","case_type":"thesis_break_watch_then_policy_relief","primary_archetype":"TAX_POLICY_MARKET_CONFIDENCE_4C","stage4c_date":"2025-08-01/2026-05-12_watch","stage2_date":"2025-09-11_relief","price_validation":{"price_data_source":"MarketWatch / Reuters / Barron's tax-policy anchors","stage3_price":null,"kospi_tax_proposal_mae_pct":-3.9,"capital_gains_threshold_before_krw_bn":5,"capital_gains_threshold_proposed_krw_bn":1,"transaction_tax_before_pct":0.15,"transaction_tax_proposed_pct":0.20,"ai_tax_intraday_mae_pct":-5.0,"ai_tax_close_mae_pct":-2.3,"ai_tax_comment_later_clarified_as_personal_view":true,"mfe_30d_90d":"price_data_unavailable_after_deep_search","mae_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch_then_policy_relief","rerating_result":"TAX_POLICY_MARKET_CONFIDENCE_4C","notes":"Market-reform narrative can break if tax policy damages expected investor returns."}
{"case_id":"r11_loop14_short_selling_market_access_reform_stage2","symbol":"securities_basket/KRX_market_reference","company_name":"Korea short-selling and unfair-trading reform","case_type":"success_candidate_policy_stage2","primary_archetype":"MARKET_ACCESS_REFORM_STAGE2","stage1_date":"2025-03","stage2_date":"2025-06-20/2025-07-09","price_validation":{"price_data_source":"Reuters MSCI accessibility and unfair-trading reform anchors","stage3_price":null,"short_selling_ban_lifted_after_years":5,"msci_short_selling_accessibility_rating_change":"improvements_needed_to_no_major_issues_improvements_possible","serious_short_sale_violation_fine_pct_of_order":100,"possible_penalties":["business_suspension","trading_restrictions"],"remaining_hurdles":["FX market access","lack of offshore market","onshore limitations"],"direct_price_anchor":"price_data_unavailable_after_deep_search","stage3_conditions":["foreign inflow","trading value","brokerage earnings","MSCI watchlist/upgrade progress"]},"score_price_alignment":"success_candidate_policy_stage2","rerating_result":"MARKET_ACCESS_REFORM_STAGE2","notes":"Market-access reform is Stage 2 until foreign flow, trading value and broker earnings confirm."}
{"case_id":"r11_loop14_medical_reform_doctors_strike_service_disruption","symbol":"healthcare_service_basket/telemedicine_readthrough","company_name":"Medical school quota reform / doctors strike reference","case_type":"4c_reference","primary_archetype":"MEDICAL_REFORM_SERVICE_DISRUPTION_4C_REFERENCE","stage4c_date":"2024-02-28_watch","price_validation":{"price_data_source":"Reuters / Guardian doctors strike anchors","stage3_price":null,"trainee_doctors_walkout_count_reuters":9000,"reported_doctors_in_teaching_hospitals_context":12000,"teaching_hospitals_context_count":100,"service_disruptions":["surgery_cancellations","hospital_service_delay"],"government_response":["military_doctors","community_doctors","license_suspension_warning"],"direct_listed_price_anchor":"price_data_unavailable_after_deep_search","stage3_conditions":["service capacity recovery","reimbursement economics","hospital earnings","implementation stability"]},"score_price_alignment":"thesis_break_reference","rerating_result":"MEDICAL_REFORM_SERVICE_DISRUPTION_4C_REFERENCE","notes":"Policy objective is not investable Green if service continuity breaks."}
{"case_id":"r11_loop14_2025_wildfire_disaster_recovery_reference","symbol":"insurers/construction/materials_basket","company_name":"2025 South Korea wildfire disaster reference","case_type":"disaster_4c_reference","primary_archetype":"NATURAL_DISASTER_RECOVERY_POLICY_REFERENCE","stage4c_date":"2025-03-22_to_2025-03-28","price_validation":{"price_data_source":"Reuters / AP wildfire-disaster anchors","stage3_price":null,"reuters_active_phase_deaths":16,"ap_later_deaths":28,"ap_injuries":37,"ap_acres_burned":118265,"ap_displaced_people":30000,"reuters_hectares_destroyed_active_phase_min":15000,"disaster_zone_designation":true,"direct_listed_price_anchor":"price_data_unavailable_after_deep_search","stage3_conditions":["insurance claims","government recovery budget","reconstruction orders","material margin","contract awards"]},"score_price_alignment":"disaster_reference","rerating_result":"NATURAL_DISASTER_RECOVERY_POLICY_REFERENCE","notes":"Disaster recovery theme requires claims, government budget and actual reconstruction/material orders."}
{"case_id":"r11_loop14_hanwha_aerospace_romania_k9_geopolitical_order","symbol":"012450","company_name":"Hanwha Aerospace","case_type":"success_candidate_4b_watch","primary_archetype":"GEOPOLITICAL_DEFENSE_ORDER_STAGE2","stage2_date":"2024-07-09","stage4b_date":"2025-03_dilution_reference","price_validation":{"price_data_source":"Reuters Romania K9 order and later dilution-watch anchors","stage3_price":null,"order_value_usd_bn":1.0,"k9_howitzers":54,"k10_resupply_vehicles":36,"contract_end":"2029-07","backlog_end_2021_krw_trn":5.1,"backlog_march_2024_krw_trn":30,"backlog_growth_multiple":5.88,"event_mfe_pct":5.0,"later_share_sale_krw_trn":3.6,"later_dilution_event_mae_pct":-13,"stage3_conditions":["delivery","margin","cash collection","local production","dilution-adjusted EPS"],"mfe_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_4B_watch","rerating_result":"GEOPOLITICAL_DEFENSE_ORDER_STAGE2","notes":"Defense order backlog is Stage 2 until delivery, margin, cash collection and dilution-adjusted EPS close."}
{"case_id":"r11_loop14_samsung_strike_labor_policy_systemic_export_risk","symbol":"005930/000660/KOSPI_export_chain","company_name":"Samsung Electronics / SK Hynix read-through","case_type":"4c_watch","primary_archetype":"LABOR_POLICY_SYSTEMIC_EXPORT_RISK_4C","stage4c_date":"2026-05-17_watch","price_validation":{"price_data_source":"Reuters Samsung strike / government emergency arbitration anchor","stage3_price":null,"strike_threat_days":18,"emergency_arbitration_possible":true,"industrial_action_bar_period_days":30,"single_day_halt_loss_krw_trn_max":1,"prolonged_disruption_damage_krw_trn_max":100,"samsung_export_share_pct":22.8,"samsung_employee_count":120000,"direct_event_return":"price_data_unavailable_after_deep_search","stage3_conditions":["production continuity","yield","delivery schedule","customer allocation","labor settlement durability"]},"score_price_alignment":"thesis_break_watch","rerating_result":"LABOR_POLICY_SYSTEMIC_EXPORT_RISK_4C","notes":"Labor continuity at systemic exporter is a national supply-chain gate, not just company-level HR issue."}
```

## data/sector_taxonomy/score_weight_profiles_round221_r11_loop14_v1.csv 초안

```csv
archetype,policy_implementation_certainty,legal_regulatory_finality,geopolitical_counterparty_risk,sanction_export_control_exposure,political_liquidity_risk,tax_policy_consistency,market_access_foreign_flow,service_continuity_under_policy,disaster_damage_to_cashflow,labor_continuity_systemic_risk,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
RESOURCE_DISCOVERY_POLICY_EVENT_PREMIUM,+5,+3,+2,+1,+2,+1,+0,+0,+1,+0,-5,+5,+4,Blue Whale shows presidential resource estimate needs drilling, economics and IRR.
GEOPOLITICAL_SANCTIONS_SUPPLY_CHAIN_4C,+4,+5,+5,+5,+3,+1,+1,+1,+2,+1,0,+5,+5,Hanwha Ocean China sanctions show order themes can be cut by counterparty sanctions.
POLITICAL_LIQUIDITY_SHOCK_HARD_REFERENCE,+5,+5,+4,+2,+5,+5,+4,+3,+3,+3,0,+4,+5,Martial law shock confirms political legitimacy/liquidity as cross-sector hard gate.
TAX_POLICY_MARKET_CONFIDENCE_4C,+5,+5,+1,+1,+4,+5,+4,+1,+1,+1,0,+5,+5,Tax-policy inconsistency can break market reform and Value-Up rerating.
MARKET_ACCESS_REFORM_STAGE2,+5,+5,+1,+1,+2,+3,+5,+1,+1,+1,-5,+4,+3,Short-selling/MSCI reforms need foreign flow, trading value and broker earnings.
MEDICAL_REFORM_SERVICE_DISRUPTION_4C_REFERENCE,+4,+5,+1,+1,+2,+2,+0,+5,+2,+2,0,+4,+4,Medical reform is not Green if service continuity breaks.
NATURAL_DISASTER_RECOVERY_POLICY_REFERENCE,+4,+4,+1,+1,+3,+1,+0,+2,+5,+1,0,+4,+4,Disaster recovery requires claims, budget and contracts before theme scoring.
GEOPOLITICAL_DEFENSE_ORDER_STAGE2,+4,+4,+5,+4,+2,+1,+0,+1,+1,+2,-4,+5,+4,Hanwha Romania order needs delivery, margin, cash collection and dilution-adjusted EPS.
LABOR_POLICY_SYSTEMIC_EXPORT_RISK_4C,+4,+5,+2,+2,+4,+2,+2,+4,+1,+5,0,+5,+5,Samsung strike risk shows labor continuity is systemic export-chain gate.
```

---

# 이번 R11 Loop 14 결론

```text
1. Korea Gas / Blue Whale은 price_moved_without_evidence다.
   +30% 급등은 policy/resource headline이었고, drilling result와 economic viability가 없었다.

2. Hanwha Ocean은 geopolitical sanctions 4C-watch다.
   U.S.-ROK shipbuilding cooperation은 수혜이면서 동시에 중국 제재 리스크를 만든다.

3. Martial law shock은 R11 hard reference다.
   정치 리스크는 개별 섹터보다 먼저 유동성·환율·외국인 신뢰를 흔든다.

4. Tax policy / AI windfall tax는 market-confidence 4C다.
   시장개혁을 말해도 세제 일관성이 없으면 KOSPI가 즉시 반응한다.

5. Short-selling / unfair-trading reform은 Stage 2다.
   MSCI 접근성 평가는 좋아졌지만, foreign flow와 brokerage earnings가 Stage 3 조건이다.

6. Medical reform은 service-disruption reference다.
   정책 목적이 좋아도 병원 service capacity가 깨지면 Green이 아니다.

7. Wildfire는 disaster recovery reference다.
   복구 수혜는 claims, budget, reconstruction contracts 전에는 Stage 3가 아니다.

8. Hanwha Aerospace Romania K9은 defense-order success_candidate다.
   order와 backlog는 좋지만 delivery, margin, cash collection, dilution-adjusted EPS가 필요하다.

9. Samsung strike risk는 labor-policy systemic 4C-watch다.
   하루 생산중단 손실 1T won 가능성은 노사 이슈가 아니라 수출 시스템 리스크다.
```

한 문장으로 압축하면:

> **R11에서 진짜 Stage 3는 “정책·제재·재난·자원·개혁·방산 이벤트가 크다”가 아니라, policy implementation·legal finality·sanction exposure·political liquidity·tax consistency·service continuity·disaster cashflow·labor continuity가 실제 숫자로 닫히는 순간이다.**

[1]: https://www.reuters.com/world/asia-pacific/skoreas-yoon-says-vast-amount-oil-gas-reserve-possible-off-east-coast-2024-06-03/?utm_source=chatgpt.com "South Korea's Yoon approves exploration of vast oil and gas prospects"
[2]: https://www.reuters.com/world/asia-pacific/china-takes-steps-against-us-linked-units-skorea-shipbuilder-hanwha-2025-10-14/?utm_source=chatgpt.com "China takes steps against US-linked units of S.Korea shipbuilder Hanwha"
[3]: https://www.reuters.com/markets/asia/skorea-authorities-vow-stabilize-markets-parliament-votes-lift-martial-law-2024-12-03/?utm_source=chatgpt.com "South Korea rushes to stabilise markets after Yoon's martial law bid"
[4]: https://www.marketwatch.com/story/south-koreas-new-tax-proposals-derail-one-of-the-worlds-best-performing-stock-markets-of-2025-9432538d?utm_source=chatgpt.com "South Korea's new tax proposals derail one of the world's best performing stock markets of 2025."
[5]: https://www.reuters.com/world/asia-pacific/south-koreas-short-selling-accessibility-has-improved-msci-says-2025-06-20/?utm_source=chatgpt.com "South Korea's short-selling accessibility has improved, MSCI says"
[6]: https://www.reuters.com/world/asia-pacific/south-korea-send-military-doctors-hospitals-amid-doctors-protest-2024-02-28/?utm_source=chatgpt.com "South Korea to send military doctors to hospitals amid doctors' protest"
[7]: https://www.reuters.com/world/asia-pacific/death-toll-south-korea-wildfires-rises-15-yonhap-says-2025-03-25/?utm_source=chatgpt.com "Death toll in South Korea wildfires rises to 16"
[8]: https://www.reuters.com/business/aerospace-defense/south-koreas-hanwha-aerospace-wins-1-bln-order-romania-k9-howitzers-2024-07-09/?utm_source=chatgpt.com "South Korea's Hanwha Aerospace wins $1 bln order from Romania for self-propelled howitzers"
[9]: https://www.reuters.com/business/world-at-work/south-korea-says-it-will-pursue-all-options-avoid-samsung-strike-2026-05-17/?utm_source=chatgpt.com "South Korea says it will pursue all options to avoid Samsung strike"
