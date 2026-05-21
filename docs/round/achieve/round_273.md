순서상 이번은 **R4 Loop 13 — 소재·스프레드·전략자원 가격경로 검증 라운드**다.

```text
round = R4 Loop 13
round_id = round_201
large_sector = MATERIALS_SPREAD_STRATEGIC_RESOURCES
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = false
next_round = R5 Loop 13
```

이번 R4 Loop 13은 기존 대표축인 단순 POSCO/MinRes·L&F·Korea Zinc critical minerals만 반복하지 않고, **Korea Zinc 지배권/희석, graphite·lithium price event, 철강 관세 양면성, Hyundai Steel 정책 CAPEX false positive, petrochemical 구조조정, Lotte Indonesia petrochemical capex, Poongsan 방산·구리 optionality**를 같이 봤다.

가장 큰 제한은 그대로다. 이번 환경에서 KRX/Naver/Yahoo/Stooq의 **수정주가 일봉 전체 구간**은 안정적으로 확보하지 못했다. 그래서 30D/90D/180D full OHLC는 임의로 만들지 않고, Reuters / WSJ / FT / MarketWatch가 보도한 **event price, event return, 계약·투자·정책금액, capacity, margin-risk anchor**만 계산했다. full OHLC가 필요한 칸은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R4 = 소재·스프레드·전략자원
```

R4에서 진짜 Stage 3는 “전략광물”, “구리”, “철강 관세”, “리튬”, “graphite”, “석유화학 구조조정”이라는 단어가 아니다.

진짜 Stage 3는 **제품 스프레드, 원가곡선, offtake, call-off, capacity utilization, working capital, FCF, governance/dilution risk, export-control risk**가 같이 닫히는 순간이다.

---

# 2. 대상 canonical archetype

```text
CRITICAL_MINERALS_CONTROL_PREMIUM_AND_DILUTION
GRAPHITE_LITHIUM_POLICY_PRICE_EVENT
STEEL_TARIFF_TWO_SIDED_RELIEF_RISK
POLICY_CAPEX_FALSE_POSITIVE
PETROCHEMICAL_CAPACITY_RESTRUCTURING
PETROCHEMICAL_OVERSEAS_CAPEX_SPREAD_GATE
DEFENSE_METALS_AMMUNITION_OPTIONALITY
COPPER_COMMODITY_OVERHEAT_4B
```

---

# 3. deep sub-archetype

```text
전략광물 / governance:
- Korea Zinc
- MBK / Young Poong tender offer
- U.S. Tennessee critical minerals refinery
- new share issuance / dilution / control battle

Graphite / lithium:
- POSCO Future M
- L&F read-through
- U.S. graphite anti-dumping tariff
- CATL lithium mine suspension
- price event vs actual material margin

철강:
- POSCO Holdings
- Hyundai Steel
- SeAH Steel
- Chinese steel plate anti-dumping relief
- U.S. 25% / 50% tariff export risk
- U.S. plant CAPEX false positive

석유화학:
- LG Chem
- Hanwha Solutions / DL Chemical / YNCC
- Lotte Chemical / HD Hyundai Chemical
- Lotte Indonesia naphtha cracker
- NCC shutdown / overcapacity / spread recovery

구리·방산금속:
- Poongsan
- copper products
- ammunition business
- Hanwha Aerospace acquisition rumor
- sale denial / event premium
```

---

# 4. 국장 신규 후보 case

## Case A — Korea Zinc `event premium + dilution/governance 4B-watch`

```text
symbol = 010130
case_type = success_candidate + overheat + 4B-watch
archetype = CRITICAL_MINERALS_CONTROL_PREMIUM_AND_DILUTION
```

### stage date

```text
Stage 1:
2024-09-13
- MBK Partners + Young Poong tender offer
- Korea Zinc control battle
- world’s largest refined-zinc producer
- nonferrous / strategic metals governance premium

Stage 2:
2024-09-13
- MBK tender offer about 2T won / $1.5B
- purchase price 660,000 won per share
- shares jump as much as +24% to record 690,000 won
- target controlling stake 47.74%

Stage 4B:
2024-09-13
- control premium moved price first
- record-high spike is not operating Stage 3

Stage 4B / governance watch:
2024-11-13
- Korea Zinc withdraws $1.8B share sale plan after investigation and selloff
- shares initially +6%, then -7% intraday

Stage 4B / dilution watch:
2025-12-16
- MBK / Young Poong seek injunction against new share sale for $7.4B Tennessee critical-minerals refinery
- Korea Zinc shares -13%

Stage 3:
없음
- tender offer / critical minerals plan / refinery plan are Stage 2
- offtake, margin, funding structure, dilution control, FCF 확인 전 Green 금지
```

Korea Zinc는 R4에서 가장 좋은 전략광물 후보이지만, 동시에 가장 좋은 4B-watch다. MBK tender offer 때 주가는 +24%로 690,000원 record high까지 갔고, 이후 share sale·dilution·지배권 분쟁이 반복되며 `strategic minerals`가 곧바로 Stage 3가 아니라는 점을 보여줬다. 2025년 Tennessee refinery 투자와 share sale 이슈에서는 주요 주주가 injunction을 신청했고, 주가는 -13% 하락했다. 즉 Korea Zinc는 **전략광물 Stage 2 + governance/dilution gate**로 둔다. ([월스트리트저널][1])

### 실제 가격경로 검증

```json
{
  "price_data_source": "WSJ / Reuters tender-offer, share-sale, injunction anchors",
  "stage3_price": null,
  "tender_offer_price_krw": 660000,
  "event_high_price_krw": 690000,
  "event_mfe_pct": 24,
  "tender_offer_value_krw_trn": 2.0,
  "tender_offer_value_usd_bn": 1.5,
  "target_controlling_stake_pct": 47.74,
  "withdrawn_share_sale_usd_bn": 1.8,
  "withdrawal_initial_mfe_pct": 6,
  "withdrawal_later_mae_pct": -7,
  "tennessee_refinery_project_usd_bn": 7.4,
  "injunction_event_mae_pct": -13,
  "mfe_30d_90d_180d_1y": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_4B_watch
rerating_result = critical_minerals_control_premium_watch
stage_failure_type = control_premium_and_dilution_not_operating_green
```

---

## Case B — POSCO Future M / graphite·lithium event `price_moved_without_evidence`

```text
symbol = 003670
case_type = event_premium + price_moved_without_evidence
archetype = GRAPHITE_LITHIUM_POLICY_PRICE_EVENT
```

### stage date

```text
Stage 1:
2025-07-18
- U.S. announces 93.5% anti-dumping tariff on Chinese graphite anode active materials
- non-China graphite / anode material supply-chain optionality
- POSCO Future M read-through

Stage 2:
2025-07-18
- POSCO Future M +20%
- Syrah +22%, Nouveau Monde +26%, Novonix +15%
- tariff raises total U.S. tariff rate on Chinese graphite to roughly 160%

Stage 4B:
2025-07-18
- policy/tariff headline moved price before confirmed non-China graphite contract or margin

Stage 4B 추가:
2025-08-11
- CATL suspends Yichun lithium mining project
- POSCO Future M +8.3%
- L&F +10%
- Samsung SDI +3.2%
- LGES +2.8%

Stage 3:
없음
- graphite/lithium price event is not Green
- actual non-China sourcing, customer certification, spread, margin, FCF 필요
```

POSCO Future M은 R4 전략자원/배터리소재 사이의 교차 case다. Graphite tariff와 CATL lithium mine suspension 때 각각 +20%, +8.3%가 나왔지만, 이건 아직 **price event**다. Tariff가 올라간다고 POSCO Future M의 non-China graphite sourcing, customer qualification, spread, margin이 자동으로 닫히지는 않는다. ([Financial Times][2])

### 실제 가격경로 검증

```json
{
  "price_data_source": "FT graphite-tariff anchor + WSJ CATL lithium event anchor",
  "stage3_price": null,
  "graphite_tariff_event_mfe_pct": 20,
  "us_antidumping_tariff_on_chinese_graphite_pct": 93.5,
  "approx_total_us_tariff_rate_on_chinese_graphite_pct": 160,
  "catl_lithium_event_mfe_pct": 8.3,
  "lnf_same_context_mfe_pct": 10,
  "samsung_sdi_same_context_mfe_pct": 3.2,
  "lges_same_context_mfe_pct": 2.8,
  "actual_graphite_supply_contract_confirmed": false,
  "margin_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = price_moved_without_evidence
rerating_result = graphite_lithium_policy_price_event
stage_failure_type = tariff_or_lithium_event_not_margin_green
```

---

## Case C — POSCO / Hyundai Steel / SeAH Steel `two-sided tariff case`

```text
symbols = 005490 / 004020 / 306200
case_type = event_premium + 4C-watch
archetype = STEEL_TARIFF_TWO_SIDED_RELIEF_RISK
```

### stage date

```text
Stage 1:
2025-02-10
- Trump 25% steel/aluminium tariff talk
- Korean steel export margin risk

Stage 4C-watch:
2025-02-10
- POSCO Holdings -3.6% to 230,500 won
- Hyundai Steel -2.9%
- KOSPI -0.5%

Stage 2 relief:
2025-02-20
- Korea provisionally imposes 27.91~38.02% anti-dumping tariffs on Chinese steel plates
- Hyundai Steel +5.8%
- POSCO Holdings +3.9%
- KOSPI -0.7%

Stage 4C-watch 강화:
2025-06-02
- U.S. tariff doubled to 50%
- POSCO / Hyundai Steel -3%
- SeAH Steel -8%

Stage 3:
없음
- domestic anti-dumping relief and U.S. export tariff risk coexist
- spread, export margin, domestic volume, FCF 확인 전 Green 금지
```

철강은 R4에서 가장 전형적인 양면 case다. 중국산 steel plate anti-dumping은 국내 철강에 relief를 줬지만, U.S. tariff는 export margin을 바로 때렸다. 같은 sector에서 2월 20일에는 Hyundai Steel +5.8%, POSCO +3.9%였고, 6월 2일 50% tariff 이벤트에서는 POSCO·Hyundai Steel -3%, SeAH Steel -8%였다. 국내 보호정책만 보고 Green을 주면 export-risk 4C를 놓친다. ([Reuters][3])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters steel tariff / anti-dumping event anchors",
  "stage3_price": null,
  "posco_25pct_tariff_event_low_krw": 230500,
  "posco_25pct_tariff_event_mae_pct": -3.6,
  "hyundai_steel_25pct_tariff_event_mae_pct": -2.9,
  "kospi_25pct_tariff_context_pct": -0.5,
  "korea_antidumping_tariff_pct": "27.91-38.02",
  "hyundai_steel_antidumping_mfe_pct": 5.8,
  "posco_antidumping_mfe_pct": 3.9,
  "kospi_antidumping_context_pct": -0.7,
  "hyundai_relative_outperformance_pp": 6.5,
  "posco_relative_outperformance_pp": 4.6,
  "us_50pct_tariff_posco_hyundai_mae_pct": -3.0,
  "seah_steel_50pct_tariff_mae_pct": -8.0,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_plus_thesis_break_watch
rerating_result = steel_tariff_two_sided_relief_risk
stage_failure_type = policy_relief_not_spread_FCF_green
```

---

## Case D — Hyundai Steel U.S. plant `false_positive_score`

```text
symbol = 004020
case_type = failed_rerating
archetype = POLICY_CAPEX_FALSE_POSITIVE
```

### stage date

```text
Stage 1:
2025-03-24
- Hyundai Motor Group announces U.S. investment package
- tariff hedge / U.S. localization / low-carbon steel story

Stage 2:
2025-03-25
- Hyundai Steel $5.8B Louisiana steel plant
- annual capacity 2.7M tonnes
- part of Hyundai Motor Group $21B U.S. package

Stage 4C-watch:
2025-04-22
- shares lost 21.2% since announcement
- POSCO -18.3%
- KOSPI -5.5%
- unclear funding details
- investors question long-term tariff benefit and financial viability

Stage 3:
없음
```

Hyundai Steel은 R4의 clean false positive다. “U.S. plant + tariff hedge + strategic localization”은 좋아 보였지만, funding detail과 ROI가 없었고, 주가는 발표 이후 -21.2%까지 밀렸다. KOSPI 대비 -15.7pp 언더퍼폼했다. ([Reuters][4])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters U.S. plant / investor backlash anchor",
  "stage3_price": null,
  "plant_investment_usd_bn": 5.8,
  "annual_capacity_mn_tonnes": 2.7,
  "group_us_investment_package_usd_bn": 21,
  "post_announcement_drawdown_pct": -21.2,
  "posco_same_period_pct": -18.3,
  "kospi_same_period_pct": -5.5,
  "relative_underperformance_vs_kospi_pp": -15.7,
  "funding_plan_status": "incomplete_at_event_stage",
  "mfe": "N/A",
  "mae_30d_90d": "reported_anchor_not_full_ohlc"
}
```

### alignment

```text
score_price_alignment = false_positive_score
rerating_result = policy_CAPEX_failed_rerating
stage_failure_type = CAPEX_without_funding_ROI_green
```

---

## Case E — LG Chem / Hanwha Solutions / DL Chemical / YNCC `petrochemical credit 4C-watch`

```text
symbols = 051910 / 009830 / DL Chemical exposure
case_type = 4C-watch
archetype = PETROCHEMICAL_CAPACITY_RESTRUCTURING
```

### stage date

```text
Stage 1:
2025-08-27
- Korea petrochemical sector overcapacity
- naphtha-cracking capacity cut pressure
- China/Middle East supply pressure

Stage 4C-watch:
2025-08-27
- ten companies agree to reduce NCC capacity by 2.7M~3.7M tpy
- about 25% of total capacity including Shaheen
- YNCC may shut one or two of three crackers
- YNCC debt-to-equity 249%
- No.3 cracker already shut in August

Stage 2 relief:
2025-12-19
- LG Chem submits restructuring plan
- DL Chemical and Hanwha Solutions submit YNCC-related plans
- details undisclosed

Stage 3:
없음
- restructuring plan is relief
- spread recovery, capacity shutdown, OPM, debt cleanup, FCF required
```

석유화학은 R4에서 hard 4C 후보에 가까운 credit/spread case다. YNCC debt-to-equity 249%, NCC capacity cut 25%, No.3 cracker shutdown은 단순 cycle 조정이 아니라 credit watch다. LG Chem과 Hanwha/DL이 계획을 냈지만, detail이 공개되지 않았으므로 Green이 아니라 relief다. ([Reuters][5])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters petrochemical overhaul / restructuring-plan anchors",
  "stage3_price": null,
  "capacity_cut_target_mn_tpy": "2.7-3.7",
  "capacity_cut_equivalent_pct": 25,
  "naphtha_feedstock_share_for_ethylene_pct": 82,
  "yncc_debt_to_equity_1h2025_pct": 249,
  "yncc_possible_shutdown": "one or two of three crackers",
  "yncc_no3_cracker_status": "shut in August 2025",
  "shaheen_new_supply_2026_mn_tpy": 1.8,
  "lg_chem_plan_status": "submitted; details undisclosed",
  "hanwha_dl_yncc_plan_status": "submitted; details undisclosed",
  "mfe_mae": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = petrochemical_credit_and_capacity_break_watch
stage_failure_type = restructuring_plan_not_spread_FCF_green
```

---

## Case F — Lotte Chemical / HD Hyundai Chemical `restructuring relief, not Green`

```text
symbols = 011170 / 267250 exposure
case_type = success_candidate_policy_relief
archetype = PETROCHEMICAL_CAPACITY_RESTRUCTURING
```

### stage date

```text
Stage 1:
2025-11-26
- HD Hyundai / Lotte Chemical submit plan to restructure petrochemical businesses
- Lotte Daesan spin-off / merge with HD Hyundai Chemical
- industry-wide 25% capacity cut target

Stage 2:
2026-02-24
- government approves first petrochemical restructuring project
- Daesan NCC 1.1M tpy shutdown for 3 years
- HD Hyundai Oilbank and Lotte Chemical each inject 600B won
- total capital increase 1.2T won
- government support package >2T won
- utility cost savings up to 115B won
- R&D funding 26B won

Stage 3:
없음
- shutdown/support package is crisis relief
- product spread, OPM, FCF, debt cleanup 확인 전 Green 금지
```

Lotte/HD Hyundai Chemical은 R4에서 구조조정 relief의 좋은 예다. Daesan NCC 110만 tpy shutdown, 1.2조 원 capital increase, 2조 원 이상 support package는 강한 Stage 2지만, 이건 **위기 완화**다. Stage 3는 spread와 FCF가 돌아오는 순간이다. ([Reuters][6])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters restructuring approval / plan anchors",
  "stage3_price": null,
  "daesan_ncc_shutdown_capacity_mn_tpy": 1.1,
  "shutdown_duration_years": 3,
  "capital_increase_krw_trn": 1.2,
  "each_parent_injection_krw_bn": 600,
  "government_support_package_krw_trn": 2.0,
  "utility_cost_savings_krw_bn": 115,
  "rnd_funding_krw_bn": 26,
  "lotte_daesan_capacity_mn_tpy": 1.1,
  "hd_hyundai_capacity_mn_tpy": 0.85,
  "combined_capacity_before_shutdown_mn_tpy": 1.95,
  "daesan_shutdown_share_of_combined_capacity_pct": 56.4,
  "mfe_mae": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_policy_relief
rerating_result = petrochemical_restructuring_relief
stage_failure_type = capacity_shutdown_support_not_green_until_spread_FCF
```

---

## Case G — Lotte Chemical Indonesia / Pakistan `overseas petrochemical portfolio reshuffle`

```text
symbol = 011170
case_type = success_candidate + 4B-watch
archetype = PETROCHEMICAL_OVERSEAS_CAPEX_SPREAD_GATE
```

### stage date

```text
Stage 1:
2025-11-06
- Lotte Chemical Indonesia Cilegon plant inauguration
- overseas petrochemical capacity / import-substitution story

Stage 2:
2025-11-06
- $4B petrochemical production facility in Indonesia
- 1M metric tons ethylene/year
- first new naphtha cracker in Indonesia in 30 years
- expected to reduce Indonesia ethylene imports by more than 90%

Stage 2 portfolio recycling:
2025-11-13
- Lotte sells 75% stake in Pakistan subsidiary for 98B won / $68.94M
- Pakistan plant produces 500,000 tons PTA annually
- part of portfolio restructuring under low demand / oversupply pressure

Stage 3:
없음
- overseas capex and asset sale are not Green
- ethylene spread, utilization, working capital, FCF, local demand needed
```

Lotte Chemical overseas case는 R4에서 애매하지만 중요하다. Indonesia $4B cracker는 import-substitution story가 강하지만, 국내 NCC가 과잉이면 해외 신공장도 spread gate를 통과해야 한다. 동시에 Pakistan PTA 지분 75% 매각은 portfolio recycling이지만, ROIC 개선이 확인되어야 한다. ([Reuters][7])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters Indonesia plant / Pakistan asset-sale anchors",
  "stage3_price": null,
  "indonesia_project_value_usd_bn": 4.0,
  "indonesia_ethylene_capacity_mn_tpy": 1.0,
  "indonesia_import_reduction_target_pct": 90,
  "pakistan_stake_sold_pct": 75,
  "pakistan_sale_value_krw_bn": 98,
  "pakistan_sale_value_usd_mn": 68.94,
  "pakistan_pta_capacity_tpy": 500000,
  "ethane_naphtha_spread_confirmed": false,
  "utilization_confirmed": false,
  "mfe_mae": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_but_insufficient_price_data
rerating_result = overseas_petrochemical_portfolio_watch
stage_failure_type = capex_asset_sale_not_spread_FCF_green
```

---

## Case H — Poongsan `defense-metals optionality, event premium`

```text
symbol = 103140
case_type = event_premium
archetype = DEFENSE_METALS_AMMUNITION_OPTIONALITY
```

### stage date

```text
Stage 1:
2026-04-03
- Hanwha Aerospace reportedly submits bid for Poongsan defense business
- estimated value 1.5T won / $1.1B
- Poongsan has copper products and ammunition business
- supplies small- and large-caliber rounds and missile warheads

Stage 2:
보류
- M&A rumor itself is not structural Green
- copper spread / ammunition orders / confirmed sale required

Stage 4B:
2026-04-09
- Hanwha drops acquisition review
- Poongsan says it is not pursuing ammunition business sale
- rumor premium should be removed

Stage 3:
없음
```

Poongsan은 구리·방산금속 optionality가 있지만, 이번 case는 오히려 **rumor is not Green** 교정용이다. Hanwha bid 보도 후 며칠 만에 Hanwha가 검토를 중단했고, Poongsan도 sale plan을 부인했다. 따라서 Poongsan을 R4 Green으로 보려면 M&A rumor가 아니라 copper spread, ammunition order, cash return, confirmed transaction이 필요하다. ([Reuters][8])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters M&A rumor / denial anchors",
  "stage3_price": null,
  "reported_deal_value_krw_trn": 1.5,
  "reported_deal_value_usd_bn": 1.1,
  "businesses": [
    "copper products",
    "ammunition manufacturing",
    "small-caliber rounds",
    "large-caliber shells",
    "missile warheads"
  ],
  "transaction_status": "not confirmed; Hanwha dropped review; Poongsan denied sale plan",
  "mfe_mae": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium
rerating_result = defense_metals_optional_watch
stage_failure_type = M&A_rumor_not_green
```

---

# 5. 이번 R4 case별 stage date 요약

| case                         | Stage 1    | Stage 2                         | Stage 3 | Stage 4B              | Stage 4C                  |
| ---------------------------- | ---------- | ------------------------------- | ------- | --------------------- | ------------------------- |
| Korea Zinc                   | 2024-09-13 | tender / refinery plan          | N/A     | 2024-09 / 2025-12     | dilution/governance watch |
| POSCO Future M               | 2025-07-18 | graphite tariff / lithium event | N/A     | +20%, +8.3% events    | N/A                       |
| POSCO / Hyundai / SeAH Steel | 2025-02-10 | 2025-02-20 relief               | N/A     | policy relief watch   | 25%/50% tariff watch      |
| Hyundai Steel U.S. plant     | 2025-03-24 | 2025-03-25                      | N/A     | N/A                   | 2025-04-22 watch          |
| LG Chem / YNCC               | 2025-08-27 | 2025-12-19 relief               | N/A     | N/A                   | credit/spread watch       |
| Lotte / HD Hyundai Chemical  | 2025-11-26 | 2026-02-24                      | N/A     | relief watch          | N/A                       |
| Lotte Indonesia/Pakistan     | 2025-11-06 | 2025-11-13                      | N/A     | portfolio/capex watch | spread watch              |
| Poongsan                     | 2026-04-03 | weak rumor                      | N/A     | 2026-04-09            | N/A                       |

---

# 6. 실제 가격경로 검증 총괄

| case                     |                                   anchor | MFE / MAE 해석                           | 판정                           |
| ------------------------ | ---------------------------------------: | -------------------------------------- | ---------------------------- |
| Korea Zinc               |             +24% to 690,000원, later -13% | control premium과 dilution risk가 동시에 작동 | 4B-watch                     |
| POSCO Future M           |             graphite +20%, lithium +8.3% | 정책·가격 event가 먼저 움직임                    | price_moved_without_evidence |
| Steel tariff basket      | relief +5.8%/+3.9%, tariff shock -3%/-8% | 양면 정책 case                             | event + 4C-watch             |
| Hyundai Steel U.S. plant |                -21.2% since announcement | policy CAPEX false positive            | false_positive_score         |
| LG Chem / YNCC           |               25% capacity cut, D/E 249% | credit/spread 4C-watch                 | thesis_break_watch           |
| Lotte / HD Hyundai       |           1.1M tpy shutdown, >2T support | relief not Green                       | policy relief                |
| Lotte overseas           |  $4B Indonesia capex, 98B won asset sale | utilization/spread 미확인                 | success_candidate            |
| Poongsan                 |                  1.5T won rumor → denied | M&A rumor 제거                           | event premium                |

---

# 7. score-price alignment 판정

```text
success_candidate:
- Korea Zinc, but only if dilution/governance and project economics clear
- Lotte Chemical Indonesia, but only if spread/utilization/FCF clear
- Lotte / HD Hyundai Chemical, but only as restructuring relief

false_positive_score:
- Hyundai Steel U.S. plant

event_premium:
- Korea Zinc tender offer
- POSCO Future M graphite/lithium event
- Poongsan M&A rumor
- Steel anti-dumping relief

price_moved_without_evidence:
- POSCO Future M +20% graphite tariff event before actual contract/margin
- Poongsan M&A rumor before confirmed transaction
- Korea Zinc control premium before operating cashflow

thesis_break_watch:
- Korea Zinc dilution/governance
- Steel U.S. tariff
- LG Chem / YNCC petrochemical credit stress
- Lotte/HD restructuring if spread recovery fails

hard_4C_confirmed:
- false
```

이번 R4 Loop 13에서는 hard 4C를 억지로 만들지 않는다. 대신 **Korea Zinc governance/dilution**, **Hyundai Steel policy CAPEX**, **steel tariff export shock**, **YNCC credit/spread stress**를 강한 4C-watch로 둔다.

---

# 8. 점수비중 교정

## 올릴 축

```text
product_spread_visibility +5
cost_curve_advantage +5
offtake_or_actual_contract +5
capacity_utilization +5
working_capital_control +5
FCF_after_restructuring +5
governance_dilution_control +5
export_control_resilience +5
commodity_price_pass_through +4
policy_relief_to_margin_bridge +4
```

### 왜 올리나

Korea Zinc는 전략광물 자체보다 governance와 dilution이 valuation을 흔들었다. POSCO Future M은 graphite/lithium event로 가격은 뛰었지만 actual contract/margin이 확인되지 않았다. Hyundai Steel은 CAPEX headline이 funding/ROI 없이 나오면 바로 실패한다. Petrochemical은 capacity shutdown과 support package가 있어도 spread/FCF가 돌아와야 한다.

## 내릴 축

```text
control_premium_only -5
M&A_rumor_only -5
tariff_relief_only -5
policy_CAPEX_without_ROI -5
commodity_price_event_only -5
restructuring_plan_undisclosed -4
capacity_shutdown_without_spread -4
dilution_or_governance_fight -5
export_tariff_exposure -5
```

### 왜 내리나

Korea Zinc tender premium은 operating Green이 아니다. Poongsan rumor는 며칠 만에 사라졌다. Graphite/lithium price event는 소재주를 올렸지만 margin evidence가 없다. Hyundai Steel은 tariff hedge CAPEX가 오히려 -21.2% false positive였다. Petrochemical restructuring은 relief이지 Green이 아니다.

## Green gate 강화 조건

```text
R4 Stage 3-Green 필수:
1. product spread 개선 확인
2. cost curve advantage 확인
3. actual offtake / contract / call-off 확인
4. capacity utilization 확인
5. working capital 안정
6. FCF 확인
7. governance / dilution risk 없음
8. export tariff / China restriction 통과
9. restructuring이면 capacity shutdown 이후 margin 회복 확인
10. price path가 evidence 이후 따라옴

금지:
control premium only
M&A rumor only
commodity price event only
tariff relief only
policy CAPEX only
restructuring plan only
capacity shutdown only
```

## 4B 조기감지 조건

```text
4B-watch:
tender offer / control premium으로 +20% 이상 급등
commodity tariff / lithium mine event로 +10~20% 급등
anti-dumping relief로 철강주 급등
policy CAPEX 발표 후 funding/ROI 없음
M&A rumor가 confirmed transaction 전 가격화
restructuring support package가 spread 전 가격화

4B-elevated:
dilution 가능성
governance fight
actual supply contract 없음
spread recovery 없음
CAPEX funding 불명
export tariff / China restriction 남음
```

## 4C hard gate 조건

```text
contract cancellation
dilutive issuance that destroys existing holders
export tariff destroying margin
China end-use restriction / sanction
commodity price collapse without hedge
petrochemical credit event / workout
capacity cut fails to restore spread
CAPEX funding failure
M&A denial after rumor-driven rally
```

---

# 9. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 10. 레포 반영용 patch-ready 출력

## docs/round/round_201.md 요약

```md
# R4 Loop 13. Materials / Spread / Strategic Resources Price Validation

이번 라운드는 R4 Loop 13 price-validation 라운드다.

핵심 결론:
- Korea Zinc is critical-minerals success_candidate plus governance/dilution 4B-watch. MBK tender offer sent shares +24% to 690,000 won; later share-sale/injunction events caused +6% to -7% reversal and -13% decline. Strategic minerals are Stage 2, not Green without offtake, margin, funding and dilution control.
- POSCO Future M is graphite/lithium policy-price event premium. U.S. graphite tariff drove POSCO Future M +20%, while CATL lithium suspension drove POSCO Future M +8.3% and L&F +10%. Actual contracts and margin are unconfirmed.
- Steel tariff case is two-sided. Domestic anti-dumping tariffs drove Hyundai Steel +5.8% and POSCO +3.9%, but U.S. 25%/50% tariff events drove POSCO -3.6%, Hyundai -2.9% to -3%, and SeAH Steel -8%.
- Hyundai Steel U.S. plant is policy CAPEX false positive. $5.8B Louisiana plant / 2.7M t capacity story led to -21.2% post-announcement drawdown versus KOSPI -5.5%.
- LG Chem / Hanwha Solutions / DL Chemical / YNCC is petrochemical credit/spread 4C-watch. Capacity cut target 2.7M~3.7M tpy, YNCC debt/equity 249%, No.3 cracker shut; submitted plans are not Green.
- Lotte / HD Hyundai Chemical restructuring is policy relief. 1.1M tpy Daesan NCC shutdown for three years, 1.2T won capital increase, >2T won support package. Spread/OPM/FCF required.
- Lotte Chemical overseas portfolio is success_candidate but spread-gated. Indonesia $4B cracker with 1M tpy ethylene capacity and Pakistan 75% stake sale for 98B won need utilization and ROIC proof.
- Poongsan is defense-metals optionality but event premium. 1.5T won defense-business sale rumor was denied after Hanwha stopped review. M&A rumor is not Green.
```

## docs/checkpoints/checkpoint_28a_round201_r4_loop13.md 요약

```md
# Checkpoint 28A Round 201 R4 Loop 13 Materials Spread Strategic Resources Price Validation

## 반영 내용
- R4 Loop 13 price-validation 라운드를 추가했다.
- Korea Zinc governance/dilution, POSCO Future M graphite/lithium event, steel tariff two-sided risk, Hyundai Steel policy CAPEX false positive, petrochemical restructuring, Lotte overseas portfolio, Poongsan defense-metals rumor를 비교했다.
- Reuters / WSJ / FT / MarketWatch anchors로 가능한 event MFE/MAE와 price/valuation/capacity metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- product spread visibility, cost curve, offtake/actual contract, capacity utilization, working capital, FCF after restructuring, governance/dilution control, export-control resilience 가중치 강화
- control premium-only, M&A rumor-only, tariff relief-only, policy CAPEX without ROI, commodity price event-only, restructuring plan undisclosed, capacity shutdown without spread 감점 강화
```

## data/e2r_case_library/cases_r4_loop13_round201.jsonl 초안

```jsonl
{"case_id":"r4_loop13_korea_zinc_control_premium_dilution_watch","symbol":"010130","company_name":"Korea Zinc","case_type":"success_candidate_4b_watch","primary_archetype":"CRITICAL_MINERALS_CONTROL_PREMIUM_AND_DILUTION","stage1_date":"2024-09-13","stage2_date":"2024-09-13/2025-12-16","stage4b_date":"2024-09-13/2024-11-13/2025-12-16","price_validation":{"price_data_source":"WSJ/Reuters tender-offer/share-sale/injunction anchors","stage3_price":null,"tender_offer_price_krw":660000,"event_high_price_krw":690000,"event_mfe_pct":24,"tender_offer_value_krw_trn":2.0,"tender_offer_value_usd_bn":1.5,"target_controlling_stake_pct":47.74,"withdrawn_share_sale_usd_bn":1.8,"withdrawal_initial_mfe_pct":6,"withdrawal_later_mae_pct":-7,"tennessee_refinery_project_usd_bn":7.4,"injunction_event_mae_pct":-13,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_4B_watch","rerating_result":"critical_minerals_control_premium_watch","notes":"Strategic minerals are Stage 2; dilution/governance and project economics must clear before Green."}
{"case_id":"r4_loop13_posco_futurem_graphite_lithium_event","symbol":"003670","company_name":"POSCO Future M","case_type":"event_premium","primary_archetype":"GRAPHITE_LITHIUM_POLICY_PRICE_EVENT","stage1_date":"2025-07-18","stage2_date":"2025-07-18/2025-08-11","stage4b_date":"2025-07-18/2025-08-11","price_validation":{"price_data_source":"FT graphite-tariff anchor + WSJ CATL lithium event anchor","stage3_price":null,"graphite_tariff_event_mfe_pct":20,"us_antidumping_tariff_on_chinese_graphite_pct":93.5,"approx_total_us_tariff_rate_on_chinese_graphite_pct":160,"catl_lithium_event_mfe_pct":8.3,"lnf_same_context_mfe_pct":10,"samsung_sdi_same_context_mfe_pct":3.2,"lges_same_context_mfe_pct":2.8,"actual_graphite_supply_contract_confirmed":false,"margin_confirmed":false,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"graphite_lithium_policy_price_event","notes":"Tariff/lithium events are not Green without non-China sourcing, customer certification, spread, margin and FCF."}
{"case_id":"r4_loop13_steel_tariff_two_sided_posco_hyundai_seah","symbol":"005490/004020/306200","company_name":"POSCO Holdings / Hyundai Steel / SeAH Steel","case_type":"event_premium_4c_watch","primary_archetype":"STEEL_TARIFF_TWO_SIDED_RELIEF_RISK","stage1_date":"2025-02-10","stage2_date":"2025-02-20","stage4c_date":"2025-02-10/2025-06-02_watch","price_validation":{"price_data_source":"Reuters steel tariff/anti-dumping event anchors","stage3_price":null,"posco_25pct_tariff_event_low_krw":230500,"posco_25pct_tariff_event_mae_pct":-3.6,"hyundai_steel_25pct_tariff_event_mae_pct":-2.9,"kospi_25pct_tariff_context_pct":-0.5,"korea_antidumping_tariff_pct":"27.91-38.02","hyundai_steel_antidumping_mfe_pct":5.8,"posco_antidumping_mfe_pct":3.9,"kospi_antidumping_context_pct":-0.7,"hyundai_relative_outperformance_pp":6.5,"posco_relative_outperformance_pp":4.6,"us_50pct_tariff_posco_hyundai_mae_pct":-3.0,"seah_steel_50pct_tariff_mae_pct":-8.0,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_plus_thesis_break_watch","rerating_result":"steel_tariff_two_sided_relief_risk","notes":"Domestic anti-dumping relief and export tariff risk coexist; spread/export margin required before Green."}
{"case_id":"r4_loop13_hyundai_steel_us_plant_policy_capex_false_positive","symbol":"004020","company_name":"Hyundai Steel","case_type":"failed_rerating","primary_archetype":"POLICY_CAPEX_FALSE_POSITIVE","stage2_date":"2025-03-25","stage4c_date":"2025-04-22_watch","price_validation":{"price_data_source":"Reuters U.S. plant/investor backlash anchor","stage3_price":null,"plant_investment_usd_bn":5.8,"annual_capacity_mn_tonnes":2.7,"group_us_investment_package_usd_bn":21,"post_announcement_drawdown_pct":-21.2,"posco_same_period_pct":-18.3,"kospi_same_period_pct":-5.5,"relative_underperformance_vs_kospi_pp":-15.7,"funding_plan_status":"incomplete_at_event_stage","price_validation_status":"reported_anchor_not_full_ohlc"},"score_price_alignment":"false_positive_score","rerating_result":"policy_CAPEX_failed_rerating","notes":"U.S. tariff hedge CAPEX failed because funding/ROI were unclear."}
{"case_id":"r4_loop13_lgchem_hanwha_dl_yncc_petchem_credit_watch","symbol":"051910/009830/DL_Chemical_exposure","company_name":"LG Chem / Hanwha Solutions / DL Chemical / YNCC","case_type":"4c_watch","primary_archetype":"PETROCHEMICAL_CAPACITY_RESTRUCTURING","stage4c_date":"2025-08-27_watch","stage2_date":"2025-12-19_relief","price_validation":{"price_data_source":"Reuters petrochemical overhaul/restructuring-plan anchors","stage3_price":null,"capacity_cut_target_mn_tpy":"2.7-3.7","capacity_cut_equivalent_pct":25,"naphtha_feedstock_share_for_ethylene_pct":82,"yncc_debt_to_equity_1h2025_pct":249,"yncc_possible_shutdown":"one or two of three crackers","yncc_no3_cracker_status":"shut in August 2025","shaheen_new_supply_2026_mn_tpy":1.8,"lg_chem_plan_status":"submitted; details undisclosed","hanwha_dl_yncc_plan_status":"submitted; details undisclosed","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"petrochemical_credit_and_capacity_break_watch","notes":"Restructuring-plan submission is relief only; spread, OPM, debt cleanup and FCF must confirm."}
{"case_id":"r4_loop13_lotte_hd_hyundai_petchem_restructuring_relief","symbol":"011170/267250_exposure","company_name":"Lotte Chemical / HD Hyundai Chemical","case_type":"success_candidate_policy_relief","primary_archetype":"PETROCHEMICAL_CAPACITY_RESTRUCTURING","stage1_date":"2025-11-26","stage2_date":"2026-02-24","price_validation":{"price_data_source":"Reuters restructuring approval/plan anchors","stage3_price":null,"daesan_ncc_shutdown_capacity_mn_tpy":1.1,"shutdown_duration_years":3,"capital_increase_krw_trn":1.2,"each_parent_injection_krw_bn":600,"government_support_package_krw_trn":2.0,"utility_cost_savings_krw_bn":115,"rnd_funding_krw_bn":26,"lotte_daesan_capacity_mn_tpy":1.1,"hd_hyundai_capacity_mn_tpy":0.85,"combined_capacity_before_shutdown_mn_tpy":1.95,"daesan_shutdown_share_of_combined_capacity_pct":56.4,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_policy_relief","rerating_result":"petrochemical_restructuring_relief","notes":"Shutdown and support package are crisis relief; product spread, OPM, FCF and debt cleanup required."}
{"case_id":"r4_loop13_lotte_chemical_overseas_portfolio_spread_gate","symbol":"011170","company_name":"Lotte Chemical","case_type":"success_candidate","primary_archetype":"PETROCHEMICAL_OVERSEAS_CAPEX_SPREAD_GATE","stage2_date":"2025-11-06/2025-11-13","price_validation":{"price_data_source":"Reuters Indonesia plant/Pakistan asset-sale anchors","stage3_price":null,"indonesia_project_value_usd_bn":4.0,"indonesia_ethylene_capacity_mn_tpy":1.0,"indonesia_import_reduction_target_pct":90,"pakistan_stake_sold_pct":75,"pakistan_sale_value_krw_bn":98,"pakistan_sale_value_usd_mn":68.94,"pakistan_pta_capacity_tpy":500000,"ethane_naphtha_spread_confirmed":false,"utilization_confirmed":false,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_insufficient_price_data","rerating_result":"overseas_petrochemical_portfolio_watch","notes":"Overseas capex and asset sale are not Green without utilization, spread, ROIC and FCF."}
{"case_id":"r4_loop13_poongsan_defense_metals_mna_rumor","symbol":"103140","company_name":"Poongsan","case_type":"event_premium","primary_archetype":"DEFENSE_METALS_AMMUNITION_OPTIONALITY","stage1_date":"2026-04-03","stage4b_date":"2026-04-09","price_validation":{"price_data_source":"Reuters M&A rumor/denial anchors","stage3_price":null,"reported_deal_value_krw_trn":1.5,"reported_deal_value_usd_bn":1.1,"businesses":["copper products","ammunition manufacturing","small-caliber rounds","large-caliber shells","missile warheads"],"transaction_status":"not confirmed; Hanwha dropped review; Poongsan denied sale plan","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium","rerating_result":"defense_metals_optional_watch","notes":"M&A rumor is not Green; copper spread, ammunition order, confirmed transaction or cash return required."}
```

## data/sector_taxonomy/score_weight_profiles_round201_r4_loop13_v1.csv 초안

```csv
archetype,product_spread_visibility,cost_curve_advantage,offtake_actual_contract,capacity_utilization,working_capital_control,fcf_after_restructuring,governance_dilution_control,export_control_resilience,commodity_price_pass_through,policy_relief_to_margin_bridge,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
CRITICAL_MINERALS_CONTROL_PREMIUM_AND_DILUTION,+4,+5,+5,+4,+5,+5,+5,+5,+3,+3,-5,+5,+5,Korea Zinc needs offtake/margin/funding/dilution control beyond control premium.
GRAPHITE_LITHIUM_POLICY_PRICE_EVENT,+5,+4,+5,+5,+4,+5,+3,+5,+5,+3,-5,+5,+4,POSCO Future M graphite/lithium events need supply contract and margin proof.
STEEL_TARIFF_TWO_SIDED_RELIEF_RISK,+5,+5,+3,+4,+4,+5,+2,+5,+4,+4,-5,+5,+5,Domestic tariff relief and export tariff risk must be scored together.
POLICY_CAPEX_FALSE_POSITIVE,+3,+3,+2,+4,+5,+5,+3,+4,+2,+2,-5,+5,+5,Hyundai Steel U.S. CAPEX failed without funding/ROI clarity.
PETROCHEMICAL_CAPACITY_RESTRUCTURING,+5,+4,+2,+5,+5,+5,+3,+2,+4,+5,-4,+5,+5,NCC shutdown/support package is relief until spread/OPM/FCF recover.
PETROCHEMICAL_OVERSEAS_CAPEX_SPREAD_GATE,+5,+4,+3,+5,+5,+5,+3,+3,+4,+3,-4,+4,+4,Lotte overseas capex/asset sale requires utilization, ROIC and spread.
DEFENSE_METALS_AMMUNITION_OPTIONALITY,+4,+4,+5,+4,+4,+5,+3,+4,+4,+2,-5,+5,+4,Poongsan M&A rumor is event premium until confirmed order/transaction/cash return.
COPPER_COMMODITY_OVERHEAT_4B,+5,+4,+3,+3,+4,+4,+2,+3,+5,+2,-5,+5,+4,Copper/metal price rallies need pass-through, demand and FCF confirmation.
```

---

# 이번 R4 Loop 13 결론

```text
1. Korea Zinc는 strategic minerals success_candidate지만, 지금 점수상 핵심은 governance/dilution gate다.
   control premium +24%, injunction -13%가 모두 가격경로로 확인됐다.

2. POSCO Future M은 graphite/lithium price event premium이다.
   +20%, +8.3%는 컸지만 actual contract/margin 전에는 Green 금지다.

3. 철강은 domestic relief와 export 4C가 동시에 붙는다.
   Hyundai Steel +5.8%, POSCO +3.9% relief 뒤, U.S. tariff에서는 POSCO/Hyundai -3%, SeAH -8%가 나왔다.

4. Hyundai Steel U.S. plant는 policy CAPEX false positive다.
   -21.2% drawdown은 funding/ROI 없는 CAPEX headline의 위험을 보여준다.

5. LG Chem / Hanwha / DL / YNCC는 petrochemical credit/spread 4C-watch다.
   YNCC D/E 249%, capacity cut 25%는 Green이 아니라 hard gate 후보다.

6. Lotte / HD Hyundai restructuring은 relief다.
   Daesan shutdown과 2T won support package가 있어도 spread/FCF 전에는 Stage 3가 아니다.

7. Lotte Chemical overseas capex는 success_candidate지만 spread-gated다.
   Indonesia $4B cracker와 Pakistan asset sale 모두 utilization/ROIC가 필요하다.

8. Poongsan은 defense-metals optionality가 있지만 M&A rumor는 Green이 아니다.
   Hanwha review가 중단되고 Poongsan이 sale plan을 부인했다.
```

한 문장으로 압축하면:

> **R4에서 진짜 Stage 3는 “전략광물·graphite·lithium·철강관세·석유화학 구조조정·방산금속이 뜬다”가 아니라, 제품 스프레드·offtake·capacity utilization·working capital·FCF가 실제로 닫히고 governance·dilution·export-control·credit risk를 통과하는 순간이다.**

* [월스트리트저널](https://www.wsj.com/world/asia/korea-zinc-shares-hit-record-high-after-mbks-1-5-billion-tender-offer-ff915b9b?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/mbk-youngpoong-seek-court-injunction-block-korea-zincs-share-sale-plan-2025-12-16/?utm_source=chatgpt.com)
* [Financial Times](https://www.ft.com/content/d76f744c-cc19-4aaf-9aa5-69c7b92e2cc4?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/markets/asia/south-korea-provisionally-slaps-tariffs-chinese-steel-plates-dumping-2025-02-20/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/south-korea-minimise-impact-50-tariff-steel-products-ministry-says-2025-06-02/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/autos-transportation/hyundai-steels-6-bln-us-investment-draws-investor-ire-tests-seouls-tariff-2025-04-22/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/energy/south-korea-petrochemical-overhaul-likely-shut-small-stand-alone-naphtha-2025-08-27/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/south-korea-approves-first-petrochemical-restructuring-deal-supply-glut-weighs-2026-02-24/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/hanwha-seeks-buy-poongsans-ammunition-business-about-11-billion-newspaper-says-2026-04-03/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/hanwha-aerospace-drops-plan-acquire-poongsans-defence-unit-2026-04-09/?utm_source=chatgpt.com)

[1]: https://www.wsj.com/world/asia/korea-zinc-shares-hit-record-high-after-mbks-1-5-billion-tender-offer-ff915b9b?utm_source=chatgpt.com "Korea Zinc Shares Hit Record High After MBK's $1.5 Billion Tender Offer"
[2]: https://www.ft.com/content/d76f744c-cc19-4aaf-9aa5-69c7b92e2cc4?utm_source=chatgpt.com "Shares in non-Chinese graphite producers rally after US unveils 93.5% tariff"
[3]: https://www.reuters.com/markets/asia/shares-south-korean-steelmakers-drop-trump-talks-tariffs-2025-02-10/?utm_source=chatgpt.com "Shares of South Korean steelmakers drop as Trump talks tariffs"
[4]: https://www.reuters.com/business/autos-transportation/hyundai-steels-6-bln-us-investment-draws-investor-ire-tests-seouls-tariff-2025-04-22/?utm_source=chatgpt.com "Hyundai Steel's $6 billion US investment draws investor ire, tests Seoul's tariff strategy"
[5]: https://www.reuters.com/business/energy/south-korea-petrochemical-overhaul-likely-shut-small-stand-alone-naphtha-2025-08-27/?utm_source=chatgpt.com "South Korea petrochemical overhaul likely to shut small, stand-alone naphtha crackers"
[6]: https://www.reuters.com/world/asia-pacific/south-koreas-hd-hyundai-lotte-chemical-submit-plan-restructure-petrochemical-2025-11-26/?utm_source=chatgpt.com "South Korea's HD Hyundai, Lotte Chemical submit plan to restructure petrochemical businesses"
[7]: https://www.reuters.com/business/energy/indonesia-president-inaugurates-4-billion-petrochemical-plant-by-lotte-chemical-2025-11-06/?utm_source=chatgpt.com "Indonesia president inaugurates $4 billion petrochemical plant by Lotte Chemical"
[8]: https://www.reuters.com/world/asia-pacific/hanwha-seeks-buy-poongsans-ammunition-business-about-11-billion-newspaper-says-2026-04-03/?utm_source=chatgpt.com "Hanwha seeks to buy Poongsan's ammunition business for about $1.1 billion, newspaper says"
