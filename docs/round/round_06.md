좋아. 이번 라운드는 **“누락 대섹터를 더 채우면서, 점수와 주가 경로가 맞는지 검증 가능한 구조”**에 초점을 맞춰서 확장할게.

지금 레포의 28A 상태는 아직 뼈대 단계야. taxonomy는 fixture-only이고, mapped symbols 13개, archetype 8개만 쓰고 있으며, case library도 25개 archetype 중 2개 성공 + 2개 반례 조건을 만족한 게 0개야. 그러니까 지금은 scoring 구현보다 **case matrix를 더 깊게 채우는 단계**가 맞다.

기존 정신은 유지해야 해. 핵심은 “좋은 회사 찾기”가 아니라 **산업 구조 변화 → EPS/FCF 체급 변화 → 시장의 과거 프레임 오해 → 밸류에이션 리레이팅 → 논리 훼손 전까지 보유**야.

---

# Round 6 핵심: 대섹터 누락 보정

이번 라운드에서 내가 추가로 확정하고 싶은 대섹터 구조는 이거야.

| 대섹터       | 하위 archetype                                               | 핵심 판단                                  |
| --------- | ---------------------------------------------------------- | -------------------------------------- |
| AI/전력/인프라 | AI Data Center Infra, Contract Backlog, Grid, Cooling, PCB | 구조적 Green 가능. 단, 실제 수주·CAPEX·EPS 확인 필요 |
| 정책/국가전략   | Nuclear/SMR, Defense, Strategic Materials                  | 정책 기대와 실제 계약·매출화 분리                    |
| 자본배분/밸류업  | Financial, Holding/Governance, Shareholder Return          | PBR-ROE-환원 실행이 핵심                      |
| 경기/사이클    | Shipping, Commodity, Construction, Travel                  | EPS 폭발 가능하지만 Green 제한                  |
| 테마/기술 기대  | Robotics, Platform, Game/IP, Biotech                       | 매출화 전 Green 제한                         |
| 반복수출/브랜드  | K-Food, K-Beauty, Medical Device, Consumer Export          | 반복수요·채널·OPM이 있으면 Green 가능              |

이번 라운드에서 특히 중요한 건, **좋아 보이는 기업을 성공사례로 넣지 않는 것**이야. 점수상 높게 줬는데 Stage 3 이후 주가가 안 오르거나, 오르더라도 EPS/FCF가 따라오지 않으면 그건 성공사례가 아니라 **점수비중 실패 사례**로 넣어야 해.

---

# 1. AI Data Center Infrastructure

## 왜 별도 archetype인가

이건 전력기기 하나로 묶으면 안 돼. AI 데이터센터 CAPEX는 전력기기, 전선, 냉각, 서버, PCB, IDC, ESS, 전력망까지 동시에 움직이는 구조야.

```text
AI 데이터센터 증설
→ 전력/냉각/서버/네트워크/전력망 병목
→ 다년 CAPEX
→ 수주잔고와 EPS 상향
→ 시장이 기존 산업재 프레임으로 봄
→ 리레이팅
```

## 성공 후보

| 케이스                   | 판단                                                                                                                                         |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| HD현대일렉트릭 / 효성중공업      | 전력망·변압기 수요. 기존 Contract Backlog와 겹치지만 AI DC 인프라 하위로도 들어가야 함                                                                                |
| LS ELECTRIC / LS전선 관련 | 전력망, 전선, 배전, 데이터센터 전력 연결                                                                                                                   |
| 이수페타시스                | AI 서버/네트워크 PCB. 반도체 장비와 다른 DC 인프라 supply chain                                                                                             |
| 냉각/공조 관련 기업           | 데이터센터 cooling exposure 확인 필요                                                                                                               |
| 현대차그룹 AI 데이터센터/로봇공장   | 현대차그룹은 2026년 한국에 약 6.3bn 달러 규모 AI 데이터센터와 로봇공장 투자를 발표했고, AI 데이터센터는 5만 GPU 규모로 보도됐다. 이건 자동차 본업이 아니라 AI 인프라 CAPEX case로 봐야 한다. ([Reuters][1]) |

## 반례

```text
- AI 데이터센터 테마만 붙은 기업
- 실제 수주/납품 exposure 없음
- CAPEX 기대가 주가에 먼저 반영
- 데이터센터 프로젝트 지연
- 고객사 AI CAPEX cut
```

## Stage 기준

```text
Stage 1:
AI 데이터센터 CAPEX 뉴스
전력부족/냉각/전력망 키워드
거래대금 급증

Stage 2:
수주/계약
고객사 CAPEX visibility
OP/EPS revision
공식 공시 또는 리포트 evidence

Stage 3:
다년 CAPEX visibility
핵심 병목 위치
공급 제약
가격전가력
FY1/FY2/FY3 상향

4B:
AI CAPEX narrative 과열
여러 종목 동반 급등
신규 capacity 과잉 우려
리포트 톤 과열

4C:
AI CAPEX cut
데이터센터 지연
전력망/인허가 병목으로 매출 지연
수주 취소/납품 지연
```

## 점수비중 초안

```text
EPS/FCF: 22
Structural Visibility: 23
Bottleneck/Pricing: 20
Market Mispricing: 14
Valuation: 12
Risk penalty: AI CAPEX cut / project delay
```

**주가-점수 검증:**
AI 데이터센터 테마는 주가가 먼저 움직이기 쉽다. 실제 수주·납품·EPS revision이 없으면 Stage 3가 아니라 Theme Overheat로 내려야 한다.

---

# 2. Nuclear / SMR / Grid Policy

## 왜 별도 archetype인가

원전은 유틸리티가 아니라 **정책 + 수주 + 법적 리스크 + 장기 CAPEX + 기자재 매출화** 구조야.

## 성공 후보

| 케이스                    | 판단                                                                                                                                              |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 두산에너빌리티 / 한전기술 / 한전KPS | 체코 원전, 원전 수출, 설계·정비·주기기 매출화 경로                                                                                                                  |
| KHNP 체코 원전             | 체코 법원이 EDF의 항소로 KHNP와 CEZ의 18bn 달러 원전 계약 서명을 일시 중단시켰고, CEZ는 항소하겠다고 밝혔다. 이 케이스는 “정책 기대 → 계약 경로 → 법적 리스크”를 동시에 보여주는 좋은 test case다. ([Reuters][2]) |
| 원전 기자재주                | 실제 기자재 수주와 마진 경로 확인 필요                                                                                                                          |

## 반례

```text
- 수주 기대만 있는 원전 테마주
- 계약 전 기대감으로 주가 선반영
- 소송/정책 지연
- 원가 상승 또는 프로젝트 지연
```

## Stage 기준

```text
Stage 1:
원전 정책
우선협상대상자
SMR 테마

Stage 2:
실제 계약/LOI
project financing
기자재 매출화 경로
법적 리스크 감소

Stage 3:
다년 수주잔고
수익성/마진 확인
법적/정책 리스크 낮음
FY2/FY3 매출화 근거

4B:
원전 기대가 가격에 선반영
테마주 동반 과열
수주 확정 전 과도한 valuation

4C:
소송 패소/지연
정책 반전
프로젝트 지연
원가 상승
```

## 점수비중 초안

```text
EPS/FCF: 18
Visibility: 22
Bottleneck/Pricing: 8
Mispricing: 14
Valuation: 12
Risk penalty: legal / policy / delay
```

**주가-점수 검증:**
원전주는 뉴스 하나로 강하게 오를 수 있지만, 계약 확정과 기자재 매출화가 없으면 Stage 3 성공이 아니라 event premium이다.

---

# 3. Robotics / Factory Automation

## 지금 판단

로봇은 Green 오판 위험이 큰 archetype이야. 대기업 투자와 정책은 Stage 1/2 신호지만, 실제 수주·매출·반복매출 전환 전에는 Green 금지에 가깝다.

## 성공 후보

| 케이스                 | 판단                                                                                                                                 |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Rainbow Robotics    | 삼성전자가 267bn 원 지분 투자로 최대주주가 되었고, CEO 직속 Future Robotics Office를 만들었다. 이건 강한 Stage 1/2 신호지만, 매출·OP 전환 전에는 Green이 아니다. ([Reuters][3]) |
| 현대차그룹 robot factory | 현대차그룹은 AI 데이터센터와 함께 로봇공장 투자를 발표했다. 이는 로봇 theme이 아니라 실제 생산 인프라 후보로 추적해야 한다. ([Reuters][1])                                          |
| Doosan Robotics     | 협동로봇, 글로벌 확장. 다만 상장 후 valuation과 EPS/FCF 괴리 확인 필요                                                                                  |

## 반례

```text
- 무실적 로봇 테마주
- MOU/PoC만 있는 자동화주
- 고밸류 IPO 로봇주
- 로봇 TAM만 강조하고 매출화가 없는 기업
```

## Stage 기준

```text
Stage 1:
대기업 투자
로봇 정책
MOU/PoC
거래대금 증가

Stage 2:
실제 고객사 도입
수주/매출화
gross margin 개선
반복 서비스/소모품 매출

Stage 3:
고객사 다변화
반복 매출 구조
OPM 개선
valuation이 아직 테마가 아니라 산업재/플랫폼 전환을 덜 반영

4B:
humanoid/robotics 과열
EPS보다 주가가 먼저 감
장밋빛 TAM 리포트 남발

4C:
수주 지연
매출화 실패
대기업 투자 철회
현금흐름 악화
```

## 점수비중

```text
EPS/FCF: 18
Visibility: 15
Bottleneck/Pricing: 10
Mispricing: 12
Valuation: 10
Theme penalty: 강하게
```

**검증 규칙:**
로봇은 주가 급등 자체가 성공이 아니다. 대기업 투자 뉴스 이후 실제 매출·수주·OP가 안 붙으면 반례다.

---

# 4. Platform / Software / Internet

## 지금 판단

플랫폼은 “좋은 회사”와 “E2R 성공”을 분리해야 해. 네이버나 카카오를 무조건 성공사례로 넣으면 점수비중이 망가진다.

## 후보/반례

| 케이스         | 판단                                                                                                                                  |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| NAVER       | 광고·커머스·AI 비용효율화가 실제 OP/EPS 상향과 주가 리레이팅으로 이어지는지 확인 전까지는 성공후보만                                                                        |
| Kakao       | 플랫폼 자산은 있지만, 규제·거버넌스·법적 리스크가 valuation rerating을 막을 수 있음. Kakao 창업자 김범수의 SM엔터 주가조작 관련 구속/기소 이슈는 플랫폼 risk case로 적합하다. ([Reuters][4]) |
| 더존비즈온       | ERP/SaaS 반복매출, AI/클라우드 전환, OPM 레버리지 확인 필요                                                                                           |
| MAU만 높은 플랫폼 | 트래픽이 수익화되지 않으면 E2R 아님                                                                                                               |

## Stage 기준

```text
Stage 1:
트래픽/MAU 회복
광고/커머스 회복
비용절감
AI/클라우드 신사업

Stage 2:
ARPU 상승
take-rate 상승
OPM 개선
FY1/FY2 OP 상향
반복매출 증가

Stage 3:
recurring revenue lock-in
비용 레버리지
regulation risk 낮음
시장 저성장 플랫폼 프레임
실제 주가 리레이팅

4B:
AI/플랫폼 narrative 과열
multiple expansion 완료
ARPU 성장 둔화

4C:
규제
take-rate 하락
트래픽 감소
AI 비용 과다
governance/legal risk
```

## 점수비중

```text
EPS/FCF: 20
Visibility: 22
Bottleneck/Pricing: 6~8
Mispricing: 16
Valuation: 14
Risk penalty: regulation / AI cost / governance
```

**검증 규칙:**
MAU나 AI 키워드로 점수 높게 줬는데 주가 리레이팅이 없으면 점수 실패다. ARPU·OPM·FCF 가중치를 높이고 트래픽·테마 가중치를 낮춰야 한다.

---

# 5. Game / Content / IP

## 지금 판단

게임·엔터는 신작/IP 기대만으로는 안 돼. 실제 매출화와 반복 monetization이 핵심이다.

## 후보/반례

| 케이스                  | 판단                                                                                                 |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| Krafton              | PUBG/BGMI 글로벌 IP, 인도 exposure. BGMI는 큰 다운로드 기반이 있으나, 규제/ban/relaunch 이력도 있어 반복 IP와 규제 리스크를 같이 봐야 함 |
| Shift Up             | Nikke/Stellar Blade, 높은 OPM 가능성. 단일 신작 의존도를 확인해야 함                                                 |
| HYBE/JYP/SM          | 팬덤/IP/투어 monetization. 다만 아티스트·계약·거버넌스 리스크                                                         |
| SM 인수전/K-pop 경영권 이벤트 | 이벤트 프리미엄과 구조적 EPS/FCF를 분리해야 함                                                                      |

## Stage 기준

```text
Stage 1:
신작/컴백/투어
예약판매
글로벌 흥행 뉴스
다운로드/트래픽 증가

Stage 2:
실제 매출화
OP/EPS 상향
IP 반복성 확인

Stage 3:
IP portfolio
글로벌 monetization
낮은 churn
반복 revenue 구조
시장이 아직 단일 hit 프레임

4B:
신작 흥행 peak
신작 기대 과열
multiple saturation

4C:
신작 실패
핵심 IP 훼손
아티스트/계약 리스크
규제/판호 리스크
```

## 점수비중

```text
EPS/FCF: 20
Visibility: 18
Bottleneck/Pricing: 5~8
Mispricing: 14
Valuation: 12
Risk penalty: hit-driven discount
```

**검증 규칙:**
신작 발표 후 주가가 올라도, 출시 후 OP/EPS가 못 따라오면 성공사례가 아니라 false score / theme overheat다.

---

# 6. Shipping / Freight Cycle

## 지금 판단

해운은 EPS 폭발이 가능하지만 구조적 Green을 매우 제한해야 해. 운임 peak-out 이후 EPS/FCF가 빠르게 무너질 수 있다.

## 케이스

| 케이스                     | 판단                                                                                                                  |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------- |
| HMM 2020~2021           | 운임 급등, 컨테이너 부족으로 EPS 폭발. 다만 구조적 Green보다는 cyclical success                                                           |
| Maersk 2021~2022        | post-pandemic 운임 호황의 글로벌 비교                                                                                         |
| Maersk 2023~2024        | 운임 하락과 과잉공급 반례. Maersk는 2023년에 어려운 컨테이너 환경으로 1만명 감원을 발표했고, 2024년에는 운임이 지속 불가능한 수준으로 떨어졌다고 CEO가 언급했다. ([AP News][5]) |
| Red Sea disruption 2024 | 일시적 운임 반등. 구조적 수요인지 이벤트성인지 분리 필요                                                                                    |

## Stage 기준

```text
Stage 1:
spot freight spike
컨테이너 shortage
운임지수 급등

Stage 2:
contract freight 반영
OP/EPS 폭발
선복 부족

Stage 3:
구조적 Green 매우 제한
multi-year contract freight와 선복 공급 제약 필요

4B:
운임 peak
신규선박 공급
spot/future divergence

4C:
운임 급락
overcapacity
demand slowdown
```

## 점수비중

```text
EPS/FCF: 20
Visibility: 8~10
Bottleneck/Pricing: 18
Mispricing: 8
Valuation: 8
Cyclical risk: 매우 큼
```

**검증 규칙:**
HMM처럼 주가와 EPS가 폭발해도, 운임 정상화로 무너지면 Stage 3-Green 성공이 아니라 cyclical boom-bust다.

---

# 7. Construction / Real Estate / Credit

## 지금 판단

건설은 수주보다 PF·미분양·현금흐름·신용 리스크가 먼저야.

## 케이스

| 케이스                      | 판단                                                                                                                  |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| PF 리스크 해소형 건설사           | 부실 정리 후 cash flow 회복 시 후보                                                                                           |
| 해외 플랜트/인프라 수주형           | 수주 질과 마진 확정 시 후보                                                                                                    |
| Taeyoung E&C / PF stress | 한국 정부는 2024년 고금리와 부동산 부진으로 중소기업·건설사를 돕기 위해 40.6조원 지원책을 발표했고, Taeyoung E&C의 채무 재조정이 유동성 우려 배경으로 언급됐다. ([Reuters][6]) |
| PF delinquency           | 부동산 프로젝트 연체율은 2021년 말 0.37%에서 2023년 말 2.70%로 상승했고, 금융당국은 구조조정 강화를 발표했다. ([Reuters][7])                              |

## Stage 기준

```text
Stage 1:
PF 우려 완화
대형 수주
유동성 지원
낙폭과대

Stage 2:
부실 정리
cash flow 개선
원가율 안정
부채 감소

Stage 3:
매우 제한적
구조조정 후 반복 cash flow
해외수주 마진 확정
PF risk 낮음

4B:
부동산 회복 기대 과열
미분양 risk 무시

4C:
PF 부실
미분양 증가
신용등급 하락
유동성 위기
```

## 점수비중

```text
EPS/FCF: 18
Visibility: 10~12
Bottleneck/Pricing: 5
Mispricing: 12
Valuation: 10
Risk penalty: 매우 큼
```

**검증 규칙:**
건설주 반등은 credit relief rally일 수 있다. PF/미분양/현금흐름이 해결되지 않으면 E2R 성공사례가 아니다.

---

# 8. Auto / Mobility Components

## 지금 판단

자동차는 단순 경기민감이 아니라 **믹스 개선 + 하이브리드 대응 + 주주환원 + valuation discount 해소**가 같이 있으면 E2R 후보가 될 수 있다.

## 케이스

| 케이스           | 판단                                                                                                                               |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Hyundai Motor | 현대차는 2030년 판매량을 2023년 대비 30% 늘리고, hybrid 라인업을 두 배로 확대하며, 2025~2027년 최대 4조원 자사주 매입과 주주환원 확대를 발표했다. 발표 당일 주가도 상승했다. ([Reuters][8]) |
| Kia           | 믹스 개선, 미국 판매, 주주환원 확인 필요                                                                                                         |
| 현대모비스 / HL만도  | 전장/ADAS, 고객 다변화                                                                                                                  |
| EV 수요 둔화 부품주  | CAPA 확장 후 수요 미달 시 반례                                                                                                             |
| 원가전가 실패 부품주   | 매출 증가에도 OPM 훼손                                                                                                                   |

## Stage 기준

```text
Stage 1:
판매/환율/믹스 개선
주주환원 발표
EV/하이브리드 전략 변경

Stage 2:
OP/EPS 상향
high-margin mix
shareholder return 실행

Stage 3:
global share gain
valuation discount 해소
ROE/FCF 지속성
자본배분 개선

4B:
peak margin
관세/policy risk
valuation rerating 완료

4C:
관세/수요둔화
원가 상승
리콜/품질 비용
```

## 점수비중

```text
EPS/FCF: 20
Visibility: 18
Bottleneck/Pricing: 10
Mispricing: 15
Valuation: 17
Capital Allocation: 10
```

**검증 규칙:**
자동차는 주가 상승이 실적과 환원정책에 의해 뒷받침되어야 성공사례다. 단순 EV/하이브리드 narrative는 부족하다.

---

# 9. Holding / Governance / Restructuring

## 지금 판단

지주/거버넌스는 EPS 폭발보다 **NAV discount 해소와 자본배분 실행**이 핵심. 하지만 경영권 분쟁만으로 오른 주가는 event premium일 수 있다.

## 케이스

| 케이스            | 판단                                                                                                                      |
| -------------- | ----------------------------------------------------------------------------------------------------------------------- |
| SK스퀘어 / 삼성물산   | 자회사 가치, 자사주/소각, NAV discount 해소 여부                                                                                      |
| Korea Zinc     | MBK/Young Poong 공개매수 발표 후 주가가 19.8% 급등했다. 이건 governance/event premium case로 좋지만, EPS/FCF 구조 변화와 분리해야 한다. ([Reuters][9]) |
| 자사주 발표만 있는 지주사 | 소각·반복환원 없으면 value trap                                                                                                  |
| 경영권 분쟁만 있는 종목  | 이벤트 종료 후 주가가 꺾이면 Stage 3 실패                                                                                             |

## Stage 기준

```text
Stage 1:
자사주/소각/배당
경영권 분쟁
value-up 공시

Stage 2:
실제 소각
반복 환원정책
자회사 실적 개선
discount 축소 가능성

Stage 3:
governance regime change
반복 환원정책
NAV discount 구조적 해소

4B:
이벤트 프리미엄 반영 완료
공개매수/분쟁 종결

4C:
환원 미이행
자회사 가치 훼손
지배주주 리스크 재부각
```

## 점수비중

```text
EPS/FCF: 10~12
Visibility: 18
Mispricing: 20
Valuation: 25
Capital Allocation: 10
```

**검증 규칙:**
경영권 분쟁으로 주가가 올랐으면 event premium으로 분류하고, 구조적 NAV/환원 변화가 없으면 E2R 성공사례로 넣지 않는다.

---

# 10. Financial Spread / Balance Sheet

## 지금 판단

금융주는 EPS 폭발보다 **ROE-PBR-주주환원** 정합성이 핵심이다.

## 케이스

| 케이스                | 판단                          |
| ------------------ | --------------------------- |
| KB금융 / 신한지주 / 하나금융 | ROE, CET1, 자사주·배당, value-up |
| 메리츠금융 / 삼성화재       | 자본효율, 환원정책, 보험계약마진/ROE      |
| 단순 저PBR 금융주        | ROE/환원정책 없으면 value trap     |
| PF/충당금 리스크 금융      | credit cost 상승이면 4C         |

## Stage 기준

```text
Stage 1:
value-up 공시
자사주/배당
저PBR

Stage 2:
ROE 개선
자본비율 안정
충당금 안정
환원정책 실행

Stage 3:
PBR-ROE 프레임 변화
recurring ROE
shareholder return credible
credit risk 낮음

4B:
PBR이 ROE 대비 정상화
모두가 value-up 성공주로 인정

4C:
credit cost 증가
PF 부실
자본비율 악화
```

## 점수비중

```text
EPS/FCF: 15
Visibility: 20
Bottleneck/Pricing: 5
Mispricing: 15
Valuation: 25
Capital Allocation: 10
```

**검증 규칙:**
저PBR만으로 score를 높이면 실패. ROE, 자본비율, 실제 환원정책이 따라와야 한다.

---

# 11. Biotech / Regulatory

## 지금 판단

바이오는 하나로 묶으면 안 된다.

```text
A. Pre-revenue clinical biotech
B. Royalty / technology-transfer biotech
C. Revenue-generating pharma / CDMO
```

## 케이스

| 케이스           | 판단                                                   |
| ------------- | ---------------------------------------------------- |
| 알테오젠          | 기술이전/SC 제형/로열티 가능성. 실제 royalty visibility 필요         |
| 유한양행          | 신약 허가/로열티/매출화 여부                                     |
| 삼성바이오로직스      | CDMO 장기계약/가동률. 일반 바이오보다 contract backlog healthcare형 |
| 셀트리온          | 바이오시밀러 매출화, 글로벌 판매                                   |
| 임상 뉴스만 있는 바이오 | EPS/FCF 전환 전 Green 금지                                |
| CB/유증 반복 바이오  | dilution risk로 Green 차단                              |

## Stage 기준

```text
Stage 1:
임상/허가/기술이전 뉴스

Stage 2:
milestone payment
허가 가능성
cash runway
매출화 계획

Stage 3:
실제 매출/로열티
EPS/FCF 전환
dilution risk 낮음
반복 revenue visibility

4B:
신약 기대 과열
valuation이 매출화보다 먼저 감

4C:
임상 실패
허가 지연
유증/CB
파트너 계약 해지
```

## 점수비중

```text
Pre-revenue:
EPS/FCF 낮게, Green 거의 금지

Royalty/tech transfer:
Visibility = milestone + royalty probability

CDMO/revenue pharma:
EPS/FCF + contract visibility로 평가 가능
```

**검증 규칙:**
바이오는 주가가 급등해도 매출화 전이면 E2R 성공사례가 아니라 regulatory/event premium이다.

---

# 12. Travel / Leisure / Reopening

## 지금 판단

리테일과 분리해야 한다. 여행·카지노·항공·면세는 reopening/recovery 성격이 강하고 사이클성이 크다.

## 케이스

| 케이스                | 판단                                   |
| ------------------ | ------------------------------------ |
| 파라다이스 / GKL        | 카지노 drop amount, 일본/중국 VIP, 관광객 회복   |
| 호텔신라 / 신세계         | 면세·관광 회복, 중국 의존도 확인                  |
| 대한항공 / 제주항공        | 여객 회복, 유가, 환율, 화물 정상화                |
| 중국 단체관광 기대만 있는 면세주 | actual traffic/매출 없이 기대만 있으면 Stage 1 |
| 유가 급등 항공주          | 수요는 좋아도 마진 훼손                        |

## Stage 기준

```text
Stage 1:
출입국 회복
관광객 증가
카지노 drop / 면세 매출

Stage 2:
OP/EPS 상향
fixed cost leverage
고마진 고객 mix

Stage 3:
반복 관광/구조적 방문객 증가
중국 의존도 낮음
비용/유가 안정

4B:
reopening 기대 모두 반영
관광객 peak

4C:
경기 둔화
유가/환율 악화
중국/규제 리스크
```

## 점수비중

```text
EPS/FCF: 18
Visibility: 14
Bottleneck/Pricing: 5
Mispricing: 12
Valuation: 10
Cyclical risk cap
```

**검증 규칙:**
Reopening 주가 급등은 구조적 E2R이 아닐 수 있다. traffic peak 후 EPS가 꺾이면 cycle trade다.

---

# 13. Education / Specialty Services

## 지금 판단

교육·시험·특수서비스는 플랫폼도 소비재도 아니다. 반복 수강, 정책, 가격 인상, 성인교육/해외 확장, B2B 구독이 핵심이다.

## 케이스

| 케이스          | 판단                     |
| ------------ | ---------------------- |
| 메가스터디교육      | 입시/사교육 반복수요, 가격, 수강생 수 |
| 웅진씽크빅 / 대교   | 학습지/에듀테크, 반복매출         |
| 자격시험/특수교육 기업 | 정책/시험 수요 증가 가능         |
| 저출산 TAM 축소   | 장기 수요 감소               |
| 정책 규제        | 사교육 규제, 가격 제한          |
| AI 튜터 경쟁     | 가격 하락과 차별화 약화          |

## Stage 기준

```text
Stage 1:
정책 변화
학생 수/수강생 증가
가격 인상

Stage 2:
반복매출
OPM 개선
비용 효율화

Stage 3:
구조적 lock-in
해외/성인교육 확장
저출산 리스크 상쇄

4C:
정책 규제
학생 수 감소
가격 하락
```

## 점수비중

```text
EPS/FCF: 18
Visibility: 20
Bottleneck/Pricing: 5
Mispricing: 12
Valuation: 12
Risk: population / regulation
```

**검증 규칙:**
학생 수 감소를 가격 인상과 성인/해외 확장이 상쇄하는지 봐야 한다. 단순 정책 수혜는 Stage 1~2.

---

# 14. 이번 라운드에서 정리된 “가격-점수 정합성” 규칙

앞으로 case library는 이걸 반드시 기록해야 한다.

```text
score_price_alignment:
- aligned
- false_positive_score
- missed_due_to_score
- price_moved_without_evidence
- evidence_good_but_price_failed

rerating_result:
- true_rerating
- cyclical_rerating
- event_premium
- theme_overheat
- no_rerating
- thesis_break

price_pattern:
- straight_rerating
- stair_step_rerating
- cycle_boom_bust
- theme_overheat
- accounting_trust_break
- event_premium
- credit_relief_rally
- reopening_cycle
```

성공사례로 인정하려면:

```text
Stage 2/3 신호 이후 주가가 6~24개월 안에 리레이팅
EPS/OP/FCF revision이 주가 상승과 동행
상승이 테마가 아니라 실적/계약/수출/ROE/환원과 연결
4B/4C 신호가 이후 가격 경로를 설명
```

반례로 넣어야 하는 경우:

```text
점수상 좋아 보였지만 주가 리레이팅이 안 됨
주가는 올랐지만 EPS/FCF가 안 따라옴
Stage 3처럼 보였지만 4C가 빨리 옴
이벤트 프리미엄 종료 후 주가 하락
```

---

# 15. 다음에 꼭 채워야 할 실제 price-path 항목

다음에 에이전트가 데이터를 넣을 때는 case마다 아래가 필요해.

```text
stage1_price
stage2_price
stage3_price
stage4b_price
stage4c_price
peak_price

MFE_30D
MFE_90D
MFE_180D
MFE_1Y
MFE_2Y

MAE_30D
MAE_90D
MAE_180D
MAE_1Y
MAE_2Y

below_stage3_price_flag
time_to_50pct
time_to_100pct
drawdown_after_peak
```

이게 들어가야 “네이버를 플랫폼 성공사례로 점수 높게 줬는데 주가가 안 갔다” 같은 오류를 자동으로 잡을 수 있어.

---

# 16. 이번 라운드 후 분류 업데이트

## Green 가능성이 상대적으로 높은 archetype

```text
AI Data Center Infrastructure
Contract / Backlog Industrial
Defense / Government Backlog
Shipbuilding / Offshore Backlog
Export / Recurring Consumer
K-Beauty / Export Distribution
Memory / HBM Capacity
Semi Equipment / Advanced Packaging
Medical Device / Healthcare Export
Financial Spread / Shareholder Return
Turnaround / Cost Restructuring
```

## Stage 3-Watch / Yellow 중심 archetype

```text
Platform / Software
Game / Content / IP
Robotics / Factory Automation
Auto / Mobility
Nuclear / SMR / Grid Policy
Holding / Governance
Travel / Leisure
Education / Specialty Services
Rare Metals / Strategic Materials
Utilities / Regulated Tariff
```

## Red / 4B 방어 중심 archetype

```text
Shipping / Freight Cycle
Commodity Spread
Battery Materials / Capex Overheat
Construction / Real Estate / Credit
Pre-revenue Biotech
One-off Event Demand
Theme / Valuation Overheat
```

---

# 17. 다음 라운드에서 더 볼 곳

아직 덜 채워진 곳은 이거야.

```text
1. Commodity Spread 세부 사례
   - 정유/화학/철강/비철 각각 성공·반례

2. Turnaround / Cost Restructuring
   - 실제 구조조정 성공 사례와 일회성 비용절감 반례

3. Financial Spread
   - KB/신한/메리츠/삼성화재의 실제 ROE-PBR-환원 price-path 확인

4. Biotech 세분화
   - 알테오젠/유한양행/삼성바이오/셀트리온
   - 임상 뉴스만 있는 반례

5. Medical Device
   - 클래시스/휴젤/파마리서치/원텍 price-path 확인

6. Platform
   - 네이버/카카오/더존이 실제 E2R 성공인지 반례인지 주가와 실적으로 확인

7. Rare Metals / Strategic Materials
   - Korea Zinc event premium과 구조적 FCF rerating 분리

8. AI Data Center Infra
   - 전력기기/전선/냉각/PCB/IDC를 하나의 supply chain으로 case화
```

---

# 18. 결론

이번 라운드에서 가장 중요한 정리는 이거야.

> **점수비중은 반드시 주가 경로로 검증되어야 한다.**
> **점수는 높은데 Stage 3 이후 주가가 리레이팅되지 않았다면, 그 archetype 점수비중은 틀린 것이다.**

그리고 다음의 방향이 확정된다.

```text
- 플랫폼/게임/로봇/바이오는 Green보다 false-positive 방어가 중요.
- 해운/건설/commodity는 EPS 폭발이 있어도 cycle/credit cap이 필요.
- 금융/지주사는 EPS보다 ROE/PBR/환원/NAV discount가 핵심.
- 원전/AI 데이터센터/희소금속은 별도 archetype으로 분리해야 함.
- 성공사례와 반례는 반드시 price-path validation을 포함해야 함.
```

이렇게 계속 확장하면, 나중에 에이전트에 넣을 때 단순한 종목 나열이 아니라 **섹터별 Stage 1→2→3→4B/4C 정합성 테이블**로 들어갈 수 있어.

[1]: https://www.reuters.com/business/autos-transportation/hyundai-motor-group-invest-63-bln-ai-data-centre-robot-factory-south-korea-2026-02-27/?utm_source=chatgpt.com "Hyundai Motor Group to invest $6.3 bln in AI data centre, robot factory in South Korea"
[2]: https://www.reuters.com/sustainability/boards-policy-regulation/czech-court-halts-nuclear-plant-signing-with-khnp-after-last-minute-appeal-2025-05-06/?utm_source=chatgpt.com "Czech court halts nuclear plant signing with KHNP after last-minute appeal"
[3]: https://www.reuters.com/technology/samsung-electronics-becomes-largest-shareholder-south-koreas-rainbow-robotics-2024-12-30/?utm_source=chatgpt.com "Samsung Electronics becomes largest shareholder of South Korea's Rainbow Robotics"
[4]: https://www.reuters.com/technology/south-korean-court-approves-arrest-warrant-kakao-founder-2024-07-22/?utm_source=chatgpt.com "Founder of South Korea's Kakao arrested for suspected stock manipulation"
[5]: https://apnews.com/article/848c5822bf1e684e612cb4dc77a7da2e?utm_source=chatgpt.com "Shipping company Maersk to slash 10,000 jobs, citing the difficult container trade environment"
[6]: https://www.reuters.com/markets/asia/south-korea-prepares-financial-support-small-businesses-builders-2024-03-27/?utm_source=chatgpt.com "South Korea prepares financial support for small businesses, builders"
[7]: https://www.reuters.com/markets/asia/south-korea-tightens-scrutiny-speed-up-real-estate-restructuring-2024-05-13/?utm_source=chatgpt.com "South Korea tightens scrutiny to speed up real estate restructuring"
[8]: https://www.reuters.com/business/autos-transportation/hyundai-motor-targets-30-rise-sales-by-2030-it-expands-hybrid-lineup-2024-08-28/?utm_source=chatgpt.com "Hyundai targets 30% rise in sales by 2030, as it doubles hybrid lineups"
[9]: https://www.reuters.com/markets/deals/private-equity-mbk-young-poong-launch-15-bln-tender-offer-korea-zinc-shares-2024-09-13/?utm_source=chatgpt.com "Private equity MBK, Young Poong launch $1.5 bln tender offer for Korea Zinc shares"
