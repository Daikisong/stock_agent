순서상 이번은 **R10 Loop 15 — 건설·부동산·건자재 trigger-level price validation 라운드**다.

이번 R10의 핵심은 “수주가 크다 / 부동산 공급책이 나왔다 / 해외 EPC가 좋다”가 아니라, **수주 → backlog → margin → 현금흐름**, **주택공급 정책 → 실제 착공/분양/미분양 흡수**, **PF 구조조정 → 부실 정리**, **품질·안전 사고 → 브랜드·영업정지·원가 충당금**을 각각 다른 trigger로 보는 것이다.

```text
round = R10 Loop 15
round_id = round_233
large_sector = CONSTRUCTION_REAL_ESTATE_BUILDING_MATERIALS
method = trigger_level_backtest_v1
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R11 Loop 15
```

이번에도 KRX/Naver/Yahoo/Stooq의 수정주가 일봉 OHLC 30D/90D/180D/1Y window를 안정적으로 직접 추출하지 못했다. 그래서 full MFE/MAE는 만들지 않고 `price_data_unavailable_after_deep_search`로 둔다. 대신 Reuters/WSJ/AP/MarketWatch에 보도된 **reported event return, event price, contract value, policy amount, PF delinquency, tariff/support amount, project delay/legal block**을 trigger anchor로 쓴다. 계산 불가능한 MFE/MAE는 만들지 않는다.

---

# 1. 이번 라운드 대섹터

```text
R10 = 건설·부동산·건자재
```

R10의 core gate는 아래다.

```text
해외 EPC / 플랜트:
수주 공시 → 계약금액 → 연간 수주잔고 대비 크기 → gross margin → cash collection → cost overrun / delay

원전·인프라:
preferred bidder → final contract → legal appeal → financing model → EPC/설계/기자재 배분 → 착공 → margin

주택·부동산:
정책공급 → 인허가 → 착공 → 분양률 → 미분양 흡수 → PF 상환 → 현금흐름

PF / 개발:
PF 만기 → 리파이낸싱 → 보증/유동성 지원 → 부실사업장 정리 → impairment → surviving builder rerating

건자재:
주택 착공 / 인프라 발주 → rebar/cement/glass/dry mortar 수요 → ASP → 원가/전력비 → spread → 재고

품질·안전:
붕괴 / 하자 / 철근 누락 → 영업정지 / 브랜드 훼손 → 보상·재시공 → 수주 제한 → hard 4C
```

---

# 2. 대상 canonical archetype

```text
OVERSEAS_EPC_MEGA_ORDER_STAGE2_ACTIONABLE
NUCLEAR_CONSTRUCTION_EXPORT_STAGE2_WITH_LEGAL_4B
REAL_ESTATE_PF_RESTRUCTURING_4C_WATCH
HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_POLICY
CONSTRUCTION_QUALITY_SAFETY_HARD_4C
BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING
BUILDER_LIQUIDITY_SUPPORT_FALSE_POSITIVE_WATCH
```

---

# 3. deep sub-archetype

```text
Samsung E&A:
- Saudi Aramco Fadhili gas expansion
- $6B contract
- shares +8.5% vs KOSPI -1.4%
- annual contract wins average KRW8.6T context
- Stage2-Actionable / Stage3-Yellow candidate

GS E&C:
- included in Aramco Fadhili EPC award group
- large overseas plant backlog trigger
- but domestic quality/PF/safety overlay remains
- price unavailable in sourced article

Czech nuclear construction basket:
- KHNP preferred bidder for 2 reactors
- first large overseas nuclear project since 2009
- Doosan Enerbility +48%, KEPCO Plant S&E +14%, KEPCO E&C +41% over 3 months
- legal block / EDF appeal / final signing delay
- Stage2 with 4B legal overlay

Taeyoung / PF crisis:
- builder debt rescheduling trigger
- 40.6T won support package
- PF delinquency 2.70% end-2023 vs 0.37% end-2021
- 1T won syndicated loan, expandable to 5T won
- 4C-watch / restructuring stage

Housing supply / Seoul reconstruction:
- Seoul price rebound
- 400k homes over six years
- LTV tightening in wealthy districts 50%→40%
- LH land use, reconstruction-regulation simplification
- Stage2 policy, not Green

HDC Hyundai Development / Gwangju collapse:
- 2022 Hwajeong I-Park exterior-wall collapse
- six deaths
- faulty construction / substandard materials / unauthorized slab change
- hard 4C construction-quality reference

Hyundai Steel rebar / construction-material demand:
- weak construction demand
- rebar price -10% expected
- net profit estimate cut -73% to KRW215B
- shares -1.2% at KRW29,000
- 건자재 failed rerating reference
```

---

# 4. 선정 case 요약

| bucket                                      | case                                  | 핵심 판정                                                                     |
| ------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------- |
| Stage2-Actionable / Stage3-Yellow candidate | Samsung E&A / Saudi Fadhili           | $6B contract, +8.5%, KOSPI -1.4%. 수주잔고 대비 크고 가격반응 강함                      |
| Stage2 with margin/delay gate               | GS E&C / Fadhili participation        | Aramco $7.7B package에 포함. 가격자료 부족, 품질/PF overlay 필요                       |
| Stage2 + 4B legal overlay                   | Czech nuclear construction basket     | KHNP preferred bidder, nuclear stocks 3개월 +14~48%, court/legal appeal로 4B |
| 4C-watch / restructuring                    | Taeyoung / PF crisis                  | 40.6T 지원, PF delinquency 2.70%, restructuring 필요. builder-wide hard watch |
| Stage2 policy                               | Seoul housing supply / reconstruction | 가격 반등과 공급정책은 Stage2. 실제 착공·분양·PF 상환 전 Green 금지                            |
| hard 4C                                     | HDC / Gwangju Hwajeong I-Park         | 붕괴·사망·부실시공 reference. 건설 품질 hard gate                                     |
| failed_rerating                             | Hyundai Steel rebar demand            | rebar -10%, NP estimate -73%, shares -1.2%. 건자재 수요·spread 4C-watch        |
| false-positive watch                        | Builder liquidity support             | 유동성 지원은 survival trigger일 뿐, margin/분양률 없으면 Green 아님                      |

---

# 5. Case별 trigger grid

## Case A — Samsung E&A / Saudi Aramco Fadhili gas expansion

```text
symbol = 028050
case_type = Stage2-Actionable / Stage3-Yellow candidate
archetype = OVERSEAS_EPC_MEGA_ORDER_STAGE2_ACTIONABLE
```

| trigger | type                    |       date | 당시 공개 evidence                                                                                         | 가격 anchor                     | outcome          |
| ------- | ----------------------- | ---------: | ------------------------------------------------------------------------------------------------------ | ----------------------------- | ---------------- |
| T0      | awareness               | 2024-04-02 | Saudi Aramco Fadhili gas expansion $7.7B award; Samsung E&A and GS E&C included                        | no company price yet          | Stage2 evidence  |
| T1      | Stage2-Actionable       | 2024-04-03 | Samsung E&A signs around $6B contract, lion’s share of Fadhili expansion                               | +8.5%, KRW26,750, KOSPI -1.4% | excellent event  |
| T2      | Stage3-Yellow candidate | 2024-04-03 | contract size close to Samsung E&A’s 2017~2023 average annual wins of KRW8.6T; completion due Nov 2027 | same                          | Yellow candidate |
| T3      | 4B-watch                |  2024~2027 | EPC margin, cost escalation, Saudi execution delay, cash collection not yet verified                   | no full OHLC                  | 4B               |
| T4      | Stage3-Green            |        N/A | backlog-to-margin / cashflow conversion not confirmed                                                  | N/A                           | no Green         |

Samsung E&A의 Fadhili trigger는 R10에서 가장 깨끗한 Stage2-Actionable이다. Aramco는 Fadhili gas plant expansion에 $7.7B를 awarded했고, capacity를 2.5B scf/d에서 4B scf/d로 키우는 프로젝트라고 밝혔다. Samsung E&A와 GS E&C가 EPC contractor로 포함됐다. ([Reuters][1])

다음 날 WSJ/Dow Jones 보도 기준으로 Samsung E&A는 약 $6B 계약을 체결했고, 주가는 장중 +8.5%로 KRW26,750까지 상승했다. 같은 시간 KOSPI는 -1.4%였고, KB Securities는 이 계약이 회사의 2017~2023년 평균 annual contract wins KRW8.6T와 비교해 매우 큰 규모라고 평가했다. 이 조합은 “수주 headline”이 아니라 **계약금액·상대강도·연간수주잔고 대비 크기**가 닫힌 Stage2-Actionable이다. ([월스트리트저널][2])

```json
{
  "case_id": "r10_loop15_samsung_ea_fadhili",
  "symbol": "028050",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable_to_Stage3-Yellow_candidate",
  "trigger_date": "2024-04-03",
  "contract_value_usd_bn": 6.0,
  "aramco_total_package_usd_bn": 7.7,
  "event_mfe_pct": 8.5,
  "event_price_high_krw": 26750,
  "kospi_same_context_pct": -1.4,
  "market_relative_return_pp": 9.9,
  "average_annual_contract_wins_2017_2023_krw_trn": 8.6,
  "completion_target": "2027-11",
  "stage3_gate_missing": [
    "gross_margin",
    "cost_overrun_visibility",
    "cash_collection_schedule",
    "Saudi_execution_delay_risk",
    "backlog_to_OP_conversion"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable"
}
```

### 판정

```text
score_price_alignment = Stage2_promote_candidate
new_rule = 해외 EPC에서 계약금액이 연간수주잔고 대비 크고, 당일 상대강도 +5pp 이상이면 Stage2-Actionable
but = margin/cashflow 전에는 Green 금지
```

---

## Case B — GS E&C / Fadhili participation with domestic-quality overlay

```text
symbol = 006360
case_type = Stage2 overseas EPC evidence + quality/PF overlay
archetype = OVERSEAS_EPC_MEGA_ORDER_STAGE2_ACTIONABLE
```

| trigger | type                        |       date | 당시 공개 evidence                                                       | 가격 anchor                       | outcome   |
| ------- | --------------------------- | ---------: | -------------------------------------------------------------------- | ------------------------------- | --------- |
| T0      | Stage2 evidence             | 2024-04-02 | Aramco awards Fadhili EPC contracts to Samsung E&A, GS E&C and Nesma | GS E&C direct price unavailable | Stage2    |
| T1      | Stage2-Actionable candidate | 2024-04-02 | $7.7B project, 60% capacity expansion, Nov 2027 completion           | no price                        | candidate |
| T2      | 4B/PF-watch                 |      2024~ | 국내 주택/PF/품질 리스크와 해외 EPC margin을 분리해야 함                               | no full OHLC                    | overlay   |
| T3      | Stage3-Yellow               |        N/A | GS-specific contract value / margin / cash collection not located    | N/A                             | no Yellow |

GS E&C도 Fadhili package에 포함됐지만, 이번 검색에서 **GS E&C의 당일 event return과 개별 계약금액**은 확인하지 못했다. 그래서 Samsung E&A와 달리 Stage2-Actionable으로 확정하지 않고, `Stage2 overseas EPC evidence`로 둔다. Aramco project 자체는 $7.7B, completion target Nov 2027, gas capacity +60%로 충분히 큰데, GS E&C는 개별 margin·cash collection과 국내 주택/PF/품질 overlay가 따로 필요하다. ([Reuters][1])

```json
{
  "case_id": "r10_loop15_gsenc_fadhili_overlay",
  "symbol": "006360",
  "best_trigger": "T0/T1",
  "best_trigger_type": "Stage2_overseas_EPC_evidence",
  "trigger_date": "2024-04-02",
  "aramco_total_package_usd_bn": 7.7,
  "project_capacity_before_bcf_per_day": 2.5,
  "project_capacity_after_bcf_per_day": 4.0,
  "completion_target": "2027-11",
  "company_specific_contract_value": "price_data_unavailable_after_deep_search",
  "event_return": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "GS_E&C_specific_contract_value",
    "project_margin",
    "cash_collection",
    "domestic_PF_exposure",
    "quality_safety_overhang"
  ],
  "trigger_outcome_label": "Stage2_evidence_but_not_actionable_without_company_price"
}
```

### 판정

```text
score_price_alignment = success_candidate_stage2
new_rule = consortium/package 수주만으로는 Actionable 아님; 개별 계약금액·가격반응·margin 필요
```

---

## Case C — Czech nuclear construction basket / KHNP preferred bidder

```text
symbols = 034020 / 051600 / 052690 / 015760 read-through
company_scope = Doosan Enerbility / KEPCO Plant S&E / KEPCO E&C / KEPCO-KHNP
case_type = Stage2 with legal 4B overlay
archetype = NUCLEAR_CONSTRUCTION_EXPORT_STAGE2_WITH_LEGAL_4B
```

| trigger | type                |       date | 당시 공개 evidence                                                                                               | 가격 anchor                                                       | outcome                  |
| ------- | ------------------- | ---------: | ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- | ------------------------ |
| T0      | awareness           | 2024-04-30 | CEZ receives binding bids from KHNP and EDF for up to four nuclear units                                     | no price                                                        | Stage1                   |
| T1      | Stage2 evidence     | 2024-07-17 | Czech government picks KHNP preferred bidder for two reactors; first major overseas nuclear order since 2009 | Doosan +48%, KEPCO Plant S&E +14%, KEPCO E&C +41% over 3 months | Stage2-Actionable basket |
| T2      | 4B/legal watch      | 2024-10-30 | Czech anti-monopoly office temporarily blocks contract signing amid Westinghouse/EDF appeals                 | no KRX price                                                    | legal 4B                 |
| T3      | 4B/legal watch      | 2025-05-06 | Czech court halts $18B signing after EDF complaint                                                           | no KRX price                                                    | delay                    |
| T4      | relief / validation | 2025-06-04 | Czech side signs deal after court clears way; contract 407B koruna / $18.7B                                  | no KRX price                                                    | Stage2 validation        |
| T5      | Stage3-Yellow       |        N/A | Korean listed contractors’ exact work split, margin, payment schedule not confirmed                          | N/A                                                             | no Yellow                |

Czech nuclear trigger는 R10의 대형 인프라 Stage2다. Reuters는 Czech government가 KHNP를 two reactors preferred bidder로 선정했고, 이는 한국의 2009년 UAE 이후 첫 대형 해외 원전 수주라고 보도했다. 같은 보도에서 Doosan Enerbility는 3개월간 +48%, KEPCO Plant S&E는 +14%, KEPCO E&C는 +41% 올랐다고 설명했다. 이건 확실한 `Stage2-Actionable basket`이다. ([Reuters][3])

하지만 바로 Green은 아니다. Czech anti-monopoly office는 EDF/Westinghouse appeals 이후 계약 체결을 일시적으로 막았고, 2025년 5월에는 Czech court가 EDF complaint로 $18B 계약 signing을 halted했다. 이후 AP는 Czech side가 court clearance 뒤 KHNP와 two reactors deal을 signed했고, 계약 규모를 407B koruna, 약 $18.7B로 보도했다. 즉 이 case는 `Stage2 + legal 4B overlay + relief validation`이다. ([Reuters][4])

```json
{
  "case_id": "r10_loop15_czech_nuclear_construction_basket",
  "symbols": "034020/051600/052690/015760_readthrough",
  "best_trigger": "T1/T4",
  "best_trigger_type": "Stage2-Actionable_with_legal_4B_overlay",
  "t1_date": "2024-07-17",
  "reactors_count": 2,
  "preferred_bidder": "KHNP",
  "first_major_overseas_nuclear_order_since": 2009,
  "unit_cost_estimate_czk_bn": 200,
  "doosan_3m_return_pct": 48,
  "kepco_plant_se_3m_return_pct": 14,
  "kepco_ec_3m_return_pct": 41,
  "t2_legal_block_date": "2024-10-30",
  "t3_court_halt_date": "2025-05-06",
  "t4_contract_signed_date": "2025-06-04",
  "signed_contract_value_czk_bn": 407,
  "signed_contract_value_usd_bn": 18.7,
  "stage3_gate_missing": [
    "listed_company_work_share",
    "EPC_or_design_margin",
    "payment_schedule",
    "final_subcontract_awards",
    "legal_appeal_resolution",
    "construction_start"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_Actionable_with_legal_4B_overlay"
}
```

### 판정

```text
score_price_alignment = Stage2_promote_candidate
new_rule = preferred bidder + sector basket rerating은 Stage2-Actionable
but = final contract, legal appeals, listed-company work split 전에는 Green 금지
```

---

## Case D — Taeyoung / real-estate PF restructuring

```text
symbol = 009410
case_type = 4C-watch / restructuring
archetype = REAL_ESTATE_PF_RESTRUCTURING_4C_WATCH
```

| trigger | type                  |       date | 당시 공개 evidence                                                                                                   | 가격 anchor         | outcome       |
| ------- | --------------------- | ---------: | ---------------------------------------------------------------------------------------------------------------- | ----------------- | ------------- |
| T0      | 4C awareness          |    2023-12 | Taeyoung E&C plans debt rescheduling; market worries about builder liquidity                                     | no price          | PF 4C-watch   |
| T1      | Stage2 policy support | 2024-03-27 | government prepares KRW40.6T support for SMEs/builders; liquidity support and guarantees for profitable projects | no Taeyoung price | relief Stage2 |
| T2      | 4C validation         | 2024-05-13 | PF delinquency rises to 2.70% end-2023 from 0.37% end-2021; tougher restructuring assessment                     | no price          | hard watch    |
| T3      | relief liquidity      | 2024-05-13 | KRW1T syndicated loan, expandable to KRW5T                                                                       | no price          | support       |
| T4      | Stage3-Yellow         |        N/A | bad PF cleanup / write-down / surviving builder margin not confirmed                                             | N/A               | no Yellow     |

Taeyoung/PF case는 R10에서 “유동성 지원 = Green”이 아님을 보여준다. Reuters는 2024년 3월 정부가 고금리와 부동산 부진에 타격을 받은 중소기업·건설사를 위해 KRW40.6T 지원책을 준비했고, builder에는 보증 확대와 시장안정펀드 지원이 들어간다고 보도했다. 같은 보도는 Taeyoung E&C가 2023년 12월 debt rescheduling 계획을 밝히며 다른 건설사 liquidity concerns를 키웠다고 설명했다. ([Reuters][5])

5월에는 FSS가 real estate PF restructuring을 강화했다. PF delinquency rate는 2021년 말 0.37%에서 2023년 말 2.70%로 올라갔고, commercial banks/insurers는 KRW1T syndicated loan을 준비했으며 필요 시 KRW5T까지 키울 수 있다고 했다. 이건 Stage2 relief이지만, equity 입장에서는 부실사업장 정리·충당금·write-down이 남아 있는 4C-watch다. ([Reuters][6])

```json
{
  "case_id": "r10_loop15_taeyoung_pf_restructuring",
  "symbol": "009410",
  "best_trigger": "T0/T2",
  "best_trigger_type": "4C_watch_with_policy_relief",
  "debt_rescheduling_awareness_date": "2023-12",
  "support_package_date": "2024-03-27",
  "support_package_krw_trn": 40.6,
  "pf_delinquency_end_2021_pct": 0.37,
  "pf_delinquency_end_2023_pct": 2.70,
  "syndicated_loan_initial_krw_trn": 1.0,
  "syndicated_loan_max_krw_trn": 5.0,
  "taeyoung_event_price": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "PF_project_profitability_reassessment",
    "debt_restructuring_terms",
    "impairment_size",
    "cashflow_after_workout",
    "new_order_access"
  ],
  "trigger_outcome_label": "PF_4C_watch_with_policy_relief"
}
```

### 판정

```text
score_price_alignment = thesis_break_watch
new_rule = PF 유동성 지원은 Stage2 relief일 뿐, bad PF 정리와 equity dilution/write-down 전에는 Green 금지
```

---

## Case E — Seoul housing supply / reconstruction policy

```text
symbols = 000720 / 047040 / 006360 / 375500 / 028050 / housing_developer_basket
company_scope = Hyundai E&C / Daewoo E&C / GS E&C / DL E&C / Samsung E&A read-through
case_type = Stage2 policy
archetype = HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_POLICY
```

| trigger | type            |       date | 당시 공개 evidence                                                                                               | 가격 anchor              | outcome       |
| ------- | --------------- | ---------: | ------------------------------------------------------------------------------------------------------------ | ---------------------- | ------------- |
| T0      | awareness       | 2024-07/08 | Seoul house prices rebound; reconstruction demand                                                            | no direct basket price | Stage1        |
| T1      | Stage2 evidence | 2024-08-16 | Seoul prices +0.76% in July, fastest monthly rise since Dec 2019; government plans 400k homes over six years | no basket price        | Stage2 policy |
| T2      | 4B-watch        | 2025-03-19 | wealthy Seoul districts trading permits tightened; speculation control                                       | no price               | policy cap    |
| T3      | Stage2 relief   | 2025-09-07 | LTV in Gangnam/Yongsan cut 50%→40%, but affordable housing supply and reconstruction simplification planned  | no price               | mixed policy  |
| T4      | Stage3-Yellow   |        N/A | actual permits / starts / presales / PF repayment not confirmed                                              | N/A                    | no Yellow     |

Housing supply policy는 R10에서 반드시 Stage2로만 둔다. Reuters는 2024년 7월 Seoul prices가 +0.76% 올라 2019년 12월 이후 가장 빠른 monthly rise였고, 정부가 6년간 400,000 homes 공급 계획을 냈다고 보도했다. 이건 주택 developer/builder 입장에서는 demand/supply policy trigger다. ([Reuters][7])

하지만 2025년에는 speculative heat를 잡기 위해 wealthy Seoul districts에 transaction permits가 다시 tightened 됐고, 9월에는 Gangnam/Yongsan 등에서 LTV를 50%에서 40%로 낮추는 동시에 LH land 활용과 reconstruction simplification을 추진했다. 즉 이 trigger는 “주택공급 호재”와 “대출/거래 규제”가 같이 있는 mixed Stage2다. 실제 착공·분양률·미분양 흡수·PF 상환이 없으면 Stage3가 아니다. ([Reuters][8])

```json
{
  "case_id": "r10_loop15_seoul_housing_supply_reconstruction",
  "symbols": "000720/047040/006360/375500/housing_developer_basket",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2_policy_mixed",
  "seoul_price_july_2024_mom_pct": 0.76,
  "fastest_since": "2019-12",
  "planned_homes_over_6y": 400000,
  "wealthy_district_transaction_permit_tightening": true,
  "ltv_cut_from_pct": 50,
  "ltv_cut_to_pct": 40,
  "state_land_supply": true,
  "reconstruction_regulation_simplification": true,
  "direct_basket_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "building_permits",
    "housing_starts",
    "presale_rate",
    "unsold_inventory_absorption",
    "PF_refinancing",
    "construction_margin"
  ],
  "trigger_outcome_label": "Stage2_policy_not_Green"
}
```

### 판정

```text
score_price_alignment = success_candidate_stage2
new_rule = 주택공급/재건축 정책은 Stage2, 실제 착공·분양률·PF 상환 전에는 Yellow/Green 금지
```

---

## Case F — HDC Hyundai Development / Gwangju Hwajeong I-Park collapse

```text
symbol = 294870
case_type = hard 4C construction-quality reference
archetype = CONSTRUCTION_QUALITY_SAFETY_HARD_4C
```

| trigger | type                  |                 date | 당시 공개 evidence                                                                                       | 가격 anchor                               | outcome    |
| ------- | --------------------- | -------------------: | ---------------------------------------------------------------------------------------------------- | --------------------------------------- | ---------- |
| T0      | hard 4C               |           2022-01-11 | Gwangju Hwajeong I-Park exterior wall collapse, six deaths                                           | price unavailable in accessible sources | hard 4C    |
| T1      | 4C validation         | 2022-03/2023 summary | investigation points to faulty construction methods, substandard materials, unauthorized slab change | no price                                | validation |
| T2      | governance/brand risk |                 2022 | HDC chairman resigns amid public criticism/scrutiny                                                  | no price                                | brand 4C   |
| T3      | relief                |                  N/A | trust recovery / order recovery not confirmed                                                        | N/A                                     | no relief  |

HDC case는 R10의 hard construction-quality reference다. 접근 가능한 open-source incident summary에 따르면 2022년 1월 11일 Gwangju Hwajeong I-Park 외벽 붕괴로 6명이 사망했고, 이후 investigation은 faulty construction methods, substandard building materials, unauthorized structural changes를 원인으로 지적했다. 이건 단순 하자비용이 아니라 **브랜드·인허가·수주·품질 신뢰가 동시에 깨지는 hard 4C**다. ([위키백과][9])

```json
{
  "case_id": "r10_loop15_hdc_gwangju_quality_hard_4c",
  "symbol": "294870",
  "best_trigger": "T0/T1",
  "best_trigger_type": "hard_4C_construction_quality",
  "incident_date": "2022-01-11",
  "fatalities": 6,
  "incident": "Gwangju Hwajeong I-Park exterior wall collapse",
  "investigation_findings": [
    "faulty_construction_methods",
    "substandard_building_materials",
    "unauthorized_structural_change"
  ],
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "hard_4c_confirmed": true,
  "trigger_outcome_label": "hard_4c_success_quality_safety"
}
```

### 판정

```text
score_price_alignment = hard_4c_success
new_rule = 건설 품질·안전 사고는 R10 hard gate. 수주잔고/정책호재보다 먼저 차감
```

---

## Case G — Hyundai Steel / rebar weak demand as building-material failed rerating

```text
symbol = 004020
case_type = failed_rerating / building-material demand 4C-watch
archetype = BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING
```

| trigger | type          |       date | 당시 공개 evidence                                                     | 가격 anchor               | outcome         |
| ------- | ------------- | ---------: | ------------------------------------------------------------------ | ----------------------- | --------------- |
| T0      | awareness     |    2024-H1 | construction/shipbuilding material demand weakening                | no price                | watch           |
| T1      | 4C-watch      | 2024-06-21 | rebar price expected -10%; net-profit estimate cut -73% to KRW215B | shares -1.2%, KRW29,000 | failed rerating |
| T2      | Stage2 relief |        N/A | anti-dumping or infrastructure demand could offset later           | not this trigger        | no relief       |
| T3      | Stage3-Yellow |        N/A | rebar ASP / construction starts / margin recovery not confirmed    | N/A                     | no Yellow       |

Hyundai Steel is not a pure builder, but R10에서 **건자재 demand/spread**를 calibrate하기 좋다. MarketWatch/Dow Jones는 Nomura가 weak construction and shipbuilding demand를 이유로 2024년 rebar price -10%를 예상했고, Hyundai Steel의 2024 net profit estimate를 73% 낮춰 KRW215B로 조정했으며, 목표주가도 14% 낮춘 KRW30,000로 제시했다고 보도했다. 당시 주가는 -1.2%로 KRW29,000이었다. 이 trigger는 건설 경기와 건자재 spread가 깨질 때의 failed-rerating template다. ([마켓워치][10])

```json
{
  "case_id": "r10_loop15_hyundai_steel_rebar_weak_construction_demand",
  "symbol": "004020",
  "best_trigger": "T1",
  "best_trigger_type": "4C_watch_failed_rerating",
  "trigger_date": "2024-06-21",
  "entry_price_anchor_krw": 29000,
  "event_return_pct": -1.2,
  "expected_rebar_price_decline_pct": -10,
  "net_profit_estimate_after_cut_krw_bn": 215,
  "net_profit_estimate_cut_pct": -73,
  "target_price_after_krw": 30000,
  "target_price_cut_pct": -14,
  "stage3_gate_missing": [
    "construction_starts_recovery",
    "rebar_ASP_recovery",
    "raw_material_spread",
    "inventory_drawdown",
    "infrastructure_order_pull"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "failed_rerating_4C_watch"
}
```

### 판정

```text
score_price_alignment = failed_rerating
new_rule = 건자재는 수요·ASP·spread가 없으면 정책/인프라 기대만으로 Stage3 금지
```

---

## Case H — Builder liquidity support / policy-relief false-positive watch

```text
symbols = builder_basket
case_type = false_positive_watch
archetype = BUILDER_LIQUIDITY_SUPPORT_FALSE_POSITIVE_WATCH
```

| trigger | type                 |       date | 당시 공개 evidence                                                                                                                | 가격 anchor       | outcome           |
| ------- | -------------------- | ---------: | ----------------------------------------------------------------------------------------------------------------------------- | --------------- | ----------------- |
| T0      | Stage2 relief        | 2024-03-27 | KRW40.6T support for small businesses/builders                                                                                | no basket price | relief            |
| T1      | Stage2 relief        | 2024-07-03 | government to expand public-sector investment, infrastructure projects and policy financing by KRW15T more than planned in H2 | no basket price | relief            |
| T2      | 4C-watch             | 2024-05-13 | PF restructuring stricter, delinquency high                                                                                   | no price        | underlying stress |
| T3      | false-positive watch |    ongoing | liquidity support may support survival but not margin/ROE                                                                     | no price        | watch             |
| T4      | Stage3-Yellow        |        N/A | project profitability and cashflow recovery not confirmed                                                                     | N/A             | no Yellow         |

Government support is not Green. Reuters reported KRW40.6T support for SMEs/builders in March, and later an additional policy thrust to revive construction via KRW15T more public-sector investment/infrastructure/policy financing in the second half of 2024. But the same policy environment also contained PF restructuring, default-risk assessment, and liquidity stress. So this is **Stage2 relief**, not Stage3. ([Reuters][5])

```json
{
  "case_id": "r10_loop15_builder_liquidity_support_false_positive_watch",
  "symbols": "builder_basket",
  "best_trigger": "T0/T1",
  "best_trigger_type": "Stage2_relief_false_positive_watch",
  "support_package_2024_03_krw_trn": 40.6,
  "additional_public_sector_investment_2024_h2_krw_trn": 15,
  "pf_restructuring_ongoing": true,
  "direct_basket_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "project_profitability",
    "presale_rate",
    "PF_maturity_extension_terms",
    "gross_margin",
    "cash_collection",
    "debt_ratio_stabilization"
  ],
  "trigger_outcome_label": "policy_relief_not_Green"
}
```

### 판정

```text
score_price_alignment = false_positive_watch
new_rule = 건설사 유동성 지원은 survival trigger. margin/분양률/PF 상환 전에는 Stage3 금지
```

---

# 6. Trigger별 가격경로 검증 요약

| case                      | best trigger |   entry anchor |                                       event MFE/MAE |       market-relative | full MFE/MAE | outcome                     |
| ------------------------- | ------------ | -------------: | --------------------------------------------------: | --------------------: | ------------ | --------------------------- |
| Samsung E&A Fadhili       | T1/T2        | KRW26,750 high |                                               +8.5% | +9.9pp vs KOSPI -1.4% | unavailable  | Stage2-Actionable           |
| GS E&C Fadhili            | T0/T1        |    unavailable |                                         unavailable |           unavailable | unavailable  | Stage2 evidence only        |
| Czech nuclear basket      | T1/T4        | sector returns | Doosan +48%, KEPCO PSE +14%, KEPCO E&C +41% over 3M |           unavailable | unavailable  | Stage2 + legal 4B           |
| Taeyoung/PF               | T0/T2        |    unavailable |                                         unavailable |           unavailable | unavailable  | 4C-watch                    |
| Seoul housing supply      | T1/T3        |    unavailable |                                         unavailable |           unavailable | unavailable  | Stage2 policy               |
| HDC Gwangju collapse      | T0/T1        |    unavailable |                                         unavailable |                   N/A | unavailable  | hard 4C                     |
| Hyundai Steel rebar       | T1           |      KRW29,000 |                                               -1.2% |           unavailable | unavailable  | failed_rerating             |
| Builder liquidity support | T0/T1        |    unavailable |                                         unavailable |           unavailable | unavailable  | relief false-positive watch |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
GS E&C Fadhili:
package 수주 evidence는 있지만 GS-specific price/contract value가 없어 Actionable 보류.

Taeyoung/PF:
정책 지원은 relief지만 equity entry가 아니라 restructuring watch.

Seoul housing supply:
주택공급·재건축 정책은 Stage2지만 착공/분양/미분양 흡수 전에는 Yellow 보류.
```

## Stage 2-Actionable entry 성과

```text
Samsung E&A:
$6B contract + +8.5% + KOSPI -1.4%는 excellent Stage2-Actionable.

Czech nuclear basket:
preferred bidder + sector 3개월 +14~48%는 Stage2-Actionable.
다만 legal appeals와 final work allocation 때문에 4B overlay.
```

## Stage3-Yellow 후보

```text
Samsung E&A:
gross margin, cost overrun, cash collection이 보이면 Yellow.

Czech nuclear:
final contract, listed-company work split, payment schedule, legal clarity가 닫히면 Yellow.

Seoul housing/reconstruction:
permits, housing starts, presale rate, PF refinancing이 닫히면 Yellow.
```

## Stage3-Green

```text
이번 R10 Loop 15에서 확정 Green 없음.

이유:
- EPC는 수주에서 margin/cashflow까지 아직 멀다.
- 원전은 legal appeal / work split / 착공까지 남아 있다.
- 주택공급은 정책에서 실제 착공·분양까지 남아 있다.
- PF는 구조조정이 끝나지 않았다.
- 건자재는 demand/spread가 약하다.
```

---

# 8. score-price alignment 판정

```text
Stage2_promote_candidate:
- Samsung E&A / Fadhili
- Czech nuclear construction basket

Stage3-Yellow candidate:
- Samsung E&A, if margin/cashflow conversion confirms
- Czech nuclear, if legal/work allocation clears
- Seoul housing supply, if permits/starts/presales confirm

failed_rerating:
- Hyundai Steel rebar / construction-material demand

event_premium:
- Nuclear preferred-bidder basket if treated as final EPC margin too early
- Housing supply policy if treated as immediate builder earnings

false_positive_score:
- Builder liquidity support if treated as earnings recovery
- PF support without project cleanup
- Housing policy without starts/presales

thesis_break_watch:
- Taeyoung/PF restructuring
- GS E&C or any builder with quality/PF overhang
- HDC construction-quality reference

hard_4C_success:
- HDC / Gwangju construction-quality collapse reference
```

---

# 9. 점수비중 교정

## 올릴 축

```text
contract_value_vs_annual_backlog +5
project_margin_visibility +5
cash_collection_schedule +5
cost_overrun_delay_control +5
final_contract_signed_not_preferred_bidder +5
legal_appeal_clearance +4
housing_starts_presale_rate +5
PF_restructuring_completion +5
construction_quality_safety_trust +5
building_material_spread_visibility +4
```

### 근거

Samsung E&A는 contract value와 price reaction이 매우 강했으므로 `contract_value_vs_annual_backlog`와 `relative_strength`를 올린다. 하지만 Green까지 가려면 margin과 cash collection이 필요하다. Czech nuclear는 preferred bidder와 sector rerating은 강하지만, court/legal block이 실제로 있었으므로 `final_contract_signed_not_preferred_bidder`와 `legal_appeal_clearance`를 별도 gate로 둬야 한다. PF와 주택공급은 정책보다 `housing_starts_presale_rate`, `PF_restructuring_completion`이 핵심이다. HDC reference 때문에 `construction_quality_safety_trust`는 hard gate로 올린다.

## 내릴 축

```text
headline_order_without_margin -5
preferred_bidder_without_final_contract -5
policy_support_without_project_cashflow -5
housing_supply_headline_without_starts -4
PF_liquidity_without_impairment_cleanup -5
construction_material_demand_assumption_only -4
large_project_without_legal_clearance -4
```

### 근거

GS E&C는 package 수주만으로 Actionable까지 못 올린다. Czech nuclear는 preferred bidder만으로 Green을 주면 legal appeal 리스크를 놓친다. Taeyoung/PF와 builder support는 survival relief일 뿐 margin recovery가 아니다. Seoul housing supply는 착공·분양률이 없으면 Green이 아니다.

---

# 10. Stage 2-Actionable 승격 조건

R10 Loop 15 shadow rule:

```text
R10에서 Stage 2 evidence가 아래 중 3개 이상이면 Stage2-Actionable로 승격한다.

1. 계약금액이 회사 연간수주 또는 backlog 대비 의미 있게 크다.
2. 당일 market-relative +5pp 이상 가격반응이 있다.
3. 발주처·계약범위·완공시점이 구체적이다.
4. preferred bidder가 아니라 final signed contract 또는 award가 확인된다.
5. project margin / cash collection / cost overrun risk가 일부라도 설명된다.
6. 주택은 정책이 아니라 permits, starts, presale rate, unsold inventory absorption이 확인된다.
7. PF는 liquidity support가 아니라 restructuring terms와 impairment cleanup이 확인된다.
```

적용:

```text
Samsung E&A:
계약금액 + 가격반응 + 발주처/범위/완공시점 → Stage2-Actionable.

Czech nuclear:
preferred bidder + basket rerating은 Stage2-Actionable 가능하지만 legal 4B overlay.

Seoul housing:
아직 policy Stage2. permits/starts/presales 전에는 Actionable 보류.

Taeyoung/PF:
아직 4C-watch. restructuring terms 전에는 Actionable 아님.
```

---

# 11. Stage 3-Yellow 조건

```text
Stage3-Yellow:
- 건설/EPC trigger가 EPS/OP/FCF 경로를 바꿀 가능성이 숫자로 보임
- 하지만 margin, cash collection, cost overrun, legal appeal, PF cleanup 중 하나가 남아 있음
```

후보:

```text
Samsung E&A:
$6B Fadhili contract. 남은 gate: gross margin, cash collection, cost overrun.

Czech nuclear:
$18.7B signing. 남은 gate: listed-company work allocation, legal cleanup, payment schedule.

Housing supply:
400k homes / reconstruction simplification. 남은 gate: permits, starts, presales, PF.
```

---

# 12. Stage 3-Green 조건

```text
Stage3-Green:
- EPC 수주가 실제 backlog-to-OP로 전환됨
- margin/cash collection/cost overrun risk가 통제됨
- preferred bidder가 final contract와 subcontract allocation으로 닫힘
- housing policy가 actual starts/presales로 바뀜
- PF restructuring이 impairment cleanup and refinancing으로 마무리됨
- construction quality/safety overhang이 해소됨
- full-window MFE/MAE가 우호적
```

이번 R10 Loop 15에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- preferred bidder만으로 원전/인프라 basket이 크게 rerating
- 대형 EPC 수주가 margin 없이 가격만 먼저 오름
- 정부 유동성 지원으로 builder가 급등하지만 PF impairment가 남아 있음
- 주택공급 정책으로 developer가 오르지만 착공/분양이 없음
- 품질사고 이후 relief headline만으로 반등
```

적용:

```text
Czech nuclear:
preferred bidder → legal appeal → final signing. legal 4B overlay 필수.

Samsung E&A:
대형수주는 좋지만 cost overrun/cash collection 전에는 4B-watch.

Taeyoung/PF:
지원책으로 살아나는 듯 보일 때 false-positive watch.

Housing supply:
policy headline은 4B-watch. actual starts 전에는 Green 금지.
```

---

# 14. 4C hard gate 조건

```text
R10 4C:
- 붕괴/사망/중대 품질사고
- 영업정지 / 인허가 제한 / 브랜드 신뢰 훼손
- PF default / workout / debt restructuring
- project cancellation / legal block / final contract failure
- cost overrun causing margin collapse
- 미분양 급증 / presale failure
- 건자재 ASP collapse / spread collapse
```

이번 R10 Loop 15 hard 4C:

```text
HDC Gwangju Hwajeong I-Park collapse = hard_4C_success reference
```

Strong 4C-watch:

```text
- Taeyoung/PF restructuring
- Czech nuclear legal appeal before final signing
- Hyundai Steel rebar demand decline
- any builder with domestic PF/quality overhang
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_233.md 요약

```md
# R10 Loop 15. Construction / Real Estate / Building Materials Trigger-level Price Validation

이번 라운드는 R10 Loop 15 trigger-level validation 라운드다.

핵심 결론:
- Samsung E&A / Fadhili is the cleanest Stage2-Actionable case. Samsung E&A signed an around $6B Saudi Aramco Fadhili contract; shares rose as much as 8.5% to KRW26,750 while KOSPI fell 1.4%. The contract is large versus Samsung E&A’s 2017~2023 average annual contract wins of KRW8.6T. Green requires margin, cash collection and cost-overrun visibility.
- GS E&C / Fadhili is Stage2 overseas EPC evidence but not actionable without GS-specific contract value and event return. Domestic PF/quality overlays should remain.
- Czech nuclear construction basket is Stage2-Actionable with legal 4B overlay. KHNP was picked as preferred bidder for two reactors; Doosan Enerbility rose 48%, KEPCO Plant S&E 14%, KEPCO E&C 41% over three months. Later legal blocks and EDF appeals showed why preferred bidder is not Green. Final signing of the 407B koruna / $18.7B deal is validation but listed-company work allocation remains.
- Taeyoung / PF restructuring is 4C-watch with policy relief. Korea prepared KRW40.6T support for SMEs/builders, but PF delinquency rose to 2.70% at end-2023 from 0.37% at end-2021. A KRW1T syndicated loan, expandable to KRW5T, is relief not Green.
- Seoul housing supply / reconstruction is Stage2 policy. Seoul house prices rose 0.76% in July 2024, fastest since December 2019, and the government planned 400k homes over six years. Later LTV cuts and transaction restrictions show mixed policy. Green requires starts, presales and PF repayment.
- HDC / Gwangju Hwajeong I-Park is hard construction-quality 4C reference. The 2022 collapse killed six workers and investigation pointed to faulty construction, substandard materials and unauthorized structural change.
- Hyundai Steel / rebar weak demand is building-material failed rerating. Rebar price was expected to fall 10%; 2024 net profit estimate was cut 73% to KRW215B; shares were down 1.2% at KRW29,000.
- Builder liquidity support is false-positive watch. Policy support can keep projects alive, but without project profitability, presales, PF cleanup and gross margin it is not Stage3.

Main calibration:
- Raise contract_value_vs_annual_backlog, project_margin_visibility, cash_collection_schedule, cost_overrun_delay_control, final_contract_signed_not_preferred_bidder, legal_appeal_clearance, housing_starts_presale_rate, PF_restructuring_completion, construction_quality_safety_trust, building_material_spread_visibility.
- Lower headline_order_without_margin, preferred_bidder_without_final_contract, policy_support_without_project_cashflow, housing_supply_headline_without_starts, PF_liquidity_without_impairment_cleanup, construction_material_demand_assumption_only, large_project_without_legal_clearance.
```

## docs/checkpoints/checkpoint_28a_round233_r10_loop15.md 요약

```md
# Checkpoint 28A Round 233 R10 Loop 15 Trigger-level Calibration

## 반영 내용
- R10 Loop 15 trigger-level validation을 수행했다.
- Samsung E&A Fadhili, GS E&C Fadhili participation, Czech nuclear basket, Taeyoung/PF restructuring, Seoul housing supply/reconstruction, HDC construction-quality hard 4C, Hyundai Steel rebar demand, builder liquidity support를 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 Reuters / WSJ / AP / MarketWatch의 reported event return과 event price anchor를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- 해외 EPC 수주는 contract value, relative strength, annual backlog relevance로 Stage2-Actionable을 판단한다.
- preferred bidder는 final signed contract와 legal clearance 전에는 Green 금지다.
- 주택공급 정책은 actual permits, starts, presales, PF repayment로 승격한다.
- builder liquidity support는 survival relief이며 earnings recovery가 아니다.
- 건설 품질·안전 사고는 R10 hard 4C로 처리한다.
```

## data/e2r_case_library/cases_r10_loop15_round233.jsonl 초안

```jsonl
{"case_id":"r10_loop15_samsung_ea_fadhili","symbol":"028050","company_name":"Samsung E&A","case_type":"Stage2_promote_candidate","primary_archetype":"OVERSEAS_EPC_MEGA_ORDER_STAGE2_ACTIONABLE","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable_to_Stage3-Yellow_candidate","price_validation":{"trigger_date":"2024-04-03","contract_value_usd_bn":6.0,"aramco_total_package_usd_bn":7.7,"event_mfe_pct":8.5,"event_price_high_krw":26750,"kospi_same_context_pct":-1.4,"market_relative_return_pp":9.9,"average_annual_contract_wins_2017_2023_krw_trn":8.6,"completion_target":"2027-11","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate","notes":"Large overseas EPC contract plus strong relative price reaction makes this Stage2-Actionable; Green requires margin/cashflow."}
{"case_id":"r10_loop15_gsenc_fadhili_overlay","symbol":"006360","company_name":"GS E&C","case_type":"success_candidate_stage2","primary_archetype":"OVERSEAS_EPC_MEGA_ORDER_STAGE2_ACTIONABLE","best_trigger":"T0/T1","stage_candidate":"Stage2_overseas_EPC_evidence","price_validation":{"trigger_date":"2024-04-02","aramco_total_package_usd_bn":7.7,"project_capacity_before_bcf_per_day":2.5,"project_capacity_after_bcf_per_day":4.0,"completion_target":"2027-11","company_specific_contract_value":"price_data_unavailable_after_deep_search","event_return":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_stage2","notes":"Consortium package evidence is Stage2; company-specific contract value, price reaction, margin and quality/PF overlay are missing."}
{"case_id":"r10_loop15_czech_nuclear_construction_basket","symbol":"034020/051600/052690/015760_readthrough","company_name":"Doosan Enerbility / KEPCO Plant S&E / KEPCO E&C / KEPCO-KHNP","case_type":"Stage2_promote_candidate_with_legal_4B","primary_archetype":"NUCLEAR_CONSTRUCTION_EXPORT_STAGE2_WITH_LEGAL_4B","best_trigger":"T1/T4","stage_candidate":"Stage2-Actionable + 4B-watch","price_validation":{"preferred_bidder_date":"2024-07-17","reactors_count":2,"preferred_bidder":"KHNP","first_major_overseas_nuclear_order_since":2009,"unit_cost_estimate_czk_bn":200,"doosan_3m_return_pct":48,"kepco_plant_se_3m_return_pct":14,"kepco_ec_3m_return_pct":41,"legal_block_date":"2024-10-30/2025-05-06","contract_signed_date":"2025-06-04","signed_contract_value_czk_bn":407,"signed_contract_value_usd_bn":18.7,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate","notes":"Preferred bidder and sector rerating are Actionable, but final contract, legal clearance and work allocation are required for Yellow/Green."}
{"case_id":"r10_loop15_taeyoung_pf_restructuring","symbol":"009410","company_name":"Taeyoung E&C / PF restructuring reference","case_type":"4c_watch_with_policy_relief","primary_archetype":"REAL_ESTATE_PF_RESTRUCTURING_4C_WATCH","best_trigger":"T0/T2","stage_candidate":"4C-watch","price_validation":{"debt_rescheduling_awareness_date":"2023-12","support_package_date":"2024-03-27","support_package_krw_trn":40.6,"pf_delinquency_end_2021_pct":0.37,"pf_delinquency_end_2023_pct":2.70,"syndicated_loan_initial_krw_trn":1.0,"syndicated_loan_max_krw_trn":5.0,"taeyoung_event_price":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","notes":"PF liquidity support is relief, not earnings recovery; impairment cleanup and restructuring terms are required."}
{"case_id":"r10_loop15_seoul_housing_supply_reconstruction","symbol":"000720/047040/006360/375500/housing_developer_basket","company_name":"Hyundai E&C / Daewoo E&C / GS E&C / DL E&C / housing developer basket","case_type":"success_candidate_stage2","primary_archetype":"HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_POLICY","best_trigger":"T1/T3","stage_candidate":"Stage2_policy_mixed","price_validation":{"seoul_price_july_2024_mom_pct":0.76,"fastest_since":"2019-12","planned_homes_over_6y":400000,"wealthy_district_transaction_permit_tightening":true,"ltv_cut_from_pct":50,"ltv_cut_to_pct":40,"state_land_supply":true,"reconstruction_regulation_simplification":true,"direct_basket_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_stage2","notes":"Housing supply/reconstruction policy is Stage2; actual permits, starts, presales and PF repayment are needed for Yellow."}
{"case_id":"r10_loop15_hdc_gwangju_quality_hard_4c","symbol":"294870","company_name":"HDC Hyundai Development","case_type":"hard_4c_reference","primary_archetype":"CONSTRUCTION_QUALITY_SAFETY_HARD_4C","best_trigger":"T0/T1","stage_candidate":"4C","price_validation":{"incident_date":"2022-01-11","fatalities":6,"incident":"Gwangju Hwajeong I-Park exterior wall collapse","investigation_findings":["faulty_construction_methods","substandard_building_materials","unauthorized_structural_change"],"direct_price_anchor":"price_data_unavailable_after_deep_search","hard_4c_confirmed":true},"score_price_alignment":"hard_4c_success","notes":"Construction safety/quality failure is R10 hard 4C and must override backlog or policy positives."}
{"case_id":"r10_loop15_hyundai_steel_rebar_weak_construction_demand","symbol":"004020","company_name":"Hyundai Steel / rebar building-material read-through","case_type":"failed_rerating_4c_watch","primary_archetype":"BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING","best_trigger":"T1","stage_candidate":"4C-watch","price_validation":{"trigger_date":"2024-06-21","entry_price_anchor_krw":29000,"event_return_pct":-1.2,"expected_rebar_price_decline_pct":-10,"net_profit_estimate_after_cut_krw_bn":215,"net_profit_estimate_cut_pct":-73,"target_price_after_krw":30000,"target_price_cut_pct":-14,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"failed_rerating","notes":"Weak construction-material demand and rebar ASP pressure are failed-rerating triggers."}
{"case_id":"r10_loop15_builder_liquidity_support_false_positive_watch","symbol":"builder_basket","company_name":"Korean builder liquidity support basket","case_type":"false_positive_watch","primary_archetype":"BUILDER_LIQUIDITY_SUPPORT_FALSE_POSITIVE_WATCH","best_trigger":"T0/T1","stage_candidate":"Stage2_relief","price_validation":{"support_package_2024_03_krw_trn":40.6,"additional_public_sector_investment_2024_h2_krw_trn":15,"pf_restructuring_ongoing":true,"direct_basket_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"false_positive_watch","notes":"Liquidity support is survival relief; project cashflow, presales, PF cleanup and margins are required for Stage3."}
```

## data/e2r_trigger_calibration/triggers_r10_loop15_round233.jsonl 초안

```jsonl
{"trigger_id":"r10l15_samsungea_fadhili_T1","case_id":"r10_loop15_samsung_ea_fadhili","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-03","evidence_available":"Samsung E&A signs around $6B Saudi Aramco Fadhili contract; shares +8.5% to KRW26,750 while KOSPI -1.4%","event_return_pct":8.5,"market_relative_return_pp":9.9,"trigger_outcome_label":"excellent_stage2_actionable","promote_to":"Stage3-Yellow_candidate"}
{"trigger_id":"r10l15_gsenc_fadhili_T0","case_id":"r10_loop15_gsenc_fadhili_overlay","trigger_type":"Stage2_evidence","trigger_date":"2024-04-02","evidence_available":"Aramco awards Fadhili EPC contracts to Samsung E&A, GS E&C and Nesma; $7.7B total package","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_evidence_not_actionable_without_company_price","promote_to":"Stage2"}
{"trigger_id":"r10l15_czech_nuclear_T1","case_id":"r10_loop15_czech_nuclear_construction_basket","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-17","evidence_available":"Czech government selects KHNP preferred bidder for two reactors; Doosan +48%, KEPCO Plant S&E +14%, KEPCO E&C +41% over three months","event_return_pct":"Doosan +48 / KEPCO PSE +14 / KEPCO E&C +41 over 3M","trigger_outcome_label":"Stage2_promote_candidate","promote_to":"Stage2-Actionable"}
{"trigger_id":"r10l15_czech_nuclear_T3","case_id":"r10_loop15_czech_nuclear_construction_basket","trigger_type":"4B-watch","trigger_date":"2025-05-06","evidence_available":"Czech court temporarily halts signing of $18B KHNP nuclear contract after EDF complaint","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"legal_4B_watch","promote_to":"4B-watch"}
{"trigger_id":"r10l15_taeyoung_pf_T2","case_id":"r10_loop15_taeyoung_pf_restructuring","trigger_type":"4C-watch","trigger_date":"2024-05-13","evidence_available":"FSS tightens PF restructuring; real estate PF delinquency rises to 2.70% end-2023 from 0.37% end-2021; 1T loan expandable to 5T","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"PF_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r10l15_seoul_housing_T1","case_id":"r10_loop15_seoul_housing_supply_reconstruction","trigger_type":"Stage2_policy","trigger_date":"2024-08-16","evidence_available":"Seoul home prices +0.76% in July 2024, fastest since Dec 2019; government plans 400k homes over six years","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"success_candidate_stage2_policy","promote_to":"Stage2"}
{"trigger_id":"r10l15_hdc_gwangju_T0","case_id":"r10_loop15_hdc_gwangju_quality_hard_4c","trigger_type":"hard_4C","trigger_date":"2022-01-11","evidence_available":"Gwangju Hwajeong I-Park exterior wall collapse kills six; faulty construction and substandard materials later identified","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"hard_4c_success","promote_to":"4C"}
{"trigger_id":"r10l15_hyundai_steel_rebar_T1","case_id":"r10_loop15_hyundai_steel_rebar_weak_construction_demand","trigger_type":"failed_rerating","trigger_date":"2024-06-21","evidence_available":"Rebar price expected -10%, net profit estimate cut 73% to KRW215B, target cut 14%, shares -1.2% at KRW29,000","event_return_pct":-1.2,"trigger_outcome_label":"failed_rerating_4C_watch","promote_to":"4C-watch"}
```

## data/sector_taxonomy/score_weight_profiles_round233_r10_loop15_v1.csv 초안

```csv
archetype,contract_value_vs_annual_backlog,project_margin_visibility,cash_collection_schedule,cost_overrun_delay_control,final_contract_signed_not_preferred_bidder,legal_appeal_clearance,housing_starts_presale_rate,pf_restructuring_completion,construction_quality_safety_trust,building_material_spread_visibility,headline_order_without_margin_penalty,preferred_bidder_without_final_contract_penalty,policy_support_without_project_cashflow_penalty,housing_supply_headline_without_starts_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
OVERSEAS_EPC_MEGA_ORDER_STAGE2_ACTIONABLE,+5,+5,+5,+5,+4,+3,+0,+1,+3,+1,-5,-2,-2,-1,contract value+relative strength,margin/cash collection pending,backlog-to-OP+cash conversion,Samsung E&A Fadhili template.
NUCLEAR_CONSTRUCTION_EXPORT_STAGE2_WITH_LEGAL_4B,+4,+4,+4,+5,+5,+5,+0,+0,+4,+1,-4,-5,-2,-1,preferred bidder+sector rerating,final contract/legal/work split pending,contract+work allocation+margin,Czech nuclear basket.
REAL_ESTATE_PF_RESTRUCTURING_4C_WATCH,+0,+2,+4,+3,+0,+0,+3,+5,+3,+2,-2,-1,-5,-3,PF stress/support,impairment cleanup pending,PF cleanup+cashflow recovery,Taeyoung/PF template.
HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_POLICY,+0,+3,+3,+2,+0,+0,+5,+4,+3,+2,-1,-1,-4,-5,supply policy/reconstruction,starts/presales pending,starts+presales+margin,Seoul housing policy Stage2.
CONSTRUCTION_QUALITY_SAFETY_HARD_4C,+0,+1,+2,+5,+0,+0,+1,+2,+5,+1,-1,-1,-1,-1,safety/quality incident,trust recovery pending,safety cleared+orders recovered,HDC hard 4C reference.
BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING,+0,+3,+2,+2,+0,+0,+4,+2,+2,+5,-2,-1,-2,-2,rebar/ASP demand cut,spread recovery pending,ASP+volume+spread recovery,Hyundai Steel rebar weak-demand case.
BUILDER_LIQUIDITY_SUPPORT_FALSE_POSITIVE_WATCH,+0,+2,+4,+2,+0,+0,+3,+5,+3,+2,-2,-1,-5,-4,liquidity support,project cashflow pending,PF cleanup+margin recovery,Builder policy relief false-positive watch.
```

---

# 이번 R10 Loop 15 결론

```text
1. Samsung E&A / Fadhili는 R10의 가장 강한 Stage2-Actionable case다.
   $6B 수주, +8.5%, KOSPI -1.4%, 연간수주잔고 대비 크기가 닫혔다.

2. GS E&C / Fadhili는 Stage2 evidence지만 Actionable 확정은 아니다.
   GS-specific 계약금액과 가격반응, margin 정보가 부족하다.

3. Czech nuclear basket은 Stage2-Actionable + legal 4B다.
   preferred bidder와 sector rally는 강하지만, legal appeal과 final contract/work split이 gate다.

4. Taeyoung/PF restructuring은 4C-watch다.
   KRW40.6T support와 KRW1T~5T loan은 relief일 뿐, PF cleanup이 핵심이다.

5. Seoul housing supply/reconstruction은 Stage2 policy다.
   가격 반등과 공급정책은 좋지만, 실제 착공·분양률·PF 상환 전에는 Green이 아니다.

6. HDC / Gwangju collapse는 R10 hard 4C다.
   건설 품질·안전은 수주잔고보다 우선 차감되는 hard gate다.

7. Hyundai Steel rebar weak demand는 건자재 failed rerating이다.
   rebar ASP와 net-profit estimate가 동시에 깨지면 건설경기 score를 낮춰야 한다.

8. Builder liquidity support는 false-positive watch다.
   유동성 지원은 생존장치이지, 이익경로 변화가 아니다.
```

한 문장으로 압축하면:

> **R10 Loop 15에서 배운 핵심은 “수주·정책·공급 headline”이 아니라, 계약금액 대비 backlog, margin, cash collection, legal clearance, 착공·분양률, PF cleanup, 품질·안전 신뢰가 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 preferred bidder, 유동성 지원, 주택공급 정책, 대형수주 headline만으로는 4B/false positive가 되기 쉽다.**

[1]: https://www.reuters.com/markets/commodities/aramco-awards-77-bln-contracts-fadhili-gas-expansion-2024-04-02/?utm_source=chatgpt.com "Aramco awards $7.7 bln in contracts for Fadhili gas expansion"
[2]: https://www.wsj.com/articles/samsung-e-a-shares-rise-on-6-billion-saudi-contract-win-10a5b2f4?utm_source=chatgpt.com "Samsung E&A Shares Rise on $6 Billion Saudi Contract Win"
[3]: https://www.reuters.com/business/energy/south-koreas-winning-bid-czech-nuclear-power-project-2024-07-17/?utm_source=chatgpt.com "South Korea's winning bid for Czech nuclear power project"
[4]: https://www.reuters.com/sustainability/boards-policy-regulation/czech-court-halts-nuclear-plant-signing-with-khnp-after-last-minute-appeal-2025-05-06/?utm_source=chatgpt.com "Czech court halts nuclear plant signing with KHNP after last-minute appeal"
[5]: https://www.reuters.com/markets/asia/south-korea-prepares-financial-support-small-businesses-builders-2024-03-27/?utm_source=chatgpt.com "South Korea prepares financial support for small businesses, builders"
[6]: https://www.reuters.com/markets/asia/south-korea-tightens-scrutiny-speed-up-real-estate-restructuring-2024-05-13/?utm_source=chatgpt.com "South Korea tightens scrutiny to speed up real estate restructuring"
[7]: https://www.reuters.com/markets/asia/home-prices-seoul-rise-fastest-pace-more-than-4-years-2024-08-16/?utm_source=chatgpt.com "Home prices in Seoul rise at fastest pace in more than 4 years"
[8]: https://www.reuters.com/markets/asia/south-korea-tighten-apartment-trading-rules-wealthy-seoul-districts-2025-03-19/?utm_source=chatgpt.com "South Korea to tighten apartment trading rules in wealthy Seoul districts"
[9]: https://en.wikipedia.org/wiki/Gwangju_Hwajeong_I-Park_exterior_wall_collapse?utm_source=chatgpt.com "Gwangju Hwajeong I-Park exterior wall collapse"
[10]: https://www.marketwatch.com/story/hyundai-steel-s-2024-earnings-could-be-hit-by-weak-demand-market-talk-bcbe77c8?utm_source=chatgpt.com "Hyundai Steel's 2024 Earnings Could Be Hit by Weak Demand -- Market Talk"
