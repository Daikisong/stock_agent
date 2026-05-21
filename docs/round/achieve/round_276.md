순서상 이번은 **R7 Loop 13 — 바이오·헬스케어·의료기기 가격경로 검증 라운드**다.

```text
round = R7 Loop 13
round_id = round_204
large_sector = BIO_HEALTHCARE_MEDICAL_DEVICE
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = false
hard_4c_reference_confirmed = true_for_vaccine_demand_and_regulatory_quality
next_round = R8 Loop 13
```

이번 R7 Loop 13은 **Yuhan lazertinib, Alteogen/Merck SC Keytruda, Samsung Biologics·Celltrion·SK Bioscience의 tariff/CDMO 대응, Jeisys Medical aesthetics device, 제약업종 tariff-policy rally, SK Bioscience SkyCovione demand failure**를 중심으로 봤다.

이번에도 KRX/Naver/Yahoo/Stooq의 **수정주가 일봉 전체 구간**은 안정적으로 확보하지 못했다. 그래서 30D/90D/180D full OHLC를 임의로 만들지 않고, Reuters / WSJ / MarketWatch / FT / Barron’s / 공개 백과형 소스가 제공한 **event price, event return, FDA 승인·CRL·계약·M&A·시설투자·IPO·수요부진 anchor**만 계산했다. full OHLC가 필요한 칸은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R7 = 바이오·헬스케어·의료기기
```

R7에서 진짜 Stage 3는 “FDA 승인”, “CDMO 공장”, “AI 의료”, “미용기기”, “신약 후보”, “미국 생산시설”, “정책지원”, “바이오 수출”이라는 말이 아니다.

진짜 Stage 3는 **허가 → 실제 처방/판매 → royalty·milestone·CMO 매출 인식 → gross margin / OP / FCF → 생산시설 utilization → 규제·임상·품질·수요 리스크 통과**가 같이 닫히는 순간이다.

---

# 2. 대상 canonical archetype

```text
KOREAN_ORIGIN_DRUG_GLOBAL_APPROVAL
PLATFORM_TECH_ENZYME_ROYALTY_OPTIONALITY
CDMO_US_TARIFF_HEDGE_STAGE2
BIOPHARMA_US_FACTORY_TARIFF_HEDGE
VACCINE_CDMO_M_AND_A_STAGE2
AESTHETIC_MEDICAL_DEVICE_PE_TAKEOUT
BIOPHARMA_POLICY_RALLY_EVENT_PREMIUM
VACCINE_DEMAND_COLLAPSE_HARD_REFERENCE
```

---

# 3. deep sub-archetype

```text
신약 글로벌 승인:
- Yuhan / lazertinib / Leclaza-Lazcluze
- J&J Rybrevant + lazertinib
- FDA first-line EGFR-mutated NSCLC approval
- peak sales / royalty / actual launch / prescription ramp

플랫폼 기술:
- Alteogen / hyaluronidase enzyme
- Merck SC Keytruda
- Keytruda patent cliff hedge
- 2-minute injection vs 30-minute infusion
- 30~40% adoption expectation
- Halozyme patent challenge

CDMO / tariff hedge:
- Samsung Biologics / GSK Rockville facility
- Celltrion / Eli Lilly ImClone facility
- U.S. pharmaceutical tariff risk
- plant utilization / customer transfer / margin / capex

Vaccine CDMO:
- SK Bioscience / IDT Biologika
- post-COVID vaccine demand reset
- European CDMO entry
- M&A pop vs integration and utilization

의료기기:
- Jeisys Medical / energy-based aesthetics device
- ArchiMed take-private
- revenue CAGR / earnings CAGR
- global aesthetics market growth

정책 rally:
- Korean pharma sector jumps on government support against U.S. tariffs
- Samsung Biologics +6.23%, Celltrion +0.35%
- policy relief vs company earnings bridge

Vaccine demand hard reference:
- SK Bioscience SkyCovione
- 10M doses purchased, 600k released, only 3,787 shots
- production suspended / unused doses likely discarded
```

---

# 4. 국장 신규 후보 case

## Case A — Yuhan / lazertinib `success_candidate`

```text
symbol = 000100
case_type = success_candidate
archetype = KOREAN_ORIGIN_DRUG_GLOBAL_APPROVAL
```

### stage date

```text
Stage 1:
2024-08-20
- J&J Rybrevant + lazertinib FDA approval
- EGFR-mutated NSCLC first-line chemotherapy-free regimen
- Korean-origin drug reaches U.S. first-line lung-cancer market

Stage 2:
2024-08-20
- FDA approves Rybrevant + Lazcluze/lazertinib
- EGFR mutation occurs in 10~15% of U.S. NSCLC cases
- late-stage data showed longer progression-free survival versus AstraZeneca Tagrisso
- J&J expects Rybrevant to generate more than $5B peak sales

Stage 3:
보류
- FDA approval is strong, but Yuhan Green requires royalty/milestone recognition, actual prescription ramp, J&J launch performance, margin visibility

Stage 4C-watch:
2024-12-16
- FDA declined to approve subcutaneous Rybrevant version
- CRL tied to manufacturing facility inspection observations, not efficacy/safety
- no additional clinical studies requested
- IV Rybrevant + lazertinib approval remains intact
```

Yuhan은 이번 R7의 가장 좋은 신약 글로벌 승인 후보지만, FDA 승인 하나만으로 Stage 3를 확정하지 않는다. Reuters는 J&J의 Rybrevant+lazertinib 조합이 EGFR 변이 NSCLC 1차 치료로 FDA 승인을 받았고, J&J가 Rybrevant peak sales를 $5B 이상으로 기대한다고 보도했다. 다만 Yuhan의 실제 Stage 3는 J&J launch가 처방·royalty·milestone·현금흐름으로 내려오는 순간이다. 이후 subcutaneous Rybrevant CRL은 효능 문제가 아니라 제조시설 inspection 문제였고, IV 조합 승인은 유지됐지만, 상업적 편의성 ramp에는 watch를 붙인다. ([Reuters][1])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters / MarketWatch FDA approval and CRL anchors",
  "entry_date": "N/A",
  "stage3_price": null,
  "fda_approval_date": "2024-08-20",
  "approved_combo": "Rybrevant + lazertinib / Lazcluze",
  "indication": "first-line EGFR-mutated NSCLC",
  "egfr_mutation_share_us_nsclc_pct": "10-15",
  "jnj_expected_rybrevant_peak_sales_usd_bn": 5,
  "marketwatch_phase3_risk_reduction_pct": 30,
  "trial_patient_count_marketwatch": 1074,
  "subcutaneous_rybrevant_crl_date": "2024-12-16",
  "crl_cause": "pre-approval manufacturing facility inspection observations",
  "additional_clinical_studies_requested": false,
  "yuhan_stock_ohlc": "price_data_unavailable_after_deep_search",
  "mfe_30d_90d_180d_1y_2y": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_but_price_data_unavailable
rerating_result = Korean_origin_drug_global_approval_stage2
stage_failure_type = FDA_approval_not_royalty_cashflow_green
```

---

## Case B — Alteogen / Merck SC Keytruda `structural_success_candidate + patent 4C-watch`

```text
symbol = 196170
case_type = structural_success_candidate + 4B-watch + 4C-watch
archetype = PLATFORM_TECH_ENZYME_ROYALTY_OPTIONALITY
```

### stage date

```text
Stage 1:
2024-11-19
- Merck says injectable Keytruda is non-inferior to IV version
- Alteogen enzyme used with SC Keytruda
- 2~3 minute administration vs 30-minute IV infusion
- Keytruda patent cliff hedge

Stage 2:
2025-03-27
- Merck plans U.S. SC Keytruda launch on 2025-10-01 if FDA approves
- FDA decision target 2025-09-23
- expected peak adoption at least 30~40% of Keytruda patients within two years
- Keytruda nearly $30B 2024 sales
- Alteogen develops/manufactures enzyme used with SC formulation

Stage 4B:
2024~2025
- Alteogen market-cap surge / KOSDAQ leadership context, but full OHLC unavailable

Stage 4C-watch:
2025
- potential Halozyme patent challenge
- Merck says it will not delay launch and believes its position is strong
```

Alteogen은 R7에서 플랫폼 기술의 핵심 후보이다. Reuters는 Merck의 SC Keytruda가 IV 제형과 비열등성을 보였고, SC 제형이 2~3분 투여로 기존 30분 IV infusion보다 훨씬 짧다고 보도했다. 2025년 Reuters 보도에서는 Merck가 FDA 결정 target을 2025년 9월 23일로 보고 10월 1일 출시를 준비하며, SC Keytruda peak adoption을 Keytruda 환자의 30~40%로 기대한다고 밝혔다. Keytruda 2024 매출은 거의 $30B였고, Alteogen은 해당 SC formulation에 쓰이는 enzyme을 개발·제조한다. 다만 Halozyme patent dispute와 실제 royalty 인식 전에는 Green 확정이 아니다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters / WSJ SC Keytruda trial, launch and patent anchors",
  "entry_date": "N/A",
  "stage3_price": null,
  "keytruda_2024_sales_usd_bn": 30,
  "sc_keytruda_expected_adoption_pct": "30-40",
  "sc_injection_time_minutes": "2-3",
  "iv_infusion_time_minutes": 30,
  "time_reduction_low_pct": 90,
  "fda_decision_target": "2025-09-23",
  "planned_us_launch_date": "2025-10-01",
  "merck_premarket_reaction_to_noninferiority_pct": 1.8,
  "wsj_sc_keytruda_sales_prediction_usd_bn": 6,
  "patent_challenge_watch": "Halozyme",
  "alteogen_direct_ohlc": "price_data_unavailable_after_deep_search",
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = structural_success_candidate_but_4B_and_patent_watch
rerating_result = platform_enzyme_royalty_optionality
stage_failure_type = platform_option_not_royalty_cashflow_green
```

---

## Case C — Samsung Biologics / GSK Rockville facility `success_candidate + event_failed_price`

```text
symbol = 207940
case_type = success_candidate + evidence_good_but_price_failed
archetype = CDMO_US_TARIFF_HEDGE_STAGE2
```

### stage date

```text
Stage 1:
2025-05-21
- Korean pharma sector policy support against U.S. tariff risk
- Samsung Biologics FDA inspection / export-tariff concern
- domestic biopharma manufacturing becomes strategic sector

Stage 2:
2025-12-22
- Samsung Biologics acquires first U.S. drug production facility from GSK
- $280M deal
- 100% stake in Human Genome Sciences Inc., Rockville, Maryland
- facility has 60,000L drug substance capacity
- deal expected to close around end-Q1 2026
- Samsung Biologics shares -0.4%, KOSPI +2%

Stage 3:
없음
- facility acquisition is Stage 2
- utilization, customer transfer, FDA inspection, margin, capex, FCF 확인 전 Green 금지
```

Samsung Biologics는 R7 CDMO의 좋은 Stage 2다. GSK로부터 Rockville facility를 $280M에 사들이며 U.S. manufacturing footprint를 확보했지만, 발표 당일 주가는 -0.4%였고 KOSPI는 +2%였다. 시장은 “미국 공장” 자체보다 시설 활용률, 고객 이전, 규제검사, margin, 추가 투자비를 기다린 것이다. ([Reuters][3])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters GSK facility acquisition and sector-support anchors",
  "entry_date": "N/A",
  "stage3_price": null,
  "facility_acquisition_usd_mn": 280,
  "facility_location": "Rockville, Maryland",
  "acquired_entity": "Human Genome Sciences Inc.",
  "stake_acquired_pct": 100,
  "drug_substance_capacity_liters": 60000,
  "expected_close": "around end-Q1 2026",
  "event_mae_pct": -0.4,
  "kospi_same_context_pct": 2.0,
  "relative_underperformance_pp": -2.4,
  "facility_utilization_confirmed": false,
  "customer_transfer_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed
rerating_result = CDMO_US_tariff_hedge_stage2
stage_failure_type = facility_acquisition_not_utilization_margin_green
```

---

## Case D — Celltrion / U.S. factory tariff hedge `success_candidate`

```text
symbol = 068270
case_type = success_candidate
archetype = BIOPHARMA_US_FACTORY_TARIFF_HEDGE
```

### stage date

```text
Stage 1:
2025-05~2025-07
- U.S. pharmaceutical tariff risk
- Korean biosimilar exporters consider U.S. production
- Celltrion postpones and then resumes U.S. manufacturing decision path

Stage 2:
2025-07-29
- Celltrion becomes preferred bidder for U.S. pharma manufacturing facility
- planned 700B won investment for acquisition/operation
- possible additional 300B~700B won depending on tariff policy

Stage 2 validation:
2025-09-23
- Celltrion U.S. subsidiary acquires ImClone Systems LLC from Eli Lilly for $330M
- intended to protect U.S. product lines and future launches from tariff exposure

Stage 2 추가:
2025-11-19
- Celltrion plans up to 700B won / $478M expansion at U.S. factory

Stage 3:
없음
- U.S. factory acquisition and expansion are Stage 2
- product transfer, regulatory approval, utilization, margin, tariff saving, FCF 필요
```

Celltrion은 Samsung Biologics와 같은 U.S. manufacturing hedge 구조다. Reuters는 Celltrion이 미국 공장 인수를 위해 7000억 원 투자 계획을 세웠고, 이후 Eli Lilly의 ImClone Systems를 $330M에 인수했다고 보도했다. 11월에는 미국 공장 증설에 최대 7000억 원을 투자한다고 밝혔다. 하지만 Green은 plant acquisition이 아니라 **제품 이전, 생산허가, utilization, tariff saving, margin**이 확인될 때다. ([Reuters][4])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters Celltrion U.S. factory acquisition and expansion anchors",
  "stage3_price": null,
  "preferred_bidder_investment_plan_krw_bn": 700,
  "possible_additional_investment_krw_bn": "300-700",
  "imclone_acquisition_usd_mn": 330,
  "us_factory_expansion_max_krw_bn": 700,
  "us_factory_expansion_max_usd_mn": 478.17,
  "tariff_driver": "U.S. pharmaceutical tariff risk",
  "product_transfer_confirmed": false,
  "utilization_confirmed": false,
  "margin_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_but_price_data_unavailable
rerating_result = biopharma_US_factory_tariff_hedge_stage2
stage_failure_type = acquisition_expansion_not_product_transfer_margin_green
```

---

## Case E — SK Bioscience / IDT Biologika `success_candidate + M&A event premium`

```text
symbol = 302440
case_type = success_candidate + event_premium
archetype = VACCINE_CDMO_M_AND_A_STAGE2
```

### stage date

```text
Stage 1:
2024-06-27
- SK Bioscience moves beyond post-COVID vaccine cycle
- CDMO / vaccine manufacturing expansion into Europe
- SK Group business rebalancing context

Stage 2:
2024-06-27
- SK Bioscience to acquire 60% stake in Germany’s IDT Biologika
- deal value 339B won / $243.75M
- Klocke retains 40%
- first major M&A since 2021 IPO
- SK Bioscience shares +11.7% in morning trading

Stage 3:
없음
- acquisition is Stage 2
- integration, order book, fill-finish utilization, vaccine pipeline, margin, FCF 확인 필요

Stage 4B:
2024-06-27
- +11.7% M&A pop before utilization/order book proof
```

SK Bioscience는 post-COVID vaccine company에서 European CDMO로 전환하려는 Stage 2다. IDT Biologika 60% 인수는 3390억 원 규모이고, announcement day에 주가는 +11.7% 뛰었다. 하지만 과거 vaccine demand collapse가 있었기 때문에, Green은 acquisition이 아니라 **order book, utilization, margin, recurring CDMO contracts**로만 가능하다. ([Reuters][5])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters SK Bioscience / IDT Biologika deal anchor",
  "stage3_price": null,
  "idt_stake_acquired_pct": 60,
  "deal_value_krw_bn": 339,
  "deal_value_usd_mn": 243.75,
  "klocke_remaining_stake_pct": 40,
  "ipo_context": "first_major_M&A_since_2021_IPO",
  "ipo_raise_2021_usd_bn": 1.33,
  "event_mfe_pct": 11.7,
  "order_book_confirmed": false,
  "utilization_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_success_candidate
rerating_result = vaccine_CDMO_MA_stage2
stage_failure_type = acquisition_not_utilization_revenue_green
```

---

## Case F — Jeisys Medical / ArchiMed take-private `success_candidate + takeout event`

```text
symbol = Jeisys Medical, formerly publicly traded
case_type = success_candidate + event_premium
archetype = AESTHETIC_MEDICAL_DEVICE_PE_TAKEOUT
```

### stage date

```text
Stage 1:
2024-06~2024-09
- Korea aesthetics medical-device export
- energy-based devices / EBD
- non-invasive anti-aging treatment demand

Stage 2:
2024-09-11
- ArchiMed acquires Jeisys Medical for about $742M
- Jeisys shares closed 12,860 won before delisting process context
- founder reinvests more than half of stake
- revenue rose 44% annually to $107M over three years through FY2023
- adjusted pretax earnings rose 45% annually to $31M
- global EBD market projected >$16B by 2032 from ~$4.5B previous year

Stage 3:
없음
- take-private and PE validation are Stage 2
- listed investor Green impossible after delisting path
- for peer scoring, need export sell-through, consumables/service revenue, margin, reorder, clinic utilization
```

Jeisys Medical은 R7 의료기기에서 좋은 benchmark다. WSJ는 ArchiMed가 Jeisys를 약 $742M에 인수하며 아시아 첫 deal을 완료했고, Jeisys의 3년 매출 CAGR이 44%, adjusted pretax earnings CAGR이 45%라고 보도했다. 이건 aesthetics EBD 산업의 real revenue/earnings benchmark지만, listed investor 관점에서는 take-private event라 Stage 3 trading row로는 쓰기 어렵다. Peer scoring에는 **clinic utilization, export sell-through, consumables/service revenue** 축을 올리는 데 쓴다. ([월스트리트저널][6])

### 실제 가격경로 검증

```json
{
  "price_data_source": "WSJ Jeisys / ArchiMed take-private anchor",
  "stage3_price": null,
  "take_private_value_usd_mn": 742,
  "pre_delisting_close_price_krw": 12860,
  "revenue_fy2023_usd_mn": 107,
  "revenue_cagr_3y_pct": 44,
  "adjusted_pretax_earnings_fy2023_usd_mn": 31,
  "adjusted_pretax_earnings_cagr_3y_pct": 45,
  "pretax_margin_fy2023_pct": 29.0,
  "global_ebd_market_previous_year_usd_bn": 4.5,
  "global_ebd_market_2032_usd_bn": 16,
  "global_ebd_market_growth_to_2032_pct": 255.6,
  "listed_status_after_deal": "delisting_process",
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_takeout_event
rerating_result = aesthetic_medical_device_revenue_earnings_benchmark
stage_failure_type = take_private_not_tradeable_stage3
```

---

## Case G — Pharma tariff-support rally `event_premium / policy relief`

```text
symbols = 207940 / 068270 / pharma sector basket
case_type = event_premium + policy_relief
archetype = BIOPHARMA_POLICY_RALLY_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2025-05-20
- U.S. tariffs weigh on Korean export sectors
- government pledges support for biopharma and autos
- pharmaceutical exports to U.S. become policy issue

Stage 2:
2025-05-21
- KOSPI +0.99% to 2,627.63
- pharmaceutical sector +3.97%
- Samsung Biologics +6.23%
- Celltrion +0.35%
- foreigners net-buy 113.7B won
- Korean pharmaceutical exports 2024: $9.59B
- 16% shipped to U.S.

Stage 3:
없음
- government support and sector rally are policy relief
- company Green requires tariff exemption, U.S. production plan, margin, product demand, FCF
```

이 case는 R7의 policy event premium이다. 정부가 biopharma support를 약속하자 제약업종이 +3.97%, Samsung Biologics가 +6.23% 올랐다. 하지만 이것은 policy relief이지 Stage 3가 아니다. 실제 Green은 tariff exposure가 margin·FCF로 안정되는지, U.S. production이 비용을 감당하는지로 확인한다. ([Reuters][7])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters Korea market / policy-support anchors",
  "stage3_price": null,
  "kospi_event_mfe_pct": 0.99,
  "kospi_event_close": 2627.63,
  "pharma_sector_mfe_pct": 3.97,
  "samsung_biologics_mfe_pct": 6.23,
  "celltrion_mfe_pct": 0.35,
  "foreign_net_buy_krw_bn": 113.7,
  "pharmaceutical_exports_2024_usd_bn": 9.59,
  "us_export_share_pct": 16,
  "implied_us_pharma_exports_2024_usd_bn": 1.53,
  "tariff_exemption_confirmed": false,
  "company_margin_bridge_confirmed": false
}
```

### alignment

```text
score_price_alignment = event_premium_policy_relief
rerating_result = biopharma_tariff_support_stage2
stage_failure_type = policy_relief_not_company_margin_green
```

---

## Case H — SK Bioscience SkyCovione `vaccine demand-collapse hard reference`

```text
symbol = 302440
case_type = failed_rerating_reference
archetype = VACCINE_DEMAND_COLLAPSE_HARD_REFERENCE
```

### stage date

```text
Stage 1:
2022-06
- Korea’s first domestic COVID-19 vaccine approval
- government procurement support
- pandemic vaccine sovereignty narrative

Stage 4C-reference:
2022-11
- production indefinitely suspended because of low demand
- government bought 10M doses
- 600,000 doses released to hospitals
- only 3,787 shots administered as of November 2022
- unused doses likely to be discarded

Stage 4C-reference 추가:
2023-09 / 2024-05
- EU marketing authorization application withdrawn
- WHO emergency-use listing later delisted in May 2024

Stage 3:
없음
- approval and government procurement did not become demand
```

SK Bioscience SkyCovione은 R7에서 백신 수요 hard reference로 사용한다. 승인과 정부 구매가 있어도 실제 접종 수요가 없으면 Stage 3는 아니다. 공개 자료는 정부가 1000만 도스를 구매했고 60만 도스가 병원에 배포됐지만, 2022년 11월 기준 접종은 3,787회뿐이었다고 정리한다. 이 case는 R7에서 `approval/procurement ≠ demand`를 강하게 박아야 한다. ([위키백과][8])

### 실제 가격경로 검증

```json
{
  "price_data_source": "public vaccine-demand-collapse reference",
  "stage3_price": null,
  "government_purchase_doses_mn": 10,
  "released_to_hospitals_doses": 600000,
  "administered_shots": 3787,
  "administered_share_of_released_pct": 0.63,
  "administered_share_of_purchased_pct": 0.038,
  "production_status": "indefinitely_suspended_due_low_demand",
  "unused_doses_likely_discarded": true,
  "eu_authorization_application_withdrawn": "2023-09",
  "who_eul_delisted": "2024-05",
  "direct_stock_ohlc": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = failed_rerating_reference
rerating_result = vaccine_approval_procurement_not_demand
stage_failure_type = demand_collapse_reference
```

---

# 5. 이번 R7 case별 stage date 요약

| case                     | Stage 1       | Stage 2                 | Stage 3 | Stage 4B                      | Stage 4C                          |
| ------------------------ | ------------- | ----------------------- | ------- | ----------------------------- | --------------------------------- |
| Yuhan / lazertinib       | 2024-08-20    | 2024-08-20              | 보류      | royalty ramp watch            | 2024-12-16 SC Rybrevant CRL watch |
| Alteogen / SC Keytruda   | 2024-11-19    | 2025-03-27              | 보류      | KOSDAQ platform premium watch | Halozyme patent watch             |
| Samsung Biologics        | 2025-12-22    | 2025-12-22              | N/A     | U.S. facility theme watch     | facility utilization/FDA watch    |
| Celltrion                | 2025-07~09    | 2025-09-23 / 2025-11-19 | N/A     | tariff hedge watch            | capex/utilization watch           |
| SK Bioscience / IDT      | 2024-06-27    | 2024-06-27              | N/A     | 2024-06-27 +11.7%             | integration/utilization watch     |
| Jeisys Medical           | 2024-09-11    | 2024-09-11              | N/A     | take-private event            | delisting / tradeability issue    |
| Pharma policy rally      | 2025-05-21    | 2025-05-21              | N/A     | sector rally                  | tariff margin watch               |
| SK Bioscience SkyCovione | 2022 approval | procurement             | N/A     | N/A                           | demand-collapse reference         |

---

# 6. 실제 가격경로 검증 총괄

| case                |                                                         anchor | MFE / MAE 해석                                 | 판정                   |
| ------------------- | -------------------------------------------------------------: | -------------------------------------------- | -------------------- |
| Yuhan / lazertinib  |                    J&J peak Rybrevant sales >$5B, FDA approval | clinical success, Yuhan price unavailable    | success_candidate    |
| Alteogen            | Keytruda nearly $30B, SC adoption 30~40%, Merck +1.8% on trial | platform option strong, royalty proof needed | structural_candidate |
| Samsung Bio         |              $280M facility, 60,000L, stock -0.4% vs KOSPI +2% | evidence good but price failed               | Stage 2              |
| Celltrion           |                       $330M ImClone + up to 700B won expansion | tariff hedge, no margin bridge               | Stage 2              |
| SK Bioscience / IDT |                                               339B won, +11.7% | M&A pop before utilization                   | event premium        |
| Jeisys              |         $742M take-private, 12,860 won close, 44% revenue CAGR | real device benchmark, not tradable Stage 3  | takeout benchmark    |
| Pharma policy rally |                              pharma +3.97%, Samsung Bio +6.23% | policy event premium                         | event_premium        |
| SkyCovione          |                           10M bought, 3,787 shots administered | approval/procurement failed demand           | failed reference     |

---

# 7. score-price alignment 판정

```text
structural_success_candidate:
- Alteogen / SC Keytruda
- Yuhan / lazertinib
- Jeisys Medical as revenue/earnings benchmark, but take-private

success_candidate:
- Samsung Biologics U.S. facility
- Celltrion U.S. factory
- SK Bioscience / IDT Biologika

event_premium:
- SK Bioscience +11.7% on IDT acquisition
- pharma sector +3.97% on tariff-support policy
- Jeisys take-private premium

evidence_good_but_price_failed:
- Samsung Biologics GSK facility, because stock -0.4% vs KOSPI +2%

failed_rerating_reference:
- SK Bioscience SkyCovione demand collapse

price_moved_without_evidence:
- biopharma tariff-policy rally if treated as company Green
- CDMO U.S. facility acquisitions before utilization/margin
- AI/medical-device or platform premium before reimbursement/usage/reorder

thesis_break_watch:
- Yuhan/J&J subcutaneous Rybrevant CRL
- Alteogen/Halozyme patent challenge
- Samsung Bio / Celltrion facility utilization and tariff economics
- SK Bioscience integration / post-COVID demand reset

hard_4C_confirmed:
- direct listed hard 4C: false
- sector reference: SkyCovione demand collapse
```

---

# 8. 점수비중 교정

## 올릴 축

```text
actual_prescription_ramp +5
royalty_milestone_cashflow +5
commercial_launch_execution +5
CDMO_capacity_utilization +5
customer_transfer_success +5
regulatory_quality_clearance +5
reimbursement_and_access +5
device_clinic_utilization +5
recurring_consumables_or_service +4
ex_policy_margin_FCF +5
```

### 왜 올리나

Yuhan과 Alteogen은 기술·허가 evidence가 좋지만, royalty·milestone·처방 ramp가 닫혀야 한다. Samsung Bio와 Celltrion은 U.S. facility 자체보다 utilization과 margin이 중요하다. SK Bioscience는 IDT 인수로 Stage 2가 생겼지만, SkyCovione demand collapse가 approval/procurement만으로는 부족하다는 반례다. Jeisys는 revenue/earnings growth가 검증된 medical-device benchmark지만, 상장투자자는 take-private으로 빠진다.

## 내릴 축

```text
FDA_approval_without_sales_bridge -4
platform_tech_without_royalty_cash -5
CDMO_facility_acquisition_only -5
policy_tariff_support_only -5
M&A_without_utilization -5
vaccine_procurement_without_demand -5
device_takeout_not_tradeable -3
patent_or_CRL_overhang -5
```

### 왜 내리나

FDA 승인은 중요하지만 처방과 cashflow가 없으면 Stage 3가 아니다. CDMO 공장은 고객이 실제로 넘어와야 한다. 정책지원은 margin bridge가 필요하다. 백신은 정부가 사도 국민이 맞지 않으면 demand가 아니다. SC Keytruda처럼 큰 플랫폼 기술도 patent challenge와 royalty timing을 통과해야 한다.

## Green gate 강화 조건

```text
R7 Stage 3-Green 필수:
1. FDA / EMA / MFDS 승인 이후 실제 처방·판매 ramp 확인
2. royalty / milestone / product sales 현금흐름 확인
3. CDMO는 capacity utilization과 customer transfer 확인
4. U.S. facility는 FDA inspection / tariff economics / margin 확인
5. medical device는 clinic utilization / recurring consumables / service revenue 확인
6. vaccine은 procurement가 아니라 administered dose / repeat demand 확인
7. platform tech는 patent risk와 exclusivity 확인
8. price path가 evidence 이후 따라옴

금지:
FDA approval only
license/platform tech headline only
CDMO plant acquisition only
policy support only
M&A pop only
government procurement only
take-private benchmark를 tradable Stage 3로 사용
```

## 4B 조기감지 조건

```text
4B-watch:
FDA approval / global approval headline로 주가 급등
SC Keytruda / platform enzyme story로 royalty 전 rerating
CDMO U.S. facility acquisition으로 utilization 전 급등
M&A announcement +10% 이상 급등
policy-support sector rally +3~6% 이상
medical-device takeout / aesthetics theme로 peer valuation 과열
government procurement / vaccine sovereignty narrative로 demand 전 가격화

4B-elevated:
royalty cashflow 미확인
facility utilization 미확인
FDA inspection / CMC overhang
patent challenge
reimbursement access 미확인
post-COVID vaccine demand weak
```

## 4C hard gate 조건

```text
FDA CRL / approval rejection
clinical hold / serious safety event
CMC / manufacturing inspection failure
patent injunction / launch delay
royalty or milestone non-realization
CDMO facility underutilization
vaccine demand collapse
device recall / safety issue
reimbursement denial
tariff economics negative despite U.S. facility
```

이번 R7 Loop 13에서는 **direct listed hard 4C는 확정하지 않는다.** 대신 **SkyCovione demand collapse**를 sector hard reference로 두고, **SC Rybrevant CRL**, **Alteogen patent challenge**, **CDMO facility utilization**, **SK Bioscience post-COVID demand reset**을 4C-watch로 둔다.

---

# 9. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 10. 레포 반영용 patch-ready 출력

## docs/round/round_204.md 요약

```md
# R7 Loop 13. Bio / Healthcare / Medical Device Price Validation

이번 라운드는 R7 Loop 13 price-validation 라운드다.

핵심 결론:
- Yuhan / lazertinib is Korean-origin drug global approval Stage 2. J&J Rybrevant + lazertinib received FDA first-line approval for EGFR-mutated NSCLC. J&J expects Rybrevant peak sales above $5B. Yuhan Green requires royalty/milestone cashflow and prescription ramp.
- Alteogen / Merck SC Keytruda is platform-tech structural candidate plus patent watch. SC Keytruda could reduce administration time from about 30 minutes to 2~3 minutes; Merck expects 30~40% adoption among Keytruda patients. Keytruda had nearly $30B sales in 2024. Halozyme patent challenge remains watch.
- Samsung Biologics / GSK Rockville facility is CDMO U.S. tariff-hedge Stage 2. $280M acquisition, 60,000L capacity, but stock -0.4% versus KOSPI +2%. Facility utilization and customer transfer required.
- Celltrion U.S. factory is tariff-hedge Stage 2. It acquired ImClone Systems from Eli Lilly for $330M and plans up to 700B won U.S. expansion. Product transfer, utilization and margin required.
- SK Bioscience / IDT Biologika is vaccine-CDMO M&A Stage 2. 60% stake for 339B won / $243.75M; shares +11.7%. Order book and utilization required.
- Jeisys Medical is aesthetics medical-device benchmark. ArchiMed $742M take-private, close 12,860 won, revenue CAGR 44% to $107M, adjusted pretax earnings CAGR 45% to $31M. Take-private benchmark, not tradable Stage 3.
- Pharma tariff-support rally is event premium. Pharma sector +3.97%, Samsung Biologics +6.23%, Celltrion +0.35% after government support pledge. Margin bridge required.
- SK Bioscience SkyCovione is vaccine demand-collapse reference. Government purchased 10M doses, 600k released, only 3,787 administered by Nov 2022. Approval/procurement was not demand.
```

## docs/checkpoints/checkpoint_28a_round204_r7_loop13.md 요약

```md
# Checkpoint 28A Round 204 R7 Loop 13 Bio Healthcare Medical Device Price Validation

## 반영 내용
- R7 Loop 13 price-validation 라운드를 추가했다.
- Yuhan lazertinib, Alteogen SC Keytruda enzyme, Samsung Biologics U.S. facility, Celltrion U.S. factory, SK Bioscience IDT acquisition, Jeisys Medical take-private, pharma tariff-support rally, SkyCovione demand collapse를 비교했다.
- Reuters / WSJ / MarketWatch / FT / Barron's / public reference anchors로 가능한 event MFE/MAE 및 business metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- actual prescription ramp, royalty/milestone cashflow, commercial launch execution, CDMO utilization, customer transfer, regulatory quality clearance, reimbursement/access, device clinic utilization, recurring consumables/service revenue 가중치 강화
- FDA approval-only, platform tech without royalty cash, CDMO facility acquisition-only, policy tariff support-only, M&A without utilization, vaccine procurement without demand 감점 강화
```

## data/e2r_case_library/cases_r7_loop13_round204.jsonl 초안

```jsonl
{"case_id":"r7_loop13_yuhan_lazertinib_global_fda_approval","symbol":"000100","company_name":"Yuhan / lazertinib / J&J Rybrevant combo","case_type":"success_candidate","primary_archetype":"KOREAN_ORIGIN_DRUG_GLOBAL_APPROVAL","stage1_date":"2024-08-20","stage2_date":"2024-08-20","stage4c_date":"2024-12-16_watch","price_validation":{"price_data_source":"Reuters/MarketWatch FDA approval and CRL anchors","stage3_price":null,"fda_approval_date":"2024-08-20","approved_combo":"Rybrevant + lazertinib / Lazcluze","indication":"first-line EGFR-mutated NSCLC","egfr_mutation_share_us_nsclc_pct":"10-15","jnj_expected_rybrevant_peak_sales_usd_bn":5,"marketwatch_phase3_risk_reduction_pct":30,"trial_patient_count_marketwatch":1074,"subcutaneous_rybrevant_crl_date":"2024-12-16","crl_cause":"pre-approval manufacturing facility inspection observations","additional_clinical_studies_requested":false,"price_validation_status":"yuhan_stock_ohlc_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_price_data_unavailable","rerating_result":"Korean_origin_drug_global_approval_stage2","notes":"FDA approval is strong Stage 2; Yuhan Green requires royalty/milestone cashflow and prescription ramp."}
{"case_id":"r7_loop13_alteogen_merck_sc_keytruda_platform","symbol":"196170","company_name":"Alteogen / Merck SC Keytruda enzyme","case_type":"structural_success_candidate","primary_archetype":"PLATFORM_TECH_ENZYME_ROYALTY_OPTIONALITY","stage1_date":"2024-11-19","stage2_date":"2025-03-27","stage4c_date":"patent_watch","price_validation":{"price_data_source":"Reuters/WSJ SC Keytruda trial, launch and patent anchors","stage3_price":null,"keytruda_2024_sales_usd_bn":30,"sc_keytruda_expected_adoption_pct":"30-40","sc_injection_time_minutes":"2-3","iv_infusion_time_minutes":30,"time_reduction_low_pct":90,"fda_decision_target":"2025-09-23","planned_us_launch_date":"2025-10-01","merck_premarket_reaction_to_noninferiority_pct":1.8,"wsj_sc_keytruda_sales_prediction_usd_bn":6,"patent_challenge_watch":"Halozyme","price_validation_status":"alteogen_stock_ohlc_unavailable_after_deep_search"},"score_price_alignment":"structural_success_candidate_but_4B_and_patent_watch","rerating_result":"platform_enzyme_royalty_optionality","notes":"Platform option is large, but royalty cashflow, patent clearance and launch adoption are required before Green."}
{"case_id":"r7_loop13_samsung_biologics_gsk_rockville_facility","symbol":"207940","company_name":"Samsung Biologics","case_type":"success_candidate","primary_archetype":"CDMO_US_TARIFF_HEDGE_STAGE2","stage2_date":"2025-12-22","price_validation":{"price_data_source":"Reuters GSK facility acquisition and sector-support anchors","stage3_price":null,"facility_acquisition_usd_mn":280,"facility_location":"Rockville, Maryland","acquired_entity":"Human Genome Sciences Inc.","stake_acquired_pct":100,"drug_substance_capacity_liters":60000,"expected_close":"around end-Q1 2026","event_mae_pct":-0.4,"kospi_same_context_pct":2.0,"relative_underperformance_pp":-2.4,"facility_utilization_confirmed":false,"customer_transfer_confirmed":false,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"CDMO_US_tariff_hedge_stage2","notes":"U.S. facility acquisition is Stage 2; utilization, customer transfer, FDA inspection, margin and FCF required."}
{"case_id":"r7_loop13_celltrion_us_factory_tariff_hedge","symbol":"068270","company_name":"Celltrion","case_type":"success_candidate","primary_archetype":"BIOPHARMA_US_FACTORY_TARIFF_HEDGE","stage2_date":"2025-07-29/2025-09-23/2025-11-19","price_validation":{"price_data_source":"Reuters Celltrion U.S. factory acquisition and expansion anchors","stage3_price":null,"preferred_bidder_investment_plan_krw_bn":700,"possible_additional_investment_krw_bn":"300-700","imclone_acquisition_usd_mn":330,"us_factory_expansion_max_krw_bn":700,"us_factory_expansion_max_usd_mn":478.17,"tariff_driver":"U.S. pharmaceutical tariff risk","product_transfer_confirmed":false,"utilization_confirmed":false,"margin_confirmed":false,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_price_data_unavailable","rerating_result":"biopharma_US_factory_tariff_hedge_stage2","notes":"Factory acquisition/expansion is Stage 2; product transfer, utilization, tariff saving, margin and FCF required."}
{"case_id":"r7_loop13_sk_bioscience_idt_biologika_cdmomna","symbol":"302440","company_name":"SK Bioscience / IDT Biologika","case_type":"success_candidate_event_premium","primary_archetype":"VACCINE_CDMO_M_AND_A_STAGE2","stage2_date":"2024-06-27","stage4b_date":"2024-06-27","price_validation":{"price_data_source":"Reuters SK Bioscience / IDT Biologika deal anchor","stage3_price":null,"idt_stake_acquired_pct":60,"deal_value_krw_bn":339,"deal_value_usd_mn":243.75,"klocke_remaining_stake_pct":40,"ipo_context":"first_major_M&A_since_2021_IPO","ipo_raise_2021_usd_bn":1.33,"event_mfe_pct":11.7,"order_book_confirmed":false,"utilization_confirmed":false,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"vaccine_CDMO_MA_stage2","notes":"European CDMO acquisition is Stage 2; integration, order book, utilization and margin required."}
{"case_id":"r7_loop13_jeisys_medical_archimed_aesthetic_device_takeout","symbol":"Jeisys_formerly_public","company_name":"Jeisys Medical","case_type":"success_candidate_takeout_event","primary_archetype":"AESTHETIC_MEDICAL_DEVICE_PE_TAKEOUT","stage2_date":"2024-09-11","price_validation":{"price_data_source":"WSJ Jeisys / ArchiMed take-private anchor","stage3_price":null,"take_private_value_usd_mn":742,"pre_delisting_close_price_krw":12860,"revenue_fy2023_usd_mn":107,"revenue_cagr_3y_pct":44,"adjusted_pretax_earnings_fy2023_usd_mn":31,"adjusted_pretax_earnings_cagr_3y_pct":45,"pretax_margin_fy2023_pct":29.0,"global_ebd_market_previous_year_usd_bn":4.5,"global_ebd_market_2032_usd_bn":16,"global_ebd_market_growth_to_2032_pct":255.6,"listed_status_after_deal":"delisting_process","price_validation_status":"reported_takeout_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_takeout_event","rerating_result":"aesthetic_medical_device_revenue_earnings_benchmark","notes":"Real medical-device benchmark, but take-private means not a tradable Stage 3 row."}
{"case_id":"r7_loop13_biopharma_tariff_support_policy_rally","symbol":"207940/068270/pharma_sector","company_name":"Samsung Biologics / Celltrion / Korean pharma sector","case_type":"event_premium_policy_relief","primary_archetype":"BIOPHARMA_POLICY_RALLY_EVENT_PREMIUM","stage2_date":"2025-05-21","price_validation":{"price_data_source":"Reuters Korea market / policy-support anchors","stage3_price":null,"kospi_event_mfe_pct":0.99,"kospi_event_close":2627.63,"pharma_sector_mfe_pct":3.97,"samsung_biologics_mfe_pct":6.23,"celltrion_mfe_pct":0.35,"foreign_net_buy_krw_bn":113.7,"pharmaceutical_exports_2024_usd_bn":9.59,"us_export_share_pct":16,"implied_us_pharma_exports_2024_usd_bn":1.53,"tariff_exemption_confirmed":false,"company_margin_bridge_confirmed":false,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_policy_relief","rerating_result":"biopharma_tariff_support_stage2","notes":"Policy support is relief, not Green; company margin/FCF bridge needed."}
{"case_id":"r7_loop13_sk_bioscience_skycovione_demand_collapse_reference","symbol":"302440_reference","company_name":"SK Bioscience / SkyCovione","case_type":"failed_rerating_reference","primary_archetype":"VACCINE_DEMAND_COLLAPSE_HARD_REFERENCE","stage1_date":"2022-06","stage4c_date":"2022-11_reference/2024-05_reference","price_validation":{"price_data_source":"public vaccine-demand-collapse reference","stage3_price":null,"government_purchase_doses_mn":10,"released_to_hospitals_doses":600000,"administered_shots":3787,"administered_share_of_released_pct":0.63,"administered_share_of_purchased_pct":0.038,"production_status":"indefinitely_suspended_due_low_demand","unused_doses_likely_discarded":true,"eu_authorization_application_withdrawn":"2023-09","who_eul_delisted":"2024-05","price_validation_status":"stock_ohlc_unavailable_after_deep_search"},"score_price_alignment":"failed_rerating_reference","rerating_result":"vaccine_approval_procurement_not_demand","notes":"Approval and government procurement did not become actual demand; use as vaccine demand-collapse reference."}
```

## data/sector_taxonomy/score_weight_profiles_round204_r7_loop13_v1.csv 초안

```csv
archetype,actual_prescription_ramp,royalty_milestone_cashflow,commercial_launch_execution,cdmo_capacity_utilization,customer_transfer_success,regulatory_quality_clearance,reimbursement_access,device_clinic_utilization,recurring_consumables_service,ex_policy_margin_fcf,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
KOREAN_ORIGIN_DRUG_GLOBAL_APPROVAL,+5,+5,+5,+0,+0,+5,+5,+0,+0,+5,-4,+4,+5,Yuhan/lazertinib needs royalty/milestone cash and prescription ramp after FDA approval.
PLATFORM_TECH_ENZYME_ROYALTY_OPTIONALITY,+3,+5,+5,+0,+0,+5,+4,+0,+0,+5,-5,+5,+5,Alteogen/SC Keytruda needs royalty cashflow, launch adoption and patent clearance.
CDMO_US_TARIFF_HEDGE_STAGE2,+0,+0,+3,+5,+5,+5,+0,+0,+0,+5,-5,+4,+4,Samsung Bio U.S. facility needs utilization, customer transfer, FDA inspection and margin.
BIOPHARMA_US_FACTORY_TARIFF_HEDGE,+0,+0,+3,+5,+5,+5,+0,+0,+0,+5,-5,+4,+4,Celltrion U.S. factory needs product transfer, tariff saving, utilization and FCF.
VACCINE_CDMO_M_AND_A_STAGE2,+0,+0,+3,+5,+5,+5,+0,+0,+1,+5,-5,+5,+4,SK Bioscience/IDT M&A needs order book, integration and utilization.
AESTHETIC_MEDICAL_DEVICE_PE_TAKEOUT,+0,+0,+4,+0,+0,+4,+3,+5,+5,+5,-3,+4,+3,Jeisys is device benchmark; peer scoring needs clinic utilization and consumables/service revenue.
BIOPHARMA_POLICY_RALLY_EVENT_PREMIUM,+0,+0,+2,+3,+2,+3,+0,+0,+0,+5,-5,+5,+4,Policy support rally is not Green without tariff/margin bridge.
VACCINE_DEMAND_COLLAPSE_HARD_REFERENCE,+0,+0,+2,+2,+0,+4,+3,+0,+0,+5,0,+3,+5,SkyCovione shows approval/procurement without administered demand can fail.
```

---

# 이번 R7 Loop 13 결론

```text
1. Yuhan / lazertinib은 R7의 좋은 global approval Stage 2다.
   하지만 FDA approval만으로 Green은 아니다. royalty/milestone cashflow와 prescription ramp가 필요하다.

2. Alteogen / SC Keytruda는 platform-tech structural candidate다.
   Keytruda $30B market, SC adoption 30~40% 가능성은 크지만 patent/royalty/launch gate가 남아 있다.

3. Samsung Biologics는 U.S. CDMO tariff-hedge Stage 2다.
   $280M facility와 60,000L capacity는 좋지만 발표일 주가가 KOSPI 대비 -2.4pp였다.

4. Celltrion은 U.S. factory hedge Stage 2다.
   ImClone $330M acquisition과 700B won expansion은 제품이전·utilization·margin 전에는 Green이 아니다.

5. SK Bioscience / IDT Biologika는 vaccine-CDMO M&A Stage 2다.
   +11.7% event pop은 order book과 utilization 전에는 4B-watch다.

6. Jeisys Medical은 aesthetics device revenue/earnings benchmark다.
   하지만 take-private라 tradeable Stage 3가 아니라 peer scoring benchmark로 써야 한다.

7. 제약업종 tariff-support rally는 policy relief다.
   Samsung Bio +6.23%, pharma sector +3.97%는 margin bridge 전 event premium이다.

8. SkyCovione은 vaccine demand-collapse reference다.
   승인과 정부구매가 있어도 실제 접종수요가 없으면 thesis는 끊긴다.
```

한 문장으로 압축하면:

> **R7에서 진짜 Stage 3는 “FDA 승인·CDMO 공장·플랫폼 기술·의료기기 M&A·정책지원이 있다”가 아니라, 처방 ramp·royalty cash·capacity utilization·regulatory quality·device usage·reimbursement·FCF가 실제 숫자로 닫히는 순간이다.**

[1]: https://www.reuters.com/business/healthcare-pharmaceuticals/us-fda-approves-jjs-combination-therapy-type-lung-cancer-2024-08-20/?utm_source=chatgpt.com "US FDA approves J&J's chemotherapy-free treatment for lung cancer"
[2]: https://www.reuters.com/business/healthcare-pharmaceuticals/merck-says-keytruda-injection-par-with-approved-iv-version-trial-2024-11-19/?utm_source=chatgpt.com "Merck says Keytruda injection on par with approved IV version in trial"
[3]: https://www.reuters.com/business/healthcare-pharmaceuticals/samsung-biologics-buy-us-drug-production-facility-gsk-280-mln-2025-12-21/?utm_source=chatgpt.com "Samsung Biologics to buy US drug production facility from GSK for $280 million"
[4]: https://www.reuters.com/business/healthcare-pharmaceuticals/south-koreas-celltrion-says-tapped-buy-us-pharma-factory-offset-tariff-risk-2025-07-29/?utm_source=chatgpt.com "South Korea's Celltrion says tapped to buy US pharma factory to offset tariff risk"
[5]: https://www.reuters.com/markets/deals/south-koreas-sk-bioscience-buy-control-germanys-idt-biologika-244-mln-2024-06-27/?utm_source=chatgpt.com "South Korea's SK Bioscience to buy control of Germany's IDT Biologika for $244 mln"
[6]: https://www.wsj.com/articles/europes-archimed-bets-on-anti-aging-trend-in-first-asia-deal-cbe16f5e?utm_source=chatgpt.com "Europe's ArchiMed Bets on Anti-Aging Trend in First Asia Deal"
[7]: https://www.reuters.com/business/healthcare-pharmaceuticals/south-korean-shares-rise-1-pharmaceutical-stocks-jump-2025-05-21/?utm_source=chatgpt.com "South Korean shares rise 1% as pharmaceutical stocks jump"
[8]: https://en.wikipedia.org/wiki/Skycovione?utm_source=chatgpt.com "Skycovione"
