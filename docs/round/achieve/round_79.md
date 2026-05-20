좋아. **R12 Loop 3까지 끝났으니, 이번은 R13 Loop 3 — Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리**로 간다.

이번 R13은 새 섹터를 더 파는 라운드가 아니라, **R1~R12 전체 후보를 마지막으로 걸러내는 공통 게이트**다. 지금까지 12개 대섹터는 Theme Tag Map v0.5 기준으로 거의 전 테마를 흡수했고, R13은 그 후보들이 진짜 구조적 E2R인지, 이미 4B 졸업 구간인지, 아니면 테마·사이클·이벤트·회계 리스크인지 분류하는 층이다.

그리고 Checkpoint 20 원칙처럼 계약금액, 계약기간, 매출 대비 계약금액, OP YoY, dilution, 감사의견, 거래정지, 공시 detail 값은 **실제 확인된 필드만 써야 하고 없는 값을 만들면 안 된다.** R13은 이 원칙을 모든 섹터에 강제하는 마지막 방어막이다.

서생원식으로도 R13의 역할은 명확하다. “좋아 보이는 테마”가 아니라 **산업 구조 변화 → EPS/FCF 체급 변화 → 시장의 과거 프레임 오해 → 밸류에이션 리레이팅**이 실제로 연결되는지만 남겨야 한다.

---

# R13 Loop 3. Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리

## 1. 이번 라운드 대섹터

```text
R13 = Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리
Loop 3 목표 = R1~R12 후보를 structural / 4B / 4C / cycle / event / false-positive로 최종 분류
```

R13은 산업군이 아니다.
R1~R12에서 나온 모든 후보를 통과시키는 **최종 검문소**다.

```text
R1~R12 후보 발생
→ sector-aware score 산출
→ evidence merge
→ R13 RedTeam overlay
→ price-path validation
→ 최종 case_type 확정
```

R13 Loop 3에서 고정할 핵심 원칙은 이거다.

```text
점수가 높다
≠ Green

점수가 높고
+ EPS/FCF 증거가 있고
+ 가격경로가 맞고
+ RedTeam hard flag가 없고
+ 4B 과열이 아직 지나치지 않아야
Stage 3 후보가 된다.
```

R13은 특히 세 가지를 잡아내야 한다.

```text
1. 좋은 구조였지만 이미 늦은 4B
2. 처음엔 맞았지만 논리가 깨진 4C
3. 점수는 높았지만 가격경로가 틀린 false-positive
```

---

## 2. 대상 canonical archetype

| canonical archetype                | 역할                             | 최종 처리             |
| ---------------------------------- | ------------------------------ | ----------------- |
| `STRUCTURAL_SUCCESS_ALIGNED`       | EPS/FCF와 가격경로가 같이 맞은 진짜 구조적 성공 | Green 유지 가능       |
| `SECTOR_SUCCESS_BUT_4B_WATCH`      | 구조는 맞지만 이미 시장이 대부분 인정한 상태      | 비중축소·졸업 감시        |
| `PRICE_ONLY_RALLY`                 | 주가만 오르고 근거 없음                  | Green 금지          |
| `EVENT_PREMIUM`                    | 정책·공개매수·재난·질병·MOU로 오른 가격       | Event로 분리         |
| `EVENT_TO_CONTRACT_ESCALATION`     | 이벤트가 실제 계약·주문·매출로 승격           | Stage 2 후보        |
| `CYCLICAL_SUCCESS`                 | 원자재·운임·가격 cycle로 수익 발생         | structural과 분리    |
| `FALSE_POSITIVE_SCORE`             | 점수는 높았지만 EPS/가격경로 검증 실패        | 해당 archetype 재보정  |
| `EVIDENCE_GOOD_BUT_PRICE_FAILED`   | 증거는 있었지만 시장이 리레이팅하지 않음         | valuation/프레임 재검토 |
| `REDTEAM_ACCOUNTING_TRUST_OVERLAY` | 감사·공시·내부통제·회계 신뢰도              | hard gate         |
| `OPERATIONAL_TRUST_BREAK`          | 보안장애·운영사고·대형 고객 피해             | hard gate         |
| `LEGAL_REGULATORY_REDTEAM`         | 규제·소송·청소년 안전·광고품질·허가 불확실       | hard/soft gate    |
| `LEVERAGE_FCF_BREAKDOWN`           | 부채·FCF 적자·refinancing 압박       | Green 금지          |
| `COMMERCIALIZATION_FAILURE`        | 허가·임상 후 매출화 실패                 | 4C                |
| `AFFO_CASHFLOW_INTEGRITY_RISK`     | REIT/부동산 현금흐름 착시               | hard review       |
| `STABLECOIN_CONVERTIBILITY_RISK`   | 준비금·상환·de-peg·run 리스크          | hard gate         |
| `POLICY_MARKET_SHOCK_EVENT`        | 정책 발언·세금·분배 이슈가 price-path 훼손  | 4B/4C overlay     |
| `UNKNOWN_INSUFFICIENT_EVIDENCE`    | 증거 부족                          | Stage 3 금지        |

---

## 3. deep sub-archetype

```text
STRUCTURAL_SUCCESS_ALIGNED
- EPS/OP/FCF 추정치 상향
- 수주잔고·장기계약·CAPA 병목
- OPM 개선
- 컨센서스 상향
- valuation frame 변화
- 가격경로 MFE 우상향

SECTOR_SUCCESS_BUT_4B_WATCH
- 모두가 새 프레임 인정
- 목표가 과밀 상향
- valuation band 포화
- 1~2년 급등
- EPS 상향보다 multiple 확장이 먼저 감
- 신규 진입자·CAPA 증설 증가

PRICE_ONLY_RALLY
- 주가만 급등
- EPS/FCF 증거 없음
- 계약·매출·수주 없음
- 테마명만 있음
- SNS/뉴스 기반 과열

EVENT_PREMIUM
- 공개매수
- 경영권 분쟁
- 정책 발표
- 재난/질병 뉴스
- 재건회의/MOU
- 상장 기대

CYCLICAL_SUCCESS
- 운임 급등
- 원자재 가격 상승
- 정제마진 상승
- 계란·육계·사료 가격 급등
- 금·구리·리튬·화학 spread
- peak 이후 정상화 가능성

REDTEAM_ACCOUNTING_TRUST_OVERLAY
- 감사인 사임
- 감사보고서 지연
- 내부통제 중대결함
- 재무제표 재작성 가능성
- SEC/검찰/규제기관 조사
- 관련자거래 의혹

OPERATIONAL_TRUST_BREAK
- 보안 업데이트 장애
- 고객 피해
- 대형 소송
- 갱신율 하락
- 플랫폼 신뢰도 훼손
- 대형 고객 이탈

LEVERAGE_FCF_BREAKDOWN
- FCF 적자
- 고부채
- debt refinancing pressure
- 이자비용 급등
- 배당 삭감
- going concern
- discounted offering

COMMERCIALIZATION_FAILURE
- FDA/EMA 허가 후 처방 부진
- 보험·환급 실패
- 환자 uptake 부진
- cash runway 붕괴
- discounted take-private

AFFO_CASHFLOW_INTEGRITY_RISK
- maintenance capex 착시
- AFFO 과대계상 의혹
- capex burden
- 배당 커버리지 약화
- REIT funding cost 상승

STABLECOIN_CONVERTIBILITY_RISK
- de-peg
- reserve failure
- redemption failure
- algorithmic stablecoin
- liquidity run
- fraud / market manipulation

POLICY_MARKET_SHOCK_EVENT
- 세금정책 발언
- AI windfall tax
- citizen dividend
- 거래세·양도세·법인세
- 배당세 정책
- 시장 전체 risk premium 급등
```

---

# 4. 성공사례

## 4-1. SK하이닉스 HBM / AI 메모리 — `STRUCTURAL_SUCCESS_ALIGNED + 4B_WATCH`

SK하이닉스는 R13 기준으로 가장 강한 `STRUCTURAL_SUCCESS_ALIGNED` 예시다. AI 서버용 HBM과 전통 메모리 수요가 동시에 붙으면서 SK하이닉스 주가는 2025년 274%, 2026년 200% 이상 상승했고, 시가총액은 약 9,420억 달러까지 올라 1조 달러에 근접했다. 이건 “AI 테마”가 아니라 **HBM 병목 → EPS/FCF 체급 변화 → 시장 프레임 전환 → 가격경로 리레이팅**이 연결된 케이스다. ([Reuters][1])

```text
case_type:
STRUCTURAL_SUCCESS_ALIGNED
+
SECTOR_SUCCESS_BUT_4B_WATCH

이유:
- HBM/메모리 병목이 실제 이익 체급 변화로 연결
- 시장 프레임이 과거 메모리 cycle에서 AI infrastructure로 이동
- 가격경로가 이미 강하게 리레이팅
- 1~2년 급등으로 4B 감시 필요
```

R13 결론은 “좋은 사례이므로 계속 Green”이 아니라, **진짜 성공사례이면서 동시에 4B 감시 대상**이라는 것이다.

---

## 4-2. 한국 상법 개정 / 자사주 소각 강제 — `POLICY_TO_EXECUTION_BACKGROUND`

한국 국회는 2026년 2월 상장사가 새로 취득한 자사주를 1년 안에 소각하도록 하는 상법 개정안을 통과시켰다. 기존 자사주는 6개월 유예기간을 받았고, 개정안은 자사주를 경영권 방어 수단으로 쓰던 관행을 줄이고 소수주주 권리를 강화하려는 Korea Discount 해소 정책의 일부다. ([Reuters][2])

```text
case_type:
POLICY_TO_EXECUTION_BACKGROUND

단, 개별 종목 판정:
정책 발표 = Stage 1
실제 자사주 소각 = Stage 2
ROE/PBR band 변화 + 반복 환원 = Stage 3
```

정책 자체는 구조적 배경이다. 하지만 R13에서는 개별 종목의 **실제 소각·배당·ROE 개선·PBR band 변화**를 다시 확인해야 한다.

---

## 4-3. regulated stablecoin infrastructure — `REGULATED_STABLECOIN_INFRA`

Circle은 regulated fiat-backed stablecoin infrastructure의 좋은 reference다. 2026년 5월 Circle은 USDC 수요와 유통량 증가에 힘입어 분기 revenue/reserve income이 20% 증가한 6.94억 달러를 기록했고, USDC circulation은 전년 대비 28% 증가해 770억 달러가 됐다. Circle은 준비금으로 보유한 미국 국채·은행예금에서 이자수익을 얻는 구조라 금리와 규제에 민감하며, IPO 가격 31달러 대비 주가가 3배 이상 오른 상태라 4B-watch도 같이 붙는다. ([Reuters][3])

```text
case_type:
REGULATED_STABLECOIN_INFRA_SUCCESS_BUT_4B_WATCH

좋은 점:
- fiat-backed stablecoin
- reserve income
- 발행량/circulation 증가
- 규제 프레임워크 수혜 가능성

주의:
- 금리 민감도
- issuer margin 압박
- 준비금·상환 구조 검증 필요
- IPO 이후 valuation 과열
```

R13 기준으로 stablecoin은 반드시 분리한다.

```text
regulated fiat-backed stablecoin
≠ algorithmic stablecoin
≠ STO 테마주
≠ 블록체인 이름만 붙은 관련주
```

---

## 4-4. `EVENT_TO_CONTRACT_ESCALATION` — 이벤트가 실제 계약으로 승격되는 경우

R11에서 본 전염병·재건·폭염 이벤트 중 일부는 Stage 2로 승격될 수 있다. 다만 조건은 매우 엄격하다.

```text
이벤트 뉴스
→ 정부 주문 / stockpile / 예산 / financing / 실제 계약
→ 매출 가이던스 또는 EPS 반영
```

이런 경우만 `EVENT_TO_CONTRACT_ESCALATION`으로 분류한다. 그렇지 않으면 대부분 `EVENT_PREMIUM`이다.

---

# 5. 반례

## 5-1. Supermicro — AI 서버 성장 후 회계신뢰도 hard 4C

Supermicro는 R13의 핵심 반례다. AI 서버 수요로 급등했지만, Ernst & Young이 Supermicro 감사인에서 사임하자 주가가 30% 이상 급락했다. EY는 governance와 financial reporting control에 대한 우려를 제기했고, 이 사안은 Hindenburg의 회계조작 주장, annual report filing delay, DOJ 조사 보도 이후 나왔다. ([Reuters][4])

```text
case_type:
EARLY_RERATING_SUCCESS_THEN_HARD_4C

R13 규칙:
auditor_resignation = hard 4C
filing_delay = hard 4C
internal_control_issue = hard 4C
related_party_risk = hard 4C

처리:
Stage 3-Green 즉시 차단
score_after_redteam 강제 하향
```

이 사례는 R2 AI 서버, R8 SaaS, R10 REIT, R6 금융까지 모두에 적용된다.
**성장률이 아무리 좋아도 회계 신뢰도 게이트를 통과하지 못하면 Green은 끝난다.**

---

## 5-2. CrowdStrike — 보안 ARR 이후 운영 신뢰도 hard 4C

CrowdStrike는 보안 SaaS가 반복매출이어도 운영 신뢰가 깨지면 어떻게 무너지는지 보여준다. 2024년 7월 잘못된 업데이트로 800만 대 이상 컴퓨터가 영향을 받았고, CrowdStrike 주가는 이후 12일 동안 32% 하락해 250억 달러 시가총액이 사라졌다. Delta는 해당 outage로 7,000편 이상 항공편이 취소되고 1.3 million passengers가 영향을 받았다며 약 5억~5.5억 달러 규모 손해를 주장했다. ([위키백과][5])

```text
case_type:
OPERATIONAL_TRUST_BREAK_4C

R13 규칙:
global_outage = hard review
customer_damage = hard review
shareholder_lawsuit = hard review
customer_lawsuit = hard review
renewal_risk = Green 제한
```

R8 보안·SaaS뿐 아니라 R2 AI 인프라, R6 핀테크, R5 이커머스에도 같은 원칙을 적용한다.
**반복매출은 신뢰가 살아 있을 때만 반복매출이다.**

---

## 5-3. Bluebird bio — 허가 후 상업화 실패

Bluebird bio는 승인된 유전자치료제를 갖고 있었지만 severe cash crunch 속에 Carlyle·SK Capital에 주당 3달러로 비상장화되기로 했다. 이 가격은 직전 종가 대비 57.4% 할인된 수준이었고, 발표 후 주가는 36% 하락했다. Reuters는 Bluebird의 gene therapy uptake가 느렸고 cash crunch가 심각했다고 보도했다. ([Reuters][6])

```text
case_type:
APPROVAL_WITHOUT_COMMERCIALIZATION_4C

R13 규칙:
approval_status = 필요조건
patient_uptake = 필수
reimbursement_status = 필수
commercial_revenue = 필수
cash_runway_months 부족 = 4C-watch
going_concern_flag = hard 4C
```

바이오에서 “승인”은 끝이 아니라 시작이다.
R13에서는 허가를 받아도 **처방량·보험·환급·매출·FCF**가 없으면 Green을 막는다.

---

## 5-4. Novo Nordisk — 고성장 시장도 4B에서 4C로 간다

GLP-1은 대형 성장시장처럼 보였지만, Novo Nordisk는 2026년 sales와 profit이 최대 13% 감소할 수 있다고 경고했다. 원인은 미국 가격 압박, 경쟁 심화, weight-loss 시장 내 경쟁, semaglutide 관련 가격·특허 리스크 등으로 설명됐다. 이 뉴스 이후 Novo의 미국 상장 주식은 하락했고, GLP-1 시장도 TAM만으로 방어되지 않는다는 기준 사례가 됐다. ([Reuters][7])

```text
case_type:
GROWTH_MARKET_4B_TO_4C

R13 규칙:
huge_TAM = Stage 1
weekly_scripts = Stage 2 검증
price_pressure = 4B/4C
competition = 4B/4C
insurance/reimbursement risk = Green 제한
```

거대한 TAM도 숫자로 방어되지 않으면 4B에서 4C로 내려간다.

---

## 5-5. Equinix — 데이터센터 REIT AFFO / capex integrity risk

데이터센터 REIT도 AI 수혜라는 이름만으로 Green을 줄 수 없다. Hindenburg Research는 Equinix가 maintenance capex를 expansion capex로 잘못 분류해 AFFO를 부풀렸다고 주장했고, Reuters는 이 주장 공개 후 Equinix 주가가 약 2% 하락했다고 보도했다. ([Reuters][8])

```text
case_type:
AFFO_CASHFLOW_INTEGRITY_RISK

R13 규칙:
AFFO growth = 검증 전까지 불충분
maintenance_capex = 필수
expansion_capex = 필수
dividend_coverage_ratio = 필수
power_constraint = data-center REIT RedTeam
```

R10의 데이터센터 REIT, 콜드체인 REIT, 리츠 전반은 R13에서 AFFO 무결성을 반드시 통과해야 한다.

---

## 5-6. TerraUSD / Luna — algorithmic stablecoin hard 4C

TerraUSD/Luna는 R6 디지털자산에서 절대 잊으면 안 되는 반례다. Do Kwon은 TerraUSD·Luna 붕괴와 관련해 미국에서 fraud 혐의로 15년형을 선고받았고, 해당 붕괴는 400억 달러 이상 투자자 손실과 연결됐다. ([Financial Times][9])

```text
case_type:
ALGORITHMIC_STABLECOIN_THESIS_BREAK

R13 규칙:
algorithmic_stablecoin_flag = hard 4C
depeg_event_flag = hard 4C
reserve_failure_flag = hard 4C
convertibility_risk_flag = hard 4C
```

stablecoin은 이름이 아니라 **준비금·상환·규제·issuer economics**로 봐야 한다.

---

# 6. 4B-watch 사례

4B는 “망했다”가 아니다.
**좋은 논리가 이미 시장에 너무 많이 반영되어 기대수익률이 낮아지는 구간**이다.

## 6-1. AI 메모리 / HBM 4B

```text
4B 조건:
- 1~2년 급등
- 모두가 AI memory rerating 인정
- 시총/valuation band 급상승
- 고객사 가격저항 가능성
- CAPA 증설 뉴스 증가
- EPS 상향은 지속되지만 multiple 확장 여지는 줄어듦
```

SK하이닉스는 구조적으로 맞은 케이스지만, 2025년 274%, 2026년 200% 이상 상승한 가격경로는 동시에 강한 4B 신호다. ([Reuters][1])

---

## 6-2. Korea value-up / 저PBR 4B

```text
4B 조건:
- 모두가 Korea Discount 해소를 인정
- 저PBR주 전반 동반 급등
- 실제 소각·배당보다 PBR band가 먼저 상승
- ROE 개선 전 valuation만 먼저 확장
```

상법 개정은 좋은 구조적 배경이지만, 개별 종목이 실제 소각·배당·ROE 개선을 보여주지 못하면 `VALUEUP_POLICY_PREMIUM`에 머문다. ([Reuters][2])

---

## 6-3. AI 서버·AI 인프라 4B

```text
4B 조건:
- AI 서버/광통신/냉각/전력장비 관련주 동반 급등
- 수주보다 valuation이 먼저 감
- 고객사 concentration 무시
- 회계·공시 신뢰도 무시
- CAPA 정상화 가능성 무시
```

Supermicro는 이 항목의 기준 반례다. AI 서버 매출 성장으로 리레이팅됐어도, 회계 신뢰도 hard flag가 나오면 바로 4C가 된다. ([Reuters][4])

---

## 6-4. GLP-1 / 바이오 고성장 4B

```text
4B 조건:
- 시장규모 narrative 과밀
- 처방량보다 valuation이 먼저 감
- 가격·보험·경쟁·조제약 리스크를 낮게 봄
- 실적 하향 하나로 큰 drawdown
```

Novo Nordisk 사례는 GLP-1도 “거대한 시장”만으로 방어되지 않는다는 기준이다. ([Reuters][7])

---

## 6-5. 데이터센터 REIT / AI real asset 4B

```text
4B 조건:
- AI 데이터센터 수요가 모두에게 알려짐
- 자산·tenant·AFFO 없이 valuation 상승
- capex·funding cost·power/water risk를 무시
- AFFO 품질 검증 전 배당률만 반영
```

Equinix 사례처럼 데이터센터 REIT도 capex 분류와 AFFO 무결성을 통과해야 한다. ([Reuters][8])

---

## 6-6. Stablecoin infrastructure 4B

```text
4B 조건:
- stablecoin 법안·규제 프레임워크 기대가 과밀
- 발행량·reserve income 증가만 보고 valuation이 먼저 감
- 금리 하락 시 issuer economics를 무시
- convertibility·reserve·run risk를 낮게 봄
```

Circle은 regulated stablecoin infrastructure 후보지만, IPO 가격 대비 3배 이상 오른 가격경로에서는 4B-watch가 필요하다. ([Reuters][3])

---

## 6-7. 정책·세금 shock 4B

```text
4B 조건:
- 이미 AI·반도체·밸류업 rally가 과열
- 정책 코멘트 하나로 index와 주도주가 크게 흔들림
- 정부 해명 전까지 risk premium이 급등
```

한국 증시는 AI 초과이익·시민배당성 발언 이후 코스피가 장중 5%까지 하락하고 종가 기준 2.3% 하락한 사례가 있었다. 이는 crowded rally에서는 정책 이벤트가 thesis를 깨지 않아도 price-path를 강하게 흔들 수 있음을 보여준다. ([Barron's][10])

---

# 7. 4C-thesis-break 사례

4C는 단순 조정이 아니다.
**논리 훼손**이다.

## 7-1. 회계·감사 4C

```text
hard 4C:
auditor_resignation
filing_delay
internal_control_weakness
financial_restatement
regulatory_probe
related_party_transaction
```

Supermicro는 이 기준을 가장 잘 보여준다. 감사인이 사임하고 경영진·감사위원회 신뢰 문제를 제기하면, AI 서버 매출 성장은 더 이상 Green을 방어하지 못한다. ([Reuters][4])

---

## 7-2. 운영 신뢰도 4C

```text
hard 4C:
global_outage
faulty_update
customer_damage
shareholder_lawsuit
customer_lawsuit
renewal_risk
```

CrowdStrike는 보안 SaaS의 핵심 반례다. 반복매출 기업도 운영 신뢰가 깨지면 RedTeam hard review로 내려가야 한다. ([위키백과][5])

---

## 7-3. 상업화 실패 4C

```text
hard 4C:
approval_but_no_uptake
slow_prescription
reimbursement_failure
cash_runway_collapse
going_concern
discounted_take_private
```

Bluebird bio는 승인된 치료제를 갖고도 uptake·현금흐름·상업화가 안 되면 주가가 무너질 수 있음을 보여준다. ([Reuters][6])

---

## 7-4. 가격·수요 붕괴 4C

```text
4C:
commodity_price_crash
freight_rate_collapse
EV_demand_slowdown
capacity_overbuild
margin_compression
price_pressure
```

Novo Nordisk처럼 구조 성장시장에서도 가격 압박과 경쟁이 수익 경로를 훼손하면 4C가 된다. ([Reuters][7])

---

## 7-5. 레버리지·FCF 붕괴 4C

```text
4C:
FCF_negative
debt_refinancing_pressure
interest_expense_spike
capex_burden
dividend_cut
going_concern
```

이건 R2 neocloud, R7 biotech, R9 eVTOL, R10 REIT, R12 스마트팜에 공통 적용한다.

---

## 7-6. 디지털자산 붕괴 4C

```text
hard 4C:
depeg
reserve_failure
convertibility_failure
liquidity_run
fraud
algorithmic_stablecoin_failure
```

TerraUSD/Luna는 이 항목의 기준 사례다. ([Financial Times][9])

---

## 7-7. AFFO·현금흐름 착시 4C

```text
4C-watch:
AFFO overstatement allegation
maintenance capex misclassification
AI pipe dream narrative
power constraint
tenant concentration
```

Equinix Hindenburg 사례는 데이터센터 REIT와 AI real asset 후보에 반드시 적용해야 하는 R13 게이트다. ([Reuters][8])

---

## 7-8. 정책 shock 4C-watch

```text
4C-watch:
market_wide_policy_shock
tax_or_redistribution_comment
government_clarification_needed
valuation_risk_premium_spike
crowded_trade_unwind
```

정책 코멘트가 실제 세금으로 확정되지 않았더라도, 주도주와 지수가 이미 4B 구간에 있으면 price-path를 깨는 강한 overlay가 된다. ([Barron's][10])

---

# 8. 점수비중 보정표 — R13 Loop 3 / v3.0

R13은 일반 섹터 점수표가 아니라 **overlay / gate / validation score**다.

| cross-archetype                    | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation |  Capital | Info | 처리                     |
| ---------------------------------- | ------: | ---------: | ---------: | ---------: | --------: | -------: | ---: | ---------------------- |
| `STRUCTURAL_SUCCESS_ALIGNED`       |       + |          + |          + |          + |         + | optional |    + | Green 유지 가능            |
| `SECTOR_SUCCESS_BUT_4B_WATCH`      |      유지 |         유지 |         유지 |         약화 |        감점 | optional |   유지 | 비중축소·졸업 감시             |
| `PRICE_ONLY_RALLY`                 |       0 |          0 |          0 |          - |         - |        0 |    - | Green 금지               |
| `EVENT_PREMIUM`                    |     0~+ |          0 |          0 |          + |         0 |        0 |   보통 | Event로 분리              |
| `EVENT_TO_CONTRACT_ESCALATION`     |       + |          + |   optional |          + |  optional |        0 |    + | Stage 2 후보             |
| `CYCLICAL_SUCCESS`                 |       + |         낮음 |          + |          0 |        낮음 |        0 |   보통 | cycle_success 분리       |
| `FALSE_POSITIVE_SCORE`             |       - |          - |          - |          - |         - |        0 |    - | 해당 archetype 재보정       |
| `EVIDENCE_GOOD_BUT_PRICE_FAILED`   |       + |          + |   optional |          0 |         - | optional |    + | valuation/프레임 재검토      |
| `REDTEAM_ACCOUNTING_TRUST_OVERLAY` |    gate |       gate |       gate |       gate |      gate |     gate | gate | hard block             |
| `OPERATIONAL_TRUST_BREAK`          |    gate |       gate |       gate |       gate |      gate |     gate | gate | hard review            |
| `LEGAL_REGULATORY_REDTEAM`         |    gate |       gate |       gate |       gate |      gate |     gate | gate | hard/soft gate         |
| `LEVERAGE_FCF_BREAKDOWN`           |       - |          - |          0 |          - |         - |        - |   보통 | Green 금지               |
| `COMMERCIALIZATION_FAILURE`        |  hard - |     hard - |          0 |     hard - |    hard - |   hard - |    + | 4C                     |
| `AFFO_CASHFLOW_INTEGRITY_RISK`     |    gate |       gate |       gate |       gate |      gate |     gate | gate | REIT hard review       |
| `STABLECOIN_CONVERTIBILITY_RISK`   |    gate |       gate |       gate |       gate |      gate |     gate | gate | hard block             |
| `POLICY_MARKET_SHOCK_EVENT`        |    gate |       gate |       gate |       gate |      gate |     gate | gate | 4B 구간 price-path shock |
| `UNKNOWN_INSUFFICIENT_EVIDENCE`    |       0 |          0 |          0 |          0 |         0 |        0 |   낮음 | Stage 3 금지             |

Loop 3에서 가장 중요한 보정은 이거다.

```text
1. 4B는 “나쁜 종목”이 아니라 “좋은 논리가 이미 반영된 상태”로 분리한다.
2. 회계·감사·공시 지연은 성장률과 무관하게 hard gate로 둔다.
3. SaaS·보안·플랫폼은 operational trust gate를 별도로 둔다.
4. 바이오는 approval보다 commercialization을 본다.
5. REIT는 AFFO와 maintenance capex를 검증한다.
6. stablecoin은 fiat-backed / algorithmic / exchange / STO를 분리한다.
7. 정책 shock은 crowded 4B 구간의 price-path를 깨는 overlay로 둔다.
8. 가격경로가 틀리면 점수체계를 재보정한다.
```

---

# 9. stage date 후보

R13 Loop 3부터 모든 case는 아래 stage date를 강제한다.

```text
stage1_date:
산업 변화, 정책, 테마, 임상, 계약 기대, 가격 이벤트가 처음 포착된 날짜

stage2_date:
실제 공시, 계약, 수주, 실적, 처방량, 가동률, 매출, EPS 상향이 확인된 날짜

stage3_date:
중장기 EPS/FCF 상향 + valuation frame 변화 + cross-evidence가 확인된 날짜

stage4b_date:
모두가 새 프레임을 인정하고 valuation이 포화되기 시작한 날짜

stage4c_date:
논리 훼손이 확인된 날짜
```

각 stage 의미는 이렇게 고정한다.

```text
Stage 1:
관찰 시작. 테마 가능성은 있으나 Green 아님.

Stage 2:
증거가 생김. 계약·실적·매출·처방·가동률 중 하나 이상 확인.

Stage 3:
구조적 후보. EPS/FCF 지속성과 valuation frame 전환이 같이 확인.

Stage 4B:
졸업·과열 감시. 좋은 논리가 시장에 널리 알려짐.

Stage 4C:
논리 훼손. Stage 강등 또는 제외.
```

R13 Loop 3에서는 특히 `stage4b_date`와 `stage4c_date`를 더 중요하게 본다.
Stage 3 후보를 찾는 것보다, **언제 Stage 3가 더 이상 싸지 않은지**, **언제 논리가 깨졌는지**를 못 잡으면 전체 시스템이 위험해진다.

---

# 10. 가격경로 검증계획

## 10-1. 필수 가격지표

모든 R1~R12 case에 아래 가격 필드를 강제한다.

```text
MFE_5D
MFE_20D
MFE_30D
MFE_60D
MFE_90D
MFE_180D
MFE_1Y
MFE_2Y

MAE_5D
MAE_20D
MAE_30D
MAE_60D
MAE_90D
MAE_180D
MAE_1Y

peak_price
peak_date
drawdown_after_peak

below_stage1_price_flag
below_stage2_price_flag
below_stage3_price_flag
```

## 10-2. 필수 최종 판정값

```text
STRUCTURAL_SUCCESS_ALIGNED:
증거 이후 주가·EPS/FCF가 같이 리레이팅.

SECTOR_SUCCESS_BUT_4B_WATCH:
성공은 맞지만 이미 시장이 대부분 인정.

CYCLICAL_SUCCESS:
가격·운임·원자재·spread로 수익은 났지만 구조적 지속성 낮음.

EVENT_PREMIUM:
공개매수·정책·재난·전염병·MOU로 오른 가격.

EVENT_TO_CONTRACT_ESCALATION:
이벤트가 실제 계약·정부주문·예산·매출로 승격.

PRICE_MOVED_WITHOUT_EVIDENCE:
주가는 올랐지만 계약·실적·EPS 증거 없음.

EVIDENCE_GOOD_BUT_PRICE_FAILED:
증거는 있었지만 시장이 리레이팅하지 않음.

FALSE_POSITIVE_SCORE:
에이전트 점수는 높았지만 가격·실적 검증 실패.

HARD_4C_THESIS_BREAK:
회계·법적·운영·부채·수요 붕괴로 논리 훼손.

POLICY_MARKET_SHOCK:
정책·세금·분배 코멘트가 crowded trade price-path를 훼손.

UNKNOWN_INSUFFICIENT_PRICE_DATA:
가격 backfill 부족으로 판정 유보.
```

## 10-3. archetype별 검증기간

```text
수주·backlog형:
180D / 1Y / 2Y 중심

AI·반도체형:
90D / 180D / 1Y / 2Y + 4B drawdown 중심

소비재·브랜드형:
90D / 180D / 1Y + 재고/채권 동행 확인

금융·value-up형:
180D / 1Y / 2Y + PBR band 변화 확인

바이오·헬스케어형:
30D 이벤트 반응 + 180D/1Y 상업화 확인

플랫폼·SaaS형:
90D / 180D / 1Y + ARR/churn/FCF 확인

REIT·부동산형:
180D / 1Y + AFFO/NOI/dividend coverage 확인

정책·이벤트형:
5D / 20D / 60D / 90D 중심

사이클형:
가격 peak 이후 drawdown 중심
```

## 10-4. R13 Loop 3에서 가격검증 실패 시 처리

```text
점수 높음 + 가격경로 맞음 + EPS/FCF 맞음:
→ STRUCTURAL_SUCCESS_ALIGNED

점수 높음 + 가격경로 좋음 + EPS/FCF 일회성:
→ CYCLICAL_SUCCESS or EVENT_PREMIUM

점수 높음 + 가격만 오름 + 증거 없음:
→ PRICE_ONLY_RALLY

점수 높음 + 증거 있음 + 주가 실패:
→ EVIDENCE_GOOD_BUT_PRICE_FAILED

점수 높음 + 이후 4C 발생:
→ FALSE_POSITIVE_SCORE + THESIS_BREAK_4C

점수 낮았는데 가격·EPS 모두 맞음:
→ scoring miss, archetype weight 재조정
```

---

# 11. 다음에 에이전트가 채워야 할 price fields

R13 Loop 3부터는 모든 case library에 아래 공통 필드를 강제한다.

```text
case_id
symbol
company_name
market
primary_sector_round
primary_archetype
secondary_archetypes
case_type

stage1_date
stage2_date
stage3_date
stage4b_date
stage4c_date

stage1_evidence_type
stage2_evidence_type
stage3_evidence_type
stage4b_evidence_type
stage4c_evidence_type

stage1_price
stage2_price
stage3_price
stage4b_price
stage4c_price
peak_price
peak_date

MFE_5D
MFE_20D
MFE_30D
MFE_60D
MFE_90D
MFE_180D
MFE_1Y
MFE_2Y

MAE_5D
MAE_20D
MAE_30D
MAE_60D
MAE_90D
MAE_180D
MAE_1Y

drawdown_after_peak
below_stage1_price_flag
below_stage2_price_flag
below_stage3_price_flag

revenue_revision_1q
revenue_revision_1y
op_revision_1q
op_revision_1y
eps_revision_1q
eps_revision_1y
fcf_margin_change
gross_margin_change
op_margin_change

valuation_metric_before
valuation_metric_after
pbr_before
pbr_after
per_before
per_after
ev_ebitda_before
ev_ebitda_after

contract_value
contract_duration_months
contract_amount_to_sales
backlog_growth
capacity_utilization
customer_concentration

debt_to_ebitda
net_debt
interest_expense
cash_runway_months
refinancing_risk_flag
dividend_cut_flag
buyback_cancelled_flag

auditor_resignation_flag
filing_delay_flag
internal_control_issue_flag
regulatory_probe_flag
related_party_risk_flag

security_outage_flag
privacy_breach_flag
customer_lawsuit_flag
operational_trust_break_flag

approval_status
commercial_revenue
patient_uptake
reimbursement_status
going_concern_flag

affo_growth
noi_growth
maintenance_capex
expansion_capex
affo_integrity_risk_flag
dividend_coverage_ratio

stablecoin_type
depeg_event_flag
reserve_failure_flag
convertibility_risk_flag
algorithmic_stablecoin_flag
stablecoin_circulation
reserve_income
redemption_at_par_flag

event_only_flag
cycle_only_flag
price_only_rally_flag
crowded_4b_flag
hard_4c_flag
policy_market_shock_flag
unknown_insufficient_evidence_flag

score_before_redteam
score_after_redteam
stage_before_redteam
stage_after_redteam
score_price_alignment
price_validation_status
review_notes
```

---

# R13 Loop 3 최종 결론

R13 Loop 3의 결론은 명확하다.

```text
R1~R12:
어디서 후보가 나오는가?

R13:
그 후보가 진짜인가?
이미 늦었는가?
테마뿐인가?
사이클뿐인가?
이벤트뿐인가?
회계·법적·운영·부채·상업화 리스크가 논리를 깨는가?
가격경로가 점수와 맞는가?
```

R13에서 확정할 최종 규칙은 이거다.

```text
Stage 3-Green은 점수만으로 절대 나오면 안 된다.

반드시:
1. cross-evidence
2. EPS/FCF 지속성
3. 가격경로 alignment
4. RedTeam hard flag 부재
5. 4B 과열 미포화

이 다섯 개를 통과해야 한다.
```

**R13 Loop 3 점수정규화의 핵심 문장:**

> Cross-archetype 검증은 “좋아 보이는 후보”를 고르는 단계가 아니라, **좋아 보이는 후보 중에서 실제 EPS/FCF와 가격경로가 맞은 것만 남기고, 테마·사이클·이벤트·회계·부채·운영 신뢰·상업화 실패·정책 shock 리스크를 제거하는 단계**다.

이제 **R1~R13 Loop 3가 완료**됐다.
다음에 같은 지시가 오면 규칙대로 **R1 — 산업재·수주·인프라 Loop 4**로 돌아가서, 지금까지 쌓은 RedTeam과 가격검증 기준을 반영해 다시 더 촘촘하게 판다.

[1]: https://www.reuters.com/world/asia-pacific/ai-boom-puts-sk-hynix-cusp-1-trillion-market-value-2026-05-14/?utm_source=chatgpt.com "AI boom puts SK Hynix on cusp of $1 trillion market value"
[2]: https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-parliament-approves-commercial-act-revision-aimed-boosting-share-2026-02-25/?utm_source=chatgpt.com "South Korea parliament approves commercial act revision aimed at boosting share valuations"
[3]: https://www.reuters.com/technology/circles-quarterly-earnings-benefit-stablecoin-safety-during-volatile-period-2026-05-11/?utm_source=chatgpt.com "Circle revenue boosted as stablecoin demand rises amid volatility; shares up"
[4]: https://www.reuters.com/technology/super-micro-computer-says-ernst-young-resigns-its-accountant-shares-tank-2024-10-30/?utm_source=chatgpt.com "Super Micro Computer says Ernst & Young resigns as auditor, shares tank"
[5]: https://en.wikipedia.org/wiki/2024_CrowdStrike-related_IT_outages?utm_source=chatgpt.com "2024 CrowdStrike-related IT outages"
[6]: https://www.reuters.com/markets/deals/bluebird-bio-be-taken-private-by-carlyle-sk-capital-amid-cash-crunch-2025-02-21/?utm_source=chatgpt.com "Gene therapy maker bluebird to go private in discounted deal amid cash crunch"
[7]: https://www.reuters.com/business/novo-nordisk-warns-2026-sales-decline-2026-02-03/?utm_source=chatgpt.com "Novo Nordisk warns on profits and sales amid Trump drug price crackdown"
[8]: https://www.reuters.com/business/media-telecom/hindenburg-research-takes-short-position-data-center-operator-equinix-2024-03-20/?utm_source=chatgpt.com "Hindenburg shorts data center firm Equinix alleging inflated profit metric"
[9]: https://www.ft.com/content/1bacfc09-6a29-4be9-8da8-ed0960e0c774?utm_source=chatgpt.com "Crypto entrepreneur Do Kwon sentenced to 15 years in prison"
[10]: https://www.barrons.com/articles/ai-tax-stock-market-kospi-2e468921?utm_source=chatgpt.com "Why the World's Hottest Stock Market Got Derailed by Talk of an AI Tax"
