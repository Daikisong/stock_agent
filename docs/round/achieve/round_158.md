좋아. **R12 Loop 9까지 끝났으니, 이번은 R13 Loop 9 — Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리**다.

R13은 새 섹터가 아니라 **R1~R12에서 만든 후보를 마지막으로 통과시키는 검문소**다. Theme Tag Map 기준으로도 각 섹터는 이미 Green 가능 영역과 Event/Watch/Red 영역이 나뉘어 있고, R13의 역할은 후보들이 진짜 서생원식 구조 변화인지, 아니면 테마·사이클·이벤트·4B·4C인지 재분류하는 것이다.

서생원식 핵심은 “좋아 보이는 종목”이 아니라 **산업의 성격이 바뀌면서 EPS/FCF가 폭발적으로 올라가고, 시장이 아직 과거 프레임으로 낮은 밸류에이션을 주는 구간**을 찾는 것이다. R13은 이 공식을 모든 라운드에 다시 덮어씌운다.

그리고 공시·데이터 검증도 여기서 최종 gate가 된다. 단일판매·공급계약, 신규시설투자, 잠정실적, 영업실적 전망, 유상증자, CB/BW, 감사의견, 거래정지, 계약 해지·정정 같은 watch disclosure는 detail에서 계약금액, 계약기간, 상대방, 매출 대비 계약금액, OP YoY, 희석률을 실제 확인해야 한다. 없는 값은 만들지 않고, routine disclosure는 cheap-scan positive를 만들면 안 된다.

---

# R13 Loop 9. Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리

## 1. 이번 라운드 대섹터

```text
R13 = Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리

Loop 9 목표 =
R1~R12 후보를

structural success
4B
4C
cycle
event premium
evidence-good-but-price-failed
disclosure-capped
false-positive

로 최종 재분류
```

R13은 산업군이 아니다.
R1~R12에서 나온 후보를 아래 순서로 검문한다.

```text
sector candidate
→ sector score
→ evidence check
→ disclosure confidence
→ RedTeam overlay
→ price-path validation
→ final case_type
```

이번 R13 Loop 9의 핵심 질문은 이것이다.

```text
이 후보는 진짜 EPS/FCF 체급 변화인가?

아니면 가격만 먼저 움직인 테마인가?
```

R13 stage는 이렇게 고정한다.

```text
Stage 1:
테마·정책·기술·수요 변화가 처음 포착된 구간

Stage 2:
계약, 수주, 고객, 매출, guidance, 처방량, ARR, backlog, 정부주문 등
검증 가능한 증거가 붙은 구간

Stage 3:
EPS/FCF·ROE·AFFO·OPM 같은 이익 체급 변화와
실제 가격경로가 동행한 구간

Stage 4B:
논리는 맞지만 모두가 인정해서 valuation room이 줄어든 구간

Stage 4C:
회계, 운영, 법적, 부채, 상업화, 가격경쟁, 정책 shock으로
논리가 훼손된 구간
```

R13 Loop 9에서 최종적으로 강제할 규칙은 이거다.

```text
Stage 3-Green은 점수만으로 나오면 안 된다.

필수:
1. EPS/FCF 또는 동등한 현금흐름 지표
2. 구조적 지속성
3. 시장의 과거 프레임 오해
4. disclosure detail
5. 가격경로 alignment
6. 4B valuation room
7. 4C hard flag 부재
```

---

## 2. 대상 canonical archetype

| canonical archetype                | 역할                             | 최종 처리             |
| ---------------------------------- | ------------------------------ | ----------------- |
| `STRUCTURAL_SUCCESS_ALIGNED`       | EPS/FCF와 가격경로가 같이 맞은 진짜 구조적 성공 | Green 유지 가능       |
| `STRUCTURAL_SUCCESS_BUT_4B_WATCH`  | 구조는 맞지만 이미 시장이 대부분 인정          | 졸업·과열 감시          |
| `PRICE_ONLY_RALLY`                 | 주가만 오르고 EPS/FCF 증거 없음          | Green 금지          |
| `EVENT_PREMIUM`                    | 정책·재난·공개매수·질병·MOU로 오른 가격       | Event로 분리         |
| `EVENT_TO_CONTRACT_ESCALATION`     | 이벤트가 실제 계약·정부주문·매출로 승격         | Stage 2 후보        |
| `CYCLICAL_SUCCESS`                 | 운임·원자재·spread·가격 cycle로 이익 발생  | structural과 분리    |
| `EVIDENCE_GOOD_BUT_PRICE_FAILED`   | 증거는 있었지만 주가 리레이팅 실패            | valuation/프레임 재검토 |
| `DISCLOSURE_CONFIDENCE_CAPPED`     | 계약·고객·금액·기간·마진 detail 부족       | Stage 3 제한        |
| `REDTEAM_ACCOUNTING_TRUST_OVERLAY` | 감사·공시·내부통제·회계 신뢰도 문제           | hard gate         |
| `OPERATIONAL_TRUST_BREAK`          | 보안장애·운영사고·대형 고객 피해             | hard gate         |
| `LEGAL_REGULATORY_REDTEAM`         | 소송·규제·청소년 안전·허가 불확실            | hard/soft gate    |
| `LEVERAGE_FCF_BREAKDOWN`           | 부채·FCF 적자·refinancing 압박       | Green 금지          |
| `COMMERCIALIZATION_FAILURE`        | 허가·승인 후 매출화 실패                 | 4C                |
| `AFFO_CASHFLOW_INTEGRITY_RISK`     | REIT/부동산 현금흐름 착시               | hard review       |
| `CAPEX_AFFO_DILUTION_RISK`         | CAPEX가 per-share AFFO보다 빠르게 증가 | REIT/infra 감점     |
| `CIRCULAR_AI_FINANCING_WATCH`      | 공급자·투자자·고객이 얽힌 AI funding 구조   | hard review       |
| `STABLECOIN_CONVERTIBILITY_RISK`   | 준비금·상환·de-peg·run risk         | hard gate         |
| `POLICY_MARKET_SHOCK_EVENT`        | 세금·분배·규제 발언으로 crowded trade 훼손 | 4B/4C overlay     |
| `UNKNOWN_INSUFFICIENT_EVIDENCE`    | 증거 부족                          | Stage 3 금지        |

---

## 3. deep sub-archetype

```text
STRUCTURAL_SUCCESS_ALIGNED
- EPS/OP/FCF 상향
- 중장기 guidance 상향
- 장기계약
- 수주잔고
- capacity bottleneck
- 반복매출
- OPM 개선
- capital return
- 가격경로 상승

STRUCTURAL_SUCCESS_BUT_4B_WATCH
- 모두가 새 프레임 인정
- 주가 1~2년 급등
- 목표가 과밀 상향
- valuation band 포화
- EPS 상향보다 multiple 확장이 먼저 감
- 신규 진입자·CAPA 증설 증가

PRICE_ONLY_RALLY
- 주가만 급등
- 계약 없음
- 매출 없음
- EPS/FCF 없음
- SNS·정책·MOU·논문만 있음
- 테마 basket 동반 상승

EVENT_PREMIUM
- 공개매수
- 경영권 분쟁
- 정책 발표
- 재건회의
- 질병 뉴스
- 관광정책
- 재난 뉴스
- 단기 가격반응

CYCLICAL_SUCCESS
- 원자재 가격 상승
- 운임 상승
- 정제마진 상승
- 계란·육계·사료 가격 급등
- 금·구리·리튬 가격 상승
- peak 이후 정상화 가능성

REDTEAM_ACCOUNTING_TRUST_OVERLAY
- 감사인 사임
- 감사보고서 지연
- 내부통제 문제
- 회계조작 의혹
- SEC/DOJ/금감원 조사
- 관련자거래 의혹

OPERATIONAL_TRUST_BREAK
- 보안 업데이트 장애
- 글로벌 서비스 중단
- 고객 피해
- 고객 소송
- 갱신율 하락
- 플랫폼 신뢰도 훼손

COMMERCIALIZATION_FAILURE
- 승인 후 uptake 부진
- 처방량 부진
- 보험·환급 실패
- 환자 수 부족
- cash runway 부족
- going concern
- discounted take-private

AFFO_CASHFLOW_INTEGRITY_RISK
- maintenance capex 착시
- expansion capex 과다
- AFFO 과대계상 의혹
- 배당 커버리지 약화
- tenant concentration
- funding cost 상승

CIRCULAR_AI_FINANCING_WATCH
- GPU vendor 투자
- customer·supplier 겸업 구조
- unused capacity guarantee
- GPU collateral debt
- customer concentration
- FCF negative
- refinancing risk

POLICY_MARKET_SHOCK_EVENT
- AI windfall tax
- citizen dividend
- 세금·분배 발언
- 정책 해명 필요
- crowded trade unwind
- index-wide selloff
```

---

## 4. 성공사례

### 4-1. SK하이닉스 HBM — R13 기준 `STRUCTURAL_SUCCESS_ALIGNED`, 동시에 4B 감시

SK하이닉스는 R13에서 가장 명확한 구조적 성공 사례다. AI 서버용 HBM과 기존 메모리 수요가 실제 이익 체급과 시가총액을 바꿨고, Reuters는 SK하이닉스 주가가 2025년에 274%, 2026년에 200% 이상 상승해 시가총액 약 9,420억 달러에 근접했다고 보도했다. 이것은 “메모리 = 과거 시클리컬” 프레임이 “메모리 = AI 인프라 병목” 프레임으로 바뀐 가격경로다. ([Reuters][1])

```text
case_type:
STRUCTURAL_SUCCESS_ALIGNED
+
STRUCTURAL_SUCCESS_BUT_4B_WATCH

stage 포착:
Stage 1 = AI 서버 메모리·HBM 병목
Stage 2 = HBM 매출·점유율·OP/EPS 상향
Stage 3 = EPS 체급 변화 + valuation frame 전환 + 주가 리레이팅
Stage 4B = 2025년 +274%, 2026년 +200% 이상

가격경로 판정:
점수표가 매우 잘 맞았다.
서생원식 구조 변화, EPS 폭발, 시장 프레임 전환, 가격경로가 모두 동행했다.
```

**정규화 결론**

```text
HBM식 성공사례는 R13에서 Green 유지 가능.
하지만 Stage 4B 이후에는 “좋은 구조”와 “아직 싼 구조”를 분리한다.
```

---

### 4-2. GE Vernova — R1 산업재 후보가 R13에서도 structural success로 통과한 사례

GE Vernova는 전력장비·가스터빈·grid equipment 수요가 단순 수주 뉴스가 아니라 backlog, margin guide, power/electrification profit, 주가로 연결된 사례다. 회사는 2026년 매출 전망을 445억~455억 달러, adjusted EBITDA margin을 12~14%로 올렸고, backlog는 1,630억 달러로 늘었으며, 발표 후 주가는 13% 넘게 상승했다. 동시에 wind 부문 매출 감소·손실 확대와 tariff cost는 RedTeam으로 남는다. ([Reuters][2])

```text
case_type:
POWER_EQUIPMENT_BACKLOG_TO_FCF
+
STRUCTURAL_SUCCESS_ALIGNED
+
SEGMENT_DRAG_WATCH

stage 포착:
Stage 1 = AI data-center 전력수요, grid 병목
Stage 2 = backlog 증가, revenue/margin guide 상향
Stage 3 = power/electrification profit 개선 + 주가 +13%
Stage 4C-watch = wind loss, tariff cost

가격경로 판정:
R1에서 잡은 stage가 R13 price-path 검증도 통과했다.
단, good case ≠ risk-free case.
```

**정규화 결론**

```text
수주잔고가 EPS/FCF와 가격경로로 연결되면 structural.
하지만 segment drag가 있으면 4B 이후 방어 점수를 낮춘다.
```

---

### 4-3. Datadog / Fortinet / Cisco — AI가 SW를 “대체”한 게 아니라 특정 infra SW의 매출을 키운 사례

Datadog은 AI workload monitoring·observability가 실제 revenue/guidance/가격경로로 연결된 사례다. 2026년 1분기 매출은 전년 대비 32% 증가했고, 연간 revenue guidance는 43억~43.4억 달러로 상향됐으며, 주가는 약 30% 급등했다. ([Barron's][3])

Fortinet도 AI-driven cyber threat와 networking-security convergence가 billings/revenue/EPS로 연결된 사례다. 2026년 1분기 revenue는 전년 대비 20% 증가했고, billings는 31% 증가했으며, 주가는 22% 상승했다. ([마켓워치][4])

Cisco는 AI networking orders가 가격경로와 연결된 crossover 사례다. hyperscaler AI infrastructure orders는 fiscal year-to-date 53억 달러, full-year expectation은 90억 달러로 올라갔고, 발표 후 주가는 extended trading에서 16% 이상 상승했다. ([Investors][5])

```text
case_type:
AI_INFRA_SOFTWARE_SUCCESS_BASKET
+
ARR_BILLINGS_ORDERS_ALIGNED

공통 stage 포착:
Stage 1 = AI가 SW를 먹는다는 공포 / AI infra 수요 narrative
Stage 2 = revenue, billings, AI orders, guidance 확인
Stage 3 후보 = ARR/FCF/retention/renewal 확인 필요
Stage 4B-watch = 단기 급등, consensus 과밀

가격경로 판정:
AI 기능 출시가 아니라,
AI workload를 지탱하는 monitoring/security/networking 수요가 숫자로 확인됐을 때 가격이 움직였다.
```

**정규화 결론**

```text
R8에서는 AI SW를 두 갈래로 나눈다.

좋은 쪽:
AI workload 증가 → ARR/billings/orders 증가

나쁜 쪽:
AI agent가 기존 seat/license를 대체
```

---

### 4-4. Circle / USDC — regulated stablecoin infra는 Stage 2~3 후보지만 4B 감시

Circle은 regulated fiat-backed stablecoin infrastructure가 실제 수익 모델로 연결될 수 있음을 보여준다. 2026년 1분기 revenue/reserve income은 전년 대비 20% 증가한 6.94억 달러였고, USDC circulation은 28% 증가한 770억 달러였다. Barron’s는 Q1 실적 이후 주가가 14.8% 상승했고, Circle이 AI-agent payment, nanopayment, wallet, developer tools 같은 option value를 제시했다고 보도했다. ([Barron's][6])

다만 Circle은 단순한 “스테이블코인 테마”가 아니라 reserve income, circulation, redemption, regulation을 모두 통과해야 한다. WSJ 보도 기준으로도 Circle은 Arc token presale로 2.22억 달러를 조달했고, Arc는 USDC settlement를 중심으로 한 stablecoin-based network로 설명됐다. 이것은 option value이지만, Stage 3로 가려면 non-reserve fee revenue와 규제경제학까지 확인돼야 한다. ([월스트리트저널][7])

```text
case_type:
REGULATED_STABLECOIN_INFRA_STAGE2_3_CANDIDATE
+
STABLECOIN_AI_AGENT_PAYMENT_OPTION
+
STRUCTURAL_SUCCESS_BUT_4B_WATCH

stage 포착:
Stage 1 = stablecoin 제도권 편입·디지털금융 narrative
Stage 2 = USDC circulation, reserve income, regulatory framework 확인
Stage 3 후보 = reserve income 증가 + 주가 반응 + 반복 사용성
Stage 4B = IPO 이후 주가 급등, AI payment option 선반영 가능성

가격경로 판정:
regulated fiat-backed stablecoin infra stage는 가격상승과 맞았다.
하지만 rate sensitivity, issuer margin, redemption risk, regulation을 계속 봐야 한다.
```

**정규화 결론**

```text
stablecoin은 반드시 분리한다.

regulated fiat-backed stablecoin
≠ algorithmic stablecoin
≠ STO 테마
≠ 블록체인 이름만 붙은 관련주
```

---

### 4-5. Bayer Crop Science — R12 농업 input도 IP/licensing이면 구조 후보가 될 수 있음

Bayer는 R12에서 보기 드문 구조 후보 사례다. 2026년 1분기 adjusted EBITDA는 9% 증가한 44.5억 유로로 시장 예상 39.3억 유로를 웃돌았고, Corteva와의 soy seed licensing dispute 해결 효과로 Crop Science EBITDA가 17.9% 증가해 30억 유로가 됐다. 이건 단순 “식량안보 테마”가 아니라 seed/IP/licensing이 실제 EBITDA로 연결된 Stage 2 사례다. ([Reuters][8])

```text
case_type:
AGRI_INPUT_LICENSED_IP_SUCCESS_STAGE2

stage 포착:
Stage 1 = 식량안보·종자·작물보호제 narrative
Stage 2 = soy seed licensing dispute resolution + Crop Science EBITDA +17.9%
Stage 3 = 반복 licensing revenue, litigation 비용 통제, FCF 확인 필요
Stage 4C-watch = Roundup litigation, 규제·특허 리스크

가격경로 판정:
R12에서도 “생활필수·농업”이라는 이름이 아니라,
IP/licensing → EBITDA로 연결될 때만 구조 후보가 된다.
```

---

### 4-6. BXDC — 성공이 아니라 “Stage 1~2에서 멈춰야 하는 좋은 예시”

Blackstone Digital Infrastructure Trust는 AI 데이터센터 real asset 수요가 capital market vehicle로 만들어지는 사례다. BXDC는 17.5억 달러 IPO를 했고, Blackstone은 1,500억 달러 규모 data center assets portfolio와 약 250억 달러 near-term opportunities를 제시했다. 하지만 상장 첫날 주가는 IPO 가격 20달러와 같은 수준으로 flat하게 출발했고, Reuters는 아직 데이터센터 자산을 취득하지 않은 상태라 투자자는 Blackstone의 execution capability를 사는 구조라고 설명했다. ([Reuters][9])

```text
case_type:
DATA_CENTER_REIT_IPO_NO_ASSET_STAGE1_2
+
DISCLOSURE_CONFIDENCE_CAPPED

stage 포착:
Stage 1 = AI data-center real asset demand
Stage 2 후보 = IPO funding, sponsor premium, acquisition pipeline
Stage 3 금지 = asset 없음, tenant 없음, NOI/AFFO 없음
가격경로 = IPO debut flat

가격경로 판정:
시장은 AI real asset 가능성은 인정했지만,
자산·tenant·NOI/AFFO가 없으면 강한 리레이팅을 주지 않았다.
```

**정규화 결론**

```text
sponsor premium은 Stage 1~2 가점일 뿐이다.

Stage 3 조건:
asset acquired
+ binding lease
+ NOI/AFFO
+ power/water secured
+ dividend coverage
```

---

## 5. 반례

### 5-1. Supermicro — AI 서버 성장도 회계 신뢰가 깨지면 hard 4C

Supermicro는 R13의 가장 중요한 회계 신뢰도 반례다. EY가 감사인에서 사임하자 Supermicro 주가는 33% 급락했고, EY는 transparency, internal control, management integrity 관련 우려를 제기했다. 이 사안은 Hindenburg의 회계조작 주장과 annual report filing delay, DOJ probe 보도 이후 이어졌다. ([AP News][10])

```text
case_type:
AI_SERVER_RERATING_THEN_ACCOUNTING_HARD_4C

stage 포착:
Stage 1~2 = AI server revenue growth
Stage 3 후보처럼 보였음
Stage 4C = auditor resignation, filing delay, internal control concern

가격경로 판정:
회계 RedTeam이 실제 -30% 이상 주가 하락과 맞았다.
성장률이 아무리 좋아도 회계 신뢰도 gate를 통과하지 못하면 Green은 끝난다.
```

**정규화 결론**

```text
auditor_resignation_flag = hard 4C
filing_delay_flag = hard 4C
internal_control_issue_flag = hard 4C

이 셋은 EPS/매출 성장보다 우선한다.
```

---

### 5-2. CrowdStrike — 보안 ARR도 운영 신뢰가 깨지면 hard 4C

CrowdStrike는 R8과 R13을 잇는 운영 신뢰도 반례다. 2024년 7월 flawed software update가 글로벌 outage를 일으켰고, 800만 대 이상 컴퓨터가 영향을 받았으며, CrowdStrike 주가는 12일 동안 32% 하락해 약 250억 달러 시가총액이 사라졌다. 이후 shareholder class action과 Delta Air Lines 소송도 이어졌다. ([Reuters][11])

```text
case_type:
OPERATIONAL_TRUST_BREAK_HARD_4C

stage 포착:
Stage 1~2 = cybersecurity ARR / AI threat demand / platform trust
Stage 4C = global outage, faulty update, customer damage, shareholder lawsuit
가격경로 = 12일 -32%, 약 $25B 시총 소멸

가격경로 판정:
보안 반복매출은 trust가 살아 있을 때만 반복매출이다.
운영 신뢰가 깨지면 Stage 3-Green은 즉시 차단된다.
```

**정규화 결론**

```text
security_outage_flag = hard gate
customer_damage_flag = hard gate
shareholder_lawsuit_flag = hard review
renewal_risk_flag = Stage 3 제한
```

---

### 5-3. Bluebird bio — FDA 승인 후 상업화 실패

Bluebird bio는 승인된 gene therapy를 갖고 있었지만 severe cash crunch로 Carlyle과 SK Capital에 인수되기로 했다. WSJ 보도 기준으로 Bluebird 투자자는 주당 3달러 cash와 조건부 권리를 받는 구조였고, initial consideration은 직전 종가 7.04달러보다 낮았다. 이 케이스는 “승인된 제품”이 있어도 uptake·환급·cash runway가 없으면 Stage 4C로 내려간다는 기준이다. ([월스트리트저널][12])

```text
case_type:
APPROVAL_WITHOUT_COMMERCIALIZATION_4C

stage 포착:
Stage 1 = 희귀질환 gene therapy approval
Stage 2 = 승인된 제품 보유
Stage 4C = slow uptake, reimbursement uncertainty, cash crunch, discounted take-private

가격경로 판정:
approval-only biotech을 Stage 3로 올리면 false-positive다.
R7/R13에서는 commercialization failure가 hard 4C다.
```

**정규화 결론**

```text
approval_status = 필요조건
patient_uptake = 필수
reimbursement_status = 필수
commercial_revenue = 필수
cash_runway_months = 필수

승인만으로 Green 금지.
```

---

### 5-4. Novo Nordisk — 거대한 TAM도 가격·경쟁 압박이 오면 4B에서 4C로 간다

Novo Nordisk는 GLP-1 대형 성장시장 대표였지만, 2026년 sales와 operating profit이 5~13% 감소할 수 있다고 경고했고, Reuters는 미국 상장주가 12% 하락했다고 보도했다. 원인은 미국 가격 압박, 경쟁 심화, semaglutide 특허 만료, copycat drug 압박이었다. ([Reuters][13])

이후 Barron’s는 Novo 주가가 전일 15% 하락한 뒤 다음 날에도 추가 하락했다고 보도했고, The Guardian은 하루 17% 하락과 연간 큰 폭 조정을 언급했다. 즉 거대한 TAM과 기존 고성장도 가격·경쟁·보험·copycat 압박 앞에서는 Stage 4C로 내려갈 수 있다. ([Barron's][14])

```text
case_type:
GROWTH_MARKET_4B_TO_4C

stage 포착:
Stage 1 = obesity GLP-1 mega-TAM
Stage 2~3 = Wegovy/Ozempic revenue growth
Stage 4C = price pressure, competition, sales/profit decline warning

가격경로 판정:
큰 TAM은 Stage 1일 뿐이다.
가격·보험·경쟁·gross-to-net이 깨지면 고성장 시장도 4C로 내려간다.
```

**정규화 결론**

```text
huge_TAM = 가점 아님
scripts = Stage 2 검증
insurance/gross_to_net = Stage 3 gate
price_war = 4C
```

---

### 5-5. Equinix — AI 데이터센터 수요가 진짜여도 AFFO integrity를 통과해야 한다

Equinix는 AI 데이터센터 수요의 수혜 후보이지만, REIT는 AFFO 품질을 통과해야 한다. Hindenburg Research는 Equinix가 maintenance capex를 expansion capex로 분류해 AFFO를 부풀렸다고 주장했고, Reuters 기준 Equinix 주가는 보도 후 약 2% 하락했다. Hindenburg는 이 분류 문제가 2015년 REIT 전환 이후 AFFO를 누적 30억 달러 부풀렸다고 주장했다. ([Reuters][15])

```text
case_type:
AFFO_CASHFLOW_INTEGRITY_RISK

stage 포착:
Stage 1 = AI data-center demand narrative
Stage 2 = AFFO/growth forecast
Stage 4C-watch = maintenance capex misclassification allegation, AFFO integrity risk

가격경로 판정:
AI real asset 수요가 진짜여도 cash-flow quality가 흔들리면 Stage 3가 제한된다.
```

**정규화 결론**

```text
REIT/infra Stage 3 조건:
NOI
AFFO
AFFO per share
maintenance capex
expansion capex
dividend coverage

AFFO 숫자만 보고 Green 금지.
```

---

### 5-6. CoreWeave / Nvidia — 계약 visibility가 있어도 circular financing과 부채를 봐야 한다

CoreWeave류 neocloud는 대형 AI 계약이 visibility를 높이지만, 공급자·투자자·고객 관계가 얽히면 R13 hard review가 필요하다. Reuters는 Nvidia CEO Jensen Huang 부부 재단이 CoreWeave에서 1.083억 달러의 AI computing resources를 구매해 기부했고, Nvidia가 CoreWeave에 20억 달러를 투자했으며, 63억 달러 규모 unused cloud capacity 구매 구조도 있다고 보도했다. 이 구조는 투자자 사이에서 circular financing 우려를 낳았다. ([Reuters][16])

```text
case_type:
CONTRACT_VISIBILITY_BUT_CIRCULAR_FINANCING_WATCH

stage 포착:
Stage 1 = AI compute shortage
Stage 2 = 대형 AI cloud contract / Nvidia-linked capacity
Stage 3 제한 = FCF, debt, utilization, customer diversification 필요
Stage 4C-watch = circular financing, GPU collateral debt, customer concentration

가격경로 판정:
계약 visibility만으로 Stage 3를 올리면 위험하다.
AI infra는 FCF와 부채 구조를 반드시 본다.
```

**정규화 결론**

```text
large_contract_value = Stage 2
FCF negative + debt + circular financing = Stage 3 차단
```

---

### 5-7. Fermi — AI power campus도 no tenant / no revenue면 hard Watch

Fermi는 AI real asset narrative의 대표 반례다. Fermi는 2025년 4.86억 달러 순손실을 발표한 뒤 주가가 종가 기준 13%, 장중 최대 24% 하락했고, flagship Project Matador에는 아직 tenant가 없으며 1.5억 달러 funding agreement도 종료된 것으로 보도됐다. ([Financial Times][17])

```text
case_type:
AI_DATA_CENTER_NO_REVENUE_NO_TENANT_4C_WATCH

stage 포착:
Stage 1 = AI power campus, land, power narrative
Stage 2 미달 = tenant signed 없음, revenue 없음
Stage 4C = net loss, funding agreement terminated, stock drawdown

가격경로 판정:
AI power narrative가 있어도 tenant·revenue가 없으면 Stage 3가 아니다.
R10/R13에서 no-revenue real asset은 강한 cap을 둔다.
```

**정규화 결론**

```text
AI_DATA_CENTER_POWER_CAMPUS는 Stage 1 narrative로만 둔다.

Stage 2 조건:
binding lease
+ financing
+ power secured
+ water/permitting secured

Stage 3 조건:
revenue
+ NOI/AFFO
+ tenant concentration 관리
```

---

### 5-8. Policy market shock — 구조가 맞아도 crowded 4B에서는 정책 발언이 가격경로를 깬다

2026년 5월 12일 한국 증시는 AI 수익·세수 재분배성 발언 이후 KOSPI가 장중 5.1% 하락하고 종가 기준 2.3% 하락했다. 해당 발언은 세율 인상보다는 늘어난 tax revenue 활용 취지였지만, AI 반도체 랠리로 크게 오른 시장을 놀라게 했다. ([마켓워치][18])

Barron’s도 이 발언이 AI windfall tax 또는 citizen dividend로 해석되며 시장을 흔들었고, 대통령실이 개인 의견이라고 선을 그었음에도 KOSPI가 장중 5%가량 하락했다고 보도했다. ([Barron's][19])

```text
case_type:
POLICY_MARKET_SHOCK_EVENT
+
SECTOR_SUCCESS_BUT_POLICY_SHOCK_WATCH

stage 포착:
Stage 1~3 = AI 반도체·밸류업 rally
Stage 4B = crowded trade
Stage 4C-watch = policy comment, tax redistribution concern, market-wide selloff
가격경로 = KOSPI intraday -5.1%, close -2.3%

가격경로 판정:
정책 발언이 기업 EPS를 즉시 훼손하지 않아도,
4B 구간에서는 price-path를 깨는 overlay가 된다.
```

**정규화 결론**

```text
policy_shock_flag = true
crowded_4b_flag = true
market_wide_selloff_flag = true

이면 valuation room을 낮춘다.
```

---

## 6. 지금 점수표로 실제 어떻게 stage를 포착했고, 주가상승·하락과 맞았는지를 통한 점수비중정규화

R13 Loop 9부터 공통 overlay 점수표는 이렇게 둔다.

```text
R13 v9 Cross-archetype overlay = 100점

1. EPS/FCF·ROE·AFFO·OPM 체급 변화        24점

2. 증거 visibility                         20점
   - 계약
   - 수주
   - 고객
   - 처방량
   - ARR
   - billings
   - backlog
   - government order
   - tenant lease

3. 지속성·반복성                           16점
   - 장기계약
   - 반복매출
   - 환원정책
   - 가동률
   - renewal
   - prescription continuity

4. disclosure confidence / RedTeam           12점

5. capital discipline / leverage / FCF       10점

6. 시장 오해·리레이팅 gap                  10점

7. valuation room / 4B 여지                  8점
```

### 6-1. stage별 점수 cap

```text
Stage 1 cap:
최대 45점

조건:
- 테마
- 정책
- MOU
- 논문
- viral
- TAM
- 사용자 수
- 수요 뉴스
- 가격 상승 headline

예:
AI 기능 출시
전고체 뉴스
희토류 수출통제
관광정책
AI data-center REIT IPO
```

```text
Stage 2 cap:
최대 70점

조건:
- 계약
- 고객
- 금액
- 기간
- guidance 상향
- 처방량
- ARR/billings/bookings
- 정부주문
- tenant lease
- 자사주 소각
- PBM/보험 등재

예:
Circle USDC circulation/reserve income
BXDC IPO funding
Bavarian Nordic stockpile
LGES–Tesla Megapack 계약
Samsung HBM4 shipment
```

```text
Stage 3:
70점 이상 가능

조건:
- EPS/FCF·ROE·AFFO·OPM 실제 개선
- 반복성 확인
- 가격경로 상승
- disclosure detail 충분
- RedTeam hard flag 없음

예:
SK하이닉스 HBM
GE Vernova power equipment backlog
Datadog AI observability
Intuitive Surgical recurring instruments/accessories
Samyang Buldak export/ASP/OP revision
```

```text
Stage 4B:
점수는 높아도 기대수익률 감점

조건:
- 이미 시장이 새 프레임 인정
- 주가 1~2년 급등
- valuation이 EPS보다 먼저 확장
- consensus crowded
- 정책 shock에 취약

예:
SK하이닉스 HBM
Circle stablecoin infra
Palantir enterprise AI
Akamai edge AI cloud
APR beauty device
Kioxia NAND
```

```text
Stage 4C:
hard RedTeam

조건:
- 감사인 사임
- 공시 지연
- 내부통제 문제
- 대형 운영장애
- 상업화 실패
- cash crunch
- price war
- contract cancellation
- funding withdrawal
- dividend cut
- AFFO integrity risk
- de-peg
- policy shock
```

---

### 6-2. 실제 가격경로와 맞은 case / 안 맞은 case

| case                      |         점수표가 잡은 stage |                         실제 가격경로 확인 | 판정                             | 정규화 조정                                  |
| ------------------------- | --------------------: | ---------------------------------: | ------------------------------ | --------------------------------------- |
| SK하이닉스 HBM                |            Stage 3→4B |        2025년 +274%, 2026년 +200% 이상 | 매우 잘 맞음                        | EPS/FCF·Bottleneck 상향, valuation 감점     |
| GE Vernova                |            Stage 3 후보 |               outlook 상향 후 +13% 이상 | 매우 잘 맞음                        | backlog→FCF 구조 상향                       |
| Datadog                   |          Stage 2→3 후보 |          Q1 beat·guidance 후 약 +30% | 잘 맞음                           | ARR/guidance/AI infra SW 상향             |
| Fortinet                  |          Stage 2→3 후보 |             billings +31%, 주가 +22% | 잘 맞음                           | billings·security demand 상향             |
| Cisco                     |          Stage 2→3 후보 |    AI orders guide 후 extended +16% | 잘 맞음                           | AI networking orders 상향                 |
| Circle / USDC             |     Stage 2→3 후보 + 4B | Q1 후 +14.8%, USDC circulation +28% | stage 포착 맞음, 4B 강함             | stablecoin infra 상향, rate/regulation 감점 |
| Bayer Crop Science        |          Stage 2→3 후보 |         Crop Science EBITDA +17.9% | R12 구조 후보                      | seed/IP/licensing 상향                    |
| BXDC                      |             Stage 1~2 |                     IPO debut flat | no-asset cap이 맞음               | sponsor premium은 Stage 3 금지             |
| Supermicro                |              Stage 4C |                       EY 사임 후 -33% | accounting gate 매우 잘 맞음        | 회계 hard gate 최상위                        |
| CrowdStrike               |              Stage 4C |               12일 -32%, $25B 시총 소멸 | operational trust gate 매우 잘 맞음 | 보안·플랫폼 trust hard gate                  |
| Bluebird bio              |              Stage 4C |            distressed take-private | commercialization failure      | 승인-only biotech 강등                      |
| Novo Nordisk              |                 4B→4C |                          -12%~-17% | price-war overlay 매우 잘 맞음      | TAM 점수 cap, 가격·보험 가중치 상향                |
| Equinix Hindenburg        |              4C-watch |                              약 -2% | AFFO integrity gate 맞음         | REIT cash-flow quality 강화               |
| CoreWeave/Nvidia          | Stage 2 + hard review |              circular financing 우려 | Green 제한이 맞음                   | AI infra leverage/circular gate         |
| Fermi                     |      Stage 1→4C-watch |        no tenant/no revenue + -13% | real asset cap 맞음              | no-tenant gate 강화                       |
| AI citizen dividend shock |   4B price-path shock |           KOSPI 장중 -5.1%, 종가 -2.3% | policy shock overlay 잘 맞음      | crowded valuation room 감점               |

---

### 6-3. R13 Loop 9 점수비중 재조정

이번 검증 결과 R13 공통 점수표는 이렇게 조정한다.

```text
상향:
EPS/FCF·ROE·AFFO·OPM 실체
가격경로 alignment
회계·감사 hard gate
운영 신뢰 hard gate
상업화 실패 gate
capital/leverage gate
AFFO/cash-flow integrity
policy shock overlay
4B valuation-room 감점

유지:
event-to-contract 승격
cyclical success 분리
disclosure confidence cap
stablecoin convertibility gate
AI infra circular financing watch

하향 또는 cap:
TAM-only
theme-only
price-only rally
policy-only
MOU-only
approval-only
AUC-only
user-count-only
asset-pipeline-only
sponsor-premium-only
```

구체적으로는 이렇게 간다.

| 항목                    | Loop 8 감각 |              Loop 9 조정 |
| --------------------- | --------: | ---------------------: |
| EPS/FCF 체급 변화         |       최상위 |                  유지·강화 |
| 가격경로 alignment        |        중요 |  더 중요. 실제 stage 검증의 핵심 |
| 계약·수주·고객 visibility   |        중요 |   유지. 단 detail 없으면 cap |
| valuation room        |        보조 |            4B 감점축으로 강화 |
| 회계·감사 신뢰도             |        중요 |         hard gate로 최상위 |
| 운영 신뢰도                |        중요 |         hard gate로 최상위 |
| 상업화·처방·환급             |        중요 |          바이오 hard gate |
| AFFO/capex integrity  |        중요 |         REIT hard gate |
| circular AI financing |     Watch |        hard review로 강화 |
| policy shock          |        보조 | crowded 4B overlay로 강화 |

---

### 6-4. 최종 case_type 판정 규칙

```text
STRUCTURAL_SUCCESS_ALIGNED:
점수 높음
+ EPS/FCF·ROE·AFFO·OPM 개선
+ 가격경로 상승
+ disclosure detail 충분
+ hard RedTeam 없음
```

```text
STRUCTURAL_SUCCESS_BUT_4B_WATCH:
구조는 맞음
+ 가격도 이미 크게 상승
+ 시장이 새 프레임을 인정
+ valuation room 감소
```

```text
EVENT_PREMIUM:
정책·질병·재난·MOU·공개매수로 주가 상승
+ 실적·계약·반복매출 없음
```

```text
EVENT_TO_CONTRACT_ESCALATION:
이벤트
+ 실제 계약
+ 정부주문
+ 예산
+ 매출 guidance
```

```text
CYCLICAL_SUCCESS:
가격·운임·spread로 EPS 상승
+ 지속성 낮음
+ peak 이후 drawdown 가능
```

```text
FALSE_POSITIVE_SCORE:
점수는 높았음
+ price-path 실패
+ EPS/FCF 미확인
+ RedTeam 발생
```

```text
EVIDENCE_GOOD_BUT_PRICE_FAILED:
계약·증거는 있음
+ 주가가 반응하지 않음
+ valuation 또는 market-frame 재검토
```

```text
DISCLOSURE_CONFIDENCE_CAPPED:
계약금액·고객명·기간·마진·처방량·tenant·AFFO detail 부족
+ Stage 3 제한
```

```text
HARD_4C_THESIS_BREAK:
회계
운영
상업화
부채
법적
안전
정책 shock
중 하나가 논리를 훼손
```

---

# R13 Loop 9 최종 결론

R13 Loop 9의 결론은 명확하다.

```text
R1~R12는 후보를 만든다.
R13은 후보를 죽인다.
```

좋은 후보를 많이 찾는 것보다 더 중요한 것은, **좋아 보이는 후보 중에서 false-positive를 제거하는 것**이다.

이번 Loop 9에서 최종적으로 확인된 구조는 이거다.

```text
진짜 structural success:
SK하이닉스 HBM
GE Vernova 전력장비
Datadog observability
Fortinet cybersecurity billings
Cisco AI networking
Intuitive Surgical 반복소모품
Samyang Buldak 수출/ASP/OP revision

성공이지만 4B:
SK하이닉스
Circle
Palantir
Akamai
APR beauty device
Kioxia NAND
Datadog 단기 급등 구간

Stage 2지만 아직 Green 아님:
BXDC
Bavarian Nordic
Samsung HBM4
LGES–Tesla ESS
K뷰티 입점
바이오시밀러 PBM/formulary
Zoetis conditional vaccine
Bayer Crop Science

hard 4C:
Supermicro 회계
CrowdStrike 운영 신뢰
Bluebird 상업화 실패
Novo 가격전쟁
Equinix AFFO integrity
CoreWeave circular financing
Coupang trust/security
Whirlpool hardware cycle
Hertz EV fleet economics
LK-99 재현 실패
Fermi no tenant/no revenue
```

**R13 Loop 9 점수정규화의 핵심 문장:**

> Cross-archetype 검증은 “좋아 보이는 후보”를 고르는 단계가 아니라, **좋아 보이는 후보 중에서 실제 EPS/FCF와 가격경로가 맞은 것만 남기고, 테마·사이클·이벤트·회계·부채·운영 신뢰·상업화 실패·정책 shock·공시 detail 부족 리스크를 제거하는 단계**다.

따라서 다음 R1 Loop 10로 돌아가면, 모든 섹터에서 이 공통 규칙을 먼저 깔아야 한다.

```text
Stage 3-Green =
sector score 높음
+ EPS/FCF 체급 변화
+ 반복성
+ 가격경로 alignment
+ disclosure confidence
+ 4B valuation room
+ 4C hard flag 없음
```

이제 **R1~R13 Loop 9 완료**다.
다음 라운드는 규칙대로 **R1 — 산업재·수주·인프라 Loop 10**로 돌아간다.

[1]: https://www.reuters.com/world/asia-pacific/ai-boom-puts-sk-hynix-cusp-1-trillion-market-value-2026-05-14/?utm_source=chatgpt.com "AI boom puts SK Hynix on cusp of $1 trillion market value"
[2]: https://www.reuters.com/business/energy/ge-vernova-lifts-annual-revenue-forecast-data-center-demand-2026-04-22/?utm_source=chatgpt.com "GE Vernova lifts 2026 outlook as AI boom fuels power equipment demand"
[3]: https://www.barrons.com/articles/datadog-earnings-stock-price-c84c9acd?utm_source=chatgpt.com "Datadog Stock Is Having a Record Day. Why 'Observability' Could Be the Next Big Thing."
[4]: https://www.marketwatch.com/story/fortinets-stock-rockets-as-earnings-help-dispel-fears-of-ai-disruption-8a8f0107?utm_source=chatgpt.com "Fortinet's stock rockets higher as earnings help dispel fears of AI disruption"
[5]: https://www.investors.com/research/investing-action-plan/stock-market-week-ahead-dow-jones-breakout-watch/?utm_source=chatgpt.com "Stock Market Week Ahead: Dow Jones Breakout Watch"
[6]: https://www.barrons.com/articles/stablecoin-firm-circle-reports-earnings-on-monday-ai-could-be-in-focus-5bbf8ab8?utm_source=chatgpt.com "Circle Internet Stock Rockets After Earnings. The Stablecoin Company Is Betting on AI."
[7]: https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-05-11-2026/card/circle-raises-222-million-for-new-blockchain-ET1IkQV7VQ3OTxyPpajp?utm_source=chatgpt.com "Circle Raises $222 Million for New Blockchain"
[8]: https://www.reuters.com/business/bayer-q1-operating-profit-up-9-crop-protection-unit-gains-2026-05-12/?utm_source=chatgpt.com "Bayer Q1 operating profit jumps 9% on boost from soy business"
[9]: https://www.reuters.com/technology/blackstone-data-center-vehicle-opens-flat-new-york-debut-after-175-billion-ipo-2026-05-14/?utm_source=chatgpt.com "Blackstone data center vehicle makes muted debut after $1.75 billion IPO"
[10]: https://apnews.com/article/d1cc4377628b3024e659dcfec9318dcd?utm_source=chatgpt.com "Super Micro Computer's shares plunge 33% after server maker's accounting firm quits"
[11]: https://www.reuters.com/legal/crowdstrike-is-sued-by-shareholders-over-huge-software-outage-2024-07-31/?utm_source=chatgpt.com "CrowdStrike is sued by shareholders over huge software outage"
[12]: https://www.wsj.com/articles/bluebird-bio-to-be-acquired-by-carlyle-group-sk-capital-72ace9f9?utm_source=chatgpt.com "Bluebird Bio to Be Acquired by Carlyle Group, SK Capital"
[13]: https://www.reuters.com/business/novo-nordisk-warns-2026-sales-decline-2026-02-03/?utm_source=chatgpt.com "Novo Nordisk warns on profits and sales amid Trump drug price crackdown"
[14]: https://www.barrons.com/articles/novo-nordisk-earnings-stock-price-e4dd7f15?utm_source=chatgpt.com "Novo Nordisk Stock Extends Losses as Ozempic Maker Sees Sales Falling in 2026"
[15]: https://www.reuters.com/business/media-telecom/hindenburg-research-takes-short-position-data-center-operator-equinix-2024-03-20/?utm_source=chatgpt.com "Hindenburg shorts data center firm Equinix alleging inflated profit metric"
[16]: https://www.reuters.com/legal/transactional/nvidia-ceos-foundation-buys-108-million-ai-computing-coreweave-donates-it-2026-05-13/?utm_source=chatgpt.com "Nvidia CEO's foundation buys $108 million of AI computing from CoreWeave, donates it to researchers"
[17]: https://www.ft.com/content/49a8b5c8-d655-4eb8-b0dc-6bd403860925?utm_source=chatgpt.com "Fermi shares plunge 13% on $486mn net loss"
[18]: https://www.marketwatch.com/story/the-hottest-stock-market-in-the-world-finally-met-its-match-taxes-55cf54c6?utm_source=chatgpt.com "The hottest stock market in the world finally met its match: taxes"
[19]: https://www.barrons.com/articles/ai-tax-stock-market-kospi-2e468921?utm_source=chatgpt.com "Why the World's Hottest Stock Market Got Derailed by Talk of an AI Tax"
