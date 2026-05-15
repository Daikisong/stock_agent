맞아. **A를 진행하면서 내가 archetype별 점수비중을 계속 말해주고, 성공/반례/주가검증을 보면서 계속 교정하는 방식이 맞다.**

지금 우리가 하는 건:

```text
A. cases_v04 / v05 계속 확장
→ 성공사례·반례 딥서치
→ 각 archetype의 must-have evidence / red-flag evidence 정리
→ 점수비중 가설 부여
→ 나중에 에이전트가 price path / MFE / MAE로 검증
→ shadow scoring
→ 그 후 production scoring 반영 여부 판단
```

아직 production scoring은 건드리면 안 된다. 서생원식 핵심은 여전히 **산업 구조 변화 → EPS/FCF 체급 변화 → 시장의 과거 프레임 오해 → 밸류에이션 리레이팅**이고, 테마명 자체가 점수가 되면 안 된다.
또 계약금액, 계약기간, 매출 대비 계약금액, OP YoY 같은 필드는 실제 공시/리포트에서 확인된 것만 써야 하고, 비어 있는 값은 절대 만들어내면 안 된다.

---

# Round 15: cases_v04 확장 + 점수비중 보정

이번 라운드는 아직 얇았던 archetype을 중심으로 채운다.

```text
1. RAIL_INFRASTRUCTURE
2. AI_DATA_CENTER_COOLING
3. WASTE_RECYCLING_ENVIRONMENT
4. CLOUD_AI_SOFTWARE_INFRA
5. SECURITY_IDENTITY_DEEPFAKE
6. CRO_CLINICAL_SERVICE
7. APPAREL_BRAND_OEM
8. BUILDING_MATERIALS_CYCLE / REIT
9. CDMO_HEALTHCARE_CONTRACT
10. RARE_METALS_STRATEGIC_MATERIALS
```

---

# 1. RAIL_INFRASTRUCTURE

철도 / 고속철 / 대형 인프라 수주

## 핵심 구조

```text
국가 인프라 예산·해외 발주
→ 대형 계약
→ 납품 스케줄
→ 매출·OP 인식
→ 수주잔고 기반 visibility
```

## 성공사례 후보

**현대로템 철도 수출**은 좋은 케이스야. 현대 로템은 모로코 국영철도 ONCF로부터 약 2.2조원, 15.4억 달러 규모의 2층 전동차 수주를 확보했고, Reuters는 이 계약이 현대로템 철도사업 사상 최대 수주라고 보도했어. 이건 단순 철도 테마가 아니라 **실제 계약 + 대형 수주 + 납품 visibility**가 있는 Stage 1→2 사례로 볼 수 있어. ([Reuters][1])

## 반례

```text
- 철도 정책 기대만 있는 종목
- 우크라 재건 / 네옴시티 / 철도 테마만 붙은 종목
- 실제 계약 없이 MOU만 있는 기업
- 수주는 있으나 마진·납기·원가가 불명확한 기업
```

## 점수비중 v0.6

```text
EPS/FCF: 20
Structural Visibility: 23
Bottleneck/Pricing: 12
Market Mispricing: 14
Valuation Rerating: 12
Capital Allocation: 1
Information Confidence: 5
Risk Penalty: project_delay / margin_uncertainty
```

## Green 조건

```text
계약금액/매출 비중
납품 스케줄
마진 확인
FY1/FY2 OP 상향
실제 수주잔고 반영
```

**정규화 포인트:**
철도는 `CONTRACT_BACKLOG_INDUSTRIAL`과 비슷하지만, 방산·전력기기보다 **프로젝트 마진과 납기 리스크**를 더 크게 봐야 한다.

---

# 2. AI_DATA_CENTER_COOLING

AI 데이터센터 냉각 / HVAC / 액침냉각

## 핵심 구조

```text
AI 서버 고밀도화
→ 발열·전력 밀도 상승
→ 액체냉각 / HVAC / 전력·냉각 병목
→ 데이터센터 CAPEX와 동행
→ 수주·납품·서비스 매출
```

## 성공사례 후보

Ecolab은 AI 데이터센터 냉각 수요를 잡기 위해 CoolIT Systems를 약 47.5억 달러에 인수하기로 했고, Reuters는 AI 인프라 투자 증가로 기존 공랭에서 더 고밀도 전력부하를 처리할 수 있는 액체냉각으로 이동하고 있다고 설명했어. 이건 `AI_DATA_CENTER_COOLING`을 독립 sub-archetype으로 둘 근거야. ([Reuters][2])

삼성전자도 독일 HVAC 기업 FlaktGroup을 15억 유로에 인수해 AI 데이터센터 냉각 수요 대응을 강화하려 했다. 이 역시 냉각이 단순 설비가 아니라 AI 인프라 병목으로 커지고 있다는 신호다. ([Reuters][3])

## 반례

```text
- 액침냉각 테마만 있고 실제 고객·납품 없음
- 데이터센터 CAPEX 지연
- HVAC 매출은 있으나 AI DC exposure가 작은 기업
- 수주는 있으나 저마진 설비 납품에 그치는 기업
- AI CAPEX cut 발생
```

## 점수비중 v0.6

```text
EPS/FCF: 21
Structural Visibility: 22
Bottleneck/Pricing: 22
Market Mispricing: 13
Valuation Rerating: 12
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: AI_capex_delay / project_margin
```

## Green 조건

```text
고객사 데이터센터 CAPEX와 직접 연결
실제 수주/납품
냉각 기술 병목 지위
서비스·유지보수 반복매출
FY1/FY2 OP 상향
```

**정규화 포인트:**
AI 냉각은 Green 가능성이 있다. 다만 “액침냉각 테마”만으로는 Stage 1이고, 고객·수주·납품·마진이 있어야 Stage 2/3로 올린다.

---

# 3. WASTE_RECYCLING_ENVIRONMENT

폐기물처리 / 재활용 / 폐배터리 / 탈플라스틱

## 핵심 구조

```text
규제 강화 / 처리 수요
→ 허가권 / 처리시설 / 장기계약
→ 반복 처리량
→ 반복 FCF
```

## 성공사례 후보

EQT는 한국 KJ Environment와 계열사를 인수해 폐기물 처리 플랫폼을 만들기로 했고, Reuters는 이 플랫폼이 플라스틱 재활용·폐기물 에너지화·재활용 폐기물 선별을 포함하며 수도권 중심으로 한국 인구 절반 이상을 커버한다고 보도했어. 이건 폐기물처리가 단순 ESG 테마가 아니라 **허가권·처리시설·반복 FCF 인프라**가 될 수 있다는 근거다. ([Reuters][4])

## 반례

```text
- 폐배터리 테마만 있고 실제 회수량 없음
- 재활용 설비는 있으나 가동률 낮음
- 금속가격 하락으로 회수 마진 악화
- 규제 기대만 있고 실제 처리량 없음
- CAPEX 부담으로 FCF 악화
```

## 점수비중 v0.6

```text
EPS/FCF: 18
Structural Visibility: 22
Bottleneck/Pricing: 15
Market Mispricing: 13
Valuation Rerating: 12
Capital Allocation: 3
Information Confidence: 5
Risk Penalty: utilization / commodity_price / capex
```

## Green 조건

```text
허가권 또는 진입장벽
처리시설 가동률 상승
장기 처리계약
반복 FCF
CAPEX 부담 통제
```

**정규화 포인트:**
폐기물처리는 Green 가능. 폐배터리·재활용 테마는 실제 처리량과 FCF가 없으면 Watch에 머문다.

---

# 4. CLOUD_AI_SOFTWARE_INFRA

클라우드 / ERP / B2B 소프트웨어 / 컨택센터

## 핵심 구조

```text
반복 소프트웨어 매출
→ 고객 lock-in
→ ARPU / take-rate / OPM 개선
→ FCF 개선
```

## 성공사례 후보

더존비즈온은 국내 B2B 소프트웨어 기준 케이스로 볼 수 있다. EQT는 더존비즈온 지분 37.6%를 약 9.3억 달러에 인수하기로 했고, Reuters는 더존비즈온이 중소기업 대상 클라우드 ERP·회계·세무·컴플라이언스 소프트웨어를 제공한다고 설명했다. 이건 `CLOUD_AI_SOFTWARE_INFRA`에서 반복매출·SMB lock-in·운영 개선을 볼 수 있는 Stage 1~2 사례다. ([Reuters][5])

## 반례

```text
- AI 기능만 추가하고 매출화 없음
- 클라우드 비용 증가로 OPM 하락
- 고객 이탈 / churn 상승
- 컨택센터·원격근무 테마만 있고 반복매출 없음
- SI성 매출만 있고 SaaS 전환 없음
```

## 점수비중 v0.6

```text
EPS/FCF: 20
Structural Visibility: 23
Bottleneck/Pricing: 8
Market Mispricing: 16
Valuation Rerating: 14
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: AI_cost / churn / margin
```

## Green 조건

```text
반복매출 증가
ARPU 상승
OPM 개선
고객 lock-in
FCF conversion
AI 비용 통제
```

**정규화 포인트:**
클라우드/SaaS는 Green 가능하지만, 핵심은 AI 키워드가 아니라 **반복매출·OPM·FCF**다.

---

# 5. SECURITY_IDENTITY_DEEPFAKE

IT보안 / 딥페이크 / 생체인식 / CCTV

## 핵심 구조

```text
보안 위협 증가 / 규제 강화
→ 기업·정부 보안 지출
→ 반복 구독 또는 장기계약
→ OPM·ARR·FCF 개선
```

## 성공사례 후보

```text
- 반복 보안 구독 기업
- 공공/기업 장기 보안계약
- 딥페이크 탐지·인증 솔루션 실제 도입 기업
- 생체인식/CCTV가 공공·산업 계약으로 연결되는 기업
```

## 핵심 반례

CrowdStrike는 이 archetype에서 반드시 넣어야 하는 반례야. 사이버보안 수요 자체는 구조적으로 강해도, 2024년 잘못된 소프트웨어 업데이트로 800만 대 이상 컴퓨터가 영향을 받았고, 주가가 12일간 32% 하락하며 250억 달러 시가총액이 사라졌다는 Reuters 보도가 있다. 즉 보안업체는 반복매출이 있어도 **운영 신뢰도·장애·소송 리스크가 hard 4C**가 될 수 있다. ([Reuters][6])

## 점수비중 v0.6

```text
EPS/FCF: 20
Structural Visibility: 20
Bottleneck/Pricing: 10
Market Mispricing: 14
Valuation Rerating: 13
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: operational_trust / outage / legal
```

## Green 조건

```text
반복 구독 매출
낮은 churn
고객 다변화
OPM 개선
운영 신뢰도
대형 장애·소송 리스크 부재
```

**정규화 포인트:**
보안은 Green 가능성이 있지만, CrowdStrike 같은 운영 신뢰도 붕괴는 즉시 4C로 보내야 한다.

---

# 6. CRO_CLINICAL_SERVICE

CRO / 임상시험수탁 / 임상서비스

## 핵심 구조

```text
제약·바이오 R&D 증가
→ 임상시험 수탁
→ 반복 서비스 매출
→ 고객사 다변화
→ OP/FCF 개선
```

## 성공사례 후보

IQVIA는 CRO/healthcare data/analytics의 기준 사례로 볼 수 있다. 2024년 2분기에는 실적이 기대를 넘고 연간 가이던스를 상향하면서 주가가 반응했고, Technology & Analytics 부문과 임상 서비스가 혼합된 모델이라는 점이 중요하다. ([Investopedia][7])

ICON도 CRO의 글로벌 scale 기준 케이스다. 2024년 매출과 순이익이 증가한 글로벌 CRO로, 대형 고객·다지역 임상 수행능력·규모의 경제가 무엇인지 보여주는 참고 사례가 된다. ([위키백과][8])

## 반례

Charles River는 CRO/바이오 서비스의 반례다. 2024년에 바이오 고객사의 funding crunch가 지속되며 연간 전망을 낮췄고, 이 때문에 주가가 크게 압박받았다. 즉 CRO는 반복 서비스처럼 보여도 **바이오 funding cycle과 고객사 R&D 예산**이 꺾이면 4C로 가야 한다. ([Reuters][9])

## 점수비중 v0.6

```text
EPS/FCF: 18
Structural Visibility: 20
Bottleneck/Pricing: 8
Market Mispricing: 12
Valuation Rerating: 12
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: biotech_funding_cycle / customer_concentration
```

## Green 조건

```text
수주잔고 또는 backlog
고객사 다변화
반복 임상서비스 매출
OPM 개선
바이오 funding cycle 안정
```

**정규화 포인트:**
CRO는 CDMO보다 Green 강도가 낮다. 실제 수주와 고객 다변화가 있으면 Watch-to-Green, 바이오 funding crunch가 오면 4C.

---

# 7. APPAREL_BRAND_OEM

의류 브랜드 / 의류 OEM·ODM / 의류소재

## 핵심 구조

```text
브랜드 / 수출 / 고객사 주문
→ 재고 관리
→ OPM·FCF 개선
```

## 성공사례 후보

의류는 성공사례를 매우 엄격하게 잡아야 해. 글로벌 비교로는 Inditex/Zara처럼 빠른 재고 회전과 수요 대응능력이 구조적 강점이 될 수 있다. Reuters는 Inditex가 Shein과 경쟁하기 위해 저가 브랜드 Lefties를 확대하고 있으며, Shein의 가격 경쟁이 전통 의류 리테일에 압박을 주고 있다고 보도했다. 이건 의류 archetype에서 **재고 회전·가격대응·채널전략**이 핵심임을 보여준다. ([Reuters][10])

## 반례

Forever 21은 좋은 반례다. 한때 대형 fast fashion 브랜드였지만 Shein·Temu 같은 초저가 디지털 경쟁자에 밀려 파산했고, 이건 의류 브랜드가 **재고·속도·가격경쟁·채널 적응 실패**를 겪으면 4C로 가야 한다는 사례다. ([Vogue][11])

Shein 역시 성공과 반례를 동시에 제공한다. 초고속 DTC 모델과 낮은 재고비용은 성공요인이지만, 환경·관세·노동·규제 리스크는 red flag다. ([월스트리트저널][12])

## 점수비중 v0.6

```text
EPS/FCF: 18
Structural Visibility: 16
Bottleneck/Pricing: 8
Market Mispricing: 14
Valuation Rerating: 12
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: inventory / markdown / fashion_cycle / channel_concentration
```

## Green 조건

```text
해외 채널 확장
재고 회전 안정
할인율 낮음
OPM 개선
고객사 또는 브랜드 수요 반복
```

**정규화 포인트:**
의류는 K뷰티/K푸드보다 Green을 더 보수적으로 줘야 한다. 재고와 할인율이 가장 중요한 red flag다.

---

# 8. BUILDING_MATERIALS_CYCLE / REIT_DEVELOPMENT_TRUST

건자재 / 시멘트 / 철근 / 가구 / 리츠

## 핵심 구조

```text
건설 착공 / 원가 / 가격인상 / 금리
→ OPM·배당·FCF 변화
```

## 성공사례 후보

```text
- 시멘트 가격 인상 + 출하량 안정
- 철근 spread 개선
- 리츠 금리 하락 + 배당 안정
- 공실률 낮고 임대료 상승하는 자산형 REIT
```

## 핵심 반례

건설·건자재·리츠는 PF 리스크를 피할 수 없다. 한국 부동산 PF 연체율은 2021년 말 0.37%에서 2023년 말 2.70%로 상승했고, 금융당국은 부동산 프로젝트 구조조정 강화를 발표했다. 이건 건설/건자재/리츠 archetype의 핵심 red flag다. ([Reuters][13])

또 정부가 40.6조원 규모 지원책을 준비했다는 것은 단기 relief rally를 만들 수 있지만, 구조적 E2R 성공으로 바로 볼 수는 없다. 지원 의존성은 Stage 1 relief이지 Stage 3 근거가 아니다. ([Reuters][14])

## 점수비중 v0.6

```text
EPS/FCF: 17
Structural Visibility: 12
Bottleneck/Pricing: 12
Market Mispricing: 12
Valuation Rerating: 12
Capital Allocation: 5
Information Confidence: 5
Risk Penalty: credit / rates / vacancy / PF
```

## Green 조건

```text
원가 안정
가격인상 성공
출하량 회복
PF 리스크 낮음
배당 안정 또는 FCF 개선
```

**정규화 포인트:**
건자재/리츠는 금리·PF·공실·착공량에 묶인다. 부동산 회복 테마만으로 Green 금지.

---

# 9. CDMO_HEALTHCARE_CONTRACT

CMO / 원료의약품 / 바이오시밀러

## 핵심 구조

```text
장기 생산계약 / capacity / 고객사 다변화
→ 가동률 상승
→ OP/FCF 개선
```

## 성공사례 후보

Samsung Biologics는 이 archetype의 핵심 후보야. Reuters에 따르면 Samsung Biologics는 GSK로부터 미국 Rockville 생산시설을 2억 8천만 달러에 인수해 첫 미국 생산거점을 확보하고, 60,000L drug substance capacity를 추가한다. 이건 CDMO를 pre-revenue biotech이 아니라 **장기 수요·capacity·고객사·가동률**로 평가해야 한다는 근거다. ([Reuters][15])

## 반례

```text
- capacity overbuild
- 고객사 계약 지연
- 가동률 하락
- patent/litigation
- 가격경쟁
```

## 점수비중 v0.6

```text
EPS/FCF: 20
Structural Visibility: 24
Bottleneck/Pricing: 12
Market Mispricing: 12
Valuation Rerating: 12
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: litigation / capacity_utilization / customer_concentration
```

## Green 조건

```text
다년 생산 visibility
높은 가동률
고객사 다변화
장기계약
FCF conversion
```

**정규화 포인트:**
CDMO는 바이오 임상주와 다르게 Green 가능성이 있다. 단, capacity만 있고 가동률이 없으면 4C.

---

# 10. RARE_METALS_STRATEGIC_MATERIALS

전략금속 / 비철금속 / 거버넌스 이벤트

## 핵심 구조

```text
전략금속 / 제련마진 / 공급망 / 경영권 / 자본배분
```

## 성공사례 후보와 반례

Korea Zinc는 이 archetype의 대표 case다. MBK·Young Poong의 공개매수 발표 후 Korea Zinc 주가는 19.8% 급등했고, 이는 전략금속 supply chain과 governance event가 주가를 움직일 수 있음을 보여준다. 하지만 이걸 바로 structural_success로 넣으면 안 된다. 공개매수·경영권 프리미엄은 `event_premium`일 수 있고, 구조적 FCF 리레이팅과 분리해야 한다. ([Reuters][16])

또 Korea Zinc 경영권 분쟁은 공개매수 가격 상향, 자사주 매입, 신주발행 논란, 금융당국 조사 등으로 이어졌고, 이건 governance event가 4B/4C로도 바뀔 수 있음을 보여준다. ([Reuters][17])

## 점수비중 v0.6

```text
EPS/FCF: 18
Structural Visibility: 16
Bottleneck/Pricing: 15
Market Mispricing: 16
Valuation Rerating: 15
Capital Allocation: 10
Information Confidence: 5
Risk Penalty: governance_event / commodity_price / takeover_uncertainty
```

## Green 조건

```text
제련마진 또는 FCF 개선
공급망 병목
자본배분 개선
governance rerating
이벤트 프리미엄이 아닌 구조적 가치 개선
```

**정규화 포인트:**
전략금속은 Green 가능성이 있지만, 공개매수·경영권 분쟁은 대부분 event premium으로 먼저 분류해야 한다.

---

# cases_v04에 넣을 후보 정리

```text
RAIL_INFRASTRUCTURE:
- hyundai_rotem_morocco_rail_order_success_candidate
- rail_policy_no_contract_counterexample
- reconstruction_rail_theme_event_watch

AI_DATA_CENTER_COOLING:
- ecolab_coolit_ai_liquid_cooling_candidate
- samsung_flaktgroup_hvac_candidate
- liquid_cooling_theme_no_order_counterexample
- ai_capex_delay_cooling_4c

WASTE_RECYCLING_ENVIRONMENT:
- eqt_kj_environment_waste_platform_candidate
- recycling_capacity_low_utilization_counterexample
- battery_recycling_no_volume_counterexample
- waste_capex_burden_4c

CLOUD_AI_SOFTWARE_INFRA:
- douzone_bizon_cloud_erp_candidate
- ai_feature_no_fcf_counterexample
- cloud_cost_margin_pressure_4c
- churn_saas_counterexample

SECURITY_IDENTITY_DEEPFAKE:
- recurring_security_subscription_candidate
- crowdstrike_outage_4c_counterexample
- deepfake_regulation_stage1_candidate
- security_theme_no_contract_counterexample

CRO_CLINICAL_SERVICE:
- iqvia_clinical_data_scale_candidate
- icon_global_cro_scale_candidate
- charles_river_biotech_funding_crunch_4c
- cro_customer_budget_cut_counterexample

APPAREL_BRAND_OEM:
- inditex_inventory_speed_reference_success
- shein_fast_fashion_efficiency_reference
- forever21_fast_fashion_bankruptcy_4c
- apparel_inventory_markdown_counterexample

BUILDING_MATERIALS_REIT:
- cement_price_hike_candidate
- reit_rate_cut_dividend_candidate
- korea_pf_delinquency_4c
- builder_liquidity_support_relief_rally_counterexample

CDMO_HEALTHCARE_CONTRACT:
- samsung_biologics_us_capacity_candidate
- celltrion_biosimilar_candidate
- cdmo_capacity_underutilization_4c
- cdmo_patent_litigation_delay_4c

RARE_METALS_STRATEGIC_MATERIALS:
- korea_zinc_tender_event_premium
- korea_zinc_strategic_materials_candidate
- korea_zinc_share_issue_governance_risk_4c
- pure_metal_price_cycle_counterexample
```

---

# 이번 라운드 점수비중 요약

| Archetype                       | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | 성격                   |
| ------------------------------- | ------: | ---------: | ---------: | ---------: | --------: | -------------------- |
| RAIL_INFRASTRUCTURE             |      20 |         23 |         12 |         14 |        12 | 수주형, 마진/납기 중요        |
| AI_DATA_CENTER_COOLING          |      21 |         22 |         22 |         13 |        12 | 병목형, AI CAPEX 민감     |
| WASTE_RECYCLING_ENVIRONMENT     |      18 |         22 |         15 |         13 |        12 | 인프라형 FCF 가능          |
| CLOUD_AI_SOFTWARE_INFRA         |      20 |         23 |          8 |         16 |        14 | 반복매출·OPM 중심          |
| SECURITY_IDENTITY_DEEPFAKE      |      20 |         20 |         10 |         14 |        13 | 반복매출 가능, 신뢰 리스크 큼    |
| CRO_CLINICAL_SERVICE            |      18 |         20 |          8 |         12 |        12 | 바이오 funding cycle 민감 |
| APPAREL_BRAND_OEM               |      18 |         16 |          8 |         14 |        12 | 재고·할인율 핵심            |
| BUILDING_MATERIALS_REIT         |      17 |         12 |         12 |         12 |        12 | 금리·PF·공실 리스크         |
| CDMO_HEALTHCARE_CONTRACT        |      20 |         24 |         12 |         12 |        12 | 장기계약·가동률 중심          |
| RARE_METALS_STRATEGIC_MATERIALS |      18 |         16 |         15 |         16 |        15 | event premium 분리 필요  |

---

# 지금 결론

응. **A를 진행하면서 이렇게 내가 계속 점수비중을 붙이는 게 맞다.**

지금은 완성된 점수표가 아니라:

```text
archetype별 score-weight hypothesis
```

를 만드는 중이야.

그리고 이 가설은 반드시 다음으로 검증해야 해.

```text
1. cases_v04에 넣는다.
2. stage date 후보를 잡는다.
3. price path를 채운다.
4. MFE/MAE, peak, drawdown을 계산한다.
5. 점수 높게 준 case가 실제 주가 리레이팅됐는지 확인한다.
6. 틀린 archetype은 다시 점수비중을 교정한다.
```

이게 진짜 정규화 루프야.

한 줄로 정리하면:

> **성공사례는 점수축을 강화하고, 반례는 Green gate와 risk penalty를 강화한다.
> 주가검증은 그 점수비중이 실제 시장에서 맞았는지 확인하는 계기판이다.**

[1]: https://www.reuters.com/markets/deals/hyundai-rotem-wins-15-billion-order-moroccos-national-rail-operator-2025-02-26/?utm_source=chatgpt.com "Hyundai Rotem wins $1.5 billion order from Morocco's national rail operator"
[2]: https://www.reuters.com/business/ecolab-acquire-coolit-systems-475-billion-2026-03-20/?utm_source=chatgpt.com "Ecolab to buy CoolIT for $4.75 billion to tap into AI data center boom"
[3]: https://www.reuters.com/markets/deals/samsung-electronics-buy-flktgroup-15-bln-euro-2025-05-13/?utm_source=chatgpt.com "Samsung to buy German cooling system maker FlaktGroup for $1.7 billion"
[4]: https://www.reuters.com/markets/deals/eqt-strikes-deal-acquire-south-korean-waste-treatment-platform-2024-08-16/?utm_source=chatgpt.com "EQT strikes deal to acquire South Korean waste treatment platform"
[5]: https://www.reuters.com/world/asia-pacific/swedish-firm-eqt-shells-out-930-million-slice-south-koreas-douzone-bizon-2025-11-07/?utm_source=chatgpt.com "Swedish firm EQT shells out $930 million for a slice of South Korea's Douzone Bizon"
[6]: https://www.reuters.com/legal/crowdstrike-is-sued-by-shareholders-over-huge-software-outage-2024-07-31/?utm_source=chatgpt.com "CrowdStrike is sued by shareholders over huge software outage"
[7]: https://www.investopedia.com/iqvia-stock-pops-after-it-beats-q2-earnings-estimates-8681570?utm_source=chatgpt.com "IQVIA Stock Pops After It Beats Q2 Earnings Estimates"
[8]: https://en.wikipedia.org/wiki/ICON_PLC?utm_source=chatgpt.com "ICON PLC"
[9]: https://www.reuters.com/business/healthcare-pharmaceuticals/charles-river-cuts-2024-forecast-funding-crunch-among-biotech-clients-persists-2024-08-07/?utm_source=chatgpt.com "Charles River cuts 2024 forecast as funding crunch among biotech clients persists"
[10]: https://www.reuters.com/business/retail-consumer/zara-owner-inditex-expands-bargain-brand-counter-shein-2024-02-22/?utm_source=chatgpt.com "Zara owner Inditex expands bargain brand to counter Shein"
[11]: https://www.vogue.com/article/what-forever-21s-bankruptcy-says-about-the-future-of-fast-fashion?utm_source=chatgpt.com "What Forever 21's bankruptcy says about the future of fast fashion"
[12]: https://www.wsj.com/business/retail/shein-faces-italian-antitrust-scrutiny-over-environmental-claims-ade94abc?utm_source=chatgpt.com "Shein Faces Italian Antitrust Scrutiny Over Environmental Claims"
[13]: https://www.reuters.com/markets/asia/south-korea-tightens-scrutiny-speed-up-real-estate-restructuring-2024-05-13/?utm_source=chatgpt.com "South Korea tightens scrutiny to speed up real estate restructuring"
[14]: https://www.reuters.com/markets/asia/south-korea-prepares-financial-support-small-businesses-builders-2024-03-27/?utm_source=chatgpt.com "South Korea prepares financial support for small businesses, builders"
[15]: https://www.reuters.com/business/healthcare-pharmaceuticals/samsung-biologics-buy-us-drug-production-facility-gsk-280-mln-2025-12-21/?utm_source=chatgpt.com "Samsung Biologics to buy US drug production facility from GSK for $280 million"
[16]: https://www.reuters.com/markets/deals/private-equity-mbk-young-poong-launch-15-bln-tender-offer-korea-zinc-shares-2024-09-13/?utm_source=chatgpt.com "Private equity MBK, Young Poong launch $1.5 bln tender offer for Korea Zinc shares"
[17]: https://www.reuters.com/markets/commodities/private-equity-firm-mbk-young-poong-raise-korea-zinc-tender-offer-188-bln-2024-10-04/?utm_source=chatgpt.com "Private equity firm MBK, Young Poong raise Korea Zinc tender offer to $1.88 bln"
