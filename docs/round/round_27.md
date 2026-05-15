좋아. **Round 21: 얇은 archetype + 주요 archetype 점수비중 v1.2 보강**으로 계속 채울게.

이번 라운드는 특히 “성공처럼 보이지만 실제로는 반례가 될 수 있는 케이스”를 더 강하게 넣는다. 점수정규화에서 제일 위험한 건 좋은 기업을 성공사례로 착각하는 거야. **점수가 높아야 할 이유와, 그 점수 이후 주가·EPS·FCF가 실제로 같이 갔는지**를 계속 분리해야 한다.

기본 원칙은 그대로야. 에이전트는 테마봇이 아니라, **산업 구조 변화 → EPS/FCF 체급 변화 → 시장의 과거 프레임 오해 → 밸류에이션 리레이팅**을 찾는 시스템이어야 한다.
그리고 계약금액, 계약기간, 매출 대비 계약금액, OP YoY 같은 값은 실제 공시·리포트에서 확인될 때만 써야 한다. 없는 숫자를 만들어 넣으면 안 된다.

---

# 1. GAME_CONTENT_IP

## 게임 / IP / 인도 게임시장 / 신작 리스크

### 핵심 구조

```text
글로벌 IP
→ 반복 monetization
→ 지역 확장
→ 규제 리스크 관리
→ OP/FCF 지속성
```

게임은 “신작 기대”와 “반복 IP 수익화”를 분리해야 해. 신작 발표만으로 주가가 오르면 그건 Stage 1~2일 수 있지만, Stage 3가 되려면 실제 매출·OP·반복성이 확인되어야 한다.

### 성공 후보: Krafton / BGMI

Krafton은 `GAME_CONTENT_IP`의 성공 후보로 볼 수 있다. Reuters는 Krafton이 Naver·Mirae와 함께 인도 tech fund를 추진했고, Krafton이 BGMI를 통해 인도 게임시장에 큰 노출을 갖고 있으며 BGMI가 2억 4천만 다운로드 이상을 기록했다고 보도했다. 다만 BGMI는 과거 데이터 보안 우려로 ban 이력이 있었다는 점도 함께 언급됐다. ([Reuters][1])

즉 이 케이스는 성공과 반례를 동시에 준다.

```text
성공 요소:
- 글로벌 IP
- 거대한 인도 사용자 기반
- 반복 monetization 가능성
- 현지 ecosystem 투자

반례 요소:
- 규제/데이터 보안 리스크
- 특정 지역 의존도
- 신작/게임 cycle
```

### 점수비중 v1.2

```text
EPS/FCF: 20
Structural Visibility: 18
Bottleneck/Pricing: 6
Market Mispricing: 14
Valuation Rerating: 12
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: hit_driven / regulation / data_security / single_IP_dependency
```

### 정규화 교정

게임/IP는 **Watch 중심**이 맞다.

```text
Green 조건:
- IP가 단일 신작이 아니라 반복 monetization 구조
- 지역/플랫폼 다변화
- 실제 OP/EPS 상향
- 규제·데이터 리스크 낮음
- 신작 출시 후 매출이 확인됨

Green 금지:
- 신작 기대만 있음
- 다운로드/트래픽만 있고 monetization 없음
- 규제 ban risk가 큼
- 단일 IP 의존
```

---

# 2. MEDICAL_DEVICE_HEALTHCARE_EXPORT

## 미용기기 / 보톡스 / 임플란트 / 의료기기 수출

### 핵심 구조

```text
제품 판매
→ 반복 시술·소모품
→ 수출국 확대
→ OPM/FCF 개선
→ 의료기기 프레임 리레이팅
```

의료기기는 pre-revenue biotech보다 훨씬 E2R에 가까울 수 있어. 이유는 제품 매출, 반복 시술, 소모품, 수출국, OPM을 숫자로 확인할 수 있기 때문이야.

### 성공 후보: Classys

Classys는 비침습 피부미용 의료기기 회사로 정리되며, 2025년 기준 60개국 이상에 수출한다고 나온다. 이런 케이스는 `MEDICAL_DEVICE_HEALTHCARE_EXPORT`에서 수출국 확대와 반복 시술/소모품 구조를 확인하는 기준 케이스로 쓸 수 있다. ([위키백과][2])

### 반례: Botox류 규제·위조 리스크

보툴리눔 톡신/미용의료는 반복 수요가 강하지만, 규제·안전·위조품 리스크가 크다. FDA가 승인되지 않았거나 위조 가능성이 있는 Botox류 제품 판매 웹사이트에 경고를 보낸 사례는, 이 archetype의 red flag로 넣어야 한다. ([AP News][3])

### 점수비중 v1.2

```text
EPS/FCF: 20
Structural Visibility: 22
Bottleneck/Pricing: 13
Market Mispricing: 14
Valuation Rerating: 12
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: approval / safety / counterfeit / channel_quality / competition
```

### 정규화 교정

의료기기는 **Green 가능 archetype**으로 둬도 된다.
단, 장비 판매만으로는 부족하다.

```text
Green 조건:
- 수출국 확대
- 반복 시술 또는 소모품 매출
- OPM/ROE 개선
- 허가·규제 리스크 낮음
- 채널 품질 안정

4C 조건:
- 허가 지연
- 위조/안전 이슈
- 경쟁 심화로 ASP 하락
- 단일 장비 판매 후 반복매출 부재
```

---

# 3. DIGITAL_HEALTHCARE_AI

## 의료AI / 영상진단 / 원격의료 / 유전체검사

### 핵심 구조

```text
임상 문제
→ AI 진단·판독·문서화 솔루션
→ 병원 도입
→ 수가·보험·반복 사용
→ 매출/FCF 전환
```

의료AI는 “AI니까 좋다”가 아니라, **외부 임상검증 + 병원 워크플로우 도입 + 수가/과금 + 매출화**가 있어야 한다.

### 성공 후보: mammography AI

대규모 mammography AI 연구는 약 50만 개 이상의 검사 데이터를 바탕으로 높은 AUROC와 recall 감소 가능성을 제시했고, radiologist workload를 줄일 가능성도 보여줬다. 이건 의료AI의 Stage 1~2 근거가 될 수 있다. ([arXiv][4])

### 반례: subgroup 성능·임상 일반화 리스크

반면 Lunit INSIGHT DBT 모델을 16만 건 이상의 mammography exam에서 평가한 연구는 전체 AUC가 높더라도, non-invasive cancer, calcification, dense breast tissue 같은 subgroup에서 성능 차이가 있음을 지적했다. 이건 의료AI가 “전체 성능 좋음”만으로 Green이 될 수 없고, 외부 검증·subgroup 성능·workflow 적용을 봐야 한다는 반례다. ([arXiv][5])

### 점수비중 v1.2

```text
EPS/FCF: 18
Structural Visibility: 17
Bottleneck/Pricing: 8
Market Mispricing: 13
Valuation Rerating: 12
Capital Allocation: 0
Information Confidence: 7
Risk Penalty: regulation / reimbursement / clinical_validation / subgroup_bias / liability
```

### 정규화 교정

의료AI는 **Watch-to-Green**이다.

```text
Green 조건:
- 외부 임상검증
- 허가/승인
- 병원 도입
- 수가·보험 또는 반복 과금
- 실제 매출/OP 전환

Green 금지:
- 논문 성능만 있음
- PoC만 있음
- 병원 도입 없음
- 수가/과금 구조 없음
- subgroup 성능 리스크 큼
```

---

# 4. RETAIL_ECOMMERCE_LOGISTICS

## 편의점 / 이커머스 / 홈쇼핑 / 콜드체인

### 핵심 구조

```text
점포망 / 물류망 / PB상품
→ same-store sales
→ 물류비·재고 통제
→ OPM / FCF 개선
```

### 성공 후보: 편의점

CU와 GS25는 한국 편의점 archetype의 기준 케이스로 쓸 수 있다. CU는 2025년 기준 한국 내 18,000개 이상 점포와 해외 점포를 가진 것으로 정리되고, GS25도 2024년 말 기준 18,000개 이상 국내 점포로 정리된다. 점포망 자체가 점수 근거는 아니지만, **점포 효율·PB mix·해외 확장·OPM 개선**을 볼 수 있는 기준이 된다. ([위키백과][6])

### 반례: Coupang 규제·공급업체 압박·데이터 보안

Coupang은 이커머스 물류 scale의 성공 후보이면서 동시에 강한 반례다. KFTC가 Coupang에 납품업체 압박과 대금 지연 문제로 과징금을 부과했다는 Reuters 보도는, 유통 플랫폼의 마진 개선이 구조적 효율인지 공급업체 압박인지 구분해야 한다는 점을 보여준다. ([Reuters][7])

또 Coupang의 대규모 개인정보 유출 사건은 디지털 유통 플랫폼에서 데이터 보안이 4C로 작동할 수 있음을 보여준다. 약 3,300만 명 고객 데이터가 노출됐고, 주가도 하락했다는 보도는 `data_security`를 강한 red flag로 넣어야 한다는 근거다. ([Reuters][8])

### 점수비중 v1.2

```text
EPS/FCF: 18
Structural Visibility: 16
Bottleneck/Pricing: 5
Market Mispricing: 13
Valuation Rerating: 14
Capital Allocation: 3
Information Confidence: 5
Risk Penalty: logistics_cost / inventory / supplier_regulation / data_security / competition
```

### 정규화 교정

유통·이커머스는 **매출 성장보다 OPM/FCF가 핵심**이다.

```text
Stage 2 이상 조건:
- OPM 개선
- 물류비 안정
- 재고 정상화
- 반복 고객/점포 효율
- 규제·보안 리스크 낮음

4C 조건:
- 공급업체 압박·규제
- 데이터 유출
- 물류비 급증
- 매출은 늘지만 FCF 악화
```

---

# 5. EDUCATION_SPECIALTY_SERVICES

## 교육 / 입시 / 키즈 / 유아용품 / 에듀테크

### 핵심 구조

```text
반복 수강
→ 가격 결정력
→ 온라인/성인/해외 확장
→ OPM·FCF 개선
```

교육은 사교육 수요가 크지만, 저출산과 규제 리스크가 강하다. 한국의 사교육 문제는 구조적으로 깊고, 정부의 “킬러문항” 제거 같은 규제도 사교육 시장에 영향을 줄 수 있다는 보도가 있다. 즉 교육은 수요가 강하더라도 정책·인구 리스크를 반드시 반영해야 한다. ([Time][9])

### 성공 후보

```text
- 성인교육 / 자격시험 / 직무교육 플랫폼
- 온라인 반복수강 플랫폼
- 해외 확장 교육기업
- B2B 기업교육
```

### 반례

```text
- 유아·키즈 중심 기업: 저출산 직접 타격
- 입시 규제
- 오프라인 학원 고정비 부담
- AI 튜터 경쟁
- 단기 입시제도 변경 테마
```

### 점수비중 v1.2

```text
EPS/FCF: 18
Structural Visibility: 17
Bottleneck/Pricing: 5
Market Mispricing: 12
Valuation Rerating: 12
Capital Allocation: 2
Information Confidence: 5
Risk Penalty: birthrate / regulation / AI_substitution / offline_fixed_cost
```

### 정규화 교정

교육은 **Watch 중심**이다.

```text
Green 조건:
- 성인교육/해외/B2B로 저출산 리스크 상쇄
- 반복수강·구독 구조
- OPM 개선
- 정책 리스크 낮음

Green 금지:
- 입시제도 테마만 있음
- 키즈/유아용품 내수 중심
- 오프라인 학원 고정비 큼
```

---

# 6. TELECOM_GRID_AI_NETWORK

## 5G·6G / 광통신 / 스마트그리드 / 전력망 효율화

### 핵심 구조

```text
AI 데이터센터·전력수요 증가
→ 송전망·광통신·통신망 병목
→ CAPEX / 장비 수주
→ 단, 통신·전력 인프라는 규제와 CAPEX 부담 큼
```

전력망은 AI 데이터센터와 재생에너지 확산 때문에 중요한데, 한국 전력망은 정적 송전용량 산정 방식의 한계가 있다는 연구도 있다. 이는 스마트그리드·송전망 효율화가 구조적 필요를 가질 수 있음을 보여준다. 다만 이것이 특정 기업의 EPS/FCF로 연결되려면 실제 장비 수주·계약·OP 전환이 필요하다. ([arXiv][10])

### 성공 후보

```text
- 스마트그리드 장비
- 광통신·광케이블
- AI 데이터센터 연결 전력망
- 통신망 보안·네트워크 장비
```

### 반례

```text
- 5G/6G 정책 테마만 있음
- CAPEX 기대만 있고 수주 없음
- 통신사 CAPEX 부담으로 FCF 훼손
- 규제 요금/투자회수 불확실
```

### 점수비중 v1.2

```text
EPS/FCF: 17
Structural Visibility: 18
Bottleneck/Pricing: 12
Market Mispricing: 12
Valuation Rerating: 10
Capital Allocation: 2
Information Confidence: 5
Risk Penalty: capex_burden / regulation / project_delay / low_margin_equipment
```

### 정규화 교정

스마트그리드·통신망은 **Watch-to-Green**이다.

```text
Green 조건:
- 실제 장비 수주
- AI 데이터센터/전력망과 직접 연결
- 장기 CAPEX visibility
- OP/EPS 상향

Green 금지:
- 5G/6G/스마트그리드 키워드만 있음
- 정부 정책만 있음
- 통신사 CAPEX 부담만 커짐
```

---

# 7. GAME_CONTENT_IP — 재보정

앞에서 Krafton/BGMI를 봤듯이 게임은 “글로벌 IP + 반복 monetization”이 있어야 한다. Krafton은 인도 BGMI exposure와 2억 4천만 다운로드 기반이 있어 성공 후보지만, 과거 ban 이력과 데이터 보안 이슈가 있어 Green은 조건부다. ([Reuters][1])

### 점수비중 v1.2

```text
EPS/FCF: 20
Structural Visibility: 18
Bottleneck/Pricing: 6
Market Mispricing: 14
Valuation Rerating: 12
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: hit_driven / regulation / data_security / single_IP_dependency
```

### 정규화 교정

```text
점수 강화:
- IP portfolio
- 글로벌 monetization
- 실제 매출/OP
- 낮은 churn
- 지역 다변화

점수 제한:
- 신작 기대만 있음
- 단일 게임 의존
- 규제 ban risk
- 출시 후 매출 미달
```

---

# 8. MEDICAL_DEVICE_HEALTHCARE_EXPORT — 재보정

Classys 같은 미용 의료기기는 반복 시술·수출국·OPM이 있으면 Green 가능성이 높다. ([위키백과][2])
하지만 Botox류처럼 규제·안전·위조품 이슈가 생기면 strong red flag다. ([AP News][3])

### 점수비중 v1.2

```text
EPS/FCF: 20
Structural Visibility: 22
Bottleneck/Pricing: 13
Market Mispricing: 14
Valuation Rerating: 12
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: approval / safety / counterfeit / competition / channel_quality
```

### 정규화 교정

```text
Green 조건:
- 수출국 확대
- 반복 시술/소모품
- 허가 안정
- OPM/FCF 개선
- 경쟁 심화에도 ASP 유지

4C 조건:
- 안전성 이슈
- 허가 지연
- 위조품/규제 이슈
- 단일 장비 판매 후 반복매출 부재
```

---

# 9. 주요 점수비중 v1.2 요약표

| Archetype               | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | 핵심 리스크       |
| ----------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ------------ |
| GAME_CONTENT_IP         |      20 |         18 |          6 |         14 |        12 |       0 | 규제, 단일 IP    |
| MEDICAL_DEVICE_EXPORT   |      20 |         22 |         13 |         14 |        12 |       0 | 허가, 안전, 경쟁   |
| DIGITAL_HEALTHCARE_AI   |      18 |         17 |          8 |         13 |        12 |       0 | 수가, 검증, 책임   |
| RETAIL_ECOMMERCE        |      18 |         16 |          5 |         13 |        14 |       3 | 물류비, 규제, 보안  |
| EDUCATION_SERVICES      |      18 |         17 |          5 |         12 |        12 |       2 | 저출산, 규제      |
| TELECOM_GRID_AI_NETWORK |      17 |         18 |         12 |         12 |        10 |       2 | CAPEX, 규제    |
| AI_DATA_CENTER_COOLING  |      21 |         22 |         22 |         13 |        12 |       0 | 프로젝트 지연      |
| SECURITY_IDENTITY       |      20 |         20 |         10 |         14 |        13 |       0 | 장애, 소송       |
| CLOUD_AI_SOFTWARE       |      20 |         23 |          8 |         16 |        14 |       0 | AI 비용, churn |
| INSURANCE_UNDERWRITING  |      15 |         21 |          4 |         15 |        25 |      10 | 손해율, 자본      |

---

# 10. cases_v09 추가 후보

```text
GAME_CONTENT_IP:
- krafton_bgmi_india_ip_candidate
- bgmi_regulatory_ban_risk_counterexample
- new_game_hype_no_revenue_counterexample
- single_ip_dependency_4c

MEDICAL_DEVICE_HEALTHCARE_EXPORT:
- classys_aesthetic_device_export_candidate
- hugel_botox_us_approval_candidate
- botox_counterfeit_safety_risk_4c
- single_device_no_consumable_counterexample

DIGITAL_HEALTHCARE_AI:
- mammography_ai_external_validation_candidate
- lunit_subgroup_performance_risk_counterexample
- hospital_ai_no_reimbursement_counterexample
- medical_ai_liability_risk_4c

RETAIL_ECOMMERCE_LOGISTICS:
- cu_gs25_store_efficiency_candidate
- coupang_logistics_scale_candidate
- coupang_supplier_regulation_risk_4c
- coupang_data_breach_4c

EDUCATION_SPECIALTY_SERVICES:
- adult_education_subscription_candidate
- hagwon_demand_candidate
- low_birthrate_kids_education_counterexample
- education_regulation_counterexample

TELECOM_GRID_AI_NETWORK:
- smart_grid_line_rating_candidate
- ai_datacenter_grid_capex_candidate
- 5g_6g_policy_no_revenue_counterexample
- telecom_capex_burden_4c

GAME_CONTENT_IP:
- krafton_india_fund_candidate
- krafton_bgmi_data_security_counterexample

MEDICAL_DEVICE_HEALTHCARE_EXPORT:
- classys_export_device_candidate
- botox_counterfeit_safety_counterexample
```

---

# Round 21 핵심 교정

```text
1. 게임/IP는 global IP와 반복 monetization이 있어야 한다.
   다운로드/트래픽만으로 Green 금지.

2. 의료기기는 Green 가능성이 높지만, 허가·안전·반복 소모품이 필수.

3. 의료AI는 논문 성능과 매출화를 분리해야 한다.
   subgroup 성능·수가·병원 도입 없으면 Watch.

4. 편의점은 점포 수가 아니라 점포 효율·PB·OPM을 본다.

5. 이커머스는 물류 scale이 있어도 규제·공급업체 압박·데이터 보안이 4C가 될 수 있다.

6. 교육은 수요가 강해도 저출산·규제 리스크 때문에 Watch 중심.

7. 스마트그리드/통신망은 구조적 필요가 있어도 실제 장비수주와 OP 전환 전까지 Green 제한.

8. 보안은 반복매출이 있어도 운영 신뢰 붕괴가 hard 4C.

9. HBM/AI 데이터센터/클라우드/SaaS/의료기기/K뷰티/보험은 Green 가능성이 있는 쪽.
   단, 모두 actual evidence가 필수.

10. 대부분의 테마는 여전히 price-path validation 전까지 production scoring에 넣으면 안 된다.
```

---

# 현재 판단

성공/반례 기반 점수정규화는 계속 좋아지고 있다.
이제 특히 좋아진 건:

```text
- Green 가능 archetype과 Watch/Red archetype의 경계가 선명해짐
- 같은 테마 안에서도 성공 조건과 반례 조건이 분리됨
- 주가가 올라도 EPS/FCF가 안 따라오면 성공사례가 아니라는 원칙이 확립됨
- risk penalty가 archetype별로 달라짐
```

하지만 마지막으로 다시 강조하면, 아직은 **점수비중 가설 v1.2**야.
다음 검증은 반드시:

```text
case stage date
price path
MFE/MAE
drawdown_after_peak
score-price alignment
shadow scoring
```

으로 해야 한다.

[1]: https://www.reuters.com/world/asia-pacific/pubg-maker-krafton-leads-south-korean-trio-666-million-india-tech-bet-2025-12-19/?utm_source=chatgpt.com "PUBG maker Krafton leads South Korean trio in $666 million India tech bet"
[2]: https://en.wikipedia.org/wiki/Classys?utm_source=chatgpt.com "Classys"
[3]: https://apnews.com/article/67afcdc72e100204181c20aacec39d89?utm_source=chatgpt.com "FDA warns websites selling unapproved Botox for cosmetic purposes"
[4]: https://arxiv.org/abs/2504.05636?utm_source=chatgpt.com "A Multi-Modal AI System for Screening Mammography: Integrating 2D and 3D Imaging to Improve Breast Cancer Detection in a Prospective Clinical Study"
[5]: https://arxiv.org/abs/2503.13581?utm_source=chatgpt.com "Subgroup Performance of a Commercial Digital Breast Tomosynthesis Model for Breast Cancer Detection"
[6]: https://en.wikipedia.org/wiki/CU_%28store%29?utm_source=chatgpt.com "CU (store)"
[7]: https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-watchdog-fines-coupang-16-million-pressuring-suppliers-delaying-2026-02-26/?utm_source=chatgpt.com "South Korea watchdog fines Coupang $1.6 million for pressuring suppliers, delaying payments"
[8]: https://www.reuters.com/sustainability/boards-policy-regulation/south-koreas-lee-calls-tougher-penalties-after-coupang-data-breach-2025-12-02/?utm_source=chatgpt.com "South Korea's Lee calls for tougher penalties after Coupang data breach"
[9]: https://time.com/6292773/south-korea-crackdown-hagwons-cram-schools-competition/?utm_source=chatgpt.com "Why S. Korea's Crackdown on Private Tutoring Is Just a 'Band-Aid' on a Much Larger Problem"
[10]: https://arxiv.org/abs/2503.02274?utm_source=chatgpt.com "Rethinking Static Line Rating for Economic and Efficient Power Operation in South Korea"
