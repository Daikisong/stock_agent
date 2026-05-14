좋아. 이번 라운드는 **Round 8: 빈 archetype 보강 + 점수-주가 정합성 기준 강화 + “성공사례로 넣으면 안 되는 후보” 걸러내기**로 진행할게.

현재 레포 기준으로는 아직 scoring을 바꾸면 안 되는 상태가 맞아. 28A taxonomy는 `fixture_only: True`, mapped symbols 13개, archetypes used 8개뿐이고, case library도 25개 archetype 중 **2개 성공 + 2개 반례**를 충족한 항목이 0개야. 그래서 지금 해야 할 일은 “점수 구현”이 아니라, **성공/반례 케이스를 더 채우고, 그 케이스에서 점수와 주가 경로가 실제로 맞았는지 검증할 수 있게 만드는 것**이야.

기존 정신은 그대로 유지해야 해. 핵심은 **산업 구조 변화 → EPS/FCF 체급 변화 → 시장의 과거 프레임 오해 → 밸류에이션 리레이팅 → 논리 훼손 전까지 보유**야. 이 순서가 깨지면, 아무리 주가가 올랐어도 정통 E2R 성공사례가 아니야.

---

# 0. 이번 라운드의 추가 원칙

이번부터 case library에는 단순히 `성공`, `반례`만 넣으면 부족해. 반드시 아래 판정을 같이 넣어야 해.

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
- credit_relief_rally
- policy_event_rerating

price_pattern:
- straight_rerating
- stair_step_rerating
- cycle_boom_bust
- theme_overheat
- accounting_trust_break
- event_premium
- credit_relief_rally
- reopening_cycle
- policy_contract_delay
```

성공사례 인정 조건은 더 빡세게 둬야 해.

```text
성공사례 =
Stage 1/2 신호 발생
+ EPS/OP/FCF 또는 수주/수출/가격/마진 증거
+ Stage 2/3 이후 6~24개월 내 의미 있는 주가 리레이팅
+ 주가 상승이 테마가 아니라 실적/계약/수출/ROE/환원과 연결
+ 4B/4C 신호도 사후 설명 가능
```

반대로 아래는 반례로 넣어야 해.

```text
반례 =
점수상 좋아 보였지만 주가 리레이팅 없음
또는 주가는 올랐지만 EPS/FCF 미동행
또는 이벤트 프리미엄 종료 후 하락
또는 Stage 3처럼 보였지만 4C가 빨리 옴
```

---

# 1. Turnaround / Cost Restructuring

## 핵심 구조

턴어라운드는 “적자에서 흑자 전환” 자체가 아니라, **비용구조가 바뀌어서 EPS/FCF 체급이 지속적으로 올라가는가**가 핵심이야.

```text
적자사업 제거 / 고정비 절감 / 구조조정
→ OPM 개선
→ OP 흑자전환
→ FCF 개선
→ 시장이 아직 부실기업 프레임으로 평가
→ 리레이팅
```

## 성공 후보

| 케이스               | 분류   | 봐야 할 것                            |
| ----------------- | ---- | --------------------------------- |
| 적자사업 매각 기업        | 성공후보 | 매각 후 고정비 감소, OP 흑자전환, FCF 개선      |
| 플랫폼/제조 비용구조 개선 기업 | 성공후보 | 매출 성장 없이도 비용구조가 바뀌어 OPM 상승        |
| 구조조정 후 순현금 전환 기업  | 성공후보 | 부채 감소와 FCF 개선이 같이 나타나는지           |
| 일회성 비용절감 기업       | 반례   | 비용이 1회성으로 줄었지만 매출/마진 구조가 안 바뀌면 실패 |
| 구조조정 실패 기업        | 반례   | 유동성 악화, 부채 증가, 유증/CB 반복           |

## Stage 기준

```text
Stage 1:
적자 축소
비용절감 발표
사업부 매각
인력 구조조정
부채 리파이낸싱

Stage 2:
OP 흑자전환
FCF 개선
순차입금 감소
비용구조 개선이 2분기 이상 확인

Stage 3:
매출 성장과 비용구조 개선이 동시에 발생
OPM이 과거 밴드를 벗어남
시장에 아직 부실/저마진 프레임이 남아 있음

4B:
턴어라운드가 모두에게 알려짐
밸류에이션 정상화
비용절감 효과가 peak-out

4C:
적자 재발
유동성 악화
유증/CB
매출 둔화로 고정비 레버리지 역회전
```

## 점수비중

```text
EPS/FCF: 22
Visibility: 18
Bottleneck/Pricing: 5~8
Mispricing: 15
Valuation: 12
Risk penalty: debt / liquidity / one-off cost cut
```

## 주가-점수 검증

```text
성공:
Stage 2 흑자전환 이후 6~18개월 내 주가 리레이팅
OPM 개선이 2~4분기 이상 지속
FCF가 실제로 개선

반례:
1회성 비용절감 후 주가만 반등
다음 분기에 적자 재발
유동성 이슈로 주가 하락
```

---

# 2. Commodity Spread 세분화

Commodity는 하나로 묶으면 너무 거칠어. 최소한 아래 4개로 나눠야 해.

```text
A. Refining / Oil Spread
B. Chemical Spread
C. Steel / Metal Spread
D. Rare Metals / Strategic Materials
```

## 2-1. Refining / Oil Spread

```text
정제마진 상승
→ 재고평가이익/OP 개선
→ 하지만 유가·수요·공급에 민감
```

### Stage 기준

```text
Stage 1:
정제마진 상승
유가/제품가격 spread 개선
재고평가이익 가능성

Stage 2:
OP/EPS 상향
가동률 상승
수요 개선

Stage 3:
매우 제한적
구조적 공급부족 또는 장기 cost advantage 필요

4B:
정제마진 peak
모두가 정유 호황 인정

4C:
정제마진 하락
수요 둔화
재고 손실
```

### 점수비중

```text
EPS/FCF: 20
Visibility: 10~12
Bottleneck/Pricing: 18
Mispricing: 10
Valuation: 10
Cyclical risk: 강함
```

## 2-2. Chemical Spread

화학은 중국 공급과잉이 핵심 반례야.

```text
제품가격 상승
→ 원가와 spread 개선
→ 하지만 중국 증설/수요 둔화 시 빠르게 붕괴
```

### 반례 조건

```text
중국 공급과잉
가동률 하락
제품 spread reversal
재고 증가
```

화학은 Stage 3-Green을 매우 제한해야 해. “싸다”와 “spread가 좋아졌다”만으로는 E2R 성공이 아니다.

## 2-3. Steel / Metal Spread

철강도 단순 가격 상승보다 **원가, 중국 공급, 수요, 배당/자본배분**을 같이 봐야 해.

```text
Stage 2:
철강 가격 상승
원가 안정
OP/EPS 상향

Stage 3:
구조적 공급조절
수요 회복 장기화
cost curve advantage
```

## 2-4. Rare Metals / Strategic Materials

Korea Zinc처럼 단순 commodity가 아니라 **전략소재 + 제련마진 + 거버넌스 + 공개매수**가 섞이면 별도 archetype으로 둬야 해. MBK/Young Poong 공개매수 발표 후 Korea Zinc 주가는 19.8% 상승했고, 이건 `event_premium`과 `strategic_materials_rerating`을 분리해 봐야 하는 사례야. ([Reuters][1])

Korea Zinc의 18억 달러 신주발행 계획이 금융당국의 정정요구로 중단되며 주가가 8% 하락한 사례는, 경영권 이벤트가 4C 또는 hard RedTeam 신호로 바뀔 수 있음을 보여줘. ([Reuters][2])

### 점수비중

```text
EPS/FCF: 18
Visibility: 16
Bottleneck/Pricing: 15
Mispricing: 16
Valuation: 15
Governance/event risk: 별도 강한 penalty
```

---

# 3. Auto / Mobility Components 세분화

Auto는 완성차와 부품을 분리해야 해.

```text
A. Completed Vehicle / Shareholder Return
B. Mobility Components / ADAS / EV parts
C. EV Demand Slowdown Counterexample
```

## 3-1. Completed Vehicle

현대차는 단순 자동차 경기주가 아니라 **하이브리드 전환 + 판매 목표 + 주주환원 + 밸류 할인 해소**를 같이 보는 케이스야. 현대차는 2030년 판매량 30% 증가 목표, 하이브리드 라인업 확대, 2025~2027년 최대 4조원 자사주 매입, 배당 확대 계획을 발표했어. ([Reuters][3])

### Stage 기준

```text
Stage 1:
하이브리드/EV 전략 변화
판매 목표 상향
주주환원 발표

Stage 2:
OP/EPS 상향
고마진 mix
북미/글로벌 판매 호조
자사주/배당 실행

Stage 3:
ROE/FCF 지속성
valuation discount 해소
자본배분 개선
과거 경기민감/저PBR 프레임 제거

4B:
주주환원과 mix 개선이 모두 반영
관세/정책 리스크 부각
peak margin 우려

4C:
수요 둔화
관세/정책 리스크
원가 상승
리콜/품질 비용
```

### 점수비중

```text
EPS/FCF: 20
Visibility: 18
Bottleneck/Pricing: 10
Mispricing: 15
Valuation: 17
Capital Allocation: 10
```

## 3-2. Mobility Components

부품주는 완성차보다 더 위험해. **고객 다변화와 원가전가**가 핵심이다.

```text
성공 조건:
ADAS/전장 비중 증가
고객사 다변화
OPM 개선
원가전가 가능

반례:
EV 수요 둔화
단일 고객 의존
원가전가 실패
재고 증가
```

---

# 4. Financial / Value-Up / Shareholder Return

금융주는 EPS 폭발보다 **ROE-PBR-자본비율-주주환원** 프레임이 핵심이다.

## 성공 후보

```text
KB금융
신한지주
하나금융
메리츠금융
삼성화재
DB손해보험
```

## 반례

```text
단순 저PBR 금융주
ROE 낮은 은행
PF/충당금 리스크 금융
자본비율 낮은 보험/증권
```

SK Square는 금융은 아니지만 value-up/holding archetype에서 좋은 케이스야. SK Square는 SK Hynix 지분가치 대비 저평가 상태에서 자사주 매입·소각과 독립이사 선임을 발표했고, Reuters는 이 조치가 Value-Up 프로그램 및 Palliser Capital의 undervaluation 해소 요구와 연결된다고 보도했어. ([Reuters][4])

## Stage 기준

```text
Stage 1:
value-up 공시
자사주/배당
저PBR

Stage 2:
ROE 개선
CET1/자본비율 안정
충당금 안정
환원정책 실행

Stage 3:
PBR-ROE 프레임 변화
반복 환원정책
credit risk 낮음
시장에 아직 value trap 프레임 존재

4B:
PBR 정상화
모두가 value-up 성공주로 인정

4C:
credit cost 증가
PF 부실
자본비율 악화
환원정책 후퇴
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

## 주가-점수 검증

```text
성공:
ROE 유지/상승 + PBR 리레이팅 + 자사주/배당 실행

반례:
저PBR이지만 ROE 낮고 환원정책 없음
주가 반등 후 credit cost 증가
```

---

# 5. CDMO / Healthcare Contract

이건 바이오와 분리해야 해. 삼성바이오로직스 같은 CDMO는 임상 바이오가 아니라 **장기계약 + capacity + 글로벌 고객 + 가동률** archetype에 가깝다.

Samsung Biologics는 GSK로부터 미국 Rockville 생산시설을 2억 8천만 달러에 인수해 첫 미국 생산거점을 마련하고, 60,000L drug substance capacity를 확보한다고 발표했어. 이건 장기 미국 수요 대응과 capacity 확장의 Stage 1/2 신호로 볼 수 있어. ([Reuters][5])

## 성공 후보

```text
Samsung Biologics
Celltrion
Samsung Bioepis
글로벌 CDMO 비교군: Lonza, WuXi Biologics 등
```

## 반례

```text
가동률 하락
계약 지연
patent/litigation
가격경쟁
capacity 과잉
```

## Stage 기준

```text
Stage 1:
대형 생산계약
capacity 확장
미국/글로벌 생산거점 확보

Stage 2:
가동률 상승
매출/OP 상향
장기계약
고객사 다변화

Stage 3:
다년 생산 visibility
높은 FCF conversion
계약/가동률/마진 동시 개선
시장에 아직 고정비/바이오 할인 프레임 존재

4B:
capacity 기대 과열
valuation 포화
신규 설비 기대 모두 반영

4C:
가동률 하락
계약 지연
patent/litigation
가격경쟁
```

## 점수비중

```text
EPS/FCF: 20
Visibility: 24
Bottleneck/Pricing: 12
Mispricing: 12
Valuation: 12
Risk: litigation / capacity utilization
```

---

# 6. Royalty / Drug Commercialization Biotech

이건 pre-revenue biotech과 다르다. 핵심은 **approval → commercialization → royalty/revenue**야.

## 성공 후보

```text
유한양행 / Lazertinib
알테오젠
기술이전 후 royalty visibility 있는 기업
```

## 반례

```text
임상 뉴스만 있는 바이오
기술이전 headline만 있고 royalty 불명확
CB/유증 반복
partner 계약 해지
```

## Stage 기준

```text
Stage 1:
임상/허가/기술이전 뉴스

Stage 2:
approval 가능성
milestone payment
partner validation

Stage 3:
실제 매출/로열티
EPS/FCF 전환
dilution risk 낮음
반복 revenue visibility

4B:
신약 기대가 valuation에 과도 반영
매출화 전 주가 과열

4C:
임상 실패
허가 지연
partner 계약 해지
유증/CB
```

## 점수비중

```text
Pre-revenue:
EPS/FCF 낮게, Green 거의 금지

Royalty:
Visibility = milestone + royalty probability + partner quality

Revenue pharma:
EPS/FCF와 recurring sales로 평가
```

---

# 7. Platform / Software — 네이버/카카오 판별 강화

플랫폼은 **좋은 회사**와 **E2R 성공사례**를 분리해야 해.

Naver는 AI/커머스/광고 회복 논리가 있어도, AI 투자와 GPU 비용이 마진을 누르면 Stage 3 성공이 아니야. Kakao는 플랫폼 자산은 있지만 SM엔터 인수 관련 주가조작 의혹으로 창업자가 체포되며 주가가 하락했고, 이런 governance/legal risk는 4C 또는 RedTeam 신호로 들어가야 해. ([Reuters][6])

## Stage 기준

```text
Stage 1:
MAU/traffic 회복
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
AI 비용이 FCF를 훼손하지 않음
주가가 실제 리레이팅

4B:
AI narrative 과열
multiple expansion 완료
ARPU 성장 둔화

4C:
규제
governance/legal risk
AI 비용 과다
take-rate 하락
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

## 주가-점수 검증

```text
네이버를 성공사례로 넣으려면:
OP/EPS 상향 + FCF 개선 + 주가 리레이팅 필요

카카오는:
플랫폼 자산은 있어도 governance/legal risk가 valuation을 누르면 반례
```

---

# 8. Shipping / Freight Cycle

해운은 EPS 폭발이 가능하지만 구조적 Green은 제한해야 해. Maersk CEO는 2024년 컨테이너 운임이 지속 불가능한 수준까지 떨어졌고, overcapacity가 문제라고 말했다. 이건 HMM류 해운 사이클의 4C 반례로 좋다. ([Reuters][7])

## Stage 기준

```text
Stage 1:
운임 급등
컨테이너 shortage
spot rate spike

Stage 2:
contract freight 반영
OP/EPS 폭발

Stage 3:
구조적 Green 매우 제한
multi-year contract freight와 선복 공급 제약 필요

4B:
운임 peak
신규 선박 공급
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

## 주가-점수 검증

```text
HMM처럼 EPS와 주가가 폭발해도
운임 정상화로 붕괴하면
Stage 3-Green 성공이 아니라 cyclical boom-bust다.
```

---

# 9. Nuclear / SMR / Grid Policy

원전은 유틸리티가 아니라 **정책 + 수주 + 법적 리스크 + 기자재 매출화** archetype이야. 체코 법원이 EDF의 항소로 KHNP와 CEZ의 18bn 달러 원전 계약 서명을 일시 중단한 사례는, 정책·수주 기대가 있더라도 legal risk가 4C 신호가 될 수 있음을 보여준다. ([Reuters][8])

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

4C:
소송 패소/지연
정책 반전
프로젝트 지연
원가 상승
```

## 점수비중

```text
EPS/FCF: 18
Visibility: 22
Bottleneck/Pricing: 8
Mispricing: 14
Valuation: 12
Risk penalty: legal / policy / delay
```

---

# 10. AI Data Center Infrastructure

AI 데이터센터 인프라는 별도 archetype으로 확정하는 게 맞아. 현대차그룹은 한국에 약 6.26bn 달러를 투자해 50,000 GPU 규모 AI 데이터센터, 로봇공장, 수소·태양광 시설을 구축한다고 발표했어. 이건 AI 인프라 capex가 자동차, 로봇, 전력, 데이터센터로 퍼지는 좋은 관찰 사례야. ([Reuters][9])

## 포함 섹터

```text
전력기기
전선
IDC
냉각
서버/PCB
전력망
ESS
통신망
로봇공장/physical AI 인프라
```

## Stage 기준

```text
Stage 1:
데이터센터 capex 뉴스
전력부족/냉각/전력망 키워드

Stage 2:
수주/계약
고객사 capex visibility
OP/EPS revision

Stage 3:
다년 capex visibility
핵심 병목 위치
공급 제약
가격전가력

4B:
AI capex narrative 과열
신규 capacity 과잉 우려

4C:
AI capex cut
데이터센터 지연
전력망/인허가 병목
수주 취소/납품 지연
```

## 점수비중

```text
EPS/FCF: 22
Visibility: 23
Bottleneck/Pricing: 20
Mispricing: 14
Valuation: 12
Risk penalty: AI capex cut / project delay
```

---

# 11. Memory / HBM Capacity — 4B 기준 강화

SK Hynix는 구조적 성공사례이면서 동시에 4B-watch 기준을 잡는 데 매우 중요해. Reuters는 SK Hynix가 AI 수요로 2025년 274%, 2026년 200% 이상 오른 뒤 시총 1tn 달러에 근접했다고 보도했다. 이건 “성공사례”인 동시에, 너무 많이 오른 뒤에는 4B-watch가 필요하다는 신호야. ([Reuters][10])

또 빅테크 고객들이 SK Hynix 공급 확보를 위해 생산라인·EUV 장비 투자 지원과 장기계약, 가격밴드, 선수금 구조를 제안했다는 보도는, 이 archetype의 Stage 3 핵심 증거가 무엇인지 보여준다. ([Reuters][11])

## Stage 3 핵심 증거

```text
HBM 수요
DRAM/NAND 가격 상승
공급규율
장기계약 / 선수금 / price band
CAPA constraint
multiple-year consensus revision
PBR에서 PER 평가 전환
```

## 4B 기준

```text
주가 1~2년 급등
시총/멀티플 포화
고객사 가격 저항
CAPEX 증설 뉴스
모두가 AI memory rerating을 인정
정책/분배/노동 이슈 부각
```

## 4C 기준

```text
HBM/DRAM/NAND 가격 하락
AI capex 둔화
공급과잉
consensus revision down
고객사 주문 축소
```

---

# 12. 이번 라운드의 case-library 추가 후보

에이전트에 넣을 때는 아래를 추가 후보로 보면 돼.

```text
TURNAROUND_COST_RESTRUCTURING:
- 적자사업 매각 성공 기업
- 흑자전환 후 FCF 개선 기업
- 일회성 비용절감 반례
- 유동성 악화 반례

COMMODITY_SPREAD:
- 정유 spread 회복 성공후보
- 화학 중국 공급과잉 반례
- 철강 spread 회복 후보
- 금속가격만 오른 반례

AUTO_MOBILITY:
- 현대차 2024 shareholder return/hybrid case
- 기아 mix/shareholder return case
- 원가전가 실패 부품주 반례
- EV 수요 둔화 부품주 반례

FINANCIAL_VALUE_UP:
- KB금융
- 신한지주
- 메리츠금융
- 삼성화재
- 단순 저PBR value trap 반례
- PF/충당금 리스크 반례

CDMO_HEALTHCARE_CONTRACT:
- Samsung Biologics
- Celltrion
- capacity overbuild 반례
- patent/litigation 반례

PLATFORM_SOFTWARE:
- NAVER 후보/반례
- Kakao governance 반례
- 더존비즈온 후보
- MAU-only platform 반례

SHIPPING_FREIGHT_CYCLE:
- HMM
- Maersk boom/bust
- overcapacity 반례

NUCLEAR_SMR_GRID_POLICY:
- KHNP/체코 원전
- 두산에너빌리티
- 한전기술
- 소송/정책 지연 반례

AI_DATA_CENTER_INFRA:
- HD현대일렉트릭/효성중공업
- LS ELECTRIC/전선
- 이수페타시스
- 냉각/공조 후보
- AI capex cut 반례

MEMORY_HBM_CAPACITY:
- SK Hynix Stage 3 success
- SK Hynix 4B-watch
- Samsung memory recovery candidate
- simple DRAM rebound 반례
```

---

# 13. 이번 라운드의 최종 규칙

이번 라운드에서 가장 중요한 건 이거야.

```text
1. 성공사례는 점수와 주가가 같이 맞아야 한다.
2. 주가만 오른 사례는 event premium / theme overheat / cyclical boom으로 분리한다.
3. EPS만 오른 사례도 지속성 없으면 one-off/cycle로 분리한다.
4. Stage 3-Green은 구조적 visibility가 있는 archetype에만 희귀하게 허용한다.
5. Stage 3-Watch / Stage 2-High를 적극 활용한다.
6. 4B/4C는 archetype별 논리 훼손 조건으로 잡는다.
```

현재까지의 분류를 업데이트하면:

```text
Green 가능:
AI Data Center Infra
Contract/Backlog
Defense
Shipbuilding
Export Consumer
K-Beauty
Memory/HBM
Semi Equipment
CDMO/Healthcare Contract
Medical Device
Financial/Shareholder Return
Turnaround

Watch/Yellow 중심:
Platform
Game/IP
Robotics
Auto/Mobility
Nuclear/SMR
Holding/Governance
Travel/Leisure
Education/Specialty
Rare Metals
Utilities
Royalty Biotech

Red/4B 방어 중심:
Shipping
Commodity
Battery Materials
Construction/Credit
Pre-revenue Biotech
One-off Event
Theme Overheat
```

이제 다음 라운드에서는 이걸 **실제 case record 형태**로 더 변환해야 해. 특히 각 케이스마다 `stage2_date`, `stage3_date`, `stage3_price`, `peak_price`, `MFE/MAE`, `drawdown_after_peak`를 채우는 방향으로 가야, 점수비중이 실제 주가와 맞는지 검증할 수 있다.

[1]: https://www.reuters.com/markets/deals/private-equity-mbk-young-poong-launch-15-bln-tender-offer-korea-zinc-shares-2024-09-13/?utm_source=chatgpt.com "Private equity MBK, Young Poong launch $1.5 bln tender offer for Korea Zinc shares"
[2]: https://www.reuters.com/markets/deals/korea-zincs-share-sale-plan-suspended-due-regulators-revision-request-filing-2024-11-06/?utm_source=chatgpt.com "Korea Zinc's $1.8 bln share sale plan suspended due to regulator's revision order"
[3]: https://www.reuters.com/business/autos-transportation/hyundai-motor-targets-30-rise-sales-by-2030-it-expands-hybrid-lineup-2024-08-28/?utm_source=chatgpt.com "Hyundai targets 30% rise in sales by 2030, as it doubles hybrid lineups"
[4]: https://www.reuters.com/technology/artificial-intelligence/south-koreas-ai-chip-investor-announces-plan-share-buybacks-2024-11-21/?utm_source=chatgpt.com "South Korea's AI chip investor announces plan for share buybacks"
[5]: https://www.reuters.com/business/healthcare-pharmaceuticals/samsung-biologics-buy-us-drug-production-facility-gsk-280-mln-2025-12-21/?utm_source=chatgpt.com "Samsung Biologics to buy US drug production facility from GSK for $280 million"
[6]: https://www.reuters.com/technology/south-korean-court-approves-arrest-warrant-kakao-founder-2024-07-22/?utm_source=chatgpt.com "Founder of South Korea's Kakao arrested for suspected stock manipulation"
[7]: https://www.reuters.com/markets/europe/maersk-ceo-says-container-rates-have-fallen-unsustainable-levels-2024-03-14/?utm_source=chatgpt.com "Container rates drop to unsustainable levels, Maersk CEO says"
[8]: https://www.reuters.com/sustainability/boards-policy-regulation/czech-court-halts-nuclear-plant-signing-with-khnp-after-last-minute-appeal-2025-05-06/?utm_source=chatgpt.com "Czech court halts nuclear plant signing with KHNP after last-minute appeal"
[9]: https://www.reuters.com/business/autos-transportation/hyundai-motor-group-invest-63-bln-ai-data-centre-robot-factory-south-korea-2026-02-27/?utm_source=chatgpt.com "Hyundai Motor Group to invest $6.3 bln in AI data centre, robot factory in South Korea"
[10]: https://www.reuters.com/world/asia-pacific/ai-boom-puts-sk-hynix-cusp-1-trillion-market-value-2026-05-14/?utm_source=chatgpt.com "AI boom puts SK Hynix on cusp of $1 trillion market value"
[11]: https://www.reuters.com/world/asia-pacific/sk-hynix-flooded-with-unprecedented-offers-big-tech-firms-secure-chip-supplies-2026-05-07/?utm_source=chatgpt.com "SK Hynix flooded with unprecedented offers from big tech firms to secure chip supplies"
