좋아. **Round 18: 얇은 archetype 보강 + 주요 archetype 점수비중 v0.9 교정**으로 계속 간다.

이번 라운드의 목적은 단순히 케이스를 더 많이 붙이는 게 아니라, **성공사례와 반례가 실제로 어떤 점수축을 강화하거나 제한해야 하는지** 더 정교하게 만드는 거야.

기본 정신은 그대로 유지한다.

> 테마명은 점수 근거가 아니다.
> 점수는 산업 구조 변화, EPS/FCF 체급 변화, 시장의 과거 프레임 오해, 밸류에이션 리레이팅 가능성에서 나온다.
> 그리고 계약금액·계약기간·매출대비 계약금액 같은 필드는 실제 공시/리포트에서 확인될 때만 써야 하고, 없는 값은 절대 만들어내면 안 된다.

---

# Round 18에서 더 파는 Archetype

이번에는 아래 10개를 더 채운다.

```text
1. RAIL_INFRASTRUCTURE
2. CLOUD_AI_SOFTWARE_INFRA
3. CRO_CLINICAL_SERVICE
4. RETAIL_ECOMMERCE_LOGISTICS
5. SOLAR_TARIFF_SUPPLYCHAIN
6. INSURANCE_UNDERWRITING_CYCLE
7. DIGITAL_HEALTHCARE_AI
8. SECURITY_IDENTITY_DEEPFAKE
9. BATTERY_RECYCLING_ESS_SHIFT
10. SECURITIES_BROKERAGE_CYCLE
```

---

# 1. RAIL_INFRASTRUCTURE

철도 / 고속철 / 대형 인프라 수주

## 핵심 구조

```text
국가 인프라 예산 또는 해외 발주
→ 실제 대형 계약
→ 납품 스케줄
→ 매출·OP 인식
→ 수주잔고 기반 visibility
```

## 성공사례 후보

**현대로템 모로코 철도 수주**는 이 archetype의 기준 케이스로 좋다. 현대로템은 모로코 국영철도 ONCF로부터 약 2.2조원, 15.4억 달러 규모의 2층 전동차 수주를 받았고, Reuters는 이 계약이 현대로템 철도사업 사상 최대 수주라고 보도했다. 이건 단순 철도 테마가 아니라 **실제 계약 + 수주잔고 + 납품 visibility**가 있는 Stage 1→2 사례다. ([Reuters][1])

## 반례

```text
- 철도 정책 기대만 있는 관련주
- 우크라 재건 / 네옴시티 / 철도 테마만 붙은 종목
- 실제 계약 없이 MOU만 있는 기업
- 수주는 있으나 마진·납기·원가가 불명확한 기업
```

## 점수비중 v0.9

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

## 정규화 교정

철도는 전력기기·방산처럼 수주형이지만, **마진과 납기 리스크**를 더 세게 봐야 한다.
따라서 `Structural Visibility`는 높게 주되, Green은 아래 조건을 만족해야 한다.

```text
계약금액/매출 비중
납품 스케줄
마진 확인
FY1/FY2 OP 상향
프로젝트 financing 리스크 낮음
```

---

# 2. CLOUD_AI_SOFTWARE_INFRA

클라우드 / ERP / B2B SaaS / 컨택센터

## 핵심 구조

```text
반복 소프트웨어 매출
→ 고객 lock-in
→ ARPU / OPM 개선
→ FCF 개선
```

## 성공사례 후보

**더존비즈온**은 국내 B2B 소프트웨어 archetype의 중요한 기준 케이스다. EQT는 더존비즈온 지분 37.6%를 약 9.3억 달러에 인수하기로 했고, Reuters는 더존비즈온이 중소기업 대상 클라우드 ERP·회계·세무·컴플라이언스 소프트웨어를 제공한다고 설명했다. 이건 “AI 테마”가 아니라 **반복 B2B 소프트웨어 매출 + 고객 lock-in + 운영 개선 가능성**을 보는 Stage 1~2 사례다. ([Reuters][2])

## 반례

```text
- AI 기능만 추가하고 FCF 훼손
- 클라우드 비용 증가로 OPM 하락
- 고객 이탈 / churn 상승
- SI성 매출만 있고 SaaS 전환 없음
- 컨택센터·원격근무 테마만 있고 반복매출 없음
```

## 점수비중 v0.9

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

## 정규화 교정

클라우드/SaaS는 Green 가능성이 있다.
다만 점수는 `AI 키워드`가 아니라 아래에서 나온다.

```text
반복매출 증가
ARPU 상승
고객 retention
OPM 개선
FCF conversion
AI 비용 통제
```

즉 `AI 기능 추가`는 Stage 1 신호일 뿐이고, **반복매출과 FCF가 안 붙으면 Stage 3 금지**다.

---

# 3. CRO_CLINICAL_SERVICE

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

CRO는 pre-revenue biotech과 다르게 봐야 한다. 실제 서비스 매출과 고객사 다변화가 있으면 Watch-to-Green 가능성이 있다.

## 핵심 반례

**Charles River Laboratories**는 CRO/바이오서비스 반례로 중요하다. 2024년에 바이오 고객사의 funding crunch가 지속되면서 연간 전망을 낮췄고, Reuters는 이 소식으로 주가가 premarket에서 15% 하락했다고 보도했다. 즉 CRO는 반복 서비스처럼 보여도 **바이오 funding cycle과 고객사 R&D 예산**이 꺾이면 4C로 가야 한다. ([Reuters][3])

## 점수비중 v0.9

```text
EPS/FCF: 18
Structural Visibility: 20
Bottleneck/Pricing: 8
Market Mispricing: 12
Valuation Rerating: 12
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: biotech_funding_cycle / customer_concentration / backlog_quality
```

## 정규화 교정

CRO는 CDMO보다 약하지만, pre-revenue biotech보다 훨씬 점수화 가능하다.

```text
CDMO:
장기 생산계약 + capacity + 가동률

CRO:
수주잔고 + 고객사 다변화 + R&D funding cycle

Pre-revenue biotech:
임상 뉴스만으로 Green 금지
```

CRO에서 Green을 주려면 `고객사 다변화`, `수주잔고`, `매출/OP 증가`, `R&D funding cycle 안정`이 필요하다.

---

# 4. RETAIL_ECOMMERCE_LOGISTICS

편의점 / 이커머스 / 홈쇼핑 / 콜드체인

## 핵심 구조

```text
점포망 / 물류망 / PB상품
→ same-store sales
→ 비용 레버리지
→ OPM / FCF 개선
```

## 성공후보와 반례

**Coupang**은 이 archetype에서 성공과 반례를 동시에 제공한다. Coupang은 한국 이커머스·물류 인프라의 대표 기업이지만, 2024년 1분기에는 Farfetch 인수 영향으로 순이익이 크게 감소했고, developing offerings 손실 부담이 있었다. 즉 매출 성장과 물류 인프라가 있어도 **신사업 손실·비용 구조·FCF**를 확인해야 한다. ([월스트리트저널][4])

또 Coupang은 2026년에 공정위로부터 납품업체 압박·대금 지연 문제로 과징금을 받았다는 Reuters 보도가 있다. 이는 유통 플랫폼의 **마진 개선이 공급업체 압박에서 나온 것인지, 구조적 효율에서 나온 것인지** 구분해야 한다는 반례다. ([Reuters][5])

## 반례 조건

```text
- 매출 성장하지만 물류비·배송비로 FCF 악화
- 홈쇼핑 구조 둔화
- 상장 기대만 있는 관련주
- 중국 직구/저가 e-commerce 압박
- 공급업체 압박·규제 리스크
- 데이터 유출·보안 리스크
```

## 점수비중 v0.9

```text
EPS/FCF: 18
Structural Visibility: 16
Bottleneck/Pricing: 5
Market Mispricing: 13
Valuation Rerating: 14
Capital Allocation: 3
Information Confidence: 5
Risk Penalty: logistics_cost / inventory / supplier_regulation / data_security
```

## 정규화 교정

유통·이커머스는 Green을 보수적으로 줘야 한다.

```text
Stage 1:
매출 성장, 점포/물류망 확대, 상장 이벤트

Stage 2:
OPM 개선, 물류비 안정, 재고 정상화, FY1/FY2 OP 상향

Stage 3:
반복 고객 + 비용 레버리지 + FCF 개선 + 규제 리스크 낮음
```

**매출 성장만으로 Stage 3 금지.**
FCF와 OPM이 핵심이다.

---

# 5. SOLAR_TARIFF_SUPPLYCHAIN

태양광 / 관세 / 공급망 / 보조금

## 핵심 구조

```text
정책·보조금·관세
→ 생산시설·부품 공급망
→ 가동률·마진
→ OP/FCF 전환
```

## 성공후보와 반례

**Qcells / Hanwha Solutions**는 태양광 supply chain archetype의 좋은 기준 사례다. Qcells는 미국 조지아에서 대규모 태양광 생산 투자를 진행 중이지만, 미국 세관이 중국 강제노동방지법 관련으로 핵심 부품을 억류하면서 약 1,000명 노동자의 근무시간과 임금을 줄이고 300명 계약직을 해고했다는 보도가 있었다. 즉 태양광은 정책 수혜가 있어도 **관세·통관·부품 공급망 리스크**가 4C가 될 수 있다. ([AP News][6])

Reuters도 Qcells가 부품 지연으로 미국 공장 노동자 약 1,000명을 furlough했고, 해외 부품 조달 지연이 생산 차질로 이어졌다고 보도했다. ([Reuters][7])

## 점수비중 v0.9

```text
EPS/FCF: 18
Structural Visibility: 17
Bottleneck/Pricing: 12
Market Mispricing: 12
Valuation Rerating: 10
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: tariff / customs / subsidy / supply_chain
```

## 정규화 교정

태양광은 `정책 수혜`만으로 Green을 주면 안 된다.
Green을 주려면:

```text
가동률 상승
부품 공급 안정
관세 리스크 낮음
OP/FCF 개선
고객사 또는 장기 수요 확인
```

이 필요하다.

태양광은 `watch_only` 또는 `watch_to_green`이고, 관세·부품 억류·보조금 축소가 나오면 4C로 내려야 한다.

---

# 6. INSURANCE_UNDERWRITING_CYCLE

손해보험 / 생명보험 / 보증보험 / 화재

## 핵심 구조

```text
손해율 안정
→ CSM / ROE 개선
→ 자본비율 안정
→ 주주환원
→ PBR-ROE 프레임 리레이팅
```

## 성공후보

**Samsung Fire & Marine Insurance**는 손해보험 archetype의 기준 케이스로 쓸 수 있다. 자동차보험·장기보험·일반보험 포트폴리오를 가진 대형 손보사라서, 손해율·ROE·자본비율·환원정책을 보는 데 적합하다. ([위키백과][8])

**SGI서울보증**은 보증보험 archetype의 특수 케이스다. 보증보험은 반복 보험료 수익과 신용위험 관리가 중요하지만, SGI는 2025년에 랜섬웨어 공격으로 서비스가 며칠간 중단된 사례가 있어 보험·금융 인프라에서도 **사이버 운영 리스크**를 봐야 한다. ([위키백과][9])

## 반례

```text
- 단순 저PBR 보험주
- 손해율 악화
- 자본비율 낮아 환원 제한
- 사이버 장애 / 랜섬웨어
- 부동산 PF / 대체투자 손실
```

## 점수비중 v0.9

```text
EPS/FCF: 15
Structural Visibility: 21
Bottleneck/Pricing: 4
Market Mispricing: 15
Valuation Rerating: 25
Capital Allocation: 10
Information Confidence: 5
Risk Penalty: underwriting / capital_ratio / cyber_operational / credit_cost
```

## 정규화 교정

보험은 EPS 폭발형이 아니라 **PBR-ROE-환원 리레이팅형**이다.

```text
Green 조건:
ROE 개선
CSM 또는 손해율 안정
자본비율 안정
실제 배당·자사주
credit/cyber risk 낮음
```

---

# 7. DIGITAL_HEALTHCARE_AI

의료AI / 원격의료 / 유전체검사

## 핵심 구조

```text
임상 문제
→ AI 진단·판독·문서화 솔루션
→ 병원 도입
→ 수가·보험·반복 사용
→ 매출/FCF 전환
```

## 성공후보

의료AI는 논문 성능만으로 Green을 주면 안 되지만, 실제 임상 workflow를 개선하면 Watch-to-Green 가능성이 있다. 최근 mammography AI 연구는 50만 개 이상 검사로 학습한 AI가 내부 test에서 높은 AUROC를 보이고 recall과 radiologist workload를 줄일 가능성을 제시했다. 다만 이건 아직 **임상 성능 근거**이지 곧바로 매출/FCF 근거는 아니다. ([arXiv][10])

## 반례

```text
- 논문 성능은 좋지만 병원 매출 없음
- 수가/보험 없음
- 병원 workflow 도입 실패
- 오진·책임소재 리스크
- 규제 승인 지연
```

## 점수비중 v0.9

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

## 정규화 교정

의료AI는 `Watch-to-Green`이다.
Green 조건은 아래처럼 빡세게 둔다.

```text
외부 임상 검증
규제 승인
병원 도입
수가·보험 또는 반복 과금
매출/OP 전환
```

논문·PoC·AI 키워드만 있으면 Stage 1~2.

---

# 8. SECURITY_IDENTITY_DEEPFAKE

IT보안 / 딥페이크 / 생체인식 / CCTV

## 핵심 구조

```text
보안 위협 증가 / 규제 강화
→ 기업·정부 보안 지출
→ 반복 구독 또는 장기계약
→ ARR·OPM·FCF 개선
```

## 성공후보와 반례

보안은 구조적 수요가 강하지만, 운영 신뢰 리스크가 매우 크다. CrowdStrike는 대표 반례다. 2024년 CrowdStrike의 잘못된 Falcon Sensor 업데이트로 약 850만 대 Windows 기기가 장애를 겪었고, 항공·의료·금융·정부 서비스 등 광범위한 분야가 영향을 받았다. 이는 보안 소프트웨어 기업에서 **운영 신뢰도·업데이트 리스크가 hard 4C**가 될 수 있음을 보여준다. ([위키백과][11])

The Guardian도 이 outage가 미국 Fortune 500 기업들에 54억 달러 규모 비용을 유발할 수 있다고 보도했다. 즉 보안은 반복매출이 있어도 대형 장애 하나가 4C로 전환될 수 있다. ([가디언][12])

## 점수비중 v0.9

```text
EPS/FCF: 20
Structural Visibility: 20
Bottleneck/Pricing: 10
Market Mispricing: 14
Valuation Rerating: 13
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: operational_trust / outage / legal / customer_retention
```

## 정규화 교정

보안은 Green 가능성이 있지만, `운영 신뢰도`를 강한 gate로 넣어야 한다.

```text
Green 조건:
반복 구독 매출
낮은 churn
고객 다변화
OPM 개선
대형 장애·소송 리스크 부재
```

딥페이크·생체인식·CCTV는 실제 공공/기업 계약 전까지 Watch.

---

# 9. BATTERY_RECYCLING_ESS_SHIFT

폐배터리 / ESS / 전고체 / EV 수요 둔화

## 핵심 구조

```text
EV 성장 기대
→ 소재/부품/CAPA 투자
→ EV 수요 둔화·광물가격·CAPA 과잉 리스크
→ ESS 전환이 일부 보완 가능
```

## 성공후보와 반례

EV 배터리에서는 ESS 전환이 새로운 Watch 포인트다. GM-LG Ohio 배터리 공장의 재가동 시점은 EV 수요 둔화로 불확실했고, Tennessee 공장은 ESS 셀 생산으로 전환되는 흐름이 나타났다. 이는 EV 소재/CAPA archetype에서 **EV 수요 둔화는 반례, ESS 전환은 별도 후보**로 분리해야 한다는 근거다. ([Reuters][7])

Qcells 사례처럼 친환경 공급망은 정책·보조금 수혜가 있어도 부품 조달·관세·통관 리스크가 production disruption으로 이어질 수 있다. 이 logic은 배터리/ESS에도 그대로 적용된다. ([AP News][6])

## 점수비중 v0.9

```text
EPS/FCF: 20
Structural Visibility: 16
Bottleneck/Pricing: 14
Market Mispricing: 10
Valuation Rerating: 10
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: EV_demand / mineral_price / capex_overbuild / policy
```

## 정규화 교정

2차전지·폐배터리·ESS는 Green을 제한한다.

```text
Stage 2 가능:
실제 ESS 수요
고객사 계약
가동률 개선
FCF 훼손 없는 CAPEX

Stage 3 제한:
장기계약 + 가격전가 + 수요지속 + valuation 여지

4C:
EV 수요 둔화
광물가격 하락
CAPA 과잉
margin compression
```

---

# 10. SECURITIES_BROKERAGE_CYCLE

증권사 / VC / 거래대금 / IPO

## 핵심 구조

```text
거래대금 증가
→ 브로커리지 수수료 증가
→ IPO/IB 회복
→ 자기자본 운용성과
→ ROE 개선
```

## 성공후보

```text
- 거래대금 증가와 브로커리지 수익 증가가 확인되는 대형 증권사
- IPO·ECM·DCM pipeline 회복
- PF 리스크 낮고 자본비율 안정적인 증권사
- VC 회수시장 회복 기업
```

## 반례

```text
- 거래대금 단기 급증 후 소멸
- 부동산 PF/대체투자 손실
- 자기자본 운용손실
- IPO 회복 기대만 있고 실적 없음
- VC 회수시장 막힘
```

## 점수비중 v0.9

```text
EPS/FCF: 18
Structural Visibility: 14
Bottleneck/Pricing: 5
Market Mispricing: 15
Valuation Rerating: 18
Capital Allocation: 8
Information Confidence: 5
Risk Penalty: market_turnover / PF / proprietary_loss / IPO_cycle
```

## 정규화 교정

증권사는 은행·보험보다 **더 사이클성이 강하다.**
따라서 Green은 제한하고 Watch 중심으로 둔다.

```text
Stage 1:
거래대금 증가, 증시 랠리, IPO 기대

Stage 2:
브로커리지 수익 증가, IB fee 증가, OP/EPS 상향

Stage 3:
반복적 시장활동 회복 + PF 리스크 낮음 + ROE 구조 개선

4C:
거래대금 급감, PF 손실, 자기자본 운용손실
```

---

# Round 18 점수비중 요약표

| Archetype                    | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Risk 성격     |
| ---------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ----------- |
| RAIL_INFRASTRUCTURE          |      20 |         23 |         12 |         14 |        12 |       1 | 납기·마진       |
| CLOUD_AI_SOFTWARE_INFRA      |      20 |         23 |          8 |         16 |        14 |       0 | AI비용·churn  |
| CRO_CLINICAL_SERVICE         |      18 |         20 |          8 |         12 |        12 |       0 | 바이오 funding |
| RETAIL_ECOMMERCE_LOGISTICS   |      18 |         16 |          5 |         13 |        14 |       3 | 물류비·규제      |
| SOLAR_TARIFF_SUPPLYCHAIN     |      18 |         17 |         12 |         12 |        10 |       0 | 관세·통관       |
| INSURANCE_UNDERWRITING_CYCLE |      15 |         21 |          4 |         15 |        25 |      10 | 손해율·자본      |
| DIGITAL_HEALTHCARE_AI        |      18 |         17 |          8 |         13 |        12 |       0 | 허가·수가       |
| SECURITY_IDENTITY_DEEPFAKE   |      20 |         20 |         10 |         14 |        13 |       0 | 장애·소송       |
| BATTERY_RECYCLING_ESS_SHIFT  |      20 |         16 |         14 |         10 |        10 |       0 | CAPA·EV수요   |
| SECURITIES_BROKERAGE_CYCLE   |      18 |         14 |          5 |         15 |        18 |       8 | 거래대금·PF     |

---

# 이번 라운드의 핵심 교정

```text
1. 철도는 실제 해외 대형계약이 있으면 Stage 2 이상 가능.
   단, 정책/재건 테마만으로는 event_watch.

2. 클라우드/SaaS는 Green 가능.
   하지만 AI 키워드가 아니라 반복매출·OPM·FCF가 핵심.

3. CRO는 pre-revenue biotech보다 강하지만 CDMO보다 약함.
   바이오 funding cycle과 고객사 예산이 4C 조건.

4. 이커머스/유통은 매출 성장보다 OPM/FCF.
   공급업체 압박·규제·물류비·보안 리스크를 감점.

5. 태양광은 정책 수혜만으로 Green 금지.
   관세·통관·부품 공급망 리스크가 강한 4C.

6. 보험은 EPS 폭발형이 아니라 PBR-ROE-환원형.
   손해율·CSM·자본비율·환원이 핵심.

7. 의료AI는 논문·PoC만으로 Green 금지.
   허가·수가·병원 도입·매출화가 필요.

8. 보안은 구조적 수요가 있지만 대형 장애는 hard 4C.

9. 배터리/ESS는 Green보다 과열 방어가 중요.
   ESS 전환은 후보지만 EV 수요 둔화는 반례.

10. 증권사는 거래대금 cycle 성격이 강해 Watch 중심.
```

---

# cases_v06 추가 후보

```text
RAIL_INFRASTRUCTURE:
- hyundai_rotem_morocco_rail_order_success_candidate
- rail_policy_no_contract_counterexample
- reconstruction_rail_theme_event_watch
- rail_project_margin_delay_4c

CLOUD_AI_SOFTWARE_INFRA:
- douzone_bizon_cloud_erp_candidate
- ai_feature_no_fcf_counterexample
- cloud_cost_margin_pressure_4c
- saas_churn_counterexample

CRO_CLINICAL_SERVICE:
- cro_revenue_backlog_candidate
- charles_river_funding_crunch_4c
- biotech_customer_budget_cut_counterexample
- cro_customer_diversification_success_candidate

RETAIL_ECOMMERCE_LOGISTICS:
- coupang_logistics_scale_candidate
- coupang_farfetch_loss_counterexample
- coupang_supplier_regulation_risk
- ecommerce_fresh_loss_counterexample

SOLAR_TARIFF_SUPPLYCHAIN:
- qcells_us_supply_chain_candidate
- qcells_customs_detention_4c
- solar_subsidy_dependency_counterexample
- solar_component_tariff_risk

INSURANCE_UNDERWRITING_CYCLE:
- samsung_fire_underwriting_valueup_candidate
- sgi_guarantee_insurance_candidate
- sgi_ransomware_operational_risk_4c
- low_pbr_insurer_no_capital_return_counterexample

DIGITAL_HEALTHCARE_AI:
- mammography_ai_workflow_candidate
- medical_ai_no_reimbursement_counterexample
- hospital_ai_poC_no_revenue_counterexample
- medical_ai_liability_risk_4c

SECURITY_IDENTITY_DEEPFAKE:
- recurring_security_subscription_candidate
- crowdstrike_outage_4c
- deepfake_regulation_stage1_candidate
- security_theme_no_contract_counterexample

BATTERY_RECYCLING_ESS_SHIFT:
- ess_shift_candidate
- ev_demand_slowdown_4c
- battery_recycling_no_volume_counterexample
- solid_state_no_commercialization_counterexample

SECURITIES_BROKERAGE_CYCLE:
- brokerage_trading_value_rally_candidate
- securities_pf_loss_4c
- ipo_pipeline_recovery_candidate
- vc_exit_market_weakness_counterexample
```

---

# 지금 상태 판단

이제 점수비중은 많이 정교해지고 있다.
특히 이번 라운드에서 중요한 건, **Green 가능 archetype과 Watch/Red archetype의 경계가 더 선명해졌다**는 점이야.

```text
Green 가능성이 상대적으로 높음:
클라우드/SaaS, 철도 대형수주, 보험 underwriting, 의료AI 일부, 보안 일부

Watch 중심:
CRO, 증권사, 유통/e-commerce, 태양광, 배터리 ESS

Red/4C 방어 중요:
CrowdStrike류 보안 장애, Qcells류 공급망 차질, Charles River류 funding crunch, Coupang류 규제/비용 리스크
```

아직 production scoring은 금지다.
다음 단계는 계속 같은 루프야.

```text
성공/반례 추가
→ 점수비중 교정
→ cases_v06/v07 확장
→ price path backfill
→ shadow scoring
→ 틀린 archetype 재보정
```

지금 방향은 맞고, 더 많은 성공/반례를 쌓을수록 점수정규화가 점점 실제 시장에 가까워질 거야.

[1]: https://www.reuters.com/markets/deals/hyundai-rotem-wins-15-billion-order-moroccos-national-rail-operator-2025-02-26/?utm_source=chatgpt.com "Hyundai Rotem wins $1.5 billion order from Morocco's national rail operator"
[2]: https://www.reuters.com/world/asia-pacific/swedish-firm-eqt-shells-out-930-million-slice-south-koreas-douzone-bizon-2025-11-07/?utm_source=chatgpt.com "Swedish firm EQT shells out $930 million for a slice of South Korea's Douzone Bizon"
[3]: https://www.reuters.com/business/healthcare-pharmaceuticals/charles-river-cuts-2024-forecast-funding-crunch-among-biotech-clients-persists-2024-08-07/?utm_source=chatgpt.com "Charles River cuts 2024 forecast as funding crunch among biotech clients persists"
[4]: https://www.wsj.com/articles/coupang-1q-profit-drops-hit-by-farfetch-acquisition-87ac9527?utm_source=chatgpt.com "Coupang 1Q Profit Drops, Hit by Farfetch Acquisition"
[5]: https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-watchdog-fines-coupang-16-million-pressuring-suppliers-delaying-2026-02-26/?utm_source=chatgpt.com "South Korea watchdog fines Coupang $1.6 million for pressuring suppliers, delaying payments"
[6]: https://apnews.com/article/f49d0579e0584d689f1feec36ff16ad1?utm_source=chatgpt.com "South Korean solar firm cuts pay and hours for Georgia workers as US officials detain imports"
[7]: https://www.reuters.com/sustainability/climate-energy/qcells-furloughs-1000-workers-us-solar-factories-due-stalled-shipments-2025-11-08/?utm_source=chatgpt.com "Qcells furloughs 1,000 workers at US solar factories due to stalled shipments"
[8]: https://en.wikipedia.org/wiki/Samsung_Fire_%26_Marine_Insurance?utm_source=chatgpt.com "Samsung Fire & Marine Insurance"
[9]: https://en.wikipedia.org/wiki/Seoul_Guarantee_Insurance?utm_source=chatgpt.com "Seoul Guarantee Insurance"
[10]: https://arxiv.org/abs/2504.05636?utm_source=chatgpt.com "A Multi-Modal AI System for Screening Mammography: Integrating 2D and 3D Imaging to Improve Breast Cancer Detection in a Prospective Clinical Study"
[11]: https://en.wikipedia.org/wiki/CrowdStrike?utm_source=chatgpt.com "CrowdStrike"
[12]: https://www.theguardian.com/technology/article/2024/jul/24/crowdstrike-outage-companies-cost?utm_source=chatgpt.com "CrowdStrike global outage to cost US Fortune 500 companies $5.4bn"
