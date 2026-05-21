순서상 이번은 **R3 Loop 13 — 2차전지·전기차·친환경 가격경로 검증 라운드**다.

```text
round = R3 Loop 13
round_id = round_200
large_sector = BATTERY_EV_GREEN
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true
next_round = R4 Loop 13
```

이번 R3 Loop 13은 이전 R3의 LGES/Ford·Samsung SDI/StarPlus·SK On/Ford JV를 반복하지 않고, **L&F/Tesla 4680 계약 붕괴, LGES LFP ESS 긍정계약과 IRA 의존성, Samsung SDI ESS 보도 미확정, LG Chem의 LGES 지분매각, EcoPro Materials precursor overheat, Aricell/S-Connect 배터리 안전 hard reference, graphite/FEOC 정책 relief**를 중심으로 본다.

이번에도 KRX/Naver/Yahoo/Stooq의 **수정주가 일봉 전체 구간**은 안정적으로 확보하지 못했다. 그래서 30D/90D/180D full OHLC는 임의로 만들지 않고, Reuters / WSJ / FT / MarketWatch가 제공한 **event price, event return, 계약금액, 취소금액, 매출비율, 정책금액**만 계산했다. full OHLC가 필요한 칸은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R3 = 2차전지·전기차·친환경
```

R3에서 진짜 Stage 3는 “2차전지”, “ESS”, “LFP”, “Tesla”, “IRA”, “폐배터리”, “탈중국”이라는 단어가 아니다.

진짜 Stage 3는 **실제 call-off, GWh volume, 납품 개시, utilization, IRA 제외 OP, margin, FCF, 안전·품질·정책 리스크 통과**가 확인되는 순간이다.

---

# 2. 대상 canonical archetype

```text
EV_BATTERY_MATERIAL_CONTRACT_COLLAPSE
ESS_LFP_CONTRACT_STAGE2_NOT_GREEN
IRA_SUBSIDY_DEPENDENCE_QUALITY_GATE
BATTERY_PARENT_CAPITAL_RECYCLING
ESS_REPORT_UNCONFIRMED_EVENT_PREMIUM
PRECURSOR_IPO_OVERHEAT_DEMAND_BREAK
BATTERY_SAFETY_HARD_REFERENCE
FEOC_GRAPHITE_POLICY_RELIEF_NOT_GREEN
```

---

# 3. deep sub-archetype

```text
양극재 / 소재 계약:
- L&F / Tesla 4680 high-nickel cathode deal
- initial $2.9B projection → $7,386 residual value
- Tesla 4680 production-yield issue, Cybertruck weakness, EV demand slowdown

ESS / LFP:
- LGES / Tesla LFP ESS supply
- $4.3B contract, 2027~2030
- option to extend up to 7 years
- U.S. factories, ESS pivot
- not Green until volume, margin, utilization, IRA-ex-credit OP clear

IRA / subsidy quality:
- LGES Q2 2025 OP doubled
- but ex-IRA tax credit OP only 1.4B won
- shares -2.3%
- subsidy-adjusted OP gate

자본배분:
- LG Chem sells 2T won worth of LGES shares
- price return swap
- loans for battery materials / biotech
- stake falls 2.5pp to 79.4%

Samsung SDI ESS:
- reported Tesla ESS deal >3T won / $2.11B
- Samsung SDI says nothing decided
- event premium, not Green

Precursor / EcoPro Materials:
- cathode precursor IPO / weak EV demand
- EcoPro Materials -11% to 119,200 won
- precursor demand shock / vertical-integration overheat

배터리 안전:
- Aricell Hwaseong lithium battery fire
- 23 deaths
- quality failures and temporary-worker safety failure
- S-Connect, Aricell majority stakeholder, reportedly -23%
- CEO sentenced 15 years

정책 / FEOC:
- China graphite dominance
- Korea warns IRA subsidy regime may collapse without graphite flexibility
- Korea announces 9.7T won / $7.14B battery supply-chain support
- policy relief, not company Green
```

---

# 4. 국장 신규 후보 case

## Case A — L&F / Tesla 4680 cathode `hard 4C`

```text
symbol = 066970
case_type = 4C-thesis-break
archetype = EV_BATTERY_MATERIAL_CONTRACT_COLLAPSE
```

### stage date

```text
Stage 1:
2023-02
- L&F signs high-nickel cathode materials supply deal with Tesla and affiliates
- expected supply period January 2024 ~ December 2025
- planned for Tesla 4680 cells

Stage 2:
2023-02
- initial contract projection $2.9B
- Tesla 4680 / affordable EV / Cybertruck production ramp expectation

Stage 4C:
2025-12-29
- contract value reduced from $2.9B to $7,386
- Tesla 4680 production-yield issue
- Cybertruck demand disappointment
- EV demand slowdown
- analyst: battery-sector anxiety

Stage 3:
없음
- initial contract headline failed actual call-off
```

L&F는 이번 R3 Loop 13의 가장 깨끗한 소재 hard 4C다. 2023년 Tesla cathode deal은 $2.9B로 기대됐지만, 2025년 12월 계약가치가 $7,386으로 줄었다고 Reuters가 보도했다. Tesla 4680 생산수율 문제, EV 수요 둔화, Cybertruck 부진이 배경으로 제시됐다. 즉 “Tesla 고객명 + 계약금액”만으로 Stage 3를 주면 안 된다. 실제 call-off와 납품량이 없으면 계약은 종이에서 먼지로 바뀐다. ([Reuters][1])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters contract-collapse anchor",
  "entry_date": "N/A",
  "stage3_price": null,
  "initial_contract_projection_usd_bn": 2.9,
  "revised_contract_value_usd": 7386,
  "contract_value_collapse_pct": -99.9997,
  "supply_period": "2024-01 to 2025-12",
  "application": "Tesla 4680 high-nickel cathode materials",
  "risk_causes": [
    "4680 production yield issue",
    "EV demand slowdown",
    "Cybertruck demand weakness"
  ],
  "mfe": "N/A",
  "mae_30d_90d_180d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = EV_battery_material_contract_quality_failure
stage_failure_type = hard_4C
```

---

## Case B — LG Energy Solution / Tesla LFP ESS `success_candidate + not Green`

```text
symbol = 373220
case_type = success_candidate
archetype = ESS_LFP_CONTRACT_STAGE2_NOT_GREEN
```

### stage date

```text
Stage 1:
2025-07-25
- LGES warns EV demand may slow due U.S. tariff and EV subsidy end
- company plans to boost ESS battery production and delay/cut some investments

Stage 2:
2025-07-30
- LGES signs $4.3B LFP battery supply contract
- WSJ reports customer is Tesla
- contract period August 2027 ~ July 2030
- option to extend up to 7 years and increase volume
- batteries expected for Tesla ESS
- LGES shares +0.6% after announcement

Stage 3:
없음
- contract is Stage 2
- actual GWh volume, shipment, utilization, margin, ex-IRA OP, FCF 확인 필요

Stage 4B:
계약 headline로 ESS pivot premium이 먼저 커지면 watch
```

LGES/Tesla LFP ESS 계약은 R3에서 좋은 Stage 2다. EV 수요 둔화를 ESS로 hedge하는 방향은 맞다. 다만 Reuters는 LGES가 고객명을 공개하지 않았고, WSJ는 Tesla라고 보도했으며, 계약은 2027년 8월부터 2030년 7월까지다. 주가는 발표 후 0.6% 상승에 그쳤다. 이건 “좋은 계약”이지 아직 Stage 3가 아니다. GWh, 생산라인 utilization, margin, IRA 제외 OP가 확인되어야 한다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters / WSJ contract and event-return anchors",
  "stage3_price": null,
  "contract_value_usd_bn": 4.3,
  "customer": "Tesla reported by WSJ; not identified by LGES due confidentiality",
  "contract_period": "2027-08 to 2030-07",
  "extension_option_years": 7,
  "use_case": "ESS LFP batteries",
  "event_mfe_pct": 0.6,
  "actual_gwh_volume": "not_disclosed",
  "margin": "not_disclosed",
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = ESS_LFP_contract_stage2
stage_failure_type = contract_without_volume_margin_green
```

---

## Case C — LGES Q2 2025 IRA dependence `evidence_good_but_quality_gate_failed`

```text
symbol = 373220
case_type = evidence_good_but_quality_gate_failed
archetype = IRA_SUBSIDY_DEPENDENCE_QUALITY_GATE
```

### stage date

```text
Stage 1:
2025-07-25
- LGES Q2 OP more than doubled
- U.S. production tax credit and customer stockpiling supported earnings
- EV subsidy end / tariff risk ahead

Stage 2:
2025-07-25
- Q2 OP 492B won vs 195B won YoY
- but ex-IRA tax credit OP only 1.4B won
- shares -2.3%
- CFO warns U.S. tariffs and EV subsidy end could slow North America EV growth

Stage 3:
없음
- headline OP beat is not Green if ex-subsidy OP quality is weak

Stage 4B / 4C-watch:
subsidy-quality adjustment required
```

LGES Q2 2025는 “좋은 실적처럼 보여도 quality gate를 통과해야 한다”는 case다. 영업이익은 4,920억 원으로 전년 1,950억 원보다 두 배 이상 증가했지만, IRA tax credit을 제외하면 영업이익은 14억 원에 불과했다. 그래서 주가는 실적 발표 후 -2.3%였다. 이건 R3 scoring에서 **headline OP가 아니라 ex-subsidy OP**를 봐야 한다는 증거다. ([Reuters][3])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters earnings and subsidy-quality anchor",
  "stage3_price": null,
  "q2_2025_op_krw_bn": 492,
  "q2_2024_op_krw_bn": 195,
  "op_growth_pct": 152.3,
  "ex_ira_tax_credit_op_krw_bn": 1.4,
  "ex_ira_share_of_reported_op_pct": 0.28,
  "event_mae_pct": -2.3,
  "risk": [
    "U.S. tariffs",
    "early end of federal EV subsidy",
    "EV demand slowdown"
  ],
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed
rerating_result = subsidy_adjusted_OP_quality_gate
stage_failure_type = headline_profit_not_green
```

---

## Case D — LG Chem / LGES stake sale `capital recycling + dilution/value-gap watch`

```text
symbol = 051910
case_type = failed_rerating_watch
archetype = BATTERY_PARENT_CAPITAL_RECYCLING
```

### stage date

```text
Stage 1:
2025-10-01
- LG Chem needs balance-sheet repair
- new business loans related to battery materials and biotech
- parent-subsidiary value gap / LGES stake monetization

Stage 2:
2025-10-01
- LG Chem to sell 2T won / $1.43B worth of LGES shares
- transaction via price return swap
- proceeds used to reduce loans for battery materials and biotech
- LG Chem stake in LGES falls by 2.5pp to 79.4%

Stage 3:
없음
- stake sale is not Green
- debt reduction, ROIC, battery-material order/margin, shareholder return 확인 필요

Stage 4B:
parent value-up 기대가 자본재활용보다 먼저 가격화되면 watch

Stage 4C:
forced sale perception, LGES valuation decline, battery-material capex ROI miss
```

LG Chem의 LGES 지분매각은 “배터리 value unlock”이 아니라 우선 **balance sheet / capital recycling**으로 봐야 한다. 2조 원 규모 지분을 price return swap으로 매각하고, proceeds는 battery materials와 biotech 신사업 관련 대출을 줄이는 데 쓰인다. 지분율은 2.5pp 낮아져 79.4%가 된다. Green은 매각 자체가 아니라 debt reduction, ROIC, shareholder return, battery-material margin으로 확인해야 한다. ([Reuters][4])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters stake-sale anchor",
  "stage3_price": null,
  "stake_sale_krw_trn": 2.0,
  "stake_sale_usd_bn": 1.43,
  "transaction_method": "price return swap",
  "stake_reduction_pp": 2.5,
  "post_sale_lges_stake_pct": 79.4,
  "use_of_proceeds": "reduce loans used for battery materials and biotech",
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_capital_recycling_watch
rerating_result = parent_battery_value_recycling_stage2
stage_failure_type = stake_sale_not_roic_green
```

---

## Case E — Samsung SDI / reported Tesla ESS deal `event premium, not Green`

```text
symbol = 006400
case_type = event_premium
archetype = ESS_REPORT_UNCONFIRMED_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2025-11-03
- Korea Economic Daily reports Samsung SDI reached agreement with Tesla
- ESS battery supply over three years
- EV demand slowdown makes ESS pivot attractive

Stage 2:
2025-11-03
- reported value more than 3T won / $2.11B
- three-year ESS supply
- Tesla did not comment
- Samsung SDI says nothing had been decided yet

Stage 3:
없음
- press report / unnamed source / company says not decided
- no signed final contract, no GWh, no margin

Stage 4B:
Tesla ESS headline로 price가 먼저 움직이면 watch
```

Samsung SDI/Tesla ESS 보도는 event premium이다. Reuters는 Korea Economic Daily를 인용해 3조 원 이상, 약 $2.11B 규모 ESS battery supply agreement를 보도했지만, Samsung SDI는 “아직 결정된 것이 없다”고 했고 Tesla도 comment하지 않았다. 이런 case는 Stage 2도 아주 약하게만 주고, Stage 3는 절대 금지다. ([Reuters][5])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters report-based anchor",
  "stage3_price": null,
  "reported_contract_value_krw_trn": 3.0,
  "reported_contract_value_usd_bn": 2.11,
  "reported_supply_period_years": 3,
  "customer": "Tesla, per Korea Economic Daily report",
  "company_confirmation": "Samsung SDI said nothing had been decided",
  "tesla_comment": "no immediate comment",
  "actual_signed_contract": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium
rerating_result = ESS_headline_unconfirmed_watch
stage_failure_type = report_not_contract
```

---

## Case F — EcoPro Materials `failed_rerating / precursor demand break`

```text
symbol = 450080
case_type = failed_rerating
archetype = PRECURSOR_IPO_OVERHEAT_DEMAND_BREAK
```

### stage date

```text
Stage 1:
2023-11
- EcoPro Materials IPO
- cathode precursor vertical-integration story
- EV battery material supply-chain localization

Stage 2:
2023 IPO context
- raised about 419B won
- priced lower / reduced share count due weak EV demand
- precursor expansion narrative

Stage 4C-watch:
2024-06-14
- EcoPro Materials shares -11% to 119,200 won
- battery material names under pressure
- EV demand / mineral-price / precursor cycle weakness

Stage 3:
없음
- IPO and vertical integration are not Green
- customer order, utilization, margin, FCF required
```

EcoPro Materials는 precursor vertical-integration narrative가 강했지만, IPO itself가 Green은 아니었다. MarketWatch는 2024년 6월 14일 EcoPro Materials가 -11% 하락해 119,200원에 거래됐다고 보도했다. 별도 공개 자료에 따르면 IPO는 약 4,190억 원을 조달했지만 EV 수요 약화 때문에 공모 구조와 가격에서 부담이 있었다. R3에서 precursor는 “공급망 국산화”보다 utilization과 margin이 먼저다. ([마켓워치][6])

### 실제 가격경로 검증

```json
{
  "price_data_source": "MarketWatch price anchor + company profile/IPO context",
  "stage3_price": null,
  "event_date": "2024-06-14",
  "event_price_krw": 119200,
  "event_mae_pct": -11,
  "implied_pre_event_price_krw": 133933,
  "ipo_raise_krw_bn": 419,
  "business": "cathode precursor materials",
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = failed_rerating
rerating_result = precursor_vertical_integration_overheat
stage_failure_type = IPO_story_without_demand_margin
```

---

## Case G — Aricell / S-Connect battery safety `hard 4C reference`

```text
symbols = S-Connect read-through / lithium battery safety basket
case_type = hard_4C_reference
archetype = BATTERY_SAFETY_HARD_REFERENCE
```

### stage date

```text
Stage 1:
2024-06-24
- Hwaseong lithium battery factory fire
- Aricell plant
- lithium primary battery production / military and sensor use

Stage 4C:
2024-06-24
- 23 workers killed
- FT: S-Connect, Aricell majority stakeholder, shares -23%
- warehouse contained about 35,000 battery units
- 19 foreign nationals among initial dead report

Stage 4C validation:
2024-08-23
- police blame quality failures
- company hurried to meet production deadline
- failed quality inspection / temporary workers / inadequate escape training

Stage 4C legal validation:
2025-09-23
- Aricell CEO sentenced to 15 years
- son/senior executive also sentenced 15 years
- toughest ruling over industrial accident under Korea safety law
```

Aricell fire는 R3에서 battery safety hard reference다. 직접 대형 KRX battery maker는 아니지만, 배터리업의 **품질·안전·임시직 교육·생산기한 압박**이 어떻게 hard gate가 되는지 보여준다. FT는 S-Connect, Aricell majority stakeholder, shares -23%라고 보도했고, Reuters는 이후 CEO가 15년형을 받았다고 보도했다. ([Financial Times][7])

### 실제 가격경로 검증

```json
{
  "price_data_source": "FT / Reuters safety and legal anchors",
  "stage3_price": null,
  "fatalities": 23,
  "injured_context": "multiple; FT initial report included injured and missing",
  "battery_units_in_warehouse": 35000,
  "s_connect_reported_mae_pct": -23,
  "ceo_sentence_years": 15,
  "son_executive_sentence_years": 15,
  "police_cause_context": [
    "quality failures",
    "rush to meet production deadline",
    "temporary workers",
    "inadequate emergency escape training"
  ],
  "mfe": "N/A",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = battery_safety_quality_hard_reference
stage_failure_type = hard_4C_reference
```

---

## Case H — Korea graphite / FEOC battery policy `policy relief, not Green`

```text
symbols = battery supply-chain basket
case_type = success_candidate_policy_relief
archetype = FEOC_GRAPHITE_POLICY_RELIEF_NOT_GREEN
```

### stage date

```text
Stage 1:
2024-04-26
- Korea warns China graphite dominance risks IRA subsidy collapse
- China controls >99% battery-grade graphite and 69% synthetic graphite
- FEOC rules threaten EV tax-credit eligibility

Stage 2:
2024-05-08
- Korea announces 9.7T won / $7.14B battery supply-chain support
- cheaper state loans and tax incentives
- source critical minerals from U.S. and FTA partners
- support lithium-metal / graphite alternatives
- U.S. grants temporary flexibility for Chinese graphite until 2026/2027 transition

Stage 3:
없음
- policy support is not company Green
- actual supply contracts, non-China graphite, customer certification, margin needed

Stage 4B:
탈중국 정책만으로 소재주가 먼저 움직이면 watch
```

FEOC/graphite 정책은 R3 전체에 필요한 Stage 2 relief다. FT는 중국이 battery-grade graphite 99% 이상, synthetic graphite 69%를 지배한다고 보도했고, 한국은 IRA subsidy regime collapse 가능성을 경고했다. 이후 WSJ는 한국이 9.7조 원, 약 $7.14B 지원책을 내놨다고 보도했다. 하지만 정책은 Green이 아니다. 실제 non-China sourcing, 고객 인증, 원가·마진이 확인되어야 한다. ([Financial Times][8])

### 실제 가격경로 검증

```json
{
  "price_data_source": "FT / WSJ policy anchors",
  "stage3_price": null,
  "china_battery_grade_graphite_share_pct": 99,
  "china_synthetic_graphite_share_pct": 69,
  "korea_support_package_krw_trn": 9.7,
  "korea_support_package_usd_bn": 7.14,
  "policy_tools": [
    "cheap state loans",
    "tax incentives",
    "critical minerals sourcing support",
    "lithium-metal / graphite alternatives"
  ],
  "company_level_contracts_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_policy_relief
rerating_result = FEOC_graphite_supply_chain_relief
stage_failure_type = policy_not_supply_margin_green
```

---

# 5. 이번 R3 case별 stage date 요약

| case                   | Stage 1    | Stage 2       | Stage 3 | Stage 4B              | Stage 4C                  |
| ---------------------- | ---------- | ------------- | ------- | --------------------- | ------------------------- |
| L&F / Tesla            | 2023-02    | 2023 contract | N/A     | N/A                   | 2025-12-29 hard           |
| LGES / Tesla LFP ESS   | 2025-07-25 | 2025-07-30    | N/A     | watch                 | N/A                       |
| LGES IRA dependence    | 2025-07-25 | 2025-07-25    | N/A     | subsidy-quality watch | quality gate              |
| LG Chem stake sale     | 2025-10-01 | 2025-10-01    | N/A     | watch                 | N/A                       |
| Samsung SDI ESS report | 2025-11-03 | weak Stage 2  | N/A     | 2025-11-03 watch      | N/A                       |
| EcoPro Materials       | 2023 IPO   | 2023 IPO      | N/A     | IPO overheat          | 2024-06-14 watch          |
| Aricell / S-Connect    | 2024-06-24 | N/A           | N/A     | N/A                   | 2024-06-24 hard reference |
| FEOC / graphite policy | 2024-04-26 | 2024-05-08    | N/A     | policy watch          | N/A                       |

---

# 6. 실제 가격경로 검증 총괄

| case              |                                     anchor | MFE / MAE 해석                       | 판정                             |
| ----------------- | -----------------------------------------: | ---------------------------------- | ------------------------------ |
| L&F               |                             $2.9B → $7,386 | contract value -99.9997%           | hard 4C                        |
| LGES LFP ESS      |                         $4.3B, stock +0.6% | 좋은 계약이지만 시장은 제한적 반응                | Stage 2                        |
| LGES Q2           |   OP +152.3%, ex-IRA OP 0.28%, stock -2.3% | headline OP quality fail           | evidence_good_but_price_failed |
| LG Chem           |                     2T won LGES stake sale | 자본재활용, Green 아님                    | Stage 2                        |
| Samsung SDI ESS   | reported >3T won, company says not decided | unconfirmed event premium          | event_premium                  |
| EcoPro Materials  |                        -11% to 119,200 won | precursor demand / IPO story break | failed_rerating                |
| Aricell/S-Connect |                  S-Connect -23%, 23 deaths | safety hard reference              | hard 4C reference              |
| FEOC policy       |                           9.7T won support | policy relief, not margin proof    | policy relief                  |

---

# 7. score-price alignment 판정

```text
aligned:
- none as full Stage 3 this round

success_candidate:
- LGES / Tesla LFP ESS
- LG Chem capital recycling, but only if ROIC and debt reduction prove out
- FEOC / graphite policy relief, but only at sector-policy level

evidence_good_but_price_failed:
- LGES Q2 2025

failed_rerating:
- EcoPro Materials
- LGES subsidy-quality headline if scored as Green
- L&F initial Tesla contract headline

event_premium:
- Samsung SDI reported Tesla ESS deal
- LGES LFP contract if price runs before GWh / margin
- FEOC policy if basket rises before actual contracts

price_moved_without_evidence:
- Samsung SDI ESS report if treated as signed deal
- FEOC policy beneficiaries if actual non-China sourcing not confirmed

thesis_break:
- L&F contract collapse
- Aricell / S-Connect battery safety reference

thesis_break_watch:
- LGES IRA dependence
- EcoPro Materials precursor demand weakness
- FEOC / graphite supply-chain risk

hard_4C:
- L&F / Tesla contract collapse
- Aricell battery safety reference
```

---

# 8. 점수비중 교정

## 올릴 축

```text
actual_calloff +5
GWh_volume_disclosed +5
delivery_start +5
utilization_visibility +5
ex_subsidy_OP_quality +5
margin_and_FCF_visibility +5
counterparty_program_health +5
battery_safety_quality +5
non_China_sourcing_certification +4
capital_allocation_ROIC +4
```

### 왜 올리나

L&F는 $2.9B Tesla 계약이 $7,386로 무너졌다. LGES는 OP가 좋아 보였지만 ex-IRA OP가 거의 없었다. Aricell은 안전·품질·임시직 훈련 문제가 hard gate가 됐다. FEOC/graphite는 정책만으로는 부족하고 실제 non-China sourcing과 고객 인증이 필요하다.

## 내릴 축

```text
customer_name_headline_only -5
contract_value_without_calloff -5
reported_deal_without_confirmation -5
subsidy_adjusted_profit_dependency -5
IPO_vertical_integration_story_only -4
policy_support_without_contracts -5
capital_recycling_without_ROIC -4
battery_safety_incident -5
counterparty_4680_or_EV_program_risk -5
```

### 왜 내리나

Tesla 이름이 붙은 계약이라도 실제 call-off가 없으면 4C가 된다. Samsung SDI ESS처럼 보도만 있고 회사가 “결정된 것 없다”고 하면 Green 금지다. IRA tax credit이 OP 대부분이면 quality gate를 통과하지 못한다. EcoPro Materials는 IPO와 vertical integration만으로는 수요·마진을 증명하지 못했다.

## Green gate 강화 조건

```text
R3 Stage 3-Green 필수:
1. signed contract + actual call-off
2. GWh volume / material volume disclosed
3. delivery start or revenue recognition confirmed
4. utilization improvement
5. ex-subsidy OP quality
6. margin / FCF improvement
7. counterparty EV/ESS program health
8. safety / quality risk 없음
9. non-China sourcing / FEOC compliance if relevant
10. price path가 evidence 이후 따라옴

금지:
Tesla / GM / Ford customer name only
reported deal without confirmation
contract value without call-off
IRA subsidy-driven OP only
policy support only
IPO vertical-integration story only
battery safety incident unresolved
```

## 4B 조기감지 조건

```text
4B-watch:
Tesla / ESS / LFP headline로 단기 급등
IRA / FEOC policy support로 소재주 급등
battery recycler / precursor IPO premium 확대
subsidy benefit으로 OP 증가 후 valuation 확장
capital recycling story로 parent rerating
reported contract before company confirmation

4B-elevated:
GWh undisclosed
margin undisclosed
call-off 미확인
ex-IRA OP 약함
counterparty program risk 있음
China/graphite dependency 남음
safety incident history 있음
```

## 4C hard gate 조건

```text
contract value collapse
customer program cancellation
actual call-off failure
order cancellation
subsidy removal exposing near-zero OP
battery fire / fatal safety incident
quality failure / recall
FEOC non-compliance
non-China sourcing failure
counterparty production-yield failure
```

이번 R3 Loop 13의 hard 4C는 **L&F/Tesla contract collapse**와 **Aricell/S-Connect battery safety reference**로 확정한다. LGES IRA dependence, EcoPro Materials precursor weakness, FEOC/graphite policy는 4C-watch다.

---

# 9. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 10. 레포 반영용 patch-ready 출력

## docs/round/round_200.md 요약

```md
# R3 Loop 13. Battery / EV / Green Price Validation

이번 라운드는 R3 Loop 13 price-validation 라운드다.

핵심 결론:
- L&F / Tesla 4680 cathode is hard 4C. Initial $2.9B projected contract value collapsed to $7,386, effectively -99.9997%, due to Tesla 4680 yield issues, EV slowdown and Cybertruck weakness.
- LGES / Tesla LFP ESS is Stage 2, not Green. $4.3B contract from August 2027 to July 2030, option to extend up to 7 years; WSJ says customer is Tesla. Stock reaction only +0.6%.
- LGES Q2 2025 is evidence_good_but_price_failed. Reported OP 492B won, +152.3% YoY, but ex-IRA tax credit OP only 1.4B won, 0.28% of reported OP. Shares -2.3%.
- LG Chem stake sale is capital recycling Stage 2. It sells 2T won / $1.43B worth of LGES shares via price return swap; stake falls 2.5pp to 79.4%. ROIC and debt reduction need verification.
- Samsung SDI / Tesla ESS is event premium. Reported >3T won / $2.11B ESS deal, but Samsung SDI said nothing was decided and Tesla did not comment.
- EcoPro Materials is failed_rerating / precursor demand break. Shares -11% to 119,200 won on 2024-06-14; IPO/vertical-integration story needs utilization and margin proof.
- Aricell / S-Connect is battery safety hard reference. 23 workers killed; S-Connect reportedly -23%; CEO and senior executive sentenced to 15 years.
- FEOC / graphite policy is sector relief, not Green. China controls >99% of battery-grade graphite and 69% synthetic graphite; Korea announced 9.7T won / $7.14B support package.
```

## docs/checkpoints/checkpoint_28a_round200_r3_loop13.md 요약

```md
# Checkpoint 28A Round 200 R3 Loop 13 Battery EV Green Price Validation

## 반영 내용
- R3 Loop 13 price-validation 라운드를 추가했다.
- L&F/Tesla contract collapse, LGES/Tesla LFP ESS deal, LGES IRA subsidy-quality issue, LG Chem stake sale, Samsung SDI unconfirmed ESS report, EcoPro Materials precursor weakness, Aricell/S-Connect battery safety, FEOC/graphite policy relief를 비교했다.
- Reuters / WSJ / FT / MarketWatch anchors로 가능한 event MFE/MAE와 valuation/contract metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- actual call-off, GWh volume, delivery start, utilization, ex-subsidy OP quality, margin/FCF, counterparty program health, battery safety quality, non-China sourcing certification 가중치 강화
- customer name-only, contract value without call-off, reported deal without confirmation, subsidy-adjusted profit dependency, policy support without contracts, battery safety incident 감점 강화
```

## data/e2r_case_library/cases_r3_loop13_round200.jsonl 초안

```jsonl
{"case_id":"r3_loop13_lnf_tesla_4680_contract_collapse","symbol":"066970","company_name":"L&F","case_type":"4c_thesis_break","primary_archetype":"EV_BATTERY_MATERIAL_CONTRACT_COLLAPSE","stage1_date":"2023-02","stage4c_date":"2025-12-29","price_validation":{"price_data_source":"Reuters contract-collapse anchor","stage3_price":null,"initial_contract_projection_usd_bn":2.9,"revised_contract_value_usd":7386,"contract_value_collapse_pct":-99.9997,"supply_period":"2024-01_to_2025-12","application":"Tesla 4680 high-nickel cathode materials","risk_causes":["4680 production yield issue","EV demand slowdown","Cybertruck demand weakness"],"price_validation_status":"reported_contract_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"EV_battery_material_contract_quality_failure","notes":"Tesla customer-name and contract headline failed actual call-off; hard 4C."}
{"case_id":"r3_loop13_lges_tesla_lfp_ess_stage2","symbol":"373220","company_name":"LG Energy Solution","case_type":"success_candidate","primary_archetype":"ESS_LFP_CONTRACT_STAGE2_NOT_GREEN","stage1_date":"2025-07-25","stage2_date":"2025-07-30","price_validation":{"price_data_source":"Reuters/WSJ contract and event-return anchors","stage3_price":null,"contract_value_usd_bn":4.3,"customer":"Tesla reported by WSJ; not identified by LGES due confidentiality","contract_period":"2027-08_to_2030-07","extension_option_years":7,"use_case":"ESS LFP batteries","event_mfe_pct":0.6,"actual_gwh_volume":"not_disclosed","margin":"not_disclosed","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"ESS_LFP_contract_stage2","notes":"Good ESS pivot contract, but Green requires GWh, shipment, utilization, margin and ex-subsidy OP."}
{"case_id":"r3_loop13_lges_ira_subsidy_op_quality_gate","symbol":"373220","company_name":"LG Energy Solution","case_type":"evidence_good_but_price_failed","primary_archetype":"IRA_SUBSIDY_DEPENDENCE_QUALITY_GATE","stage2_date":"2025-07-25","price_validation":{"price_data_source":"Reuters earnings and subsidy-quality anchor","stage3_price":null,"q2_2025_op_krw_bn":492,"q2_2024_op_krw_bn":195,"op_growth_pct":152.3,"ex_ira_tax_credit_op_krw_bn":1.4,"ex_ira_share_of_reported_op_pct":0.28,"event_mae_pct":-2.3,"risk":["U.S. tariffs","early end of federal EV subsidy","EV demand slowdown"],"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"subsidy_adjusted_OP_quality_gate","notes":"Headline profit was strong, but ex-IRA OP quality failed and shares fell."}
{"case_id":"r3_loop13_lgchem_lges_stake_sale_capital_recycling","symbol":"051910","company_name":"LG Chem","case_type":"success_candidate_capital_recycling_watch","primary_archetype":"BATTERY_PARENT_CAPITAL_RECYCLING","stage2_date":"2025-10-01","price_validation":{"price_data_source":"Reuters stake-sale anchor","stage3_price":null,"stake_sale_krw_trn":2.0,"stake_sale_usd_bn":1.43,"transaction_method":"price_return_swap","stake_reduction_pp":2.5,"post_sale_lges_stake_pct":79.4,"use_of_proceeds":"reduce loans used for battery materials and biotech","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_capital_recycling_watch","rerating_result":"parent_battery_value_recycling_stage2","notes":"Stake sale is not Green until ROIC, debt reduction, shareholder return and battery-material margin confirm."}
{"case_id":"r3_loop13_samsung_sdi_tesla_ess_unconfirmed_report","symbol":"006400","company_name":"Samsung SDI","case_type":"event_premium","primary_archetype":"ESS_REPORT_UNCONFIRMED_EVENT_PREMIUM","stage2_date":"2025-11-03_weak","stage4b_date":"2025-11-03_watch","price_validation":{"price_data_source":"Reuters report-based anchor","stage3_price":null,"reported_contract_value_krw_trn":3.0,"reported_contract_value_usd_bn":2.11,"reported_supply_period_years":3,"customer":"Tesla per Korea Economic Daily report","company_confirmation":"Samsung SDI said nothing had been decided","tesla_comment":"no immediate comment","actual_signed_contract":false,"price_validation_status":"reported_deal_not_confirmed"},"score_price_alignment":"event_premium","rerating_result":"ESS_headline_unconfirmed_watch","notes":"Reported deal cannot be Stage 3 when company says nothing is decided."}
{"case_id":"r3_loop13_ecopro_materials_precursor_demand_break","symbol":"450080","company_name":"EcoPro Materials","case_type":"failed_rerating","primary_archetype":"PRECURSOR_IPO_OVERHEAT_DEMAND_BREAK","stage2_date":"2023_IPO","stage4c_date":"2024-06-14_watch","price_validation":{"price_data_source":"MarketWatch price anchor + IPO/company context","stage3_price":null,"event_date":"2024-06-14","event_price_krw":119200,"event_mae_pct":-11,"implied_pre_event_price_krw":133933,"ipo_raise_krw_bn":419,"business":"cathode precursor materials","price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"failed_rerating","rerating_result":"precursor_vertical_integration_overheat","notes":"IPO/vertical-integration story needs utilization, customer order, margin and FCF; price broke."}
{"case_id":"r3_loop13_aricell_sconnect_battery_safety_hard_reference","symbol":"S-Connect_readthrough/battery_safety_basket","company_name":"Aricell / S-Connect","case_type":"hard_4c_reference","primary_archetype":"BATTERY_SAFETY_HARD_REFERENCE","stage4c_date":"2024-06-24/2025-09-23","price_validation":{"price_data_source":"FT/Reuters safety and legal anchors","stage3_price":null,"fatalities":23,"battery_units_in_warehouse":35000,"s_connect_reported_mae_pct":-23,"ceo_sentence_years":15,"son_executive_sentence_years":15,"police_cause_context":["quality failures","rush to meet production deadline","temporary workers","inadequate emergency escape training"],"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"battery_safety_quality_hard_reference","notes":"Battery safety and quality failure is R3 hard reference; safety gate must override order/revenue story."}
{"case_id":"r3_loop13_feoc_graphite_policy_relief","symbol":"battery_supply_chain_basket","company_name":"Korea FEOC / graphite supply-chain policy relief basket","case_type":"success_candidate_policy_relief","primary_archetype":"FEOC_GRAPHITE_POLICY_RELIEF_NOT_GREEN","stage1_date":"2024-04-26","stage2_date":"2024-05-08","price_validation":{"price_data_source":"FT/WSJ policy anchors","stage3_price":null,"china_battery_grade_graphite_share_pct":99,"china_synthetic_graphite_share_pct":69,"korea_support_package_krw_trn":9.7,"korea_support_package_usd_bn":7.14,"policy_tools":["cheap state loans","tax incentives","critical minerals sourcing support","lithium-metal / graphite alternatives"],"company_level_contracts_confirmed":false,"price_validation_status":"policy_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_policy_relief","rerating_result":"FEOC_graphite_supply_chain_relief","notes":"Policy support is Stage 2; actual non-China sourcing, customer certification, margin and FCF required."}
```

## data/sector_taxonomy/score_weight_profiles_round200_r3_loop13_v1.csv 초안

```csv
archetype,actual_calloff,gwh_volume_disclosed,delivery_start,utilization_visibility,ex_subsidy_op_quality,margin_fcf_visibility,counterparty_program_health,battery_safety_quality,non_china_sourcing_certification,capital_allocation_roic,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
EV_BATTERY_MATERIAL_CONTRACT_COLLAPSE,+5,+5,+5,+5,+3,+5,+5,+4,+3,+2,0,+4,+5,L&F/Tesla proves customer-name contract can hard-break without call-off.
ESS_LFP_CONTRACT_STAGE2_NOT_GREEN,+5,+5,+5,+5,+4,+5,+4,+4,+4,+2,-3,+5,+4,LGES/Tesla ESS is Stage 2 until GWh/margin/utilization prove out.
IRA_SUBSIDY_DEPENDENCE_QUALITY_GATE,+3,+3,+4,+5,+5,+5,+4,+3,+3,+3,-4,+4,+5,LGES Q2 shows reported OP must be adjusted for IRA tax credit.
BATTERY_PARENT_CAPITAL_RECYCLING,+2,+0,+0,+1,+3,+4,+2,+2,+3,+5,-4,+4,+4,LG Chem stake sale needs ROIC/debt reduction/shareholder return proof.
ESS_REPORT_UNCONFIRMED_EVENT_PREMIUM,+4,+5,+5,+4,+3,+4,+4,+3,+3,+1,-5,+5,+3,Samsung SDI reported ESS deal is not Green without company confirmation.
PRECURSOR_IPO_OVERHEAT_DEMAND_BREAK,+4,+4,+4,+5,+3,+5,+4,+3,+4,+2,-5,+5,+5,EcoPro Materials needs utilization/margin, not IPO/vertical-integration story.
BATTERY_SAFETY_HARD_REFERENCE,+0,+0,+0,+0,+0,+0,+0,+5,+2,+0,0,+3,+5,Aricell/S-Connect shows battery safety/quality hard gate.
FEOC_GRAPHITE_POLICY_RELIEF_NOT_GREEN,+2,+2,+2,+3,+3,+4,+4,+3,+5,+3,-5,+4,+4,FEOC/graphite policy is relief until actual supply contracts and certification.
```

---

# 이번 R3 Loop 13 결론

```text
1. L&F는 이번 라운드 hard 4C다.
   Tesla 4680 cathode 계약이 $2.9B에서 $7,386로 사실상 붕괴했다.

2. LGES / Tesla LFP ESS는 좋은 Stage 2다.
   하지만 GWh, margin, utilization, ex-subsidy OP 전에는 Green 금지다.

3. LGES Q2는 headline OP가 좋아도 quality gate에서 걸렸다.
   ex-IRA OP는 reported OP의 0.28%뿐이었고 주가는 -2.3%였다.

4. LG Chem stake sale은 capital recycling이다.
   ROIC와 debt reduction, battery-material margin이 확인되어야 한다.

5. Samsung SDI / Tesla ESS 보도는 event premium이다.
   회사가 “결정된 것 없다”고 했으면 Stage 3 금지다.

6. EcoPro Materials는 precursor overheat / demand break다.
   -11% price anchor는 IPO·vertical integration story만으로 부족하다는 증거다.

7. Aricell / S-Connect는 battery safety hard reference다.
   배터리 업종은 safety·quality failure가 즉시 hard gate다.

8. FEOC / graphite policy는 sector relief다.
   정책지원은 좋지만 실제 non-China supply와 인증, margin 전에는 Green이 아니다.
```

한 문장으로 압축하면:

> **R3에서 진짜 Stage 3는 “Tesla·ESS·LFP·IRA·탈중국·배터리 소재가 좋다”가 아니라, 실제 call-off·GWh·납품·utilization·ex-subsidy OP·margin·FCF·safety gate가 가격경로와 함께 닫히는 순간이다.**

[1]: https://www.reuters.com/world/asia-pacific/south-koreas-lf-says-value-battery-material-supply-deal-with-tesla-cut-7386-2025-12-29/?utm_source=chatgpt.com "South Korea's L&F slashes value of battery material supply deal with Tesla"
[2]: https://www.reuters.com/business/energy/lg-energy-solution-signs-43-billion-battery-supply-contract-2025-07-30/?utm_source=chatgpt.com "LG Energy Solution signs $4.3 billion battery supply contract"
[3]: https://www.reuters.com/business/autos-transportation/ev-battery-firm-lg-energy-sees-demand-slowdown-after-q2-profit-jump-2025-07-25/?utm_source=chatgpt.com "EV battery firm LG Energy sees demand slowdown after Q2 profit jump"
[4]: https://www.reuters.com/markets/emerging/lg-chem-sell-14-bln-worth-shares-lg-energy-solution-2025-10-01/?utm_source=chatgpt.com "LG Chem to sell $1.4 billion worth of shares in LG Energy Solution"
[5]: https://www.reuters.com/business/autos-transportation/tesla-buy-2-bln-ess-batteries-samsung-sdi-over-3-years-newspaper-says-2025-11-03/?utm_source=chatgpt.com "Tesla to buy $2 bln of ESS batteries from Samsung SDI over 3 years, newspaper says"
[6]: https://www.marketwatch.com/story/ecopro-materials-shares-fall-11-to-krw119-200-103f38d7?utm_source=chatgpt.com "Ecopro Materials Shares Fall 11% to KRW119,200"
[7]: https://www.ft.com/content/c4c93131-e8da-46bb-aae8-36e16c0e295e?utm_source=chatgpt.com "Fire at South Korean lithium battery plant kills 22"
[8]: https://www.ft.com/content/7a7ba474-7068-46fc-89da-19d87e83f9d3?utm_source=chatgpt.com "China's EV supply chain dominance risks 'collapse' of US subsidies, warns South Korea"
