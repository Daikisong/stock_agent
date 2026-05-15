좋아. **Round 28: 얇은 archetype 추가 보강 + 주요 archetype 점수비중 v1.9 교정**으로 계속 채울게.

이번 라운드는 그동안 상대적으로 덜 판 테마군 중에서, 실제 시장에서 자주 테마화되지만 점수화가 까다로운 쪽을 더 파고든다.

```text
1. CARBON_CREDIT_CBAM_COMPLIANCE
   탄소배출권 / CBAM / 탈탄소 규제 / 탄소비용 전가

2. PAYMENT_FINTECH_INFRA
   결제서비스 / PG / e-wallet / 신용정보 / 토스류 핀테크

3. OPTICAL_NETWORKING_AI_DATACENTER
   광섬유 / 광케이블 / AI 데이터센터 네트워크 / 5G·6G와 구분

4. TELECOM_5G_6G_CAPEX_CYCLE
   5G·6G / 통신장비 / Open RAN / 통신사 CAPEX cycle

5. LITHIUM_BATTERY_RAW_MATERIAL
   리튬 / 비철금속-리튬 / 배터리 원재료 / 광물가격 cycle

6. HOME_LIVING_APPLIANCE_RENTAL
   밥솥 / 생활가전 / 렌탈 / 스마트홈

7. AI_ACCELERATOR_CHIP_PUREPLAY
   AI칩 / 퓨리오사AI류 / Cerebras류 AI accelerator

8. MOBILITY_RENTAL_MICROMOBILITY
   렌터카 / 중고차 / 자전거 / 전동킥보드 / Lime류 mobility
```

기본 원칙은 그대로다. 테마명은 점수 근거가 아니고, 점수는 **산업 구조 변화 → EPS/FCF 체급 변화 → 시장의 과거 프레임 오해 → 밸류에이션 리레이팅**에서 나와야 한다.
그리고 계약금액, 계약기간, 매출 대비 계약금액, OP YoY 같은 값은 실제 상세공시·리포트에서 확인된 것만 써야 하고, 비어 있는 값을 추정해서 채우면 안 된다.

---

# 1. CARBON_CREDIT_CBAM_COMPLIANCE

## 탄소배출권 / CBAM / 탄소비용 전가 / 탈탄소 규제

### 핵심 구조

```text
탄소가격·규제 강화
→ 탄소비용 또는 탄소감축 CAPEX 발생
→ 비용 전가 가능 기업과 불가능 기업 분리
→ 탄소 회계·검증·저탄소 소재 수요
→ 단, 탄소배출권 자체는 가격·정책 변동성이 큼
```

탄소배출권은 “탄소 가격이 오른다 → 관련주 오른다”로 보면 위험하다. EU ETS는 2005년부터 작동한 핵심 탄소가격제지만, 정책 개편, 산업 경쟁력 논쟁, free allowance, 항공·건물·운송으로의 확장 여부 같은 변수에 크게 흔들린다. EU 집행위는 ETS 개편을 통해 더 많은 수익을 산업계로 되돌리고 탈탄소 투자를 유도하는 방향을 검토하고 있다. 즉 탄소배출권은 구조적 정책축이지만, 가격과 제도 설계가 계속 바뀐다. ([Reuters][1])

CBAM은 철강, 시멘트, 알루미늄, 비료, 전기, 수소 등 탄소집약 수입품에 비용을 부과하는 구조라서, 단순 탄소배출권 테마보다 **철강·시멘트·화학·전력·비철금속의 원가/가격 전가 능력**을 보는 데 더 중요하다. CBAM 인증서 가격은 EU ETS 가격과 연결되므로, 수출기업에는 실질 비용·마진 이슈가 된다. ([위키백과][2])

### 성공 후보

```text
- 탄소비용을 제품 가격에 전가할 수 있는 저탄소 소재 기업
- CBAM 대응용 탄소회계·검증·모니터링 서비스 기업
- 저탄소 철강·시멘트·알루미늄 전환에 실제 고객계약이 있는 기업
- 탄소저감 CAPEX가 수익성 개선 또는 premium pricing으로 이어지는 기업
```

### 반례

자발적 탄소시장이나 보상형 크레딧은 integrity 문제가 크다. 최근 umbrella review는 carbon tax·ETS는 어느 정도 배출 감축 효과가 있지만, voluntary carbon market과 REDD+류 보상시장에는 additionality, permanence, leakage, double counting 문제가 있어 실제 기후효과가 과대평가될 수 있다고 지적한다. 이건 탄소배출권/탄소크레딧 테마에서 **“크레딧 발행량”만 보고 Green을 주면 안 된다**는 강한 반례다. ([arXiv][3])

### 점수비중 v1.9

```text
EPS/FCF: 14
Structural Visibility: 17
Bottleneck/Pricing: 10
Market Mispricing: 12
Valuation Rerating: 8
Capital Allocation: 2
Information Confidence: 6
Risk Penalty: policy_change / allowance_price_volatility / greenwashing / pass_through_failure
```

### 정규화 교정

```text
점수 강화:
- CBAM/ETS 비용을 가격에 전가 가능
- 탄소회계·검증·모니터링 반복매출
- 저탄소 제품 premium pricing
- 규제 대응이 실제 계약으로 연결
- 탄소비용 절감이 FCF로 반영

점수 제한:
- 탄소배출권 가격 상승 테마만 있음
- voluntary offset 크레딧 품질 불명확
- greenwashing 리스크
- 탄소비용 전가 실패
- 정책 개편에 의존
```

**핵심:**
탄소배출권은 대부분 **Watch 중심**이다. Green은 “탄소가격 exposure”가 아니라 **탄소비용 전가력, 탄소회계 반복매출, 저탄소 제품 premium**이 확인될 때만 가능하다.

---

# 2. PAYMENT_FINTECH_INFRA

## 결제서비스 / PG / e-wallet / 신용정보 / 토스류 핀테크

### 핵심 구조

```text
거래액 증가
→ take rate / 결제망 수수료 / 부가 금융서비스
→ 반복 결제 인프라 매출
→ unit economics와 규제 안정성
```

결제서비스는 스테이블코인/STO와 분리해야 한다. 순수 결제·PG·e-wallet은 **거래액, take rate, 고객 수, 금융서비스 attach rate, 연체·규제 리스크**가 핵심이다.

### 성공 후보

필리핀 GCash 운영사 Mynt는 e-wallet archetype의 좋은 참고 케이스다. Reuters는 Mynt가 2026년 IPO에서 최소 80억 달러 valuation을 목표로 하고, GCash가 필리핀 인구 1억 2천만 명 중 9,400만 명 사용자를 보유하며 bill payment, 송금, 저축, 대출, 보험 접근을 제공한다고 보도했다. 이건 e-wallet이 단순 결제앱을 넘어 **금융서비스 플랫폼으로 확장될 때** 점수가 올라갈 수 있음을 보여준다. ([Reuters][4])

Stripe도 결제 인프라 성공사례 후보로 쓸 수 있다. Reuters는 Stripe가 2025년 tender offer에서 915억 달러 valuation을 받았고, 2024년에 흑자를 냈으며 2025년 이후에도 수익성을 기대한다고 보도했다. 결제 인프라에서 중요한 것은 사용자 수가 아니라 **거래액, 대형 고객, 자동화 금융 프로세스, 수익성**이다. ([Reuters][5])

### 반례

스테이블코인은 결제비용을 낮출 수 있는 잠재력이 있지만, 국제 규제 충돌과 convertibility risk가 크다. Bank of England 총재 Andrew Bailey는 stablecoin이 위기 때 실제 달러로 전환되는 방식과 국제 규제 기준을 둘러싼 리스크를 경고했다. 이건 결제/디지털금융 archetype에서 **규제와 유동성 안정성**을 강하게 봐야 한다는 반례다. ([Reuters][6])

### 점수비중 v1.9

```text
EPS/FCF: 18
Structural Visibility: 20
Bottleneck/Pricing: 8
Market Mispricing: 14
Valuation Rerating: 14
Capital Allocation: 2
Information Confidence: 5
Risk Penalty: regulation / take_rate_pressure / credit_loss / security / competition
```

### 정규화 교정

```text
점수 강화:
- 거래액 증가
- take rate 유지
- 대형 고객/가맹점 lock-in
- 부가 금융서비스 attach
- 흑자 또는 FCF 전환
- 규제 리스크 낮음

점수 제한:
- 사용자 수만 많음
- 결제액은 크지만 take rate 하락
- 대출·BNPL 연체 리스크
- 보안사고
- 스테이블코인 규제 불확실
```

**핵심:**
결제/PG/e-wallet은 **Watch-to-Green** 가능하다. 다만 스테이블코인/STO와 달리 실제 거래액과 수익성이 확인되어야 한다. 사용자 수만으로 Green 금지.

---

# 3. OPTICAL_NETWORKING_AI_DATACENTER

## 광섬유 / 광케이블 / 광통신 / AI 데이터센터 네트워크

### 핵심 구조

```text
AI 데이터센터 대규모 GPU cluster
→ 서버 간 데이터 이동 폭증
→ 광섬유·광케이블·광트랜시버 수요 증가
→ hyperscaler 장기계약
→ 단, valuation 과열과 고객 집중 리스크
```

### 성공 후보

Meta와 Corning의 광섬유 계약은 이 archetype의 핵심 성공 후보야. Reuters는 Meta가 AI 데이터센터 구축을 위해 Corning에 최대 60억 달러를 지급하는 계약을 맺었고, Corning이 advanced optical fiber, cable, connectivity product를 공급하며 Meta가 North Carolina cable factory의 anchor customer가 된다고 보도했다. 이건 광통신이 단순 통신장비가 아니라 **AI 데이터센터 병목 부품**으로 바뀌는 사례다. ([Reuters][7])

### 반례

광통신 관련주는 AI 데이터센터 수요 때문에 급등할 수 있지만, valuation 과열 리스크가 크다. Barron’s는 Coherent, Lumentum, Applied Optoelectronics 같은 optical networking 주식들이 AI 데이터센터 수요로 급등했고, Applied Optoelectronics가 2026년에 440% 상승했다고 보도했다. 이건 수요가 강해도 **주가가 너무 먼저 가면 4B-watch**를 켜야 한다는 사례다. ([Barron's][8])

### 점수비중 v1.9

```text
EPS/FCF: 21
Structural Visibility: 22
Bottleneck/Pricing: 20
Market Mispricing: 13
Valuation Rerating: 12
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: hyperscaler_concentration / valuation_crowding / capex_delay / inventory
```

### 정규화 교정

```text
점수 강화:
- hyperscaler 장기계약
- AI 데이터센터 직접 공급
- 광트랜시버/광케이블 병목
- 생산능력 확대와 수익성 개선
- OP/EPS 상향

점수 제한:
- 광통신 테마만 있음
- AI 데이터센터 exposure 불명확
- 고객사 단일 의존
- valuation 과열
- CAPEX 지연
```

**핵심:**
광통신/광케이블은 이제 **AI_DATA_CENTER_INFRASTRUCTURE의 Green 가능 하위축**으로 올릴 수 있다. 단, hyperscaler 계약과 실제 납품이 있어야 한다.

---

# 4. TELECOM_5G_6G_CAPEX_CYCLE

## 5G·6G / 통신장비 / Open RAN / 통신사 CAPEX

### 핵심 구조

```text
통신 세대교체
→ 장비 CAPEX
→ 납품·수주
→ 이후 CAPEX peak-out과 매출 둔화
```

통신장비는 광통신 AI 데이터센터와 분리해야 한다. 5G/6G 네트워크 장비는 통신사 CAPEX cycle에 묶이고, operator 투자 지연에 매우 취약하다.

### 반례

Nokia는 통신장비 capex cycle의 강한 반례다. AP는 Nokia가 5G 네트워크 수요 부진과 북미 투자 지연으로 매출과 이익이 급감하자 최대 14,000명 감원을 발표했다고 보도했다. 모바일 네트워크 사업 매출은 24% 감소했고, 북미 매출은 45% 급감했다. 이건 5G/통신장비 archetype에서 **세대교체 peak 이후 CAPEX 둔화가 4C로 작동**한다는 기준 반례다. ([AP News][9])

FT는 중국이 Nokia와 Ericsson 장비 사용을 제한하면서 두 회사의 중국 mobile telecom network 시장점유율이 2020년 12%에서 2024년 4%로 떨어졌다고 보도했다. 즉 통신장비는 기술 수요뿐 아니라 **지정학·보안심사·국산화 정책** 리스크가 매우 크다. ([파이낸셜 타임스][10])

### 점수비중 v1.9

```text
EPS/FCF: 16
Structural Visibility: 13
Bottleneck/Pricing: 8
Market Mispricing: 12
Valuation Rerating: 9
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: telecom_capex_cycle / geopolitics / security_review / operator_delay
```

### 정규화 교정

```text
점수 강화:
- 통신사 CAPEX 확정
- 실제 장비 수주
- Open RAN 또는 private network 수익화
- AI 데이터센터 네트워크로 확장

점수 제한:
- 5G/6G 정책 테마만 있음
- 통신사 투자 지연
- 세대교체 peak-out
- 중국/미국/유럽 보안심사
- 국산화 정책 리스크
```

**핵심:**
5G/6G 통신장비는 대부분 **Watch/Red**다. AI 데이터센터 광통신과 같은 Green profile로 보면 안 된다.

---

# 5. LITHIUM_BATTERY_RAW_MATERIAL

## 리튬 / 비철금속-리튬 / 배터리 원재료

### 핵심 구조

```text
EV·ESS 수요
→ 리튬 가격 상승
→ 광산·정제·소재 수익 증가
→ 단, 공급 재개와 가격 급락 리스크 큼
```

### 반례

Reuters는 리튬 가격이 2022년 11월 고점에서 86% 폭락했고, 이로 인해 전 세계 광산 폐쇄가 발생했다고 보도했다. 2025년에 가격 안정 가능성이 있었지만, 수익성이 회복되면 폐쇄 광산이 재가동될 수 있어 상승폭이 제한될 수 있다고 분석했다. 이건 리튬 archetype에서 **가격 상승 = 구조적 Green**이 아니라는 강한 반례다. ([Reuters][11])

Albemarle은 리튬 가격 하락의 대표 반례다. Reuters는 Albemarle이 리튬 가격 급락에도 비용절감으로 흑자 전환했지만, energy storage 부문 매출이 가격 하락으로 11억 달러 줄었고 CAPEX를 절반 수준으로 낮춘다고 보도했다. 즉 리튬 기업은 **원가절감·저비용 자산**이 있어도 가격 cycle에 크게 묶인다. ([Reuters][12])

### 점수비중 v1.9

```text
EPS/FCF: 19
Structural Visibility: 10
Bottleneck/Pricing: 16
Market Mispricing: 9
Valuation Rerating: 8
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: lithium_price / mine_restart / EV_demand / oversupply / capex
```

### 정규화 교정

```text
점수 강화:
- 저비용 광산·정제능력
- 장기 offtake
- ESS/EV 수요 확인
- 가격 하락에도 FCF 방어
- CAPEX 절제

점수 제한:
- 리튬 가격 반등 테마
- 광산 개발 계획만 있음
- EV 수요 둔화
- 폐쇄 광산 재가동 가능성
- 가격 급락
```

**핵심:**
리튬은 대부분 **Cycle/Watch**다. Green은 장기 offtake와 저비용 구조, FCF 방어력이 있을 때만 제한적으로 가능하다.

---

# 6. HOME_LIVING_APPLIANCE_RENTAL

## 밥솥 / 생활가전 / 렌탈 / 스마트홈

### 핵심 구조

```text
생활가전 판매
→ 교체수요 또는 렌탈·구독 모델
→ 반복 서비스·필터·관리 매출
→ 단, 내수 교체수요·주택경기·소비심리에 민감
```

### 반례

Whirlpool은 생활가전 hardware cycle의 강한 반례다. Reuters는 Whirlpool이 2026년 실적 전망을 절반으로 낮추고 배당을 중단했으며, 높은 금리, 주택 거래 부진, 소비심리 위축, 인플레이션으로 대형 가전 교체수요가 줄었다고 보도했다. 주가는 14년 저점까지 하락했다. 이건 생활가전에서 **hardware 교체수요만으로 Green을 주면 안 된다**는 반례다. ([Reuters][13])

### 성공 후보

반대로 Coway 같은 렌탈·구독형 생활가전은 일반 hardware 업체와 다르게 볼 수 있다. Coway는 정수기·공기청정기·비데·매트리스 렌탈/관리 기반의 한국 생활가전 기업으로 정리되며, 한국뿐 아니라 말레이시아, 미국, 태국, 인도네시아, 베트남 등 해외 자회사도 보유한다. 이런 모델은 **제품 판매보다 관리·렌탈 반복매출**을 볼 수 있어 Watch-to-Green 후보가 된다. ([위키백과][14])

### 점수비중 v1.9

```text
EPS/FCF: 17
Structural Visibility: 15
Bottleneck/Pricing: 6
Market Mispricing: 12
Valuation Rerating: 10
Capital Allocation: 2
Information Confidence: 5
Risk Penalty: replacement_cycle / housing_market / consumer_sentiment / inventory / competition
```

### 정규화 교정

```text
점수 강화:
- 렌탈·구독 반복매출
- 필터·관리 서비스
- 해외 계정 증가
- 낮은 해지율
- FCF 안정

점수 제한:
- 일회성 하드웨어 판매
- 주택경기 둔화
- 소비심리 악화
- 배당 중단
- 가격 경쟁
```

**핵심:**
생활가전은 hardware cycle이면 Watch/Red, 렌탈·관리 반복매출이면 Watch-to-Green이다.

---

# 7. AI_ACCELERATOR_CHIP_PUREPLAY

## Cerebras류 AI accelerator / 퓨리오사AI / AI칩 pure-play

### 핵심 구조

```text
AI inference/training 수요
→ accelerator chip 수요
→ 고객사 계약·양산·매출
→ 단, Nvidia 경쟁·고객집중·valuation risk 큼
```

### 성공 후보

Cerebras는 AI accelerator pure-play archetype의 좋은 참고 사례다. Reuters는 Cerebras가 2026년 IPO에서 55.5억 달러를 조달했고, 완전희석 valuation이 564억 달러였으며, 2025년 매출이 5.1억 달러로 2024년 2.9억 달러에서 증가했다고 보도했다. 이는 AI칩 pure-play가 실제 매출이 붙으면 큰 valuation을 받을 수 있음을 보여준다. ([Reuters][15])

### 반례

그러나 AI칩 pure-play는 valuation과 고객검증 리스크가 크다.

```text
- Nvidia와의 경쟁
- 고객사 양산 검증 실패
- 파운드리 수율 문제
- 대규모 CAPEX와 R&D 비용
- 매출은 증가하지만 valuation이 과도
- 고객사 concentration
```

### 점수비중 v1.9

```text
EPS/FCF: 18
Structural Visibility: 15
Bottleneck/Pricing: 13
Market Mispricing: 15
Valuation Rerating: 10
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: customer_validation / Nvidia_competition / valuation_overheat / foundry_yield / R&D_burn
```

### 정규화 교정

```text
점수 강화:
- 실제 매출
- 고객사 양산 채택
- inference/training 비용우위
- 공급망·파운드리 안정
- gross margin 개선

점수 제한:
- AI칩 관련주로만 묶임
- tape-out만 있음
- 고객사 계약 없음
- 매출 대비 valuation 과열
- Nvidia 대비 차별성 불명확
```

**핵심:**
AI칩 pure-play는 Watch-to-Green 가능하지만, 대부분 관련주는 Watch/Red다. 실제 고객·매출·수율·마진 없으면 Green 금지.

---

# 8. MOBILITY_RENTAL_MICROMOBILITY

## 렌터카 / 중고차 / 자전거 / 전동킥보드 / 공유 모빌리티

### 핵심 구조

```text
도심 이동수요
→ 공유 모빌리티·렌탈 플랫폼
→ 이용량 증가
→ unit economics / 유지보수 / 규제
→ FCF 전환
```

### 성공 후보

Lime은 micro-mobility archetype의 좋은 성공 후보이자 검증 사례다. Reuters는 Lime이 미국 IPO filing에서 2025년 매출이 29.1% 증가해 8.867억 달러였고, 29개국 230개 도시에서 운영하며, 3년 연속 positive free cash flow를 기록했다고 보도했다. 다만 여전히 순손실을 냈기 때문에 투자자들은 지속 가능한 수익성 전환을 볼 것이라고 설명했다. ([Reuters][16])

### 반례

```text
- 이용량은 늘지만 unit economics 부진
- 유지보수·배터리·재배치 비용 증가
- 도시 규제
- 사고·보험 리스크
- 계절성
- 경쟁 심화
```

### 점수비중 v1.9

```text
EPS/FCF: 17
Structural Visibility: 14
Bottleneck/Pricing: 6
Market Mispricing: 12
Valuation Rerating: 10
Capital Allocation: 1
Information Confidence: 5
Risk Penalty: unit_economics / regulation / maintenance_cost / seasonality / competition
```

### 정규화 교정

```text
점수 강화:
- positive FCF
- 도시별 이용률 안정
- 유지보수 비용 통제
- 규제 안정
- 반복 이용자 기반

점수 제한:
- 매출 성장만 있음
- 순손실 지속
- 규제 리스크
- unit economics 불명확
```

**핵심:**
렌터카·중고차·공유 모빌리티는 대부분 Watch다. FCF 전환과 unit economics가 확인될 때만 Stage 2~3 후보.

---

# Round 28 점수비중 요약표

| Archetype                     | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | 핵심 리스크                   |
| ----------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ------------------------ |
| CARBON_CREDIT_CBAM            |      14 |         17 |         10 |         12 |         8 |       2 | 정책개편, greenwashing       |
| PAYMENT_FINTECH_INFRA         |      18 |         20 |          8 |         14 |        14 |       2 | take rate, 규제, 보안        |
| OPTICAL_NETWORKING_AI_DC      |      21 |         22 |         20 |         13 |        12 |       0 | 고객집중, valuation crowding |
| TELECOM_5G_6G_CAPEX           |      16 |         13 |          8 |         12 |         9 |       0 | CAPEX cycle, 지정학         |
| LITHIUM_BATTERY_RAW_MATERIAL  |      19 |         10 |         16 |          9 |         8 |       0 | 가격급락, 공급재개               |
| HOME_LIVING_APPLIANCE_RENTAL  |      17 |         15 |          6 |         12 |        10 |       2 | 교체수요, 주택경기               |
| AI_ACCELERATOR_CHIP_PUREPLAY  |      18 |         15 |         13 |         15 |        10 |       0 | 고객검증, valuation          |
| MOBILITY_RENTAL_MICROMOBILITY |      17 |         14 |          6 |         12 |        10 |       1 | unit economics, 규제       |

---

# cases_v16 추가 후보

```text
CARBON_CREDIT_CBAM_COMPLIANCE:
- cbam_compliance_service_candidate
- carbon_cost_pass_through_success_candidate
- voluntary_carbon_credit_integrity_counterexample
- carbon_allowance_price_volatility_4c

PAYMENT_FINTECH_INFRA:
- mynt_gcash_wallet_financial_services_candidate
- stripe_profitable_payment_infra_candidate
- stablecoin_convertibility_regulation_4c
- high_user_count_no_take_rate_counterexample

OPTICAL_NETWORKING_AI_DATACENTER:
- meta_corning_fiber_ai_datacenter_contract_candidate
- optical_networking_ai_demand_candidate
- optical_stock_valuation_crowding_4b
- optical_customer_concentration_counterexample

TELECOM_5G_6G_CAPEX_CYCLE:
- nokia_5g_capex_slowdown_4c
- china_restricts_nokia_ericsson_geopolitical_4c
- open_ran_policy_no_revenue_watch
- 6g_policy_no_revenue_counterexample

LITHIUM_BATTERY_RAW_MATERIAL:
- lithium_price_stabilization_candidate
- albemarle_cost_cut_low_lithium_price_case
- lithium_price_crash_oversupply_4c
- mine_restart_supply_rebound_counterexample

HOME_LIVING_APPLIANCE_RENTAL:
- coway_rental_subscription_candidate
- whirlpool_replacement_cycle_4c
- appliance_dividend_suspension_counterexample
- smart_home_no_subscription_counterexample

AI_ACCELERATOR_CHIP_PUREPLAY:
- cerebras_ipo_revenue_growth_candidate
- ai_chip_valuation_overheat_4b
- ai_chip_no_customer_validation_counterexample
- foundry_yield_risk_4c

MOBILITY_RENTAL_MICROMOBILITY:
- lime_positive_fcf_candidate
- micromobility_revenue_growth_no_profit_counterexample
- city_regulation_4c
- maintenance_cost_unit_economics_counterexample
```

---

# 이번 라운드 핵심 교정

```text
1. 탄소배출권은 정책축이지만 Green은 어렵다.
   CBAM 대응·탄소회계·비용전가가 실제 매출/마진으로 연결될 때만 점수 상승.

2. 결제·PG·e-wallet은 Watch-to-Green 가능.
   사용자 수가 아니라 거래액, take rate, 반복 금융서비스, FCF가 핵심.

3. 광섬유·광통신은 AI 데이터센터 병목으로 Green 가능성이 생겼다.
   단, hyperscaler 계약과 실제 납품이 필요.

4. 5G/6G 통신장비는 광통신 AI 데이터센터와 다르게 CAPEX cycle과 지정학 리스크가 커서 Watch/Red 중심.

5. 리튬은 가격 반등만으로 Green 금지.
   저비용 구조, 장기 offtake, FCF 방어력이 있어야 한다.

6. 생활가전은 hardware cycle이면 Watch/Red, 렌탈·관리 반복매출이면 Watch-to-Green.

7. AI accelerator pure-play는 실제 매출이 있으면 후보지만, valuation과 고객검증 리스크가 크다.

8. 공유 모빌리티·렌터카·중고차는 FCF와 unit economics가 핵심. 매출 성장만으로 Green 금지.
```

---

# 현재 판단

이제 **점수비중 가설 v1.9**까지 왔다고 보면 된다.
테마 흡수 구조는 상당히 넓어졌고, 얇았던 archetype도 많이 보강됐다.

하지만 마지막 검증은 여전히 필요하다.

```text
1. cases_v16 반영
2. 각 case의 stage date 후보 설정
3. price path backfill
4. MFE/MAE/drawdown 계산
5. score-price alignment 확인
6. shadow scoring
7. 틀린 archetype 점수 재교정
```

지금 단계에서 중요한 건 **production scoring 적용이 아니라, 성공/반례/주가검증용 case library를 더 두껍게 만드는 것**이다.

[1]: https://www.reuters.com/sustainability/climate-energy/eu-carbon-trading-revamp-boost-revenue-return-industry-commissioner-says-2026-05-12/?utm_source=chatgpt.com "EU carbon trading revamp to boost revenue return to industry, commissioner says"
[2]: https://en.wikipedia.org/wiki/EU_Carbon_Border_Adjustment_Mechanism?utm_source=chatgpt.com "EU Carbon Border Adjustment Mechanism"
[3]: https://arxiv.org/abs/2512.06887?utm_source=chatgpt.com "Effectiveness of Carbon Pricing and Compensation Instruments: An Umbrella Review of the Empirical Evidence"
[4]: https://www.reuters.com/world/asia-pacific/philippine-e-wallet-firm-mynt-aiming-8-billion-valuation-ipo-sources-say-2026-05-14/?utm_source=chatgpt.com "Philippine e-wallet firm Mynt aiming for $8 billion valuation in IPO, sources say"
[5]: https://www.reuters.com/technology/stripe-valued-915-billion-latest-tender-offer-cnbc-reports-2025-02-27/?utm_source=chatgpt.com "Fintech firm Stripe valued at $91.5 billion in latest tender offer"
[6]: https://www.reuters.com/sustainability/boards-policy-regulation/bank-englands-bailey-sees-wrestle-with-us-stablecoin-regulation-2026-05-08/?utm_source=chatgpt.com "Bank of England's Bailey sees 'wrestle' with US on stablecoin regulation"
[7]: https://www.reuters.com/business/meta-signs-deal-pay-corning-up-6-billion-fiber-optic-cables-cnbc-reports-2026-01-27/?utm_source=chatgpt.com "Meta, Corning sign deal worth up to $6 billion for fiber-optic cables in AI data centers"
[8]: https://www.barrons.com/articles/coherent-lumentum-ai-networking-stocks-data-center-boom-4db319b8?utm_source=chatgpt.com "Coherent and Lumentum Stocks Rise as the AI Networking Trade Stays Hot"
[9]: https://apnews.com/article/f13fa6283193a4ed22b8c7f0585c4d19?utm_source=chatgpt.com "Nokia plans to cut up to 14,000 jobs after sales and profits plunge in a weak market"
[10]: https://www.ft.com/content/7d08731c-189e-4835-8cfa-048fe68611bd?utm_source=chatgpt.com "China curbs use of Nokia and Ericsson in telecoms networks"
[11]: https://www.reuters.com/markets/commodities/lithium-prices-stabilise-2025-mine-closures-china-ev-sales-ease-glut-analysts-2025-01-13/?utm_source=chatgpt.com "Lithium prices to stabilise in 2025 as mine closures, China EV sales ease glut, analysts say"
[12]: https://www.reuters.com/markets/commodities/albemarle-swings-quarterly-profit-cost-cuts-offset-lithium-price-drop-2025-02-12/?utm_source=chatgpt.com "Cost cuts help Albemarle's results offset low lithium prices"
[13]: https://www.reuters.com/business/whirlpool-shares-tumble-after-revenue-miss-dividend-suspension-2026-05-07/?utm_source=chatgpt.com "Whirlpool shares hit 14-year low after slashing annual targets, suspending dividend"
[14]: https://en.wikipedia.org/wiki/Coway_%28company%29?utm_source=chatgpt.com "Coway (company)"
[15]: https://www.reuters.com/legal/government/cerebras-prices-ipo-185-per-share-raise-555-billion-sources-say-2026-05-13/?utm_source=chatgpt.com "Cerebras prices IPO at $185 per share to raise $5.55 billion"
[16]: https://www.reuters.com/technology/lime-files-go-public-new-york-2026-05-08/?utm_source=chatgpt.com "Uber-backed Lime reveals revenue surge in US IPO filing"
