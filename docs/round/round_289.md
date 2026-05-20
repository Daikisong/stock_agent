순서상 이번은 **R7 Loop 14 — 바이오·헬스케어·의료기기 가격경로 검증 라운드**다.

```text
round = R7 Loop 14
round_id = round_217
large_sector = BIO_HEALTHCARE_MEDICAL_DEVICE
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
direct_KRX_hard_4c_confirmed = false
sector_hard_4c_reference_confirmed = true
next_round = R8 Loop 14
```

이번 R7은 **Samsung Biologics, Celltrion, SK Bioscience, Alteogen, Yuhan, Hugel, ADEL, 글로벌 임상/FDA 실패 reference**를 본다. R7의 핵심은 “바이오니까 기술수출”, “FDA 승인”, “CMO 증설”, “미국 공장”, “Keytruda”, “AI/ADC/GLP-1” 같은 단어가 아니라, **허가·계약·공장·임상·기술수출이 실제 매출·마진·규제 리스크·주가경로로 닫혔는지**다.

이번 환경에서는 KRX/Naver/Yahoo/Stooq 기준의 **수정주가 일봉 OHLC 전체 window**를 안정적으로 확보하지 못했다. 따라서 30D/90D/180D/1Y full MFE·MAE는 만들지 않고, Reuters/WSJ/MarketWatch/AP/FT가 제공한 **event return, deal value, tariff context, facility capacity, adoption target, clinical/FDA failure drawdown**을 price anchor로 사용했다. full OHLC가 필요한 칸은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R7 = 바이오·헬스케어·의료기기
```

R7에서 진짜 Stage 3는 아래가 숫자로 닫힐 때다.

```text
CMO/CDMO:
계약 → batch slot → facility utilization → tech transfer → FDA inspection → gross margin → recurring order

신약/바이오시밀러:
임상 성공 → FDA/EMA 승인 → launch → reimbursement → market share → royalty / sales → margin

기술수출:
upfront → milestone probability → partner execution → regulatory success → royalty durability

의료기기/미용:
FDA approval → U.S. launch → physician adoption → ASP → repeat procedure volume → distributor margin

디지털/AI 의료:
FDA clearance → hospital workflow adoption → reimbursement → recurring software revenue

임상/FDA risk:
CRL / clinical hold / trial failure → valuation reset → financing risk → pipeline repricing
```

---

# 2. 대상 canonical archetype

```text
BIO_CMO_US_LOCALIZATION_STAGE2
BIOSIMILAR_US_TARIFF_HEDGE_STAGE2
VACCINE_CDMO_MA_EVENT_PREMIUM
BLOCKBUSTER_SC_FORMULATION_STAGE3_CANDIDATE
ONCOLOGY_LICENSE_ROYALTY_STAGE2
AESTHETIC_MEDICAL_DEVICE_US_LAUNCH_STAGE2
KOREAN_BIOTECH_TECH_EXPORT_STAGE2
GLOBAL_CLINICAL_FAILURE_HARD_4C_REFERENCE
```

---

# 3. deep sub-archetype

```text
CMO/CDMO:
- Samsung Biologics / GSK Rockville facility
- Celltrion / Eli Lilly ImClone facility
- SK Bioscience / IDT Biologika
- tariff hedge and U.S. localization

Blockbuster formulation:
- Alteogen enzyme
- Merck Keytruda Qlex
- SC conversion, 30~40% adoption target
- Halozyme patent dispute watch

Oncology licensing:
- Yuhan / Lazertinib / J&J Rybrevant combination
- FDA approval, peak-sales potential, royalty/launch execution

Aesthetic medical:
- Hugel / Letybo
- U.S. neuromodulator market entry
- counterfeit Botox / safety regulation watch

Unlisted Korean biotech reference:
- ADEL / Sanofi Alzheimer's drug deal
- upfront and milestones, early-stage risk

Hard 4C reference:
- HilleVax trial failure
- Corcept FDA rejection
- PepGen partial clinical hold
```

---

# 4. 국장 신규 후보 case

## Case A — Samsung Biologics / GSK U.S. facility `evidence_good_but_price_failed`

```text
symbol = 207940
case_type = evidence_good_but_price_failed
archetype = BIO_CMO_US_LOCALIZATION_STAGE2
```

### stage date

```text
Stage 1:
2025-05~2025-12
- U.S. pharmaceutical tariff risk rises.
- Korean biopharma exporters begin U.S. localization / reshoring response.

Stage 2:
2025-12-22
- Samsung Biologics announces first U.S. drug-production facility acquisition.
- buys 100% of Human Genome Sciences Inc. in Rockville, Maryland from GSK.
- acquisition value: $280M.
- existing site capacity: 60,000 liters drug-substance capacity.
- expected close: around end-Q1 2026.
- U.S. imports of Korean pharmaceuticals under trade deal capped at max 15% tariff, generics tariff-free.

Stage price / event:
- Samsung Biologics shares -0.4%.
- KOSPI +2%.
- relative underperformance: -2.4pp.

Stage 3:
없음
- U.S. facility acquisition is Stage 2.
- Green requires facility utilization, FDA inspection / tech transfer success, batch margin, recurring customer orders.
```

Samsung Biologics case는 좋은 전략 뉴스였지만, 가격경로는 Green을 주지 않았다. Reuters는 Samsung Biologics가 GSK에서 Rockville facility를 $280M에 인수해 첫 U.S. production site를 확보한다고 보도했고, 해당 facility는 60,000L drug-substance capacity를 가진다. 그런데 같은 보도에서 Samsung Biologics 주가는 -0.4%, KOSPI는 +2%였다고 나온다. 즉 **U.S. localization은 Stage 2지만, market은 facility utilization과 margin을 아직 확인하지 않았다.** ([Reuters][1])

### 실제 가격경로 검증

```json
{
  "case_id": "r7_loop14_samsung_biologics_gsk_us_facility",
  "symbol": "207940",
  "stage2_date": "2025-12-22",
  "stage3_price": null,
  "price_data_source": "Reuters Samsung Biologics-GSK facility event anchor",
  "acquisition_value_usd_mn": 280,
  "facility_location": "Rockville, Maryland",
  "facility_capacity_liters": 60000,
  "expected_close": "2026_Q1_end",
  "korean_pharma_tariff_cap_pct": 15,
  "generic_drugs_tariff_free": true,
  "event_mae_pct": -0.4,
  "kospi_same_context_pct": 2.0,
  "relative_underperformance_pp": -2.4,
  "facility_utilization_confirmed": false,
  "fda_inspection_transfer_confirmed": false,
  "mfe_30d_90d_180d_1y": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed
rerating_result = BIO_CMO_US_LOCALIZATION_STAGE2
stage_failure_type = facility_acquisition_not_utilization_margin_green
```

---

## Case B — Celltrion / U.S. factory tariff hedge `success_candidate`

```text
symbol = 068270
case_type = success_candidate
archetype = BIOSIMILAR_US_TARIFF_HEDGE_STAGE2
```

### stage date

```text
Stage 1:
2025-07-29
- Celltrion says it became preferred bidder for U.S. pharma manufacturing facility.
- purpose: offset U.S. pharmaceutical tariff risk.

Stage 2:
2025-09-23
- Celltrion U.S. subsidiary acquires ImClone Systems LLC from Eli Lilly.
- acquisition value: $330M.
- target: complete process by year-end.
- facility to protect key U.S. products and future launches from tariff exposure.

Stage 2 추가:
2025-11-19
- Celltrion plans up to 700B won / $478.17M additional U.S. factory capacity investment.
- rationale: tariffs and rising demand.

Stage 3:
없음
- acquisition + expansion is Stage 2.
- Green requires product transfer, FDA inspection, utilization, tariff savings, biosimilar market share, margin.
```

Celltrion은 Samsung Biologics보다 가격 anchor가 약하지만, 전략적 Stage 2는 명확하다. Reuters는 Celltrion이 Eli Lilly에서 ImClone Systems를 $330M에 인수했고, 이후 최대 700B won을 추가 투자해 U.S. manufacturing capacity를 확대할 계획이라고 보도했다. 이 case는 **U.S. tariff hedge가 좋은 전략이지만, 실제 제품 이전·가동률·tariff saving·biosimilar market share가 확인되어야 Green**이라는 row다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "case_id": "r7_loop14_celltrion_us_factory_tariff_hedge",
  "symbol": "068270",
  "stage1_date": "2025-07-29",
  "stage2_date": "2025-09-23/2025-11-19",
  "stage3_price": null,
  "price_data_source": "Reuters Celltrion U.S. factory acquisition and expansion anchors",
  "factory_acquisition_value_usd_mn": 330,
  "target_seller": "Eli Lilly / ImClone Systems LLC",
  "additional_capacity_investment_krw_bn": 700,
  "additional_capacity_investment_usd_mn": 478.17,
  "tariff_hedge_rationale": true,
  "product_transfer_confirmed": false,
  "us_factory_utilization_confirmed": false,
  "direct_event_return": "price_data_unavailable_after_deep_search",
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_but_price_data_unavailable
rerating_result = BIOSIMILAR_US_TARIFF_HEDGE_STAGE2
stage_failure_type = acquisition_capacity_not_tariff_saving_margin_green
```

---

## Case C — SK Bioscience / IDT Biologika `event_premium + success_candidate`

```text
symbol = 302440
case_type = event_premium + success_candidate
archetype = VACCINE_CDMO_MA_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2024-06-27
- SK Bioscience shifts from post-COVID vaccine weakness toward global vaccine/CDMO M&A.
- first major post-IPO M&A.

Stage 2:
2024-06-27
- SK Bioscience acquires 60% stake in German CDMO IDT Biologika.
- deal value: 339B won / $243.75M.
- Klocke Group retains 40%.
- first major M&A since SK Bioscience's 2021 IPO, which raised $1.33B.
- shares +11.7% in morning trading.

Stage 2 validation:
2025-08-06
- Novavax raises 2025 revenue forecast partly on vaccine-supply partnerships including SK Bioscience.
- Novavax revenue beat driven by U.S. Nuvaxovid approval-related milestone.
```

SK Bioscience는 R7에서 가장 명확한 **event premium + Stage 2 success_candidate**다. Reuters는 SK Bioscience가 IDT Biologika 60%를 339B won에 인수한다고 보도했고, 발표 후 SK Bioscience 주가는 +11.7%였다. 하지만 이 역시 Stage 3가 아니다. M&A 이후 실제 CDMO backlog, plant utilization, tech transfer, vaccine demand, margin이 확인되어야 한다. ([Reuters][3])

Novavax가 2025년 revenue forecast를 올리며 SK Bioscience와의 vaccine supply partnerships를 언급한 것은 SK Bioscience의 CDMO/partnership 방향을 보강하지만, SK Bioscience 자체 Stage 3에는 아직 부족하다. ([Reuters][4])

### 실제 가격경로 검증

```json
{
  "case_id": "r7_loop14_sk_bioscience_idt_biologika_ma",
  "symbol": "302440",
  "stage2_date": "2024-06-27",
  "stage3_price": null,
  "price_data_source": "Reuters SK Bioscience-IDT Biologika M&A anchor",
  "acquired_stake_pct": 60,
  "deal_value_krw_bn": 339,
  "deal_value_usd_mn": 243.75,
  "seller_retained_stake_pct": 40,
  "ipo_2021_raise_usd_bn": 1.33,
  "event_mfe_pct": 11.7,
  "novavax_partnership_validation": true,
  "cdmo_backlog_confirmed": false,
  "plant_utilization_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_success_candidate
rerating_result = VACCINE_CDMO_MA_STAGE2
stage_failure_type = ma_control_not_cdmo_utilization_green
```

---

## Case D — Alteogen / Keytruda Qlex `structural_success_candidate + patent 4B-watch`

```text
symbol = 196170
case_type = structural_success_candidate + 4B-watch
archetype = BLOCKBUSTER_SC_FORMULATION_STAGE3_CANDIDATE
```

### stage date

```text
Stage 1:
2024-11-19
- Merck says injectable Keytruda version is non-inferior to IV Keytruda in late-stage trial.
- Alteogen enzyme is used with the formulation.

Stage 2:
2025-03-27
- Merck plans U.S. launch of subcutaneous Keytruda on Oct. 1.
- FDA decision target: 2025-09-23.
- Merck expects peak adoption of at least 30%~40% of Keytruda patients within two years.
- Keytruda 2024 sales nearly $30B.
- Alteogen develops/manufactures the enzyme used with the SC formulation.

Stage 3 candidate:
2025-09-19
- FDA approves Keytruda Qlex.
- injection can be administered in around 1~2 minutes vs IV infusion around 30 minutes.
- Merck expects U.S. availability in late September.
- adoption target 30%~40% within two years remains key.

Stage 4B-watch:
- Halozyme patent dispute / enzyme IP challenge risk.
- SC adoption and royalty economics need confirmation.
```

Alteogen은 R7에서 가장 강한 structural success_candidate다. Reuters는 Merck의 Keytruda SC version이 non-inferior trial result를 냈고, Alteogen이 Keytruda formulation에 쓰이는 enzyme을 개발·제조한다고 보도했다. 이후 FDA는 Keytruda Qlex를 승인했고, Merck는 Keytruda patients 중 30%~40% adoption을 2년 내 목표로 제시했다. 다만 WSJ는 Halozyme patent dispute를 보도했으므로, Green은 **SC adoption, royalty conversion, patent risk**를 통과해야 한다. ([Reuters][5])

### 실제 가격경로 검증

```json
{
  "case_id": "r7_loop14_alteogen_keytruda_qlex_sc_formulation",
  "symbol": "196170",
  "stage1_date": "2024-11-19",
  "stage2_date": "2025-03-27",
  "stage3_date_candidate": "2025-09-19",
  "stage3_price": null,
  "price_data_source": "Reuters Keytruda SC trial/launch/approval anchors + WSJ patent-dispute anchor",
  "keytruda_2024_sales_usd_bn": 30,
  "target_peak_adoption_pct_range": "30-40",
  "administration_time_sc_minutes": "1-2",
  "administration_time_iv_minutes": 30,
  "us_availability_expected": "late_2025_09",
  "alteogen_enzyme_role": "develops_and_manufactures_enzyme_used_with_Keytruda_SC",
  "patent_dispute_watch": true,
  "royalty_conversion_confirmed": false,
  "alteogen_direct_ohlc": "price_data_unavailable_after_deep_search",
  "mfe_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = structural_success_candidate_but_price_data_unavailable
rerating_result = BLOCKBUSTER_SC_FORMULATION_STAGE3_CANDIDATE
stage_failure_type = FDA_approval_not_royalty_adoption_patent_green
```

---

## Case E — Yuhan / Lazertinib / J&J Rybrevant `oncology royalty Stage 2`

```text
symbol = 000100
case_type = success_candidate
archetype = ONCOLOGY_LICENSE_ROYALTY_STAGE2
```

### stage date

```text
Stage 1:
2024-08-20
- U.S. FDA approves J&J's chemotherapy-free Rybrevant + lazertinib combination for first-line EGFR-mutated NSCLC.
- Yuhan's lazertinib becomes part of global oncology approval story.

Stage 2:
2024-08-20
- approval based on late-stage study.
- regimen increased progression-free time vs AstraZeneca Tagrisso.
- J&J expects Rybrevant peak sales above $5B.
- launch to proceed immediately after FDA decision.

Stage 4C-watch:
2024-12-16
- FDA declines to approve injectable Rybrevant formulation.
- CRL related to pre-approval inspection at manufacturing facility.
- not related to formulation, efficacy or safety data.
- IV Rybrevant remains unaffected.
```

Yuhan은 R7 oncology license/royalty Stage 2다. FDA approval 자체는 강한 evidence다. Reuters는 J&J의 Rybrevant + lazertinib combination이 EGFR-mutated NSCLC 1차 치료로 FDA approval을 받았고, J&J는 Rybrevant peak sales를 $5B 이상으로 기대한다고 보도했다. 그러나 2024년 12월 subcutaneous Rybrevant formulation은 제조시설 inspection issue로 CRL을 받았다. 이 case는 **drug approval과 royalty economics는 좋지만, manufacturing/formulation regulatory gate가 따로 있다**는 교정값이다. ([Reuters][6])

### 실제 가격경로 검증

```json
{
  "case_id": "r7_loop14_yuhan_lazertinib_jnj_rybrevant_approval",
  "symbol": "000100",
  "stage2_date": "2024-08-20",
  "stage4c_watch_date": "2024-12-16",
  "stage3_price": null,
  "price_data_source": "Reuters FDA approval and later CRL anchors",
  "indication": "first-line EGFR-mutated non-small cell lung cancer",
  "combination": "Rybrevant + lazertinib",
  "rybrevant_peak_sales_expectation_usd_bn": 5,
  "pfs_benefit_vs_tagrisso": true,
  "later_crl_related_to": "pre-approval inspection at manufacturing facility",
  "later_crl_not_related_to": ["formulation", "efficacy", "safety_data"],
  "iv_rybrevant_unaffected": true,
  "yuhan_direct_price_anchor": "price_data_unavailable_after_deep_search",
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_but_price_data_unavailable
rerating_result = ONCOLOGY_LICENSE_ROYALTY_STAGE2
stage_failure_type = approval_not_royalty_launch_margin_green
```

---

## Case F — Hugel / Letybo U.S. launch `aesthetic medical Stage 2 + safety watch`

```text
symbol = 145020
case_type = success_candidate + regulatory_watch
archetype = AESTHETIC_MEDICAL_DEVICE_US_LAUNCH_STAGE2
```

### stage date

```text
Stage 1:
2024~2025
- Hugel's Letybo enters U.S. neuromodulator market.
- Korean botulinum toxin product becomes U.S. aesthetic export story.

Stage 2:
2025-03
- Letybo begins appearing in U.S. dermatology practices after FDA approval for glabellar lines.
- Letybo known in Korea as Botulax.
- potential pricing advantage vs Botox in U.S. aesthetic market.

Stage 4C-watch:
2025-11
- FDA warns websites selling counterfeit or unapproved Botox-like products.
- botulinum toxin category has safety, misbranding and provider-quality risk.
```

Hugel/Letybo는 의료미용 Stage 2다. Allure는 Letybo가 FDA approval 이후 U.S. dermatology practices에 들어가기 시작했고, 한국에서는 Botulax로 오래 사용됐다고 설명했다. 그러나 botulinum toxin category는 category safety risk가 크다. AP는 FDA가 counterfeit/unapproved Botox-like products를 판매하는 웹사이트들에 warning letters를 보냈다고 보도했다. 즉 Hugel Green은 approval이 아니라 **physician adoption, reimbursement/pricing, distributor margin, safety compliance**다. ([Allure][7])

### 실제 가격경로 검증

```json
{
  "case_id": "r7_loop14_hugel_letybo_us_aesthetic_launch",
  "symbol": "145020",
  "stage2_date": "2025-03",
  "stage4c_watch_date": "2025-11",
  "stage3_price": null,
  "price_data_source": "Allure Letybo U.S. launch context + AP FDA counterfeit Botox warning",
  "product": "Letybo / Botulax",
  "us_indication": "glabellar_lines",
  "category": "botulinum_toxin_A_neuromodulator",
  "pricing_advantage_context": true,
  "category_safety_watch": true,
  "physician_adoption_confirmed": false,
  "distributor_margin_confirmed": false,
  "hugel_direct_ohlc": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_but_price_data_unavailable
rerating_result = AESTHETIC_MEDICAL_US_LAUNCH_STAGE2
stage_failure_type = FDA_approval_not_adoption_margin_green
```

---

## Case G — ADEL / Sanofi Alzheimer’s deal `Korean biotech tech-export Stage 2 reference`

```text
symbol = unlisted
case_type = success_candidate_reference
archetype = KOREAN_BIOTECH_TECH_EXPORT_STAGE2
```

### stage date

```text
Stage 1:
2025-12-15
- Korean biotech ADEL signs major Alzheimer's drug co-development/commercialization deal with Sanofi.
- Korean neurodegenerative pipeline enters global pharma validation path.

Stage 2:
2025-12-15
- deal worth up to $1.04B.
- upfront payment: $80M.
- ADEL-Y01 antibody therapy targets harmful forms of tau-related protein.
- currently in early-stage human trials in U.S.
- Sanofi praises distinct tau acetylation approach.

Stage 3:
없음
- unlisted tech export is not listed Korean biotech Green.
- Green requires Phase 2/3 data, milestone probability, royalty economics, listed read-through if any.
```

ADEL은 상장사는 아니지만 R7에서 **기술수출 Stage 2 reference**로 중요하다. Reuters는 ADEL이 Sanofi와 최대 $1.04B 규모의 Alzheimer’s drug deal을 체결했고, upfront는 $80M이라고 보도했다. 다만 early-stage human trial 단계라서, listed biotech scoring에는 직접 Green으로 전이하면 안 된다. ([Reuters][8])

### 실제 가격경로 검증

```json
{
  "case_id": "r7_loop14_adel_sanofi_alzheimers_tech_export_reference",
  "symbol": "unlisted",
  "stage2_date": "2025-12-15",
  "stage3_price": null,
  "price_data_source": "Reuters ADEL-Sanofi deal anchor",
  "deal_value_max_usd_bn": 1.04,
  "upfront_payment_usd_mn": 80,
  "candidate": "ADEL-Y01",
  "disease_area": "Alzheimer's disease",
  "mechanism_context": "tau acetylation / harmful tau-related protein forms",
  "clinical_stage": "early-stage human trials in U.S.",
  "listed_stock_readthrough_confirmed": false,
  "price_validation_status": "unlisted_reference_no_ohlc"
}
```

### alignment

```text
score_price_alignment = success_candidate_reference_only
rerating_result = KOREAN_BIOTECH_TECH_EXPORT_STAGE2
stage_failure_type = upfront_milestone_deal_not_phase3_royalty_green
```

---

## Case H — Global clinical/FDA failure reference `sector hard 4C reference`

```text
symbol = global_reference
case_type = sector_hard_4C_reference
archetype = GLOBAL_CLINICAL_FAILURE_HARD_4C_REFERENCE
```

### stage date

```text
Reference 1:
2024-07-08
- HilleVax stops infant norovirus vaccine development after Phase 2 failure.
- efficacy only 5%.
- shares plunge as much as -87.6% to record low $1.75.

Reference 2:
2025-12-31
- Corcept shares fall 50.8% after FDA rejects relacorilant application.
- stock moves from $70.20 to $34.51.
- market value falls by $3.7B.

Reference 3:
2026-03-04
- FDA places partial clinical hold on PepGen rare muscle-disease drug trial.
- shares down more than 25% in extended trading.
- regulator concerns tied to earlier lab/animal studies, not patient safety data.
```

이번 R7에서는 직접 KRX hard 4C를 확정하지 않는다. 대신 글로벌 임상/FDA failure reference를 hard gate로 둔다. HilleVax는 mid-stage trial에서 efficacy 5%로 개발을 중단하자 -87.6%까지 급락했고, Corcept는 FDA rejection 이후 -50.8%, PepGen은 partial clinical hold 이후 -25% 이상 하락했다. 이 reference는 R7 scoring에서 **임상/FDA event가 valuation을 한 번에 재설정한다**는 hard rule이다. ([Reuters][9])

### 실제 가격경로 검증

```json
{
  "case_id": "r7_loop14_global_clinical_fda_failure_hard_reference",
  "symbol": "global_reference",
  "stage4c_reference_dates": ["2024-07-08", "2025-12-31", "2026-03-04"],
  "stage3_price": null,
  "price_data_source": "Reuters/Barron's clinical trial failure and FDA rejection/hold anchors",
  "hillevax_trial_efficacy_pct": 5,
  "hillevax_event_mae_pct": -87.6,
  "hillevax_event_low_usd": 1.75,
  "corcept_event_mae_pct": -50.8,
  "corcept_price_before_usd": 70.20,
  "corcept_price_after_usd": 34.51,
  "corcept_market_value_loss_usd_bn": 3.7,
  "pepgen_after_hours_mae_pct": -25,
  "direct_krx_hard_4c_confirmed": false,
  "use_as_sector_hard_reference": true
}
```

### alignment

```text
score_price_alignment = thesis_break_reference
rerating_result = GLOBAL_CLINICAL_FAILURE_HARD_4C_REFERENCE
stage_failure_type = clinical_or_FDA_failure_resets_pipeline_valuation
```

---

# 5. 이번 R7 case별 stage date 요약

| case                        | Stage 1                  | Stage 2                        | Stage 3   | Stage 4B               | Stage 4C                          |
| --------------------------- | ------------------------ | ------------------------------ | --------- | ---------------------- | --------------------------------- |
| Samsung Biologics           | 2025 tariff/localization | 2025-12-22 U.S. facility       | N/A       | N/A                    | price failed                      |
| Celltrion                   | 2025-07 preferred bidder | 2025-09/11 U.S. facility       | N/A       | N/A                    | tariff/facility execution watch   |
| SK Bioscience               | 2024-06 M&A              | 2024-06 IDT acquisition        | N/A       | +11.7% event premium   | integration/utilization watch     |
| Alteogen                    | 2024-11 trial            | 2025-03 / 2025-09 FDA approval | candidate | patent/adoption watch  | patent dispute watch              |
| Yuhan                       | 2024-08 FDA approval     | 2024-08 oncology approval      | N/A       | launch premium watch   | 2024-12 manufacturing CRL watch   |
| Hugel                       | 2025 U.S. launch         | 2025-03 Letybo U.S. rollout    | N/A       | U.S. aesthetic premium | category safety/counterfeit watch |
| ADEL                        | 2025-12 Sanofi deal      | 2025-12 $1.04B deal            | N/A       | tech-export premium    | early-stage trial risk            |
| Global clinical failure ref | 2024~2026                | N/A                            | N/A       | N/A                    | sector hard reference             |

---

# 6. 실제 가격경로 검증 총괄

| case                 |                                           가격·거래 anchor | 해석                             | 판정                             |
| -------------------- | -----------------------------------------------------: | ------------------------------ | ------------------------------ |
| Samsung Biologics    |                     $280M facility, -0.4% vs KOSPI +2% | evidence good but price failed | evidence_good_but_price_failed |
| Celltrion            |            $330M acquisition, up to 700B won expansion | tariff hedge Stage 2           | success_candidate              |
| SK Bioscience        |                             339B won IDT stake, +11.7% | M&A event premium              | success_candidate              |
| Alteogen             |     Keytruda Qlex FDA approval, 30~40% adoption target | strong structural candidate    | success_candidate              |
| Yuhan                | J&J combo FDA approval, $5B+ Rybrevant peak-sales goal | oncology royalty Stage 2       | success_candidate              |
| Hugel                |          Letybo U.S. launch, FDA warning category risk | medical aesthetic Stage 2      | success_candidate              |
| ADEL                 |                       $1.04B Sanofi deal, $80M upfront | tech-export Stage 2 reference  | reference                      |
| Clinical failure ref |          HilleVax -87.6%, Corcept -50.8%, PepGen -25%+ | global hard 4C reference       | thesis_break_reference         |

---

# 7. score-price alignment 판정

```text
aligned:
- none fully confirmed with full OHLC.
- Alteogen is strongest Stage 3 candidate but direct adjusted OHLC unavailable.

structural_success_candidate:
- Alteogen / Keytruda Qlex.
- Samsung Biologics and Celltrion, if U.S. facilities convert into utilization and tariff savings.
- SK Bioscience, if IDT integration creates CDMO backlog and margin.

success_candidate:
- Yuhan / Lazertinib.
- Hugel / Letybo.
- ADEL / Sanofi as unlisted reference.

evidence_good_but_price_failed:
- Samsung Biologics, because GSK facility news saw -0.4% while KOSPI +2%.

event_premium:
- SK Bioscience +11.7% on IDT acquisition.
- Hugel/Letybo U.S. aesthetic launch if traded before physician adoption.
- ADEL/Sanofi if applied to listed read-through before milestones.

price_moved_without_evidence:
- Any Alteogen read-through before royalty/adoption/patent clarity.
- Any CDMO localization rally before facility utilization.
- Any tech-export rally before milestone probability and Phase 2/3 data.

thesis_break_watch:
- Yuhan/J&J manufacturing CRL for injectable Rybrevant formulation.
- Alteogen patent dispute risk.
- Hugel category safety/counterfeit-product regulation.
- Samsung Biologics/Celltrion facility execution risk.

sector_hard_4C_reference:
- HilleVax clinical failure.
- Corcept FDA rejection.
- PepGen partial clinical hold.

direct_KRX_hard_4C_confirmed:
- false
```

---

# 8. 점수비중 교정

## 올릴 축

```text
FDA_approval_to_launch_conversion +5
royalty_milestone_probability +5
facility_utilization +5
FDA_inspection_and_tech_transfer +5
CMO_recurring_order_visibility +5
clinical_endpoint_quality +5
partner_execution_quality +5
patent_IP_freedom_to_operate +5
reimbursement_and_market_access +5
physician_adoption_sellthrough +4
```

### 왜 올리나

Samsung Biologics는 좋은 facility acquisition에도 주가가 KOSPI 대비 underperform했다. Celltrion은 U.S. tariff hedge가 좋지만 facility utilization이 필요하다. SK Bioscience는 M&A 발표 후 +11.7%였지만 integration과 backlog가 필요하다. Alteogen은 FDA approval까지 간 강한 후보지만 patent dispute와 adoption/royalty gate가 남는다. HilleVax, Corcept, PepGen reference는 clinical/FDA failure가 valuation을 한 번에 끊을 수 있음을 보여준다.

## 내릴 축

```text
FDA_headline_only -5
facility_acquisition_only -5
CMO_capacity_without_utilization -5
tech_export_upfront_only -5
early_stage_deal_without_phase2_3 -5
approval_without_reimbursement -4
aesthetic_launch_without_doctor_adoption -4
patent_dispute_unresolved -5
clinical_hold_or_CRL -5
```

### 왜 내리나

R7에서 가장 큰 함정은 “허가/계약/공장/기술수출이 나왔다”를 곧바로 Stage 3로 주는 것이다. 바이오는 증거의 층위가 길다. FDA approval도 launch와 reimbursement를 지나야 매출이고, CMO capacity도 batch slot이 차야 매출이며, upfront도 milestone probability가 낮으면 valuation을 지탱하지 못한다.

---

# 9. Green gate 강화 조건

```text
R7 Stage 3-Green 필수:
1. FDA/EMA/MFDS approval 이후 실제 launch 확인.
2. reimbursement / formulary / market access 확인.
3. 기술수출은 upfront보다 milestone probability와 partner execution 확인.
4. CMO/CDMO는 facility capacity보다 utilization, tech transfer, inspection 결과 확인.
5. biosimilar는 pricing, market share, interchangeability / payer adoption 확인.
6. 의료미용은 FDA approval보다 physician adoption, distributor margin, safety compliance 확인.
7. 특허/IP dispute가 있으면 Green 유예.
8. 임상은 endpoint quality, sample size, adverse event, regulatory path 확인.
9. price path가 evidence 이후 따라옴.
```

---

# 10. 4B 조기감지 조건

```text
4B-watch:
- FDA approval headline 후 실제 launch/reimbursement 전 급등.
- 기술수출 upfront/milestone 총액만으로 valuation 확장.
- CDMO facility acquisition/capacity만으로 margin 전 rerating.
- KOSDAQ 바이오가 global partner name 하나로 급등.
- aesthetic product U.S. launch 전 physician adoption 없이 과열.
- unlisted Korean biotech deal을 listed peers로 무리하게 read-through.
```

---

# 11. 4C hard gate 조건

```text
Hard 4C:
- FDA CRL / rejection.
- clinical hold.
- pivotal trial primary endpoint failure.
- partner termination / milestone cancellation.
- FDA inspection failure at key facility.
- reimbursement failure after approval.
- patent injunction or freedom-to-operate failure.
- serious safety signal / product recall.
```

이번 R7 Loop 14에서는 직접 KRX hard 4C는 확정하지 않는다. 대신 **HilleVax -87.6%, Corcept -50.8%, PepGen -25%+**를 sector hard reference로 둔다. 국내 상장사에서는 **Samsung Biologics price-failed facility acquisition**, **Yuhan/J&J manufacturing CRL watch**, **Alteogen patent/adoption gate**, **SK Bioscience M&A integration gate**가 핵심 shadow calibration이다.

---

# 12. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 13. 레포 반영용 patch-ready 출력

## docs/round/round_217.md 요약

```md
# R7 Loop 14. Bio / Healthcare / Medical Device Price Validation

이번 라운드는 R7 Loop 14 price-validation 라운드다.

핵심 결론:
- Samsung Biologics is evidence_good_but_price_failed. It agreed to acquire its first U.S. production facility from GSK for $280M, adding 60,000L drug-substance capacity, but shares fell -0.4% while KOSPI gained +2%. U.S. facility acquisition is Stage 2; utilization, FDA inspection, tech transfer and recurring orders required.
- Celltrion is U.S. tariff-hedge success_candidate. It acquired ImClone Systems from Eli Lilly for $330M and later planned up to 700B won / $478M U.S. expansion. Product transfer, tariff saving, utilization and biosimilar market share required.
- SK Bioscience is vaccine/CDMO M&A event premium. It acquired a 60% stake in Germany’s IDT Biologika for 339B won / $243.75M, and shares rose +11.7%. M&A control is Stage 2; CDMO backlog and margin required.
- Alteogen is the strongest structural success_candidate. Merck’s Keytruda Qlex was FDA-approved; Keytruda generated nearly $30B sales in 2024, Merck targets 30~40% patient adoption within two years, and Alteogen develops/manufactures the enzyme used in the formulation. Patent/IP and royalty adoption remain gates.
- Yuhan / Lazertinib is oncology license Stage 2. FDA approved J&J’s Rybrevant + lazertinib first-line EGFR-mutated NSCLC regimen; J&J expects Rybrevant peak sales above $5B. Later injectable Rybrevant CRL tied to facility inspection shows manufacturing regulatory risk.
- Hugel / Letybo is medical-aesthetic U.S. launch Stage 2. Letybo entered U.S. dermatology practices after FDA approval for glabellar lines, but physician adoption, distributor margin and botulinum-toxin safety/compliance remain gates.
- ADEL / Sanofi is Korean biotech tech-export reference. Deal worth up to $1.04B with $80M upfront for Alzheimer’s antibody ADEL-Y01. Early-stage clinical status means not Stage 3.
- Global clinical/FDA failure reference confirms hard 4C logic. HilleVax -87.6% after Phase 2 failure, Corcept -50.8% after FDA rejection, PepGen -25%+ after partial clinical hold.
```

## docs/checkpoints/checkpoint_28a_round217_r7_loop14.md 요약

```md
# Checkpoint 28A Round 217 R7 Loop 14 Bio Healthcare Medical Device Price Validation

## 반영 내용
- R7 Loop 14 price-validation 라운드를 추가했다.
- Samsung Biologics, Celltrion, SK Bioscience, Alteogen, Yuhan, Hugel, ADEL, global clinical/FDA failure reference를 비교했다.
- Reuters / WSJ / MarketWatch / AP / FT anchors로 가능한 event MFE/MAE, deal value, facility capacity, FDA approval, adoption target, clinical/FDA failure drawdown을 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- FDA approval-to-launch conversion, royalty/milestone probability, facility utilization, FDA inspection/tech transfer, CMO recurring order visibility, clinical endpoint quality, partner execution, patent freedom-to-operate, reimbursement/market access, physician adoption 가중치 강화.
- FDA headline-only, facility acquisition-only, CMO capacity without utilization, tech-export upfront-only, early-stage deal without Phase 2/3, approval without reimbursement, patent dispute unresolved, clinical hold/CRL 감점 강화.
```

## data/e2r_case_library/cases_r7_loop14_round217.jsonl 초안

```jsonl
{"case_id":"r7_loop14_samsung_biologics_gsk_us_facility","symbol":"207940","company_name":"Samsung Biologics","case_type":"evidence_good_but_price_failed","primary_archetype":"BIO_CMO_US_LOCALIZATION_STAGE2","stage2_date":"2025-12-22","price_validation":{"price_data_source":"Reuters Samsung Biologics-GSK facility event anchor","stage3_price":null,"acquisition_value_usd_mn":280,"facility_location":"Rockville, Maryland","facility_capacity_liters":60000,"expected_close":"2026_Q1_end","korean_pharma_tariff_cap_pct":15,"generic_drugs_tariff_free":true,"event_mae_pct":-0.4,"kospi_same_context_pct":2.0,"relative_underperformance_pp":-2.4,"facility_utilization_confirmed":false,"fda_inspection_transfer_confirmed":false,"mfe_30d_90d_180d_1y":"price_data_unavailable_after_deep_search","mae_30d_90d_180d_1y":"price_data_unavailable_after_deep_search"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"BIO_CMO_US_LOCALIZATION_STAGE2","notes":"U.S. facility acquisition underperformed market; utilization and margin required."}
{"case_id":"r7_loop14_celltrion_us_factory_tariff_hedge","symbol":"068270","company_name":"Celltrion","case_type":"success_candidate_price_unavailable","primary_archetype":"BIOSIMILAR_US_TARIFF_HEDGE_STAGE2","stage1_date":"2025-07-29","stage2_date":"2025-09-23/2025-11-19","price_validation":{"price_data_source":"Reuters Celltrion U.S. factory acquisition and expansion anchors","stage3_price":null,"factory_acquisition_value_usd_mn":330,"target_seller":"Eli Lilly / ImClone Systems LLC","additional_capacity_investment_krw_bn":700,"additional_capacity_investment_usd_mn":478.17,"tariff_hedge_rationale":true,"product_transfer_confirmed":false,"us_factory_utilization_confirmed":false,"direct_event_return":"price_data_unavailable_after_deep_search","mfe_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_price_data_unavailable","rerating_result":"BIOSIMILAR_US_TARIFF_HEDGE_STAGE2","notes":"U.S. tariff hedge is Stage 2; product transfer, utilization and margin required."}
{"case_id":"r7_loop14_sk_bioscience_idt_biologika_ma","symbol":"302440","company_name":"SK Bioscience","case_type":"event_premium_success_candidate","primary_archetype":"VACCINE_CDMO_MA_EVENT_PREMIUM","stage2_date":"2024-06-27","price_validation":{"price_data_source":"Reuters SK Bioscience-IDT Biologika M&A anchor","stage3_price":null,"acquired_stake_pct":60,"deal_value_krw_bn":339,"deal_value_usd_mn":243.75,"seller_retained_stake_pct":40,"ipo_2021_raise_usd_bn":1.33,"event_mfe_pct":11.7,"novavax_partnership_validation":true,"cdmo_backlog_confirmed":false,"plant_utilization_confirmed":false,"mfe_30d_90d":"price_data_unavailable_after_deep_search","mae_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"VACCINE_CDMO_MA_STAGE2","notes":"IDT acquisition drove +11.7%, but integration/backlog/margin required."}
{"case_id":"r7_loop14_alteogen_keytruda_qlex_sc_formulation","symbol":"196170","company_name":"Alteogen","case_type":"structural_success_candidate_price_unavailable","primary_archetype":"BLOCKBUSTER_SC_FORMULATION_STAGE3_CANDIDATE","stage1_date":"2024-11-19","stage2_date":"2025-03-27","stage3_date":"2025-09-19_candidate","price_validation":{"price_data_source":"Reuters Keytruda SC trial/launch/approval anchors + WSJ patent-dispute anchor","stage3_price":null,"keytruda_2024_sales_usd_bn":30,"target_peak_adoption_pct_range":"30-40","administration_time_sc_minutes":"1-2","administration_time_iv_minutes":30,"us_availability_expected":"late_2025_09","alteogen_enzyme_role":"develops_and_manufactures_enzyme_used_with_Keytruda_SC","patent_dispute_watch":true,"royalty_conversion_confirmed":false,"alteogen_direct_ohlc":"price_data_unavailable_after_deep_search","mfe_30d_90d_180d_1y":"price_data_unavailable_after_deep_search"},"score_price_alignment":"structural_success_candidate_but_price_data_unavailable","rerating_result":"BLOCKBUSTER_SC_FORMULATION_STAGE3_CANDIDATE","notes":"FDA approval and adoption target are strong; royalty, adoption and patent freedom-to-operate required."}
{"case_id":"r7_loop14_yuhan_lazertinib_jnj_rybrevant_approval","symbol":"000100","company_name":"Yuhan","case_type":"success_candidate_price_unavailable","primary_archetype":"ONCOLOGY_LICENSE_ROYALTY_STAGE2","stage2_date":"2024-08-20","stage4c_date":"2024-12-16_watch","price_validation":{"price_data_source":"Reuters FDA approval and later CRL anchors","stage3_price":null,"indication":"first-line EGFR-mutated non-small cell lung cancer","combination":"Rybrevant + lazertinib","rybrevant_peak_sales_expectation_usd_bn":5,"pfs_benefit_vs_tagrisso":true,"later_crl_related_to":"pre-approval inspection at manufacturing facility","later_crl_not_related_to":["formulation","efficacy","safety_data"],"iv_rybrevant_unaffected":true,"yuhan_direct_price_anchor":"price_data_unavailable_after_deep_search","mfe_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_price_data_unavailable","rerating_result":"ONCOLOGY_LICENSE_ROYALTY_STAGE2","notes":"FDA approval is Stage 2; royalty economics, launch uptake and manufacturing regulatory gate remain."}
{"case_id":"r7_loop14_hugel_letybo_us_aesthetic_launch","symbol":"145020","company_name":"Hugel","case_type":"success_candidate_regulatory_watch","primary_archetype":"AESTHETIC_MEDICAL_DEVICE_US_LAUNCH_STAGE2","stage2_date":"2025-03","stage4c_date":"2025-11_watch","price_validation":{"price_data_source":"Allure Letybo U.S. launch context + AP FDA counterfeit Botox warning","stage3_price":null,"product":"Letybo / Botulax","us_indication":"glabellar_lines","category":"botulinum_toxin_A_neuromodulator","pricing_advantage_context":true,"category_safety_watch":true,"physician_adoption_confirmed":false,"distributor_margin_confirmed":false,"hugel_direct_ohlc":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_price_data_unavailable","rerating_result":"AESTHETIC_MEDICAL_US_LAUNCH_STAGE2","notes":"FDA approval and U.S. launch need physician adoption, distributor margin and safety compliance."}
{"case_id":"r7_loop14_adel_sanofi_alzheimers_tech_export_reference","symbol":"unlisted","company_name":"ADEL / Sanofi","case_type":"success_candidate_reference_only","primary_archetype":"KOREAN_BIOTECH_TECH_EXPORT_STAGE2","stage2_date":"2025-12-15","price_validation":{"price_data_source":"Reuters ADEL-Sanofi deal anchor","stage3_price":null,"deal_value_max_usd_bn":1.04,"upfront_payment_usd_mn":80,"candidate":"ADEL-Y01","disease_area":"Alzheimer's disease","mechanism_context":"tau acetylation / harmful tau-related protein forms","clinical_stage":"early-stage human trials in U.S.","listed_stock_readthrough_confirmed":false,"price_validation_status":"unlisted_reference_no_ohlc"},"score_price_alignment":"success_candidate_reference_only","rerating_result":"KOREAN_BIOTECH_TECH_EXPORT_STAGE2","notes":"Upfront/milestone deal is Stage 2; Phase 2/3 data and royalty probability required."}
{"case_id":"r7_loop14_global_clinical_fda_failure_hard_reference","symbol":"global_reference","company_name":"HilleVax / Corcept / PepGen reference","case_type":"sector_hard_4c_reference","primary_archetype":"GLOBAL_CLINICAL_FAILURE_HARD_4C_REFERENCE","stage4c_date":"2024-07-08/2025-12-31/2026-03-04_reference","price_validation":{"price_data_source":"Reuters/Barron's clinical trial failure and FDA rejection/hold anchors","stage3_price":null,"hillevax_trial_efficacy_pct":5,"hillevax_event_mae_pct":-87.6,"hillevax_event_low_usd":1.75,"corcept_event_mae_pct":-50.8,"corcept_price_before_usd":70.20,"corcept_price_after_usd":34.51,"corcept_market_value_loss_usd_bn":3.7,"pepgen_after_hours_mae_pct":-25,"direct_krx_hard_4c_confirmed":false,"use_as_sector_hard_reference":true},"score_price_alignment":"thesis_break_reference","rerating_result":"GLOBAL_CLINICAL_FAILURE_HARD_4C_REFERENCE","notes":"Clinical/FDA failure can reset biotech valuation immediately; use as hard 4C reference."}
```

## data/sector_taxonomy/score_weight_profiles_round217_r7_loop14_v1.csv 초안

```csv
archetype,fda_approval_to_launch_conversion,royalty_milestone_probability,facility_utilization,fda_inspection_tech_transfer,cmo_recurring_order_visibility,clinical_endpoint_quality,partner_execution_quality,patent_ip_freedom_to_operate,reimbursement_market_access,physician_adoption_sellthrough,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
BIO_CMO_US_LOCALIZATION_STAGE2,+3,+1,+5,+5,+5,+2,+4,+2,+2,+0,-5,+4,+4,Samsung Biologics shows facility acquisition is not Green without utilization and margin.
BIOSIMILAR_US_TARIFF_HEDGE_STAGE2,+4,+3,+5,+5,+4,+3,+4,+3,+5,+0,-5,+4,+4,Celltrion U.S. factory hedge needs product transfer, market share and tariff savings.
VACCINE_CDMO_MA_EVENT_PREMIUM,+3,+1,+5,+5,+5,+3,+4,+2,+3,+0,-5,+5,+4,SK Bioscience IDT acquisition needs CDMO backlog, integration and margin.
BLOCKBUSTER_SC_FORMULATION_STAGE3_CANDIDATE,+5,+5,+2,+4,+2,+5,+5,+5,+5,+4,-3,+5,+4,Alteogen/Keytruda Qlex needs adoption, royalty and patent freedom-to-operate.
ONCOLOGY_LICENSE_ROYALTY_STAGE2,+5,+5,+2,+4,+1,+5,+5,+4,+5,+0,-4,+4,+4,Yuhan/Lazertinib needs launch uptake, royalty economics and manufacturing gate.
AESTHETIC_MEDICAL_DEVICE_US_LAUNCH_STAGE2,+5,+3,+1,+3,+1,+3,+4,+3,+2,+5,-4,+5,+3,Hugel/Letybo needs physician adoption, distributor margin and safety compliance.
KOREAN_BIOTECH_TECH_EXPORT_STAGE2,+3,+5,+0,+1,+0,+5,+5,+4,+3,+0,-5,+5,+4,ADEL/Sanofi upfront deal is Stage 2 until Phase 2/3 and royalty probability improve.
GLOBAL_CLINICAL_FAILURE_HARD_4C_REFERENCE,+5,+5,+0,+5,+0,+5,+3,+5,+5,+0,0,+5,+5,Trial failure, FDA rejection or clinical hold must be hard 4C reference.
```

---

# 이번 R7 Loop 14 결론

```text
1. Samsung Biologics는 evidence_good_but_price_failed다.
   $280M U.S. facility 인수에도 주가는 -0.4%, KOSPI는 +2%였다.

2. Celltrion은 U.S. tariff hedge success_candidate다.
   $330M factory acquisition과 700B won expansion은 좋지만 제품 이전·가동률·margin이 필요하다.

3. SK Bioscience는 CDMO M&A event premium이다.
   IDT Biologika 60% 인수에 주가 +11.7%였지만 integration과 backlog가 Stage 3 조건이다.

4. Alteogen은 R7의 가장 강한 structural success_candidate다.
   Keytruda Qlex FDA approval과 30~40% adoption target은 강하지만 royalty conversion과 patent risk가 남아 있다.

5. Yuhan은 oncology royalty Stage 2다.
   FDA approval은 좋지만 royalty economics, launch uptake, 제조시설 regulatory gate가 필요하다.

6. Hugel은 medical-aesthetic U.S. launch Stage 2다.
   Letybo FDA approval 이후 physician adoption과 safety compliance가 Green 조건이다.

7. ADEL/Sanofi는 Korean biotech tech-export reference다.
   $1.04B deal과 $80M upfront는 Stage 2지만 early-stage라 Green은 아니다.

8. 이번 R7에서는 직접 KRX hard 4C는 확정하지 않는다.
   대신 HilleVax -87.6%, Corcept -50.8%, PepGen -25%+를 sector hard 4C reference로 둔다.
```

한 문장으로 압축하면:

> **R7에서 진짜 Stage 3는 “FDA·CMO·기술수출·Keytruda·미국 공장·의료미용이 좋다”가 아니라, approval-to-launch·facility utilization·royalty conversion·partner execution·patent freedom·reimbursement·physician adoption이 실제 숫자로 닫히는 순간이다.**

[1]: https://www.reuters.com/business/healthcare-pharmaceuticals/samsung-biologics-buy-us-drug-production-facility-gsk-280-mln-2025-12-21/ "https://www.reuters.com/business/healthcare-pharmaceuticals/samsung-biologics-buy-us-drug-production-facility-gsk-280-mln-2025-12-21/"
[2]: https://www.reuters.com/business/healthcare-pharmaceuticals/celltrion-unit-pays-330-million-eli-lilly-production-facility-filing-shows-2025-09-23/ "https://www.reuters.com/business/healthcare-pharmaceuticals/celltrion-unit-pays-330-million-eli-lilly-production-facility-filing-shows-2025-09-23/"
[3]: https://www.reuters.com/markets/deals/south-koreas-sk-bioscience-buy-control-germanys-idt-biologika-244-mln-2024-06-27/ "https://www.reuters.com/markets/deals/south-koreas-sk-bioscience-buy-control-germanys-idt-biologika-244-mln-2024-06-27/"
[4]: https://www.reuters.com/business/healthcare-pharmaceuticals/novavax-raises-annual-revenue-forecast-vaccine-supply-partnerships-2025-08-06/ "https://www.reuters.com/business/healthcare-pharmaceuticals/novavax-raises-annual-revenue-forecast-vaccine-supply-partnerships-2025-08-06/"
[5]: https://www.reuters.com/business/healthcare-pharmaceuticals/merck-says-keytruda-injection-par-with-approved-iv-version-trial-2024-11-19/ "https://www.reuters.com/business/healthcare-pharmaceuticals/merck-says-keytruda-injection-par-with-approved-iv-version-trial-2024-11-19/"
[6]: https://www.reuters.com/business/healthcare-pharmaceuticals/us-fda-approves-jjs-combination-therapy-type-lung-cancer-2024-08-20/ "https://www.reuters.com/business/healthcare-pharmaceuticals/us-fda-approves-jjs-combination-therapy-type-lung-cancer-2024-08-20/"
[7]: https://www.allure.com/story/letybo-neuromodulator-injectable "https://www.allure.com/story/letybo-neuromodulator-injectable"
[8]: https://www.reuters.com/business/healthcare-pharmaceuticals/south-koreas-adel-signs-up-104-billion-alzheimers-drug-development-deal-with-2025-12-15/ "https://www.reuters.com/business/healthcare-pharmaceuticals/south-koreas-adel-signs-up-104-billion-alzheimers-drug-development-deal-with-2025-12-15/"
[9]: https://www.reuters.com/business/healthcare-pharmaceuticals/hillevax-shares-plummet-after-norovirus-vaccine-fails-mid-stage-study-2024-07-08/ "https://www.reuters.com/business/healthcare-pharmaceuticals/hillevax-shares-plummet-after-norovirus-vaccine-fails-mid-stage-study-2024-07-08/"
