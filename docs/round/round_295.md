순서상 이번은 **R13 Loop 14 — Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리 라운드**다.

```text
round = R13 Loop 14
round_id = round_223
large_sector = CROSS_ARCHETYPE_REDTEAM_4B_ACCOUNTING_TRUST_PRICE_VALIDATION
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R1 Loop 15
```

이번 R13은 특정 업종을 늘리는 라운드가 아니라, 앞의 R1~R12에서 반복적으로 나온 **점수표의 오판 패턴**을 잡는 라운드다. 핵심은 하나다.

> **Stage 3는 “좋은 뉴스”가 아니라, 뉴스가 매출·마진·현금흐름·계약이행·리스크 제거로 닫힌 상태다.**

이번에도 KRX/Naver/Yahoo/Stooq 조정 OHLC 전체 window는 안정적으로 확보하지 못했다. 대신 Reuters/FT/WSJ/MarketWatch가 보도한 **event return, event price, 계약금액 변화, capex·증자 규모, 벌금·보상·매출전망 조정, IPO price/debut price**를 price anchor로 사용했다. full 30D/90D/180D/1Y MFE·MAE는 만들지 않고, 해당 칸은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R13 = Cross-archetype RedTeam / 4B / Accounting Trust / Price Validation
```

R13에서 보는 축은 업종이 아니라 **오판 엔진**이다.

```text
1. headline_vs_cashflow
2. order_backlog_vs_delivery_margin
3. signed_contract_vs_actual_calloff
4. capex_localization_vs_IRR_funding
5. IPO_demand_vs_aftermarket_validation
6. control_premium_vs_operating_cashflow
7. governance_proposal_vs_execution
8. data_trust_or_safety_event_vs_brand_moat
9. resource_estimate_vs_drilling_economics
10. capital_raise_dilution_vs_growth_story
```

---

# 2. 대상 canonical archetype

```text
DEFENSE_BACKLOG_DILUTION_4B
SIGNED_CONTRACT_COLLAPSE_HARD_4C
RESOURCE_DISCOVERY_PRICE_MOVED_WITHOUT_EVIDENCE
AI_CLOUD_IPO_FALSE_POSITIVE
VALUE_UP_SHAREHOLDER_RETURN_FALSE_POSITIVE
DATA_TRUST_HARD_4C
LOCALIZATION_CAPEX_FALSE_POSITIVE
CONTROL_PREMIUM_4B_GOVERNANCE_WATCH
```

---

# 3. deep sub-archetype

```text
방산:
- order backlog / 지정학 수혜 / 해외공장 / 증자 희석
- Hanwha Aerospace

배터리 소재:
- customer-name contract / Tesla / actual call-off / 4680 ramp failure
- L&F

자원개발:
- 대통령 발표 / 14B barrels / drilling success probability / economic viability
- Korea Gas / Daesung Energy / SK Innovation / SK Gas

AI·cloud IPO:
- cloud/AI sales mix / IPO oversubscription / weak debut
- LG CNS

Value-Up:
- activist proposal / dividend / buyback / NPS vote / governance execution
- Samsung C&T

통신·보안:
- data breach / USIM leak / compensation / security capex / revenue forecast cut
- SK Telecom

철강·capex:
- U.S. localization / tariff hedge / funding plan / IRR
- Hyundai Steel

지배권 premium:
- tender offer / control premium / buyback / governance / operating cashflow separation
- Korea Zinc
```

---

# 4. 국장 cross-case 후보

## Case A — Hanwha Aerospace: 방산 order backlog + 증자 희석

```text
symbol = 012450
case_type = overheat / false_positive_score / 4B-watch
archetype = DEFENSE_BACKLOG_DILUTION_4B
```

### stage date

```text
Stage 1:
2024~2025
- 유럽 재무장, K9/K10 수출, 방산 order backlog 확대.
- 지정학 수혜로 defense rerating 진행.

Stage 4B:
2025-03-21
- Hanwha Aerospace shares had more than doubled YTD.
- 회사가 3.6T won / $2.5B 규모 share sale 계획 발표.
- 증자가는 605,000 won, 전일 종가 대비 16% 할인.
- 주가 -13%.
- 목적: 해외공장, 해외 파트너 지분, 글로벌 생산능력 확대.

Stage 4C-watch:
2025-03-27
- FSS가 3.6T won capital raising filing을 수정하라고 명령.
- “투자자의 합리적 의사결정에 필요한 정보가 부족”했다는 취지.
```

이 case는 R13의 핵심 4B다. 방산 order backlog가 아무리 좋아도, 그 성장이 **희석을 동반한 자본조달**로 이어지면 기존 주주는 즉시 맞는다. Hanwha Aerospace는 수주 기대와 지정학 premium으로 주가가 이미 크게 오른 상태에서 3.6T won 증자 계획을 발표했고, 주가는 -13%를 맞았다. 이후 FSS가 filing 수정을 명령한 점은 **capital allocation disclosure quality** 자체가 점수 축이어야 한다는 근거다. ([Financial Times][1])

### 실제 가격경로 검증

```json
{
  "case_id": "r13_loop14_hanwha_aerospace_backlog_dilution_4b",
  "symbol": "012450",
  "stage4b_date": "2025-03-21",
  "stage4c_watch_date": "2025-03-27",
  "stage3_price": null,
  "price_data_source": "FT / Reuters share-sale and FSS filing-revision anchors",
  "share_sale_krw_trn": 3.6,
  "share_sale_usd_bn": 2.5,
  "offer_price_krw": 605000,
  "discount_to_prior_close_pct": 16,
  "event_mae_pct": -13,
  "ytd_pre_event_gain_context": "more_than_double",
  "fss_revision_order": true,
  "disclosure_quality_issue": true,
  "mfe_30d_90d_180d_1y": "N/A_no_valid_stage3",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = false_positive_score
rerating_result = defense_backlog_4B_dilution_reset
stage_failure_type = order_backlog_not_dilution_adjusted_EPS_green
```

---

## Case B — L&F / Tesla: signed contract hard 4C

```text
symbol = 066970
case_type = hard_4C
archetype = SIGNED_CONTRACT_COLLAPSE_HARD_4C
```

### stage date

```text
Stage 1:
2023
- L&F signs high-nickel cathode material supply deal with Tesla and affiliates.
- market links contract to Tesla 4680 battery ramp.

Stage 2:
2023
- expected deal value: $2.9B.
- supply period: January 2024 ~ December 2025.

Stage 4C:
2025-12-29
- contract value cut to $7,386.
- collapse ratio: about -99.9997%.
- likely drivers: Tesla 4680 production/ramp issues, EV demand slowdown, Cybertruck underperformance.
```

이 case는 R13에서 가장 강한 **계약 신뢰도 hard 4C**다. “Tesla 계약”이라는 고객명과 $2.9B 금액이 있어도 실제 call-off가 없으면 계약은 매출이 아니다. Reuters는 L&F의 계약금액이 $2.9B에서 $7,386로 줄었다고 보도했고, EV 수요 둔화와 Tesla 4680 ramp 문제가 배경으로 언급됐다. 계산상 계약가치는 약 -99.9997% 붕괴다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "case_id": "r13_loop14_lnf_tesla_signed_contract_collapse_hard_4c",
  "symbol": "066970",
  "stage4c_date": "2025-12-29",
  "stage3_price": null,
  "price_data_source": "Reuters L&F/Tesla contract-value collapse anchor",
  "initial_contract_value_usd_bn": 2.9,
  "revised_contract_value_usd": 7386,
  "contract_value_collapse_pct": -99.9997,
  "supply_period": "2024-01_to_2025-12",
  "customer": "Tesla and affiliates",
  "material": "high-nickel cathode materials",
  "application_context": "Tesla 4680 cells",
  "reported_likely_drivers": [
    "EV demand slowdown",
    "4680 production/ramp difficulty",
    "Cybertruck underperformance"
  ],
  "mfe_30d_90d_180d_1y": "N/A_no_valid_stage3",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = signed_contract_collapse_hard_4C
stage_failure_type = signed_contract_without_actual_calloff
```

---

## Case C — Korea Gas / Blue Whale: resource headline event premium

```text
symbols = 036460 / 117580 / 096770 / 018670
case_type = price_moved_without_evidence
archetype = RESOURCE_DISCOVERY_PRICE_MOVED_WITHOUT_EVIDENCE
```

### stage date

```text
Stage 1:
2024-06-03
- 대통령이 동해 심해 oil/gas 탐사 시추 승인.
- 최대 14B barrels 가능성 발표.

Stage 4B:
2024-06-03
- Korea Gas +30%, 17-month high.
- Daesung Energy +30%.
- SK Innovation +6%.
- SK Gas +7%.
- KOSPI +1.9%.
- project cost >500B won.
- per-well cost around 100B won.
- success probability about 20%.
- commercial production target 2035.
- economic viability unconfirmed.
```

이 case는 **정책·자원 headline이 가격을 먼저 움직인 전형**이다. 매장량 estimate는 크지만, Reuters는 “시추해야 실제로 얼마나 있는지 알 수 있다”는 Rystad Energy 분석을 인용했고, 성공확률은 약 20%라고 보도했다. WSJ도 경제성은 아직 확정되지 않았고, 최소 여러 차례 시추가 필요하다고 설명했다. 따라서 이 case는 Stage 3가 아니라 `price_moved_without_evidence`다. ([Reuters][3])

### 실제 가격경로 검증

```json
{
  "case_id": "r13_loop14_kogas_blue_whale_resource_event_premium",
  "symbols": "036460/117580/096770/018670",
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
  "drilling_result_confirmed": false,
  "economic_viability_confirmed": false,
  "stage3_mfe_mae": "N/A_no_valid_stage3"
}
```

### alignment

```text
score_price_alignment = price_moved_without_evidence
rerating_result = resource_discovery_event_premium
stage_failure_type = resource_estimate_without_drilling_IRR
```

---

## Case D — LG CNS: AI/cloud IPO false positive

```text
symbol = 064400
case_type = evidence_good_but_price_failed
archetype = AI_CLOUD_IPO_FALSE_POSITIVE
```

### stage date

```text
Stage 1:
2025-01~2025-02
- LG CNS marketed as IT/cloud/AI service IPO.
- cloud and AI services accounted for over half of sales in first three quarters of 2024.

Stage 2:
2025-02-05
- IPO price: 61,900 won.
- opening price: 60,500 won.
- morning trading price: 59,700 won.
- debut price move vs IPO at 59,700 won: about -3.55%.
- IPO raised 1.2T won / $827.1M.
- retail tranche oversubscribed nearly 123x.
- institutional bids about 76T won.

Stage 3:
없음
- AI/cloud sales mix and oversubscription did not pass aftermarket price test.
```

LG CNS는 R13의 **IPO quality gate**다. AI/cloud 비중이 높고 청약 수요가 강해도, 상장 후 가격이 공모가를 지키지 못하면 Stage 3가 아니다. Reuters는 LG CNS가 공모가 61,900원보다 낮은 59,700원에 거래됐다고 보도했다. 계산상 59,700원 기준 debut move는 약 -3.55%다. ([Reuters][4])

### 실제 가격경로 검증

```json
{
  "case_id": "r13_loop14_lg_cns_ai_cloud_ipo_false_positive",
  "symbol": "064400",
  "stage2_date": "2025-02-05",
  "stage3_price": null,
  "price_data_source": "Reuters LG CNS IPO/debut anchor",
  "ipo_price_krw": 61900,
  "open_price_krw": 60500,
  "morning_trading_price_krw": 59700,
  "debut_mae_vs_ipo_pct": -3.55,
  "ipo_raise_krw_trn": 1.2,
  "ipo_raise_usd_mn": 827.1,
  "retail_oversubscription_multiple": 123,
  "institutional_bids_krw_trn": 76,
  "cloud_ai_sales_share_context": "over_half_of_9m_2024_sales",
  "aftermarket_demand_confirmed": false,
  "mfe_30d_90d_180d_1y": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed
rerating_result = AI_cloud_IPO_quality_gate
stage_failure_type = AI_cloud_sales_mix_not_aftermarket_green
```

---

## Case E — Samsung C&T: Value-Up proposal failure

```text
symbol = 028260
case_type = false_positive_score
archetype = VALUE_UP_SHAREHOLDER_RETURN_FALSE_POSITIVE
```

### stage date

```text
Stage 1:
2024-03
- activist investors push Samsung C&T for higher dividends and buybacks.
- Korea Value-Up optimism lifts governance/capital-return expectations.

Stage 4C-watch:
2024-03-15
- activist proposals fail.
- Norway oil fund and Canadian pension investors supported the proposals.
- National Pension Service sides with Samsung C&T management.
- shares close almost -10%.
```

Samsung C&T는 “Value-Up 기대”와 “실제 주주환원 실행”을 분리해야 한다는 반례다. FT는 배당과 자사주 확대 제안이 실패했고, NPS가 management 편에 섰으며, Samsung C&T shares가 거의 -10% 하락했다고 보도했다. 즉 governance proposal은 Stage 2도 약하다. Green은 **board adoption, payout execution, treasury cancellation**이 실제로 나와야 한다. ([Financial Times][5])

### 실제 가격경로 검증

```json
{
  "case_id": "r13_loop14_samsung_ct_valueup_proposal_failure",
  "symbol": "028260",
  "stage4c_watch_date": "2024-03-15",
  "stage3_price": null,
  "price_data_source": "FT activist proposal failure anchor",
  "event_mae_pct": -10.0,
  "activist_backers": [
    "Norway oil fund",
    "Canadian pension investors"
  ],
  "nps_vote": "sided_with_management",
  "proposal_type": [
    "dividend increase",
    "share buyback increase"
  ],
  "proposal_passed": false,
  "stage3_conditions": [
    "board adoption",
    "payout execution",
    "treasury-share cancellation",
    "minority shareholder alignment"
  ],
  "mfe_30d_90d_180d_1y": "N/A_no_valid_stage3"
}
```

### alignment

```text
score_price_alignment = false_positive_score
rerating_result = shareholder_return_proposal_failed
stage_failure_type = governance_proposal_not_capital_return_execution
```

---

## Case F — SK Telecom: data-trust hard 4C

```text
symbol = 017670
case_type = hard_4C
archetype = DATA_TRUST_HARD_4C
```

### stage date

```text
Stage 1:
2025-04-18
- SK Telecom detects malware-linked data breach.

Stage 4C:
2025-04-28
- shares fall as much as -8.5%.
- close -6.7%.
- KOSPI +0.1%.
- all 23M users offered free USIM replacement.
- more than 2,600 stores used.
- 5.54M users had signed up for USIM Protection Service.

Stage 4C validation:
2025-07-04
- 26.96M pieces of user data leaked.
- shares close -5.6%.
- data-protection investment: 700B won over five years.
- August bill discount for 24M customers.
- 2025 revenue forecast cut by 800B won.
- customer benefit package cost about 500B won.

Stage 4C liability expansion:
2025-12-21
- consumer agency compensation order for 58 class-action applicants.
- broader compensation for all victims could cost nearly 2.3T won.
```

SK Telecom은 R13의 가장 명확한 **data-trust hard 4C**다. 보안사고는 일회성 PR 비용이 아니라, 주가, 고객보상, capex, 매출전망, 과징금, 잠재 집단보상까지 한꺼번에 때린다. Reuters는 최초 disclosure 후 SKT가 장중 -8.5%, 종가 -6.7%였고 KOSPI는 +0.1%였다고 보도했다. 7월 조사 이후에는 700B won 보안투자, 800B won revenue forecast cut, 약 500B won customer package가 나왔다. 이후 소비자원 compensation order는 전체 피해자 보상 시 2.3T won 가능성까지 열었다. ([Reuters][6])

### 실제 가격경로 검증

```json
{
  "case_id": "r13_loop14_skt_data_trust_hard_4c",
  "symbol": "017670",
  "stage4c_date": "2025-04-28/2025-07-04/2025-12-21",
  "stage3_price": null,
  "price_data_source": "Reuters SK Telecom breach, government investigation and compensation anchors",
  "initial_intraday_mae_pct": -8.5,
  "initial_close_mae_pct": -6.7,
  "kospi_same_context_pct": 0.1,
  "relative_underperformance_initial_pp": -6.8,
  "free_usim_replacement_users_mn": 23,
  "retail_stores_involved": 2600,
  "usim_protection_service_signups_mn": 5.54,
  "leaked_data_pieces_mn": 26.96,
  "july_event_close_mae_pct": -5.6,
  "data_protection_investment_krw_bn": 700,
  "revenue_forecast_cut_krw_bn": 800,
  "customer_benefit_package_cost_krw_bn": 500,
  "consumer_agency_possible_total_compensation_krw_trn": 2.3,
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = data_trust_hard_4C
stage_failure_type = customer_data_internal_control_break
```

---

## Case G — Hyundai Steel: U.S. localization capex false positive

```text
symbol = 004020
case_type = false_positive_score
archetype = LOCALIZATION_CAPEX_FALSE_POSITIVE
```

### stage date

```text
Stage 1:
2025-03-24
- Hyundai Motor Group announces U.S. investment package.
- Hyundai Steel included with $6B U.S. plant plan.

Stage 4C-watch / false positive:
2025-04-22
- Hyundai Steel stock lost 21.2% after the investment announcement.
- POSCO lost 18.3%.
- KOSPI lost 5.5%.
- Hyundai Motor lost 12.9%.
- funding details unclear.
- plant expected to produce enough steel for 1.8M vehicles annually, above Hyundai/Kia U.S. production target of 1.2M units.
- Hyundai Steel planned to fund 50% with borrowing, with remaining funding not fully disclosed.
```

이 case는 “미국 현지화 capex = tariff hedge = Green”이 왜 위험한지 보여준다. Reuters는 Hyundai Steel의 $6B U.S. plant 계획이 투자자 반발을 불렀고, 발표 이후 주가가 21.2% 하락했다고 보도했다. 핵심은 공장 자체가 아니라 **funding clarity, IRR, customer demand, tariff-saving durability**다. Capex가 클수록 Green이 아니라, 잘못하면 debt/dilution/ROIC 악화다. ([Reuters][7])

### 실제 가격경로 검증

```json
{
  "case_id": "r13_loop14_hyundai_steel_us_localization_capex_false_positive",
  "symbol": "004020",
  "stage4c_watch_date": "2025-04-22",
  "stage3_price": null,
  "price_data_source": "Reuters Hyundai Steel U.S. plant investor-backlash anchor",
  "us_plant_investment_usd_bn": 6,
  "hyundai_group_us_package_usd_bn": 21,
  "hyundai_steel_stock_decline_since_announcement_pct": -21.2,
  "posco_same_period_decline_pct": -18.3,
  "kospi_same_period_decline_pct": -5.5,
  "hyundai_motor_same_period_decline_pct": -12.9,
  "planned_output_vehicle_equivalent_mn": 1.8,
  "hyundai_kia_us_production_target_mn": 1.2,
  "debt_funding_share_pct": 50,
  "full_funding_plan_disclosed": false,
  "mfe_30d_90d_180d_1y": "N/A_no_valid_stage3",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = false_positive_score
rerating_result = localization_capex_false_positive
stage_failure_type = capex_without_IRR_funding_clarity
```

---

## Case H — Korea Zinc: control premium 4B

```text
symbol = 010130 / 000670
case_type = 4B-watch
archetype = CONTROL_PREMIUM_4B_GOVERNANCE_WATCH
```

### stage date

```text
Stage 1:
2024-09-13
- MBK Partners and Young Poong launch tender offer for Korea Zinc.
- non-ferrous metal / strategic smelter control premium enters market.

Stage 4B:
2024-09-13
- tender offer value: 2T won / $1.5B.
- offer price: 660,000 won.
- prior close: 556,000 won.
- target stake: 6.98%~14.61%.
- Korea Zinc +19.8%.
- Young Poong daily limit +30%.

Stage 4C-watch:
- control premium and governance dispute are not smelting-margin Green.
- tender control, buyback, financing, regulatory and safety issues must be separated from operating cashflow.
```

Korea Zinc는 R13의 지배권 premium 4B다. Korea Zinc +19.8%, Young Poong +30%라는 event return은 강하지만, 이건 zinc spread, smelter margin, FCF가 아니라 control premium이다. Reuters는 MBK/Young Poong tender offer가 2T won 규모였고 Korea Zinc가 이를 hostile takeover attempt로 규정했다고 보도했다. 따라서 Stage 3는 불가능하고, 이 row는 **control premium을 operating rerating과 분리하는 calibration**이다. ([Reuters][8])

### 실제 가격경로 검증

```json
{
  "case_id": "r13_loop14_korea_zinc_control_premium_4b",
  "symbol": "010130/000670",
  "stage4b_date": "2024-09-13",
  "stage3_price": null,
  "price_data_source": "Reuters Korea Zinc tender-offer anchor",
  "tender_offer_value_krw_trn": 2.0,
  "tender_offer_value_usd_bn": 1.5,
  "offer_price_krw": 660000,
  "prior_close_krw": 556000,
  "tender_premium_to_prior_close_pct": 18.7,
  "target_stake_min_pct": 6.98,
  "target_stake_max_pct": 14.61,
  "korea_zinc_event_mfe_pct": 19.8,
  "young_poong_event_mfe_pct": 30.0,
  "young_poong_existing_stake_pct": 25.4,
  "combined_stake_if_success_pct": 40.0,
  "operating_cashflow_improvement_confirmed": false,
  "mfe_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_4B_watch
rerating_result = control_premium_not_operating_green
stage_failure_type = tender_offer_governance_premium_not_margin_FCF
```

---

# 5. 이번 R13 case별 stage date 요약

| case                 | Stage 1           | Stage 2           | Stage 3 | Stage 4B                  | Stage 4C                  |
| -------------------- | ----------------- | ----------------- | ------- | ------------------------- | ------------------------- |
| Hanwha Aerospace     | 방산 order/backlog  | 증자 계획             | N/A     | 2025-03 overheat/dilution | FSS filing quality watch  |
| L&F/Tesla            | 2023 계약           | $2.9B headline    | N/A     | N/A                       | 2025-12 contract collapse |
| Korea Gas/Blue Whale | 2024-06 발표        | 시추 승인             | N/A     | +30% resource event       | economics unconfirmed     |
| LG CNS               | AI/cloud IPO      | IPO priced        | N/A     | IPO demand                | weak debut                |
| Samsung C&T          | Value-Up proposal | activist push     | N/A     | governance hope           | proposal failure          |
| SK Telecom           | breach detected   | mitigation        | N/A     | N/A                       | data-trust hard 4C        |
| Hyundai Steel        | U.S. capex        | localization plan | N/A     | N/A                       | funding/IRR backlash      |
| Korea Zinc           | tender offer      | control bid       | N/A     | +19.8% control premium    | governance/FCF watch      |

---

# 6. 실제 가격경로 검증 총괄

| case                 |                                  가격·사업 anchor | 해석                            | 판정                             |
| -------------------- | --------------------------------------------: | ----------------------------- | ------------------------------ |
| Hanwha Aerospace     | share sale 3.6T won, -13%, FSS revision order | backlog 과열 후 dilution reset   | false_positive_score           |
| L&F/Tesla            |                     $2.9B → $7,386, -99.9997% | signed contract hard break    | thesis_break                   |
| Korea Gas/Blue Whale |           KOGAS +30%, success probability 20% | resource headline만 선반영        | price_moved_without_evidence   |
| LG CNS               |                   61,900 → 59,700 won, -3.55% | AI/cloud IPO demand failed    | evidence_good_but_price_failed |
| Samsung C&T          |           activist proposal fail, almost -10% | Value-Up proposal ≠ execution | false_positive_score           |
| SK Telecom           |    -8.5% intraday, revenue forecast -800B won | data trust hard 4C            | thesis_break                   |
| Hyundai Steel        |                  -21.2% after U.S. plant plan | capex/funding false positive  | false_positive_score           |
| Korea Zinc           |                      +19.8%, Young Poong +30% | control premium 4B            | event_premium                  |

---

# 7. score-price alignment 판정

```text
aligned:
- 없음. R13은 실패/과열/검증 게이트를 찾는 RedTeam 라운드.

false_positive_score:
- Hanwha Aerospace: backlog와 지정학 premium을 dilution-adjusted EPS로 보정하지 않음.
- Samsung C&T: shareholder-return proposal을 execution으로 오인.
- Hyundai Steel: U.S. localization capex를 IRR/funding clarity 없이 Green으로 오인.
- LG CNS: AI/cloud sales mix와 IPO demand를 aftermarket validation 없이 Green으로 오인.

price_moved_without_evidence:
- Korea Gas / Blue Whale.
- Kyochon류 meme rally와 같은 구조의 resource-event version.

event_premium:
- Korea Zinc control premium.
- Korea Gas resource event.
- Hanwha Aerospace backlog/defense premium before dilution.
- LG CNS IPO subscription demand.

evidence_good_but_price_failed:
- LG CNS.
- Samsung C&T.
- Hyundai Steel U.S. plant.

thesis_break:
- L&F/Tesla contract collapse.
- SK Telecom data-trust breach.

4B-watch:
- Hanwha Aerospace.
- Korea Zinc.
- Korea Gas.
- LG CNS IPO demand.

hard_4C:
- L&F/Tesla.
- SK Telecom.
```

---

# 8. 점수비중 교정

## 올릴 축

```text
actual_calloff_vs_signed_contract +5
dilution_adjusted_EPS +5
capital_raise_disclosure_quality +5
capex_IRR_and_funding_clarity +5
aftermarket_price_validation +5
data_trust_internal_control +5
contingent_liability_risk +5
governance_execution_not_proposal +5
control_premium_separation +4
resource_economic_viability +5
```

### 어떤 case 때문에 올리나

L&F는 signed contract가 actual call-off가 아니면 거의 0까지 줄 수 있음을 보여줬다. Hanwha Aerospace는 backlog가 좋아도 증자 희석이 들어오면 EPS가 바뀐다는 점을 보여줬다. 현대제철은 U.S. capex headline보다 funding과 IRR이 먼저라는 사실을 검증했다. LG CNS는 AI/cloud mix와 청약 경쟁률보다 상장 후 가격이 더 강한 검증이라는 것을 보여줬다. SK Telecom은 data trust failure가 비용·매출전망·보상·보안투자로 바로 내려오는 hard gate다.

## 내릴 축

```text
headline_order_backlog_only -5
large_customer_name_only -5
policy_or_presidential_announcement_only -5
IPO_oversubscription_only -5
activist_or_valueup_proposal_only -5
control_premium_as_operating_green -5
capex_localization_headline_only -5
resource_estimate_without_drilling -5
data_breach_treated_as_oneoff -5
```

### 어떤 case 때문에 내리나

Korea Gas는 대통령 발표와 14B barrels headline만으로 +30%가 나왔지만 경제성이 없었다. Samsung C&T는 Value-Up proposal이 실패하자 -10%가 나왔다. Korea Zinc는 control premium이 operating cashflow와 다르다. SK Telecom은 data breach를 일회성으로 처리하면 안 된다. L&F는 고객명과 계약금액 headline을 actual demand로 착각하면 hard 4C가 발생한다.

---

# 9. Green gate 강화 조건

```text
R13 cross-archetype Stage 3-Green 필수:
1. 계약은 signed amount가 아니라 actual call-off / revenue recognition 확인.
2. 수주는 delivery schedule, margin, cash collection 확인.
3. 자사주·배당·Value-Up은 proposal이 아니라 board adoption, execution, cancellation 확인.
4. IPO는 청약경쟁률이 아니라 aftermarket price, first earnings, guide 확인.
5. Capex는 funding source, IRR, customer demand, ramp schedule 확인.
6. 자원개발은 drilling result, reserve certification, economic viability, CAPEX/IRR 확인.
7. M&A/control premium은 operating cashflow와 따로 scoring.
8. 데이터·안전·규제 사고는 contingent liability와 revenue forecast impact 확인.
9. 증자/CB/희석은 dilution-adjusted EPS로 재계산.
10. price path가 evidence 이후 따라오는지 확인.
```

---

# 10. 4B 조기감지 조건

```text
4B-watch early trigger:
- 주가가 6~12개월 안에 2배 이상 오른 뒤 대규모 증자/CB 가능성이 생김.
- order backlog / defense / AI / resource headline으로 PER rerating만 먼저 나옴.
- IPO 청약경쟁률이 높지만 debut price가 공모가를 못 지킴.
- control premium으로 +15~30% 급등하지만 영업현금흐름 변화 없음.
- 대통령/정부 발표 하나로 +20~30% 급등하고 실물 검증은 없음.
- capex/localization headline이 크지만 funding plan, IRR, customer demand가 미공개.
- activist proposal 기대만 있고 board adoption이 없음.
```

---

# 11. 4C hard gate 조건

```text
Hard 4C:
- signed contract value collapse.
- data breach / trust failure with compensation, capex, revenue-forecast impact.
- fatal safety or service-trust event.
- financing plan blocked or revised by regulator due disclosure quality.
- capex plan causes major dilution/debt without IRR clarity.
- governance proposal fails after Value-Up rerating.
- resource drilling fails after speculative rally.
- customer call-off or model cancellation destroys expected revenue.
```

이번 R13 Loop 14에서 hard 4C는 두 개다.

```text
1. L&F / Tesla contract collapse:
   signed contract headline이 actual call-off가 아니라는 hard 4C.

2. SK Telecom data breach:
   data trust failure가 매출전망, 보상, capex, 과징금, 잠재 보상으로 번진 hard 4C.
```

Hanwha Aerospace, Korea Gas, LG CNS, Samsung C&T, Hyundai Steel, Korea Zinc는 hard 4C가 아니라 **4B-watch / false_positive / price_moved_without_evidence / event premium**이다.

---

# 12. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 13. 레포 반영용 patch-ready 출력

## docs/round/round_223.md 요약

```md
# R13 Loop 14. Cross-archetype RedTeam / 4B / Accounting Trust / Price Validation

이번 라운드는 R13 Loop 14 cross-archetype red-team 라운드다.

핵심 결론:
- Hanwha Aerospace is DEFENSE_BACKLOG_DILUTION_4B. Shares had more than doubled YTD but fell 13% after a 3.6T won / $2.5B share-sale plan. The FSS later ordered a revised filing, saying information needed for rational investor decisions was lacking.
- L&F / Tesla is SIGNED_CONTRACT_COLLAPSE_HARD_4C. The expected $2.9B cathode supply deal was cut to $7,386, a near-total collapse. Customer name and signed amount are not actual call-off.
- Korea Gas / Blue Whale is RESOURCE_DISCOVERY_PRICE_MOVED_WITHOUT_EVIDENCE. KOGAS +30%, Daesung Energy +30%, SK Innovation +6%, SK Gas +7% after the presidential drilling approval, but success probability was about 20% and economic viability was unconfirmed.
- LG CNS is AI_CLOUD_IPO_FALSE_POSITIVE. IPO price 61,900 won, morning trade 59,700 won, about -3.55% vs IPO, despite 1.2T won IPO, nearly 123x retail oversubscription and cloud/AI sales mix over half.
- Samsung C&T is VALUE_UP_SHAREHOLDER_RETURN_FALSE_POSITIVE. Activist dividend/buyback proposals backed by Norway’s oil fund and Canadian pension investors failed; NPS sided with management; shares closed almost -10%.
- SK Telecom is DATA_TRUST_HARD_4C. Shares -8.5% intraday and -6.7% close after breach; later 26.96M data pieces leaked, 700B won security investment, 800B won revenue forecast cut, 500B won customer package, and possible broader compensation up to 2.3T won.
- Hyundai Steel U.S. plant is LOCALIZATION_CAPEX_FALSE_POSITIVE. Shares lost 21.2% after a $6B U.S. plant plan amid unclear funding, IRR and customer-demand questions.
- Korea Zinc is CONTROL_PREMIUM_4B. Tender offer value 2T won, offer price 660,000 won, Korea Zinc +19.8%, Young Poong +30%. Control premium is not operating-cashflow Green.

Shadow correction:
- Raise actual_calloff_vs_signed_contract, dilution_adjusted_EPS, capital_raise_disclosure_quality, capex_IRR_and_funding_clarity, aftermarket_price_validation, data_trust_internal_control, contingent_liability_risk, governance_execution_not_proposal, control_premium_separation, resource_economic_viability.
- Lower headline_order_backlog_only, large_customer_name_only, policy_or_presidential_announcement_only, IPO_oversubscription_only, activist_or_valueup_proposal_only, control_premium_as_operating_green, capex_localization_headline_only, resource_estimate_without_drilling, data_breach_treated_as_oneoff.
```

## docs/checkpoints/checkpoint_28a_round223_r13_loop14.md 요약

```md
# Checkpoint 28A Round 223 R13 Loop 14 Cross-archetype RedTeam

## 반영 내용
- R13 Loop 14 cross-archetype red-team 라운드를 추가했다.
- Hanwha Aerospace, L&F/Tesla, Korea Gas/Blue Whale, LG CNS, Samsung C&T, SK Telecom, Hyundai Steel, Korea Zinc를 비교했다.
- Reuters / FT / WSJ / MarketWatch anchors로 event return, event price, contract collapse, share-sale amount, capex plan, compensation and revenue-forecast impact, IPO price/debut price metrics를 검증했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- actual_calloff_vs_signed_contract, dilution_adjusted_EPS, capital_raise_disclosure_quality, capex_IRR_and_funding_clarity, aftermarket_price_validation, data_trust_internal_control, contingent_liability_risk, governance_execution_not_proposal, control_premium_separation, resource_economic_viability 가중치 강화.
- headline_order_backlog_only, large_customer_name_only, policy_or_presidential_announcement_only, IPO_oversubscription_only, activist_or_valueup_proposal_only, control_premium_as_operating_green, capex_localization_headline_only, resource_estimate_without_drilling, data_breach_treated_as_oneoff 감점 강화.
```

## data/e2r_case_library/cases_r13_loop14_round223.jsonl 초안

```jsonl
{"case_id":"r13_loop14_hanwha_aerospace_backlog_dilution_4b","symbol":"012450","company_name":"Hanwha Aerospace","case_type":"false_positive_score_4b_watch","primary_archetype":"DEFENSE_BACKLOG_DILUTION_4B","stage4b_date":"2025-03-21","stage4c_watch_date":"2025-03-27","price_validation":{"price_data_source":"FT / Reuters share-sale and FSS filing-revision anchors","stage3_price":null,"share_sale_krw_trn":3.6,"share_sale_usd_bn":2.5,"offer_price_krw":605000,"discount_to_prior_close_pct":16,"event_mae_pct":-13,"ytd_pre_event_gain_context":"more_than_double","fss_revision_order":true,"disclosure_quality_issue":true,"mfe_30d_90d_180d_1y":"N/A_no_valid_stage3","mae_30d_90d_180d_1y":"price_data_unavailable_after_deep_search"},"score_price_alignment":"false_positive_score","rerating_result":"defense_backlog_4B_dilution_reset","notes":"Order backlog and geopolitical premium must be adjusted for dilution and disclosure quality."}
{"case_id":"r13_loop14_lnf_tesla_signed_contract_collapse_hard_4c","symbol":"066970","company_name":"L&F","case_type":"hard_4c","primary_archetype":"SIGNED_CONTRACT_COLLAPSE_HARD_4C","stage4c_date":"2025-12-29","price_validation":{"price_data_source":"Reuters L&F/Tesla contract-value collapse anchor","stage3_price":null,"initial_contract_value_usd_bn":2.9,"revised_contract_value_usd":7386,"contract_value_collapse_pct":-99.9997,"supply_period":"2024-01_to_2025-12","customer":"Tesla and affiliates","material":"high-nickel cathode materials","application_context":"Tesla 4680 cells","reported_likely_drivers":["EV demand slowdown","4680 production/ramp difficulty","Cybertruck underperformance"],"mfe_30d_90d_180d_1y":"N/A_no_valid_stage3","mae_30d_90d_180d_1y":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break","rerating_result":"signed_contract_collapse_hard_4C","notes":"Customer-name and signed contract amount are not Green without actual call-off/revenue recognition."}
{"case_id":"r13_loop14_kogas_blue_whale_resource_event_premium","symbol":"036460/117580/096770/018670","company_name":"Korea Gas / Daesung Energy / SK Innovation / SK Gas","case_type":"price_moved_without_evidence","primary_archetype":"RESOURCE_DISCOVERY_PRICE_MOVED_WITHOUT_EVIDENCE","stage4b_date":"2024-06-03","price_validation":{"price_data_source":"Reuters / WSJ resource-discovery event anchors","stage3_price":null,"korea_gas_event_mfe_pct":30,"korea_gas_event_price_krw":38700,"daesung_energy_event_mfe_pct":30,"sk_innovation_event_mfe_pct":6,"sk_gas_event_mfe_pct":7,"kospi_same_context_pct":1.9,"potential_resource_boe_bn":14,"project_cost_krw_bn_min":500,"per_well_cost_krw_bn":100,"success_probability_pct":20,"commercial_production_target":2035,"drilling_result_confirmed":false,"economic_viability_confirmed":false,"stage3_mfe_mae":"N/A_no_valid_stage3"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"resource_discovery_event_premium","notes":"Resource estimate and presidential announcement moved price before drilling and economic viability."}
{"case_id":"r13_loop14_lg_cns_ai_cloud_ipo_false_positive","symbol":"064400","company_name":"LG CNS","case_type":"evidence_good_but_price_failed","primary_archetype":"AI_CLOUD_IPO_FALSE_POSITIVE","stage2_date":"2025-02-05","price_validation":{"price_data_source":"Reuters LG CNS IPO/debut anchor","stage3_price":null,"ipo_price_krw":61900,"open_price_krw":60500,"morning_trading_price_krw":59700,"debut_mae_vs_ipo_pct":-3.55,"ipo_raise_krw_trn":1.2,"ipo_raise_usd_mn":827.1,"retail_oversubscription_multiple":123,"institutional_bids_krw_trn":76,"cloud_ai_sales_share_context":"over_half_of_9m_2024_sales","aftermarket_demand_confirmed":false,"mfe_30d_90d_180d_1y":"price_data_unavailable_after_deep_search","mae_30d_90d_180d_1y":"price_data_unavailable_after_deep_search"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"AI_cloud_IPO_quality_gate","notes":"AI/cloud sales mix and IPO oversubscription failed aftermarket validation."}
{"case_id":"r13_loop14_samsung_ct_valueup_proposal_failure","symbol":"028260","company_name":"Samsung C&T","case_type":"false_positive_score","primary_archetype":"VALUE_UP_SHAREHOLDER_RETURN_FALSE_POSITIVE","stage4c_watch_date":"2024-03-15","price_validation":{"price_data_source":"FT activist proposal failure anchor","stage3_price":null,"event_mae_pct":-10.0,"activist_backers":["Norway oil fund","Canadian pension investors"],"nps_vote":"sided_with_management","proposal_type":["dividend increase","share buyback increase"],"proposal_passed":false,"stage3_conditions":["board adoption","payout execution","treasury-share cancellation","minority shareholder alignment"],"mfe_30d_90d_180d_1y":"N/A_no_valid_stage3"},"score_price_alignment":"false_positive_score","rerating_result":"shareholder_return_proposal_failed","notes":"Value-Up proposal is not Green unless board adoption and cash-return execution occur."}
{"case_id":"r13_loop14_skt_data_trust_hard_4c","symbol":"017670","company_name":"SK Telecom","case_type":"hard_4c","primary_archetype":"DATA_TRUST_HARD_4C","stage4c_date":"2025-04-28/2025-07-04/2025-12-21","price_validation":{"price_data_source":"Reuters SK Telecom breach, government investigation and compensation anchors","stage3_price":null,"initial_intraday_mae_pct":-8.5,"initial_close_mae_pct":-6.7,"kospi_same_context_pct":0.1,"relative_underperformance_initial_pp":-6.8,"free_usim_replacement_users_mn":23,"retail_stores_involved":2600,"usim_protection_service_signups_mn":5.54,"leaked_data_pieces_mn":26.96,"july_event_close_mae_pct":-5.6,"data_protection_investment_krw_bn":700,"revenue_forecast_cut_krw_bn":800,"customer_benefit_package_cost_krw_bn":500,"consumer_agency_possible_total_compensation_krw_trn":2.3,"mae_30d_90d_180d_1y":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break","rerating_result":"data_trust_hard_4C","notes":"Data breach is not a one-off event when it changes revenue forecast, capex, compensation and contingent liability."}
{"case_id":"r13_loop14_hyundai_steel_us_localization_capex_false_positive","symbol":"004020","company_name":"Hyundai Steel","case_type":"false_positive_score","primary_archetype":"LOCALIZATION_CAPEX_FALSE_POSITIVE","stage4c_watch_date":"2025-04-22","price_validation":{"price_data_source":"Reuters Hyundai Steel U.S. plant investor-backlash anchor","stage3_price":null,"us_plant_investment_usd_bn":6,"hyundai_group_us_package_usd_bn":21,"hyundai_steel_stock_decline_since_announcement_pct":-21.2,"posco_same_period_decline_pct":-18.3,"kospi_same_period_decline_pct":-5.5,"hyundai_motor_same_period_decline_pct":-12.9,"planned_output_vehicle_equivalent_mn":1.8,"hyundai_kia_us_production_target_mn":1.2,"debt_funding_share_pct":50,"full_funding_plan_disclosed":false,"mfe_30d_90d_180d_1y":"N/A_no_valid_stage3","mae_30d_90d_180d_1y":"price_data_unavailable_after_deep_search"},"score_price_alignment":"false_positive_score","rerating_result":"localization_capex_false_positive","notes":"Localization capex needs funding clarity, IRR, customer demand and tariff-saving durability."}
{"case_id":"r13_loop14_korea_zinc_control_premium_4b","symbol":"010130/000670","company_name":"Korea Zinc / Young Poong / MBK","case_type":"event_premium_4b_watch","primary_archetype":"CONTROL_PREMIUM_4B_GOVERNANCE_WATCH","stage4b_date":"2024-09-13","price_validation":{"price_data_source":"Reuters Korea Zinc tender-offer anchor","stage3_price":null,"tender_offer_value_krw_trn":2.0,"tender_offer_value_usd_bn":1.5,"offer_price_krw":660000,"prior_close_krw":556000,"tender_premium_to_prior_close_pct":18.7,"target_stake_min_pct":6.98,"target_stake_max_pct":14.61,"korea_zinc_event_mfe_pct":19.8,"young_poong_event_mfe_pct":30.0,"young_poong_existing_stake_pct":25.4,"combined_stake_if_success_pct":40.0,"operating_cashflow_improvement_confirmed":false,"mfe_30d_90d_180d_1y":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_4B_watch","rerating_result":"control_premium_not_operating_green","notes":"Tender/control premium must be separated from operating cashflow, smelter margin and FCF."}
```

## data/sector_taxonomy/score_weight_profiles_round223_r13_loop14_v1.csv 초안

```csv
archetype,actual_calloff_vs_signed_contract,dilution_adjusted_eps,capital_raise_disclosure_quality,capex_irr_funding_clarity,aftermarket_price_validation,data_trust_internal_control,contingent_liability_risk,governance_execution_not_proposal,control_premium_separation,resource_economic_viability,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
DEFENSE_BACKLOG_DILUTION_4B,+2,+5,+5,+4,+2,+1,+3,+3,+2,+1,0,+5,+4,Hanwha shows backlog premium must be corrected for dilution and disclosure quality.
SIGNED_CONTRACT_COLLAPSE_HARD_4C,+5,+2,+2,+2,+1,+1,+3,+2,+1,+1,0,+4,+5,L&F/Tesla proves signed amount is not Green without actual call-off.
RESOURCE_DISCOVERY_PRICE_MOVED_WITHOUT_EVIDENCE,+1,+1,+2,+3,+1,+0,+2,+1,+0,+5,-5,+5,+4,Blue Whale shows resource estimate requires drilling and economic viability.
AI_CLOUD_IPO_FALSE_POSITIVE,+1,+2,+2,+2,+5,+2,+1,+2,+0,+0,-5,+5,+3,LG CNS shows AI/cloud mix and oversubscription need aftermarket validation.
VALUE_UP_SHAREHOLDER_RETURN_FALSE_POSITIVE,+1,+3,+3,+1,+2,+1,+1,+5,+2,+0,0,+5,+4,Samsung C&T shows shareholder-return proposal is not execution.
DATA_TRUST_HARD_4C,+1,+2,+3,+3,+2,+5,+5,+3,+0,+0,0,+4,+5,SK Telecom confirms data trust breach can alter revenue, capex and liabilities.
LOCALIZATION_CAPEX_FALSE_POSITIVE,+1,+4,+4,+5,+2,+1,+3,+2,+0,+0,0,+5,+4,Hyundai Steel shows localization capex needs funding clarity and IRR.
CONTROL_PREMIUM_4B_GOVERNANCE_WATCH,+1,+2,+3,+2,+2,+1,+3,+4,+5,+1,-4,+5,+3,Korea Zinc shows control premium must be separated from operating Green.
```

---

# 이번 R13 Loop 14 결론

```text
1. Hanwha Aerospace는 backlog-dilution 4B다.
   수주가 좋아도 증자 희석과 disclosure quality가 나쁘면 Stage 3가 아니라 false positive다.

2. L&F/Tesla는 signed-contract hard 4C다.
   고객명과 계약금액 headline은 actual call-off가 확인되기 전까지 Green이 아니다.

3. Korea Gas/Blue Whale은 price_moved_without_evidence다.
   대통령 발표와 14B barrels headline은 drilling result와 IRR이 나오기 전까지 4B다.

4. LG CNS는 AI/cloud IPO false positive다.
   AI/cloud 매출비중과 청약경쟁률보다 aftermarket price가 더 강한 검증이다.

5. Samsung C&T는 Value-Up false positive다.
   proposal과 execution을 분리하지 않으면 주주환원 score가 틀린다.

6. SK Telecom은 data-trust hard 4C다.
   보안사고는 주가, 매출전망, capex, 보상, 잠재부채를 동시에 바꾼다.

7. Hyundai Steel은 localization capex false positive다.
   U.S. plant capex는 funding clarity와 IRR 없이 Green이 아니라 리스크다.

8. Korea Zinc는 control-premium 4B다.
   tender premium은 operating cashflow Green이 아니다.
```

한 문장으로 압축하면:

> **R13에서 진짜 교정값은 “headline을 믿지 말고, call-off·희석조정 EPS·IRR·aftermarket price·실제 주주환원·내부통제·우발부채·operating cashflow로 다시 재단하라”다.**

다음 순서는 **R1 Loop 15 — 산업재·수주·인프라**다.

[1]: https://www.ft.com/content/994a0a80-414f-442f-bf41-f2dbde5a04ca?utm_source=chatgpt.com "South Korea's biggest defence group plans $2.5bn share sale to expand overseas"
[2]: https://www.reuters.com/world/asia-pacific/south-koreas-lf-says-value-battery-material-supply-deal-with-tesla-cut-7386-2025-12-29/?utm_source=chatgpt.com "South Korea's L&F slashes value of battery material supply deal with Tesla"
[3]: https://www.reuters.com/world/asia-pacific/skoreas-yoon-says-vast-amount-oil-gas-reserve-possible-off-east-coast-2024-06-03/?utm_source=chatgpt.com "South Korea's Yoon approves exploration of vast oil and gas prospects"
[4]: https://www.reuters.com/technology/skorean-tech-services-firm-lg-cns-falls-stock-market-debut-2025-02-05/?utm_source=chatgpt.com "South Korean tech services firm LG CNS drops in market debut"
[5]: https://www.ft.com/content/647fe2ef-9b01-4ab9-a93b-15b18f474563?utm_source=chatgpt.com "Samsung quashes activist proposals backed by Norway's oil fund"
[6]: https://www.reuters.com/sustainability/boards-policy-regulation/sk-telecom-shares-plunge-after-data-breach-due-cyberattack-2025-04-28/?utm_source=chatgpt.com "SK Telecom shares plunge after data breach due to cyberattack"
[7]: https://www.reuters.com/business/autos-transportation/hyundai-steels-6-bln-us-investment-draws-investor-ire-tests-seouls-tariff-2025-04-22/?utm_source=chatgpt.com "Hyundai Steel's $6 billion US investment draws investor ire, tests Seoul's tariff strategy"
[8]: https://www.reuters.com/markets/deals/private-equity-mbk-young-poong-launch-15-bln-tender-offer-korea-zinc-shares-2024-09-13/?utm_source=chatgpt.com "Private equity MBK, Young Poong launch $1.5 bln tender offer for Korea Zinc shares"
