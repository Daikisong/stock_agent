좋아. 이번 라운드는 **Round 9: 테마 태그 전체 흡수 + 신규 세부 archetype 케이스 보강 + 점수-주가 정합성 기준 확장**으로 볼게.

현재 레포 상태를 기준으로 하면 아직 28A는 “전체 시장 완성판”이 아니야. taxonomy 산출물은 `full_live_taxonomy_built: False`, `fixture_only: True`, mapped symbols 13개, archetypes used 8개로 되어 있고, case coverage도 25개 archetype 중 2+2, 즉 성공 2개 + 반례 2개를 만족한 항목이 0개야.
그래서 우리가 지금 하는 작업은 production scoring 적용이 아니라, **전 테마를 품을 수 있는 case/archetype 기반 설계**를 계속 채우는 거야.

핵심 정신은 그대로야.

> **산업 구조 변화 → EPS/FCF 체급 변화 → 시장의 과거 프레임 오해 → 밸류에이션 리레이팅 → 논리 훼손 전까지 보유.**

서생원식 에이전트는 “테마를 따라가는 봇”이 아니라, **몇 년짜리 이익 체급 변화와 밸류에이션 프레임 변화를 먼저 잡는 도구**여야 해.

---

# 1. 이번 라운드 결론

네가 준 테마 리스트를 보면 기존 구조는 더 쪼개야 해.

지금까지는 대략:

```text
10~12개 대섹터
32개 안팎 archetype
```

이었는데, 실제 테마를 흡수하려면 이렇게 가는 게 맞아.

```text
12개 대섹터
→ 60~70개 archetype/sub-archetype
→ 200개+ raw theme tag
→ 각 archetype별 성공/반례 case
→ price-path validation
→ 점수비중 shadow 적용
```

여기서 중요한 건:

```text
테마명 자체는 점수를 주는 근거가 아니다.
테마명은 검색/분류/쿼리 생성용 tag다.
점수는 evidence와 archetype 구조에서 나온다.
```

예를 들면:

```text
초전도체 / 맥신 / 그래핀
→ SPECULATIVE_SCIENCE_THEME
→ 실제 매출/계약/상용화 없으면 Green 금지

스테이블코인 / STO / 토스 관련주
→ DIGITAL_ASSET_TOKENIZATION or PAYMENT_FINTECH_INFRA
→ 규제 승인 + 실제 거래량 + 수익모델 없으면 Green 금지

편의점
→ RETAIL_CONVENIENCE_OFFLINE
→ 점포효율, PB, OPM, same-store sales 없으면 Green 금지

손해보험
→ INSURANCE_UNDERWRITING_CYCLE
→ 손해율, CSM, ROE, 자본비율, 환원정책 확인

HBM
→ MEMORY_HBM_CAPACITY
→ HBM 수요 + 공급제약 + 장기계약/선수금 + EPS revision 필요
```

---

# 2. 이번에 추가 확정할 세부 Archetype

아래 archetype은 새로 확정하거나 더 독립시켜야 해.

```text
1. RETAIL_CONVENIENCE_OFFLINE
2. ECOMMERCE_FRESH_LOGISTICS
3. INSURANCE_UNDERWRITING_CYCLE
4. PAYMENT_FINTECH_INFRA
5. DIGITAL_ASSET_TOKENIZATION
6. BEAUTY_OEM_ODM_SUPPLYCHAIN
7. AGRI_LIVESTOCK_FOOD_COMMODITY
8. BUILDING_MATERIALS_CYCLE
9. RENEWABLE_ENERGY_POLICY
10. HYDROGEN_FUEL_CELL_INFRA
11. SOLAR_TARIFF_SUPPLYCHAIN
12. TIRE_AUTO_COMPONENT_SPREAD
13. EVENT_DISEASE_PEST_DEMAND
14. SPECULATIVE_SCIENCE_THEME
15. WASTE_RECYCLING_ENVIRONMENT
16. MEDIA_AD_CONTENT_CYCLE
17. CLOUD_AI_SOFTWARE_INFRA
18. SECURITY_IDENTITY_DEEPFAKE
```

이걸 넣으면 네가 준 테마 중 많은 부분이 더 자연스럽게 흡수돼.

---

# 3. 신규 보강 1: 편의점 / 홈쇼핑 / 음식료 유통 / 콜드체인

## Archetype

```text
RETAIL_CONVENIENCE_OFFLINE
ECOMMERCE_FRESH_LOGISTICS
```

## 포함 테마

```text
편의점
홈쇼핑
음식료-유통
마켓컬리·오아시스 관련주
콜드체인
키즈/유아용품 일부
밥솥/생활소비 일부
```

## 구조

```text
점포망 / 물류망 / PB상품
→ same-store sales
→ 객단가 / 고마진 mix
→ 비용 레버리지
→ OPM/FCF 개선
```

## 성공 후보

| 케이스          | 분류                                 | 봐야 할 것                  |
| ------------ | ---------------------------------- | ----------------------- |
| BGF리테일 / CU  | success_candidate                  | 점포효율, PB상품, 해외점포, OPM   |
| GS리테일 / GS25 | success_candidate                  | 편의점 경쟁강도, PB, 점포 수익성    |
| 컬리/오아시스 관련주  | success_candidate 또는 event_premium | 상장/지분 이벤트와 실제 물류·수익성 분리 |
| 콜드체인 물류      | success_candidate                  | 실제 물류 수요와 마진 확인         |

## 반례

| 반례                     | 이유                          |
| ---------------------- | --------------------------- |
| 대형마트/홈쇼핑 구조 경쟁 심화      | 온라인 경쟁, 수수료 압박, OPM 저하      |
| 중국 직구/저가 e-commerce 압박 | 가격경쟁으로 유통마진 훼손              |
| 상장 기대만 있는 관련주          | event premium일 뿐 EPS/FCF 없음 |
| 트래픽만 있고 적자 지속          | Stage 1 이상 제한               |

## Stage 기준

```text
Stage 1:
- same-store sales 회복
- 점포 확대
- PB/고마진 상품 뉴스
- 상장/지분 이벤트

Stage 2:
- OPM 개선
- 재고 정상화
- 비용 레버리지
- FY1/FY2 OP 상향

Stage 3:
- 점포 효율 구조 변화
- 물류/콜드체인 반복매출
- FCF 개선
- 시장이 내수 저성장 유통 프레임으로 평가

4B:
- 소비 회복 모두 반영
- 점포 성장 한계
- 임대료/인건비 압박

4C:
- 재고 증가
- 온라인 경쟁 심화
- 소비 둔화
- 물류비 상승
```

## 점수비중 초안

```text
EPS/FCF: 18
Structural Visibility: 16
Bottleneck/Pricing: 5
Market Mispricing: 14
Valuation: 14
Capital Allocation: 3
Information Confidence: 5
```

## 점수-주가 검증

```text
성공:
OPM/FCF 개선이 2~4분기 이상 유지되고 주가가 따라감

반례:
상장 기대, 소비 회복 뉴스, 점포 수 증가만으로 주가가 올랐지만
OPM/FCF가 안 따라오면 false_positive_score
```

---

# 4. 신규 보강 2: 손해보험 / 생명보험 / 금융지주 / 고배당

## Archetype

```text
INSURANCE_UNDERWRITING_CYCLE
FINANCIAL_SPREAD_BALANCE_SHEET
VALUE_UP_SHAREHOLDER_RETURN
```

## 포함 테마

```text
손해보험
생명보험
은행
금융지주회사
증권사
벤처캐피탈
고배당주
밸류업 지수 편입
부동산 자산 보유
```

## 구조

```text
ROE / CSM / 손해율 / 자본비율 / 주주환원
→ PBR-ROE 프레임 변화
→ Korea discount 해소
```

손해보험은 은행과 다르게 **손해율, CSM, 위험손해율, 자본비율, 배당/자사주**가 핵심이야. Samsung Fire & Marine은 2024년 이익 성장과 CSM 증가 전망, 강한 지급여력·손실흡수 능력이 언급된 바 있어서 보험 archetype의 좋은 후보가 돼. ([월스트리트저널][1])

SK스퀘어처럼 지주/자본배분 케이스는 보유자산 가치와 자사주 소각이 핵심이야. SK스퀘어는 SK하이닉스 지분 가치 대비 저평가, 자사주 매입·소각 계획, Value-Up 프로그램과 연결된 사례로 볼 수 있어. ([Reuters][2])

## 성공 후보

| 케이스            | 분류                | 봐야 할 것                          |
| -------------- | ----------------- | ------------------------------- |
| 삼성화재 / DB손보    | success_candidate | 손해율, CSM, ROE, 자본비율, 환원         |
| KB금융 / 신한 / 하나 | success_candidate | ROE, CET1, PBR, 주주환원            |
| 메리츠금융          | success_candidate | 자본효율, 환원정책                      |
| SK스퀘어          | success_candidate | NAV discount, 자사주 소각, SK하이닉스 지분 |

## 반례

| 반례            | 이유                    |
| ------------- | --------------------- |
| 단순 저PBR 은행    | ROE/환원 없으면 value trap |
| PF/충당금 리스크 금융 | credit cost 상승 시 4C   |
| 자본비율 낮은 보험    | 주주환원 제한               |
| 자사주 매입 후 미소각  | value-up 실패           |

## Stage 기준

```text
Stage 1:
- value-up 공시
- 자사주/배당
- 저PBR
- 손해율 개선 뉴스

Stage 2:
- ROE 개선
- CET1/K-ICS 안정
- CSM 증가
- 충당금 안정
- 환원정책 실행

Stage 3:
- PBR-ROE 프레임 변화
- 반복 환원
- credit/underwriting risk 낮음
- 시장이 아직 value trap으로 평가

4B:
- PBR이 ROE 대비 정상화
- 모두가 value-up 성공주로 인정

4C:
- credit cost 증가
- 손해율 악화
- 자본비율 악화
- 환원정책 후퇴
```

## 점수비중 초안

```text
EPS/FCF: 15
Structural Visibility: 20
Bottleneck/Pricing: 5
Market Mispricing: 15
Valuation: 25
Capital Allocation: 10
Information Confidence: 5
```

## 점수-주가 검증

```text
성공:
ROE/CSM/CET1/환원정책이 실제로 개선되고 PBR 리레이팅이 발생

반례:
저PBR만 보고 점수 높게 줬는데 ROE/환원 없이 주가가 못 감
```

---

# 5. 신규 보강 3: 스테이블코인 / STO / 결제서비스 / 토스

## Archetype

```text
PAYMENT_FINTECH_INFRA
DIGITAL_ASSET_TOKENIZATION
```

## 포함 테마

```text
스테이블코인
STO
디지털자산-블록체인
결제서비스
토스 관련주
지역화폐
신용정보
NFT
```

## 구조

```text
규제 승인 / 발행 라이선스
→ 거래량 / 결제망 채택
→ 수수료 / 예치금 / spread 수익
→ 반복 금융 인프라 매출
```

Toss는 호주 진출과 원화 스테이블코인 발행 의지를 밝힌 사례야. 다만 이는 아직 규제 승인과 사업모델 확인이 필요하기 때문에 Stage 1~2 후보이지 바로 Green은 아니야. ([Reuters][3])
스테이블코인은 결제에서 잠재력이 있지만, open-loop retail payments에서는 소비자 보호와 사용성/분쟁처리 문제가 있고, closed-loop나 cross-border 같은 고마찰 영역에서 비교우위가 더 크다는 연구도 있어. ([arXiv][4])

## 성공 후보

| 케이스              | 분류                | 봐야 할 것                     |
| ---------------- | ----------------- | -------------------------- |
| Toss / 원화 스테이블코인 | success_candidate | 규제 승인, 실제 발행, 거래량, 수수료 모델  |
| 결제 PG사           | success_candidate | 거래액, take rate, 비용구조       |
| STO 플랫폼          | success_candidate | 토큰증권 법제화, 발행 실적, 수탁/중개 수수료 |
| 신용정보/데이터 기업      | success_candidate | 반복 데이터 매출, 금융사 채택          |

## 반례

| 반례                 | 이유                     |
| ------------------ | ---------------------- |
| 코인 테마만 있는 기업       | 실질 매출 없음               |
| STO 법제화 기대만 있는 관련주 | 발행 실적과 수익모델 없음         |
| 스테이블코인 규제 지연       | 4C 또는 Stage 1 제한       |
| NFT 테마             | 대부분 theme_overheat로 분류 |

## Stage 기준

```text
Stage 1:
- 법안/규제 뉴스
- 사업 진출 발표
- 거래소/은행/핀테크 제휴

Stage 2:
- 실제 라이선스/발행/거래량
- 수수료 모델
- 금융기관 채택
- 반복 매출

Stage 3:
- 결제/수탁/정산 인프라로 고착
- 규제 리스크 낮음
- FCF/OPM 개선
- 시장이 아직 테마주로 평가

4B:
- 규제 기대가 과열
- 관련주 동반 급등
- 실제 실적 대비 valuation 과다

4C:
- 규제 지연/불허
- 보안사고
- 거래량 부진
- 수익모델 부재
```

## 점수비중 초안

```text
EPS/FCF: 16
Structural Visibility: 18
Bottleneck/Pricing: 8
Market Mispricing: 16
Valuation: 12
Risk Penalty: regulation / security / adoption
```

## 점수-주가 검증

```text
성공:
규제 승인 + 실제 거래량 + 수익모델 + 주가 리레이팅

반례:
법안 기대나 테마만으로 주가가 오르고 실적이 없으면 theme_overheat
```

---

# 6. 신규 보강 4: 태양광 / 풍력 / 탄소배출권 / 수소

## Archetype

```text
RENEWABLE_ENERGY_POLICY
SOLAR_TARIFF_SUPPLYCHAIN
HYDROGEN_FUEL_CELL_INFRA
```

## 포함 테마

```text
태양광
풍력
탄소배출권
수소차 연료전지
수소차 인프라
수소차 기타부품
LNG 발전유통
전력망
스마트그리드
```

## 구조

```text
정책 / 보조금 / 전력수요 / CAPEX
→ 실제 수주·설비·가동률
→ 매출·OP 전환
```

수소는 정책 테마성이 강하지만, Hyundai가 울산에 9,300억원 규모 수소연료전지 생산시설을 착공하고 2027년 완공 계획을 밝힌 사례처럼 실제 CAPEX와 생산시설이 있으면 Stage 1~2 신호가 될 수 있어. ([Reuters][5])
반대로 태양광은 정책·관세·공급망 리스크가 크다. Qcells는 미국 세관의 부품 억류로 조지아 공장 노동시간/임금 축소와 계약직 해고를 겪었고, 이는 solar supply chain 4C 반례로 적합해. ([AP News][6])

## 성공 후보

| 케이스                              | 분류                | 봐야 할 것                |
| -------------------------------- | ----------------- | --------------------- |
| Hyundai hydrogen fuel cell plant | success_candidate | 실제 CAPEX, 생산능력, 고객/수요 |
| Doosan Fuel Cell / 연료전지          | success_candidate | 수주, 가동률, 반복 서비스       |
| 풍력 기자재                           | success_candidate | 터빈/타워 수주, 정책 지원       |
| ESS/LFP 전환                       | success_candidate | EV 둔화 보완 수요           |

## 반례

| 반례           | 이유          |
| ------------ | ----------- |
| 태양광 관세/부품 억류 | 공급망 리스크     |
| 보조금 의존 사업    | 정책 바뀌면 4C   |
| 수소 테마만 있는 기업 | 실제 생산/매출 없음 |
| 풍력 프로젝트 지연   | 인허가/원가 리스크  |

## Stage 기준

```text
Stage 1:
- 정책/보조금
- 수소/태양광/풍력 CAPEX
- 공장 착공
- 수주 뉴스

Stage 2:
- 실제 계약/가동률
- OP/EPS 상향
- 보조금과 수익성 확인

Stage 3:
- 다년 수요
- 고객사/정부 수요 고정
- 정책 리스크 낮음
- 원가 경쟁력 확보

4B:
- 정책 기대 과열
- 보조금 수혜 선반영
- capex 부담 부각

4C:
- 보조금 축소
- 관세/통관/공급망 문제
- 프로젝트 지연
- 가동률 하락
```

## 점수비중 초안

```text
EPS/FCF: 18
Structural Visibility: 18
Bottleneck/Pricing: 12
Market Mispricing: 12
Valuation: 10
Risk Penalty: policy / subsidy / supply chain
```

---

# 7. 신규 보강 5: 2차전지 소재 / 폐배터리 / ESS

## Archetype

```text
BATTERY_MATERIALS_CAPEX_OVERHEAT
BATTERY_EQUIPMENT_PARTS
BATTERY_RECYCLING_ESS_SHIFT
```

## 포함 테마

```text
2차전지 소재
2차전지 부품
2차전지 공정장비
2차전지 생산-판매
폐배터리
전고체 배터리
리튬
전기차 화재
전기차 인프라
ESS
```

## 구조

```text
EV 성장 기대
→ 소재/부품/CAPA 투자
→ 하지만 EV 수요 둔화, 광물가격, CAPA 과잉, 보조금 변화에 민감
```

LG에너지솔루션은 2025년 EV 배터리 수요 둔화와 미국 관세·정책 불확실성을 경고했고, ESS 생산 확대를 통해 EV 둔화를 보완하겠다고 했어. 이는 battery archetype에서 **EV 소재 Green 제한 + ESS 전환 watch**의 좋은 근거야. ([Reuters][7])
SK On은 장기간 적자와 EV 수요 부진으로 “emergency management”를 선언했다는 FT 보도가 있어, CAPEX overheat 반례에 가깝다. ([Financial Times][8])

## 성공 후보

| 케이스        | 분류                | 봐야 할 것              |
| ---------- | ----------------- | ------------------- |
| ESS 전환 배터리 | success_candidate | ESS 수요, LFP, 가동률 개선 |
| 폐배터리       | success_candidate | 실제 회수량, 금속가격, 마진    |
| 2차전지 공정장비  | success_candidate | 수주/납품/고객사 CAPEX     |
| 전고체 배터리    | watch_only        | 상용화 전 Green 제한      |

## 반례

| 반례             | 이유                 |
| -------------- | ------------------ |
| 에코프로비엠/에코프로 과열 | valuation/crowding |
| EV 수요 둔화       | 매출/가동률 훼손          |
| 광물가격 하락        | 판가/마진 훼손           |
| CAPA 과잉        | FCF 악화             |

## Stage 기준

```text
Stage 1:
- 장기계약
- CAPA 증설
- EV/ESS 수요 뉴스

Stage 2:
- 가격/마진 동반 개선
- customer contract quality
- FCF 훼손 없는 CAPEX
- ESS 전환 실적화

Stage 3:
- 제한적
- 장기계약 + 가격전가 + 수요지속 + valuation 여지

4B:
- price runup
- crowding
- PER/PBR 과열
- revision slowdown

4C:
- EV 수요 둔화
- 광물가격 하락
- CAPA 과잉
- margin compression
```

## 점수비중 초안

```text
EPS/FCF: 20
Structural Visibility: 16
Bottleneck/Pricing: 14
Market Mispricing: 10
Valuation: 10
Risk Penalty: very high
```

---

# 8. 신규 보강 6: 타이어 / 자동차 부품 / 경량화

## Archetype

```text
TIRE_AUTO_COMPONENT_SPREAD
AUTO_MOBILITY_COMPONENTS
```

## 포함 테마

```text
타이어
현대-기아차 부품주
자동차 연비개선 경량화
전기차 부품
자율주행
카메라
MLCC 일부
스마트폰 부품 일부
```

## 구조

```text
완성차 판매 / OE·RE 타이어 수요
→ ASP와 원재료 spread
→ OPM 개선
→ 고객사 다변화
```

Kumho Tire는 2025년 광주 공장 화재로 주가가 8% 하락했고, 해당 공장은 글로벌 생산능력의 약 20%를 차지한다고 보도됐어. 이건 타이어/부품 archetype의 4C 반례, 즉 **생산중단·고객사 공급차질·공장 리스크**로 좋다. ([Reuters][9])
Hankook Tire는 원재료 가격 상승으로 마진 압박 가능성이 언급된 바 있어, 타이어는 ASP보다 원재료 spread가 중요하다는 반례 포인트가 된다. ([월스트리트저널][10])

## 성공 후보

| 케이스          | 분류                | 봐야 할 것                     |
| ------------ | ----------------- | -------------------------- |
| Hankook Tire | success_candidate | RE/OE mix, ASP, 원재료 spread |
| 현대모비스/HL만도   | success_candidate | ADAS/전장, 고객 다변화            |
| 경량화 부품       | success_candidate | 실제 채택률, 마진                 |

## 반례

| 반례                      | 이유                          |
| ----------------------- | --------------------------- |
| Kumho Tire factory fire | 생산차질 4C                     |
| 원재료 상승 타이어              | margin compression          |
| EV 수요 둔화 부품             | 고객사 CAPEX/판매 둔화             |
| 단일 고객 부품주               | customer concentration risk |

## Stage 기준

```text
Stage 1:
- 완성차 판매 호조
- ASP 상승
- 고객사 수주

Stage 2:
- OPM 개선
- 원재료 안정
- 고객 다변화
- FY1/FY2 OP 상향

Stage 3:
- 고마진 mix 전환
- 전장/ADAS/EV exposure
- 반복 납품 visibility
- valuation discount 해소

4B:
- peak margin
- 완성차 cycle peak
- valuation 정상화

4C:
- 원재료 급등
- 생산중단
- 고객사 판매 둔화
- 리콜/품질비용
```

## 점수비중 초안

```text
EPS/FCF: 20
Structural Visibility: 18
Bottleneck/Pricing: 10
Market Mispricing: 14
Valuation: 14
Risk Penalty: raw materials / customer concentration
```

---

# 9. 신규 보강 7: 화장품 OEM·ODM / 원재료·부자재

## Archetype

```text
BEAUTY_OEM_ODM_SUPPLYCHAIN
K_BEAUTY_EXPORT_DISTRIBUTION
```

## 포함 테마

```text
화장품 OEM-ODM
화장품 원재료 및 부자재
화장품 브랜드
K뷰티
```

## 구조

```text
K뷰티 브랜드 수요
→ ODM/OEM 주문 증가
→ 고객사 다변화
→ OPM/ROE 개선
```

K뷰티는 2024년 한국이 미국 화장품 수출에서 프랑스를 앞섰고, 미국 e-commerce와 오프라인 채널 확장이 중요하다는 Reuters 보도가 있어. ([Reuters][11])
APR/Medicube처럼 디바이스+브랜드가 viral e-commerce에서 오프라인 유통으로 확장하는 사례는 성공 후보이지만, tariff와 경쟁 심화는 반례 신호야. ([Financial Times][12])

## 성공 후보

| 케이스            | 분류                | 봐야 할 것                       |
| -------------- | ----------------- | ---------------------------- |
| 코스맥스 / 한국콜마    | success_candidate | 글로벌 브랜드 고객, ODM 수주, OPM      |
| 실리콘투           | success_candidate | 글로벌 유통, 브랜드 다변화, 반복 주문       |
| APR / Medicube | success_candidate | 디바이스, TikTok, 오프라인 채널, 해외 매출 |
| 원재료/부자재 업체     | success_candidate | 고객사 다변화, 반복 수요               |

## 반례

| 반례               | 이유            |
| ---------------- | ------------- |
| 중국 의존 화장품        | 중국 채널 둔화      |
| viral-only 브랜드   | 반복 주문 없음      |
| channel stuffing | 재고/매출채권 악화    |
| tariff/규제        | 미국 관세, 인증 리스크 |

## Stage 기준

```text
Stage 1:
- 미국/일본 수출 증가
- K뷰티 viral
- ODM 주문 증가

Stage 2:
- FY1/FY2 OP/EPS 상향
- OPM/ROE 개선
- 고객사 다변화
- 채널 확대

Stage 3:
- 반복 주문
- 오프라인/대형 리테일 진입
- 재고/채권 문제 없음
- 중국 의존도 하락

4B:
- K뷰티 overcrowding
- 목표가 과열
- 경쟁 브랜드 난립

4C:
- sell-through 둔화
- 재고 증가
- 매출채권 악화
- tariff/regulation impact
```

## 점수비중 초안

```text
EPS/FCF: 22
Structural Visibility: 23
Bottleneck/Pricing: 12
Market Mispricing: 16
Valuation: 13
Risk Penalty: inventory / receivables / China dependency
```

---

# 10. 신규 보강 8: 진단 / 전염병 / 엠폭스 / 빈대 / 황사마스크

## Archetype

```text
DIAGNOSTICS_INFECTIOUS_DISEASE
EVENT_DISEASE_PEST_DEMAND
ONE_OFF_EVENT_DEMAND
```

## 포함 테마

```text
엠폭스
코로나19 제약
전염병 진단
동물백신 방역
빈대퇴치
황사마스크
황사미세먼지 공기정화
```

## 구조

```text
이벤트성 수요
→ 단기 EPS 폭발 가능
→ 정상화 후 급락 위험
```

씨젠은 팬데믹 진단키트 수요로 이익이 폭발했지만, 구조적 반복수요가 아니었기 때문에 one-off 반례로 넣어야 해.
Stable EPS/FCF가 아니라 이벤트 수요면 Stage 3-Green이 아니라 Stage 3-Red/Yellow 또는 4B-watch가 맞다.

## 성공 후보

| 케이스       | 분류                    | 봐야 할 것                     |
| --------- | --------------------- | -------------------------- |
| 반복 진단 플랫폼 | success_candidate 제한적 | 팬데믹 이후에도 반복 검사·소모품 수요가 있는지 |
| 동물백신/방역   | watch_only            | 실제 수주/매출 반복성 확인            |
| 공기정화/마스크  | one_off               | 황사/전염병 이벤트성 수요             |

## 반례

| 반례           | 이유                      |
| ------------ | ----------------------- |
| 씨젠 2020      | one-off pandemic demand |
| 마스크/방역 단기 테마 | 수요 정상화                  |
| 엠폭스/빈대 테마    | 단기 이벤트 가능성              |
| 코로나 치료제 기대   | 실적화 전 테마                |

## Stage 기준

```text
Stage 1:
- 감염병/재난 뉴스
- 진단키트/방역 수요 급증

Stage 2:
- 매출/OP 폭발
- 공급부족
- 단기 수요 확인

Stage 3:
- Green 금지에 가깝다
- 반복 플랫폼/소모품 evidence가 있을 때만 Yellow/Watch

4B:
- 모두가 구조 성장으로 착각
- valuation overheat

4C:
- 수요 정상화
- guidance down
- 재고 증가
```

## 점수비중 초안

```text
EPS/FCF: 20
Structural Visibility: 5
Bottleneck/Pricing: 5
Mispricing: 5
Valuation: 5
One-off risk penalty: very high
```

---

# 11. 신규 보강 9: 초전도체 / 맥신 / 그래핀 / 양자 / 스페이스X

## Archetype

```text
SPECULATIVE_SCIENCE_THEME
THEME_VALUATION_OVERHEAT
```

## 포함 테마

```text
초전도체
맥신
그래핀
양자 기술
스페이스X
페라이트
뉴로모픽 반도체 일부
퓨리오사AI 관련주 중 실체 불명확한 경우
```

## 구조

```text
과학/기술 narrative
→ 주가 급등
→ 실제 매출/상용화/계약 검증 전에는 EPS/FCF 없음
```

## 성공 후보

매우 제한적이야.

```text
실제 양자/우주/AI칩 매출 계약
정부/대기업 장기계약
제품 상용화와 FY1/FY2 매출
```

이 없는 경우 대부분 Stage 1 또는 Theme Overheat.

## 반례

```text
초전도체 테마 급등
맥신/그래핀 논문 테마
스페이스X 지분/납품 불명확 관련주
양자 기술 뉴스만 있는 종목
```

## Stage 기준

```text
Stage 1:
- 논문/테마/정책 뉴스
- 거래대금 급증

Stage 2:
- 실제 계약/매출/상용화가 있을 때만

Stage 3:
- 매우 제한적
- EPS/FCF와 반복 매출 확인 필요

4B:
- price-only rally
- 테마 종목 동반 급등

4C:
- 검증 실패
- 매출화 실패
- 관련성 부인
```

## 점수비중 초안

```text
EPS/FCF: 5~10
Structural Visibility: 5
Bottleneck/Pricing: 5
Mispricing: 5
Valuation: 5
Theme penalty: extreme
```

---

# 12. 신규 보강 10: 농축산 / 사료 / 대두 / 참치

## Archetype

```text
AGRI_LIVESTOCK_FOOD_COMMODITY
FOOD_AGRI_LIVESTOCK_CYCLE
```

## 포함 테마

```text
양돈주
육계주
배합사료
대두
농업 종자비료농약
참치 원양어업
스마트팜
농기계
```

## 구조

```text
곡물/사료/육류/어가 가격
→ 원가 또는 판가
→ 단기 OP 변화
→ 대부분 사이클
```

## 성공 후보

| 케이스      | 분류                    | 봐야 할 것               |
| -------- | --------------------- | -------------------- |
| 스마트팜/농기계 | success_candidate     | 실제 수주, 해외 확장, 반복 서비스 |
| 원양어업     | cyclical_success      | 참치 가격, 어획량, 유가, 환율   |
| 종자/농약/비료 | success_candidate 제한적 | 가격전가, 정책, 수요 지속성     |

## 반례

| 반례          | 이유                       |
| ----------- | ------------------------ |
| 조류독감/질병 이벤트 | 단기 가격 급등                 |
| 사료 원가 상승    | 양돈/육계 margin compression |
| 대두 가격 급등    | 음식료/사료 원가 부담             |
| 날씨 이벤트      | 단기 테마                    |

## Stage 기준

```text
Stage 1:
- 질병/날씨/곡물가격 뉴스
- 식품가격 상승
- 사료/비료 가격 변화

Stage 2:
- 판가 전가
- OP/EPS 상향
- 원가 안정

Stage 3:
- 제한적
- 가격전가 구조와 반복 수요, FCF 확인 필요

4B:
- commodity price peak
- disease/event demand peak

4C:
- 가격 정상화
- 원가 재상승
- 재고 증가
```

## 점수비중 초안

```text
EPS/FCF: 18
Structural Visibility: 8~12
Bottleneck/Pricing: 14
Mispricing: 8
Valuation: 8
Cyclical risk cap: strong
```

---

# 13. 신규 보강 11: 건자재 / 시멘트 / 철근 / 가구 / 거푸집

## Archetype

```text
BUILDING_MATERIALS_CYCLE
CONSTRUCTION_REAL_ESTATE_CREDIT
```

## 포함 테마

```text
건자재
건자재-철근
건자재-시멘트레미콘콘크리트
건자재-가구
건자재-거푸집
제지/골판지 일부
```

## 구조

```text
건설착공 / 분양 / 원가 / 가격인상
→ 매출·마진 변화
→ PF/부동산 사이클에 매우 민감
```

## 성공 후보

```text
시멘트 가격 인상 + 출하량 안정
철근 spread 개선
인테리어/가구 B2B 수주 회복
```

## 반례

```text
PF 부실
착공 감소
미분양 증가
원가 상승
가격 인상 실패
```

## Stage 기준

```text
Stage 1:
- 건설 경기 회복
- 가격 인상
- 출하량 회복

Stage 2:
- OPM 개선
- 원가 안정
- 수요 회복

Stage 3:
- 제한적
- 구조적 공급 재편이나 가격협상력 필요

4B:
- 부동산 회복 기대 과열

4C:
- 착공 감소
- PF 부실
- 원가 상승
```

## 점수비중 초안

```text
EPS/FCF: 18
Structural Visibility: 10
Bottleneck/Pricing: 12
Mispricing: 10
Valuation: 8
Credit/cycle risk: high
```

---

# 14. Theme Tag → Archetype 매핑 원칙

이제 에이전트에 들어갈 `theme_tag_map.csv`는 이런 필드를 가져야 해.

```text
theme_tag
large_sector
primary_archetype
secondary_archetypes
green_policy
stage1_query_terms
must_have_evidence
red_flag_evidence
score_weight_profile
```

예:

```text
theme_tag: 초전도체
large_sector: 정책·지정학·재난·이벤트
primary_archetype: SPECULATIVE_SCIENCE_THEME
green_policy: green_restricted
must_have_evidence: commercial_contract, revenue_conversion, verified_product
red_flag_evidence: paper_only, relatedness_unclear, price_only_rally
```

```text
theme_tag: 편의점
large_sector: 소비재·유통·브랜드
primary_archetype: RETAIL_CONVENIENCE_OFFLINE
green_policy: green_allowed_if_strong
must_have_evidence: same_store_sales, opm_improvement, pb_mix, fcf_improvement
red_flag_evidence: rent_wage_pressure, traffic_only, inventory_build
```

```text
theme_tag: 스테이블코인
large_sector: 금융·자본배분·디지털금융
primary_archetype: DIGITAL_ASSET_TOKENIZATION
green_policy: watch_only_until_regulated_revenue
must_have_evidence: regulation_approval, issued_volume, fee_model, institutional_adoption
red_flag_evidence: law_delay, security_issue, no_revenue
```

---

# 15. 이번 라운드 결론

이번 확장에서 가장 중요한 변화는 이거야.

```text
1. 편의점/홈쇼핑/콜드체인 등 유통 테마를 Retail/E-commerce로 분리.
2. 손해보험/생명보험을 은행과 별도 underwriting cycle로 분리.
3. 스테이블코인/STO/결제서비스를 Digital Asset/Payment Infra로 분리.
4. 태양광/풍력/수소를 Renewable Policy와 Hydrogen Infra로 분리.
5. 2차전지는 소재/장비/ESS/폐배터리로 세분화.
6. 타이어/자동차 부품은 raw material spread와 고객사 리스크를 반영.
7. 화장품 OEM/ODM은 K뷰티 브랜드와 별도 supply-chain archetype으로 분리.
8. 엠폭스/빈대/전염병/황사마스크는 one-off/event demand로 분리.
9. 초전도체/맥신/그래핀/양자는 speculative science theme로 Green 제한.
10. 농축산/사료/대두/참치는 commodity food cycle로 분리.
11. 건자재는 건설 PF와 연결된 building materials cycle로 분리.
```

이제 네가 준 긴 테마 리스트는 대부분 아래 구조로 흡수 가능해.

```text
12개 대섹터
→ 60~70개 archetype/sub-archetype
→ theme tag map
→ case library
→ price-path validation
```

다음 라운드에서는 이걸 더 구체적으로 **`theme_tag_map.csv` 초안 + cases_v03 후보 리스트** 형태로 만들어줄 수 있어.

[1]: https://www.wsj.com/finance/investing/financial-services-roundup-market-talk-25c7667f?utm_source=chatgpt.com "Financial Services Roundup: Market Talk"
[2]: https://www.reuters.com/technology/artificial-intelligence/south-koreas-ai-chip-investor-announces-plan-share-buybacks-2024-11-21/?utm_source=chatgpt.com "South Korea's AI chip investor announces plan for share buybacks"
[3]: https://www.reuters.com/business/finance/south-korean-fintech-toss-plans-global-push-starting-australia-aims-issue-won-2025-09-09/?utm_source=chatgpt.com "South Korean fintech Toss plans global push starting in Australia, aims to issue won stablecoin"
[4]: https://arxiv.org/abs/2601.00196?utm_source=chatgpt.com "SoK: Stablecoins in Retail Payments"
[5]: https://www.reuters.com/world/asia-pacific/hyundai-motor-breaks-ground-680-million-hydrogen-fuel-cell-plant-south-korea-2025-10-30/?utm_source=chatgpt.com "Hyundai Motor breaks ground on $680 million hydrogen fuel cell plant in South Korea"
[6]: https://apnews.com/article/f49d0579e0584d689f1feec36ff16ad1?utm_source=chatgpt.com "South Korean solar firm cuts pay and hours for Georgia workers as US officials detain imports"
[7]: https://www.reuters.com/business/autos-transportation/lg-energy-solution-warns-slowing-ev-battery-demand-due-us-tariffs-policy-2025-07-25/?utm_source=chatgpt.com "LG Energy Solution warns of slowing EV battery demand due to U.S. tariffs, policy headwinds"
[8]: https://www.ft.com/content/5affede6-1f1d-458e-b4d0-e2e7e902dcca?utm_source=chatgpt.com "Battery maker SK On declares 'emergency' as EV sales disappoint"
[9]: https://www.reuters.com/markets/europe/kumho-tire-shares-skid-after-weekend-fire-disrupts-production-2025-05-19/?utm_source=chatgpt.com "Kumho Tire shares skid after weekend fire disrupts production"
[10]: https://www.wsj.com/world/asia/auto-transport-roundup-market-talk-3d2f792f?utm_source=chatgpt.com "Auto & Transport Roundup: Market Talk"
[11]: https://www.reuters.com/world/asia-pacific/korean-beauty-startups-bet-booming-us-demand-outlasts-tariff-pain-2025-06-05/?utm_source=chatgpt.com "Korean beauty startups bet booming US demand outlasts tariff pain"
[12]: https://www.ft.com/content/6a0f7e2c-f3b9-4eb6-961c-d69af28f7183?utm_source=chatgpt.com "Kardashian endorsement of skincare gadget creates K-beauty champion"
