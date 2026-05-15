좋아. **Round 25: 얇은 archetype 추가 보강 + 주요 archetype 점수비중 v1.6 교정**으로 계속 채울게.

이번 라운드는 특히 그동안 상대적으로 얇았던 축을 더 파고든다.

```text
1. DATA_CENTER_REIT_INFRASTRUCTURE
2. WASTE_RECYCLING_ENVIRONMENT
3. MEDICAL_DEVICE_DENTAL_IMPLANT
4. CONSUMER_REGULATED_PRODUCT
5. APPAREL_FAST_FASHION_BRAND_OEM
6. DIGITAL_ASSET_TOKENIZATION 재보정
7. AI_DATA_CENTER_INFRASTRUCTURE 재보정
8. VALUE_UP_SHAREHOLDER_RETURN 재보정
```

기본 원칙은 그대로다.
테마명은 점수 근거가 아니다. 점수는 **산업 구조 변화 → EPS/FCF 체급 변화 → 시장의 과거 프레임 오해 → 밸류에이션 리레이팅**에서 나와야 한다.
계약금액, 계약기간, 매출 대비 계약금액, OP YoY 같은 값도 실제 상세공시·리포트에서 확인된 것만 써야 하고, 비어 있는 값을 추정해서 채우면 안 된다.

---

# 1. DATA_CENTER_REIT_INFRASTRUCTURE

## 데이터센터 REIT / IDC / AI 인프라 부동산

### 핵심 구조

```text
AI CAPEX 증가
→ 데이터센터 임대수요 증가
→ hyperscale tenant 장기계약
→ 전력·냉각·토지 확보
→ FFO/AFFO 성장
```

### 성공사례 후보

Blackstone Digital Infrastructure Trust는 이 archetype의 기준 케이스로 좋다. Reuters에 따르면 Blackstone의 데이터센터 REIT는 17.5억 달러 IPO를 통해 대형 hyperscale tenant용 데이터센터 자산에 투자하려 하고, Blackstone은 이미 QTS 등 디지털 인프라 포트폴리오를 크게 보유하고 있다. 이건 AI 인프라가 “GPU만”이 아니라 **부동산·전력·냉각·장기 임대계약**으로 확장된다는 증거다. ([Reuters][1])

Equinix의 말레이시아 데이터센터 투자도 좋은 후보야. Equinix는 쿠알라룸푸르에 1.9억 달러 이상을 투자해 2,200개 이상 cabinet을 수용할 새 데이터센터를 만들고, AI·고성능 컴퓨팅 수요를 위해 액체냉각 기술을 포함한다고 밝혔다. 다만 Reuters는 말레이시아 데이터센터 붐이 전력·수자원 문제와 지정학적 압력 때문에 둔화될 수 있다고도 언급했다. 즉 성공 후보이면서 동시에 **전력·수자원·정책 제약 반례**를 같이 준다. ([Reuters][2])

### 반례

```text
- AI 데이터센터 테마만 있고 실제 자산·임차인 없음
- hyperscale tenant concentration이 과도함
- 전력·수자원·인허가 병목
- CAPEX는 커지는데 FFO/AFFO 개선 없음
- 금리·funding cost 상승
```

### 점수비중 v1.6

```text
EPS/FCF: 18
Structural Visibility: 23
Bottleneck/Pricing: 18
Market Mispricing: 13
Valuation Rerating: 13
Capital Allocation: 5
Information Confidence: 5
Risk Penalty: capex_burden / power_water_constraint / tenant_concentration / funding_cost
```

### 정규화 교정

데이터센터 REIT는 **Green 가능 archetype**이지만, 일반 AI 테마와 다르게 봐야 한다.

```text
점수 강화:
- hyperscale tenant 장기 임대계약
- 높은 occupancy
- 전력·냉각·토지 확보
- FFO/AFFO 성장
- funding cost 통제

점수 제한:
- AI 데이터센터 테마만 있음
- 자산 없음
- tenant concentration 과도
- CAPEX만 늘고 FFO 개선 없음
```

---

# 2. WASTE_RECYCLING_ENVIRONMENT

## 폐기물처리 / 재활용 / 폐배터리 / 탈플라스틱

### 핵심 구조

```text
규제 강화 / 처리 수요 증가
→ 허가권·처리시설·장기계약
→ 반복 처리량
→ 반복 FCF
```

### 성공사례 후보

EQT의 한국 KJ Environment 인수는 폐기물 archetype의 좋은 성공 후보야. Reuters는 EQT가 KJ Environment와 계열사를 인수해 한국 폐기물 처리 플랫폼을 만들기로 했고, 이 플랫폼이 플라스틱 재활용·폐기물 에너지화·재활용 폐기물 선별을 포함하며 한국 인구 절반 이상을 커버할 수 있다고 보도했다. 즉 폐기물처리는 단순 ESG 테마가 아니라 **허가권·처리시설·반복 FCF형 인프라**가 될 수 있다. ([Reuters][3])

### 반례

```text
- 폐배터리 테마만 있고 실제 회수량 없음
- 재활용 설비는 있으나 가동률 낮음
- 금속가격 하락으로 회수 마진 훼손
- CAPEX 부담으로 FCF 악화
- 규제 기대만 있고 실제 처리량 없음
```

### 점수비중 v1.6

```text
EPS/FCF: 18
Structural Visibility: 22
Bottleneck/Pricing: 15
Market Mispricing: 13
Valuation Rerating: 12
Capital Allocation: 3
Information Confidence: 5
Risk Penalty: utilization / commodity_price / capex / regulation_delay
```

### 정규화 교정

폐기물처리는 **Green 가능**으로 봐도 된다.
반면 폐배터리·재활용 테마는 실제 처리량과 FCF가 나오기 전까지 Watch다.

```text
점수 강화:
- 허가권
- 처리시설 가동률
- 장기 처리계약
- 반복 FCF
- 고객사 다변화

점수 제한:
- 재활용/폐배터리 테마만 있음
- 가동률 낮음
- 금속가격 하락
- CAPEX 부담
```

---

# 3. MEDICAL_DEVICE_DENTAL_IMPLANT

## 치아·임플란트 / 미용의료 / 의료기기 수출

### 핵심 구조

```text
의료기기 제품 판매
→ 반복 시술·소모품
→ 해외 허가·채널 확대
→ OPM/FCF 개선
```

### 성공사례 후보

치아·임플란트는 의료기기 중에서도 반복수요와 해외 확장이 확인되면 Green 가능성이 있다. Straumann은 2025년 매출이 예상을 넘었고 2026년에도 성장 가이던스를 제시했지만, 중국의 volume-based procurement, 즉 VBP 제도 불확실성이 계속 리스크로 남아 있다고 Reuters가 보도했다. 이건 치아·임플란트 archetype에서 **해외 성장 + 규제/가격통제 리스크**를 동시에 봐야 한다는 좋은 기준 케이스다. ([Reuters][4])

### 반례

```text
- 중국 VBP 같은 가격통제
- 허가 지연
- ASP 하락
- 경쟁 심화
- 단일 장비 판매 후 반복 소모품 없음
- 위조·안전성 이슈
```

### 점수비중 v1.6

```text
EPS/FCF: 20
Structural Visibility: 22
Bottleneck/Pricing: 13
Market Mispricing: 14
Valuation Rerating: 12
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: approval / VBP_price_control / safety / competition / channel_quality
```

### 정규화 교정

의료기기 수출은 **Green 가능 archetype**이다.
다만 가격통제·허가·경쟁 리스크를 강하게 봐야 한다.

```text
점수 강화:
- 수출국 확대
- 반복 시술·소모품 매출
- 허가 안정
- OPM/ROE 개선
- 채널 품질

점수 제한:
- 중국 VBP/가격통제
- 허가 지연
- ASP 하락
- 반복매출 없음
```

---

# 4. CONSUMER_REGULATED_PRODUCT

## 전자담배 / 주정 / 마리화나 / 규제형 소비재

### 핵심 구조

```text
반복소비
→ 브랜드·유통망
→ 규제 승인 또는 안정
→ 단, 규제 리스크가 항상 큼
```

### 성공사례 후보

전자담배는 반복소비와 브랜드·디바이스 ecosystem이 있으면 후보가 될 수 있다. Juul의 경우 FDA가 2025년에 tobacco·menthol e-cigarette 제품 판매를 승인했다는 Reuters 보도가 있었는데, 이것은 규제 승인 하나가 기업가치와 시장 접근성을 바꿀 수 있음을 보여준다. ([Reuters][5])

하지만 같은 사례가 반례도 된다. Juul은 2022년 FDA의 판매 금지 명령을 겪었고 이후 항소와 심사를 거쳐 2025년에 일부 제품 승인을 받은 것이므로, 전자담배 archetype에서는 **규제 승인/불허가 Stage 2↔4C를 결정하는 핵심 변수**다. ([Reuters][5])

### 반례

```text
- 규제 강화
- 판매 금지
- 청소년 사용 논란
- 건강·안전성 리스크
- 사회적 반발
- 허가 기대만 있고 실제 승인 없음
```

### 점수비중 v1.6

```text
EPS/FCF: 18
Structural Visibility: 14
Bottleneck/Pricing: 8
Market Mispricing: 12
Valuation Rerating: 10
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: regulation / public_health / legal / social_backlash
```

### 정규화 교정

규제형 소비재는 **Watch 중심**이다.

```text
점수 강화:
- 반복소비
- 규제 승인
- 유통망
- 브랜드 lock-in
- 안정적 FCF

점수 제한:
- 허가 불확실
- 규제 강화
- 건강·안전 이슈
- 사회적 반발
```

---

# 5. APPAREL_FAST_FASHION_BRAND_OEM

## 의류 브랜드 / 의류 OEM·ODM / K패션 / 초저가 패션 경쟁

### 핵심 구조

```text
브랜드·채널 확장
→ 재고 회전
→ 할인율 통제
→ OPM/FCF 개선
```

### 성공·반례 동시 사례: Shein / Temu

Shein·Temu의 법적 분쟁은 의류·초저가 패션 archetype의 중요한 반례 자료다. Reuters는 Shein이 영국 법정에서 Temu를 “industrial scale” 저작권 침해로 고소했고, Temu는 Shein이 경쟁을 억누르려 한다고 맞소송을 제기했다고 보도했다. 이건 fast fashion이 단순 성장시장이 아니라 **저작권, 공급망, 가격경쟁, 플랫폼 독점, 규제 리스크**가 큰 시장이라는 증거다. ([Reuters][6])

### 성공 후보

```text
- 글로벌 채널 확장 K패션 브랜드
- 재고 회전 빠른 브랜드
- 고객사 다변화된 의류 OEM·ODM
- 할인율 낮고 OPM 개선되는 브랜드
```

### 반례

```text
- 단일 유행 브랜드
- 재고 증가
- 할인 판매 증가
- 초저가 플랫폼과 가격경쟁
- 저작권·공급망·규제 리스크
- OEM 고객사 주문 둔화
```

### 점수비중 v1.6

```text
EPS/FCF: 18
Structural Visibility: 16
Bottleneck/Pricing: 8
Market Mispricing: 14
Valuation Rerating: 12
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: inventory / markdown / fashion_cycle / channel_concentration / IP_legal_risk
```

### 정규화 교정

의류는 K뷰티/K푸드보다 Green을 더 보수적으로 둔다.

```text
점수 강화:
- 해외 채널 확장
- 재고 회전 안정
- 낮은 할인율
- OPM 개선
- 고객사 다변화

점수 제한:
- 유행성 매출
- 재고 증가
- 할인율 상승
- IP/저작권 리스크
- 초저가 플랫폼 경쟁
```

---

# 6. DIGITAL_ASSET_TOKENIZATION 재보정

## 스테이블코인 / STO / NFT / 블록체인

### 핵심 구조

```text
규제 승인
→ 실제 발행·거래량·결제망 채택
→ 수수료·예치금·스프레드 수익
→ 반복 금융 인프라 매출
```

### 점수비중 v1.6

```text
EPS/FCF: 16
Structural Visibility: 18
Bottleneck/Pricing: 8
Market Mispricing: 16
Valuation Rerating: 12
Capital Allocation: 3
Information Confidence: 5
Risk Penalty: regulation / security / adoption / liquidity / no_revenue
```

### 교정

```text
스테이블코인/STO:
Watch 가능. 규제 승인과 실제 거래량이 핵심.

NFT/메타버스:
대부분 Red/Watch. 반복매출 없으면 Green 금지.

코인 관련주:
실질 매출·지분·수수료 모델 없으면 theme_overheat.
```

즉 같은 디지털자산이라도:

```text
스테이블코인 결제 인프라
≠ NFT 테마
```

둘을 같은 점수체계로 보면 안 된다.

---

# 7. AI_DATA_CENTER_INFRASTRUCTURE 재보정

### 성공사례 후보

Blackstone 데이터센터 REIT와 Equinix의 AI 대응 데이터센터 투자는 AI 인프라가 GPU·메모리만이 아니라 **부동산·전력·냉각·장기 임대계약·전력망**으로 확장되고 있음을 보여준다. ([Reuters][1])

### 점수비중 v1.6

```text
EPS/FCF: 22
Structural Visibility: 23
Bottleneck/Pricing: 20
Market Mispricing: 14
Valuation Rerating: 12
Capital Allocation: 2
Information Confidence: 5
Risk Penalty: AI_capex_cut / project_delay / grid_constraint / overbuild / water_power_constraint
```

### 교정

AI 데이터센터 인프라는 Green 가능성이 높지만, 너무 넓은 테마라 하위축을 분리해야 한다.

```text
Green 가능:
- 전력설비/변압기/전선
- 냉각/HVAC/액침냉각
- AI 서버 PCB
- 데이터센터 REIT with hyperscale lease
- 장기 전력 PPA

Watch:
- 스마트그리드 PoC
- 일반 HVAC
- IDC 관련주지만 실제 tenant 불명확
- 데이터센터 부동산 테마

Red:
- AI CAPEX 테마만 있음
- 매출 exposure 불명확
- project delay
- overbuild
```

---

# 8. VALUE_UP_SHAREHOLDER_RETURN 재보정

### 핵심 구조

```text
저PBR·NAV discount
→ 자사주·소각·배당
→ ROE 개선
→ 시장 프레임 변화
```

### 점수비중 v1.6

```text
EPS/FCF: 12
Structural Visibility: 18
Bottleneck/Pricing: 4
Market Mispricing: 20
Valuation Rerating: 25
Capital Allocation: 10
Information Confidence: 5
Risk Penalty: governance / execution / low_ROE / no_cancellation / credit_cost
```

### 교정

```text
점수 강화:
- 실제 자사주 소각
- 반복 배당정책
- ROE 유지/개선
- NAV discount 축소
- 지배구조 개선

점수 제한:
- 밸류업 지수 편입만 있음
- 저PBR만 있음
- 자사주 매입 후 미소각
- ROE 낮음
- 지배주주 리스크
```

밸류업은 **정책 테마가 아니라 실행 테마**다.

---

# Round 25 점수비중 요약표

| Archetype                  | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | 핵심 리스크         |
| -------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | -------------- |
| DATA_CENTER_REIT_INFRA     |      18 |         23 |         18 |         13 |        13 |       5 | 전력·수자원·funding |
| WASTE_RECYCLING_ENV        |      18 |         22 |         15 |         13 |        12 |       3 | 가동률·CAPEX      |
| MEDICAL_DEVICE_DENTAL      |      20 |         22 |         13 |         14 |        12 |       0 | 가격통제·허가        |
| CONSUMER_REGULATED         |      18 |         14 |          8 |         12 |        10 |       0 | 규제·사회적 반발      |
| APPAREL_FAST_FASHION       |      18 |         16 |          8 |         14 |        12 |       0 | 재고·저작권·경쟁      |
| DIGITAL_ASSET_TOKENIZATION |      16 |         18 |          8 |         16 |        12 |       3 | 규제·거래량         |
| AI_DATA_CENTER_INFRA       |      22 |         23 |         20 |         14 |        12 |       2 | CAPEX cut·전력망  |
| VALUE_UP_SHAREHOLDER       |      12 |         18 |          4 |         20 |        25 |      10 | 실행·거버넌스        |

---

# cases_v13 추가 후보

```text
DATA_CENTER_REIT_INFRASTRUCTURE:
- blackstone_digital_infra_reit_candidate
- equinix_malaysia_ai_liquid_cooling_candidate
- data_center_reit_power_water_constraint_4c
- data_center_reit_capex_affo_pressure_counterexample

WASTE_RECYCLING_ENVIRONMENT:
- eqt_kj_environment_waste_platform_candidate
- waste_permit_recurring_fcf_candidate
- battery_recycling_no_volume_counterexample
- recycling_capex_low_utilization_4c

MEDICAL_DEVICE_DENTAL_IMPLANT:
- straumann_dental_implant_growth_candidate
- dental_implant_vbp_price_control_counterexample
- medical_device_approval_delay_4c
- single_device_no_consumable_counterexample

CONSUMER_REGULATED_PRODUCT:
- juul_fda_approval_stage2_candidate
- juul_prior_fda_ban_4c
- e_cigarette_youth_regulation_risk
- cannabis_policy_event_only_counterexample

APPAREL_FAST_FASHION_BRAND_OEM:
- shein_fast_fashion_scale_candidate
- shein_temu_ip_litigation_risk_4c
- apparel_inventory_markdown_counterexample
- kfashion_channel_expansion_candidate

DIGITAL_ASSET_TOKENIZATION:
- stablecoin_payment_infra_candidate
- sto_regulation_no_revenue_counterexample
- nft_theme_overheat_counterexample
- crypto_related_stock_no_revenue_counterexample

AI_DATA_CENTER_INFRASTRUCTURE:
- blackstone_ai_datacenter_reit_candidate
- equinix_ai_datacenter_liquid_cooling_candidate
- ai_datacenter_power_water_constraint_4c
- ai_capex_overbuild_counterexample

VALUE_UP_SHAREHOLDER_RETURN:
- buyback_cancellation_success_candidate
- low_pbr_low_roe_value_trap
- buyback_no_cancel_counterexample
- governance_discount_persistent_counterexample
```

---

# 이번 라운드 핵심 교정

```text
1. 데이터센터 REIT는 AI 인프라 수혜지만 FFO/AFFO, tenant, funding cost가 핵심이다.
2. 폐기물처리는 허가권·처리시설·반복 FCF가 있으면 Green 가능하다.
3. 치아·임플란트/의료기기는 수출·반복시술·소모품이 있으면 Green 가능하지만, VBP/가격통제 리스크를 크게 봐야 한다.
4. 전자담배·규제형 소비재는 반복소비가 있어도 규제 승인/불허가가 Stage를 크게 좌우한다.
5. 의류·패션은 재고·할인율·저작권·초저가 경쟁 때문에 K뷰티/K푸드보다 Green을 보수적으로 줘야 한다.
6. 디지털자산은 stablecoin/STO와 NFT/theme을 분리해야 한다.
7. AI 데이터센터 인프라는 전력·냉각·부동산·PPA·PCB로 세분화해야 한다.
8. 밸류업은 지수 편입이 아니라 실제 소각·배당·ROE 개선이 핵심이다.
```

---

# 현재 판단

이제 “얇았던 archetype”도 상당히 많이 두꺼워지고 있다.
특히 이번 라운드로 아래 축이 더 안정됐다.

```text
- 데이터센터 REIT / IDC
- 폐기물처리 / 재활용
- 치아·임플란트 / 의료기기
- 규제형 소비재
- 의류 / fast fashion
- 디지털자산 / stablecoin / STO
- AI 데이터센터 인프라
- 밸류업 / 주주환원
```

하지만 아직 마지막 검증은 변하지 않는다.

```text
성공/반례 case 추가
→ stage date 후보 설정
→ price path backfill
→ MFE/MAE/drawdown 계산
→ score-price alignment
→ shadow scoring
→ 틀린 archetype 점수 재교정
```

지금은 **점수비중 가설 v1.6**까지 온 상태로 보면 된다.

[1]: https://www.reuters.com/legal/transactional/blackstone-data-center-reit-raises-175-billion-us-ipo-2026-05-13/?utm_source=chatgpt.com "Blackstone data center REIT raises $1.75 billion in US IPO"
[2]: https://www.reuters.com/world/asia-pacific/equinix-create-new-malaysia-data-centre-with-over-190-million-investment-2026-05-12/?utm_source=chatgpt.com "Equinix to create new Malaysia data centre with over $190 million investment"
[3]: https://www.reuters.com/markets/deals/eqt-strikes-deal-acquire-south-korean-waste-treatment-platform-2024-08-16/?utm_source=chatgpt.com "EQT strikes deal to acquire South Korean waste treatment platform"
[4]: https://www.reuters.com/business/healthcare-pharmaceuticals/straumann-beats-earnings-expectations-2026-02-18/?utm_source=chatgpt.com "Straumann forecasts 2026 growth despite China procurement uncertainty, shares rise"
[5]: https://www.reuters.com/sustainability/boards-policy-regulation/fda-approves-juuls-tobacco-menthol-e-cigarettes-2025-07-17/?utm_source=chatgpt.com "FDA approves Juul's tobacco and menthol e-cigarettes"
[6]: https://www.reuters.com/legal/litigation/shein-accuses-temu-industrial-scale-copyright-breaches-uk-legal-battle-2026-05-11/?utm_source=chatgpt.com "Shein accuses Temu of 'industrial scale' copyright breaches in UK legal battle"
