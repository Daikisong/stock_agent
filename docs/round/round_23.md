맞아. 계속 A를 진행해야 해.
지금은 **성공/반례를 더 많이 쌓을수록 점수정규화 품질이 좋아지는 구간**이야.

현재까지의 원칙은 그대로 유지한다.

> **서생원식 핵심 = 산업 구조 변화 → EPS/FCF 체급 변화 → 시장의 과거 프레임 오해 → 밸류에이션 리레이팅.**
> 테마명은 검색·분류용 꼬리표일 뿐이고, 점수는 실제 공시·리포트·재무·가격 evidence에서만 나와야 한다.
> 계약금액, 계약기간, 매출 대비 계약금액, OP YoY 같은 필드는 실제로 추출될 때만 써야 하고, 없는 숫자를 만들어 넣으면 안 된다.

이번은 **Round 17: 얇은 archetype 보강 + 주요 archetype 재정규화 v0.8**로 갈게.

---

# 1. DIGITAL_HEALTHCARE_AI

의료AI / 원격의료 / 유전체검사 / AI 진단

## 핵심 구조

```text
의료 현장 문제
→ AI 진단/판독/문서화 솔루션
→ 병원 도입
→ 수가·보험·반복 사용
→ 매출/FCF 전환
```

의료AI는 “AI니까 좋다”가 아니라, **임상 성능 + 규제/허가 + 병원 워크플로우 도입 + 수가/반복매출**이 있어야 해.

## 성공 후보

| 케이스                    | 판단                                                                                                                                                                                                       |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Lunit / mammography AI | 의료영상 AI의 성능·도입 가능성 후보. Lunit INSIGHT DBT 모델을 대규모 mammography 데이터에서 평가한 연구는 AUC 0.91을 보였지만, 비침습암·calcification·dense breast tissue에서 성능 차이가 있음을 지적한다. 즉 성공 후보이면서 동시에 subgroup validation이 필수라는 반례 성격도 있다. |
| 병원 워크플로우 AI            | 판독 보조, 임상문서화, triage 등 반복 사용이 있으면 후보                                                                                                                                                                     |
| 원격의료 플랫폼               | 제도화·수가·반복 이용량이 확인되면 후보                                                                                                                                                                                   |
| 유전체검사/정밀의료             | 반복 검사·보험·병원 채택이 있으면 후보                                                                                                                                                                                   |

의료AI는 신뢰성과 실제 배포 가능성이 매우 중요하다. FUTURE-AI consensus guideline은 의료AI가 실제 임상에 배포되려면 fairness, universality, traceability, usability, robustness, explainability 같은 원칙을 만족해야 한다고 정리한다. ([arXiv][1])

## 반례

| 반례                 | 왜 위험한가                          |
| ------------------ | ------------------------------- |
| 논문 성능만 있고 병원 매출 없음 | 연구 성능과 매출화는 다름                  |
| 수가/보험 없음           | 병원 도입이 느릴 수 있음                  |
| 과신/오진 리스크          | 의료 AI는 사용자가 부정확한 답변도 신뢰할 위험이 있음 |
| 규제·책임소재 불명확        | 의료기기 허가와 실제 사용은 별개              |

AI 의료 응답에 대한 과신 문제도 red flag다. 한 연구는 비전문가들이 정확도가 낮은 AI 의료 응답도 의사 답변처럼 신뢰하는 경향을 보였다고 보고했다. 따라서 의료AI는 “성능 좋음”만으로 Green이 아니라, 임상 검증·책임·수가·반복매출까지 확인해야 한다.

## 점수비중 v0.8

```text
EPS/FCF: 18
Structural Visibility: 17
Bottleneck/Pricing: 8
Market Mispricing: 13
Valuation Rerating: 12
Capital Allocation: 0
Information Confidence: 7
Risk Penalty: regulation / reimbursement / clinical_validation / liability
```

## 정규화 포인트

의료AI는 **Watch-to-Green** archetype이다.
Green을 주려면 아래가 필요하다.

```text
허가/승인
병원 도입
수가·보험 또는 반복 과금
임상 성능의 외부검증
매출/OP 전환
```

AI 키워드, 논문, PoC만 있으면 Stage 1~2에 머문다.

---

# 2. TELECOM_5G_6G_AI_NETWORK

5G·6G / 광통신 / 통신망 / AI 네트워크

## 핵심 구조

```text
통신망 CAPEX
→ 5G/6G/AI-native network
→ 장비·광통신·보안·데이터센터
→ 반복 통신 매출 또는 CAPEX 수주
```

이 archetype은 `AI_DATA_CENTER_INFRASTRUCTURE`와 겹치지만, 통신사는 별도 위험이 있어. 통신주는 안정적 반복매출을 가지지만, 성장률이 낮고 CAPEX 부담이 커서 Green을 쉽게 주면 안 돼.

## 성공 후보

| 케이스                    | 판단                                                                                     |
| ---------------------- | -------------------------------------------------------------------------------------- |
| SKT / AI 데이터센터         | SK와 AWS가 울산에 약 7조원 규모 AI 데이터센터를 건설하기로 한 사례는 통신·클라우드·AI 인프라가 결합되는 Stage 1~2 후보로 볼 수 있다. |
| 광통신·광케이블·5G/6G 장비      | 실제 통신사 CAPEX와 수주가 붙으면 후보                                                               |
| AI-native network / 6G | 장기 테마지만 실제 매출화 전 Green 제한                                                              |

SK/AWS 데이터센터는 100MW 초기 규모와 2029년 가동 예정이라는 점에서 AI 인프라 수요의 실제 CAPEX 신호다. 다만 통신·IDC 관련주는 실제 수주·매출 인식까지 확인해야 한다. ([Reuters][2])

## 반례

| 반례              | 왜 위험한가                               |
| --------------- | ------------------------------------ |
| 5G 장비 테마 반복     | 과거 5G cycle처럼 CAPEX peak 이후 실적 둔화 가능 |
| 통신사 보안 사고       | 반복매출은 있어도 신뢰·규제 리스크가 생김              |
| 6G 논문/정책만 있는 테마 | 매출화 전 Green 금지                       |
| CAPEX 부담        | 수익성 개선 없이 투자만 증가하면 FCF 훼손            |

6G는 AI-native network, sovereign AI, O-RAN 등 장기 변화가 있을 수 있지만, 아직 상당 부분은 기술·정책 구상 단계다. 따라서 `TELECOM_5G_6G_AI_NETWORK`는 Stage 1 radar에는 유용하지만, 실제 장비 수주·통신사 ARPU·IDC 매출 전환이 없으면 Stage 3로 올리면 안 된다. ([arXiv][3])

## 점수비중 v0.8

```text
EPS/FCF: 16
Structural Visibility: 18
Bottleneck/Pricing: 10
Market Mispricing: 12
Valuation Rerating: 10
Capital Allocation: 3
Information Confidence: 5
Risk Penalty: capex_burden / regulation / security_breach
```

## 정규화 포인트

통신·5G·6G는 **Watch 중심**이다.
AI 데이터센터와 실제 IDC 매출이 붙으면 점수를 올릴 수 있지만, 네트워크 세대교체 테마만으로 Green은 금지.

---

# 3. MEDIA_AD_CONTENT_CYCLE

광고 / 방송·언론 / 미디어 콘텐츠 / 음원서비스

## 핵심 구조

```text
광고 경기 회복 / 콘텐츠 IP / 플랫폼 유통
→ 매출화
→ OPM 개선
→ 반복 IP·광고 회복 확인
```

미디어·광고는 생각보다 cyclical하다. 콘텐츠와 엔터는 IP 반복성이 있으면 좋지만, 광고·방송은 경기와 플랫폼 변화에 크게 흔들린다.

## 성공 후보

| 케이스                         | 판단                                   |
| --------------------------- | ------------------------------------ |
| HYBE / K-pop global touring | 글로벌 투어, 팬덤, IP monetization이 반복되면 후보 |
| JYP / SM / YG               | 투어·앨범·MD·플랫폼 매출이 반복되면 후보             |
| 광고대행사                       | 광고 경기 회복 + 디지털 전환 + OPM 개선 필요        |
| 음원서비스                       | 반복 구독과 ARPU가 있으면 후보                  |

K-pop IP는 매출화가 명확할 때만 점수를 높여야 한다. 예를 들어 글로벌 투어의 attendance와 gross가 확인되는 경우에는 IP monetization evidence로 사용할 수 있지만, 특정 아티스트 의존과 계약 리스크가 함께 존재한다. 최근 K-pop 투어 데이터들은 대형 IP가 실제 매출을 만들 수 있음을 보여주지만, 엔터사는 hit-driven risk와 아티스트 계약 리스크를 동시에 봐야 한다. ([위키백과][4])

## 반례

| 반례              | 왜 위험한가             |
| --------------- | ------------------ |
| 신작·컴백 기대만 있는 엔터 | 실제 매출화 전까지 Stage 1 |
| 광고 경기 둔화        | 매출과 OPM이 바로 흔들림    |
| 단일 아티스트 의존      | 계약·군입대·스캔들 리스크     |
| 방송·언론 구조 둔화     | 광고 이탈, 플랫폼 전환 실패   |

## 점수비중 v0.8

```text
EPS/FCF: 18
Structural Visibility: 16
Bottleneck/Pricing: 6
Market Mispricing: 14
Valuation Rerating: 12
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: hit_driven / ad_cycle / contract_risk
```

## 정규화 포인트

게임·엔터·미디어는 **Watch 중심**이다.
반복 IP 포트폴리오와 글로벌 monetization이 확인될 때만 Stage 2~3 후보. 신작/컴백 기대만으로는 Green 금지.

---

# 4. SERVICE_KIOSK_AUTOMATION

키오스크 / 컨택센터 / 무인화 / 서비스 자동화

## 핵심 구조

```text
인건비 상승 / 무인화 수요
→ 키오스크·컨택센터·자동화 솔루션 도입
→ 반복 유지보수·SaaS 매출
→ OPM 개선
```

이 archetype은 로봇과 비슷하지만 더 실용적이다. 휴머노이드보다 매출화가 빠를 수 있지만, 단순 장비 판매만 있으면 Green을 주면 안 된다.

## 성공 후보

| 케이스        | 판단                           |
| ---------- | ---------------------------- |
| 키오스크 제조·운영 | 설치대수 + 유지보수 + 결제 수수료가 있으면 후보 |
| 컨택센터 자동화   | B2B 반복계약, AI 상담, 비용절감 효과 필요  |
| 무인점포 솔루션   | 실제 가맹점 도입과 반복 과금 필요          |
| 스마트팩토리 서비스 | 장비 판매보다 유지보수·SW 매출 확인        |

## 반례

| 반례                 | 왜 위험한가      |
| ------------------ | ----------- |
| 장비 일회성 판매          | 반복매출 없음     |
| 최저임금 테마만 있는 종목     | 실제 도입·매출 없음 |
| 고객 이탈/저가경쟁         | 마진 훼손       |
| 설치는 많지만 유지보수 수익 없음 | FCF 약함      |

## 점수비중 v0.8

```text
EPS/FCF: 18
Structural Visibility: 17
Bottleneck/Pricing: 7
Market Mispricing: 13
Valuation Rerating: 11
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: one_off_hardware_sales / margin_competition
```

## 정규화 포인트

서비스 자동화는 Watch-to-Green 가능하지만, **반복 유지보수·SaaS·결제 수익**이 핵심이다. 단순 장비 판매는 Stage 1~2 제한.

---

# 5. SMART_FARM_AGRI_TECH

스마트팜 / 농기계 / 종자·비료·농약

## 핵심 구조

```text
농업 인력 부족 / 식량안보 / 기후 리스크
→ 스마트팜·농기계·종자·비료 수요
→ 수주 또는 반복 판매
→ 그러나 commodity cycle과 정책 의존성 큼
```

## 성공 후보

| 케이스        | 판단                          |
| ---------- | --------------------------- |
| 스마트팜 수출 기업 | 실제 해외 수주·운영계약이 있으면 후보       |
| 농기계        | 해외 판매와 부품·서비스 매출이 있으면 후보    |
| 종자·비료·농약   | 가격전가, 반복 구매, 작황 cycle 확인 필요 |
| 식량안보 정책 수혜 | 실제 계약 전까지는 Watch            |

## 반례

| 반례             | 왜 위험한가       |
| -------------- | ------------ |
| 곡물가격 테마        | 가격 cycle일 뿐  |
| 대두·사료 원가 급등    | 음식료/축산 마진 압박 |
| 스마트팜 정책만 있는 종목 | 실제 수주 없음     |
| 날씨 이벤트         | 일회성 수요       |

## 점수비중 v0.8

```text
EPS/FCF: 18
Structural Visibility: 14
Bottleneck/Pricing: 12
Market Mispricing: 9
Valuation Rerating: 9
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: commodity_cycle / subsidy / weather_event
```

## 정규화 포인트

스마트팜·농기계는 Watch 중심.
Green은 해외 수주·반복 서비스·OPM 개선이 있을 때만 가능. 곡물·사료·대두는 cycle/event로 본다.

---

# 6. HOME_LIVING_APPLIANCE / HOME_CHILD_EDUCATION

밥솥 / 스마트홈 / 키즈 / 유아용품

## 핵심 구조

```text
생활소비재 / 가전 / 유아용품
→ 반복수요 제한적
→ 수출·브랜드·프리미엄화가 있어야 E2R 가능
```

## 성공 후보

| 케이스        | 판단                          |
| ---------- | --------------------------- |
| 밥솥·생활가전 수출 | 중국/미국/동남아 수출, 프리미엄화가 있으면 후보 |
| 스마트홈       | 플랫폼 lock-in과 반복 서비스가 있으면 후보 |
| 키즈·유아용품    | 출생아 감소를 해외/프리미엄화로 상쇄해야 후보   |

## 반례

| 반례                | 왜 위험한가  |
| ----------------- | ------- |
| 내수 가전 교체수요만 있는 기업 | 성장성 낮음  |
| 저출산 유아용품          | TAM 축소  |
| 스마트홈 테마만 있음       | 반복매출 없음 |
| 단일 제품 유행          | 재고 리스크  |

## 점수비중 v0.8

```text
EPS/FCF: 17
Structural Visibility: 13
Bottleneck/Pricing: 6
Market Mispricing: 12
Valuation Rerating: 10
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: birthrate / replacement_cycle / inventory
```

## 정규화 포인트

생활가전·유아용품은 Green 제한.
수출·프리미엄화·반복 서비스가 있어야 Stage 2 이상.

---

# 7. CONSUMER_REGULATED_PRODUCT

전자담배 / 마리화나 / 주정 / 규제형 소비재

## 핵심 구조

```text
규제 허용 / 반복소비
→ 브랜드·유통망
→ 그러나 규제 리스크가 항상 큼
```

## 성공 후보

| 케이스  | 판단                                 |
| ---- | ---------------------------------- |
| 전자담배 | 반복소비·유통망·규제 안정성 필요                 |
| 주정   | 식품·의약·소독 수요와 규제, 원가 확인             |
| 마리화나 | 국내는 규제 리스크가 너무 크므로 대부분 event/watch |

## 반례

| 반례           | 왜 위험한가             |
| ------------ | ------------------ |
| 규제 강화        | 매출 직격              |
| 허가 기대만 있는 테마 | 실적 없음              |
| 사회적 반발       | valuation discount |
| 일회성 수요       | 반복성 부족             |

## 점수비중 v0.8

```text
EPS/FCF: 18
Structural Visibility: 14
Bottleneck/Pricing: 8
Market Mispricing: 12
Valuation Rerating: 10
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: regulation / social_backlash / legal
```

## 정규화 포인트

규제형 소비재는 Watch 중심. 반복소비가 있어도 규제 리스크가 크면 Green 제한.

---

# 8. 주요 archetype 재보정: MEMORY_HBM vs AI_DATA_CENTER_INFRA

## MEMORY_HBM_CAPACITY

기존보다 4B 감시를 더 강하게 해야 해.
SK하이닉스는 HBM과 AI 서버 수요로 구조적 리레이팅이 가능한 대표 사례지만, 이미 주가가 2025년 274%, 2026년 200% 이상 급등했다는 보도처럼 4B-watch의 기준이기도 하다. ([Reuters][5])

```text
점수비중 v0.8:
EPS/FCF: 24
Structural Visibility: 21
Bottleneck/Pricing: 19
Market Mispricing: 15
Valuation Rerating: 12
Risk Penalty: cycle / capex_reversal / crowding
```

## AI_DATA_CENTER_INFRASTRUCTURE

SK/AWS 데이터센터와 OpenAI의 한국 반도체·데이터센터 협력 같은 사례를 보면 AI 인프라는 전력·냉각·메모리·서버·전력망이 연결되는 별도 대형 archetype으로 봐야 한다. 다만 CAPEX 기대만으로 모든 관련주를 Green으로 올리면 안 된다. 실제 수주·납품·EPS revision이 필요하다. ([Reuters][2])

```text
점수비중 v0.8:
EPS/FCF: 22
Structural Visibility: 23
Bottleneck/Pricing: 20
Market Mispricing: 14
Valuation Rerating: 12
Risk Penalty: AI_capex_cut / project_delay
```

---

# 9. Round 17 cases_v05 추가 후보

```text
DIGITAL_HEALTHCARE_AI:
- lunit_mammography_ai_candidate
- medical_ai_no_reimbursement_counterexample
- ai_medical_overtrust_risk_counterexample
- hospital_workflow_ai_revenue_candidate

TELECOM_5G_6G_AI_NETWORK:
- sk_aws_ulsan_ai_datacenter_candidate
- 5g_capex_peak_counterexample
- 6g_policy_no_revenue_watch
- telecom_security_breach_4c

MEDIA_AD_CONTENT_CYCLE:
- hybe_global_tour_ip_monetization_candidate
- kpop_single_artist_contract_risk_counterexample
- advertising_cycle_recovery_candidate
- broadcast_ad_decline_counterexample

SERVICE_KIOSK_AUTOMATION:
- kiosk_recurring_maintenance_candidate
- contact_center_ai_subscription_candidate
- kiosk_hardware_oneoff_counterexample
- unmanned_store_no_margin_counterexample

SMART_FARM_AGRI_TECH:
- smart_farm_export_order_candidate
- agri_machinery_overseas_sales_candidate
- soybean_feed_cost_pressure_counterexample
- weather_event_agri_theme_counterexample

HOME_LIVING_APPLIANCE:
- premium_home_appliance_export_candidate
- smart_home_subscription_candidate
- low_birthrate_kids_goods_counterexample
- single_product_home_appliance_counterexample

CONSUMER_REGULATED_PRODUCT:
- e_cigarette_repeat_consumption_candidate
- cannabis_regulation_event_watch
- regulation_crackdown_4c
- alcohol_tobacco_social_discount_counterexample
```

---

# 10. Round 17 점수비중 요약

| Archetype                  | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | 성격                 |
| -------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------------------ |
| DIGITAL_HEALTHCARE_AI      |      18 |         17 |          8 |         13 |        12 | 허가·수가·병원도입 필요      |
| TELECOM_5G_6G_AI_NETWORK   |      16 |         18 |         10 |         12 |        10 | CAPEX·보안·저성장 리스크   |
| MEDIA_AD_CONTENT_CYCLE     |      18 |         16 |          6 |         14 |        12 | IP 반복성 vs hit risk |
| SERVICE_KIOSK_AUTOMATION   |      18 |         17 |          7 |         13 |        11 | 반복 유지보수/SaaS 필요    |
| SMART_FARM_AGRI_TECH       |      18 |         14 |         12 |          9 |         9 | 정책·원자재 cycle       |
| HOME_LIVING_APPLIANCE      |      17 |         13 |          6 |         12 |        10 | 수출·프리미엄화 필요        |
| CONSUMER_REGULATED_PRODUCT |      18 |         14 |          8 |         12 |        10 | 규제 리스크 큼           |
| MEMORY_HBM_CAPACITY        |      24 |         21 |         19 |         15 |        12 | Green 가능 + 4B 감시   |
| AI_DATA_CENTER_INFRA       |      22 |         23 |         20 |         14 |        12 | Green 가능, 수주 확인 필요 |

---

# 11. 이번 라운드 정규화 교정

이번에 추가된 핵심 교정은 이거야.

```text
1. 의료AI는 Green 가능성이 있지만, 허가·수가·병원 도입·반복매출 없으면 Watch.
2. 5G/6G/통신망은 CAPEX 테마만으로 Green 금지. AI 데이터센터 매출이 붙어야 점수 상승.
3. 미디어/엔터는 글로벌 IP가 매출화되면 후보지만, 단일 아티스트·신작 의존은 Red flag.
4. 키오스크/자동화는 장비 판매가 아니라 반복 유지보수·SaaS·결제수익이 핵심.
5. 스마트팜/농기계는 정책보다 실제 수주·해외매출이 핵심.
6. 생활가전/키즈는 내수 교체수요·저출산 리스크 때문에 Green 제한.
7. 규제형 소비재는 반복소비가 있어도 규제 리스크 때문에 Watch 중심.
8. HBM은 Green 가능성이 강하지만, 주가 폭등 후에는 4B-watch가 필수.
9. AI 데이터센터 인프라는 별도 Green 가능 archetype이지만, 실제 수주와 EPS revision 없으면 theme overheat.
```

---

# 12. 현재까지 진행상태 판단

지금은 정말 많이 채워졌다.
다만 아직 완성은 아니다.

```text
테마 흡수:
거의 됨.

얇은 archetype:
상당수 보강됨.

점수비중:
v0.8까지 가설화됨.

남은 핵심:
price-path validation.
```

결국 다음 단계에서 확인해야 하는 건 이것이다.

```text
점수 높게 준 성공 후보가 실제로 Stage 2/3 이후 주가 리레이팅됐는가?
반례로 둔 케이스는 실제로 4B/4C 또는 no-rerating이었는가?
```

이 검증 전까지 production scoring은 금지.
하지만 A를 계속 진행하면서 성공/반례를 더 많이 쌓는 방향은 맞다.

[1]: https://arxiv.org/abs/2503.13581?utm_source=chatgpt.com "Subgroup Performance of a Commercial Digital Breast Tomosynthesis Model for Breast Cancer Detection"
[2]: https://www.reuters.com/business/retail-consumer/south-korea-says-sk-amazon-invest-5-bln-countrys-biggest-data-centre-2025-06-20/?utm_source=chatgpt.com "South Korea says SK and Amazon to invest $5 billion in country's biggest data centre"
[3]: https://arxiv.org/abs/2509.06700?utm_source=chatgpt.com "Sovereign AI for 6G: Towards the Future of AI-Native Networks"
[4]: https://en.wikipedia.org/wiki/Ready_to_Be_World_Tour?utm_source=chatgpt.com "Ready to Be World Tour"
[5]: https://www.reuters.com/world/asia-pacific/ai-boom-puts-sk-hynix-cusp-1-trillion-market-value-2026-05-14/?utm_source=chatgpt.com "AI boom puts SK Hynix on cusp of $1 trillion market value"
