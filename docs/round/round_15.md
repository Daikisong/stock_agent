좋아. 이번은 **Round 12: 누락 테마군을 더 흡수하고, 성공/반례를 점수비중에 연결하는 라운드**로 진행할게.

먼저 확실히 짚고 가면, 지금 우리가 하는 건 “테마명별 점수표”를 만드는 게 아니야. 서생원식 핵심은 여전히 **산업 구조 변화 → EPS/FCF 체급 변화 → 시장의 과거 프레임 오해 → 밸류에이션 리레이팅 → 논리 훼손 전까지 보유**야. 테마명은 검색과 분류를 돕는 꼬리표일 뿐이고, 점수는 실제 증거에서 나와야 한다.

---

# 1. 이번 라운드에서 더 채울 테마군

이번에는 기존에 어느 정도 다뤘지만 아직 얇았던 쪽을 더 보강할게.

```text
1. 폐기물처리 / 재활용 / 폐배터리 / 탈플라스틱
2. 정유 / 화학 / 철강 / 비철금속 스프레드
3. 편의점 / 이커머스 / 콜드체인 / 홈쇼핑
4. 손해보험 / 생명보험 / 증권 / VC / 신용정보
5. 스테이블코인 / STO / 결제서비스 / 토스
6. 수소 / 태양광 / 풍력 / 탄소배출권
7. 타이어 / 자동차 부품 / 전장 / 경량화
8. CDMO / 바이오시밀러 / 원료의약품
9. 보안 / 딥페이크 / 생체인식 / CCTV
10. 농축산 / 사료 / 대두 / 참치 / 스마트팜
```

이번 라운드의 핵심은 “이 테마가 핫하다”가 아니라, **해당 테마가 E2R로 승격될 수 있는 조건과, 반대로 Green을 막아야 하는 조건**을 분리하는 거야.

---

# 2. WASTE_RECYCLING_ENVIRONMENT

폐기물처리 / 폐배터리 / 탈플라스틱 / 재활용

## 포함 테마

```text
폐기물처리
폐배터리
탈 플라스틱
골판지/제지 일부
전자폐기물
플라스틱 재활용
폐기물 에너지화
```

## 핵심 구조

```text
규제 강화 / 폐기물 처리 수요
→ 처리 단가 또는 재활용 소재 수요 증가
→ 장기 계약 / 허가권 / 처리 인프라
→ 반복 FCF
```

이 archetype은 생각보다 E2R에 가까울 수 있어. 이유는 “처리 인허가 + 반복 처리량 + 장기 계약”이 있으면 일회성 테마가 아니라 **인프라형 현금흐름**이 되기 때문이야. EQT가 2024년에 한국 KJ Environment 및 계열사를 인수해 플라스틱 재활용·폐기물 에너지화 플랫폼을 만들겠다고 한 사례는, 폐기물/재활용이 단순 테마가 아니라 인프라 투자 대상이 될 수 있음을 보여준다. ([Reuters][1])

## 성공 후보

| 케이스        | 판단                              |
| ---------- | ------------------------------- |
| 폐기물 처리 플랫폼 | 허가권, 처리시설, 장기계약, 반복 FCF가 있으면 후보 |
| 플라스틱 재활용   | 실제 처리량, 고객사, 마진 확인 필요           |
| 폐배터리 재활용   | 회수량, 금속가격, 재활용 수율, 고객사 필요       |
| 폐기물 에너지화   | 처리단가와 발전/열 판매 구조가 확인되면 후보       |

## 반례

| 반례                | 왜 위험한가              |
| ----------------- | ------------------- |
| 폐배터리 테마만 있는 기업    | 실제 회수량과 금속 회수 수익 없음 |
| 재활용 설비만 있고 가동률 낮음 | CAPEX만 크고 FCF 미발생   |
| 규제 기대만 있는 테마주     | 실적 전환 전 Stage 1 제한  |
| 원재료 가격 하락         | 재활용 금속/소재 마진 훼손     |

## Stage 기준

```text
Stage 1:
- 폐기물/재활용 규제 강화
- 처리시설 인수
- 폐배터리/플라스틱 재활용 뉴스

Stage 2:
- 처리량 증가
- 장기계약
- 가동률 상승
- OP/FCF 개선

Stage 3:
- 허가권/처리시설 병목
- 반복 FCF
- 고객사 다변화
- 시장이 단순 테마가 아닌 인프라형 사업으로 재평가

4B:
- ESG/재활용 테마 과열
- 폐배터리 기대가 valuation에 과반영

4C:
- 가동률 하락
- 금속가격 하락
- 규제 지연
- CAPEX 부담
```

## 점수비중 v0.5

```text
EPS/FCF: 18
Structural Visibility: 22
Bottleneck/Pricing: 15
Market Mispricing: 13
Valuation Rerating: 12
Capital Allocation: 3
Information Confidence: 5
Risk Penalty: 가동률 / 소재가격 / CAPEX
```

**정규화 포인트:**
폐기물처리는 Green 가능성이 있지만, 폐배터리·재활용 테마는 실제 처리량과 FCF가 확인되기 전까지 Watch로 둬야 한다.

---

# 3. REFINING_CHEMICAL_STEEL_SPREAD

정유 / 화학 / 철강 / 비철 스프레드

이건 기존 `COMMODITY_SPREAD`를 더 쪼개야 해.

```text
REFINING_OIL_SPREAD
CHEMICAL_SPREAD
STEEL_METAL_SPREAD
NONFERROUS_STRATEGIC_METALS
```

## 3-1. 정유

정유는 정제마진과 제품 mix가 핵심이야. SK Innovation은 2026년 1분기 큰 흑자 전환을 했지만, 정유 회복은 시간이 걸릴 수 있다고 경고했다. 이건 정유 archetype에서 “EPS가 반등해도 structural visibility는 낮게 시작해야 한다”는 좋은 예시야. ([Reuters][2])

### 점수비중

```text
EPS/FCF: 20
Structural Visibility: 10
Bottleneck/Pricing: 18
Market Mispricing: 10
Valuation: 10
Risk Penalty: 유가 / 정제마진 / 재고평가손익
```

### Green 조건

```text
정제마진 반등 + 수요 지속 + 재고 리스크 낮음 + FCF 개선
```

단순 정제마진 반등만으로 Green 금지.

---

## 3-2. 화학

화학은 중국·중동 공급과잉 리스크가 너무 중요해. 2024년에 LG화학과 롯데케미칼은 공급과잉으로 이익이 크게 악화됐고, 롯데케미칼은 2011년 이후 최대 영업손실을 기록했다. 이건 화학 archetype의 대표적인 4C 반례다. ([Reuters][3])

### 점수비중

```text
EPS/FCF: 20
Structural Visibility: 8~10
Bottleneck/Pricing: 16
Market Mispricing: 8
Valuation: 8
Risk Penalty: 중국 공급과잉 very high
```

### Green 조건

매우 제한적.

```text
제품 spread 개선
+ 공급과잉 완화
+ 구조조정/설비 폐쇄
+ OP/FCF 개선
```

화학은 “싸다” 하나로 Green 금지.

---

## 3-3. 철강

철강은 POSCO/현대제철 같은 대형사는 단순 철강가격보다 **중국 공급, 건설 수요, 원가, 고부가제품 mix**가 중요해.

### 성공 후보

```text
고부가 강재 mix 개선
조선/자동차향 수요 회복
중국 공급 조절
원가 안정
```

### 반례

```text
중국산 저가 철강 유입
건설 경기 둔화
철근 oversupply
원가 상승
```

### 점수비중

```text
EPS/FCF: 18
Structural Visibility: 10
Bottleneck/Pricing: 16
Market Mispricing: 10
Valuation: 10
Risk Penalty: 중국 공급 / 건설 수요 / 원가
```

**정규화 포인트:**
철강은 대부분 Cycle/Watch. 구조적 Green은 공급 조절과 고부가 mix가 확인될 때만.

---

# 4. RETAIL_ECOMMERCE_LOGISTICS

편의점 / 홈쇼핑 / 콜드체인 / 이커머스

## 포함 테마

```text
편의점
홈쇼핑
음식료 유통
마켓컬리·오아시스 관련주
콜드체인
택배와 종합물류 일부
```

## 핵심 구조

```text
점포망 / 물류망 / PB상품
→ same-store sales
→ 객단가 / 고마진 mix
→ 비용 레버리지
→ OPM / FCF 개선
```

한국 이커머스는 중국 직구와 플랫폼 경쟁이 큰 변수야. 2025년 한국 공정위는 AliExpress Korea와 신세계 Gmarket 계열의 합작을 조건부 승인했는데, 중국 직구 시장에서 알리바바의 비중, 고객 데이터, 국경간 이커머스 점유율 문제가 제기됐다. 이건 국내 유통/이커머스 archetype에서 **경쟁 심화와 마진 압박 반례**로 중요하다. ([Reuters][4])

## 성공 후보

| 케이스      | 판단                    |
| -------- | --------------------- |
| 편의점      | 점포효율, PB mix, 비용 레버리지 |
| 콜드체인     | 신선식품/의약품 반복 물류 수요     |
| 음식료 유통   | 고마진 상품 mix와 물류비 안정    |
| 이커머스 플랫폼 | 흑자전환과 물류비 통제 필요       |

## 반례

| 반례              | 이유                |
| --------------- | ----------------- |
| 중국 직구 압박        | 가격경쟁, 마진 하락       |
| 상장 기대만 있는 관련주   | event premium     |
| 매출 성장하지만 물류비 적자 | FCF 훼손            |
| 홈쇼핑 구조 둔화       | TV 트래픽 감소, 수수료 압박 |

## 점수비중

```text
EPS/FCF: 18
Structural Visibility: 16
Bottleneck/Pricing: 5
Market Mispricing: 14
Valuation: 14
Risk Penalty: 물류비 / 경쟁 / 재고
```

**정규화 포인트:**
유통은 Green이 가능하지만, **OPM과 FCF가 개선되지 않으면 단순 소비 회복/상장 이벤트**다.

---

# 5. INSURANCE_FINANCIAL_VALUEUP

보험 / 금융지주 / 증권 / VC / 신용정보

## 포함 테마

```text
손해보험
생명보험
화재
금융지주회사
은행
증권사
VC
고배당주
밸류업 지수 편입
신용정보
```

## 핵심 구조

```text
ROE / CSM / 손해율 / 자본비율 / 주주환원
→ PBR-ROE 프레임 변화
```

손해보험사는 일반 은행과 다르게 손해율과 CSM, 자본비율이 핵심이고, 은행은 CET1·ROE·충당금·환원정책이 핵심이다. 삼성화재는 국내 대표 손보사이고 자동차보험·장기보험·일반보험 포트폴리오를 가진 기준 케이스로 쓸 수 있다. ([위키백과][5])

## 성공 후보

| 케이스            | 봐야 할 것                      |
| -------------- | --------------------------- |
| 삼성화재 / DB손보    | 손해율, CSM, ROE, 자본비율, 자사주/배당 |
| KB금융 / 신한 / 하나 | CET1, ROE, credit cost, 환원  |
| 메리츠금융          | 자본효율, 주주환원 지속성              |
| 증권사            | 거래대금, IB, 자본비율, 배당          |

## 반례

| 반례          | 이유                     |
| ----------- | ---------------------- |
| 단순 저PBR 금융주 | ROE와 환원 없으면 value trap |
| 자본비율 낮은 보험  | 환원 제한                  |
| 손해율 악화      | underwriting break     |
| PF/충당금 리스크  | 4C                     |

## 점수비중

```text
EPS/FCF: 15
Structural Visibility: 20
Bottleneck/Pricing: 5
Market Mispricing: 15
Valuation: 25
Capital Allocation: 10
Risk Penalty: 손해율 / 자본비율 / credit cost
```

**정규화 포인트:**
금융은 EPS 폭발보다 **ROE-PBR-환원정책**의 정합성이 중요하다.

---

# 6. DIGITAL_ASSET_TOKENIZATION

스테이블코인 / STO / 결제서비스 / 토스

## 포함 테마

```text
스테이블코인
STO
디지털자산·블록체인
결제서비스
토스 관련주
지역화폐
NFT
```

## 핵심 구조

```text
규제 승인
→ 실제 발행/거래량/결제망 채택
→ 수수료·예치금·스프레드 수익
→ 반복 금융 인프라 매출
```

Toss는 2025년에 글로벌 확장과 원화 스테이블코인 발행 의지를 밝혔고, 한국 정부가 관련 입법을 준비 중이라는 보도가 있었다. 하지만 규제 승인과 실제 발행·수익모델이 나오기 전까지는 Stage 1~2 후보일 뿐이다. ([Reuters][6])
스테이블코인 자체도 설계·보안·유동성 리스크가 큰 영역이다. 2025년 연구는 스테이블코인이 안정적인 것처럼 보이지만 실제 안정성은 시장 신뢰와 유동성, 설계 구조에 의존하는 취약한 상태라고 정리했다. ([arXiv][7])

## 성공 후보

```text
Toss / 원화 스테이블코인
결제 PG사
STO 플랫폼
신용정보/데이터 기업
```

## 반례

```text
코인 테마만 있는 기업
NFT 테마
STO 법제화 기대만 있는 관련주
규제 지연/불허
보안사고
```

## 점수비중

```text
EPS/FCF: 16
Structural Visibility: 18
Bottleneck/Pricing: 8
Market Mispricing: 16
Valuation: 12
Risk Penalty: regulation / security / adoption
```

**정규화 포인트:**
디지털금융은 **규제 승인 + 실제 거래량 + 수익모델** 전까지 Green 금지.

---

# 7. HYDROGEN_RENEWABLE_POLICY

수소 / 태양광 / 풍력 / 탄소배출권

## 포함 테마

```text
수소차 연료전지
수소차 인프라
수소차 기타부품
태양광
풍력
탄소배출권
LNG 발전유통
스마트그리드
```

## 핵심 구조

```text
정책 / 보조금 / CAPEX
→ 실제 수주·생산·가동률
→ OP/EPS 전환
```

현대차는 2025년에 울산에 9,300억원 규모 수소연료전지 생산시설 착공을 발표했고, 2027년 완공 후 승용차·상용차·건설기계·선박용 연료전지와 전해조를 생산할 계획이다. 이건 수소 테마 중에서도 실제 CAPEX가 있는 Stage 1~2 후보 사례다. ([Reuters][8])

## 성공 후보

```text
수소 연료전지 생산시설
연료전지 업체
풍력 기자재
ESS/BESS
스마트그리드 장비
```

## 반례

```text
보조금 의존 사업
수소 테마만 있는 기업
풍력 프로젝트 지연
태양광 관세/공급망 리스크
가동률 낮은 CAPEX
```

## 점수비중

```text
EPS/FCF: 18
Structural Visibility: 18
Bottleneck/Pricing: 12
Market Mispricing: 12
Valuation: 10
Risk Penalty: policy / subsidy / supply chain
```

**정규화 포인트:**
정책 뉴스는 Stage 1. Stage 2 이상은 실제 계약·가동률·OP/EPS 전환이 있어야 한다.

---

# 8. BATTERY_RECYCLING_ESS_SHIFT

폐배터리 / ESS / 전고체 / 전기차 화재

## 포함 테마

```text
폐배터리
ESS
전고체 배터리
전기차 화재
2차전지 소재/부품/장비
리튬
```

## 핵심 구조

```text
EV 성장 기대
→ 소재/부품/CAPA 투자
→ EV 수요 둔화·광물가격·CAPA 과잉 리스크
→ ESS 전환이 일부 보완 가능
```

폐배터리·재활용은 실제 회수량과 금속 회수 수익이 없으면 테마에 머물러. Green Li-ion처럼 폐배터리에서 pCAM·리튬탄산염 등 소재를 회수해 다시 배터리 생산에 투입하는 사업 모델은 구조적 후보가 될 수 있지만, 실제 처리량과 수익성이 핵심이다. ([위키백과][9])

## 성공 후보

```text
ESS 전환 배터리
폐배터리 처리/소재 회수 기업
2차전지 공정장비
전고체 상용화 후보
```

## 반례

```text
EV 수요 둔화
광물가격 하락
CAPA 과잉
전고체 테마만 있는 기업
폐배터리 회수량 부족
```

## 점수비중

```text
EPS/FCF: 20
Structural Visibility: 16
Bottleneck/Pricing: 14
Market Mispricing: 10
Valuation: 10
Risk Penalty: very high
```

**정규화 포인트:**
2차전지는 Green보다 **과열/4B/4C 방어**가 더 중요하다.

---

# 9. TIRE_AUTO_COMPONENT_SPREAD

타이어 / 자동차 부품 / 경량화 / 자율주행 부품

## 포함 테마

```text
타이어
현대·기아차 부품주
자동차 연비개선 경량화
전기차 부품
자율주행
카메라
스마트폰 부품 일부
```

## 핵심 구조

```text
완성차 판매 / OE·RE 수요
→ ASP와 원재료 spread
→ OPM 개선
→ 고객사 다변화
```

## 성공 후보

```text
한국타이어
현대모비스
HL만도
전장/ADAS 부품
경량화 부품
```

## 반례

```text
원재료 상승
생산중단/화재
EV 수요 둔화 부품
단일 고객 의존
리콜/품질 비용
```

## 점수비중

```text
EPS/FCF: 20
Structural Visibility: 18
Bottleneck/Pricing: 10
Market Mispricing: 14
Valuation: 14
Risk Penalty: raw materials / customer concentration
```

**정규화 포인트:**
자동차 부품은 고객사와 원가에 묶인다. 고객 다변화와 원재료 안정 없이는 Green 제한.

---

# 10. DIAGNOSTICS_INFECTIOUS_EVENT

엠폭스 / 코로나 / 빈대 / 황사 / 마스크

## 포함 테마

```text
엠폭스
코로나19
전염병 진단
동물백신·방역
빈대퇴치
황사미세먼지 마스크
공기정화
```

## 핵심 구조

```text
이벤트성 수요
→ 단기 EPS 폭발 가능
→ 정상화 후 급락 위험
```

씨젠 2020처럼 팬데믹 수요로 EPS가 폭발할 수 있지만, 반복 수요가 아니면 정통 E2R이 아니다. 기존 case library에도 씨젠은 one-off 반례로 들어가 있다.

## 성공 후보

```text
반복 진단 플랫폼
소모품 기반 진단 장비
정부 장기 방역 계약
```

## 반례

```text
씨젠 팬데믹 일회성
마스크/방역 단기 테마
엠폭스/빈대 이벤트
코로나 치료제 기대만 있는 기업
```

## 점수비중

```text
EPS/FCF: 20
Structural Visibility: 5
Bottleneck/Pricing: 5
Market Mispricing: 5
Valuation: 5
Risk Penalty: one-off very high
```

**정규화 포인트:**
EPS 폭발이 있어도 Green 금지에 가깝다. Stage 3-Red/Yellow 또는 4B-watch로 보는 게 맞다.

---

# 11. SPECULATIVE_SCIENCE_THEME

초전도체 / 맥신 / 그래핀 / 양자 / 스페이스X

## 포함 테마

```text
초전도체
맥신
그래핀
양자 기술
스페이스X
퓨리오사AI 관련주 중 실체 불명확한 경우
뉴로모픽 반도체 테마
```

## 핵심 구조

```text
과학/기술 narrative
→ 주가 급등
→ 실제 매출/계약/상용화 전에는 EPS/FCF 없음
```

## 성공 후보

매우 제한적.

```text
실제 제품 매출
정부/기업 장기계약
상용화된 기술
FY1/FY2 매출·OP 확인
```

## 반례

```text
논문/테마만 있는 초전도체
맥신/그래핀 관련성 불명확
스페이스X 지분/납품 불명확
양자 기술 뉴스만 있는 종목
```

## 점수비중

```text
EPS/FCF: 5~10
Structural Visibility: 5
Bottleneck/Pricing: 5
Market Mispricing: 5
Valuation: 5
Risk Penalty: extreme
```

**정규화 포인트:**
이 archetype은 **Green을 거의 막는 필터**로 봐야 한다.

---

# 12. AGRI_LIVESTOCK_FOOD_COMMODITY

양돈 / 육계 / 사료 / 대두 / 참치

## 포함 테마

```text
양돈주
육계주
배합사료
대두
농업 종자·비료·농약
참치 원양어업
스마트팜
농기계
```

## 핵심 구조

```text
곡물/사료/육류/어가 가격
→ 원가 또는 판가
→ 단기 OP 변화
→ 대부분 사이클
```

## 성공 후보

```text
스마트팜/농기계 실제 수주
원양어업 가격·어획량·환율 개선
종자/농약/비료 가격전가
```

## 반례

```text
조류독감/질병 이벤트
사료 원가 상승
대두 가격 급등
날씨 이벤트
```

## 점수비중

```text
EPS/FCF: 18
Structural Visibility: 8~12
Bottleneck/Pricing: 14
Market Mispricing: 8
Valuation: 8
Risk Penalty: commodity / disease event
```

**정규화 포인트:**
농축산은 대부분 cycle/event. 판가 전가와 반복수요가 없으면 Green 제한.

---

# 13. 이번 라운드 정리: 신규 테마 점수정규화 표

| Archetype                     | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Green 정책          |
| ----------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ----------------- |
| WASTE_RECYCLING_ENVIRONMENT   |      18 |         22 |         15 |         13 |        12 | 허가권/반복 FCF 있으면 가능 |
| REFINING_OIL_SPREAD           |      20 |         10 |         18 |         10 |        10 | 제한적               |
| CHEMICAL_SPREAD               |      20 |          8 |         16 |          8 |         8 | 중국 공급과잉 때문에 제한    |
| RETAIL_ECOMMERCE_LOGISTICS    |      18 |         16 |          5 |         14 |        14 | OPM/FCF 확인 시 가능   |
| INSURANCE_UNDERWRITING_CYCLE  |      15 |         20 |          5 |         15 |        25 | ROE/CSM/환원 필요     |
| DIGITAL_ASSET_TOKENIZATION    |      16 |         18 |          8 |         16 |        12 | 규제·거래량 전까지 제한     |
| BEAUTY_OEM_ODM_SUPPLYCHAIN    |      22 |         23 |         12 |         16 |        13 | 가능, 재고/채권 감시      |
| BATTERY_RECYCLING_ESS_SHIFT   |      20 |         16 |         14 |         10 |        10 | 과열 방어 우선          |
| HYDROGEN_RENEWABLE_POLICY     |      18 |         18 |         12 |         12 |        10 | 정책만으론 금지          |
| TIRE_AUTO_COMPONENT_SPREAD    |      20 |         18 |         10 |         14 |        14 | 고객 다변화 필요         |
| DIAGNOSTICS_INFECTIOUS_EVENT  |      20 |          5 |          5 |          5 |         5 | Green 금지에 가까움     |
| SPECULATIVE_SCIENCE_THEME     |    5~10 |          5 |          5 |          5 |         5 | Green 거의 금지       |
| AGRI_LIVESTOCK_FOOD_COMMODITY |      18 |       8~12 |         14 |          8 |         8 | 대부분 cycle         |

---

# 14. 지금 제대로 정규화 중인가?

응. **방법은 맞다.**
다만 아직 최종 적용 단계는 아니다.

지금 정규화의 핵심은:

```text
성공사례:
어떤 증거가 점수를 높여야 하는지 알려줌

반례:
어떤 조건에서 Green을 막아야 하는지 알려줌

주가 경로:
그 점수 판단이 실제 리레이팅과 맞았는지 검증함
```

예를 들면:

```text
K뷰티 OEM/ODM:
성공하려면 수출, 고객사 다변화, OPM, 재고/채권 안정이 필요.
그래서 visibility와 EPS/FCF 가중치를 높게 준다.

스테이블코인:
규제·거래량·수익모델 전까지는 테마.
그래서 visibility는 중간, risk penalty를 강하게 둔다.

화학:
EPS가 좋아져도 중국 공급과잉이면 4C.
그래서 cyclical risk cap을 강하게 둔다.

진단/전염병:
EPS 폭발이 가능하지만 one-off.
그래서 EPS는 인정하되 visibility를 낮게 주고 Green을 막는다.
```

이게 우리가 원하는 “성공/반례 기반 점수정규화”야.

---

# 15. 다음 라운드에서 할 것

다음 라운드에서는 이제 진짜로:

```text
1. theme_tag_map.csv 초안
2. 각 theme_tag의 primary_archetype / green_policy
3. cases_v03 후보 리스트
4. price-validation 필드
5. under-covered archetype 리스트
```

형태로 더 구조화하면 돼.

이번 라운드에서 확장한 신규 부분은:

```text
폐기물/재활용
정유/화학/철강
편의점/이커머스/콜드체인
보험/금융 value-up
스테이블코인/STO/결제
수소/태양광/풍력
폐배터리/ESS
타이어/자동차 부품
CDMO
보안/딥페이크
전염병/이벤트
초전도체/그래핀/양자
농축산/사료/대두
```

이제 네가 준 세부 테마 대부분이 상위 구조에 흡수되고 있어. 다음엔 이걸 **테마 매핑표 + 케이스 레코드 후보표**로 더 기계가 먹기 쉬운 형태로 변환하면 된다.

[1]: https://www.reuters.com/markets/deals/eqt-strikes-deal-acquire-south-korean-waste-treatment-platform-2024-08-16/?utm_source=chatgpt.com "EQT strikes deal to acquire South Korean waste treatment platform"
[2]: https://www.reuters.com/world/asia-pacific/sk-innovation-warns-refining-recovery-take-time-beats-q1-profit-estimates-2026-05-13/?utm_source=chatgpt.com "SK Innovation warns refining recovery to take time, beats Q1 profit estimates"
[3]: https://www.reuters.com/markets/commodities/south-korean-petrochemical-firms-profits-plunge-2024-oversupply-persists-2025-02-07/?utm_source=chatgpt.com "South Korean petrochemical firms' profits plunge in 2024 as oversupply persists"
[4]: https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-conditionally-approves-aliexpress-shinsegae-unit-joint-venture-2025-09-18/?utm_source=chatgpt.com "South Korea conditionally approves AliExpress, Shinsegae unit joint venture"
[5]: https://en.wikipedia.org/wiki/Samsung_Fire_%26_Marine_Insurance?utm_source=chatgpt.com "Samsung Fire & Marine Insurance"
[6]: https://www.reuters.com/business/finance/south-korean-fintech-toss-plans-global-push-starting-australia-aims-issue-won-2025-09-09/?utm_source=chatgpt.com "South Korean fintech Toss plans global push starting in Australia, aims to issue won stablecoin"
[7]: https://arxiv.org/abs/2506.17622?utm_source=chatgpt.com "SoK: Stablecoin Designs, Risks, and the Stablecoin LEGO"
[8]: https://www.reuters.com/world/asia-pacific/hyundai-motor-breaks-ground-680-million-hydrogen-fuel-cell-plant-south-korea-2025-10-30/?utm_source=chatgpt.com "Hyundai Motor breaks ground on $680 million hydrogen fuel cell plant in South Korea"
[9]: https://en.wikipedia.org/wiki/Green_li-ion?utm_source=chatgpt.com "Green li-ion"
