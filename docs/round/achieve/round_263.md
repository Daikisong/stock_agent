순서상 이번은 **R7 Loop 12 — 바이오·헬스케어·의료기기 가격경로 검증 라운드**다.

```text
round = R7 Loop 12
round_id = round_191
large_sector = BIOTECH_HEALTHCARE_MEDICAL_DEVICE
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = false
```

이번 R7 Loop 12는 지난 R7의 Alteogen·Yuhan·Samsung Bio·Celltrion 중심축을 반복하지 않고, **미용의료기기, 홈/클리닉 beauty device, 톡신 미국 진출, 불법·비공식 톡신 유통, 의료AI 외부검증, 의사파업/의대정원 리스크, 치과·임플란트 M&A**를 중심으로 본다.

---

# 1. 이번 라운드 대섹터

```text
R7 = 바이오·헬스케어·의료기기
```

R7에서 Stage 3는 “FDA 승인”, “M&A”, “논문 AUC”, “K-aesthetic”, “AI 진단”, “의료정책”이라는 말이 아니다.

진짜 Stage 3는 **시술량·처방량·소모품 반복매출·설치대수·utilization·보험/수가·gross margin·FCF·안전/규제 신뢰**가 확인되는 순간이다.

---

# 2. 대상 canonical archetype

```text
AESTHETIC_EBD_GLOBAL_BUYOUT
BEAUTY_DEVICE_CONSUMER_CLINIC_CROSSOVER
AESTHETIC_DEVICE_EXPORT_PLATFORM
BOTULINUM_TOXIN_US_LAUNCH
UNAPPROVED_TOXIN_SAFETY_TRUST_4C
MEDICAL_AI_EXTERNAL_VALIDATION_NOT_REVENUE
MEDICAL_SERVICE_DISRUPTION_POLICY_4C
DENTAL_IMPLANT_GLOBAL_M_AND_A
```

---

# 3. deep sub-archetype

```text
미용의료기기:
- Jeisys Medical
- Classys
- EBD / HIFU / RF / laser / body contouring
- device installed base + consumables + overseas clinic channel
- buyout / delisting / PE validation

Beauty device crossover:
- APR / Medicube
- at-home beauty devices
- overseas revenue, TikTok / influencer demand
- device concentration / regulatory boundary

톡신:
- Hugel / Letybo
- FDA approval / U.S. launch
- price advantage vs Botox
- provider adoption / repeat procedures / distributor execution

안전·규제:
- Medytox / Innotox
- unauthorized online use / DIY injection
- FDA warning letters / UK concern
- patient safety / brand trust / regulatory gate

AI 진단:
- Lunit
- external validation AUC
- subgroup weakness
- reimbursement / hospital adoption / recurring revenue

의료정책:
- doctors’ strike / medical-school quota
- elective procedures / hospital utilization / medtech access
- policy uncertainty

치과:
- Osstem Implant / ZimVie
- dental implant M&A
- delisted Korean buyer / U.S. target event
```

---

# 4. 국장 신규 후보 case

## Case A — Jeisys Medical `structural_success_candidate / PE buyout`

```text
symbol = 287410, delisting process after ArchiMed deal
case_type = structural_success_candidate
archetype = AESTHETIC_EBD_GLOBAL_BUYOUT
```

### stage date

```text
Stage 1:
2024-06
- ArchiMed tender offer / control transaction
- energy-based aesthetic device market expansion
- Korean EBD manufacturer global buyout validation

Stage 2:
2024-09-11
- ArchiMed finalizing roughly $742M acquisition
- Jeisys shares closed at 12,860 won before delisting process
- revenue CAGR 44% to $107M through FY2023
- adjusted pretax earnings CAGR 45% to $31M
- EBD global market expected >$16B by 2032 vs about $4.5B prior year

Stage 3:
보류
- listed equity is delisting, so post-deal public-stock Stage 3 tracking 불가
- 하지만 business-quality validation은 강함

Stage 4B:
buyout premium / delisting premium으로 public price가 먼저 닫힌 구간

Stage 4C:
delisting 이후 public-market tracking 불가능, acquisition leverage / integration risk
```

Jeisys는 R7 Loop 12에서 “미용의료기기 사업 품질은 검증됐지만, 상장주로는 더 이상 Stage 3 추적이 어렵다”는 case다. ArchiMed는 Jeisys를 약 $742M에 인수하고 delisting process를 시작했으며, Jeisys의 FY2023까지 3년 매출 CAGR은 44%, adjusted pretax earnings CAGR은 45%로 제시됐다. WSJ는 Jeisys가 RF·ultrasound·laser 기반 EBD를 만들고, aesthetic EBD 시장이 약 $4.5B에서 2032년 $16B 이상으로 커질 전망이라고 전했다. ([월스트리트저널][1])

### 실제 가격경로 검증

```text
price_data_source:
WSJ ArchiMed / Jeisys acquisition anchor

entry_date:
2024-09-11 evidence date

stage3_price:
N/A

stage2_price_anchor:
12,860 won

deal_value:
$742M

Jeisys_FY2023_revenue:
$107M

Jeisys_FY2023_adjusted_pretax_earnings:
$31M

revenue_CAGR_through_FY2023:
+44%

adjusted_pretax_earnings_CAGR:
+45%

deal_value_to_revenue:
742 / 107
= 6.93x

deal_value_to_adjusted_pretax_earnings:
742 / 31
= 23.9x

global_EBD_market_prior:
about $4.5B

global_EBD_market_2032_expected:
>$16B

market_growth_multiple:
16 / 4.5
= >3.56x

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

reason:
- WSJ provides transaction and price anchor.
- Delisting process makes post-event public adjusted OHLC unsuitable for Stage 3 tracking.
```

### alignment

```text
score_price_alignment = structural_success_candidate
rerating_result = aesthetic_EBD_business_quality_validated
stage_failure_type = public_equity_tracking_closed_after_delisting
```

---

## Case B — APR / Medicube device `structural_success + 4B concentration watch`

```text
symbol = 278470
case_type = structural_success_candidate + 4B-watch
archetype = BEAUTY_DEVICE_CONSUMER_CLINIC_CROSSOVER
```

### stage date

```text
Stage 1:
2025
- at-home beauty device boom
- K-beauty device + skincare hybrid
- U.S. social-commerce demand

Stage 2:
2025-10-20
- APR stock price more than four-fold since January
- market value about $6B
- $180 facial skincare device promoted on TikTok
- device forms about one-third of U.S. sales
- overseas revenue nearly 80% of Q2 2025 revenue
- revenue up sevenfold since 2018

Stage 3:
보류
- revenue conversion은 강하나 R7 관점에서는 medical/aesthetic device boundary, concentration, channel durability 확인 필요

Stage 4B:
- four-fold stock rise
- device/social-commerce concentration
- beauty-device premium이 medical/aesthetic category로 과도 확장될 경우 watch
```

APR은 R5에서 beauty brand로 봤지만, R7에서는 “consumer beauty device가 quasi-medical aesthetic demand로 넘어가는가”를 보는 crossover case다. FT는 APR 주가가 2025년 1월 이후 4배 이상 올랐고 market value가 약 $6B에 도달했으며, $180 facial skincare device가 U.S. sales의 약 3분의 1을 만들고 Q2 2025 매출의 거의 80%가 해외에서 나왔다고 보도했다. 다만 R7 Green은 단순 viral device가 아니라 반복구매·소모품·clinic crossover·규제 boundary·채널 유지율까지 봐야 한다. ([Financial Times][2])

### 실제 가격경로 검증

```text
price_data_source:
FT APR / beauty-device anchor

stage3_price:
N/A

reported_stock_return_since_January_2025:
> +300%  (more than four-fold)

market_value:
about $6B

device_price:
$180

device_share_of_U.S._sales:
about one-third

Q2_2025_overseas_revenue_share:
nearly 80%

revenue_growth_since_2018:
7x

MFE_from_January_2025_minimum:
> +300%

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = aligned_partial
rerating_result = beauty_device_structural_rerating_candidate
stage_failure_type = current_state_4B_concentration_watch
```

---

## Case C — Classys `success_candidate / aesthetic-device export platform`

```text
symbol = 214150
case_type = success_candidate + insufficient_price_data
archetype = AESTHETIC_DEVICE_EXPORT_PLATFORM
```

### stage date

```text
Stage 1:
2022~2025
- Bain Capital control stake
- HIFU / RF / aesthetic device export platform
- global K-aesthetic procedure demand

Stage 2:
2025 context
- Classys exports devices to over 60 countries
- non-invasive skin-care / aesthetic treatment technologies
- Bain acquired 60.84% stake in 2022 for 670B won

Stage 3:
없음
- installed base, device shipments, consumables, OPM, FCF, overseas distributor quality 필요

Stage 4B:
Bain exit / Samsung acquisition rumor / K-aesthetic premium으로 주가가 먼저 움직이면 watch

Stage 4C:
procedure slowdown, distributor inventory, regulatory issue, consumable attach-rate miss
```

Classys는 R7의 clean aesthetic-device platform 후보지만, 이번 deep search에서는 신뢰할 만한 event-price anchor와 full OHLC를 확보하지 못했다. 공개 프로필 기준 Classys는 비침습 aesthetic treatment 기술에 특화했고, 2025년 기준 60개국 이상으로 수출하며, Bain Capital이 2022년 60.84% 지분을 6,700억 원에 인수했다는 정보가 확인된다. 이건 Stage 2 후보지만, Green은 installed base·consumable attach-rate·overseas OPM·FCF가 있어야 한다. ([위키백과][3])

### 실제 가격경로 검증

```text
price_data_source:
public company profile / secondary summary

stage3_price:
N/A

Bain_stake:
60.84%

Bain_transaction_value:
670B won

export_countries:
60+

business:
non-invasive skin-care and aesthetic treatment technologies

Classys_full_OHLC:
price_data_unavailable_after_deep_search

reason:
- Search confirmed business/export/control-stake anchors.
- Reliable reported event-return or adjusted OHLC path was not available in this pass.
```

### alignment

```text
score_price_alignment = success_candidate_but_insufficient_price_data
rerating_result = aesthetic_device_export_platform_watch
stage_failure_type = business_quality_without_price_validation
```

---

## Case D — Hugel / Letybo `success_candidate / U.S. toxin launch`

```text
symbol = 145020
case_type = success_candidate
archetype = BOTULINUM_TOXIN_US_LAUNCH
```

### stage date

```text
Stage 1:
2024-02
- Letybo FDA approval for glabellar lines
- Korean botulinum toxin enters U.S. aesthetic market

Stage 2:
2025-03
- Letybo begins appearing in U.S. dermatology practices
- pricing estimate $9~12/unit vs Botox $12~18/unit
- expected to be available by end-March 2025
- U.S. neuromodulator market competitive but large

Stage 3:
없음
- provider adoption, repeat injection volume, U.S. distributor execution, ASP, royalty / sales margin 확인 필요

Stage 4B:
FDA approval / cheaper-than-Botox narrative로 stock rerating이 먼저 가면 watch

Stage 4C:
counterfeit/unapproved toxin confusion, price war, provider adoption weak, safety issue
```

Hugel은 FDA approval 자체는 Stage 2다. Allure는 Letybo가 미국에서 glabellar lines 치료용으로 FDA approval을 받았고, Botox·Xeomin·Dysport·Daxxify·Jeuveau와 같은 neuromodulator category에 들어간다고 설명했다. NY Post는 Letybo의 U.S. price가 대략 $9~12/unit으로 Botox의 $12~18/unit보다 낮을 수 있고, 2025년 3월 말까지 더 널리 공급될 것으로 보도했다. 다만 R7 Green은 approval이 아니라 repeat procedure volume과 ASP·margin이 확인될 때다. ([Allure][4])

### 실제 가격경로 검증

```text
price_data_source:
Allure / NY Post U.S. launch and price anchors

stage3_price:
N/A

FDA_approval:
U.S. approval for glabellar lines

U.S._launch_context:
appearing in U.S. dermatologist offices by March 2025

Letybo_estimated_price:
$9~12/unit

Botox_estimated_price:
$12~18/unit

25_unit_Letybo_cost:
$225~300

25_unit_Botox_cost:
$300~450

relative_unit_price_discount_low_case:
1 - 12 / 18
= 33.3%

relative_unit_price_discount_high_case:
1 - 9 / 12
= 25.0%

Hugel_stock_OHLC:
price_data_unavailable_after_deep_search

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = U.S._botulinum_toxin_launch_watch
stage_failure_type = approval_not_green_until_provider_adoption_margin
```

---

## Case E — Medytox / Innotox unauthorized distribution `4C-watch`

```text
symbol = 086900
case_type = 4C-watch
archetype = UNAPPROVED_TOXIN_SAFETY_TRUST_4C
```

### stage date

```text
Stage 1:
2025
- Innotox online / DIY injection trend
- K-toxin brand visibility outside approved channels

Stage 4C-watch:
2025-07 / 2025-08
- experts warn against DIY Innotox self-injection
- Innotox not licensed in UK
- Medytox / Luvantas investigating unauthorized importation
- patient safety, unauthorized distribution, brand trust risk

Stage 4C-watch 강화:
2025-11
- FDA warning letters to companies selling unapproved botulinum toxin products
- Korean-origin toxin products often appear in unapproved/counterfeit discussions
- category trust risk

Stage 3:
없음
- unofficial distribution/safety risk exists, so Green 금지
```

Medytox는 승인된 commercial channel보다 **비공식 유통·DIY injection·환자 안전**이 RedTeam이 되는 case다. Guardian은 Innotox가 UK에서 licensed product가 아니며, online DIY injection trend에 대해 전문가들이 eyelid droop, infection, botulism 같은 위험을 경고했다고 보도했다. Medytox 자회사 Luvantas의 CEO는 unauthorized importation을 인지했고, sources shut-down을 위해 조사 중이라고 밝혔다. People은 FDA가 unapproved botulinum toxin products를 판매한 여러 기업에 warning letters를 보냈다고 보도했다. ([가디언][5])

### 실제 가격경로 검증

```text
price_data_source:
Guardian / People safety-regulatory anchors

stage3_price:
N/A

risk_event:
unauthorized Innotox online / DIY injection trend

UK_license_status:
not licensed for use in the UK per Guardian article

company_response:
Medytox / Luvantas investigating unauthorized importation

FDA_warning_context:
warning letters to sellers of unapproved botulinum toxin products

Medytox_stock_OHLC:
price_data_unavailable_after_deep_search

MFE:
N/A

MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = toxin_safety_distribution_trust_watch
stage_failure_type = 4C_watch_not_hard_4C
```

---

## Case F — Lunit / INSIGHT DBT `insufficient_evidence / validation not revenue`

```text
symbol = 328130
case_type = insufficient_evidence
archetype = MEDICAL_AI_EXTERNAL_VALIDATION_NOT_REVENUE
```

### stage date

```text
Stage 1:
2024~2025
- medical AI / cancer screening AI
- hospital workflow adoption expectation

Stage 2:
2025-03-17
- Lunit INSIGHT DBT external validation
- 163,449 screening mammography exams
- 1,368 screen-detected cancers
- overall AUC 0.91
- precision 0.08, recall 0.73

Stage 4C-watch:
- non-invasive cancers AUC 0.85
- calcification AUC 0.80
- dense breast tissue AUC 0.90
- subgroup performance weakness

Stage 3:
없음
- external validation is not reimbursement / hospital adoption / recurring revenue
```

Lunit은 R7에서 “논문 검증과 상업 Green을 분리해야 하는” 핵심 case다. arXiv 연구는 Lunit INSIGHT DBT를 163,449건의 screening mammography exams에서 평가했고, 전체 AUC 0.91을 기록했다. 그러나 non-invasive cancers, calcification, dense breast tissue subgroup에서는 상대적으로 낮은 성능이 나와, 임상 도입에는 subgroup별 vigilance가 필요하다고 결론냈다. ([arXiv][6])

### 실제 가격경로 검증

```text
price_data_source:
arXiv external-validation evidence

stage3_price:
N/A

exam_count:
163,449

positive_cases:
1,368 screen-detected cancers

negative_exams:
162,081

overall_AUC:
0.91

precision:
0.08

recall:
0.73

non_invasive_cancer_AUC:
0.85

calcification_AUC:
0.80

dense_breast_AUC:
0.90

Lunit_stock_OHLC:
price_data_unavailable_after_deep_search

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = insufficient_evidence
rerating_result = medical_AI_validation_watch
stage_failure_type = validation_not_reimbursement_or_revenue
```

---

## Case G — Medical-school quota / doctors’ strike `medical-service 4C-watch`

```text
symbol = hospital / medtech / elective-procedure basket
case_type = 4C-watch
archetype = MEDICAL_SERVICE_DISRUPTION_POLICY_4C
```

### stage date

```text
Stage 1:
2024-02-20
- trainee doctors walkout
- medical-school quota dispute
- elective procedure / hospital capacity disruption

Stage 4C-watch:
2025-03-07
- 13-month dispute
- government offers to freeze new medical student numbers around 3,000
- 90% of trainee doctors had resigned
- overstretched emergency care / surgery delays

Stage 2 policy-relief:
2026-02-10
- government revives plan to raise medical student quota
- 3,058 → 3,548 in 2027
- 3,871 by 2030

Stage 3:
없음
- policy resolution / quota change is not healthcare-stock Green
- procedure volume, hospital utilization, medtech demand, reimbursement 확인 필요
```

의대정원·의사파업 case는 R7에서 policy upside와 service disruption이 동시에 붙는다. Reuters는 2025년 3월 정부가 13개월 분쟁 해결을 위해 신입 의대생 숫자를 약 3,000명으로 동결하는 방안을 제시했다고 보도했고, 당시 trainee doctors의 90%가 사직했으며 emergency care와 surgery delays가 발생했다고 설명했다. 2026년에는 정원을 3,058명에서 2027년 3,548명, 2030년 3,871명으로 늘리는 계획이 다시 나왔다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / AP medical-crisis policy anchors

stage3_price:
N/A

dispute_duration:
13 months as of 2025-03-07

trainee_doctor_resignation_share:
90%

original_medical_quota:
3,058

2027_quota:
3,548

2030_quota:
3,871

2027_increase:
3,548 / 3,058 - 1
= +16.0%

2030_increase:
3,871 / 3,058 - 1
= +26.6%

listed_healthcare_stock_OHLC:
price_data_unavailable_after_deep_search

MFE / MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = healthcare_service_policy_disruption_watch
stage_failure_type = policy_event_not_procedure_volume_green
```

---

## Case H — Osstem Implant / ZimVie `dental M&A event premium`

```text
direct_company = Osstem Implant, delisted
event_target = ZimVie, U.S.-listed
case_type = event_premium / global dental M&A validation
archetype = DENTAL_IMPLANT_GLOBAL_M_AND_A
```

### stage date

```text
Stage 1:
2023~2024
- Osstem voluntarily delisted from Korea market
- dental implant global expansion
- Korean dental company seeking U.S. asset

Stage 2:
2024-07-18
- reports that Osstem was near final bid for ZimVie
- ZimVie stock +12.5% to $21.31
- ZimVie market cap around $517M prior close
- Osstem direct KRX price tracking unavailable due delisting

Stage 3:
없음
- M&A rumor / target rally is not Korean listed Green
- confirmed close, integration, margin, debt, cash return needed

Stage 4B:
U.S. target stock rally before confirmed transaction close
```

Osstem/ZimVie는 R7 dental 글로벌 M&A validation이지만, 한국 상장주 Green은 아니다. Osstem은 2023년 자진 상장폐지됐고, 2024년 ZimVie 인수 가능성 보도에 ZimVie 주가는 12.5% 오른 $21.31에 마감했다. 한국 상장 price path는 없고, M&A rumor는 Stage 2/event premium일 뿐이다. ([Investors][8])

### 실제 가격경로 검증

```text
price_data_source:
Investors.com / Bloomberg-reported takeover rumor anchor

stage3_price:
N/A

Korean_listed_price:
N/A, Osstem delisted in 2023

ZimVie_event_price:
$21.31

ZimVie_event_MFE:
+12.5%

ZimVie_market_cap_prior:
about $517M

takeover_status:
reported final bid / financing arrangement, not confirmed close in source

MFE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = event_premium
rerating_result = dental_implant_global_M&A_watch
stage_failure_type = delisted_buyer_and_unconfirmed_M&A_not_green
```

---

# 5. 이번 R7 case별 요약표

| case                   | 분류                               |                                                    실제 가격검증 | alignment                      |
| ---------------------- | -------------------------------- | ---------------------------------------------------------: | ------------------------------ |
| Jeisys Medical         | structural_success_candidate     |   12,860원, $742M buyout, revenue CAGR 44%, pretax CAGR 45% | business validated / delisting |
| APR / Medicube device  | structural_success + 4B          |         stock >4x, market value $6B, device 1/3 U.S. sales | aligned_partial / 4B           |
| Classys                | success_candidate / insufficient |                       60+ countries, Bain 60.84%, 670B won | price unavailable              |
| Hugel / Letybo         | success_candidate                |              FDA approval, $9~12/unit vs Botox $12~18/unit | launch Stage 2                 |
| Medytox / Innotox      | 4C-watch                         | unauthorized DIY trend, UK unlicensed, FDA warning context | safety trust watch             |
| Lunit                  | insufficient_evidence            |                 163,449 exams, AUC 0.91, subgroup weakness | validation not revenue         |
| Medical quota / strike | 4C-watch                         |     90% trainee doctors resigned, quota +16.0%/+26.6% plan | policy disruption              |
| Osstem / ZimVie        | event premium                    |                             ZimVie +12.5%, Osstem delisted | M&A event                      |

---

# 6. score-price alignment 판정

```text
structural_success_candidate:
- Jeisys Medical
- APR / Medicube device

success_candidate:
- Classys
- Hugel / Letybo

insufficient_evidence:
- Lunit
- Classys price path
- Osstem Korean listed price path

event_premium:
- Osstem / ZimVie takeover rumor
- APR device valuation if it outruns recurring device revenue
- Jeisys buyout / delisting premium

price_moved_without_evidence:
- dental M&A rumor before confirmed integration
- FDA approval narrative before U.S. procedure volume
- AI validation before reimbursement / recurring revenue

thesis_break_watch:
- Medytox / Innotox unauthorized distribution
- medical-school quota / doctors’ strike disruption
- Lunit subgroup weakness

hard_4C_confirmed:
- false
```

이번 R7 Loop 12에서는 hard 4C를 억지로 확정하지 않는다. 대신 **톡신 안전·비공식 유통**, **의료서비스 disruption**, **AI 진단 subgroup weakness**, **FDA approval without commercial conversion**을 4C-watch로 올린다.

---

# 7. 점수비중 교정

## 올릴 축

```text
procedure_volume +5
device_installed_base +5
consumable_attach_rate +5
repeat_treatment_frequency +5
provider_adoption +5
reimbursement_or_selfpay_conversion +4
gross_margin_visibility +5
regulatory_safety_trust +5
commercial_revenue_conversion +5
cash_conversion +4
```

### 왜 올리나

Jeisys는 매출·pretax earnings 성장과 PE buyout으로 business quality가 검증됐다. APR은 device demand가 실제 해외매출과 market value로 연결됐다. Hugel은 FDA approval과 price advantage가 있지만, provider adoption과 repeat injections가 필요하다. Lunit은 AUC가 있어도 보험·병원도입·반복매출이 없으면 Green이 아니다.

## 내릴 축

```text
approval_headline_only -5
M&A_rumor_only -5
external_validation_without_revenue -5
device_viral_demand_only -4
unlisted_subsidiary_or_delisted_tracking_gap -4
unauthorized_distribution_risk -5
safety_or_counterfeit_toxin_risk -5
medical_service_disruption -4
subgroup_performance_weakness -4
```

### 왜 내리나

FDA approval은 launch option이지 Stage 3가 아니다. Osstem/ZimVie는 target stock event는 있어도 한국 상장 price path가 없다. Medytox/Innotox는 unauthorized distribution이 제품 신뢰를 때릴 수 있다. Doctors’ strike는 병원 capacity와 elective procedure 수요를 교란한다.

## Green gate 강화 조건

```text
R7 Stage 3-Green 필수:
1. procedure volume 또는 prescription volume 확인
2. installed base / utilization 확인
3. consumable 또는 repeat-treatment revenue 확인
4. provider adoption / hospital adoption 확인
5. reimbursement 또는 self-pay ASP 확인
6. gross margin / FCF 확인
7. safety / counterfeit / unauthorized distribution risk 없음
8. policy disruption 없음
9. 가격경로가 evidence 이후 따라옴

금지:
FDA approval only
M&A rumor only
external validation only
unlisted/delisted asset only
device viral story only
비공식 톡신 유통 risk 존재
의사파업 / 의료서비스 capacity disruption 존재
```

## 4B 조기감지 조건

```text
4B-watch:
PE buyout / delisting premium
FDA approval 직후 procedure volume 전 급등
medical device export story로 valuation 먼저 확장
beauty device가 viral demand만으로 3~4배 상승
M&A rumor로 target/basket 급등
AI validation 논문만으로 medical AI stock 급등
의료정책 뉴스로 healthcare basket 급등

4B-elevated:
provider adoption 미확인
소모품 attach-rate 미확인
single device / single toxin concentration
safety distribution issue
subgroup weakness
unlisted/delisted tracking gap
```

## 4C hard gate 조건

```text
FDA rejection / CRL
post-approval safety signal
counterfeit / unauthorized distribution causing regulatory action
provider adoption failure
reimbursement failure
clinical subgroup failure that blocks adoption
M&A cancellation
medical-service disruption causing procedure-volume collapse
cash burn / dilution from commercialization failure
```

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
```

---

# 9. patch-ready 출력

## docs/round/round_191.md 요약

```md
# R7 Loop 12. Biotech / Healthcare / Medical Device Price Validation

이번 라운드는 R7 Loop 12 price-validation 라운드다.

핵심 결론:
- Jeisys Medical is aesthetic EBD business-quality validation. ArchiMed acquisition roughly $742M, Jeisys price anchor 12,860 won, revenue CAGR 44% to $107M and adjusted pretax earnings CAGR 45% to $31M through FY2023. Public-equity tracking closes after delisting.
- APR / Medicube device is beauty-device structural success plus 4B-watch. Stock more than four-fold since January 2025, market value about $6B, device about one-third of U.S. sales, overseas revenue nearly 80% of Q2 revenue.
- Classys is aesthetic-device export platform Stage 2 but price-data insufficient. Exports to 60+ countries, Bain 60.84% stake at 670B won, but installed base, consumables, OPM and FCF required.
- Hugel / Letybo is U.S. toxin launch Stage 2. FDA approval for glabellar lines and estimated $9~12/unit pricing versus Botox $12~18/unit. Provider adoption, repeat injection volume, ASP and margin required.
- Medytox / Innotox is safety-trust 4C-watch. Unauthorized online/DIY injection trend, UK unlicensed status, and FDA warning context for unapproved botulinum toxins create regulatory and brand-trust risk.
- Lunit is medical AI validation, not Green. External validation showed 163,449 exams and AUC 0.91, but subgroup weakness and no reimbursement/hospital adoption/revenue bridge.
- Medical quota / doctors’ strike is healthcare-service 4C-watch. 90% trainee doctors resigned during dispute, and quota-policy changes are not procedure-volume Green.
- Osstem / ZimVie is dental M&A event premium. ZimVie +12.5% to $21.31 on takeover rumor, but Osstem is delisted and the transaction was not confirmed in the source.
```

## docs/checkpoints/checkpoint_28a_round191_r7_loop12.md 요약

```md
# Checkpoint 28A Round 191 R7 Loop 12 Healthcare Medical Device Price Validation

## 반영 내용
- R7 Loop 12 price-validation 라운드를 추가했다.
- Aesthetic EBD buyout, beauty device crossover, aesthetic-device export platform, U.S. toxin launch, unauthorized toxin safety risk, medical AI validation, medical-service disruption, dental implant M&A를 비교했다.
- WSJ / FT / Reuters / Allure / NY Post / Guardian / People / arXiv / IBD anchors로 가능한 MFE/MAE 및 event metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- procedure volume, installed base, consumable attach-rate, repeat-treatment frequency, provider adoption, reimbursement/self-pay conversion, regulatory safety trust, commercial revenue conversion 가중치 강화
- approval headline-only, M&A rumor-only, external validation without revenue, device viral demand-only, unauthorized distribution risk, toxin safety/counterfeit risk, medical-service disruption 감점 강화
```

## data/e2r_case_library/cases_r7_loop12_round191.jsonl 초안

```jsonl
{"case_id":"r7_loop12_jeisys_archimed_aesthetic_ebd_buyout","symbol":"287410_delisting","company_name":"Jeisys Medical","case_type":"structural_success_candidate","primary_archetype":"AESTHETIC_EBD_GLOBAL_BUYOUT","stage2_date":"2024-09-11","stage4b_date":"2024-09-11_delisting_premium","price_validation":{"price_data_source":"WSJ ArchiMed/Jeisys acquisition anchor","entry_date":"2024-09-11","stage3_price":null,"stage2_price_anchor_krw":12860,"deal_value_usd_mn":742,"fy2023_revenue_usd_mn":107,"fy2023_adjusted_pretax_earnings_usd_mn":31,"revenue_cagr_pct":44,"adjusted_pretax_earnings_cagr_pct":45,"deal_value_to_revenue":6.93,"deal_value_to_adjusted_pretax_earnings":23.9,"global_ebd_market_prior_usd_bn":4.5,"global_ebd_market_2032_expected_usd_bn":16,"market_growth_multiple":3.56,"price_validation_status":"reported_price_anchor_then_delisting_tracking_gap"},"score_price_alignment":"structural_success_candidate","rerating_result":"aesthetic_EBD_business_quality_validated","notes":"Business quality validated by PE buyout, but public-equity Stage 3 tracking closes after delisting."}
{"case_id":"r7_loop12_apr_medicube_beauty_device_crossover","symbol":"278470","company_name":"APR / Medicube","case_type":"structural_success_candidate","primary_archetype":"BEAUTY_DEVICE_CONSUMER_CLINIC_CROSSOVER","stage2_date":"2025-10-20","stage4b_date":"2025-10-20_watch","price_validation":{"price_data_source":"FT APR beauty-device anchor","stage3_price":null,"reported_stock_return_since_jan_2025_pct":300,"market_value_usd_bn":6,"device_price_usd":180,"device_share_of_us_sales":"about_one_third","q2_2025_overseas_revenue_share_pct":80,"revenue_growth_since_2018_multiple":7,"price_validation_status":"reported_return_anchor_not_full_ohlc"},"score_price_alignment":"aligned_partial","rerating_result":"beauty_device_structural_rerating_candidate","notes":"Strong device revenue conversion, but R7 Green requires repeat revenue, channel durability and regulatory/aesthetic boundary control."}
{"case_id":"r7_loop12_classys_aesthetic_device_export_platform","symbol":"214150","company_name":"Classys","case_type":"success_candidate","primary_archetype":"AESTHETIC_DEVICE_EXPORT_PLATFORM","stage2_date":"2025_context","price_validation":{"price_data_source":"public company profile / secondary summary","stage3_price":null,"bain_stake_pct":60.84,"bain_transaction_value_krw_bn":670,"export_countries":60,"business":"non-invasive skin-care and aesthetic treatment technologies","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_insufficient_price_data","rerating_result":"aesthetic_device_export_platform_watch","notes":"Business/export evidence exists, but installed base, consumable attach-rate, OPM/FCF and price path required before Green."}
{"case_id":"r7_loop12_hugel_letybo_us_launch","symbol":"145020","company_name":"Hugel / Letybo","case_type":"success_candidate","primary_archetype":"BOTULINUM_TOXIN_US_LAUNCH","stage1_date":"2024-02","stage2_date":"2025-03","price_validation":{"price_data_source":"Allure / NY Post U.S. launch and price anchors","stage3_price":null,"fda_approval":"glabellar_lines","letybo_estimated_unit_price_usd":"9-12","botox_estimated_unit_price_usd":"12-18","letybo_25_unit_cost_usd":"225-300","botox_25_unit_cost_usd":"300-450","relative_unit_discount_low_case_pct":33.3,"relative_unit_discount_high_case_pct":25.0,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"U.S._botulinum_toxin_launch_watch","notes":"FDA approval and price advantage are Stage 2; provider adoption, repeat procedure volume, ASP and margin required before Green."}
{"case_id":"r7_loop12_medytox_innotox_unauthorized_distribution_watch","symbol":"086900","company_name":"Medytox / Innotox","case_type":"4c_watch","primary_archetype":"UNAPPROVED_TOXIN_SAFETY_TRUST_4C","stage4c_date":"2025-07/2025-08/2025-11_watch","price_validation":{"price_data_source":"Guardian / People safety-regulatory anchors","stage3_price":null,"risk_event":"unauthorized Innotox online / DIY injection trend","uk_license_status":"not licensed for use in UK per Guardian article","company_response":"Medytox/Luvantas investigating unauthorized importation","fda_warning_context":"warning letters to sellers of unapproved botulinum toxin products","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"toxin_safety_distribution_trust_watch","notes":"Unauthorized distribution and DIY injection create safety, regulatory and brand-trust 4C-watch."}
{"case_id":"r7_loop12_lunit_insight_dbt_external_validation","symbol":"328130","company_name":"Lunit","case_type":"insufficient_evidence","primary_archetype":"MEDICAL_AI_EXTERNAL_VALIDATION_NOT_REVENUE","stage2_date":"2025-03-17","stage4c_date":"subgroup_performance_watch","price_validation":{"price_data_source":"arXiv external-validation evidence","stage3_price":null,"exam_count":163449,"positive_cases":1368,"negative_exams":162081,"overall_auc":0.91,"precision":0.08,"recall":0.73,"non_invasive_cancer_auc":0.85,"calcification_auc":0.80,"dense_breast_auc":0.90,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"insufficient_evidence","rerating_result":"medical_AI_validation_watch","notes":"External validation is Stage 2; reimbursement, hospital adoption, recurring revenue and subgroup robustness required before Green."}
{"case_id":"r7_loop12_medical_quota_doctors_strike_service_disruption","symbol":"hospital_medtech_elective_procedure_basket","company_name":"Medical quota / doctors’ strike service-disruption basket","case_type":"4c_watch","primary_archetype":"MEDICAL_SERVICE_DISRUPTION_POLICY_4C","stage1_date":"2024-02-20","stage4c_date":"2025-03-07_watch","stage2_date":"2026-02-10_policy_relief","price_validation":{"price_data_source":"Reuters / AP medical-crisis policy anchors","stage3_price":null,"dispute_duration_months":13,"trainee_doctor_resignation_share_pct":90,"original_medical_quota":3058,"quota_2027":3548,"quota_2030":3871,"quota_2027_increase_pct":16.0,"quota_2030_increase_pct":26.6,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"healthcare_service_policy_disruption_watch","notes":"Quota policy can create attention, but procedure volume, hospital utilization and reimbursement must confirm before Green."}
{"case_id":"r7_loop12_osstem_zimvie_dental_mna_event","symbol":"Osstem_delisted/ZIMV_target","company_name":"Osstem Implant / ZimVie","case_type":"event_premium","primary_archetype":"DENTAL_IMPLANT_GLOBAL_M_AND_A","stage2_date":"2024-07-18","stage4b_date":"2024-07-18","price_validation":{"price_data_source":"Investors.com / Bloomberg-reported takeover rumor anchor","stage3_price":null,"korean_listed_price":"N/A_Osstem_delisted_2023","zimvie_event_price_usd":21.31,"zimvie_event_mfe_pct":12.5,"zimvie_market_cap_prior_usd_mn":517,"takeover_status":"reported final bid / financing arrangement, not confirmed close in source","price_validation_status":"Korean_buyer_delisted_target_event_only"},"score_price_alignment":"event_premium","rerating_result":"dental_implant_global_M&A_watch","notes":"Dental M&A validates strategic intent, but delisted buyer and unconfirmed transaction are not Korean listed-stock Green."}
```

## data/sector_taxonomy/score_weight_profiles_round191_r7_loop12_v1.csv 초안

```csv
archetype,procedure_volume,installed_base,consumable_attach_rate,repeat_treatment,provider_adoption,reimbursement_selfpay,gross_margin,regulatory_safety_trust,commercial_revenue,cash_conversion,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
AESTHETIC_EBD_GLOBAL_BUYOUT,+5,+5,+5,+4,+5,+4,+5,+4,+5,+4,-3,+4,+3,Jeisys buyout validates business quality, but delisting closes public Stage 3 tracking.
BEAUTY_DEVICE_CONSUMER_CLINIC_CROSSOVER,+4,+4,+4,+5,+3,+4,+5,+3,+5,+4,-4,+5,+3,APR device revenue is strong but concentration and channel durability require 4B-watch.
AESTHETIC_DEVICE_EXPORT_PLATFORM,+5,+5,+5,+4,+5,+4,+5,+4,+5,+4,-3,+4,+3,Classys export platform requires installed base, consumables, OPM/FCF and price path before Green.
BOTULINUM_TOXIN_US_LAUNCH,+5,+2,+3,+5,+5,+5,+5,+5,+5,+4,-5,+5,+5,Hugel approval/launch is Stage 2 until provider adoption and repeat injection revenue confirm.
UNAPPROVED_TOXIN_SAFETY_TRUST_4C,+0,+0,+0,+0,+0,+0,+0,+5,+0,+0,0,+3,+5,Medytox/Innotox unauthorized distribution creates safety/regulatory trust watch.
MEDICAL_AI_EXTERNAL_VALIDATION_NOT_REVENUE,+2,+0,+0,+0,+5,+5,+4,+5,+5,+4,-5,+4,+4,Lunit external validation needs reimbursement, adoption, recurring revenue and subgroup robustness.
MEDICAL_SERVICE_DISRUPTION_POLICY_4C,+0,+0,+0,+0,+3,+3,+2,+4,+2,+2,-4,+3,+4,Doctors’ strike and quota dispute can disrupt procedure volume and medtech utilization.
DENTAL_IMPLANT_GLOBAL_M_AND_A,+3,+3,+3,+4,+3,+4,+5,+3,+4,+4,-5,+5,+3,Osstem/ZimVie rumor is M&A validation but not Korean listed Green.
```

---

# 이번 R7 Loop 12 결론

```text
1. Jeisys는 미용의료기기 business quality가 PE buyout으로 검증된 case다.
   다만 delisting으로 public Stage 3 price tracking은 닫힌다.

2. APR/Medicube는 beauty-device structural success 후보지만,
   R7 관점에서는 device concentration과 regulatory/clinic boundary 때문에 4B-watch가 붙는다.

3. Classys는 aesthetic-device export platform Stage 2다.
   installed base, consumables, OPM/FCF, price path 전에는 Green 금지다.

4. Hugel/Letybo는 U.S. toxin launch Stage 2다.
   FDA approval과 가격 advantage는 좋지만, provider adoption과 반복 시술량 전에는 Stage 3가 아니다.

5. Medytox/Innotox는 toxin safety/distribution 4C-watch다.
   비공식 유통과 DIY injection은 brand trust와 regulatory risk를 동시에 건드린다.

6. Lunit은 medical AI validation Stage 2다.
   AUC 0.91이어도 reimbursement, hospital adoption, recurring revenue 전에는 Green이 아니다.

7. 의사파업/의대정원은 healthcare service disruption 4C-watch다.
   정책 숫자보다 procedure volume, hospital utilization, medtech demand가 Stage 3 조건이다.

8. Osstem/ZimVie는 dental M&A event premium이다.
   한국 buyer가 delisted이고 deal close가 확인되지 않았으므로 Korean listed-stock Green은 아니다.
```

한 문장으로 압축하면:

> **R7에서 진짜 Stage 3는 “FDA 승인·AI 검증·M&A·K-aesthetic story가 있다”가 아니라, 시술량·처방량·설치대수·소모품 반복매출·provider adoption·수가/ASP·gross margin·안전/규제 신뢰가 실제로 닫히는 순간이다.**

[1]: https://www.wsj.com/articles/europes-archimed-bets-on-anti-aging-trend-in-first-asia-deal-cbe16f5e?utm_source=chatgpt.com "Europe's ArchiMed Bets on Anti-Aging Trend in First Asia Deal"
[2]: https://www.ft.com/content/6a0f7e2c-f3b9-4eb6-961c-d69af28f7183?utm_source=chatgpt.com "Kardashian endorsement of skincare gadget creates K-beauty champion"
[3]: https://en.wikipedia.org/wiki/Classys?utm_source=chatgpt.com "Classys"
[4]: https://www.allure.com/story/letybo-neuromodulator-injectable?utm_source=chatgpt.com "Everything You Need to Know About Letybo, the Newest Botox Competitor"
[5]: https://www.theguardian.com/lifeandstyle/2025/aug/10/diy-botox-like-injection-innotox-available-illegally-online-warning?utm_source=chatgpt.com "Experts warn against DIY Botox-like injections available illegally online"
[6]: https://arxiv.org/abs/2503.13581?utm_source=chatgpt.com "Subgroup Performance of a Commercial Digital Breast Tomosynthesis Model for Breast Cancer Detection"
[7]: https://www.reuters.com/world/asia-pacific/south-korea-prepared-freeze-new-medical-student-numbers-minister-says-2025-03-07/?utm_source=chatgpt.com "South Korea offers to freeze medical student numbers to resolve 13-month dispute"
[8]: https://www.investors.com/news/technology/zimvie-stock-breakout-osstem-implant-deal/?utm_source=chatgpt.com "ZimVie Stock Launches 13% Into Breakout Territory On Rumored Takeover"
